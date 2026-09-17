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

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Empire Archers": {
        # https://tow.whfb.app/unit/empire-archers - 7 pts per model, unit size 5+
        # Fights with the Archer row.
        # Shooting is not simulated, so these are left out of the options: warbows.
        "points": 7,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Marksman', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Human",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Detachment", "Move Through Cover", "Open Order", "Skirmishers", "Vanguard"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Fire & Flee", "Scouts"],
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
    "Empire Greatswords": {
        # https://tow.whfb.app/unit/empire-greatswords - 11 pts per model, unit size
        # 5+
        # Fights with the Greatsword row.
        "points": 11,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': "Count's Champion", 'Movement': 4, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Full Plate Armor",
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Furious Charge", "Regimental Unit", "Stubborn"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled", "Veteran"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Flagellants": {
        # https://tow.whfb.app/unit/flagellants - 13 pts per model, unit size 5+
        # Fights with the Flagellant row.
        "points": 13,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Prophet of Doom', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 2, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 2,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Human",
            "Armor": None,
            "Weapon": "Flail",
            "Shield": False,
            "SpecialRules": ["Close Order", "Fanatical Zeal", "Feel No Pain", "Furious Charge", "Immune to Psychology", "Impetuous", "Hatred (all enemies)", "Unbreakable"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Flail"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Free Company Militia": {
        # https://tow.whfb.app/unit/free-company-militia - 6 pts per model, unit size
        # 10+ (5+ if a detachment)
        # Fights with the Militia Fighter row.
        # Shooting is not simulated, so these are left out of the options: throwing
        # weapons.
        "points": 6,
        "points_per": "model",
        "unit_size": "10+ (5+ if a detachment)",
        "champion": {'Name': 'Militia Leader', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Leadership": 6,
            "Race": "Human",
            "Armor": None,
            "Weapon": "Two Hand Weapons",
            "Shield": False,
            "SpecialRules": ["Detachment", "Furious Charge", "Horde", "Impetuous", "Levies", "Open Order", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Two Hand Weapons"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Imperial Ogres": {
        # https://tow.whfb.app/unit/imperial-ogres - 29 pts per model, unit size 3+
        # Fights with the Imperial Ogre row.
        # Shooting is not simulated, so these are left out of the options: Light
        # cannon, Ogre pistol.
        "points": 29,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Ogre Captain', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 3, 'Attacks': 4, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Ogre",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Close Order", "Fear", "Impact Hits (1)", "Mercenaries", "Motley Crew", "Ogre Charge"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Morning Star"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Nuln State Missile Troops": {
        # https://tow.whfb.app/unit/nuln-state-missile-troops - 8 pts per model, unit
        # size 5+
        # Fights with the State Missile Trooper row.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # pistols, Hochland long rifle, Repeater handgun, handguns.
        "points": 8,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Sergeant', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Human",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Detachment", "Nuln State Troops"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Nuln State Troops": {
        # https://tow.whfb.app/unit/nuln-state-troops - 6 pts per model, unit size 10+
        # Fights with the State Trooper row.
        "points": 6,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Sergeant', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Halberd",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Nuln State Troops", "Regimental Unit"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Nuln Swordsmen": {
        # https://tow.whfb.app/unit/nuln-swordsmen - 6 pts per model, unit size 5+
        # Fights with the Swordsman row.
        "points": 6,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Sergeant', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Detachment", "Horde", "Nuln State Troops"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Nuln Veteran State Troops": {
        # https://tow.whfb.app/unit/nuln-veteran-state-troops - 8 pts per model, unit
        # size 10+
        # Fights with the Veteran State Trooper row.
        # Also has a profile for Veteran Sergeant (M4 WS4 BS3 S3 T3 W1 I3 A2 Ld7); not
        # simulated.
        "points": 8,
        "points_per": "model",
        "unit_size": "10+",
        "other_profiles": [
            {'Name': 'Veteran Sergeant', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Halberd",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Nuln State Troops", "Regimental Unit", "Veteran"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "State Missile Troops": {
        # https://tow.whfb.app/unit/state-missile-troops - 7 pts per model, unit size
        # 10+ (5+ if a detachment)
        # Fights with the State Missile Trooper row.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # pistols, Hochland long rifle, Repeater handgun, crossbows, handguns.
        "points": 7,
        "points_per": "model",
        "unit_size": "10+ (5+ if a detachment)",
        "champion": {'Name': 'Sergeant', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Human",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Detachment", "Regimental Unit"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "State Troops": {
        # https://tow.whfb.app/unit/state-troops - 5 pts per model, unit size 10+ (5+
        # if a detachment)
        # Fights with the State Trooper row.
        "points": 5,
        "points_per": "model",
        "unit_size": "10+ (5+ if a detachment)",
        "champion": {'Name': 'Sergeant', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Detachment", "Horde", "Regimental Unit"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd", "Thrusting Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Teutogen Guard": {
        # https://tow.whfb.app/unit/teutogen-guard - 13 pts per model, unit size 5+
        # Fights with the Teutogen Guard row.
        "points": 13,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'First Knight', 'Movement': 4, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Full Plate Armor",
            "Weapon": "Wolf Hammer",
            "Shield": False,
            "SpecialRules": ["Blessings of Ulric", "Ward6 (Flaming)", "Close Order", "Drilled", "Stubborn", "Veteran"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Guardians of the Temple"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Wolf Hammer"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Veteran State Troops": {
        # https://tow.whfb.app/unit/veteran-state-troops - 7 pts per model, unit size
        # 10+ (5+ if a detachment)
        # Fights with the Veteran State Trooper row.
        # Also has a profile for Veteran Sergeant (M4 WS4 BS3 S3 T3 W1 I3 A2 Ld7); not
        # simulated.
        "points": 7,
        "points_per": "model",
        "unit_size": "10+ (5+ if a detachment)",
        "other_profiles": [
            {'Name': 'Veteran Sergeant', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Human",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Detachment", "Horde", "Regimental Unit", "Veteran"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd", "Thrusting Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Demigryph Knights": {
        # https://tow.whfb.app/unit/demigryph-knights - 58 pts per model, unit size
        # 2-12
        # Fights with the Demigryph Knight row.
        # Also has a profile for Demigryph (M7 WS4 BS- S5 T- W- I4 A3 Ld-); not
        # simulated.
        "points": 58,
        "points_per": "model",
        "unit_size": "2-12",
        "champion": {'Name': 'Demigryph Preceptor', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 3, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Demigryph', 'Movement': 7, 'WeaponSkill': 4, 'BallisticSkill': None, 'Strength': 5, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 3, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Counter Charge", "First Charge", "Fear", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd", "Lance"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Empire Knights": {
        # https://tow.whfb.app/unit/empire-knights - 20 pts per model, unit size 4+
        # Fights with the Empire Knight row.
        # Also has a profile for Barded Warhorse (M7 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        "points": 20,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'Preceptor', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [
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
            "Shield": True,
            "SpecialRules": ["Close Order", "Counter Charge", "First Charge", "Swiftstride"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled", "Stubborn"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Empire Road Wardens": {
        # https://tow.whfb.app/unit/empire-road-wardens - 18 pts per model, unit size
        # 4+
        # Fights with the Road Warden row.
        # Also has a profile for Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # pistols, Repeater pistol, braces of pistols, crossbow, crossbows.
        "points": 18,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'Captain', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Human",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fast Cavalry", "Fire & Flee", "Open Order", "Skirmishers", "Swiftstride", "Vanguard"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Feigned Flight", "Vanguard", "Ambushers", "Scouts"],
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
    "Inner Circle Knights": {
        # https://tow.whfb.app/unit/inner-circle-knights - 28 pts per model, unit size
        # 4+
        # Fights with the Inner Circle Knight row.
        # Also has a profile for Barded Warhorse (M7 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        "points": 28,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'Inner Circle Preceptor', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 9},
        "other_profiles": [
            {'Name': 'Barded Warhorse', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Human",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Close Order", "Counter Charge", "Drilled", "First Charge", "Inner Circle", "Reroll Hits 1", "Swiftstride", "Veteran"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Stubborn"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon", "Lance"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Outriders": {
        # https://tow.whfb.app/unit/outriders - 19 pts per model, unit size 4+
        # Fights with the Outrider row.
        # Also has a profile for Empire Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Brace of
        # pistols, Grenade launching blunderbuss, Repeater pistol, pistols, repeater
        # handguns.
        "points": 19,
        "points_per": "model",
        "unit_size": "4+",
        "champion": {'Name': 'Sharpshooter', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Empire Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Human",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Fast Cavalry", "Fire & Flee", "Open Order", "Skirmishers", "Swiftstride", "Vanguard"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
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
    "Pistoliers": {
        # https://tow.whfb.app/unit/pistoliers - 15 pts per model, unit size 5+
        # Fights with the Pistolier row.
        # Also has a profile for Empire Warhorse (M8 WS3 BS- S3 T- W- I3 A1 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Grenade
        # launching blunderbuss, Repeater handgun, Repeater pistol, brace of pistols.
        "points": 15,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Veteran', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Empire Warhorse', 'Movement': 8, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
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
            "Leadership": 6,
            "Race": "Human",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Counter Charge", "Fast Cavalry", "Fire & Flee", "Impetuous", "Open Order", "Skirmishers", "Swiftstride"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
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
    "Empire Steam Tank": {
        # https://tow.whfb.app/unit/empire-steam-tank - 265 pts per unit
        # Fights with the Engineer Commander (x1) row, using the Steam Tank row's
        # Toughness and Wounds.
        # Also has a profile for Steam Tank (M4 WS- BS- S6 T7 W10 I- A- Ld-); not
        # simulated.
        # Armour value 3+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: Hochland
        # long rifle, Repeater pistol.
        "points": 265,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Steam Tank', 'Movement': 4, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 6, 'Toughness': 7, 'Initiative': None, 'Wounds': 10, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 7,
            "Initiative": 3,
            "Wounds": 10,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Armour Value 3+",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Grinding Wheels", "Immune to Psychology", "Impact Hits (D6+1)", "Large Target", "Steam Power", "Stomp Attacks (D3+1)", "Temperamental", "Terror", "Unbreakable"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
            "OptionalRules": ["Pigeon bombs"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Armour Value 3+"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Empire War Wagon": {
        # https://tow.whfb.app/unit/empire-war-wagon - 140 pts per unit
        # Fights with the War Wagon Crew (x6) row, using the War Wagon row's Toughness
        # and Wounds.
        # Also has a profile for War Wagon (M- WS- BS- S5 T5 W6 I- A- Ld-); not
        # simulated.
        # Also has a profile for Barded Warhorse (x2) (M7 WS3 BS- S3 T- W- I3 A1 Ld-);
        # not simulated.
        # Armour value 3+ as printed on the site.
        "points": 140,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'War Wagon', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 6, 'Attacks': None, 'Leadership': None},
            {'Name': 'Barded Warhorse (x2)', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 6,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Human",
            "Armor": "Armour Value 3+",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Crushing Weight", "Impact Hits (D6+1, War Wagon only)", "Large Target", "Stable Firing Platform", "Stomp Attacks (D3+1)"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Armour Value 3+"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Great Cannon": {
        # https://tow.whfb.app/unit/great-cannon - 125 pts per unit
        # Fights with the Gun Crew row.
        # Also has a profile for Great Cannon (M- WS- BS- S- T6 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Great
        # cannon.
        "points": 125,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Great Cannon', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "SpecialRules": ["Skirmishers"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
            "OptionalRules": ["Veteran"],
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
    "Helblaster Volley Gun": {
        # https://tow.whfb.app/unit/helblaster-volley-gun - 120 pts per unit
        # Fights with the Gun Crew row.
        # Also has a profile for Helblaster Volley Gun (M- WS- BS- S- T6 W3 I- A-
        # Ld-); not simulated.
        # Shooting is not simulated, so these are left out of the options: Helblaster
        # Volley Gun.
        "points": 120,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Helblaster Volley Gun', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "SpecialRules": ["Skirmishers"],
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
    "Helstorm Rocket Battery": {
        # https://tow.whfb.app/unit/helstorm-rocket-battery - 125 pts per unit
        # Fights with the Gun Crew row.
        # Also has a profile for Helstorm Rocket Battery (M- WS- BS- S- T6 W3 I- A-
        # Ld-); not simulated.
        # Shooting is not simulated, so these are left out of the options: Helstorm
        # Rocket Battery.
        "points": 125,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Helstorm Rocket Battery', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "SpecialRules": ["Skirmishers"],
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
    "Mortar": {
        # https://tow.whfb.app/unit/mortar - 95 pts per unit
        # Fights with the Gun Crew row.
        # Also has a profile for Mortar (M- WS- BS- S- T6 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Mortar.
        "points": 95,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Mortar', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
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
            "SpecialRules": ["Skirmishers"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
            "OptionalRules": ["Veteran"],
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


# Army-wide special rules for this faction. `status` is how far the engine
# goes with each: "implemented", "partial", or None for recorded only.
FACTION_RULES = {
    'Hold the Line!': {
        "status": None,
        "text": (
            "This character and any unit they have joined automatically passes any "
            "Panic tests they are required to make."
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
            "If this model joins a unit of Empire Knights, Inner Circle Knights or "
            "Demigryph Knights, that unit will gain the Immune To Psychology "
            "special rule. Should this model leave a unit it has joined for any "
            "reason, that unit loses this special rule."
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
    "Blessings of Ulric": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/blessings-of-ulric",
        "text": (
            "A model with this special rule has a 6+ Ward save against any wounds "
            "suffered that were caused by an attack that has the Flaming Attacks "
            "special rule."
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
    "Crushing Weight": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/crushing-weight",
        "text": (
            "Stomp Attacks made by a War Wagon have an Armour Piercing "
            "characteristic of - 1. In addition, and unlike other chariots, this "
            "model treats low linear obstacles as dangerous terrain rather than as "
            "impassable terrain."
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
    "Fanatical Zeal": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fanatical-zeal",
        "text": (
            "A unit with this special rule can be joined by a Lector of Sigmar or a "
            "Priest of Sigmar. However, these are the only characters that can join "
            "this unit. A Lector of Sigmar or Priest of Sigmar that joins a unit of "
            "Flagellants is considered to have the Unbreakable special rule for as "
            "long as they remain with the unit. Note that a unit with the "
            "Unbreakable special rule cannot normally be joined by a character "
            "without it. This rule provides an exception that represents the "
            "fanaticism of Sigmar's priesthood."
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
    "Feel No Pain": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/feel-no-pain",
        "text": (
            "A model with this special rule has: - A 6+ Ward save against any "
            "wounds suffered that were caused by a non-magical enemy attack. - A 5+ "
            "Ward save against any wounds suffered that were caused by a non- "
            "magical enemy attack with a Strength 5 or higher."
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
    "Furious Charge": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/furious-charge",
        "text": (
            "During a turn in which it made a charge move of 3\" or more, a model "
            "with this special rule gains a +1 modifier to its Attacks "
            "characteristic."
        ),
    },
    "Grinding Wheels": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/grinding-wheels",
        "text": (
            "Stomp Attacks made by a this model have an Armour Piercing "
            "characteristic of -2. However, this rule cannot be used against models "
            "whose troop type is behemoth – they are simply too large to be caught "
            "beneath the wheels. In addition, and unlike other chariots, this model "
            "treats low linear obstacles as open terrain rather than as impassable "
            "terrain."
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
    "Inner Circle": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/inner-circle",
        "text": (
            "When engaged in combat, a model with this special rule (but not its "
            "mount) may re-roll any rolls To Hit of a natural 1."
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
    "Mercenaries": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/mercenaries",
        "text": (
            "Often, an army can include certain units drawn from another army list "
            "as mercenaries. Any such units included in your army gain this special "
            "rule. Mercenaries cannot use the Inspiring Presence rule of the army's "
            "General nor the \"Hold your Ground\" rule of a Battle Standard. "
            "Mercenaries cannot be joined by characters drawn from another army "
            "list."
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
    "Nuln State Troops": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/nuln-state-troops",
        "text": (
            "Regiments of Nuln State Troops and Nuln Veteran State Troops are made "
            "as follows, using the profiles for State Troops and Veteran State "
            "Troops in the Empire of Man army list, accompanied by detachments of "
            "State Missile Troops: - A regiment of Nuln State Troops consists of a "
            "regimental unit of State Troops, accompanied by 1-2 detachments of "
            "State Missile Troops and/or Swordsmen. - A regiment of Nuln Veteran "
            "State Troops consists of a regimental unit of Veteran State Troops, "
            "accompanied by 1-2 detachments of State Missile Troops and/or "
            "Swordsmen. - Each unit of State Troops or Veteran State Troops must be "
            "equipped with halberds. - Each detachment of State Missile Troops must "
            "be equipped with [...]"
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
    "Stable Firing Platform": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/stable-firing-platform",
        "text": (
            "To reflect the stability of a War Wagon, any missile weapons carried "
            "by the crew can be used in the Shooting phase even if the War Wagon "
            "marched this turn."
        ),
    },
    "Steam Power": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/steam-power",
        "text": (
            "A Steam Tank cannot march. Instead, you may make a 'Steam Power' roll "
            "and add the result to the model's Movement characteristic. To make a "
            "Steam Power roll, roll two D6 and discard the lowest result. The "
            "highest result is the result of the Steam Power roll. If both dice "
            "roll the same result, discard either."
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
    "Temperamental": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/temperamental",
        "text": (
            "If a natural 1 is rolled on either of the dice when the Steam Tank "
            "makes a Steam Power roll or a Charge roll, the pressure has reached "
            "dangerous levels and, if not quickly released, will cause irreparable "
            "damage. Choose one of the following: - Bang! The crew ignores the "
            "building pressure which, inevitably, finds its own release. The Steam "
            "Tank loses a single Wound. - Phweee! Amidst billowing clouds of steam "
            "and with an ear splitting whistle, the pressure is released, rendering "
            "the Steam Tank immobile. The Steam Tank halts immediately and cannot "
            "move again for the remainder of this turn. However, if a natural 1 is "
            "rolled on both of the dice, the pressure is too great to be released "
            "safely. [...]"
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
