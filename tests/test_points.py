"""Points costs, gear summaries, the X (y) statline and the shop search."""

from __future__ import annotations

import unittest

from support import fighter

from app_model import (
    FighterSpec,
    choice_label,
    compare_stats,
    fighting_stats,
    item_matches,
    item_summary,
    option_price,
    points_breakdown,
    purchasable_items,
    total_points,
    weapon_summary,
)
from armor import get_armour_save
from magic_items import get_magic_item
from faction_profiles import FactionProfiles
from mounts import Mounts
from option_costs import OPTION_COSTS

# Priced on the site but not a melee choice the rosters offer: thrown weapons,
# and a great weapon only the Gor Herd's champion may take.
NOT_OFFERED = {("Beastmen Brayherds", "Gor Herd", "Great Weapon")}


def spec(faction, profile, weapon="Hand Weapon", armour="None", **kw):
    return FighterSpec(name=profile, faction=faction, profile=profile,
                       weapon=weapon, armour=armour, **kw)


class TestOptionCosts(unittest.TestCase):
    def test_every_priced_option_is_one_the_profile_offers(self):
        for faction, profiles in OPTION_COSTS.items():
            for profile, costs in profiles.items():
                offered = FactionProfiles[faction][profile]["equipment_options"]
                with self.subTest(faction=faction, profile=profile):
                    for weapon in costs.get("weapons", {}):
                        if weapon == "Throwing Spears" or (faction, profile, weapon) in NOT_OFFERED:
                            continue
                        self.assertIn(weapon, offered["weapons"])
                    for armour in costs.get("armour", {}):
                        self.assertIn(get_armour_save(armour),
                                      {get_armour_save(a) for a in offered["armor"]}, armour)
                    for mount in costs.get("mounts", {}):
                        self.assertIn(mount, Mounts)
                    if "shield" in costs:
                        self.assertTrue(offered["shield"], "priced shield not offered")

    def test_known_prices(self):
        self.assertEqual(option_price("High Elf Realms", "Prince", "weapons", "Great Weapon"), 4)
        self.assertEqual(option_price("High Elf Realms", "Prince", "armour", "Full Plate Armor"), 6)
        # "Plate Armor" in a roster is the same suit as the site's full plate.
        self.assertEqual(option_price("High Elf Realms", "Prince", "armour", "Plate Armor"), 6)
        self.assertEqual(option_price("High Elf Realms", "Prince", "mounts", "Griffon (High Elves)"), 130)
        self.assertEqual(option_price("High Elf Realms", "Prince", "shield", "Shield"), 2)
        self.assertEqual(option_price("Warriors of Chaos", "Chaos Lord", "rules", "Mark of Khorne"), 10)
        self.assertEqual(option_price("Kingdom of Bretonnia", "Baron", "rules", "The Grail Vow"), 20)

    def test_free_and_unknown_options_cost_nothing(self):
        self.assertEqual(option_price("High Elf Realms", "Prince", "weapons", "Hand Weapon"), 0)
        self.assertEqual(option_price("High Elf Realms", "Prince", "weapons", "Nonsense"), 0)
        self.assertEqual(option_price("Atlantis", "King", "weapons", "Great Weapon"), 0)

    def test_an_unpriced_mount_falls_back_to_its_own_points(self):
        self.assertEqual(option_price("High Elf Realms", "Prince", "mounts", "Barded Elven Steed"),
                         Mounts["Barded Elven Steed"]["points"])


class TestPointsBreakdown(unittest.TestCase):
    def test_a_bare_character_costs_its_profile(self):
        prince = spec("High Elf Realms", "Prince")
        self.assertEqual(points_breakdown(prince), [("Prince", 130)])

    def test_a_kitted_character_adds_every_priced_choice(self):
        prince = spec("High Elf Realms", "Prince", "Great Weapon", "Plate Armor",
                      mount="Griffon (High Elves)", magic_items=["Armour of Caledor"])
        self.assertEqual(points_breakdown(prince), [
            ("Prince", 130), ("Great Weapon", 4), ("Plate Armor", 6),
            ("Griffon (High Elves)", 130), ("Armour of Caledor", 35),
        ])
        self.assertEqual(total_points(prince), 305)

    def test_marks_and_vows_are_priced(self):
        lord = spec("Warriors of Chaos", "Chaos Lord", "Great Weapon", "Full Plate Armor",
                    optional_rules=["Mark of Khorne"], mount="Chaos Steed")
        self.assertEqual(total_points(lord), 195 + 4 + 16 + 10)

    def test_default_kit_is_free(self):
        # A Chaos Lord comes in full plate; wearing it costs nothing extra.
        lord = spec("Warriors of Chaos", "Chaos Lord", armour="Full Plate Armor")
        self.assertEqual(total_points(lord), 195)

    def test_a_shield_is_priced(self):
        baron = spec("Kingdom of Bretonnia", "Baron", armour="Heavy Armor", shield=True)
        self.assertIn(("Shield", 2), points_breakdown(baron))

    def test_a_fixed_mount_is_part_of_the_profile(self):
        entry = FactionProfiles["High Elf Realms"]["Dragon Mage"]
        mage = spec("High Elf Realms", "Dragon Mage", mount="Sun Dragon")
        self.assertEqual(points_breakdown(mage), [("Dragon Mage", entry["points"])])

    def test_a_unit_pays_per_model(self):
        troops = spec("Empire of Man", "State Troops", "Halberd", "Light Armor",
                      shield=True, kind="unit", models=20, frontage=5)
        self.assertEqual(points_breakdown(troops), [
            ("State Troops (20 x 5)", 100), ("Halberd (20 x 1)", 20), ("Shield (20 x 1)", 20),
        ])

    def test_magic_items_are_bought_once_for_a_unit(self):
        troops = spec("Empire of Man", "State Troops", kind="unit", models=10, frontage=5,
                      magic_items=["Sword of Might"])
        cost = get_magic_item("Sword of Might")["cost"]
        self.assertEqual(points_breakdown(troops)[1:], [("Sword of Might", cost)])


class TestGearSummaries(unittest.TestCase):
    def test_weapon_profiles(self):
        self.assertEqual(weapon_summary("Great Weapon"),
                         "S+2, AP -2; Strike Last, Armour Bane (1), Requires Two Hands")
        self.assertEqual(weapon_summary("Two Hand Weapons"),
                         "S; Extra Attacks (+1), Requires Two Hands")
        self.assertEqual(weapon_summary("Hand Weapon"), "S")
        self.assertEqual(weapon_summary("Not a weapon"), "")
        # The engine stores the Lance's AP as a magnitude; it still reads as -2.
        self.assertTrue(weapon_summary("Lance").startswith("S+2, AP -2"))

    def test_item_summaries(self):
        self.assertEqual(item_summary("Armour of Caledor"), "Full Plate Armor (4+) | Ward save (5+)")
        self.assertIn("Killing Blow", item_summary("Headsman's Axe"))
        self.assertIn("WS+1", item_summary("Blood of Caledor"))
        self.assertIn("unlocks Sword of Hoeth", item_summary("Warden of Saphery"))
        self.assertEqual(item_summary("Opal Amulet"), "")  # single use, not modelled

    def test_picker_labels_carry_price_and_profile(self):
        self.assertEqual(choice_label("High Elf Realms", "Prince", "weapons", "Great Weapon"),
                         "Great Weapon · +4 pts · S+2, AP -2")
        self.assertEqual(choice_label("Empire of Man", "State Troops", "weapons", "Halberd"),
                         "Halberd · +1 pts/model · S+1, AP -1")
        self.assertEqual(choice_label("High Elf Realms", "Prince", "armour", "Plate Armor"),
                         "Plate Armor · +6 pts · 4+ save")
        self.assertEqual(choice_label("High Elf Realms", "Prince", "weapons", "Hand Weapon"),
                         "Hand Weapon")

    def test_shop_entries_carry_their_summary(self):
        items = {i["name"]: i for i in purchasable_items("High Elf Realms", "Prince")}
        self.assertEqual(items["Armour of Caledor"]["summary"], item_summary("Armour of Caledor"))


class TestStatComparison(unittest.TestCase):
    def test_a_bare_fighter_matches_its_profile(self):
        stats = compare_stats(spec("High Elf Realms", "Prince"))
        self.assertTrue(all(now == bare for now, bare in stats.values()), stats)

    def test_weapon_strength_shows_against_the_bare_profile(self):
        stats = compare_stats(spec("High Elf Realms", "Prince", "Great Weapon", "Plate Armor"))
        self.assertEqual(stats["S"], (6, 4))
        self.assertEqual(stats["WS"], (7, 7))

    def test_extra_attacks_from_weapon_and_mark(self):
        lord = spec("Warriors of Chaos", "Chaos Lord", "Two Hand Weapons", "Full Plate Armor",
                    optional_rules=["Mark of Khorne"])
        self.assertEqual(compare_stats(lord)["A"], (7, 5))

    def test_item_characteristic_changes_show(self):
        prince = spec("High Elf Realms", "Prince", magic_items=["Blood of Caledor"])
        self.assertEqual(compare_stats(prince)["WS"], (8, 7))

    def test_dice_attacks_read_as_text(self):
        model = fighter("A", Attacks=2, SpecialRules=["Extra Attacks (+D3)", "Frenzy"])
        self.assertEqual(fighting_stats(model)["A"], "3+D3")

    def test_reading_stats_leaves_the_fighter_unchanged(self):
        model = fighter("A", Weapon="Great Weapon", Strength=4)
        self.assertEqual(fighting_stats(model)["S"], 6)
        self.assertEqual(model.Strength, 4)


class TestItemSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = purchasable_items("High Elf Realms", "Prince")

    def found(self, query):
        return {i["name"] for i in self.items if item_matches(i, query)}

    def test_empty_query_matches_everything(self):
        self.assertEqual(len(self.found("  ")), len(self.items))

    def test_names_match(self):
        self.assertIn("Armour of Caledor", self.found("caledor"))

    def test_rules_match_as_well_as_names(self):
        killing = self.found("Killing Blow")
        # Headsman's Axe only lists Killing Blow in its weapon profile;
        # Warden of Saphery only in the rules it grants.
        self.assertTrue({"Headsman's Axe", "Warden of Saphery", "Armour of Stars"} <= killing)
        self.assertNotIn("Sword of Might", killing)

    def test_shorthand_rules_are_spelled_out(self):
        # Dragon Helm's data says "Ward6 (Flaming)".
        self.assertTrue({"Armour of Caledor", "Dragon Helm", "Talisman of Protection"}
                        <= self.found("ward save"))
        self.assertIn("Giant Blade", self.found("armour bane"))

    def test_every_word_must_match_somewhere(self):
        self.assertNotIn("Headsman's Axe", self.found("killing banana"))


if __name__ == "__main__":
    unittest.main()
