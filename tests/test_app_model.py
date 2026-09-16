"""Tests for app_model, the display-free half of the desktop app."""

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app_model import (  # noqa: E402
    NO_ARMOUR_LABEL,
    CharacterStore,
    FighterSpec,
    faction_names,
    gear_options,
    narrate_duel,
    profile_names,
    run_statistics,
)


def prince(**overrides):
    fields = dict(name="Aenarion", faction="High Elves", profile="Prince",
                  weapon="Great Weapon", armour="Plate Armor")
    fields.update(overrides)
    return FighterSpec(**fields)


def warboss(**overrides):
    fields = dict(name="Grimgor", faction="Orcs", profile="Orc Warboss",
                  weapon="Great Weapon", armour="Light Armor")
    fields.update(overrides)
    return FighterSpec(**fields)


class TestGearOptions(unittest.TestCase):
    def test_every_profile_builds_with_every_offered_weapon(self):
        for faction in faction_names():
            for profile in profile_names(faction):
                opts = gear_options(faction, profile)
                defaults = opts["defaults"]
                self.assertIn(defaults["armour"], opts["armour"], profile)
                for weapon in opts["weapons"]:
                    with self.subTest(faction=faction, profile=profile, weapon=weapon):
                        FighterSpec(profile, faction, profile, weapon,
                                    defaults["armour"], defaults["shield"]).build()

    def test_armour_is_led_by_none(self):
        self.assertEqual(gear_options("High Elves", "Prince")["armour"][0], NO_ARMOUR_LABEL)

    def test_upgrades_and_honours_are_offered_where_the_profile_allows(self):
        self.assertEqual(gear_options("Orcs", "Orc Warboss")["optional_rules"],
                         ["Frenzy", "Warpaint"])
        self.assertIn("BloodofCaledor", gear_options("High Elves", "Prince")["honours"])
        self.assertEqual(gear_options("Orcs", "Orc Warboss")["honours"], [])


class TestFighterSpec(unittest.TestCase):
    def test_choosing_no_armour_overrides_the_profile_default(self):
        self.assertFalse(prince(armour=NO_ARMOUR_LABEL).build().Armor)

    def test_illegal_armour_is_rejected(self):
        with self.assertRaises(ValueError):
            warboss(armour="Plate Armor").build()

    def test_two_handed_weapon_with_shield_is_rejected(self):
        with self.assertRaises(ValueError):
            prince(shield=True).build()

    def test_upgrades_and_honours_reach_the_character(self):
        self.assertIn("Frenzy", warboss(optional_rules=["Frenzy"]).build().SpecialRules)
        built = prince(honours=["BloodofCaledor"]).build()
        self.assertEqual(built.WeaponSkill, 8)

    def test_round_trips_through_a_dict(self):
        spec = warboss(optional_rules=["Frenzy"])
        self.assertEqual(FighterSpec.from_dict(spec.to_dict()), spec)


class TestRuns(unittest.TestCase):
    def test_statistics_account_for_every_duel(self):
        stats = run_statistics(prince(), warboss(), runs=200, rounds=3, seed=1)
        self.assertEqual(stats.wins_a + stats.wins_b + stats.draws, 200)
        self.assertLessEqual(stats.kills_a, stats.wins_a)
        self.assertIn("Aenarion", stats.summary())

    def test_seeded_statistics_are_reproducible(self):
        first = run_statistics(prince(), warboss(), runs=100, rounds=3, seed=5)
        second = run_statistics(prince(), warboss(), runs=100, rounds=3, seed=5)
        self.assertEqual(first, second)

    def test_progress_is_reported(self):
        seen = []
        run_statistics(prince(), warboss(), runs=50, rounds=1, seed=1, progress=seen.append)
        self.assertEqual(seen[-1], 50)

    def test_narration_is_reproducible_and_names_both_fighters(self):
        text = narrate_duel(prince(), warboss(), rounds=4, seed=3)
        self.assertEqual(text, narrate_duel(prince(), warboss(), rounds=4, seed=3))
        self.assertIn("=== Round 1 ===", text)
        self.assertIn("Result:", text)

    def test_identically_named_fighters_are_told_apart(self):
        text = narrate_duel(warboss(), warboss(), rounds=1, seed=1)
        self.assertIn("Grimgor (A)", text)
        self.assertIn("Grimgor (B)", text)


class TestCharacterStore(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = Path(self.dir.name) / "sub" / "chars.json"

    def tearDown(self):
        self.dir.cleanup()

    def test_saved_characters_survive_a_reload(self):
        CharacterStore(self.path).save(warboss(optional_rules=["Frenzy"]))
        store = CharacterStore(self.path)
        self.assertEqual(store.names(), ["Grimgor"])
        self.assertEqual(store.get("Grimgor").optional_rules, ["Frenzy"])

    def test_saving_the_same_name_replaces(self):
        store = CharacterStore(self.path)
        store.save(warboss())
        store.save(warboss(weapon="Hand Weapon"))
        self.assertEqual(CharacterStore(self.path).get("Grimgor").weapon, "Hand Weapon")

    def test_illegal_or_unnamed_characters_are_not_saved(self):
        store = CharacterStore(self.path)
        for spec in (warboss(armour="Plate Armor"), warboss(name="  ")):
            with self.assertRaises(ValueError):
                store.save(spec)
        self.assertFalse(self.path.exists())

    def test_delete(self):
        store = CharacterStore(self.path)
        store.save(warboss())
        store.delete("Grimgor")
        self.assertEqual(CharacterStore(self.path).names(), [])


if __name__ == "__main__":
    unittest.main()
