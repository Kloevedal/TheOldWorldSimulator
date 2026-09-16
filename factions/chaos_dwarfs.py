"""Chaos Dwarfs.

Profiles from https://tow.whfb.app/army/chaos-dwarfs
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Chaos Dwarfs"

# Other names that should resolve to this faction.
ALIASES = [
    "Chaos Dwarves",
    "Dawi Zharr",
    "Chaos Dwarfs",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Taur'ruk": "Bull Centaur Taur'ruk",
    "Castellan": "Infernal Castellan",
    "Seneschal": "Infernal Seneschal",
}

# Blackshard Armour is a 5+ Ward against Flaming Attacks; the parseable
# "Ward5 (Flaming)" is carried alongside the rule name so the engine sees it.
CHARACTERS = {
    "Infernal Castellan": {
        # https://tow.whfb.app/unit/infernal-castellan - 125 pts
        # Also has fireglaive, hailshot blunderbuss, pistol and naptha bomb options;
        # shooting is not simulated.
        "points": 125,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Chaos Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blackshard Armour", "Ward5 (Flaming)", "Ensorcelled Weapons", "Rallying Cry", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Darkforged Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Infernal Seneschal": {
        # https://tow.whfb.app/unit/infernal-seneschal - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Chaos Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blackshard Armour", "Ward5 (Flaming)", "Ensorcelled Weapons", "Rallying Cry", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Darkforged Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Sorcerer-Prophet": {
        # https://tow.whfb.app/unit/sorcerer-prophet - 195 pts
        "points": 195,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Chaos Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blackshard Armour", "Ward5 (Flaming)", "Ensorcelled Weapons", "Infernal Engineer", "Lore of Hashut", "Resolute", "Sorcerer's Curse", "Stubborn"],
            "WizardLevel": 3,
            "Lores": ["Daemonology", "Dark Magic", "Elementalism"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Darkforged Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Bale Taurus", "Great Taurus", "Lammasu"]
        }
    },
    "Daemonsmith Sorcerer": {
        # https://tow.whfb.app/unit/daemonsmith-sorcerer - 85 pts
        "points": 85,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Chaos Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blackshard Armour", "Ward5 (Flaming)", "Ensorcelled Weapons", "Infernal Engineer", "Lore of Hashut", "Resolute", "Sorcerer's Curse", "Stubborn"],
            "WizardLevel": 1,
            "Lores": ["Daemonology", "Dark Magic", "Elementalism"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Darkforged Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Great Taurus", "Lammasu"]
        }
    },
    "Bull Centaur Taur'ruk": {
        # https://tow.whfb.app/unit/bull-centaur-taurruk - 145 pts
        # A bull centaur: the profile already includes its own four legs.
        "points": 145,
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 5,
            "BallisticSkill": 2,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Bull Centaur",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Armoured Hide (1)", "Blackshard Armour", "Ward5 (Flaming)", "Ensorcelled Weapons", "Fear", "First Charge", "Impact Hits (D3+1)", "Loner", "Stampede", "Stubborn", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Darkforged Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Hobgoblin Khan": {
        # https://tow.whfb.app/unit/hobgoblin-khan - 45 pts
        # Carries throwing weapons as standard; shooting is not simulated.
        "points": 45,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Hobgoblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Backstab", "Evasive", "Levies", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Giant Wolf"]
        }
    },
}

# Regular (non-character) units go here.
UNITS = {}


# Army-wide special rules for this faction. `status` is how far the engine
# goes with each: "implemented", "partial", or None for recorded only.
FACTION_RULES = {
    'Blackshard Armour': {
        "status": 'implemented',
        "text": (
            "A 5+ Ward save against wounds from an attack with Flaming Attacks. "
            "A Wizard with this rule may wear armour without penalty. "
        ),
    },
    'Ensorcelled Weapons': {
        "status": 'implemented',
        "text": (
            "A hand weapon carried by this model has Magical Attacks and an "
            "Armour Piercing of -1. "
        ),
    },
    'Lore of Hashut': {
        "status": None,
        "text": (
            "Magic is not simulated. "
        ),
    },
    'Infernal Engineer': {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
    "Sorcerer's Curse": {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
    'Resolute': {
        "status": None,
        "text": (
            "-1 to any Flee or Pursuit roll. Neither happens in a duel. "
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
