"""Orc & Goblin Tribes.

Profiles from https://tow.whfb.app/army/orc-and-goblin-tribes
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Orcs"

# Other names that should resolve to this faction.
ALIASES = [
    "Orc & Goblin Tribes",
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
            "Shield": None,
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
            "Shield": None,
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
            "mounts": ["War Boar", "Orc Boar Chariot"]
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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
            "Shield": None,
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

# Regular (non-character) units go here.
UNITS = {}


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
}

PROFILES = dict(CHARACTERS, **UNITS)
