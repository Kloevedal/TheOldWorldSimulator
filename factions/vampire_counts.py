"""Vampire Counts.

Profiles from https://tow.whfb.app/army/vampire-counts, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Vampire Counts"

# Other names that should resolve to this faction.
ALIASES = [
    "Vampire Counts",
    "VC",
    "Vampires",
    "Undead",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Necromancer": "Master Necromancer",
    "Acolyte": "Necromantic Acolyte",
    "Banshee": "Tomb Banshee",
    "Ghoul King": "Strigoi Ghoul King",
}

CHARACTERS = {
    "Cairn Wraith": {
        # https://tow.whfb.app/unit/cairn-wraith - 50 pts
        "points": 50,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 6,
            "Race": "Spirit",
            "Armor": None,
            "Weapon": "Spectral Scythe",
            "Shield": False,
            "SpecialRules": ["Ethereal", "Indomitable (1)", "Necromantic Undead", "Regeneration (6+)", "Terror"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Spectral Scythe"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Master Necromancer": {
        # https://tow.whfb.app/unit/master-necromancer - 130 pts
        "points": 130,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Necromancer",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dark Vitality", "Indomitable (1)", "Invocation of Nehek", "Lore of Undeath", "Necromantic Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 3,
            "Lores": ["Dark Magic", "Illusion", "Necromancy"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Nightmare", "Mortis Engine", "Abyssal Terror", "Zombie Dragon"]
        }
    },
    "Necromantic Acolyte": {
        # https://tow.whfb.app/unit/necromantic-acolyte - 60 pts
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
            "Race": "Necromancer",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dark Vitality", "Indomitable (1)", "Invocation of Nehek", "Lore of Undeath", "Necromantic Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Dark Magic", "Illusion", "Necromancy"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Nightmare", "Mortis Engine"]
        }
    },
    "Strigoi Ghoul King": {
        # https://tow.whfb.app/unit/strigoi-ghoul-king - 145 pts
        "points": 145,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 7,
            "Wounds": 3,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Vampire",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dark Vitality", "Flammable", "Hatred (all enemies)", "Indomitable (1)", "Lore of Undeath", "Necromantic Undead", "Poisoned Attacks", "Regeneration (5+)", "The Hunger"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 0,
            "Lores": ["Battle Magic", "Dark Magic", "Necromancy"],
            "OptionalRules": ["Vampiric Powers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Terrorgheist"]
        }
    },
    "Tomb Banshee": {
        # https://tow.whfb.app/unit/tomb-banshee - 90 pts
        "points": 90,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Spirit",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ethereal", "Indomitable (1)", "Magical Attacks", "Necromantic Undead", "Regeneration (6+)", "Terror", "Wailing Dirge"],
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
            "mounts": []
        }
    },
    "Vampire Count": {
        # https://tow.whfb.app/unit/vampire-count - 160 pts
        "points": 160,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 7,
            "BallisticSkill": 5,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Vampire",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dark Vitality", "Flammable", "Indomitable (2)", "Lore of Undeath", "Necromantic Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 0,
            "Lores": ["Dark Magic", "Illusion", "Necromancy"],
            "OptionalRules": ["Vampiric Powers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Lance"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Nightmare", "Coven Throne", "Abyssal Terror", "Zombie Dragon"]
        }
    },
    "Vampire Thrall": {
        # https://tow.whfb.app/unit/vampire-thrall - 75 pts
        "points": 75,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Vampire",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Banner of the Count", "Dark Vitality", "Flammable", "Indomitable (1)", "Lore of Undeath", "Necromantic Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 0,
            "Lores": ["Dark Magic", "Illusion", "Necromancy"],
            "OptionalRules": ["Vampiric Powers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Lance"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Nightmare", "Coven Throne"]
        }
    },
    "Wight King": {
        # https://tow.whfb.app/unit/wight-king - 85 pts
        "points": 85,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Wight",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Indomitable (1)", "Killing Blow", "Necromantic Undead", "Regeneration (5+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Vampire Counts)"]
        }
    },
    "Wight Lord": {
        # https://tow.whfb.app/unit/wight-lord - 40 pts
        "points": 40,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Wight",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Killing Blow", "Necromantic Undead", "Regeneration (6+)", "Wight Banner"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Skeletal Steed (Vampire Counts)"]
        }
    },
}

# Regular (non-character) units go here.
UNITS = {}


# Special rules carried by this faction's characters. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {
    "Banner of the Count": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/banner-of-the-count",
        "text": (
            "A Vampire Thrall that has been upgraded to be your Battle Standard "
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
    "Dark Vitality": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dark-vitality",
        "text": (
            "Models with this special rule are not subject to the Death of a "
            "General rule. In addition, unless they have joined a unit that does "
            "not have this special rule they (and their mounts) can march as "
            "normal."
        ),
    },
    "Ethereal": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/ethereal",
        "text": (
            "Ethereal creatures treat all terrain as open ground for the purposes "
            "of movement. They cannot end their movement inside impassable terrain, "
            "though they can pass through it. In addition, Ethereal creatures can "
            "only be wounded by Magical attacks. Characters that are not Ethereal "
            "cannot join units that are, and vice versa."
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
    "Invocation of Nehek": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/invocation-of-nehek",
        "text": (
            "During the Command sub-phase of their turn, if they are not engaged in "
            "combat, this character may attempt to resurrect the fallen by making a "
            "Leadership test (using their own Leadership). If this test is passed, "
            "a single friendly unit that has the Necromantic Undead special rule "
            "and is within 12\" of this character recovers a number of lost Wounds. "
            "However, magically repairing great Undead beasts is much harder than "
            "raising Zombies from the dirt. Therefore, how many Wounds are "
            "recovered depends upon the unit's troop type and this character's "
            "Level of Wizardry: - If the unit's troop type is regular infantry or "
            "heavy infantry, it recovers a number of Wounds equal to this "
            "character's Level of [...]"
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
    "Lore of Undeath": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-undeath",
        "text": (
            "Mystery shrouds the study of Necromancy. To learn this dark art, an "
            "aspirant must find a willing tutor and become their apprentice, or "
            "acquire forbidden books rich in the secrets of undeath. It is this "
            "intrinsic mystery that drives Necromancers to become servants of the "
            "Vampire Counts, hoping to learn first-hand from the masters of "
            "undeath. A Wizard with the 'Lore of Undeath' special rule may discard "
            "one of their randomly generated spells as normal. When they do so, "
            "they may select instead either the signature spell of their chosen "
            "Lore of Magic, or one of the spells listed below. Lore of Undeath Lore"
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
    "Necromantic Undead": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/necromantic-undead",
        "text": (
            "Models with this special rule are 'Undead'. Undead models cannot march "
            "(unless they have the Fly (X) special rule and choose to move by "
            "flying). In addition, all Undead models have the following universal "
            "special rules: - Fear - Immune To Psychology - Unbreakable - Unstable "
            "A character with this special rule cannot join a unit without this "
            "special rule, and vice versa."
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
    "The Hunger": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/the-hunger",
        "text": (
            "At the end of any Combat phase in which this character inflicted one "
            "or more unsaved wounds, roll a D6. On a roll of 6, this character "
            "recovers a single lost Wound. However, so great is this character's "
            "hunger that, whenever they (and any unit they have joined) make a "
            "Pursuit roll, they roll only a single D6 (rather than the usual 2D6)."
        ),
    },
    "Wailing Dirge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/wailing-dirge",
        "text": (
            "During the Shooting phase of its turn, unless it marched during the "
            "preceding Movement phase, a model with this special rule may make a "
            "'Wailing Dirge' attack. A Wailing Dirge attack may target any enemy "
            "unit that is within 8\" of this model (including units that are engaged "
            "in combat) and that this model can draw a line of sight to, or that "
            "this model is engaged in combat with. The target must make a "
            "Leadership test with a -2 modifier to its Leadership characteristic "
            "(to a minimum of 2). If this test is failed, the target suffers a "
            "number of wounds equal to the amount by which it failed the test, with "
            "no armour or Regeneration saves permitted (Ward saves can be attempted "
            "as normal). Note [...]"
        ),
    },
    "Wight Banner": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/wight-banner",
        "text": (
            "A Wight Lord that has been upgraded to be your Battle Standard Bearer "
            "replaces the \"Hold your Ground\" rule given in the Warhammer: the Old "
            "World rulebook with the version given below: \"Hold Your Ground\" "
            "Friendly units within the Battle Standard Bearer's Command range may "
            "re-roll any failed Leadership test. In addition, friendly units within "
            "the Battle Standard Bearer's Command range reduce the number of Wounds "
            "lost due to the Unstable special rule by D3. Note that this is not "
            "cumulative with the Indomitable (X) special rule. If a unit is "
            "affected by both, use the highest value."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
