"""Orc & Goblin Tribes.

Profiles from https://tow.whfb.app/army/orc-and-goblin-tribes
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Orc & Goblin Tribes"

# Other names that should resolve to this faction.
ALIASES = [
    "Orcs",
    "Orcs & Goblins",
    "Orc and Goblin",
    "O&G",
    "Greenskins",
    "Goblins",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Kiknik": "Kiknik Toofsnatcha",
    "Ogdruz": "Ogdruz Swampdigga",
}

CHARACTERS = {
    "Orc BigBoss": {
        # https://tow.whfb.app/unit/orc-bigboss - 55 pts
        "points": 55,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Orc",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Choppas","Furious Charge", "Ignore Goblin Panic", "Impetuous", "Rallying Cry", "Waaagh!", "Warband"],
            "OptionalRules": ["Frenzy","Warpaint"],
            "TroopType": "RegularInfantry",
            "UnitCategory":"Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "warpaint": False,
            "items": [],
        },
        "mount_options":{
            "mounts": ["War Boar", "Orc Boar Chariot"]
        }
    
    },
    "Black Orc Bigboss": {
        # https://tow.whfb.app/unit/black-orc-bigboss - 75 pts
        "points": 75,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Orc",
            "Armor": "Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Choppas","Da Boyz","Furious Charge", "Ignore Panic", "Quell Impetuosity", "Rallying Cry", "Waaagh!"],
            "TroopType": "HeavyInfantry",
            "UnitCategory":"Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options":{
            "mounts": ["War Boar", "Orc Boar Chariot", "Black Orc Boar Chariot"]
        }
    },
    "Orc Warboss": {
        # https://tow.whfb.app/unit/orc-warboss - 110 pts
        "points": 110,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 2,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Orc",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Choppas", "Furious Charge", "Ignore Goblin Panic", "Impetuous", "Rallying Cry", "Waaagh!", "Warband"],
            "OptionalRules": ["Frenzy", "Warpaint"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "warpaint": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["War Boar", "Orc Boar Chariot", "Wyvern"]
        }
    },
    "Black Orc Warboss": {
        # https://tow.whfb.app/unit/black-orc-warboss - 135 pts
        "points": 135,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 7,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Orc",
            "Armor": "Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Choppas", "Da Boyz", "Furious Charge", "Ignore Panic", "Quell Impetuosity", "Rallying Cry", "Waaagh!"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["War Boar", "Orc Boar Chariot", "Black Orc Boar Chariot", "Wyvern"]
        }
    },
    "Goblin Warboss": {
        # https://tow.whfb.app/unit/goblin-warboss - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 7,
            "Race": "Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Impetuous", "Rallying Cry", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Giant Wolf", "Gigantic Spider", "Goblin Wolf Chariot"]
        }
    },
    "Goblin Bigboss": {
        # https://tow.whfb.app/unit/goblin-bigboss - 35 pts
        "points": 35,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 6,
            "Race": "Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Impetuous", "Rallying Cry", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Giant Wolf", "Gigantic Spider", "Goblin Wolf Chariot"]
        }
    },
    "Night Goblin Warboss": {
        # https://tow.whfb.app/unit/night-goblin-warboss - 55 pts
        "points": 55,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 6,
            "Race": "Night Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Hatred (Dwarfs)", "Rallying Cry", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Giant Cave Squig"]
        }
    },
    "Night Goblin Bigboss": {
        # https://tow.whfb.app/unit/night-goblin-bigboss - 30 pts
        "points": 30,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 5,
            "Race": "Night Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Hatred (Dwarfs)", "Rallying Cry", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Giant Cave Squig"]
        }
    },
    "Orc Weirdnob": {
        # https://tow.whfb.app/unit/orc-weirdnob - 140 pts
        "points": 140,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Orc",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Choppas", "Ignore Goblin Panic", "Lore of Gork", "Mob Rule", "Warband"],
            "OptionalRules": ["Frenzy", "Warpaint"],
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Elementalism", "Waaagh! Magic"],
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
            "mounts": ["War Boar", "Wyvern"]
        }
    },
    "Orc Weirdboy": {
        # https://tow.whfb.app/unit/orc-weirdboy - 65 pts
        "points": 65,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Orc",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Choppas", "Ignore Goblin Panic", "Lore of Gork", "Mob Rule", "Warband"],
            "OptionalRules": ["Frenzy", "Warpaint"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "Waaagh! Magic"],
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
            "mounts": ["War Boar"]
        }
    },
    "Goblin Oddnob": {
        # https://tow.whfb.app/unit/goblin-oddnob - 135 pts
        "points": 135,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Lore of Mork", "Warband"],
            "WizardLevel": 3,
            "Lores": ["Elementalism", "Waaagh! Magic"],
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
            "mounts": ["Giant Wolf", "Goblin Wolf Chariot", "Arachnarok Spider"]
        }
    },
    "Goblin Oddgit": {
        # https://tow.whfb.app/unit/goblin-oddgit - 60 pts
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
            "Leadership": 6,
            "Race": "Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Lore of Mork", "Warband"],
            "WizardLevel": 1,
            "Lores": ["Elementalism", "Waaagh! Magic"],
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
            "mounts": ["Giant Wolf", "Goblin Wolf Chariot"]
        }
    },
    "Night Goblin Oddnob": {
        # https://tow.whfb.app/unit/night-goblin-oddnob - 130 pts
        "points": 130,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 6,
            "Race": "Night Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Hatred (Dwarfs)", "Lore of Mork", "Warband"],
            "WizardLevel": 3,
            "Lores": ["Illusion", "Waaagh! Magic"],
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
    "Night Goblin Oddgit": {
        # https://tow.whfb.app/unit/night-goblin-oddgit - 55 pts
        "points": 55,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Night Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Hatred (Dwarfs)", "Lore of Mork", "Warband"],
            "WizardLevel": 1,
            "Lores": ["Illusion", "Waaagh! Magic"],
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
    "Troll Hag": {
        # https://tow.whfb.app/unit/troll-hag - 235 pts
        # Scaly skin counts as heavy armour; the gnarled stump as a hand weapon.
        "points": 235,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 6,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Troll",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Flammable", "Immune to Psychology", "Indiscriminate Hunger", "Large Target", "Motherly Love", "Regeneration (5+)", "Slimy Shanks", "Stomp Attacks (D6)", "Stupidity", "Terror", "Timmm-berrr!", "Unbreakable"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Lore of Troll Magic"],
            "TroopType": "Behemoth",
            "UnitCategory": "Character",
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
    "Ogdruz Swampdigga": {
        # https://tow.whfb.app/unit/ogdruz-swampdigga - 195 pts
        # An Orc Weirdnob with fixed wargear; must be fielded as presented.
        "points": 195,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Orc",
            "Armor": None,
            "Weapon": "Bog-wood Staff",
            "Shield": False,
            "SpecialRules": ["Choppas", "Da Troll Calla", "Ignore Goblin Panic", "Protect Da Boss", "Syphoned Strength", "Warband"],
            "WizardLevel": 3,
            "Lores": ["Elementalism", "Troll Magic"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Bog-wood Staff", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": ["Bog-wood Staff", "Trollhide Shawl", "Lore Familiar"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Kiknik Toofsnatcha": {
        # https://tow.whfb.app/unit/kiknik-toofsnatcha - 105 pts
        # Rides Chompa (M9 WS3 S4 I3 A2); the mount is not simulated yet.
        "points": 105,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Goblin",
            "Armor": "Light Armor",
            "Weapon": "Da Skull Smasha",
            "Shield": True,
            "SpecialRules": ["All Sneaky Like", "Ambushers", "Armour Bane (1, Chompa only)", "Armoured Hide (1)", "Chariot Runners", "Fast Cavalry", "Fear of Elves", "Hit & Run", "Impetuous", "Rallying Cry", "Swiftstride", "Warband"],
            "TroopType": "LightCavalry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Da Skull Smasha", "Da Skull Smasha (Pick)", "Cavalry Spear", "Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": ["Da Boss's Trophy Rack", "Da Skull Smasha"],
        },
        "mount_options": {
            "mounts": ["Chompa"]
        }
    },
}

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Badlands Ogre Bulls": {
        # https://tow.whfb.app/unit/badlands-ogre-bulls - 31 pts per model, unit size
        # 3+
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
            "SpecialRules": ["Armour Bane (1)", "Close Order", "Fear", "Impact Hits (1)", "Mercenaries", "Motley Crew", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Ironfist"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Black Orc Mob": {
        # https://tow.whfb.app/unit/black-orc-mob - 12 pts per model, unit size 5+
        # Fights with the Black Orc row.
        # Also has a profile for Black Orc Boss (M4 WS4 BS3 S4 T4 W1 I3 A2 Ld8); not
        # simulated.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "other_profiles": [
            {'Name': 'Black Orc Boss', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Orc",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Choppas", "Close Order", "Da Boyz", "Furious Charge", "Ignore Panic", "Motley Crew", "Quell Impetuosity"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Stubborn", "Veteran"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Common Troll Mob": {
        # https://tow.whfb.app/unit/common-troll-mob - 39 pts per model, unit size 1-9
        # Fights with the Common Troll row.
        "points": 39,
        "points_per": "model",
        "unit_size": "1-9",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 1,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 6,
            "Race": "Troll",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Close Order", "Fear", "Flammable", "Motley Crew", "Regeneration (5+)", "Stupidity"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Troll Vomit", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Goblin Mob": {
        # https://tow.whfb.app/unit/goblin-mob - 3 pts per model, unit size 10+
        # Fights with the Goblin row.
        # Shooting is not simulated, so these are left out of the options: shortbows.
        "points": 3,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Boss', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
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
            "Leadership": 5,
            "Race": "Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Fear of Elves", "Horde", "Impetuous", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Close Order", "Skirmishers"],
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
    "Nasty Skulker": {
        # https://tow.whfb.app/unit/nasty-skulker - None pts per unit
        # Fights with the Nasty Skulker row.
        "points": 10,
        "points_note": "+10 points",
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 6,
            "Race": "Goblin",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2)", "Fear of Elves", "Horde", "Skulking Menace", "Strike First"],
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
    "Night Goblin Mob": {
        # https://tow.whfb.app/unit/night-goblin-mob - 3 pts per model, unit size 10+
        # Fights with the Night Goblin row.
        # Shooting is not simulated, so these are left out of the options: shortbows.
        "points": 3,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Boss', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
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
            "Leadership": 4,
            "Race": "Night Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Fear of Elves", "Hatred (Dwarfs)", "Horde", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Netters"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Thrusting Spear"],
            "armor": [],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Night Goblin Squig Herd": {
        # https://tow.whfb.app/unit/night-goblin-squig-herd - None pts per model, unit
        # size 1+/5+
        # Fights with the Squig Herder row.
        # Also has a profile for Cave Squig (M4 WS4 BS- S5 T3 W1 I4 A2 Ld3); not
        # simulated.
        "points": 3,
        "points_note": "3 points (Squig Herder), 10 points (Cave Squig)",
        "points_per": "model",
        "unit_size": "1+/5+",
        "other_profiles": [
            {'Name': 'Cave Squig', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 3},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Night Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hatred (Dwarfs)", "Immune to Psychology", "Impetuous", "Loner", "Motley Crew", "Open Order", "Skirmishers", "Squigs Go Wild", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Thrusting Spear"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Orc Mob": {
        # https://tow.whfb.app/unit/orc-mob - 5 pts per model, unit size 5+
        # Fights with the Orc Boy row.
        # Shooting is not simulated, so these are left out of the options: Warbows.
        "points": 5,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Boss', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Orc",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Choppas", "Close Order", "Furious Charge", "Ignore Goblin Panic", "Impetuous", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Big 'Uns", "Close Order", "Skirmishers", "Frenzy", "Warpaint", "Big Stabbas"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Thrusting Spear", "Throwing Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "River Troll Mob": {
        # https://tow.whfb.app/unit/river-troll-mob - 47 pts per model, unit size 1-9
        # Fights with the River Troll row.
        "points": 47,
        "points_per": "model",
        "unit_size": "1-9",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 1,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 1,
            "Wounds": 4,
            "Attacks": 3,
            "Leadership": 6,
            "Race": "Troll",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Close Order", "Fear", "Flammable", "Motley Crew", "Regeneration (5+)", "Stupidity"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Troll Vomit", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Snotling Mob": {
        # https://tow.whfb.app/unit/snotling-mob - 35 pts per model, unit size 2+
        # Fights with the Snotlings row.
        # Shooting is not simulated, so these are left out of the options: throwing
        # weapons.
        "points": 35,
        "points_per": "model",
        "unit_size": "2+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 2,
            "Toughness": 2,
            "Initiative": 3,
            "Wounds": 6,
            "Attacks": 5,
            "Leadership": 4,
            "Race": "Snotling",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Immune to Psychology", "Impetuous", "Loner", "Open Order", "Skirmishers", "Unbreakable", "Vanguard"],
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
    "Stone Troll Mob": {
        # https://tow.whfb.app/unit/stone-troll-mob - 43 pts per model, unit size 1-9
        # Fights with the Stone Troll row.
        "points": 43,
        "points_per": "model",
        "unit_size": "1-9",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 1,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 1,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Troll",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Armoured Hide (1)", "Close Order", "Fear", "Flammable", "Magic Resistance (-1)", "Motley Crew", "Regeneration (5+)", "Stupidity"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Troll Vomit", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Goblin Spider Rider Mob": {
        # https://tow.whfb.app/unit/goblin-spider-rider-mob - 12 pts per model, unit
        # size 5+
        # Fights with the Spider Rider row.
        # Also has a profile for Giant Spider (M7 WS3 BS- S3 T- W- I4 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Shortbows.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Boss', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [
            {'Name': 'Giant Spider', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Fast Cavalry", "Fear of Elves", "Impetuous", "Move Through Cover", "Open Order", "Poisoned Attacks", "Swiftstride", "Warband"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
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
    "Goblin Wolf Rider Mob": {
        # https://tow.whfb.app/unit/goblin-wolf-rider-mob - 10 pts per model, unit
        # size 5+
        # Fights with the Wolf Rider row.
        # Also has a profile for Giant Wolf (M9 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: shortbows.
        "points": 10,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Boss', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [
            {'Name': 'Giant Wolf', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Chariot Runners", "Fast Cavalry", "Fear of Elves", "Fire & Flee", "Impetuous", "Open Order", "Skirmishers", "Swiftstride", "Warband"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
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
    "Night Goblin Squig Hopper Mob": {
        # https://tow.whfb.app/unit/night-goblin-squig-hopper-mob - 12 pts per model,
        # unit size 5+
        # Fights with the Squig Hopper row.
        # Also has a profile for  Bounder Squig (M3D6 WS4 BS- S5 T- W- I4 A2 Ld-); not
        # simulated.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Boss', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [
            {'Name': ' Bounder Squig', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': None, 'Strength': 5, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Night Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hatred (Dwarfs)", "Immune to Psychology", "Impact Hits (1)", "Loner", "Open Order", "Random Movement", "Skirmishers", "Warband"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
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
    "Orc Boar Boy Mob": {
        # https://tow.whfb.app/unit/orc-boar-boy-mob - 15 pts per model, unit size 4+
        # Fights with the Boar Boy row.
        # Also has a profile for War Boar (M7 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        "points": 15,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'Boss', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'War Boar', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Orc",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (1)", "Choppas", "Close Order", "Counter Charge", "Furious Charge (Riders only)", "Ignore Goblin Panic", "Impetuous", "Swiftstride", "Tusker Charge", "Warband"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Big 'Uns", "Frenzy", "Warpaint"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Black Orc Boar Chariot": {
        # https://tow.whfb.app/unit/black-orc-boar-chariot - 130 pts per unit
        # Fights with the Black Orc Crew (x2) row, using the Chariot row's Toughness
        # and Wounds.
        # Also has a profile for Chariot (M- WS- BS- S5 T5 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for War Boars (x2) (M7 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Armour value 3+ as printed on the site.
        "points": 130,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'War Boars (x2)', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Orc",
            "Armor": "Armour Value 3+",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Choppas", "Close Order", "First Charge", "Furious Charge (Black Orc Crew only)", "Ignore Panic", "Impact Hits (D6+1)", "Tusker Charge"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Armour Value 3+"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Goblin Wolf Chariot": {
        # https://tow.whfb.app/unit/goblin-wolf-chariot - 53 pts per model, unit size
        # 1-5
        # Fights with the Goblin Crew (x3) row, using the Chariot row's Toughness and
        # Wounds.
        # Also has a profile for Chariot (M- WS- BS- S5 T4 W3 I- A- Ld-); not
        # simulated.
        # Also has a profile for Giant Wolves (x2) (M9 WS3 BS- S3 T- W- I3 A1 Ld-);
        # not simulated.
        # Armour value 5+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: shortbows.
        "points": 53,
        "points_per": "model",
        "unit_size": "1-5",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 4, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
            {'Name': 'Giant Wolves (x2)', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Goblin",
            "Armor": "Heavy Armor",
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Impact Hits (D3+1)", "Impetuous", "Open Order", "Swiftstride", "Warband"],
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
    "Orc Boar Chariot": {
        # https://tow.whfb.app/unit/orc-boar-chariot - 90 pts per unit
        # Fights with the Orc Crew (x2) row, using the Chariot row's Toughness and
        # Wounds.
        # Also has a profile for Chariot (M- WS- BS- S5 T5 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for War Boars (x2) (M7 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Armour value 4+ as printed on the site.
        "points": 90,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'War Boars (x2)', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Orc",
            "Armor": "Full Plate Armor",
            "Weapon": "Cavalry Spear",
            "Shield": False,
            "SpecialRules": ["Choppas", "Close Order", "First Charge", "Ignore Goblin Panic", "Impact Hits (D6+1)", "Impetuous", "Tusker Charge", "Warband"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
            "OptionalRules": ["Frenzy", "Warpaint"],
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
    "Snotling Pump Wagon": {
        # https://tow.whfb.app/unit/snotling-pump-wagon - 35 pts per model, unit size
        # 1-6
        # Fights with the Snotling Crew (x6) row, using the Pump Wagon row's Toughness
        # and Wounds.
        # Also has a profile for Pump Wagon (M2D6 WS- BS- S4 T4 W3 I- A- Ld-); not
        # simulated.
        # Armour value 6+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: throwing
        # weapons.
        "points": 35,
        "points_per": "model",
        "unit_size": "1-6",
        "other_profiles": [
            {'Name': 'Pump Wagon', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 4, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 2,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 1,
            "Leadership": 4,
            "Race": "Snotling",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (3, Pump Wagon Impact Hits only)", "Immune to Psychology", "Impact Hits (D3+1)", "Loner", "Open Order", "Random Movement"],
            "TroopType": "LightChariot",
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
    "Arachnarok Spider": {
        # https://tow.whfb.app/unit/arachnarok-spider - 310 pts per unit
        # Fights with the Arachnarok Spider row.
        # Also has a profile for Goblin Crew (x8) (M- WS2 BS3 S3 T- W- I3 A1 Ld7); not
        # simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: spidersilk
        # lobber.
        "points": 310,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Goblin Crew (x8)', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': 7},
        ],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 4,
            "BallisticSkill": None,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 4,
            "Wounds": 7,
            "Attacks": 6,
            "Leadership": None,
            "Race": "Goblin",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Howdah", "Immune to Psychology", "Large Target", "Move Through Cover", "Poisoned Attacks", "Stomp Attacks (D6)", "Stubborn", "Swiftstride", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Venom Surge"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Bonegrinder Giant": {
        # https://tow.whfb.app/unit/bonegrinder-giant - 300 pts per unit
        # Its Attacks are *, a dice value the engine cannot use yet; recorded as None,
        # so it makes no attacks.
        # Fights with the Bonegrinder Giant row.
        "points": 300,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 1,
            "Strength": 7,
            "Toughness": 7,
            "Initiative": 3,
            "Wounds": 8,
            "Attacks": None,
            "Leadership": 10,
            "Race": "Giant",
            "Armor": "Light Armor",
            "Weapon": "Bonegrinder Giant's Club",
            "Shield": False,
            "SpecialRules": ["Bonegrinder Giant Attacks", "Close Order", "Immune to Psychology", "Large Target", "Mercenaries", "Stomp Attacks (D6+1)", "Terror", "Timmm-berrr!", "Unbreakable"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Bonegrinder Giant's Club"],
            "armor": ["Light Armor"],
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
    "Mangler Squigs": {
        # https://tow.whfb.app/unit/mangler-squigs - 95 pts per unit
        # Its Attacks are D6, a dice value the engine cannot use yet; recorded as
        # None, so it makes no attacks.
        # Fights with the Mangler Squig row.
        "points": 95,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": None,
            "Leadership": 4,
            "Race": "Squig",
            "Armor": "Heavy Armor",
            "Weapon": "Colossal Fang-filled Gob",
            "Shield": False,
            "SpecialRules": ["Close Order", "Hatred (Dwarfs)", "Immune to Psychology", "Impact Hits (D6)", "Ker-splat", "Large Target", "Random Attacks", "Random Movement", "Spiked Ball & Chains", "Stomp Attacks (D3)", "Timmm-berrr!"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Colossal Fang-filled Gob"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Doom Diver Catapult": {
        # https://tow.whfb.app/unit/doom-diver-catapult - 95 pts per unit
        # Fights with the Goblin Crew row.
        # Also has a profile for Doom Diver Catapult (M- WS- BS- S- T5 W3 I- A- Ld-);
        # not simulated.
        # Shooting is not simulated, so these are left out of the options: stone
        # thrower.
        "points": 95,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Doom Diver Catapult', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 5, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 4,
            "Race": "Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Doom Diver", "Fear of Elves", "Skirmishers"],
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
    "Goblin Bolt Throwa": {
        # https://tow.whfb.app/unit/goblin-bolt-throwa - 45 pts per unit
        # Fights with the Goblin Crew row.
        # Also has a profile for Bolt Throwa (M- WS- BS- S- T5 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Bolt
        # thrower.
        "points": 45,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Bolt Throwa', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 5, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 4,
            "Race": "Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Skirmishers"],
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
    "Goblin Rock Lobber": {
        # https://tow.whfb.app/unit/goblin-rock-lobber - 75 pts per unit
        # Fights with the Goblin Crew row.
        # Also has a profile for Rock Lobber (M- WS- BS- S- T6 W4 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Stone
        # thrower.
        "points": 75,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Rock Lobber', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 3,
            "Leadership": 4,
            "Race": "Goblin",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fear of Elves", "Skirmishers"],
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
    "Orc Bully": {
        # https://tow.whfb.app/unit/orc-bully - None pts per unit
        # Fights with the Orc Bully row.
        "points": 10,
        "points_note": "+10 points",
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Orc",
            "Armor": None,
            "Weapon": "Whip",
            "Shield": False,
            "SpecialRules": ["Bully", "Choppas"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Whip"],
            "armor": [],
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
    'Choppas': {
        "status": 'implemented',
        "text": (
            "During a turn in which it charged, may reroll To Wound rolls of a "
            "natural 1 and improves its weapon's Armour Piercing by 1. Non- "
            "magical weapons only. "
        ),
    },
    'Furious Charge': {
        "status": 'implemented',
        "text": (
            "During a turn in which it made a charge move of 3\" or more, +1 "
            "Attack. "
        ),
    },
    'Waaagh!': {
        "status": None,
        "text": (
            "Army-wide; no effect in a duel. "
        ),
    },
    'Warband': {
        "status": None,
        "text": (
            "Army-wide; no effect in a duel. "
        ),
    },
    'Animosity': {
        "status": None,
        "text": (
            "Army-wide; no effect in a duel. "
        ),
    },
    'Mob Rule': {
        "status": None,
        "text": (
            "Army-wide; no effect in a duel. "
        ),
    },
    'Ignore Goblin Panic': {
        "status": None,
        "text": (
            "Panic; no effect in a duel. "
        ),
    },
    'Fear of Elves': {
        "status": None,
        "text": (
            "Psychology; no effect in a duel. "
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
    "Bonegrinder Giant Attacks": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/bonegrinder-giant-attacks",
        "text": (
            "Instead of attacking normally during the Combat phase, a Bonegrinder "
            "Giant must make a 'Bonegrinder Giant Attack'. To do so, nominate an "
            "enemy unit that the Bonegrinder Giant is engaged in combat with to be "
            "the target of the attack and roll on the Bonegrinder Giant Attacks "
            "table below. The Troop Type of the target unit determines whether it "
            "is a 'little thing', a 'big thing' or a 'bigger thing': - Little "
            "Things: Units whose Troop Type is regular infantry, heavy infantry, "
            "swarms, light cavalry, heavy cavalry or war beasts. - Big Things: "
            "Units whose Troop Type is monstrous infantry, monstrous cavalry, light "
            "chariot or war machine. - Bigger Things: Units whose Troop Type is "
            "heavy chariot, [...]"
        ),
    },
    "Bully": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/bully",
        "text": (
            "An Orc Bully is a special type of character that can be taken as an "
            "upgrade to accompany a war machine. During deployment, position an Orc "
            "Bully with its war machine, as you would a character that has joined a "
            "unit. Once placed, an Orc Bully cannot leave its war machine. Unless "
            "this model is fleeing, friendly war machines that are within its "
            "Command range can use this model's Leadership instead of their own."
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
    "Da Boyz": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/da-boyz",
        "text": (
            "Your army must include one Black Orc Boss for every Black Orc Mob it "
            "includes, and vice versa. In other words: - For each Black Orc Mob "
            "your army includes, it must also include one Black Orc War Boss or Big "
            "Boss. - For each Black Orc War Boss or Big Boss your army includes, it "
            "must also include one Black Orc Mob."
        ),
    },
    "Doom Diver": {
        "status": None,
        "url": "https://tow.whfb.app/weapons-of-war/doom-diver",
        "text": (
            "When shooting a Doom Diver catapult, follow the Bombardment special "
            "rule as usual. Once step 2, Scatter, is complete, you may roll a D3 "
            "and move the 3\" blast template by that many inches in any direction, "
            "representing the Doom Diver wildly flapping its arms to guide its "
            "erratic flight. Should you choose to fire a Doom Diver catapult "
            "indirectly, the skill of the crew has no bearing on the accuracy of "
            "the shot. If a 'Hit!' is rolled on the Scatter dice, use the small "
            "arrow above the Hit! symbol to determine the direction of the Scatter "
            "as usual, then move the template a number of inches equal to the roll "
            "of the Artillery dice minus D3 (to a minimum of zero), representing "
            "the efforts of the [...]"
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
    "Flammable": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/flammable",
        "text": (
            "A model with this special rule cannot make a Regeneration save against "
            "a wound caused by a Flaming attack."
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
    "Howdah": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/howdah",
        "text": (
            "To represent its howdah and crew, a behemoth with this special rule "
            "has a split profile and follows both the Split Profile (Chariots) and "
            "Firing Platform. In all other respects, this model is a behemoth."
        ),
    },
    "Ignore Panic": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ignore-panic",
        "text": (
            "This unit does not have to make a Panic test when a friendly unit that "
            "does not also have this special rule is destroyed or Breaks and flees "
            "from combat whilst within 6\" of it. Nor does this unit have to make a "
            "Panic test when it is fled through by a friendly unit that does not "
            "have this special rule."
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
    "Ker-splat": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ker-splat",
        "text": (
            "Mangler Squigs treat all difficult terrain as dangerous terrain."
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
    "Mercenaries": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/mercenaries",
        "text": (
            "Often, an army can include certain units drawn from another army list "
            "as mercenaries. Any such units included in your army gain this special "
            "rule. Mercenaries cannot use the Inspiring Presence rule of the army's "
            "General nor the \"Hold your Ground\" rule of a Battle Standard. "
            "Mercenaries cannot be joined by characters drawn from another army "
            "list."
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
    "Quell Impetuosity": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/quell-impetuosity",
        "text": (
            "Whilst within 6\" of a unit with this special rule, a friendly "
            "Impetuous unit may re-roll a failed Leadership test when testing to "
            "determine if it must declare a charge or act as normal."
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
    "Random Movement": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/random-movement",
        "text": (
            "Models with this special rule do not have a normal Movement "
            "characteristic. Instead, a dice roll is given (2D6, for example). When "
            "a model with this special rule moves, roll the dice to determine its "
            "maximum movement. Models with this special rule move during the "
            "Compulsory Moves sub-phase. They cannot march or declare a charge. "
            "They can wheel to change direction, but cannot perform any other "
            "manoeuvres. If the model is able to make contact with an enemy unit "
            "during the Compulsory Moves sub-phase or whilst pursuing, it may do so "
            "and counts as having charged. The model aligns against the enemy unit "
            "and stops moving. A unit charged in this way must Hold. If every model "
            "in a unit has this [...]"
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
    "Skulking Menace": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/skulking-menace",
        "text": (
            "Nasty Skulkers are not placed on the battlefield at the start of the "
            "game. Instead, make a note of which Goblin Mobs include Nasty "
            "Skulkers, and of how many they include. These units are referred to as "
            "'concealing' units. At the start of its first round of combat, during "
            "Step 1.1 of the Choose Combat & Fight sub-phase, a concealing unit "
            "must reveal its Nasty Skulkers – they cannot be revealed at any other "
            "time. Position each revealed Nasty Skulker as you would a character "
            "that has joined the unit. Once placed, Nasty Skulkers cannot leave "
            "their concealing unit. If a concealing unit is destroyed or flees the "
            "battlefield before its Nasty Skulkers are revealed, they are removed "
            "as casualties."
        ),
    },
    "Spiked Ball & Chains": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/spiked-ball-and-chains",
        "text": (
            "Impact Hits caused by this model have an Armour Piercing "
            "characteristic of -3."
        ),
    },
    "Squigs Go Wild": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/squigs-go-wild",
        "text": (
            "Should a Squig Herd ever Break and flees from combat, the Cave Squigs "
            "will go wild. If the Squig Herd contains five or more Cave Squigs, "
            "every unit (friend or foe) within 2D6\" of it suffers D3 Strength 5 "
            "hits, each with an AP of -1. For every additional five Cave Squigs the "
            "Squig Herd contains, apply a +1 modifier to the D3. Once these hits "
            "have been resolved, treat the unit as having been completely destroyed "
            "in combat and remove it from play."
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
    "Tusker Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/tusker-charge",
        "text": (
            "During a turn in which it charged, a War Boar's Tusks (hand weapon) "
            "have a Strength characteristic of S+1 and an Armour Piercing "
            "characteristic of -1. Note that this special rule only applies to "
            "attacks made by a War Boar, not to their rider, a chariot or its crew."
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
