"""Generate item_allowances.py: what each character may buy, from its unit page.

    python3 tools/transcribe_allowances.py -w

A character's options say how many points it may spend on each kind of item
("may purchase magic items up to a total of 100 points", "Daemonic Gifts up to
a total of 50 points") and which abilities it may pick without a points cap
("may have an Elven Honour", "may take a Knightly Virtue"). The result is
{faction: {profile: {budget: points or None}}}, where None means "may pick
from this group" with no points limit of its own.

Named characters are not listed: their wargear is fixed.

Units get UNIT_OPTIONS: {faction: {profile: {"command": [roles],
"champion": name, "champion_items": {budget: points},
"standard_items": {budget: points}}}} - which of a champion, standard bearer
and musician the unit may include, what its champion may buy ("A Sergeant
may purchase magic items up to a total of 25 points") and what its standard
bearer may carry ("Purchase a magic standard worth up to 50 points",
"Purchase Standard runes up to a total of 50 points").
"""

from __future__ import annotations

import importlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT]

import tow_site as site  # noqa: E402
import transcribe_faction as tf  # noqa: E402
import verify_rosters as vr  # noqa: E402

OUT = os.path.join(ROOT, "item_allowances.py")

# Allowance wording -> budget name.
BUDGETS = [
    (r"weapon, armour and talismanic runes|weapon runes|armour runes|talismanic runes"
     r"|standard runes|engineering runes|\bruness?\b", "Runes"),
    (r"daemonic gifts", "Daemonic Gifts"),
    (r"gifts of chaos", "Gifts of Chaos"),
    (r"chaos mutations", "Chaos Mutations"),
    (r"forest spites", "Forest Spites"),
    (r"vampiric powers", "Vampiric Powers"),
    (r"magic items|magic standard", "Magic Items"),
]

# Abilities picked without a points allowance, by the wording that offers them.
FREE_PICKS = [
    (r"elven honour", "Elven Honours"),
    (r"knightly virtue", "Knightly Virtues"),
    (r"noble kindred|\bkindred\b", "Noble Kindreds"),
    (r"chaotic trait", "Chaotic Traits"),
    (r"big name", "Big Names"),
    (r"runic tattoo", "Runic Tattoos"),
    (r"discipline", "Disciplines of the Old Ones"),
    (r"infamous origin", "Infamous Origins"),
    (r"knightly order", "Knightly Orders"),
]

# Ability groups an army offers to its characters in general rather than on
# each character's page. The items' own text says which characters qualify.
ARMY_PICKS = {
    "Wood Elf Realms": ["Noble Kindreds", "Alter Kindreds"],
    "Empire of Man": ["Knightly Orders"],
    "Realms of Men": ["Infamous Origins"],
}

_TOTAL = re.compile(r"([^\n.]*?) up to a total of (\d+) points?", re.I)


def allowances(options):
    found = {}
    for what, points in _TOTAL.findall(options):
        for pattern, budget in BUDGETS:
            if re.search(pattern, what, re.I):
                found[budget] = found.get(budget, 0) + int(points)
                break
    for pattern, group in FREE_PICKS:
        if re.search(pattern, options, re.I):
            found.setdefault(group, None)
    return found


_CHAMPION = re.compile(r"upgrade one model to an? (.+?) \(champion\)", re.I)
_STANDARD = re.compile(r"(?:purchase|take) an? magic standard worth up to (\d+) points?", re.I)
_STANDARD_RUNES = re.compile(r"standard runes up to a total of (\d+) points?", re.I)


def unit_options(options):
    """What a unit's options page offers its command group."""
    found = {"command": []}
    champion = _CHAMPION.search(options)
    if champion:
        found["command"].append("champion")
        found["champion"] = champion.group(1)
    if re.search(r"upgrade one model to an? standard bearer", options, re.I):
        found["command"].append("standard")
    if re.search(r"upgrade one model to an? musician", options, re.I):
        found["command"].append("musician")
    standard = {}
    if _STANDARD.search(options):
        standard["Magic Items"] = int(_STANDARD.search(options).group(1))
    if _STANDARD_RUNES.search(options):
        standard["Runes"] = int(_STANDARD_RUNES.search(options).group(1))
    if standard:
        found["standard_items"] = standard
    if champion:
        # "A Sergeant may purchase ...", or "A Shartak may:" / "An Elder may
        # purchase:" followed by indented lines.
        name = re.escape(champion.group(1))
        block = re.search(rf"^-\s*An? {name} may(.*?)(?=^- |\Z)", options, re.I | re.M | re.S)
        if block:
            items = {}
            for what, points in _TOTAL.findall(block.group(0)):
                for pattern, budget in BUDGETS:
                    if re.search(pattern, what, re.I):
                        items[budget] = items.get(budget, 0) + int(points)
                        break
            if items:
                found["champion_items"] = items
    return found if (found["command"] or len(found) > 1) else None


def build_units():
    result = {}
    for key, cfg in tf.FACTIONS.items():
        if not cfg.get("module"):
            continue
        module = importlib.import_module(f"factions.{cfg['module']}")
        folded = {vr._fold(k): k for k in getattr(module, "UNITS", {})}
        for section, slug, name in site.army_units(cfg["army"]):
            mine = folded.get(vr._fold(vr.SITE_NAMES.get(name, name)))
            if not mine:
                continue
            found = unit_options(site.unit(slug)["options"])
            if found:
                result.setdefault(cfg["faction"], {})[mine] = found
    return result


def build():
    result = {}
    for key, cfg in tf.FACTIONS.items():
        if not cfg.get("module"):
            continue
        module = importlib.import_module(f"factions.{cfg['module']}")
        folded = {vr._fold(k): k for k in module.CHARACTERS}
        for section, slug, name in site.army_units(cfg["army"]):
            if section.strip().lower() != "character":
                continue  # named characters have fixed wargear
            mine = folded.get(vr._fold(vr.SITE_NAMES.get(name, name)))
            if not mine:
                continue
            found = allowances(site.unit(slug)["options"])
            for group in ARMY_PICKS.get(cfg["faction"], []):
                found.setdefault(group, None)
            if found:
                result.setdefault(cfg["faction"], {})[mine] = found
    return result


def render_units(result):
    lines = ["", "# What each unit's command group may be and buy (see the module docstring).",
             "UNIT_OPTIONS = {"]
    for faction in sorted(result):
        lines.append(f"    {faction!r}: {{")
        for profile in sorted(result[faction]):
            lines.append(f"        {profile!r}: {result[faction][profile]!r},")
        lines.append("    },")
    lines.append("}")
    return "\n".join(lines) + "\n"


def render(result):
    lines = ['"""What each character may buy: {faction: {profile: {budget: points or None}}}.',
             "",
             "GENERATED by tools/transcribe_allowances.py - do not edit by hand.",
             "None means the character may pick from that group with no points cap.",
             '"""', "", "ALLOWANCES = {"]
    for faction in sorted(result):
        lines.append(f"    {faction!r}: {{")
        for profile in sorted(result[faction]):
            lines.append(f"        {profile!r}: {result[faction][profile]!r},")
        lines.append("    },")
    lines.append("}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    data = build()
    total = sum(len(v) for v in data.values())
    print(total, "characters with allowances")
    units = build_units()
    print(sum(len(v) for v in units.values()), "units with command options")
    if "-w" in sys.argv:
        with open(OUT, "w", encoding="utf-8") as fh:
            fh.write(render(data) + render_units(units))
        print("wrote", OUT)
    else:
        for faction, profiles in data.items():
            for profile, found in profiles.items():
                print(f"{faction:25} {profile:35} {found}")
