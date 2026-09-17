"""Shared helpers for the test suite.

Two tiers:

* quick (default) - every test runs, with sample sizes small enough that the
  whole suite finishes in a few seconds. This is what the pre-commit hook runs.
* full - set TOW_FULL_TESTS=1 (or `python3 run_tests.py --full`). Statistical
  tests use far larger samples and the whole-roster round robin runs.
"""

from __future__ import annotations

import io
import math
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dice  # noqa: E402
from character_model import Character  # noqa: E402
from combat_simulations import combat_simulation  # noqa: E402
from faction_profiles import FactionProfiles  # noqa: E402

FULL = os.environ.get("TOW_FULL_TESTS") == "1"

# Sample sizes: (quick, full).
SAMPLES_SMALL = 400 if not FULL else 4000
SAMPLES_LARGE = 2000 if not FULL else 40000

full_only = unittest.skipUnless(FULL, "full tier only - run with --full")


def fighter(name="Fighter", **overrides):
    """A plain custom character; override any characteristic by keyword."""
    stats = dict(
        Movement=4, WeaponSkill=4, BallisticSkill=3, Strength=4, Toughness=4,
        Initiative=4, Wounds=3, Attacks=2, Leadership=7, Race="Human",
        Weapon="Hand Weapon",
    )
    stats.update(overrides)
    return Character(name=name, **stats)


def all_profiles(kind="characters"):
    """(faction, profile) pairs in a stable order.

    `kind` is "characters", "units" or "all". The split comes from each faction
    module's CHARACTERS / UNITS, which is what the registry is built from.
    """
    from factions import FACTION_MODULES

    pairs = []
    for module in sorted(FACTION_MODULES, key=lambda m: m.FACTION):
        names = set()
        if kind in ("characters", "all"):
            names |= set(module.CHARACTERS)
        if kind in ("units", "all"):
            names |= set(getattr(module, "UNITS", {}))
        pairs += [(module.FACTION, name) for name in sorted(names)]
    return pairs


def build(faction, profile, name=None, **kwargs):
    """Build a profile quietly (construction can print item warnings)."""
    with redirect_stdout(io.StringIO()):
        return Character(
            name=name or profile, faction_type=faction, profile_name=profile, **kwargs
        )


def legal_loadouts(faction, profile):
    """Every legal (weapon, armour, shield) combination for a profile."""
    from armor import get_armour_save
    from special_rules import RequiresTwoHands
    from weapons import get_weapon_special_rules

    options = FactionProfiles[faction][profile]["equipment_options"]
    armours = [None] + [a for a in options["armor"] if get_armour_save(a)]
    shields = [False, True] if options["shield"] else [False]
    for weapon in options["weapons"]:
        two_handed = RequiresTwoHands in get_weapon_special_rules(weapon)
        for armour in armours:
            for shield in shields:
                if shield and two_handed:
                    continue
                yield weapon, armour, shield


def narrate(make_a, make_b, seed, rounds=3):
    """Seeded, verbose duel. Returns (narration, winner name or None).

    `make_a`/`make_b` are zero-argument callables so each call gets fresh
    fighters.
    """
    a, b = make_a(), make_b()
    dice.seed(seed)
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        winner = combat_simulation(a, b, rounds=rounds, verbose=True)
    return buffer.getvalue(), (winner.name if winner else None)


def win_rates(make_a, make_b, runs, rounds=3, seed=0):
    """(A win fraction, B win fraction, draw fraction) over `runs` duels."""
    dice.seed(seed)
    wins_a = wins_b = 0
    for _ in range(runs):
        a, b = make_a(), make_b()
        winner = combat_simulation(a, b, rounds=rounds, verbose=False)
        if winner is a:
            wins_a += 1
        elif winner is b:
            wins_b += 1
    return wins_a / runs, wins_b / runs, (runs - wins_a - wins_b) / runs


def tolerance(p, n, sigmas=4.0):
    """Half-width of a `sigmas` confidence band for a proportion.

    Four sigma keeps false alarms below 1 in 10,000 per assertion while still
    catching real regressions of a few percentage points.
    """
    p = min(max(p, 0.01), 0.99)
    return sigmas * math.sqrt(p * (1 - p) / n)


class StatisticalCase(unittest.TestCase):
    def assertProportion(self, observed, expected, n, msg=None):
        band = tolerance(expected, n)
        self.assertAlmostEqual(
            observed, expected, delta=band,
            msg=msg or f"observed {observed:.4f}, expected {expected:.4f} ± {band:.4f} (n={n})",
        )

    def assertNotWorse(self, better, worse, n, msg=None):
        """`better` should be at least `worse`, allowing sampling noise."""
        band = tolerance(max(better, worse), n) * math.sqrt(2)
        self.assertGreaterEqual(
            better + band, worse,
            msg=msg or f"{better:.4f} should not be below {worse:.4f} (n={n})",
        )
