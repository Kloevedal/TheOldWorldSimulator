"""Dwarfen Mountain Holds.

Profiles from https://tow.whfb.app/army/dwarfen-mountain-holds
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Dwarfen Mountain Holds"

# Other names that should resolve to this faction.
ALIASES = [
    "Dwarfs",
    "Dwarves",
    "Dwarfen Mountain Holds",
    "Mountain Holds",
    "Dawi",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Ungrim": "Ungrim Ironfist",
    "Thorgrim": "Thorgrim Ulleksson",
    "Burlok": "Burlok Damminson",
    "Dwarf King": "King",
    "Dwarf Engineer": "Engineer",
}

CHARACTERS = {
    "King": {
        # https://tow.whfb.app/unit/king - 125 pts
        # May take up to 125 pts of Weapon, Armour and Talismanic runes; runes are
        # not modelled.
        "points": 125,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 7,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ancestral Grudge", "Dwarf Crafted", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Rallying Cry", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Shieldbearers"]
        }
    },
    "Thane": {
        # https://tow.whfb.app/unit/thane - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ancestral Grudge", "Dwarf Crafted", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Rallying Cry", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Shieldbearers"]
        }
    },
    "Runelord": {
        # https://tow.whfb.app/unit/runelord - 120 pts
        "points": 120,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Forgefire", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-2)", "Resolute", "Rune Lore", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Runesmith": {
        # https://tow.whfb.app/unit/runesmith - 65 pts
        "points": 65,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Forgefire", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-2)", "Resolute", "Rune Lore", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Daemon Slayer": {
        # https://tow.whfb.app/unit/daemon-slayer - 130 pts
        # Slayers wear no armour.
        "points": 130,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 7,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Deathblow", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Immune to Psychology", "Killing Blow", "Loner", "Magic Resistance (-2)", "Resolute", "Slayer of Daemons", "Unbreakable", "Vanguard"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Dragon Slayer": {
        # https://tow.whfb.app/unit/dragon-slayer - 70 pts
        # Slayers wear no armour.
        "points": 70,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Deathblow", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Immune to Psychology", "Killing Blow", "Loner", "Magic Resistance (-2)", "Resolute", "Slayer of Dragons", "Unbreakable", "Vanguard"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Engineer": {
        # https://tow.whfb.app/unit/engineer - 50 pts
        "points": 50,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Artillery Master", "Dwarf Crafted", "Entrenchment", "Gromril Armour", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute", "Stand Back Chief", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
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
    "Engineer Sapper": {
        # https://tow.whfb.app/unit/engineer-sapper - 70 pts
        "points": 70,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dig In!", "Dwarf Crafted", "Gromril Armour", "Hatred (Orcs & Goblins)", "Hostile Terrain", "Magic Resistance (-1)", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
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
    "Ungrim Ironfist": {
        # https://tow.whfb.app/unit/ungrim-ironfist - 315 pts
        # Fixed wargear; must be fielded as presented.
        "points": 315,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 9,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 6,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": "Light Armor",
            "Weapon": "Axe of Dargo",
            "Shield": False,
            "SpecialRules": ["Deathblow", "Gromril Armour", "Hatred (Orcs & Goblins)", "Immune to Psychology", "King of the Slayer Hold", "Magic Resistance (-2)", "Rallying Cry", "Resolute", "Slayer", "Unbreakable"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Axe of Dargo", "Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": ["Axe of Dargo", "Slayer Crown"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Thorgrim Ulleksson": {
        # https://tow.whfb.app/unit/thorgrim-ulleksson - 250 pts
        # His armour is the Armour of Skaldour, a magic item rather than a standard
        # armour type, so Armor is None until runic items are modelled.
        "points": 250,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Grudge-Settler",
            "Shield": True,
            "SpecialRules": ["Gromril Armour", "Grudgelore", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Rallying Cry", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Grudge-Settler", "Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": ["Grudge-Settler", "Grudgestone", "Armour of Skaldour"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Burlok Damminson": {
        # https://tow.whfb.app/unit/burlok-damminson - 85 pts
        # Fixed wargear. The Furnace Hammer rolls an Artillery dice for its
        # Strength and can Misfire; the rivet gun is ranged and is not simulated.
        "points": 85,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Furnace Hammer",
            "Shield": False,
            "SpecialRules": ["Dwarf Crafted", "Gromril Armour", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Prepared Positions", "Range Finding Optics", "Resolute", "Stand Back Chief", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Furnace Hammer", "Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": ["Furnace Hammer", "Rivet Gun"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Anvil of Doom": {
        # https://tow.whfb.app/unit/anvil-of-doom - 235 pts
        # Uses the Forgefather & Anvil Guard row: a war machine fights with its
        # crew's characteristics, including T and W (Split Profile (War
        # Machine)). The machine's own row is T7 W5, used only outside combat.
        # The crew losing -1 Attack per Wound lost is not modelled. Its runes
        # (up to 100 points) are not modelled either.
        "points": 235,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Ancestral Shield", "Ward5", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Immune to Psychology", "Immovable Object", "Magic Resistance (-3)", "Resolute", "Rune Lore", "Skirmishers", "Strike the Runes", "Unbreakable"],
            "TroopType": "WarMachine",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
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
    "Brotherhood of Grimnir": {
        # https://tow.whfb.app/unit/brotherhood-of-grimnir - 18 pts per model, unit
        # size 5-30 models
        # Fights with the Shrine Guards row.
        "points": 18,
        "points_per": "model",
        "unit_size": "5-30 models",
        "champion": {'Name': 'Shrine Keeper', 'Movement': 3, 'WeaponSkill': 6, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 3, 'Wounds': 2, 'Attacks': 2, 'Leadership': 10},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blessings of Grimnir (Shrine Keeper only)", "Close Order", "Deathblow", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Immune to Psychology", "Loner", "Magic Resistance (-2)", "Motley Crew", "Open Order", "Resolute", "Slayer", "Unbreakable"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Standard runes", "runic tattoos", "Weapon runes", "Talismanic runes"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Doomseeker": {
        # https://tow.whfb.app/unit/doomseeker - 50 pts per unit
        # Its Attacks are 2D3, a dice value the engine cannot use yet; recorded as
        # None, so it makes no attacks.
        # Fights with the Doomseeker row.
        "points": 50,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": None,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Deathblow", "Doomseeker", "First to the Fray", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Immune to Psychology", "Impact Hits (D3+1)", "Loner", "Magic Resistance (-2)", "Random Attacks", "Resolute", "Skirmishers", "Unbreakable", "Vanguard", "Whirlwind of Death"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Weapon runes", "runic tattoos"],
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
    "Dwarf Warriors": {
        # https://tow.whfb.app/unit/dwarf-warriors - 8 pts per model, unit size 5+
        # Fights with the Dwarf Warrior row.
        "points": 8,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Veteran', 'Movement': 3, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute", "Shieldwall"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Weapon runes", "Drilled", "Veteran", "Standard runes"],
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
    "Hammerers": {
        # https://tow.whfb.app/unit/hammerers - 16 pts per model, unit size 5+
        # Fights with the Hammerer row.
        "points": 16,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Royal Champion', 'Movement': 3, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Great Hammer",
            "Shield": False,
            "SpecialRules": ["Close Order", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute", "Royal Guard", "Shieldwall", "Stoic Defenders", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled", "Veteran", "Standard runes", "Weapon runes", "Talismanic runes"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Hammer"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Imperial Dwarf Mercenaries": {
        # https://tow.whfb.app/unit/imperial-dwarf-mercenaries - 8 pts per model, unit
        # size 5+
        # Fights with the Warrior row.
        # Shooting is not simulated, so these are left out of the options: Crossbows,
        # Handguns.
        "points": 8,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Veteran', 'Movement': 3, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute", "Shieldwall"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Weapon runes", "Drilled", "Veteran", "Standard runes"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Thrusting Spear"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Ironbreakers": {
        # https://tow.whfb.app/unit/ironbreakers - 15 pts per model, unit size 5+
        # Fights with the Ironbreaker row.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # drakefire pistols, Drakegun, cinderblast bombs.
        "points": 15,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Ironbeard', 'Movement': 3, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Regimental Unit", "Resolute", "Runes of Protection", "Ward6 (non-magical)", "Shieldwall", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Weapon runes", "Drilled", "Standard runes"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Irondrakes": {
        # https://tow.whfb.app/unit/irondrakes - 15 pts per model, unit size 5+
        # Fights with the Irondrake row.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # drakefire pistols, Trollhammer torpedo, cinderblast bombs, drakegun,
        # drakeguns.
        "points": 15,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Ironwarden', 'Movement': 3, 'WeaponSkill': 4, 'BallisticSkill': 5, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 1, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Detachment", "Gromril Armour", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute", "Runes of Warding", "Ward5 (Flaming)", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled", "Standard runes"],
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
    "Longbeards": {
        # https://tow.whfb.app/unit/longbeards - 12 pts per model, unit size 5+
        # Fights with the Longbeard row.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Elder', 'Movement': 3, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute", "Shieldwall", "Venerable", "Veteran"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Standard runes", "Weapon runes", "Talismanic runes", "Drilled"],
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
    "Miners": {
        # https://tow.whfb.app/unit/miners - 12 pts per model, unit size 5+
        # Fights with the Miner row.
        # Shooting is not simulated, so these are left out of the options: blasting
        # charges.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Prospector', 'Movement': 3, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Ambushers", "Close Order", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute", "Vanguard"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Close Order", "Open Order", "Veteran", "Standard runes"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Steam Drill"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Quarrellers": {
        # https://tow.whfb.app/unit/quarrellers - 9 pts per model, unit size 5+
        # Fights with the Quarreller row.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # pistols, Pistol, crossbows.
        "points": 9,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Veteran', 'Movement': 3, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 1, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Dwarf Crafted", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute"],
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
    "Rangers": {
        # https://tow.whfb.app/unit/rangers - 11 pts per model, unit size 5-20
        # Fights with the Ranger row.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # pistols, Pistol, crossbows, throwing axes.
        "points": 11,
        "points_per": "model",
        "unit_size": "5-20",
        "champion": {'Name': "Ol' Deadeye", 'Movement': 3, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dwarf Crafted", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Move Through Cover", "Open Order", "Resolute", "Scouts", "Skirmishers"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Standard runes"],
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
    "Royal Clan Warriors": {
        # https://tow.whfb.app/unit/royal-clan-warriors - 10 pts per model, unit size
        # 5+
        # Fights with the Royal Clan Warrior row.
        "points": 10,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Royal Clan Veteran', 'Movement': 3, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute", "Shieldwall"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Standard runes", "Weapon runes", "Talismanic runes", "Drilled", "Stubborn", "Veteran"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Gromril Great Axe"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Slayers": {
        # https://tow.whfb.app/unit/slayers - 12 pts per model, unit size 5+
        # Fights with the Troll Slayer row.
        # Also has a profile for Giant Slayer (M3 WS5 BS3 S4 T4 W1 I3 A2 Ld10); not
        # simulated.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "other_profiles": [
            {'Name': 'Giant Slayer', 'Movement': 3, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 10},
        ],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Deathblow", "\"Fight Me!\" (Giant Slayers only)", "Furious Charge", "Hatred (Orcs & Goblins)", "Immune to Psychology", "Loner", "Magic Resistance (-2)", "Motley Crew", "Open Order", "Resolute", "Slayer", "Unbreakable"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Standard runes"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Thunderers": {
        # https://tow.whfb.app/unit/thunderers - 10 pts per model, unit size 5+
        # Fights with the Thunderer row.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # pistols, Pistol, handguns.
        "points": 10,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Veteran', 'Movement': 3, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 1, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Dwarf Crafted", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute"],
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
    "Gyrobomber": {
        # https://tow.whfb.app/unit/gyrobomber - 95 pts per unit
        # Fights with the Gyrobomber row.
        # Shooting is not simulated, so these are left out of the options: Brimstone
        # gun, Clattergun, steam gun.
        "points": 95,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 1,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 4,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Bombing Run", "Close Order", "Fly (8)", "Hatred (Orcs & Goblins)", "Impact Hits (D3+1)", "Magic Resistance (-1)", "Swiftstride"],
            "TroopType": "MonstrousCreature",
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
    "Gyrocopter": {
        # https://tow.whfb.app/unit/gyrocopter - 60 pts per model, unit size 1-6
        # Fights with the Gyrocopter row.
        # Shooting is not simulated, so these are left out of the options: Brimstone
        # gun, Clattergun, steam gun.
        "points": 60,
        "points_per": "model",
        "unit_size": "1-6",
        "other_profiles": [],
        "base_profile": {
            "Movement": 1,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dispersed Formation", "Dive Bomb", "Fire & Flee", "Fly (9)", "Hatred (Orcs & Goblins)", "Impact Hits (D3)", "Magic Resistance (-1)", "Skirmishers", "Swiftstride", "Vanguard"],
            "TroopType": "MonstrousCavalry",
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
    "Scout Gyrocopter": {
        # https://tow.whfb.app/unit/scout-gyrocopter - 60 pts per model, unit size 1-2
        # Fights with the Scout Gyrocopters row.
        # Shooting is not simulated, so these are left out of the options: clattergun.
        "points": 60,
        "points_per": "model",
        "unit_size": "1-2",
        "other_profiles": [],
        "base_profile": {
            "Movement": 1,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dispersed Formation", "Fire & Flee", "Fly (10)", "Hatred (Orcs & Goblins)", "Hit & Run", "Impact Hits (D3)", "Magic Resistance (-1)", "Skirmishers", "Swiftstride", "Vanguard"],
            "TroopType": "MonstrousCavalry",
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
    "Dwarf Cart": {
        # https://tow.whfb.app/unit/dwarf-cart - 65 pts per unit
        # Fights with the Dwarf Crew (x1) row, using the Dwarf Cart row's Toughness
        # and Wounds.
        # Also has a profile for Dwarf Cart (M- WS- BS- S4 T5 W3 I- A- Ld-); not
        # simulated.
        # Also has a profile for Draft Pony (M6 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Armour value 5+ as printed on the site.
        "points": 65,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Dwarf Cart', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 5, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
            {'Name': 'Draft Pony', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hatred (Orcs & Goblins)", "Impact Hits (D3)", "Magic Resistance (-1)", "Open Order", "Resolute"],
            "TroopType": "LightChariot",
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
    "Bolt Thrower": {
        # https://tow.whfb.app/unit/bolt-thrower - 55 pts per unit
        # Fights with the Dwarf Crew row.
        # Also has a profile for Bolt Thrower (M- WS- BS- S- T6 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Bolt
        # thrower.
        "points": 55,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Bolt Thrower', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "Race": "Dwarf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Skirmishers", "Stubborn"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
            "OptionalRules": ["Engineering runes"],
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
    "Cannon": {
        # https://tow.whfb.app/unit/cannon - 95 pts per unit
        # Fights with the Dwarf Crew row.
        # Also has a profile for Cannon (M- WS- BS- S- T7 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Cannon.
        "points": 95,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Cannon', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 7, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "Race": "Dwarf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Skirmishers", "Stubborn"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
            "OptionalRules": ["Engineering runes"],
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
    "Flame Cannon": {
        # https://tow.whfb.app/unit/flame-cannon - 120 pts per unit
        # Fights with the Dwarf Crew row.
        # Also has a profile for Flame Cannon (M- WS- BS- S- T6 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Fire
        # thrower.
        "points": 120,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Flame Cannon', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "Race": "Dwarf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Skirmishers", "Stubborn"],
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
    "Goblin-Hewer": {
        # https://tow.whfb.app/unit/goblin-hewer - 120 pts per unit
        # Fights with the Slayer Crew row.
        # Also has a profile for Goblin-Hewer (M- WS- BS- S- T6 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Goblin-
        # Hewer.
        "points": 120,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Goblin-Hewer', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hatred (Orcs & Goblins)", "Immune to Psychology", "Magic Resistance (-1)", "Skirmishers", "Unbreakable"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
            "OptionalRules": ["Engineering runes"],
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
    "Grudge Thrower": {
        # https://tow.whfb.app/unit/grudge-thrower - 95 pts per unit
        # Fights with the Dwarf Crew row.
        # Also has a profile for Grudge Thrower (M- WS- BS- S- T7 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Stone
        # thrower.
        "points": 95,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Grudge Thrower', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 7, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "Race": "Dwarf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Skirmishers", "Stubborn"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
            "OptionalRules": ["Engineering runes"],
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
    "Organ Gun": {
        # https://tow.whfb.app/unit/organ-gun - 115 pts per unit
        # Fights with the Dwarf Crew row.
        # Also has a profile for Organ Gun (M- WS- BS- S- T7 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Organ gun.
        "points": 115,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Organ Gun', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 7, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "Race": "Dwarf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Skirmishers", "Stubborn"],
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
    'Gromril Armour': {
        "status": 'implemented',
        "text": (
            "May reroll any roll of a natural 1 made when making an Armour Save "
            "roll. "
        ),
    },
    'Gromril Weapons': {
        "status": 'implemented',
        "text": (
            "A hand weapon carried by this model has an Armour Piercing of -1. "
            "A single, ordinary hand weapon only - not two hand weapons, "
            "another weapon type, or a runed hand weapon. "
        ),
    },
    'Resolute': {
        "status": None,
        "text": (
            "-1 to any Flee or Pursuit roll (min 1). Neither happens in a duel. "
        ),
    },
    'Ancestral Grudge': {
        "status": None,
        "text": (
            "A model with this special rule has the Hatred (enemy characters) "
            "special rule, meaning it hates all characters in the opposing army. If "
            "this character joins a unit of Longbeards or Hammerers, that unit will "
            "also gain this special rule. Should this character leave a unit of "
            "Longbeards or Hammerers they have joined for any reason, that unit "
            "loses this special rule."
        ),
    },
    'Hatred (Orcs & Goblins)': {
        "status": 'implemented',
        "text": (
            "Reroll failed To Hit rolls in the first round against Orcs and "
            "Goblins. "
        ),
    },
    'Rune Lore': {
        "status": None,
        "text": (
            "Runes are not modelled. "
        ),
    },
    'Forgefire': {
        "status": None,
        "text": (
            "If this character joins a unit, that unit will gain the Armour Bane "
            "(2) and Flaming Attacks special rules. Should this character leave a "
            "unit it has joined for any reason, that unit loses these special "
            "rules."
        ),
    },
    "Ancestral Shield": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/ancestral-shield",
        "text": (
            "An Anvil of Doom and the Forgefather & Anvil Guard have a 5+ Ward save "
            "against any wounds suffered."
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
    "Strike the Runes": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/strike-the-runes",
        "text": (
            "An Anvil of Doom can cast the following Bound spells, with a Power "
            "Level of 2: Rune of Oath & Steel, Rune of Hearth & Home, Rune of Haste "
            "& Urgency & Rune of Wrath & Ruin Rune of Oath & Steel Rune of Hearth & "
            "Home Rune of Haste & Urgency Rune of Wrath & Ruin"
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
    "\"Fight Me!\"": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fight-me",
        "text": (
            "Any model with this special rule can issue and accept challenges in "
            "the same manner as a character."
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
    "Blessings of Grimnir": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/blessings-of-grimnir",
        "text": (
            "A model with this special rule may be nominated to attempt a Wizardly "
            "Dispel, as if it were a Wizard. However, unlike regular Wizards, a "
            "Shrine Keeper does not have a Level of Wizardry to determine their "
            "Dispel range or modify their Dispel rolls. Instead, a Shrine Keeper "
            "has a Dispel range of 21\" and may apply a +1 modifier to their Dispel "
            "rolls."
        ),
    },
    "Bombing Run": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/bombing-run",
        "text": (
            "This model may perform a 'Bombing Run' attack against a single enemy "
            "unit that is not engaged in combat. To do so, this model must move (by "
            "flying) over the unit it wishes to attack during the Remaining Moves "
            "sub-phase. Once this model's movement is complete, roll on the Bombing "
            "Run table below: D6 | Result 1 | Premature Detonation: The release "
            "mechanism jams and a bomb explodes prematurely. This model loses a "
            "single Wound. 2 | Dud: A solitary bomb is released, but fails to "
            "detonate before landing squarely upon the head of an unfortunate "
            "enemy. The enemy unit loses a single Wound. 3-4 | Direct Hit: A "
            "cluster of bombs lands directly on-target. Place a large (5\") blast "
            "template so that its [...]"
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
    "Deathblow": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/deathblow",
        "text": (
            "When a model with this special rule is reduced to zero Wounds by an "
            "enemy attack during the Combat phase, the unit that made the attack "
            "suffers a Strength 3 hit, with an AP of -1. Note that if this model is "
            "reduced to zero Wounds whilst engaged in a challenge, it is the model "
            "that made the attack that suffers this hit, rather than its unit."
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
    "Dive Bomb": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dive-bomb",
        "text": (
            "Once per game, a unit with this special rule may perform a 'Dive Bomb' "
            "attack against a single enemy unit that is not engaged in combat. To "
            "do so, this unit must move (by flying) over the unit it wishes to "
            "attack during the Remaining Moves sub-phase. Once this unit's movement "
            "is complete, the enemy unit suffers D6 Strength 3 hits, each with an "
            "AP of -1, for each model in this unit that moved over it. However, for "
            "each roll of a natural 1 made when determining the number of hits, a "
            "bomb has misfired and this unit loses a single Wound instead."
        ),
    },
    "Doomseeker": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/doomseeker",
        "text": (
            "At the end of the battle, a Doomseeker that has been slain is worth no "
            "Victory Points. However, if a Doomseeker is still alive, the enemy "
            "player wins a bonus number of Victory Points equal to 100% of its "
            "points cost."
        ),
    },
    "Dwarf Crafted": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dwarf-crafted",
        "text": (
            "Models with this special rule do not suffer the usual -1 To Hit "
            "modifier when making a Stand & Shoot charge reaction."
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
    "First to the Fray": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/first-to-the-fray",
        "text": (
            "This model increases its maximum possible charge range by 3\" and, when "
            "it makes a Charge roll, may apply a +D3 modifier to the result."
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
    "Hit & Run": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/hit-and-run",
        "text": (
            "Should it win a round of combat, a unit with this special rule may "
            "choose to Fall Back in Good Order rather than making a follow up or "
            "pursuit move."
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
    "Loner": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/loner",
        "text": (
            "A character with this special rule cannot be your General and cannot "
            "join a unit without this special rule. A unit with this special rule "
            "cannot be joined by a character without this special rule."
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
    "Regimental Unit": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/regimental-unit",
        "text": (
            "A unit with this special rule can be accompanied by detachment."
        ),
    },
    "Royal Guard": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/royal-guard",
        "text": (
            "Your army may include one unit of Hammerers for every King or Thane it "
            "includes. Any model in a unit of Hammerers that has been joined by a "
            "King or Thane can issue and accept challenges in the same manner as a "
            "character. Should the King or Thane leave the unit for any reason, the "
            "unit loses this ability."
        ),
    },
    "Runes of Protection": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/runes-of-protection",
        "text": (
            "Models with this special rule have a 6+ Ward save against any wounds "
            "suffered that were caused by a non-magical enemy attack."
        ),
    },
    "Runes of Warding": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/runes-of-warding",
        "text": (
            "A model with this special rule has a 5+ Ward save against any wounds "
            "suffered that were caused by an attack that has the Flaming Attacks "
            "special rule."
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
    "Slayer": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/slayer",
        "text": (
            "When this model makes a roll To Wound, a roll of 4+ is always a "
            "success, regardless of the target's Toughness."
        ),
    },
    "Stoic Defenders": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/stoic-defenders",
        "text": (
            "During a turn in which it was charged by the enemy, a model with this "
            "special rule gains a +1 modifier to its Initiative and Attacks "
            "characteristics."
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
    "Venerable": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/venerable",
        "text": (
            "Unless this unit is fleeing, friendly units within 6\" of it can re- "
            "roll any failed Panic test."
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
    "Whirlwind of Death": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/whirlwind-of-death",
        "text": (
            "Impact Hits caused by this model are resolved using the profile of its "
            "whirling blades of death. In addition, when this model makes a roll To "
            "Wound, a roll of 4+ is always a success, regardless of the target's "
            "Toughness."
        ),
    },
    "\"Fight Me!\"": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fight-me",
        "text": (
            "Any model with this special rule can issue and accept challenges in "
            "the same manner as a character."
        ),
    },
    "\"Fight Me!\"": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fight-me",
        "text": (
            "Any model with this special rule can issue and accept challenges in "
            "the same manner as a character."
        ),
    },
    "\"Fight Me!\"": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fight-me",
        "text": (
            "Any model with this special rule can issue and accept challenges in "
            "the same manner as a character."
        ),
    },
    "\"Fight Me!\"": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fight-me",
        "text": (
            "Any model with this special rule can issue and accept challenges in "
            "the same manner as a character."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
