"""High Elf Realms.

Profiles from https://tow.whfb.app/army/high-elf-realms
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "High Elf Realms"

# Other names that should resolve to this faction.
ALIASES = [
    "High Elves",
    "High Elf",
    "Asur",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Korhil": "Korhil Lionmane",
    "Sea Guard Commander": "Sea Guard Garrison Commander",
    "Garrison Commander": "Sea Guard Garrison Commander",
    "Handmaiden": "Handmaiden of the Everqueen",
}

CHARACTERS = {
    "Prince": {
        # https://tow.whfb.app/unit/prince - 130 pts
        # Strike First does not apply to this model's mount.
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
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ithilmar Weapons", "Strike First", "Valour of Ages"],
            "ElvenHonours": True,
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd", "Cavalry Spear", "Lance"],
            "armor": ["Light Armor", "Heavy Armor", "Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Barded Elven Steed", "Tiranoc Chariot", "Griffon (High Elves)", "Great Eagle", "Moon Dragon", "Star Dragon", "Lion Chariot of Chrace", "Lothern Skycutter", "Sun Dragon", "Flamespyre Phoenix", "Frostheart Phoenix"]
        }
    },
    "Noble": {
        # https://tow.whfb.app/unit/noble - 70 pts
        # Strike First does not apply to this model's mount.
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
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ithilmar Weapons", "Strike First", "Valour of Ages"],
            "ElvenHonours": True,
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd", "Cavalry Spear", "Lance"],
            "armor": ["Light Armor", "Heavy Armor", "Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Barded Elven Steed", "Tiranoc Chariot", "Griffon (High Elves)", "Great Eagle", "Lion Chariot of Chrace", "Lothern Skycutter", "Sun Dragon", "Flamespyre Phoenix", "Frostheart Phoenix"]
        }
    },
    "Chracian Chieftain": {
        # https://tow.whfb.app/unit/chracian-chieftain - 105 pts
        # Furious Charge, Move Through Cover and Strike First do not apply to
        # the mount.
        "points": 105,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Furious Charge", "Ithilmar Weapons", "Lion Cloak", "Move Through Cover", "Strike First", "Stubborn", "Valour of Ages"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Chracian Great Blade"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Chieftain's Chariot"]
        }
    },
    "Sea Guard Garrison Commander": {
        # https://tow.whfb.app/unit/sea-guard-garrison-commander - 90 pts
        # Carries a warbow as standard; shooting is not simulated.
        "points": 90,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Accomplished Archers", "Ithilmar Weapons", "Naval Discipline", "Strike First", "Valour of Ages"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Lothern Skycutter", "Griffon (High Elves)", "Great Eagle"]
        }
    },
    "Handmaiden of the Everqueen": {
        # https://tow.whfb.app/unit/handmaiden-of-the-everqueen - 65 pts
        # Also carries a Bow of Avelorn; shooting is not simulated.
        "points": 65,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arrows of Isha", "Evasive", "Ignores Cover", "Immune to Psychology", "Ithilmar Armour", "Ithilmar Weapons", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Handmaiden's Spear"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": ["Horn of Isha"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Archmage": {
        # https://tow.whfb.app/unit/archmage - 155 pts
        "points": 155,
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
            "Race": "High Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Ithilmar Weapons", "Lileath's Blessing", "Lore of Saphery", "Valour of Ages"],
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Elementalism", "High Magic", "Illusion"],
            "ElvenHonours": True,
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
            "mounts": ["Elven Steed", "Barded Elven Steed", "Great Eagle", "Moon Dragon", "Star Dragon", "Lion Chariot of Chrace", "Lothern Skycutter", "Sun Dragon", "Flamespyre Phoenix", "Frostheart Phoenix"]
        }
    },
    "Mage": {
        # https://tow.whfb.app/unit/mage - 80 pts
        "points": 80,
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
            "Race": "High Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Ithilmar Weapons", "Lileath's Blessing", "Lore of Saphery", "Valour of Ages"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "High Magic", "Illusion"],
            "ElvenHonours": True,
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
            "mounts": ["Elven Steed", "Barded Elven Steed", "Great Eagle", "Lion Chariot of Chrace", "Lothern Skycutter", "Sun Dragon", "Flamespyre Phoenix", "Frostheart Phoenix"]
        }
    },
    "Storm Weaver": {
        # https://tow.whfb.app/unit/storm-weaver - 85 pts
        # 0-1 per 1,000 points in a Grand Army list.
        "points": 85,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Ithilmar Weapons", "Lore of Saphery", "Valour of Ages"],
            "WizardLevel": 1,
            "Lores": ["Dark Magic", "Elementalism", "Illusion"],
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
            "mounts": ["Unicorn"]
        }
    },
    "Dragon Mage": {
        # https://tow.whfb.app/unit/dragon-mage - 275 pts
        # Movement is '-' on the profile; the Sun Dragon mount (M6 WS5 S5 I4 A4)
        # supplies it, and T5/W6 are the dragon's. The mount is not simulated.
        "points": 275,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 6,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blessings of Asuryan", "Close Order", "Dragon Armour", "Elven Reflexes", "Fly (10)", "Impetuous", "Ithilmar Weapons", "Large Target", "Lileath's Blessing", "Lore of Saphery", "Stomp Attacks (D6)", "Swiftstride", "Terror", "Valour of Ages"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism"],
            "TroopType": "Behemoth",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Sun Dragon"]
        }
    },
    "Korhil Lionmane": {
        # https://tow.whfb.app/unit/korhil-lionmane - 175 pts
        # Fixed wargear. Furious Charge and Move Through Cover do not apply to
        # his mount.
        "points": 175,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 7,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Chayal",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Furious Charge", "Mighty Constitution", "Move Through Cover", "Stubborn", "Valour of Ages"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Chayal"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": ["Pelt of Charandis"],
        },
        "mount_options": {
            "mounts": ["Chieftain's Chariot"]
        }
    },
    "Ishaya Vess": {
        # https://tow.whfb.app/unit/ishaya-vess - 170 pts
        # Fixed wargear: also a warbow. Her shield is standard, so pass
        # Shield=False to wield the two-handed Mathlann's Ire.
        "points": 170,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 7,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 7,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Mathlann's Ire",
            "Shield": True,
            "SpecialRules": ["Commanding Voice", "Ithilmar Weapons", "Naval Discipline", "Precision Strikes", "Rallying Cry", "Strike First", "Valour of Ages"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Mathlann's Ire", "Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": ["Mathlann's Ire"],
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
    "Chracian Woodsmen": {
        # https://tow.whfb.app/unit/chracian-woodsmen - 12 pts per model, unit size 5+
        # Fights with the Chracian Woodsman row.
        # Shooting is not simulated, so these are left out of the options: warbows.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Chracian Captain', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Chracian Great Blade",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Move Through Cover", "Skirmishers", "Valour of Ages", "Vanguard"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Lion Cloak", "Scouts", "Ambushers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Chracian Great Blade"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Elven Archers": {
        # https://tow.whfb.app/unit/elven-archers - 9 pts per model, unit size 5+
        # Fights with the Elven Archer row.
        # Shooting is not simulated, so these are left out of the options: longbows.
        "points": 9,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Sentinel', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
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
            "Race": "High Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Detachment", "Elven Reflexes", "Valour of Ages"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Valour of Ages", "Veteran"],
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
    "Elven Spearmen": {
        # https://tow.whfb.app/unit/elven-spearmen - 8 pts per model, unit size 5+
        # Fights with the Elven Spearman row.
        "points": 8,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Sentinel', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
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
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Thrusting Spear",
            "Shield": True,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Martial Prowess", "Regimental Unit", "Valour of Ages"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Shieldwall", "Valour of Ages", "Veteran"],
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
    "Lion Guard": {
        # https://tow.whfb.app/unit/lion-guard - 17 pts per model, unit size 5+
        # Fights with the Lion Guard Captain row.
        "points": 17,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Lion Guard', 'Movement': 5, 'WeaponSkill': 6, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 1, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Chracian Great Blade",
            "Shield": False,
            "SpecialRules": ["Champions of Chrace", "Close Order", "Elven Reflexes", "Furious Charge", "Lion Cloak", "Stubborn", "Veteran"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Chracian Great Blade"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Lothern Sea Guard": {
        # https://tow.whfb.app/unit/lothern-sea-guard - 10 pts per model, unit size 5+
        # Fights with the Sea Guard row.
        # Shooting is not simulated, so these are left out of the options: warbows.
        "points": 10,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Sea Master', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
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
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Thrusting Spear",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Martial Prowess", "Naval Discipline", "Valour of Ages"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Valour of Ages", "Veteran"],
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
    "Phoenix Guard": {
        # https://tow.whfb.app/unit/phoenix-guard - 16 pts per model, unit size 5+
        # Fights with the Phoenix Guard row.
        "points": 16,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Keeper of the Flame', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
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
            "Race": "High Elf",
            "Armor": "Full Plate Armor",
            "Weapon": "Ceremonial Halberd",
            "Shield": False,
            "SpecialRules": ["Blessings of Asuryan", "Close Order", "Elven Reflexes", "Fear", "Martial Prowess", "Veteran", "Witness to Destiny"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Ceremonial Halberd"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Shadow Warriors": {
        # https://tow.whfb.app/unit/shadow-warriors - 14 pts per model, unit size 5+
        # Fights with the Shadow Warrior row.
        # Shooting is not simulated, so these are left out of the options: longbows.
        "points": 14,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Shadow-walker', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 6, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
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
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Evasive", "Fire & Flee", "Ithilmar Weapons", "Move Through Cover", "Scouts", "Skirmishers", "Veteran", "Warriors of Nagarythe"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers", "Chariot Runners", "Feigned Flight"],
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
    "Ship's Company": {
        # https://tow.whfb.app/unit/ships-company - 9 pts per model, unit size 5+
        # Fights with the Ship's Company row.
        # Also has a profile for Bosun (M5 WS4 BS4 S3 T3 W1 I4 A2 Ld8); not simulated.
        # Shooting is not simulated, so these are left out of the options: warbows.
        "points": 9,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Midshipman', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Bosun', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        ],
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
            "Race": "High Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Detachment", "Elven Reflexes", "Evasive", "Fire & Flee", "Open Order", "Valour of Ages"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Open Order", "Skirmishers", "Valour of Ages", "Veteran"],
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
    "Sisters of Avelorn": {
        # https://tow.whfb.app/unit/sisters-of-avelorn - 15 pts per model, unit size
        # 5+
        # Fights with the Sister of Avelorn row.
        # Shooting is not simulated, so these are left out of the options: bows of
        # Avelorn.
        "points": 15,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'High Sister', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 6, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
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
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arrows of Isha", "Evasive", "Ignores Cover", "Immune to Psychology", "Ithilmar Armour", "Ithilmar Weapons", "Open Order", "Skirmishers", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers", "Stubborn"],
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
    "Swordmasters of Hoeth": {
        # https://tow.whfb.app/unit/swordmasters-of-hoeth - 14 pts per model, unit
        # size 5+
        # Fights with the Swordmaster row.
        "points": 14,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Bladelord', 'Movement': 5, 'WeaponSkill': 6, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 6, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Sword of Hoeth",
            "Shield": False,
            "SpecialRules": ["Cleaving Blow", "Close Order", "Deflect Shots", "Elven Reflexes", "Ithilmar Armour", "Magic Resistance (-1)", "Valour of Ages", "Warriors of the White Tower"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Sword of Hoeth"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "White Lions of Chrace": {
        # https://tow.whfb.app/unit/white-lions-of-chrace - 14 pts per model, unit
        # size 5+
        # Fights with the White Lion row.
        "points": 14,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Guardian', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
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
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Chracian Great Blade",
            "Shield": False,
            "SpecialRules": ["Chracian Warriors", "Elven Reflexes", "Furious Charge", "King's Guard", "Lion Cloak", "Move Through Cover", "Open Order", "Stubborn", "Valour of Ages"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Valour of Ages", "Veteran"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Chracian Great Blade"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Dragon Princes": {
        # https://tow.whfb.app/unit/dragon-princes - 37 pts per model, unit size 3+
        # Fights with the Dragon Prince row.
        # Also has a profile for Barded Elven Steed (M8 WS3 BS- S3 T- W- I4 A1 Ld-);
        # not simulated.
        "points": 37,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Drakemaster', 'Movement': None, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 3, 'Leadership': 9},
        "other_profiles": [
            {'Name': 'Barded Elven Steed', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": "Full Plate Armor",
            "Weapon": "Lance",
            "Shield": True,
            "SpecialRules": ["Close Order", "Counter Charge", "Dragon Armour", "Drilled", "Elven Reflexes", "First Charge", "Impetuous", "Ithilmar Barding", "Ithilmar Weapons", "Sons of Caledor", "Swiftstride", "Valour of Ages"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Lance"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Ellyrian Reavers": {
        # https://tow.whfb.app/unit/ellyrian-reavers - 16 pts per model, unit size 5+
        # Fights with the Ellyrian Reaver row.
        # Also has a profile for Elven Steed (M9 WS3 BS- S3 T- W- I4 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: shortbows.
        "points": 16,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Harbinger', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Elven Steed', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
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
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Fast Cavalry", "Open Order", "Swiftstride", "Valour of Ages"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Scouts", "Skirmishers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Silver Helms": {
        # https://tow.whfb.app/unit/silver-helms - 23 pts per model, unit size 4+
        # Fights with the Silver Helm row.
        # Also has a profile for Barded Elven Steed (M8 WS3 BS- S3 T- W- I4 A1 Ld-);
        # not simulated.
        "points": 23,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'High Helm', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Barded Elven Steed', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Lance",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes", "First Charge", "Ithilmar Barding", "Swiftstride", "Valour of Ages"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
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
    "War Lions": {
        # https://tow.whfb.app/unit/war-lions - 18 pts per model, unit size 2-6
        # Fights with the War Lion row.
        "points": 18,
        "points_per": "model",
        "unit_size": "2-6",
        "other_profiles": [],
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "High Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Cleaving Blow", "Fear", "Move Through Cover", "Open Order", "Swiftstride", "Vanguard"],
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
    "Chieftain's Chariot": {
        # https://tow.whfb.app/unit/chieftains-chariot - 105 pts per unit
        # Fights with the Charioteer (x1) row, using the Chieftain's Chariot row's
        # Toughness and Wounds.
        # Also has a profile for Chieftain's Chariot (M- WS- BS- S5 T4 W3 I- A- Ld-);
        # not simulated.
        # Also has a profile for Chracian Lion (x2) (M8 WS5 BS- S4 T- W- I4 A2 Ld-);
        # not simulated.
        # Armour value 4+ as printed on the site.
        "points": 105,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': "Chieftain's Chariot", 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 4, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
            {'Name': 'Chracian Lion (x2)', 'Movement': 8, 'WeaponSkill': 5, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 1,
            "Leadership": None,
            "Race": "High Elf",
            "Armor": "Full Plate Armor",
            "Weapon": "Chracian Great Blade",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1, Chracian Lions only)", "Close Order", "Elven Reflexes", "Fear", "First Charge", "Impact Hits (D6, Chieftain's Chariot only)", "Stubborn", "Valour of Ages"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Chracian Great Blade"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Lion Chariot of Chrace": {
        # https://tow.whfb.app/unit/lion-chariot-of-chrace - 125 pts per unit
        # Fights with the Lion Charioteer (x2) row, using the Lion Chariot row's
        # Toughness and Wounds.
        # Also has a profile for Lion Chariot (M- WS- BS- S5 T4 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for War Lion (x2) (M8 WS5 BS- S4 T- W- I4 A2 Ld-); not
        # simulated.
        # Armour value 4+ as printed on the site.
        "points": 125,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Lion Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 4, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'War Lion (x2)', 'Movement': 8, 'WeaponSkill': 5, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Full Plate Armor",
            "Weapon": "Chracian Great Blade",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Fear", "First Charge", "Impact Hits (D6)", "Lion Cloak", "Stubborn", "Valour of Ages"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Chracian Great Blade"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Lothern Skycutter": {
        # https://tow.whfb.app/unit/lothern-skycutter - 90 pts per unit
        # Fights with the Sea Guard Crew (x3) row, using the Lothern Skycutter row's
        # Toughness and Wounds.
        # Also has a profile for Lothern Skycutter (M- WS- BS- S5 T4 W4 I- A- Ld-);
        # not simulated.
        # Also has a profile for Swiftfeather Roc (x1) (M2 WS5 BS- S4 T- W- I4 A2
        # Ld-); not simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: eagle-eye
        # bolt thrower, shortbows.
        "points": 90,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Lothern Skycutter', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 4, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Swiftfeather Roc (x1)', 'Movement': 2, 'WeaponSkill': 5, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
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
            "Race": "High Elf",
            "Armor": "Full Plate Armor",
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes (Crew only)", "Fear", "Fly (10)", "Impact Hits (D3+1)", "Swiftstride", "Valour of Ages"],
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
    "Tiranoc Chariot": {
        # https://tow.whfb.app/unit/tiranoc-chariot - 75 pts per model, unit size 1-4
        # Fights with the Tiranoc Charioteer (x2) row, using the Tiranoc Chariot row's
        # Toughness and Wounds.
        # Also has a profile for Tiranoc Chariot (M- WS- BS- S5 T4 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Elven Steed (x2) (M9 WS3 BS- S3 T- W- I4 A1 Ld-); not
        # simulated.
        # Armour value 5+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: longbows.
        "points": 75,
        "points_per": "model",
        "unit_size": "1-4",
        "other_profiles": [
            {'Name': 'Tiranoc Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 4, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Elven Steed (x2)', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
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
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Impact Hits (D6)", "Open Order", "Quick Shot", "Swiftstride", "Valour of Ages"],
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
    "Flamespyre Phoenix": {
        # https://tow.whfb.app/unit/flamespyre-phoenix - 170 pts per unit
        # Fights with the Flamespyre Phoenix row.
        "points": 170,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 2,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 5,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Blessings of Asuryan", "Close Order", "Fear", "Flaming Attacks", "Fly (10)", "From the Ashes", "Large Target", "Stomp Attacks (2)", "Swiftstride", "Wake of Fire"],
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
    "Frostheart Phoenix": {
        # https://tow.whfb.app/unit/frostheart-phoenix - 205 pts per unit
        # Fights with the Frostheart Phoenix row.
        "points": 205,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 2,
            "WeaponSkill": 6,
            "BallisticSkill": 0,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 3,
            "Wounds": 5,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Full Plate Armor",
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Blizzard Aura", "Close Order", "Fear", "Fly (9)", "Large Target", "Stomp Attacks (2)", "Swiftstride"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Wicked Claws"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Great Eagle": {
        # https://tow.whfb.app/unit/great-eagle - 60 pts per unit
        # Fights with the Great Eagle row.
        "points": 60,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 2,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 6,
            "Race": "High Elf",
            "Armor": None,
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Close Order", "Fear", "Fly (10)", "Stomp Attacks (1)", "Swiftstride"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Wicked Claws", "Serrated Maw"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Merwyrm": {
        # https://tow.whfb.app/unit/merwyrm - 200 pts per unit
        # Fights with the Merwyrm row.
        # Shooting is not simulated, so these are left out of the options: briny
        # breath.
        "points": 200,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 0,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 3,
            "Wounds": 6,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Lashing Talons",
            "Shield": False,
            "SpecialRules": ["Abyssal Cloak", "Close Order", "Enfeebling Cold", "Impact Hits (D3)", "Large Target", "Stomp Attacks (D3+1)", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Lashing Talons", "Serpentine Tail"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Eagle-Claw Bolt Thrower": {
        # https://tow.whfb.app/unit/eagle-claw-bolt-thrower - 70 pts per unit
        # Fights with the Sea Guard Crew row.
        # Also has a profile for Eagle-Claw Bolt Thrower (M- WS- BS- S- T6 W2 I- A-
        # Ld-); not simulated.
        # Shooting is not simulated, so these are left out of the options: Repeater
        # bolt thrower.
        "points": 70,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Eagle-Claw Bolt Thrower', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 2, 'Attacks': None, 'Leadership': None},
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
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Skirmishers", "Valour of Ages"],
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
    'Valour of Ages': {
        "status": None,
        "text": (
            "A unit with this special rule may re-roll any failed Panic test caused "
            "by taking heavy casualties or by being fled through by a friendly "
            "unit."
        ),
    },
    'Ithilmar Weapons': {
        "status": 'implemented',
        "text": (
            "Reroll To Hit rolls of a natural 1 when using a hand weapon. "
        ),
    },
    'Elven Reflexes': {
        "status": 'implemented',
        "text": (
            "+1 Initiative (max 10) during the first round of any combat. "
        ),
    },
    'Strike First': {
        "status": 'implemented',
        "text": (
            "Strikes before models without it, regardless of Initiative. "
        ),
    },
    "Lileath's Blessing": {
        "status": None,
        "text": (
            "Once per turn, a model with this special rule may re-roll a single "
            "failed Casting roll."
        ),
    },
    'Blessings of Asuryan': {
        "status": 'implemented',
        "text": (
            "A 5+ Ward save against Flaming Attacks. "
        ),
    },
    'Dragon Armour': {
        "status": 'implemented',
        "text": (
            "A 6+ Ward save. "
        ),
    },
    'Witness to Destiny': {
        "status": 'implemented',
        "text": (
            "A 6+ Ward save. "
        ),
    },
    'Lion Cloak': {
        "status": None,
        "text": (
            "A model with this special rule improves its armour value by 1 (to a "
            "maximum of 2+) against non-magical shooting attacks."
        ),
    },
    "Abyssal Cloak": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/abyssal-cloak",
        "text": (
            "Any enemy model that targets this model during the Shooting phase "
            "suffers a -2 To Hit modifier for firing at long range, rather than the "
            "usual -1."
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
    "Arrows of Isha": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/arrows-of-isha",
        "text": (
            "Any bow (longbow, shortbow, warbow or Bow of Avelorn) carried by a "
            "model with this special rule has the Armour Bane (1) special rule and "
            "an Armour Piercing characteristic of -1."
        ),
    },
    "Blizzard Aura": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/blizzard-aura",
        "text": (
            "Whilst in base contact with this model, enemy models become subject to "
            "the Strike Last special rule."
        ),
    },
    "Champions of Chrace": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/champions-of-chrace",
        "text": (
            "Any model in a unit of Lion Guard can accept challenges in the same "
            "manner as a character. In addition, once per turn a character that has "
            "joined a unit of Lion Guard may re-roll their \"Look Out, Sir!\" roll."
        ),
    },
    "Chracian Warriors": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/chracian-warriors",
        "text": (
            "A unit with this special rule may only be joined by your army's "
            "General, or by a character with the Chracian Hunter Elven Honour."
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
    "Deflect Shots": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/deflect-shots",
        "text": (
            "A model with this special rule has a 6+ Ward save against any wounds "
            "suffered that were caused by a non-magical shooting attack."
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
    "Enfeebling Cold": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/enfeebling-cold",
        "text": (
            "Whilst in base contact with this model, enemy models suffer a - 1 "
            "modifier to their Strength characteristic (to a minimum of 1)."
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
    "From the Ashes": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/from-the-ashes",
        "text": (
            "When a Flamespyre Phoenix loses its last Wound, roll a D6 before "
            "removing the model from play: - On a roll of 1-2, the Phoenix crumbles "
            "into cold ashes and is removed from play. - On a roll of 3-5, the "
            "Phoenix explodes into flame. Every enemy unit in base contact with it "
            "suffers D6 Strength 3 hits, each with an AP of -1 and the Flaming "
            "Attacks special rule. Once these hits are resolved, this model is "
            "removed from play. - On a roll of 6, the Phoenix (and its rider, "
            "should it have one) are briefly consumed in a ball of flames, and are "
            "immediately reborn, recovering D3 Wounds."
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
    "Ignores Cover": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ignores-cover",
        "text": (
            "If a model making a shooting attack has this special rule, it ignores "
            "any To Hit modifiers caused by partial or full cover."
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
    "Ithilmar Armour": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ithilmar-armour-ithilmar-barding",
        "text": (
            "A model with this special rule may re-roll any rolls of 1 when making "
            "Dangerous Terrain tests. In addition, a Wizard with this special rule "
            "may wear armour without penalty."
        ),
    },
    "Ithilmar Barding": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ithilmar-armour-ithilmar-barding",
        "text": (
            "A model with this special rule may re-roll any rolls of 1 when making "
            "Dangerous Terrain tests. In addition, a Wizard with this special rule "
            "may wear armour without penalty."
        ),
    },
    "King's Guard": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/kings-guard",
        "text": (
            "Any model in a unit of White Lions of Chrace that has been joined by "
            "your army's General can issue and accept challenges in the same manner "
            "as a character. Should your General leave the unit for any reason, the "
            "unit loses this ability."
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
    "Naval Discipline": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/naval-discipline",
        "text": (
            "A unit of Lothern Sea Guard may use this special rule when it makes a "
            "Stand & Shoot charge reaction. A unit that does so can make a Stand & "
            "Shoot charge reaction regardless of how close the charging unit is. "
            "Once this shooting has been resolved, the charged unit may make a free "
            "redress the ranks manoeuvre, after which it will Hold and await the "
            "charging unit. Units that are fleeing, that are already engaged in "
            "combat when charged, or that have been joined by a character that does "
            "not have this special rule cannot use this special rule."
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
    "Quick Shot": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/quick-shot",
        "text": (
            "A weapon with this special rule does not suffer the usual -1 To Hit "
            "modifier for Moving and Shooting. In addition, a unit equipped with "
            "weapons with this special rule can use them to make a Stand & Shoot "
            "charge reaction regardless of how close the charging unit is."
        ),
    },
    "Regimental Unit": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/regimental-unit",
        "text": (
            "A unit with this special rule can be accompanied by detachment."
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
    "Sons of Caledor": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/sons-of-caledor",
        "text": (
            "A unit with this special rule may only be joined by your army's "
            "General, or by a character with the Blood of Caledor Elven Honour."
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
    "Veteran": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/veteran",
        "text": (
            "If the majority of the models in a unit have this special rule, the "
            "unit may re-roll any failed Leadership test. Note that a Break test is "
            "not a Leadership test."
        ),
    },
    "Wake of Fire": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/wake-of-fire",
        "text": (
            "This model may perform a 'Wake of Fire' attack against a single enemy "
            "unit that is not engaged in combat. To do so, this model must move (by "
            "flying) over the unit it wishes to attack during the Remaining Moves "
            "sub-phase. Once this model's movement is complete, the enemy unit "
            "suffers D6 Strength 4 hits, each with an AP of -1 and with the Flaming "
            "Attacks special rule."
        ),
    },
    "Warriors of Nagarythe": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/warriors-of-nagarythe",
        "text": (
            "A unit with this special rule may only be joined by a character with "
            "the Shadow Stalker Elven Honour."
        ),
    },
    "Warriors of the White Tower": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/warriors-of-the-white-tower",
        "text": (
            "A unit with this special rule may only be joined by a High Elf Mage, "
            "or by a character with either the Warden of Saphery or Loremaster "
            "Elven Honour."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
