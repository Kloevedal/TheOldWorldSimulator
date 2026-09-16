"""The non-GUI half of the desktop app: fighter specs, saved characters, and runs.

Everything here is plain Python so it can be tested without a display. The
Tk interface in simulator_app.py only collects choices into a `FighterSpec`
and hands it to `run_statistics` or `narrate_duel`.
"""

from __future__ import annotations

import io
import json
import os
from contextlib import redirect_stdout
from dataclasses import asdict, dataclass, field
from pathlib import Path

import dice
from armor import NO_ARMOUR
from character_model import Character
from combat_simulations import combat_simulation
from elven_honors import ElvenHonors
from faction_profiles import FactionProfiles

NO_ARMOUR_LABEL = "None"


# -- catalogue ----------------------------------------------------------------


def faction_names():
    return sorted(FactionProfiles)


def profile_names(faction):
    return sorted(FactionProfiles.get(faction, {}))


def profile_entry(faction, profile):
    return FactionProfiles[faction][profile]


def gear_options(faction, profile):
    """What the gear selectors should offer for a profile.

    Returns a dict with `weapons`, `armour` (always led by "None"), `shield`
    (bool), `optional_rules`, `honours` and the profile `defaults`.
    """
    entry = profile_entry(faction, profile)
    base = entry["base_profile"]
    options = entry["equipment_options"]
    default_armour = base.get("Armor")
    if default_armour in NO_ARMOUR:
        default_armour = NO_ARMOUR_LABEL
    return {
        "weapons": list(options["weapons"]),
        "armour": [NO_ARMOUR_LABEL] + list(options["armor"]),
        "shield": bool(options["shield"]),
        "optional_rules": list(base.get("OptionalRules") or []),
        "honours": sorted(ElvenHonors) if base.get("ElvenHonours") else [],
        "defaults": {
            "weapon": base.get("Weapon") or "Hand Weapon",
            "armour": default_armour,
            "shield": bool(base.get("Shield")),
        },
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

    def build(self, name=None):
        """A fresh Character. Raises ValueError for an illegal loadout."""
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
            )

    def statline(self):
        c = self.build()
        return (
            f"WS{c.WeaponSkill}  S{c.Strength}  T{c.Toughness}  "
            f"W{c.Wounds}  I{c.Initiative}  A{c.Attacks}  Ld{c.Leadership}"
        )

    def rules(self):
        return list(self.build().SpecialRules)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        known = {k: data[k] for k in cls.__dataclass_fields__ if k in data}
        return cls(**known)


def _fighter_names(spec_a, spec_b):
    """Distinct display names, so the narration never reads 'Orc hits Orc'."""
    a, b = spec_a.name.strip() or spec_a.profile, spec_b.name.strip() or spec_b.profile
    if a == b:
        a, b = f"{a} (A)", f"{b} (B)"
    return a, b


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

        return (
            f"{self.runs} duels, up to {self.rounds} round(s) each\n\n"
            + side(self.name_a, self.wins_a, self.kills_a, self.wounds_left_a)
            + "\n"
            + side(self.name_b, self.wins_b, self.kills_b, self.wounds_left_b)
            + f"\nDraws       {self.draws:>7}  ({self.pct(self.draws):5.1f}%)\n"
        )


def run_statistics(spec_a, spec_b, runs, rounds, seed=None, progress=None):
    """Fight `runs` duels and tally them. `progress(done)` is called periodically."""
    name_a, name_b = _fighter_names(spec_a, spec_b)
    # Build once up front so an illegal loadout fails before the loop starts.
    spec_a.build(name_a)
    spec_b.build(name_b)

    dice.seed(seed)
    stats = DuelStats(name_a, name_b, runs, rounds)
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
    name_a, name_b = _fighter_names(spec_a, spec_b)
    a, b = spec_a.build(name_a), spec_b.build(name_b)
    dice.seed(seed)
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        print(f"{name_a}: {spec_a.profile} ({spec_a.faction}) with {spec_a.weapon}")
        print(f"{name_b}: {spec_b.profile} ({spec_b.faction}) with {spec_b.weapon}")
        winner = combat_simulation(a, b, rounds=rounds, verbose=True)
        print(
            f"\nResult: {winner.name if winner else 'Draw'}  "
            f"({name_a} {a.current_wounds}/{a.Wounds} W, "
            f"{name_b} {b.current_wounds}/{b.Wounds} W)"
        )
    return buffer.getvalue().lstrip("\n")


# -- saved characters -----------------------------------------------------------


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
    """Saved custom characters, keyed by name, in one JSON file."""

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
            self._specs[spec.name] = spec

    def _write(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        payload = [s.to_dict() for s in self._specs.values()]
        tmp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        tmp.replace(self.path)

    def names(self):
        return sorted(self._specs, key=str.lower)

    def get(self, name):
        return self._specs[name]

    def __contains__(self, name):
        return name in self._specs

    def save(self, spec):
        """Validate and store a spec, replacing any with the same name."""
        if not spec.name.strip():
            raise ValueError("A saved character needs a name")
        spec.build()
        self._specs[spec.name] = spec
        self._write()

    def delete(self, name):
        self._specs.pop(name, None)
        self._write()
