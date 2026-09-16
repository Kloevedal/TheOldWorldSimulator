"""Tomb Kings of Khemri.

Profiles from https://tow.whfb.app/army/tomb-kings-of-khemri, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Tomb Kings of Khemri"

# Other names that should resolve to this faction.
ALIASES = [
    "Tomb Kings",
    "TK",
    "Khemri",
    "Tomb Kings of Khemri",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Settra": "Settra the Imperishable",
    "Apophas": "Prince Apophas",
}

CHARACTERS = {
    "Nekaph": {
        # https://tow.whfb.app/unit/nekaph - 120 pts
        "points": 120,
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
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "The Flail of Conquered Kings",
            "Shield": False,
            "SpecialRules": ["Dry as Dust", "Flammable", "Herald of Despair", "Indomitable (2)", "Killing Blow", "Nehekharan Undead", "Regeneration (5+)", "Settra's Champion", "Killing Blow 5+", "Sworn Protector"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["The Flail of Conquered Kings"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": ["The Flail of Conquered Kings"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Prince Apophas": {
        # https://tow.whfb.app/unit/prince-apophas - 130 pts
        # Shooting is not simulated, so these are left out of the options: swarming
        # mass.
        "points": 130,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 1,
            "Wounds": 4,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ambushers", "Fly (9)", "Indomitable (2)", "Khopesh", "Loner", "Nehekharan Undead", "Regeneration (5+)", "Scarab Prince", "Usirian's Reaper", "Terror"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
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
    "Settra the Imperishable": {
        # https://tow.whfb.app/unit/settra-the-imperishable - 445 pts
        # Also has a profile for Chariot of the Gods (M- WS- BS- S5 T5 W8 I- A- Ld-);
        # not simulated.
        # Also has a profile for Skeletal Steed (x4) (M8 WS2 BS- S3 T- W- I2 A1 Ld-);
        # not simulated.
        # Settra's own Wounds are '-': he uses the Chariot of the Gods' W8 (and its
        # T5, the same as his).
        "points": 445,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 7,
            "BallisticSkill": 3,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 8,
            "Attacks": 5,
            "Leadership": 10,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "The Blessed Blade of Ptra",
            "Shield": False,
            "SpecialRules": ["Commander of Legions", "Curse of the Necropolis", "Dry as Dust", "Flammable", "Impact Hits (2D3)", "Indomitable (3)", "Lore of Nehekhara", "My Will Be Done", "Nehekharan Undead", "Regeneration (5+)", "Settra Does Not Kneel!", "Settra the Great"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "NamedCharacter",
            "WizardLevel": 1,
            "Lores": ["Necromancy"],
        },
        "equipment_options": {
            "weapons": ["The Blessed Blade of Ptra"],
            "armor": [],
            "shield": False,
            "items": ["The Blessed Blade of Ptra", "The Chariot of the Gods", "The Crown of Nehekhara", "The Scarab Brooch of Usirian"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Arch Necrotect": {
        # https://tow.whfb.app/unit/arch-necrotect - 90 pts
        "points": 90,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dry as Dust", "Flammable", "Immortal Overseer", "Khopesh", "Nehekharan Undead", "Regeneration (5+)", "Stone Shaper"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Incantation Scroll"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Whip"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "High Priest": {
        # https://tow.whfb.app/unit/high-priest - 140 pts
        "points": 140,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arise!", "Curse of the Necropolis", "Indomitable (1)", "Khopesh", "Lore of Nehekhara", "Nehekharan Undead", "Regeneration (5+)", "From Beneath the Sands"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 3,
            "Lores": ["Elementalism", "Illusion", "Necromancy"],
            "OptionalRules": ["Incantation Scrolls"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Tomb Kings)", "Barded Skeletal Steed", "Necrolith Bone Dragon"]
        }
    },
    "Mortuary Priest": {
        # https://tow.whfb.app/unit/mortuary-priest - 55 pts
        "points": 55,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Tomb King",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arise!", "Curse of the Necropolis", "Indomitable (1)", "Khopesh", "Lore of Nehekhara", "Nehekharan Undead", "Regeneration (5+)", "From Beneath the Sands"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Elementalism", "Illusion", "Necromancy"],
            "OptionalRules": ["Incantation Scrolls"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Tomb Kings)", "Barded Skeletal Steed"]
        }
    },
    "Necrotect": {
        # https://tow.whfb.app/unit/necrotect - 55 pts
        "points": 55,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dry as Dust", "Eternal Taskmaster", "Flammable", "Khopesh", "Nehekharan Undead", "Regeneration (6+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Incantation Scroll"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Whip"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Royal Herald": {
        # https://tow.whfb.app/unit/royal-herald - 60 pts
        "points": 60,
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
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Banner of the King", "Dry as Dust", "Flammable", "Indomitable (1)", "Khopesh", "Nehekharan Undead", "Regeneration (5+)", "Sworn Protector"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail", "Great Weapon", "Halberd", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Tomb Kings)", "Barded Skeletal Steed", "Skeleton Chariot"]
        }
    },
    "Tomb King": {
        # https://tow.whfb.app/unit/tomb-king - 160 pts
        "points": 160,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Tomb King",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Curse of the Necropolis", "Dry as Dust", "Flammable", "Indomitable (2)", "Khopesh", "My Will Be Done", "Nehekharan Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail", "Great Weapon", "Halberd", "Cavalry Spear"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Tomb Kings)", "Barded Skeletal Steed", "Skeleton Chariot", "Necrolith Bone Dragon", "Khemrian Warsphinx"]
        }
    },
    "Tomb Prince": {
        # https://tow.whfb.app/unit/tomb-prince - 90 pts
        "points": 90,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Tomb King",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Curse of the Necropolis", "Dry as Dust", "Flammable", "Indomitable (2)", "Khopesh", "My Will Be Done", "Nehekharan Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail", "Great Weapon", "Halberd", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Tomb Kings)", "Barded Skeletal Steed", "Skeleton Chariot"]
        }
    },
}

# Regular (non-character) units go here.
UNITS = {}


# Special rules carried by this faction's characters. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {
    "Ambushers": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ambushers",
        "text": (
            "A unit with this special rule may be held in reserve rather than be "
            "deployed at the start of the game. From the beginning of round two "
            "onwards, roll a D6 during each of your Start of Turn sub-phases for "
            "each unit of Ambushers in your army that is held in reserve. On a roll "
            "of 1-3, the unit is delayed until your next turn at least. On a roll "
            "of 4+, the unit arrives, entering the battle as reinforcements during "
            "the Compulsory Moves sub-phase. The unit may be placed on any edge of "
            "the battlefield, chosen by its controlling player, but cannot be "
            "placed within 8\" of an enemy model. If any Ambushers are still held in "
            "reserve by the start of round five, they arrive automatically."
        ),
    },
    "Arise!": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/arise",
        "text": (
            "During the Command sub-phase of their turn, if they are not engaged in "
            "combat, this character may attempt to resurrect the fallen by making a "
            "Leadership test (using their own Leadership). If this test is passed, "
            "a single friendly unit that has the Nehekharan Undead special rule and "
            "is within 12\" of this character recovers a number of lost Wounds. "
            "However, magically repairing gigantic undead constructs is much harder "
            "than raising skeletons from the sand. Therefore, how many Wounds are "
            "recovered depends upon the unit's troop type and this character's "
            "Level of Wizardry: - If the unit's troop type is regular infantry, "
            "heavy infantry or swarms, it recovers a number of Wounds equal to this "
            "[...]"
        ),
    },
    "Banner of the King": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/banner-of-the-king",
        "text": (
            "A Royal Herald that has been upgraded to be your Battle Standard "
            "Bearer replaces the \"Hold your Ground\" rule given in the Warhammer: "
            "the Old World rulebook with the version given below: \"Hold Your "
            "Ground\" Friendly units within the Battle Standard Bearer's Command "
            "range may re-roll any failed Leadership test. In addition, friendly "
            "units within the Battle Standard Bearer's Command range reduce the "
            "number of Wounds lost due to the Unstable special rule by D3. Note "
            "that this is not cumulative with the Indomitable (X) special rule. If "
            "a unit is affected by both, use the highest value."
        ),
    },
    "Commander of Legions": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/commander-of-legions",
        "text": (
            "Settra gains the Arise! special rule and, unlike other models with "
            "this special rule, may use it even when engaged in combat."
        ),
    },
    "Curse of the Necropolis": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/curse-of-the-necropolis",
        "text": (
            "If a model with this special rule loses its last Wound to an enemy "
            "attack, the unit that made the attack must immediately make a "
            "Leadership test. If this test is failed, the enemy unit suffers D3 "
            "Strength 2 hits, each with an AP of -."
        ),
    },
    "Dry as Dust": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dry-as-dust",
        "text": (
            "Each time this model suffers an unsaved wound from a Flaming Attack, "
            "your opponent may roll a D6. On a roll of 1-3, the flames quickly die "
            "down and this model escapes further harm. On a roll of 4+, the flames "
            "take hold and this model loses one additional Wound. Note that excess "
            "wounds caused to a model will have no additional effect except in the "
            "case of a character that is part of a challenge, in which case this "
            "special rule counts for Overkill. Excess wounds do not 'spill over' "
            "onto other models in the unit."
        ),
    },
    "Eternal Taskmaster": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/eternal-taskmaster",
        "text": (
            "During the Command sub-phase of their turn, this character may attempt "
            "to drive a unit they have joined to greater efforts by making a "
            "Leadership test (using their own Leadership). If this test is passed, "
            "until your next Start of Turn sub-phase this character and any unit "
            "they have joined gains the Extra Attacks (+1) and Hatred (all enemies) "
            "special rules."
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
    "From Beneath the Sands": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/from-beneath-the-sands",
        "text": (
            "During the Command sub-phase of their turn, if they are not engaged in "
            "combat, this character may choose a single friendly unit that has both "
            "the Nehekharan Undead and the Ambushers special rules, and that is "
            "currently held in reserve, and attempt to summon it by making a "
            "Leadership test (using their own Leadership): - If this test is "
            "passed, the chosen unit is successfully summoned and can be placed on "
            "the battlefield anywhere completely within 12\" of this model, but not "
            "within 6\" of any enemy models. The unit cannot charge during this turn "
            "and counts as having moved for the purposes of shooting, but can "
            "otherwise act as normal. - If this test is failed, the Ambushers pay "
            "no heed to this [...]"
        ),
    },
    "Herald of Despair": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/herald-of-despair",
        "text": (
            "Any enemy unit that is in base contact with Nekaph or a unit he has "
            "joined must roll an extra D6 when making a Fear or Terror test, and "
            "discard the lowest result."
        ),
    },
    "Immortal Overseer": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/immortal-overseer",
        "text": (
            "During the Command sub-phase of their turn, this character may attempt "
            "to drive a single friendly unit within their Command range to greater "
            "efforts by making a Leadership test (using their own Leadership). If "
            "this test is passed, until your next Start of Turn sub-phase that unit "
            "gains a +D3 modifier to its Initiative characteristic (to a maximum of "
            "10)."
        ),
    },
    "Impact Hits": {
        "status": None,
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
    "Indomitable": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/indomitable",
        "text": (
            "A unit with this special rule reduces the number of wounds suffered "
            "due to the Unstable special rule by the number shown in brackets "
            "(shown here as 'X'). Note that this special rule is not cumulative. If "
            "two or more models in a unit have this special rule, use the highest "
            "value for the entire unit. For example, if a character with "
            "Indomitable (2) joins a unit with Indomitable (1), the whole unit uses "
            "the character's Indomitable (2) special rule."
        ),
    },
    "Khopesh": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/khopesh",
        "text": (
            "A hand weapon carried by a model with this special rule has an Armour "
            "Piercing characteristic of -1. Note that this special rule only "
            "applies to a single, ordinary hand weapon and does not apply to a "
            "model's mount (should it have one). If the model is using two hand "
            "weapons or any other sort of weapon, this special rule ceases to "
            "apply."
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
    "Loner": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/loner",
        "text": (
            "A character with this special rule cannot be your General and cannot "
            "join a unit without this special rule. A unit with this special rule "
            "cannot be joined by a character without this special rule."
        ),
    },
    "Lore of Nehekhara": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-nehekhara",
        "text": (
            "The magic of Nehekhara was perfected millennia ago and has remained "
            "unchanged in the long centuries since. The wording of every "
            "incantation used in the preservation and reanimating of the dead is "
            "recorded on dusty papyrus in the mysterious hieroglyphs of Nehekhara’s "
            "ancient language, to be uttered aloud in long, monotonous ritual. A "
            "Wizard with the 'Lore of Nehekhara' special rule may discard one of "
            "their randomly generated spells as normal. When they do so, they may "
            "select instead either the signature spell of their chosen Lore of "
            "Magic, or one of the spells listed below. Lore of Nehekhara Lore"
        ),
    },
    "My Will Be Done": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/my-will-be-done",
        "text": (
            "During the Command sub-phase of their turn, this character may attempt "
            "to exert their will upon those around them by making a Leadership test "
            "(using their own Leadership). If this test is passed, choose one of "
            "the following modifiers. Until your next Start of Turn sub-phase this "
            "character, their mount and any unit they have joined gain that "
            "modifier (to a maximum of 10): - \"Forward to Glory!\": +D3 Movement. - "
            "\"My Worthy Champions!\": +1 Weapon Skill. - \"Strike like the Cobra!\": "
            "+D3 Initiative. Note that this special rule is not cumulative. In "
            "other words, using it more than once on the same unit during the same "
            "turn has no further effect."
        ),
    },
    "Nehekharan Undead": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/nehekharan-undead",
        "text": (
            "Models with this special rule are 'Undead'. Undead models cannot march "
            "(unless they have the Fly (X) special rule and choose to move by "
            "flying). In addition, all Undead models have the following universal "
            "special rules: - Fear - Immune To Psychology - Unbreakable - Unstable "
            "A character with this special rule cannot join a unit without this "
            "special rule, and vice versa."
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
    "Scarab Prince": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/scarab-prince",
        "text": (
            "Should Prince Apophas lose his last Wound, before his model is removed "
            "from play, all enemy units within 2D6\" of him suffer 2D6 Strength 2 "
            "hits with an AP of -1."
        ),
    },
    "Settra Does Not Kneel!": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/settra-does-not-kneel",
        "text": (
            "Settra must always accept a challenge unless Nekaph, Emissary of "
            "Settra is engaged in the same combat. In which case, Nekaph must "
            "accept the challenge on Settra's behalf."
        ),
    },
    "Settra the Great": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/settra-the-great",
        "text": (
            "If your army includes Settra, he must be the army's General and must "
            "be chosen to be the army's Hierophant, even if he does not have the "
            "highest Level of Wizardry in your army. In addition, Settra has a "
            "Command Range of 18\"."
        ),
    },
    "Settra's Champion": {
        "status": "partial",
        "url": "https://tow.whfb.app/special-rules/settras-champion",
        "text": (
            "Nekaph must always issue and accept challenges (if possible). However, "
            "challenges issued by Nekaph cannot be refused. In addition, whilst "
            "engaged in a challenge, Nekaph strikes a Killing Blow if he rolls a "
            "natural 5 or 6 when making a roll To Wound, rather than the usual 6."
        ),
    },
    "Stone Shaper": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/stone-shaper",
        "text": (
            "During the Command sub-phase of their turn, if they are not engaged in "
            "combat, this character may nominate a single friendly Necrolith "
            "Colossus, Necrosphinx, unit of Ushabti or unit of Venerable Ushabti "
            "that is within their Command range. Until the end of this turn, the "
            "nominated unit improves the Regeneration value of its Regeneration "
            "save by 1."
        ),
    },
    "Sworn Protector": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/sworn-protector",
        "text": (
            "Should a Monarch of Nehekhara model suffer a hit whilst within 3\" of "
            "this model, you may choose to transfer that hit and all of its effects "
            "onto this model."
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
    "Usirian's Reaper": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/usirians-reaper",
        "text": (
            "After deployment, nominate a single character in your opponent's "
            "Muster List. Apophas may re-roll any failed rolls To Hit or To Wound "
            "made against that character. In addition, any hits inflicted by "
            "Apophas against the nominated character gain the Magical Attacks "
            "special rule."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
