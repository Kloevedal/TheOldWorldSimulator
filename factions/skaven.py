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

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Clanrats": {
        # https://tow.whfb.app/unit/clanrats - 4 pts per model, unit size 20-40
        # Fights with the Clanrat row.
        "points": 4,
        "points_per": "model",
        "unit_size": "20-40",
        "champion": {'Name': 'Clawleader', 'Movement': 5, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 4,
            "Race": "Skaven",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Scurry Away", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Thrusting Spear"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Gutter Runners": {
        # https://tow.whfb.app/unit/gutter-runners - 14 pts per model, unit size 5+
        # Fights with the Gutter Runner row.
        # Shooting is not simulated, so these are left out of the options: Slings,
        # Throwing weapons.
        "points": 14,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Assassin', 'Movement': 6, 'WeaponSkill': 4, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Two Hand Weapons",
            "Shield": False,
            "SpecialRules": ["Evasive", "Feigned Flight", "Fire & Flee", "Move Through Cover", "Scouts", "Scurry Away", "Skirmishers"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers", "Poisoned Attacks"],
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
    "Master Moulder": {
        # https://tow.whfb.app/unit/master-moulder - None pts per model, unit size
        # (see Rat Ogre & Giant Rat profiles)
        # Fights with the Master Moulder row.
        "points": 7,
        "points_note": "+7 points",
        "points_per": "model",
        "unit_size": "(see Rat Ogre & Giant Rat profiles)",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Skaven",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Leader of the Pack", "Motley Crew", "Scurry Away", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Whip", "Things-catcher"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Night Runners": {
        # https://tow.whfb.app/unit/night-runners - 7 pts per model, unit size 10+
        # Fights with the Night Runner row.
        # Shooting is not simulated, so these are left out of the options: Slings,
        # Throwing weapons.
        "points": 7,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Nightleader', 'Movement': 6, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Evasive", "Fire & Flee", "Scurry Away", "Skirmishers"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Packmaster": {
        # https://tow.whfb.app/unit/packmaster - None pts per model, unit size (see
        # Rat Ogre & Giant Rat profiles)
        # Fights with the Packmaster row.
        "points": 5,
        "points_note": "+5 points",
        "points_per": "model",
        "unit_size": "(see Rat Ogre & Giant Rat profiles)",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 6,
            "Race": "Skaven",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Leader of the Pack", "Motley Crew", "Scurry Away", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Whip", "Things-catcher"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Plague Censer Bearers": {
        # https://tow.whfb.app/unit/plague-censer-bearers - 13 pts per model, unit
        # size 2-10
        # Fights with the Plague Censer Bearer row.
        "points": 13,
        "points_per": "model",
        "unit_size": "2-10",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Plague Censer",
            "Shield": False,
            "SpecialRules": ["Frenzy", "Scurry Away", "Skirmishers", "Stubborn", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Plague Censer"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Plague Monks": {
        # https://tow.whfb.app/unit/plague-monks - 7 pts per model, unit size 10+
        # Fights with the Plague Monk row.
        "points": 7,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Plague Deacon', 'Movement': 5, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 4, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 5},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Frenzy", "Horde", "Scurry Away", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Poisoned Wind Globadiers": {
        # https://tow.whfb.app/unit/poisoned-wind-globadiers - 10 pts per model, unit
        # size 2-10
        # Fights with the Globadier row.
        # Shooting is not simulated, so these are left out of the options: Poisoned
        # Wind globes.
        "points": 10,
        "points_per": "model",
        "unit_size": "2-10",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Skaven",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Scurry Away", "Skirmishers", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
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
    "Rat Ogres": {
        # https://tow.whfb.app/unit/rat-ogres - 48 pts per model, unit size 3+
        # Fights with the Rat Ogre row.
        "points": 48,
        "points_per": "model",
        "unit_size": "3+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 4,
            "BallisticSkill": 1,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 5,
            "Race": "Skaven",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2)", "Close Order", "Fear", "Frenzy", "Horde", "Safe from Harm", "Scurry Away", "Warband"],
            "TroopType": "MonstrousInfantry",
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
    "Rat Swarms": {
        # https://tow.whfb.app/unit/rat-swarms - 36 pts per model, unit size 3+
        # Fights with the Rat Swarm row.
        "points": 36,
        "points_per": "model",
        "unit_size": "3+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 2,
            "BallisticSkill": 0,
            "Strength": 2,
            "Toughness": 2,
            "Initiative": 4,
            "Wounds": 5,
            "Attacks": 5,
            "Leadership": 4,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Immune to Psychology", "Loner", "Skirmishers", "Unbreakable", "Vanguard"],
            "TroopType": "Swarm",
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
    "Stormvermin": {
        # https://tow.whfb.app/unit/stormvermin - 10 pts per model, unit size 10+
        # Fights with the Stormvermin row.
        "points": 10,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Fangleader', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Skaven",
            "Armor": "Heavy Armor",
            "Weapon": "Halberd",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Scurry Away", "Warband", "Warpstone Weapons"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Halberd"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Warplock Jezzails": {
        # https://tow.whfb.app/unit/warplock-jezzails - 19 pts per model, unit size 3+
        # Fights with the Jezzail Team row.
        # Shooting is not simulated, so these are left out of the options: warplock
        # jezzails.
        "points": 19,
        "points_per": "model",
        "unit_size": "3+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 5,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Open Order", "Scurry Away", "Warband"],
            "TroopType": "RegularInfantry",
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
    "Weapon Team": {
        # https://tow.whfb.app/unit/weapon-team - 15 pts per unit
        # Fights with the Weapon Team Crew row.
        # Shooting is not simulated, so these are left out of the options: Poisoned
        # Wind Mortar, Ratling Gun, Warpfire Thrower.
        "points": 15,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 4,
            "Race": "Skaven",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Loner", "Open Order", "Scurry Away", "Deploying Weapon Teams", "Weapon Team Leadership", "Targeting Weapon Teams"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Doom-Flayer", "Warp Grinder"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Giant Rats": {
        # https://tow.whfb.app/unit/giant-rats - 3 pts per model, unit size 10-30
        # Fights with the Giant Rat row.
        "points": 3,
        "points_per": "model",
        "unit_size": "10-30",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 2,
            "BallisticSkill": 0,
            "Strength": 2,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 3,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Fight in Extra Rank", "Horde", "Scurry Away", "Warband"],
            "TroopType": "WarBeast",
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
    "Doomwheel": {
        # https://tow.whfb.app/unit/doomwheel - 145 pts per unit
        # Fights with the Warlock (x1) row, using the Doomwheel row's Toughness and
        # Wounds.
        # Also has a profile for Doomwheel (M3D6 WS- BS- S5 T5 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Rats (M- WS2 BS0 S2 T- W- I4 A2D6 Ld5); not
        # simulated.
        # Armour value 5+ as printed on the site.
        "points": 145,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Doomwheel', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 5, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Rats', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 0, 'Strength': 2, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': None, 'Leadership': 5},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 5,
            "Initiative": 3,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Skaven",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Crushing Bulk", "Immune to Psychology", "Impact Hits (D3+1)", "Large Target", "Random Attacks (Rats only)", "Random Movement", "Stomp Attacks (2)", "Zzzzap!"],
            "TroopType": "HeavyChariot",
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
    "Screaming Bell": {
        # https://tow.whfb.app/unit/screaming-bell - None pts per unit
        # Fights with the Rat Ogre Crew (x1) row, using the Screaming Bell row's
        # Toughness and Wounds.
        # Also has a profile for Screaming Bell (M2 WS- BS- S5 T6 W5 I- A- Ld-); not
        # simulated.
        # Armour value 4+ as printed on the site.
        "points": 185,
        "points_note": "+185 points",
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Screaming Bell', 'Movement': 2, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 6, 'Initiative': None, 'Wounds': 5, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 5,
            "Toughness": 6,
            "Initiative": 4,
            "Wounds": 5,
            "Attacks": 3,
            "Leadership": 5,
            "Race": "Skaven",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2, Rat Ogre only)", "Blessings of the Horned Rat", "Ward5 (non-magical)", "Dragged Along", "Impact Hits (D6+1)", "Large Target", "Magic Resistance (-3)", "Scurrying Masses", "Stubborn", "Terror", "Tolling the Bell"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Hell Pit Abomination": {
        # https://tow.whfb.app/unit/hell-pit-abomination - 210 pts per unit
        # Its Attacks are D6+1, a dice value the engine cannot use yet; recorded as
        # None, so it makes no attacks.
        # Fights with the Hell Pit Abomination row.
        "points": 210,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 1,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 6,
            "Attacks": None,
            "Leadership": 8,
            "Race": "Skaven",
            "Armor": None,
            "Weapon": "Warpstone Claws",
            "Shield": False,
            "SpecialRules": ["Abominable Attacks", "Close Order", "Immune to Psychology", "Large Target", "Magic Resistance (-1)", "Random Attacks", "Random Movement", "Regeneration (5+)", "Stomp Attacks (D3+1)", "Terror", "Timmm-berrr!", "Too Horrible to Die", "Unbreakable"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Warpstone Claws"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Plagueclaw Catapult": {
        # https://tow.whfb.app/unit/plagueclaw-catapult - 110 pts per unit
        # Its Attacks are D3+3, a dice value the engine cannot use yet; recorded as
        # None, so it makes no attacks.
        # Fights with the Plague Monk Crew row.
        # Also has a profile for Plagueclaw Catapult (M- WS- BS- S- T6 W4 I- A- Ld-);
        # not simulated.
        # Shooting is not simulated, so these are left out of the options: Plagueclaw
        # Catapult.
        "points": 110,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Plagueclaw Catapult', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": None,
            "Leadership": 6,
            "Race": "Skaven",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Random Attacks", "Skirmishers", "Stubborn"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
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
    "Warp Lightning Cannon": {
        # https://tow.whfb.app/unit/warp-lightning-cannon - 110 pts per unit
        # Fights with the Engineer & Crew row.
        # Also has a profile for Warp Lightning Cannon (M- WS- BS- S- T6 W4 I- A-
        # Ld-); not simulated.
        # Shooting is not simulated, so these are left out of the options: Warp
        # Lightning Cannon.
        "points": 110,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Warp Lightning Cannon', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 6,
            "Race": "Skaven",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Skirmishers"],
            "TroopType": "WarMachine",
            "UnitCategory": "Unit",
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
}


# Special rules carried by this faction's characters and units. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {
    "Abominable Attacks": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/abominable-attacks",
        "text": (
            "Instead of attacking normally during the Combat phase, a Hell Pit "
            "Abomination may choose to make one of the following Abominable "
            "Attacks: Feed & Avalanche of Flesh Feed Avalanche of Flesh"
        ),
    },
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
    "Blessings of the Horned Rat": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/blessings-of-the-horned-rat",
        "text": (
            "This model has a 5+ Ward save against any wounds suffered that were "
            "caused by a non-magical enemy attack."
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
    "Cloud of Flies": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/cloud-of-flies",
        "text": (
            "Any enemy model that directs its attacks against this character during "
            "the Combat phase suffers a -1 modifier to its rolls To Hit."
        ),
    },
    "Crushing Bulk": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/crushing-bulk",
        "text": (
            "Any Stomp Attacks made by a Doom Wheel have an Armour Piercing "
            "characteristic of -1. In addition, an enemy unit that suffers Impact "
            "Hits from this model must immediately make a Leadership test. If this "
            "test is failed, the unit becomes Disrupted until the end of the "
            "current Combat phase."
        ),
    },
    "Deploying Weapon Teams": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/deploying-weapon-teams",
        "text": (
            "A Weapon Team must be deployed at the same time as its 'parent' unit "
            "(the unit it was bought as an upgrade for), and must be deployed "
            "within 3\" of that unit."
        ),
    },
    "Dragged Along": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/dragged-along",
        "text": (
            "A model with this special rule that begins its movement within 1\" of a "
            "friendly unit whose troop type is infantry, that is not fleeing and "
            "that contains ten or more models, may replace its Movement "
            "characteristic with that of the unit."
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
    "Fight in Extra Rank": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fight-in-extra-rank",
        "text": (
            "A model with this special rule may make a supporting attacks."
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
    "Leader of the Pack": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/leader-of-the-pack-skaven",
        "text": (
            "Models with this special rule can only be taken as part of a unit of "
            "Rat Ogres, or a unit of Giant Rats. Models with this special rule "
            "(including command group models) must be positioned at the rear of "
            "their unit, making up its rear rank(s). Any Rat Ogres or Giant Rats "
            "the unit contains must always occupy the front rank(s) of the unit, "
            "pushing past any models with this special rule to get there if "
            "necessary (such as when the unit turns). Note that a Master Moulder "
            "may issue and accept challenges even if they are not within the "
            "fighting rank."
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
    "Poisoned Attacks": {
        "status": "implemented",
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
    "Random Attacks": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/random-attacks",
        "text": (
            "Models with this special rule do not have a normal Attacks "
            "characteristic. Instead, a dice roll is given (D3+1, for example). "
            "Each time a model with this special rule attacks in combat, roll the "
            "dice to determine the number of attacks it will make, then roll To Hit "
            "as normal. If a fighting rank contains more than one model with this "
            "special rule, roll separately for each, unless specified otherwise."
        ),
    },
    "Random Movement": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/random-movement",
        "text": (
            "Models with this special rule do not have a normal Movement "
            "characteristic. Instead, a dice roll is given (2D6, for example). When "
            "a model with this special rule moves, roll the dice to determine its "
            "maximum movement. Models with this special rule move during the "
            "Compulsory Moves sub-phase. They cannot march or declare a charge. "
            "They can wheel to change direction, but cannot perform any other "
            "manoeuvres. If the model is able to make contact with an enemy unit "
            "during the Compulsory Moves sub-phase or whilst pursuing, it may do so "
            "and counts as having charged. The model aligns against the enemy unit "
            "and stops moving. A unit charged in this way must Hold. If every model "
            "in a unit has this [...]"
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
    "Safe from Harm": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/safe-from-harm",
        "text": (
            "When an enemy unit shoots at a unit of Rat Ogres that also contains "
            "one or more Packmasters, the enemy player must roll a D6 for each "
            "successful roll To Hit before making any rolls To Wound. On a roll of "
            "1-4, the hit is inflicted upon a Rat Ogre. In combat, enemy models "
            "must allocate their attacks against a model they are in base contact "
            "with (or against the closest model if they are within the fighting "
            "rank but not in base contact) before rolling To Hit."
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
    "Scurry Away": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/scurry-away",
        "text": (
            "Models with this special rule have a +1 modifier to the result of any "
            "Flee roll they make."
        ),
    },
    "Scurrying Masses": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/scurrying-masses",
        "text": (
            "Whilst within 3\" of a friendly unit, this model gains a positive (+) "
            "modifier to its Leadership characteristic equal to that unit's current "
            "Rank Bonus, up to a maximum of Leadership 10."
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
    "Targeting Weapon Teams": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/targeting-weapon-teams",
        "text": (
            "If it is within 3\" of its parent unit, and if that unit contains five "
            "or more models (and is not itself fleeing), a Weapon Team cannot be "
            "targeted by enemy shooting or by enemy spells, unless the Weapon Team "
            "is the closest target."
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
    "Tolling the Bell": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/tolling-the-bell",
        "text": (
            "A Screaming Bell may be rung during the Command sub-phase of your "
            "turn. Roll on the table below to determine the effect this has: 2D6 | "
            "Result 2 | Magical Backlash: Every unit (friend or foe) that is within "
            "this model's Command range suffers D3 Strength 4 hits, each with an AP "
            "of -2. 3-4 | Dissonant Peal: Until your next Start of Turn sub-phase, "
            "all enemy units within 18\" of this model suffer a -1 modifier to their "
            "Leadership characteristic (to a minimum of 2). 5-6 | Wall of Unholy "
            "Sound: Until your next Start of Turn sub-phase, all friendly Skaven "
            "units within 18\" of this model gain the Fear special rule. 7 | "
            "Resonant Power: Until the end of this turn, all friendly Skaven "
            "Wizards within [...]"
        ),
    },
    "Too Horrible to Die": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/too-horrible-to-die",
        "text": (
            "The first time a Hell Pit Abomination loses its last Wound, roll a D6 "
            "before removing the model from play: - On a roll of 1-3, the beast "
            "wheezes its last breath and is removed from play. - On a roll of 4 or "
            "5, the great corpse shudders and a swarm of rats bursts forth. Place a "
            "Rat Swarm of one model within 3\" of this model, then remove this model "
            "from play. - On a roll of 6, the Hell Pit Abomination jolts and "
            "shudders with unnatural vitality before rising anew. This model "
            "immediately recovers D3 Wounds."
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
    "Weapon Team Leadership": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/weapon-team-leadership",
        "text": (
            "Whilst within 3\" of its parent unit, a Weapon Team gains a positive "
            "(+) modifier to its Leadership characteristic equal to the parent "
            "unit's current Rank Bonus, up to a maximum of Leadership 10."
        ),
    },
    "Zzzzap!": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/zzzzap",
        "text": (
            "At the end of every Shooting phase, after all shooting has been "
            "resolved, place up to three small (3\") blast templates so that their "
            "central hole is within 6\" of this model. Once placed, each template "
            "will scatter D6\". Any model (friend or foe) whose base lies underneath "
            "a template's final position risks being hit and suffering a single "
            "hit, the Strength of which is determined by rolling an Artillery dice. "
            "Each hit has an AP of -2. If a 'Misfire' is rolled when rolling to "
            "determine the Strength of a template, this model suffers the brunt of "
            "the warp lightning bolt. The template is removed and any models hit by "
            "it are left unharmed, but this model loses a single Wound."
        ),
    },
}

PROFILES = dict(CHARACTERS, **UNITS)
