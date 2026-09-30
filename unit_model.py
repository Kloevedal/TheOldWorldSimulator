"""The display-free half of unit fights, used by the desktop app and the website.

A `UnitSide` is a unit (a FighterSpec of kind "unit", which carries its size,
frontage and gear) plus what goes with it in a fight: its command group, the
characters that have joined it and where they stand, spells, and how it
behaves (challenges, pursuit). `UnitFight` adds how the fight starts. Both
save to and load from plain dicts.
"""

from __future__ import annotations

import io
import re
from contextlib import redirect_stdout
from dataclasses import asdict, dataclass, field

import dice
import spells as sp
import standards
import unit_combat as uc
from app_model import CHARACTER, UNIT, FighterSpec, points_breakdown, profile_entry
from magic_items import check_unit_purchase, unit_command_options
from faction_profiles import resolve_faction
from option_costs import OPTION_COSTS
from unit_extras import BASE_SIZES, CREW, MOUNT_BASES, WIZARDS

DEFAULT_UNIT_RUNS = 100
FORMATIONS = {"Close Order": "close", "Open Order": "open", "Skirmishers": "skirmish",
              "Lance Formation": "close"}
CHARGERS = ("A", "B", None)
ARCS = ("front", "flank", "rear")


@dataclass
class JoinedCharacter:
    spec: dict  # a FighterSpec.to_dict() of kind "character"
    slot: int | None = None
    battle_standard: bool = False
    general: bool = False
    wizard_level: int = 0
    spells: list = field(default_factory=list)  # Assailment spells to cast

    def fighter(self):
        return FighterSpec.from_dict(dict(self.spec, kind=CHARACTER))


@dataclass
class UnitSide:
    unit: dict  # a FighterSpec.to_dict() of kind "unit"
    champion: bool = True
    standard: bool = True
    musician: bool = True
    characters: list = field(default_factory=list)  # [JoinedCharacter as dict]
    formation: str | None = None  # None: the unit's first formation
    inspiring_leadership: int | None = None
    battle_standard_nearby: bool = False
    high_ground: bool = False
    issue_challenges: bool = True
    accept_challenges: bool = True
    pursue: bool = True
    hexes: list = field(default_factory=list)
    enchantments: list = field(default_factory=list)
    champion_items: list = field(default_factory=list)  # magic items for the champion
    standard_items: list = field(default_factory=list)  # a magic standard (or standard runes)

    def spec(self):
        return FighterSpec.from_dict(dict(self.unit, kind=UNIT, extras={}))

    def joined(self):
        return [c if isinstance(c, JoinedCharacter) else JoinedCharacter(**c) for c in self.characters]

    def to_dict(self):
        data = asdict(self)
        data["characters"] = [asdict(c) for c in self.joined()]
        return data

    @classmethod
    def from_dict(cls, data):
        known = {k: data[k] for k in cls.__dataclass_fields__ if k in data}
        return cls(**known)


@dataclass
class UnitFight:
    charger: str | None = "A"  # "A", "B" or None (already engaged)
    charge_distance: float = 6.0
    arc: str = "front"
    disordered: bool = False
    max_turns: int = 20


# -- options for the pickers ------------------------------------------------------


def unit_options(faction, profile):
    """What a unit may take: which command models (from its page), the
    champion's name, what the champion and standard bearer may buy, its
    formations and its base size."""
    entry = profile_entry(faction, profile)
    rules = entry["base_profile"].get("SpecialRules") or []
    # A formation the unit may swap to ("Replace the Close Order special rule
    # with Skirmishers") is offered as an option; both are formation choices.
    rules = list(rules) + list(entry["base_profile"].get("OptionalRules") or [])
    formations = [FORMATIONS[r] for r in rules if r in FORMATIONS]
    command = unit_command_options(faction, profile)
    roles = list(command["command"])
    if not entry.get("champion") and "champion" in roles:
        roles.remove("champion")  # no champion statline to fight with
    return {
        "command": roles,
        "champion": command.get("champion") or (entry.get("champion") or {}).get("Name"),
        "champion_items": command.get("champion_items") or {},
        "standard_items": command.get("standard_items") or {},
        "formations": list(dict.fromkeys(formations)) or ["close"],
        "base": BASE_SIZES.get(resolve_faction(faction) or faction, {}).get(profile),
    }


def command_item_choices(faction, profile, role):
    """[{name, cost, budget, summary, note}] a champion ("champion") or
    standard bearer ("standard") may buy."""
    from app_model import item_summary
    from magic_items import get_magic_item, item_budget, unit_items_for

    found = []
    for name in unit_items_for(faction, profile, role):
        entry = get_magic_item(name) or {}
        note = ""
        if role == "standard":
            if name in standards.NOT_IN_A_FIGHT:
                note = "no effect in a unit fight: " + standards.NOT_IN_A_FIGHT[name]
        elif entry.get("status") == "not modelled":
            note = "not simulated"
        found.append({"name": name, "cost": entry.get("cost") or 0, "budget": item_budget(name),
                      "summary": item_summary(name) if role == "champion" else _standard_summary(name),
                      "note": note})
    return sorted(found, key=lambda i: (i["cost"], i["name"]))


_STANDARD_WORDS = {
    "cr": "+{} combat result", "cr_charge": "+{} combat result on the charge",
    "cr_once": "+{} combat result once", "charge_strength": "+{} Strength on the charge",
    "rank_bonus_double": "Rank Bonus +2 per rank", "steadfast": "may fall back even if outnumbered",
    "break_3d6": "Break tests on 3D6, drop the highest", "cold_blooded": "once: Break test with an extra die",
    "ignore_negative_ld": "ignores Leadership penalties", "ld_bonus": "+{} Leadership",
    "fearless": "passes Fear and Terror tests", "fear_3d6": "Fear tests on 3D6, drop the highest",
    "keep_frenzy": "never loses Frenzy", "improve_regen": "Regeneration +{}",
    "enemy_ld": "enemy -{} Leadership", "enemy_fear_ld": "enemy -{} Leadership on Fear tests",
    "enemy_fear_extra_die": "enemy Fear tests with an extra die", "worse_armour_both": "all armour saves -{}",
    "front_charge_disordered": "chargers in front are disordered",
    "hesitation": "chargers in front do not count as charging", "no_rear_bonus": "no rear bonus for enemies",
    "no_stomps_against": "no Stomps against it", "impact_reroll_wounds": "re-roll failed Impact Hit wounds",
    "spell_deflect": "enemy spells fail on {}+", "enemy_casting": "enemy casting -{}",
    "pursuit_reroll": "re-roll Pursuit", "reroll_move_ones": "re-roll 1s to flee and pursue",
    "fear_or_terror": "Fear (Terror if it has Fear)", "lothern": "spears support from the third rank",
}


def _standard_summary(name):
    """A standard's effect in a few words."""
    effect = standards.EFFECTS.get(name)
    if not effect:
        return ""
    parts = []
    for key, value in effect.items():
        if key in ("rules", "rules_not_mounts", "charge_rules", "first_round_rules", "enemy_rules"):
            prefix = {"charge_rules": "on the charge: ", "first_round_rules": "first round: ",
                      "enemy_rules": "enemy gains ", "rules_not_mounts": ""}.get(key, "")
            parts.append(prefix + ", ".join(value))
        elif key in ("stats", "enemy_stats"):
            words = ", ".join(f"{k} {v:+d}" if isinstance(v, int) else f"{k} {v}" for k, v in value.items())
            parts.append(("enemy " if key == "enemy_stats" else "") + words)
        elif key == "start_hits":
            parts.append(f"{value[0]} S{value[1]} hits each Combat phase")
        elif key == "pursuit_dice":
            parts.append("Pursuit on 1D6" if value == "one" else "Pursuit on 3D6, drop the lowest")
        else:
            parts.append(_STANDARD_WORDS.get(key, key.replace("_", " ")).format(value))
    return "; ".join(parts)


def wizard_info(faction, profile):
    """{"level": n, "lores": [...], "assailment": [...]} or None."""
    info = WIZARDS.get(resolve_faction(faction) or faction, {}).get(profile)
    if not info:
        return None
    return dict(info, assailment=sp.assailment_spells(info["lores"]))


def spell_choices():
    """{"Hex": [...], "Enchantment": [...]}: spells that do something in a fight."""
    return sp.hexes_and_enchantments()


# -- building the engine's sides -----------------------------------------------------


def _parts(entry):
    parts = []
    for row in entry.get("other_profiles") or []:
        if isinstance(row.get("WeaponSkill"), int) and isinstance(row.get("Attacks"), int):
            count = re.search(r"\(x(\d+)\)", row.get("Name") or "")
            parts.append((row, int(count.group(1)) if count else 1))
    return parts


def _chariot_strength(entry):
    body = next((r for r in entry.get("other_profiles") or []
                 if r.get("WeaponSkill") is None and r.get("Strength")), None)
    return body and body.get("Strength")


def build_side(side: UnitSide, name=None):
    """The engine's SideSetup. Raises ValueError for an illegal loadout."""
    spec = side.spec()
    model = spec.build(name or spec.name)
    faction = resolve_faction(spec.faction) or spec.faction
    entry = profile_entry(faction, spec.profile)
    options = unit_options(faction, spec.profile)
    formation = side.formation if side.formation in options["formations"] else options["formations"][0]
    if side.champion and side.champion_items:
        check_unit_purchase(faction, spec.profile, "champion", side.champion_items)
    if side.standard and side.standard_items:
        check_unit_purchase(faction, spec.profile, "standard", side.standard_items)
    placed = []
    for joined in side.joined():
        char_spec = joined.fighter()
        character = char_spec.build()
        placed.append(uc.Placement(
            character=character, slot=joined.slot, battle_standard=joined.battle_standard,
            general=joined.general, wizard_level=joined.wizard_level or 0,
            spells=[s for s in joined.spells if s in sp.ASSAILMENT]))
    return uc.SideSetup(
        name=name or spec.name, model=model, models=spec.models, frontage=spec.frontage,
        base=options["base"] or uc._DEFAULT_BASE,
        champion=entry.get("champion") if side.champion and "champion" in options["command"] else None,
        standard=side.standard and "standard" in options["command"],
        musician=side.musician and "musician" in options["command"], characters=placed,
        champion_items=list(side.champion_items) if side.champion else [],
        standard_items=list(side.standard_items) if side.standard else [],
        parts=_parts(entry), impact_strength=_chariot_strength(entry),
        crew=CREW.get(faction, {}).get(spec.profile, 1), formation=formation,
        inspiring_leadership=side.inspiring_leadership,
        battle_standard_nearby=side.battle_standard_nearby, high_ground=side.high_ground,
        issue_challenges=side.issue_challenges, accept_challenges=side.accept_challenges,
        pursue=side.pursue,
        hexes=[s for s in side.hexes if s in sp.EFFECTS],
        enchantments=[s for s in side.enchantments if s in sp.EFFECTS],
    )


def layout(side: UnitSide):
    """{"front": [occupant], "ranks": [sizes]} for drawing the unit. A
    character appears as its name."""
    setup = build_side(side)
    unit = uc.Unit(0, setup)
    slots = unit.slots()
    front = []
    for slot in range(len(slots)):
        occupant = slots[slot]
        front.append(occupant[1].character.name if isinstance(occupant, tuple) else occupant)
    return {"front": front, "ranks": unit.rank_sizes()}


def side_for(spec):
    """The UnitSide a unit FighterSpec describes (its `extras` hold the rest)."""
    extras = {k: v for k, v in (spec.extras or {}).items() if k != "unit"}
    return UnitSide.from_dict(dict(extras, unit=dict(spec.to_dict(), extras={})))


def _names(side_a, side_b):
    a, b = side_a.spec().name.strip() or side_a.spec().profile, side_b.spec().name.strip() or side_b.spec().profile
    return (f"{a} (A)", f"{b} (B)") if a == b else (a, b)


def build_fight(side_a: UnitSide, side_b: UnitSide, fight: UnitFight):
    name_a, name_b = _names(side_a, side_b)
    charger = {"A": 0, "B": 1}.get(fight.charger)
    return uc.FightSetup(
        sides=(build_side(side_a, name_a), build_side(side_b, name_b)), charger=charger,
        charge_distance=max(0.0, float(fight.charge_distance)),
        arc=fight.arc if fight.arc in ARCS else "front",
        disordered=bool(fight.disordered), max_turns=max(1, int(fight.max_turns)))


def side_points(side: UnitSide):
    """[(label, points)]: the unit, its command group, then each character."""
    spec = side.spec()
    lines = points_breakdown(spec)
    faction = resolve_faction(spec.faction) or spec.faction
    command = OPTION_COSTS.get(faction, {}).get(spec.profile, {}).get("command", {})
    options = unit_options(faction, spec.profile)
    champion = options["champion"]
    for key, label in (("champion", champion or "Champion"), ("standard", "Standard bearer"),
                       ("musician", "Musician")):
        if getattr(side, key) and key in options["command"] and command.get(key):
            lines.append((label, command[key]))
    from magic_items import get_magic_item

    for key, items in (("champion", side.champion_items), ("standard", side.standard_items)):
        if getattr(side, key) and key in options["command"]:
            for name in items:
                lines.append((name, (get_magic_item(name) or {}).get("cost") or 0))
    for joined in side.joined():
        char_spec = joined.fighter()
        lines.append((char_spec.name or char_spec.profile, sum(c for _l, c in points_breakdown(char_spec))))
    return lines


# -- runs ---------------------------------------------------------------------------


@dataclass
class UnitStats:
    name_a: str
    name_b: str
    runs: int
    wins: list = field(default_factory=lambda: [0, 0])
    draws: int = 0
    outcomes: list = field(default_factory=lambda: [{}, {}])  # how each side's wins came about
    turns: int = 0
    models_left: list = field(default_factory=lambda: [0, 0])  # summed over that side's wins

    kind = UNIT

    @property
    def wins_a(self):
        return self.wins[0]

    @property
    def wins_b(self):
        return self.wins[1]

    def pct(self, count):
        return 100.0 * count / self.runs if self.runs else 0.0

    def summary(self):
        lines = [f"{self.runs} unit fights\n"]
        for i, name in enumerate((self.name_a, self.name_b)):
            wins = self.wins[i]
            lines.append(f"{name}: {wins} wins ({self.pct(wins):.1f}%)")
            for outcome, count in sorted(self.outcomes[i].items(), key=lambda kv: -kv[1]):
                lines.append(f"  enemy {outcome}: {count}")
            if wins:
                lines.append(f"  models left when winning: {self.models_left[i] / wins:.1f} on average")
        lines.append(f"Draws / still fighting: {self.draws}")
        lines.append(f"Average length: {self.turns / max(1, self.runs):.1f} turns")
        return "\n".join(lines) + "\n"


def run_unit_statistics(side_a, side_b, fight=None, runs=DEFAULT_UNIT_RUNS, seed=None, progress=None):
    fight = fight or UnitFight()
    build_fight(side_a, side_b, fight)  # fail early on an illegal loadout
    dice.seed(seed)
    name_a, name_b = _names(side_a, side_b)
    stats = UnitStats(name_a, name_b, runs)
    step = max(1, runs // 100)
    for i in range(runs):
        result = uc.fight(build_fight(side_a, side_b, fight))
        stats.turns += result.turns
        if result.winner is None:
            stats.draws += 1
        else:
            w = result.winner
            stats.wins[w] += 1
            stats.outcomes[w][result.outcome] = stats.outcomes[w].get(result.outcome, 0) + 1
            stats.models_left[w] += result.models_left[w]
        if progress and (i + 1) % step == 0:
            progress(i + 1)
    return stats


def narrate_unit_fight(side_a, side_b, fight=None, seed=None):
    fight = fight or UnitFight()
    setup = build_fight(side_a, side_b, fight)
    dice.seed(seed)
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        for side in setup.sides:
            chars = ", ".join(p.character.name for p in side.characters)
            print(f"{side.name}: {side.models} models, {side.frontage} wide"
                  + (f", with {chars}" if chars else ""))
        result = uc.Fight(setup, verbose=True).play()
        winner = setup.sides[result.winner].name if result.winner is not None else "nobody"
        print(f"\nResult: {winner} wins - the enemy {result.outcome} "
              f"after {result.turns} turn(s)" if result.winner is not None
              else f"\nResult: {result.outcome} after {result.turns} turn(s)")
    return buffer.getvalue().lstrip("\n")
