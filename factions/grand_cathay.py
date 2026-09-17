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

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Crane Gunner Teams": {
        # https://tow.whfb.app/unit/crane-gunner-teams - 16 pts per model, unit size
        # 3-8
        # Fights with the Crane Gunner Team row.
        # Shooting is not simulated, so these are left out of the options: crane guns.
        "points": 16,
        "points_per": "model",
        "unit_size": "3-8",
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Cathayan",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": True,
            "SpecialRules": ["Open Order"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers", "Reserve Move"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
            "armor": ["Light Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Iron Hail Gunners": {
        # https://tow.whfb.app/unit/iron-hail-gunners - 12 pts per model, unit size
        # 4-12
        # Fights with the Iron Hail Gunner row.
        # Shooting is not simulated, so these are left out of the options: gunpowder
        # bombs, iron hail guns.
        "points": 12,
        "points_per": "model",
        "unit_size": "4-12",
        "champion": {'Name': 'Marksman', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Cathayan",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Open Order", "Skirmishers"],
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
    "Jade Warriors": {
        # https://tow.whfb.app/unit/jade-warriors - 8 pts per model, unit size 5+
        # Fights with the Jade Warrior row.
        "points": 8,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Jade Officer', 'Movement': 4, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 8},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Cathayan",
            "Armor": "Heavy Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Defensive Stance", "Detachment", "Regimental Unit", "Will of the Dragons"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Drilled", "Stubborn"],
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
    "Peasant Levy": {
        # https://tow.whfb.app/unit/peasant-levy - 4 pts per model, unit size 10+
        # Fights with the Peasant Soldier row.
        # Shooting is not simulated, so these are left out of the options: Warbows.
        "points": 4,
        "points_per": "model",
        "unit_size": "10+",
        "champion": {'Name': 'Peasant Elder', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 4, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 6},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Cathayan",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Horde", "Warband"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Close Order", "Skirmishers", "Ambushers"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Long Spear"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Jade Lancers": {
        # https://tow.whfb.app/unit/jade-lancers - 20 pts per model, unit size 5+
        # Fights with the Jade Lancer Officer row.
        # Also has a profile for Cathayan Warhorse (M7 WS3 BS- S3 T- W- I3 A1 Ld-);
        # not simulated.
        "points": 20,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Jade Lancer', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 1, 'Leadership': 8},
        "other_profiles": [
            {'Name': 'Cathayan Warhorse', 'Movement': 7, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 1,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Cathayan",
            "Armor": "Heavy Armor",
            "Weapon": "Cathayan Lance",
            "Shield": True,
            "SpecialRules": ["Cathayan Cataphracts", "Close Order", "Counter Charge", "Horde", "Swiftstride", "Will of the Dragons"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers", "Drilled", "Stubborn"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Cathayan Lance"],
            "armor": ["Heavy Armor"],
            "shield": True,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Sky Lantern": {
        # https://tow.whfb.app/unit/sky-lantern - 135 pts per unit
        # Fights with the Lantern Gunners (x4) row, using the Sky Lantern row's
        # Toughness and Wounds.
        # Also has a profile for Sky Lantern (M1 WS- BS- S5 T4 W7 I- A- Ld-); not
        # simulated.
        # Also has a profile for Commander (x1) (M- WS3 BS5 S3 T- W- I3 A2 Ld8); not
        # simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: Iron hail
        # guns, Sky Lantern Crane Guns, dragon fire bombs, gunpowder bombs.
        "points": 135,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Sky Lantern', 'Movement': 1, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 5, 'Toughness': 4, 'Initiative': None, 'Wounds': 7, 'Attacks': None, 'Leadership': None},
            {'Name': 'Commander (x1)', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 5, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 2, 'Leadership': 8},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 3,
            "Wounds": 7,
            "Attacks": 1,
            "Leadership": 8,
            "Race": "Cathayan",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Disengage", "Eye of the Dragon", "Feigned Flight", "Fire & Flee", "Flammable", "Fly (8)", "Heavenly Beacon", "Impact Hits (D3+1, Sky Lantern only)", "Large Target", "Reserve Move", "Scouts"],
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
    "Cathayan Sentinel": {
        # https://tow.whfb.app/unit/cathayan-sentinel - 230 pts per unit
        # Fights with the Cathayan Sentinel row.
        "points": 230,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 5,
            "BallisticSkill": 1,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 3,
            "Wounds": 6,
            "Attacks": 3,
            "Leadership": 10,
            "Race": "Cathayan",
            "Armor": "Heavy Armor",
            "Weapon": "Scything Blow",
            "Shield": False,
            "SpecialRules": ["Close Order", "Immune to Psychology", "Implacable", "Large Target", "Stomp Attacks (D3+1)", "Terror", "Timmm-berrr!", "Unbreakable"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
            "OptionalRules": ["Terracotta Sentinel", "Jade Sentinel", "Obsidian Sentinel", "Granite Sentinel", "Warpstone Sentinel"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Scything Blow"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Cathayan Grand Cannon": {
        # https://tow.whfb.app/unit/cathayan-grand-cannon - 130 pts per unit
        # Fights with the Cathayan Artillery Crew (x3) row.
        # Also has a profile for Grand Cannon (M- WS- BS- S- T6 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Grand
        # cannon.
        "points": 130,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Grand Cannon', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Cathayan",
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
    "Fire Rain Rocket Battery": {
        # https://tow.whfb.app/unit/fire-rain-rocket-battery - 130 pts per unit
        # Fights with the Cathayan Artillery Crew (x3) row.
        # Also has a profile for Fire Rain Rocket (M- WS- BS- S- T6 W3 I- A- Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: Fire rain
        # rocket.
        "points": 130,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Fire Rain Rocket', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': None, 'Toughness': 6, 'Initiative': None, 'Wounds': 3, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Cathayan",
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
    "Ogre Loader": {
        # https://tow.whfb.app/unit/ogre-loader - 35 pts per unit
        # Fights with the Ogre Loader row.
        # Shooting is not simulated, so these are left out of the options: gunpowder
        # bombs.
        "points": 35,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Ogre",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Enough for Everyone", "Mercenary Crew"],
            "TroopType": "MonstrousInfantry",
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
    "Cathayan Cataphracts": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/cathayan-cataphracts",
        "text": (
            "When a unit in which the majority of the models have this special rule "
            "makes a follow up move, the unit counts as having charged during the "
            "next turn."
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
    "Close Order": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/close-order",
        "text": (
            "A unit consisting of models with this special rule may adopt a Close "
            "Order formation."
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
    "Defensive Stance": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/defensive-stance",
        "text": (
            "Unless it charged during the preceding Movement phase, or counts as "
            "having charged this turn, a unit with this special rule may re-roll "
            "any Armour Save rolls of a natural 1 made during the Combat phase."
        ),
    },
    "Detachment": {
        "status": None,
        "url": "https://tow.whfb.app/warhammer-armies/detachment-special-rules",
        "text": (
            "Detachments follow a number of special rules, representing the "
            "specialised way in which they function alongside their regimental "
            "units: - Regimental Deployment - Regimental Leadership - Regimental "
            "Psychology - Supporting Actions"
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
    "Disengage": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/disengage",
        "text": (
            "Should this model lose a round of combat and Give Ground, it may "
            "choose to Fall Back in Good Order instead. Enemy units can follow up "
            "as if this model had given ground, moving 2\" directly towards it, but "
            "cannot pursue it. In addition, should it win a round of combat and "
            "choose to restrain and reform, this model may choose to Fall Back in "
            "Good Order rather than remaining where it is."
        ),
    },
    "Enough for Everyone": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/enough-for-everyone",
        "text": (
            "If an Ogre Loader is equipped with gunpowder bombs, the crew of the "
            "war machine that Ogre Loader has joined is also equipped with "
            "gunpowder bombs."
        ),
    },
    "Eye of the Dragon": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/eye-of-the-dragon",
        "text": (
            "Friendly models whose weapons shoot using the Bombardment special rule "
            "can shoot using this model's line of sight rather than their own."
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
    "Heavenly Beacon": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/heavenly-beacon",
        "text": (
            "Unless this model is fleeing, friendly units within 12\" of it may re- "
            "roll any failed Panic or Rally test. In addition, whilst this model is "
            "on the battlefield, unless it is fleeing, you may apply a +1 or -1 "
            "modifier to the result when rolling to determine if a friendly unit "
            "with the Ambushers special rule that is currently held in reserve "
            "arrives this turn as reinforcements or is delayed. Finally, a Lord "
            "Magistrate or Strategist mounted on a Sky Lantern has a Command range "
            "of 12\"."
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
    "Implacable": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/implacable",
        "text": (
            "Once per game, during a turn in which it was charged, this model may "
            "choose not to Give Ground should it lose a round of combat. In "
            "addition, once per game this model may re-roll its Charge roll."
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
    "Mercenary Crew": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/mercenary-crew",
        "text": (
            "An Ogre Loader is an additional crew member that can be taken as an "
            "upgrade to accompany a Cathayan war machine. During deployment, "
            "position an Ogre Loader with its war machine, as you would any other "
            "crew member. Once placed, an Ogre Loader cannot leave its war machine. "
            "The crew of any war machine joined by an Ogre Loader gains a + 1 "
            "modifier to its Movement characteristic and the Stubborn special rule. "
            "In addition, once per game, a Fire Rain Rocket Battery or Cathayan "
            "grand cannon that includes an Ogre Loader may fire twice during the "
            "Shooting phase, or re-roll a single Artillery dice."
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
    "Regimental Unit": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/regimental-unit",
        "text": (
            "A unit with this special rule can be accompanied by detachment."
        ),
    },
    "Reserve Move": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/reserve-move",
        "text": (
            "Unless it charged, marched or fled during the Movement phase, a unit "
            "in which the majority of the models have this special rule may make a "
            "Reserve move at the end of the Shooting phase of its turn, after all "
            "shooting has been resolved. A unit making a Reserve move moves as "
            "described in the Basic Movement rules. It may manoeuvre normally, but "
            "cannot march."
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
