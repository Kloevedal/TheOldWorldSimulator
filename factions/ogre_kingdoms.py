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

# Regular (non-character) units go here.
UNITS = {}


# Special rules carried by this faction's characters. `status` is how far the
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
    "Impact Hits": {
        "status": None,
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
}

PROFILES = dict(CHARACTERS, **UNITS)
