"""Marks of Chaos, Chivalrous Vows, the Blessings of the Lady and bought abilities.

Honours, Kindreds, Knightly Virtues, Gifts, Vampiric Powers and runes are all
magic-item entries (type "Ability" or a rune category) bought through
Character(magic_items=...). Marks and Vows are exclusive options passed as
special rules, replacing the profile's default.
"""

from __future__ import annotations

import unittest

from support import SAMPLES_LARGE, StatisticalCase, build, fighter

import dice
from combat_simulations import (
    RollToHit,
    StrikeResult,
    Wound,
    apply_extra_attacks,
    apply_weapon_stats,
    determine_strike_order,
    effective_initiative,
    reset_weapon_stats,
    resolve_strike,
    RollToWound,
)
from special_rules import parse_ward

N = SAMPLES_LARGE * 5


def hit_rate(attacker, defender, trials=N, seed=0):
    dice.seed(seed)
    return sum(RollToHit(attacker, defender, verbose=False) for _ in range(trials)) / (
        trials * attacker.Attacks)


def damage_rate(defender, result, trials=N, seed=0):
    dice.seed(seed)
    total = 0
    for _ in range(trials):
        defender.current_wounds = 100
        total += resolve_strike(defender, result, verbose=False)[0]
    return total / trials


class TestMarksOfChaos(StatisticalCase):
    def lord(self, *rules):
        return build("Warriors of Chaos", "Chaos Lord", SpecialRules=list(rules))

    def test_a_mark_replaces_undivided(self):
        marks = [r for r in self.lord("Mark of Khorne").SpecialRules if r.startswith("Mark of")]
        self.assertEqual(marks, ["Mark of Khorne"])

    def test_the_default_mark_stays_without_a_choice(self):
        self.assertIn("Mark of Chaos Undivided", self.lord().SpecialRules)

    def test_only_one_mark(self):
        with self.assertRaisesRegex(ValueError, "only have one"):
            self.lord("Mark of Khorne", "Mark of Nurgle")

    def test_only_marks_the_profile_offers(self):
        with self.assertRaisesRegex(ValueError, "cannot take"):
            build("Warriors of Chaos", "Exalted Sorcerer", SpecialRules=["Mark of Khorne"])

    def test_khorne_is_frenzied(self):
        self.assertEqual(apply_extra_attacks(self.lord("Mark of Khorne")),
                         apply_extra_attacks(self.lord()) + 1)

    def test_khorne_and_frenzy_do_not_stack(self):
        both = fighter(Attacks=2, SpecialRules=["Mark of Khorne", "Frenzy"])
        self.assertEqual(apply_extra_attacks(both), 3)

    def test_nurgle_makes_enemies_reroll_sixes_to_hit(self):
        # WS4 v WS4 hits on 4+: 4 and 5 hit (1/3), a 6 is rerolled (1/6 * 1/2).
        target = fighter(SpecialRules=["Mark of Nurgle"])
        self.assertProportion(hit_rate(fighter(Attacks=1), target), 1 / 3 + 1 / 12, N)

    def test_slaanesh_strikes_faster_in_the_first_round_only(self):
        blessed = fighter(Initiative=4, SpecialRules=["Mark of Slaanesh"])
        self.assertEqual(effective_initiative(blessed, is_first_round=True), 5)
        self.assertEqual(effective_initiative(blessed, is_first_round=False), 4)
        order = determine_strike_order(blessed, fighter(Initiative=4), False, is_first_round=True)
        self.assertEqual(order[0][0][0], blessed)

    def test_tzeentch_attacks_are_flaming(self):
        _, flaming, _ = RollToWound(fighter(SpecialRules=["Mark of Tzeentch"]), fighter(), 0,
                                    verbose=False)
        self.assertTrue(flaming)


class TestBretonnia(StatisticalCase):
    def test_a_vow_replaces_the_knights_vow(self):
        baron = build("Kingdom of Bretonnia", "Baron", SpecialRules=["The Grail Vow"])
        vows = [r for r in baron.SpecialRules if "Vow" in r]
        self.assertEqual(vows, ["The Grail Vow"])

    def test_the_grail_vow_makes_attacks_magical(self):
        _, _, magical = RollToWound(fighter(SpecialRules=["The Grail Vow"]), fighter(), 0,
                                    verbose=False)
        self.assertTrue(magical)

    def test_the_blessing_is_a_six_up_ward_or_five_up_against_strength_five(self):
        rules = ["Blessings of the Lady"]
        self.assertEqual(parse_ward(rules), 6)
        self.assertEqual(parse_ward(rules, strength=4), 6)
        self.assertEqual(parse_ward(rules, strength=5), 5)
        self.assertEqual(parse_ward(["The Grail Vow"], strength=7), 5)

    def test_the_blessing_uses_the_attacks_strength_in_a_strike(self):
        knight = fighter(Wounds=100, SpecialRules=["Blessings of the Lady"])
        weak = StrikeResult(unsaved=[Wound(roll=4)], strength=3)
        strong = StrikeResult(unsaved=[Wound(roll=4)], strength=6)
        self.assertProportion(damage_rate(knight, weak), 5 / 6, N)
        self.assertProportion(damage_rate(knight, strong), 2 / 3, N)

    def test_every_blessed_bretonnian_character_has_the_ward(self):
        for profile in ("Duke", "Baron", "Paladin", "Damsel", "Prophetess"):
            with self.subTest(profile=profile):
                self.assertEqual(parse_ward(build("Kingdom of Bretonnia", profile).SpecialRules), 6)


class TestGrantedEquipment(unittest.TestCase):
    """Abilities that unlock weapons or armour make them selectable."""

    GRANTS = [
        ("High Elves", "Noble", "Warden of Saphery", "Sword of Hoeth"),
        ("High Elves", "Prince", "Loremaster", "Sword of Hoeth"),
        ("High Elves", "Noble", "Anointed of Asuryan", "Ceremonial Halberd"),
        ("High Elves", "Noble", "Chracian Hunter", "Chracian Great Blade"),
        ("Empire of Man", "Grand Master", "Order of the White Wolf", "Wolf Hammer"),
        ("Empire of Man", "Captain of the Empire", "Order of the Knights Panther", "Lance"),
        ("Realms of Men", "Renegade Captain", "The Wandering Diestro", "Two Hand Weapons"),
    ]

    def test_each_granted_weapon_needs_its_ability(self):
        from app_model import weapon_choices

        for faction, profile, ability, weapon in self.GRANTS:
            with self.subTest(ability=ability):
                offered = weapon_choices(faction, profile)
                if weapon not in offered:
                    with self.assertRaisesRegex(ValueError, "Invalid weapon"):
                        build(faction, profile, Weapon=weapon)
                self.assertIn(weapon, weapon_choices(faction, profile, [ability]))
                model = build(faction, profile, Weapon=weapon, magic_items=[ability])
                self.assertEqual(model.Weapon, weapon)

    def test_blood_of_caledor_allows_full_plate(self):
        noble = build("High Elves", "Noble", Armor="Full Plate Armor", magic_items=["Blood of Caledor"])
        self.assertEqual(noble.Armor, "Full Plate Armor")

    def test_bows_are_recorded_but_not_offered(self):
        from app_model import weapon_choices
        from magic_items import get_magic_item

        self.assertEqual(get_magic_item("Sea Guard")["grants"], {"ranged": ["warbow"]})
        self.assertEqual(weapon_choices("High Elves", "Noble", ["Sea Guard"]),
                         weapon_choices("High Elves", "Noble"))

    def test_every_granted_weapon_has_a_profile(self):
        from magic_items import MagicItemDict
        from weapons import find_weapon_key

        for name, entry in MagicItemDict.items():
            for weapon in entry.get("grants", {}).get("weapons", []):
                with self.subTest(item=name, weapon=weapon):
                    self.assertIsNotNone(find_weapon_key(weapon))


class TestStrengthLimitedWards(unittest.TestCase):
    def test_pendant_of_khaeleth(self):
        rules = fighter(magic_items=["Pendant of Khaeleth"]).SpecialRules
        self.assertEqual(parse_ward(rules, strength=3), 5)
        self.assertEqual(parse_ward(rules, strength=5), 4)
        self.assertIsNone(parse_ward(rules))  # an attack of unknown Strength


class TestBoughtAbilities(StatisticalCase):
    def test_an_elven_honour_bought_as_an_ability_matches_the_legacy_option(self):
        bought = build("High Elves", "Prince", magic_items=["Blood of Caledor"])
        legacy = build("High Elves", "Prince", elven_honors=["BloodofCaledor"])
        self.assertEqual(bought.WeaponSkill, legacy.WeaponSkill)
        self.assertEqual(parse_ward(bought.SpecialRules), parse_ward(legacy.SpecialRules))

    def test_a_knightly_virtue(self):
        ideal = build("Kingdom of Bretonnia", "Duke", magic_items=["Virtue of the Ideal"])
        base = build("Kingdom of Bretonnia", "Duke")
        for stat in ("WeaponSkill", "Initiative", "Attacks", "Leadership"):
            with self.subTest(stat=stat):
                self.assertEqual(getattr(ideal, stat), getattr(base, stat) + 1)

    def test_heroism_needs_a_mundane_weapon(self):
        plain = build("Kingdom of Bretonnia", "Duke", magic_items=["Virtue of Heroism"])
        self.assertIn("Killing Blow", plain.SpecialRules)
        magic = build("Kingdom of Bretonnia", "Duke",
                      magic_items=["Virtue of Heroism", "Sword of Might"])
        self.assertNotIn("Killing Blow", magic.SpecialRules)

    def test_unnatural_fortitude_needs_light_armour(self):
        light = fighter(Armor="Light Armor", magic_items=["Unnatural Fortitude"])
        heavy = fighter(Armor="Heavy Armor", magic_items=["Unnatural Fortitude"])
        self.assertEqual((light.Toughness, heavy.Toughness), (5, 4))

    def test_enhanced_reflexes_needs_a_hand_weapon(self):
        self.assertEqual(fighter(magic_items=["Enhanced Reflexes"]).Initiative, 6)
        self.assertEqual(fighter(Weapon="Great Weapon", magic_items=["Enhanced Reflexes"]).Initiative, 4)

    def test_gouge_tusks_improve_armour_piercing(self):
        beast = fighter(magic_items=["Gouge-tusks"])
        apply_weapon_stats(beast, verbose=False)
        try:
            self.assertEqual(beast.ArmourPiercing, 1)
        finally:
            reset_weapon_stats(beast)
        self.assertEqual(beast.ArmourPiercing, 0)

    def test_audacity_rerolls_misses_only_against_better_fighters(self):
        audacious = fighter(Attacks=1, SpecialRules=["Reroll Failed Hits (against higher Weapon Skill)"])
        # WS4 v WS5 hits on 4+ (1/2), reroll misses: 3/4. WS4 v WS3: 3+, no reroll.
        self.assertProportion(hit_rate(audacious, fighter(WeaponSkill=5)), 3 / 4, N)
        self.assertProportion(hit_rate(audacious, fighter(WeaponSkill=3)), 2 / 3, N)

    def test_beguile_makes_a_failed_leadership_test_hit_on_sixes_only(self):
        # Ld7 passes on 2D6 21/36; then WS4 v WS4 hits on 4+.
        vampire = fighter(SpecialRules=["Enemy Must Pass Leadership To Hit"])
        expected = 21 / 36 * 1 / 2 + 15 / 36 * 1 / 6
        self.assertProportion(hit_rate(fighter(Attacks=1, Leadership=7), vampire), expected, N)

    def test_the_fiery_heart_strikes_faster_in_the_first_round(self):
        knight = fighter(SpecialRules=["+1 Initiative in the First Round"])
        self.assertEqual(effective_initiative(knight, is_first_round=True), 5)

    def test_rune_tattoos_stack_two(self):
        slayer = build("Dwarfen Mountain Holds", "Daemon Slayer",
                       magic_items=["Rune of Wrath", "Warrior's Rune"])
        base = build("Dwarfen Mountain Holds", "Daemon Slayer")
        self.assertEqual(slayer.Attacks, base.Attacks + 1)
        self.assertEqual(slayer.WeaponSkill, min(10, base.WeaponSkill + 1))

    def test_daemonic_gifts_come_from_their_own_budget(self):
        herald = build("Daemons of Chaos", "Daemonic Herald of Khorne", magic_items=["Might of Khorne"])
        self.assertEqual(herald.Strength, build("Daemons of Chaos", "Daemonic Herald of Khorne").Strength + 1)
        with self.assertRaises(ValueError):
            build("Daemons of Chaos", "Daemonic Herald of Khorne", magic_items=["Sword of Might"])

    def test_a_daemonic_weapon_gift_is_wielded(self):
        prince = build("Daemons of Chaos", "Daemon Prince", magic_items=["Axe of Khorne"])
        self.assertEqual(prince.Weapon, "Axe of Khorne")


if __name__ == "__main__":
    unittest.main()
