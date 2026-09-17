"""Faction data: statlines, points, special rules and legal equipment.

The profiles themselves live one module per faction in the `factions` package;
this module assembles them and provides the name-resolution helpers. Adding a
faction means adding a module there, not editing this file.
"""

from __future__ import annotations

from factions import (
    build_faction_aliases,
    build_profile_aliases,
    build_profiles,
)

# Race synonyms. Races cut across factions (a Goblin appears in an Orc army),
# so this stays central rather than being split per faction.
RACE_NAMES = {
    "HIGH_ELVES": ["High Elf", "High Elves", "Asur"],
    "DARK_ELVES": ["Dark Elf", "Dark Elves", "Druchii"],
    "ORCS": ["Orc", "Orcs", "Greenskins", "Orks", "Ork"],
    "GOBLINS": ["Goblin", "Goblins", "Grot", "Grots", "Hobgoblin", "Snotling", "Squig"],
    "NIGHT_GOBLINS": ["Night Goblin", "Night Goblins"],
    "TROLLS": ["Troll", "Trolls"],
    "EMPIRE": ["Empire", "Human", "Humans", "Men"],
    "DWARVES": ["Dwarf", "Dwarfs", "Dwarves", "Dawi"],
    "LIZARDMEN": ["Lizardman", "Lizardmen", "Saurus", "Skink", "Slann"],
    "BRETONNIA": ["Bretonnia", "Bretonnian", "French"],
    "CHAOS": ["Chaos", "Chaos Warrior", "Chaos Warriors", "Chaos Marauder",
              "Marauder", "Chaos Dragon"],
    "SKAVEN": ["Skaven", "Ratmen"],
    "VAMPIRE_COUNTS": ["Vampire Counts", "Vampires", "Vampire", "Necromancer",
                       "Wight", "Spirit", "Undead", "Ghoul"],
    "OGRES": ["Ogre", "Ogres", "Gnoblar"],
    "GIANTS": ["Giant", "Giants"],
    "WOOD_ELVES": ["Wood Elf", "Wood Elves", "Asrai", "Forest Spirit"],
    "TOMB_KINGS": ["Tomb Kings", "Tomb King", "Nehekhara"],
    "CATHAY": ["Cathay", "Cathayan"],
    "CHAOS_DWARVES": ["Chaos Dwarf", "Chaos Dwarves", "Dawi Zharr",
                      "Bull Centaur"],
    "DAEMONS": ["Daemon", "Daemons", "Chaos Daemons"],
    "BEASTMEN": ["Beastman", "Beastmen", "Beastmen of Chaos", "Gor", "Centigor",
                 "Minotaur", "Farm Animals"],
    "KISLEV": ["Kislev", "Kislevites"],
}


FactionProfiles = build_profiles()

# Alternative names for the keys of FactionProfiles, contributed by each faction
# module. Matching is case-insensitive and ignores '&'/'and' and punctuation, so
# "Orc and Goblin Tribes" and "orc & goblin tribes" both resolve.
FACTION_ALIASES = build_faction_aliases()

# Shorthand names for profiles, per faction.
PROFILE_ALIASES = build_profile_aliases()


def _normalise_faction(name):
    """Lowercase, drop punctuation, and treat '&' as 'and' for alias matching."""
    if not isinstance(name, str):
        return ""
    text = name.lower().replace("&", " and ")
    text = "".join(ch if ch.isalnum() else " " for ch in text)
    return " ".join(text.split())


_FACTION_LOOKUP = {_normalise_faction(k): v for k, v in FACTION_ALIASES.items()}


def resolve_faction(name):
    """Return the FactionProfiles key for a faction name or alias, else None."""
    if name in FactionProfiles:
        return name
    return _FACTION_LOOKUP.get(_normalise_faction(name))


def resolve_profile(faction, name):
    """Return the profile key within `faction` for a name, alias or casing.

    `faction` may itself be an alias ("High Elves" for "High Elf Realms").
    """
    faction = resolve_faction(faction) or faction
    profiles = FactionProfiles.get(faction, {})
    if name in profiles:
        return name
    if not isinstance(name, str):
        return None
    aliases = PROFILE_ALIASES.get(faction, {})
    folded = {key.lower(): key for key in profiles}
    folded.update({alias.lower(): key for alias, key in aliases.items()})
    return folded.get(name.strip().lower())
