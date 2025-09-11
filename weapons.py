from faction_profiles import *
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

def find_weapon_key(weapon):
    """Return the MeleeWeaponDict key tuple that contains the given weapon name, or None."""
    for key in MeleeWeaponDict:
        if weapon in key:
            return key
    return None


def get_weapon_stats(weapon, raise_on_missing=True):
    """Return (strength_bonus, armour_piercing, special_rules) for a weapon name.
    If raise_on_missing is True, raise ValueError when weapon not found.
    """
    key = find_weapon_key(weapon)
    if key is None:
        if raise_on_missing:
            raise ValueError(f"Weapon '{weapon}' not found in MeleeWeaponDict")
        return (None, 0, [])
    data = MeleeWeaponDict[key]
    strength_bonus = data[0]
    armour_piercing = data[1]
    rules = data[2] if data[2] else []
    return (strength_bonus, armour_piercing, rules)


def get_weapon_special_rules(weapon):
    # Return normalized list of special rules, don't raise on missing by default
    try:
        _, _, rules = get_weapon_stats(weapon, raise_on_missing=False)
        return rules
    except Exception:
        return []

def get_weapon_strength_bonus(weapon, raise_on_missing=True):
    """Return the weapon's strength bonus (or None)."""
    strength, _, _ = get_weapon_stats(weapon, raise_on_missing=raise_on_missing)
    return strength


def get_weapon_ap(weapon, raise_on_missing=True):
    """Return the weapon's armour-piercing value (int, may be negative or 0)."""
    _, ap, _ = get_weapon_stats(weapon, raise_on_missing=raise_on_missing)
    return ap
