"""Transcribe mount profiles from https://tow.whfb.app into mounts.py data.

    python3 tools/transcribe_mounts.py          # report the mapping
    python3 tools/transcribe_mounts.py -w       # write mounts_data.generated

The generated file holds the body of the `Mounts` dict in mounts.py; paste it
over the generated part there, keeping the hand entries at the end.

Each character's mounts are resolved through the links on that character's
own unit page, so a name like "Warhorse", which means a different mount in
Bretonnia than in the Realms of Men, reaches the right profile. Mounts are
keyed by the site's own name with any "(Mount)" suffix removed.
"""

from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

import tow_site as site  # noqa: E402

_URL = re.compile(r"tow\.whfb\.app/unit/([a-z0-9-]+)")


def canonical(name):
    return re.sub(r"\s*\(Mount\)$", "", name).strip()


def _fold(name):
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def character_slugs(module):
    """{profile name: unit slug}, read from each profile's source comment."""
    source = open(module.__file__, encoding="utf-8").read()
    slugs = {}
    for name in module.CHARACTERS:
        start = source.find(f'    "{name}": {{')
        if start < 0:
            start = source.find(f"    {name!r}: {{")
        match = _URL.search(source, start) if start >= 0 else None
        if match:
            slugs[name] = match.group(1)
    return slugs


def option_points(options_text, shown):
    """Points for a mount option line, or None.

    The name must start the option ("- Warhorse (+12 points)", "mounted on a
    Warhorse (+12 points)"), so "Warhorse" does not match "Bretonnian Warhorse".
    """
    pattern = re.compile(
        r"(?:^\s*-\s*(?:0-\d+\s+)?|\b(?:on|an?)\s+)" + re.escape(shown)
        + r"\s*(?:\((?!\+)[^)]*\)\s*)*\(\+(\d+) points?\)",
        re.IGNORECASE,
    )
    for line in options_text.splitlines():
        match = pattern.search(line)
        if match:
            return int(match.group(1))
    return None


# Mounts that exist only as a row on their rider's page. mounts.py keeps these
# as hand entries; the resolver leaves them alone.
RIDER_PAGE_MOUNTS = {"Sun Dragon", "Chompa", "Chaos Warhound"}


def army_slug(module):
    match = re.search(r"tow\.whfb\.app/army/([a-z0-9-]+)", module.__doc__ or "")
    return match.group(1) if match else None


def find_in_army(army, name):
    """Slug of the unit in `army` whose name matches `name`, Mounts first."""
    wanted = _fold(name)
    ranked = sorted(site.army_units(army), key=lambda u: u[0] != "Mount")
    for _section, slug, unit_name in ranked:
        folded = _fold(canonical(unit_name))
        if folded == wanted or folded.startswith(wanted + " "):
            return slug
    return None


def resolve():
    """(mapping, problems).

    mapping: {(faction, profile, listed mount name): (slug, canonical, points)}
    """
    from factions import FACTION_MODULES

    mapping, problems = {}, []
    for module in FACTION_MODULES:
        slugs = character_slugs(module)
        for name, entry in module.CHARACTERS.items():
            listed = entry["mount_options"]["mounts"]
            if not listed:
                continue
            if name not in slugs:
                problems.append(f"{module.FACTION}/{name}: no source URL")
                continue
            unit = site.unit(slugs[name])
            links = {}
            for shown, slug, kind in unit["option_links"]:
                if kind != "armyListEntry":
                    continue
                target = canonical(site.unit(slug)["name"])
                if not set(_fold(re.sub(r"\s*\(.*$", "", shown)).split()) <= set(_fold(target).split()):
                    # The link text and its target disagree - a site data
                    # error, such as "Cold One" linking to the Terradon page.
                    fixed = find_in_army(army_slug(module), shown)
                    problems.append(
                        f"{module.FACTION}/{name}: site links {shown!r} to "
                        f"{slug!r}; using {fixed!r}"
                    )
                    if fixed is None:
                        continue
                    slug = fixed
                    target = canonical(site.unit(slug)["name"])
                for key in (shown, target, canonical(shown), re.sub(r"\s*\(.*\)$", "", target)):
                    links.setdefault(_fold(key), (slug, target, shown))
            for mount in listed:
                if mount in RIDER_PAGE_MOUNTS:
                    continue
                hit = links.get(_fold(mount))
                if hit is None:
                    fixed = find_in_army(army_slug(module), mount)
                    problems.append(
                        f"{module.FACTION}/{name}: mount {mount!r} not linked on "
                        f"its page; found {fixed!r} in the army list"
                    )
                    if fixed is None:
                        continue
                    hit = (fixed, canonical(site.unit(fixed)["name"]), mount)
                slug, target, shown = hit
                mapping[(module.FACTION, name, mount)] = (
                    slug, target, option_points(unit["options"], shown),
                )
    return mapping, problems


def _stat(value):
    """'-' -> None, '4' -> 4, '(+1)' -> '+1' (a bonus to the rider)."""
    value = str(value).strip()
    if value.isdigit():
        return int(value)
    bonus = re.fullmatch(r"\(?([+-]\d+)\)?", value)
    if bonus:
        return bonus.group(1)
    return None if value in ("-", "", "N/A") else value


_STATS = (("Movement", "M"), ("WeaponSkill", "WS"), ("BallisticSkill", "BS"),
          ("Strength", "S"), ("Toughness", "T"), ("Initiative", "I"),
          ("Wounds", "W"), ("Attacks", "A"), ("Leadership", "Ld"))


def mount_entries(mapping):
    """{canonical name: entry} for every resolved mount."""
    by_name = {}
    for (faction, rider, _listed), (slug, name, points) in sorted(mapping.items()):
        entry = by_name.get(name)
        if entry is None:
            unit = site.unit(slug)
            rows = unit["profiles"]
            main = next((r for r in rows if canonical(r["Name"]) == name), rows[0])
            troop = [t for t in unit["troop_type"] if t not in ("Character", "Named Character")]
            entry = {"url": slug, "points": points,
                     "troop_type": troop[0].replace(" ", "") if troop else None}
            for key, col in _STATS:
                entry[key] = _stat(main[col])
            entry["SpecialRules"] = unit["special_rules"]
            entry["equipment"] = site.text(unit["raw"].get("equipment")).strip()
            if len(rows) > 1:
                entry["profiles"] = [
                    dict({"Name": r["Name"]}, **{k: _stat(r[c]) for k, c in _STATS})
                    for r in rows
                ]
            entry["_riders"] = {}
            by_name[name] = entry
        entry["_riders"][f"{faction}/{rider}"] = points
    for entry in by_name.values():
        riders = entry.pop("_riders")
        costs = {p for p in riders.values() if p is not None}
        if len(costs) > 1:
            entry["points"] = None
            entry["points_by_rider"] = dict(sorted(riders.items()))
        elif costs:
            entry["points"] = costs.pop()
    return dict(sorted(by_name.items()))


def render(entries):
    lines = []
    for name, e in entries.items():
        lines.append(f"    {name!r}: {{")
        for key, value in e.items():
            if key == "profiles":
                lines.append('        "profiles": [')
                for row in value:
                    lines.append(f"            {row!r},")
                lines.append("        ],")
            elif key == "points_by_rider":
                lines.append('        "points_by_rider": {')
                for rider, pts in value.items():
                    lines.append(f"            {rider!r}: {pts!r},")
                lines.append("        },")
            else:
                lines.append(f"        {key!r}: {value!r},")
        lines.append("    },")
    return "\n".join(lines)


if __name__ == "__main__":
    mapping, problems = resolve()
    renames = {k: v for k, v in mapping.items() if k[2] != v[1]}
    for (f, n, m), (slug, target, pts) in sorted(renames.items()):
        print(f"RENAME {f}/{n}: {m!r} -> {target!r} ({slug})")
    for p in problems:
        print("PROBLEM", p)
    if "-w" in sys.argv:
        out = os.path.join(ROOT, "mounts_data.generated")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(render(mount_entries(mapping)) + "\n")
        print("wrote", out)
    print(len(mapping), "links;", len({v[0] for v in mapping.values()}), "distinct mounts")
