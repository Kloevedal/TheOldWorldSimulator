"""Generate option_costs.py: what each option costs, from every unit page.

    python3 tools/transcribe_costs.py          # report unmatched option lines
    python3 tools/transcribe_costs.py -w       # write option_costs.py

A profile's options list prices such as "Great weapon (+4 points)", "Heavy
armour (+3 points)", "Griffon (+130 points)", "Mark of Khorne (+10 points)" or,
for units, "Halberds (+1 point per model)". Each priced line is matched to the
name the simulator uses for that weapon, armour, mount or rule:

    {faction: {profile: {"weapons": {name: cost}, "armour": {...},
                         "shield": cost, "mounts": {...}, "rules": {...},
                         "per_model": bool}}}

`per_model` is set for units whose weapon and armour upgrades are priced per
model. Lines that match nothing (bows, command groups, wizard levels) are left
out and listed by the report.
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

OUT = os.path.join(ROOT, "option_costs.py")

_PRICED = re.compile(r"^(.*?)\s*\((?:\+(\d+) points?(?: per (model|unit))?|Free)\)\s*$", re.I)
_LEAD = re.compile(r"^(?:[-\s]*)(?:a character with .*? may be mounted on (?:a |an )?|"
                   r"(?:may )?take (?:a |an )?|the entire unit may take |"
                   r"(?:may )?replace .*? with (?:a |an )?|may be mounted on (?:a |an )?|"
                   r"(?:may )?have (?:the )?|may be (?:a |an )?)", re.I)

_ARMOUR = {"light armour": "Light Armor", "heavy armour": "Heavy Armor",
           "full plate armour": "Full Plate Armor", "barding": None}
_SPECIAL_WEAPONS = {"additional hand weapon": "Two Hand Weapons",
                    "additional hand weapons": "Two Hand Weapons"}


def _fold(text):
    return set(re.sub(r"[^a-z0-9 ]+", " ", text.lower()).split()) - {"the", "a", "an", "of", "special", "rule"}


def _label(line):
    text = _LEAD.sub("", line.strip()).strip()
    text = re.sub(r"\s*\((?:if appropriately mounted|0-1[^)]*|[^)]*only)\)?", "", text, flags=re.I)
    return text.strip(" :-")


def classify(label, entry):
    """(kind, simulator name) for an option label, or None."""
    import transcribe_items as ti

    low = label.lower()
    base = entry["base_profile"]
    if low in ("shield", "shields"):
        return "shield", "Shield"
    singular = ti._singular(low)
    if low in _ARMOUR or singular in _ARMOUR:
        name = _ARMOUR.get(low) or _ARMOUR.get(singular)
        return ("armour", name) if name else None
    if low in _SPECIAL_WEAPONS:
        return "weapons", _SPECIAL_WEAPONS[low]
    found = ti._equipment_name(low)
    if found and found[0] == "weapon":
        return "weapons", found[1]
    offered = list(base.get("OptionalRules") or []) + list(base.get("MarksOfChaos") or [])
    words = _fold(label)
    for rule in offered:
        if words and _fold(rule) == words:
            return "rules", rule
    for mount in entry.get("mount_options", {}).get("mounts", []):
        mount_words = _fold(re.sub(r"\s*\(.*\)$", "", mount))
        if words and (words <= mount_words or mount_words <= words):
            return "mounts", mount
    return None


def costs_for(slug, entry):
    result = {"weapons": {}, "armour": {}, "mounts": {}, "rules": {}}
    unmatched = []
    per_model = False
    for line in site.unit(slug)["options"].splitlines():
        match = _PRICED.match(line.strip(" -"))
        if not match:
            continue
        label = _label(match.group(1))
        cost = int(match.group(2) or 0)
        if match.group(3) == "model":
            per_model = True
        found = classify(label, entry)
        if not found:
            unmatched.append(label)
            continue
        kind, name = found
        if kind == "shield":
            result["shield"] = cost
        else:
            result[kind].setdefault(name, cost)
    result = {k: v for k, v in result.items() if v or k == "shield"}
    if per_model:
        result["per_model"] = True
    return result, unmatched


def build():
    table, report = {}, []
    for key, cfg in tf.FACTIONS.items():
        if not cfg.get("module"):
            continue
        module = importlib.import_module(f"factions.{cfg['module']}")
        profiles = {**module.CHARACTERS, **getattr(module, "UNITS", {})}
        folded = {vr._fold(k): k for k in profiles}
        for section, slug, name in site.army_units(cfg["army"]):
            mine = folded.get(vr._fold(vr.SITE_NAMES.get(name, name)))
            if not mine:
                continue
            costs, unmatched = costs_for(slug, profiles[mine])
            if costs:
                table.setdefault(cfg["faction"], {})[mine] = costs
            report += [f"{cfg['faction']}/{mine}: {label}" for label in unmatched]
    return table, report


def render(table):
    lines = ['"""Option prices per profile, from tow.whfb.app.', "",
             "GENERATED by tools/transcribe_costs.py - do not edit by hand.", '"""', "",
             "OPTION_COSTS = {"]
    for faction in sorted(table):
        lines.append(f"    {faction!r}: {{")
        for profile in sorted(table[faction]):
            lines.append(f"        {profile!r}: {table[faction][profile]!r},")
        lines.append("    },")
    lines.append("}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    table, report = build()
    print(sum(len(v) for v in table.values()), "profiles priced;", len(report), "unmatched option lines")
    if "-v" in sys.argv:
        for line in report:
            print("  ", line)
    if "-w" in sys.argv:
        with open(OUT, "w", encoding="utf-8") as fh:
            fh.write(render(table))
        print("wrote", OUT)
