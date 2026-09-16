"""The To Hit and To Wound charts, pinned cell by cell against the rulebook.

Transcribed from:
  https://tow.whfb.app/the-combat-phase/roll-to-hit-combat
  https://tow.whfb.app/the-combat-phase/roll-to-wound-combat

Every roll in the engine goes through these two tables, so a single wrong cell
skews every result. They were hand-entered originally and carried six errors.
"""

from __future__ import annotations

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from charts import WeaponSkillChart, Wounds_vs_ToughnessChart

_ = None

RULEBOOK_TO_HIT = [
    [4, 4, 5, 5, 5, 5, 5, 5, 5, 5],
    [3, 4, 4, 4, 5, 5, 5, 5, 5, 5],
    [2, 3, 4, 4, 4, 4, 5, 5, 5, 5],
    [2, 3, 3, 4, 4, 4, 4, 4, 5, 5],
    [2, 2, 3, 3, 4, 4, 4, 4, 4, 4],
    [2, 2, 3, 3, 3, 4, 4, 4, 4, 4],
    [2, 2, 2, 3, 3, 3, 4, 4, 4, 4],
    [2, 2, 2, 3, 3, 3, 3, 4, 4, 4],
    [2, 2, 2, 2, 3, 3, 3, 3, 4, 4],
    [2, 2, 2, 2, 3, 3, 3, 3, 3, 4],
]

RULEBOOK_TO_WOUND = [
    [4, 5, 6, 6, 6, 6, _, _, _, _],
    [3, 4, 5, 6, 6, 6, 6, _, _, _],
    [2, 3, 4, 5, 6, 6, 6, 6, _, _],
    [2, 2, 3, 4, 5, 6, 6, 6, 6, _],
    [2, 2, 2, 3, 4, 5, 6, 6, 6, 6],
    [2, 2, 2, 2, 3, 4, 5, 6, 6, 6],
    [2, 2, 2, 2, 2, 3, 4, 5, 6, 6],
    [2, 2, 2, 2, 2, 2, 3, 4, 5, 6],
    [2, 2, 2, 2, 2, 2, 2, 3, 4, 5],
    [2, 2, 2, 2, 2, 2, 2, 2, 3, 4],
]


class TestToHitChart(unittest.TestCase):
    def test_every_cell_matches_the_rulebook(self):
        for attacker in range(10):
            for target in range(10):
                with self.subTest(attacker_ws=attacker + 1, target_ws=target + 1):
                    self.assertEqual(
                        WeaponSkillChart[attacker][target],
                        RULEBOOK_TO_HIT[attacker][target],
                    )

    def test_the_chart_is_ten_by_ten(self):
        self.assertEqual(len(WeaponSkillChart), 10)
        for row in WeaponSkillChart:
            self.assertEqual(len(row), 10)

    def test_equal_weapon_skill_always_hits_on_a_four(self):
        for ws in range(10):
            self.assertEqual(WeaponSkillChart[ws][ws], 4)

    def test_no_target_is_better_than_two_or_worse_than_five(self):
        for row in WeaponSkillChart:
            for value in row:
                self.assertGreaterEqual(value, 2)
                self.assertLessEqual(value, 5)


class TestToWoundChart(unittest.TestCase):
    def test_every_cell_matches_the_rulebook(self):
        for strength in range(10):
            for toughness in range(10):
                with self.subTest(strength=strength + 1, toughness=toughness + 1):
                    self.assertEqual(
                        Wounds_vs_ToughnessChart[strength][toughness],
                        RULEBOOK_TO_WOUND[strength][toughness],
                    )

    def test_the_chart_is_ten_by_ten(self):
        self.assertEqual(len(Wounds_vs_ToughnessChart), 10)
        for row in Wounds_vs_ToughnessChart:
            self.assertEqual(len(row), 10)

    def test_equal_strength_and_toughness_wounds_on_a_four(self):
        for i in range(10):
            self.assertEqual(Wounds_vs_ToughnessChart[i][i], 4)

    def test_toughness_six_higher_than_strength_cannot_be_wounded(self):
        """A gap of 5 still wounds on a 6+; a gap of 6 or more cannot wound."""
        for strength in range(10):
            for toughness in range(10):
                gap = toughness - strength
                cell = Wounds_vs_ToughnessChart[strength][toughness]
                with self.subTest(strength=strength + 1, toughness=toughness + 1):
                    if gap >= 6:
                        self.assertIsNone(cell)
                    else:
                        self.assertIsNotNone(cell)
                        if gap == 5:
                            self.assertEqual(cell, 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
