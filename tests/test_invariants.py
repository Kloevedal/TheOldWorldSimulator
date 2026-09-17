"""Properties that must hold for every profile, every loadout and every duel.

These are roster-wide sweeps rather than rule-by-rule checks, so a new faction
or weapon is covered the moment it is registered.
"""

from __future__ import annotations

import io
import itertools
import unittest
from contextlib import redirect_stdout

from support import FULL, all_profiles, build, full_only, legal_loadouts

import dice
from combat_simulations import combat_simulation
from faction_profiles import FactionProfiles

_PERSISTENT_STATS = ("Wounds", "Strength", "Initiative", "Weapon", "Armor", "Shield")


def _snapshot(character):
    return {stat: getattr(character, stat) for stat in _PERSISTENT_STATS}


class DuelInvariants(unittest.TestCase):
    def assertDuelIsSound(self, a, b, rounds=4):
        before_a, before_b = _snapshot(a), _snapshot(b)
        rules_a, rules_b = list(a.SpecialRules), list(b.SpecialRules)
        out = io.StringIO()
        with redirect_stdout(out):
            winner = combat_simulation(a, b, rounds=rounds, verbose=False)

        self.assertEqual(out.getvalue(), "", "a quiet duel printed something")
        self.assertIn(winner, (a, b, None))
        for fighter, before, rules in ((a, before_a, rules_a), (b, before_b, rules_b)):
            self.assertGreaterEqual(fighter.current_wounds, 0)
            self.assertLessEqual(fighter.current_wounds, fighter.Wounds)
            self.assertEqual(_snapshot(fighter), before, "a duel left stats modified")
            self.assertEqual(fighter.SpecialRules, rules, "a duel changed special rules")
            self.assertEqual(fighter.ArmourPiercing, 0)

        if winner is None:
            # A draw is either a double kill or equal wounds remaining.
            both_down = a.current_wounds == 0 and b.current_wounds == 0
            self.assertTrue(both_down or a.current_wounds == b.current_wounds)
        else:
            loser = b if winner is a else a
            self.assertGreater(winner.current_wounds, 0)
            self.assertLess(loser.current_wounds, winner.current_wounds + 1)
            if loser.current_wounds > 0:
                self.assertGreater(winner.current_wounds, loser.current_wounds)
        return winner


class TestEveryCharacter(DuelInvariants):
    KIND = "characters"

    def loadouts(self, faction, profile):
        return legal_loadouts(faction, profile)

    def test_every_legal_loadout_builds(self):
        for faction, profile in all_profiles(self.KIND):
            for weapon, armour, shield in self.loadouts(faction, profile):
                with self.subTest(profile=profile, weapon=weapon, armour=armour, shield=shield):
                    c = build(faction, profile, Weapon=weapon, Armor=armour or "", Shield=shield)
                    self.assertEqual(c.current_wounds, c.Wounds)
                    self.assertGreater(c.Wounds or 0, 0)

    def test_every_legal_loadout_fights_a_mirror_match(self):
        dice.seed(1)
        for faction, profile in all_profiles(self.KIND):
            for weapon, armour, shield in self.loadouts(faction, profile):
                with self.subTest(profile=profile, weapon=weapon, armour=armour, shield=shield):
                    kit = dict(Weapon=weapon, Armor=armour or "", Shield=shield)
                    self.assertDuelIsSound(
                        build(faction, profile, name="Left", **kit),
                        build(faction, profile, name="Right", **kit),
                    )

    def test_every_profile_survives_extreme_dice(self):
        for value in (1, 6):
            for faction, profile in all_profiles(self.KIND):
                with self.subTest(dice=value, profile=profile):
                    with dice.constant_dice(value):
                        self.assertDuelIsSound(
                            build(faction, profile, name="Left"),
                            build(faction, profile, name="Right"),
                        )

    def test_every_profile_fights_each_faction_sample(self):
        # One opponent per faction keeps the quick tier fast; the full tier
        # plays the whole round robin below.
        dice.seed(2)
        samples = {}
        for faction, profile in all_profiles("characters"):
            samples.setdefault(faction, profile)
        for faction, profile in all_profiles(self.KIND):
            for other_faction, other in samples.items():
                with self.subTest(a=profile, b=other):
                    self.assertDuelIsSound(
                        build(faction, profile, name="A"),
                        build(other_faction, other, name="B"),
                    )

    @full_only
    def test_full_round_robin(self):
        dice.seed(3)
        profiles = all_profiles(self.KIND)
        for (fa, pa), (fb, pb) in itertools.product(profiles, repeat=2):
            with self.subTest(a=pa, b=pb):
                self.assertDuelIsSound(build(fa, pa, name="A"), build(fb, pb, name="B"))


class TestEveryUnit(TestEveryCharacter):
    """The same sweeps for regular units, fought as single models."""

    KIND = "units"

    def loadouts(self, faction, profile):
        # Units have many kit combinations; the quick tier fights the default.
        options = list(legal_loadouts(faction, profile))
        return options if FULL else options[:1]

    @full_only
    def test_full_round_robin(self):
        # Every unit against every other would be ~114k fights; one character
        # and one unit per faction covers each matchup type in a fraction of it.
        dice.seed(3)
        opponents = {}
        for kind in ("characters", "units"):
            for faction, profile in all_profiles(kind):
                opponents.setdefault((kind, faction), profile)
        for fa, pa in all_profiles("units"):
            for (_, fb), pb in opponents.items():
                with self.subTest(a=pa, b=pb):
                    self.assertDuelIsSound(build(fa, pa, name="A"), build(fb, pb, name="B"))

    def test_unit_entries_are_well_formed(self):
        for faction, profile in all_profiles("units"):
            entry = FactionProfiles[faction][profile]
            with self.subTest(unit=profile):
                self.assertEqual(entry["base_profile"].get("UnitCategory"), "Unit")
                self.assertIn(entry.get("points_per"), ("model", "unit"))
                self.assertTrue(entry.get("unit_size"))
                if entry.get("points") is None:
                    self.assertTrue(entry.get("points_note"), "no points and no note")

    def test_no_name_is_both_a_character_and_a_unit(self):
        from factions import FACTION_MODULES

        for module in FACTION_MODULES:
            with self.subTest(faction=module.FACTION):
                self.assertFalse(set(module.CHARACTERS) & set(getattr(module, "UNITS", {})))

    def test_characters_are_not_filed_as_units(self):
        for faction, profile in all_profiles("characters"):
            category = FactionProfiles[faction][profile]["base_profile"].get("UnitCategory")
            with self.subTest(character=profile):
                self.assertIn(category, ("Character", "NamedCharacter"))


class TestReproducibility(unittest.TestCase):
    PAIRS = [
        (("High Elves", "Prince"), ("Orcs", "Black Orc Warboss")),
        (("Dwarfen Mountain Holds", "King"), ("Warriors of Chaos", "Chaos Lord")),
        (("Vampire Counts", "Vampire Count"), ("Empire of Man", "General of the Empire")),
    ]

    def _fight(self, pair, seed, reuse=None):
        (fa, pa), (fb, pb) = pair
        a, b = reuse or (build(fa, pa, name="A"), build(fb, pb, name="B"))
        dice.seed(seed)
        winner = combat_simulation(a, b, rounds=5, verbose=False)
        return (winner.name if winner else None, a.current_wounds, b.current_wounds)

    def test_the_same_seed_gives_the_same_duel(self):
        for pair in self.PAIRS:
            with self.subTest(pair=pair):
                for seed in range(20):
                    self.assertEqual(self._fight(pair, seed), self._fight(pair, seed))

    def test_fighters_can_be_reused_between_duels(self):
        # combat_simulation resets wounds, so a reused pair must fight exactly
        # as a freshly built one does.
        for pair in self.PAIRS:
            (fa, pa), (fb, pb) = pair
            a, b = build(fa, pa, name="A"), build(fb, pb, name="B")
            with self.subTest(pair=pair):
                for seed in range(20):
                    self.assertEqual(
                        self._fight(pair, seed, reuse=(a, b)), self._fight(pair, seed)
                    )

    def test_different_seeds_give_different_duels(self):
        results = {self._fight(self.PAIRS[0], seed) for seed in range(50)}
        self.assertGreater(len(results), 1)


class TestVerboseAndQuietAgree(unittest.TestCase):
    def test_narration_does_not_change_the_outcome(self):
        for seed in range(30 if not FULL else 300):
            outcomes = []
            for verbose in (False, True):
                a = build("Orcs", "Orc Warboss", name="A", SpecialRules=["Frenzy"])
                b = build("Beastmen Brayherds", "Beastlord", name="B")
                dice.seed(seed)
                with redirect_stdout(io.StringIO()):
                    winner = combat_simulation(a, b, rounds=4, verbose=verbose)
                outcomes.append((winner and winner.name, a.current_wounds, b.current_wounds))
            with self.subTest(seed=seed):
                self.assertEqual(outcomes[0], outcomes[1])


if __name__ == "__main__":
    unittest.main()
