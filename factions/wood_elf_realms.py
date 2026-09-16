"""Wood Elf Realms.

Profiles from https://tow.whfb.app/army/wood-elf-realms, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Wood Elf Realms"

# Other names that should resolve to this faction.
ALIASES = [
    "Wood Elves",
    "Wood Elf",
    "Asrai",
    "Wood Elf Realms",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Araloth": "Araloth, Lord of Talsyn",
    "Orion": "Orion, the King in the Woods",
}

CHARACTERS = {
    "Araloth, Lord of Talsyn": {
        # https://tow.whfb.app/unit/araloth-lord-of-talsyn - 150 pts
        "points": 150,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 8,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 8,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Wood Elf",
            "Armor": "Heavy Armor",
            "Weapon": "Spear of Talsyn",
            "Shield": True,
            "SpecialRules": ["Boldest of the Bold", "Evasive", "Favour of the Goddess", "Ward5", "Move Through Cover", "Rallying Cry", "Skaryn the Eye Thief", "Strike First", "Stubborn"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Spear of Talsyn"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": ["Spear of Talsyn"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Orion, the King in the Woods": {
        # https://tow.whfb.app/unit/orion-the-king-in-the-woods - 405 pts
        "points": 405,
        "base_profile": {
            "Movement": 9,
            "WeaponSkill": 8,
            "BallisticSkill": 6,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 8,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 10,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "The Spear of Kurnous",
            "Shield": False,
            "SpecialRules": ["Frenzy", "Immune to Psychology", "Magic Resistance (-2)", "Move Through Cover", "Open Order*", "Stomp Attacks (D3+2)", "Strike First", "Terror", "Unbreakable"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["The Spear of Kurnous"],
            "armor": [],
            "shield": False,
            "items": ["Cloak of Isha", "Hawk's Talon", "Horn of the Wild Hunt", "The Spear of Kurnous"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Branchwraith": {
        # https://tow.whfb.app/unit/branchwraith - 80 pts
        "points": 80,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 6,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 6,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Forest Spirit",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Fear", "Flammable", "Furious Charge", "Immune to Psychology", "Lore of Athel Loren", "Magical Attacks", "Move Through Cover", "Regeneration (6+)", "Tree Spirit"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "Illusion"],
            "OptionalRules": ["Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Glade Captain": {
        # https://tow.whfb.app/unit/glade-captain - 70 pts
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbow.
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
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["The Arrow of Kurnous", "Evasive", "Fire & Flee", "Ignores Cover", "Move Through Cover", "Rallying Cry", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows", "Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Great Stag", "Warhawk", "Great Eagle"]
        }
    },
    "Glade Lord": {
        # https://tow.whfb.app/unit/glade-lord - 135 pts
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbow.
        "points": 135,
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
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["The Arrow of Kurnous", "Evasive", "Fire & Flee", "Ignores Cover", "Move Through Cover", "Rallying Cry", "Strike First"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows", "Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Great Stag", "Warhawk", "Forest Dragon", "Great Eagle"]
        }
    },
    "Shadowdancer": {
        # https://tow.whfb.app/unit/shadowdancer - 85 pts
        "points": 85,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 8,
            "BallisticSkill": 6,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 7,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Evasive", "Furious Charge", "Immune to Psychology", "Loner", "Move Through Cover", "Strike First", "Talismanic Tattoos", "Ward6", "Troubadour of Loec"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 0,
            "Lores": ["Battle Magic", "Illusion"],
            "OptionalRules": ["Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Spear of Loec", "Trickster's Blades"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Spellsinger": {
        # https://tow.whfb.app/unit/spellsinger - 80 pts
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
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Lore of Athel Loren", "Magical Attacks", "Move Through Cover"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "High Magic", "Illusion"],
            "OptionalRules": ["Talismanic Tattoos", "Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Unicorn", "Warhawk", "Great Eagle"]
        }
    },
    "Spellweaver": {
        # https://tow.whfb.app/unit/spellweaver - 155 pts
        "points": 155,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Lore of Athel Loren", "Magical Attacks", "Move Through Cover"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 3,
            "Lores": ["Battle Magic", "Elementalism", "High Magic", "Illusion"],
            "OptionalRules": ["Talismanic Tattoos", "Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Elven Steed", "Unicorn", "Warhawk", "Great Eagle"]
        }
    },
    "Treeman Ancient": {
        # https://tow.whfb.app/unit/treemen-ancient - 265 pts
        # Shooting is not simulated, so these are left out of the options:
        # Strangleroots.
        "points": 265,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 5,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 2,
            "Wounds": 6,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Forest Spirit",
            "Armor": "Full Plate Armor",
            "Weapon": "Oaken Fists",
            "Shield": False,
            "SpecialRules": ["Close Order", "Flammable", "Immune to Psychology", "Large Target", "Lore of Athel Loren", "Magical Attacks", "Move Through Cover", "Regeneration (5+)", "Stomp Attacks (D3)", "Stubborn", "Terror", "Timmm-berrr!", "Tree Spirit", "Tree Whack"],
            "TroopType": "Behemoth",
            "UnitCategory": "Character",
            "WizardLevel": 2,
            "Lores": ["Battle Magic", "Elementalism"],
            "OptionalRules": ["Forest Spites"],
        },
        "equipment_options": {
            "weapons": ["Oaken Fists"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Warden of Talsyn": {
        # https://tow.whfb.app/unit/warden-of-talsyn - 125 pts
        "points": 125,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 7,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Wood Elf",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Courage Beyond Compare", "Drilled", "Elven Reflexes", "Immune to Psychology", "Move Through Cover", "Parry", "Strike First", "Stubborn"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Asrai Spear", "Two Hand Weapons", "Great Weapon"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Waystalker": {
        # https://tow.whfb.app/unit/waystalker - 85 pts
        # Shooting is not simulated, so these are left out of the options: Asrai
        # longbow.
        "points": 85,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 7,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Wood Elf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Elven Reflexes", "Evasive", "Feigned Flight", "Fire & Flee", "Hawk-eyed Archer", "Ignores Cover", "Move Through Cover", "Scouts"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "OptionalRules": ["Arcane bodkins", "Hagbane tips", "Moonfire shot", "Swiftshiver shards", "Trueflight arrows", "Forest Spites", "Ambushers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
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
    "Boldest of the Bold": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/boldest-of-the-bold",
        "text": (
            "Araloth ignores all negative modifiers to his Leadership "
            "characteristic."
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
    "Courage Beyond Compare": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/courage-beyond-compare",
        "text": (
            "If this character joins a unit of Guardians of Talsyn, that unit gains "
            "the Immune to Psychology special rule. Should this character leave the "
            "unit for any reason, the unit loses this special rule."
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
    "Elven Reflexes": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/elven-reflexes",
        "text": (
            "A model with this special rule (but not its mount) has a +1 modifier "
            "to its Initiative characteristic (to a maximum of 10) during the first "
            "round of any combat."
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
    "Favour of the Goddess": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/favour-of-the-goddess",
        "text": (
            "Araloth has a 5+ Ward save against any wounds suffered."
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
    "Flammable": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/flammable",
        "text": (
            "A model with this special rule cannot make a Regeneration save against "
            "a wound caused by a Flaming attack."
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
    "Furious Charge": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/furious-charge",
        "text": (
            "During a turn in which it made a charge move of 3\" or more, a model "
            "with this special rule gains a +1 modifier to its Attacks "
            "characteristic."
        ),
    },
    "Hawk-eyed Archer": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/hawk-eyed-archer",
        "text": (
            "A model with this special rule can target any enemy character it can "
            "draw a line of sight to, regardless of the usual rules for targeting "
            "Lone characters. In addition, a model with this special rule can "
            "target a specific model within its target unit, such as a champion or "
            "a character."
        ),
    },
    "Ignores Cover": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/ignores-cover",
        "text": (
            "If a model making a shooting attack has this special rule, it ignores "
            "any To Hit modifiers caused by partial or full cover."
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
    "Loner": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/loner",
        "text": (
            "A character with this special rule cannot be your General and cannot "
            "join a unit without this special rule. A unit with this special rule "
            "cannot be joined by a character without this special rule."
        ),
    },
    "Lore of Athel Loren": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-athel-loren",
        "text": (
            "Wood Elf Mages have a unique relationship with the forest. They are a "
            "part of it, much like Dryads and Treemen, yet possessed of a greater "
            "sense of individuality. This bond allows them to commune with the "
            "forest, to entreat with it on behalf of their kin and, in times of "
            "war, to awaken it to their aid. A Wizard with the 'Lore of Athel "
            "Loren' special rule may discard one of their randomly generated spells "
            "as normal. When they do so, they may select instead either the "
            "signature spell of their chosen Lore of Magic, or one of the spells "
            "listed below. Lore of Athel Loren Lore"
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
    "Parry": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/parry-wood-elves",
        "text": (
            "When fighting with a hand weapon and shield, or Asrai spear and "
            "shield, this unit improves its armour value by 1."
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
    "Scouts": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/scouts",
        "text": (
            "Units with this special rule may be deployed after all other units "
            "from both armies. They can be deployed anywhere on the battlefield "
            "that is more than 12\" away from an enemy model. If deployed in this "
            "way, Scouts cannot declare a charge during their first turn. If both "
            "armies contain Scouts, a roll-off should determine which player "
            "deploys Scouts first. The players then alternate deploying their "
            "scouting units one at a time, starting with the player who won the "
            "roll-off."
        ),
    },
    "Skaryn the Eye Thief": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/skaryn-the-eye-thief",
        "text": (
            "During the Command sub-phase of his turn, Araloth may attempt to "
            "dispatch Skaryn to strike from the skies by rolling a D6. On a roll of "
            "1-2, Skaryn lingers out of reach of the enemy and nothing happens. On "
            "a roll of 3+, Skaryn descends from the skies to strike at his master's "
            "mark. Nominate a single enemy model within 18\" of Araloth. That model "
            "suffers a single Strength 4 hit with an AP of -1. If the target "
            "suffers an unsaved wound, its Weapon Skill and Initiative "
            "characteristics are reduced by D3 (to a minimum of 1) for the "
            "remainder of the game."
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
    "Strike First": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/strike-first",
        "text": (
            "During the Combat phase, a model with this special rule that is "
            "engaged in combat improves its Initiative characteristic to 10 (before "
            "any other modifiers are applied). If a model has both this rule and "
            "Strike Last, the two rules cancel one another out."
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
    "Talismanic Tattoos": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/talismanic-tattoos",
        "text": (
            "Talismanic Tattoos give their wearer a 6+ Ward save against any wounds "
            "suffered."
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
    "The Arrow of Kurnous": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/the-arrow-of-kurnous",
        "text": (
            "Once deployment is complete, but before the roll-off to determine "
            "which player takes the first turn, if the General of your opponent's "
            "army is within 36\" of one or more models in your army that has this "
            "special rule, one of those models may fire the Arrow of Kurnous. If "
            "the Arrow of Kurnous is fired, the General of your opponent's army "
            "immediately suffers a single Strength 3 hit, with no armour or "
            "Regeneration saves permitted (Ward saves can be attempted as normal). "
            "However, if the Arrow of Kurnous is fired, your opponent adds +1 to "
            "their roll when rolling off to determine who takes the first turn."
        ),
    },
    "Timmm-berrr!": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/timmm-berrr",
        "text": (
            "When this model is reduced to zero Wounds, the winner of a roll-off "
            "chooses one of its arcs (front, flank or rear) for it to fall into. "
            "Any units that are within the chosen arc and in base contact with this "
            "model suffer D6 hits, each using the Strength characteristic of this "
            "model, with an AP of -1. Once these hits are resolved, this model is "
            "removed from play."
        ),
    },
    "Tree Spirit": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/tree-spirit",
        "text": (
            "A character with this special rule cannot join a unit without this "
            "special rule. A unit with this special rule cannot be joined by, or "
            "use the Leadership characteristic of, a character without this special "
            "rule. However, a unit with this special rule can use the Leadership "
            "characteristic of a friendly character with this special rule that is "
            "not fleeing whilst within that character's Command range."
        ),
    },
    "Tree Whack": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/tree-whack",
        "text": (
            "Once per turn, during the Combat phase, a model with this special rule "
            "may use one of its Attacks to make a single 'Tree Whack' attack. To "
            "make a Tree Whack attack, nominate a single model within an enemy unit "
            "that this model is engaged in combat with to be the target of the "
            "attack. That model must immediately make an Initiative test: - If the "
            "test is failed, the target suffers D3 hits, each using the Strength "
            "characteristic of this model, with no armour save save permitted (Ward "
            "and Regeneration saves can be attempted as normal). - If the test is "
            "passed, the target manages to avoid the Tree Whack."
        ),
    },
    "Troubadour of Loec": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/troubadour-of-loec",
        "text": (
            "A Shadowdancer that joins a unit of Wardancers is considered to have "
            "the Dances of Loec special rule for as long as they remain with the "
            "unit."
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
}

PROFILES = dict(CHARACTERS, **UNITS)
