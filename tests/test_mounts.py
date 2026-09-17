"""Mounted characters: split profiles, improved characteristics, armour and strike order."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from support import FULL, SAMPLES_LARGE, StatisticalCase, all_profiles, build, fighter

import dice
from combat_simulations import combat_simulation, determine_strike_order
from faction_profiles import FactionProfiles
from mounted import INTEGRAL_MOUNTS, integral_mount
from mounts import HONOUR_MOUNTS, Mounts
from special_rules import parse_armour_bonus, parse_ward


def duel(a, b, rounds=3, verbose=False):
    out = io.StringIO()
    with redirect_stdout(out):
        winner = combat_simulation(a, b, rounds=rounds, verbose=verbose)
    return winner, out.getvalue()


class TestMountedProfiles(unittest.TestCase):
    def test_cavalry_keeps_the_riders_toughness_and_armour(self):
        prince = build("High Elves", "Prince", mount="Elven Steed")
        on_foot = build("High Elves", "Prince")
        self.assertEqual((prince.Toughness, prince.Wounds), (on_foot.Toughness, on_foot.Wounds))
        self.assertEqual(prince.Armor, on_foot.Armor)
        self.assertEqual(prince.TroopType, "LightCavalry")

    def test_barding_improves_armour_by_one(self):
        prince = build("High Elves", "Prince", mount="Barded Elven Steed")
        self.assertEqual(parse_armour_bonus(prince.SpecialRules), 1)

    def test_a_ridden_monster_raises_toughness_and_wounds(self):
        prince = build("High Elves", "Prince", mount="Star Dragon")
        # Star Dragon: T (+3), W (+6), counts as full plate armour.
        self.assertEqual((prince.Toughness, prince.Wounds), (6, 9))
        self.assertEqual(prince.Armor, "Full Plate Armor")
        self.assertEqual(prince.TroopType, "Behemoth")

    def test_the_better_armour_value_is_used(self):
        # A Griffon counts as heavy armour; a Prince in full plate keeps his.
        plated = build("High Elves", "Prince", Armor="Plate Armor", mount="Griffon (High Elves)")
        self.assertEqual(plated.Armor, "Plate Armor")
        light = build("High Elves", "Prince", mount="Griffon (High Elves)")
        self.assertEqual(light.Armor, "Heavy Armor")

    def test_a_chariot_adds_its_wounds_and_uses_the_higher_toughness(self):
        warboss = build("Orcs", "Orc Warboss", mount="Orc Boar Chariot")
        on_foot = build("Orcs", "Orc Warboss")
        self.assertEqual(warboss.Wounds, on_foot.Wounds + 4)
        self.assertEqual(warboss.Toughness, max(on_foot.Toughness, 5))
        self.assertEqual(warboss.Armor, "Full Plate Armor")  # the chariot's printed 4+

    def test_chariot_crew_and_beasts_attack(self):
        prince = build("High Elves", "Prince", mount="Tiranoc Chariot")
        names = sorted(p.name for p in prince.mount_parts)
        self.assertEqual(len(names), 2)
        self.assertTrue(all(p.Attacks == 2 for p in prince.mount_parts))  # (x2) rows

    def test_rider_only_rules_stay_with_the_rider(self):
        prince = build("High Elves", "Prince", mount="Elven Steed")
        (steed,) = prince.mount_parts
        self.assertIn("Strike First", prince.SpecialRules)
        self.assertNotIn("Strike First", steed.SpecialRules)
        self.assertNotIn("Ithilmar Weapons", steed.SpecialRules)

    def test_other_rules_are_shared(self):
        warboss = build("Orcs", "Orc Warboss", SpecialRules=["Frenzy"], mount="War Boar")
        (boar,) = warboss.mount_parts
        self.assertIn("Frenzy", boar.SpecialRules)
        self.assertIn("Armoured Hide (1)", warboss.SpecialRules)  # the boar's hide

    def test_items_stay_with_the_rider(self):
        general = build("Empire of Man", "General of the Empire",
                        magic_items=["Talisman of Protection"], mount="Empire Warhorse")
        (horse,) = general.mount_parts
        self.assertNotIn("Ward5", horse.SpecialRules)

    def test_mount_damage_and_healing_go_to_the_rider(self):
        prince = build("High Elves", "Prince", mount="Elven Steed")
        (steed,) = prince.mount_parts
        steed.current_wounds = 1
        self.assertEqual(prince.current_wounds, 1)


class TestMountRules(unittest.TestCase):
    def test_only_offered_mounts(self):
        with self.assertRaisesRegex(ValueError, "cannot ride"):
            build("High Elves", "Prince", mount="War Boar")

    def test_unknown_mount(self):
        with self.assertRaisesRegex(ValueError, "Unknown mount"):
            build("High Elves", "Prince", mount="Hippo")

    def test_honour_mounts_need_their_honour(self):
        for mount, honour in HONOUR_MOUNTS.items():
            with self.subTest(mount=mount):
                with self.assertRaisesRegex(ValueError, honour):
                    build("High Elves", "Prince", mount=mount)
                build("High Elves", "Prince", mount=mount, magic_items=[honour])

    def test_an_honour_limits_the_mounts(self):
        with self.assertRaisesRegex(ValueError, "may only ride"):
            build("High Elves", "Prince", mount="Elven Steed", magic_items=["Chracian Hunter"])
        with self.assertRaisesRegex(ValueError, "no mount"):
            build("High Elves", "Prince", mount="Elven Steed", magic_items=["Warden of Saphery"])

    def test_the_legacy_honour_option_counts(self):
        build("High Elves", "Prince", mount="Sun Dragon", elven_honors=["BloodofCaledor"])

    def test_integral_mounts_are_always_ridden_without_double_counting(self):
        for (faction, profile), mount in INTEGRAL_MOUNTS.items():
            with self.subTest(profile=profile):
                model = build(faction, profile)
                base = FactionProfiles[faction][profile]["base_profile"]
                self.assertEqual(model.mount, mount)
                self.assertEqual((model.Toughness, model.Wounds), (base["Toughness"], base["Wounds"]))
                self.assertTrue(model.mount_parts)

    def test_an_integral_mount_cannot_be_swapped(self):
        with self.assertRaisesRegex(ValueError, "always rides"):
            build("High Elves", "Dragon Mage", mount="Star Dragon")

    def test_a_mount_only_rule_arms_the_mount_not_the_rider(self):
        kiknik = build("Orcs", "Kiknik Toofsnatcha")
        (chompa,) = kiknik.mount_parts
        self.assertIn("Armour Bane (1)", chompa.SpecialRules)
        self.assertNotIn("Armour Bane (1)", kiknik.SpecialRules)

    def test_scoped_impact_hits_still_belong_to_the_model(self):
        from special_rules import parse_impact_hits

        korhil = build("High Elves", "Korhil Lionmane", mount="Chieftain's Chariot")
        self.assertEqual(parse_impact_hits(korhil.SpecialRules), ["D6"])
        self.assertEqual(korhil.mount_strength, 5)

    def test_born_of_fire_wards_the_model(self):
        riders = [(f, p) for f, p in all_profiles("characters")
                  if "Great Taurus" in FactionProfiles[f][p]["mount_options"]["mounts"]]
        self.assertTrue(riders)
        faction, profile = riders[0]
        rider = build(faction, profile, mount="Great Taurus")
        self.assertEqual(parse_ward(rider.SpecialRules, is_flaming=True), 3)


class TestMountedCombat(StatisticalCase):
    def test_a_mount_strikes_at_its_own_initiative(self):
        prince = build("High Elves", "Prince", name="Prince", mount="Star Dragon")  # dragon I2
        foe = fighter("Foe", Initiative=4)
        steps = determine_strike_order(prince, foe, verbose=False, is_first_round=False)
        order = [[a.name for a, _d in step] for step in steps]
        self.assertEqual(order, [["Prince"], ["Foe"], ["Prince's Star Dragon"]])

    def test_the_mount_attacks_the_other_fighter(self):
        prince = build("High Elves", "Prince", name="Prince", mount="Star Dragon")
        foe = fighter("Foe")
        steps = determine_strike_order(prince, foe, verbose=False)
        for step in steps:
            for attacker, defender in step:
                self.assertIs(defender, foe if attacker is not foe else prince)

    def test_stomps_use_the_mounts_strength(self):
        prince = build("High Elves", "Prince", name="Prince", mount="Star Dragon")
        with dice.constant_dice(6):
            _, text = duel(prince, fighter("Wall", Toughness=10, Wounds=50, Attacks=0),
                           rounds=1, verbose=True)
        self.assertIn("Stomp Attacks (S7", text)

    def test_a_mounted_character_beats_itself_on_foot(self):
        runs = SAMPLES_LARGE // 2
        dice.seed(4)
        wins = 0
        for _ in range(runs):
            rider = build("High Elves", "Prince", name="Rider", mount="Griffon (High Elves)")
            walker = build("High Elves", "Prince", name="Walker")
            winner, _ = duel(rider, walker)
            wins += winner is rider
        self.assertGreater(wins / runs, 0.7)

    def test_mounted_mirror_matches_are_symmetric(self):
        import math

        runs = SAMPLES_LARGE
        dice.seed(8)
        left = right = 0
        for _ in range(runs):
            a = build("Orcs", "Orc Warboss", name="Left", mount="Orc Boar Chariot")
            b = build("Orcs", "Orc Warboss", name="Right", mount="Orc Boar Chariot")
            winner, _ = duel(a, b)
            left += winner is a
            right += winner is b
        band = 4 * math.sqrt(max(left + right, 1)) / runs
        self.assertAlmostEqual(left / runs, right / runs, delta=band)


class TestEveryMount(unittest.TestCase):
    def test_every_character_rides_every_mount_it_may_take(self):
        dice.seed(12)
        tried = 0
        for faction, profile in all_profiles("characters"):
            if integral_mount(faction, profile):
                continue
            mounts = FactionProfiles[faction][profile].get("mount_options", {}).get("mounts", [])
            for mount in mounts if FULL else mounts[:3]:
                if mount not in Mounts:
                    continue
                honour = HONOUR_MOUNTS.get(mount)
                items = [honour] if honour else []
                with self.subTest(profile=profile, mount=mount):
                    try:
                        rider = build(faction, profile, name="Rider", mount=mount, magic_items=items)
                    except ValueError as exc:
                        self.assertRegex(str(exc), "Elven Honour|cannot take")  # honour not offered
                        continue
                    tried += 1
                    self.assertGreaterEqual(rider.Wounds, 1)
                    foe = build(faction, profile, name="Foe")
                    winner, _ = duel(rider, foe)
                    self.assertIn(winner, (rider, foe, None))
                    self.assertGreaterEqual(rider.current_wounds, 0)
                    self.assertLessEqual(rider.current_wounds, rider.Wounds)
        self.assertGreater(tried, 150)


if __name__ == "__main__":
    unittest.main()
