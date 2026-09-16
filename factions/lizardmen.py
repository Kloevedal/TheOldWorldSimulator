"""Lizardmen.

Profiles from https://tow.whfb.app/army/lizardmen, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Lizardmen"

# Other names that should resolve to this faction.
ALIASES = [
    "Lizardmen",
    "Lizardman",
    "Seraphon",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Oldblood": "Saurus Oldblood",
    "Scar-Veteran": "Saurus Scar-Veteran",
    "Slann": "Slann Mage-Priest",
}

CHARACTERS = {
    "Saurus Oldblood": {
        # https://tow.whfb.app/unit/saurus-oldblood - 140 pts
        "points": 140,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 6,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 5,
            "Leadership": 8,
            "Race": "Saurus",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Cold Blooded", "Furious Charge", "Obsidian Blades", "Rallying Cry"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Cavalry Spear", "Great Weapon", "Halberd"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Cold One (Lizardmen)", "Carnosaur"]
        }
    },
    "Saurus Scar-Veteran": {
        # https://tow.whfb.app/unit/saurus-scar-veteran - 90 pts
        "points": 90,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 4,
            "Leadership": 8,
            "Race": "Saurus",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Cold Blooded", "Furious Charge", "Obsidian Blades", "Rallying Cry"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Cavalry Spear", "Great Weapon", "Halberd"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Cold One (Lizardmen)", "Carnosaur"]
        }
    },
    "Skink Chief": {
        # https://tow.whfb.app/unit/skink-chief - 45 pts
        # Shooting is not simulated, so these are left out of the options: Blowpipe,
        # Javelins.
        "points": 45,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 6,
            "Race": "Skink",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Aquatic", "Cold Blooded", "Poisoned Attacks"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Cavalry Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Terradon", "Ripperdactyl", "Stegadon"]
        }
    },
    "Skink Priest": {
        # https://tow.whfb.app/unit/skink-priest - 60 pts
        "points": 60,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 2,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Skink",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arcane Vassal", "Aquatic", "Cold Blooded", "Lore of Lustria"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Elementalism", "Illusion"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Ancient Stegadon"]
        }
    },
    "Slann Mage-Priest": {
        # https://tow.whfb.app/unit/slann-mage-priest - 285 pts
        "points": 285,
        "base_profile": {
            "Movement": 2,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 5,
            "Attacks": 1,
            "Leadership": 9,
            "Race": "Slann",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Arcane Shield", "Ward5", "Close Order", "Cold Blooded", "Fly (8)", "Large Target", "Lore of Lustria"],
            "TroopType": "MonstrousCreature",
            "UnitCategory": "Character",
            "WizardLevel": 4,
            "Lores": ["Battle Magic", "Elementalism", "High Magic", "Illusion", "Necromancy"],
            "OptionalRules": ["Discipline of the Old Ones"],
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

# Regular (non-character) units go here.
UNITS = {}


# Special rules carried by this faction's characters. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {
    "Aquatic": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/aquatic",
        "text": (
            "Models with this special rule do not suffer any modifiers to their "
            "Movement characteristic when moving through any difficult or dangerous "
            "terrain feature which has been designated a 'water feature'. This "
            "might include shallow streams or fords, swampy ground, fast flowing "
            "rivers, ponds or lakes, and players should agree prior to the game if "
            "any terrain is a water feature."
        ),
    },
    "Arcane Shield": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/arcane-shield",
        "text": (
            "This character has a 5+ Ward save against any wounds suffered."
        ),
    },
    "Arcane Vassal": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/arcane-vassal",
        "text": (
            "Once per turn, unless this model is fleeing or engaged in combat, a "
            "single friendly Slann Mage-Priest that is within 12\" of this model may "
            "'channel' a spell through this model. If they do, the range, targeting "
            "restrictions and all effects of the spell are measured from this "
            "model, rather than from the caster. If the spell requires a line of "
            "sight, it is determined from this model. Note that spells with a range "
            "of Self cannot be channelled in this way."
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
    "Cold Blooded": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/cold-blooded",
        "text": (
            "When required to make a Fear, Panic or Terror test, models with this "
            "special rule may roll an extra D6 and discard the highest result."
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
    "Furious Charge": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/furious-charge",
        "text": (
            "During a turn in which it made a charge move of 3\" or more, a model "
            "with this special rule gains a +1 modifier to its Attacks "
            "characteristic."
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
    "Lore of Lustria": {
        "status": None,
        "url": "https://tow.whfb.app/the-lores-of-magic/lore-of-lustria",
        "text": (
            "The Slann Mage-Priests are masters of magic able to wield tremendous "
            "power with almost contemptuous ease. With this power they are able to "
            "alter the environment around them and the fates of their loyal "
            "servants, summoning rains to wash away their foes, or calling upon the "
            "Winds of Magic to heal their champions. A Wizard with the 'Lore of "
            "Lustria' special rule may discard one of their randomly generated "
            "spells as normal. When they do so, they may select instead either the "
            "signature spell of their chosen Lore of Magic, or one of the spells "
            "listed below. Lore of Lustria Lore"
        ),
    },
    "Obsidian Blades": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/obsidian-blades",
        "text": (
            "A hand weapon carried by a model with this special rule has an Armour "
            "Piercing characteristic of -1. Note that this special rule only "
            "applies to a single, non-magical hand weapon and does not apply to a "
            "model's mount (should it have one). If the model is using two hand "
            "weapons or any other sort of weapon, this special rule ceases to "
            "apply."
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
}

PROFILES = dict(CHARACTERS, **UNITS)
