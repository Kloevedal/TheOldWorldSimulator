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

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Hobgoblin Cutthroats": {
        # https://tow.whfb.app/unit/hobgoblin-cutthroats - 3 pts per model, unit size
        # 10+
        # Fights with the Cutthroat row.
        # Shooting is not simulated, so these are left out of the options: shortbows.
        "points": 3,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Boss', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 4,
            "Race": "Hobgoblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Backstab", "Close Order", "Horde", "Levies", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Infernal Guard": {
        # https://tow.whfb.app/unit/infernal-guard - 11 pts per model, unit size 10+
        # Fights with the Infernal Guard row.
        # Shooting is not simulated, so these are left out of the options:
        # Fireglaives, Hailshot blunderbusses, Naptha bombs, Pistol.
        "points": 11,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Deathmask', 'Movement': 3, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Chaos Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Detachment", "Regimental Unit", "Resolute", "Shieldwall", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled", "Blackshard Armour"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Infernal Ironsworn": {
        # https://tow.whfb.app/unit/infernal-ironsworn - 19 pts per model, unit size
        # 10+
        # Fights with the Infernal Ironsworn row.
        # Shooting is not simulated, so these are left out of the options: Naptha
        # bombs, Pistol.
        "points": 19,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Overseer', 'Movement': 3, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 3, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Chaos Dwarf",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blackshard Armour", "Ward5 (Flaming)", "Close Order", "Drilled", "Ensorcelled Weapons", "Quell Panic", "Regimental Unit", "Resolute", "Shieldwall", "Stubborn", "Veteran"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Halberd"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "K'daai Fireborn": {
        # https://tow.whfb.app/unit/kdaai-fireborn - 41 pts per model, unit size 3+
        # Fights with the K'daai Fireborn row.
        "points": 41,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Manburner', 'Movement': 6, 'WeaponSkill': 4, 'BallisticSkill': 2, 'Strength': 5, 'Toughness': 4, 'Initiative': 4, 'Wounds': 2, 'Attacks': 4, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Chaos Dwarf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blazing Body", "Close Order", "Ensorcelled Weapons", "Fear", "Flaming Attacks", "Immune to Psychology", "Regeneration (5+)", "Unbreakable", "Unstable", "Warp-spawned"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Sneaky Gits": {
        # https://tow.whfb.app/unit/sneaky-gits - 6 pts per model, unit size 10+
        # Fights with the Sneaking Git row.
        # Shooting is not simulated, so these are left out of the options: throwing
        # weapons.
        "points": 6,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Murder Boss', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Hobgoblin",
            "Armor": None,
            "Weapon": "Two Hand Weapons",
            "Shield": False,
            "SpecialRules": ["Ambushers", "Backstab", "Evasive", "Levies", "Move Through Cover", "Skirmishers"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Two Hand Weapons"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Bull Centaur Renders": {
        # https://tow.whfb.app/unit/bull-centaur-renders - 56 pts per model, unit size
        # 3+
        # Fights with the Bull Centaur Render row.
        # Also has a profile for Bull Centaur Ba'hal (M7 WS4 BS2 S4 T5 W3 I3 A3 Ld8);
        # not simulated.
        "points": 56,
        "points_per": "model",
        "unit_size": "3+",
        "other_profiles": [
            {'Name': "Bull Centaur Ba'hal", 'Movement': 7, 'WeaponSkill': 4, 'BallisticSkill': 2, 'Strength': 4, 'Toughness': 5, 'Initiative': 3, 'Wounds': 3, 'Attacks': 3, 'Leadership': 8},
        ],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Bull Centaur",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (1)", "Blackshard Armour", "Ward5 (Flaming)", "Close Order", "Ensorcelled Weapons", "Fear", "First Charge", "Impact Hits (D3)", "Loner", "Stampede", "Stubborn", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Hobgoblin Wolf Riders": {
        # https://tow.whfb.app/unit/hobgoblin-wolf-riders - 12 pts per model, unit
        # size 5+
        # Fights with the Hobgoblin Wolf Rider row.
        # Also has a profile for Giant Wolf (M9 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Shortbows.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Boss', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [
            {'Name': 'Giant Wolf', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Hobgoblin",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Backstab", "Evasive", "Fast Cavalry", "Fire & Flee", "Levies", "Open Order", "Skirmishers", "Swiftstride"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Feigned Flight", "Reserve Move"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Iron Daemon": {
        # https://tow.whfb.app/unit/iron-daemon - 275 pts per unit
        # Fights with the Chaos Dwarf Crew (x3) row, using the Iron Daemon row's
        # Toughness and Wounds.
        # Also has a profile for Iron Daemon (M5 WS- BS- S8 T7 W7 I- A- Ld-); not
        # simulated.
        # Armour value 3+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: Steam
        # Cannonade.
        "points": 275,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Iron Daemon', 'Movement': 5, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 8, 'Toughness': 7, 'Initiative': None, 'Wounds': 7, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 7,
            "Initiative": 2,
            "Wounds": 7,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Chaos Dwarf",
            "Armor": "Armour Value 3+",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Carriage Hauler", "Close Order", "Fear", "Grinding Wheels", "Immune to Psychology", "Impact Hits (D6+1)", "Large Target", "Lumbering Destruction", "Stomp Attacks (D3+1)", "Unbreakable"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
            "OptionalRules": ["Hellbound", "Skullcracker"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Armour Value 3+"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Deathshrieker Rocket Launcher": {
        # https://tow.whfb.app/unit/deathshrieker-rocket-launcher - 120 pts per unit
        # Fights with the Chaos Dwarf Crew row.
        # Also has a profile for Deathshrieker Rocket Launcher (M- WS- BS- S- T6 W3 I-
        # A- Ld-); not simulated.
        # Shooting is not simulated, so these are left out of the options: Demolition
        # Rockets, Infernal Incendiaries.
        "points": 120,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Deathshrieker Rocket Launcher', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Chaos Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blackshard Armour", "Ward5 (Flaming)", "Skirmishers"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
            "OptionalRules": ["Hellbound", "Steam Carriage"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Dreadquake Mortar": {
        # https://tow.whfb.app/unit/dreadquake-mortar - 165 pts per unit
        # Fights with the Chaos Dwarf Crew row.
        # Also has a profile for Dreadquake Mortar (M- WS- BS- S- T7 W4 I- A- Ld-);
        # not simulated.
        # Also has a profile for Ogre Loader (M- WS3 BS- S4 T- W(+2) I2 A(+2) Ld-);
        # not simulated.
        # Shooting is not simulated, so these are left out of the options: Dreadquake
        # Mortar.
        "points": 165,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Dreadquake Mortar', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 7, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Ogre Loader', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Chaos Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blackshard Armour", "Ward5 (Flaming)", "Skirmishers"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
            "OptionalRules": ["Hellbound", "Steam Carriage"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Hobgoblin Bolt Thrower": {
        # https://tow.whfb.app/unit/hobgoblin-bolt-thrower - 45 pts per unit
        # Fights with the Hobgoblin Crew row.
        # Also has a profile for Bolt Thrower (M- WS- BS- S- T4 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Bolt
        # thrower.
        "points": 45,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Bolt Thrower', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 4, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 6,
            "Race": "Hobgoblin",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Levies", "Skirmishers"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Magma Cannon": {
        # https://tow.whfb.app/unit/magma-cannon - 125 pts per unit
        # Fights with the Chaos Dwarf Crew row.
        # Also has a profile for Magma Cannon (M- WS- BS- S- T6 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Fire
        # thrower.
        "points": 125,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Magma Cannon', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Chaos Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blackshard Armour", "Ward5 (Flaming)", "Skirmishers"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
            "OptionalRules": ["Hellbound", "Steam Carriage"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
}


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
            "Unless this model is fleeing or engaged in combat, once per turn a "
            "friendly war machine that is within its Command range may re-roll one "
            "Scatter dice or one Artillery dice."
        ),
    },
    "Sorcerer's Curse": {
        "status": None,
        "text": (
            "If this model miscasts a spell, it must immediately make a Toughness "
            "test. If this test is failed, it loses a single Wound and gains a +1 "
            "modifier to its Toughness characteristic instead of rolling on the "
            "Miscast table. If this test is passed, it rolls on the Miscast table "
            "as normal."
        ),
    },
    'Resolute': {
        "status": None,
        "text": (
            "-1 to any Flee or Pursuit roll. Neither happens in a duel. "
        ),
    },
    "Ambushers": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ambushers",
        "text": (
            "A unit with this special rule may be held in reserve rather than be "
            "deployed at the start of the game. From the beginning of round two "
            "onwards, roll a D6 during each of your Start of Turn sub-phases for "
            "each unit of Ambushers in your army that is held in reserve. On a roll "
            "of 1-3, the unit is delayed until your next turn at least. On a roll "
            "of 4+, the unit arrives, entering the battle as reinforcements during "
            "the Compulsory Moves sub-phase. The unit may be placed on any edge of "
            "the battlefield, chosen by its controlling player, but cannot be "
            "placed within 8\" of an enemy model. If any Ambushers are still held in "
            "reserve by the start of round five, they arrive automatically."
        ),
    },
    "Armoured Hide": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/armoured-hide",
        "text": (
            "The hide of some creatures forms natural armour and improves their "
            "armour value (and that of their rider). By how much armour value is "
            "improved varies from model to model, as shown in brackets after the "
            "name of this special rule (shown here as 'X'). Note that a model that "
            "wears no armour is considered to have an armour value of 7+ for the "
            "purposes of rules that improve armour value."
        ),
    },
    "Backstab": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/backstab",
        "text": (
            "If a unit with this special rule is engaged with an enemy unit's flank "
            "or rear arc, it may re-roll any failed rolls To Hit made against that "
            "enemy unit."
        ),
    },
    "Blazing Body": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/blazing-body",
        "text": (
            "At the start of every Combat phase, any model (friend or foe) that is "
            "in base contact with this model and that does not also have this "
            "special rule suffers a single Strength 3 hit with an AP of -. This hit "
            "has the Flaming Attacks special rule. Note that any Wounds lost due to "
            "these hits do not count towards the combat result."
        ),
    },
    "Carriage Hauler": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/carriage-hauler",
        "text": (
            "During the Movement phase, up to two friendly war machines with the "
            "'Steam Carriage' upgrade that are completely within this model's rear "
            "arc and within 8\" of its base at the beginning of the phase can be "
            "moved when this model moves. These war machines must finish their "
            "movement completely within this model's rear arc and within 8\" of its "
            "base. Unless this model moves using the Lumbering Destruction special "
            "rule or makes a charge move, these war machines are not considered to "
            "have moved this turn."
        ),
    },
    "Close Order": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/close-order",
        "text": (
            "A unit consisting of models with this special rule may adopt a Close "
            "Order formation."
        ),
    },
    "Detachment": {
        "status": None,
        "url": "https://tow.whfb.app/warhammer-armies/detachment-special-rules",
        "text": (
            "Detachments follow a number of special rules, representing the "
            "specialised way in which they function alongside their regimental "
            "units: - Regimental Deployment - Regimental Leadership - Regimental "
            "Psychology - Supporting Actions"
        ),
    },
    "Drilled": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/drilled",
        "text": (
            "Unless it is fleeing, a Drilled unit may perform a free redress the "
            "ranks manoeuvre immediately before moving. Once this manoeuvre is "
            "complete, the unit moves as normal. In addition, a Drilled unit can "
            "march whilst within 8\" of an enemy unit without first having to make a "
            "Leadership test. Note that any character that joins a Drilled unit is "
            "considered to be Drilled as well."
        ),
    },
    "Evasive": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/evasive",
        "text": (
            "Once per turn, when a unit in which the majority of the models have "
            "this special rule is declared the target during the enemy Shooting "
            "phase, that unit may choose to Fall Back in Good Order, fleeing "
            "directly away from the enemy unit shooting at it. Once this unit has "
            "completed its move, the enemy unit may continue with its shooting as "
            "declared."
        ),
    },
    "Fast Cavalry": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fast-cavalry",
        "text": (
            "If all of the models (including characters) within a unit arrayed in "
            "an Open Order formation have this special rule, the unit may perform "
            "its Quick Turn even if it marched."
        ),
    },
    "Fear": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fear",
        "text": (
            "Models with this special rule cause Fear: - If a unit wishes to "
            "declare a charge against an enemy unit that both causes Fear and has a "
            "higher Unit Strength, it must first make a Leadership test. If this "
            "test is failed, the unit cannot charge. It does not move and is "
            "considered to have made a failed charge. If this test is passed, the "
            "unit can charge as normal. - If a unit is engaged with an enemy unit "
            "that both causes Fear and has a higher Unit Strength when its combat "
            "is chosen during any Choose & Fight Combat sub-phase, it must make a "
            "Leadership test. If this test is failed, any models in the unit that "
            "direct their attacks against the Fear-causing enemy suffer a -1 "
            "modifier to their rolls [...]"
        ),
    },
    "Fire & Flee": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fire-and-flee",
        "text": (
            "If the majority of the models in a unit armed with missile weapons "
            "have this special rule, the unit may declare that it will 'Fire & "
            "Flee' as a charge reaction: Fire & Flee The unit launches a volley of "
            "weapons fire before turning to flee from the enemy. If a unit with "
            "this special rule is armed with missile weapons and can draw a line of "
            "sight to the charging unit, it may declare that it will Fire & Flee. "
            "The unit will Stand & Shoot before turning tail and fleeing from the "
            "charge. However, due to the time spent shooting at the charging foe, "
            "when making its Flee roll the unit rolls two D6 and discards the "
            "lowest result. If both dice roll the same result, discard either. Note "
            "that, if the [...]"
        ),
    },
    "First Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/first-charge",
        "text": (
            "If this unit's first charge of the game is successful (i.e., if the "
            "unit makes contact with the charge target), the charge target becomes "
            "Disrupted until the end of the Combat phase of that turn."
        ),
    },
    "Flaming Attacks": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/flaming-attacks",
        "text": (
            "Any attack made or hits caused by a model with this special rule, or "
            "made using a weapon or spell with this special rule, is a 'Flaming' "
            "attack. In addition, a model with this special rule causes Fear in "
            "models whose troop type is war beasts or swarms. Unless otherwise "
            "stated, a model with this special rule makes Flaming attacks both when "
            "shooting and in combat (though any spells cast by the model are "
            "unaffected, as are any attacks made with magic weapons they might be "
            "wielding)."
        ),
    },
    "Grinding Wheels": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/grinding-wheels",
        "text": (
            "Stomp Attacks made by a this model have an Armour Piercing "
            "characteristic of -2. However, this rule cannot be used against models "
            "whose troop type is behemoth – they are simply too large to be caught "
            "beneath the wheels. In addition, and unlike other chariots, this model "
            "treats low linear obstacles as open terrain rather than as impassable "
            "terrain."
        ),
    },
    "Horde": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/horde",
        "text": (
            "A unit with this special rule may increase the maximum Rank Bonus it "
            "can claim (as determined by its troop type) by one."
        ),
    },
    "Immune to Psychology": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/immune-to-psychology",
        "text": (
            "If the majority of the models in a unit are Immune to Psychology, the "
            "unit automatically passes any Fear, Panic or Terror tests it is "
            "required to make. However, if the majority of the models in a unit "
            "have this special rule, the unit cannot choose to Flee as a charge "
            "reaction. Note that this special rule does not make a unit immune to "
            "any test made against Leadership not stated here."
        ),
    },
    "Impact Hits": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/impact-hits",
        "text": (
            "The number of Impact Hits caused varies from model to model, and will "
            "be shown in brackets after the name of this special rule (shown here "
            "as 'X'). Often, this is determined by the roll of a dice. Resolving "
            "Impact Hits Impact Hits can only be made by a charging model that "
            "moved 3\" or more and that is in base contact with the enemy. Impact "
            "Hits are resolved against the charged unit when the combat is chosen "
            "during Step 1.1 of the Choose Combat & Fight sub-phase, before issuing "
            "challenges. They hit automatically and use the unmodified Strength of "
            "the model making them."
        ),
    },
    "Large Target": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/large-target",
        "text": (
            "Large Targets do not benefit from partial or full cover. In addition, "
            "a unit can draw a line of sight to a Large Target over or through "
            "another unit, and vice versa, provided that unit is not also a Large "
            "Target. Finally, a unit that shoots at a Large Target can shoot with "
            "one additional rank. For example, a unit armed with crossbows can "
            "shoot with its first two ranks when shooting at a Large Target, or "
            "with its first three if also standing on a hill."
        ),
    },
    "Levies": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/levies",
        "text": (
            "Models with this special rule cannot use the Inspiring Presence rule "
            "of the army's General nor the \"Hold your Ground\" rule of a Battle "
            "Standard. However, little is expected from Levies in battle. "
            "Therefore, units that do not have this special rule are not required "
            "to make a Panic test when a friendly unit of Levies Breaks and flees "
            "from combat."
        ),
    },
    "Loner": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/loner",
        "text": (
            "A character with this special rule cannot be your General and cannot "
            "join a unit without this special rule. A unit with this special rule "
            "cannot be joined by a character without this special rule."
        ),
    },
    "Lumbering Destruction": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/lumbering-destruction",
        "text": (
            "An Iron Daemon cannot march. Instead, you may roll a D6 and add its "
            "result to the model's Movement characteristic. However, if a natural 1 "
            "is rolled when making this roll, something has gone wrong deep within "
            "the infernal machine, rendering it immobile. The Iron Daemon halts "
            "immediately and cannot move again for the remainder of this turn."
        ),
    },
    "Move Through Cover": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/move-through-cover",
        "text": (
            "Models with this special rule do not suffer any modifiers to their "
            "Movement characteristic for moving through difficult or dangerous "
            "terrain. In addition, a model with this special rule may re-roll any "
            "rolls of 1 when making Dangerous Terrain tests."
        ),
    },
    "Open Order": {
        "status": None,
        "url": "https://tow.whfb.app/unusual-formations/open-order-formation",
        "text": (
            "A unit arrayed in an Open Order formation closely resembles one in a "
            "Close Order formation; the key differences lie in how the unit moves "
            "and interacts with terrain. As with a unit in Close Order, a unit in "
            "Open Order consists of two or more models that are arranged in base "
            "contact with each other, edge-to-edge and front corner to front "
            "corner, as shown in Fig 182.1. All models in such a unit must face the "
            "same direction. In addition, all models in the unit must be arranged "
            "in a formation that consists of one or more horizontal rows, called "
            "ranks, and a number of vertical rows, called files. As far as "
            "possible, there must be the same number of models in each rank. Where "
            "this is not [...]"
        ),
    },
    "Quell Panic": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/quell-panic",
        "text": (
            "Unless this unit is fleeing, any friendly unit that is within 6\" of "
            "this unit and that has the Levies special rule may re-roll a failed "
            "Panic test."
        ),
    },
    "Regeneration": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/regeneration",
        "text": (
            "Immediately after a Wound is lost, but before models with zero Wounds "
            "remaining are removed from play, a model with this special rule may "
            "make a 'Regeneration save' roll by rolling a D6 and comparing the "
            "result to its 'Regeneration value', shown in brackets after the name "
            "of this special rule (shown here as 'X+'). If the Regeneration save "
            "roll equals or exceeds the model's Regeneration value, the lost Wound "
            "is recovered, but is still counted for the purposes of calculating the "
            "combat result. Rules that affect armour values do not affect "
            "Regeneration values unless stated otherwise."
        ),
    },
    "Regimental Unit": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/regimental-unit",
        "text": (
            "A unit with this special rule can be accompanied by detachment."
        ),
    },
    "Shieldwall": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/shieldwall",
        "text": (
            "Once per game, during a turn in which it was charged, a unit with this "
            "special rule that is arrayed in a Close Order formation, and that is "
            "equipped with and chooses to use shields, may Give Ground rather than "
            "Fall Back in Good Order."
        ),
    },
    "Skirmishers": {
        "status": None,
        "url": "https://tow.whfb.app/unusual-formations/skirmish-formation",
        "text": (
            "A unit of models in Skirmish formation (often referred to as "
            "'Skirmishers' in the rules that follow) never consists of rigid ranks "
            "and files. Instead, it moves as a single loose group or rough line. "
            "This enables Skirmishers to move quickly and take advantage of terrain "
            "to shelter from the enemy."
        ),
    },
    "Stampede": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/stampede",
        "text": (
            "Impact Hits caused by a model with this special rule have an Armour "
            "Piercing characteristic of -2."
        ),
    },
    "Stomp Attacks": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/stomp-attacks",
        "text": (
            "The number of Stomp Attacks caused varies from model to model, and "
            "will be shown in brackets after the name of this special rule (shown "
            "here as 'X'). Often, this is determined by the roll of a dice. "
            "Resolving Stomp Attacks Stomp Attacks can only be made by a model that "
            "is in base contact with the enemy. Stomp Attacks are attacks made in "
            "combat that must be made last, after all other attacks have been made, "
            "including attacks made at Initiative 1. They hit automatically and use "
            "the unmodified Strength of the model making them."
        ),
    },
    "Stubborn": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/stubborn",
        "text": (
            "The first time this unit is required to make a Break test it may "
            "choose not to and will automatically Falling Back in Good Order "
            "instead, even if the Unit Strength of the winning side is more than "
            "twice that of the losing side. A unit that is not Stubborn does not "
            "become Stubborn when joined by a character that is. A Stubborn "
            "character cannot use this special rule whilst part of a unit that is "
            "not Stubborn."
        ),
    },
    "Swiftstride": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/swiftstride",
        "text": (
            "A unit which consists entirely of models with this special rule "
            "increases its maximum possible charge range by 3\" and, before making a "
            "Charge, Flee or Pursuit roll, may choose to apply a +D6 modifier to "
            "the result."
        ),
    },
    "Unbreakable": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/unbreakable",
        "text": (
            "If a unit with this special rule loses a round of combat, it is not "
            "required to make a Break test. Instead, it will automatically Give "
            "Ground as it is pushed back by the enemy. Characters that are not "
            "Unbreakable cannot join units that are, and vice versa."
        ),
    },
    "Unstable": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/unstable",
        "text": (
            "If a unit with this special rule loses a round of combat, it loses one "
            "additional Wound for every combat result point by which it lost. These "
            "Wounds are lost after combat results have been calculated but before "
            "Break tests are made. These Wounds cannot be recovered by a "
            "Regeneration save. If an Unstable unit contains any Unstable "
            "characters, allocate wounds to the unit until each model has been "
            "allocated one wound. Any remaining wounds are divided as equally as "
            "possible between the character(s) and the unit."
        ),
    },
    "Veteran": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/veteran",
        "text": (
            "If the majority of the models in a unit have this special rule, the "
            "unit may re-roll any failed Leadership test. Note that a Break test is "
            "not a Leadership test."
        ),
    },
    "Warband": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/warband",
        "text": (
            "Unless it is fleeing, a Warband gains a positive (+) modifier to its "
            "Leadership characteristic equal to its current Rank Bonus, up to a "
            "maximum of Leadership 10. However, a Warband cannot use this modifier "
            "to its Leadership should it ever choose to make a Restraint test or, "
            "if it is Impetuous, when testing to see if it must declare a charge or "
            "may act as normal. In addition, if the majority of the models in a "
            "unit have this special rule, it may re-roll its Charge roll. Note that "
            "unless a character also has this special rule, their Leadership cannot "
            "be modified by this special rule. A Warband can use either its own "
            "modified Leadership, the modified Leadership of a Warband character, "
            "or the [...]"
        ),
    },
    "Warp-spawned": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/warp-spawned",
        "text": (
            "A model with this special rule cannot make a Regeneration save against "
            "a wound caused by a Magical attack. In addition, characters that are "
            "not Warp-spawned cannot join units that are, and vice versa."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
