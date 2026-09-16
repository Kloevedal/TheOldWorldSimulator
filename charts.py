"""The core To Hit and To Wound charts.

Both are transcribed from The Old World rules index:
  https://tow.whfb.app/the-combat-phase/roll-to-hit-combat
  https://tow.whfb.app/the-combat-phase/roll-to-wound-combat

These are Old World values, not an earlier edition of Warhammer Fantasy.
`tests/test_charts.py` pins every cell against that source.
"""

from __future__ import annotations

from armor import *
from elven_honors import *
from magic_items import *
from weapons import *

# Row = attacker's Weapon Skill, column = target's Weapon Skill (both 1-10).
WeaponSkillChart = [
    [4, 4, 5, 5, 5, 5, 5, 5, 5, 5],  # Attacker WS 1
    [3, 4, 4, 4, 5, 5, 5, 5, 5, 5],  # Attacker WS 2
    [2, 3, 4, 4, 4, 4, 5, 5, 5, 5],  # Attacker WS 3
    [2, 3, 3, 4, 4, 4, 4, 4, 5, 5],  # Attacker WS 4
    [2, 2, 3, 3, 4, 4, 4, 4, 4, 4],  # Attacker WS 5
    [2, 2, 3, 3, 3, 4, 4, 4, 4, 4],  # Attacker WS 6
    [2, 2, 2, 3, 3, 3, 4, 4, 4, 4],  # Attacker WS 7
    [2, 2, 2, 3, 3, 3, 3, 4, 4, 4],  # Attacker WS 8
    [2, 2, 2, 2, 3, 3, 3, 3, 4, 4],  # Attacker WS 9
    [2, 2, 2, 2, 3, 3, 3, 3, 3, 4],  # Attacker WS 10
]

# Row = attacker's Strength, column = target's Toughness (both 1-10).
# None means the attack cannot wound at all.
Wounds_vs_ToughnessChart = [
    [4, 5, 6, 6, 6, 6, None, None, None, None],  # Strength 1
    [3, 4, 5, 6, 6, 6, 6, None, None, None],     # Strength 2
    [2, 3, 4, 5, 6, 6, 6, 6, None, None],        # Strength 3
    [2, 2, 3, 4, 5, 6, 6, 6, 6, None],           # Strength 4
    [2, 2, 2, 3, 4, 5, 6, 6, 6, 6],              # Strength 5
    [2, 2, 2, 2, 3, 4, 5, 6, 6, 6],              # Strength 6
    [2, 2, 2, 2, 2, 3, 4, 5, 6, 6],              # Strength 7
    [2, 2, 2, 2, 2, 2, 3, 4, 5, 6],              # Strength 8
    [2, 2, 2, 2, 2, 2, 2, 3, 4, 5],              # Strength 9
    [2, 2, 2, 2, 2, 2, 2, 2, 3, 4],              # Strength 10
]
