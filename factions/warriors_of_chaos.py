"""Warriors of Chaos.

Profiles from https://tow.whfb.app/army/warriors-of-chaos
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Warriors of Chaos"

# Other names that should resolve to this faction.
ALIASES = [
    "WoC",
    "Chaos",
    "Chaos Warriors",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Frydaal": "Frydaal The Chainmaker",
    "Chainmaker": "Frydaal The Chainmaker",
}

CHARACTERS = {
    "Chaos Lord": {
        # https://tow.whfb.app/unit/chaos-lord - 195 pts
        "points": 195,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 7,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 6,
            "Wounds": 4,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Chaos Warrior",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Chaos Armour (5+)", "Ensorcelled Weapons", "Gaze of the Gods", "Mark of Chaos Undivided", "Rallying Cry"],
            "MarksOfChaos": ["Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail", "Great Weapon", "Halberd", "Lance"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Chaos Steed", "Daemonic Mount", "Chaos Chariot", "Gorebeast Chariot", "Manticore (Warriors of Chaos)", "Chaos Dragon"]
        }
    },
    "Exalted Champion": {
        # https://tow.whfb.app/unit/exalted-champion - 125 pts
        "points": 125,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Chaos Armour (5+)", "Ensorcelled Weapons", "Gaze of the Gods", "Mark of Chaos Undivided", "Rallying Cry"],
            "MarksOfChaos": ["Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail", "Great Weapon", "Halberd", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Chaos Steed", "Daemonic Mount", "Chaos Chariot", "Gorebeast Chariot", "Manticore (Warriors of Chaos)", "Chaos Dragon"]
        }
    },
    "Aspiring Champion": {
        # https://tow.whfb.app/unit/aspiring-champion - 70 pts
        "points": 70,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Chaos Armour (5+)", "Ensorcelled Weapons", "Gaze of the Gods", "Mark of Chaos Undivided", "Rallying Cry"],
            "MarksOfChaos": ["Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail", "Great Weapon", "Halberd", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Chaos Steed", "Daemonic Mount", "Chaos Chariot", "Gorebeast Chariot"]
        }
    },
    "Sorcerer Lord": {
        # https://tow.whfb.app/unit/sorcerer-lord - 195 pts
        "points": 195,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Chaos Armour (5+)", "Ensorcelled Weapons", "Gaze of the Gods", "Lore of Chaos", "Mark of Chaos Undivided"],
            "MarksOfChaos": ["Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Lore of the Shadowlands"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Chaos Steed", "Daemonic Mount", "Chaos Chariot", "Manticore (Warriors of Chaos)", "Chaos Dragon"]
        }
    },
    "Exalted Sorcerer": {
        # https://tow.whfb.app/unit/exalted-sorcerer - 90 pts
        # May not take the Mark of Khorne.
        "points": 90,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Chaos Armour (5+)", "Ensorcelled Weapons", "Gaze of the Gods", "Lore of Chaos", "Mark of Chaos Undivided"],
            "MarksOfChaos": ["Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Lore of the Shadowlands"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Chaos Steed", "Daemonic Mount", "Chaos Chariot"]
        }
    },
    "Marauder Tribe Chieftain": {
        # https://tow.whfb.app/unit/marauder-tribe-chieftain - 65 pts
        # May also take throwing axes or javelins; shooting is not simulated.
        "points": 65,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Chaos Marauder",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ambushers", "Chaos Armour (6+)", "Gaze of the Gods", "Mark of Chaos Undivided", "Rallying Cry", "Warband"],
            "MarksOfChaos": ["Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Flail", "Great Weapon", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Warhorse (Warriors of Chaos)"]
        }
    },
    "Daemon Prince": {
        # https://tow.whfb.app/unit/daemon-prince-warriors-of-chaos - 215 pts
        # May be a Level 1-4 Wizard unless bearing the Mark of Khorne, and may
        # buy Fly (9); neither is modelled.
        "points": 215,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 7,
            "BallisticSkill": 5,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 7,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Daemon",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Chaos Armour (4+)", "Ensorcelled Weapons", "Fear", "Gaze of the Gods", "Immune to Psychology", "Lore of Chaos", "Mark of Chaos Undivided", "Regeneration (5+)", "Stomp Attacks (D3+1)", "Unbreakable", "Unstable", "Warp-spawned"],
            "MarksOfChaos": ["Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
            "WizardLevel": 0,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Chaos Warhound Handler": {
        # https://tow.whfb.app/unit/chaos-warhound-handler - 15 pts
        # Costs +15 points as an upgrade. Rides a Chaos Warhound (M7 WS4 S3 T3
        # W1 I3 A1) with Armoured Hide (1), Poisoned Attacks and Swiftstride;
        # the mount is not simulated.
        "points": 15,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Handler", "Loner", "Mark of Chaos Undivided", "Move Through Cover", "Vanguard"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Whip"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Chaos Warhound"]
        }
    },
    "Frydaal The Chainmaker": {
        # https://tow.whfb.app/unit/frydaal-the-chainmaker - 235 pts
        # An Exalted Champion with fixed wargear; must be fielded as presented.
        "points": 235,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Chaos Warrior",
            "Armor": "Full Plate Armor",
            "Weapon": "Storm's Wrath",
            "Shield": True,
            "SpecialRules": ["Ambushers", "Chainmaker", "Chaos Armour (5+)", "Commander & Captain", "Ensorcelled Weapons", "Gaze of the Gods", "Impact Hits (1)", "Mark of Chaos Undivided", "Peerless Raider", "Rallying Cry"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Storm's Wrath", "Hand Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": ["Storm's Wrath"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Galrauch": {
        # https://tow.whfb.app/unit/galrauch - 465 pts
        # Draconic scales count as full plate armour; wicked claws as a hand
        # weapon. His breath attacks are not simulated.
        "points": 465,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 4,
            "Wounds": 6,
            "Attacks": 6,
            "Leadership": 9,
            "Race": "Chaos Dragon",
            "Armor": "Full Plate Armor",
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (1)", "Breath of Change", "Close Order", "Fly (10)", "Large Target", "Mark of Tzeentch", "Regeneration (5+)", "Spirit of Galrauch", "Stomp Attacks (D6)", "Swiftstride", "Terror", "Two-headed Dragon"],
            "WizardLevel": 4,
            "Lores": ["Dark Magic"],
            "TroopType": "Behemoth",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Wicked Claws"],
            "armor": ["Full Plate Armor"],
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
    "Chaos Marauders": {
        # https://tow.whfb.app/unit/chaos-marauders - 6 pts per model, unit size 5+
        # Fights with the Chaos Marauder row.
        "points": 6,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Marauder Headman', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Chaos Marauder",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Mark of Chaos Undivided", "Shieldwall", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Chaotic Cult", "Cult of the Bloodied Hound", "Cult of the Carrion Crow", "Cult of the Slithering Serpent", "Cult of the Fell Raptor", "Chaotic Trait", "Ambushers", "Close Order", "Skirmishers", "Close Order", "Open Order"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Flail"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Chaos Ogres": {
        # https://tow.whfb.app/unit/chaos-ogres - 31 pts per model, unit size 3-15
        # Fights with the Chaos Ogre row.
        "points": 31,
        "points_per": "model",
        "unit_size": "3-15",
        "champion": {'Name': 'Champion', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': 2, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 3, 'Attacks': 4, 'Leadership': 7},
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
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Close Order", "Fear", "Impact Hits (1)", "Mark of Chaos Undivided", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Mark of Chaos Undivided", "Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Chaos Spawn": {
        # https://tow.whfb.app/unit/chaos-spawn - 50 pts per model, unit size 1-4
        # Its Attacks are D6, a dice value the engine cannot use yet; recorded as
        # None, so it makes no attacks.
        # Fights with the Chaos Spawn row.
        "points": 50,
        "points_per": "model",
        "unit_size": "1-4",
        "other_profiles": [],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": None,
            "Leadership": 10,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2)", "Fear", "Immune to Psychology", "Open Order", "Random Attacks", "Random Movement", "Stomp Attacks (1)", "Unbreakable"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Spawn of Khorne", "Spawn of Nurgle", "Spawn of Slaanesh", "Spawn of Tzeentch"],
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
    "Chaos Trolls": {
        # https://tow.whfb.app/unit/chaos-trolls - 39 pts per model, unit size 1-9
        # Fights with the Chaos Troll row.
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
    "Chaos Warriors": {
        # https://tow.whfb.app/unit/chaos-warriors - 13 pts per model, unit size 5+
        # Fights with the Chaos Warrior row.
        "points": 13,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Champion', 'Movement': 4, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Chaos Armour (6+)", "Close Order", "Ensorcelled Weapons", "Furious Charge", "Mark of Chaos Undivided"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Mark of Chaos Undivided", "Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch", "Chaotic Trait"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Chosen Chaos Warriors": {
        # https://tow.whfb.app/unit/chosen-chaos-warriors - 17 pts per model, unit
        # size 5+
        # Fights with the Chosen Chaos Warrior row.
        "points": 17,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Champion', 'Movement': 4, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 1, 'Attacks': 3, 'Leadership': 9},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Chaos Armour (6+)", "Close Order", "Ensorcelled Weapons", "Furious Charge", "Mark of Chaos Undivided", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Mark of Chaos Undivided", "Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch", "Drilled", "Chaotic Traits"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Forsaken": {
        # https://tow.whfb.app/unit/forsaken - 19 pts per model, unit size 5+
        # Its Attacks are D3, a dice value the engine cannot use yet; recorded as
        # None, so it makes no attacks.
        # Fights with the Forsaken row.
        "points": 19,
        "points_per": "model",
        "unit_size": "5+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": None,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Chaos Armour (5+)", "Ensorcelled Weapons", "Furious Charge", "Immune to Psychology", "Impetuous", "Loner", "Open Order", "Rampant Mutation", "Random Attacks", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Forsaken by Khorne", "Forsaken by Nurgle", "Forsaken by Slaanesh", "Forsaken by Tzeentch"],
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
    "Marauder Tribe Berserkers": {
        # https://tow.whfb.app/unit/marauder-tribe-berserkers - 8 pts per model, unit
        # size 5+
        # Fights with the Marauder Tribe Berserker row.
        # Shooting is not simulated, so these are left out of the options: throwing
        # axes.
        "points": 8,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Headtaker', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Chaos Marauder",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Frenzy", "Mark of Chaos Undivided", "Move Through Cover", "Open Order", "Relentless Warriors", "Ward6 (non-magical)", "Skirmishers", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Chaotic Trait", "Ambushers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Skin Wolves": {
        # https://tow.whfb.app/unit/skin-wolves - 45 pts per model, unit size 2+
        # Fights with the Skin Wolf Jarl row.
        "points": 45,
        "points_per": "model",
        "unit_size": "2+",
        "champion": {'Name': 'Skin Wolf', 'Movement': 7, 'WeaponSkill': 5, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 3, 'Attacks': 3, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 5,
            "BallisticSkill": None,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 7,
            "Race": "Chaos Marauder",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blood Rage", "Fear", "Mark of Chaos Undivided", "Open Order", "Primal Fury", "Regeneration (5+)", "Skirmishers", "Swiftstride", "Warped Form"],
            "TroopType": "MonstrousInfantry",
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
    "Chaos Knights": {
        # https://tow.whfb.app/unit/chaos-knights - 27 pts per model, unit size 4+
        # Fights with the Chaos Knight row.
        # Also has a profile for Chaos Steed (M7 WS3 BS- S4 T- W- I3 A1 Ld-); not
        # simulated.
        "points": 27,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'Champion', 'Movement': None, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Chaos Steed', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Chaos Armour (6+)", "Close Order", "Counter Charge", "Ensorcelled Weapons", "First Charge", "Mark of Chaos Undivided", "Swiftstride"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Mark of Chaos Undivided", "Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch", "Chaotic Trait"],
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
    "Chaos Warhounds": {
        # https://tow.whfb.app/unit/chaos-warhounds - 6 pts per model, unit size 5+
        # Fights with the Chaos Warhound row.
        "points": 6,
        "points_per": "model",
        "unit_size": "5+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Chaos Warrior",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Loner", "Move Through Cover", "Open Order", "Swiftstride"],
            "TroopType": "WarBeast",
            "UnitCategory": "Unit",
            "OptionalRules": ["Armoured Hide (1)", "Poisoned Attacks", "Vanguard"],
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
    "Chosen Chaos Knights": {
        # https://tow.whfb.app/unit/chosen-chaos-knights - 36 pts per model, unit size
        # 3+
        # Fights with the Chosen Chaos Knight row.
        # Also has a profile for Chaos Steed (M7 WS3 BS- S4 T- W- I3 A1 Ld-); not
        # simulated.
        "points": 36,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Champion', 'Movement': None, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 1, 'Attacks': 3, 'Leadership': 9},
        "other_profiles": [
            {'Name': 'Chaos Steed', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Chaos Armour (6+)", "Close Order", "Counter Charge", "Ensorcelled Weapons", "First Charge", "Mark of Chaos Undivided", "Stubborn", "Swiftstride"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Mark of Chaos Undivided", "Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch", "Chaotic Traits"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Lance"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Marauder Horsemen": {
        # https://tow.whfb.app/unit/marauder-horsemen - 12 pts per model, unit size 5+
        # Fights with the Marauder Horseman row.
        # Also has a profile for Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: throwing
        # axes.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Marauder Horsemaster', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
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
            "Leadership": 6,
            "Race": "Chaos Marauder",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Fast Cavalry", "Fire & Flee", "Mark of Chaos Undivided", "Open Order", "Swiftstride", "Warband"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Chaotic Cult", "Cult of the Bloodied Hound", "Cult of the Carrion Crow", "Cult of the Slithering Serpent", "Cult of the Fell Raptor", "Chaotic Trait", "Ambushers", "Close Order", "Skirmishers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear", "Throwing Spear", "Flail"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Marauder Tribe Huscarls": {
        # https://tow.whfb.app/unit/marauder-tribe-huscarls - 18 pts per model, unit
        # size 5+
        # Fights with the Marauder Tribe Huscarl row.
        # Also has a profile for Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Javelins,
        # Throwing axes.
        "points": 18,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'First Sword', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Chaos Marauder",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Counter Charge", "Furious Charge", "Mark of Chaos Undivided", "Swiftstride", "Warband"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Mark of Chaos Undivided", "Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch", "Drilled", "Chaotic Traits"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear", "Flail"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Chaos Chariot": {
        # https://tow.whfb.app/unit/chaos-chariot - 110 pts per unit
        # Fights with the Chaos Charioteer (x2) row, using the Chariot row's Toughness
        # and Wounds.
        # Also has a profile for Chariot (M- WS- BS- S5 T5 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Chaos Steed (x2) (M7 WS3 BS- S4 T- W- I3 A1 Ld-); not
        # simulated.
        # Armour value 3+ as printed on the site.
        "points": 110,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Chaos Steed (x2)', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Armour Value 3+",
            "Weapon": "Halberd",
            "Shield": False,
            "SpecialRules": ["Close Order", "Ensorcelled Weapons", "First Charge", "Impact Hits (D6+1)", "Mark of Chaos Undivided"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
            "OptionalRules": ["Mark of Chaos Undivided", "Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd"],
            "armor": ["Armour Value 3+"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Chosen Chaos Chariot": {
        # https://tow.whfb.app/unit/chosen-chaos-chariot - 140 pts per unit
        # Fights with the Chosen Charioteer (x2) row, using the Chariot row's
        # Toughness and Wounds.
        # Also has a profile for Chariot (M- WS- BS- S5 T5 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Chaos Steed (x2) (M7 WS3 BS- S4 T- W- I3 A1 Ld-); not
        # simulated.
        # Armour value 3+ as printed on the site.
        "points": 140,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Chaos Steed (x2)', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Chaos Warrior",
            "Armor": "Armour Value 3+",
            "Weapon": "Halberd",
            "Shield": False,
            "SpecialRules": ["Close Order", "Counter Charge", "Ensorcelled Weapons", "First Charge", "Impact Hits (D6+1, Chariot only)", "Mark of Chaos Undivided"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
            "OptionalRules": ["Mark of Chaos Undivided", "Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd"],
            "armor": ["Armour Value 3+"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Gorebeast Chariot": {
        # https://tow.whfb.app/unit/gorebeast-chariot - 135 pts per unit
        # Fights with the Chaos Charioteer (x2) row, using the Chariot row's Toughness
        # and Wounds.
        # Also has a profile for Chariot (M- WS- BS- S5 T5 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Gorebeast (x1) (M6 WS4 BS- S5 T- W- I2 A3 Ld-); not
        # simulated.
        # Armour value 3+ as printed on the site.
        "points": 135,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Gorebeast (x1)', 'Movement': 6, 'WeaponSkill': 4, 'BallisticSkill': None, 'Strength': 5, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 3, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Armour Value 3+",
            "Weapon": "Halberd",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1, Gorebeast only)", "Close Order", "Ensorcelled Weapons", "First Charge", "Impact Hits (D6+2)", "Killing Blow (Gorebeast only)", "Mark of Chaos Undivided"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
            "OptionalRules": ["Mark of Chaos Undivided", "Mark of Khorne", "Mark of Nurgle", "Mark of Slaanesh", "Mark of Tzeentch"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd"],
            "armor": ["Armour Value 3+"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Chimera": {
        # https://tow.whfb.app/unit/chimera - 170 pts per unit
        # Fights with the Chimera row.
        # Shooting is not simulated, so these are left out of the options: flaming
        # breath.
        "points": 170,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 5,
            "Attacks": 6,
            "Leadership": 5,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2, claws and fangs only)", "Close Order", "Fly (10)", "Large Target", "Stomp Attacks (D3)", "Swiftstride", "Terror"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Fiend Tail"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Gigantic Spawn of Chaos": {
        # https://tow.whfb.app/unit/gigantic-spawn-of-chaos - 145 pts per unit
        # Its Attacks are D6+1, a dice value the engine cannot use yet; recorded as
        # None, so it makes no attacks.
        # Fights with the Gigantic Spawn row.
        "points": 145,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 3,
            "Wounds": 6,
            "Attacks": None,
            "Leadership": 10,
            "Race": "Chaos Warrior",
            "Armor": "Heavy Armor",
            "Weapon": "Slashing Talons",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2)", "Close Order", "First Charge", "Immune to Psychology", "Large Target", "Random Attacks", "Random Movement", "Stomp Attacks (D6)", "Terror", "Timmm-berrr!", "Unbreakable"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
            "OptionalRules": ["Gigantic Spawn of Khorne", "Gigantic Spawn of Nurgle", "Gigantic Spawn of Slaanesh", "Gigantic Spawn of Tzeentch"],
        },
        "equipment_options": {
            "weapons": ["Slashing Talons", "Gnashing Maws"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Hellcannon": {
        # https://tow.whfb.app/unit/hellcannon - 215 pts per unit
        # Fights with the Hellcannon row.
        # Also has a profile for Chaos Dwarf Handlers (x3) (M3 WS4 BS- S3 T- W- I2 A1
        # Ld9); not simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: Doomfire.
        "points": 215,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Chaos Dwarf Handlers (x3)', 'Movement': 3, 'WeaponSkill': 4, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 1, 'Leadership': 9},
        ],
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 1,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 4,
            "Race": "Chaos Warrior",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Caged Fury", "Close Order", "Ensorcelled Weapons", "Immune to Psychology", "Impact Hits (D6)", "Large Target", "Monster Handlers", "Regeneration (6+)", "Terror", "Unbreakable", "Warp-spawned"],
            "TroopType": "Behemoth",
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
    "Warpfire Dragon": {
        # https://tow.whfb.app/unit/warpfire-dragon - 375 pts per unit
        # Fights with the Warpfire Dragon row.
        # Shooting is not simulated, so these are left out of the options: Warpfire
        # Blast.
        "points": 375,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 0,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 3,
            "Wounds": 6,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Chaos Warrior",
            "Armor": "Full Plate Armor",
            "Weapon": "Wicked Claws",
            "Shield": False,
            "SpecialRules": ["Close Order", "Explosive Demise", "Fire & Chaos", "Fly (10)", "Large Target", "Lore of Chaos", "Magical Attacks", "Magic Resistance (-2)", "Mark of Chaos Undivided", "Regeneration (5+)", "Stomp Attacks (D6)", "Swiftstride", "Terror", "Warpfire Aura"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
            "WizardLevel": 0,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic"],
        },
        "equipment_options": {
            "weapons": ["Wicked Claws"],
            "armor": ["Full Plate Armor"],
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
    'Chaos Armour (X+)': {
        "status": 'implemented',
        "text": (
            "A Ward save against any wounds suffered, at the value in brackets. "
            "A Wizard with this rule may wear armour without penalty. "
        ),
    },
    'Ensorcelled Weapons': {
        "status": 'implemented',
        "text": (
            "A hand weapon carried by this model has Magical Attacks and an "
            "Armour Piercing of -1. A single, non-magical hand weapon only. "
        ),
    },
    'Gaze of the Gods': {
        "status": None,
        "text": (
            "A Command sub-phase D6 roll granting a random boon. There is no "
            "command phase in a duel. "
        ),
    },
    'Marks of Chaos': {
        "status": None,
        "text": (
            "Undivided, Khorne, Nurgle, Slaanesh or Tzeentch; their effects are "
            "not modelled. "
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
    "Blood Rage": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/blood-rage",
        "text": (
            "If, when testing to see if it becomes subject to Primal Fury, this "
            "unit passes its Leadership test with any roll of a natural double, it "
            "will also become Frenzied. A unit with this special rule may become "
            "Frenzied in this way even if it has lost Frenzy earlier in the game."
        ),
    },
    "Caged Fury": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/caged-fury",
        "text": (
            "During the Start of Turn sub-phase of each of your turns, make a "
            "Leadership test for this model. If this test is failed, roll "
            "immediately on the Hellcannon Misfire table."
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
    "Explosive Demise": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/explosive-demise",
        "text": (
            "When a Warpfire Dragon loses its last Wound, before the model is "
            "removed from play, every unit (friend or foe) within 6\" of it suffers "
            "D6 Strength 5 hits, each with an AP of -2."
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
    "Fire & Chaos": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fire-and-chaos",
        "text": (
            "Warpfire Dragons have a 5+ Ward save against any wounds suffered that "
            "were caused by an attack that has either the Magical Attacks or "
            "Flaming Attacks special rule."
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
    "Handler": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/handler",
        "text": (
            "A Chaos Warhound Handler is a special type of character that can be "
            "taken as an upgrade to accompany a unit of Chaos Warhounds. During "
            "deployment, position a Chaos Warhound Handler with its unit of Chaos "
            "Warhounds, as you would a character that has joined a unit. Once "
            "placed, a Chaos Warhound Handler cannot leave its unit. Unless this "
            "model is fleeing, friendly units of Chaos Warhounds that are within "
            "its Command range can use this model's Leadership instead of their "
            "own."
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
    "Killing Blow": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/killing-blow",
        "text": (
            "If a model with this special rule rolls a natural 6 when making a roll "
            "To Wound for an attack made in combat, it has struck a 'Killing Blow'. "
            "Enemy models whose troop type is infantry or cavalry are not permitted "
            "an armour or Regeneration save against a Killing Blow (Ward saves can "
            "be attempted as normal). If an enemy model whose troop type is "
            "infantry or cavalry suffers an unsaved wound from a Killing Blow, it "
            "loses all of its remaining Wounds. Note that if an attack wounds "
            "automatically, this special rule cannot be used."
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
    "Lore of Chaos": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-chaos",
        "text": (
            "Chaos Sorcerers are gifted understanding of dark magic by the Ruinous "
            "Powers which they serve. Spells creep into their minds through dreams, "
            "visions, and the whispers of the Dark Gods themselves. A Wizard with "
            "the 'Lore of Chaos' special rule may discard one of their randomly "
            "generated spells as normal. When they do so, they may select instead "
            "either the signature spell of their chosen Lore of Magic, or the spell "
            "that corresponds to their Mark of Chaos listed below. Lore of Chaos "
            "Lore"
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
    "Mark of Chaos Undivided": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/mark-of-chaos-undivided",
        "text": (
            "Models with the Mark of Chaos Undivided can re-roll any failed Fear, "
            "Panic or Terror test."
        ),
    },
    "Monster Handlers": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/monster-handlers",
        "text": (
            "A monster with this special rule is accompanied by one or more models "
            "representing its handlers. During deployment, position these models "
            "anywhere that is adjacent to, and in base contact with, the monster. "
            "If the handlers are found to be blocking movement or line of sight, "
            "simply move them aside. In combat, each handler adds its attacks to "
            "those of the monster. If the monster suffers an unsaved wound, roll a "
            "D6. On a roll of 1-4 the monster loses a Wound, but on a roll of 5+ "
            "one of the handlers is removed instead. If the monster is removed from "
            "play, so are its handlers."
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
    "Primal Fury": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/primal-fury",
        "text": (
            "When this unit's combat is chosen during Step 1.1 of any Choose & "
            "Fight Combat sub-phase, it must make a Leadership test. If this test "
            "is passed, the unit becomes subject to 'Primal Fury' until the end of "
            "this Combat phase. A unit subject to Primal Fury may re-roll any rolls "
            "To Hit of a natural 1."
        ),
    },
    "Rampant Mutation": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/rampant-mutation",
        "text": (
            "When this unit's combat is chosen during Step 1.1 of any Choose & "
            "Fight Combat sub-phase, roll on the table below to determine which "
            "mutation it is currently afflicted with: D6 | Result 1-2 | Venomous "
            "Fangs: With jaws distended, the Forsaken sink venomous fangs into "
            "their foes. Until the end of this Combat phase, the unit gains the "
            "Poisoned Attacks special rule. 3-4 | Razor Talons: With talons like "
            "the blades of daggers, the Forsaken slash at their enemies. Until the "
            "end of this Combat phase, all of the unit's attacks have an Armour "
            "Piercing characteristic of -2. 5-6 | Decapitating Claws: With "
            "gigantic, snapping claws, the Forsaken dismember the enemy. Until the "
            "end of this Combat phase, [...]"
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
    "Relentless Warriors": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/relentless-warriors",
        "text": (
            "A model with this special rule has a 6+ Ward save against any wounds "
            "suffered that were caused by a non-magical enemy attack."
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
    "Warp-spawned": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/warp-spawned",
        "text": (
            "A model with this special rule cannot make a Regeneration save against "
            "a wound caused by a Magical attack. In addition, characters that are "
            "not Warp-spawned cannot join units that are, and vice versa."
        ),
    },
    "Warped Form": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/warped-form",
        "text": (
            "When this unit's combat is chosen during Step 1.1 of any Choose & "
            "Fight combat sub-phase, choose one of the following Transfigurations. "
            "Each Transfiguration lasts until your next Start of Turn sub-phase: - "
            "Enlarged Claws: The Armour Piercing characteristics of this unit's "
            "weapons is improved by 1. Additionally, they gain the Armour Bane (2) "
            "special rule. - Barbed Protrusions: The unit gains the Extra Attacks "
            "(+1) special rule. - Toughened Flesh: The unit improves its Toughness "
            "characteristic by 1 and its armour value by 2."
        ),
    },
    "Warpfire Aura": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/warpfire-aura",
        "text": (
            "Other models (both friend and foe) are not permitted a Ward save "
            "whilst within 3\" of this model."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
