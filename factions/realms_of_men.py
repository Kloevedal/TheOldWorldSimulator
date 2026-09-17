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

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Sellsword Infantry": {
        # https://tow.whfb.app/unit/sellsword-infantry - 4 pts per model, unit size 5+
        # Fights with the Sellsword row.
        # Shooting is not simulated, so these are left out of the options: Crossbows,
        # Handguns.
        "points": 4,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Officer', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
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
            "Leadership": 5,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Detachment", "Horde", "Regimental Unit", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Thrusting Spear", "Halberd", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Veteran Sellswords": {
        # https://tow.whfb.app/unit/veteran-sellswords - 5 pts per model, unit size 5+
        # Fights with the Veteran Sellsword row.
        # Also has a profile for Veteran Officer (M4 WS4 BS3 S3 T3 W1 I3 A2 Ld6); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Crossbows,
        # Handguns.
        "points": 5,
        "points_per": "model",
        "unit_size": "5+",
        "other_profiles": [
            {'Name': 'Veteran Officer', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Detachment", "Horde", "Regimental Unit", "Warband", "Veteran"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Thrusting Spear", "Halberd", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Freeblade Knights": {
        # https://tow.whfb.app/unit/freeblade-knights - 18 pts per model, unit size 5+
        # Fights with the Freeblade Knight row.
        # Also has a profile for Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Also has a profile for Barded Warhorse (M7 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        "points": 18,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Commander', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
            {'Name': 'Barded Warhorse', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Counter Charge", "First Charge", "Swiftstride"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Lance", "Great Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Hireling Outriders": {
        # https://tow.whfb.app/unit/hireling-outriders - 11 pts per model, unit size
        # 5+
        # Fights with the Hireling Outrider row.
        # Also has a profile for Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # pistols, Pistols, Shortbows.
        "points": 11,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Captain', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Human",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fast Cavalry", "Fire & Flee", "Open Order", "Skirmishers", "Swiftstride"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Feigned Flight", "Reserve Move", "Vanguard"],
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
    "Veteran Freeblades": {
        # https://tow.whfb.app/unit/veteran-freeblades - 22 pts per model, unit size
        # 5+
        # Fights with the Veteran Freeblade row.
        # Also has a profile for Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Also has a profile for Barded Warhorse (M7 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        "points": 22,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Commander', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
            {'Name': 'Barded Warhorse', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Counter Charge", "First Charge", "Swiftstride", "Veteran"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Lance", "Great Weapon"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Border Princes Mortar": {
        # https://tow.whfb.app/unit/border-princes-mortar - 90 pts per unit
        # Fights with the Gun Crew row.
        # Also has a profile for Mortar (M- WS- BS- S- T7 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Mortar.
        "points": 90,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Mortar', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 7, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "Race": "Human",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Levies", "Skirmishers"],
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
    "Border Princes Organ Gun": {
        # https://tow.whfb.app/unit/border-princes-organ-gun - 125 pts per unit
        # Fights with the Gun Crew row.
        # Also has a profile for Organ Gun (M- WS- BS- S- T7 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Organ gun.
        "points": 125,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Organ Gun', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 7, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "Race": "Human",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Levies", "Skirmishers"],
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
    "Fast Cavalry": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fast-cavalry",
        "text": (
            "If all of the models (including characters) within a unit arrayed in "
            "an Open Order formation have this special rule, the unit may perform "
            "its Quick Turn even if it marched."
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
    "Horde": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/horde",
        "text": (
            "A unit with this special rule may increase the maximum Rank Bonus it "
            "can claim (as determined by its troop type) by one."
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
    "Regimental Unit": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/regimental-unit",
        "text": (
            "A unit with this special rule can be accompanied by detachment."
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
