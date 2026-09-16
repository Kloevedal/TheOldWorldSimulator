"""Beastmen Brayherds.

Profiles from https://tow.whfb.app/army/beastmen-brayherds
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Beastmen Brayherds"

# Other names that should resolve to this faction.
ALIASES = [
    "Beastmen",
    "Brayherds",
    "Beastmen Brayherds",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Ghorros": "Ghorros Warhoof",
    "Kralmaw": "Kralmaw, the Prophet of Ruin",
}

CHARACTERS = {
    "Beastlord": {
        # https://tow.whfb.app/unit/beastlord - 115 pts
        # 0-1 per 1,000 pts may take Ambushers or a chariot. Chaos Mutations are not
        # modelled.
        "points": 115,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blood Rage", "Brayhorn (General only)", "Foe Render", "Gaze of the Gods", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Tuskgor Chariot", "Razorgor Chariot"]
        }
    },
    "Wargor": {
        # https://tow.whfb.app/unit/wargor - 55 pts
        "points": 55,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blood Rage", "Brayhorn (General only)", "Foe Render", "Gaze of the Gods", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Tuskgor Chariot", "Razorgor Chariot"]
        }
    },
    "Doombull": {
        # https://tow.whfb.app/unit/doombull - 210 pts
        "points": 210,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Blood Greed", "Blood Rage", "Bull-gors", "Fear", "Foe Render", "Gaze of the Gods", "Impact Hits (1)", "Mark of Chaos Undivided", "Primal Fury", "Slaughterer's Call", "Warband"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Gorebull": {
        # https://tow.whfb.app/unit/gorebull - 130 pts
        "points": 130,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Blood Greed", "Blood Rage", "Bull-gors", "Fear", "Foe Render", "Gaze of the Gods", "Impact Hits (1)", "Mark of Chaos Undivided", "Primal Fury", "Slaughterer's Call", "Warband"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Great Bray-Shaman": {
        # https://tow.whfb.app/unit/great-bray-shaman - 150 pts
        "points": 150,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Braystaff",
            "Shield": False,
            "SpecialRules": ["Gaze of the Gods", "Lore of Beasts", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "WizardLevel": 3,
            "Lores": ["Daemonology", "Dark Magic", "Elementalism"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Braystaff", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Tuskgor Chariot", "Razorgor Chariot"]
        }
    },
    "Bray-Shaman": {
        # https://tow.whfb.app/unit/bray-shaman - 65 pts
        "points": 65,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Braystaff",
            "Shield": False,
            "SpecialRules": ["Gaze of the Gods", "Lore of Beasts", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "WizardLevel": 1,
            "Lores": ["Daemonology", "Dark Magic", "Elementalism"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Braystaff", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Tuskgor Chariot", "Razorgor Chariot"]
        }
    },
    "Warhoof": {
        # https://tow.whfb.app/unit/warhoof - 75 pts
        # A centigor: the profile already includes its own four legs, so there is no
        # separate mount.
        "points": 75,
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 7,
            "Race": "Centigor",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Drunken", "Fast Cavalry", "Gaze of the Gods", "Mark of Chaos Undivided", "Move Through Cover", "Primal Fury", "Stomp Attacks (1)", "Swiftstride", "Warband"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Ghorros Warhoof": {
        # https://tow.whfb.app/unit/ghorros-warhoof - 155 pts
        # Fixed wargear; must be fielded as presented.
        "points": 155,
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Centigor",
            "Armor": None,
            "Weapon": "Mansmasher",
            "Shield": False,
            "SpecialRules": ["Drunken", "Father of Beasts", "Gaze of the Gods", "Mark of Chaos Undivided", "Move Through Cover", "Primal Fury", "Stomp Attacks (D3)", "Swiftstride", "The Sons of Ghorros", "Warband"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Mansmasher", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": ["Mansmasher", "Skull of the Unicorn Lord"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Kralmaw, the Prophet of Ruin": {
        # https://tow.whfb.app/unit/kralmaw-the-prophet-of-ruin - 245 pts
        # Fixed wargear. The Grisly Totem is his Braystaff.
        "points": 245,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Beastman",
            "Armor": None,
            "Weapon": "Grisly Totem",
            "Shield": False,
            "SpecialRules": ["Future Sight", "Gaze of the Gods", "Leering Spirit", "Lore of Beasts", "Mark of Chaos Undivided", "Primal Fury", "Warband"],
            "WizardLevel": 4,
            "Lores": ["Dark Magic", "Lore of Primal Magic"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Grisly Totem", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": ["Grisly Totem"],
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
    'Primal Fury': {
        "status": 'implemented',
        "text": (
            "On a passed Leadership test at the start of its combat, the unit "
            "may reroll To Hit rolls of a natural 1 for the rest of the Combat "
            "phase. The Leadership test is implemented; see combat_simulations. "
        ),
    },
    'Blood Rage': {
        "status": 'implemented',
        "text": (
            "If the Primal Fury Leadership test is passed on a natural double, "
            "the model also becomes Frenzied. "
        ),
    },
    'Gaze of the Gods': {
        "status": None,
        "text": (
            "A Command sub-phase roll; no command phase in a duel. "
        ),
    },
    'Impact Hits (X)': {
        "status": None,
        "text": (
            "Automatic hits at unmodified Strength on a charge of 3\" or more. "
            "Charges are not modelled. "
        ),
    },
    'Foe Render': {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
    'Warband': {
        "status": None,
        "text": (
            "Army-wide; no effect in a duel. "
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
