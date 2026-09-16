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
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemonic Charge", "Daemons of Khorne", "Fly (10)", "Furious Charge", "Impact Hits (D3)", "Impetuous", "Infernal Favour (2)", "Large Target", "Magic Resistance (-2)", "Terror"],
            "TroopType": "Behemoth",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon", "Flail", "Great Weapon"],
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
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemon of Slaanesh", "Infernal Favour (2)", "Large Target", "Lore of Daemons", "Stomp Attacks (D3)", "Swiftstride", "Terror"],
            "WizardLevel": 1,
            "Lores": ["Daemonology", "Dark Magic", "Illusion"],
            "TroopType": "Behemoth",
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
            "weapons": ["Hand Weapon", "Two Hand Weapons", "Flail"],
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
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Chaos Armour", "Ensorcelled Weapons", "Infernal Favour (2)", "Lore of Daemons"],
            "TroopType": "MonstrousInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
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
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemons of Khorne", "Furious Charge", "Impetuous", "Infernal Favour (1)", "Magic Resistance (-1)"],
            "TroopType": "HeavyInfantry",
            "UnitCategory": "Character",
        },
        "equipment_options": {
            "weapons": ["Hand Weapon"],
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
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemon of Nurgle", "Infernal Favour (1)", "Lore of Daemons", "Poisoned Attacks", "Regeneration (6+)"],
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
            "Weapon": "Hand Weapon",
            "Shield": False,
            "SpecialRules": ["Daemonic", "Ward5 (non-magical)", "Daemonic Instability", "Fear", "Immune to Psychology", "Magical Attacks", "Unbreakable", "Warp-spawned", "Daemon of Slaanesh", "Infernal Favour (1)", "Lore of Daemons"],
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

# Regular (non-character) units go here.
UNITS = {}


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
}

PROFILES = dict(CHARACTERS, **UNITS)
