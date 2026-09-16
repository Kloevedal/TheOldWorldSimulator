"""Dark Elves.

Profiles from https://tow.whfb.app/army/dark-elves
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Dark Elves"

# Other names that should resolve to this faction.
ALIASES = [
    "Druchii",
    "Dark Elf",
    "Dark Elves",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Dark Elf Dreadlord": "Dreadlord",
    "Dark Elf Master": "Master",
    "Assassin": "Khainite Assassin",
}

CHARACTERS = {
    "Dreadlord": {
        # https://tow.whfb.app/unit/dark-elf-dreadlord - 130 pts
        # Hatred and Strike First do not apply to his mount. Repeater crossbows and
        # handbows are shooting, which is not simulated.
        "points": 130,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 7,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Eternal Hatred", "Hatred (High Elves)", "Murderous", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd", "Lance"],
            "armor": ["Light Armor", "Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Dark Steed", "Cold One (Dark Elves)", "Cold One Chariot", "Black Dragon", "Manticore (Dark Elves)"]
        }
    },
    "Master": {
        # https://tow.whfb.app/unit/dark-elf-master - 70 pts
        "points": 70,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 6,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Eternal Hatred", "Hatred (High Elves)", "Murderous", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd", "Lance"],
            "armor": ["Light Armor", "Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Dark Steed", "Cold One (Dark Elves)", "Cold One Chariot"]
        }
    },
    "Supreme Sorceress": {
        # https://tow.whfb.app/unit/supreme-sorceress - 150 pts
        "points": 150,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Eternal Hatred", "Hatred (High Elves)", "Hekarti's Blessing", "Lore of Naggaroth", "Murderous"],
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Elementalism", "Illusion"],
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
            "mounts": ["Dark Steed", "Cold One (Dark Elves)", "Dark Pegasus", "Black Dragon"]
        }
    },
    "Sorceress": {
        # https://tow.whfb.app/unit/sorceress - 75 pts
        "points": 75,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Eternal Hatred", "Hatred (High Elves)", "Hekarti's Blessing", "Lore of Naggaroth", "Murderous"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Elementalism", "Illusion"],
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
            "mounts": ["Dark Steed", "Cold One (Dark Elves)", "Dark Pegasus"]
        }
    },
    "Khainite Assassin": {
        # https://tow.whfb.app/unit/khainite-assassin - 80 pts
        # Carries throwing weapons as standard, and may take a forbidden poison;
        # neither is simulated.
        "points": 80,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 8,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 7,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Eternal Hatred", "Hatred (all enemies)", "Hidden", "Immune to Psychology", "Murderous", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
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
    "Death Hag": {
        # https://tow.whfb.app/unit/death-hag - 70 pts
        # Fights with two hand weapons as standard. Gifts of Khaine are not
        # modelled.
        "points": 70,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 6,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 7,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Dark Elf",
            "Armor": None,
            "Weapon": "Two Hand Weapons",
            "Shield": False,
            "SpecialRules": ["Eternal Hatred", "Frenzy", "Hatred (all enemies)", "Loner", "Murderous", "Poisoned Attacks", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Two Hand Weapons", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Cauldron of Blood"]
        }
    },
    "High Beastmaster": {
        # https://tow.whfb.app/unit/high-beastmaster - 75 pts
        # Movement is '-' on the profile: a mount is compulsory and supplies it.
        # Mounts are not simulated, so he fights on foot here.
        "points": 75,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 7,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Dark Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Eternal Hatred", "Goad Beast", "Hatred (High Elves)", "Murderous", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Whip", "Cavalry Spear"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Scourgerunner Chariot", "Manticore (Dark Elves)"]
        }
    },
}

# Regular (non-character) units go here.
UNITS = {}


# Army-wide special rules for this faction. `status` is how far the engine
# goes with each: "implemented", "partial", or None for recorded only.
FACTION_RULES = {
    'Murderous': {
        "status": 'implemented',
        "text": (
            "When fighting with a hand weapon, may reroll To Wound rolls of a "
            "natural 1. A single, non-magical hand weapon only. "
        ),
    },
    'Eternal Hatred': {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
    'Hatred (High Elves)': {
        "status": 'implemented',
        "text": (
            "Reroll failed To Hit rolls in the first round against High Elves. "
        ),
    },
    'Strike First': {
        "status": 'implemented',
        "text": (
            "Strikes before models without it, regardless of Initiative. "
        ),
    },
    'Elven Reflexes': {
        "status": 'implemented',
        "text": (
            "+1 Initiative (max 10) during the first round of any combat. "
        ),
    },
    "Hekarti's Blessing": {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
    'Sea Dragon Cloak': {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
