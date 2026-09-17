"""Daemons of Chaos.

Profiles from https://tow.whfb.app/army/daemons-of-chaos
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = "Daemons of Chaos"

# Other names that should resolve to this faction.
ALIASES = [
    "Daemons",
    "Chaos Daemons",
    "Daemons of Chaos",
    "DoC",
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {
    "Herald of Khorne": "Daemonic Herald of Khorne",
    "Herald of Nurgle": "Daemonic Herald of Nurgle",
    "Herald of Slaanesh": "Daemonic Herald of Slaanesh",
    "Herald of Tzeentch": "Daemonic Herald of Tzeentch",
}

CHARACTERS = {
    "Bloodthirster": {
        # https://tow.whfb.app/unit/bloodthirster - 355 pts
        # Its Bloodflail, Great axe and Lash of Khorne options have not been
        # transcribed; the generic weapons here stand in for them.
        "points": 355,
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 10,
            "BallisticSkill": 5,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 7,
            "Wounds": 6,
            "Attacks": 6,
            "Leadership": 9,
            "Race": "Daemon",
            "Armor": "Heavy Armor",
            "Weapon": "Bloodflail",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemonic Charge", "Daemons of Khorne", "Fly (10)", "Furious Charge", "Impact Hits (D3)", "Impetuous", "Infernal Favour (2)", "Large Target", "Magic Resistance (-2)", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Bloodflail", "Great Axe", "Lash of Khorne"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Keeper of Secrets": {
        # https://tow.whfb.app/unit/keeper-of-secrets - 330 pts
        # Armed with impaling claws, whose profile has not been transcribed; treated
        # as a hand weapon.
        "points": 330,
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 7,
            "BallisticSkill": 6,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 7,
            "Wounds": 6,
            "Attacks": 6,
            "Leadership": 9,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Impaling Claws",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemon of Slaanesh", "Infernal Favour (2)", "Large Target", "Lore of Daemons", "Stomp Attacks (D3)", "Swiftstride", "Terror"],
            "WizardLevel": 1,
            "Lores": ["Daemonology", "Dark Magic", "Illusion"],
            "TroopType": "Behemoth",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Impaling Claws"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Great Unclean One": {
        # https://tow.whfb.app/unit/great-unclean-one - 330 pts
        # Its Bilesword and Plagueflail options have not been transcribed.
        "points": 330,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 6,
            "BallisticSkill": 3,
            "Strength": 6,
            "Toughness": 7,
            "Initiative": 4,
            "Wounds": 7,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemon of Nurgle", "Infernal Favour (2)", "Large Target", "Lore of Daemons", "Poisoned Attacks", "Regeneration (5+)", "Stomp Attacks (D3+1)", "Terror"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic"],
            "TroopType": "Behemoth",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Bilesword", "Plagueflail"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Lord of Change": {
        # https://tow.whfb.app/unit/lord-of-change - 310 pts
        # Its staff of Tzeentch counts as a great weapon.
        "points": 310,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 6,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 6,
            "Wounds": 6,
            "Attacks": 4,
            "Leadership": 9,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Great Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemon of Tzeentch", "Flaming Attacks", "Fly (9)", "Infernal Favour (2)", "Large Target", "Lore of Daemons", "Stomp Attacks (D3)", "Swiftstride", "Terror"],
            "WizardLevel": 2,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Elementalism", "Illusion"],
            "TroopType": "Behemoth",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Great Weapon", "Hand Weapon"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Daemon Prince": {
        # https://tow.whfb.app/unit/daemon-prince-daemons-of-chaos - 210 pts
        # Its Chaos Armour is written without a value on the army list, so no Ward
        # is read from it - only the Daemonic 5+ applies. Worth checking.
        "points": 210,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 7,
            "BallisticSkill": 5,
            "Strength": 6,
            "Toughness": 5,
            "Initiative": 7,
            "Wounds": 4,
            "Attacks": 5,
            "Leadership": 9,
            "Race": "Daemon",
            "Armor": "Light Armor",
            "Weapon": "Ensorcelled Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Chaos Armour", "Infernal Favour (2)", "Lore of Daemons"],
            "WizardLevel": 0,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Ensorcelled Weapon"],
            "armor": ["Light Armor", "Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Daemonic Herald of Khorne": {
        # https://tow.whfb.app/unit/daemonic-herald-of-khorne - 80 pts
        # Carries a Hellblade; its profile has not been transcribed. Its calloused
        # hide counts as light armour.
        "points": 80,
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 7,
            "BallisticSkill": 4,
            "Strength": 5,
            "Toughness": 4,
            "Initiative": 6,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Daemon",
            "Armor": "Light Armor",
            "Weapon": "Hellblade",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Khorne", "Furious Charge", "Impetuous", "Infernal Favour (1)", "Magic Resistance (-1)"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hellblade"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Juggernaut of Khorne", "Blood Throne of Khorne"]
        }
    },
    "Daemonic Herald of Nurgle": {
        # https://tow.whfb.app/unit/daemonic-herald-of-nurgle - 95 pts
        # Carries a Plaguesword; its profile has not been transcribed.
        "points": 95,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 5,
            "BallisticSkill": 5,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Plaguesword",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemon of Nurgle", "Infernal Favour (1)", "Lore of Daemons", "Poisoned Attacks", "Regeneration (6+)"],
            "WizardLevel": 0,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Plaguesword"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Palanquin of Nurgle"]
        }
    },
    "Daemonic Herald of Slaanesh": {
        # https://tow.whfb.app/unit/daemonic-herald-of-slaanesh - 85 pts
        # Armed with piercing claws; their profile has not been transcribed.
        "points": 85,
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 6,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 6,
            "Wounds": 2,
            "Attacks": 3,
            "Leadership": 8,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Piercing Claws",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemon of Slaanesh", "Infernal Favour (1)", "Lore of Daemons"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Piercing Claws"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": ["Steed of Slaanesh", "Seeker Chariot of Slaanesh", "Exalted Seeker Chariot of Slaanesh"]
        }
    },
    "Daemonic Herald of Tzeentch": {
        # https://tow.whfb.app/unit/daemonic-herald-of-tzeentch - 90 pts
        "points": 90,
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 4,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 3,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 8,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemon of Tzeentch", "Infernal Favour (1)", "Lore of Daemons"],
            "WizardLevel": 1,
            "Lores": ["Battle Magic", "Daemonology", "Dark Magic", "Elementalism", "Illusion"],
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
            "mounts": ["Disc of Tzeentch", "Chariot of Tzeentch", "Burning Chariot of Tzeentch"]
        }
    },
}

# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {
    "Beasts of Nurgle": {
        # https://tow.whfb.app/unit/beasts-of-nurgle - 62 pts per model, unit size 2+
        # Its Attacks are D6+1, a dice value the engine cannot use yet; recorded as
        # None, so it makes no attacks.
        # Fights with the Beast of Nurgle row.
        "points": 62,
        "points_per": "model",
        "unit_size": "2+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 4,
            "Attacks": None,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Writhing Tentacles (Daemons of Chaos)",
            "Shield": False,
            "SpecialRules": ["Attention Seeker", "Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Nurgle", "Impetuous", "Infernal Favour (1)", "Loner", "Poisoned Attacks", "Random Attacks", "Regeneration (5+)", "Slime Trail"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Writhing Tentacles (Daemons of Chaos)"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Bloodletters of Khorne": {
        # https://tow.whfb.app/unit/bloodletters-of-khorne - 14 pts per model, unit
        # size 8+
        # Fights with the Bloodletter row.
        "points": 14,
        "points_per": "model",
        "unit_size": "8+",
        "champion": {'Name': 'Bloodreaper', 'Movement': 5, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 3, 'Initiative': 4, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": "Light Armor",
            "Weapon": "Hellblade",
            "Shield": False,
            "SpecialRules": ["Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Khorne", "Impetuous", "Magic Resistance (-1)"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Daemonic Icon"],
        },
        "equipment_options": {
            "weapons": ["Hellblade"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Blue Horrors of Tzeentch": {
        # https://tow.whfb.app/unit/blue-horrors-of-tzeentch - 9 pts per model, unit
        # size 9+
        # Fights with the Blue Horror row.
        # Shooting is not simulated, so these are left out of the options: flames of
        # Tzeentch.
        "points": 9,
        "points_per": "model",
        "unit_size": "9+",
        "champion": {'Name': 'Ectoplasmic Horror', 'Movement': 4, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Tzeentch", "Move Through Cover", "Open Order"],
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
    "Brimstone Horrors of Tzeentch": {
        # https://tow.whfb.app/unit/brimstone-horrors-of-tzeentch - 38 pts per model,
        # unit size 2+
        # Fights with the Brimstone Horrors row.
        "points": 38,
        "points_per": "model",
        "unit_size": "2+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 5,
            "WeaponSkill": 2,
            "BallisticSkill": 2,
            "Strength": 2,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 6,
            "Attacks": 4,
            "Leadership": 5,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Tzeentch", "Flaming Attacks", "Loner", "Skirmishers"],
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
    "Chaos Furies": {
        # https://tow.whfb.app/unit/chaos-furies - 12 pts per model, unit size 5+
        # Fights with the Chaos Fury row.
        "points": 12,
        "points_per": "model",
        "unit_size": "5+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 3,
            "Initiative": 4,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 5,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Daemonic Talons",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Fly (8)", "Furious Charge", "Skirmishers", "Swiftstride", "Vanguard"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Daemons of Khorne", "Daemons of Nurgle", "Daemons of Slaanesh", "Daemons of Tzeentch"],
        },
        "equipment_options": {
            "weapons": ["Daemonic Talons"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Daemonettes of Slaanesh": {
        # https://tow.whfb.app/unit/daemonettes-of-slaanesh - 11 pts per model, unit
        # size 6+
        # Fights with the Daemonette row.
        "points": 11,
        "points_per": "model",
        "unit_size": "6+",
        "champion": {'Name': 'Alluress', 'Movement': 5, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Piercing Claws",
            "Shield": False,
            "SpecialRules": ["Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Slaanesh"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Daemonic Icon"],
        },
        "equipment_options": {
            "weapons": ["Piercing Claws"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Flamers of Tzeentch": {
        # https://tow.whfb.app/unit/flamers-of-tzeentch - 40 pts per model, unit size
        # 3-6
        # Fights with the Flamer row.
        # Also has a profile for Exalted Flamer (M6 WS2 BS5 S4 T4 W3 I4 A2 Ld7); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: warpflame.
        "points": 40,
        "points_per": "model",
        "unit_size": "3-6",
        "champion": {'Name': 'Pyroclaster', 'Movement': 6, 'WeaponSkill': 2, 'BallisticSkill': 5, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 2, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Exalted Flamer', 'Movement': 6, 'WeaponSkill': 2, 'BallisticSkill': 5, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 3, 'Attacks': 2, 'Leadership': 7},
        ],
        "base_profile": {
            "Movement": 6,
            "WeaponSkill": 2,
            "BallisticSkill": 4,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Tzeentch", "Flaming Attacks", "Infernal Favour (1, Exalted Flamer only)", "Lore of Daemons (Exalted Flamer only)", "Move Through Cover", "Skirmishers"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "WizardLevel": 1,
            "Lores": ["Daemonology", "Dark Magic", "Elementalism", "Illusion"],
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
    "Nurglings": {
        # https://tow.whfb.app/unit/nurglings - 45 pts per model, unit size 3+
        # Its Attacks are D3+1, a dice value the engine cannot use yet; recorded as
        # None, so it makes no attacks.
        # Fights with the Nurglings row.
        "points": 45,
        "points_per": "model",
        "unit_size": "3+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 2,
            "BallisticSkill": 0,
            "Strength": 2,
            "Toughness": 3,
            "Initiative": 2,
            "Wounds": 7,
            "Attacks": None,
            "Leadership": 5,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Nurgle", "Loner", "Poisoned Attacks", "Random Attacks", "Regeneration (6+)", "Skirmishers"],
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
    "Pink Horrors of Tzeentch": {
        # https://tow.whfb.app/unit/pink-horrors-of-tzeentch - 12 pts per model, unit
        # size 9+
        # Fights with the Pink Horror row.
        # Shooting is not simulated, so these are left out of the options: flames of
        # Tzeentch.
        "points": 12,
        "points_per": "model",
        "unit_size": "9+",
        "champion": {'Name': 'Iridescent Horror', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 3, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
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
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Tzeentch", "Scintillating Sorcery"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Daemonic Icon"],
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
    "Plaguebearers of Nurgle": {
        # https://tow.whfb.app/unit/plaguebearers-of-nurgle - 13 pts per model, unit
        # size 7+
        # Fights with the Plaguebearer row.
        "points": 13,
        "points_per": "model",
        "unit_size": "7+",
        "champion": {'Name': 'Plagueridden', 'Movement': 4, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 2, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [],
        "base_profile": {
            "Movement": 4,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 2,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Plaguesword",
            "Shield": False,
            "SpecialRules": ["Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Nurgle", "Poisoned Attacks", "Regeneration (6+)"],
            "TroopType": "RegularInfantry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Daemonic Icon"],
        },
        "equipment_options": {
            "weapons": ["Plaguesword"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Bloodcrushers of Khorne": {
        # https://tow.whfb.app/unit/bloodcrushers-of-khorne - 65 pts per model, unit
        # size 3+
        # Fights with the Bloodletter row.
        # Also has a profile for Juggernaut of Khorne (M7 WS4 BS- S5 T- W- I2 A2 Ld-);
        # not simulated.
        "points": 65,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Bloodreaper', 'Movement': None, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 4, 'Initiative': 4, 'Wounds': 3, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Juggernaut of Khorne', 'Movement': 7, 'WeaponSkill': 4, 'BallisticSkill': None, 'Strength': 5, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 3,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": "Light Armor",
            "Weapon": "Hellblade",
            "Shield": False,
            "SpecialRules": ["Armoured Hide (1)", "Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Khorne", "Impact Hits (2)", "Impetuous", "Magic Resistance (-1)", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Daemonic Icon"],
        },
        "equipment_options": {
            "weapons": ["Hellblade"],
            "armor": ["Light Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Fiends of Slaanesh": {
        # https://tow.whfb.app/unit/fiends-of-slaanesh - 66 pts per model, unit size
        # 3+
        # Fights with the Fiend of Slaanesh row.
        "points": 66,
        "points_per": "model",
        "unit_size": "3+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 4,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 6,
            "Wounds": 3,
            "Attacks": 3,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Piercing Claws",
            "Shield": False,
            "SpecialRules": ["Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Slaanesh", "Soporific Musk", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Piercing Claws", "Venomous Tail"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Flesh Hounds of Khorne": {
        # https://tow.whfb.app/unit/flesh-hounds-of-khorne - 32 pts per model, unit
        # size 5+
        # Fights with the Flesh Hound row.
        "points": 32,
        "points_per": "model",
        "unit_size": "5+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 5,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": "Light Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1)", "Close Order", "Counter Charge", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Khorne", "Impetuous", "Magic Resistance (-2)"],
            "TroopType": "HeavyCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Ambushers", "Vanguard"],
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
    "Plague Drones of Nurgle": {
        # https://tow.whfb.app/unit/plague-drones-of-nurgle - 63 pts per model, unit
        # size 3+
        # Fights with the Plaguebearer row.
        # Also has a profile for Rot Fly (M1 WS3 BS- S5 T- W- I2 A3 Ld-); not
        # simulated.
        # Shooting is not simulated, so these are left out of the options: death's
        # heads.
        "points": 63,
        "points_per": "model",
        "unit_size": "3+",
        "champion": {'Name': 'Plagueridden', 'Movement': None, 'WeaponSkill': 3, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': 5, 'Initiative': 2, 'Wounds': 3, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Rot Fly', 'Movement': 1, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 5, 'Toughness': None, 'Initiative': 2, 'Wounds': None, 'Attacks': 3, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 4,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 3,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Plaguesword",
            "Shield": False,
            "SpecialRules": ["Armour Bane (2, Rot Fly only)", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Nurgle", "Fly (9)", "Poisoned Attacks", "Regeneration (6+)", "Skirmishers", "Swiftstride"],
            "TroopType": "MonstrousCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Daemonic Icon", "Plague Proboscis"],
        },
        "equipment_options": {
            "weapons": ["Plaguesword", "Venom Sting"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Screamers of Tzeentch": {
        # https://tow.whfb.app/unit/screamers-of-tzeentch - 44 pts per model, unit
        # size 3+
        # Fights with the Screamer row.
        "points": 44,
        "points_per": "model",
        "unit_size": "3+",
        "other_profiles": [],
        "base_profile": {
            "Movement": 1,
            "WeaponSkill": 3,
            "BallisticSkill": 0,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 2,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Lamprey's Bite",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Tzeentch", "Fly (9)", "Loner", "Skirmishers", "Slashing Attack"],
            "TroopType": "WarBeast",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Lamprey's Bite"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Seekers of Slaanesh": {
        # https://tow.whfb.app/unit/seekers-of-slaanesh - 21 pts per model, unit size
        # 5+
        # Fights with the Seeker row.
        # Also has a profile for Steed of Slaanesh (M9 WS3 BS- S3 T- W- I5 A1 Ld-);
        # not simulated.
        "points": 21,
        "points_per": "model",
        "unit_size": "5+",
        "champion": {'Name': 'Heartseeker', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': 3, 'Initiative': 5, 'Wounds': 1, 'Attacks': 2, 'Leadership': 7},
        "other_profiles": [
            {'Name': 'Steed of Slaanesh', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 5, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 3,
            "Initiative": 5,
            "Wounds": 1,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": None,
            "Weapon": "Piercing Claws",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1, Steed of Slaanesh only)", "Counter Charge", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Slaanesh", "Fast Cavalry", "Open Order", "Poisoned Attacks (Steed of Slaanesh only)", "Skirmishers", "Swiftstride"],
            "TroopType": "LightCavalry",
            "UnitCategory": "Unit",
            "OptionalRules": ["Daemonic Icon"],
        },
        "equipment_options": {
            "weapons": ["Piercing Claws"],
            "armor": [],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Burning Chariot of Tzeentch": {
        # https://tow.whfb.app/unit/burning-chariot-of-tzeentch - 190 pts per unit
        # Fights with the Exalted Flamer row, using the Burning Chariot of Tzeentch
        # row's Toughness and Wounds.
        # Also has a profile for Burning Chariot of Tzeentch (M- WS- BS- S4 T4 W4 I-
        # A- Ld-); not simulated.
        # Also has a profile for Blue Horror Crew (x3) (M- WS2 BS3 S3 T- W- I3 A1
        # Ld7); not simulated.
        # Also has a profile for Screamer (x2) (M1 WS3 BS- S4 T- W- I4 A2 Ld-); not
        # simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: warpflame.
        "points": 190,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Burning Chariot of Tzeentch', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 4, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Blue Horror Crew (x3)', 'Movement': None, 'WeaponSkill': 2, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': None, 'Initiative': 3, 'Wounds': None, 'Attacks': 1, 'Leadership': 7},
            {'Name': 'Screamer (x2)', 'Movement': 1, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 4, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 2, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 2,
            "BallisticSkill": 5,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Tzeentch", "Fly (9)", "Impact Hits (D6+1)", "Lore of Daemons", "Slashing Attack (Screamers only)"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
            "WizardLevel": 1,
            "Lores": ["Daemonology", "Dark Magic", "Elementalism", "Illusion"],
            "OptionalRules": ["Daemonic Gifts"],
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
    "Chariot of Tzeentch": {
        # https://tow.whfb.app/unit/chariot-of-tzeentch - None pts per unit
        # Fights with the Screamer (x2) row, using the Chariot of Tzeentch row's
        # Toughness and Wounds.
        # Also has a profile for Chariot of Tzeentch (M- WS- BS- S4 T4 W4 I- A- Ld-);
        # not simulated.
        # Armour value 4+ as printed on the site.
        "points": 90,
        "points_note": "+90",
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Chariot of Tzeentch', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 4, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": 1,
            "WeaponSkill": 3,
            "BallisticSkill": None,
            "Strength": 4,
            "Toughness": 4,
            "Initiative": 4,
            "Wounds": 4,
            "Attacks": 2,
            "Leadership": None,
            "Race": "Daemon",
            "Armor": "Full Plate Armor",
            "Weapon": "Lamprey's Bite",
            "Shield": False,
            "SpecialRules": ["Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Tzeentch", "Fly (9)", "Impact Hits (D6+1)", "Slashing Attack (Screamers only)"],
            "TroopType": "HeavyChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Lamprey's Bite"],
            "armor": ["Full Plate Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Hellflayer of Slaanesh": {
        # https://tow.whfb.app/unit/hellflayer-of-slaanesh - 145 pts per unit
        # Fights with the Exalted Alluress row, using the Hellflayer row's Toughness
        # and Wounds.
        # Also has a profile for Hellflayer (M- WS- BS- S4 T4 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Daemonette Crew (x2) (M- WS4 BS3 S3 T- W- I5 A1 Ld7);
        # not simulated.
        # Also has a profile for Steed of Slaanesh (x2) (M9 WS3 BS- S3 T- W- I5 A1
        # Ld-); not simulated.
        # Armour value 5+ as printed on the site.
        "points": 145,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Hellflayer', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 4, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Daemonette Crew (x2)', 'Movement': None, 'WeaponSkill': 4, 'BallisticSkill': 3, 'Strength': 3, 'Toughness': None, 'Initiative': 5, 'Wounds': None, 'Attacks': 1, 'Leadership': 7},
            {'Name': 'Steed of Slaanesh (x2)', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 5, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 5,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 4,
            "Attacks": 2,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": "Heavy Armor",
            "Weapon": "Piercing Claws",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1, Steed of Slaanesh only)", "Close Order", "Counter Charge", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Slaanesh", "First Charge", "Impact Hits (2D6+1)", "Poisoned Attacks (Steed of Slaanesh only)", "Swiftstride"],
            "TroopType": "LightChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Piercing Claws"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Seeker Chariot of Slaanesh": {
        # https://tow.whfb.app/unit/seeker-chariot-of-slaanesh - 100 pts per model,
        # unit size 1-3
        # Fights with the Daemonette Crew (x2) row, using the Seeker Chariot row's
        # Toughness and Wounds.
        # Also has a profile for Seeker Chariot (M- WS- BS- S4 T4 W4 I- A- Ld-); not
        # simulated.
        # Also has a profile for Steed of Slaanesh (x2) (M9 WS3 BS- S3 T- W- I5 A1
        # Ld-); not simulated.
        # Armour value 5+ as printed on the site.
        "points": 100,
        "points_per": "model",
        "unit_size": "1-3",
        "other_profiles": [
            {'Name': 'Seeker Chariot', 'Movement': None, 'WeaponSkill': None, 'BallisticSkill': None, 'Strength': 4, 'Toughness': 4, 'Initiative': None, 'Wounds': 4, 'Attacks': None, 'Leadership': None},
            {'Name': 'Steed of Slaanesh (x2)', 'Movement': 9, 'WeaponSkill': 3, 'BallisticSkill': None, 'Strength': 3, 'Toughness': None, 'Initiative': 5, 'Wounds': None, 'Attacks': 1, 'Leadership': None},
        ],
        "base_profile": {
            "Movement": None,
            "WeaponSkill": 4,
            "BallisticSkill": 3,
            "Strength": 3,
            "Toughness": 4,
            "Initiative": 5,
            "Wounds": 4,
            "Attacks": 1,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": "Heavy Armor",
            "Weapon": "Piercing Claws",
            "Shield": False,
            "SpecialRules": ["Armour Bane (1, Steed of Slaanesh only)", "Counter Charge", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Slaanesh", "First Charge", "Impact Hits (D3+1)", "Open Order", "Poisoned Attacks (Steed of Slaanesh only)", "Swiftstride"],
            "TroopType": "LightChariot",
            "UnitCategory": "Unit",
        },
        "equipment_options": {
            "weapons": ["Piercing Claws"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
    "Skull Cannon of Khorne": {
        # https://tow.whfb.app/unit/skull-cannon-of-khorne - 185 pts per unit
        # Fights with the Skull Cannon row.
        # Also has a profile for Bloodletter Crew (2x) (M- WS5 BS3 S4 T- W- I4 A1
        # Ld7); not simulated.
        # Armour value 4+ as printed on the site.
        # Shooting is not simulated, so these are left out of the options: cannon of
        # Khorne.
        "points": 185,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [
            {'Name': 'Bloodletter Crew (2x)', 'Movement': None, 'WeaponSkill': 5, 'BallisticSkill': 3, 'Strength': 4, 'Toughness': None, 'Initiative': 4, 'Wounds': None, 'Attacks': 1, 'Leadership': 7},
        ],
        "base_profile": {
            "Movement": 7,
            "WeaponSkill": 5,
            "BallisticSkill": None,
            "Strength": 5,
            "Toughness": 5,
            "Initiative": 2,
            "Wounds": 4,
            "Attacks": 3,
            "Leadership": None,
            "Race": "Daemon",
            "Armor": "Full Plate Armor",
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Brazen Wheels", "Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Khorne", "First Charge", "Impact Hits (D3+1)", "Impetuous", "Stomp Attacks (D3)"],
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
    "Soul Grinder": {
        # https://tow.whfb.app/unit/soul-grinder - 255 pts per unit
        # Fights with the Soul Grinder row.
        # Shooting is not simulated, so these are left out of the options: Baleful
        # torrent, Warp gaze, harvester cannon.
        "points": 255,
        "points_per": "unit",
        "unit_size": "1",
        "other_profiles": [],
        "base_profile": {
            "Movement": 8,
            "WeaponSkill": 3,
            "BallisticSkill": 3,
            "Strength": 6,
            "Toughness": 6,
            "Initiative": 3,
            "Wounds": 6,
            "Attacks": 4,
            "Leadership": 7,
            "Race": "Daemon",
            "Armor": "Heavy Armor",
            "Weapon": "Iron Claw",
            "Shield": False,
            "SpecialRules": ["Close Order", "Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Furious Charge", "Large Target", "Reserve Move", "Stomp Attacks (D6+1)", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Unit",
            "OptionalRules": ["Daemon of Khorne", "Daemon of Nurgle", "Daemons of Slaanesh", "Daemons of Tzeentch"],
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Iron Claw"],
            "armor": ["Heavy Armor"],
            "shield": False,
            "items": [],
        },
        "mount_options": {
            "mounts": []
        }
    },
}


# Army-wide special rules for this faction. `status` is how far the engine
# goes with each: "implemented", "partial", or None for recorded only.
FACTION_RULES = {
    'Daemonic': {
        "status": 'implemented',
        "text": (
            "A 5+ Ward save against wounds from non-magical enemy attacks, plus "
            "Daemonic Instability, Fear, Immune to Psychology, Magical Attacks, "
            "Unbreakable and Warp-spawned. Expanded into its parts on each "
            "profile. "
        ),
    },
    'Infernal Favour (X)': {
        "status": None,
        "text": (
            "Reduces wounds suffered from Daemonic Instability by X. It is NOT "
            "a Ward save, and instability does not occur in a duel. "
        ),
    },
    'Daemonic Instability': {
        "status": None,
        "text": (
            "Army-wide; no effect in a duel. "
        ),
    },
    'Lore of Daemons': {
        "status": None,
        "text": (
            "Magic is not simulated. "
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
    "Attention Seeker": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/attention-seeker",
        "text": (
            "Every model in a unit of Beasts of Nurgle can issue and accept "
            "challenges in the same manner as a character."
        ),
    },
    "Brazen Wheels": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/brazen-wheels",
        "text": (
            "Stomp Attacks made by a Skull Cannon of Khorne have an Armour Piercing "
            "characteristic of -3. However, this rule cannot be used against models "
            "whose troop type is behemoth – they are simply too large to be caught "
            "beneath a Skull Cannon's wheels."
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
    "Daemons of Khorne": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/daemon-of-khorne",
        "text": (
            "Daemons of Khorne have the Hatred (Daemons of Slaanesh) special rule. "
            "In addition, during a turn in which it made a charge move, a Daemon of "
            "Khorne (but not its mount) gains a +1 modifier to its Strength "
            "characteristic."
        ),
    },
    "Daemons of Nurgle": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/daemon-of-nurgle",
        "text": (
            "Daemons of Nurgle have the Hatred (Daemons of Tzeentch) special rule. "
            "In addition, any enemy model that directs its attacks against a Daemon "
            "of Nurgle during the Combat phase must re-roll any rolls To Hit of a "
            "natural 6."
        ),
    },
    "Daemons of Slaanesh": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/daemon-of-slaanesh",
        "text": (
            "Daemons of Slaanesh have the Hatred (Daemons of Khorne) special rule. "
            "In addition, Daemons of Slaanesh increase their maximum possible "
            "charge range by 1\" and have a +1 modifier to the result of any Charge "
            "or Pursuit roll they make."
        ),
    },
    "Daemons of Tzeentch": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/daemon-of-tzeentch",
        "text": (
            "Daemons of Tzeentch have the Hatred (Daemons of Nurgle) special rule. "
            "In addition, a Daemon of Tzeentch that is also a Wizard may apply a +1 "
            "modifier to any Casting roll they make. Note that this is a modifier "
            "to the result of a roll – it does not negate a roll of a natural "
            "double 1."
        ),
    },
    "Fast Cavalry": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/fast-cavalry",
        "text": (
            "If all of the models (including characters) within a unit arrayed in "
            "an Open Order formation have this special rule, the unit may perform "
            "its Quick Turn even if it marched."
        ),
    },
    "First Charge": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/first-charge",
        "text": (
            "If this unit's first charge of the game is successful (i.e., if the "
            "unit makes contact with the charge target), the charge target becomes "
            "Disrupted until the end of the Combat phase of that turn."
        ),
    },
    "Flaming Attacks": {
        "status": "implemented",
        "url": "https://tow.whfb.app/special-rules/flaming-attacks",
        "text": (
            "Any attack made or hits caused by a model with this special rule, or "
            "made using a weapon or spell with this special rule, is a 'Flaming' "
            "attack. In addition, a model with this special rule causes Fear in "
            "models whose troop type is war beasts or swarms. Unless otherwise "
            "stated, a model with this special rule makes Flaming attacks both when "
            "shooting and in combat (though any spells cast by the model are "
            "unaffected, as are any attacks made with magic weapons they might be "
            "wielding)."
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
    "Impetuous": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/impetuous",
        "text": (
            "If during the Declare Charges & Charge Reactions sub-phase of its "
            "turn, a unit that includes one or more Impetuous models is able to "
            "declare a charge, it must make a Leadership test. If this test is "
            "failed, the unit must declare a charge. If this test is passed, the "
            "unit may act as normal."
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
    "Scintillating Sorcery": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/scintillating-sorcery",
        "text": (
            "A unit of Pink Horrors knows one of the spells that corresponds to "
            "their Daemonic Alignment (chosen by their controlling player before "
            "armies are deployed). The unit may cast this spell as a Bound spell, "
            "with a Power Level equal to the unit's current Rank Bonus."
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
    "Slashing Attack": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/slashing-attack",
        "text": (
            "A unit with this special rule may perform a 'Slashing Attack' against "
            "a single enemy unit that is not engaged in combat. To do so, this unit "
            "must move (by flying) over the unit it wishes to attack during the "
            "Remaining Moves sub-phase. Once this unit's movement is complete, the "
            "enemy unit suffers D3 Strength 4 hits, each with an AP of -, for each "
            "model in this unit that moved over it."
        ),
    },
    "Slime Trail": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/slime-trail",
        "text": (
            "Enemy units cannot claim any bonus combat result points for being "
            "engaged within this unit's flank or rear arc."
        ),
    },
    "Soporific Musk": {
        "status": None,
        "url": "https://tow.whfb.app/special-rules/soporific-musk",
        "text": (
            "Enemy models engaged in combat with a model with this special rule "
            "cannot use the Strike First special rule. Enemy models that do not "
            "have the Strike First special rule become subject to the Strike Last "
            "special rule instead."
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
}

PROFILES = dict(CHARACTERS, **UNITS)
