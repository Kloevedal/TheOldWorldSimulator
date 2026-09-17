"""Ogre Kingdoms.

Profiles from https://tow.whfb.app/army/ogre-kingdoms, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Ogre Kingdoms"

# Other names that should resolve to this faction.
ALIASES = [
    "Ogres",
    "Ogre Kingdoms",
    "OK",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Ogre Tyrant": "Tyrant",
    "Ogre Bruiser": "Bruiser",
}

CHARACTERS = {
    "Bruiser": {
        # https://tow.whfb.app/unit/bruiser - 110 pts
        # Shooting is not simulated, so these are left out of the options: Brace of
        # Ogre pistols, Ogre pistol.
        "points": 110,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Ogre",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Bull Charge", "Fear", "Impact Hits (2)", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Big Name"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Ironfist", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Stonehorn", "Thundertusk"]
        }
    },
    "Butcher": {
        # https://tow.whfb.app/unit/butcher - 105 pts
        "points": 105,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 4,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Ogre",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Fear", "Impact Hits (2)", "Lore of the Great Maw", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "Illusion"],
            "OptionalRules": ["Butcher's Cauldron", "Big Name"],
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
    "Firebelly": {
        # https://tow.whfb.app/unit/firebelly - 110 pts
        # Shooting is not simulated, so these are left out of the options: flaming
        # breath.
        "points": 110,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 4,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Ogre",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Blessings of the Volcano God", "Ward4 (Flaming)", "Fear", "Flaming Attacks", "Impact Hits (1)", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism"],
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
    "Hunter": {
        # https://tow.whfb.app/unit/hunter - 115 pts
        # Shooting is not simulated, so these are left out of the options: great
        # throwing spear, harpoon launcher.
        "points": 115,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Ogre",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Fear", "Impact Hits (1)", "Loner", "Move Through Cover", "Ogre Charge", "Running with the Pack"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Ambushers", "Scouts", "Vanguard", "Big Name"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Stonehorn", "Thundertusk"]
        }
    },
    "Slaughtermaster": {
        # https://tow.whfb.app/unit/slaughtermaster - 230 pts
        "points": 230,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 5,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Ogre",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Fear", "Impact Hits (2)", "Lore of the Great Maw", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Elementalism", "Illusion"],
            "OptionalRules": ["Butcher's Cauldron", "Big Name"],
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
    "Tyrant": {
        # https://tow.whfb.app/unit/tyrant - 185 pts
        # Shooting is not simulated, so these are left out of the options: Brace of
        # Ogre pistols, Ogre pistol.
        "points": 185,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Ogre",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Bull Charge", "Fear", "Impact Hits (2)", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Big Name"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Ironfist", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Stonehorn", "Thundertusk"]
        }
    },
}

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Gnoblar Fighters": {
        # https://tow.whfb.app/unit/gnoblar-fighters - 2 pts per model, unit size 20+
        # Fights with the Gnoblar Fighter row.
        # Shooting is not simulated, so these are left out of the options: throwing
        # weapons.
        "points": 2,
        "points_per": "model",
        "unit_size": "20+",
        "champion": {'Name': 'Groinbiter', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 2, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 2,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Gnoblar",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Largely Insignificant"],
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
    "Gnoblar Trappers": {
        # https://tow.whfb.app/unit/gnoblar-trappers - 5 pts per model, unit size 10+
        # Fights with the Gnoblar Trapper row.
        # Shooting is not simulated, so these are left out of the options: throwing
        # weapons.
        "points": 5,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Snarefinger', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 4, 'Strength': 2, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 2,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Gnoblar",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Largely Insignificant", "Move Through Cover", "Scouts", "Skirmishers", "Traps & Snares"],
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
    "Ironguts": {
        # https://tow.whfb.app/unit/ironguts - 39 pts per model, unit size 3+
        # Fights with the Irongut row.
        "points": 39,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Gutlord', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': 2, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 3, 'Attacks': 4, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Ogre",
            "Armor": "Heavy Armor",
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Fear", "Impact Hits (1)", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Look-out Gnoblar", "Veteran"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Leadbelchers": {
        # https://tow.whfb.app/unit/leadbelchers - 41 pts per model, unit size 2+
        # Fights with the Leadbelcher row.
        # Shooting is not simulated, so these are left out of the options: leadbelcher
        # guns.
        "points": 41,
        "points_per": "model",
        "unit_size": "2+",
        "champion": {'Name': 'Thunderfist', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 3, 'Attacks': 4, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Ogre",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Fear", "Impact Hits (1)", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Veteran"],
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
    "Maneaters": {
        # https://tow.whfb.app/unit/maneaters - 54 pts per model, unit size 2+
        # Fights with the Maneater Captain row.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # Ogre pistols, Ogre pistol.
        "points": 54,
        "points_per": "model",
        "unit_size": "2+",
        "champion": {'Name': 'Maneater', 'Movement': 6, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 5, 'Toughness': 4, 'Initiative': 3, 'Wounds': 3, 'Attacks': 4, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Ogre",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Fear", "Impact Hits (1)", "Motley Crew", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Look-out Gnoblar", "Immune to Psychology", "Poisoned Attacks", "Stubborn", "Vanguard"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Ironfist", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Ogre Bulls": {
        # https://tow.whfb.app/unit/ogre-bulls - 31 pts per model, unit size 3+
        # Fights with the Ogre row.
        "points": 31,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Crusher', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': 2, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 3, 'Attacks': 4, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Ogre",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Close Order", "Fear", "Impact Hits (1)", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Look-out Gnoblar"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Ironfist"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Yhetees": {
        # https://tow.whfb.app/unit/yhetees - 46 pts per model, unit size 3+
        # Fights with the Yhetee row.
        "points": 46,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Greyback', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': 0, 'Strength': 5, 'Toughness': 4, 'Initiative': 4, 'Wounds': 3, 'Attacks': 4, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Ogre",
            "Armor": None,
            "Weapon": "Grimfrost Weapon",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (1)", "Fear", "Flammable", "Loner", "Move Through Cover", "Numbing Chill", "Open Order", "Swiftstride"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Scouts", "Vanguard"],
        },
        "equipment_options": {
            "weapons": ["Grimfrost Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Mournfang Cavalry": {
        # https://tow.whfb.app/unit/mournfang-cavalry - 64 pts per model, unit size 2+
        # Fights with the Ogre row.
        # Also has a profile for Mournfang (M8 WS3 BS- S5 T- W- I2 A3 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: brace of
        # Ogre pistols.
        "points": 64,
        "points_per": "model",
        "unit_size": "2+",
        "champion": {'Name': 'Crusher', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 2, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 4, 'Attacks': 4, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Mournfang', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 5, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 3, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 4,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Ogre",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (1)", "Close Order", "Fear", "Impact Hits (D3)", "Mournfang Charge", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Ironfist"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Sabretusk Pack": {
        # https://tow.whfb.app/unit/sabretusk-pack - 17 pts per model, unit size 2-10
        # Fights with the Sabretusk row.
        "points": 17,
        "points_per": "model",
        "unit_size": "2-10",
        "other_profiles": [],
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 6,
            "Race": "Ogre",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Fear", "Impetuous", "Loner", "Move Through Cover", "Open Order", "Skirmishers", "Swiftstride"],
            "TroopType": "WarBeast",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers", "Scouts", "Vanguard"],
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
    "Gnoblar Scraplauncher": {
        # https://tow.whfb.app/unit/gnoblar-scraplauncher - 140 pts per unit
        # Fights with the Gnoblar Scrapper (x7) row, using the Scraplauncher row's
        # Toughness and Wounds.
        # Also has a profile for Scraplauncher (M- WS- BS- S5 T5 W5 I- A- Ld-); not
        # simulated.
        # Also has a profile for Rhinox (x1) (M6 WS3 BS- S5 T- W- I2 A3 Ld-); not
        # simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: throwing
        # weapons.
        "points": 140,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Scraplauncher', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 5, 'Attacks': None, 'Leadership': None},
            {'Name': 'Rhinox (x1)', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 5, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 3, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 2,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 5,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Gnoblar",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2, Rhinox only)", "Close Order", "Fear", "First Charge", "Impact Hits (D6+1)", "Large Target"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Ironblaster": {
        # https://tow.whfb.app/unit/ironblaster - 185 pts per unit
        # Fights with the Leadbelcher (x1) row, using the Ironblaster row's Toughness
        # and Wounds.
        # Also has a profile for Ironblaster (M- WS- BS- S5 T6 W5 I- A- Ld-); not
        # simulated.
        # Also has a profile for Gnoblar Scrapper (x1) (M- WS2 BS3 S2 T- W- I3 A1
        # Ld5); not simulated.
        # Also has a profile for Rhinox (x1) (M6 WS3 BS- S5 T- W- I2 A3 Ld-); not
        # simulated.
        # Armour value 4+ as printed on the site.
        "points": 185,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Ironblaster', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 6, 'Initiative': None, 'Wounds': 5, 'Attacks': None, 'Leadership': None},
            {'Name': 'Gnoblar Scrapper (x1)', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 2, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': 5},
            {'Name': 'Rhinox (x1)', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 5, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 3, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 6,
            "Initiative": 2,
            "Wounds": 5,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Ogre",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2, Rhinox only)", "Close Order", "Fear", "First Charge", "Impact Hits (D6+1)", "Large Target"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Giant": {
        # https://tow.whfb.app/unit/giant - 200 pts per unit
        # Its Attacks are *, a dice value the engine cannot use yet; recorded as None,
        # so it makes no attacks.
        # Fights with the Giant row.
        "points": 200,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 1,
            "Strength": 6,
            "Toughness": 7,
            "Initiative": 2,
            "Wounds": 6,
            "Attacks": None,
            "Leadership": 10,
            "Race": "Giant",
            "Armor": "Light Armor",
            "Weapon": "Giant's Club",
            "Shield": False,
            "SpecialRules": ["Close Order", "Giant Attacks", "Immune to Psychology", "Large Target", "Pick Up And…", "Stomp Attacks (D6)", "Terror", "Timmm-berrr!", "Unbreakable"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Giant's Club"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Gorger": {
        # https://tow.whfb.app/unit/gorger - 90 pts per unit
        # Fights with the Gorger row.
        "points": 90,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Ogre",
            "Armor": "Light Armor",
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Ambushers", "Close Order", "Fear", "Frenzy", "Ravenous Hunger", "Regeneration (6+)", "Swiftstride", "Unbreakable"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
            "OptionalRules": ["Scouts", "Vanguard"],
        },
        "equipment_options": {
            "weapons": ["Wicked Claws", "Distensible Jaw"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Stonehorn Riders": {
        # https://tow.whfb.app/unit/stonehorn-riders - 245 pts per unit
        # Fights with the Stonehorn row.
        # Also has a profile for Ogre Beast Rider (x1) (M- WS3 BS3 S4 T- W- I2 A3
        # Ld7); not simulated.
        # Also has a profile for Ogre Crew (x1) (M- WS3 BS3 S4 T- W- I2 A3 Ld7); not
        # simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: blood
        # vulture, chaintrap, harpoon launcher.
        "points": 245,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Ogre Beast Rider (x1)', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 3, 'Leadership': 7},
            {'Name': 'Ogre Crew (x1)', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 3, 'Leadership': 7},
        ],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 3,
            "BallisticSkill": None,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 2,
            "Wounds": 6,
            "Attacks": 4,
            "Leadership": None,
            "Race": "Ogre",
            "Armor": "Full Plate Armor",
            "Weapon": "Horns of Stone",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2, Stonehorn only)", "Close Order", "First Charge", "Howdah", "Impact Hits (D6+1)", "Large Target", "Stone Skeleton", "Swiftstride", "Terror", "Thunderous Charge"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Horns of Stone"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Thundertusk Riders": {
        # https://tow.whfb.app/unit/thundertusk-riders - 215 pts per unit
        # Fights with the Thundertusk row.
        # Also has a profile for Ogre Beast Rider (x1) (M- WS3 BS3 S4 T- W- I2 A3
        # Ld7); not simulated.
        # Also has a profile for Ogre Crew (x1) (M- WS3 BS3 S4 T- W- I2 A3 Ld7); not
        # simulated.
        # Armour value 5+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: blood
        # vulture, chaintrap, chill breath, harpoon launcher.
        "points": 215,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Ogre Beast Rider (x1)', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 3, 'Leadership': 7},
            {'Name': 'Ogre Crew (x1)', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 3, 'Leadership': 7},
        ],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": None,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 2,
            "Wounds": 6,
            "Attacks": 4,
            "Leadership": None,
            "Race": "Ogre",
            "Armor": "Heavy Armor",
            "Weapon": "Great Tusks",
            "Shield": False,
            "SpecialRules": ["Close Order", "First Charge", "Howdah", "Impact Hits (D3)", "Large Target", "Numbing Chill", "Stomp Attacks (3)", "Swiftstride", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Great Tusks"],
            "armor": ["Heavy Armor"],
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
    "Blessings of the Volcano God": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/blessings-of-the-volcano-god",
        "text": (
            "A model with this special rule has a 4+ Ward save against any wounds "
            "suffered that were caused by an attack that has the Flaming Attacks "
            "special rule."
        ),
    },
    "Bull Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/bull-charge",
        "text": (
            "Impact Hits caused by this model (but not its mount) have an Armour "
            "Piercing characteristic of -1."
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
    "Giant Attacks": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/giant-attacks",
        "text": (
            "Instead of attacking normally during the Combat phase or making a Pick "
            "Up And... attack, a Giant may choose to make a 'Giant Attack'. To make "
            "a Giant Attack, nominate an enemy unit that the Giant is engaged in "
            "combat with to be the target of the attack and roll on the Giant "
            "Attacks table below to determine what the Giant does: D6 | Result 1 | "
            "'Eadbutt 2 | Belly Flop 3-4 | Mighty Swing 5 | Thump with Club 6 | "
            "Jump Up & Down"
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
    "Howdah": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/howdah",
        "text": (
            "To represent its howdah and crew, a behemoth with this special rule "
            "has a split profile and follows both the Split Profile (Chariots) and "
            "Firing Platform. In all other respects, this model is a behemoth."
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
    "Largely Insignificant": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/largely-insignificant",
        "text": (
            "Units with this special rule never cause friendly units to make Panic "
            "tests. However, a unit with this special rule cannot be joined by a "
            "character without this special rule."
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
    "Lore of the Great Maw": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-the-great-maw",
        "text": (
            "Emissaries of the Great Maw suck marrow from cracked bones or stuff "
            "huge chunks of raw meat into their mouths to aid their magical "
            "abilities. As they do, those around them feel replenished, the gnawing "
            "hunger that eternally chews at their guts subsiding. A Wizard with the "
            "'Lore of the Great Maw' special rule may discard one of their randomly "
            "generated spells as normal. When they do so, they may select instead "
            "either the signature spell of their chosen Lore of Magic, or one of "
            "the spells listed below. Lore of the Great Maw Lore"
        ),
    },
    "Motley Crew": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/motley-crew",
        "text": (
            "Units with this special rule may include models of the same type that "
            "are equipped differently to one another, and/or models of different "
            "types that fight together in a single unit. If necessary, the army "
            "list entry for such units will be accompanied by a brief explanation "
            "of the unit's composition. Different Weapons The fighting rank of a "
            "Motley Crew may contain models that are armed with different weapons. "
            "In such cases, the controlling player must roll different batches of "
            "dice for the different models, making it clear to their opponent which "
            "model's attacks they represent and where they are being directed. "
            "These attacks are made in the Initiative order of the individual "
            "models, as [...]"
        ),
    },
    "Mournfang Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/mournfang-charge",
        "text": (
            "Impact Hits caused by a model with this special rule have the Armour "
            "Bane (1) special rule and an Armour Piercing characteristic of -1."
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
    "Numbing Chill": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/numbing-chill",
        "text": (
            "Whilst in base contact with this model, enemy models suffer a -1 "
            "modifier to their Weapon Skill and Initiative characteristics, to a "
            "minimum of 1."
        ),
    },
    "Ogre Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ogre-charge",
        "text": (
            "The Armour Piercing characteristic of any Impact Hits caused by a "
            "model with this special rule (but not its mount) is improved by the "
            "current Rank Bonus of its unit (or, in the case of characters, the "
            "current Rank Bonus of any unit they have joined)."
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
    "Pick Up And…": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/pick-up-and",
        "text": (
            "Instead of attacking normally during the Combat phase or making a "
            "Giant Attack, a Giant that is engaged in combat with one or more units "
            "whose troop type is regular infantry or heavy infantry may choose to "
            "make a 'Pick Up And...' attack. To make a Pick Up And... attack, "
            "nominate an enemy unit of regular or heavy infantry that the Giant is "
            "engaged in combat with. The unit must immediately make an Initiative "
            "test: - If this test is failed, a victim is picked up by the Giant. "
            "What happens next does not bear thinking about but, whatever it is, a "
            "single model belonging to the target unit is immediately removed from "
            "play as a casualty. - If this test is passed, the warriors manage to "
            "duck and [...]"
        ),
    },
    "Ravenous Hunger": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ravenous-hunger",
        "text": (
            "When a Gorger declares a charge, it may re-roll its Charge roll."
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
    "Running with the Pack": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/running-with-the-pack",
        "text": (
            "A Hunter that joins a unit of Sabretusks gains the Swiftstride special "
            "rule for as long as they remain with the unit. In addition, for as "
            "long as the Hunter remains with the unit, the Sabretusks lose the "
            "Impetuous special rule."
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
    "Stone Skeleton": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/stone-skeleton",
        "text": (
            "This model is less vulnerable to the Multiple Wounds (X) special rule. "
            "If it suffers an unsaved wound from an attack with this special rule, "
            "reduce the number of Wounds lost by 1, to a minimum of 1."
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
    "Thunderous Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/thunderous-charge",
        "text": (
            "Impact Hits caused by this model have an Armour Piercing "
            "characteristic of -2."
        ),
    },
    "Timmm-berrr!": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/timmm-berrr",
        "text": (
            "When this model is reduced to zero Wounds, the winner of a roll-off "
            "chooses one of its arcs (front, flank or rear) for it to fall into. "
            "Any units that are within the chosen arc and in base contact with this "
            "model suffer D6 hits, each using the Strength characteristic of this "
            "model, with an AP of -1. Once these hits are resolved, this model is "
            "removed from play."
        ),
    },
    "Traps & Snares": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/traps-and-snares",
        "text": (
            "Any enemy model that ends its charge move in base contact with a model "
            "with this special rule must make a Dangerous Terrain test."
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
}

PROFILES = dict(CHARACTERS, **UNITS)
