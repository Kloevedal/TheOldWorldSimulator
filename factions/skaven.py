"""Skaven.

Profiles from https://tow.whfb.app/army/skaven, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Skaven"

# Other names that should resolve to this faction.
ALIASES = [
    "Skaven",
    "Ratmen",
    "Clans of Skaven",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Warlord": "Skaven Warlord",
    "Chieftain": "Skaven Chieftain",
    "Assassin": "Master Assassin",
}

CHARACTERS = {
    "Grey Seer": {
        # https://tow.whfb.app/unit/grey-seer - 185 pts
        "points": 185,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Lore of the Horned Rat", "Magical Attacks", "Magic Resistance (-1)", "Scurry Away", "Verminous Valour", "Warband", "Warpstone Weapons"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Elementalism", "Illusion"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": ["Warpstone Tokens"],
        },
        "mount_options": {
            "mounts": ["Screaming Bell"]
        }
    },
    "Master Assassin": {
        # https://tow.whfb.app/unit/master-assassin - 90 pts
        # Shooting is not simulated, so these are left out of the options: throwing
        # weapons.
        "points": 90,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 8,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 8,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Two Hand Weapons",
            "Shield": False,
            "SpecialRules": ["Ambushers", "Eshin Infiltration", "Evasive", "Feigned Flight", "Fire & Flee", "Hidden", "Move Through Cover", "Poisoned Attacks", "Scurry Away", "Verminous Valour", "Warpstone Weapons"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
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
    "Plague Priest": {
        # https://tow.whfb.app/unit/plague-priest - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 6,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Cloud of Flies", "Frenzy", "Lore of the Horned Rat", "Magical Attacks", "Scurry Away", "Verminous Valour", "Warband", "Warpstone Weapons"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 0,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Plague Censer"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Plague Furnace"]
        }
    },
    "Skaven Chieftain": {
        # https://tow.whfb.app/unit/skaven-chieftain - 45 pts
        "points": 45,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 6,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 6,
            "Race": "Skaven",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Scurry Away", "Verminous Valour", "Warband", "Warpstone Weapons"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Skaven Warlord": {
        # https://tow.whfb.app/unit/skaven-warlord - 90 pts
        "points": 90,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 7,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 7,
            "Race": "Skaven",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Scurry Away", "Verminous Valour", "Warband", "Warpstone Weapons"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Halberd"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Warlock Engineer": {
        # https://tow.whfb.app/unit/warlock-engineer - 35 pts
        # Shooting is not simulated, so these are left out of the options: Warplock
        # musket, Warplock pistol.
        "points": 35,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 5,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Lore of the Horned Rat", "Magical Attacks", "Scurry Away", "Verminous Valour", "Warband", "Warpstone Weapons"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 0,
            "Lores": ["Battle Magic", "Elementalism"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": ["Warpstone Tokens"],
        },
        "mount_options": {
            "mounts": []
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
    "Cloud of Flies": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/cloud-of-flies",
        "text": (
            "Any enemy model that directs its attacks against this character during "
            "the Combat phase suffers a -1 modifier to its rolls To Hit."
        ),
    },
    "Eshin Infiltration": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/eshin-infiltration",
        "text": (
            "When a friendly unit of Gutter Runners with the Ambushers special rule "
            "arrives from reserve, it can be placed on the battlefield anywhere "
            "completely within 12\" of a revealed Master Assassin, but not within 6\" "
            "of any enemy models (rather than entering the battle as "
            "reinforcements). The unit cannot charge during this turn and counts as "
            "having moved for the purposes of shooting, but can otherwise act as "
            "normal. Note that this character cannot use this special rule whilst "
            "it remains hidden."
        ),
    },
    "Evasive": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/evasive",
        "text": (
            "Once per turn, when a unit in which the majority of the models have "
            "this special rule is declared the target during the enemy Shooting "
            "phase, that unit may choose to Fall Back in Good Order, fleeing "
            "directly away from the enemy unit shooting at it. Once this unit has "
            "completed its move, the enemy unit may continue with its shooting as "
            "declared."
        ),
    },
    "Feigned Flight": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/feigned-flight",
        "text": (
            "If this unit chooses to Flee (or Fire & Flee) as a charge reaction, it "
            "automatically rallies at the end of its move."
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
    "Frenzy": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/frenzy",
        "text": (
            "During a turn in which it made a charge move, or during the turn after "
            "it made a follow up move, a Frenzied model has a +1 modifier to its "
            "Attacks characteristic. This modifier does not apply to the model’s "
            "mount (in the case of a cavalry model), to the beasts that draw it (in "
            "the case of a chariot), or to its rider (in the case of a monster). In "
            "addition: - If the majority of the models in a unit are Frenzied, the "
            "unit automatically passes any Fear, Panic or Terror tests it is "
            "required to make. - If a unit that includes one or more Frenzied "
            "models is able to declare a charge during the Declare Charges & Charge "
            "Reactions sub-phase of its turn, it must do so. - If the majority of "
            "the models [...]"
        ),
    },
    "Hidden": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/hidden-skaven",
        "text": (
            "Master Assassins are not placed on the battlefield at the start of the "
            "game. Instead, they are 'hidden' within a friendly Skaven unit whose "
            "troop type is infantry and that has a Unit Strength of ten or more. "
            "Make a note of which unit each Master Assassin is hiding within. A "
            "hidden Master Assassin may be revealed during any Start of Turn sub- "
            "phase or at the start of any Combat phase. Position the revealed "
            "Master Assassin as you would a character that has joined the unit. If "
            "a unit in which a Master Assassin is hiding is destroyed or flees the "
            "battlefield before the Master Assassin is revealed, the Master "
            "Assassin is removed as a casualty. A Master Assassin cannot be your "
            "army General."
        ),
    },
    "Lore of the Horned Rat": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-the-horned-rat",
        "text": (
            "Skaven believe all magic originates from the same source, their "
            "powerful and fickle god – the Horned Rat. In truth, the potent and "
            "destructive magic of the Skaven relies upon the manipulation of the "
            "Winds of Magic, without which even the most devout and cunning Skaven "
            "would be unable to weave the simplest spell. A Wizard with the 'Lore "
            "of the Horned Rat' special rule may discard one of their randomly "
            "generated spells as normal. When they do so, they may select instead "
            "either the signature spell of their chosen Lore of Magic, or one of "
            "the spells listed below. Lore of the Horned Rat Lore"
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
    "Poisoned Attacks": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/poisoned-attacks",
        "text": (
            "If a model with Poisoned Attacks rolls a natural 6 when making a roll "
            "To Hit, it may apply a +2 modifier to that hit’s roll To Wound. Unless "
            "otherwise stated, a model with this special rule may use it when "
            "making both shooting and combat attacks. Any spells cast by the model "
            "are unaffected, as are any attacks made with magic weapons. Note that "
            "if an attack needs a To Hit roll of 7+, or hits automatically, this "
            "special rule cannot be used."
        ),
    },
    "Scurry Away": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/scurry-away",
        "text": (
            "Models with this special rule have a +1 modifier to the result of any "
            "Flee roll they make."
        ),
    },
    "Verminous Valour": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/verminous-valour",
        "text": (
            "Unless they are engaged in a challenge, a character with this special "
            "rule that has joined a unit that has a Unit Strength of 10 or more may "
            "voluntarily 'retire' to the rear of the unit at any time, moving "
            "through the ranks and taking up a position away from the combat. "
            "Should they do so, they are no longer within the fighting rank and "
            "cannot make any attacks or have attacks directed against them. "
            "However, the unit may still use this character's Leadership."
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
    "Warpstone Weapons": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/warpstone-weapons",
        "text": (
            "A hand weapon carried by a model with this special rule has the "
            "Magical Attacks special rule and an Armour Piercing characteristic of "
            "-1. Note that this special rule only applies to a single, ordinary "
            "hand weapon. If the model is using two hand weapons or any other sort "
            "of weapon, this special rule ceases to apply."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
