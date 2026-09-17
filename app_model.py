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
from faction_profiles import FactionProfiles
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
from special_rules import RequiresTwoHands
from weapons import get_weapon_special_rules

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
    for module in FACTION_MODULES:
        if module.FACTION == faction:
            return sorted(_roster(module, kind))
    return []


def profile_entry(faction, profile):
    return FactionProfiles[faction][profile]


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
        })
    return sorted(found, key=lambda i: (i["pane"], i["name"]))


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


@dataclass
class DuelStats:
    name_a: str
    name_b: str
    runs: int
    rounds: int
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
        header = f"{self.runs} {noun}, up to {self.rounds} round(s) each\n\n"
        if self.kind == UNIT:
            header = f"Note: {UNIT_COMBAT_NOTE}\n\n" + header
        return (
            header
            + side(self.name_a, self.wins_a, self.kills_a, self.wounds_left_a)
            + "\n"
            + side(self.name_b, self.wins_b, self.kills_b, self.wounds_left_b)
            + f"\nDraws       {self.draws:>7}  ({self.pct(self.draws):5.1f}%)\n"
        )


def run_statistics(spec_a, spec_b, runs, rounds, seed=None, progress=None):
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
        winner = combat_simulation(a, b, rounds=rounds, verbose=False)
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


def narrate_duel(spec_a, spec_b, rounds, seed=None):
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
        winner = combat_simulation(a, b, rounds=rounds, verbose=True)
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
