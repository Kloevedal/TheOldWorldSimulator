"""Vampire Counts.

Profiles from https://tow.whfb.app/army/vampire-counts, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Vampire Counts"

# Other names that should resolve to this faction.
ALIASES = [
    "Vampire Counts",
    "VC",
    "Vampires",
    "Undead",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Necromancer": "Master Necromancer",
    "Acolyte": "Necromantic Acolyte",
    "Banshee": "Tomb Banshee",
    "Ghoul King": "Strigoi Ghoul King",
}

CHARACTERS = {
    "Cairn Wraith": {
        # https://tow.whfb.app/unit/cairn-wraith - 50 pts
        "points": 50,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 6,
            "Race": "Spirit",
            "Armor": None,
            "Weapon": "Spectral Scythe",
            "Shield": False,
            "SpecialRules": ["Ethereal", "Indomitable (1)", "Necromantic Undead", "Regeneration (6+)", "Terror"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Spectral Scythe"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Master Necromancer": {
        # https://tow.whfb.app/unit/master-necromancer - 130 pts
        "points": 130,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Necromancer",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dark Vitality", "Indomitable (1)", "Invocation of Nehek", "Lore of Undeath", "Necromantic Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 3,
            "Lores": ["Dark Magic", "Illusion", "Necromancy"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Nightmare", "Mortis Engine", "Abyssal Terror", "Zombie Dragon"]
        }
    },
    "Necromantic Acolyte": {
        # https://tow.whfb.app/unit/necromantic-acolyte - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Necromancer",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dark Vitality", "Indomitable (1)", "Invocation of Nehek", "Lore of Undeath", "Necromantic Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Dark Magic", "Illusion", "Necromancy"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Nightmare", "Mortis Engine"]
        }
    },
    "Strigoi Ghoul King": {
        # https://tow.whfb.app/unit/strigoi-ghoul-king - 145 pts
        "points": 145,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 7,
            "Wounds": 3,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Vampire",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dark Vitality", "Flammable", "Hatred (all enemies)", "Indomitable (1)", "Lore of Undeath", "Necromantic Undead", "Poisoned Attacks", "Regeneration (5+)", "The Hunger"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 0,
            "Lores": ["Battle Magic", "Dark Magic", "Necromancy"],
            "OptionalRules": ["Vampiric Powers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Terrorgheist"]
        }
    },
    "Tomb Banshee": {
        # https://tow.whfb.app/unit/tomb-banshee - 90 pts
        "points": 90,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Spirit",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ethereal", "Indomitable (1)", "Magical Attacks", "Necromantic Undead", "Regeneration (6+)", "Terror", "Wailing Dirge"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
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
    "Vampire Count": {
        # https://tow.whfb.app/unit/vampire-count - 160 pts
        "points": 160,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 7,
            "BallisticSkill": 5,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Vampire",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dark Vitality", "Flammable", "Indomitable (2)", "Lore of Undeath", "Necromantic Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 0,
            "Lores": ["Dark Magic", "Illusion", "Necromancy"],
            "OptionalRules": ["Vampiric Powers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Lance"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Nightmare", "Coven Throne", "Abyssal Terror", "Zombie Dragon"]
        }
    },
    "Vampire Thrall": {
        # https://tow.whfb.app/unit/vampire-thrall - 75 pts
        "points": 75,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Vampire",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Banner of the Count", "Dark Vitality", "Flammable", "Indomitable (1)", "Lore of Undeath", "Necromantic Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 0,
            "Lores": ["Dark Magic", "Illusion", "Necromancy"],
            "OptionalRules": ["Vampiric Powers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Lance"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Nightmare", "Coven Throne"]
        }
    },
    "Wight King": {
        # https://tow.whfb.app/unit/wight-king - 85 pts
        "points": 85,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Wight",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Indomitable (1)", "Killing Blow", "Necromantic Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Vampire Counts)"]
        }
    },
    "Wight Lord": {
        # https://tow.whfb.app/unit/wight-lord - 40 pts
        "points": 40,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Wight",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Killing Blow", "Necromantic Undead", "Regeneration (6+)", "Wight Banner"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Vampire Counts)"]
        }
    },
}

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Bat Swarms": {
        # https://tow.whfb.app/unit/bat-swarms - 39 pts per model, unit size 3+
        # Fights with the Bat Swarm row.
        "points": 39,
        "points_per": "model",
        "unit_size": "3+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 1,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 2,
            "Toughness": 2,
            "Initiative": 4,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 3,
            "Race": "Undead",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fly (7)", "Necromantic Undead", "Regeneration (6+)", "Skirmishers"],
            "TroopType": "Swarm",
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
    "Crypt Ghouls": {
        # https://tow.whfb.app/unit/crypt-ghouls - 9 pts per model, unit size 10+
        # Fights with the Crypt Ghoul row.
        "points": 9,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Crypt Ghast', 'Movement': 5, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 3, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 5,
            "Race": "Ghoul",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Move Through Cover", "Necromantic Undead", "Open Order", "Poisoned Attacks", "Regeneration (6+)", "Reserve Move", "Skirmishers"],
            "TroopType": "RegularInfantry",
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
    "Crypt Horrors": {
        # https://tow.whfb.app/unit/crypt-horrors - 46 pts per model, unit size 3+
        # Fights with the Crypt Horror row.
        "points": 46,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Crypt Haunter', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': 0, 'Strength': 4, 'Toughness': 5, 'Initiative': 2, 'Wounds': 3, 'Attacks': 4, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 5,
            "Race": "Ghoul",
            "Armor": None,
            "Weapon": "Filth-Encrusted Claws",
            "Shield": False,
            "SpecialRules": ["Indomitable (1)", "Move Through Cover", "Necromantic Undead", "Open Order", "Regeneration (6+)", "Stomp Attacks (1)"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Filth-Encrusted Claws"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Fell Bats": {
        # https://tow.whfb.app/unit/fell-bats - 15 pts per model, unit size 3+
        # Fights with the Fell Bat row.
        "points": 15,
        "points_per": "model",
        "unit_size": "3+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 1,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 3,
            "Race": "Undead",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fly (10)", "Necromantic Undead", "Regeneration (6+)", "Skirmishers", "Swiftstride"],
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
    "Grave Guard": {
        # https://tow.whfb.app/unit/grave-guard - 11 pts per model, unit size 10+
        # Fights with the Grave Guard row.
        "points": 11,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Seneschal', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Undead",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Cleaving Blow", "Close Order", "Indomitable (1)", "Necromantic Undead", "Regeneration (6+)"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled", "Implacable Defence"],
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
    "Skeleton Warriors (Vampire Counts)": {
        # https://tow.whfb.app/unit/skeleton-warriors-vampire-counts - 5 pts per
        # model, unit size 10+
        # Fights with the Skeleton Warrior row.
        "points": 5,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Skeleton Champion', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Undead",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Horde", "Necromantic Undead", "Regeneration (6+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Thrusting Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Spirit Hosts": {
        # https://tow.whfb.app/unit/spirit-hosts - 49 pts per model, unit size 3-6
        # Fights with the Spirit Host row.
        "points": 49,
        "points_per": "model",
        "unit_size": "3-6",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 1,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 4,
            "Race": "Undead",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Bound Spirits", "Ethereal", "Magical Attacks", "Necromantic Undead", "Open Order", "Regeneration (6+)", "Reserve Move"],
            "TroopType": "Swarm",
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
    "Vargheists": {
        # https://tow.whfb.app/unit/vargheists - 61 pts per model, unit size 3+
        # Fights with the Vargheist row.
        "points": 61,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Vargoyle', 'Movement': 6, 'WeaponSkill': 4, 'BallisticSkill': 0, 'Strength': 5, 'Toughness': 4, 'Initiative': 4, 'Wounds': 3, 'Attacks': 4, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Vampire",
            "Armor": None,
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2)", "Dark Vitality", "Flammable", "Fly (9)", "Frenzy", "Indomitable (1)", "Necromantic Undead", "Regeneration (6+)", "Skirmishers"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Wicked Claws"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Zombies": {
        # https://tow.whfb.app/unit/zombies - 3 pts per model, unit size 20-40
        # Fights with the Zombies row.
        "points": 3,
        "points_per": "model",
        "unit_size": "20-40",
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 1,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 2,
            "Race": "Undead",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Necromantic Undead", "Regeneration (6+)", "The Newly Dead"],
            "TroopType": "RegularInfantry",
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
    "Black Knights": {
        # https://tow.whfb.app/unit/black-knights - 24 pts per model, unit size 5+
        # Fights with the Black Knight row.
        # Also has a profile for Skeletal Steed (M7 WS2 BS- S3 T- W- I2 A1 Ld-); not
        # simulated.
        "points": 24,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Hell Knight', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 0, 'Strength': 4, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [
            {'Name': 'Skeletal Steed', 'Movement': 7, 'WeaponSkill': 2, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Undead",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Cleaving Blow (Riders only)", "Close Order", "First Charge", "Necromantic Undead", "Regeneration (6+)", "Swiftstride"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Barding"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Blood Knights": {
        # https://tow.whfb.app/unit/blood-knights - 39 pts per model, unit size 5+
        # Fights with the Blood Knight row.
        # Also has a profile for Nightmare (M7 WS3 BS- S4 T- W- I2 A1 Ld-); not
        # simulated.
        "points": 39,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Kastellan', 'Movement': None, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 1, 'Attacks': 3, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Nightmare', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Vampire",
            "Armor": "Heavy Armor",
            "Weapon": "Lance",
            "Shield": True,
            "SpecialRules": ["Accursed Weapons", "Close Order", "Counter Charge", "Dark Vitality", "First Charge", "Flammable", "Indomitable (1)", "Martial Pride", "Necromantic Undead", "Regeneration (6+)", "Swiftstride"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled", "Vampiric Powers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Lance"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Dire Wolves": {
        # https://tow.whfb.app/unit/dire-wolves - 8 pts per model, unit size 5-20
        # Fights with the Dire Wolf row.
        "points": 8,
        "points_per": "model",
        "unit_size": "5-20",
        "champion": {'Name': 'Doom Wolf', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': 0, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 3},
        "other_profiles": [],
        "base_profile": {
            "Movement": 9,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 3,
            "Race": "Undead",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Necromantic Undead", "Open Order", "Regeneration (6+)", "Reserve Move", "Slavering Charge", "Swiftstride", "Vanguard"],
            "TroopType": "WarBeast",
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
    "Hexwraiths": {
        # https://tow.whfb.app/unit/hexwraiths - 31 pts per model, unit size 5-10
        # Fights with the Hexwraith row.
        # Also has a profile for Spectral Steed (M8 WS2 BS- S3 T- W- I2 A1 Ld-); not
        # simulated.
        "points": 31,
        "points_per": "model",
        "unit_size": "5-10",
        "champion": {'Name': 'Hellwraith', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 0, 'Strength': 3, 'Toughness': 3, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [
            {'Name': 'Spectral Steed', 'Movement': 8, 'WeaponSkill': 2, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Undead",
            "Armor": None,
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Ethereal", "Flaming Attacks", "Fly (8)", "Magical Attacks", "Necromantic Undead", "Open Order", "Regeneration (6+)", "Spectral Reapers", "Swiftstride", "Terror"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Black Coach": {
        # https://tow.whfb.app/unit/black-coach - 205 pts per unit
        # Fights with the Wraith (x1) row, using the Black Coach row's Toughness and
        # Wounds.
        # Also has a profile for Black Coach (M- WS- BS- S5 T6 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Nightmares (x2) (M8 WS3 BS- S4 T- W- I2 A1 Ld-); not
        # simulated.
        # Armour value 3+ as printed on the site.
        "points": 205,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Black Coach', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 6, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Nightmares (x2)', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 6,
            "Initiative": 2,
            "Wounds": 4,
            "Attacks": 2,
            "Leadership": 5,
            "Race": "Undead",
            "Armor": "Armour Value 3+",
            "Weapon": "Spectral Scythe (Black Coach)",
            "Shield": False,
            "SpecialRules": ["Close Order", "First Charge", "Impact Hits (D6+2)", "Indomitable (1)", "Magical Attacks", "Necromantic Undead", "Regeneration (6+)", "Spectral Coach", "Terror"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Spectral Scythe (Black Coach)"],
            "armor": ["Armour Value 3+"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Corpse Cart": {
        # https://tow.whfb.app/unit/corpse-cart - 115 pts per unit
        # Fights with the Corpsemaster (x1) row, using the Corpse Cart row's Toughness
        # and Wounds.
        # Also has a profile for Corpse Cart (M- WS- BS- S4 T4 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for The Restless Dead (M4 WS1 BS0 S3 T- W- I1 A2D6 Ld-);
        # not simulated.
        # Armour value 4+ as printed on the site.
        "points": 115,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Corpse Cart', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 4, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'The Restless Dead', 'Movement': 4, 'WeaponSkill': 1, 'BallisticSkill': 0, 'Strength': 3, 'Toughness': None, 'Initiative': 1, 'Wounds': None, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Undead",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Dark Vitality", "First Charge", "Impact Hits (D3+1)", "Indomitable (1)", "Lore of Undeath", "Necromantic Undead", "Random Attacks (The Restless Dead only)", "Regeneration (6+)"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
            "WizardLevel": 1,
            "Lores": ["Necromancy"],
            "OptionalRules": ["Balefire Brazier", "Warped Tintinnabulation"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Whip", "Cavalry Spear"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Terrorgheist": {
        # https://tow.whfb.app/unit/terrorgheist - 205 pts per unit
        # Fights with the Terrorgheist row.
        "points": 205,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 3,
            "Wounds": 6,
            "Attacks": 4,
            "Leadership": 4,
            "Race": "Undead",
            "Armor": "Light Armor",
            "Weapon": "Filth-Encrusted Talons",
            "Shield": False,
            "SpecialRules": ["Close Order", "Fly (9)", "Indomitable (1)", "Infested", "Large Target", "Necromantic Undead", "Regeneration (5+)", "Stomp Attacks (D6)", "Swiftstride", "Terror", "Wailing Dirge"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Filth-Encrusted Talons", "Rancid Maw"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Varghulf": {
        # https://tow.whfb.app/unit/varghulf - 140 pts per unit
        # Fights with the Varghulf row.
        "points": 140,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 4,
            "Race": "Vampire",
            "Armor": "Light Armor",
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Bestial Fury", "Close Order", "Counter Charge", "Dark Vitality", "Flammable", "Frenzy", "Indomitable (1)", "Necromantic Undead", "Regeneration (5+)", "Swiftstride", "Terror"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Wicked Claws"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
}


# Special rules carried by this faction's characters and units. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {
    "Accursed Weapons": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/accursed-weapons",
        "text": (
            "A hand weapon carried by a model with this special rule has the "
            "Magical Attacks special rule and an Armour Piercing characteristic of "
            "-1."
        ),
    },
    "Armour Bane": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/armour-bane",
        "text": (
            "If a model with this special rule rolls a natural 6 when making a roll "
            "To Wound, the Armour Piercing characteristic of its weapon is improved "
            "by the amount shown in brackets after the name of this special rule "
            "(shown here as 'X'). For example, if a natural 6 is rolled when "
            "rolling To Wound with a weapon that has an AP of ' - ' and the Armour "
            "Bane (1) special rule, its AP counts as being -1 when making an Armour "
            "Save roll against that wound."
        ),
    },
    "Banner of the Count": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/banner-of-the-count",
        "text": (
            "A Vampire Thrall that has been upgraded to be your Battle Standard "
            "Bearer replaces the \"Hold your Ground\" rule given in the Warhammer: "
            "the Old World rulebook with the version given below: \"Hold Your "
            "Ground\" Friendly units within the Battle Standard Bearer's Command "
            "range may re-roll any failed Leadership test. In addition, friendly "
            "units within the Battle Standard Bearer's Command range reduce the "
            "number of Wounds lost due to the Unstable special rule by D3. Note "
            "that this is not cumulative with the Indomitable (X) special rule. If "
            "a unit is affected by both, use the highest value."
        ),
    },
    "Bestial Fury": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/bestial-fury",
        "text": (
            "Enemy units cannot claim any bonus combat result points for being "
            "engaged with this model's flank or rear arc."
        ),
    },
    "Bound Spirits": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/bound-spirits",
        "text": (
            "Unlike other swarms, this unit is not subject to the Undisciplined "
            "rule. In other words, this unit can use the Inspiring Presence rule of "
            "the army's General and the \"Hold your Ground\" rule of a Battle "
            "Standard."
        ),
    },
    "Cleaving Blow": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/cleaving-blow",
        "text": (
            "If a model with this special rule rolls a natural 6 when making a roll "
            "To Wound for an attack made in combat, it has struck a 'Cleaving "
            "Blow'. Enemy models whose troop type is regular infantry, heavy "
            "infantry, light cavalry, heavy cavalry or war beasts are not permitted "
            "an armour or Regeneration save against a Cleaving Blow (Ward saves can "
            "be attempted as normal). Note that if an attack wounds automatically, "
            "this special rule cannot be used."
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
    "Counter Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/counter-charge",
        "text": (
            "This special rule can only be used by units that consist entirely of "
            "models with this special rule. When a unit with this special rule is "
            "charged in its front arc by an enemy unit whose troop type is cavalry, "
            "chariot or monster, it may declare a 'Counter Charge' charge reaction: "
            "Counter Charge The unit surges forward to meet the enemy charge. "
            "Measure the distance between the two units. If the distance is less "
            "than the Movement characteristic of the charging unit, the charged "
            "unit has not enough time to meet the enemy charge and must either Hold "
            "or Flee instead. Otherwise, pivot the unit about its centre so that it "
            "is facing directly towards the centre of the charging enemy unit. "
            "After [...]"
        ),
    },
    "Dark Vitality": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dark-vitality",
        "text": (
            "Models with this special rule are not subject to the Death of a "
            "General rule. In addition, unless they have joined a unit that does "
            "not have this special rule they (and their mounts) can march as "
            "normal."
        ),
    },
    "Ethereal": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/ethereal",
        "text": (
            "Ethereal creatures treat all terrain as open ground for the purposes "
            "of movement. They cannot end their movement inside impassable terrain, "
            "though they can pass through it. In addition, Ethereal creatures can "
            "only be wounded by Magical attacks. Characters that are not Ethereal "
            "cannot join units that are, and vice versa."
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
    "Flammable": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/flammable",
        "text": (
            "A model with this special rule cannot make a Regeneration save against "
            "a wound caused by a Flaming attack."
        ),
    },
    "Fly": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fly",
        "text": (
            "Except when following up or pursuing, a model with this special rule "
            "can choose to move by flying through the air, rather than moving "
            "across the ground as normal. When a model flies it uses a special ‘Fly "
            "Movement’ characteristic, shown in brackets after the name of this "
            "special rule (shown here as ‘X’). Models that choose to move by "
            "flying: - May move as normal (i.e., they may charge, march and "
            "manoeuvre as if moving on the ground), except that they are able to "
            "pass freely above other models, units and terrain features without any "
            "penalty, and they can march whilst within 8\" of an enemy unit without "
            "first having to make a Leadership test. - May end their movement in "
            "terrain, but will [...]"
        ),
    },
    "Frenzy": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/frenzy",
        "text": (
            "During a turn in which it made a charge move, or during the turn after "
            "it made a follow up move, a Frenzied model has a +1 modifier to its "
            "Attacks characteristic. This modifier does not apply to the model’s "
            "mount (in the case of a cavalry model), to the beasts that draw it (in "
            "the case of a chariot), or to its rider (in the case of a monster). In "
            "addition: - If the majority of the models in a unit are Frenzied, the "
            "unit automatically passes any Fear, Panic or Terror tests it is "
            "required to make. - If a unit that includes one or more Frenzied "
            "models is able to declare a charge during the Declare Charges & Charge "
            "Reactions sub-phase of its turn, it must do so. - If the majority of "
            "the models [...]"
        ),
    },
    "Hatred": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/hatred",
        "text": (
            "A model with this special rule may re-roll any failed rolls To Hit "
            "made against a hated enemy during the first round of combat. Which "
            "enemies are hated varies from model to model and will be shown in "
            "brackets after the name of this special rule (shown here as 'X'). Some "
            "models hate 'all enemies', meaning they hate all enemy models equally."
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
    "Indomitable": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/indomitable",
        "text": (
            "A unit with this special rule reduces the number of wounds suffered "
            "due to the Unstable special rule by the number shown in brackets "
            "(shown here as 'X'). Note that this special rule is not cumulative. If "
            "two or more models in a unit have this special rule, use the highest "
            "value for the entire unit. For example, if a character with "
            "Indomitable (2) joins a unit with Indomitable (1), the whole unit uses "
            "the character's Indomitable (2) special rule."
        ),
    },
    "Infested": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/infested",
        "text": (
            "When this model loses its last Wound, every unit in base contact with "
            "it (friend or foe) suffers D6 Strength 2 hits, each with an AP of -1."
        ),
    },
    "Invocation of Nehek": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/invocation-of-nehek",
        "text": (
            "During the Command sub-phase of their turn, if they are not engaged in "
            "combat, this character may attempt to resurrect the fallen by making a "
            "Leadership test (using their own Leadership). If this test is passed, "
            "a single friendly unit that has the Necromantic Undead special rule "
            "and is within 12\" of this character recovers a number of lost Wounds. "
            "However, magically repairing great Undead beasts is much harder than "
            "raising Zombies from the dirt. Therefore, how many Wounds are "
            "recovered depends upon the unit's troop type and this character's "
            "Level of Wizardry: - If the unit's troop type is regular infantry or "
            "heavy infantry, it recovers a number of Wounds equal to this "
            "character's Level of [...]"
        ),
    },
    "Killing Blow": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/killing-blow",
        "text": (
            "If a model with this special rule rolls a natural 6 when making a roll "
            "To Wound for an attack made in combat, it has struck a 'Killing Blow'. "
            "Enemy models whose troop type is infantry or cavalry are not permitted "
            "an armour or Regeneration save against a Killing Blow (Ward saves can "
            "be attempted as normal). If an enemy model whose troop type is "
            "infantry or cavalry suffers an unsaved wound from a Killing Blow, it "
            "loses all of its remaining Wounds. Note that if an attack wounds "
            "automatically, this special rule cannot be used."
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
    "Lore of Undeath": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-undeath",
        "text": (
            "Mystery shrouds the study of Necromancy. To learn this dark art, an "
            "aspirant must find a willing tutor and become their apprentice, or "
            "acquire forbidden books rich in the secrets of undeath. It is this "
            "intrinsic mystery that drives Necromancers to become servants of the "
            "Vampire Counts, hoping to learn first-hand from the masters of "
            "undeath. A Wizard with the 'Lore of Undeath' special rule may discard "
            "one of their randomly generated spells as normal. When they do so, "
            "they may select instead either the signature spell of their chosen "
            "Lore of Magic, or one of the spells listed below. Lore of Undeath Lore"
        ),
    },
    "Magical Attacks": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/magical-attacks",
        "text": (
            "Any attack made or hit caused by a model with this special rule, or "
            "made using a weapon with this special rule, is a 'Magical' attack. "
            "Note that all spells are considered to have this special rule, as are "
            "any hits caused by magic items."
        ),
    },
    "Martial Pride": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/martial-pride",
        "text": (
            "Every model in a unit of Blood Knights can issue and accept challenges "
            "in the same manner as a character. However, a unit with this special "
            "rule cannot refuse a challenge – if a challenge is issued and a model "
            "belonging to this unit could accept it, a model belonging to the unit "
            "must accept it."
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
    "Necromantic Undead": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/necromantic-undead",
        "text": (
            "Models with this special rule are 'Undead'. Undead models cannot march "
            "(unless they have the Fly (X) special rule and choose to move by "
            "flying). In addition, all Undead models have the following universal "
            "special rules: - Fear - Immune To Psychology - Unbreakable - Unstable "
            "A character with this special rule cannot join a unit without this "
            "special rule, and vice versa."
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
    "Poisoned Attacks": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/poisoned-attacks",
        "text": (
            "If a model with Poisoned Attacks rolls a natural 6 when making a roll "
            "To Hit, it may apply a +2 modifier to that hit’s roll To Wound. Unless "
            "otherwise stated, a model with this special rule may use it when "
            "making both shooting and combat attacks. Any spells cast by the model "
            "are unaffected, as are any attacks made with magic weapons. Note that "
            "if an attack needs a To Hit roll of 7+, or hits automatically, this "
            "special rule cannot be used."
        ),
    },
    "Random Attacks": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/random-attacks",
        "text": (
            "Models with this special rule do not have a normal Attacks "
            "characteristic. Instead, a dice roll is given (D3+1, for example). "
            "Each time a model with this special rule attacks in combat, roll the "
            "dice to determine the number of attacks it will make, then roll To Hit "
            "as normal. If a fighting rank contains more than one model with this "
            "special rule, roll separately for each, unless specified otherwise."
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
    "Reserve Move": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/reserve-move",
        "text": (
            "Unless it charged, marched or fled during the Movement phase, a unit "
            "in which the majority of the models have this special rule may make a "
            "Reserve move at the end of the Shooting phase of its turn, after all "
            "shooting has been resolved. A unit making a Reserve move moves as "
            "described in the Basic Movement rules. It may manoeuvre normally, but "
            "cannot march."
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
    "Slavering Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/slavering-charge",
        "text": (
            "During a turn in which it charged, this model has a +1 modifier to its "
            "Strength characteristic."
        ),
    },
    "Spectral Coach": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/spectral-coach",
        "text": (
            "A Black Coach is not wholly corporeal. To represent this, a Black "
            "Coach may become 'Incorporeal' during the Command sub-phase of its "
            "turn, and will remain Incorporeal until your next Start of Turn sub- "
            "phase. Whilst Incorporeal, a Black Coach: - Loses the Impact Hits "
            "(D6+2) special rule. - Gains the Ethereal and Fly (10) special rules."
        ),
    },
    "Spectral Reapers": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/spectral-reapers",
        "text": (
            "A unit with this special rule may perform a 'Spectral Reapers' attack "
            "against a single enemy unit that is not engaged in combat. To do so, "
            "this unit must move (by flying) over the unit it wishes to attack "
            "during the Remaining Moves sub-phase. Once this unit's movement is "
            "complete, the enemy unit suffers a single Strength 4 hit, with no "
            "armour save permitted (Ward and Regeneration saves can be attempted as "
            "normal), and with the Flaming Attacks and Magical Attacks special "
            "rules, for each model in this unit that moved over it."
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
    "Terror": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/terror",
        "text": (
            "Models with this special rule cause Terror. Models that cause Terror "
            "also cause Fear: - When a unit that causes Terror declares a charge, "
            "the charge target must immediately make a Leadership test. If this "
            "test is failed, it must Flee. If this test is passed, it can declare "
            "its charge reaction normally. - If the winning side of a combat "
            "includes one or more units that cause Terror, each unit that belongs "
            "to the losing side must apply a -1 modifier to its Leadership "
            "characteristic when making its Break test. Note that if a charged unit "
            "cannot choose to Flee, it does not make this Leadership test. Models "
            "with the Fear special rule Fear models that cause Terror. Models that "
            "cause Terror are [...]"
        ),
    },
    "The Hunger": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/the-hunger",
        "text": (
            "At the end of any Combat phase in which this character inflicted one "
            "or more unsaved wounds, roll a D6. On a roll of 6, this character "
            "recovers a single lost Wound. However, so great is this character's "
            "hunger that, whenever they (and any unit they have joined) make a "
            "Pursuit roll, they roll only a single D6 (rather than the usual 2D6)."
        ),
    },
    "The Newly Dead": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/the-newly-dead",
        "text": (
            "When resurrecting the fallen, a unit with this special rule can be "
            "taken beyond its starting size (but not beyond its maximum size)."
        ),
    },
    "Vanguard": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/vanguard",
        "text": (
            "After deployment, units with this special rule may make a Vanguard "
            "move. A unit making a Vanguard move moves as described in the Basic "
            "Movement rules. It may manoeuvre normally but cannot march. If both "
            "armies contain Vanguard units, a roll-off determines who moves first. "
            "The players then alternate moving their Vanguard units one at a time, "
            "starting with the player who won the roll-off. Units that make a "
            "Vanguard move cannot declare a charge during their first turn."
        ),
    },
    "Wailing Dirge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/wailing-dirge",
        "text": (
            "During the Shooting phase of its turn, unless it marched during the "
            "preceding Movement phase, a model with this special rule may make a "
            "'Wailing Dirge' attack. A Wailing Dirge attack may target any enemy "
            "unit that is within 8\" of this model (including units that are engaged "
            "in combat) and that this model can draw a line of sight to, or that "
            "this model is engaged in combat with. The target must make a "
            "Leadership test with a -2 modifier to its Leadership characteristic "
            "(to a minimum of 2). If this test is failed, the target suffers a "
            "number of wounds equal to the amount by which it failed the test, with "
            "no armour or Regeneration saves permitted (Ward saves can be attempted "
            "as normal). Note [...]"
        ),
    },
    "Wight Banner": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/wight-banner",
        "text": (
            "A Wight Lord that has been upgraded to be your Battle Standard Bearer "
            "replaces the \"Hold your Ground\" rule given in the Warhammer: the Old "
            "World rulebook with the version given below: \"Hold Your Ground\" "
            "Friendly units within the Battle Standard Bearer's Command range may "
            "re-roll any failed Leadership test. In addition, friendly units within "
            "the Battle Standard Bearer's Command range reduce the number of Wounds "
            "lost due to the Unstable special rule by D3. Note that this is not "
            "cumulative with the Indomitable (X) special rule. If a unit is "
            "affected by both, use the highest value."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
