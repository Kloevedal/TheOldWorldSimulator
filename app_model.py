"""The non-GUI half of the desktop app: fighter specs, saved fighters, and runs.

Everything here is plain Python so it can be tested without a display. The
Tk interface in simulator_app.py only collects choices into a `FighterSpec`
and hands it to `run_statistics` or `narrate_duel`.

The app has two modes, kept apart so rank-and-file combat can slot in later:

    "character"  character duels - what the engine simulates today
    "unit"       unit vs unit. The engine has no charges, ranks or combat
                 resolution yet, so for now a unit fights as a single model of
                 its profile. Unit size and frontage are recorded on the spec
                 for when it does.
"""

from __future__ import annotations

import io
import json
import math
import os
import re
from contextlib import redirect_stdout
from dataclasses import asdict, dataclass, field
from pathlib import Path

import dice
from armor import NO_ARMOUR
from character_model import EXCLUSIVE_OPTIONS, Character, offered_options
from combat_simulations import combat_simulation
from elven_honors import ElvenHonors
from factions import FACTION_MODULES
from faction_profiles import FactionProfiles, resolve_faction
from magic_items import (
    ENGINEER_ONLY,
    allowance_for,
    check_purchase,
    get_magic_item,
    granted_equipment,
    item_budget,
    items_for,
)
from mounted import integral_mount
from mounts import HONOUR_MOUNTS, Mounts
from option_costs import OPTION_COSTS
from special_rules import RequiresTwoHands
from weapons import find_weapon_key, get_weapon_special_rules, get_weapon_stats

NO_ARMOUR_LABEL = "None"

CHARACTER = "character"
UNIT = "unit"
KINDS = (CHARACTER, UNIT)
KIND_LABELS = {CHARACTER: "Character duel", UNIT: "Unit vs unit"}

UNIT_COMBAT_NOTE = (
    "Rank-and-file combat (charges, ranks, supporting attacks, combat "
    "resolution) is not simulated yet. Each unit currently fights as a single "
    "model of its profile; unit size and frontage are recorded for later."
)


# -- catalogue ----------------------------------------------------------------


def _roster(module, kind):
    return module.CHARACTERS if kind == CHARACTER else getattr(module, "UNITS", {})


def faction_names(kind=CHARACTER):
    """Factions with at least one profile of this kind."""
    return sorted(m.FACTION for m in FACTION_MODULES if _roster(m, kind))


def profile_names(faction, kind=CHARACTER):
    faction = resolve_faction(faction) or faction
    for module in FACTION_MODULES:
        if module.FACTION == faction:
            return sorted(_roster(module, kind))
    return []


def profile_entry(faction, profile):
    return FactionProfiles[resolve_faction(faction) or faction][profile]


def is_two_handed(weapon):
    return RequiresTwoHands in get_weapon_special_rules(weapon)


def minimum_unit_size(entry):
    """The smallest legal unit size, read from e.g. "10+"; 1 if not given."""
    match = re.search(r"\d+", str(entry.get("unit_size") or ""))
    return int(match.group()) if match else 1


# Option labels that name a group of bought abilities rather than a rule;
# those are chosen through the magic item list instead.
_ABILITY_GROUP_LABELS = {"Knightly Virtue", "Elven Honour", "Chaotic Trait", "Chaotic Traits",
                         "Gifts of Chaos", "Chaos Mutations"}

EXCLUSIVE_GROUP_NAMES = ("Mark of Chaos", "Chivalrous Vow")


def exclusive_choices(faction, profile):
    """[(group name, choices, default)] for options that replace one another."""
    base = profile_entry(faction, profile)["base_profile"]
    available = set(offered_options(base)) | set(base.get("SpecialRules") or [])
    groups = []
    for name, members in zip(EXCLUSIVE_GROUP_NAMES, EXCLUSIVE_OPTIONS):
        choices = [m for m in members if m in available]
        if len(choices) > 1:
            default = next((m for m in choices if m in (base.get("SpecialRules") or [])), choices[0])
            groups.append((name, choices, default))
    return groups


def gear_options(faction, profile):
    """What the gear selectors should offer for a profile.

    Returns a dict with `weapons`, `two_handed` (the subset that cannot be used
    with a shield), `armour` (always led by "None"), `shield` (bool),
    `optional_rules` (independent upgrades), `exclusive` (groups that replace
    one another, such as Marks of Chaos), `honours` (the legacy Elven Honour
    option), `allowance` (what the character may buy), the profile `defaults`,
    and `unit` (size and points details, or None for a character).
    """
    faction = resolve_faction(faction) or faction
    entry = profile_entry(faction, profile)
    base = entry["base_profile"]
    options = entry["equipment_options"]
    weapons = list(options["weapons"])
    default_weapon = base.get("Weapon") or "Hand Weapon"
    default_armour = base.get("Armor")
    if default_armour in NO_ARMOUR:
        default_armour = NO_ARMOUR_LABEL
    unit = None
    if base.get("UnitCategory") == "Unit":
        unit = {
            "unit_size": entry.get("unit_size"),
            "minimum_size": minimum_unit_size(entry),
            "points": entry.get("points"),
            "points_per": entry.get("points_per"),
        }
    return {
        "weapons": weapons,
        "two_handed": [w for w in weapons if is_two_handed(w)],
        "armour": [NO_ARMOUR_LABEL] + list(options["armor"]),
        "shield": bool(options["shield"]),
        "optional_rules": [
            r for r in (base.get("OptionalRules") or [])
            if r not in _ABILITY_GROUP_LABELS and not any(r in g for g in EXCLUSIVE_OPTIONS)
        ],
        "exclusive": exclusive_choices(faction, profile),
        "allowance": allowance_for(faction, profile),
        "honours": sorted(ElvenHonors) if base.get("ElvenHonours") else [],
        "mounts": [m for m in entry.get("mount_options", {}).get("mounts", []) if m in Mounts],
        "fixed_mount": integral_mount(faction, profile),
        "honour_mounts": {m: h for m, h in HONOUR_MOUNTS.items()
                          if m in entry.get("mount_options", {}).get("mounts", [])},
        "defaults": {
            "weapon": default_weapon,
            "armour": default_armour,
            "shield": bool(base.get("Shield")) and not is_two_handed(default_weapon),
        },
        "unit": unit,
    }


# -- fighter specs ------------------------------------------------------------


@dataclass
class FighterSpec:
    """Everything needed to rebuild one fighter, and what gets saved to disk."""

    name: str
    faction: str
    profile: str
    weapon: str
    armour: str = NO_ARMOUR_LABEL
    shield: bool = False
    optional_rules: list = field(default_factory=list)
    honours: list = field(default_factory=list)
    magic_items: list = field(default_factory=list)
    mount: str | None = None  # None: on foot, or the profile's own fixed mount
    kind: str = CHARACTER
    models: int = 1  # unit size; always 1 for a character
    frontage: int = 1  # models in the front rank

    @property
    def ranks(self):
        """Full and partial ranks the unit is deployed in."""
        return math.ceil(self.models / max(1, self.frontage))

    def build(self, name=None):
        """A fresh Character. Raises ValueError for an illegal loadout."""
        if self.kind not in KINDS:
            raise ValueError(f"Unknown fighter kind {self.kind!r}")
        if self.kind == UNIT and (self.models < 1 or self.frontage < 1):
            raise ValueError("A unit needs at least one model and a frontage of one")
        # Construction can print warnings (unrecognised items); keep them out
        # of the terminal and out of the narration.
        with redirect_stdout(io.StringIO()):
            return Character(
                name=name or self.name,
                faction_type=self.faction,
                profile_name=self.profile,
                Weapon=self.weapon,
                # None means "use the profile default", so an explicit choice of
                # no armour has to be passed as a falsy value the model accepts.
                Armor="" if self.armour in NO_ARMOUR else self.armour,
                Shield=self.shield,
                SpecialRules=list(self.optional_rules),
                elven_honors=list(self.honours),
                magic_items=list(self.magic_items),
                mount=self.mount or None,
            )

    def statline(self):
        c = self.build()
        return (
            f"WS{c.WeaponSkill}  S{c.Strength}  T{c.Toughness}  "
            f"W{c.Wounds}  I{c.Initiative}  A{c.Attacks}  Ld{c.Leadership}"
        )

    def formation(self):
        """A one-line description of a unit's formation, or '' for a character."""
        if self.kind != UNIT:
            return ""
        return f"{self.models} models, {self.frontage} wide, {self.ranks} rank(s)"

    def rules(self):
        return list(self.build().SpecialRules)

    def __post_init__(self):
        # Specs saved under an older army name ("High Elves") load under the
        # official one ("High Elf Realms").
        self.faction = resolve_faction(self.faction) or self.faction

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        known = {k: data[k] for k in cls.__dataclass_fields__ if k in data}
        return cls(**known)


def weapon_choices(faction, profile, items=()):
    """The profile's weapons plus any its bought abilities unlock."""
    weapons = list(profile_entry(faction, profile)["equipment_options"]["weapons"])
    for weapon in granted_equipment(items)["weapons"]:
        if weapon not in weapons:
            weapons.append(weapon)
    return weapons


def armour_choices(faction, profile, items=()):
    """"None", the profile's armour, and any its bought abilities unlock."""
    from armor import get_armour_save

    armour = [NO_ARMOUR_LABEL] + list(profile_entry(faction, profile)["equipment_options"]["armor"])
    offered = {get_armour_save(a) for a in armour}
    for suit in granted_equipment(items)["armour"]:
        if get_armour_save(suit) not in offered:  # "Plate" and "Full Plate" are one suit
            armour.append(suit)
    return armour


# Shop panes: item type -> pane, with runes in their own panes.
_PANES = {
    "Magic Weapon": "Weapons", "Magic Armour": "Armour", "Talisman": "Talismans",
    "Enchanted Item": "Enchanted Items", "Arcane Item": "Arcane Items",
    "Magic Standard": "Standards",
}
_RUNE_PANES = {"Weapon Runes", "Armour Runes", "Talismanic Runes", "Standard Runes",
               "Engineers' Weapon Runes", "Engineering Runes"}


def shop_pane(entry):
    """The shop pane an item is listed under."""
    category = entry.get("category") or ""
    if category in _RUNE_PANES:
        return category
    if entry.get("type") in _PANES:
        return _PANES[entry["type"]]
    return category or entry.get("type") or "Other"


def purchasable_items(faction, profile):
    """Items this character may buy.

    [{name, cost, budget, type, pane, common, status, text}], where `common`
    marks the rulebook's items, which every army may take.
    """
    allowance = allowance_for(faction, profile)
    found = []
    for name in items_for(faction):
        budget = item_budget(name)
        if budget not in allowance:
            continue
        entry = get_magic_item(name)
        if entry.get("category") in ENGINEER_ONLY and "Engineer" not in profile:
            continue
        found.append({
            "name": name,
            "cost": entry.get("cost") or 0,
            "budget": budget,
            "type": entry.get("category") or entry.get("type"),
            "pane": shop_pane(entry),
            "common": not entry.get("armies"),
            "status": entry.get("status"),
            "text": entry.get("text", ""),
            "summary": item_summary(name),
        })
    return sorted(found, key=lambda i: (i["pane"], i["name"]))


def item_matches(item, query):
    """True if a shop item's name, type or rules text mentions every word of
    `query`, so "killing blow" finds items that grant Killing Blow as well as
    items named after it."""
    words = query.lower().split()
    if not words:
        return True
    haystack = " ".join([item["name"], item.get("type") or "", item.get("text") or "",
                         *item_rule_terms(item["name"])]).lower()
    return all(word in haystack for word in words)


_RULE_SHORTHAND = [
    (re.compile(r"^Ward(\d)"), r"Ward save (\1+)"),
    (re.compile(r"^Regen(\d)"), r"Regeneration save (\1+)"),
    (re.compile(r"^AB(\d)"), r"Armour Bane (\1)"),
    (re.compile(r"^([+-]\d)A$"), r"Extra Attacks (\1)"),
]


def item_rule_terms(name):
    """The rules an item grants, spelled out for searching."""
    entry = get_magic_item(name) or {}
    rules = list(entry.get("rules") or [])
    if entry.get("is_weapon"):
        rules += get_weapon_special_rules(name)
    if entry.get("armour"):
        rules.append(entry["armour"])
    terms = []
    for rule in map(str, rules):
        for pattern, spelled in _RULE_SHORTHAND:
            rule = pattern.sub(spelled, rule)
        terms.append(rule)
    return terms


_READABLE_RULES = {"1st round strength only": "Strength bonus in the first round only",
                   "Magic": None, "Magical Attacks": "Magical Attacks"}
_STAT_SHORT = {"WeaponSkill": "WS", "BallisticSkill": "BS", "Strength": "S", "Toughness": "T",
               "Wounds": "W", "Initiative": "I", "Attacks": "A", "Leadership": "Ld",
               "Movement": "M"}


def _readable(rules):
    out = []
    for rule in map(str, rules):
        for pattern, spelled in _RULE_SHORTHAND:
            rule = pattern.sub(spelled, rule)
        rule = _READABLE_RULES.get(rule, rule)
        if rule and rule not in out:
            out.append(rule)
    return out


def weapon_summary(weapon):
    """A weapon's profile in one line: "S+2, AP -2; Strike Last, Armour Bane (1)"."""
    if not weapon or find_weapon_key(weapon) is None:
        return ""
    strength, ap, rules = get_weapon_stats(weapon)
    parts = [f"S+{strength}" if strength else "S"]
    if ap:
        parts.append(f"AP -{abs(ap)}")
    readable = _readable(rules)
    return ", ".join(parts) + (("; " + ", ".join(readable)) if readable else "")


def item_summary(name):
    """What an item does in game terms: its weapon profile, armour, stat
    changes and rules. Empty for items with no modelled effect."""
    from armor import get_armour_save

    entry = get_magic_item(name) or {}
    parts = []
    if entry.get("is_weapon") or entry.get("weapon"):
        profile = weapon_summary(name) or weapon_summary(entry.get("weapon"))
        if profile:
            parts.append(profile)
    if entry.get("armour"):
        save = get_armour_save(entry["armour"])
        parts.append(f"{entry['armour']}" + (f" ({save}+)" if save else ""))
    if entry.get("shield"):
        parts.append("Shield (-1 save)")
    mods = entry.get("stat_mods") or {}
    if mods:
        parts.append(" ".join(f"{_STAT_SHORT.get(k, k)}{v:+d}" for k, v in mods.items()))
    rules = _readable(entry.get("rules") or [])
    if rules:
        parts.append(", ".join(rules))
    grants = entry.get("grants") or {}
    for kind in ("weapons", "armour"):
        if grants.get(kind):
            parts.append("unlocks " + ", ".join(grants[kind]))
    return " | ".join(parts)


STAT_ORDER = (("WS", "WeaponSkill"), ("S", "Strength"), ("T", "Toughness"), ("W", "Wounds"),
              ("I", "Initiative"), ("A", "Attacks"), ("Ld", "Leadership"))


def _bare_spec(spec):
    """The same model with nothing added: hand weapon, no armour, shield,
    upgrades, honours, items or optional mount."""
    return FighterSpec(name=spec.name, faction=spec.faction, profile=spec.profile,
                       weapon="Hand Weapon", armour=NO_ARMOUR_LABEL, kind=spec.kind,
                       models=spec.models, frontage=spec.frontage)


def fighting_stats(character):
    """{short name: value} as the fighter strikes in the first round: weapon
    Strength and extra attacks included. Dice attacks read like "3+D3"."""
    from combat_simulations import apply_weapon_stats, reset_weapon_stats
    from special_rules import FuriousCharge, Frenzy, MarkOfKhorne, parse_extra_attacks

    apply_weapon_stats(character, is_first_round=True, verbose=False)
    values = {short: getattr(character, attr, None) for short, attr in STAT_ORDER}
    reset_weapon_stats(character)
    weapon_rules = get_weapon_special_rules(character.Weapon)
    rules = character.SpecialRules or []
    fixed, dice_parts = 0, []
    for amount in parse_extra_attacks(rules, weapon_rules):
        if isinstance(amount, int) or str(amount).lstrip("+-").isdigit():
            fixed += int(amount)
        else:
            dice_parts.append(str(amount))
    for rule in map(str, weapon_rules):
        if re.fullmatch(r"\+\d+A", rule):
            fixed += int(rule[1:-1])
    if Frenzy in rules or MarkOfKhorne in rules:
        fixed += 1
    if FuriousCharge in rules:
        fixed += 1
    attacks = (values["A"] or 0) + fixed
    values["A"] = "+".join([str(attacks), *dice_parts]) if dice_parts else attacks
    return values


def compare_stats(spec):
    """{short name: (with everything, bare profile)} for the X (y) statline."""
    current = fighting_stats(spec.build())
    try:
        bare = fighting_stats(_bare_spec(spec).build())
    except ValueError:
        bare = {}
    return {short: (current[short], bare.get(short)) for short, _attr in STAT_ORDER}


def purchase_problem(faction, profile, items):
    """Why a set of items may not be bought, or None if it may."""
    try:
        check_purchase(faction, profile, items)
    except ValueError as exc:
        return str(exc)
    return None


def spent(items):
    """{budget: points} spent on a set of items."""
    totals = {}
    for name in items:
        entry = get_magic_item(name)
        if entry is not None:
            budget = item_budget(name)
            totals[budget] = totals.get(budget, 0) + (entry.get("cost") or 0)
    return totals


def _same_armour(a, b):
    from armor import get_armour_save

    return a == b or get_armour_save(a) == get_armour_save(b)


def points_breakdown(spec):
    """[(label, points)] for everything the fighter costs, base profile first.

    Weapon, armour, shield, mount and rule prices come from the profile's
    options (option_costs.py); anything the profile carries for free costs
    nothing. A unit priced per model pays its base cost and its per-model
    upgrades once for each model.
    """
    entry = profile_entry(spec.faction, spec.profile)
    prices = OPTION_COSTS.get(resolve_faction(spec.faction) or spec.faction, {}).get(spec.profile, {})
    per_model = spec.kind == UNIT and entry.get("points_per") == "model"
    models = max(1, spec.models) if per_model else 1
    upgrade_times = models if prices.get("per_model") and per_model else 1
    lines = []
    base = entry.get("points") or 0
    lines.append((f"{spec.profile} ({models} x {base})" if models > 1 else spec.profile, base * models))

    def add(label, cost, times=upgrade_times):
        if cost:
            lines.append((label if times == 1 else f"{label} ({times} x {cost})", cost * times))

    add(spec.weapon, prices.get("weapons", {}).get(spec.weapon, 0))
    if spec.armour not in NO_ARMOUR:
        armour = prices.get("armour", {})
        add(spec.armour, next((c for a, c in armour.items() if _same_armour(a, spec.armour)), 0))
    if spec.shield:
        add("Shield", prices.get("shield", 0))
    if spec.mount and spec.mount != integral_mount(spec.faction, spec.profile):
        cost = prices.get("mounts", {}).get(spec.mount)
        if cost is None:
            cost = (Mounts.get(spec.mount) or {}).get("points") or 0
        add(spec.mount, cost, 1)
    rule_prices = prices.get("rules", {})
    for rule in spec.optional_rules:
        add(rule, rule_prices.get(rule, 0))
    for name in spec.magic_items:
        add(name, (get_magic_item(name) or {}).get("cost") or 0, 1)
    return lines


def option_price(faction, profile, kind, name):
    """Points for one weapon, armour, mount or rule on this profile (0 if free)."""
    prices = OPTION_COSTS.get(resolve_faction(faction) or faction, {}).get(profile, {})
    if kind == "armour":
        return next((c for a, c in prices.get("armour", {}).items() if _same_armour(a, name)), 0)
    if kind == "shield":
        return prices.get("shield", 0)
    cost = prices.get(kind, {}).get(name)
    if cost is None and kind == "mounts":
        cost = (Mounts.get(name) or {}).get("points")
    return cost or 0


def choice_label(faction, profile, kind, name):
    """A picker entry with its price and short profile:
    "Great Weapon · +4 pts · S+2, AP -2"."""
    from armor import get_armour_save

    parts = [name]
    cost = option_price(faction, profile, kind, name)
    per = OPTION_COSTS.get(resolve_faction(faction) or faction, {}).get(profile, {}).get("per_model")
    if cost:
        parts.append(f"+{cost} pts" + ("/model" if per and kind != "mounts" else ""))
    if kind == "weapons":
        short = weapon_summary(name).split(";")[0]
        if short and short != "S":
            parts.append(short)
    elif kind == "armour" and name not in NO_ARMOUR:
        save = get_armour_save(name)
        if save:
            parts.append(f"{save}+ save")
    return " · ".join(parts)


def total_points(spec):
    return sum(cost for _label, cost in points_breakdown(spec))


def _fighter_names(spec_a, spec_b):
    """Distinct display names, so the narration never reads 'Orc hits Orc'."""
    a, b = spec_a.name.strip() or spec_a.profile, spec_b.name.strip() or spec_b.profile
    if a == b:
        a, b = f"{a} (A)", f"{b} (B)"
    return a, b


def _check_same_kind(spec_a, spec_b):
    if spec_a.kind != spec_b.kind:
        raise ValueError(
            f"Cannot pit a {spec_a.kind} against a {spec_b.kind}; "
            "choose two characters or two units"
        )


# -- runs ---------------------------------------------------------------------

# App defaults: Odds fights 100 times to the death; Play-by-play shows six
# rounds. rounds=TO_THE_DEATH fights until a fighter falls, capped so that two
# fighters who cannot hurt each other still finish (as a draw).
TO_THE_DEATH = None
DEATH_ROUND_CAP = 100
DEFAULT_RUNS = 100
DEFAULT_NARRATION_ROUNDS = 6


def round_limit(rounds):
    return DEATH_ROUND_CAP if rounds is TO_THE_DEATH else rounds


def rounds_text(rounds):
    return "to the death" if rounds is TO_THE_DEATH else f"up to {rounds} round(s) each"



@dataclass
class DuelStats:
    name_a: str
    name_b: str
    runs: int
    rounds: int | None  # TO_THE_DEATH or a round limit
    wins_a: int = 0
    wins_b: int = 0
    kills_a: int = 0  # wins where the opponent was slain, not out-lasted
    kills_b: int = 0
    draws: int = 0
    wounds_left_a: int = 0  # summed over A's wins
    wounds_left_b: int = 0
    kind: str = CHARACTER

    def pct(self, count):
        return 100.0 * count / self.runs if self.runs else 0.0

    def summary(self):
        def side(name, wins, kills, left):
            avg = left / wins if wins else 0.0
            return (
                f"{name}\n"
                f"  wins        {wins:>7}  ({self.pct(wins):5.1f}%)\n"
                f"  by slaying  {kills:>7}  ({self.pct(kills):5.1f}%)\n"
                f"  on wounds   {wins - kills:>7}  ({self.pct(wins - kills):5.1f}%)\n"
                f"  avg wounds left when winning: {avg:.2f}\n"
            )

        noun = "duels" if self.kind == CHARACTER else "model-vs-model fights"
        header = f"{self.runs} {noun}, {rounds_text(self.rounds)}\n\n"
        if self.kind == UNIT:
            header = f"Note: {UNIT_COMBAT_NOTE}\n\n" + header
        return (
            header
            + side(self.name_a, self.wins_a, self.kills_a, self.wounds_left_a)
            + "\n"
            + side(self.name_b, self.wins_b, self.kills_b, self.wounds_left_b)
            + f"\nDraws       {self.draws:>7}  ({self.pct(self.draws):5.1f}%)\n"
        )


def run_statistics(spec_a, spec_b, runs=DEFAULT_RUNS, rounds=TO_THE_DEATH, seed=None, progress=None):
    """Fight `runs` duels and tally them. `progress(done)` is called periodically."""
    _check_same_kind(spec_a, spec_b)
    name_a, name_b = _fighter_names(spec_a, spec_b)
    # Build once up front so an illegal loadout fails before the loop starts.
    spec_a.build(name_a)
    spec_b.build(name_b)

    dice.seed(seed)
    stats = DuelStats(name_a, name_b, runs, rounds, kind=spec_a.kind)
    step = max(1, runs // 100)
    for i in range(runs):
        a, b = spec_a.build(name_a), spec_b.build(name_b)
        winner = combat_simulation(a, b, rounds=round_limit(rounds), verbose=False)
        if winner is None:
            stats.draws += 1
        elif winner is a:
            stats.wins_a += 1
            stats.kills_a += b.current_wounds <= 0
            stats.wounds_left_a += a.current_wounds
        else:
            stats.wins_b += 1
            stats.kills_b += a.current_wounds <= 0
            stats.wounds_left_b += b.current_wounds
        if progress and (i + 1) % step == 0:
            progress(i + 1)
    return stats


def narrate_duel(spec_a, spec_b, rounds=DEFAULT_NARRATION_ROUNDS, seed=None):
    """Fight one duel and return the engine's round-by-round narration."""
    _check_same_kind(spec_a, spec_b)
    name_a, name_b = _fighter_names(spec_a, spec_b)
    a, b = spec_a.build(name_a), spec_b.build(name_b)
    dice.seed(seed)
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        if spec_a.kind == UNIT:
            print(f"Note: {UNIT_COMBAT_NOTE}\n")
        for name, spec, model in ((name_a, spec_a, a), (name_b, spec_b, b)):
            formation = f", {spec.formation()}" if spec.kind == UNIT else ""
            mount = f", riding {model.mount}" if model.mount else ""
            print(f"{name}: {spec.profile} ({spec.faction}) with {spec.weapon}{mount}{formation}")
        winner = combat_simulation(a, b, rounds=round_limit(rounds), verbose=True)
        print(
            f"\nResult: {winner.name if winner else 'Draw'}  "
            f"({name_a} {a.current_wounds}/{a.Wounds} W, "
            f"{name_b} {b.current_wounds}/{b.Wounds} W)"
        )
    return buffer.getvalue().lstrip("\n")


# -- saved fighters -------------------------------------------------------------


def default_store_path():
    override = os.environ.get("TOW_SIM_CHARACTERS")
    if override:
        return Path(override)
    return (
        Path.home()
        / "Library"
        / "Application Support"
        / "TheOldWorldSimulator"
        / "custom_characters.json"
    )


class CharacterStore:
    """Saved custom characters and units, keyed by (kind, name), in one JSON file.

    Files written before units existed have no `kind`; those entries load as
    characters.
    """

    def __init__(self, path=None):
        self.path = Path(path) if path else default_store_path()
        self._specs = {}
        self.load()

    def load(self):
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            data = []
        self._specs = {}
        for item in data:
            spec = FighterSpec.from_dict(item)
            self._specs[(spec.kind, spec.name)] = spec

    def _write(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        payload = [s.to_dict() for s in self._specs.values()]
        tmp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        tmp.replace(self.path)

    def names(self, kind=CHARACTER):
        return sorted((n for k, n in self._specs if k == kind), key=str.lower)

    def get(self, name, kind=CHARACTER):
        return self._specs[(kind, name)]

    def contains(self, name, kind=CHARACTER):
        return (kind, name) in self._specs

    def save(self, spec):
        """Validate and store a spec, replacing any of the same kind and name."""
        if not spec.name.strip():
            raise ValueError("A saved fighter needs a name")
        spec.build()
        self._specs[(spec.kind, spec.name)] = spec
        self._write()

    def delete(self, name, kind=CHARACTER):
        self._specs.pop((kind, name), None)
        self._write()
