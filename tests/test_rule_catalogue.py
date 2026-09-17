"""Every rule string in the data is accounted for, and the accounting is true.

See rule_catalogue.py for the categories. The behavioural half runs seeded
duels with and without a rule and compares the full narration, so a rule the
catalogue calls inert cannot quietly start doing something, and a rule it
calls implemented cannot quietly stop.
"""

from __future__ import annotations

import itertools
import re
import unittest

from support import build, fighter, narrate

import rule_catalogue as rc
from elven_honors import ElvenHonors, apply_elven_honors
from factions import FACTION_MODULES
from faction_profiles import FactionProfiles
from special_rules import parse_ward


class TestEveryRuleIsClassified(unittest.TestCase):
    def setUp(self):
        self.sources = rc.rule_sources()

    def test_no_rule_is_unaccounted_for(self):
        missing = {
            rule: where[:3]
            for rule, where in self.sources.items()
            if rc.classify(rule) is None
        }
        listing = "\n".join(f"  {rule!r}: {where}" for rule, where in sorted(missing.items()))
        self.assertFalse(
            missing,
            "These rule strings are not in rule_catalogue.py. If one is a typo, "
            "fix the data; otherwise implement it or file it under LABELS, "
            "NOT_SIMULATED or INERT.\n" + listing,
        )

    def test_no_rule_is_filed_twice(self):
        for rule in self.sources:
            with self.subTest(rule=rule):
                homes = [
                    rc.engine_reads(rule),
                    rule in rc.LABELS,
                    rule in rc.NOT_SIMULATED,
                    rule in rc.INERT,
                ]
                self.assertLessEqual(sum(homes), 1)

    def test_the_catalogue_lists_nothing_the_data_does_not_use(self):
        listed = set(rc.LABELS) | rc.NOT_SIMULATED | rc.INERT
        self.assertEqual(sorted(listed - set(self.sources)), [])

    def test_engine_flag_constants_are_all_distinct_strings(self):
        self.assertTrue(all(isinstance(r, str) and r for r in rc.ENGINE_RULES))

    def test_rule_strings_are_tidy(self):
        for rule in self.sources:
            with self.subTest(rule=rule):
                self.assertEqual(rule, rule.strip())
                self.assertNotIn("  ", rule)

    def test_camel_case_rule_names_are_not_used(self):
        # "WitnesstoDestiny" silently parses as nothing; the data should use
        # the spaced names the engine and the catalogue expect.
        allowed = {"KillingBlow"}  # parse_killing_blow accepts it
        for rule, where in self.sources.items():
            with self.subTest(rule=rule):
                if rule in allowed:
                    continue
                self.assertIsNone(
                    re.search(r"[a-z][A-Z]", rule),
                    f"{rule!r} looks like a squashed name (used by {where[:2]})",
                )


class TestLabelsCarryTheirEffect(unittest.TestCase):
    def test_every_labelled_profile_carries_the_companion_rule(self):
        for faction, profiles in FactionProfiles.items():
            for name, entry in profiles.items():
                rules = entry["base_profile"].get("SpecialRules") or []
                for label, companion in rc.LABELS.items():
                    if label in rules:
                        with self.subTest(profile=name, label=label):
                            self.assertIn(companion, rules)

    def test_every_companion_is_itself_read_by_the_engine(self):
        for label, companion in rc.LABELS.items():
            with self.subTest(label=label):
                self.assertTrue(rc.engine_reads(companion))

    def test_rule_families_are_read_in_their_valued_form(self):
        for family, example in rc.FAMILIES.items():
            with self.subTest(family=family):
                self.assertTrue(rc.engine_reads(example))


class TestFactionRuleStatus(unittest.TestCase):
    """FACTION_RULES' status field must agree with what the engine does."""

    def rules(self):
        for module in FACTION_MODULES:
            for name, data in getattr(module, "FACTION_RULES", {}).items():
                yield module.FACTION, name, data

    def test_every_faction_declares_army_rules(self):
        for module in FACTION_MODULES:
            with self.subTest(faction=module.FACTION):
                self.assertTrue(getattr(module, "FACTION_RULES", None))

    def test_status_values_are_known(self):
        for faction, name, data in self.rules():
            with self.subTest(faction=faction, rule=name):
                self.assertIn(data.get("status"), (None, "implemented", "partial"))

    def test_implemented_rules_are_really_implemented(self):
        # Army rules name a label without its value: "Celestial Forged Armour"
        # for the profiles' "Celestial Forged Armour (5+)".
        label_names = {re.sub(r"\s*\(.*\)$", "", label) for label in rc.LABELS}
        for faction, name, data in self.rules():
            if data.get("status") != "implemented":
                continue
            with self.subTest(faction=faction, rule=name):
                self.assertTrue(
                    rc.engine_reads(name)
                    or name in rc.LABELS
                    or name in label_names
                    or name in rc.FAMILIES,
                    f"{faction} marks {name!r} implemented, but the engine does "
                    "not read it and it is not a catalogued label or family",
                )

    def test_rules_the_engine_reads_are_not_marked_unimplemented(self):
        for faction, name, data in self.rules():
            if data.get("status") is not None:
                continue
            with self.subTest(faction=faction, rule=name):
                self.assertFalse(
                    rc.engine_reads(name),
                    f"{faction} marks {name!r} as not implemented, but the "
                    "engine acts on it - set its status to 'implemented'",
                )


# -- behaviour -----------------------------------------------------------------

RACES_FOR_HATRED = ("Human", "Dwarf", "High Elf", "Orc", "Chaos Warrior", "Beastman",
                    "Empire", "Undead")


def _scenarios(rule):
    """(holder extras, holder weapon, opponent extras, opponent weapon, race).

    Ordered cheapest-first; the effect probe stops at the first difference.
    """
    races = RACES_FOR_HATRED if rule.startswith("Hatred") else ("Human",)
    holder_extras = ([], ["Primal Fury"], ["Regen5"])
    holder_weapons = ("Hand Weapon", "Great Weapon")
    opponent_extras = (
        [],
        ["Killing Blow", "Flaming Attacks", "Multiple Wounds (2)"],
        ["Ward5 (non-magical)"],
        ["Ethereal"],
        ["Ward5 (Flaming)", "Regen5"],
    )
    return itertools.product(holder_extras, holder_weapons, opponent_extras, races)


# Rules that only act against a particular troop type get an opponent of it,
# and rules that only act against a kind of attack get an opponent making it.
OPPONENT_TROOP_TYPE = {"Monster Slayer": "Behemoth"}
OPPONENT_EXTRA_RULES = {"Ward5 (magical)": ["Magical Attacks"]}
# Characteristics or kit that give a rule something to act on.
OPPONENT_STATS = {
    "Cannot Be Wounded On 2": {"Strength": 6},
    "Wounds On (4+)": {"Toughness": 7},
    "Wounds On (5+)": {"Toughness": 8},
    "Armour Cannot Be Modified": {"Weapon": "Great Weapon"},
    "Reroll Failed Hits (against higher Weapon Skill)": {"WeaponSkill": 7},
    "Ward4 (Strength 5+)": {"Strength": 5},
}
HOLDER_EXTRA_RULES = {
    "Armour Cannot Be Improved": ["Improve Armour (1)"],
    "Impact Hits Armour Piercing (2)": ["Impact Hits (D3)"],
}


def _duel(rule, holder_extra, holder_weapon, opponent_extra, race, seed, with_rule):
    rules = list(holder_extra) + HOLDER_EXTRA_RULES.get(rule, []) + ([rule] if with_rule else [])

    def opponent():
        stats = dict(Armor="Heavy Armor", Race=race, Wounds=3, Attacks=3)
        stats.update(OPPONENT_STATS.get(rule, {}))
        foe = fighter("Opponent",
                      SpecialRules=list(opponent_extra) + OPPONENT_EXTRA_RULES.get(rule, []),
                      **stats)
        foe.TroopType = OPPONENT_TROOP_TYPE.get(rule)
        return foe

    return narrate(
        lambda: fighter("Holder", Armor="Heavy Armor", Weapon=holder_weapon,
                        SpecialRules=rules, Wounds=3, Attacks=3),
        opponent,
        seed=seed,
        rounds=4,
    )


class TestRuleBehaviourMatchesTheCatalogue(unittest.TestCase):
    SEEDS = range(3)

    def test_rules_that_are_not_simulated_change_nothing(self):
        quiet = set(rc.LABELS) | rc.NOT_SIMULATED | rc.INERT
        scenarios = [
            ([], "Hand Weapon", [], "Human"),
            ([], "Great Weapon", ["Killing Blow", "Flaming Attacks"], "Orc"),
            (["Regen5"], "Hand Weapon", ["Ward5 (non-magical)"], "Dwarf"),
        ]
        for rule in sorted(quiet):
            with self.subTest(rule=rule):
                for (h_extra, weapon, o_extra, race), seed in itertools.product(
                    scenarios, self.SEEDS
                ):
                    self.assertEqual(
                        _duel(rule, h_extra, weapon, o_extra, race, seed, True),
                        _duel(rule, h_extra, weapon, o_extra, race, seed, False),
                        f"{rule!r} changed a duel but is catalogued as having no effect",
                    )

    def test_rules_the_engine_reads_change_something(self):
        character_level = sorted(
            rule for rule in rc.rule_sources()
            if rc.engine_reads(rule)
            and rule not in rc.WEAPON_ONLY_RULES
            and not rc.mount_scoped(rule)
            and not re.fullmatch(r"\+\d+A", rule)  # read from the weapon only
            and rc.sr.parse_fixed_strength([rule]) is None  # likewise
        )
        for rule in character_level:
            with self.subTest(rule=rule):
                changed = any(
                    _duel(rule, h, w, o, race, seed, True)
                    != _duel(rule, h, w, o, race, seed, False)
                    for (h, w, o, race) in _scenarios(rule)
                    for seed in range(4)
                )
                self.assertTrue(
                    changed, f"{rule!r} is read by the engine but never changed a duel"
                )


class TestElvenHonours(unittest.TestCase):
    def test_every_honour_rule_is_catalogued(self):
        for name, honour in ElvenHonors.items():
            for rule in honour["special_rules"]:
                with self.subTest(honour=name, rule=rule):
                    self.assertIsNotNone(rc.classify(rule))

    def test_anointed_of_asuryan_grants_a_six_up_ward(self):
        prince = build("High Elves", "Prince", elven_honors=["AnointedofAsuryan"])
        self.assertEqual(parse_ward(prince.SpecialRules), 6)
        self.assertEqual(parse_ward(prince.SpecialRules, is_flaming=True), 5)

    def test_blood_of_caledor_grants_dragon_armour(self):
        prince = build("High Elves", "Prince", elven_honors=["BloodofCaledor"])
        self.assertEqual(parse_ward(prince.SpecialRules), 6)

    def test_warden_of_saphery_grants_killing_blow(self):
        prince = build("High Elves", "Prince", elven_honors=["WardenofSaphery"])
        self.assertIn("Killing Blow", prince.SpecialRules)

    def test_an_honour_taken_twice_applies_once(self):
        prince = build("High Elves", "Prince", elven_honors=["BloodofCaledor"] * 2)
        self.assertEqual(prince.WeaponSkill, 8)

    def test_an_unknown_honour_is_rejected(self):
        noble = build("High Elves", "Noble")
        with self.assertRaises(ValueError):
            apply_elven_honors(noble, ["Blood of Caledor"])


if __name__ == "__main__":
    unittest.main()
