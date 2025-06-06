# Game Data Constants

# Race Synonyms and Race Names
RACE_NAMES = {
    "HIGH_ELVES": ["High Elf", "High Elves", "Asur"],
    "DARK_ELVES": ["Dark Elf", "Dark Elves", "Druchii"],
    "ORCS": ["Orc", "Orcs", "Greenskins"],
    # Add more races as needed
}

# Special Rule Names
FirstRoundStr = "1st round strength only"
FirstRoundOnly = "First Round Only"
StrikeFirst = "Strike First"
StrikeLast = "Strike Last"
Evasive = "Evasive"
IgnoresCover = "Ignores Cover"
ImmuneToPsychology = "Immune to Psychology"
FuriousCharge = "Furious Charge"
MoveThroughCover = "Move Through Cover"
Stubborn = "Stubborn"
RallyingCry = "Rallying Cry"
RerollHits1 = "Reroll Hits 1"
FlamingAttacks = "Flaming Attacks"
Magic = "Magic"
Ethereal = "Ethereal"
Frenzy = "Frenzy"


#Derived Special Rules
ImproveArmor1InCombat = "Improve Armor 1 in Combat"
ImproveArmor2InShooting = "Improve Armor 2 in Shooting"

# High Elf Specific Special Rules
IthilmarWeapons = "Ithilmar Weapons"
ValourOfAges = "Valour of Ages"
ArrowsOfIsha = "Arrows of Isha"
IthilmarArmour = "Ithilmar Armour"
MightyConstitution = "Mighty Constitution"
CommandingVoice = "Commanding Voice"
NavalDiscipline = "Naval Discipline"
PrecisionStrikes = "Precision Strikes"




# The chart is a 2D list where the row(1st index) is the Attacker's WS
# and the column (2nd index) is the Defender's WS
WeaponSkillChart = [
    [4, 4, 5, 5, 5, 5, 5, 5, 5, 5],  # Attacker WS 1
    [3, 4, 4, 4, 5, 5, 5, 5, 5, 5],  # Attacker WS 2
    [2, 3, 4, 4, 4, 4, 5, 5, 5, 5],  # Attacker WS 3
    [2, 3, 3, 4, 4, 4, 4, 5, 5, 5],  # Attacker WS 4
    [2, 2, 3, 3, 4, 4, 4, 4, 4, 4],  # Attacker WS 5
    [2, 2, 3, 3, 3, 4, 4, 4, 4, 4],  # Attacker WS 6
    [2, 2, 2, 3, 3, 3, 4, 4, 4, 4],  # Attacker WS 7
    [2, 2, 2, 3, 3, 3, 3, 4, 4, 4],  # Attacker WS 8
    [2, 2, 2, 2, 3, 3, 3, 3, 4, 4],  # Attacker WS 9
    [2, 2, 2, 2, 2, 3, 3, 3, 3, 4],  # Attacker WS 10
]

# Defender's Toughness (T) vs Attacker's Strength (S) chart
# The chart is a 2D list where the row(1st index) is the Attacker's Strength
# and the column (2nd index) is the Defender's Toughness
Wounds_vs_ToughnessChart = [
    [4, 5, 6, 6, 6, 6, None, None, None, None],  # Strength 1
    [3, 4, 5, 6, 6, 6, None, None, None, None],  # Strength 2
    [2, 3, 4, 5, 6, 6, 6, None, None, None],  # Strength 3
    [2, 2, 3, 4, 5, 6, 6, 6, None, None],  # Strength 4
    [2, 2, 2, 3, 4, 5, 6, 6, 6, None],  # Strength 5
    [2, 2, 2, 2, 3, 4, 5, 6, 6, 6],  # Strength 6
    [2, 2, 2, 2, 2, 3, 4, 5, 6, 6],  # Strength 7
    [2, 2, 2, 2, 2, 2, 3, 4, 5, 6],  # Strength 8
    [2, 2, 2, 2, 2, 2, 2, 3, 4, 5],  # Strength 9
    [2, 2, 2, 2, 2, 2, 2, 2, 3, 4],  # Strength 10
]


ArmourDict = {
    "None": 0,
    ("Light Armor", "LA", "Light"): 6,
    ("Heavy Armor", "HA", "Heavy"): 5,
    ("Plate Armor", "PA", "Plate","Full Plate Armor","Full Plate"): 4,
}

# Dictionary for melee weapons, strength value and armor piercing value and special rules
##### IMPLEMENT THAT CHARACTERS HAVE "REQUIRES tWO HANDS" WHICH MEANS THEY CANNOT USE A SHIELD

# Special rules can include: "+1A" for +1 Attack
MeleeWeaponDict = {
    ("HW", "Hand Weapon", "HandWeapon"): [None, 0, None],  # Hand Weapon, no strength bonus, no armor piercing, no special rules
    ("Two Hand Weapons", "2xHW", "2HW"): [None, 0, ["+1A"]],  # Two Hand Weapons, no strength bonus, no armor piercing, +1 Attack
    ("Flail",): [2, -2, [FirstRoundStr]],  # Flail, +2 Strength, -2 Armor Piercing, First Round Strength only
    ("Great Weapon", "GW", "GreatWeapon"): [2, -2, [StrikeLast, "AB1"]],  # Great Weapon, +2 Strength, -2 Armor Piercing, Armour Bane 1, Strike Last
    ("Halberd",): [1, -1, ["AB1"]],  # Halberd, +1 Strength, -1 Armor Piercing, Armour Bane 1
    ("Morning Star", "MorningStar","Morningstar"): [1, -1, [FirstRoundStr]],  # Morning Star, +1 Strength, -1 Armor Piercing, First Round Strength only
    ("Whip",): [None, 0, [StrikeFirst]],  # Whip, Strike First
    ("Lance",): [2, 2, [FirstRoundOnly, "AB1"]],  # Lance, +2 Strength, +2 Armor Piercing, Armour Bane 1, First Round Only
    ("Cavalry Spear", "CavSpear", "CavalrySpear"): [1, -1, [FirstRoundOnly]],  # Cavalry Spear, +1 Strength, -1 armor piercing, First Round Only
    ("Throwing Spears", "ThrowingSpear"): [None, 0, [FirstRoundOnly]],  # Throwing Spears, No strength, no armor piercing, First Round Only
    ("Thrusting Spear", "ThrustingSpear", "Spear"): [None, 0, None],  # Thrusting Spear, no strength bonus, no armor piercing, no special rules
    ("Chayal",):[2,-3,["KillingBlow6",RerollHits1]],
    ("Mathlann's Ire",):[1,-2,["AB1","Magic"]],
}

MagicItemDict = {
    "Pelt of Charandis": [ImproveArmor1InCombat,ImproveArmor2InShooting, "Regen5"],
}



# Faction Dictionaries
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
                "SpecialRules": [StrikeFirst,IthilmarWeapons,ValourOfAges],
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
                "SpecialRules": [StrikeFirst,IthilmarWeapons,ValourOfAges],
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
                "SpecialRules": [ArrowsOfIsha,IthilmarWeapons, StrikeFirst,Evasive,IgnoresCover,ImmuneToPsychology,IthilmarArmour],
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
                "SpecialRules":[FuriousCharge, MightyConstitution, MoveThroughCover, Stubborn, ValourOfAges],
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
                "SpecialRules":[CommandingVoice,IthilmarWeapons,NavalDiscipline,RallyingCry,StrikeFirst,PrecisionStrikes,ValourOfAges],
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