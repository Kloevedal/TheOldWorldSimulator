# Faction Profiles

# Race Synonyms and Race Names
RACE_NAMES = {
    "HIGH_ELVES": ["High Elf", "High Elves", "Asur"],
    "DARK_ELVES": ["Dark Elf", "Dark Elves", "Druchii"],
    "ORCS": ["Orc", "Orcs", "Greenskins", "Orks", "Ork"],
    # Add more races as needed
}



FactionProfiles = {
    "High Elves": {
        "Noble": {
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
                "Shield": None,
                "SpecialRules": ["Strike First","Ithilmar Weapons","Valour of Ages"],
            },
            "equipment_options": {
                "weapons": ["Hand Weapon", "Great Weapon", "Lance", "Cavalry Spear", "Halberd"],
                "armor": ["Light Armor", "Heavy Armor", "Plate Armor"],
                "shield": True,
                "items": [],
            }
        },
        "Prince": {
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
                "Shield": None,
                "SpecialRules": ["Strike First","Ithilmar Weapons","Valour of Ages"],
            },
            "equipment_options": {
                "weapons": ["Hand Weapon","Two Hand Weapons", "Great Weapon", "Lance", "Cavalry Spear", "Halberd"],
                "armor": ["Light Armor", "Heavy Armor", "Plate Armor"],
                "shield": True,
                "items":[],
            },
        },
        "Handmaiden of the Everqueen": {
            "base_profile": {
                "Movement": 5,
                "WeaponSkill": 6,
                "BallisticSkill": 7,
                "Strength": 4,
                "Toughness": 3,
                "Wounds": 2,
                "Initiative": 6,
                "Race": "High Elf",
                "Attacks": 2,
                "Leadership": 8,
                "SpecialRules": ["Arrows of Isha","Ithilmar Weapons", "Strike First","Evasive","Ignores Cover","Immune to Psychology","Ithilmar Armour"],
            },
            "equipment_options": {
                "weapons":["Handmaiden's Spear", "Bow of Avelorn", "Hand Weapon"],
                "armor": ["Light Armor", "Heavy Armor"],
                "shield": False,
                "items": [],
            },
        },
        "Korhil": {
            "base_profile": {
                "Movement": 5,
                "WeaponSkill": 7,
                "BallisticSkill": 5,
                "Strength": 4,
                "Toughness": 3,
                "Initiative": 6,
                "Race": "High Elf",
                "Wounds": 3,
                "Attacks": 4,
                "Leadership": 9,
                "SpecialRules":["Furious Charge", "Mighty Constitution", "Move Through Cover", "Stubborn", "Valour of Ages"],
            },
            "equipment_options": {
                "weapons": ["Chayal", "Hand Weapon"],
                "armor": ["Heavy Armor"],
                "shield": True,
                "items": ["Pelt Of Charandis"],
            },
        },
        "Ishaya Vess": {
            "base_profile": {
                "Movement": 5,
                "WeaponSkill": 7,
                "BallisticSkill": 7,
                "Strength": 4,
                "Toughness": 3,
                "Initiative": 7,
                "Race": "High Elf",
                "Wounds": 3,
                "Attacks": 4,
                "Leadership": 9,
                "SpecialRules":["Commanding Voice","Ithilmar Weapons","Naval Discipline","Rallying Cry","Strike First","Precision Strikes","Valour of Ages"],
            },
            "equipment_options": {
                "weapons": ["Mathlann's Ire", "Hand Weapon","Warbow"],
                "armor": ["Heavy Armor"],
                "shield": True,
                "items": [],
            },
        },
    },
    "Orcs": {
        "Orc Boss": {
            "base_profile": {
                "Movement": 4,
                "WeaponSkill": 4,
                "BallisticSkill": 3,
                "Strength": 4,
                "Toughness": 4,
                "Initiative": 3,
                "Wounds": 2,
                "Attacks": 3,
                "Leadership": 8,
                "Race": "Orc",
                "Armor": None,
                "Weapon": "Hand Weapon",
                "Shield": None,
                "SpecialRules": ["Animosity"],
            },
            "equipment_options": {
                "weapons": ["Hand Weapon", "Great Weapon", "Two Hand Weapons"],
                "armor": ["Light Armor", "Heavy Armor"],
                "shield": True,
                "items": [],
            }
        },
        "Black Orc Boss": {
            "base_profile": {
                "Movement": 4,
                "WeaponSkill": 5,
                "BallisticSkill": 3,
                "Strength": 4,
                "Toughness": 4,
                "Initiative": 3,
                "Wounds": 2,
                "Attacks": 3,
                "Leadership": 8,
                "Race": "Orc",
                "Armor": "Heavy Armor",
                "Weapon": "Hand Weapon",
                "Shield": None,
                "SpecialRules": ["Immune to Psychology"],
            },
            "equipment_options": {
                "weapons": ["Hand Weapon", "Great Weapon", "Two Hand Weapons"],
                "armor": ["Heavy Armor", "Plate Armor"],
                "shield": True,
                "items": [],
            }
        }
    }
}
