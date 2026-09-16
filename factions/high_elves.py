"""High Elf Realms.

Profiles from https://tow.whfb.app/army/high-elf-realms
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "High Elves"

# Other names that should resolve to this faction.
ALIASES = [
    "High Elf Realms",
    "High Elf",
    "Asur",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Korhil": "Korhil Lionmane",
    "Sea Guard Commander": "Sea Guard Garrison Commander",
    "Garrison Commander": "Sea Guard Garrison Commander",
    "Handmaiden": "Handmaiden of the Everqueen",
}

CHARACTERS = {
    "Prince": {
        # https://tow.whfb.app/unit/prince - 130 pts
        # Strike First does not apply to this model's mount.
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
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ithilmar Weapons", "Strike First", "Valour of Ages"],
            "ElvenHonours": True,
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd", "Cavalry Spear", "Lance"],
            "armor": ["Light Armor", "Heavy Armor", "Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Barded Elven Steed", "Tiranoc Chariot", "Griffon (High Elves)", "Great Eagle", "Moon Dragon", "Star Dragon"]
        }
    },
    "Noble": {
        # https://tow.whfb.app/unit/noble - 70 pts
        # Strike First does not apply to this model's mount.
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
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ithilmar Weapons", "Strike First", "Valour of Ages"],
            "ElvenHonours": True,
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd", "Cavalry Spear", "Lance"],
            "armor": ["Light Armor", "Heavy Armor", "Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Barded Elven Steed", "Tiranoc Chariot", "Griffon (High Elves)", "Great Eagle"]
        }
    },
    "Chracian Chieftain": {
        # https://tow.whfb.app/unit/chracian-chieftain - 105 pts
        # Furious Charge, Move Through Cover and Strike First do not apply to
        # the mount.
        "points": 105,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Furious Charge", "Ithilmar Weapons", "Lion Cloak", "Move Through Cover", "Strike First", "Stubborn", "Valour of Ages"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Chracian Great Blade"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Chieftain's Chariot"]
        }
    },
    "Sea Guard Garrison Commander": {
        # https://tow.whfb.app/unit/sea-guard-garrison-commander - 90 pts
        # Carries a warbow as standard; shooting is not simulated.
        "points": 90,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Accomplished Archers", "Ithilmar Weapons", "Naval Discipline", "Strike First", "Valour of Ages"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cavalry Spear"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Lothern Skycutter", "Griffon (High Elves)", "Great Eagle"]
        }
    },
    "Handmaiden of the Everqueen": {
        # https://tow.whfb.app/unit/handmaiden-of-the-everqueen - 65 pts
        # Also carries a Bow of Avelorn; shooting is not simulated.
        "points": 65,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arrows of Isha", "Evasive", "Ignores Cover", "Immune to Psychology", "Ithilmar Armour", "Ithilmar Weapons", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Handmaiden's Spear"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": ["Horn of Isha"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Archmage": {
        # https://tow.whfb.app/unit/archmage - 155 pts
        "points": 155,
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
            "Race": "High Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Ithilmar Weapons", "Lileath's Blessing", "Lore of Saphery", "Valour of Ages"],
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Elementalism", "High Magic", "Illusion"],
            "ElvenHonours": True,
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
            "mounts": ["Elven Steed", "Barded Elven Steed", "Great Eagle", "Moon Dragon", "Star Dragon"]
        }
    },
    "Mage": {
        # https://tow.whfb.app/unit/mage - 80 pts
        "points": 80,
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
            "Race": "High Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Ithilmar Weapons", "Lileath's Blessing", "Lore of Saphery", "Valour of Ages"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "High Magic", "Illusion"],
            "ElvenHonours": True,
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
            "mounts": ["Elven Steed", "Barded Elven Steed", "Great Eagle"]
        }
    },
    "Storm Weaver": {
        # https://tow.whfb.app/unit/storm-weaver - 85 pts
        # 0-1 per 1,000 points in a Grand Army list.
        "points": 85,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Ithilmar Weapons", "Lore of Saphery", "Valour of Ages"],
            "WizardLevel": 1,
            "Lores": ["Dark Magic", "Elementalism", "Illusion"],
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
            "mounts": ["Unicorn"]
        }
    },
    "Dragon Mage": {
        # https://tow.whfb.app/unit/dragon-mage - 275 pts
        # Movement is '-' on the profile; the Sun Dragon mount (M6 WS5 S5 I4 A4)
        # supplies it, and T5/W6 are the dragon's. The mount is not simulated.
        "points": 275,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 6,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "High Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Blessings of Asuryan", "Close Order", "Dragon Armour", "Elven Reflexes", "Fly (10)", "Impetuous", "Ithilmar Weapons", "Large Target", "Lileath's Blessing", "Lore of Saphery", "Stomp Attacks (D6)", "Swiftstride", "Terror", "Valour of Ages"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism"],
            "TroopType": "Behemoth",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Sun Dragon"]
        }
    },
    "Korhil Lionmane": {
        # https://tow.whfb.app/unit/korhil-lionmane - 175 pts
        # Fixed wargear. Furious Charge and Move Through Cover do not apply to
        # his mount.
        "points": 175,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 7,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Chayal",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Furious Charge", "Mighty Constitution", "Move Through Cover", "Stubborn", "Valour of Ages"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Chayal"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": ["Pelt of Charandis"],
        },
        "mount_options": {
            "mounts": ["Chieftain's Chariot"]
        }
    },
    "Ishaya Vess": {
        # https://tow.whfb.app/unit/ishaya-vess - 170 pts
        # Fixed wargear: also a warbow. Her shield is standard, so pass
        # Shield=False to wield the two-handed Mathlann's Ire.
        "points": 170,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 7,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 7,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "High Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Mathlann's Ire",
            "Shield": True,
            "SpecialRules": ["Commanding Voice", "Ithilmar Weapons", "Naval Discipline", "Precision Strikes", "Rallying Cry", "Strike First", "Valour of Ages"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Mathlann's Ire", "Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": ["Mathlann's Ire"],
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
    'Valour of Ages': {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
    'Ithilmar Weapons': {
        "status": 'implemented',
        "text": (
            "Reroll To Hit rolls of a natural 1 when using a hand weapon. "
        ),
    },
    'Elven Reflexes': {
        "status": 'implemented',
        "text": (
            "+1 Initiative (max 10) during the first round of any combat. "
        ),
    },
    'Strike First': {
        "status": 'implemented',
        "text": (
            "Strikes before models without it, regardless of Initiative. "
        ),
    },
    "Lileath's Blessing": {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
    'Blessings of Asuryan': {
        "status": 'implemented',
        "text": (
            "A 5+ Ward save against Flaming Attacks. "
        ),
    },
    'Dragon Armour': {
        "status": 'implemented',
        "text": (
            "A 6+ Ward save. "
        ),
    },
    'Witness to Destiny': {
        "status": 'implemented',
        "text": (
            "A 6+ Ward save. "
        ),
    },
    'Lion Cloak': {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
