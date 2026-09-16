"""Realms of Men.

Profiles from https://tow.whfb.app/army/realms-of-men, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Realms of Men"

# Other names that should resolve to this faction.
ALIASES = [
    "Realms of Men",
    "Renegades",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {

}

CHARACTERS = {
    "Renegade Captain": {
        # https://tow.whfb.app/unit/renegade-captain - 35 pts
        # Shooting is not simulated, so these are left out of the options: Brace of
        # pistols, Crossbow, Pistol, Warbow.
        "points": 35,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Rallying Cry", "Veteran", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Halberd", "Lance", "Morning Star"],
            "armor": ["Light Armor", "Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Warhorse (Realms of Men)", "Barded Warhorse"]
        }
    },
    "Renegade Prince": {
        # https://tow.whfb.app/unit/renegade-prince - 75 pts
        # Shooting is not simulated, so these are left out of the options: Brace of
        # pistols, Crossbow, Pistol, Warbow.
        "points": 75,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Rallying Cry", "Veteran", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Halberd", "Lance", "Morning Star"],
            "armor": ["Light Armor", "Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Warhorse (Realms of Men)", "Barded Warhorse"]
        }
    },
}

# Regular (non-character) units go here.
UNITS = {}


# Special rules carried by this faction's characters. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {
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
