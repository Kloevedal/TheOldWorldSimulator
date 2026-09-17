"""Rosters and rules for the four factions added most recently.

Statlines are pinned against https://tow.whfb.app/army/<slug>, in the order the
profile dicts use: M WS BS S T I W A Ld.
"""

from __future__ import annotations

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dice
from character_model import Character
from combat_simulations import (
    RollToHit,
    RollToWound,
    Wound,
    apply_extra_attacks,
    resolve_strike,
    test_primal_fury,
)
from faction_profiles import FactionProfiles, resolve_faction, resolve_profile

_ = None


def fighter(name="Fighter", **overrides):
    stats = dict(
        Movement=4, WeaponSkill=4, BallisticSkill=3, Strength=4, Toughness=4,
        Initiative=4, Wounds=3, Attacks=2, Leadership=7, Race="Human",
        Weapon="Hand Weapon",
    )
    stats.update(overrides)
    return Character(name=name, **stats)


class RosterCase(unittest.TestCase):
    """Shared statline/points checks; subclasses supply the faction data."""

    FACTION = None
    EXPECTED = {}
    POINTS = {}

    def test_the_whole_roster_is_present(self):
        if self.FACTION is None:
            return
        from factions import FACTION_MODULES

        characters = next(m.CHARACTERS for m in FACTION_MODULES if m.FACTION == self.FACTION)
        self.assertEqual(set(characters), set(self.EXPECTED))

    def test_statlines_match_the_source(self):
        if self.FACTION is None:
            return
        for name, expected in self.EXPECTED.items():
            with self.subTest(profile=name):
                p = FactionProfiles[self.FACTION][name]["base_profile"]
                self.assertEqual(
                    (p["Movement"], p["WeaponSkill"], p["BallisticSkill"],
                     p["Strength"], p["Toughness"], p["Initiative"],
                     p["Wounds"], p["Attacks"], p["Leadership"]),
                    expected,
                )

    def test_points_match_the_source(self):
        if self.FACTION is None:
            return
        for name, points in self.POINTS.items():
            with self.subTest(profile=name):
                self.assertEqual(FactionProfiles[self.FACTION][name]["points"], points)


class TestBeastmen(RosterCase):
    FACTION = "Beastmen Brayherds"
    EXPECTED = {
        "Beastlord":                   (5, 6, 3, 5, 5, 5, 3, 4, 8),
        "Wargor":                      (5, 5, 3, 4, 5, 4, 2, 3, 7),
        "Doombull":                    (6, 6, 3, 6, 5, 5, 5, 5, 8),
        "Gorebull":                    (6, 5, 3, 5, 5, 4, 4, 4, 7),
        "Great Bray-Shaman":           (5, 5, 3, 4, 5, 4, 3, 2, 8),
        "Bray-Shaman":                 (5, 4, 3, 3, 4, 3, 2, 1, 7),
        "Warhoof":                     (8, 5, 3, 5, 4, 3, 3, 4, 7),
        "Ghorros Warhoof":             (8, 5, 3, 5, 4, 4, 3, 4, 8),
        "Kralmaw, the Prophet of Ruin": (5, 3, 3, 4, 5, 3, 4, 2, 8),
    }
    POINTS = {
        "Beastlord": 115, "Wargor": 55, "Doombull": 210, "Gorebull": 130,
        "Great Bray-Shaman": 150, "Bray-Shaman": 65, "Warhoof": 75,
        "Ghorros Warhoof": 155, "Kralmaw, the Prophet of Ruin": 245,
    }


class TestChaosDwarfs(RosterCase):
    FACTION = "Chaos Dwarfs"
    EXPECTED = {
        "Infernal Castellan":    (3, 6, 4, 5, 5, 3, 3, 4, 10),
        "Infernal Seneschal":    (3, 5, 4, 4, 5, 2, 2, 3, 9),
        "Sorcerer-Prophet":      (3, 5, 4, 4, 5, 2, 3, 3, 10),
        "Daemonsmith Sorcerer":  (3, 4, 4, 4, 4, 2, 2, 2, 9),
        "Bull Centaur Taur'ruk": (7, 5, 2, 5, 5, 4, 4, 4, 9),
        "Hobgoblin Khan":        (4, 5, 4, 4, 4, 5, 2, 3, 7),
    }
    POINTS = {
        "Infernal Castellan": 125, "Infernal Seneschal": 60,
        "Sorcerer-Prophet": 195, "Daemonsmith Sorcerer": 85,
        "Bull Centaur Taur'ruk": 145, "Hobgoblin Khan": 45,
    }


class TestDaemons(RosterCase):
    FACTION = "Daemons of Chaos"
    EXPECTED = {
        "Bloodthirster":               (8, 10, 5, 6, 6, 7, 6, 6, 9),
        "Keeper of Secrets":           (8, 7, 6, 6, 6, 7, 6, 6, 9),
        "Great Unclean One":           (5, 6, 3, 6, 7, 4, 7, 5, 9),
        "Lord of Change":              (6, 6, 6, 6, 6, 6, 6, 4, 9),
        "Daemon Prince":               (6, 7, 5, 6, 5, 7, 4, 5, 9),
        "Daemonic Herald of Khorne":   (5, 7, 4, 5, 4, 6, 2, 3, 8),
        "Daemonic Herald of Nurgle":   (4, 5, 5, 5, 5, 4, 2, 3, 8),
        "Daemonic Herald of Slaanesh": (6, 6, 4, 4, 3, 6, 2, 3, 8),
        "Daemonic Herald of Tzeentch": (4, 3, 4, 3, 3, 3, 2, 2, 8),
    }
    POINTS = {
        "Bloodthirster": 355, "Keeper of Secrets": 330,
        "Great Unclean One": 330, "Lord of Change": 310, "Daemon Prince": 210,
        "Daemonic Herald of Khorne": 80, "Daemonic Herald of Nurgle": 95,
        "Daemonic Herald of Slaanesh": 85, "Daemonic Herald of Tzeentch": 90,
    }


class TestDarkElves(RosterCase):
    FACTION = "Dark Elves"
    EXPECTED = {
        "Dreadlord":         (5, 7, 7, 4, 3, 6, 3, 4, 10),
        "Master":            (5, 6, 6, 4, 3, 5, 2, 3, 9),
        "Supreme Sorceress": (5, 4, 4, 3, 3, 5, 3, 2, 8),
        "Sorceress":         (5, 4, 4, 3, 3, 4, 2, 1, 8),
        "Khainite Assassin": (5, 8, 7, 4, 3, 7, 2, 3, 8),
        "Death Hag":         (5, 6, 6, 4, 3, 7, 2, 3, 8),
        "High Beastmaster":  (_, 7, 7, 4, 3, 5, 3, 3, 9),
    }
    POINTS = {
        "Dreadlord": 130, "Master": 70, "Supreme Sorceress": 150,
        "Sorceress": 75, "Khainite Assassin": 80, "Death Hag": 70,
        "High Beastmaster": 75,
    }


class TestDaemonicWard(unittest.TestCase):
    """Daemonic is a 5+ Ward against non-magical attacks only."""

    def herald(self):
        return Character(
            name="Herald", faction_type="Daemons of Chaos",
            profile_name="Herald of Khorne",
        )

    def test_it_wards_an_ordinary_attack(self):
        from special_rules import parse_ward

        self.assertEqual(parse_ward(self.herald().SpecialRules, is_magical=False), 5)

    def test_it_does_not_ward_a_magical_attack(self):
        from special_rules import parse_ward

        self.assertIsNone(parse_ward(self.herald().SpecialRules, is_magical=True))

    def test_a_magical_attacker_bypasses_it_in_resolution(self):
        from combat_simulations import StrikeResult

        herald = self.herald()
        with dice.scripted_dice([]):  # no ward dice should be rolled
            taken, _ = resolve_strike(
                herald, StrikeResult(unsaved=[Wound(4)], is_magical=True),
                verbose=False,
            )
        self.assertEqual(taken, 1)

    def test_infernal_favour_is_not_a_ward(self):
        from special_rules import parse_ward

        self.assertIsNone(parse_ward(["Infernal Favour (2)"]))

    def test_daemons_have_magical_attacks(self):
        ghost = fighter("Ghost", SpecialRules=["Ethereal"], Toughness=4)
        with dice.constant_dice(6):
            _w, _f, is_magical = RollToWound(self.herald(), ghost, 2, verbose=False)
        self.assertTrue(is_magical)


class TestBlackshardArmour(unittest.TestCase):
    def test_it_wards_only_flaming_attacks(self):
        from special_rules import parse_ward

        castellan = Character(
            name="C", faction_type="Chaos Dwarfs", profile_name="Infernal Castellan"
        )
        self.assertIsNone(parse_ward(castellan.SpecialRules))
        self.assertEqual(parse_ward(castellan.SpecialRules, is_flaming=True), 5)


class TestPrimalFury(unittest.TestCase):
    def beastlord(self):
        return Character(
            name="Beastlord", faction_type="Beastmen Brayherds",
            profile_name="Beastlord",
        )

    def test_a_passed_test_grants_the_reroll(self):
        with dice.scripted_dice([2, 3]):  # 5 vs Ld8
            furious, frenzied = test_primal_fury(self.beastlord(), verbose=False)
        self.assertTrue(furious)
        self.assertFalse(frenzied)

    def test_a_failed_test_grants_nothing(self):
        with dice.scripted_dice([6, 5]):  # 11 vs Ld8
            furious, frenzied = test_primal_fury(self.beastlord(), verbose=False)
        self.assertFalse(furious)

    def test_blood_rage_needs_a_natural_double(self):
        with dice.scripted_dice([3, 3]):
            furious, frenzied = test_primal_fury(self.beastlord(), verbose=False)
        self.assertTrue(furious)
        self.assertTrue(frenzied)

    def test_a_model_without_the_rule_never_tests(self):
        with dice.scripted_dice([]):  # no dice should be rolled
            self.assertEqual(test_primal_fury(fighter("Plain"), verbose=False),
                             (False, False))

    def test_frenzy_from_blood_rage_adds_an_attack(self):
        beastlord = self.beastlord()
        self.assertEqual(apply_extra_attacks(beastlord), 4)
        beastlord.blood_rage_frenzied = True
        self.assertEqual(apply_extra_attacks(beastlord), 5)


class TestMurderous(unittest.TestCase):
    def test_it_rerolls_to_wound_ones_with_a_hand_weapon(self):
        lord = Character(
            name="Dreadlord", faction_type="Dark Elves", profile_name="Dreadlord"
        )
        defender = fighter("D", Toughness=4)  # S4 vs T4 wounds on 4+
        with dice.scripted_dice([1, 5]):
            wounds, _, _ = RollToWound(lord, defender, 1, verbose=False)
        self.assertEqual(len(wounds), 1)

    def test_it_does_not_apply_to_a_great_weapon(self):
        from combat_simulations import has_murderous_hand_weapon

        lord = Character(
            name="Dreadlord", faction_type="Dark Elves",
            profile_name="Dreadlord", Weapon="Great Weapon",
        )
        self.assertFalse(has_murderous_hand_weapon(lord))


class TestHatredTargeting(unittest.TestCase):
    """Hatred (High Elves) must not fire at every elf."""

    def dreadlord(self):
        return Character(
            name="Dreadlord", faction_type="Dark Elves", profile_name="Dreadlord"
        )

    def test_it_hates_a_high_elf(self):
        foe = fighter("Foe", Race="High Elf", WeaponSkill=4)
        with dice.scripted_dice([1, 6] * 4):
            self.assertEqual(
                RollToHit(self.dreadlord(), foe, verbose=False, is_first_round=True), 4
            )

    def test_it_does_not_hate_a_dark_elf(self):
        foe = fighter("Foe", Race="Dark Elf", WeaponSkill=4)
        with dice.scripted_dice([1, 1, 1, 1]):  # no rerolls expected
            self.assertEqual(
                RollToHit(self.dreadlord(), foe, verbose=False, is_first_round=True), 0
            )


class TestNewFactionRegistration(unittest.TestCase):
    def test_every_army_on_the_site_is_registered(self):
        """tow.whfb.app lists 19 armies; each has a module."""
        self.assertEqual(len(FactionProfiles), 19)

    def test_new_aliases_resolve(self):
        for alias, expected in [
            ("Beastmen", "Beastmen Brayherds"),
            ("Dawi Zharr", "Chaos Dwarfs"),
            ("DoC", "Daemons of Chaos"),
            ("Druchii", "Dark Elves"),
        ]:
            with self.subTest(alias=alias):
                self.assertEqual(resolve_faction(alias), expected)

    def test_new_profile_aliases_resolve(self):
        self.assertEqual(
            resolve_profile("Beastmen Brayherds", "Ghorros"), "Ghorros Warhoof"
        )
        self.assertEqual(
            resolve_profile("Dark Elves", "Assassin"), "Khainite Assassin"
        )

    def test_every_faction_declares_its_army_rules(self):
        from factions import FACTION_MODULES

        for module in FACTION_MODULES:
            with self.subTest(faction=module.FACTION):
                rules = getattr(module, "FACTION_RULES", None)
                self.assertTrue(rules, "no FACTION_RULES")
                for name, entry in rules.items():
                    self.assertIn("status", entry)
                    self.assertIn(entry["status"],
                                  (None, "implemented", "partial"))
                    self.assertTrue(entry["text"].strip())


if __name__ == "__main__":
    unittest.main(verbosity=2)
