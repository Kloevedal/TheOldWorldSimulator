from game_data import *
from special_rules import *

# Special rules can include: "+1A" for +1 Attack
MeleeWeaponDict = {
    ("HW", "Hand Weapon", "HandWeapon"): [None, 0, None],  # Hand Weapon, no strength bonus, no armor piercing, no special rules
    ("Two Hand Weapons", "2xHW", "2HW"): [None, 0, ["+1A", "RequiresTwoHands"]],  # Two Hand Weapons, no strength bonus, no armor piercing, +1 Attack
    ("Flail",): [2, -2, [FirstRoundStr]],  # Flail, +2 Strength, -2 Armor Piercing, First Round Strength only
    ("Great Weapon", "GW", "GreatWeapon"): [2, -2, [StrikeLast, "AB1","RequiresTwoHands"]],  # Great Weapon, +2 Strength, -2 Armor Piercing, Armour Bane 1, Strike Last
    ("Halberd",): [1, -1, ["AB1", "RequiresTwoHands"]],  # Halberd, +1 Strength, -1 Armor Piercing, Armour Bane 1
    ("Morning Star", "MorningStar","Morningstar"): [1, -1, [FirstRoundStr]],  # Morning Star, +1 Strength, -1 Armor Piercing, First Round Strength only
    ("Whip",): [None, 0, [StrikeFirst]],  # Whip, Strike First
    ("Lance",): [2, 2, [FirstRoundOnly, "AB1"]],  # Lance, +2 Strength, +2 Armor Piercing, Armour Bane 1, First Round Only
    ("Cavalry Spear", "CavSpear", "CavalrySpear"): [1, -1, [FirstRoundOnly]],  # Cavalry Spear, +1 Strength, -1 armor piercing, First Round Only
    ("Throwing Spears", "ThrowingSpear"): [None, 0, [FirstRoundOnly]],  # Throwing Spears, No strength, no armor piercing, First Round Only
    ("Thrusting Spear", "ThrustingSpear", "Spear"): [None, 0, None],  # Thrusting Spear, no strength bonus, no armor piercing, no special rules
    ("Chayal",):[2,-3,["KillingBlow6",RerollHits1]], # Chayal, +2 Strength, -3 Armor Piercing, Killing Blow 6+, Reroll Hits of 1
    ("Mathlann's Ire",):[1,-2,["AB1","Magic", "RequiresTwoHands"]], # Mathlann's Ire, +1 Strength, -2 Armor Piercing, Armour Bane 1, Magic
    ("SwordofHoeth",):[2,-2,["Magic","RequiresTwoHands"]], # Sword of Hoeth, +2 Strength, -2 Armor Piercing, Magic
    ("ChracianGreatBlade",):[2,-3,["RequiresTwoHands",StrikeLast]], # Chracian Great Blade, +2 Strength, -3 Armor Piercing, Requires Two Hands, Strike Last
    
}
