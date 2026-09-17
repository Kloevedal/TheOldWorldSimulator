"""Mirror matches and seat order.

Two identical fighters striking simultaneously must win equally often, and
which fighter is passed first to combat_simulation must not matter. Both are
checked statistically, with a tolerance wide enough to never flake.
"""

from __future__ import annotations

import math
import unittest

from support import (
    FULL,
    SAMPLES_LARGE,
    StatisticalCase,
    all_profiles,
    build,
    fighter,
    tolerance,
    win_rates,
)

from combat_simulations import determine_strike_order

ARCHETYPES = {
    "plain": dict(),
    "great weapon": dict(Weapon="Great Weapon", Armor="Heavy Armor"),
    "killing blow and ward": dict(SpecialRules=["Killing Blow", "Ward5"], Armor="Light Armor"),
    "regeneration": dict(SpecialRules=["Regen5"], Toughness=5, Wounds=4),
    "frenzy and hatred": dict(SpecialRules=["Frenzy", "Hatred (all enemies)"]),
    "strike first": dict(SpecialRules=["Strike First"], Initiative=6),
    "multiple wounds": dict(SpecialRules=["Multiple Wounds (D3)"], Wounds=4),
    "flaming vs flammable": dict(SpecialRules=["Flaming Attacks", "Flammable", "Regen4"]),
    "magic vs daemonic": dict(SpecialRules=["Magical Attacks", "Ward5 (non-magical)"]),
    # Healing used to be applied mid-step, favouring whichever fighter was
    # passed second (Ogdruz Swampdigga mirrors went 37% / 49%).
    "wound stealing": dict(SpecialRules=["Wound Stealing"], Wounds=4, Attacks=3),
}

# Profiles whose mirror match once came out lopsided; always checked.
REGRESSION_MIRRORS = [("Orcs", "Ogdruz Swampdigga")]

# Asymmetric pairs for the seat-order check.
SEAT_PAIRS = [
    (("High Elves", "Prince"), ("Orcs", "Black Orc Warboss")),
    (("Dwarfen Mountain Holds", "Thane"), ("Beastmen Brayherds", "Wargor")),
    (("Dark Elves", "Dreadlord"), ("Warriors of Chaos", "Exalted Champion")),
    (("Skaven", "Warlord"), ("Lizardmen", "Saurus Oldblood")),
]


class TestMirrorMatches(StatisticalCase):
    def assertSymmetric(self, make_left, make_right, runs=SAMPLES_LARGE, rounds=4):
        left, right, _ = win_rates(make_left, make_right, runs, rounds=rounds)
        # Var(left - right) = (pL + pR - (pL - pR)^2) / n; use four sigma.
        band = 4 * math.sqrt(max(left + right, 0.02) / runs)
        self.assertAlmostEqual(left, right, delta=band,
                               msg=f"mirror match lopsided: {left:.3f} vs {right:.3f}")

    def test_custom_archetypes_are_symmetric(self):
        for label, stats in ARCHETYPES.items():
            with self.subTest(archetype=label):
                left = lambda s=stats: fighter("Left", **s)
                right = lambda s=stats: fighter("Right", **s)
                self.assertEqual(len(determine_strike_order(left(), right(), verbose=False)), 1)
                self.assertSymmetric(left, right)

    def test_profile_mirror_matches_are_symmetric(self):
        # A spread across factions: every 15th character and 40th unit in the
        # quick tier, every character and every 4th unit in the full tier.
        steps = {"characters": 1, "units": 4} if FULL else {"characters": 15, "units": 40}
        runs = 1500 if FULL else 300
        picks = list(REGRESSION_MIRRORS)
        for kind, step in steps.items():
            picks += [p for p in all_profiles(kind)[::step] if p not in picks]
        for faction, profile in picks:
            with self.subTest(profile=profile):
                self.assertSymmetric(
                    lambda: build(faction, profile, name="Left"),
                    lambda: build(faction, profile, name="Right"),
                    runs=1500 if (faction, profile) in REGRESSION_MIRRORS else runs,
                )


class TestSeatOrder(StatisticalCase):
    def test_argument_order_does_not_change_the_odds(self):
        runs = SAMPLES_LARGE
        for (fa, pa), (fb, pb) in SEAT_PAIRS:
            with self.subTest(a=pa, b=pb):
                first, _, _ = win_rates(lambda: build(fa, pa, name="X"),
                                        lambda: build(fb, pb, name="Y"), runs, seed=1)
                _, second, _ = win_rates(lambda: build(fb, pb, name="Y"),
                                         lambda: build(fa, pa, name="X"), runs, seed=2)
                self.assertAlmostEqual(
                    first, second, delta=math.sqrt(2) * tolerance(first, runs),
                    msg=f"{pa} wins {first:.3f} seated first but {second:.3f} seated second",
                )

    def test_strike_order_ignores_argument_order(self):
        for (fa, pa), (fb, pb) in SEAT_PAIRS:
            a, b = build(fa, pa, name="X"), build(fb, pb, name="Y")
            for first_round in (True, False):
                with self.subTest(a=pa, b=pb, first_round=first_round):
                    forward = determine_strike_order(a, b, False, first_round)
                    backward = determine_strike_order(b, a, False, first_round)
                    names = lambda steps: [sorted(att.name for att, _ in s) for s in steps]
                    self.assertEqual(names(forward), names(backward))


if __name__ == "__main__":
    unittest.main()
