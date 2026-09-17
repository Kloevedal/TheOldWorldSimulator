"""Beastmen Brayherds.

Profiles from https://tow.whfb.app/army/beastmen-brayherds
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Beastmen Brayherds"

# Other names that should resolve to this faction.
ALIASES = [
    "Beastmen",
    "Brayherds",
    "Beastmen Brayherds",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Ghorros": "Ghorros Warhoof",
    "Kralmaw": "Kralmaw, the Prophet of Ruin",
}

CHARACTERS = {
    "Beastlord": {
        # https://tow.whfb.app/unit/beastlord - 115 pts
        # 0-1 per 1,000 pts may take Ambushers or a chariot. Chaos Mutations are not
        # modelled.
        "points": 115,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blood Rage", "Brayhorn (General only)", "Foe Render", "Gaze of the Gods", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Tuskgor Chariot", "Razorgor Chariot"]
        }
    },
    "Wargor": {
        # https://tow.whfb.app/unit/wargor - 55 pts
        "points": 55,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blood Rage", "Brayhorn (General only)", "Foe Render", "Gaze of the Gods", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Tuskgor Chariot", "Razorgor Chariot"]
        }
    },
    "Doombull": {
        # https://tow.whfb.app/unit/doombull - 210 pts
        "points": 210,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Blood Greed", "Blood Rage", "Bull-gors", "Fear", "Foe Render", "Gaze of the Gods", "Impact Hits (1)", "Mark of Chaos Undivided", "Primal Fury", "Slaughterer's Call", "Warband"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Gorebull": {
        # https://tow.whfb.app/unit/gorebull - 130 pts
        "points": 130,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Blood Greed", "Blood Rage", "Bull-gors", "Fear", "Foe Render", "Gaze of the Gods", "Impact Hits (1)", "Mark of Chaos Undivided", "Primal Fury", "Slaughterer's Call", "Warband"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Great Bray-Shaman": {
        # https://tow.whfb.app/unit/great-bray-shaman - 150 pts
        "points": 150,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Braystaff",
            "Shield": False,
            "SpecialRules": ["Gaze of the Gods", "Lore of Beasts", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "WizardLevel": 3,
            "Lores": ["Daemonology", "Dark Magic", "Elementalism"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Braystaff", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Tuskgor Chariot", "Razorgor Chariot"]
        }
    },
    "Bray-Shaman": {
        # https://tow.whfb.app/unit/bray-shaman - 65 pts
        "points": 65,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Braystaff",
            "Shield": False,
            "SpecialRules": ["Gaze of the Gods", "Lore of Beasts", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "WizardLevel": 1,
            "Lores": ["Daemonology", "Dark Magic", "Elementalism"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Braystaff", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Tuskgor Chariot", "Razorgor Chariot"]
        }
    },
    "Warhoof": {
        # https://tow.whfb.app/unit/warhoof - 75 pts
        # A centigor: the profile already includes its own four legs, so there is no
        # separate mount.
        "points": 75,
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 7,
            "Race": "Centigor",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Drunken", "Fast Cavalry", "Gaze of the Gods", "Mark of Chaos Undivided", "Move Through Cover", "Primal Fury", "Stomp Attacks (1)", "Swiftstride", "Warband"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Ghorros Warhoof": {
        # https://tow.whfb.app/unit/ghorros-warhoof - 155 pts
        # Fixed wargear; must be fielded as presented.
        "points": 155,
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Centigor",
            "Armor": None,
            "Weapon": "Mansmasher",
            "Shield": False,
            "SpecialRules": ["Drunken", "Father of Beasts", "Gaze of the Gods", "Mark of Chaos Undivided", "Move Through Cover", "Primal Fury", "Stomp Attacks (D3)", "Swiftstride", "The Sons of Ghorros", "Warband"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Mansmasher", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": ["Mansmasher", "Skull of the Unicorn Lord"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Kralmaw, the Prophet of Ruin": {
        # https://tow.whfb.app/unit/kralmaw-the-prophet-of-ruin - 245 pts
        # Fixed wargear. The Grisly Totem is his Braystaff.
        "points": 245,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Grisly Totem",
            "Shield": False,
            "SpecialRules": ["Future Sight", "Gaze of the Gods", "Leering Spirit", "Lore of Beasts", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "WizardLevel": 4,
            "Lores": ["Dark Magic", "Lore of Primal Magic"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Grisly Totem", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": ["Grisly Totem"],
        },
        "mount_options": {
            "mounts": []
        }
    },
}

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Bestigor Herd": {
        # https://tow.whfb.app/unit/bestigor-herd - 13 pts per model, unit size 5+
        # Fights with the Bestigor row.
        # Also has a profile for Gourge-horn (M5 WS4 BS3 S4 T4 W1 I4 A2 Ld8); not
        # simulated.
        "points": 13,
        "points_per": "model",
        "unit_size": "5+",
        "other_profiles": [
            {'Name': 'Gourge-horn', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        ],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": "Heavy Armor",
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Blood Rage", "Close Order", "Furious Charge", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Chaos Mutations", "Stubborn", "Veteran"],
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
    "Gor Herd": {
        # https://tow.whfb.app/unit/gor-herd - 7 pts per model, unit size 5+
        # Fights with the Gor row.
        "points": 7,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'True-horn', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Bestial Charge", "Blood Rage", "Furious Charge", "Horde", "Mark of Chaos Undivided", "Move Through Cover", "Open Order", "Primal Fury", "Skirmishers", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons"],
            "armor": [],
            "shield": True,
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
            "Race": "Beastman",
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
    "Minotaur Herd": {
        # https://tow.whfb.app/unit/minotaur-herd - 44 pts per model, unit size 2+
        # Fights with the Minotaur row.
        "points": 44,
        "points_per": "model",
        "unit_size": "2+",
        "champion": {'Name': 'Bloodkine', 'Movement': 6, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 5, 'Toughness': 4, 'Initiative': 3, 'Wounds': 3, 'Attacks': 4, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Minotaur",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blood Greed", "Blood Rage", "Bull-gors", "Close Order", "Fear", "Foe Render", "Impact Hits (1)", "Mark of Chaos Undivided", "Motley Crew", "Primal Fury", "Warband"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Chaos Mutations", "Ambushers"],
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
    "Primal Warherd": {
        # https://tow.whfb.app/unit/primal-warherd - 7 pts per model, unit size
        # 10+/10+*
        # Fights with the Gor row.
        # Also has a profile for Ungor (M5 WS3 BS3 S3 T3 W1 I3 A1 Ld5); not simulated.
        # Also has a profile for Foe-render (M5 WS4 BS2 S3 T4 W1 I3 A2 Ld7); not
        # simulated.
        "points": 7,
        "points_note": "7 points per Gor, 6 points per Ungor",
        "points_per": "model",
        "unit_size": "10+/10+*",
        "other_profiles": [
            {'Name': 'Ungor', 'Movement': 5, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 5},
            {'Name': 'Foe-render', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        ],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Bestial Charge (Gors only)", "Blood Rage", "Close Order", "Furious Charge (Gors only)", "Horde", "Impetuous", "Mark of Chaos Undivided", "Mixed Unit", "Motley Crew*", "Move Through Cover", "Primal Fury", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Thrusting Spear", "Throwing Spear", "Great Weapon"],
            "armor": [],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Primal Warhounds": {
        # https://tow.whfb.app/unit/primal-warhounds - 6 pts per model, unit size 10+
        # Fights with the Primal Warhound row.
        "points": 6,
        "points_per": "model",
        "unit_size": "10+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Motley Crew", "Move Through Cover", "Swiftstride", "Warband"],
            "TroopType": "WarBeast",
            "UnitCategory": "Unit",
            "OptionalRules": ["Armoured Hide (1)", "Poisoned Attacks"],
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
    "Ungor Herd": {
        # https://tow.whfb.app/unit/ungor-herd - 5 pts per model, unit size 10+
        # Fights with the Ungor row.
        # Shooting is not simulated, so these are left out of the options: shortbows.
        "points": 5,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Half-horn', 'Movement': 5, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Chariot Runners", "Horde", "Mark of Chaos Undivided", "Move Through Cover", "Open Order", "Primal Fury", "Skirmishers", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Thrusting Spear", "Throwing Spear"],
            "armor": [],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Ungor Ravagers": {
        # https://tow.whfb.app/unit/ungor-ravagers - 7 pts per model
        # The site gives no unit size.
        # Fights with the Ungor Ravager row.
        "points": 7,
        "points_per": "model",
        "unit_size": "not given",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Throwing Spear",
            "Shield": True,
            "SpecialRules": ["Close Order", "Horde", "Leader of the Pack", "Move Through Cover", "Primal Fury", "Swiftstride", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Throwing Spear"],
            "armor": [],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Warped Gors": {
        # https://tow.whfb.app/unit/warped-gors - 16 pts per model, unit size 5+
        # Its Attacks are D3, a dice value the engine cannot use yet; recorded as
        # None, so it makes no attacks.
        # Fights with the Warped Gor row.
        "points": 16,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Splice-horn', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': None, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": None,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (1)", "Blessing of Chaos", "Blood Rage", "Furious Charge", "Mark of Chaos Undivided", "Move Through Cover", "Open Order", "Primal Fury", "Random Attacks", "Stubborn", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons"],
            "armor": [],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Centigor Herd": {
        # https://tow.whfb.app/unit/centigor-herd - 17 pts per model, unit size 5+
        # Fights with the Centigor row.
        # Shooting is not simulated, so these are left out of the options: Javelins,
        # Throwing axes.
        "points": 17,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Gorehoof', 'Movement': 8, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Centigor",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Drunken", "Fast Cavalry", "Horde", "Mark of Chaos Undivided", "Move Through Cover", "Open Order", "Primal Fury", "Skirmishers", "Stomp Attacks (1)", "Swiftstride", "Warband"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear", "Throwing Spear", "Great Weapon"],
            "armor": [],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Chaos Warhounds": {
        # https://tow.whfb.app/unit/chaos-warhounds - 6 pts per model, unit size 5+
        # Fights with the Chaos Warhound row.
        "points": 6,
        "points_per": "model",
        "unit_size": "5+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Loner", "Move Through Cover", "Open Order", "Swiftstride"],
            "TroopType": "WarBeast",
            "UnitCategory": "Unit",
            "OptionalRules": ["Armoured Hide (1)", "Poisoned Attacks", "Vanguard"],
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
    "Dragon Ogres": {
        # https://tow.whfb.app/unit/dragon-ogres - 59 pts per model, unit size 2-9
        # Fights with the Dragon Ogre row.
        "points": 59,
        "points_per": "model",
        "unit_size": "2-9",
        "champion": {'Name': 'Shartak', 'Movement': 7, 'WeaponSkill': 4, 'BallisticSkill': 2, 'Strength': 5, 'Toughness': 4, 'Initiative': 2, 'Wounds': 4, 'Attacks': 4, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 4,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Beastman",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Armoured Hide (2)", "Close Order", "Fear", "Ensorcelled Weapons", "Immune to Psychology", "Stomp Attacks (2)", "The Quickening Storm"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Razorgor Herd": {
        # https://tow.whfb.app/unit/razorgor-herd - 52 pts per model, unit size 1+
        # Fights with the Razorgor row.
        "points": 52,
        "points_per": "model",
        "unit_size": "1+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 6,
            "Race": "Beastman",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Fear", "Foe Render", "Impact Hits (D3)", "Loner", "Open Order", "Primal Fury", "Razor Tusks", "Swiftstride"],
            "TroopType": "WarBeast",
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
    "Razorgor Chariot": {
        # https://tow.whfb.app/unit/razorgor-chariot - 120 pts per unit
        # Fights with the Bestigor Crew (x1) row, using the Chariot row's Toughness
        # and Wounds.
        # Also has a profile for Chariot (M- WS- BS- S5 T5 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Gor Crew (x1) (M- WS4 BS3 S3 T- W- I3 A1 Ld7); not
        # simulated.
        # Also has a profile for Razorgor (x1) (M7 WS3 BS- S5 T- W- I2 A4 Ld-); not
        # simulated.
        # Armour value 4+ as printed on the site.
        "points": 120,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Gor Crew (x1)', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': 7},
            {'Name': 'Razorgor (x1)', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 5, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 4, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": "Full Plate Armor",
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1 Razorgor only)", "Close Order", "Fear", "First Charge", "Foe Render (Razorgor only)", "Impact Hits (D6+2)", "Mark of Chaos Undivided", "Primal Fury", "Razor Tusks"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Tuskgor Chariot": {
        # https://tow.whfb.app/unit/tuskgor-chariot - 85 pts per unit
        # Fights with the Bestigor Crew (x1) row, using the Chariot row's Toughness
        # and Wounds.
        # Also has a profile for Chariot (M- WS- BS- S5 T4 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Gor Crew (x1) (M- WS4 BS3 S3 T- W- I3 A1 Ld7); not
        # simulated.
        # Also has a profile for Tuskgor (x2) (M7 WS3 BS- S4 T- W- I2 A1 Ld-); not
        # simulated.
        # Armour value 4+ as printed on the site.
        "points": 85,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 4, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Gor Crew (x1)', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': 7},
            {'Name': 'Tuskgor (x2)', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": "Full Plate Armor",
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "First Charge", "Impact Hits (D6+1)", "Mark of Chaos Undivided", "Primal Fury", "Razor Tusks", "Warband"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Chaos Giant": {
        # https://tow.whfb.app/unit/chaos-giant - 200 pts per unit
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
            "OptionalRules": ["Regeneration (6+)"],
        },
        "equipment_options": {
            "weapons": ["Giant's Club"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Cockatrice": {
        # https://tow.whfb.app/unit/cockatrice - 155 pts per unit
        # Fights with the Cockatrice row.
        # Shooting is not simulated, so these are left out of the options: petrifying
        # gaze.
        "points": 155,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 6,
            "Wounds": 4,
            "Attacks": 6,
            "Leadership": 6,
            "Race": "Beastman",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Fly (10)", "Large Target", "Stomp Attacks (1)", "Stony Stare", "Swiftstride", "Terror"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
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
    "Cygor": {
        # https://tow.whfb.app/unit/cygor - 205 pts per unit
        # Fights with the Cygor row.
        # Shooting is not simulated, so these are left out of the options: hurl
        # attack.
        "points": 205,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 2,
            "BallisticSkill": 1,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 3,
            "Wounds": 6,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Beastman",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Ghostsight", "Immune to Psychology", "Large Target", "Soul-eater", "Stomp Attacks (D3)", "Stubborn", "Terror", "Timmm-berrr!"],
            "TroopType": "Behemoth",
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
    "Dragon Ogre Shaggoth": {
        # https://tow.whfb.app/unit/dragon-ogre-shaggoth - 225 pts per unit
        # Fights with the Shaggoth row.
        "points": 225,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 6,
            "BallisticSkill": 2,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 6,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Beastman",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2)", "Armoured Hide (2)", "Close Order", "Ensorcelled Weapons", "Immune to Psychology", "Large Target", "Stomp Attacks (D3+1)", "Storm Call", "Terror", "The Quickening Storm"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
            "OptionalRules": ["Chaos Mutations"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Ghorgon": {
        # https://tow.whfb.app/unit/ghorgon - 245 pts per unit
        # Fights with the Ghorgon row.
        "points": 245,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 6,
            "Toughness": 7,
            "Initiative": 4,
            "Wounds": 6,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Beastman",
            "Armor": "Light Armor",
            "Weapon": "Cleaver-limbs",
            "Shield": False,
            "SpecialRules": ["Blood Greed", "Close Order", "Frenzy", "Large Target", "Primal Fury", "Regeneration (6+)", "Stomp Attacks (D3)", "Stubborn", "Swallow Whole", "Terror", "Timmm-berrr!"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Cleaver-limbs"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Jabberslythe": {
        # https://tow.whfb.app/unit/jabberslythe - 185 pts per unit
        # Fights with the Jabberslythe row.
        # Shooting is not simulated, so these are left out of the options: slythey
        # tongue.
        "points": 185,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Beastman",
            "Armor": "Heavy Armor",
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Close Order", "Fly (9)", "Large Target", "Maddening Aura", "Poisoned Attacks", "Spurting Bile Blood", "Stomp Attacks (D3)", "Swiftstride", "Terror"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Wicked Claws"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Preyton": {
        # https://tow.whfb.app/unit/preyton - 160 pts per unit
        # Fights with the Preyton row.
        "points": 160,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 5,
            "Attacks": 4,
            "Leadership": 6,
            "Race": "Beastman",
            "Armor": "Heavy Armor",
            "Weapon": "Twisted Antlers",
            "Shield": False,
            "SpecialRules": ["Close Order", "Crown of Antlers", "Endless Malice", "Fly (10)", "Impact Hits (D3)", "Large Target", "Terror"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers", "Frenzy"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Twisted Antlers"],
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
    'Primal Fury': {
        "status": 'implemented',
        "text": (
            "On a passed Leadership test at the start of its combat, the unit "
            "may reroll To Hit rolls of a natural 1 for the rest of the Combat "
            "phase. The Leadership test is implemented; see combat_simulations. "
        ),
    },
    'Blood Rage': {
        "status": 'implemented',
        "text": (
            "If the Primal Fury Leadership test is passed on a natural double, "
            "the model also becomes Frenzied. "
        ),
    },
    'Gaze of the Gods': {
        "status": None,
        "text": (
            "A Command sub-phase roll; no command phase in a duel. "
        ),
    },
    'Impact Hits (X)': {
        "status": "implemented",
        "text": (
            "Automatic hits at unmodified Strength on a charge of 3\" or more. "
            "Charges are not modelled. "
        ),
    },
    'Foe Render': {
        "status": None,
        "text": (
            "Whilst subject to Primal Fury, a hand weapon carried by a model with "
            "this special rule has an Armour Piercing characteristic of -2. Note "
            "that this special rule only applies to a single, non-magical hand "
            "weapon and does not apply to a model's mount (should it have one). If "
            "the model is using two hand weapons or any other sort of weapon, this "
            "special rule ceases to apply."
        ),
    },
    'Warband': {
        "status": None,
        "text": (
            "Army-wide; no effect in a duel. "
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
    "Bestial Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/bestial-charge",
        "text": (
            "During a turn in which it made a charge move of 3\" or more, a model "
            "with this special rule gains a +1 modifier to its Strength "
            "characteristic."
        ),
    },
    "Blessing of Chaos": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/blessings-of-chaos",
        "text": (
            "When this unit's combat is chosen during Step 1.1 of any Choose & "
            "Fight Combat sub-phase, roll on the table below to determine the "
            "effect of its warped blessings: D6 | Result 1-2 | Stinging Barbs: The "
            "envenomed touch of the warped ones raises great weals of agony upon "
            "unarmoured flesh. Until the end of this Combat phase, models with this "
            "special rule gain the Poisoned Attacks special rule. 3-4 | Scything "
            "Talons: Insect limbs tipped with scythe-like blades erupt from the "
            "warped ones to lash at the foe. Until the end of this Combat phase, "
            "all attacks made by models with this special rule have an Armour "
            "Piercing characteristic of -2. 5-6 | Chitinous Hide: The flesh of the "
            "warped ones hardens [...]"
        ),
    },
    "Blood Greed": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/blood-greed",
        "text": (
            "Whilst Frenzied, this model has a +2 modifier to its Attacks "
            "characteristic (rather than the usual +1). However, such is this "
            "model's desperate need to feed upon flesh that it rolls only a single "
            "D6 when making a Pursuit roll (rather than the usual 2D6)."
        ),
    },
    "Bull-gors": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/bull-gors",
        "text": (
            "Impact Hits caused by a model with this special rule have an Armour "
            "Piercing characteristic of -1."
        ),
    },
    "Chariot Runners": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/chariot-runners",
        "text": (
            "Friendly models whose troop type is chariot can draw a line of sight "
            "over or through models with this special rule and can move through "
            "friendly units if they are in Skirmish formation and if the majority "
            "of models have this special rule. If the chariot's move would result "
            "in it ending up 'on top' of a Chariot Runner, simply nudge the Chariot "
            "Runner aside, by the smallest amount possible, to make space for the "
            "chariot. Whilst in Skirmish formation units of Chariot Runners can "
            "treat friendly chariots that are within 1\" of one or more of the "
            "unit's models as a part of the unit for the purposes of unit "
            "coherency."
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
    "Crown of Antlers": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/crown-of-antlers",
        "text": (
            "Impact Hits caused by a model with this special rule have the Armour "
            "Bane (1) special rule and an Armour Piercing characteristic of -1."
        ),
    },
    "Drunken": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/drunken",
        "text": (
            "During the Start of Turn sub-phase of each of your turns, roll on the "
            "Drunken table for each unit with this special rule that is not "
            "currently Frenzied, that is not engaged in combat and that is not "
            "fleeing: D6 | Result 1 | Unsteady: The unit has become somewhat "
            "unsteady. Until its next Start of Turn sub-phase, the unit is subject "
            "to the Random Movement special rule and its Movement characteristic "
            "becomes D6+2. 2-5 | Sobering Up: The alcohol has no discernible effect "
            "upon the unit. 6 | Belligerent Drunks: The unit has turned quite "
            "belligerent. Until its next Start of Turn sub-phase, the unit is "
            "subject to the Frenzy special rule. A unit with this special rule may "
            "become Frenzied in this way [...]"
        ),
    },
    "Endless Malice": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/endless-malice",
        "text": (
            "If this model wins a round of combat and chooses to restrain and "
            "reform (and passes its Leadership test to do so), enemy units within "
            "6\" of it must make a Panic test as if a nearby friend had been "
            "destroyed."
        ),
    },
    "Ensorcelled Weapons": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/ensorcelled-weapons",
        "text": (
            "A hand weapon carried by a model with this special rule has the "
            "Magical Attacks special rule and an Armour Piercing characteristic of "
            "-1. Note that this special rule only applies to a single, non-magical "
            "hand weapon and does not apply to a model's mount (should it have "
            "one). If the model is using two hand weapons or any other sort of "
            "weapon, this special rule ceases to apply."
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
    "Furious Charge": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/furious-charge",
        "text": (
            "During a turn in which it made a charge move of 3\" or more, a model "
            "with this special rule gains a +1 modifier to its Attacks "
            "characteristic."
        ),
    },
    "Ghostsight": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ghostsight",
        "text": (
            "During the Combat phase, a Cygor may re-roll any failed rolls To Hit "
            "made against enemy Wizards, enemy models or units equipped with any "
            "magic items, or enemy models or units with a Ward or Regeneration "
            "save."
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
    "Leader of the Pack": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/leader-of-the-pack-beastmen",
        "text": (
            "Models with this special rule can be taken as part of a unit of Primal "
            "Warhounds. Models with this special rule must be positioned at the "
            "rear of their unit, making up its rear rank(s). Any Primal Warhounds "
            "the unit contains must always occupy the front ranks) of the unit, "
            "pushing past any models with this special rule to get there if "
            "necessary (such as when the unit turns)."
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
    "Maddening Aura": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/maddening-aura",
        "text": (
            "During the Command sub-phase of its turn, any enemy unit that is "
            "within 8\" of this model, including units that are fleeing or that are "
            "engaged in combat, must make a Leadership test. If this test is "
            "failed, the unit suffers D3 Strength 3 hits, with no armour or "
            "Regeneration saves permitted (Ward saves can be attempted as normal)."
        ),
    },
    "Mark of Chaos Undivided": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/mark-of-chaos-undivided",
        "text": (
            "Models with the Mark of Chaos Undivided can re-roll any failed Fear, "
            "Panic or Terror test."
        ),
    },
    "Mixed Unit": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/mixed-unit",
        "text": (
            "Models within a Primal Warherd have different Weapon Skill and "
            "Toughness characteristics. Before rolling To Wound, hits caused by "
            "enemy shooting should be divided as evenly as possible between Gors "
            "and Ungors. In combat, enemy models must direct their attacks against "
            "models in the fighting rank of this unit."
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
    "Razor Tusks": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/razor-tusks",
        "text": (
            "During a turn in which it charged, the Armour Piercing characteristic "
            "of this model's tusks (hand weapon) is improved by 1. Note that this "
            "special rule only applies to attacks made by a the model, not to a "
            "chariot or its crew (should it have one)."
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
    "Soul-eater": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/soul-eater",
        "text": (
            "Any enemy Wizard that wishes to cast a spell whilst within 12\" of one "
            "or more Cygors must first make a Leadership test. If this test is "
            "failed, the Wizard has lost their nerve and, should they fail to cast "
            "the spell (i.e., should their casting result be less than the casting "
            "value of the spell), the spell has been miscast and the active player "
            "immediately rolls on the Miscast table to see what fate befalls the "
            "unfortunate Wizard. If this test is passed, the Wizard can continue "
            "with their casting attempt as normal."
        ),
    },
    "Spurting Bile Blood": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/spurting-bile-blood",
        "text": (
            "For each Wound this model loses during the Combat phase, the attacking "
            "enemy unit suffers a Strength 4 hit, with an AP of -1."
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
    "Storm Call": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/storm-call",
        "text": (
            "This model can cast the following Bound spell, with a Power Level of "
            "1. This model can cast this Bound spell even if it is engaged in "
            "combat: Type | Magic Missile Casting Value | 7+ Range | Self If this "
            "Bound spell is cast, all units within 6\" of this model (friend or "
            "foe), including units engaged in combat and this model, suffer D3 "
            "Strength 4 hits, each with an AP of -1."
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
    "Swallow Whole": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/swallow-whole",
        "text": (
            "During the Command sub-phase of its turn, a Ghorgon that is engaged in "
            "combat with one or more units of regular infantry or heavy infantry "
            "may choose to make a 'Swallow Whole' attack. To make a Swallow Whole "
            "attack, nominate an enemy unit of regular or heavy infantry that the "
            "Ghorgon is engaged in combat with. The unit must immediately make an "
            "Initiative test: - If this test is failed, the Ghorgon grabs a victim "
            "from the unit and stuffs them into its gullet. A single model "
            "belonging to the target unit is immediately removed from play as a "
            "casualty. - If this test is passed, the warriors manage to avoid the "
            "grasping Ghorgon. No one is picked up and the attack has no effect. "
            "Each time an [...]"
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
    "The Quickening Storm": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/the-quickening-storm",
        "text": (
            "A model with this special rule has a 5+ Ward save against any wounds "
            "suffered that were caused by a Magic Missile or a Magical Vortex "
            "spell. In addition, if a model with this special rule, or the unit it "
            "belongs to, suffers one or more hits from Storm Call, it becomes "
            "'Quickened'. A Quickened model has a +1 modifier to both its "
            "Initiative and Attacks characteristics. This Quickening lasts until "
            "your next Start of Turn sub-phase."
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
