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
            "armor": ["Full Plate Armor", "Plate Armor"],
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
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (1)", "Breath of Change", "Close Order", "Fly (10)", "Large Target", "Mark of Tzeentch", "Regeneration (5+)", "Spirit of Galrauch", "Stomp Attacks (D6)", "Swiftstride", "Terror", "Two-headed Dragon"],
            "WizardLevel": 4,
            "Lores": ["Dark Magic"],
            "TroopType": "Behemoth",
            "UnitCategory": "NamedCharacter",
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
}

# Regular (non-character) units go here.
UNITS = {}


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
}

PROFILES = dict(CHARACTERS, **UNITS)
