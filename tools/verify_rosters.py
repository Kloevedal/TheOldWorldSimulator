"""Compare every faction module against https://tow.whfb.app.

    python3 tools/verify_rosters.py              # all factions
    python3 tools/verify_rosters.py skaven orcs  # config keys from transcribe_faction

Reports, per faction:

* profiles on the site's army page that the module does not have, and the
  reverse;
* statlines (M WS BS S T I W A Ld) that differ from the row the model fights
  with - using the same row choice as transcribe_faction, and honouring its
  documented per-profile overrides;
* points that differ.

Uses the page cache in .tow_cache/, so it runs offline once pages are cached.
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

STATS = ("Movement", "WeaponSkill", "BallisticSkill", "Strength", "Toughness",
         "Initiative", "Wounds", "Attacks", "Leadership")

# Site sections that hold characters rather than units.
CHARACTER_SECTIONS = {"character", "named character"}
# Mounts live in mounts.py, not in a faction module.
MOUNT_SECTIONS = {"mount"}


# Site name -> the key the module files it under, where they differ.
SITE_NAMES = {
    "Daemon Prince (Warriors of Chaos)": "Daemon Prince",
    "Daemon Prince (Daemons of Chaos)": "Daemon Prince",
    "Dark Elf Dreadlord": "Dreadlord",
    "Dark Elf Master": "Master",
    "General Hans von Löwenhacke": "General Hans von Loewenhacke",
}

# Site entries that are deliberately not in any module, and why.
NOT_A_FIGHTER = {
    "Herdstone": "a scenery piece, not a model that fights",
    "Wood Elf Beast Pack": "a Beast Keeper plus beasts; each is its own unit entry",
    "Fanatic": "moves and hits only through its ball and chain; it does not fight in combat",
}

# Profiles filed under a different kind than the site's army-page section, on
# purpose. The site lists the Handler under Cavalry, but its own rules text
# calls it "a special type of character" that joins a unit of Warhounds.
KIND_EXCEPTIONS = {"Chaos Warhound Handler": "character"}


def _fold(name):
    return tf.mount_names._fold(name)


def _overrides(faction):
    """Per-profile overrides from every transcribe_faction config for a faction."""
    merged = {}
    for cfg in tf.FACTIONS.values():
        if cfg["faction"] == faction:
            merged.update(cfg.get("overrides", {}))
    return merged


def expected_stats(slug, is_unit, overrides):
    unit = site.unit(slug)
    if is_unit:
        main, _champion, body, _others = tf.unit_rows(unit)
        stats = tf._stats(main, body)
    else:
        main, _others = tf.profile_for(unit)
        stats = tf._stats(main)
    stats.update(overrides.get("base_profile", {}))
    return unit, stats


def verify(key):
    cfg = tf.FACTIONS[key]
    if not cfg.get("module"):
        return []
    module = importlib.import_module(f"factions.{cfg['module']}")
    ours = {"character": dict(module.CHARACTERS), "unit": dict(getattr(module, "UNITS", {}))}
    folded = {kind: {_fold(n): n for n in names} for kind, names in ours.items()}
    problems = []
    seen = {"character": set(), "unit": set()}
    overrides_by_name = _overrides(cfg["faction"])

    from mounts import Mounts

    mount_names = {_fold(n) for n in Mounts}
    for section, slug, name in site.army_units(cfg["army"]):
        section_key = section.strip().lower()
        bare = re.sub(r"\s*\(Mount\)$", "", name)
        if section_key in MOUNT_SECTIONS:
            if _fold(bare) not in mount_names:
                problems.append(f"MISSING mount: {bare} - unit/{slug}")
            continue
        if bare in NOT_A_FIGHTER:
            continue
        kind = "character" if section_key in CHARACTER_SECTIONS else "unit"
        kind = KIND_EXCEPTIONS.get(bare, kind)
        mine = folded[kind].get(_fold(SITE_NAMES.get(name, name)))
        if mine is None and _fold(bare) in mount_names:
            continue  # a monster or chariot taken only as a character's mount
        if mine is None:
            other = "unit" if kind == "character" else "character"
            if _fold(name) in folded[other]:
                problems.append(f"{name}: filed as a {other}, the site lists it under {section}")
                seen[other].add(folded[other][_fold(name)])
            else:
                problems.append(f"MISSING {kind}: {name} ({section}) - unit/{slug}")
            continue
        seen[kind].add(mine)
        entry = ours[kind][mine]
        try:
            unit, stats = expected_stats(slug, kind == "unit", overrides_by_name.get(mine, {}))
        except (site.PageNotFound, KeyError, IndexError) as exc:
            problems.append(f"{mine}: could not read unit/{slug} ({exc})")
            continue
        base = entry["base_profile"]
        diffs = [
            f"{stat} {base.get(stat)!r} != site {stats[stat]!r}"
            for stat in STATS
            if base.get(stat) != stats[stat]
        ]
        if diffs:
            problems.append(f"STATLINE {mine}: " + "; ".join(diffs))
        cost = tf._int(unit["cost"]) if unit["cost"] is not None else None
        if cost is not None and entry.get("points") != cost:
            problems.append(f"POINTS {mine}: {entry.get('points')!r} != site {cost}")

    for kind in ours:
        for name in sorted(set(ours[kind]) - seen[kind]):
            problems.append(f"EXTRA {kind}: {name} is not on the site's army page")
    return problems


def main(argv):
    keys = argv or [k for k, c in tf.FACTIONS.items() if c.get("module")]
    total = 0
    for key in keys:
        problems = verify(key)
        total += len(problems)
        print(f"== {key}: {len(problems)} problem(s)")
        for line in problems:
            print("   " + line)
    print(f"\n{total} problem(s) in total")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
