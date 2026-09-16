"""Grand Cathay.

Profiles from https://tow.whfb.app/army/grand-cathay, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Grand Cathay"

# Other names that should resolve to this faction.
ALIASES = [
    "Cathay",
    "Empire of Grand Cathay",
    "Grand Cathay",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Miao": "Miao Ying",
    "Storm Dragon": "Miao Ying",
}

CHARACTERS = {
    "Miao Ying": {
        # https://tow.whfb.app/unit/miao-ying - 485 pts
        # Also has a profile for Dragon Form (M8 WS8 BS3 S7 T6 W7 I6 A6 Ld10); not
        # simulated.
        # Troop type by form: Heavy Infantry, Behemoth; the first is used.
        "points": 485,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 7,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 7,
            "Wounds": 7,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Cathayan",
            "Armor": "Heavy Armor",
            "Weapon": "Talons of the Storm",
            "Shield": False,
            "SpecialRules": ["Celestial Forged Armour (5+)", "Ward5", "Disdain of the Dragons", "Hatred (Warriors of Chaos & Daemonic models)", "Fly (9) (Dragon Form only)", "Large Target (Dragon Form only)", "Magic Resistance (-1)", "Mastery of the Storm Winds", "Mastery of the Elemental Winds", "Rallying Cry (Human Form only)", "Stomp Attacks (D6) (Dragon Form only)", "Stubborn", "Supreme Matriarch of Nan-Gau", "Swiftstride (Dragon Form only)", "Terror (Dragon Form only)", "Transformation of the Dragon", "Will of the Dragons", "Wrath of the Storm"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
            "WizardLevel": 4,
            "Lores": ["Battle Magic", "Elementalism", "High Magic"],
        },
        "equipment_options": {
            "weapons": ["Talons of the Storm"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": ["Talons of the Storm"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Astromancer": {
        # https://tow.whfb.app/unit/astromancer - 65 pts
        "points": 65,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Cathayan",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Magical Attacks", "Magic Resistance (-1)", "Mastery of the Elemental Winds"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "Illusion", "High Magic"],
            "OptionalRules": ["Lore of Yang", "Lore of Yin"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Cathayan Horse"]
        }
    },
    "Gate Keeper": {
        # https://tow.whfb.app/unit/gate-keeper - 45 pts
        "points": 45,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Cathayan",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Harmony of Stone & Steel", "Will of the Dragons"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Celestial Blade", "Cathayan Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Cathayan Warhorse"]
        }
    },
    "Gate Master": {
        # https://tow.whfb.app/unit/gate-master - 80 pts
        "points": 80,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 7,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Cathayan",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Harmony of Stone & Steel", "Will of the Dragons"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Celestial Blade", "Cathayan Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Cathayan Warhorse"]
        }
    },
    "Lord Magistrate": {
        # https://tow.whfb.app/unit/lord-magistrate - 65 pts
        # Shooting is not simulated, so these are left out of the options: Dragon fire
        # bombs, Gunpowder bombs.
        "points": 65,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Cathayan",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Grand Strategist", "Harmony of Stone & Steel", "Will of the Dragons"],
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
            "mounts": ["Sky Lantern"]
        }
    },
    "Shugengan General": {
        # https://tow.whfb.app/unit/shugengan-general - 145 pts
        # Also has a profile for Great Spirit Longma (M8 WS5 BS- S5 T- W- I4 A3 Ld-);
        # not simulated.
        # Shooting is not simulated, so these are left out of the options: dragon fire
        # pistol.
        "points": 145,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 6,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Cathayan",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (2)", "Celestial Forged Armour (5+)", "Ward5", "Counter Charge", "Fear", "Fly (9)", "Impact Hits (D3+1)", "Mastery of the Elemental Winds", "Swiftstride", "Will of the Dragons"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "Illusion", "High Magic"],
            "OptionalRules": ["Lore of Yang", "Lore of Yin"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Iron Talons", "Celestial Blade", "Cathayan Lance"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Shugengan Lord": {
        # https://tow.whfb.app/unit/shugengan-lord - 220 pts
        # Also has a profile for Great Spirit Longma (M8 WS5 BS- S5 T- W- I4 A3 Ld-);
        # not simulated.
        # Shooting is not simulated, so these are left out of the options: dragon fire
        # pistol.
        "points": 220,
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 6,
            "Wounds": 7,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Cathayan",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (2)", "Celestial Forged Armour (5+)", "Ward5", "Counter Charge", "Fear", "Fly (9)", "Impact Hits (D3+1)", "Mastery of the Elemental Winds", "Swiftstride", "Will of the Dragons"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Character",
            "WizardLevel": 2,
            "Lores": ["Battle Magic", "Elementalism", "Illusion", "High Magic"],
            "OptionalRules": ["Lore of Yang", "Lore of Yin"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Iron Talons", "Celestial Blade", "Cathayan Lance"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Strategist": {
        # https://tow.whfb.app/unit/strategist - 40 pts
        # Shooting is not simulated, so these are left out of the options: Dragon fire
        # bombs, Gunpowder bombs.
        "points": 40,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Cathayan",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Grand Strategist", "Harmony of Stone & Steel", "Will of the Dragons"],
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
            "mounts": []
        }
    },
    "Supreme Astromancer": {
        # https://tow.whfb.app/unit/supreme-astromancer - 125 pts
        "points": 125,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Cathayan",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Magical Attacks", "Magic Resistance (-1)", "Mastery of the Elemental Winds"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 2,
            "Lores": ["Battle Magic", "Elementalism", "Illusion", "High Magic"],
            "OptionalRules": ["Lore of Yang", "Lore of Yin"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Cathayan Horse"]
        }
    },
}

# Regular (non-character) units go here.
UNITS = {}


# Special rules carried by this faction's characters. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {
    "Armoured Hide": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/armoured-hide",
        "text": (
            "The hide of some creatures forms natural armour and improves their "
            "armour value (and that of their rider). By how much armour value is "
            "improved varies from model to model, as shown in brackets after the "
            "name of this special rule (shown here as 'X'). Note that a model that "
            "wears no armour is considered to have an armour value of 7+ for the "
            "purposes of rules that improve armour value."
        ),
    },
    "Celestial Forged Armour": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/celestial-forged-armour-x",
        "text": (
            "A model with this special rule has a Ward save against any wounds "
            "suffered. The armour value of this Ward save is shown in brackets "
            "after the name of this special rule (shown here as 'X+'). In addition, "
            "a Wizard with this special rule may wear armour without penalty."
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
    "Disdain of the Dragons": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/disdain-of-the-dragons",
        "text": (
            "Enemy models that wish to issue a challenge whilst within Miao Ying's "
            "Command range must first make a Leadership test (using their own "
            "Leadership). If the enemy model wishes to issue a challenge whilst "
            "engaged in a combat Miao Ying is also engaged in, it must apply a +1 "
            "modifier to the dice roll if she is in her Human form, and a +2 "
            "modifier if she is in her Dragon form: - If this test is passed, the "
            "challenge is issued as normal. - If this test is failed, the challenge "
            "dies on the enemy's lips and goes unissued. Finally, challenges issued "
            "by Miao Ying cannot be refused."
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
    "Grand Strategist": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/grand-strategist",
        "text": (
            "Unless this character is fleeing, all friendly units within their "
            "Command range, except your General, can use this character's "
            "Leadership characteristic instead of their own. In addition, once per "
            "turn a friendly unit that wins a round of combat whilst within this "
            "character's Command range may choose to Fall Back in Good Order rather "
            "than making a follow up or pursuit move."
        ),
    },
    "Harmony of Stone & Steel": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/harmony-of-stone-and-steel",
        "text": (
            "A unit joined by a character with this special rule may re-roll any "
            "failed Leadership test when attempting to reform after running down a "
            "foe, when attempting to redirect a charge, or when making a Restraint "
            "test."
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
    "Mastery of the Elemental Winds": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/mastery-of-the-elemental-winds",
        "text": (
            "Once per turn, a Wizard within your army that has this special rule "
            "and that is within 6\" of one or more friendly Wizards that also have "
            "this special rule may apply a +1 modifier to a Casting roll. Note that "
            "this is a modifier to the result of a roll - it does not negate a roll "
            "of a natural double 1."
        ),
    },
    "Mastery of the Storm Winds": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/mastery-of-the-storm-winds",
        "text": (
            "Miao Ying may discard up to two of her randomly generated spells "
            "(rather than the usual one). When she does so, she may replace them "
            "with spells chosen from the Lore of Yang, the Lore of Yin, the "
            "signature spell of her chosen Lore of Magic, or with the following "
            "spell: The Storm Dragon's Fury The Storm Dragon's Fury"
        ),
    },
    "Rallying Cry": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/rallying-cry",
        "text": (
            "During the Command sub-phase of their turn, if they are not engaged in "
            "combat, this character may nominate a single fleeing friendly unit "
            "that is within their Command range. The nominated unit immediately "
            "makes a Rally test. If this test is failed, the unit may attempt to "
            "rally again as normal during the Rally sub-phase."
        ),
    },
    "Stomp Attacks": {
        "status": None,
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
    "Supreme Matriarch of Nan-Gau": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/supreme-matriarch-of-nan-gau",
        "text": (
            "If your army includes Miao Ying, she must be the army's General. In "
            "addition, 0-1 unit of Jade Warriors or 0-1 unit of Jade Lancers in her "
            "army may be upgraded to Celestial Dragon Guard for +2 points per "
            "model. Celestial Dragon Guard have a +1 modifier to their Weapon Skill "
            "and Leadership characteristics (to a maximum of 10) and gain the "
            "Celestial Armour (6+) special rule."
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
    "Transformation of the Dragon": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/transformation-of-the-dragon",
        "text": (
            "A Cathayan Dragon may adopt both Human and Dragon forms. To represent "
            "this, you may choose a Cathayan Dragon's form at the start of the game "
            "by simply placing the appropriate model on the battlefield during "
            "deployment. Each form has its own profile of characteristics."
        ),
    },
    "Will of the Dragons": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/will-of-the-dragons",
        "text": (
            "A unit with this special rule may re-roll a failed Panic test when a "
            "friendly unit is destroyed whilst within 6\" of it, or when it is fled "
            "through by a friendly unit."
        ),
    },
    "Wrath of the Storm": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/wrath-of-the-storm",
        "text": (
            "All units of Jade Warriors and Jade Lancers included in an army that "
            "is led by Miao Ying gain the Hatred (Warriors of Chaos & Daemonic "
            "models) special rule."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
