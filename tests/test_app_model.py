"""Tests for app_model, the display-free half of the desktop app."""

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app_model import (  # noqa: E402
    CHARACTER,
    exclusive_choices,
    purchasable_items,
    purchase_problem,
    spent,
    NO_ARMOUR_LABEL,
    UNIT,
    CharacterStore,
    FighterSpec,
    faction_names,
    gear_options,
    minimum_unit_size,
    narrate_duel,
    profile_entry,
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


def unit(profile, faction, **overrides):
    opts = gear_options(faction, profile)["defaults"]
    fields = dict(name=profile, faction=faction, profile=profile, weapon=opts["weapon"],
                  armour=opts["armour"], shield=opts["shield"], kind=UNIT,
                  models=20, frontage=5)
    fields.update(overrides)
    return FighterSpec(**fields)


def first_unit():
    faction = faction_names(UNIT)[0]
    return profile_names(faction, UNIT)[0], faction


class TestGearOptions(unittest.TestCase):
    def test_every_profile_builds_with_every_offered_weapon(self):
        # The app drops the shield when a two-handed weapon is chosen, so the
        # loadouts it can produce are exactly these.
        for kind in (CHARACTER, UNIT):
            for faction in faction_names(kind):
                for profile in profile_names(faction, kind):
                    opts = gear_options(faction, profile)
                    defaults = opts["defaults"]
                    self.assertIn(defaults["armour"], opts["armour"], profile)
                    self.assertIn(defaults["weapon"], opts["weapons"], profile)
                    for weapon in opts["weapons"]:
                        shield = defaults["shield"] and weapon not in opts["two_handed"]
                        with self.subTest(profile=profile, weapon=weapon):
                            FighterSpec(profile, faction, profile, weapon,
                                        defaults["armour"], shield, kind=kind).build()

    def test_the_default_loadout_never_pairs_a_shield_with_two_hands(self):
        for kind in (CHARACTER, UNIT):
            for faction in faction_names(kind):
                for profile in profile_names(faction, kind):
                    defaults = gear_options(faction, profile)["defaults"]
                    with self.subTest(profile=profile):
                        FighterSpec(profile, faction, profile, defaults["weapon"],
                                    defaults["armour"], defaults["shield"], kind=kind).build()

    def test_two_handed_weapons_are_flagged(self):
        opts = gear_options("High Elves", "Prince")
        self.assertIn("Great Weapon", opts["two_handed"])
        self.assertNotIn("Hand Weapon", opts["two_handed"])

    def test_characters_and_units_are_listed_separately(self):
        for faction in faction_names(UNIT):
            with self.subTest(faction=faction):
                characters = set(profile_names(faction, CHARACTER))
                units = set(profile_names(faction, UNIT))
                self.assertTrue(units)
                self.assertFalse(characters & units)
                for name in units:
                    self.assertIsNotNone(gear_options(faction, name)["unit"])
                for name in characters:
                    self.assertIsNone(gear_options(faction, name)["unit"])

    def test_unit_sizes_are_read_from_the_data(self):
        self.assertEqual(minimum_unit_size({"unit_size": "10+"}), 10)
        self.assertEqual(minimum_unit_size({"unit_size": "5-20"}), 5)
        self.assertEqual(minimum_unit_size({"unit_size": "not given"}), 1)
        self.assertEqual(minimum_unit_size({}), 1)
        name, faction = first_unit()
        self.assertGreaterEqual(minimum_unit_size(profile_entry(faction, name)), 1)

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


class TestExtras(unittest.TestCase):
    def test_marks_are_an_exclusive_choice_not_upgrades(self):
        opts = gear_options("Warriors of Chaos", "Chaos Lord")
        (group, choices, default), = opts["exclusive"]
        self.assertEqual(group, "Mark of Chaos")
        self.assertEqual(default, "Mark of Chaos Undivided")
        self.assertIn("Mark of Khorne", choices)
        self.assertFalse(any("Mark" in r for r in opts["optional_rules"]))

    def test_vows_are_an_exclusive_choice(self):
        (group, choices, default), = exclusive_choices("Kingdom of Bretonnia", "Baron")
        self.assertEqual((group, default), ("Chivalrous Vow", "The Knight's Vow"))
        self.assertIn("The Grail Vow", choices)

    def test_ability_group_labels_are_not_offered_as_upgrades(self):
        self.assertNotIn("Knightly Virtue", gear_options("Kingdom of Bretonnia", "Baron")["optional_rules"])
        self.assertEqual(gear_options("Orcs", "Orc Warboss")["optional_rules"], ["Frenzy", "Warpaint"])

    def test_the_shop_lists_only_what_the_character_may_buy(self):
        items = {i["name"]: i for i in purchasable_items("High Elves", "Prince")}
        self.assertIn("Sword of Might", items)
        self.assertIn("Blood of Caledor", items)
        self.assertNotIn("Runefang", items)
        self.assertNotIn("Chayal", items)
        self.assertEqual(purchasable_items("High Elves", "Korhil Lionmane"), [])

    def test_purchase_problems_are_reported_not_raised(self):
        self.assertIsNone(purchase_problem("High Elves", "Prince", ["Sword of Might"]))
        self.assertIn("not available", purchase_problem("High Elves", "Prince", ["Runefang"]))

    def test_spending_is_totalled_per_budget(self):
        self.assertEqual(spent(["Sword of Might", "Blood of Caledor"]),
                         {"Magic Items": 20, "Elven Honours": 15})

    def test_a_spec_with_items_and_a_mark_builds_and_round_trips(self):
        spec = FighterSpec("Lord", "Warriors of Chaos", "Chaos Lord", "Hand Weapon",
                           "Full Plate Armor", optional_rules=["Mark of Khorne"],
                           magic_items=["Chaos Runesword"])
        built = spec.build()
        self.assertEqual(built.Weapon, "Chaos Runesword")
        self.assertIn("Mark of Khorne", built.SpecialRules)
        self.assertNotIn("Mark of Chaos Undivided", built.SpecialRules)
        self.assertEqual(FighterSpec.from_dict(spec.to_dict()), spec)


class TestGuiModules(unittest.TestCase):
    """The GUI modules import cleanly; windows are only opened on request."""

    def test_modules_import(self):
        try:
            import tkinter  # noqa: F401
        except ImportError:
            self.skipTest("no tkinter")
        import simulator_app
        import ui_kit

        self.assertTrue(callable(simulator_app.main))
        self.assertTrue(ui_kit.SIDE_COLOURS)

    @unittest.skipUnless(os.environ.get("TOW_GUI_TESTS") == "1", "set TOW_GUI_TESTS=1 to open windows")
    def test_the_window_builds_and_fights(self):
        import tkinter as tk
        import simulator_app

        root = tk.Tk()
        try:
            app = simulator_app.SimulatorApp(root)
            app.run_mode.set("narrate")
            app.seed_var.set("1")
            app.run()
            self.assertIn("Round 1", app.log.text.get("1.0", "end"))
        finally:
            root.destroy()


class TestUnitMode(unittest.TestCase):
    def test_ranks_follow_models_and_frontage(self):
        name, faction = first_unit()
        self.assertEqual(unit(name, faction, models=20, frontage=5).ranks, 4)
        self.assertEqual(unit(name, faction, models=21, frontage=5).ranks, 5)
        self.assertEqual(unit(name, faction).formation(), "20 models, 5 wide, 4 rank(s)")
        self.assertEqual(prince().formation(), "")

    def test_an_empty_unit_is_rejected(self):
        name, faction = first_unit()
        for fields in (dict(models=0), dict(frontage=0)):
            with self.subTest(**fields), self.assertRaises(ValueError):
                unit(name, faction, **fields).build()

    def test_a_unit_cannot_fight_a_character(self):
        name, faction = first_unit()
        with self.assertRaises(ValueError):
            run_statistics(unit(name, faction), prince(), runs=1, rounds=1)
        with self.assertRaises(ValueError):
            narrate_duel(prince(), unit(name, faction), rounds=1)

    def test_unit_runs_carry_the_not_yet_simulated_note(self):
        name, faction = first_unit()
        a, b = unit(name, faction, name="Left"), unit(name, faction, name="Right")
        stats = run_statistics(a, b, runs=50, rounds=2, seed=1)
        self.assertEqual(stats.wins_a + stats.wins_b + stats.draws, 50)
        self.assertIn("not simulated yet", stats.summary())
        text = narrate_duel(a, b, rounds=2, seed=1)
        self.assertIn("not simulated yet", text)
        self.assertIn("20 models, 5 wide", text)

    def test_character_runs_have_no_unit_note(self):
        self.assertNotIn("not simulated yet", narrate_duel(prince(), warboss(), 1, seed=1))


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

    def test_units_and_characters_are_stored_apart(self):
        name, faction = first_unit()
        store = CharacterStore(self.path)
        store.save(warboss())
        store.save(unit(name, faction, name="Grimgor", models=30, frontage=6))
        reloaded = CharacterStore(self.path)
        self.assertEqual(reloaded.names(CHARACTER), ["Grimgor"])
        self.assertEqual(reloaded.names(UNIT), ["Grimgor"])
        self.assertEqual(reloaded.get("Grimgor", UNIT).models, 30)
        self.assertEqual(reloaded.get("Grimgor").kind, CHARACTER)
        reloaded.delete("Grimgor", UNIT)
        self.assertTrue(CharacterStore(self.path).contains("Grimgor"))
        self.assertFalse(CharacterStore(self.path).contains("Grimgor", UNIT))

    def test_files_saved_before_units_existed_load_as_characters(self):
        self.path.parent.mkdir(parents=True)
        legacy = warboss().to_dict()
        for key in ("kind", "models", "frontage"):
            legacy.pop(key)
        import json
        self.path.write_text(json.dumps([legacy]))
        self.assertEqual(CharacterStore(self.path).get("Grimgor").kind, CHARACTER)


if __name__ == "__main__":
    unittest.main()
