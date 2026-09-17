"""Boundary conditions: zero and out-of-range values, impossible rolls, odd kit."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from support import build, fighter

import dice
from character_model import Character
from combat_simulations import (
    BEST_POSSIBLE_ARMOUR_SAVE,
    RollArmorSave,
    RollToHit,
    RollToWound,
    Wound,
    combat_simulation,
    determine_strike_order,
)
from special_rules import parse_ward


def quiet_duel(a, b, rounds=3):
    with redirect_stdout(io.StringIO()):
        return combat_simulation(a, b, rounds=rounds, verbose=False)


class TestDegenerateDuels(unittest.TestCase):
    def test_zero_rounds_is_a_draw_at_full_wounds(self):
        a, b = fighter("A"), fighter("B")
        self.assertIsNone(quiet_duel(a, b, rounds=0))
        self.assertEqual((a.current_wounds, b.current_wounds), (3, 3))

    def test_fighters_with_no_attacks_draw(self):
        dice.seed(0)
        self.assertIsNone(quiet_duel(fighter("A", Attacks=0), fighter("B", Attacks=0)))

    def test_fighters_that_cannot_wound_each_other_draw(self):
        dice.seed(0)
        a = fighter("A", Strength=1, Toughness=10)
        b = fighter("B", Strength=1, Toughness=10)
        self.assertIsNone(quiet_duel(a, b, rounds=10))
        self.assertEqual((a.current_wounds, b.current_wounds), (3, 3))

    def test_a_one_sided_duel_is_won_by_the_only_fighter_who_can_wound(self):
        dice.seed(0)
        weak = fighter("Weak", Strength=1, Toughness=4)
        strong = fighter("Strong", Strength=4, Toughness=10)
        self.assertIs(quiet_duel(weak, strong, rounds=20), strong)

    def test_simultaneous_kills_are_a_draw(self):
        a = fighter("A", Wounds=1, Attacks=1)
        b = fighter("B", Wounds=1, Attacks=1)
        with dice.constant_dice(6):
            self.assertIsNone(quiet_duel(a, b))
        self.assertEqual((a.current_wounds, b.current_wounds), (0, 0))

    def test_a_long_duel_terminates(self):
        dice.seed(0)
        a = fighter("A", Toughness=10, Wounds=10)
        b = fighter("B", Toughness=10, Wounds=10)
        self.assertIn(quiet_duel(a, b, rounds=500), (a, b, None))

    def test_identically_named_fighters_are_told_apart_by_identity(self):
        a = fighter("Twin", Wounds=1, Attacks=5, Initiative=10)
        b = fighter("Twin", Wounds=1, Attacks=0, Initiative=1)
        with dice.constant_dice(6):
            self.assertIs(quiet_duel(a, b), a)

    def test_a_misfire_can_kill_its_own_wielder(self):
        wielder = fighter("Burlok", Weapon="Furnace Hammer", Wounds=1, Attacks=1)
        target = fighter("Target", Toughness=10, Attacks=0)
        with dice.constant_dice(6):  # 6 on the Artillery dice is a Misfire
            self.assertIs(quiet_duel(wielder, target), target)
        self.assertEqual(wielder.current_wounds, 0)


class TestOutOfRangeCharacteristics(unittest.TestCase):
    def test_characteristics_above_ten_are_clamped(self):
        dice.seed(0)
        a = fighter("A", WeaponSkill=15, Strength=14, Toughness=12, Initiative=11)
        b = fighter("B")
        self.assertIn(quiet_duel(a, b), (a, b, None))

    def test_zero_and_missing_characteristics_do_not_crash(self):
        dice.seed(0)
        a = fighter("A", WeaponSkill=0, Strength=0, Initiative=None)
        b = fighter("B", Toughness=0)
        self.assertIn(quiet_duel(a, b), (a, b, None))

    def test_ws_ten_against_ws_one_hits_on_a_two(self):
        a = fighter("A", WeaponSkill=10, Attacks=1)
        b = fighter("B", WeaponSkill=1)
        with dice.scripted_dice([2]):
            self.assertEqual(RollToHit(a, b, verbose=False), 1)
        with dice.scripted_dice([1]):
            self.assertEqual(RollToHit(a, b, verbose=False), 0)

    def test_a_natural_six_does_not_wound_what_the_chart_forbids(self):
        a, b = fighter("A", Strength=1), fighter("B", Toughness=10)
        with dice.constant_dice(6):
            wounds, _, _ = RollToWound(a, b, 5, verbose=False)
        self.assertEqual(wounds, [])

    def test_a_character_without_a_race_is_hated_by_nobody(self):
        dice.seed(0)
        a = fighter("A", SpecialRules=["Hatred (Dwarfs)"])
        b = fighter("B", Race=None)
        self.assertIn(quiet_duel(a, b), (a, b, None))


class TestArmourBoundaries(unittest.TestCase):
    def test_saves_cannot_improve_past_the_cap(self):
        attacker = fighter("A")
        tank = fighter("Tank", Armor="Plate Armor", Shield=True,
                       SpecialRules=["Armoured Hide (3)"])
        # 4+ base, -1 shield, -3 hide would be 0+; the cap keeps it at 2+.
        with dice.scripted_dice([BEST_POSSIBLE_ARMOUR_SAVE - 1]):
            self.assertEqual(len(RollArmorSave(attacker, tank, [Wound(roll=4)], verbose=False)), 1)
        with dice.scripted_dice([BEST_POSSIBLE_ARMOUR_SAVE]):
            self.assertEqual(RollArmorSave(attacker, tank, [Wound(roll=4)], verbose=False), [])

    def test_piercing_beyond_six_rolls_no_save(self):
        attacker = fighter("A")
        attacker.ArmourPiercing = 3
        target = fighter("T", Armor="Heavy Armor")  # 5+ becomes 8+
        with dice.scripted_dice([]):  # asking for a die would fail the test
            self.assertEqual(len(RollArmorSave(attacker, target, [Wound(roll=4)], verbose=False)), 1)

    def test_an_unknown_armour_saves_nothing(self):
        attacker = fighter("A")
        target = fighter("T", Armor="Cardboard")
        with dice.scripted_dice([]):
            self.assertEqual(len(RollArmorSave(attacker, target, [Wound(roll=4)], verbose=False)), 1)

    def test_no_wounds_rolls_no_saves(self):
        with dice.scripted_dice([]):
            self.assertEqual(RollArmorSave(fighter("A"), fighter("T", Armor="Plate Armor"), [], verbose=False), [])


class TestUnusualKit(unittest.TestCase):
    def test_a_weapon_with_no_melee_profile_fights_as_a_plain_weapon(self):
        dice.seed(0)
        archer, other = fighter("Archer", Weapon="Warbow"), fighter("B")
        self.assertIn(quiet_duel(archer, other), (archer, other, None))
        self.assertEqual(archer.Strength, 4)

    def test_a_custom_two_handed_weapon_with_a_shield_is_rejected(self):
        with self.assertRaises(ValueError):
            fighter("A", Weapon="Great Weapon", Shield=True)

    def test_shield_false_and_none_both_mean_no_shield(self):
        self.assertFalse(fighter("A", Shield=False).Shield)
        self.assertFalse(fighter("A", Shield=None).Shield)

    def test_honours_are_ignored_for_a_model_that_is_not_a_high_elf(self):
        orc = build("Orc & Goblin Tribes", "Orc Warboss", elven_honors=["BloodofCaledor"])
        self.assertEqual(orc.WeaponSkill, build("Orc & Goblin Tribes", "Orc Warboss").WeaponSkill)
        self.assertNotIn("Dragon Armour (6+ Ward)", orc.SpecialRules)

    def test_a_ward_with_an_unknown_condition_is_an_error(self):
        with self.assertRaises(ValueError):
            parse_ward(["Ward4 (Tuesdays)"])

    def test_a_bare_hatred_hates_nobody(self):
        a = fighter("A", Attacks=1, SpecialRules=["Hatred"])
        with dice.scripted_dice([1]):  # a miss that would be rerolled if hated
            self.assertEqual(RollToHit(a, fighter("B"), verbose=False, is_first_round=True), 0)

    def test_strike_first_on_both_sides_is_simultaneous_at_equal_initiative(self):
        a = fighter("A", SpecialRules=["Strike First"])
        b = fighter("B", SpecialRules=["Strike First"])
        self.assertEqual(len(determine_strike_order(a, b, verbose=False)), 1)

    def test_a_profile_built_twice_does_not_share_rule_lists(self):
        first = build("Orc & Goblin Tribes", "Orc Warboss", SpecialRules=["Frenzy"])
        second = build("Orc & Goblin Tribes", "Orc Warboss")
        self.assertIn("Frenzy", first.SpecialRules)
        self.assertNotIn("Frenzy", second.SpecialRules)

    def test_building_a_profile_does_not_modify_the_registry(self):
        from faction_profiles import FactionProfiles

        base = FactionProfiles["High Elf Realms"]["Prince"]["base_profile"]
        before = list(base["SpecialRules"]), base["WeaponSkill"]
        build("High Elf Realms", "Prince", elven_honors=["BloodofCaledor", "AnointedofAsuryan"])
        self.assertEqual((list(base["SpecialRules"]), base["WeaponSkill"]), before)

    def test_an_unknown_faction_or_profile_raises(self):
        with self.assertRaises(ValueError):
            Character(name="X", faction_type="Atlantis", profile_name="King")
        with self.assertRaises(ValueError):
            Character(name="X", faction_type="High Elf Realms", profile_name="Emperor")


if __name__ == "__main__":
    unittest.main()
