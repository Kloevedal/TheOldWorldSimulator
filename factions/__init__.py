"""One module per faction.

Each faction module defines:

    FACTION          the key it is filed under in FactionProfiles
    ALIASES          other names that should resolve to it
    PROFILE_ALIASES  shorthand names for individual profiles
    CHARACTERS       character profiles
    UNITS            regular unit profiles
    PROFILES         CHARACTERS + UNITS, which is what the registry reads

To add a faction, drop a module in this package and list it in FACTION_MODULES
below. Nothing else needs to change.
"""

from __future__ import annotations

from . import (
    beastmen_brayherds,
    chaos_dwarfs,
    daemons_of_chaos,
    dark_elves,
    dwarfen_mountain_holds,
    empire_of_man,
    grand_cathay,
    high_elves,
    kingdom_of_bretonnia,
    lizardmen,
    ogre_kingdoms,
    orc_and_goblin_tribes,
    realms_of_men,
    regiments_of_renown,
    skaven,
    tomb_kings_of_khemri,
    vampire_counts,
    warriors_of_chaos,
    wood_elf_realms,
)

FACTION_MODULES = (
    high_elves,
    orc_and_goblin_tribes,
    warriors_of_chaos,
    empire_of_man,
    dwarfen_mountain_holds,
    beastmen_brayherds,
    chaos_dwarfs,
    daemons_of_chaos,
    dark_elves,
    grand_cathay,
    kingdom_of_bretonnia,
    lizardmen,
    ogre_kingdoms,
    realms_of_men,
    regiments_of_renown,
    skaven,
    tomb_kings_of_khemri,
    vampire_counts,
    wood_elf_realms,
)


def build_profiles():
    """{faction key: {profile name: entry}} across every registered faction."""
    profiles = {}
    for module in FACTION_MODULES:
        if module.FACTION in profiles:
            raise ValueError(f"Duplicate faction key: {module.FACTION}")
        profiles[module.FACTION] = module.PROFILES
    return profiles


def build_faction_aliases():
    """{alias: faction key}, including each faction's own name."""
    aliases = {}
    for module in FACTION_MODULES:
        aliases[module.FACTION] = module.FACTION
        for alias in module.ALIASES:
            if alias in aliases and aliases[alias] != module.FACTION:
                raise ValueError(
                    f"Alias {alias!r} claimed by both {aliases[alias]!r} "
                    f"and {module.FACTION!r}"
                )
            aliases[alias] = module.FACTION
    return aliases


def build_profile_aliases():
    """{faction key: {alias: profile name}}."""
    return {m.FACTION: dict(m.PROFILE_ALIASES) for m in FACTION_MODULES}
