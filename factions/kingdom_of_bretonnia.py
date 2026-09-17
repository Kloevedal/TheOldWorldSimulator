"""Kingdom of Bretonnia.

Profiles from https://tow.whfb.app/army/kingdom-of-bretonnia, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Kingdom of Bretonnia"

# Other names that should resolve to this faction.
ALIASES = [
    "Bretonnia",
    "Bretonnians",
    "Kingdom of Bretonnia",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Elisse": "Lady Élisse Duchaard",
    "Lady Elisse Duchaard": "Lady Élisse Duchaard",
    "Cecil Gastonne": "Sir Cecil Gastonne",
    "Green Knight": "The Green Knight",
}

CHARACTERS = {
    "Lady Élisse Duchaard": {
        # https://tow.whfb.app/unit/lady-elisse-duchaard - 225 pts
        # Also has a profile for Ariandir (M10 WS4 BS- S4 T- W- I5 A2 Ld-); not
        # simulated.
        # Armour Bane (2) is Ariandir's; Armoured Hide (1) improves her unarmoured 7+
        # to a 6+ save.
        "points": 225,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 5,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Bretonnian",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arcane Backlash", "Armour Bane (2, Ariandir only)", "Armoured Hide (1)", "Aura of the Lady", "Beguiling Aura", "Blessings of the Lady", "Counter Charge", "Lore of the Lady", "Magical Attacks", "Magic Resistance (-2)", "Shield of the Lady", "Stomp Attacks (1)", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "NamedCharacter",
            "WizardLevel": 3,
            "Lores": ["Elementalism"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": ["Chalice of Brionne", "The Staff of the Elements"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Sir Cecil Gastonne": {
        # https://tow.whfb.app/unit/sir-cecil-gastonne - 165 pts
        "points": 165,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 7,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "Sorrow's End",
            "Shield": True,
            "SpecialRules": ["Blessings of the Lady", "Rallying Cry", "The Wyrm Slayer", "The Exile's Vow"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Sorrow's End"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": ["Sorrow's End", "Dragonhide Cloak"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "The Green Knight": {
        # https://tow.whfb.app/unit/the-green-knight - 275 pts
        # Also has a profile for The Shadow Steed (M8 WS4 BS- S4 T- W- I4 A1 Ld-); not
        # simulated.
        "points": 275,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 7,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 6,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "The Dolorous Blade",
            "Shield": True,
            "SpecialRules": ["Aura of the Fay", "Blessed Knight", "Ward5", "Ethereal", "Guardian of the Sacred Sites", "Immune to Psychology", "Loner", "Move Through Cover", "Rallying Cry", "Terror", "Unbreakable", "Unstable"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["The Dolorous Blade"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": ["The Dolorous Blade"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Baron": {
        # https://tow.whfb.app/unit/baron - 100 pts
        "points": 100,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blessings of the Lady", "Rallying Cry", "The Knight's Vow"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["The Questing Vow", "The Grail Vow", "Knightly Virtue"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Morning Star", "Great Weapon", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Bretonnian Warhorse", "Barded Pegasus", "Royal Pegasus", "Hippogryph"]
        }
    },
    "Damsel": {
        # https://tow.whfb.app/unit/damsel - 60 pts
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
            "Race": "Bretonnian",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Aura of the Lady", "Blessings of the Lady", "Lore of the Lady", "Magical Attacks", "Magic Resistance (-2)", "Shield of the Lady"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "Illusion"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Bretonnian Warhorse", "Warhorse (Bretonnia)", "Unicorn"]
        }
    },
    "Duke": {
        # https://tow.whfb.app/unit/duke - 175 pts
        "points": 175,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 7,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 4,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blessings of the Lady", "Rallying Cry", "The Grail Vow"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Knightly Virtue"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Morning Star", "Great Weapon", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Bretonnian Warhorse", "Barded Pegasus", "Royal Pegasus", "Hippogryph"]
        }
    },
    "Outcast Wizard": {
        # https://tow.whfb.app/unit/outcast-wizard - 45 pts
        "points": 45,
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
            "Race": "Bretonnian",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Magical Attacks", "Magic Resistance (-1)", "Untutored Arcanist"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Elementalism", "Illusion", "Necromancy"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Warhorse (Bretonnia)"]
        }
    },
    "Paladin": {
        # https://tow.whfb.app/unit/paladin - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blessings of the Lady", "Rallying Cry", "The Knight's Vow"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["The Questing Vow", "The Grail Vow", "Knightly Virtue"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Morning Star", "Great Weapon", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Bretonnian Warhorse", "Barded Pegasus", "Royal Pegasus"]
        }
    },
    "Prophetess": {
        # https://tow.whfb.app/unit/prophetess - 135 pts
        "points": 135,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Bretonnian",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Aura of the Lady", "Blessings of the Lady", "Lore of the Lady", "Magical Attacks", "Magic Resistance (-2)", "Shield of the Lady"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Elementalism", "Illusion"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Bretonnian Warhorse", "Warhorse (Bretonnia)", "Royal Pegasus", "Unicorn"]
        }
    },
    "Sergeant-at-Arms": {
        # https://tow.whfb.app/unit/sergeant-at-arms - 45 pts
        "points": 45,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Bretonnian",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Levies", "Peasant's Duty", "Peasantry", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Warhorse (Bretonnia)"]
        }
    },
}

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Battle Pilgrims": {
        # https://tow.whfb.app/unit/battle-pilgrims - 6 pts per model, unit size 5-30
        # Battle Pilgrims/0-1 Grail Reliquae
        # Fights with the Battle Pilgrim row.
        # Also has a profile for Grail Reliquae (M4 WS2 BS2 S3 T3 W6 I3 A6 Ld8); not
        # simulated.
        "points": 6,
        "points_per": "model",
        "unit_size": "5-30 Battle Pilgrims/0-1 Grail Reliquae",
        "other_profiles": [
            {'Name': 'Grail Reliquae', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 6, 'Attacks': 6, 'Leadership': 8},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Bretonnian",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Blessings of the Lady (Grail Reliquae)", "Close Order", "Grail Reliquae", "Hatred (all enemies)", "Levies", "Peasantry", "Retinue of the Saints (Grail Reliquae)", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Grail Reliquae"],
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
    "Border Princes Brigands": {
        # https://tow.whfb.app/unit/border-princes-brigands - 4 pts per model, unit
        # size 10+
        # Fights with the Brigand row.
        # Shooting is not simulated, so these are left out of the options:
        # Blunderbuss, Crossbow, Pistol.
        "points": 4,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Desperado', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Leadership": 6,
            "Race": "Bretonnian",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Horde", "Impetuous", "Levies", "Motley Crew", "Open Order", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Open Order", "Close Order", "Skirmishers", "Ambushers", "Scouts"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Knights of the Realm on Foot": {
        # https://tow.whfb.app/unit/knights-of-the-realm-on-foot - 11 pts per model,
        # unit size 5+
        # Fights with the Knight of the Realm row.
        "points": 11,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'First Knight', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Blessings of the Lady", "Close Order", "Furious Charge", "The Knight's Vow"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
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
    "Men-at-Arms": {
        # https://tow.whfb.app/unit/men-at-arms - 4 pts per model, unit size 10+
        # Fights with the Man-at-Arms row.
        # Also has a profile for Grail Monk (M4 WS2 BS2 S3 T3 W1 I2 A2 Ld6); not
        # simulated.
        "points": 4,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Yeoman', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [
            {'Name': 'Grail Monk', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Bretonnian",
            "Armor": "Light Armor",
            "Weapon": "Polearm Single-Handed",
            "Shield": True,
            "SpecialRules": ["Close Order", "Horde", "Levies", "Peasantry", "Shieldwall", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Grail Monk", "Blessed Triptych"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Polearm Single-Handed"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Peasant Bowmen": {
        # https://tow.whfb.app/unit/peasant-bowmen - 5 pts per model, unit size 10+
        # Fights with the Peasant Bowman row.
        # Shooting is not simulated, so these are left out of the options: longbows.
        "points": 5,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Villein', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Bretonnian",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Levies", "Peasantry"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["defensive stakes", "burning braziers", "Close Order"],
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
    "Squires": {
        # https://tow.whfb.app/unit/squires - 7 pts per model, unit size 5+
        # Fights with the Squire row.
        # Shooting is not simulated, so these are left out of the options: longbows.
        "points": 7,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Esquire', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Bretonnian",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Move Through Cover", "Open Order", "Peasantry", "Skirmishers", "Vanguard"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Fire & Flee", "Scouts"],
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
    "Yeomen Guard": {
        # https://tow.whfb.app/unit/yeomen-guard - 5 pts per model, unit size 10+
        # Fights with the Yeoman Guard row.
        # Also has a profile for Grail Monk (M4 WS3 BS2 S3 T3 W1 I2 A2 Ld6); not
        # simulated.
        "points": 5,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Warden', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [
            {'Name': 'Grail Monk', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Bretonnian",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Horde", "Peasantry", "Shieldwall", "Veteran", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Grail Monk", "Blessed Triptych"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd", "Polearm Single-Handed", "Thrusting Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Grail Knights": {
        # https://tow.whfb.app/unit/grail-knights - 38 pts per model, unit size 3+
        # Fights with the Grail Knight row.
        # Also has a profile for Bretonnian Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-);
        # not simulated.
        "points": 38,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Grail Guardian', 'Movement': None, 'WeaponSkill': 6, 'BallisticSkill': 2, 'Strength': 4, 'Toughness': 4, 'Initiative': 5, 'Wounds': 1, 'Attacks': 3, 'Leadership': 9},
        "other_profiles": [
            {'Name': 'Bretonnian Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 6,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "Lance",
            "Shield": True,
            "SpecialRules": ["Blessings of the Lady", "Close Order", "Counter Charge", "Finest Warhorses", "First Charge", "Lance Formation", "Living Saints", "Swiftstride", "The Grail Vow"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Knightly Virtue"],
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
    "Knights Errant": {
        # https://tow.whfb.app/unit/knights-errant - 19 pts per model, unit size 3+
        # Fights with the Knight Errant row.
        # Also has a profile for Bretonnian Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-);
        # not simulated.
        "points": 19,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Gallant', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Bretonnian Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "Lance",
            "Shield": True,
            "SpecialRules": ["Blessings of the Lady", "Close Order", "Finest Warhorses", "First Charge", "Impetuous", "Lance Formation", "Swiftstride", "The Knight's Vow"],
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
    "Mounted Knights of the Realm": {
        # https://tow.whfb.app/unit/mounted-knights-of-the-realm - 24 pts per model,
        # unit size 3+
        # Fights with the Knight of the Realm row.
        # Also has a profile for Bretonnian Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-);
        # not simulated.
        "points": 24,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'First Knight', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Bretonnian Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "Lance",
            "Shield": True,
            "SpecialRules": ["Blessings of the Lady", "Close Order", "Counter Charge", "Finest Warhorses", "First Charge", "Lance Formation", "Swiftstride", "The Knight's Vow"],
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
    "Mounted Yeomen": {
        # https://tow.whfb.app/unit/mounted-yeomen - 13 pts per model, unit size 5+
        # Fights with the Mounted Yeoman row.
        # Also has a profile for Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: shortbows.
        "points": 13,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Warden', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [
            {'Name': 'Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
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
            "Race": "Bretonnian",
            "Armor": None,
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Fast Cavalry", "Fire & Flee", "Levies", "Open Order", "Peasantry", "Reserve Move", "Skirmishers", "Swiftstride"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Feigned Flight"],
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
    "Pegasus Knights": {
        # https://tow.whfb.app/unit/pegasus-knights - 59 pts per model, unit size 3+
        # Fights with the Pegasus Knight row.
        # Also has a profile for Barded Pegasus (M7 WS3 BS- S4 T- W- I4 A2 Ld-); not
        # simulated.
        "points": 59,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'First Knight', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 2, 'Strength': 4, 'Toughness': 4, 'Initiative': 3, 'Wounds': 2, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Barded Pegasus', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "Lance",
            "Shield": True,
            "SpecialRules": ["Blessings of the Lady", "Counter Charge", "Dispersed Formation", "First Charge", "Fly (10)", "Furious Charge (Riders only)", "Skirmishers", "Swiftstride", "The Knight's Vow"],
            "TroopType": "MonstrousCavalry",
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
    "Questing Knights": {
        # https://tow.whfb.app/unit/questing-knights - 26 pts per model, unit size 3+
        # Fights with the Questing Knight row.
        # Also has a profile for Bretonnian Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-);
        # not simulated.
        # Carries a shield, which it cannot use with its Great Weapon; pass
        # Shield=True with a one-handed weapon.
        "points": 26,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Paragon', 'Movement': None, 'WeaponSkill': 5, 'BallisticSkill': 2, 'Strength': 4, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Bretonnian Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Bretonnian",
            "Armor": "Heavy Armor",
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Blessings of the Lady", "Close Order", "Finest Warhorses", "First Charge", "Lance Formation", "Swiftstride", "The Questing Vow"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Knightly Virtue"],
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
    "Border Princes Bombard": {
        # https://tow.whfb.app/unit/border-princes-bombard - 100 pts per unit
        # Fights with the Crew row.
        # Also has a profile for Bombard (M- WS- BS- S- T7 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Bombard.
        "points": 100,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Bombard', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 7, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Bretonnian",
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
    "Field Trebuchet": {
        # https://tow.whfb.app/unit/field-trebuchet - 100 pts per unit
        # Fights with the Peasant Crew row.
        # Also has a profile for Field Trebuchet (M- WS- BS- S- T7 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Field
        # trebuchet.
        "points": 100,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Field Trebuchet', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 7, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 6,
            "Race": "Bretonnian",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Levies", "Peasantry", "Skirmishers"],
            "TroopType": "WarMachine",
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
}


# Special rules carried by this faction's characters and units. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {
    "Arcane Backlash": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/arcane-backlash",
        "text": (
            "Lady Élisse may apply a +1 modifier to any of her Dispel rolls. In "
            "addition, should she roll any natural double when making a Dispel roll "
            "(not including rolls of a natural double 1), the spell is unbound and "
            "the casting Wizard immediately loses a single Wound."
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
    "Aura of the Fay": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/aura-of-the-fay",
        "text": (
            "When the Green Knight loses his last Wound, he is removed from play as "
            "usual, but is not slain. His controlling player may attempt to awaken "
            "him again during any of their Start of Turn sub-phases in which he is "
            "not on the battlefield, using the Guardian of the Sacred Sites special "
            "rule. However, each time the Green Knight is slain, he is weakened, "
            "and suffers a -1 modifier to the dice roll when attempting to awaken "
            "him, and a -1 modifier to his Wounds characteristic (to a minimum of "
            "1). Note that the enemy player only wins Victory Points for destroying "
            "the Green Knight the first time he loses his last Wound and is removed "
            "from play."
        ),
    },
    "Aura of the Lady": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/aura-of-the-lady",
        "text": (
            "Any unit this character has joined gains the Magical Attacks special "
            "rule."
        ),
    },
    "Beguiling Aura": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/beguiling-aura",
        "text": (
            "Enemy models must make a Leadership test before making any rolls To "
            "Hit against this model during the Combat phase. If this test is "
            "failed, only rolls of a natural 6 will hit."
        ),
    },
    "Blessed Knight": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/blessed-knight",
        "text": (
            "The Green Knight has a 5+ Ward save against any wounds suffered."
        ),
    },
    "Blessings of the Lady": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/blessings-of-the-lady",
        "text": (
            "Once deployment is complete, instead of rolling off to determine which "
            "player takes the first turn, the Kingdom of Bretonnia army may kneel "
            "and pray for the Blessings of the Lady. If it does so, the opposing "
            "player counts as having won the roll-off and the Lady's Blessing is "
            "granted, giving all models in the Kingdom of Bretonnia army with this "
            "special rule: - A 6+ Ward save against any wounds suffered. - A 5+ "
            "Ward save against any wounds suffered that were caused by an attack "
            "with a Strength of 5 or higher. Note that if there is no roll-off to "
            "determine which player takes the first turn, the Kingdom of Bretonnia "
            "army cannot kneel and pray for the Blessing. Note also that, should "
            "two Kingdom [...]"
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
    "Dispersed Formation": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dispersed-formation",
        "text": (
            "To maintain Skirmish formation, every model in this unit must be "
            "within 3\" of another model belonging to the same unit, rather than the "
            "usual 1\". However, unlike most Skirmishers, models with this special "
            "rule do not have a 360° vision arc; they instead have a 90° vision "
            "arc, corresponding to their front arc."
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
    "Fast Cavalry": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fast-cavalry",
        "text": (
            "If all of the models (including characters) within a unit arrayed in "
            "an Open Order formation have this special rule, the unit may perform "
            "its Quick Turn even if it marched."
        ),
    },
    "Finest Warhorses": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/finest-warhorses",
        "text": (
            "When a unit with this special rule makes a Charge, Flee or Pursuit "
            "roll, it may re-roll any dice that roll a natural 1, before discarding "
            "any dice that are required to be discarded."
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
    "Grail Reliquae": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/grail-reliquae",
        "text": (
            "The Grail Reliquae is placed in the centre of the front rank of its "
            "unit (or as close to the centre as possible) and occupies the space "
            "of, and counts as, six models; two in the front rank, two in the "
            "second and two in the third. If the unit turns or reforms, the Grail "
            "Reliquae must be repositioned into the new front rank. Casualties are "
            "removed from the unit as normal, but the Grail Reliquae cannot lose "
            "any Wounds whilst any Battle Pilgrims remain. Only once all of the "
            "Battle Pilgrims have been removed from the unit can the Grail Reliquae "
            "itself lose Wounds. The Grail Reliquae counts as both a standard "
            "bearer and a musician for its unit. Whilst the Grail Reliquae model "
            "itself is within 12\" [...]"
        ),
    },
    "Guardian of the Sacred Sites": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/guardian-of-the-sacred-sites",
        "text": (
            "The Green Knight is not placed on the battlefield during deployment – "
            "he slumbers until he is awakened during the game. During any of your "
            "Start of Turn sub-phases in which the Green Knight is not on the "
            "battlefield (even if he was removed from play as a casualty during a "
            "previous turn), you may attempt to awaken him by rolling a D6. On a "
            "roll of 1-2, he continues to slumber until your next turn at least. On "
            "a roll of 3+, the Green Knight awakens. If the Green Knight has not "
            "yet been awakened by the start of round five, he awakens "
            "automatically. During the Compulsory Moves sub-phase of the turn in "
            "which he was awakened, the Green Knight may be placed completely "
            "within any 'natural' terrain [...]"
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
    "Lance Formation": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/lance-formation",
        "text": (
            "A unit consisting of models with this special rule may adopt a Lance "
            "formation."
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
    "Living Saints": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/living-saints",
        "text": (
            "Every model in a unit of Grail Knights can issue and accept challenges "
            "in the same manner as a character."
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
    "Lore of the Lady": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-the-lady",
        "text": (
            "The magical powers of the Handmaidens of the Lady all resemble "
            "religious observance as much as they do sorcery. With hands clasped in "
            "devotion and rapturous joy upon her brow, a Damsel or Prophetess "
            "beseeches her goddess to protect and empower her dutiful followers. A "
            "Wizard with the 'Lore of the Lady' special rule may discard one of "
            "their randomly generated spells as normal. When they do so, they may "
            "select instead either the signature spell of their chosen Lore of "
            "Magic, or one of the spells listed below. Lore of the Lady Lore"
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
    "Peasant's Duty": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/peasants-duty",
        "text": (
            "This character and any unit they have joined may choose to Give Ground "
            "rather than Fall Back in Good Order, and does not have to make a Panic "
            "test when a friendly unit of Levies Breaks and flees from combat "
            "whilst within 6\" of it. Additionally, unless this character is "
            "fleeing, any friendly unit that is within their Command range and has "
            "the Levies special rule may re-roll a failed Panic test."
        ),
    },
    "Peasantry": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/peasantry",
        "text": (
            "If a unit with this special rule is within 6\" of a friendly model that "
            "has the Knight's Vow, the Questing Vow or the Grail Vow, and if that "
            "model is not fleeing, this unit can use that model's Leadership "
            "characteristic instead of its own. In addition, a standard carried by "
            "a unit with this special rule cannot be counted as a trophy of war. A "
            "character with this special rule can only join a unit that also has "
            "this special rule."
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
    "Retinue of the Saints": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/retinue-of-the-saints",
        "text": (
            "Your army may include up to one Grail Reliquae for every character or "
            "unit with the Grail Vow it includes."
        ),
    },
    "Shield of the Lady": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/shield-of-the-lady",
        "text": (
            "If this character has joined a unit that has a Unit Strength of 10 or "
            "more, and that has a Chivalrous Vow, they may voluntarily 'retire' to "
            "the rear of the unit at any time, moving through the ranks and taking "
            "up a position away from the combat. Should they do so, they are no "
            "longer within the fighting rank and cannot make any attacks or have "
            "attacks directed against them. However, they continue to confer "
            "benefits to the unit in the form of Leadership and special rules, and "
            "may cast spells as if they were within the fighting rank."
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
    "The Exile's Vow": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/the-exiles-vow",
        "text": (
            "The Exile's Vow is a Chivalrous Vow. A model with this Chivalrous Vow "
            "has the Stubborn and Veteran special rules. In addition, a model with "
            "this Chivalrous Vow does not have to make a Panic test when a friendly "
            "unit with either the Levies or Peasantry special rule is destroyed "
            "whilst within 6\" of it, or when it is fled through by a friendly unit "
            "with either the Levies or Peasantry special rule."
        ),
    },
    "The Grail Vow": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/the-grail-vow",
        "text": (
            "A model with this Chivalrous Vow has the Immune to Psychology, Magical "
            "Attacks and Stubborn special rules. In addition, models with this "
            "Chivalrous Vow always benefit from the Blessings of the Lady special "
            "rule and do not have to pray at the start of the game. However, a "
            "model with this Chivalrous Vow cannot refuse a challenge. A unit with "
            "this Chivalrous Vow can only be joined by a character that also has "
            "this Chivalrous Vow or by a Handmaiden of the Lady. A character with "
            "this Vow cannot join a unit with the Peasantry special rule."
        ),
    },
    "The Knight's Vow": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/the-knights-vow",
        "text": (
            "A model with this Chivalrous Vow does not have to make a Panic test "
            "when a friendly unit with the Peasantry special rule is destroyed "
            "whilst within 6\" of it, or when it is fled through by a friendly unit "
            "with the Peasantry special rule. A unit with this Chivalrous Vow "
            "cannot be joined by a character that has the Peasantry special rule. A "
            "character with this Chivalrous Vow cannot join a unit with the "
            "Peasantry special rule."
        ),
    },
    "The Questing Vow": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/the-questing-vow",
        "text": (
            "A model with this Chivalrous Vow has the Stubborn special rule and can "
            "re-roll any failed Fear, Panic or Terror test. In addition, a model "
            "with this Chivalrous Vow does not have to make a Panic test when a "
            "friendly unit with the Peasantry special rule is destroyed whilst "
            "within 6\" of it, or when it is fled through by a friendly unit with "
            "the Peasantry special rule. However, a model with this Chivalrous Vow "
            "cannot be equipped with a lance (be it magical or mundane). A unit "
            "with this Chivalrous Vow cannot be joined by a character that has the "
            "Knight's Vow or the Peasantry special rule. A character with this "
            "Chivalrous Vow cannot join a unit with the Peasantry special rule."
        ),
    },
    "The Wyrm Slayer": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/the-wyrm-slayer",
        "text": (
            "Should Sir Cecil Gastonne kill an enemy model whose troop type is "
            "monstrous infantry, monstrous cavalry, monstrous creature or behemoth "
            "during any Combat phase, he gains the Terror special rule for the "
            "remainder of the game."
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
    "Untutored Arcanist": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/untutored-arcanist",
        "text": (
            "When required to roll on the Miscast table, a Wizard with this special "
            "rule must roll an extra D6 and discard the highest result."
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
}

PROFILES = dict(CHARACTERS, **UNITS)
