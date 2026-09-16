"""Regiments of Renown.

Profiles from https://tow.whfb.app/army/regiments-of-renown, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Regiments of Renown"

# Other names that should resolve to this faction.
ALIASES = [
    "Regiments of Renown",
    "Dogs of War",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Prince Ulther": "Prince Ulther's Dragon Company",
    "Ulther": "Prince Ulther's Dragon Company",
}

CHARACTERS = {
    "Prince Ulther's Dragon Company": {
        # https://tow.whfb.app/unit/prince-ulthers-dragon-company - 115 pts
        # Also has a profile for Borri Forkbeard (champion) (M3 WS4 BS4 S3 T4 W1 I2 A2
        # Ld9); not simulated.
        # Also has a profile for Dragon Company trooper (M3 WS4 BS3 S3 T4 W1 I2 A1
        # Ld9); not simulated.
        # Shooting is not simulated, so these are left out of the options: brace of
        # pistols.
        "points": 115,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": "Light Armor",
            "Weapon": "Dragonblade",
            "Shield": True,
            "SpecialRules": ["Close Order", "Drilled", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Dragonblade"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": ["Dragonblade"],
        },
        "mount_options": {
            "mounts": []
        }
    },
}

# Regular (non-character) units go here.
UNITS = {}


# Special rules carried by this faction's characters. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {
    "Close Order": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/close-order",
        "text": (
            "A unit consisting of models with this special rule may adopt a Close "
            "Order formation."
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
    "Gromril Weapons": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/gromril-weapons",
        "text": (
            "A hand weapon carried by a model with this special rule has an Armour "
            "Piercing characteristic of -1. Note that this special rule only "
            "applies to a single, ordinary hand weapon. If the model is using two "
            "hand weapons or any other sort of weapon, or if their hand weapon is "
            "inscribed with any Weapon runes, this special rule ceases to apply."
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
    "Resolute": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/resolute",
        "text": (
            "Models with this special rule suffer a -1 modifier to the result of "
            "any Flee roll or Pursuit roll they make (to a minimum of 1). Note that "
            "this modifier does not apply to Chaos Dwarf mounted characters."
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
}

PROFILES = dict(CHARACTERS, **UNITS)
