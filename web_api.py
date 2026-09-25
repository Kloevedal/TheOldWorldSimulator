"""The web front end's view of the simulator.

The website (web/) runs this module in the visitor's browser with Pyodide.
Its page calls `call(name, args_json)` and gets JSON back, so the JavaScript
side never touches Python objects. Everything here is a thin layer over
app_model, which the desktop app uses too.

Anything that arrives from the page (including a fighter decoded from a
share link) goes through `clean_spec` first: unknown fields are dropped,
strings and lists are bounded, and FighterSpec.build then rejects an illegal
loadout.
"""

from __future__ import annotations

import json
import re

from app_model import (
    CHARACTER,
    DEFAULT_NARRATION_ROUNDS,
    DEFAULT_RUNS,
    KINDS,
    NO_ARMOUR_LABEL,
    TO_THE_DEATH,
    UNIT,
    UNIT_COMBAT_NOTE,
    FighterSpec,
    armour_choices,
    choice_label,
    compare_stats,
    faction_names,
    gear_options,
    item_rule_terms,
    narrate_duel,
    option_price,
    points_breakdown,
    profile_names,
    purchasable_items,
    purchase_problem,
    rounds_text,
    run_statistics,
    spent,
    weapon_choices,
    weapon_summary,
)
from faction_profiles import resolve_faction
from magic_items import get_magic_item

DEFAULTS = {
    CHARACTER: [("High Elf Realms", "Prince"), ("Orc & Goblin Tribes", "Black Orc Warboss")],
    UNIT: [("Empire of Man", "State Troops"), ("Orc & Goblin Tribes", "Orc Mob")],
}
STATUS_NOTES = {"partial": "partly simulated", "not modelled": "not simulated",
                "no duel effect": "no effect in a duel"}
RULES_SITE = "https://tow.whfb.app"
MAX_NAME = 40
MAX_LIST = 30
MAX_RUNS = 20000
MAX_ROUNDS = 50
_SLUG = re.compile(r"^[a-z0-9-]{1,80}$")


def _text(value, limit=80):
    return value.strip()[:limit] if isinstance(value, str) else ""


def _int(value, low, high, default):
    try:
        number = int(value)
    except (TypeError, ValueError):
        return default
    return max(low, min(high, number))


def clean_spec(data):
    """A FighterSpec from untrusted data. Raises ValueError if it names no
    known army and model."""
    if not isinstance(data, dict):
        raise ValueError("Not a fighter")
    kind = data.get("kind") if data.get("kind") in KINDS else CHARACTER
    faction = resolve_faction(_text(data.get("faction")))
    profile = _text(data.get("profile"))
    if not faction or profile not in profile_names(faction, kind):
        raise ValueError("Unknown army or model")
    lists = {}
    for key in ("optional_rules", "magic_items"):
        values = data.get(key) if isinstance(data.get(key), list) else []
        lists[key] = [_text(v) for v in values[:MAX_LIST] if _text(v)]
    return FighterSpec(
        name=_text(data.get("name"), MAX_NAME) or profile,
        faction=faction,
        profile=profile,
        weapon=_text(data.get("weapon")) or "Hand Weapon",
        armour=_text(data.get("armour")) or NO_ARMOUR_LABEL,
        shield=data.get("shield") is True,
        optional_rules=lists["optional_rules"],
        magic_items=lists["magic_items"],
        mount=_text(data.get("mount")) or None,
        kind=kind,
        models=_int(data.get("models"), 1, 200, 20) if kind == UNIT else 1,
        frontage=_int(data.get("frontage"), 1, 40, 5) if kind == UNIT else 1,
    )


# -- what the page asks for ----------------------------------------------------

def catalog():
    """Armies and models for both modes, plus the starting picks."""
    kinds = {}
    for kind in KINDS:
        kinds[kind] = {f: profile_names(f, kind) for f in faction_names(kind)}
    return {"kinds": kinds, "defaults": DEFAULTS, "unit_note": UNIT_COMBAT_NOTE,
            "default_runs": DEFAULT_RUNS, "default_rounds": DEFAULT_NARRATION_ROUNDS}


def options(faction, profile, items=()):
    """What a card offers for a model: pickers with labels, extras, the shop."""
    opts = gear_options(faction, profile)
    label = lambda kind: (lambda name: {"name": name, "label": choice_label(faction, profile, kind, name)})
    rule_price = lambda rule: option_price(faction, profile, "rules", rule)
    return {
        "weapons": [label("weapons")(w) for w in weapon_choices(faction, profile, items)],
        "two_handed": opts["two_handed"],
        "armour": [label("armour")(a) for a in armour_choices(faction, profile, items)],
        "mounts": [label("mounts")(m) for m in opts["mounts"]],
        "fixed_mount": opts["fixed_mount"],
        "shield": opts["shield"],
        "shield_cost": option_price(faction, profile, "shield", "Shield"),
        "optional_rules": [{"name": r, "cost": rule_price(r)} for r in opts["optional_rules"]],
        "exclusive": [{"group": g, "default": d,
                       "choices": [{"name": c, "cost": rule_price(c)} for c in choices]}
                      for g, choices, d in opts["exclusive"]],
        "allowance": opts["allowance"],
        "defaults": opts["defaults"],
        "unit": opts["unit"],
    }


def shop(faction, profile):
    """Items the model may buy, without the rules text: the short profile,
    a status note and a link to the item's page on tow.whfb.app."""
    found = []
    for item in purchasable_items(faction, profile):
        slug = (get_magic_item(item["name"]) or {}).get("slug") or ""
        search = " ".join([item["name"], item["type"] or "", item["summary"],
                           *item_rule_terms(item["name"])]).lower()
        found.append({
            "name": item["name"], "cost": item["cost"], "budget": item["budget"],
            "pane": item["pane"], "common": item["common"],
            "note": STATUS_NOTES.get(item["status"], ""), "summary": item["summary"],
            "link": f"{RULES_SITE}/magic-item/{slug}" if _SLUG.match(slug) else "",
            "search": search,
        })
    return found


def check_items(faction, profile, items):
    """Why these items may not be bought together (or "" if they may),
    and the points spent per budget."""
    names = [_text(i) for i in items[:MAX_LIST]]
    return {"problem": purchase_problem(faction, profile, names) or "", "spent": spent(names)}


def describe(spec):
    """Everything a fighter card shows."""
    spec = clean_spec(spec)
    try:
        built = spec.build()
    except ValueError as exc:
        return {"ok": False, "error": str(exc), "spec": spec.to_dict()}
    lines = points_breakdown(spec)
    stats = compare_stats(spec)
    return {
        "ok": True,
        "spec": spec.to_dict(),
        "stats": [{"name": k, "value": v, "bare": b} for k, (v, b) in stats.items()],
        "weapon": weapon_summary(spec.weapon),
        "points": sum(cost for _label, cost in lines),
        "breakdown": [{"label": label, "cost": cost} for label, cost in lines],
        "rules": list(built.SpecialRules),
        "mount_parts": [
            {"name": p.name.split("'s ", 1)[-1], "WS": p.WeaponSkill, "S": p.Strength,
             "I": p.Initiative, "A": p.Attacks} for p in built.mount_parts],
        "formation": spec.formation(),
    }


def _rounds(value):
    return TO_THE_DEATH if value in (None, "death") else _int(value, 1, MAX_ROUNDS, DEFAULT_NARRATION_ROUNDS)


def _seed(value):
    return None if value in (None, "") else _int(value, 0, 2**31 - 1, None)


def odds(spec_a, spec_b, runs=DEFAULT_RUNS, rounds=None, seed=None, progress=None):
    runs = _int(runs, 1, MAX_RUNS, DEFAULT_RUNS)
    stats = run_statistics(clean_spec(spec_a), clean_spec(spec_b), runs, _rounds(rounds),
                           _seed(seed), progress=progress)
    return {
        "name_a": stats.name_a, "name_b": stats.name_b, "runs": stats.runs,
        "rounds": rounds_text(stats.rounds),
        "wins_a": stats.wins_a, "wins_b": stats.wins_b, "draws": stats.draws,
        "kills_a": stats.kills_a, "kills_b": stats.kills_b,
        "wounds_left_a": stats.wounds_left_a, "wounds_left_b": stats.wounds_left_b,
        "unit": stats.kind == UNIT,
    }


def narrate(spec_a, spec_b, rounds=DEFAULT_NARRATION_ROUNDS, seed=None):
    return narrate_duel(clean_spec(spec_a), clean_spec(spec_b), _rounds(rounds), _seed(seed))


_CALLS = {"catalog": catalog, "options": options, "shop": shop, "check_items": check_items,
          "describe": describe, "odds": odds, "narrate": narrate}


def call(name, args_json="[]", progress=None):
    """The page's single entry point: JSON arguments in, JSON result out.
    Errors come back as {"error": message} rather than exceptions."""
    try:
        if name not in _CALLS:
            raise ValueError(f"Unknown call {name!r}")
        args = json.loads(args_json)
        if not isinstance(args, list):
            raise ValueError("Arguments must be a list")
        kwargs = {"progress": progress} if name == "odds" and progress is not None else {}
        return json.dumps({"result": _CALLS[name](*args, **kwargs)})
    except (ValueError, TypeError, KeyError) as exc:
        return json.dumps({"error": str(exc) or type(exc).__name__})
