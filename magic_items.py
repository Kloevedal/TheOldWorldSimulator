"""Magic items and named wargear.

Each entry records what the item does as a list of special-rule strings the
combat engine already understands. Items that are *weapons* carry no rules
here - their profile lives in `MeleeWeaponDict` and reaches the character
through the normal weapon system - but they are still listed so that
`apply_magic_items` knows they are accounted for rather than unrecognised.

Rules text from https://tow.whfb.app/magic-item/<slug>.
"""

from __future__ import annotations

from special_rules import (
    DaemonicWard,
    Flammable,
    ForceRerollOneHit,
    ImmuneToKillingBlow,
    ImproveArmor1InCombat,
    ImproveArmor2InShooting,
    RerollArmourSaves1,
)

# "is_weapon" items are equipment: see MeleeWeaponDict for their profiles.
MagicItemDict = {
    "The Pelt of Charandis": {
        "type": "Enchanted Item",
        "rules": [ImproveArmor1InCombat, ImproveArmor2InShooting, "Regen5"],
        "text": (
            "Improves armour value by 1 in combat, and by 2 (to a maximum of 2+) "
            "against non-magical shooting. Grants Regeneration (5+)."
        ),
    },
    "Trollhide Shawl": {
        "type": "Talisman",
        "rules": [ImproveArmor1InCombat, "Regen5", Flammable],
        "text": (
            "Improves armour value by 1. Grants Regeneration (5+) and Flammable."
        ),
    },
    "Da Boss's Trophy Rack": {
        "type": "Enchanted Item",
        "rules": [],
        "text": (
            "On a turn in which he charged, Kiknik and any Goblin Wolf Rider Mob "
            "he has joined cause Fear and gain +1 combat result. Neither Fear nor "
            "combat result applies to a one-on-one duel."
        ),
    },
    "Lore Familiar": {
        "type": "Arcane Item",
        "rules": [],
        "text": (
            "The owner chooses their spells rather than generating them randomly. "
            "Inert until magic is simulated."
        ),
    },
    "Chayal": {"type": "Magic Weapon", "is_weapon": True},
    "Mathlann's Ire": {"type": "Magic Weapon", "is_weapon": True},
    "Da Skull Smasha": {"type": "Magic Weapon", "is_weapon": True},
    "Bog-wood Staff": {"type": "Magic Weapon", "is_weapon": True},
    "Storm's Wrath": {"type": "Magic Weapon", "is_weapon": True},
    "Mansmasher": {"type": "Magic Weapon", "is_weapon": True},
    "Grisly Totem": {
        "type": "Magic Weapon", "is_weapon": True, "verified": False,
        "text": ("Kralmaw's Braystaff. Its profile has not been transcribed, so "
                 "it currently behaves as a plain staff."),
    },
    "Skull of the Unicorn Lord": {
        "type": "Enchanted Item", "rules": [], "verified": False,
        "text": "Page did not load; rules not transcribed.",
    },
    "Judgement": {"type": "Magic Weapon", "is_weapon": True},
    "Beast Reaver": {"type": "Magic Weapon", "is_weapon": True},
    "Axe of Dargo": {"type": "Magic Weapon", "is_weapon": True},
    "Grudge-Settler": {
        "type": "Magic Weapon", "is_weapon": True,
        "text": ("Inscribed with the Master Rune of Smiting and the Rune of "
                 "Parrying; individual runes are not modelled."),
    },
    "Furnace Hammer": {"type": "Magic Weapon", "is_weapon": True},
    "Rivet Gun": {
        "type": "Magic Weapon", "is_weapon": True,
        "text": ("Range 10\", S3, AP -2, Armour Bane (1), and causes D3 hits on a "
                 "successful roll To Hit. Shooting is not simulated."),
    },
    "Griffon Helm": {
        "type": "Magic Armour",
        "rules": ["Ward5", ImmuneToKillingBlow],
        "text": ("A 5+ Ward save against any wound, and immunity to Killing "
                 "Blow - a Killing Blow costs the wearer a single Wound "
                 "instead, with armour and Regeneration saves as normal."),
    },
    "Slayer Crown": {
        "type": "Enchanted Item",
        "rules": ["AH2", "Ward5"],
        "text": "Improves armour value by 2, and a 5+ Ward against any wounds.",
    },
    "Grudgestone": {
        "type": "Enchanted Item",
        "rules": [],
        "text": ("Once set, Thorgrim and his unit gain Unbreakable and auto-pass "
                 "Panic, but may not Flee or move freely. All of that is army- "
                 "and movement-level, so it does nothing in a duel."),
    },
    "Armour of Skaldour": {
        "type": "Magic Armour",
        # The armour itself is heavy armour, set on Thorgrim's profile; this is
        # the ward it adds on top.
        "rules": ["Ward4 (Killing Blow, Multiple Wounds)"],
        "text": ("A suit of heavy armour. Its wearer also has a 4+ Ward save "
                 "against a Killing Blow, or against wounds from an attack with "
                 "Multiple Wounds (X)."),
    },

    # Named characters from the later army lists. Rules read from each item's
    # page data on https://tow.whfb.app/magic-item/<slug>.
    "Talons of the Storm": {"type": "Magic Weapon", "is_weapon": True},
    "Sorrow's End": {"type": "Magic Weapon", "is_weapon": True},
    "The Dolorous Blade": {
        "type": "Magic Weapon", "is_weapon": True,
        "text": ("Two profiles, chosen at the start of each round: Rapid "
                 "Strikes (S, AP -1, Extra Attacks (+D6)) or Deadly Blows (S+2, "
                 "AP -1, Armour Bane (1), Multiple Wounds (2)). Both have "
                 "Magical Attacks. The Green Knight defaults to Deadly Blows."),
    },
    "Dragonblade": {"type": "Magic Weapon", "is_weapon": True},
    "The Flail of Conquered Kings": {"type": "Magic Weapon", "is_weapon": True},
    "The Blessed Blade of Ptra": {"type": "Magic Weapon", "is_weapon": True},
    "Spear of Talsyn": {"type": "Magic Weapon", "is_weapon": True},
    "The Spear of Kurnous": {
        "type": "Magic Weapon", "is_weapon": True,
        "text": ("Also has a ranged profile (18\", S+1, AP -2, shoots like a "
                 "bolt thrower); shooting is not simulated."),
    },
    "Hawk's Talon": {
        "type": "Magic Weapon", "is_weapon": True,
        "text": ("Orion's bow: 30\", S, AP -1, Magical Attacks, Multiple Shots "
                 "(D3+1). Shooting is not simulated."),
    },
    "Dragonhide Cloak": {
        "type": "Talisman",
        "rules": [ImmuneToKillingBlow, "Ward3 (Flaming)"],
        "text": ("Non-magical weapons attacking Sir Cecil have their AP reduced "
                 "by 2 (not modelled). He is immune to Killing Blow and to "
                 "Multiple Wounds (X) - an unsaved wound from either costs a "
                 "single Wound (Multiple Wounds immunity is not modelled) - and "
                 "has a 3+ Ward save against Flaming Attacks."),
    },
    "The Scarab Brooch of Usirian": {
        "type": "Talisman",
        "rules": ["Ward5"],
        "text": "Grants Settra a 5+ Ward save against any wounds suffered.",
    },
    "Cloak of Isha": {
        "type": "Talisman",
        "rules": ["Ward5"],
        "text": ("Grants Orion a 5+ Ward save. He also recovers a Wound on a 5+ "
                 "in each of his Start of Turn sub-phases, which a duel never "
                 "reaches."),
    },
    "Chalice of Brionne": {
        "type": "Enchanted Item",
        "rules": [],
        "text": ("Enemy characters in Lady Elisse's Command range suffer -2 "
                 "Leadership when using a rule or item that needs a Leadership "
                 "test. No duel effect."),
    },
    "The Staff of the Elements": {
        "type": "Arcane Item",
        "rules": [],
        "text": "Spell selection. Inert until magic is simulated.",
    },
    "The Chariot of the Gods": {
        "type": "Unique",
        "rules": [],
        "text": ("Settra's chariot: its Impact Hits are Flaming and Magical. "
                 "Chariots and Impact Hits are not simulated."),
    },
    "The Crown of Nehekhara": {
        "type": "Enchanted Item",
        "rules": [],
        "text": ("Extends My Will Be Done to every Nehekharan Undead unit within "
                 "6\". No duel effect."),
    },
    "Horn of the Wild Hunt": {
        "type": "Enchanted Item",
        "rules": [],
        "text": ("Once per game, friendly units in Orion's Command range gain "
                 "Frenzy until the end of the turn. Command-phase only."),
    },
    "Warpstone Tokens": {
        "type": "Arcane Item",
        "rules": [],
        "text": ("Single use: add D3 to a Casting roll, losing a Wound on each "
                 "natural 1. Inert until magic is simulated."),
    },
}


# The common magic items from the rulebook, available to any army. `cost` is
# in points; an asterisk on the site marks an Extremely Common item, which an
# army may take more than once (`extremely_common`). Rules text from
# https://tow.whfb.app/magic-item/<slug>, read from the page data.
#
# Only effects a one-on-one duel can use are turned into rules. Single-use
# items, potions, spell and movement effects, and banners (which belong to
# units) carry no rules and say why.
_NOT_IN_A_DUEL = "No effect in a one-on-one duel."
_SINGLE_USE = "Single-use items are not modelled yet."
COMMON_MAGIC_ITEMS = {
    # Magic weapons: profiles in MeleeWeaponDict.
    "Berserker Blade": {"type": "Magic Weapon", "cost": 20, "is_weapon": True,
                        "text": "S+1, Extra Attacks (+1), Magical Attacks; the wielder is Impetuous."},
    "Biting Blade": {"type": "Magic Weapon", "cost": 15, "is_weapon": True},
    "Burning Blade": {"type": "Magic Weapon", "cost": 5, "is_weapon": True,
                      "extremely_common": True},
    "Diestro's Blade": {"type": "Magic Weapon", "cost": 10, "is_weapon": True,
                        "text": "AP -1, Magical Attacks; +1 Initiative (not modelled)."},
    "Dragon Slaying Sword": {"type": "Magic Weapon", "cost": 50, "is_weapon": True,
                             "text": "Magical Attacks, Monster Slayer (not modelled)."},
    "Duellist's Blades": {"type": "Magic Weapon", "cost": 55, "is_weapon": True},
    "Giant Blade": {"type": "Magic Weapon", "cost": 30, "is_weapon": True},
    "Headsman's Axe": {"type": "Magic Weapon", "cost": 45, "is_weapon": True},
    "Ogre Blade": {"type": "Magic Weapon", "cost": 75, "is_weapon": True},
    "Skirmisher's Blade": {"type": "Magic Weapon", "cost": 25, "is_weapon": True,
                           "text": ("Rerolls failed To Wound rolls against an "
                                    "enemy's flank or rear; a duel has neither.")},
    "Spelleater Axe": {"type": "Magic Weapon", "cost": 35, "is_weapon": True},
    "Sword of Battle": {"type": "Magic Weapon", "cost": 60, "is_weapon": True},
    "Sword of Might": {"type": "Magic Weapon", "cost": 20, "is_weapon": True,
                       "extremely_common": True},
    "Sword of Striking": {"type": "Magic Weapon", "cost": 15, "is_weapon": True,
                          "extremely_common": True,
                          "text": "Magical Attacks; +1 To Hit in combat (not modelled)."},
    "Sword of Swiftness": {"type": "Magic Weapon", "cost": 25, "is_weapon": True},
    "Thornspitter Stave": {"type": "Magic Weapon", "cost": 20, "is_weapon": True,
                           "text": "Its ranged profile (24\", S4, AP -, Armour Bane (1), Ponderous) is not simulated."},
    "Trailblazer's Hatchet": {"type": "Magic Weapon", "cost": 15, "is_weapon": True},

    # Magic armour.
    "Armour of Destiny": {
        "type": "Magic Armour", "cost": 70, "armour": "Heavy Armor",
        "rules": ["Ward4"],
        "text": "A suit of heavy armour; its wearer has a 4+ Ward save.",
    },
    "Armour of Meteoric Iron": {
        "type": "Magic Armour", "cost": 20, "rules": [],
        "text": ("An armour value of 5+ that cannot be improved or reduced in "
                 "any way. Not modelled: the engine has no armour that ignores "
                 "Armour Piercing."),
    },
    "Armour of Silvered Steel": {
        "type": "Magic Armour", "cost": 40, "rules": [],
        "text": ("An armour value of 3+ that cannot be improved. Not modelled: "
                 "there is no 3+ armour type."),
    },
    "Bedazzling Helm": {
        "type": "Magic Armour", "cost": 60, "rules": [ImproveArmor1InCombat],
        "text": ("Infantry or cavalry only; worn with other armour. Improves "
                 "armour value by 1 (to a maximum of 2+). Enemies attacking the "
                 "wearer suffer -1 To Hit (not modelled)."),
    },
    "Charmed Shield": {
        "type": "Magic Armour", "cost": 5, "extremely_common": True,
        "shield": True, "rules": [],
        "text": "A shield. Once per game, a 5+ Ward against a single wound. " + _SINGLE_USE,
    },
    "Enchanted Shield": {
        "type": "Magic Armour", "cost": 10, "extremely_common": True,
        "shield": True, "rules": ["Ward6 (non-magical)"],
        "text": "A shield. Its bearer has a 6+ Ward save against non-magical attacks.",
    },
    "Glittering Scales": {
        "type": "Magic Armour", "cost": 35, "armour": "Light Armor",
        "rules": [ForceRerollOneHit],
        "text": ("A suit of light armour. Once per turn, the opponent must "
                 "re-roll a single roll To Hit against the wearer."),
    },
    "Helm of Courage": {
        "type": "Magic Armour", "cost": 25, "rules": [ImproveArmor1InCombat],
        "text": ("Worn with other armour; improves armour value by 1. Once per "
                 "game, a re-roll of a Break test (no duel effect)."),
    },
    "Iron-rimmed Shield": {
        "type": "Magic Armour", "cost": 15, "shield": True, "rules": [],
        "text": ("A shield. +1 Attack for the bearer, made with an ordinary "
                 "hand weapon (not modelled)."),
    },
    "Padded Hauberk": {
        "type": "Magic Armour", "cost": 20, "armour": "Heavy Armor", "rules": [],
        "text": ("A suit of heavy armour. Improves armour value by 1 against "
                 "attacks with AP '-' (not modelled)."),
    },
    "Shadowed Mantle": {
        "type": "Magic Armour", "cost": 10, "armour": "Light Armor", "rules": [],
        "text": "Infantry only. A suit of light armour; its shooting protection has no duel effect.",
    },
    "Shield of the Warrior True": {
        "type": "Magic Armour", "cost": 30, "shield": True, "rules": [],
        "text": "A shield, with a 5+ Ward save in the Shooting phase only.",
    },
    "Spellshield": {
        "type": "Magic Armour", "cost": 25, "extremely_common": True,
        "shield": True, "rules": [],
        "text": "A shield, with a 5+ Ward save against some spells only.",
    },

    # Talismans.
    "Dawnstone": {
        "type": "Talisman", "cost": 35, "rules": [RerollArmourSaves1],
        "text": "The bearer may re-roll any Armour Save roll of a natural 1.",
    },
    "Luckstone": {
        "type": "Talisman", "cost": 15, "extremely_common": True, "rules": [],
        "text": "Re-roll a single failed Armour Save roll. " + _SINGLE_USE,
    },
    "Obsidian Lodestone": {
        "type": "Talisman", "cost": 20, "extremely_common": True, "rules": [],
        "text": "Magic Resistance (-1 per Lodestone, up to three). " + _NOT_IN_A_DUEL,
    },
    "Paymaster's Coin": {
        "type": "Talisman", "cost": 25, "extremely_common": True, "rules": [],
        "text": "Re-roll failed To Hit rolls for one Combat phase. " + _SINGLE_USE,
    },
    "Talisman of Authority": {
        "type": "Talisman", "cost": 30, "rules": [],
        "text": ("Enemies must pass a Leadership test to attack the bearer. "
                 + _SINGLE_USE),
    },
    "Talisman of Protection": {
        "type": "Talisman", "cost": 30, "rules": ["Ward5"],
        "text": "A 5+ Ward save against any wounds suffered.",
    },
    "The Warding Talisman": {
        "type": "Talisman", "cost": 15, "rules": ["Ward6"],
        "text": "A 6+ Ward save against any wounds suffered.",
    },

    # Enchanted items.
    "Enchanted Almanack": {"type": "Enchanted Item", "cost": 5, "rules": [],
                           "text": "Re-roll on the Chaos of War table. " + _NOT_IN_A_DUEL},
    "Flying Carpet": {"type": "Enchanted Item", "cost": 40, "rules": ["Fly (8)", "Swiftstride"],
                      "text": "Regular or heavy infantry only. Movement rules; the bearer cannot join a unit."},
    "Healing Potion": {"type": "Enchanted Item", "cost": 35, "extremely_common": True, "rules": [],
                       "text": "Recover D3 Wounds in the Command sub-phase. " + _SINGLE_USE},
    "Potion of Foolhardiness": {"type": "Enchanted Item", "cost": 5, "extremely_common": True, "rules": [],
                                "text": "Immune to Psychology for a turn. " + _SINGLE_USE},
    "Potion of Speed": {"type": "Enchanted Item", "cost": 10, "extremely_common": True, "rules": [],
                        "text": "+D3 Initiative for a turn. " + _SINGLE_USE},
    "Potion of Strength": {"type": "Enchanted Item", "cost": 25, "extremely_common": True, "rules": [],
                           "text": "+D3 Strength for a turn. " + _SINGLE_USE},
    "Potion of Toughness": {"type": "Enchanted Item", "cost": 20, "extremely_common": True, "rules": [],
                            "text": "+D3 Toughness for a turn. " + _SINGLE_USE},
    "Ruby Ring of Ruin": {"type": "Enchanted Item", "cost": 35, "rules": [],
                          "text": "Casts Fireball as a Bound spell. Inert until magic is simulated."},
    "The All-Seeing Eye of Numas": {"type": "Enchanted Item", "cost": 15, "rules": [],
                                    "text": "Shooting line of sight and cover. " + _NOT_IN_A_DUEL},
    "The Ranger's Glass": {"type": "Enchanted Item", "cost": 20, "rules": [],
                           "text": "+1 to the roll-off for the first turn. " + _NOT_IN_A_DUEL},
    "Wilderness Map": {"type": "Enchanted Item", "cost": 10, "extremely_common": True, "rules": [],
                       "text": "Re-roll on the Wilderness Terrain table. " + _NOT_IN_A_DUEL},
    "Wizarding Hat": {"type": "Enchanted Item", "cost": 45, "rules": ["Stupidity"],
                      "text": ("The wearer becomes a Level 1 Wizard with one random spell, "
                               "and is subject to Stupidity.")},

    # Arcane items: all inert until magic is simulated.
    "Arcane Familiar": {"type": "Arcane Item", "cost": 15, "rules": [],
                        "text": "Spells from two Lores of Magic. Inert until magic is simulated."},
    "Dispel Scroll": {"type": "Arcane Item", "cost": 20, "extremely_common": True, "rules": [],
                      "text": "An extra D6 on a Dispel roll. Inert until magic is simulated."},
    "Earthing Rod": {"type": "Arcane Item", "cost": 5, "rules": [],
                     "text": "Re-roll on the Miscast table. Inert until magic is simulated."},
    "Feedback Scroll": {"type": "Arcane Item", "cost": 60, "rules": [],
                        "text": "Wounds a casting Wizard. Inert until magic is simulated."},
    "Power Scroll": {"type": "Arcane Item", "cost": 20, "extremely_common": True, "rules": [],
                     "text": "An extra D6 on a Casting roll. Inert until magic is simulated."},
    "Scroll of Deathly Whispers": {"type": "Arcane Item", "cost": 10, "extremely_common": True, "rules": [],
                                   "text": "Casts Deathly Cabal. Inert until magic is simulated."},
    "Scroll of Fiery Convocation": {"type": "Arcane Item", "cost": 15, "extremely_common": True, "rules": [],
                                    "text": "Casts Fireball. Inert until magic is simulated."},
    "Scroll of Obfuscation": {"type": "Arcane Item", "cost": 5, "extremely_common": True, "rules": [],
                              "text": "Casts Confounding Convocation. Inert until magic is simulated."},
    "Scroll of Transmogrification": {"type": "Arcane Item", "cost": 50, "extremely_common": True, "rules": [],
                                     "text": "May turn a casting Wizard into a frog. Inert until magic is simulated."},
    "Wand of Jet": {"type": "Arcane Item", "cost": 45, "rules": [],
                    "text": "+1 to Casting and Dispel rolls. Inert until magic is simulated."},
    "Wyrdstone Shard": {"type": "Arcane Item", "cost": 10, "rules": [],
                        "text": "+1 to one Casting or Dispel roll. Inert until magic is simulated."},

    # Magic standards belong to units; a character duel never uses them.
    "Banner of Iron Resolve": {"type": "Magic Standard", "cost": 50, "rules": [],
                               "text": "The unit gains Stubborn. " + _NOT_IN_A_DUEL},
    "Banner of Renown": {"type": "Magic Standard", "cost": 15, "rules": [],
                         "text": "Single use: +1 combat result. " + _NOT_IN_A_DUEL},
    "Rampaging Banner": {"type": "Magic Standard", "cost": 30, "rules": [],
                         "text": "Re-roll the unit's Charge roll. " + _NOT_IN_A_DUEL},
    "Razor Standard": {"type": "Magic Standard", "cost": 40, "rules": [],
                       "text": "The unit gains Armour Bane (2). Unit-level; not applied to a character."},
    "The Banner of the Bold": {"type": "Magic Standard", "cost": 10, "rules": [],
                               "text": "The unit gains Veteran. " + _NOT_IN_A_DUEL},
    "The Blazing Banner": {"type": "Magic Standard", "cost": 25, "rules": [],
                           "text": "The unit gains Flaming Attacks. Unit-level; not applied to a character."},
    "War Banner": {"type": "Magic Standard", "cost": 25, "rules": [],
                   "text": "+1 combat result. " + _NOT_IN_A_DUEL},
}

# The Lore Familiar is already listed above for Kiknik; record it as common.
MagicItemDict["Lore Familiar"].update(cost=30, common=True)
for _name, _entry in COMMON_MAGIC_ITEMS.items():
    if _name in MagicItemDict:
        raise ValueError(f"Common magic item {_name!r} is already in MagicItemDict")
    MagicItemDict[_name] = dict(_entry, common=True)


def _normalise(name):
    """Item names appear with and without a leading 'The'."""
    if not isinstance(name, str):
        return ""
    text = name.strip().lower()
    return text[4:] if text.startswith("the ") else text


_LOOKUP = {_normalise(k): k for k in MagicItemDict}


def get_magic_item(name):
    """Return the MagicItemDict entry for an item name, or None."""
    key = _LOOKUP.get(_normalise(name))
    return MagicItemDict[key] if key else None


def unverified_items():
    """Item names whose rules could not be read off the site.

    Their entries carry no rules, so they contribute nothing in a duel. Listed
    here so the gap is visible and testable rather than silently absent.
    """
    return sorted(k for k, v in MagicItemDict.items() if not v.get("verified", True))


def apply_magic_items(character, items, verbose: bool = False) -> list[str]:
    """Add the special rules granted by `items` to `character`.

    Magic weapons are skipped - they reach the character as its Weapon, and
    their profile lives in MeleeWeaponDict. Magic armour that *is* a suit of
    armour or a shield ("armour" / "shield" on the entry) sets the character's
    Armor or Shield. Returns the names of any items that are not in
    MagicItemDict, so an unrecognised item is visible rather than silently
    doing nothing.
    """
    unknown = []
    for name in items or []:
        entry = get_magic_item(name)
        if entry is None:
            unknown.append(name)
            continue
        if entry.get("is_weapon"):
            continue
        if entry.get("armour"):
            character.Armor = entry["armour"]
        if entry.get("shield"):
            character.Shield = True
        for rule in entry.get("rules", []):
            if rule not in character.SpecialRules:
                character.SpecialRules.append(rule)
        if verbose and entry.get("rules"):
            print(f"{character.name} gains {name}: {', '.join(entry['rules'])}")
    return unknown
