"""Empire of Man.

Profiles from https://tow.whfb.app/army/empire-of-man
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Empire of Man"

# Other names that should resolve to this faction.
ALIASES = [
    "The Empire",
    "Empire",
    "Empire of Man",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "General": "General of the Empire",
    "Captain": "Captain of the Empire",
    "Hans von Loewenhacke": "General Hans von Loewenhacke",
    "Loewenhacke": "General Hans von Loewenhacke",
    "Harald": "Harald Gemunsen",
}

CHARACTERS = {
    "General of the Empire": {
        # https://tow.whfb.app/unit/general-of-the-empire - 90 pts
        # Also has handgun, longbow and pistol options; shooting is not simulated.
        "points": 90,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hold the Line!", "Rallying Cry"],
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
            "mounts": ["Empire Warhorse", "Barded Warhorse", "Pegasus", "Demigryph", "Griffon (Empire)", "Imperial Griffon"]
        }
    },
    "Captain of the Empire": {
        # https://tow.whfb.app/unit/captain-of-the-empire - 45 pts
        "points": 45,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Hold the Line!", "Rallying Cry"],
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
            "mounts": ["Empire Warhorse", "Barded Warhorse", "Pegasus", "Demigryph", "Griffon (Empire)"]
        }
    },
    "Grand Master": {
        # https://tow.whfb.app/unit/grand-master - 145 pts
        # Movement is '-' on the profile: a mount is compulsory and supplies it.
        # Mounts are not simulated, so he fights on foot here.
        "points": 145,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Human",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Counter Charge", "First Charge", "Immune to Psychology", "Master of Battle", "Rallying Cry", "Stubborn", "Swiftstride", "Veteran"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Lance"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Barded Warhorse", "Pegasus", "Demigryph"]
        }
    },
    "Chapter Master": {
        # https://tow.whfb.app/unit/chapter-master - 75 pts
        # Movement is '-' on the profile: a mount is compulsory and supplies it.
        "points": 75,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Counter Charge", "First Charge", "Immune to Psychology", "Master of Battle", "Rallying Cry", "Stubborn", "Swiftstride", "Veteran"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Lance"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Barded Warhorse", "Pegasus", "Demigryph"]
        }
    },
    "Wizard Lord": {
        # https://tow.whfb.app/unit/wizard-lord - 130 pts
        "points": 130,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Human",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Magical Attacks", "Magic Resistance (-1)"],
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Elementalism", "Illusion", "Necromancy"],
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
            "mounts": ["Empire Warhorse", "Pegasus", "Imperial Griffon"]
        }
    },
    "Master Mage": {
        # https://tow.whfb.app/unit/master-mage - 60 pts
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
            "Leadership": 7,
            "Race": "Human",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Magical Attacks", "Magic Resistance (-1)"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Elementalism", "Illusion", "Necromancy"],
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
            "mounts": ["Empire Warhorse", "Pegasus"]
        }
    },
    "Witch Hunter": {
        # https://tow.whfb.app/unit/witch-hunter - 55 pts
        # Also has crossbow, handgun and pistol options; shooting is not simulated.
        "points": 55,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Immune to Psychology", "Killing Blow", "Suffer Not..."],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Empire Warhorse", "Pegasus"]
        }
    },
    "Lector of Sigmar": {
        # https://tow.whfb.app/unit/lector-of-sigmar - 110 pts
        "points": 110,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Magical Attacks", "Magic Resistance (-1)", "Prayers of Sigmar"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Empire Warhorse", "Barded Warhorse", "War Altar of Sigmar"]
        }
    },
    "Priest of Sigmar": {
        # https://tow.whfb.app/unit/priest-of-sigmar - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Magical Attacks", "Magic Resistance (-1)", "Prayers of Sigmar"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Empire Warhorse", "Barded Warhorse"]
        }
    },
    "High Priest of Ulric": {
        # https://tow.whfb.app/unit/high-priest-of-ulric - 110 pts
        "points": 110,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Magical Attacks", "Magic Resistance (-1)", "Prayers of Ulric"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Empire Warhorse", "Barded Warhorse"]
        }
    },
    "Priest of Ulric": {
        # https://tow.whfb.app/unit/priest-of-ulric - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Magical Attacks", "Magic Resistance (-1)", "Prayers of Ulric"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Empire Warhorse", "Barded Warhorse"]
        }
    },
    "Empire Engineer": {
        # https://tow.whfb.app/unit/empire-engineer - 45 pts
        # His whole kit is black-powder weaponry, none of which is simulated.
        "points": 45,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Human",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Clouds of Soot & Smoke", "Master of Ballistics"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Empire War Wagon"]
        }
    },
    "Harbinger of Doom": {
        # https://tow.whfb.app/unit/harbinger-of-doom - 65 pts
        # 0-1 per army, and only alongside Flagellants.
        "points": 65,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 2,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Human",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Feel No Pain", "Furious Charge", "Hatred (all enemies)", "Immune to Psychology", "Impetuous", "Prayer of the Damned", "Unbreakable", "Zealot"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Flail", "Great Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "General Hans von Loewenhacke": {
        # https://tow.whfb.app/unit/general-hans-von-loewenhacke - 190 pts
        # Fixed wargear; must be fielded as presented.
        "points": 190,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Human",
            "Armor": "Full Plate Armor",
            "Weapon": "Judgement",
            "Shield": False,
            "SpecialRules": ["Hold the Line!", "Mercenary Commander", "Rallying Cry", "Strategic Mastery", "Stubborn"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Judgement", "Hand Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": ["Judgement", "Griffon Helm"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Harald Gemunsen": {
        # https://tow.whfb.app/unit/harald-gemunsen - 185 pts
        # Fixed wargear. Rides a Barded Warhorse that supplies his Movement; the
        # mount is not simulated.
        "points": 185,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 7,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Human",
            "Armor": "Full Plate Armor",
            "Weapon": "Beast Reaver",
            "Shield": False,
            "SpecialRules": ["Counter Charge", "First Charge", "Grand Master of the Knights Panther", "Hatred (Warriors of Chaos, Beastmen Brayherds & Daemonic models)", "Immune to Psychology", "Magic Resistance (-1)", "Master of Battle", "Rallying Cry", "Skilled Duellist", "Stubborn", "Swiftstride", "Veteran"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Beast Reaver", "Hand Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": ["Beast Reaver"],
        },
        "mount_options": {
            "mounts": ["Barded Warhorse"]
        }
    },
}

# Regular (non-character) units go here.
UNITS = {}


# Army-wide special rules for this faction. `status` is how far the engine
# goes with each: "implemented", "partial", or None for recorded only.
FACTION_RULES = {
    'Hold the Line!': {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
    'Magical Attacks': {
        "status": 'implemented',
        "text": (
            "This model's attacks count as magical. "
        ),
    },
    'Magic Resistance (-X)': {
        "status": None,
        "text": (
            "Affects enemy casting; magic is not simulated. "
        ),
    },
    'Prayers of Sigmar': {
        "status": None,
        "text": (
            "Prayers are not simulated. "
        ),
    },
    'Prayers of Ulric': {
        "status": None,
        "text": (
            "Prayers are not simulated. "
        ),
    },
    'Master of Battle': {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
