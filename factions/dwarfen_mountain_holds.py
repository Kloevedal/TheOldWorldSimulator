"""Dwarfen Mountain Holds.

Profiles from https://tow.whfb.app/army/dwarfen-mountain-holds
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Dwarfen Mountain Holds"

# Other names that should resolve to this faction.
ALIASES = [
    "Dwarfs",
    "Dwarves",
    "Dwarfen Mountain Holds",
    "Mountain Holds",
    "Dawi",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Ungrim": "Ungrim Ironfist",
    "Thorgrim": "Thorgrim Ulleksson",
    "Burlok": "Burlok Damminson",
    "Dwarf King": "King",
    "Dwarf Engineer": "Engineer",
}

CHARACTERS = {
    "King": {
        # https://tow.whfb.app/unit/king - 125 pts
        # May take up to 125 pts of Weapon, Armour and Talismanic runes; runes are
        # not modelled.
        "points": 125,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 7,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ancestral Grudge", "Dwarf Crafted", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Rallying Cry", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Thane": {
        # https://tow.whfb.app/unit/thane - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Ancestral Grudge", "Dwarf Crafted", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Rallying Cry", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Runelord": {
        # https://tow.whfb.app/unit/runelord - 120 pts
        "points": 120,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Forgefire", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-2)", "Resolute", "Rune Lore", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Runesmith": {
        # https://tow.whfb.app/unit/runesmith - 65 pts
        "points": 65,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Forgefire", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Magic Resistance (-2)", "Resolute", "Rune Lore", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Heavy Armor", "Full Plate Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Daemon Slayer": {
        # https://tow.whfb.app/unit/daemon-slayer - 130 pts
        # Slayers wear no armour.
        "points": 130,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 7,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Deathblow", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Immune to Psychology", "Killing Blow", "Loner", "Magic Resistance (-2)", "Resolute", "Slayer of Daemons", "Unbreakable", "Vanguard"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Dragon Slayer": {
        # https://tow.whfb.app/unit/dragon-slayer - 70 pts
        # Slayers wear no armour.
        "points": 70,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Deathblow", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Immune to Psychology", "Killing Blow", "Loner", "Magic Resistance (-2)", "Resolute", "Slayer of Dragons", "Unbreakable", "Vanguard"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Great Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Engineer": {
        # https://tow.whfb.app/unit/engineer - 50 pts
        "points": 50,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Artillery Master", "Dwarf Crafted", "Entrenchment", "Gromril Armour", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Resolute", "Stand Back Chief", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Engineer Sapper": {
        # https://tow.whfb.app/unit/engineer-sapper - 70 pts
        "points": 70,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 4,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Dig In!", "Dwarf Crafted", "Gromril Armour", "Hatred (Orcs & Goblins)", "Hostile Terrain", "Magic Resistance (-1)", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Great Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Ungrim Ironfist": {
        # https://tow.whfb.app/unit/ungrim-ironfist - 315 pts
        # Fixed wargear; must be fielded as presented.
        "points": 315,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 9,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 6,
            "Initiative": 5,
            "Wounds": 3,
            "Attacks": 4,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": "Light Armor",
            "Weapon": "Axe of Dargo",
            "Shield": False,
            "SpecialRules": ["Deathblow", "Gromril Armour", "Hatred (Orcs & Goblins)", "Immune to Psychology", "King of the Slayer Hold", "Magic Resistance (-2)", "Rallying Cry", "Resolute", "Slayer", "Unbreakable"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Axe of Dargo", "Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": ["Axe of Dargo", "Slayer Crown"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Thorgrim Ulleksson": {
        # https://tow.whfb.app/unit/thorgrim-ulleksson - 250 pts
        # His armour is the Armour of Skaldour, a magic item rather than a standard
        # armour type, so Armor is None until runic items are modelled.
        "points": 250,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Grudge-Settler",
            "Shield": True,
            "SpecialRules": ["Gromril Armour", "Grudgelore", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Rallying Cry", "Resolute", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Grudge-Settler", "Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": ["Grudge-Settler", "Grudgestone", "Armour of Skaldour"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Burlok Damminson": {
        # https://tow.whfb.app/unit/burlok-damminson - 85 pts
        # Fixed wargear. The Furnace Hammer rolls an Artillery dice for its
        # Strength and can Misfire; the rivet gun is ranged and is not simulated.
        "points": 85,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 5,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Furnace Hammer",
            "Shield": False,
            "SpecialRules": ["Dwarf Crafted", "Gromril Armour", "Hatred (Orcs & Goblins)", "Magic Resistance (-1)", "Prepared Positions", "Range Finding Optics", "Resolute", "Stand Back Chief", "Stubborn"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "NamedCharacter",
        },
        "equipment_options": {
            "weapons": ["Furnace Hammer", "Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": ["Furnace Hammer", "Rivet Gun"],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Anvil of Doom": {
        # https://tow.whfb.app/unit/anvil-of-doom - 235 pts
        # Uses the Forgefather & Anvil Guard row: a war machine fights with its
        # crew's characteristics, including T and W (Split Profile (War
        # Machine)). The machine's own row is T7 W5, used only outside combat.
        # The crew losing -1 Attack per Wound lost is not modelled. Its runes
        # (up to 100 points) are not modelled either.
        "points": 235,
        "base_profile": {
            "Movement": 3,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Dwarf",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Ancestral Shield", "Ward5", "Gromril Armour", "Gromril Weapons", "Hatred (Orcs & Goblins)", "Immune to Psychology", "Immovable Object", "Magic Resistance (-3)", "Resolute", "Rune Lore", "Skirmishers", "Strike the Runes", "Unbreakable"],
            "TroopType": "WarMachine",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
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
    'Gromril Armour': {
        "status": 'implemented',
        "text": (
            "May reroll any roll of a natural 1 made when making an Armour Save "
            "roll. "
        ),
    },
    'Gromril Weapons': {
        "status": 'implemented',
        "text": (
            "A hand weapon carried by this model has an Armour Piercing of -1. "
            "A single, ordinary hand weapon only - not two hand weapons, "
            "another weapon type, or a runed hand weapon. "
        ),
    },
    'Resolute': {
        "status": None,
        "text": (
            "-1 to any Flee or Pursuit roll (min 1). Neither happens in a duel. "
        ),
    },
    'Ancestral Grudge': {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
    'Hatred (Orcs & Goblins)': {
        "status": 'implemented',
        "text": (
            "Reroll failed To Hit rolls in the first round against Orcs and "
            "Goblins. "
        ),
    },
    'Rune Lore': {
        "status": None,
        "text": (
            "Runes are not modelled. "
        ),
    },
    'Forgefire': {
        "status": None,
        "text": (
            "Not transcribed - page not read. "
        ),
    },
    "Ancestral Shield": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/ancestral-shield",
        "text": (
            "An Anvil of Doom and the Forgefather & Anvil Guard have a 5+ Ward save "
            "against any wounds suffered."
        ),
    },
    "Immovable Object": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/immovable-object",
        "text": (
            "Once this model has been placed on the battlefield during deployment "
            "it cannot be moved by its crew during the Remaining Moves sub-phase. "
            "Note that the model can still pivot freely at any time during its turn "
            "(the better to face the enemy) and may make a follow up move as "
            "normal."
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
    "Strike the Runes": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/strike-the-runes",
        "text": (
            "An Anvil of Doom can cast the following Bound spells, with a Power "
            "Level of 2: Rune of Oath & Steel, Rune of Hearth & Home, Rune of Haste "
            "& Urgency & Rune of Wrath & Ruin Rune of Oath & Steel Rune of Hearth & "
            "Home Rune of Haste & Urgency Rune of Wrath & Ruin"
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
