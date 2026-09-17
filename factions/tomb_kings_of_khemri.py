"""Tomb Kings of Khemri.

Profiles from https://tow.whfb.app/army/tomb-kings-of-khemri, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Tomb Kings of Khemri"

# Other names that should resolve to this faction.
ALIASES = [
    "Tomb Kings",
    "TK",
    "Khemri",
    "Tomb Kings of Khemri",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Settra": "Settra the Imperishable",
    "Apophas": "Prince Apophas",
}

CHARACTERS = {
    "Nekaph": {
        # https://tow.whfb.app/unit/nekaph - 120 pts
        "points": 120,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "The Flail of Conquered Kings",
            "Shield": False,
            "SpecialRules": ["Dry as Dust", "Flammable", "Herald of Despair", "Indomitable (2)", "Killing Blow", "Nehekharan Undead", "Regeneration (5+)", "Settra's Champion", "Killing Blow 5+", "Sworn Protector"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["The Flail of Conquered Kings"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": ["The Flail of Conquered Kings"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Prince Apophas": {
        # https://tow.whfb.app/unit/prince-apophas - 130 pts
        # Shooting is not simulated, so these are left out of the options: swarming
        # mass.
        "points": 130,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 1,
            "Wounds": 4,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ambushers", "Fly (9)", "Indomitable (2)", "Khopesh", "Loner", "Nehekharan Undead", "Regeneration (5+)", "Scarab Prince", "Usirian's Reaper", "Terror"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
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
    "Settra the Imperishable": {
        # https://tow.whfb.app/unit/settra-the-imperishable - 445 pts
        # Also has a profile for Chariot of the Gods (M- WS- BS- S5 T5 W8 I- A- Ld-);
        # not simulated.
        # Also has a profile for Skeletal Steed (x4) (M8 WS2 BS- S3 T- W- I2 A1 Ld-);
        # not simulated.
        # Armour value 4+ as printed on the site.
        # Settra's own Wounds are '-': he uses the Chariot of the Gods' W8 (and its
        # T5, the same as his).
        "points": 445,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 7,
            "BallisticSkill": 3,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 8,
            "Attacks": 5,
            "Leadership": 10,
            "Race": "Tomb King",
            "Armor": "Full Plate Armor",
            "Weapon": "The Blessed Blade of Ptra",
            "Shield": False,
            "SpecialRules": ["Commander of Legions", "Curse of the Necropolis", "Dry as Dust", "Flammable", "Impact Hits (2D3)", "Indomitable (3)", "Lore of Nehekhara", "My Will Be Done", "Nehekharan Undead", "Regeneration (5+)", "Settra Does Not Kneel!", "Settra the Great"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "NamedCharacter",
            "WizardLevel": 1,
            "Lores": ["Necromancy"],
        },
        "equipment_options": {
            "weapons": ["The Blessed Blade of Ptra"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": ["The Blessed Blade of Ptra", "The Chariot of the Gods", "The Crown of Nehekhara", "The Scarab Brooch of Usirian"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Arch Necrotect": {
        # https://tow.whfb.app/unit/arch-necrotect - 90 pts
        "points": 90,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dry as Dust", "Flammable", "Immortal Overseer", "Khopesh", "Nehekharan Undead", "Regeneration (5+)", "Stone Shaper"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Incantation Scroll"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Whip"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "High Priest": {
        # https://tow.whfb.app/unit/high-priest - 140 pts
        "points": 140,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arise!", "Curse of the Necropolis", "Indomitable (1)", "Khopesh", "Lore of Nehekhara", "Nehekharan Undead", "Regeneration (5+)", "From Beneath the Sands"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 3,
            "Lores": ["Elementalism", "Illusion", "Necromancy"],
            "OptionalRules": ["Incantation Scrolls"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Tomb Kings)", "Barded Skeletal Steed", "Necrolith Bone Dragon"]
        }
    },
    "Mortuary Priest": {
        # https://tow.whfb.app/unit/mortuary-priest - 55 pts
        "points": 55,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arise!", "Curse of the Necropolis", "Indomitable (1)", "Khopesh", "Lore of Nehekhara", "Nehekharan Undead", "Regeneration (5+)", "From Beneath the Sands"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Elementalism", "Illusion", "Necromancy"],
            "OptionalRules": ["Incantation Scrolls"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Tomb Kings)", "Barded Skeletal Steed"]
        }
    },
    "Necrotect": {
        # https://tow.whfb.app/unit/necrotect - 55 pts
        "points": 55,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dry as Dust", "Eternal Taskmaster", "Flammable", "Khopesh", "Nehekharan Undead", "Regeneration (6+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Incantation Scroll"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Whip"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Royal Herald": {
        # https://tow.whfb.app/unit/royal-herald - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Banner of the King", "Dry as Dust", "Flammable", "Indomitable (1)", "Khopesh", "Nehekharan Undead", "Regeneration (5+)", "Sworn Protector"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail", "Great Weapon", "Halberd", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Tomb Kings)", "Barded Skeletal Steed", "Skeleton Chariot"]
        }
    },
    "Tomb King": {
        # https://tow.whfb.app/unit/tomb-king - 160 pts
        "points": 160,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Tomb King",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Curse of the Necropolis", "Dry as Dust", "Flammable", "Indomitable (2)", "Khopesh", "My Will Be Done", "Nehekharan Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail", "Great Weapon", "Halberd", "Cavalry Spear"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Tomb Kings)", "Barded Skeletal Steed", "Skeleton Chariot", "Necrolith Bone Dragon", "Khemrian Warsphinx"]
        }
    },
    "Tomb Prince": {
        # https://tow.whfb.app/unit/tomb-prince - 90 pts
        "points": 90,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Curse of the Necropolis", "Dry as Dust", "Flammable", "Indomitable (2)", "Khopesh", "My Will Be Done", "Nehekharan Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail", "Great Weapon", "Halberd", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Tomb Kings)", "Barded Skeletal Steed", "Skeleton Chariot"]
        }
    },
}

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Carrion": {
        # https://tow.whfb.app/unit/carrion - 27 pts per model, unit size 2+
        # Fights with the Carrion row.
        "points": 27,
        "points_per": "model",
        "unit_size": "2+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 2,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 4,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fly (10)", "Nehekharan Undead", "Regeneration (6+)", "Skirmishers", "Swiftstride"],
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
    "Skeleton Archers": {
        # https://tow.whfb.app/unit/skeleton-archers - 5 pts per model, unit size 10+
        # (5+ if a detachment)
        # Fights with the Skeleton Archer row.
        # Shooting is not simulated, so these are left out of the options: warbows.
        "points": 5,
        "points_per": "model",
        "unit_size": "10+ (5+ if a detachment)",
        "champion": {'Name': 'Master of Arrows', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 2, 'Wounds': 1, 'Attacks': 1, 'Leadership': 5},
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
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arrows of Asaph", "Detachment", "Nehekharan Undead", "Open Order", "Regeneration (6+)"],
            "TroopType": "RegularInfantry",
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
    "Skeleton Infantry Cohort": {
        # https://tow.whfb.app/unit/skeleton-infantry-cohort - 5 pts per model, unit
        # size 10+/10+
        # Fights with the Royal Host Warrior row.
        # Also has a profile for Royal Host Archer (M4 WS2 BS2 S3 T3 W1 I2 A1 Ld5);
        # not simulated.
        "points": 5,
        "points_per": "model",
        "unit_size": "10+/10+",
        "champion": {'Name': 'Master of Arms', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [
            {'Name': 'Royal Host Archer', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 2, 'Wounds': 1, 'Attacks': 1, 'Leadership': 5},
        ],
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
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Thrusting Spear",
            "Shield": True,
            "SpecialRules": ["Arrows of Asaph", "Close Order", "Horde", "Motley Crew", "Nehekharan Undead", "Regeneration (6+)", "Regimental Unit", "Steadfast Discipline"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Nehekharan Phalanx"],
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
    "Skeleton Skirmishers": {
        # https://tow.whfb.app/unit/skeleton-skirmishers - 4 pts per model, unit size
        # 5-20
        # Fights with the Skeleton Skirmisher row.
        # Shooting is not simulated, so these are left out of the options: Warbows.
        "points": 4,
        "points_per": "model",
        "unit_size": "5-20",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 4,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arrows of Asaph", "Chariot Runners", "Nehekharan Undead", "Regeneration (6+)", "Skirmishers", "Vanguard"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Skeleton Warriors (Tomb Kings)": {
        # https://tow.whfb.app/unit/skeleton-warriors-tomb-kings - 4 pts per model,
        # unit size 10+
        # Fights with the Skeleton Warrior row.
        "points": 4,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Master of Arms', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
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
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Horde", "Nehekharan Undead", "Regeneration (6+)", "Regimental Unit"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Nehekharan Phalanx"],
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
    "Tomb Guard": {
        # https://tow.whfb.app/unit/tomb-guard - 10 pts per model, unit size 5+
        # Fights with the Tomb Guard row.
        "points": 10,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Tomb Captain', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Cleaving Blow", "Close Order", "Indomitable (1)", "Khopesh", "Nehekharan Undead", "Regeneration (6+)", "Regimental Unit"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled", "Nehekharan Phalanx"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Tomb Swarms": {
        # https://tow.whfb.app/unit/tomb-swarms - 37 pts per model, unit size 2-10
        # Fights with the Tomb Swarm row.
        "points": 37,
        "points_per": "model",
        "unit_size": "2-10",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 2,
            "Toughness": 2,
            "Initiative": 1,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 10,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dry as Dust", "Nehekharan Undead", "Poisoned Attacks", "Regeneration (6+)", "Skirmishers"],
            "TroopType": "Swarm",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers"],
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
    "Ushabti": {
        # https://tow.whfb.app/unit/ushabti - 49 pts per model, unit size 3+
        # Fights with the Ushabti row.
        # Shooting is not simulated, so these are left out of the options: greatbows.
        "points": 49,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Ancient', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 3, 'Attacks': 4, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Heavy Armor",
            "Weapon": "Ritual Blade",
            "Shield": False,
            "SpecialRules": ["Arrows of Asaph", "Close Order", "Indomitable (1)", "Khopesh", "Nehekharan Undead", "Regeneration (6+)"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Ritual Blade"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Venerable Ushabti": {
        # https://tow.whfb.app/unit/venerable-ushabti - 56 pts per model, unit size 3+
        # Fights with the Venerable Ushabti row.
        "points": 56,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Venerable Ancient', 'Movement': 4, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 5, 'Toughness': 4, 'Initiative': 2, 'Wounds': 3, 'Attacks': 4, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Heavy Armor",
            "Weapon": "Ritual Blade",
            "Shield": False,
            "SpecialRules": ["Close Order", "Indomitable (1)", "Khopesh", "Magic Resistance (-2)", "Nehekharan Undead", "Regeneration (6+)"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Ritual Blade"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Necropolis Knights": {
        # https://tow.whfb.app/unit/necropolis-knights - 54 pts per model, unit size
        # 2+
        # Fights with the Necropolis Knight row.
        # Also has a profile for Necroserpent (M7 WS3 BS- S5 T- W- I3 A3 Ld-); not
        # simulated.
        "points": 54,
        "points_per": "model",
        "unit_size": "2+",
        "champion": {'Name': 'Necropolis Captain', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 3, 'Wounds': 3, 'Attacks': 3, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Necroserpent', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 5, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 3, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Cavalry Spear",
            "Shield": True,
            "SpecialRules": ["Armoured Hide (1)", "Cleaving Blow (Riders only)", "Close Order", "Impact Hits (1)", "Indomitable (1)", "Khopesh", "Nehekharan Undead", "Poisoned Attacks (Necroserpent only)", "Regeneration (6+)", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Necroserpents": {
        # https://tow.whfb.app/unit/necroserpents - 38 pts per model, unit size 2+
        # Fights with the Necroserpent row.
        "points": 38,
        "points_per": "model",
        "unit_size": "2+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ambushers", "Armoured Hide (1)", "Impact Hits (1)", "Indomitable (1)", "Move Through Cover", "Nehekharan Undead", "Open Order", "Poisoned Attacks", "Regeneration (6+)", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
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
    "Sepulchral Stalkers": {
        # https://tow.whfb.app/unit/sepulchral-stalkers - 49 pts per model, unit size
        # 2+
        # Fights with the Sepulchral Stalkers row.
        # Shooting is not simulated, so these are left out of the options: petrifying
        # gaze.
        "points": 49,
        "points_per": "model",
        "unit_size": "2+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Heavy Armor",
            "Weapon": "Halberd",
            "Shield": False,
            "SpecialRules": ["Close Order", "Indomitable (1)", "Nehekharan Undead", "Regeneration (6+)", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Writhing Tail", "Halberd"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Skeleton Cavalry Cohort": {
        # https://tow.whfb.app/unit/skeleton-cavalry-cohort - 12 pts per model, unit
        # size 5+/5+
        # Fights with the Royal Host Horseman row.
        # Also has a profile for Royal Host Horse Archer (M- WS2 BS3 S3 T3 W1 I2 A1
        # Ld5); not simulated.
        # Also has a profile for Skeletal Steed (M8 WS2 BS- S3 T- W- I2 A1 Ld-); not
        # simulated.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+/5+",
        "champion": {'Name': 'Master of Horse', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [
            {'Name': 'Royal Host Horse Archer', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 2, 'Wounds': 1, 'Attacks': 1, 'Leadership': 5},
            {'Name': 'Skeletal Steed', 'Movement': 8, 'WeaponSkill': 2, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Cavalry Spear",
            "Shield": True,
            "SpecialRules": ["Arrows of Asaph", "Close Order", "Horde", "Motley Crew", "Nehekharan Undead", "Regeneration (6+)", "Steadfast Discipline", "Swiftstride", "Vanguard"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Counter Charge"],
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
    "Skeleton Horse Archers": {
        # https://tow.whfb.app/unit/skeleton-horse-archers - 11 pts per model, unit
        # size 5+
        # Fights with the Skeleton Horse Archer row.
        # Also has a profile for Skeletal Steed (M8 WS2 BS- S3 T- W- I2 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: warbows.
        "points": 11,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Master of Horse', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 2, 'Wounds': 1, 'Attacks': 1, 'Leadership': 5},
        "other_profiles": [
            {'Name': 'Skeletal Steed', 'Movement': 8, 'WeaponSkill': 2, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arrows of Asaph", "Nehekharan Undead", "Open Order", "Regeneration (6+)", "Reserve Move", "Scouts", "Skirmishers", "Swiftstride"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Chariot Runners"],
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
    "Skeleton Horsemen": {
        # https://tow.whfb.app/unit/skeleton-horsemen - 11 pts per model, unit size 4+
        # Fights with the Skeleton Horseman row.
        # Also has a profile for Skeletal Steed (M8 WS2 BS- S3 T- W- I2 A1 Ld-); not
        # simulated.
        "points": 11,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'Master of Horse', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [
            {'Name': 'Skeletal Steed', 'Movement': 8, 'WeaponSkill': 2, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Horde", "Nehekharan Undead", "Regeneration (6+)", "Swiftstride", "Vanguard"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Counter Charge"],
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
    "Skeleton Chariots": {
        # https://tow.whfb.app/unit/skeleton-chariots - 41 pts per model, unit size 1+
        # Fights with the Skeletal Crew (x2) row, using the Chariot row's Toughness
        # and Wounds.
        # Also has a profile for Chariot (M- WS- BS- S4 T4 W3 I- A- Ld-); not
        # simulated.
        # Also has a profile for Master Charioteer (M- WS3 BS2 S3 T- W- I2 A2 Ld7);
        # not simulated.
        # Also has a profile for Skeletal Steed (x2) (M8 WS2 BS- S3 T- W- I2 A1 Ld-);
        # not simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: warbows.
        "points": 41,
        "points_per": "model",
        "unit_size": "1+",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 4, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
            {'Name': 'Master Charioteer', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 2, 'Leadership': 7},
            {'Name': 'Skeletal Steed (x2)', 'Movement': 8, 'WeaponSkill': 2, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Tomb King",
            "Armor": "Full Plate Armor",
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Arrows of Asaph", "Dry as Dust", "Horde", "Impact Hits (D3)", "Nehekharan Undead", "Open Order", "Regeneration (6+)", "Reserve Move", "Swiftstride"],
            "TroopType": "LightChariot",
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
    "Tomb Guard Chariots": {
        # https://tow.whfb.app/unit/tomb-guard-chariots - 49 pts per model, unit size
        # 3+
        # Fights with the Tomb Guard Crew (x2) row, using the Chariot row's Toughness
        # and Wounds.
        # Also has a profile for Chariot (M- WS- BS- S4 T4 W3 I- A- Ld-); not
        # simulated.
        # Also has a profile for Tomb Captain (M- WS3 BS3 S4 T- W- I2 A2 Ld7); not
        # simulated.
        # Also has a profile for Skeletal Steed (x2) (M8 WS2 BS- S3 T- W- I2 A1 Ld-);
        # not simulated.
        # Carries a shield, which it cannot use with its Halberd; pass Shield=True
        # with a one-handed weapon.
        # Armour value 4+ as printed on the site.
        "points": 49,
        "points_per": "model",
        "unit_size": "3+",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 4, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
            {'Name': 'Tomb Captain', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 2, 'Leadership': 7},
            {'Name': 'Skeletal Steed (x2)', 'Movement': 8, 'WeaponSkill': 2, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Tomb King",
            "Armor": "Full Plate Armor",
            "Weapon": "Halberd",
            "Shield": False,
            "SpecialRules": ["Cleaving Blow (Tomb Guard Crew only)", "Dry as Dust", "Impact Hits (D3+1)", "Indomitable (2)", "Khopesh", "Nehekharan Undead", "Open Order", "Regeneration (6+)", "Reserve Move", "Swiftstride"],
            "TroopType": "LightChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Khemrian Warsphinx": {
        # https://tow.whfb.app/unit/khemrian-warsphinx - 175 pts per unit
        # Fights with the Khemrian Warsphinx row.
        # Also has a profile for Tomb Guard Crew (x2) (M- WS3 BS3 S4 T- W- I3 A1 Ld8);
        # not simulated.
        # Armour value 5+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: Fiery roar.
        "points": 175,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Tomb Guard Crew (x2)', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': 8},
        ],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": None,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 1,
            "Wounds": 5,
            "Attacks": 4,
            "Leadership": None,
            "Race": "Tomb King",
            "Armor": "Heavy Armor",
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Arrows of Asaph", "Cleaving Blow (Tomb Guard Crew only)", "Close Order", "Howdah", "Indomitable (2)", "Khopesh (Tomb Guard Crew only)", "Large Target", "Nehekharan Undead", "Regeneration (6+)", "Stomp Attacks (D3)", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Wicked Claws", "Envenomed Sting"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Necrolith Colossus": {
        # https://tow.whfb.app/unit/necrolith-colossus - 160 pts per unit
        # Fights with the Necrolith Colossus row.
        "points": 160,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 1,
            "Wounds": 5,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Heavy Armor",
            "Weapon": "Paired Great Khopeshes",
            "Shield": False,
            "SpecialRules": ["Close Order", "Indomitable (2)", "Large Target", "Nehekharan Undead", "Regeneration (6+)", "Stomp Attacks (D3)", "Terror", "Timmm-berrr!", "Unstoppable Assault"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Paired Great Khopeshes"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Necrosphinx": {
        # https://tow.whfb.app/unit/necrosphinx - 195 pts per unit
        # Fights with the Necrosphinx row.
        "points": 195,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 1,
            "Wounds": 6,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Heavy Armor",
            "Weapon": "Cleaving Blades",
            "Shield": False,
            "SpecialRules": ["Close Order", "Fly (9)", "Indomitable (2)", "Large Target", "Nehekharan Undead", "Regeneration (5+)", "Stomp Attacks (D3+2)", "Swiftstride", "Terror", "Soul Reaper"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Cleaving Blades", "Decapitating Strike", "Envenomed Sting"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Tomb Scorpion": {
        # https://tow.whfb.app/unit/tomb-scorpion - 70 pts per unit
        # Fights with the Tomb Scorpion row.
        "points": 70,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Heavy Armor",
            "Weapon": "Decapitating Claws",
            "Shield": False,
            "SpecialRules": ["Close Order", "Indomitable (1)", "Magic Resistance (-1)", "Nehekharan Undead", "Regeneration (6+)", "Stomp Attacks (D3)", "Swiftstride", "Vanguard"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers"],
        },
        "equipment_options": {
            "weapons": ["Decapitating Claws", "Envenomed Sting"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Winged Warsphinx": {
        # https://tow.whfb.app/unit/winged-warsphinx - 180 pts per unit
        # Fights with the Winged Warsphinx row.
        # Armour value 5+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: Fiery roar.
        "points": 180,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 1,
            "Wounds": 5,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Heavy Armor",
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Close Order", "Counter Charge", "Fly (9)", "Indomitable (2)", "Large Target", "Nehekharan Undead", "Regeneration (6+)", "Stomp Attacks (D3)", "Swiftstride", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Wicked Claws", "Envenomed Sting"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Casket of Souls": {
        # https://tow.whfb.app/unit/casket-of-souls - 135 pts per unit
        # Fights with the Casket Guardians row.
        # Also has a profile for Casket of Souls (M- WS- BS- S- T6 W4 I- A- Ld-); not
        # simulated.
        "points": 135,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Casket of Souls', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Cleaving Blow", "Covenant of Power", "Dry as Dust", "Immovable Object", "Indomitable (2)", "Nehekharan Undead", "Regeneration (5+)", "Skirmishers", "Unbound Spirits", "Vortex of Souls"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Screaming Skull Catapult": {
        # https://tow.whfb.app/unit/screaming-skull-catapult - 105 pts per unit
        # Fights with the Skeleton Crew row.
        # Also has a profile for Screaming Skull Catapult (M- WS- BS- S- T6 W3 I- A-
        # Ld-); not simulated.
        # Shooting is not simulated, so these are left out of the options: Screaming
        # skull catapult.
        "points": 105,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Screaming Skull Catapult', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 5,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dry as Dust", "Indomitable (1)", "Nehekharan Undead", "Regeneration (6+)", "Skirmishers"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
            "OptionalRules": ["Skulls of the Foe"],
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
    "Arise!": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/arise",
        "text": (
            "During the Command sub-phase of their turn, if they are not engaged in "
            "combat, this character may attempt to resurrect the fallen by making a "
            "Leadership test (using their own Leadership). If this test is passed, "
            "a single friendly unit that has the Nehekharan Undead special rule and "
            "is within 12\" of this character recovers a number of lost Wounds. "
            "However, magically repairing gigantic undead constructs is much harder "
            "than raising skeletons from the sand. Therefore, how many Wounds are "
            "recovered depends upon the unit's troop type and this character's "
            "Level of Wizardry: - If the unit's troop type is regular infantry, "
            "heavy infantry or swarms, it recovers a number of Wounds equal to this "
            "[...]"
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
    "Arrows of Asaph": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/arrows-of-asaph",
        "text": (
            "Units with this special rule never apply any modifiers to their rolls "
            "To Hit when shooting, regardless of the source of the modifier."
        ),
    },
    "Banner of the King": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/banner-of-the-king",
        "text": (
            "A Royal Herald that has been upgraded to be your Battle Standard "
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
    "Commander of Legions": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/commander-of-legions",
        "text": (
            "Settra gains the Arise! special rule and, unlike other models with "
            "this special rule, may use it even when engaged in combat."
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
    "Covenant of Power": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/covenant-of-power",
        "text": (
            "Whilst within 12\" of a Casket of Souls, friendly Liche Priests may "
            "apply a +1 modifier to any Casting roll they make. Additionally, any "
            "model (friend or foe) that casts a Bound spell whilst within 12\" of a "
            "Casket of Souls may apply a +1 modifier to the Casting roll. Note, "
            "however, that this bonus does not apply to any Bound spells cast by a "
            "Casket of Souls."
        ),
    },
    "Curse of the Necropolis": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/curse-of-the-necropolis",
        "text": (
            "If a model with this special rule loses its last Wound to an enemy "
            "attack, the unit that made the attack must immediately make a "
            "Leadership test. If this test is failed, the enemy unit suffers D3 "
            "Strength 2 hits, each with an AP of -."
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
    "Dry as Dust": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dry-as-dust",
        "text": (
            "Each time this model suffers an unsaved wound from a Flaming Attack, "
            "your opponent may roll a D6. On a roll of 1-3, the flames quickly die "
            "down and this model escapes further harm. On a roll of 4+, the flames "
            "take hold and this model loses one additional Wound. Note that excess "
            "wounds caused to a model will have no additional effect except in the "
            "case of a character that is part of a challenge, in which case this "
            "special rule counts for Overkill. Excess wounds do not 'spill over' "
            "onto other models in the unit."
        ),
    },
    "Eternal Taskmaster": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/eternal-taskmaster",
        "text": (
            "During the Command sub-phase of their turn, this character may attempt "
            "to drive a unit they have joined to greater efforts by making a "
            "Leadership test (using their own Leadership). If this test is passed, "
            "until your next Start of Turn sub-phase this character and any unit "
            "they have joined gains the Extra Attacks (+1) and Hatred (all enemies) "
            "special rules."
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
    "From Beneath the Sands": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/from-beneath-the-sands",
        "text": (
            "During the Command sub-phase of their turn, if they are not engaged in "
            "combat, this character may choose a single friendly unit that has both "
            "the Nehekharan Undead and the Ambushers special rules, and that is "
            "currently held in reserve, and attempt to summon it by making a "
            "Leadership test (using their own Leadership): - If this test is "
            "passed, the chosen unit is successfully summoned and can be placed on "
            "the battlefield anywhere completely within 12\" of this model, but not "
            "within 6\" of any enemy models. The unit cannot charge during this turn "
            "and counts as having moved for the purposes of shooting, but can "
            "otherwise act as normal. - If this test is failed, the Ambushers pay "
            "no heed to this [...]"
        ),
    },
    "Herald of Despair": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/herald-of-despair",
        "text": (
            "Any enemy unit that is in base contact with Nekaph or a unit he has "
            "joined must roll an extra D6 when making a Fear or Terror test, and "
            "discard the lowest result."
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
    "Immortal Overseer": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/immortal-overseer",
        "text": (
            "During the Command sub-phase of their turn, this character may attempt "
            "to drive a single friendly unit within their Command range to greater "
            "efforts by making a Leadership test (using their own Leadership). If "
            "this test is passed, until your next Start of Turn sub-phase that unit "
            "gains a +D3 modifier to its Initiative characteristic (to a maximum of "
            "10)."
        ),
    },
    "Immovable Object": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/immovable-object",
        "text": (
            "Once this model has been placed on the battlefield during deployment "
            "it cannot be moved by its crew during the Remaining Moves sub-phase. "
            "Note that the model can still pivot freely at any time during its turn "
            "(the better to face the enemy) and may make a follow up move as "
            "normal."
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
    "Khopesh": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/khopesh",
        "text": (
            "A hand weapon carried by a model with this special rule has an Armour "
            "Piercing characteristic of -1. Note that this special rule only "
            "applies to a single, ordinary hand weapon and does not apply to a "
            "model's mount (should it have one). If the model is using two hand "
            "weapons or any other sort of weapon, this special rule ceases to "
            "apply."
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
    "Loner": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/loner",
        "text": (
            "A character with this special rule cannot be your General and cannot "
            "join a unit without this special rule. A unit with this special rule "
            "cannot be joined by a character without this special rule."
        ),
    },
    "Lore of Nehekhara": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-nehekhara",
        "text": (
            "The magic of Nehekhara was perfected millennia ago and has remained "
            "unchanged in the long centuries since. The wording of every "
            "incantation used in the preservation and reanimating of the dead is "
            "recorded on dusty papyrus in the mysterious hieroglyphs of Nehekhara’s "
            "ancient language, to be uttered aloud in long, monotonous ritual. A "
            "Wizard with the 'Lore of Nehekhara' special rule may discard one of "
            "their randomly generated spells as normal. When they do so, they may "
            "select instead either the signature spell of their chosen Lore of "
            "Magic, or one of the spells listed below. Lore of Nehekhara Lore"
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
    "My Will Be Done": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/my-will-be-done",
        "text": (
            "During the Command sub-phase of their turn, this character may attempt "
            "to exert their will upon those around them by making a Leadership test "
            "(using their own Leadership). If this test is passed, choose one of "
            "the following modifiers. Until your next Start of Turn sub-phase this "
            "character, their mount and any unit they have joined gain that "
            "modifier (to a maximum of 10): - \"Forward to Glory!\": +D3 Movement. - "
            "\"My Worthy Champions!\": +1 Weapon Skill. - \"Strike like the Cobra!\": "
            "+D3 Initiative. Note that this special rule is not cumulative. In "
            "other words, using it more than once on the same unit during the same "
            "turn has no further effect."
        ),
    },
    "Nehekharan Undead": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/nehekharan-undead",
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
    "Scarab Prince": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/scarab-prince",
        "text": (
            "Should Prince Apophas lose his last Wound, before his model is removed "
            "from play, all enemy units within 2D6\" of him suffer 2D6 Strength 2 "
            "hits with an AP of -1."
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
    "Settra Does Not Kneel!": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/settra-does-not-kneel",
        "text": (
            "Settra must always accept a challenge unless Nekaph, Emissary of "
            "Settra is engaged in the same combat. In which case, Nekaph must "
            "accept the challenge on Settra's behalf."
        ),
    },
    "Settra the Great": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/settra-the-great",
        "text": (
            "If your army includes Settra, he must be the army's General and must "
            "be chosen to be the army's Hierophant, even if he does not have the "
            "highest Level of Wizardry in your army. In addition, Settra has a "
            "Command Range of 18\"."
        ),
    },
    "Settra's Champion": {
        "status": "partial",
        "url": "https://tow.whfb.app/special-rules/settras-champion",
        "text": (
            "Nekaph must always issue and accept challenges (if possible). However, "
            "challenges issued by Nekaph cannot be refused. In addition, whilst "
            "engaged in a challenge, Nekaph strikes a Killing Blow if he rolls a "
            "natural 5 or 6 when making a roll To Wound, rather than the usual 6."
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
    "Soul Reaper": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/soul-reaper",
        "text": (
            "After deployment but before the first turn begins, nominate a single "
            "enemy character. This is the soul marked by the Necrosphinx to journey "
            "into the underworld by the battle's end. This model may re-roll any "
            "rolls To Hit of a natural 1 made against the nominated character."
        ),
    },
    "Steadfast Discipline": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/steadfast-discipline",
        "text": (
            "A unit with this special rule can Volley Fire during a turn in which "
            "it moved, or whilst performing a Stand & Shoot charge reaction."
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
    "Stone Shaper": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/stone-shaper",
        "text": (
            "During the Command sub-phase of their turn, if they are not engaged in "
            "combat, this character may nominate a single friendly Necrolith "
            "Colossus, Necrosphinx, unit of Ushabti or unit of Venerable Ushabti "
            "that is within their Command range. Until the end of this turn, the "
            "nominated unit improves the Regeneration value of its Regeneration "
            "save by 1."
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
    "Sworn Protector": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/sworn-protector",
        "text": (
            "Should a Monarch of Nehekhara model suffer a hit whilst within 3\" of "
            "this model, you may choose to transfer that hit and all of its effects "
            "onto this model."
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
    "Unbound Spirits": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/unbound-spirits",
        "text": (
            "If the crew of a Casket of Souls is reduced to zero Wounds, "
            "immediately roll a D6 for every unit (friend or foe) within 12\" of the "
            "model. On a roll of 4+, the unit suffers D6 Strength 3 hits, with no "
            "armour or Regeneration saves permitted (Ward saves can be attempted as "
            "normal). Once these hits are resolved, the Casket of Souls is removed "
            "from play."
        ),
    },
    "Unstoppable Assault": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/unstoppable-assault",
        "text": (
            "During the Combat phase of any turn in which this model charged, every "
            "attack it makes that causes an unsaved wound allows it to immediately "
            "make one additional attack. These additional attacks also benefit from "
            "this special rule. Note that any unsaved wounds caused by the Stomp "
            "Attacks (D3) special rule do not benefit from this special rule."
        ),
    },
    "Usirian's Reaper": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/usirians-reaper",
        "text": (
            "After deployment, nominate a single character in your opponent's "
            "Muster List. Apophas may re-roll any failed rolls To Hit or To Wound "
            "made against that character. In addition, any hits inflicted by "
            "Apophas against the nominated character gain the Magical Attacks "
            "special rule."
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
    "Vortex of Souls": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/vortex-of-souls",
        "text": (
            "A Casket of Souls can cast the following Bound spells, with a Power "
            "Level of 2: Light of Death & Light of Protection Light of Death Light "
            "of Protection"
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
