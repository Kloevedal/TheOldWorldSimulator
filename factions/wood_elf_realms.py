"""Wood Elf Realms.

Profiles from https://tow.whfb.app/army/wood-elf-realms, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Wood Elf Realms"

# Other names that should resolve to this faction.
ALIASES = [
    "Wood Elves",
    "Wood Elf",
    "Asrai",
    "Wood Elf Realms",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Araloth": "Araloth, Lord of Talsyn",
    "Orion": "Orion, the King in the Woods",
}

CHARACTERS = {
    "Araloth, Lord of Talsyn": {
        # https://tow.whfb.app/unit/araloth-lord-of-talsyn - 150 pts
        "points": 150,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 8,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 8,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Wood Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Spear of Talsyn",
            "Shield": True,
            "SpecialRules": ["Boldest of the Bold", "Evasive", "Favour of the Goddess", "Ward5", "Move Through Cover", "Rallying Cry", "Skaryn the Eye Thief", "Strike First", "Stubborn"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Spear of Talsyn"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": ["Spear of Talsyn"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Orion, the King in the Woods": {
        # https://tow.whfb.app/unit/orion-the-king-in-the-woods - 405 pts
        "points": 405,
        "points_note": "405 points",
        "base_profile": {
            "Movement": 9,
            "WeaponSkill": 8,
            "BallisticSkill": 6,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 8,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 10,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "The Spear of Kurnous",
            "Shield": False,
            "SpecialRules": ["Frenzy", "Immune to Psychology", "Magic Resistance (-2)", "Move Through Cover", "Open Order*", "Stomp Attacks (D3+2)", "Strike First", "Terror", "Unbreakable"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["The Spear of Kurnous"],
            "armor": [],
            "shield": False,
            "items": ["Cloak of Isha", "Hawk's Talon", "Horn of the Wild Hunt", "The Spear of Kurnous"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Branchwraith": {
        # https://tow.whfb.app/unit/branchwraith - 80 pts
        "points": 80,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 6,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 6,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Forest Spirit",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Fear", "Flammable", "Furious Charge", "Immune to Psychology", "Lore of Athel Loren", "Magical Attacks", "Move Through Cover", "Regeneration (6+)", "Tree Spirit"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "Illusion"],
            "OptionalRules": ["Forest Spites"],
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
    "Glade Captain": {
        # https://tow.whfb.app/unit/glade-captain - 70 pts
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbow.
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
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["The Arrow of Kurnous", "Evasive", "Fire & Flee", "Ignores Cover", "Move Through Cover", "Rallying Cry", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows", "Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Great Stag", "Warhawk", "Great Eagle"]
        }
    },
    "Glade Lord": {
        # https://tow.whfb.app/unit/glade-lord - 135 pts
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbow.
        "points": 135,
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
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["The Arrow of Kurnous", "Evasive", "Fire & Flee", "Ignores Cover", "Move Through Cover", "Rallying Cry", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows", "Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Great Stag", "Warhawk", "Forest Dragon", "Great Eagle"]
        }
    },
    "Shadowdancer": {
        # https://tow.whfb.app/unit/shadowdancer - 85 pts
        "points": 85,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 8,
            "BallisticSkill": 6,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 7,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Evasive", "Furious Charge", "Immune to Psychology", "Loner", "Move Through Cover", "Strike First", "Talismanic Tattoos", "Ward6", "Troubadour of Loec"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 0,
            "Lores": ["Battle Magic", "Illusion"],
            "OptionalRules": ["Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Spear of Loec", "Trickster's Blades"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Spellsinger": {
        # https://tow.whfb.app/unit/spellsinger - 80 pts
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
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Lore of Athel Loren", "Magical Attacks", "Move Through Cover"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "High Magic", "Illusion"],
            "OptionalRules": ["Talismanic Tattoos", "Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Unicorn", "Warhawk", "Great Eagle"]
        }
    },
    "Spellweaver": {
        # https://tow.whfb.app/unit/spellweaver - 155 pts
        "points": 155,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Lore of Athel Loren", "Magical Attacks", "Move Through Cover"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Elementalism", "High Magic", "Illusion"],
            "OptionalRules": ["Talismanic Tattoos", "Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Unicorn", "Warhawk", "Great Eagle"]
        }
    },
    "Treeman Ancient": {
        # https://tow.whfb.app/unit/treemen-ancient - 265 pts
        # Shooting is not simulated, so these are left out of the options:
        # Strangleroots.
        "points": 265,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 5,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 2,
            "Wounds": 6,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Forest Spirit",
            "Armor": "Full Plate Armor",
            "Weapon": "Oaken Fists",
            "Shield": False,
            "SpecialRules": ["Close Order", "Flammable", "Immune to Psychology", "Large Target", "Lore of Athel Loren", "Magical Attacks", "Move Through Cover", "Regeneration (5+)", "Stomp Attacks (D3)", "Stubborn", "Terror", "Timmm-berrr!", "Tree Spirit", "Tree Whack"],
            "TroopType": "Behemoth",
            "UnitCategory": "Character",
            "WizardLevel": 2,
            "Lores": ["Battle Magic", "Elementalism"],
            "OptionalRules": ["Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Oaken Fists"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Warden of Talsyn": {
        # https://tow.whfb.app/unit/warden-of-talsyn - 125 pts
        "points": 125,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 7,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Courage Beyond Compare", "Drilled", "Elven Reflexes", "Immune to Psychology", "Move Through Cover", "Parry", "Strike First", "Stubborn"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Asrai Spear", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Waystalker": {
        # https://tow.whfb.app/unit/waystalker - 85 pts
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbow.
        "points": 85,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Evasive", "Feigned Flight", "Fire & Flee", "Hawk-eyed Archer", "Ignores Cover", "Move Through Cover", "Scouts"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows", "Forest Spites", "Ambushers"],
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
}

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Bear of Loren": {
        # https://tow.whfb.app/unit/bear-of-loren - 20 pts per model
        # The site gives no unit size.
        # Fights with the Bear of Loren row.
        "points": 20,
        "points_per": "model",
        "unit_size": "not given",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": None,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 6,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (1)", "Cleaving Blow", "Fear", "Motley Crew", "Run with the Pack", "Skirmishers"],
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
    "Beast Keeper": {
        # https://tow.whfb.app/unit/beast-keeper - 11 pts per model
        # The site gives no unit size.
        # Fights with the Beast Keeper row.
        "points": 11,
        "points_per": "model",
        "unit_size": "not given",
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
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Motley Crew", "Move Through Cover", "Run with the Pack", "Skirmishers"],
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
    "Deepwood Hound": {
        # https://tow.whfb.app/unit/deepwood-hound - 8 pts per model, unit size 1-3
        # Fights with the Deepwood Hound row.
        "points": 8,
        "points_per": "model",
        "unit_size": "1-3",
        "other_profiles": [],
        "base_profile": {
            "Movement": 9,
            "WeaponSkill": 4,
            "BallisticSkill": None,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Motley Crew", "Run with the Pack", "Skirmishers", "Warband"],
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
    "Deepwood Scouts": {
        # https://tow.whfb.app/unit/deepwood-scouts - 13 pts per model, unit size 5+
        # Fights with the Deepwood Scout row.
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbows.
        "points": 13,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': "Lord's Bowman", 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
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
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Evasive", "Fire & Flee", "Move Through Cover", "Open Order", "Scouts", "Skirmishers"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows"],
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
    "Dryads": {
        # https://tow.whfb.app/unit/dryads - 13 pts per model, unit size 5+
        # Fights with the Dryad row.
        "points": 13,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Nymph', 'Movement': 6, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 4, 'Initiative': 4, 'Wounds': 1, 'Attacks': 3, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Forest Spirit",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Fear", "Flammable", "Furious Charge", "Immune to Psychology", "Magical Attacks", "Move Through Cover", "Open Order", "Regeneration (6+)", "Skirmishers", "Stubborn", "Tree Spirit"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Forest Spites"],
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
    "Eternal Guard": {
        # https://tow.whfb.app/unit/eternal-guard - 12 pts per model, unit size 5+
        # Fights with the Eternal Guard row.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Eternal Warden', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Asrai Spear",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Martial Prowess", "Move Through Cover", "Stubborn"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled", "Veteran"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Asrai Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Forest Cat": {
        # https://tow.whfb.app/unit/forest-cat - 6 pts per model, unit size 1-3
        # Fights with the Forest Cat row.
        "points": 6,
        "points_per": "model",
        "unit_size": "1-3",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 4,
            "BallisticSkill": None,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Motley Crew", "Run with the Pack", "Skirmishers"],
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
    "Glade Guard": {
        # https://tow.whfb.app/unit/glade-guard - 10 pts per model, unit size 5+
        # Fights with the Glade Guard row.
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbows.
        "points": 10,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': "Lord's Bowman", 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
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
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Move Through Cover", "Open Order"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows", "Fire & Flee", "Vanguard"],
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
    "Guardians of Talsyn": {
        # https://tow.whfb.app/unit/guardians-of-talsyn - 18 pts per model, unit size
        # 5+
        # Fights with the Guardian of Talsyn row.
        "points": 18,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Watchmaster', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 3, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Asrai Spear",
            "Shield": False,
            "SpecialRules": ["Close Order", "Drilled", "Elven Reflexes", "Martial Prowess", "Move Through Cover", "Parry", "Stubborn", "Veteran"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Asrai Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Sylvan Boar": {
        # https://tow.whfb.app/unit/sylvan-boar - 11 pts per model, unit size 1-3
        # Fights with the Sylvan Boar row.
        "points": 11,
        "points_per": "model",
        "unit_size": "1-3",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": None,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Furious Charge", "Motley Crew", "Razor Tusks", "Run with the Pack", "Skirmishers"],
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
    "Tree Kin": {
        # https://tow.whfb.app/unit/tree-kin - 51 pts per model, unit size 2+
        # Fights with the Tree Kin row.
        "points": 51,
        "points_per": "model",
        "unit_size": "2+",
        "champion": {'Name': 'Elder', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 6, 'Initiative': 3, 'Wounds': 3, 'Attacks': 4, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 6,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Forest Spirit",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2)", "Close Order", "Fear", "Flammable", "Immune to Psychology", "Magical Attacks", "Move Through Cover", "Regeneration (5+)", "Stomp Attacks (1)", "Stubborn", "Tree Spirit", "Tree Whack"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Forest Spites"],
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
    "Wardancers": {
        # https://tow.whfb.app/unit/wardancers - 16 pts per model, unit size 5+
        # Fights with the Wardancer row.
        "points": 16,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Bladesinger', 'Movement': 5, 'WeaponSkill': 6, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 3, 'Initiative': 6, 'Wounds': 1, 'Attacks': 3, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dances of Loec", "Evasive", "Furious Charge", "Immune to Psychology", "Loner", "Motley Crew", "Move Through Cover", "Open Order", "Skirmishers", "Strike First", "Talismanic Tattoos", "Ward6"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Throwing Spear"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Waywatchers": {
        # https://tow.whfb.app/unit/waywatchers - 16 pts per model, unit size 5+
        # Fights with the Waywatcher row.
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbows.
        "points": 16,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Sentinel', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 6, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 5,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Evasive", "Feigned Flight", "Fire & Flee", "Ignores Cover", "Move Through Cover", "Scouts", "Skirmishers"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows", "Ambushers", "Vanguard", "Veteran"],
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
    "Wildwood Rangers": {
        # https://tow.whfb.app/unit/wildwood-rangers - 14 pts per model, unit size 5+
        # Fights with the Wildwood Ranger row.
        "points": 14,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Wildwood Warden', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Ranger's Glaive",
            "Shield": False,
            "SpecialRules": ["Close Order", "Elven Reflexes", "Guardians of the Wildwood", "Immune to Psychology", "Move Through Cover"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Ranger's Glaive"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Glade Riders": {
        # https://tow.whfb.app/unit/glade-riders - 17 pts per model, unit size 4+
        # Fights with the Glade Rider row.
        # Also has a profile for Elven Steed (M9 WS3 BS- S3 T- W- I4 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbows.
        "points": 17,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'Glade Knight', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
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
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Fast Cavalry", "Fire & Flee", "Open Order", "Skirmishers", "Swiftstride"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows", "Ambushers", "Drilled", "Reserve Move"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Sisters of the Thorn": {
        # https://tow.whfb.app/unit/sisters-of-the-thorn - 22 pts per model, unit size
        # 4+
        # Fights with the Sister of the Thorn row.
        # Also has a profile for Steed of Isha (M8 WS3 BS- S4 T- W- I4 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: blackbriar
        # javelins.
        "points": 22,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'Handmaiden of the Thorn', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 6, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [
            {'Name': 'Steed of Isha', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 5,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daughters of Eternity", "Ward4", "Deepwood Coven", "Elven Reflexes", "Fast Cavalry", "Fire & Flee", "Move Through Cover", "Open Order", "Poisoned Attacks", "Swiftstride"],
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
    "Warhawk Riders": {
        # https://tow.whfb.app/unit/warhawk-riders - 41 pts per model, unit size 3+
        # Fights with the Warhawk Rider row.
        # Also has a profile for Warhawk (M2 WS3 BS- S4 T- W- I4 A2 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbows.
        "points": 41,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Wind Rider', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 4, 'Initiative': 4, 'Wounds': 2, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Warhawk', 'Movement': 2, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Evasive", "Fear", "Feigned Flight", "Fire & Flee", "Fly (10)", "Skirmishers", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Wild Riders": {
        # https://tow.whfb.app/unit/wild-riders - 26 pts per model, unit size 4+
        # Fights with the Wild Rider row.
        # Also has a profile for Steed of Kurnous (M9 WS3 BS- S4 T- W- I4 A1 Ld-); not
        # simulated.
        "points": 26,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'Wild Hunter', 'Movement': None, 'WeaponSkill': 5, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [
            {'Name': 'Steed of Kurnous', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Hunting Spear",
            "Shield": False,
            "SpecialRules": ["Counter Charge", "Elven Reflexes", "Fast Cavalry", "Fear", "Frenzy", "Furious Charge (Riders only)", "Move Through Cover", "Open Order", "Swiftstride", "Talismanic Tattoos", "Ward6"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Hunting Spear"],
            "armor": ["Light Armor"],
            "shield": True,
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
            "Race": "Wood Elf",
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
    "Treeman": {
        # https://tow.whfb.app/unit/treeman - 215 pts per unit
        # Fights with the Treeman row.
        # Shooting is not simulated, so these are left out of the options:
        # Strangleroots.
        "points": 215,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 2,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Forest Spirit",
            "Armor": "Full Plate Armor",
            "Weapon": "Oaken Fists",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Close Order", "Flammable", "Immune to Psychology", "Large Target", "Magical Attacks", "Move Through Cover", "Regeneration (5+)", "Stomp Attacks (D3)", "Stubborn", "Terror", "Timmm-berrr!", "Tree Spirit", "Tree Whack"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
            "OptionalRules": ["Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Oaken Fists"],
            "armor": ["Full Plate Armor"],
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
    "Boldest of the Bold": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/boldest-of-the-bold",
        "text": (
            "Araloth ignores all negative modifiers to his Leadership "
            "characteristic."
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
    "Courage Beyond Compare": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/courage-beyond-compare",
        "text": (
            "If this character joins a unit of Guardians of Talsyn, that unit gains "
            "the Immune to Psychology special rule. Should this character leave the "
            "unit for any reason, the unit loses this special rule."
        ),
    },
    "Dances of Loec": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dances-of-loec",
        "text": (
            "When this unit's combat is chosen during Step 1.1 of any Choose & "
            "Fight Combat subphase, choose one of the following Dances of Loec for "
            "it to perform. Every model within the unit performs the same Dance: - "
            "Whirling Death: Until the end of this Combat phase, the Armour "
            "Piercing characteristic of this unit's weapons is improved by 2. - "
            "Storm of Blades: Until the end of this Combat phase, this unit gains "
            "the Extra Attacks (+1) special rule. - The Shadows Coil: Until the end "
            "of this Combat phase, this unit has a 4+ ward save against any wounds "
            "suffered. - Woven Mist: Any enemy model that directs its attacks "
            "against this unit during this Combat phase suffers a -1 modifier to "
            "its rolls To Hit. [...]"
        ),
    },
    "Daughters of Eternity": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/daughters-of-eternity",
        "text": (
            "Models with this special rule have a 4+ Ward save against any wounds "
            "suffered."
        ),
    },
    "Deepwood Coven": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/deepwood-coven",
        "text": (
            "A unit of Sisters of the Thorn knows a single, randomly generated "
            "spell from either the Battle Magic or Elementalism Lore of Magic. If "
            "you wish, this spell may be discarded and the unit may instead select "
            "the signature spell of its chosen Lore of Magic. The unit may cast "
            "this spell as a Bound spell: - If the unit includes a Handmaiden of "
            "the Thorn, it may cast this Bound spell with a Power Level of 1. - If "
            "it includes both a Handmaiden of the Thorn and a standard bearer, it "
            "may cast this Bound spell with a Power Level of 2. - Otherwise, the "
            "unit may cast this Bound spell with a Power Level of 0."
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
    "Elven Reflexes": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/elven-reflexes",
        "text": (
            "A model with this special rule (but not its mount) has a +1 modifier "
            "to its Initiative characteristic (to a maximum of 10) during the first "
            "round of any combat."
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
    "Favour of the Goddess": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/favour-of-the-goddess",
        "text": (
            "Araloth has a 5+ Ward save against any wounds suffered."
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
    "Feigned Flight": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/feigned-flight",
        "text": (
            "If this unit chooses to Flee (or Fire & Flee) as a charge reaction, it "
            "automatically rallies at the end of its move."
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
    "Furious Charge": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/furious-charge",
        "text": (
            "During a turn in which it made a charge move of 3\" or more, a model "
            "with this special rule gains a +1 modifier to its Attacks "
            "characteristic."
        ),
    },
    "Guardians of the Wildwood": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/guardians-of-the-wildwood",
        "text": (
            "Whilst it is in base contact with an enemy model that causes Fear or "
            "Terror, a model with this special rule gains a +1 modifier to its "
            "Attacks characteristics (to a maximum of 10) and the Multiple Wounds "
            "(2) special rule."
        ),
    },
    "Hawk-eyed Archer": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/hawk-eyed-archer",
        "text": (
            "A model with this special rule can target any enemy character it can "
            "draw a line of sight to, regardless of the usual rules for targeting "
            "Lone characters. In addition, a model with this special rule can "
            "target a specific model within its target unit, such as a champion or "
            "a character."
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
    "Lore of Athel Loren": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-athel-loren",
        "text": (
            "Wood Elf Mages have a unique relationship with the forest. They are a "
            "part of it, much like Dryads and Treemen, yet possessed of a greater "
            "sense of individuality. This bond allows them to commune with the "
            "forest, to entreat with it on behalf of their kin and, in times of "
            "war, to awaken it to their aid. A Wizard with the 'Lore of Athel "
            "Loren' special rule may discard one of their randomly generated spells "
            "as normal. When they do so, they may select instead either the "
            "signature spell of their chosen Lore of Magic, or one of the spells "
            "listed below. Lore of Athel Loren Lore"
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
    "Parry": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/parry-wood-elves",
        "text": (
            "When fighting with a hand weapon and shield, or Asrai spear and "
            "shield, this unit improves its armour value by 1."
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
    "Run with the Pack": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/run-with-the-pack",
        "text": (
            "Whilst one or more Beast Keeper remains within this unit, the unit is "
            "not subject to the Undisciplined rule and war beasts within this unit "
            "do not fear models with the Flaming Attacks special rule. In addition, "
            "a unit with this special rule may use the Movement characteristic of "
            "the majority of the models in the unit."
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
    "Skaryn the Eye Thief": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/skaryn-the-eye-thief",
        "text": (
            "During the Command sub-phase of his turn, Araloth may attempt to "
            "dispatch Skaryn to strike from the skies by rolling a D6. On a roll of "
            "1-2, Skaryn lingers out of reach of the enemy and nothing happens. On "
            "a roll of 3+, Skaryn descends from the skies to strike at his master's "
            "mark. Nominate a single enemy model within 18\" of Araloth. That model "
            "suffers a single Strength 4 hit with an AP of -1. If the target "
            "suffers an unsaved wound, its Weapon Skill and Initiative "
            "characteristics are reduced by D3 (to a minimum of 1) for the "
            "remainder of the game."
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
    "Strike First": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/strike-first",
        "text": (
            "During the Combat phase, a model with this special rule that is "
            "engaged in combat improves its Initiative characteristic to 10 (before "
            "any other modifiers are applied). If a model has both this rule and "
            "Strike Last, the two rules cancel one another out."
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
    "Talismanic Tattoos": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/talismanic-tattoos",
        "text": (
            "Talismanic Tattoos give their wearer a 6+ Ward save against any wounds "
            "suffered."
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
    "The Arrow of Kurnous": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/the-arrow-of-kurnous",
        "text": (
            "Once deployment is complete, but before the roll-off to determine "
            "which player takes the first turn, if the General of your opponent's "
            "army is within 36\" of one or more models in your army that has this "
            "special rule, one of those models may fire the Arrow of Kurnous. If "
            "the Arrow of Kurnous is fired, the General of your opponent's army "
            "immediately suffers a single Strength 3 hit, with no armour or "
            "Regeneration saves permitted (Ward saves can be attempted as normal). "
            "However, if the Arrow of Kurnous is fired, your opponent adds +1 to "
            "their roll when rolling off to determine who takes the first turn."
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
    "Tree Spirit": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/tree-spirit",
        "text": (
            "A character with this special rule cannot join a unit without this "
            "special rule. A unit with this special rule cannot be joined by, or "
            "use the Leadership characteristic of, a character without this special "
            "rule. However, a unit with this special rule can use the Leadership "
            "characteristic of a friendly character with this special rule that is "
            "not fleeing whilst within that character's Command range."
        ),
    },
    "Tree Whack": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/tree-whack",
        "text": (
            "Once per turn, during the Combat phase, a model with this special rule "
            "may use one of its Attacks to make a single 'Tree Whack' attack. To "
            "make a Tree Whack attack, nominate a single model within an enemy unit "
            "that this model is engaged in combat with to be the target of the "
            "attack. That model must immediately make an Initiative test: - If the "
            "test is failed, the target suffers D3 hits, each using the Strength "
            "characteristic of this model, with no armour save save permitted (Ward "
            "and Regeneration saves can be attempted as normal). - If the test is "
            "passed, the target manages to avoid the Tree Whack."
        ),
    },
    "Troubadour of Loec": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/troubadour-of-loec",
        "text": (
            "A Shadowdancer that joins a unit of Wardancers is considered to have "
            "the Dances of Loec special rule for as long as they remain with the "
            "unit."
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
