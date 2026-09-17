"""Dark Elves.

Profiles from https://tow.whfb.app/army/dark-elves
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Dark Elves"

# Other names that should resolve to this faction.
ALIASES = [
    "Druchii",
    "Dark Elf",
    "Dark Elves",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Dark Elf Dreadlord": "Dreadlord",
    "Dark Elf Master": "Master",
    "Assassin": "Khainite Assassin",
}

CHARACTERS = {
    "Dreadlord": {
        # https://tow.whfb.app/unit/dark-elf-dreadlord - 130 pts
        # Hatred and Strike First do not apply to his mount. Repeater crossbows and
        # handbows are shooting, which is not simulated.
        "points": 130,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 7,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Eternal Hatred", "Hatred (High Elves)", "Murderous", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd", "Lance"],
            "armor": ["Light Armor", "Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Dark Steed", "Cold One (Dark Elves)", "Cold One Chariot", "Black Dragon", "Manticore (Dark Elves)"]
        }
    },
    "Master": {
        # https://tow.whfb.app/unit/dark-elf-master - 70 pts
        "points": 70,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 6,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Eternal Hatred", "Hatred (High Elves)", "Murderous", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd", "Lance"],
            "armor": ["Light Armor", "Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Dark Steed", "Cold One (Dark Elves)", "Cold One Chariot"]
        }
    },
    "Supreme Sorceress": {
        # https://tow.whfb.app/unit/supreme-sorceress - 150 pts
        "points": 150,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Eternal Hatred", "Hatred (High Elves)", "Hekarti's Blessing", "Lore of Naggaroth", "Murderous"],
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Elementalism", "Illusion"],
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
            "mounts": ["Dark Steed", "Cold One (Dark Elves)", "Dark Pegasus", "Black Dragon"]
        }
    },
    "Sorceress": {
        # https://tow.whfb.app/unit/sorceress - 75 pts
        "points": 75,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Eternal Hatred", "Hatred (High Elves)", "Hekarti's Blessing", "Lore of Naggaroth", "Murderous"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Elementalism", "Illusion"],
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
            "mounts": ["Dark Steed", "Cold One (Dark Elves)", "Dark Pegasus"]
        }
    },
    "Khainite Assassin": {
        # https://tow.whfb.app/unit/khainite-assassin - 80 pts
        # Carries throwing weapons as standard, and may take a forbidden poison;
        # neither is simulated.
        "points": 80,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 8,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 7,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Eternal Hatred", "Hatred (all enemies)", "Hidden", "Immune to Psychology", "Murderous", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Death Hag": {
        # https://tow.whfb.app/unit/death-hag - 70 pts
        # Fights with two hand weapons as standard. Gifts of Khaine are not
        # modelled.
        "points": 70,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 6,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 7,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Two Hand Weapons",
            "Shield": False,
            "SpecialRules": ["Eternal Hatred", "Frenzy", "Hatred (all enemies)", "Loner", "Murderous", "Poisoned Attacks", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Two Hand Weapons", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Cauldron of Blood"]
        }
    },
    "High Beastmaster": {
        # https://tow.whfb.app/unit/high-beastmaster - 75 pts
        # Movement is '-' on the profile: a mount is compulsory and supplies it.
        # Mounts are not simulated, so he fights on foot here.
        "points": 75,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 7,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Eternal Hatred", "Goad Beast", "Hatred (High Elves)", "Murderous", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Whip", "Cavalry Spear"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Scourgerunner Chariot", "Manticore (Dark Elves)"]
        }
    },
}

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Black Ark Corsairs": {
        # https://tow.whfb.app/unit/black-ark-corsairs - 11 pts per model, unit size
        # 10+
        # Fights with the Corsair row.
        # Shooting is not simulated, so these are left out of the options: Repeater
        # handbows.
        "points": 11,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Reaver', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Hatred (High Elves)", "Move Through Cover", "Open Order", "Sea Dragon Cloak"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Black Guard of Naggarond": {
        # https://tow.whfb.app/unit/black-guard-of-naggarond - 15 pts per model, unit
        # size 10+
        # Fights with the Black Guard row.
        "points": 15,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Tower Master', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dark Elf",
            "Armor": "Full Plate Armor",
            "Weapon": "Dread Halberd",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Eternal Hatred", "Hatred (High Elves)", "Immune to Psychology", "Martial Prowess", "Stubborn"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Dread Halberd"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Dark Elf Shades": {
        # https://tow.whfb.app/unit/dark-elf-shades - 15 pts per model, unit size 5+
        # Fights with the Shade row.
        # Shooting is not simulated, so these are left out of the options: repeater
        # crossbows.
        "points": 15,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Bloodshade', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 6, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 5,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Evasive", "Hatred (High Elves)", "Move Through Cover", "Scouts", "Skirmishers"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers", "Chariot Runners", "Veteran"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Dark Elf Warriors": {
        # https://tow.whfb.app/unit/dark-elf-warriors - 8 pts per model, unit size 10+
        # Fights with the Dark Elf Warrior row.
        "points": 8,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Lordling', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Hatred (High Elves)", "Martial Prowess"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Veteran"],
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
    "Har Ganeth Executioners": {
        # https://tow.whfb.app/unit/har-ganeth-executioners - 15 pts per model, unit
        # size 10+
        # Fights with the Executioner row.
        "points": 15,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Draich Master', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dark Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Har Ganeth Greatsword",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Hatred (High Elves)", "Murderous", "Veteran"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Har Ganeth Greatsword"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Harpies": {
        # https://tow.whfb.app/unit/harpies - 11 pts per model, unit size 5+
        # Fights with the Harpy row.
        "points": 11,
        "points_per": "model",
        "unit_size": "5+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 6,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fly (10)", "Move Through Cover", "Scouts", "Skirmishers", "Swiftstride"],
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
    "Repeater Crossbowmen": {
        # https://tow.whfb.app/unit/repeater-crossbowmen - 11 pts per model, unit size
        # 10+
        # Fights with the Repeater Crossbowman row.
        # Shooting is not simulated, so these are left out of the options: repeater
        # crossbows.
        "points": 11,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Lordling', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Hatred (High Elves)", "Martial Prowess"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Veteran"],
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
    "Sisters of Slaughter": {
        # https://tow.whfb.app/unit/sisters-of-slaughter - 17 pts per model, unit size
        # 10+
        # Fights with the Sister of Slaughter row.
        "points": 17,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Hag', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 6, 'Wounds': 1, 'Attacks': 3, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Lash & Buckler",
            "Shield": False,
            "SpecialRules": ["Dance of Death", "Elven Reflexes", "Hatred (High Elves)", "Impetuous", "Loner", "Murderous", "Open Order"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Lash & Buckler"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Witch Elves": {
        # https://tow.whfb.app/unit/witch-elves - 11 pts per model, unit size 10+
        # Fights with the Witch Elf row.
        "points": 11,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Hag', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Two Hand Weapons",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Frenzy", "Hatred (High Elves)", "Horde", "Loner", "Murderous", "Poisoned Attacks"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Two Hand Weapons"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Cold One Knights": {
        # https://tow.whfb.app/unit/cold-one-knights - 31 pts per model, unit size 5+
        # Fights with the Cold One Knight row.
        # Also has a profile for Cold One (M7 WS3 BS- S4 T- W- I2 A2 Ld-); not
        # simulated.
        "points": 31,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Dread Knight', 'Movement': None, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 4, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [
            {'Name': 'Cold One', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dark Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Lance",
            "Shield": True,
            "SpecialRules": ["Armour Bane (1, Cold One only)", "Armoured Hide (1)", "Close Order", "Elven Reflexes", "Fear", "First Charge", "Hatred (High Elves)", "Stupidity", "Swiftstride"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
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
    "Dark Riders": {
        # https://tow.whfb.app/unit/dark-riders - 16 pts per model, unit size 5+
        # Fights with the Dark Rider row.
        # Also has a profile for Dark Steed (M9 WS3 BS- S3 T- W- I4 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Repeater
        # crossbows.
        "points": 16,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Herald', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Dark Steed', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Fast Cavalry", "Hatred (High Elves)", "Open Order", "Skirmishers", "Swiftstride"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Fire & Flee", "Scouts"],
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
    "Doomfire Warlocks": {
        # https://tow.whfb.app/unit/doomfire-warlocks - 22 pts per model, unit size 5+
        # Fights with the Doomfire Warlock row.
        # Also has a profile for Dark Steed (M9 WS3 BS- S3 T- W- I4 A1 Ld-); not
        # simulated.
        "points": 22,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Master', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Dark Steed', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Cursed Coven", "Dark Runes", "Ward5 (non-magical)", "Elven Reflexes", "Fast Cavalry", "Hatred (High Elves)", "Open Order", "Poisoned Attacks (Riders only)", "Swiftstride"],
            "TroopType": "LightCavalry",
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
    "Bloodwrack Shrine": {
        # https://tow.whfb.app/unit/bloodwrack-shrine - 175 pts per unit
        # Fights with the Shrinekeeper (x2) row, using the Bloodwrack Shrine row's
        # Toughness and Wounds.
        # Also has a profile for Bloodwrack Shrine (M2 WS- BS- S5 T5 W5 I- A- Ld-);
        # not simulated.
        # Also has a profile for Bloodwrack Medusa (M- WS5 BS5 S4 T- W- I5 A3 Ld-);
        # not simulated.
        # Armour value 4+ as printed on the site.
        "points": 175,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Bloodwrack Shrine', 'Movement': 2, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 5, 'Attacks': None, 'Leadership': None},
            {'Name': 'Bloodwrack Medusa', 'Movement': None, 'WeaponSkill': 5, 'BallisticSkill': 5, 'Strength': 4, 'Toughness': None, 'Initiative': 5, 'Wounds': None, 'Attacks': 3, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 5,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": "Full Plate Armor",
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Close Order", "Dragged Along", "Elven Reflexes", "Frenzy", "Hatred (High Elves)", "Impact Hits (D6+1)", "Large Target", "Magic Resistance (-1)", "Murderous", "Poisoned Attacks", "Stony Stare", "Terror"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Cavalry Spear"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Cold One Chariot": {
        # https://tow.whfb.app/unit/cold-one-chariot - 125 pts per unit
        # Fights with the Knight Charioteer (x2) row, using the Chariot row's
        # Toughness and Wounds.
        # Also has a profile for Chariot (M- WS- BS- S5 T5 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Cold One (x2) (M7 WS3 BS- S4 T- W- I2 A2 Ld-); not
        # simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: repeater
        # crossbows.
        "points": 125,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Cold One (x2)', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dark Elf",
            "Armor": "Full Plate Armor",
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1, Cold One only)", "Close Order", "Elven Reflexes", "Fear", "First Charge", "Hatred (High Elves)", "Impact Hits (D6+1)", "Stupidity"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Scourgerunner Chariot": {
        # https://tow.whfb.app/unit/scourgerunner-chariot - 85 pts per model, unit
        # size 1-3
        # Fights with the Beastmaster Crew (x2) row, using the Chariot row's Toughness
        # and Wounds.
        # Also has a profile for Chariot (M- WS- BS- S4 T4 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Dark Steed (x2) (M9 WS3 BS- S3 T- W- I4 A1 Ld-); not
        # simulated.
        # Armour value 5+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: repeater
        # crossbows.
        "points": 85,
        "points_per": "model",
        "unit_size": "1-3",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 4, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Dark Steed (x2)', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Hatred (High Elves)", "Impact Hits (D6)", "Open Order", "Sea Dragon Cloak", "Swiftstride"],
            "TroopType": "LightChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Bloodwrack Medusa": {
        # https://tow.whfb.app/unit/bloodwrack-medusa - 85 pts per unit
        # Fights with the Bloodwrack Medusa row.
        # Shooting is not simulated, so these are left out of the options: petrifying
        # gaze.
        "points": 85,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 5,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 4,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Fear", "Frenzy", "Hatred (High Elves)", "Magic Resistance (-1)", "Murderous", "Poisoned Attacks", "Stony Stare"],
            "TroopType": "MonstrousCreature",
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
    "Kharibdyss": {
        # https://tow.whfb.app/unit/kharibdyss - 195 pts per unit
        # Fights with the Kharibdyss row.
        # Also has a profile for Beastmaster Handlers (x2) (M6 WS4 BS- S3 T- W- I4 A1
        # Ld8); not simulated.
        # Armour value 5+ as printed on the site.
        "points": 195,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Beastmaster Handlers (x2)', 'Movement': 6, 'WeaponSkill': 4, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': 8},
        ],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 7,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 6,
            "Race": "Dark Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Writhing Tentacles (Dark Elves)",
            "Shield": False,
            "SpecialRules": ["Abyssal Howl", "Close Order", "Immune to Psychology", "Large Target", "Monster Handlers", "Stomp Attacks (D3+1)", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Cavernous Maw", "Writhing Tentacles (Dark Elves)"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "War Hydra": {
        # https://tow.whfb.app/unit/war-hydra - 200 pts per unit
        # Fights with the War Hydra row.
        # Also has a profile for Beastmaster Handlers (x2) (M6 WS4 BS- S3 T- W- I4 A1
        # Ld8); not simulated.
        # Armour value 5+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: fiery
        # breath.
        "points": 200,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Beastmaster Handlers (x2)', 'Movement': 6, 'WeaponSkill': 4, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': 8},
        ],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 5,
            "Attacks": 2,
            "Leadership": 6,
            "Race": "Dark Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Close Order", "Extra Attacks (+remaining Wounds)", "Immune to Psychology", "Large Target", "Monster Handlers", "Regeneration (5+)", "Stomp Attacks (D3)", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Wicked Claws", "Serrated Maws"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Reaper Bolt Thrower": {
        # https://tow.whfb.app/unit/reaper-bolt-thrower - 80 pts per unit
        # Fights with the Dark Elf Crew row.
        # Also has a profile for Reaper Bolt Thrower (M- WS- BS- S- T6 W2 I- A- Ld-);
        # not simulated.
        # Shooting is not simulated, so these are left out of the options: Repeater
        # bolt thrower.
        "points": 80,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Reaper Bolt Thrower', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 2, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Hatred (High Elves)", "Skirmishers"],
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
}


# Army-wide special rules for this faction. `status` is how far the engine
# goes with each: "implemented", "partial", or None for recorded only.
FACTION_RULES = {
    'Murderous': {
        "status": 'implemented',
        "text": (
            "When fighting with a hand weapon, may reroll To Wound rolls of a "
            "natural 1. A single, non-magical hand weapon only. "
        ),
    },
    'Eternal Hatred': {
        "status": None,
        "text": (
            "Against High Elves, this model's Hatred applies in every round of "
            "close combat, not just the first. Note that this special rule does not "
            "apply to this model's mount (should it have one)."
        ),
    },
    'Hatred (High Elves)': {
        "status": 'implemented',
        "text": (
            "Reroll failed To Hit rolls in the first round against High Elves. "
        ),
    },
    'Strike First': {
        "status": 'implemented',
        "text": (
            "Strikes before models without it, regardless of Initiative. "
        ),
    },
    'Elven Reflexes': {
        "status": 'implemented',
        "text": (
            "+1 Initiative (max 10) during the first round of any combat. "
        ),
    },
    "Hekarti's Blessing": {
        "status": None,
        "text": (
            "Once per game, a model with this special rule may re-roll a single "
            "failed Casting roll."
        ),
    },
    'Sea Dragon Cloak': {
        "status": None,
        "text": (
            "A model with this special rule improves its armour value by 1 (to a "
            "maximum of 2+) against non-magical shooting attacks."
        ),
    },
    "Abyssal Howl": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/abyssal-howl",
        "text": (
            "Whilst within 6\" of this model, enemy units suffer a -1 modifier to "
            "their Leadership characteristic (to a minimum of 2). Note that this "
            "modifier is not cumulative."
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
    "Close Order": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/close-order",
        "text": (
            "A unit consisting of models with this special rule may adopt a Close "
            "Order formation."
        ),
    },
    "Cursed Coven": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/cursed-coven",
        "text": (
            "A unit of Doomfire Warlocks knows a single spell (chosen by their "
            "controlling player before armies are deployed) from either the Dark "
            "Magic or Daemonology Lore of Magic. The unit may cast this spell as a "
            "Bound spell: - If the unit has a Unit Strength of 10 or more and "
            "includes a Master, it may cast this Bound spell with a Power Level of "
            "2. - If the unit includes a Master, but has a Unit Strength of 9 or "
            "less, it may cast this Bound spell with a Power Level of 1. - "
            "Otherwise, the unit may cast this Bound spell with a Power Level of 0."
        ),
    },
    "Dance of Death": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dance-of-death",
        "text": (
            "If this unit makes a successful charge move (i.e., if the unit makes "
            "contact with the charge target), the charge target suffers a -1 "
            "modifier to its Maximum Rank Bonus until the end of the Combat phase "
            "of that turn."
        ),
    },
    "Dark Runes": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/dark-runes",
        "text": (
            "This unit has a 5+ Ward save against any wounds suffered that were "
            "caused by a non-magical enemy attack."
        ),
    },
    "Dragged Along": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dragged-along",
        "text": (
            "A model with this special rule that begins its movement within 1\" of a "
            "friendly unit whose troop type is infantry, that is not fleeing and "
            "that contains ten or more models, may replace its Movement "
            "characteristic with that of the unit."
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
    "Extra Attacks": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/extra-attacks",
        "text": (
            "A model with this special rule has a modifier to its Attacks "
            "characteristic, as shown in brackets after the name of this special "
            "rule (shown here as '+X'). If this modifier is determined by the roll "
            "of a dice, roll when the model's combat is chosen during any Choose & "
            "Fight Combat sub-phase."
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
    "First Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/first-charge",
        "text": (
            "If this unit's first charge of the game is successful (i.e., if the "
            "unit makes contact with the charge target), the charge target becomes "
            "Disrupted until the end of the Combat phase of that turn."
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
    "Impetuous": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/impetuous",
        "text": (
            "If during the Declare Charges & Charge Reactions sub-phase of its "
            "turn, a unit that includes one or more Impetuous models is able to "
            "declare a charge, it must make a Leadership test. If this test is "
            "failed, the unit must declare a charge. If this test is passed, the "
            "unit may act as normal."
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
    "Loner": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/loner",
        "text": (
            "A character with this special rule cannot be your General and cannot "
            "join a unit without this special rule. A unit with this special rule "
            "cannot be joined by a character without this special rule."
        ),
    },
    "Magic Resistance": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/magic-resistance",
        "text": (
            "The Casting roll of any enemy spell (including Bound spells) that "
            "targets a unit that includes one or more models with this special rule "
            "suffers a modifier, as shown in brackets after the name of this "
            "special rule (shown here as '-X'). Note that this special rule is not "
            "cumulative. If two or more models in a unit have this special rule, "
            "use the highest modifier."
        ),
    },
    "Martial Prowess": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/martial-prowess",
        "text": (
            "During the first round of combat, a unit with this special rule gains "
            "a +1 modifier to its Weapon Skill characteristic. In addition, a unit "
            "with this special rule can make supporting attacks to its flank or "
            "rear, as well as to its front."
        ),
    },
    "Monster Handlers": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/monster-handlers",
        "text": (
            "A monster with this special rule is accompanied by one or more models "
            "representing its handlers. During deployment, position these models "
            "anywhere that is adjacent to, and in base contact with, the monster. "
            "If the handlers are found to be blocking movement or line of sight, "
            "simply move them aside. In combat, each handler adds its attacks to "
            "those of the monster. If the monster suffers an unsaved wound, roll a "
            "D6. On a roll of 1-4 the monster loses a Wound, but on a roll of 5+ "
            "one of the handlers is removed instead. If the monster is removed from "
            "play, so are its handlers."
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
    "Scouts": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/scouts",
        "text": (
            "Units with this special rule may be deployed after all other units "
            "from both armies. They can be deployed anywhere on the battlefield "
            "that is more than 12\" away from an enemy model. If deployed in this "
            "way, Scouts cannot declare a charge during their first turn. If both "
            "armies contain Scouts, a roll-off should determine which player "
            "deploys Scouts first. The players then alternate deploying their "
            "scouting units one at a time, starting with the player who won the "
            "roll-off."
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
    "Stony Stare": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/stony-stare",
        "text": (
            "At the start of each Combat phase, enemy models in base contact with "
            "this model must make an Initiative test. If this test is failed, they "
            "suffer D3 Strength 2 hits, with no armour save permitted (Ward and "
            "Regeneration saves can be attempted as normal)."
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
    "Stupidity": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/stupidity",
        "text": (
            "Unless it is fleeing or engaged in combat, a unit with this special "
            "rule must test for Stupidity by making a Leadership test during the "
            "Start of Turn sub-phase of each of its turns. If this test is failed, "
            "the unit succumbs to Stupidity until its next Start of Turn sub-phase. "
            "A unit that has succumbed to Stupidity: - Cannot move (except to "
            "flee). - Cannot shoot or cast spells. - Cannot attempt a Wizardly "
            "dispel. - Must Hold if charged by an enemy. A unit or mount that does "
            "not have this special rule becomes subject to it when joined or ridden "
            "by a character that does (Stupidity is contagious)."
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
    "Veteran": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/veteran",
        "text": (
            "If the majority of the models in a unit have this special rule, the "
            "unit may re-roll any failed Leadership test. Note that a Break test is "
            "not a Leadership test."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
