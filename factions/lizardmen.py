"""Lizardmen.

Profiles from https://tow.whfb.app/army/lizardmen, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Lizardmen"

# Other names that should resolve to this faction.
ALIASES = [
    "Lizardmen",
    "Lizardman",
    "Seraphon",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Oldblood": "Saurus Oldblood",
    "Scar-Veteran": "Saurus Scar-Veteran",
    "Slann": "Slann Mage-Priest",
}

CHARACTERS = {
    "Saurus Oldblood": {
        # https://tow.whfb.app/unit/saurus-oldblood - 140 pts
        "points": 140,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Saurus",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Cold Blooded", "Furious Charge", "Obsidian Blades", "Rallying Cry"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Cavalry Spear", "Great Weapon", "Halberd"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Cold One (Lizardmen)", "Carnosaur"]
        }
    },
    "Saurus Scar-Veteran": {
        # https://tow.whfb.app/unit/saurus-scar-veteran - 90 pts
        "points": 90,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Saurus",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Cold Blooded", "Furious Charge", "Obsidian Blades", "Rallying Cry"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Cavalry Spear", "Great Weapon", "Halberd"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Cold One (Lizardmen)", "Carnosaur"]
        }
    },
    "Skink Chief": {
        # https://tow.whfb.app/unit/skink-chief - 45 pts
        # Shooting is not simulated, so these are left out of the options: Blowpipe,
        # Javelins.
        "points": 45,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 6,
            "Race": "Skink",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Aquatic", "Cold Blooded", "Poisoned Attacks"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Terradon", "Ripperdactyl", "Stegadon"]
        }
    },
    "Skink Priest": {
        # https://tow.whfb.app/unit/skink-priest - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 2,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Skink",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arcane Vassal", "Aquatic", "Cold Blooded", "Lore of Lustria"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "Illusion"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Ancient Stegadon"]
        }
    },
    "Slann Mage-Priest": {
        # https://tow.whfb.app/unit/slann-mage-priest - 285 pts
        "points": 285,
        "base_profile": {
            "Movement": 2,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 5,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Slann",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arcane Shield", "Ward5", "Close Order", "Cold Blooded", "Fly (8)", "Large Target", "Lore of Lustria"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Character",
            "WizardLevel": 4,
            "Lores": ["Battle Magic", "Elementalism", "High Magic", "Illusion", "Necromancy"],
            "OptionalRules": ["Discipline of the Old Ones"],
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
}

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Chameleon Skinks": {
        # https://tow.whfb.app/unit/chameleon-skinks - 11 pts per model, unit size 5+
        # Fights with the Chameleon Skink row.
        # Shooting is not simulated, so these are left out of the options: blowpipes.
        "points": 11,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Patrol Leader', 'Movement': 6, 'WeaponSkill': 2, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 2, 'Initiative': 4, 'Wounds': 1, 'Attacks': 1, 'Leadership': 6},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 2,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 2,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Skink",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Cold Blooded", "Evasive", "Move Through Cover", "Scouts", "Skirmishers"],
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
    "Jungle Swarms": {
        # https://tow.whfb.app/unit/jungle-swarms - 40 pts per model, unit size 3+
        # Fights with the Jungle Swarm row.
        "points": 40,
        "points_per": "model",
        "unit_size": "3+",
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
            "Leadership": 5,
            "Race": "Lizardman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Cold Blooded", "Immune to Psychology", "Loner", "Move Through Cover", "Poisoned Attacks", "Skirmishers", "Unbreakable", "Vanguard"],
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
    "Kroxigor": {
        # https://tow.whfb.app/unit/kroxigor - 49 pts per model, unit size 3+
        # Fights with the Kroxigor row.
        "points": 49,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Ancient', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': 0, 'Strength': 5, 'Toughness': 4, 'Initiative': 3, 'Wounds': 3, 'Attacks': 4, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Lizardman",
            "Armor": "Heavy Armor",
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Aquatic", "Close Order", "Cold Blooded", "Fear", "Skirmish Screen"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Great Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Razordon Pack": {
        # https://tow.whfb.app/unit/razordon-pack - None pts per model, unit size
        # 3+/1+
        # Fights with the Skink Handler row.
        # Also has a profile for Razordon (M6 WS3 BS4 S5 T4 W3 I4 A2 Ld4); not
        # simulated.
        # Troop type by form: Regular Infantry, War Beast; the first is used.
        "points": 5,
        "points_note": "5 points per Skink Handler, 60 points per Razordon",
        "points_per": "model",
        "unit_size": "3+/1+",
        "other_profiles": [
            {'Name': 'Razordon', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 5, 'Toughness': 4, 'Initiative': 4, 'Wounds': 3, 'Attacks': 2, 'Leadership': 4},
        ],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 2,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Lizardman",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Aquatic", "Beast Handlers", "Cold Blooded", "Fear", "Skirmishers"],
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
    "Salamander Pack": {
        # https://tow.whfb.app/unit/salamander-pack - None pts per model, unit size
        # 3+/1+
        # Fights with the Skink Handler row.
        # Also has a profile for Salamander (M6 WS3 BS3 S5 T4 W3 I4 A2 Ld4); not
        # simulated.
        # Troop type by form: Regular Infantry, War Beast; the first is used.
        "points": 5,
        "points_note": "5 points per Skink Handler, 75 points per Salamander",
        "points_per": "model",
        "unit_size": "3+/1+",
        "other_profiles": [
            {'Name': 'Salamander', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 5, 'Toughness': 4, 'Initiative': 4, 'Wounds': 3, 'Attacks': 2, 'Leadership': 4},
        ],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 2,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Lizardman",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Aquatic", "Beast Handlers", "Cold Blooded", "Fear", "Skirmishers"],
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
    "Saurus Warriors": {
        # https://tow.whfb.app/unit/saurus-warriors - 14 pts per model, unit size 10+
        # Fights with the Saurus Warrior row.
        "points": 14,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Spawn Leader', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 0, 'Strength': 4, 'Toughness': 4, 'Initiative': 1, 'Wounds': 1, 'Attacks': 3, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 1,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Saurus",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Cold Blooded", "Obsidian Blades"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Shieldwall"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Thrusting Spear"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Skink Skirmishers": {
        # https://tow.whfb.app/unit/skink-skirmishers - 5 pts per model, unit size 10+
        # Fights with the Skink row.
        # Shooting is not simulated, so these are left out of the options: Blowpipes,
        # Javelins.
        "points": 5,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Patrol Leader', 'Movement': 6, 'WeaponSkill': 2, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 2, 'Initiative': 4, 'Wounds': 1, 'Attacks': 1, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 2,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Skink",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Cold Blooded", "Move Through Cover", "Poisoned Attacks (javelins only)", "Skirmishers"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Scouts", "Vanguard"],
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
    "Temple Guard": {
        # https://tow.whfb.app/unit/temple-guard - 16 pts per model, unit size 10+
        # Fights with the Temple Guard row.
        # Carries a shield, which it cannot use with its Halberd; pass Shield=True
        # with a one-handed weapon.
        "points": 16,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Revered Guardian', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': 0, 'Strength': 4, 'Toughness': 4, 'Initiative': 1, 'Wounds': 1, 'Attacks': 3, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 1,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Saurus",
            "Armor": "Heavy Armor",
            "Weapon": "Halberd",
            "Shield": False,
            "SpecialRules": ["Close Order", "Cold Blooded", "Guardians", "Obsidian Blades", "Shieldwall", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Cold One Riders": {
        # https://tow.whfb.app/unit/cold-one-riders - 34 pts per model, unit size 5+
        # Fights with the Cold One Rider row.
        # Also has a profile for Cold One (M7 WS3 BS- S4 T- W- I2 A2 Ld-); not
        # simulated.
        "points": 34,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Pack Leader', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 0, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 3, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Cold One', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Saurus",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Armour Bane (1, Cold One only)", "Armoured Hide (1)", "Close Order", "Cold Blooded", "Fear", "Obsidian Blades", "Stupidity", "Swiftstride"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Ripperdactyl Riders": {
        # https://tow.whfb.app/unit/ripperdactyl-riders - 40 pts per model, unit size
        # 3+
        # Fights with the Ripperdactyl Rider row.
        # Also has a profile for Ripperdactyl (M2 WS3 BS- S4 T- W- I3 A2 Ld-); not
        # simulated.
        "points": 40,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Ripperdactyl Champion', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 2, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [
            {'Name': 'Ripperdactyl', 'Movement': 2, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Lizardman",
            "Armor": "Light Armor",
            "Weapon": "Cavalry Spear",
            "Shield": True,
            "SpecialRules": ["Armoured Hide (1)", "Cleaving Blow (Ripperdactyl only)", "Cold Blooded", "Fear", "Fly (9)", "Furious Charge (Ripperdactyl only)", "Impetuous", "Skirmishers", "Swiftstride", "Toad Rage"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Terradon Riders": {
        # https://tow.whfb.app/unit/terradon-riders - 32 pts per model, unit size 3+
        # Fights with the Terradon Rider row.
        # Also has a profile for Terradon (M2 WS3 BS- S4 T- W- I2 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: fireleech
        # bolas, javelins.
        "points": 32,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Sky Leader', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 2, 'Attacks': 1, 'Leadership': 5},
        "other_profiles": [
            {'Name': 'Terradon', 'Movement': 2, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Lizardman",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (1)", "Cold Blooded", "Drop Rocks", "Fear", "Fly (10)", "Poisoned Attacks (javelins only)", "Skirmishers", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
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
    "Ancient Stegadon": {
        # https://tow.whfb.app/unit/ancient-stegadon - 230 pts per unit
        # Fights with the Ancient Stegadon row.
        # Also has a profile for Skink Crew (x5) (M- WS2 BS3 S3 T- W- I4 A1 Ld6); not
        # simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: Giant
        # blowpipes, giant bow.
        "points": 230,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Skink Crew (x5)', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': 6},
        ],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": None,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 1,
            "Wounds": 5,
            "Attacks": 3,
            "Leadership": None,
            "Race": "Lizardman",
            "Armor": "Full Plate Armor",
            "Weapon": "Great Horns",
            "Shield": False,
            "SpecialRules": ["Close Order", "Cold Blooded", "Howdah", "Immune to Psychology", "Impact Hits (D3+1)", "Large Target", "Poisoned Attacks (javelins only)", "Stomp Attacks (D3+2)", "Stubborn", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
            "OptionalRules": ["Engine of the Gods"],
        },
        "equipment_options": {
            "weapons": ["Great Horns"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Bastiladon": {
        # https://tow.whfb.app/unit/bastiladon - 160 pts per unit
        # Fights with the Bastiladon row.
        # Also has a profile for Skink Crew (x3) (M- WS2 BS3 S3 T- W- I4 A1 Ld6); not
        # simulated.
        # Armour value 3+ as printed on the site.
        "points": 160,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Skink Crew (x3)', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': 6},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": None,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 1,
            "Wounds": 4,
            "Attacks": 3,
            "Leadership": None,
            "Race": "Lizardman",
            "Armor": "Armour Value 3+",
            "Weapon": "Thunderous Bludgeon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Cold Blooded", "Immune to Psychology", "Impact Hits (D3)", "Impervious Defence", "Large Target", "Poisoned Attacks (javelins only)", "Stomp Attacks (D3+1)", "Stubborn", "Terror"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ark of Sotek", "Solar Engine"],
        },
        "equipment_options": {
            "weapons": ["Thunderous Bludgeon"],
            "armor": ["Armour Value 3+"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Stegadon": {
        # https://tow.whfb.app/unit/stegadon - 215 pts per unit
        # Fights with the Stegadon row.
        # Also has a profile for Skink Crew (x5) (M- WS2 BS3 S3 T- W- I4 A1 Ld6); not
        # simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: giant
        # blowpipes, giant bow.
        "points": 215,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Skink Crew (x5)', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': 6},
        ],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": None,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 2,
            "Wounds": 5,
            "Attacks": 4,
            "Leadership": None,
            "Race": "Lizardman",
            "Armor": "Full Plate Armor",
            "Weapon": "Great Horns",
            "Shield": False,
            "SpecialRules": ["Close Order", "Cold Blooded", "Howdah", "Immune to Psychology", "Impact Hits (D3+1)", "Large Target", "Poisoned Attacks (javelins only)", "Stomp Attacks (D3+2)", "Stubborn", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Great Horns"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Troglodon": {
        # https://tow.whfb.app/unit/troglodon - 200 pts per unit
        # Fights with the Troglodon row.
        # Also has a profile for Skink Oracle (M- WS2 BS3 S3 T- W- I4 A1 Ld8); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: venom
        # spray.
        "points": 200,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Skink Oracle', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': 8},
        ],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 3,
            "BallisticSkill": None,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 5,
            "Attacks": 3,
            "Leadership": None,
            "Race": "Lizardman",
            "Armor": "Heavy Armor",
            "Weapon": "Venomous Talons",
            "Shield": False,
            "SpecialRules": ["Arcane Vassal", "Aquatic", "Close Order", "Cold Blooded", "Immune to Psychology", "Large Target", "Lore of Lustria", "Primeval Roar", "Stomp Attacks (2)", "Stubborn", "Terror"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Illusion"],
        },
        "equipment_options": {
            "weapons": ["Venomous Talons"],
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
    "Aquatic": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/aquatic",
        "text": (
            "Models with this special rule do not suffer any modifiers to their "
            "Movement characteristic when moving through any difficult or dangerous "
            "terrain feature which has been designated a 'water feature'. This "
            "might include shallow streams or fords, swampy ground, fast flowing "
            "rivers, ponds or lakes, and players should agree prior to the game if "
            "any terrain is a water feature."
        ),
    },
    "Arcane Shield": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/arcane-shield",
        "text": (
            "This character has a 5+ Ward save against any wounds suffered."
        ),
    },
    "Arcane Vassal": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/arcane-vassal",
        "text": (
            "Once per turn, unless this model is fleeing or engaged in combat, a "
            "single friendly Slann Mage-Priest that is within 12\" of this model may "
            "'channel' a spell through this model. If they do, the range, targeting "
            "restrictions and all effects of the spell are measured from this "
            "model, rather than from the caster. If the spell requires a line of "
            "sight, it is determined from this model. Note that spells with a range "
            "of Self cannot be channelled in this way."
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
    "Beast Handlers": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/beast-handlers",
        "text": (
            "When an enemy unit shoots at a Salamander or Razordon Pack that "
            "contains one or more Skink Handlers, the enemy player must roll a D6 "
            "for each successful roll To Hit before making any rolls To Wound. On a "
            "roll of 1-4, the hit is inflicted upon a Salamander or Razordon. On a "
            "roll of 5+, the hit is inflicted upon a Skink Handler. In combat, "
            "enemy models must allocate their attacks against a model they are in "
            "base contact with (or against the closest model if they are within the "
            "fighting rank but not in base contact) before rolling To Hit."
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
    "Cold Blooded": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/cold-blooded",
        "text": (
            "When required to make a Fear, Panic or Terror test, models with this "
            "special rule may roll an extra D6 and discard the highest result."
        ),
    },
    "Drop Rocks": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/drop-rocks",
        "text": (
            "Once per game, a unit with this special rule may perform a 'Drop "
            "Rocks' attack against a single enemy unit that is not engaged in "
            "combat. To do so, this unit must move (by flying) over the unit it "
            "wishes to attack during the Remaining Moves sub-phase. Once this "
            "unit's movement is complete, the enemy unit suffers D3 Strength 4 "
            "hits, each with an AP of -, for each model in this unit that moved "
            "over it."
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
    "Furious Charge": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/furious-charge",
        "text": (
            "During a turn in which it made a charge move of 3\" or more, a model "
            "with this special rule gains a +1 modifier to its Attacks "
            "characteristic."
        ),
    },
    "Guardians": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/guardians",
        "text": (
            "Should a friendly Slann Mage-Priest model that is within 3\" of this "
            "unit suffer a hit during the Shooting phase, roll a D6. On a roll of "
            "2+, you may choose to transfer that hit and all of its effects onto "
            "this unit. In addition, any model in a unit of Temple Guard that is "
            "within the Command range of a Slann Mage-Priest can issue and accept "
            "challenges in the same manner as a character."
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
    "Impervious Defence": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/impervious-defence",
        "text": (
            "Enemy units cannot claim any bonus combat result points for being "
            "engaged with this model's flank or rear arc."
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
    "Lore of Lustria": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-lustria",
        "text": (
            "The Slann Mage-Priests are masters of magic able to wield tremendous "
            "power with almost contemptuous ease. With this power they are able to "
            "alter the environment around them and the fates of their loyal "
            "servants, summoning rains to wash away their foes, or calling upon the "
            "Winds of Magic to heal their champions. A Wizard with the 'Lore of "
            "Lustria' special rule may discard one of their randomly generated "
            "spells as normal. When they do so, they may select instead either the "
            "signature spell of their chosen Lore of Magic, or one of the spells "
            "listed below. Lore of Lustria Lore"
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
    "Obsidian Blades": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/obsidian-blades",
        "text": (
            "A hand weapon carried by a model with this special rule has an Armour "
            "Piercing characteristic of -1. Note that this special rule only "
            "applies to a single, non-magical hand weapon and does not apply to a "
            "model's mount (should it have one). If the model is using two hand "
            "weapons or any other sort of weapon, this special rule ceases to "
            "apply."
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
    "Primeval Roar": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/primeval-roar",
        "text": (
            "Once per game, during the Command sub-phase of their turn, this model "
            "may attempt to unleash the primeval savagery of the Lizardmen by "
            "making a Leadership test (using its own Leadership). If this test is "
            "passed, until the end of that turn all friendly Lizardmen units within "
            "7\" of this model gain the Furious Charge special rule."
        ),
    },
    "Rallying Cry": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/rallying-cry",
        "text": (
            "During the Command sub-phase of their turn, if they are not engaged in "
            "combat, this character may nominate a single fleeing friendly unit "
            "that is within their Command range. The nominated unit immediately "
            "makes a Rally test. If this test is failed, the unit may attempt to "
            "rally again as normal during the Rally sub-phase."
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
    "Skirmish Screen": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/skirmish-screen",
        "text": (
            "A unit with this special rule can draw a line of sight over or through "
            "friendly units of Skink Skirmishers and can move through friendly "
            "units of Skink Skirmishers that are in Skirmish formation. If this "
            "unit's move would result in it ending up 'on top' of a friendly Skink "
            "Skirmisher, simply nudge that model aside, by the smallest amount "
            "possible, to make space for this unit. Whilst in Skirmish formation "
            "units of Skink Skirmishers can treat friendly models with this special "
            "rule that are within 1\" of one or more of the unit's models as a part "
            "of the unit for the purposes of unit coherency."
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
    "Toad Rage": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/toad-rage",
        "text": (
            "Before the game starts, but after Scouts have been deployed, you may "
            "place one Lustrian blot toad marker for each unit of Ripperdactyl "
            "Riders in your army (counting only units, not including characters "
            "mounted on Ripperdactyls). A single blot toad marker can be placed on "
            "any enemy unit on the battlefield, this marker remains throughout the "
            "battle. When engaged in combat with an enemy unit with a blot toad "
            "marker, Ripperdactyls (but not their riders) gain the Extra Attacks "
            "(+1) special rule, and may re-roll any roll To Hit of a natural 1."
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
}

PROFILES = dict(CHARACTERS, **UNITS)
