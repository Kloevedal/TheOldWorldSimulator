"""Rosters and rules for the ten factions transcribed from the site's page data.

Statlines are pinned against https://tow.whfb.app/unit/<slug>, in the order the
profile dicts use: M WS BS S T I W A Ld. `_` marks a '-' on the site.
"""

from __future__ import annotations

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import dice
from character_model import Character
from combat_simulations import (
    RollToWound,
    StrikeResult,
    Wound,
    apply_weapon_stats,
    reset_weapon_stats,
    resolve_strike,
)
from faction_profiles import FactionProfiles, resolve_faction, resolve_profile
from special_rules import parse_multiple_wounds, parse_ward
from test_new_factions import RosterCase, fighter

_ = None


class TestGrandCathay(RosterCase):
    FACTION = 'Grand Cathay'
    EXPECTED = {
        'Miao Ying':                       (4, 7, 5, 4, 4, 7, 7, 4, 10),
        'Astromancer':                     (4, 3, 3, 3, 3, 3, 2, 1, 8),
        'Gate Keeper':                     (4, 6, 4, 4, 4, 4, 2, 2, 8),
        'Gate Master':                     (4, 7, 4, 4, 4, 4, 3, 3, 9),
        'Lord Magistrate':                 (4, 5, 4, 3, 3, 4, 3, 2, 9),
        'Shugengan General':               (_, 5, 3, 4, 5, 5, 6, 3, 8),
        'Shugengan Lord':                  (_, 6, 3, 4, 5, 6, 7, 4, 9),
        'Strategist':                      (4, 4, 4, 3, 3, 3, 2, 1, 9),
        'Supreme Astromancer':             (4, 3, 3, 3, 3, 3, 3, 2, 8),
    }
    POINTS = {
        'Miao Ying': 485,
        'Astromancer': 65,
        'Gate Keeper': 45,
        'Gate Master': 80,
        'Lord Magistrate': 65,
        'Shugengan General': 145,
        'Shugengan Lord': 220,
        'Strategist': 40,
        'Supreme Astromancer': 125,
    }


class TestKingdomOfBretonnia(RosterCase):
    FACTION = 'Kingdom of Bretonnia'
    EXPECTED = {
        'Lady Élisse Duchaard':            (_, 4, 3, 3, 4, 3, 5, 2, 8),
        'Sir Cecil Gastonne':              (4, 7, 3, 4, 4, 5, 3, 4, 9),
        'The Green Knight':                (_, 7, 3, 4, 4, 6, 4, 4, 9),
        'Baron':                           (4, 6, 3, 4, 4, 5, 3, 4, 9),
        'Damsel':                          (4, 3, 3, 3, 3, 3, 2, 1, 7),
        'Duke':                            (4, 7, 3, 5, 4, 5, 4, 5, 9),
        'Outcast Wizard':                  (4, 3, 3, 3, 3, 3, 2, 1, 7),
        'Paladin':                         (4, 6, 3, 4, 4, 4, 2, 3, 8),
        'Prophetess':                      (4, 4, 3, 3, 3, 3, 3, 2, 8),
        'Sergeant-at-Arms':                (4, 4, 2, 4, 3, 4, 2, 2, 7),
    }
    POINTS = {
        'Lady Élisse Duchaard': 225,
        'Sir Cecil Gastonne': 165,
        'The Green Knight': 275,
        'Baron': 100,
        'Damsel': 60,
        'Duke': 175,
        'Outcast Wizard': 45,
        'Paladin': 60,
        'Prophetess': 135,
        'Sergeant-at-Arms': 45,
    }


class TestLizardmen(RosterCase):
    FACTION = 'Lizardmen'
    EXPECTED = {
        'Saurus Oldblood':                 (4, 6, 0, 5, 5, 3, 3, 5, 8),
        'Saurus Scar-Veteran':             (4, 5, 0, 5, 5, 3, 2, 4, 8),
        'Skink Chief':                     (6, 4, 5, 4, 3, 6, 2, 3, 6),
        'Skink Priest':                    (6, 2, 3, 3, 2, 4, 2, 1, 6),
        'Slann Mage-Priest':               (2, 2, 3, 3, 4, 2, 5, 1, 9),
    }
    POINTS = {
        'Saurus Oldblood': 140,
        'Saurus Scar-Veteran': 90,
        'Skink Chief': 45,
        'Skink Priest': 60,
        'Slann Mage-Priest': 285,
    }


class TestOgreKingdoms(RosterCase):
    FACTION = 'Ogre Kingdoms'
    EXPECTED = {
        'Bruiser':                         (6, 5, 3, 5, 5, 4, 4, 4, 8),
        'Butcher':                         (6, 3, 2, 4, 5, 2, 4, 3, 7),
        'Firebelly':                       (6, 3, 2, 4, 5, 2, 4, 3, 7),
        'Hunter':                          (6, 5, 4, 5, 5, 3, 4, 4, 9),
        'Slaughtermaster':                 (6, 4, 3, 4, 5, 3, 5, 4, 8),
        'Tyrant':                          (6, 6, 4, 5, 5, 5, 5, 5, 9),
    }
    POINTS = {
        'Bruiser': 110,
        'Butcher': 105,
        'Firebelly': 110,
        'Hunter': 115,
        'Slaughtermaster': 230,
        'Tyrant': 185,
    }


class TestRealmsOfMen(RosterCase):
    FACTION = 'Realms of Men'
    EXPECTED = {
        'Renegade Captain':                (4, 5, 4, 4, 4, 4, 2, 2, 7),
        'Renegade Prince':                 (4, 6, 4, 4, 4, 5, 3, 3, 8),
    }
    POINTS = {
        'Renegade Captain': 35,
        'Renegade Prince': 75,
    }


class TestRegimentsOfRenown(RosterCase):
    FACTION = 'Regiments of Renown'
    EXPECTED = {
        "Prince Ulther's Dragon Company":  (3, 5, 5, 4, 5, 2, 2, 3, 10),
    }
    POINTS = {
        "Prince Ulther's Dragon Company": 115,
    }


class TestSkaven(RosterCase):
    FACTION = 'Skaven'
    EXPECTED = {
        'Grey Seer':                       (5, 3, 3, 3, 4, 5, 3, 2, 7),
        'Master Assassin':                 (6, 8, 7, 4, 4, 8, 2, 3, 7),
        'Plague Priest':                   (5, 5, 3, 4, 5, 5, 2, 3, 6),
        'Skaven Chieftain':                (5, 5, 4, 4, 4, 6, 2, 3, 6),
        'Skaven Warlord':                  (5, 6, 4, 4, 4, 7, 3, 4, 7),
        'Warlock Engineer':                (5, 3, 3, 3, 3, 4, 2, 2, 5),
    }
    POINTS = {
        'Grey Seer': 185,
        'Master Assassin': 90,
        'Plague Priest': 60,
        'Skaven Chieftain': 45,
        'Skaven Warlord': 90,
        'Warlock Engineer': 35,
    }


class TestTombKingsOfKhemri(RosterCase):
    FACTION = 'Tomb Kings of Khemri'
    EXPECTED = {
        'Nekaph':                          (4, 5, 3, 4, 4, 4, 2, 3, 8),
        'Prince Apophas':                  (4, 4, 3, 4, 3, 1, 4, 5, 8),
        'Settra the Imperishable':         (_, 7, 3, 6, 5, 3, 8, 5, 10),
        'Arch Necrotect':                  (4, 4, 3, 4, 4, 3, 3, 3, 8),
        'High Priest':                     (4, 3, 3, 3, 4, 2, 3, 2, 8),
        'Mortuary Priest':                 (4, 3, 3, 3, 3, 2, 2, 1, 7),
        'Necrotect':                       (4, 3, 3, 4, 4, 3, 2, 2, 7),
        'Royal Herald':                    (4, 4, 3, 4, 4, 3, 2, 3, 8),
        'Tomb King':                       (4, 6, 3, 5, 5, 4, 4, 4, 10),
        'Tomb Prince':                     (4, 5, 3, 4, 5, 3, 3, 3, 9),
    }
    POINTS = {
        'Nekaph': 120,
        'Prince Apophas': 130,
        'Settra the Imperishable': 445,
        'Arch Necrotect': 90,
        'High Priest': 140,
        'Mortuary Priest': 55,
        'Necrotect': 55,
        'Royal Herald': 60,
        'Tomb King': 160,
        'Tomb Prince': 90,
    }


class TestVampireCounts(RosterCase):
    FACTION = 'Vampire Counts'
    EXPECTED = {
        'Cairn Wraith':                    (6, 4, 0, 3, 3, 2, 3, 2, 6),
        'Master Necromancer':              (4, 3, 3, 3, 4, 3, 3, 2, 8),
        'Necromantic Acolyte':             (4, 3, 3, 3, 3, 3, 2, 1, 7),
        'Strigoi Ghoul King':              (6, 6, 3, 5, 5, 7, 3, 5, 8),
        'Tomb Banshee':                    (6, 3, 0, 3, 3, 3, 2, 1, 6),
        'Vampire Count':                   (6, 7, 5, 5, 5, 6, 3, 4, 8),
        'Vampire Thrall':                  (6, 6, 4, 5, 4, 5, 2, 3, 7),
        'Wight King':                      (4, 5, 0, 5, 5, 4, 3, 3, 9),
        'Wight Lord':                      (4, 4, 0, 4, 5, 4, 2, 2, 8),
    }
    POINTS = {
        'Cairn Wraith': 50,
        'Master Necromancer': 130,
        'Necromantic Acolyte': 60,
        'Strigoi Ghoul King': 145,
        'Tomb Banshee': 90,
        'Vampire Count': 160,
        'Vampire Thrall': 75,
        'Wight King': 85,
        'Wight Lord': 40,
    }


class TestWoodElfRealms(RosterCase):
    FACTION = 'Wood Elf Realms'
    EXPECTED = {
        'Araloth, Lord of Talsyn':         (5, 8, 7, 4, 3, 8, 3, 4, 10),
        'Orion, the King in the Woods':    (9, 8, 6, 5, 6, 8, 5, 5, 10),
        'Branchwraith':                    (6, 6, 6, 4, 4, 6, 2, 2, 8),
        'Glade Captain':                   (5, 6, 6, 4, 3, 5, 2, 3, 9),
        'Glade Lord':                      (5, 7, 7, 4, 3, 6, 3, 4, 10),
        'Shadowdancer':                    (5, 8, 6, 4, 3, 7, 2, 3, 8),
        'Spellsinger':                     (5, 4, 4, 3, 3, 4, 2, 1, 8),
        'Spellweaver':                     (5, 4, 4, 3, 3, 4, 3, 2, 8),
        'Treeman Ancient':                 (5, 5, 5, 5, 6, 2, 6, 3, 10),
        'Warden of Talsyn':                (5, 7, 4, 4, 3, 6, 3, 4, 9),
        'Waystalker':                      (5, 6, 7, 4, 3, 5, 2, 2, 8),
    }
    POINTS = {
        'Araloth, Lord of Talsyn': 150,
        'Orion, the King in the Woods': 405,
        'Branchwraith': 80,
        'Glade Captain': 70,
        'Glade Lord': 135,
        'Shadowdancer': 85,
        'Spellsinger': 80,
        'Spellweaver': 155,
        'Treeman Ancient': 265,
        'Warden of Talsyn': 125,
        'Waystalker': 85,
    }


def build(faction, profile, **kwargs):
    return Character(name=profile, faction_type=faction, profile_name=profile, **kwargs)


class TestRegistration(unittest.TestCase):
    def test_aliases_resolve(self):
        for alias, expected in [
            ("Bretonnia", "Kingdom of Bretonnia"),
            ("Cathay", "Grand Cathay"),
            ("Seraphon", "Lizardmen"),
            ("Ogres", "Ogre Kingdoms"),
            ("Renegades", "Realms of Men"),
            ("Dogs of War", "Regiments of Renown"),
            ("Ratmen", "Skaven"),
            ("TK", "Tomb Kings of Khemri"),
            ("VC", "Vampire Counts"),
            ("Asrai", "Wood Elf Realms"),
        ]:
            with self.subTest(alias=alias):
                self.assertEqual(resolve_faction(alias), expected)

    def test_profile_aliases_resolve(self):
        self.assertEqual(resolve_profile("Tomb Kings of Khemri", "Settra"),
                         "Settra the Imperishable")
        self.assertEqual(resolve_profile("Kingdom of Bretonnia", "Lady Elisse Duchaard"),
                         "Lady Élisse Duchaard")
        self.assertEqual(resolve_profile("Regiments of Renown", "Ulther"),
                         "Prince Ulther's Dragon Company")

    def test_rules_with_an_engine_effect_are_marked(self):
        from factions import skaven, tomb_kings_of_khemri, wood_elf_realms

        self.assertEqual(skaven.FACTION_RULES["Warpstone Weapons"]["status"], "implemented")
        self.assertEqual(tomb_kings_of_khemri.FACTION_RULES["Khopesh"]["status"], "implemented")
        self.assertIsNone(wood_elf_realms.FACTION_RULES["Tree Whack"]["status"])


class TestNewWards(unittest.TestCase):
    def test_named_ward_rules_carry_a_parseable_ward(self):
        for faction, profile, target in [
            ("Lizardmen", "Slann Mage-Priest", 5),         # Arcane Shield
            ("Kingdom of Bretonnia", "The Green Knight", 5),  # Blessed Knight
            ("Wood Elf Realms", "Araloth, Lord of Talsyn", 5),  # Favour of the Goddess
            ("Grand Cathay", "Miao Ying", 5),              # Celestial Forged Armour
        ]:
            with self.subTest(profile=profile):
                self.assertEqual(parse_ward(build(faction, profile).SpecialRules), target)

    def test_blessings_of_the_volcano_god_only_wards_flaming(self):
        butcher = build("Ogre Kingdoms", "Firebelly")
        self.assertIsNone(parse_ward(butcher.SpecialRules))
        self.assertEqual(parse_ward(butcher.SpecialRules, is_flaming=True), 4)

    def test_named_items_grant_their_wards(self):
        self.assertEqual(parse_ward(build("Tomb Kings of Khemri", "Settra").SpecialRules), 5)
        self.assertEqual(parse_ward(build("Wood Elf Realms", "Orion").SpecialRules), 5)

    def test_dragonhide_cloak(self):
        from combat_simulations import is_killing_blow_target

        cecil = build("Kingdom of Bretonnia", "Sir Cecil Gastonne")
        self.assertFalse(is_killing_blow_target(cecil))
        # Against ordinary attacks he has only the Blessings of the Lady.
        self.assertEqual(parse_ward(cecil.SpecialRules), 6)
        self.assertEqual(parse_ward(cecil.SpecialRules, is_flaming=True), 3)


class TestHandWeaponRules(unittest.TestCase):
    """Khopesh, Obsidian Blades and Warpstone Weapons: AP -1 on a plain hand weapon."""

    def ap_with(self, character):
        apply_weapon_stats(character, is_first_round=False, verbose=False)
        try:
            return character.ArmourPiercing
        finally:
            reset_weapon_stats(character)

    def test_each_rule_gives_a_hand_weapon_ap_minus_one(self):
        for faction, profile in [
            ("Tomb Kings of Khemri", "Tomb King"),
            ("Lizardmen", "Saurus Oldblood"),
            ("Skaven", "Skaven Warlord"),
        ]:
            with self.subTest(profile=profile):
                self.assertEqual(self.ap_with(build(faction, profile)), 1)

    def test_it_does_not_stack_onto_a_great_weapon(self):
        king = build("Tomb Kings of Khemri", "Tomb King", Weapon="Great Weapon")
        self.assertEqual(self.ap_with(king), 2)

    def test_warpstone_weapons_are_magical(self):
        warlord = build("Skaven", "Skaven Warlord")
        ghost = fighter("Ghost", SpecialRules=["Ethereal"], Toughness=3)
        with dice.constant_dice(6):
            wounds, _, is_magical = RollToWound(warlord, ghost, 1, verbose=False)
        self.assertTrue(is_magical)
        self.assertEqual(len(wounds), 1)

    def test_khopesh_is_not_magical(self):
        king = build("Tomb Kings of Khemri", "Tomb King")
        ghost = fighter("Ghost", SpecialRules=["Ethereal"], Toughness=3)
        with dice.constant_dice(6):
            wounds, _, _ = RollToWound(king, ghost, 1, verbose=False)
        self.assertEqual(wounds, [])


class TestDiceMultipleWounds(unittest.TestCase):
    def test_a_dice_value_is_parsed(self):
        self.assertEqual(parse_multiple_wounds(["Multiple Wounds (D3)"]), "D3")
        self.assertEqual(parse_multiple_wounds(["Multiple Wounds (2)"]), 2)
        self.assertEqual(parse_multiple_wounds(["Multiple Wounds (D3)", "Multiple Wounds (3)"]), 3)
        self.assertEqual(parse_multiple_wounds([]), 1)

    def test_roll_amount(self):
        with dice.scripted_dice([5, 2, 6]):
            self.assertEqual(dice.roll_amount("D3"), 3)
            self.assertEqual(dice.roll_amount("D3+1"), 2)
            self.assertEqual(dice.roll_amount("D6"), 6)
        self.assertEqual(dice.roll_amount(2), 2)

    def test_each_unsaved_wound_rolls_its_own_multiplier(self):
        target = fighter("Target", Wounds=10)
        result = StrikeResult(unsaved=[Wound(4), Wound(5)], multiple_wounds="D3")
        with dice.scripted_dice([6, 1]):  # D3 rolls: 3 and 1
            taken, slain = resolve_strike(target, result, verbose=False)
        self.assertEqual(taken, 4)
        self.assertFalse(slain)

    def test_the_cairn_wraiths_scythe_permits_no_armour_save(self):
        from combat_simulations import OneRoundMeleeCombat

        wraith = build("Vampire Counts", "Cairn Wraith")
        knight = fighter("Knight", Armor="Full Plate Armor", Shield=True, WeaponSkill=1)
        with dice.constant_dice(6):
            result = OneRoundMeleeCombat(wraith, knight, verbose=False)
        self.assertEqual(result.saves, 0)
        self.assertEqual(result.multiple_wounds, "D3")


class TestFlammable(unittest.TestCase):
    def test_a_flaming_attack_denies_regeneration(self):
        king = build("Tomb Kings of Khemri", "Tomb King")
        result = StrikeResult(unsaved=[Wound(4)], is_flaming=True)
        with dice.scripted_dice([]):  # no Regeneration roll is allowed
            taken, _ = resolve_strike(king, result, verbose=False)
        self.assertEqual(taken, 1)

    def test_an_ordinary_attack_still_allows_regeneration(self):
        king = build("Tomb Kings of Khemri", "Tomb King")
        with dice.scripted_dice([5]):
            taken, _ = resolve_strike(king, StrikeResult(unsaved=[Wound(4)]), verbose=False)
        self.assertEqual(taken, 0)

    def test_a_model_that_is_not_flammable_regenerates_against_fire(self):
        wight = build("Vampire Counts", "Wight King")
        with dice.scripted_dice([5]):
            taken, _ = resolve_strike(
                wight, StrikeResult(unsaved=[Wound(4)], is_flaming=True), verbose=False
            )
        self.assertEqual(taken, 0)


class TestMounts(unittest.TestCase):
    def test_every_referenced_mount_has_a_profile(self):
        import mounts

        self.assertEqual(mounts.missing_mounts(FactionProfiles), [])
        self.assertEqual(mounts.unverified_mounts(), [])

    def test_same_named_mounts_are_kept_apart(self):
        from mounts import Mounts

        bretonnian = Mounts["Warhorse (Bretonnia)"]
        renegade = Mounts["Warhorse (Realms of Men)"]
        self.assertIn("Fast Cavalry", bretonnian["SpecialRules"])
        self.assertNotIn("Fast Cavalry", renegade["SpecialRules"])
        self.assertEqual(Mounts["Skeletal Steed (Tomb Kings)"]["Movement"], 8)
        self.assertEqual(Mounts["Skeletal Steed (Vampire Counts)"]["Movement"], 7)

    def test_a_ridden_monster_records_its_bonus_to_the_rider(self):
        from mounts import Mounts

        self.assertEqual(Mounts["Carnosaur"]["Toughness"], "+1")
        self.assertEqual(Mounts["Carnosaur"]["Wounds"], "+4")

    def test_a_chariot_keeps_every_row(self):
        from mounts import Mounts

        names = [row["Name"] for row in Mounts["Skeleton Chariot"]["profiles"]]
        self.assertEqual(names, ["Chariot", "Skeletal Steed (x2)"])

    def test_the_sites_mislinked_cold_one_is_corrected(self):
        """The Saurus pages link "Cold One" to the Terradon page."""
        mounts = FactionProfiles["Lizardmen"]["Saurus Oldblood"]["mount_options"]["mounts"]
        self.assertEqual(mounts, ["Cold One (Lizardmen)", "Carnosaur"])


class TestCommonMagicItems(unittest.TestCase):
    """The 68 rulebook items listed on tow.whfb.app."""

    def test_every_common_item_is_recorded(self):
        from magic_items import MagicItemDict

        common = [k for k, v in MagicItemDict.items() if v.get("common")]
        # 67 new entries plus the Lore Familiar, which was already listed.
        self.assertEqual(len(common), 68)
        self.assertIn("cost", MagicItemDict["Lore Familiar"])

    def test_every_common_weapon_has_a_profile(self):
        from magic_items import MagicItemDict
        from weapons import find_weapon_key

        for name, entry in MagicItemDict.items():
            if entry.get("is_weapon") and entry.get("common"):
                with self.subTest(item=name):
                    self.assertIsNotNone(find_weapon_key(name))

    def test_armour_of_destiny_is_heavy_armour_with_a_ward(self):
        from magic_items import apply_magic_items

        wearer = fighter("W", Armor=None)
        self.assertEqual(apply_magic_items(wearer, ["Armour of Destiny"]), [])
        self.assertEqual(wearer.Armor, "Heavy Armor")
        self.assertEqual(parse_ward(wearer.SpecialRules), 4)

    def test_the_enchanted_shield_is_a_shield_that_wards_non_magical_attacks(self):
        from magic_items import apply_magic_items

        bearer = fighter("B")
        apply_magic_items(bearer, ["Enchanted Shield"])
        self.assertTrue(bearer.Shield)
        self.assertEqual(parse_ward(bearer.SpecialRules, is_magical=False), 6)
        self.assertIsNone(parse_ward(bearer.SpecialRules, is_magical=True))

    def test_the_dawnstone_rerolls_an_armour_save_of_one(self):
        from combat_simulations import RollArmorSave
        from magic_items import apply_magic_items

        attacker = fighter("A")
        bearer = fighter("B", Armor="Heavy Armor")
        apply_magic_items(bearer, ["Dawnstone"])
        with dice.scripted_dice([1, 5]):
            unsaved = RollArmorSave(attacker, bearer, [Wound(3)], verbose=False)
        self.assertEqual(unsaved, [])

    def test_an_ogre_blade_rolls_its_multiple_wounds(self):
        from combat_simulations import OneRoundMeleeCombat

        wielder = fighter("W", Weapon="Ogre Blade")
        with dice.constant_dice(6):
            result = OneRoundMeleeCombat(wielder, fighter("D"), verbose=False)
        self.assertEqual(result.multiple_wounds, "D3")
        self.assertTrue(result.is_magical)


class TestUnits(unittest.TestCase):
    """Regular units, read from the site's unit pages."""

    def unit(self, faction, name):
        return FactionProfiles[faction][name]

    def test_every_faction_but_regiments_of_renown_has_units(self):
        from factions import FACTION_MODULES

        counts = {m.FACTION: len(m.UNITS) for m in FACTION_MODULES}
        self.assertEqual(sum(counts.values()), 338)
        self.assertEqual(counts["Regiments of Renown"], 0)
        self.assertEqual(counts["Empire of Man"], 25)

    def test_statlines_units_fight_with(self):
        for faction, name, expected in [
            # (T, W, A): a war machine fights with its crew's T and W.
            ("Empire of Man", "Great Cannon", (3, 3, 3)),
            # A chariot's crew borrows the chariot's T and W.
            ("Orcs", "Orc Boar Chariot", (5, 4, 1)),
            ("High Elves", "White Lions of Chrace", (3, 1, 1)),
        ]:
            with self.subTest(unit=name):
                p = self.unit(faction, name)["base_profile"]
                self.assertEqual((p["Toughness"], p["Wounds"], p["Attacks"]), expected)

    def test_units_fight_with_their_special_weapon(self):
        self.assertEqual(self.unit("High Elves", "White Lions of Chrace")["base_profile"]["Weapon"],
                         "Chracian Great Blade")
        self.assertEqual(self.unit("Empire of Man", "Empire Greatswords")["base_profile"]["Weapon"],
                         "Great Weapon")

    def test_a_secondary_attack_is_never_the_default_weapon(self):
        trolls = self.unit("Orcs", "Common Troll Mob")
        self.assertEqual(trolls["base_profile"]["Weapon"], "Hand Weapon")
        self.assertIn("Troll Vomit", trolls["equipment_options"]["weapons"])

    def test_a_two_handed_default_sets_the_shield_aside(self):
        guard = self.unit("Lizardmen", "Temple Guard")
        self.assertEqual(guard["base_profile"]["Weapon"], "Halberd")
        self.assertFalse(guard["base_profile"]["Shield"])
        self.assertTrue(guard["equipment_options"]["shield"])

    def test_champions_and_sizes_are_recorded(self):
        greatswords = self.unit("Empire of Man", "Empire Greatswords")
        self.assertEqual(greatswords["champion"]["Name"], "Count's Champion")
        self.assertEqual(greatswords["champion"]["Attacks"], 2)
        self.assertEqual((greatswords["points"], greatswords["points_per"], greatswords["unit_size"]),
                         (11, "model", "5+"))

    def test_a_printed_armour_value_is_used(self):
        self.assertEqual(self.unit("Orcs", "Orc Boar Chariot")["base_profile"]["Armor"],
                         "Full Plate Armor")  # 4+
        self.assertEqual(self.unit("Warriors of Chaos", "Chaos Chariot")["base_profile"]["Armor"],
                         "Armour Value 3+")
        # Settra's page prints 4+ too.
        self.assertEqual(build("Tomb Kings of Khemri", "Settra").Armor, "Full Plate Armor")

    def test_a_cost_given_as_text_keeps_the_text(self):
        pack = self.unit("Lizardmen", "Razordon Pack")
        self.assertEqual(pack["points"], 5)
        self.assertIn("60 points per Razordon", pack["points_note"])

    def test_mount_only_monsters_are_not_units(self):
        self.assertNotIn("Carnosaur", FactionProfiles["Lizardmen"])
        self.assertNotIn("Star Dragon", FactionProfiles["High Elves"])

    def test_units_are_filed_as_units(self):
        self.assertEqual(self.unit("Skaven", "Clanrats")["base_profile"]["UnitCategory"], "Unit")


class TestKillingBlowRelatives(unittest.TestCase):
    def test_monster_slayer_slays_a_monster(self):
        slayer = fighter("Slayer", SpecialRules=["Monster Slayer"], Strength=5)
        monster = fighter("Monster", Toughness=5, Wounds=6)
        monster.TroopType = "Behemoth"
        with dice.scripted_dice([6]):
            wounds, _, _ = RollToWound(slayer, monster, 1, verbose=False)
        self.assertTrue(wounds[0].killing_blow)
        taken, slain = resolve_strike(monster, StrikeResult(unsaved=wounds), verbose=False)
        self.assertTrue(slain)

    def test_monster_slayer_does_nothing_to_infantry(self):
        slayer = fighter("Slayer", SpecialRules=["Monster Slayer"])
        with dice.scripted_dice([6]):
            wounds, _, _ = RollToWound(slayer, fighter("Man"), 1, verbose=False)
        self.assertFalse(wounds[0].killing_blow)

    def test_cleaving_blow_denies_armour_and_regeneration_but_does_not_slay(self):
        from combat_simulations import RollArmorSave

        swordmaster = fighter("S", SpecialRules=["Cleaving Blow"])
        knight = fighter("K", Armor="Full Plate Armor", Shield=True, Wounds=3,
                         SpecialRules=["Regen5"])
        with dice.scripted_dice([6]):
            wounds, _, _ = RollToWound(swordmaster, knight, 1, verbose=False)
        self.assertTrue(wounds[0].cleaving_blow)
        with dice.scripted_dice([]):  # no armour save and no Regeneration roll
            unsaved = RollArmorSave(swordmaster, knight, wounds, verbose=False)
            taken, slain = resolve_strike(knight, StrikeResult(unsaved=unsaved), verbose=False)
        self.assertEqual((taken, slain), (1, False))

    def test_cleaving_blow_does_not_affect_a_monster(self):
        monster = fighter("M")
        monster.TroopType = "Behemoth"
        with dice.scripted_dice([6]):
            wounds, _, _ = RollToWound(fighter("S", SpecialRules=["Cleaving Blow"]),
                                       monster, 1, verbose=False)
        self.assertFalse(wounds[0].cleaving_blow)


class TestUnitWeapons(unittest.TestCase):
    def test_a_weapon_with_its_own_strength_replaces_the_wielders(self):
        crew = fighter("Crew", Strength=3, Weapon="Warp Grinder")
        apply_weapon_stats(crew, verbose=False)
        try:
            self.assertEqual(crew.Strength, 5)
        finally:
            reset_weapon_stats(crew)
        self.assertEqual(crew.Strength, 3)

    def test_a_plaguesword_denies_regeneration(self):
        from combat_simulations import OneRoundMeleeCombat

        bearer = fighter("P", Weapon="Plaguesword")
        with dice.constant_dice(6):
            result = OneRoundMeleeCombat(bearer, fighter("D", Armor=None), verbose=False)
        self.assertTrue(result.denies_regeneration)
        troll = fighter("T", Wounds=5, SpecialRules=["Regen5"])
        with dice.scripted_dice([]):  # no Regeneration roll
            taken, _ = resolve_strike(
                troll, StrikeResult(unsaved=[Wound(4)], denies_regeneration=True), verbose=False
            )
        self.assertEqual(taken, 1)

    def test_accursed_weapons_are_magical_with_ap(self):
        from combat_simulations import has_ensorcelled_hand_weapon

        knight = build("Vampire Counts", "Blood Knights", Weapon="Hand Weapon")
        self.assertTrue(has_ensorcelled_hand_weapon(knight))

    def test_new_unit_wards(self):
        ironbreakers = build("Dwarfen Mountain Holds", "Ironbreakers")
        self.assertEqual(parse_ward(ironbreakers.SpecialRules, is_magical=False), 6)
        self.assertIsNone(parse_ward(ironbreakers.SpecialRules, is_magical=True))
        sisters = build("Wood Elf Realms", "Sisters of the Thorn")
        self.assertEqual(parse_ward(sisters.SpecialRules), 4)


class TestNamedCharacters(unittest.TestCase):
    def test_named_characters_default_to_their_signature_weapon(self):
        for faction, profile, weapon in [
            ("Grand Cathay", "Miao Ying", "Talons of the Storm"),
            ("Kingdom of Bretonnia", "Sir Cecil Gastonne", "Sorrow's End"),
            ("Kingdom of Bretonnia", "The Green Knight", "The Dolorous Blade"),
            ("Regiments of Renown", "Prince Ulther", "Dragonblade"),
            ("Tomb Kings of Khemri", "Nekaph", "The Flail of Conquered Kings"),
            ("Tomb Kings of Khemri", "Settra", "The Blessed Blade of Ptra"),
            ("Wood Elf Realms", "Araloth", "Spear of Talsyn"),
            ("Wood Elf Realms", "Orion", "The Spear of Kurnous"),
        ]:
            with self.subTest(profile=profile):
                self.assertEqual(build(faction, profile).Weapon, weapon)

    def test_nekaph_strikes_killing_blows_on_a_five_in_a_duel(self):
        nekaph = build("Tomb Kings of Khemri", "Nekaph")
        with dice.scripted_dice([5]):
            wounds, _, _ = RollToWound(nekaph, fighter("D", Toughness=3), 1, verbose=False)
        self.assertTrue(wounds[0].killing_blow)

    def test_settra_uses_his_chariots_wounds(self):
        self.assertEqual(build("Tomb Kings of Khemri", "Settra").Wounds, 8)

    def test_araloth_fights_with_spear_and_shield(self):
        araloth = build("Wood Elf Realms", "Araloth")
        self.assertTrue(araloth.Shield)


if __name__ == "__main__":
    unittest.main(verbosity=2)
