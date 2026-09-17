"""Tests for the combat engine.

Dice are either seeded (for whole-duel smoke tests) or scripted (for pinning
one specific rule), so every assertion here is deterministic.
"""

from __future__ import annotations

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dice
from character_model import Character
from combat_simulations import (
    OneRoundMeleeCombat,
    effective_initiative,
    RollArmorSave,
    RollToHit,
    RollToWound,
    Wound,
    apply_extra_attacks,
    combat_simulation,
    determine_strike_order,
    resolve_strike,
)


def fighter(name="Fighter", **overrides):
    """A plain custom character; override any characteristic by keyword."""
    stats = dict(
        Movement=4,
        WeaponSkill=4,
        BallisticSkill=3,
        Strength=4,
        Toughness=4,
        Initiative=4,
        Wounds=3,
        Attacks=2,
        Leadership=7,
        Race="Human",
        Weapon="Hand Weapon",
    )
    stats.update(overrides)
    return Character(name=name, **stats)



def faction_characters(faction):
    """The character roster of one faction - UNITS are pinned separately."""
    from factions import FACTION_MODULES

    return next(m.CHARACTERS for m in FACTION_MODULES if m.FACTION == faction)


class TestDuelRunsToCompletion(unittest.TestCase):
    """The structural fix: a duel resolves without crashing or double-striking."""

    def test_seeded_duel_completes(self):
        dice.seed(20260904)
        elf = Character(
            name="Altir",
            faction_type="High Elves",
            profile_name="Noble",
            Armor="Heavy Armor",
            Weapon="Great Weapon",
        )
        orc = Character(
            name="Grimgor",
            faction_type="Orcs",
            profile_name="Black Orc Bigboss",
            Weapon="Great Weapon",
        )
        winner = combat_simulation(elf, orc, rounds=4, verbose=False)
        self.assertIn(winner, (elf, orc, None))

    def test_profile_wounds_are_never_mutated(self):
        """`Wounds` is the profile maximum; only `current_wounds` takes damage."""
        dice.seed(7)
        a, b = fighter("A"), fighter("B")
        combat_simulation(a, b, rounds=6, verbose=False)
        self.assertEqual(a.Wounds, 3)
        self.assertEqual(b.Wounds, 3)
        self.assertTrue(a.current_wounds < 3 or b.current_wounds < 3)

    def test_each_fighter_strikes_once_per_round(self):
        """The old engine ran a third, unintended strike each round."""
        calls = []
        import combat_simulations as cs

        original = cs.OneRoundMeleeCombat

        def counting(attacker, defender, **kwargs):
            calls.append(attacker.name)
            return original(attacker, defender, **kwargs)

        cs.OneRoundMeleeCombat = counting
        try:
            dice.seed(3)
            # Toughness 10 vs Strength 1: nobody can wound, so all rounds run.
            a = fighter("A", Strength=1, Toughness=10)
            b = fighter("B", Strength=1, Toughness=10)
            combat_simulation(a, b, rounds=3, verbose=False)
        finally:
            cs.OneRoundMeleeCombat = original

        self.assertEqual(calls.count("A"), 3)
        self.assertEqual(calls.count("B"), 3)

    def test_simultaneous_combat_applies_wounds(self):
        """Equal Initiative used to crash subtracting a dict from an int."""
        dice.seed(11)
        a = fighter("A", Initiative=4, WeaponSkill=10, Strength=10, Attacks=5)
        b = fighter("B", Initiative=4, WeaponSkill=1, Toughness=1, Attacks=5)
        winner = combat_simulation(a, b, rounds=2, verbose=False)
        self.assertIsNotNone(winner)

    def test_a_slain_fighter_does_not_strike_back(self):
        killer = fighter("Killer", Initiative=10, Strength=10, WeaponSkill=10, Attacks=6)
        victim = fighter("Victim", Initiative=1, Toughness=1, WeaponSkill=1, Wounds=1)

        import combat_simulations as cs

        original = cs.OneRoundMeleeCombat
        strikers = []

        def counting(attacker, defender, **kwargs):
            strikers.append(attacker.name)
            return original(attacker, defender, **kwargs)

        cs.OneRoundMeleeCombat = counting
        try:
            with dice.constant_dice(6):
                combat_simulation(killer, victim, rounds=2, verbose=False)
        finally:
            cs.OneRoundMeleeCombat = original

        self.assertEqual(strikers, ["Killer"])


class TestStrikeOrder(unittest.TestCase):
    def test_strike_first_beats_higher_initiative(self):
        slow = fighter("Slow", Initiative=1, SpecialRules=["Strike First"])
        fast = fighter("Fast", Initiative=9)
        steps = determine_strike_order(slow, fast, verbose=False)
        self.assertEqual(len(steps), 2)
        self.assertEqual(steps[0][0][0].name, "Slow")

    def test_initiative_breaks_ties_within_strike_first(self):
        a = fighter("A", Initiative=6, SpecialRules=["Strike First"])
        b = fighter("B", Initiative=3, SpecialRules=["Strike First"])
        steps = determine_strike_order(a, b, verbose=False)
        self.assertEqual(steps[0][0][0].name, "A")

    def test_equal_footing_is_simultaneous(self):
        a, b = fighter("A", Initiative=5), fighter("B", Initiative=5)
        steps = determine_strike_order(a, b, verbose=False)
        self.assertEqual(len(steps), 1)
        self.assertEqual(len(steps[0]), 2)

    def test_strike_last_goes_after_normal(self):
        slow = fighter("Slow", Initiative=9, SpecialRules=["Strike Last"])
        normal = fighter("Normal", Initiative=1)
        steps = determine_strike_order(slow, normal, verbose=False)
        self.assertEqual(steps[0][0][0].name, "Normal")

    def test_weapon_strike_last_applies(self):
        """A Great Weapon carries Strike Last even though the fighter does not."""
        gw = fighter("GreatWeapon", Initiative=9, Weapon="Great Weapon")
        normal = fighter("Normal", Initiative=1)
        steps = determine_strike_order(gw, normal, verbose=False)
        self.assertEqual(steps[0][0][0].name, "Normal")

    def test_character_strike_first_cancels_weapon_strike_last(self):
        elf = fighter(
            "Elf", Initiative=5, Weapon="Great Weapon", SpecialRules=["Strike First"]
        )
        normal = fighter("Normal", Initiative=5)
        steps = determine_strike_order(elf, normal, verbose=False)
        self.assertEqual(len(steps), 1)  # both end up in the normal band

    def test_strike_first_and_last_cancel(self):
        both = fighter("Both", Initiative=5, SpecialRules=["Strike First", "Strike Last"])
        normal = fighter("Normal", Initiative=5)
        steps = determine_strike_order(both, normal, verbose=False)
        self.assertEqual(len(steps), 1)


class TestAttackCount(unittest.TestCase):
    def test_two_hand_weapons_grant_an_extra_attack(self):
        self.assertEqual(apply_extra_attacks(fighter(Weapon="Two Hand Weapons")), 3)

    def test_frenzy_grants_an_extra_attack(self):
        self.assertEqual(apply_extra_attacks(fighter(SpecialRules=["Frenzy"])), 3)

    def test_bonuses_stack(self):
        c = fighter(Weapon="Two Hand Weapons", SpecialRules=["Frenzy"])
        self.assertEqual(apply_extra_attacks(c), 4)

    def test_roll_to_hit_uses_the_bonus_attacks(self):
        attacker = fighter("A", Weapon="Two Hand Weapons", SpecialRules=["Frenzy"])
        with dice.scripted_dice([6, 6, 6, 6]):  # exactly 4 attacks expected
            hits = RollToHit(attacker, fighter("B"), verbose=False)
        self.assertEqual(hits, 4)


class TestArmourBane(unittest.TestCase):
    """A Halberd has AB1: a wound roll of 6 costs the defender one more on the save."""

    def _unsaved_with_wound_roll(self, wound_roll, save_roll):
        attacker = fighter("A", Weapon="Halberd")
        attacker.ArmourPiercing = 0
        defender = fighter("D", Armor="Heavy Armor")  # 5+ save
        with dice.scripted_dice([save_roll]):
            return RollArmorSave(
                attacker, defender, [Wound(roll=wound_roll)], verbose=False
            )

    def test_armour_bane_worsens_the_save_on_a_six(self):
        # 5+ save, AB1 makes it 6+. A roll of 5 saves normally but not vs AB.
        self.assertEqual(len(self._unsaved_with_wound_roll(4, 5)), 0)
        self.assertEqual(len(self._unsaved_with_wound_roll(6, 5)), 1)


class TestKillingBlow(unittest.TestCase):
    def test_weapon_granted_killing_blow_triggers(self):
        """Chayal grants Killing Blow; it must be read off the weapon."""
        attacker = fighter("A", Weapon="Chayal", Strength=4)
        defender = fighter("D", Toughness=4)  # wounds on 4+
        with dice.scripted_dice([6]):
            wounds, _, _ = RollToWound(attacker, defender, 1, verbose=False)
        self.assertEqual(len(wounds), 1)
        self.assertTrue(wounds[0].killing_blow)

    def test_character_granted_killing_blow_triggers(self):
        attacker = fighter("A", SpecialRules=["Killing Blow"])
        with dice.scripted_dice([6]):
            wounds, _, _ = RollToWound(attacker, fighter("D"), 1, verbose=False)
        self.assertTrue(wounds[0].killing_blow)

    def test_a_non_six_wound_is_not_a_killing_blow(self):
        attacker = fighter("A", SpecialRules=["Killing Blow"])
        with dice.scripted_dice([5]):
            wounds, _, _ = RollToWound(attacker, fighter("D"), 1, verbose=False)
        self.assertFalse(wounds[0].killing_blow)

    def test_killing_blow_slays_outright(self):
        from combat_simulations import StrikeResult

        defender = fighter("D", Wounds=4)
        taken, slain = resolve_strike(
            defender,
            StrikeResult(unsaved=[Wound(6, killing_blow=True)]),
            verbose=False,
        )
        self.assertTrue(slain)
        self.assertEqual(defender.current_wounds, 0)

    def test_a_ward_save_stops_a_killing_blow(self):
        from combat_simulations import StrikeResult

        defender = fighter("D", Wounds=4, SpecialRules=["Ward4"])
        with dice.scripted_dice([6]):  # ward save passes
            taken, slain = resolve_strike(
                defender, StrikeResult(unsaved=[Wound(6, killing_blow=True)]), verbose=False
            )
        self.assertFalse(slain)
        self.assertEqual(defender.current_wounds, 4)


class TestSaves(unittest.TestCase):
    def test_shield_false_grants_no_bonus(self):
        """`Shield=False` used to pass an `is not None` test and give +1."""
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        defender = fighter("D", Armor="Heavy Armor", Shield=False)  # 5+, not 4+
        with dice.scripted_dice([4]):
            unsaved = RollArmorSave(attacker, defender, [Wound(3)], verbose=False)
        self.assertEqual(len(unsaved), 1)

    def test_shield_true_grants_the_bonus(self):
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        defender = fighter("D", Armor="Heavy Armor", Shield=True)  # 4+
        with dice.scripted_dice([4]):
            unsaved = RollArmorSave(attacker, defender, [Wound(3)], verbose=False)
        self.assertEqual(len(unsaved), 0)

    def test_an_unarmoured_model_saves_on_a_six_with_a_shield(self):
        """Unarmoured is armour value 7+, which a shield improves to 6+."""
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        defender = fighter("D", Armor=None, Shield=True)
        with dice.scripted_dice([6, 5]):
            unsaved = RollArmorSave(attacker, defender, [Wound(3), Wound(3)], verbose=False)
        self.assertEqual(len(unsaved), 1)

    def test_armoured_hide_gives_an_unarmoured_model_a_save(self):
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        defender = fighter("D", Armor=None, SpecialRules=["Armoured Hide (1)"])
        with dice.scripted_dice([6]):
            unsaved = RollArmorSave(attacker, defender, [Wound(3)], verbose=False)
        self.assertEqual(unsaved, [])

    def test_an_unarmoured_model_with_nothing_else_rolls_no_save(self):
        attacker = fighter("A")
        defender = fighter("D", Armor=None)
        with dice.scripted_dice([]):  # no dice should be rolled
            unsaved = RollArmorSave(attacker, defender, [Wound(3)], verbose=False)
        self.assertEqual(len(unsaved), 1)

    def test_improve_armor_in_combat_applies_once(self):
        """It used to be applied once per rule in the character's rule list."""
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        defender = fighter(
            "D",
            Armor="Light Armor",  # 6+, improved to 5+
            SpecialRules=["Improve Armor 1 in Combat", "Frenzy", "Stubborn"],
        )
        with dice.scripted_dice([4]):  # would save if wrongly improved to 4+ or better
            unsaved = RollArmorSave(attacker, defender, [Wound(3)], verbose=False)
        self.assertEqual(len(unsaved), 1)

    def test_regeneration_negates_a_wound(self):
        from combat_simulations import StrikeResult

        defender = fighter("D", Wounds=3, SpecialRules=["Regen5"])
        with dice.scripted_dice([6]):
            taken, slain = resolve_strike(
                defender, StrikeResult(unsaved=[Wound(4)]), verbose=False
            )
        self.assertEqual(taken, 0)
        self.assertEqual(defender.current_wounds, 3)

    def test_blessings_of_asuryan_only_wards_flaming(self):
        from combat_simulations import StrikeResult
        from special_rules import BlessingsofAsuryan

        defender = fighter("D", Wounds=3, SpecialRules=[BlessingsofAsuryan])
        with dice.scripted_dice([]):  # no ward should be rolled at all
            taken, _ = resolve_strike(
                defender, StrikeResult(unsaved=[Wound(4)], is_flaming=False), verbose=False
            )
        self.assertEqual(taken, 1)


class TestWoundRules(unittest.TestCase):
    def test_ethereal_ignores_non_magical_attacks(self):
        attacker = fighter("A", Weapon="Hand Weapon")
        defender = fighter("D", SpecialRules=["Ethereal"])
        wounds, _, _ = RollToWound(attacker, defender, 3, verbose=False)
        self.assertEqual(wounds, [])

    def test_magical_weapons_can_wound_the_ethereal(self):
        attacker = fighter("A", Weapon="SwordofHoeth", Strength=4)
        defender = fighter("D", Toughness=4, SpecialRules=["Ethereal"])
        with dice.constant_dice(6):
            wounds, _, is_magical = RollToWound(attacker, defender, 2, verbose=False)
        self.assertTrue(is_magical)
        self.assertEqual(len(wounds), 2)

    def test_strength_too_low_to_wound(self):
        attacker = fighter("A", Strength=1)
        defender = fighter("D", Toughness=7)
        wounds, _, _ = RollToWound(attacker, defender, 5, verbose=False)
        self.assertEqual(wounds, [])


class TestCharacterConstruction(unittest.TestCase):
    def test_every_profile_now_states_its_equipment_explicitly(self):
        """The scraped backfill gave every profile Armor/Weapon/Shield keys."""
        from faction_profiles import FactionProfiles

        for faction, profiles in FactionProfiles.items():
            for name, entry in profiles.items():
                with self.subTest(faction=faction, profile=name):
                    base = entry["base_profile"]
                    for key in ("Armor", "Weapon", "Shield"):
                        self.assertIn(key, base)

    def test_a_profile_missing_its_weapon_falls_back_to_a_hand_weapon(self):
        """Older hand-entered profiles omitted Weapon; that must still work."""
        import copy

        from faction_profiles import FactionProfiles

        entry = copy.deepcopy(FactionProfiles["High Elves"]["Noble"])
        del entry["base_profile"]["Weapon"]
        FactionProfiles["High Elves"]["_Test Noble"] = entry
        try:
            c = Character(
                name="X", faction_type="High Elves", profile_name="_Test Noble"
            )
            self.assertEqual(c.Weapon, "Hand Weapon")
        finally:
            del FactionProfiles["High Elves"]["_Test Noble"]

    def test_korhil_defaults_to_chayal(self):
        """Chayal is his listed standard kit, not an upgrade."""
        korhil = Character(
            name="Korhil", faction_type="High Elves", profile_name="Korhil"
        )
        self.assertEqual(korhil.Weapon, "Chayal")

    def test_illegal_weapon_is_rejected(self):
        with self.assertRaises(ValueError):
            Character(
                name="Cheat",
                faction_type="Orcs",
                profile_name="Orc BigBoss",
                Weapon="Chayal",
            )

    def test_shield_with_two_handed_weapon_is_rejected(self):
        with self.assertRaises(ValueError):
            Character(
                name="Cheat",
                faction_type="High Elves",
                profile_name="Noble",
                Weapon="Great Weapon",
                Shield=True,
            )

    def test_elven_honour_stat_mods_apply(self):
        c = Character(
            name="Caledorian",
            faction_type="High Elves",
            profile_name="Prince",
            elven_honors=["BloodofCaledor"],
        )
        self.assertEqual(c.WeaponSkill, 8)  # Prince WS7 +1
        self.assertEqual(c.original_Strength, c.Strength)

    def test_current_wounds_starts_full(self):
        c = fighter(Wounds=3)
        self.assertEqual(c.current_wounds, 3)


class TestWeaponStats(unittest.TestCase):
    def test_lance_bonus_is_first_round_only(self):
        from combat_simulations import apply_weapon_stats, reset_weapon_stats

        c = fighter("Knight", Weapon="Lance", Strength=4)
        apply_weapon_stats(c, is_first_round=True, verbose=False)
        self.assertEqual(c.Strength, 6)
        reset_weapon_stats(c)
        self.assertEqual(c.Strength, 4)

        apply_weapon_stats(c, is_first_round=False, verbose=False)
        self.assertEqual(c.Strength, 4)
        reset_weapon_stats(c)

    def test_flail_strength_is_first_round_only(self):
        from combat_simulations import apply_weapon_stats, reset_weapon_stats

        c = fighter("Flagellant", Weapon="Flail", Strength=3)
        apply_weapon_stats(c, is_first_round=True, verbose=False)
        self.assertEqual(c.Strength, 5)
        reset_weapon_stats(c)

        apply_weapon_stats(c, is_first_round=False, verbose=False)
        self.assertEqual(c.Strength, 3)
        reset_weapon_stats(c)

    def test_great_weapon_bonus_persists_every_round(self):
        from combat_simulations import apply_weapon_stats, reset_weapon_stats

        c = fighter("Slayer", Weapon="Great Weapon", Strength=4)
        apply_weapon_stats(c, is_first_round=False, verbose=False)
        self.assertEqual(c.Strength, 6)
        reset_weapon_stats(c)
        self.assertEqual(c.Strength, 4)


class TestOrcRules(unittest.TestCase):
    """Choppas and Furious Charge sit on every Orc profile, so they must work."""

    def orc(self, **kw):
        return fighter("Orc", SpecialRules=["Choppas", "Furious Charge"], **kw)

    def test_furious_charge_adds_an_attack_on_the_charge_round(self):
        c = self.orc(Attacks=4)
        self.assertEqual(apply_extra_attacks(c, is_first_round=True), 5)
        self.assertEqual(apply_extra_attacks(c, is_first_round=False), 4)

    def test_choppas_rerolls_to_wound_ones_on_the_charge_round(self):
        attacker = self.orc(Strength=5)
        defender = fighter("D", Toughness=5)  # wounds on 4+
        # First roll is a 1; Choppas rerolls it into a 5, which wounds.
        with dice.scripted_dice([1, 5]):
            wounds, _, _ = RollToWound(
                attacker, defender, 1, verbose=False, is_first_round=True
            )
        self.assertEqual(len(wounds), 1)

    def test_choppas_does_not_reroll_after_the_charge_round(self):
        attacker = self.orc(Strength=5)
        defender = fighter("D", Toughness=5)
        with dice.scripted_dice([1]):  # no reroll should be requested
            wounds, _, _ = RollToWound(
                attacker, defender, 1, verbose=False, is_first_round=False
            )
        self.assertEqual(wounds, [])

    def test_choppas_improves_armour_piercing_on_the_charge_round(self):
        from combat_simulations import apply_weapon_stats, reset_weapon_stats

        c = self.orc(Weapon="Great Weapon")  # AP 2
        apply_weapon_stats(c, is_first_round=True, verbose=False)
        self.assertEqual(c.ArmourPiercing, 3)
        reset_weapon_stats(c)

        apply_weapon_stats(c, is_first_round=False, verbose=False)
        self.assertEqual(c.ArmourPiercing, 2)
        reset_weapon_stats(c)

    def test_choppas_does_nothing_for_a_magic_weapon(self):
        from combat_simulations import apply_weapon_stats, reset_weapon_stats

        c = self.orc(Weapon="SwordofHoeth")  # magic, AP 2
        apply_weapon_stats(c, is_first_round=True, verbose=False)
        self.assertEqual(c.ArmourPiercing, 2)
        reset_weapon_stats(c)


class TestOrcProfiles(unittest.TestCase):
    """Statlines scraped from tow.whfb.app, in M WS BS S T I W A Ld order."""

    EXPECTED = {
        "Orc BigBoss":          (4, 5, 2, 4, 5, 4, 2, 3, 7),
        "Black Orc Bigboss":    (4, 6, 3, 4, 5, 5, 2, 3, 8),
        "Orc Warboss":          (4, 6, 2, 5, 5, 5, 3, 4, 8),
        "Black Orc Warboss":    (4, 7, 3, 5, 5, 6, 3, 4, 9),
        "Goblin Warboss":       (4, 5, 3, 4, 4, 5, 3, 4, 7),
        "Goblin Bigboss":       (4, 4, 3, 4, 4, 4, 2, 3, 6),
        "Night Goblin Warboss": (4, 5, 3, 4, 4, 5, 3, 4, 6),
        "Night Goblin Bigboss": (4, 4, 3, 4, 4, 4, 2, 3, 5),
        "Orc Weirdnob":         (4, 4, 2, 4, 5, 4, 3, 2, 8),
        "Orc Weirdboy":         (4, 3, 2, 3, 4, 3, 2, 1, 7),
        "Goblin Oddnob":        (4, 4, 3, 3, 4, 4, 3, 2, 7),
        "Goblin Oddgit":        (4, 3, 3, 3, 3, 3, 2, 1, 6),
        "Night Goblin Oddnob":  (4, 4, 3, 3, 4, 4, 3, 2, 6),
        "Night Goblin Oddgit":  (4, 3, 3, 3, 3, 3, 2, 1, 5),
        "Troll Hag":            (5, 3, 2, 6, 5, 2, 6, 3, 8),
        "Ogdruz Swampdigga":    (4, 4, 2, 4, 5, 4, 3, 2, 8),
        "Kiknik Toofsnatcha":   (4, 5, 3, 4, 4, 5, 3, 4, 8),
    }

    def test_the_whole_roster_is_present(self):
        from faction_profiles import FactionProfiles

        self.assertEqual(set(faction_characters("Orcs")), set(self.EXPECTED))

    def test_statlines_match_the_source(self):
        from faction_profiles import FactionProfiles

        for name, expected in self.EXPECTED.items():
            with self.subTest(profile=name):
                p = FactionProfiles["Orcs"][name]["base_profile"]
                actual = (
                    p["Movement"], p["WeaponSkill"], p["BallisticSkill"],
                    p["Strength"], p["Toughness"], p["Initiative"],
                    p["Wounds"], p["Attacks"], p["Leadership"],
                )
                self.assertEqual(actual, expected)

    def test_orc_rule_names_are_spelled_as_the_engine_expects(self):
        """Typos here silently disable the rule, so pin the exact strings."""
        from faction_profiles import FactionProfiles
        from special_rules import Choppas, FuriousCharge

        for name in ("Orc BigBoss", "Black Orc Bigboss", "Orc Warboss",
                     "Black Orc Warboss"):
            with self.subTest(profile=name):
                rules = FactionProfiles["Orcs"][name]["base_profile"]["SpecialRules"]
                self.assertIn(Choppas, rules)
                self.assertIn(FuriousCharge, rules)

    def test_troll_hag_regeneration_is_read(self):
        from special_rules import parse_regeneration

        troll = Character(
            name="Troll Hag", faction_type="Orcs", profile_name="Troll Hag"
        )
        self.assertEqual(parse_regeneration(troll.SpecialRules), 5)

    def test_kiknik_armoured_hide_improves_the_save(self):
        from special_rules import parse_armour_bonus

        kiknik = Character(
            name="Kiknik", faction_type="Orcs", profile_name="Kiknik Toofsnatcha"
        )
        self.assertEqual(parse_armour_bonus(kiknik.SpecialRules), 1)

    def test_kiknik_mount_only_armour_bane_stays_inert(self):
        """Armour Bane (1, Chompa only) belongs to a mount we do not simulate."""
        from special_rules import parse_armour_bane

        kiknik = Character(
            name="Kiknik", faction_type="Orcs", profile_name="Kiknik Toofsnatcha"
        )
        self.assertEqual(parse_armour_bane(kiknik.SpecialRules), 0)
        # Chompa, now simulated as his mount, keeps it for its own attacks.
        (chompa,) = kiknik.mount_parts
        self.assertEqual(parse_armour_bane(chompa.SpecialRules), 1)

    def test_hatred_dwarfs_matches_a_dwarf_defender(self):
        """The rule says "Dwarfs"; a profile's Race says "Dwarf"."""
        goblin = Character(
            name="NG", faction_type="Orcs", profile_name="Night Goblin Warboss"
        )
        dwarf = fighter("Thorek", Race="Dwarf", WeaponSkill=4)
        # Four attacks, each missing on a 1 and rerolled into a hit by Hatred.
        with dice.scripted_dice([1, 6] * 4):
            hits = RollToHit(goblin, dwarf, verbose=False, is_first_round=True)
        self.assertEqual(hits, 4)

    def test_hatred_does_not_apply_to_an_unhated_foe(self):
        goblin = Character(
            name="NG", faction_type="Orcs", profile_name="Night Goblin Warboss"
        )
        orc = fighter("Orc", Race="Orc", WeaponSkill=4)
        with dice.scripted_dice([1, 1, 1, 1]):  # no rerolls should be requested
            hits = RollToHit(goblin, orc, verbose=False, is_first_round=True)
        self.assertEqual(hits, 0)

    def test_wizard_levels_are_recorded(self):
        from faction_profiles import FactionProfiles

        casters = {
            "Orc Weirdnob": 3, "Orc Weirdboy": 1, "Goblin Oddnob": 3,
            "Goblin Oddgit": 1, "Night Goblin Oddnob": 3, "Night Goblin Oddgit": 1,
            "Troll Hag": 1, "Ogdruz Swampdigga": 3,
        }
        for name, level in casters.items():
            with self.subTest(profile=name):
                self.assertEqual(
                    FactionProfiles["Orcs"][name]["base_profile"]["WizardLevel"], level
                )


class TestPoints(unittest.TestCase):
    """Points costs from tow.whfb.app, for eventual list validation."""

    EXPECTED = {
        "Orc BigBoss": 55, "Black Orc Bigboss": 75, "Orc Warboss": 110,
        "Black Orc Warboss": 135, "Goblin Warboss": 60, "Goblin Bigboss": 35,
        "Night Goblin Warboss": 55, "Night Goblin Bigboss": 30,
        "Orc Weirdnob": 140, "Orc Weirdboy": 65, "Goblin Oddnob": 135,
        "Goblin Oddgit": 60, "Night Goblin Oddnob": 130, "Night Goblin Oddgit": 55,
        "Troll Hag": 235, "Ogdruz Swampdigga": 195, "Kiknik Toofsnatcha": 105,
    }

    def test_every_orc_profile_has_its_points_cost(self):
        from faction_profiles import FactionProfiles

        for name, points in self.EXPECTED.items():
            with self.subTest(profile=name):
                self.assertEqual(FactionProfiles["Orcs"][name]["points"], points)


class TestFactionAliases(unittest.TestCase):
    def test_the_army_book_name_resolves(self):
        from faction_profiles import resolve_faction

        for alias in ("Orc & Goblin Tribes", "Orc and Goblin Tribes",
                      "orc & goblin tribes", "O&G", "Greenskins", "Orcs"):
            with self.subTest(alias=alias):
                self.assertEqual(resolve_faction(alias), "Orcs")

    def test_high_elf_aliases_resolve(self):
        from faction_profiles import resolve_faction

        for alias in ("High Elves", "High Elf Realms", "Asur"):
            with self.subTest(alias=alias):
                self.assertEqual(resolve_faction(alias), "High Elves")

    def test_an_unknown_faction_resolves_to_none(self):
        from faction_profiles import resolve_faction

        self.assertIsNone(resolve_faction("Kislev"))
        self.assertIsNone(resolve_faction(None))

    def test_every_alias_points_at_a_real_faction(self):
        from faction_profiles import FACTION_ALIASES, FactionProfiles

        for alias, key in FACTION_ALIASES.items():
            with self.subTest(alias=alias):
                self.assertIn(key, FactionProfiles)

    def test_a_character_can_be_built_through_an_alias(self):
        c = Character(
            name="Grimgor",
            faction_type="Orc & Goblin Tribes",
            profile_name="Black Orc Warboss",
        )
        self.assertEqual(c.faction, "Orcs")
        self.assertEqual(c.WeaponSkill, 7)

    def test_profile_names_are_matched_case_insensitively(self):
        """The published names mix "BigBoss" and "Bigboss"."""
        c = Character(
            name="Boss", faction_type="Orcs", profile_name="black orc bigboss"
        )
        self.assertEqual(c.profile_name, "Black Orc Bigboss")

    def test_unknown_names_still_raise_with_the_options_listed(self):
        with self.assertRaises(ValueError) as ctx:
            Character(name="X", faction_type="Orcs", profile_name="Squig Herder")
        self.assertIn("Troll Hag", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            Character(name="X", faction_type="Kislev", profile_name="Warlord")
        self.assertIn("High Elves", str(ctx.exception))


class TestHighElfProfiles(unittest.TestCase):
    """Statlines scraped from tow.whfb.app, in M WS BS S T I W A Ld order."""

    EXPECTED = {
        "Prince":                       (5, 7, 7, 4, 3, 6, 3, 4, 10),
        "Noble":                        (5, 6, 6, 4, 3, 5, 2, 3, 9),
        "Chracian Chieftain":           (5, 6, 4, 4, 3, 5, 3, 3, 9),
        "Sea Guard Garrison Commander": (5, 6, 7, 4, 3, 5, 2, 3, 9),
        "Handmaiden of the Everqueen":  (5, 6, 7, 4, 3, 6, 2, 2, 8),
        "Archmage":                     (5, 4, 4, 3, 3, 5, 3, 2, 8),
        "Mage":                         (5, 4, 4, 3, 3, 4, 2, 1, 8),
        "Storm Weaver":                 (5, 4, 4, 3, 3, 4, 2, 2, 9),
        "Korhil Lionmane":              (5, 7, 5, 4, 3, 6, 3, 4, 9),
        "Ishaya Vess":                  (5, 7, 7, 4, 3, 7, 3, 3, 9),
    }
    POINTS = {
        "Prince": 130, "Noble": 70, "Chracian Chieftain": 105,
        "Sea Guard Garrison Commander": 90, "Handmaiden of the Everqueen": 65,
        "Archmage": 155, "Mage": 80, "Storm Weaver": 85, "Dragon Mage": 275,
        "Korhil Lionmane": 175, "Ishaya Vess": 170,
    }

    def test_the_whole_roster_is_present(self):
        from faction_profiles import FactionProfiles

        self.assertEqual(set(faction_characters("High Elves")), set(self.POINTS))

    def test_statlines_match_the_source(self):
        from faction_profiles import FactionProfiles

        for name, expected in self.EXPECTED.items():
            with self.subTest(profile=name):
                p = FactionProfiles["High Elves"][name]["base_profile"]
                actual = (
                    p["Movement"], p["WeaponSkill"], p["BallisticSkill"],
                    p["Strength"], p["Toughness"], p["Initiative"],
                    p["Wounds"], p["Attacks"], p["Leadership"],
                )
                self.assertEqual(actual, expected)

    def test_ishaya_vess_has_three_attacks(self):
        """The source says A3; an earlier hand-entered version said A4."""
        from faction_profiles import FactionProfiles

        self.assertEqual(
            FactionProfiles["High Elves"]["Ishaya Vess"]["base_profile"]["Attacks"], 3
        )

    def test_dragon_mage_has_no_movement_of_its_own(self):
        """The profile lists M as '-'; its Sun Dragon supplies movement."""
        from faction_profiles import FactionProfiles

        self.assertIsNone(
            FactionProfiles["High Elves"]["Dragon Mage"]["base_profile"]["Movement"]
        )

    def test_points_match_the_source(self):
        from faction_profiles import FactionProfiles

        for name, points in self.POINTS.items():
            with self.subTest(profile=name):
                self.assertEqual(FactionProfiles["High Elves"][name]["points"], points)


class TestAllProfiles(unittest.TestCase):
    """Structural checks that every profile in every faction must satisfy."""

    def all_profiles(self):
        from faction_profiles import FactionProfiles

        for faction, profiles in FactionProfiles.items():
            for name, entry in profiles.items():
                yield faction, name, entry

    def test_every_profile_builds_and_fights(self):
        for faction, name, _ in self.all_profiles():
            with self.subTest(faction=faction, profile=name):
                dice.seed(1)
                c = Character(name=name, faction_type=faction, profile_name=name)
                combat_simulation(c, fighter("Foe"), rounds=3, verbose=False)

    def test_every_profile_declares_a_known_race(self):
        from faction_profiles import RACE_NAMES

        known = {n for names in RACE_NAMES.values() for n in names}
        for faction, name, entry in self.all_profiles():
            with self.subTest(faction=faction, profile=name):
                self.assertIn(entry["base_profile"]["Race"], known)

    def test_every_profile_has_a_points_cost(self):
        for faction, name, entry in self.all_profiles():
            with self.subTest(faction=faction, profile=name):
                self.assertIsInstance(entry.get("points"), int)

    def test_default_kit_satisfies_the_profiles_own_options(self):
        for faction, name, entry in self.all_profiles():
            with self.subTest(faction=faction, profile=name):
                base, options = entry["base_profile"], entry["equipment_options"]
                if base.get("Armor"):
                    self.assertIn(base["Armor"], options["armor"])
                self.assertIn(base.get("Weapon", "Hand Weapon"), options["weapons"])
                if base.get("Shield"):
                    self.assertTrue(options["shield"])

    def test_every_listed_melee_weapon_has_stats(self):
        """Bows are tolerated; a melee weapon with no entry is a data error."""
        from weapons import find_weapon_key

        ranged = ("Bow", "Longbow", "Warbow")
        for faction, name, entry in self.all_profiles():
            for weapon in entry["equipment_options"]["weapons"]:
                if any(r in weapon for r in ranged):
                    continue
                with self.subTest(faction=faction, profile=name, weapon=weapon):
                    self.assertIsNotNone(find_weapon_key(weapon))


class TestElvenReflexes(unittest.TestCase):
    def test_initiative_rises_by_one_in_the_first_round(self):
        korhil = Character(
            name="Korhil", faction_type="High Elves", profile_name="Korhil Lionmane"
        )
        self.assertEqual(korhil.Initiative, 6)
        self.assertEqual(effective_initiative(korhil, is_first_round=True), 7)
        self.assertEqual(effective_initiative(korhil, is_first_round=False), 6)

    def test_it_is_capped_at_ten(self):
        c = fighter("Swift", Initiative=10, SpecialRules=["Elven Reflexes"])
        self.assertEqual(effective_initiative(c, is_first_round=True), 10)

    def test_it_decides_the_first_round_strike_order(self):
        korhil = Character(
            name="Korhil", faction_type="High Elves", profile_name="Korhil Lionmane"
        )
        foe = fighter("Foe", Initiative=6)
        first = determine_strike_order(korhil, foe, verbose=False, is_first_round=True)
        self.assertEqual(len(first), 2)
        self.assertEqual(first[0][0][0].name, "Korhil")

        later = determine_strike_order(korhil, foe, verbose=False, is_first_round=False)
        self.assertEqual(len(later), 1)  # equal Initiative, simultaneous

    def test_a_character_without_it_is_unaffected(self):
        c = fighter("Plain", Initiative=4)
        self.assertEqual(effective_initiative(c, is_first_round=True), 4)


class TestHighElfRuleParsing(unittest.TestCase):
    def test_dragon_mage_ward_is_read_from_the_bare_rule_name(self):
        """The army list says "Dragon Armour"; the constant adds "(6+ Ward)"."""
        from special_rules import parse_ward

        mage = Character(
            name="DM", faction_type="High Elves", profile_name="Dragon Mage"
        )
        self.assertEqual(parse_ward(mage.SpecialRules), 6)

    def test_blessings_of_asuryan_still_only_wards_flaming(self):
        from special_rules import parse_ward

        mage = Character(
            name="DM", faction_type="High Elves", profile_name="Dragon Mage"
        )
        # Dragon Armour gives 6+ regardless; Blessings improves it to 5+ vs flame.
        self.assertEqual(parse_ward(mage.SpecialRules, is_flaming=True), 5)

    def test_chayal_has_its_published_rules(self):
        """S+2, AP-3, Killing Blow, Requires Two Hands, and reroll To Hit 1s."""
        from weapons import get_weapon_stats

        strength, ap, rules = get_weapon_stats("Chayal")
        self.assertEqual((strength, ap), (2, -3))
        for rule in ("Killing Blow", "Requires Two Hands", "Reroll Hits 1"):
            self.assertIn(rule, rules)

    def test_korhil_can_swing_chayal_because_he_has_no_shield(self):
        korhil = Character(
            name="Korhil", faction_type="High Elves", profile_name="Korhil"
        )
        self.assertEqual(korhil.Weapon, "Chayal")
        self.assertFalse(korhil.Shield)

    def test_mathlanns_ire_has_its_published_rules(self):
        from weapons import get_weapon_stats

        strength, ap, rules = get_weapon_stats("Mathlann's Ire")
        self.assertEqual((strength, ap), (1, -2))
        self.assertIn("AB1", rules)
        self.assertNotIn("Requires Two Hands", rules)

    def test_korhil_keeps_his_pelt_and_fixed_kit(self):
        korhil = Character(
            name="Korhil", faction_type="High Elves", profile_name="Korhil"
        )
        self.assertEqual(korhil.Armor, "Heavy Armor")
        self.assertFalse(korhil.Shield)
        self.assertIn("Elven Reflexes", korhil.SpecialRules)

    def test_ishaya_vess_carries_a_shield_as_standard(self):
        vess = Character(
            name="Vess", faction_type="High Elves", profile_name="Ishaya Vess"
        )
        self.assertTrue(vess.Shield)

    def test_she_wields_mathlanns_ire_with_her_shield(self):
        """Mathlann's Ire is one-handed, so it coexists with her shield."""
        vess = Character(
            name="Vess", faction_type="High Elves", profile_name="Ishaya Vess"
        )
        self.assertEqual(vess.Weapon, "Mathlann's Ire")
        self.assertTrue(vess.Shield)

    def test_chracian_chieftain_can_take_the_great_blade(self):
        chief = Character(
            name="Chief", faction_type="High Elves",
            profile_name="Chracian Chieftain", Weapon="Chracian Great Blade",
        )
        self.assertEqual(chief.Strength, 4)


class TestProfileAliases(unittest.TestCase):
    def test_shorthand_names_resolve(self):
        from faction_profiles import resolve_profile

        cases = [
            ("High Elves", "Korhil", "Korhil Lionmane"),
            ("High Elves", "handmaiden", "Handmaiden of the Everqueen"),
            ("High Elves", "Sea Guard Commander", "Sea Guard Garrison Commander"),
            ("Orcs", "Kiknik", "Kiknik Toofsnatcha"),
            ("Orcs", "Ogdruz", "Ogdruz Swampdigga"),
        ]
        for faction, alias, expected in cases:
            with self.subTest(alias=alias):
                self.assertEqual(resolve_profile(faction, alias), expected)

    def test_every_alias_points_at_a_real_profile(self):
        from faction_profiles import PROFILE_ALIASES, FactionProfiles

        for faction, aliases in PROFILE_ALIASES.items():
            self.assertIn(faction, FactionProfiles)
            for alias, target in aliases.items():
                with self.subTest(faction=faction, alias=alias):
                    self.assertIn(target, FactionProfiles[faction])

    def test_an_unknown_profile_still_resolves_to_none(self):
        from faction_profiles import resolve_profile

        self.assertIsNone(resolve_profile("High Elves", "Everqueen"))


class TestNamedCharacterMagicItems(unittest.TestCase):
    """Named characters carry fixed wargear, so their items apply automatically."""

    def named(self, faction, profile):
        return Character(name=profile, faction_type=faction, profile_name=profile)

    def test_korhil_gains_the_pelt_of_charandis(self):
        from special_rules import parse_armour_bonus, parse_regeneration

        korhil = self.named("High Elves", "Korhil")
        self.assertEqual(parse_armour_bonus(korhil.SpecialRules), 1)
        self.assertEqual(parse_regeneration(korhil.SpecialRules), 5)

    def test_the_pelt_actually_improves_his_save(self):
        """Heavy armour 5+, improved to 4+ by the Pelt."""
        korhil = self.named("High Elves", "Korhil")
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        with dice.scripted_dice([4]):
            unsaved = RollArmorSave(attacker, korhil, [Wound(3)], verbose=False)
        self.assertEqual(len(unsaved), 0)

    def test_ogdruz_gains_the_trollhide_shawl(self):
        from special_rules import Flammable, parse_armour_bonus, parse_regeneration

        ogdruz = self.named("Orcs", "Ogdruz")
        self.assertEqual(parse_armour_bonus(ogdruz.SpecialRules), 1)
        self.assertEqual(parse_regeneration(ogdruz.SpecialRules), 5)
        self.assertIn(Flammable, ogdruz.SpecialRules)

    def test_a_magic_weapon_item_adds_no_character_rules(self):
        """Mathlann's Ire reaches her as a Weapon, not as special rules."""
        vess = self.named("High Elves", "Ishaya Vess")
        self.assertEqual(vess.Weapon, "Mathlann's Ire")
        self.assertNotIn("Magic", vess.SpecialRules)

    def test_an_item_with_no_duel_effect_adds_nothing(self):
        """Da Boss's Trophy Rack is Fear and combat result only."""
        kiknik = self.named("Orcs", "Kiknik")
        base = FactionProfilesRules("Orcs", "Kiknik Toofsnatcha")
        self.assertEqual(kiknik.SpecialRules, base)

    def test_generic_characters_do_not_get_free_items(self):
        """The Handmaiden's Horn of Isha is a purchase, not standard kit."""
        maiden = self.named("High Elves", "Handmaiden")
        self.assertNotIn("Horn of Isha", maiden.SpecialRules)

    def test_every_named_characters_items_are_recognised(self):
        from faction_profiles import FactionProfiles
        from magic_items import get_magic_item

        for faction, profiles in FactionProfiles.items():
            for name, entry in profiles.items():
                if entry["base_profile"].get("UnitCategory") != "NamedCharacter":
                    continue
                for item in entry["equipment_options"]["items"]:
                    with self.subTest(profile=name, item=item):
                        self.assertIsNotNone(get_magic_item(item))

    def test_item_names_resolve_with_or_without_a_leading_the(self):
        from magic_items import get_magic_item

        self.assertIs(
            get_magic_item("Pelt of Charandis"),
            get_magic_item("The Pelt of Charandis"),
        )

    def test_an_unrecognised_item_is_reported(self):
        from magic_items import apply_magic_items

        c = fighter("X")
        unknown = apply_magic_items(c, ["Pelt of Charandis", "Sword of Nonsense"])
        self.assertEqual(unknown, ["Sword of Nonsense"])


def FactionProfilesRules(faction, profile):
    """The profile's own special rules, before any items are applied."""
    from faction_profiles import FactionProfiles

    return list(FactionProfiles[faction][profile]["base_profile"]["SpecialRules"])


class TestWoundStealing(unittest.TestCase):
    """The Bog-wood Staff recovers a Wound per unsaved Wound inflicted."""

    def test_it_heals_a_wounded_bearer(self):
        from combat_simulations import recover_wounds

        ogdruz = Character(
            name="Ogdruz", faction_type="Orcs", profile_name="Ogdruz"
        )
        ogdruz.current_wounds = 1
        healed = recover_wounds(ogdruz, 2, verbose=False)
        self.assertEqual(healed, 2)
        self.assertEqual(ogdruz.current_wounds, 3)

    def test_it_never_exceeds_the_profile_maximum(self):
        from combat_simulations import recover_wounds

        ogdruz = Character(
            name="Ogdruz", faction_type="Orcs", profile_name="Ogdruz"
        )
        ogdruz.current_wounds = 3  # already full
        self.assertEqual(recover_wounds(ogdruz, 3, verbose=False), 0)
        self.assertEqual(ogdruz.current_wounds, 3)

    def test_a_bearer_without_the_rule_heals_nothing(self):
        from combat_simulations import recover_wounds

        c = fighter("Plain", Wounds=3)
        c.current_wounds = 1
        self.assertEqual(recover_wounds(c, 2, verbose=False), 0)
        self.assertEqual(c.current_wounds, 1)


class TestForcedHitReroll(unittest.TestCase):
    """Mathlann's Ire makes enemies reroll one successful hit each round."""

    def test_the_first_successful_hit_is_rerolled_once(self):
        vess = Character(
            name="Vess", faction_type="High Elves", profile_name="Ishaya Vess"
        )
        attacker = fighter("A", WeaponSkill=4, Attacks=2)
        # vs WS7 the attacker needs 5+. First 6 hits but is rerolled into a 1;
        # the second 6 stands because the reroll is once per round.
        with dice.scripted_dice([6, 1, 6]):
            hits = RollToHit(attacker, vess, verbose=False)
        self.assertEqual(hits, 1)

    def test_a_reroll_that_still_hits_keeps_the_hit(self):
        vess = Character(
            name="Vess", faction_type="High Elves", profile_name="Ishaya Vess"
        )
        attacker = fighter("A", WeaponSkill=4, Attacks=1)
        with dice.scripted_dice([6, 6]):
            hits = RollToHit(attacker, vess, verbose=False)
        self.assertEqual(hits, 1)

    def test_a_defender_without_the_rule_forces_nothing(self):
        attacker = fighter("A", WeaponSkill=4, Attacks=1)
        plain = fighter("D", WeaponSkill=7)
        with dice.scripted_dice([6]):  # no reroll should be requested
            hits = RollToHit(attacker, plain, verbose=False)
        self.assertEqual(hits, 1)


class TestChaosProfiles(unittest.TestCase):
    """Statlines scraped from tow.whfb.app, in M WS BS S T I W A Ld order."""

    EXPECTED = {
        "Chaos Lord":               (4, 7, 3, 5, 5, 6, 4, 5, 9),
        "Exalted Champion":         (4, 6, 3, 5, 4, 5, 3, 4, 8),
        "Aspiring Champion":        (4, 5, 3, 4, 4, 4, 2, 3, 8),
        "Sorcerer Lord":            (4, 5, 3, 4, 4, 4, 3, 3, 8),
        "Exalted Sorcerer":         (4, 4, 3, 4, 4, 3, 2, 2, 8),
        "Marauder Tribe Chieftain": (4, 5, 3, 4, 4, 4, 2, 3, 8),
        "Daemon Prince":            (6, 7, 5, 6, 5, 7, 5, 5, 9),
        "Chaos Warhound Handler":   (5, 5, 3, 4, 4, 4, 1, 1, 8),
        "Frydaal The Chainmaker":   (4, 6, 3, 5, 4, 5, 3, 4, 9),
        "Galrauch":                 (6, 6, 3, 6, 6, 4, 6, 6, 9),
    }
    POINTS = {
        "Chaos Lord": 195, "Exalted Champion": 125, "Aspiring Champion": 70,
        "Sorcerer Lord": 195, "Exalted Sorcerer": 90,
        "Marauder Tribe Chieftain": 65, "Daemon Prince": 215,
        "Chaos Warhound Handler": 15, "Frydaal The Chainmaker": 235,
        "Galrauch": 465,
    }

    def test_the_whole_roster_is_present(self):
        from faction_profiles import FactionProfiles

        self.assertEqual(set(faction_characters("Warriors of Chaos")), set(self.EXPECTED))

    def test_statlines_match_the_source(self):
        from faction_profiles import FactionProfiles

        for name, expected in self.EXPECTED.items():
            with self.subTest(profile=name):
                p = FactionProfiles["Warriors of Chaos"][name]["base_profile"]
                actual = (
                    p["Movement"], p["WeaponSkill"], p["BallisticSkill"],
                    p["Strength"], p["Toughness"], p["Initiative"],
                    p["Wounds"], p["Attacks"], p["Leadership"],
                )
                self.assertEqual(actual, expected)

    def test_points_match_the_source(self):
        from faction_profiles import FactionProfiles

        for name, points in self.POINTS.items():
            with self.subTest(profile=name):
                self.assertEqual(
                    FactionProfiles["Warriors of Chaos"][name]["points"], points
                )

    def test_marks_of_chaos_are_recorded(self):
        from faction_profiles import FactionProfiles
        from special_rules import MARKS_OF_CHAOS, MarkOfChaosUndivided

        for name, entry in FactionProfiles["Warriors of Chaos"].items():
            marks = entry["base_profile"].get("MarksOfChaos")
            if marks is None:
                continue
            with self.subTest(profile=name):
                for mark in marks:
                    self.assertIn(mark, MARKS_OF_CHAOS)
                self.assertNotIn(MarkOfChaosUndivided, marks)  # it is the default

    def test_an_exalted_sorcerer_cannot_take_the_mark_of_khorne(self):
        from faction_profiles import FactionProfiles
        from special_rules import MarkOfKhorne

        marks = FactionProfiles["Warriors of Chaos"]["Exalted Sorcerer"][
            "base_profile"
        ]["MarksOfChaos"]
        self.assertNotIn(MarkOfKhorne, marks)


class TestChaosArmour(unittest.TestCase):
    """Chaos Armour (X+) is a Ward save, not an armour save."""

    def test_the_value_is_read_as_a_ward(self):
        from special_rules import parse_ward

        self.assertEqual(parse_ward(["Chaos Armour (5+)"]), 5)
        self.assertEqual(parse_ward(["Chaos Armour (4+)"]), 4)
        self.assertEqual(parse_ward(["Chaos Armour (6+)"]), 6)

    def test_it_does_not_improve_the_armour_save(self):
        from special_rules import parse_armour_bonus

        self.assertEqual(parse_armour_bonus(["Chaos Armour (5+)"]), 0)

    def test_a_chaos_lord_gets_his_ward(self):
        from special_rules import parse_ward

        lord = Character(
            name="Lord", faction_type="Warriors of Chaos", profile_name="Chaos Lord"
        )
        self.assertEqual(parse_ward(lord.SpecialRules), 5)

    def test_a_daemon_prince_gets_a_four_up(self):
        from special_rules import parse_ward

        prince = Character(
            name="DP", faction_type="Warriors of Chaos", profile_name="Daemon Prince"
        )
        self.assertEqual(parse_ward(prince.SpecialRules), 4)

    def test_the_ward_actually_negates_wounds(self):
        from combat_simulations import StrikeResult

        lord = Character(
            name="Lord", faction_type="Warriors of Chaos", profile_name="Chaos Lord"
        )
        with dice.scripted_dice([6]):  # 5+ ward passes
            taken, slain = resolve_strike(
                lord, StrikeResult(unsaved=[Wound(4)]), verbose=False
            )
        self.assertEqual(taken, 0)
        self.assertEqual(lord.current_wounds, 4)


class TestEnsorcelledWeapons(unittest.TestCase):
    """A plain hand weapon becomes magical with an Armour Piercing of -1."""

    def lord(self, weapon="Hand Weapon"):
        return Character(
            name="Lord", faction_type="Warriors of Chaos",
            profile_name="Chaos Lord", Weapon=weapon,
        )

    def test_a_hand_weapon_gains_armour_piercing(self):
        from combat_simulations import apply_weapon_stats

        lord = self.lord()
        apply_weapon_stats(lord, is_first_round=False, verbose=False)
        self.assertEqual(lord.ArmourPiercing, 1)

    def test_it_does_not_apply_to_two_hand_weapons(self):
        from combat_simulations import apply_weapon_stats, has_ensorcelled_hand_weapon

        lord = self.lord("Two Hand Weapons")
        self.assertFalse(has_ensorcelled_hand_weapon(lord))
        apply_weapon_stats(lord, is_first_round=False, verbose=False)
        self.assertEqual(lord.ArmourPiercing, 0)

    def test_it_does_not_apply_to_other_weapon_types(self):
        from combat_simulations import apply_weapon_stats, has_ensorcelled_hand_weapon

        lord = self.lord("Great Weapon")
        self.assertFalse(has_ensorcelled_hand_weapon(lord))
        apply_weapon_stats(lord, is_first_round=False, verbose=False)
        self.assertEqual(lord.ArmourPiercing, 2)  # the Great Weapon's own AP only

    def test_the_attacks_count_as_magical(self):
        lord = self.lord()
        ghost = fighter("Ghost", SpecialRules=["Ethereal"], Toughness=4)
        with dice.constant_dice(6):
            wounds, _, is_magical = RollToWound(lord, ghost, 2, verbose=False)
        self.assertTrue(is_magical)
        self.assertEqual(len(wounds), 2)

    def test_a_model_without_the_rule_is_unaffected(self):
        from combat_simulations import has_ensorcelled_hand_weapon

        self.assertFalse(has_ensorcelled_hand_weapon(fighter("Plain")))


class TestEmpireProfiles(unittest.TestCase):
    """Statlines scraped from tow.whfb.app, in M WS BS S T I W A Ld order."""

    EXPECTED = {
        "General of the Empire":        (4, 5, 5, 4, 4, 5, 3, 3, 10),
        "Captain of the Empire":        (4, 5, 5, 4, 4, 4, 2, 2, 9),
        "Grand Master":              (None, 6, 3, 4, 4, 6, 3, 4, 9),
        "Chapter Master":            (None, 5, 3, 4, 4, 5, 2, 3, 8),
        "Wizard Lord":                  (4, 4, 3, 3, 4, 3, 3, 2, 8),
        "Master Mage":                  (4, 3, 3, 3, 3, 3, 2, 1, 7),
        "Witch Hunter":                 (4, 4, 4, 4, 4, 5, 2, 2, 8),
        "Lector of Sigmar":             (4, 5, 3, 4, 4, 5, 3, 3, 9),
        "Priest of Sigmar":             (4, 4, 3, 4, 4, 4, 2, 2, 8),
        "High Priest of Ulric":         (4, 5, 3, 4, 4, 5, 3, 3, 9),
        "Priest of Ulric":              (4, 4, 3, 4, 4, 4, 2, 2, 8),
        "Empire Engineer":              (4, 3, 4, 3, 3, 3, 2, 1, 7),
        "Harbinger of Doom":            (4, 5, 2, 4, 4, 4, 2, 3, 8),
        "General Hans von Loewenhacke": (4, 6, 5, 4, 4, 4, 3, 4, 10),
        "Harald Gemunsen":           (None, 7, 3, 4, 4, 6, 3, 4, 9),
    }
    POINTS = {
        "General of the Empire": 90, "Captain of the Empire": 45,
        "Grand Master": 145, "Chapter Master": 75, "Wizard Lord": 130,
        "Master Mage": 60, "Witch Hunter": 55, "Lector of Sigmar": 110,
        "Priest of Sigmar": 60, "High Priest of Ulric": 110, "Priest of Ulric": 60,
        "Empire Engineer": 45, "Harbinger of Doom": 65,
        "General Hans von Loewenhacke": 190, "Harald Gemunsen": 185,
    }

    def test_the_whole_roster_is_present(self):
        from faction_profiles import FactionProfiles

        self.assertEqual(set(faction_characters("Empire of Man")), set(self.EXPECTED))

    def test_statlines_match_the_source(self):
        from faction_profiles import FactionProfiles

        for name, expected in self.EXPECTED.items():
            with self.subTest(profile=name):
                p = FactionProfiles["Empire of Man"][name]["base_profile"]
                self.assertEqual(
                    (p["Movement"], p["WeaponSkill"], p["BallisticSkill"],
                     p["Strength"], p["Toughness"], p["Initiative"],
                     p["Wounds"], p["Attacks"], p["Leadership"]),
                    expected,
                )

    def test_points_match_the_source(self):
        from faction_profiles import FactionProfiles

        for name, points in self.POINTS.items():
            with self.subTest(profile=name):
                self.assertEqual(
                    FactionProfiles["Empire of Man"][name]["points"], points
                )

    def test_mounted_only_characters_have_no_movement(self):
        """Grand Master, Chapter Master and Harald list M as '-'."""
        from faction_profiles import FactionProfiles

        for name in ("Grand Master", "Chapter Master", "Harald Gemunsen"):
            with self.subTest(profile=name):
                self.assertIsNone(
                    FactionProfiles["Empire of Man"][name]["base_profile"]["Movement"]
                )

    def test_priests_and_wizards_have_magical_attacks(self):
        """"Magical Attacks" is how the army lists spell the Magic rule."""
        for name in ("Wizard Lord", "Priest of Sigmar", "High Priest of Ulric"):
            with self.subTest(profile=name):
                caster = Character(
                    name=name, faction_type="Empire of Man", profile_name=name
                )
                ghost = fighter("Ghost", SpecialRules=["Ethereal"], Toughness=3)
                with dice.constant_dice(6):
                    wounds, _, is_magical = RollToWound(
                        caster, ghost, 2, verbose=False
                    )
                self.assertTrue(is_magical)
                self.assertEqual(len(wounds), 2)

    def test_the_witch_hunter_has_killing_blow(self):
        hunter = Character(
            name="WH", faction_type="Empire of Man", profile_name="Witch Hunter"
        )
        with dice.scripted_dice([6]):
            wounds, _, _ = RollToWound(hunter, fighter("D"), 1, verbose=False)
        self.assertTrue(wounds[0].killing_blow)

    def test_harbinger_hates_all_enemies(self):
        """The rule reads "Hatred (all enemies)", not "Hatred (all)"."""
        harbinger = Character(
            name="H", faction_type="Empire of Man", profile_name="Harbinger of Doom"
        )
        foe = fighter("Anyone", Race="Dwarf", WeaponSkill=4)
        # Three attacks plus Furious Charge on the charge round makes four.
        with dice.scripted_dice([1, 6] * 4):
            hits = RollToHit(harbinger, foe, verbose=False, is_first_round=True)
        self.assertEqual(hits, 4)


class TestDwarfProfiles(unittest.TestCase):
    """Statlines scraped from tow.whfb.app, in M WS BS S T I W A Ld order."""

    EXPECTED = {
        "King":               (3, 7, 4, 4, 5, 4, 3, 4, 10),
        "Thane":              (3, 6, 4, 4, 5, 3, 2, 3, 9),
        "Runelord":           (3, 6, 4, 4, 5, 3, 3, 3, 9),
        "Runesmith":          (3, 5, 4, 4, 4, 2, 2, 2, 9),
        "Daemon Slayer":      (3, 7, 3, 4, 5, 5, 3, 4, 10),
        "Dragon Slayer":      (3, 6, 3, 4, 5, 4, 2, 3, 10),
        "Engineer":           (3, 4, 5, 4, 4, 2, 2, 2, 9),
        "Engineer Sapper":    (3, 4, 5, 4, 4, 2, 2, 2, 9),
        "Ungrim Ironfist":    (3, 9, 4, 4, 6, 5, 3, 4, 10),
        "Thorgrim Ulleksson": (3, 6, 4, 4, 5, 3, 3, 3, 10),
        "Burlok Damminson":   (3, 5, 5, 4, 4, 2, 2, 3, 10),
        # The Forgefather & Anvil Guard row: a war machine fights with its crew.
        "Anvil of Doom":      (3, 6, 4, 4, 5, 3, 4, 5, 9),
    }
    POINTS = {
        "King": 125, "Thane": 60, "Runelord": 120, "Runesmith": 65,
        "Daemon Slayer": 130, "Dragon Slayer": 70, "Engineer": 50,
        "Engineer Sapper": 70, "Ungrim Ironfist": 315,
        "Thorgrim Ulleksson": 250, "Burlok Damminson": 85,
        "Anvil of Doom": 235,
    }

    def test_the_whole_roster_is_present(self):
        from faction_profiles import FactionProfiles

        self.assertEqual(
            set(faction_characters("Dwarfen Mountain Holds")), set(self.EXPECTED)
        )

    def test_statlines_match_the_source(self):
        from faction_profiles import FactionProfiles

        for name, expected in self.EXPECTED.items():
            with self.subTest(profile=name):
                p = FactionProfiles["Dwarfen Mountain Holds"][name]["base_profile"]
                self.assertEqual(
                    (p["Movement"], p["WeaponSkill"], p["BallisticSkill"],
                     p["Strength"], p["Toughness"], p["Initiative"],
                     p["Wounds"], p["Attacks"], p["Leadership"]),
                    expected,
                )

    def test_points_match_the_source(self):
        from faction_profiles import FactionProfiles

        for name, points in self.POINTS.items():
            with self.subTest(profile=name):
                self.assertEqual(
                    FactionProfiles["Dwarfen Mountain Holds"][name]["points"], points
                )

    def test_ungrim_has_weapon_skill_nine(self):
        """WS9 is off the end of most charts; the lookup must still work."""
        ungrim = Character(
            name="Ungrim", faction_type="Dwarfen Mountain Holds",
            profile_name="Ungrim",
        )
        self.assertEqual(ungrim.WeaponSkill, 9)
        with dice.constant_dice(4):
            self.assertGreater(RollToHit(ungrim, fighter("D"), verbose=False), 0)

    def test_hatred_of_orcs_and_goblins_matches_both(self):
        king = Character(
            name="King", faction_type="Dwarfen Mountain Holds", profile_name="King"
        )
        for race in ("Orc", "Goblin", "Night Goblin"):
            with self.subTest(race=race):
                foe = fighter("Foe", Race=race, WeaponSkill=4)
                with dice.scripted_dice([1, 6] * 4):  # 4 attacks, all rerolled
                    hits = RollToHit(king, foe, verbose=False, is_first_round=True)
                self.assertEqual(hits, 4)

    def test_it_does_not_hate_a_chaos_warrior(self):
        king = Character(
            name="King", faction_type="Dwarfen Mountain Holds", profile_name="King"
        )
        foe = fighter("Foe", Race="Chaos Warrior", WeaponSkill=4)
        with dice.scripted_dice([1, 1, 1, 1]):  # no rerolls expected
            hits = RollToHit(king, foe, verbose=False, is_first_round=True)
        self.assertEqual(hits, 0)


class TestGromrilRules(unittest.TestCase):
    def test_gromril_armour_rerolls_saves_of_one(self):
        king = Character(
            name="King", faction_type="Dwarfen Mountain Holds", profile_name="King"
        )
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        # Full plate 4+. A 1 is rerolled into a 5, which saves.
        with dice.scripted_dice([1, 5]):
            unsaved = RollArmorSave(attacker, king, [Wound(3)], verbose=False)
        self.assertEqual(len(unsaved), 0)

    def test_a_model_without_it_does_not_reroll(self):
        defender = fighter("D", Armor="Full Plate Armor")
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        with dice.scripted_dice([1]):  # no reroll should be requested
            unsaved = RollArmorSave(attacker, defender, [Wound(3)], verbose=False)
        self.assertEqual(len(unsaved), 1)

    def test_gromril_weapons_give_a_hand_weapon_armour_piercing(self):
        from combat_simulations import apply_weapon_stats, has_gromril_hand_weapon

        king = Character(
            name="King", faction_type="Dwarfen Mountain Holds", profile_name="King"
        )
        self.assertTrue(has_gromril_hand_weapon(king))
        apply_weapon_stats(king, is_first_round=False, verbose=False)
        self.assertEqual(king.ArmourPiercing, 1)

    def test_gromril_weapons_do_not_apply_to_a_great_weapon(self):
        from combat_simulations import apply_weapon_stats, has_gromril_hand_weapon

        king = Character(
            name="King", faction_type="Dwarfen Mountain Holds",
            profile_name="King", Weapon="Great Weapon",
        )
        self.assertFalse(has_gromril_hand_weapon(king))
        apply_weapon_stats(king, is_first_round=False, verbose=False)
        self.assertEqual(king.ArmourPiercing, 2)  # the Great Weapon's own AP

    def test_gromril_weapons_are_not_magical(self):
        """Unlike Ensorcelled Weapons, Gromril grants no Magical Attacks."""
        king = Character(
            name="King", faction_type="Dwarfen Mountain Holds", profile_name="King"
        )
        ghost = fighter("Ghost", SpecialRules=["Ethereal"])
        wounds, _, is_magical = RollToWound(king, ghost, 3, verbose=False)
        self.assertFalse(is_magical)
        self.assertEqual(wounds, [])


class TestFactionPackage(unittest.TestCase):
    """Each faction is one module; the registry assembles them."""

    def test_every_module_declares_the_required_names(self):
        from factions import FACTION_MODULES

        for module in FACTION_MODULES:
            with self.subTest(module=module.__name__):
                for attr in ("FACTION", "ALIASES", "PROFILE_ALIASES",
                             "CHARACTERS", "UNITS", "PROFILES"):
                    self.assertTrue(hasattr(module, attr), attr)

    def test_profiles_is_characters_plus_units(self):
        from factions import FACTION_MODULES

        for module in FACTION_MODULES:
            with self.subTest(module=module.__name__):
                self.assertEqual(
                    set(module.PROFILES),
                    set(module.CHARACTERS) | set(module.UNITS),
                )

    def test_the_registry_matches_the_modules(self):
        from faction_profiles import FactionProfiles
        from factions import FACTION_MODULES

        self.assertEqual(
            set(FactionProfiles), {m.FACTION for m in FACTION_MODULES}
        )

    def test_new_faction_aliases_resolve(self):
        from faction_profiles import resolve_faction

        self.assertEqual(resolve_faction("The Empire"), "Empire of Man")
        self.assertEqual(resolve_faction("Dwarfs"), "Dwarfen Mountain Holds")
        self.assertEqual(resolve_faction("Dawi"), "Dwarfen Mountain Holds")

    def test_new_profile_aliases_resolve(self):
        from faction_profiles import resolve_profile

        self.assertEqual(
            resolve_profile("Dwarfen Mountain Holds", "Ungrim"), "Ungrim Ironfist"
        )
        self.assertEqual(
            resolve_profile("Empire of Man", "Captain"), "Captain of the Empire"
        )

    def test_no_two_factions_claim_the_same_alias(self):
        from factions import build_faction_aliases

        build_faction_aliases()  # raises on a collision


class TestUnverifiedItems(unittest.TestCase):
    """Items whose rules pages would not load carry no rules and are tracked."""

    # Pages that would not load, or entries not yet transcribed. Keep this in
    # step with what has actually been read off the site.
    # Both were read from the site's page data in the units pass; none remain.
    EXPECTED = []

    def test_the_unverified_list_is_exactly_this(self):
        """Pinning it means the gap cannot grow without someone noticing."""
        from magic_items import unverified_items

        self.assertEqual(unverified_items(), self.EXPECTED)

    def test_unverified_items_grant_no_rules(self):
        from magic_items import MagicItemDict, unverified_items

        for name in unverified_items():
            with self.subTest(item=name):
                self.assertEqual(MagicItemDict[name].get("rules", []), [])

    def test_every_unverified_item_explains_itself(self):
        from magic_items import MagicItemDict, unverified_items

        for name in unverified_items():
            with self.subTest(item=name):
                self.assertTrue(MagicItemDict[name].get("text"))


class TestNewlyVerifiedItems(unittest.TestCase):
    def test_the_skull_of_the_unicorn_lord_wards_by_attack_type(self):
        from special_rules import parse_ward

        ghorros = Character(name="G", faction_type="Beastmen Brayherds",
                            profile_name="Ghorros Warhoof")
        self.assertEqual(parse_ward(ghorros.SpecialRules, is_magical=False), 6)
        self.assertEqual(parse_ward(ghorros.SpecialRules, is_magical=True), 5)

    def test_a_braystaff_counts_as_a_great_weapon(self):
        from weapons import get_weapon_stats

        self.assertEqual(get_weapon_stats("Braystaff"), get_weapon_stats("Grisly Totem"))
        self.assertEqual(get_weapon_stats("Braystaff")[:2], (2, -2))


class TestKillingBlowOldWorldRules(unittest.TestCase):
    """The Old World: no Armour or Regeneration save; Ward only; infantry/cavalry only."""

    def test_no_armour_save_is_allowed(self):
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        defender = fighter("D", Armor="Full Plate Armor")  # would be a 4+
        with dice.scripted_dice([]):  # no armour dice should be rolled at all
            unsaved = RollArmorSave(
                attacker, defender, [Wound(6, killing_blow=True)], verbose=False
            )
        self.assertEqual(len(unsaved), 1)

    def test_an_ordinary_wound_still_gets_its_armour_save(self):
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        defender = fighter("D", Armor="Full Plate Armor")
        with dice.scripted_dice([5]):
            unsaved = RollArmorSave(attacker, defender, [Wound(6)], verbose=False)
        self.assertEqual(len(unsaved), 0)

    def test_no_regeneration_save_is_allowed(self):
        from combat_simulations import StrikeResult

        defender = fighter("D", Wounds=3, SpecialRules=["Regen4"])
        with dice.scripted_dice([]):  # neither ward nor regen dice
            taken, slain = resolve_strike(
                defender, StrikeResult(unsaved=[Wound(6, killing_blow=True)]),
                verbose=False,
            )
        self.assertTrue(slain)

    def test_a_ward_save_is_allowed(self):
        from combat_simulations import StrikeResult

        defender = fighter("D", Wounds=3, SpecialRules=["Ward4"])
        with dice.scripted_dice([5]):
            taken, slain = resolve_strike(
                defender, StrikeResult(unsaved=[Wound(6, killing_blow=True)]),
                verbose=False,
            )
        self.assertFalse(slain)
        self.assertEqual(defender.current_wounds, 3)

    def test_it_does_not_affect_a_behemoth(self):
        """Killing Blow only bites infantry and cavalry."""
        from combat_simulations import is_killing_blow_target

        galrauch = Character(
            name="Galrauch", faction_type="Warriors of Chaos", profile_name="Galrauch"
        )
        self.assertEqual(galrauch.TroopType, "Behemoth")
        self.assertFalse(is_killing_blow_target(galrauch))

        slayer = Character(
            name="DS", faction_type="Dwarfen Mountain Holds",
            profile_name="Daemon Slayer",
        )
        with dice.constant_dice(6):
            wounds, _, _ = RollToWound(slayer, galrauch, 2, verbose=False)
        self.assertTrue(wounds)
        self.assertFalse(any(w.killing_blow for w in wounds))

    def test_it_does_not_affect_a_monstrous_creature(self):
        from combat_simulations import is_killing_blow_target

        prince = Character(
            name="DP", faction_type="Warriors of Chaos", profile_name="Daemon Prince"
        )
        self.assertFalse(is_killing_blow_target(prince))

    def test_it_does_affect_infantry_and_cavalry(self):
        from combat_simulations import is_killing_blow_target

        for faction, profile in (
            ("Dwarfen Mountain Holds", "King"),          # Heavy Infantry
            ("Orcs", "Kiknik"),                          # Light Cavalry
            ("Empire of Man", "Grand Master"),           # Heavy Cavalry
        ):
            with self.subTest(profile=profile):
                c = Character(name=profile, faction_type=faction, profile_name=profile)
                self.assertTrue(is_killing_blow_target(c))

    def test_a_custom_fighter_counts_as_infantry(self):
        from combat_simulations import is_killing_blow_target

        self.assertTrue(is_killing_blow_target(fighter("Plain")))


class TestTranscribedMagicItems(unittest.TestCase):
    """The eight items whose pages would not load, transcribed from the book."""

    def test_the_eight_empire_and_dwarf_items_are_all_verified(self):
        from magic_items import unverified_items

        transcribed = [
            "Armour of Skaldour", "Furnace Hammer", "Griffon Helm",
            "Grudge-Settler", "Grudgestone", "Judgement", "Rivet Gun",
            "Slayer Crown",
        ]
        for name in transcribed:
            with self.subTest(item=name):
                self.assertNotIn(name, unverified_items())

    def test_griffon_helm_gives_a_ward_and_killing_blow_immunity(self):
        from combat_simulations import is_killing_blow_target
        from special_rules import parse_ward

        hans = Character(
            name="Hans", faction_type="Empire of Man",
            profile_name="General Hans von Loewenhacke",
        )
        self.assertEqual(parse_ward(hans.SpecialRules), 5)
        self.assertFalse(is_killing_blow_target(hans))

    def test_killing_blow_immunity_costs_him_one_wound_with_saves(self):
        """The Helm turns a Killing Blow into an ordinary wound."""
        hans = Character(
            name="Hans", faction_type="Empire of Man",
            profile_name="General Hans von Loewenhacke",
        )
        slayer = Character(
            name="DS", faction_type="Dwarfen Mountain Holds",
            profile_name="Daemon Slayer",
        )
        with dice.constant_dice(6):
            wounds, _, _ = RollToWound(slayer, hans, 1, verbose=False)
        self.assertFalse(wounds[0].killing_blow)   # so armour applies as normal

    def test_slayer_crown_improves_armour_by_two_and_wards(self):
        from special_rules import parse_armour_bonus, parse_ward

        ungrim = Character(
            name="Ungrim", faction_type="Dwarfen Mountain Holds",
            profile_name="Ungrim",
        )
        self.assertEqual(parse_armour_bonus(ungrim.SpecialRules), 2)
        self.assertEqual(parse_ward(ungrim.SpecialRules), 5)

    def test_the_crown_actually_improves_his_save(self):
        """Light armour 6+, improved to 4+ by the Crown."""
        ungrim = Character(
            name="Ungrim", faction_type="Dwarfen Mountain Holds",
            profile_name="Ungrim",
        )
        attacker = fighter("A")
        attacker.ArmourPiercing = 0
        with dice.scripted_dice([4]):
            unsaved = RollArmorSave(attacker, ungrim, [Wound(3)], verbose=False)
        self.assertEqual(len(unsaved), 0)

    def test_armour_of_skaldour_is_heavy_armour_with_a_conditional_ward(self):
        from special_rules import parse_ward

        thorgrim = Character(
            name="Thorgrim", faction_type="Dwarfen Mountain Holds",
            profile_name="Thorgrim",
        )
        self.assertEqual(thorgrim.Armor, "Heavy Armor")
        self.assertIsNone(parse_ward(thorgrim.SpecialRules))
        self.assertEqual(parse_ward(thorgrim.SpecialRules, is_killing_blow=True), 4)
        self.assertEqual(
            parse_ward(thorgrim.SpecialRules, is_multiple_wounds=True), 4
        )

    def test_the_grudgestone_does_nothing_in_a_duel(self):
        from magic_items import MagicItemDict

        self.assertEqual(MagicItemDict["Grudgestone"]["rules"], [])

    def test_judgement_is_two_handed_with_multiple_wounds(self):
        from special_rules import parse_multiple_wounds
        from weapons import get_weapon_stats

        strength, ap, rules = get_weapon_stats("Judgement")
        self.assertEqual((strength, ap), (2, -2))
        self.assertIn("Requires Two Hands", rules)
        self.assertEqual(parse_multiple_wounds(rules), 2)

    def test_grudge_settler_has_armour_bane(self):
        from special_rules import parse_armour_bane
        from weapons import get_weapon_stats

        strength, ap, rules = get_weapon_stats("Grudge-Settler")
        self.assertEqual((strength, ap), (2, -1))
        self.assertEqual(parse_armour_bane(rules), 1)


class TestMultipleWounds(unittest.TestCase):
    def test_each_unsaved_wound_costs_the_multiplier(self):
        from combat_simulations import StrikeResult

        defender = fighter("D", Wounds=4)
        taken, slain = resolve_strike(
            defender, StrikeResult(unsaved=[Wound(4)], multiple_wounds=2),
            verbose=False,
        )
        self.assertEqual(taken, 2)
        self.assertEqual(defender.current_wounds, 2)

    def test_judgement_carries_it_into_a_strike(self):
        hans = Character(
            name="Hans", faction_type="Empire of Man",
            profile_name="General Hans von Loewenhacke",
        )
        with dice.constant_dice(6):
            result = OneRoundMeleeCombat(
                hans, fighter("D", Toughness=3), verbose=False
            )
        self.assertEqual(result.multiple_wounds, 2)

    def test_an_ordinary_weapon_multiplies_by_one(self):
        with dice.constant_dice(6):
            result = OneRoundMeleeCombat(
                fighter("A"), fighter("D", Toughness=3), verbose=False
            )
        self.assertEqual(result.multiple_wounds, 1)

    def test_excess_wounds_do_not_go_below_zero(self):
        from combat_simulations import StrikeResult

        defender = fighter("D", Wounds=1)
        taken, slain = resolve_strike(
            defender, StrikeResult(unsaved=[Wound(4)], multiple_wounds=2),
            verbose=False,
        )
        self.assertEqual(defender.current_wounds, 0)


class TestArtilleryStrength(unittest.TestCase):
    """The Furnace Hammer rolls an Artillery dice for its Strength."""

    def burlok(self):
        return Character(
            name="Burlok", faction_type="Dwarfen Mountain Holds",
            profile_name="Burlok",
        )

    def test_the_artillery_dice_has_the_right_faces(self):
        rolled = []
        for face in range(1, 7):
            with dice.constant_dice(face):
                rolled.append(dice.roll_artillery())
        self.assertEqual(rolled, [2, 4, 6, 8, 10, "Misfire"])

    def test_strength_comes_from_the_dice(self):
        burlok = self.burlok()
        self.assertEqual(burlok.Strength, 4)
        with dice.constant_dice(5):  # a 5 on the artillery dice is Strength 10
            result = OneRoundMeleeCombat(
                burlok, fighter("D", Toughness=4), verbose=False
            )
        self.assertGreater(result.hits, 0)
        self.assertEqual(burlok.Strength, 4)  # reset afterwards

    def test_a_misfire_costs_a_wound_and_all_attacks(self):
        burlok = self.burlok()
        with dice.constant_dice(6):  # a 6 on the artillery dice is a Misfire
            result = OneRoundMeleeCombat(
                burlok, fighter("D", Toughness=4), verbose=False
            )
        self.assertEqual(result.hits, 0)
        self.assertEqual(result.unsaved, [])
        self.assertEqual(result.self_wounds, 1)

    def test_a_misfire_is_applied_during_a_duel(self):
        import io, contextlib

        for seed in range(60):
            dice.seed(seed)
            burlok = self.burlok()
            foe = fighter("Foe", Toughness=6, WeaponSkill=1, Attacks=1, Wounds=6)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                combat_simulation(burlok, foe, rounds=4, verbose=True)
            if "misfires" in buf.getvalue():
                self.assertLess(burlok.current_wounds, burlok.Wounds)
                return
        self.fail("no misfire observed in 60 seeds")


if __name__ == "__main__":
    unittest.main(verbosity=2)
