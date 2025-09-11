# Game Data 

from armor import *
from elven_honors import *
from magic_items import *
from weapons import *

# The chart is a 2D list where the row(1st index) is the Attacker's WS
# and the column (2nd index) is the Defender's WS
WeaponSkillChart = [
    [4, 4, 5, 5, 5, 5, 5, 5, 5, 5],  # Attacker WS 1
    [3, 4, 4, 4, 5, 5, 5, 5, 5, 5],  # Attacker WS 2
    [2, 3, 4, 4, 4, 4, 5, 5, 5, 5],  # Attacker WS 3
    [2, 3, 3, 4, 4, 4, 4, 5, 5, 5],  # Attacker WS 4
    [2, 2, 3, 3, 4, 4, 4, 4, 4, 4],  # Attacker WS 5
    [2, 2, 3, 3, 3, 4, 4, 4, 4, 4],  # Attacker WS 6
    [2, 2, 2, 3, 3, 3, 4, 4, 4, 4],  # Attacker WS 7
    [2, 2, 2, 3, 3, 3, 3, 4, 4, 4],  # Attacker WS 8
    [2, 2, 2, 2, 3, 3, 3, 3, 4, 4],  # Attacker WS 9
    [2, 2, 2, 2, 2, 3, 3, 3, 3, 4],  # Attacker WS 10
]

# Defender's Toughness (T) vs Attacker's Strength (S) chart
# The chart is a 2D list where the row(1st index) is the Attacker's Strength
# and the column (2nd index) is the Defender's Toughness
Wounds_vs_ToughnessChart = [
    [4, 5, 6, 6, 6, 6, None, None, None, None],  # Strength 1
    [3, 4, 5, 6, 6, 6, None, None, None, None],  # Strength 2
    [2, 3, 4, 5, 6, 6, 6, None, None, None],  # Strength 3
    [2, 2, 3, 4, 5, 6, 6, 6, None, None],  # Strength 4
    [2, 2, 2, 3, 4, 5, 6, 6, 6, None],  # Strength 5
    [2, 2, 2, 2, 3, 4, 5, 6, 6, 6],  # Strength 6
    [2, 2, 2, 2, 2, 3, 4, 5, 6, 6],  # Strength 7
    [2, 2, 2, 2, 2, 2, 3, 4, 5, 6],  # Strength 8
    [2, 2, 2, 2, 2, 2, 2, 3, 4, 5],  # Strength 9
    [2, 2, 2, 2, 2, 2, 2, 2, 3, 4],  # Strength 10
]

