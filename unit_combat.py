"""Rank-and-file combat: two units fight until one breaks, is destroyed or escapes.

This follows the Combat phase rules of Warhammer: the Old World
(tow.whfb.app, "The Combat Phase", "Characters", "Command Groups", "Troop
Types in Detail"). The dice go through the duel engine's To Hit, To Wound and
armour save rolls (combat_simulations), so every weapon and special rule the
duel engine understands works here too.

A fight is a series of turns, alternating between the two players, with one
round of combat in each (the Combat phase happens in both players' turns).
The charger's turn comes first. Each round:

1. Start of turn: Hex and Enchantment spells the active player keeps up are
   (re)applied; spells that lasted "until the end of this turn" expire.
2. Fear tests for units facing a Fear-causing enemy of higher Unit Strength.
3. Impact Hits from charging models in base contact (charge of 3" or more).
4. Challenges: the active player may issue one, then the other.
5. Attacks, from the highest Initiative down. Models of equal Initiative
   strike simultaneously. Models slain before their turn to strike lose their
   attacks; models stepping forward into the fighting rank cannot attack.
   Wizards cast their Assailment spells at their Initiative. Stomp Attacks
   come last.
6. Combat result: Wounds lost (including ones later regenerated), Overkill,
   Rank Bonus, standards, flank and rear, high ground, Close Order, Massed
   Infantry, a musician in a draw.
7. The loser takes a Break test: Breaks and flees, Falls Back in Good Order
   (a Break if the winner's Unit Strength is more than double) or Gives Ground.
8. Follow up and pursuit: a unit that Gives Ground is followed up and the
   fight goes on; one that Falls Back is caught if the Pursuit roll reaches it
   (the fight goes on, the pursuer counting as having charged); one that
   flees is run down if the Pursuit roll reaches it.

Geometry: units are rectangles of their models' bases (base sizes from the
unit pages), aligned centre to centre as a charge would align them. A model
is in base contact if its base touches the enemy's, even at a corner.

Not simulated (and said so in the narration where it matters): movement
before the fight (charge declaration, Fear and Terror tests to charge, charge
reactions), rallying after the fight, multiple units in one combat, terrain,
Lance Formation's own rules, template spells, miscast results, and
characters targeting or being targeted outside challenges (rank and file
fight rank and file).
"""

from __future__ import annotations

import copy
import math
import re
from dataclasses import dataclass, field

from combat_simulations import (
    RollArmorSave,
    RollToHit,
    RollToWound,
    Wound,
    _weapon_stats_or_default,
    apply_weapon_stats,
    attempt_ward_save,
    effective_initiative,
    frenzy_bonus_applies,
    is_killing_blow_target,
    reset_weapon_stats,
)
from dice import roll_amount, roll_d6
from special_rules import (
    Flammable,
    Frenzy,
    FuriousCharge,
    ImmuneToMultipleWounds,
    ImmuneToPsychology,
    MarkOfKhorne,
    NoRegeneration,
    PoisonedAttacks,
    StrikeFirst,
    StrikeLast,
    Stubborn,
    Warband,
    parse_armour_piercing_bonus,
    parse_extra_attacks,
    parse_impact_hits,
    parse_impact_hits_ap,
    parse_multiple_wounds,
    parse_regeneration,
    parse_stomp_attacks,
)
from weapons import get_weapon_special_rules

# -- troop types ---------------------------------------------------------------

# Troop type -> (models per rank for a Rank Bonus, maximum Rank Bonus, Unit
# Strength per model; "W" means as starting Wounds). From the Troop Type Table.
TROOP_TABLE = {
    "regularinfantry": (5, 2, 1),
    "heavyinfantry": (4, 2, 1),
    "monstrousinfantry": (3, 2, 3),
    "swarm": (None, 0, 3),
    "lightcavalry": (5, 1, 2),
    "heavycavalry": (4, 1, 2),
    "monstrouscavalry": (3, 1, 3),
    "warbeast": (5, 1, 1),
    "lightchariot": (3, 1, 3),
    "heavychariot": (None, 0, 5),
    "monstrouscreature": (None, 0, "W"),
    "behemoth": (None, 0, "W"),
    "warmachine": (None, 0, "W"),
}
# Troop types with the Press of Battle, Massed Infantry and Parry rules.
_BATTLE_LINE = ("regularinfantry", "heavyinfantry")
_CAVALRY = ("lightcavalry", "heavycavalry", "monstrouscavalry", "warbeast")
_CHARIOTS = ("lightchariot", "heavychariot")
_MONSTERS = ("monstrouscreature", "behemoth")

SUPPORT_WEAPONS = ("Thrusting Spear", "Cavalry Spear")
FIGHT_IN_EXTRA_RANK = "Fight in Extra Rank"
CHARGE_ONLY_WEAPONS = ("Lance",)
_DEFAULT_BASE = (25, 25)
EPS = 1e-6

# Outcomes of a fight.
DESTROYED = "destroyed"
RUN_DOWN = "broke and was run down"
FLED = "broke and fled"
FELL_BACK = "fell back in good order"
GAVE_GROUND = "gave ground"
STALEMATE = "still fighting"
MUTUAL = "both destroyed"


def troop_key(model) -> str:
    return re.sub(r"[^a-z]", "", str(getattr(model, "TroopType", "") or "").lower())


def troop_stats(model):
    return TROOP_TABLE.get(troop_key(model), (5, 2, 1))


def _rules(model):
    return list(model.SpecialRules or []) + list(get_weapon_special_rules(model.Weapon))


def _has(model, rule):
    return rule in (model.SpecialRules or [])


def _frenzied(model):
    rules = model.SpecialRules or []
    return Frenzy in rules or MarkOfKhorne in rules


# -- sides -----------------------------------------------------------------------


@dataclass
class Placement:
    """A character that has joined the unit, in front-rank slot `slot`."""

    character: object  # a built Character
    slot: int | None = None  # None: as close to the centre as possible
    battle_standard: bool = False
    general: bool = False
    wizard_level: int = 0
    spells: list = field(default_factory=list)  # Assailment spells it will cast
    retired: bool = False  # refused a challenge and hid in the rear ranks


@dataclass
class SideSetup:
    """One side of a unit fight."""

    name: str
    model: object  # a built Character: the rank-and-file profile, as equipped
    models: int
    frontage: int
    base: tuple = _DEFAULT_BASE
    champion: dict | None = None  # the champion's statline, or None
    standard: bool = False
    musician: bool = False
    characters: list = field(default_factory=list)  # [Placement]
    parts: list = field(default_factory=list)  # [(row dict, count)] mounts / beasts
    impact_strength: int | None = None  # a chariot's Strength, for Impact Hits
    crew: int = 1  # models sharing the rank-and-file statline (a chariot's crew)
    formation: str = "close"  # "close", "open" or "skirmish"
    inspiring_leadership: int | None = None  # a nearby General's Leadership
    battle_standard_nearby: bool = False  # Hold Your Ground from outside the unit
    high_ground: bool = False
    issue_challenges: bool = True
    accept_challenges: bool = True
    pursue: bool = True
    hexes: list = field(default_factory=list)  # spell names cast on this unit by the enemy
    enchantments: list = field(default_factory=list)  # spell names cast on it by its own side
    champion_items: list = field(default_factory=list)  # magic items the champion carries
    standard_items: list = field(default_factory=list)  # the magic standard (or standard runes)


@dataclass
class FightSetup:
    sides: tuple  # (SideSetup, SideSetup)
    charger: int | None = 0  # index of the charging side; None: already engaged
    charge_distance: float = 6.0  # inches the charger moved before contact
    arc: str = "front"  # which arc of the charged unit was charged
    disordered: bool = False  # a disordered charge: no Initiative bonus
    max_turns: int = 20


@dataclass
class FightResult:
    winner: int | None  # side index, or None
    outcome: str  # what happened to the loser (or STALEMATE / MUTUAL)
    turns: int
    models_left: tuple
    wounds_caused: tuple  # total Wounds each side made the other lose
    log: list = field(default_factory=list)


class Unit:
    """A unit's state during the fight."""

    def __init__(self, index, setup: SideSetup):
        self.index = index
        self.setup = setup
        self.name = setup.name
        self.model = setup.model
        self.model.current_wounds = self.model.Wounds
        self.wounds_each = max(1, self.model.Wounds or 1)
        self.models = setup.models
        self.start_models = setup.models
        self.frontage = max(1, setup.frontage)
        self.base = setup.base or _DEFAULT_BASE
        self.damage = 0  # Wounds lost by the model that will be removed next
        self.champion = None
        if setup.champion:
            self.champion = _champion(self.model, setup.champion)
            if setup.champion_items:
                from magic_items import equip

                equip(self.champion, setup.champion_items)
        self.standard = setup.standard
        import standards

        self._banners = [standards.effect(n) for n in (setup.standard_items if setup.standard else [])]
        self.banner_used = False  # single-use standards
        self.cold_blooded_used = False
        self.enemy_rolls = {}  # dice rolled once per fight for effects on the enemy
        self.musician = setup.musician
        self.characters = list(setup.characters)
        for placed in self.characters:
            placed.character.current_wounds = placed.character.Wounds
        self.parts = [_part(self.model, row, count) for row, count in setup.parts]
        # Regular and heavy infantry Parry with a hand weapon and shield.
        for model in [self.model, self.champion] + [p.character for p in self.characters]:
            if model is not None and troop_key(model) in _BATTLE_LINE and "Parry" not in (model.SpecialRules or []):
                model.SpecialRules = list(model.SpecialRules or []) + ["Parry"]
        self.formation = setup.formation
        self.stubborn_used = False
        self.shieldwall_used = False
        self.first_charge_used = False
        self.frenzy_lost = False
        self.ld_penalty = 0
        self.no_inspiring = self.accursed_mirror = self.ramparts = False
        self.followed_up = False  # made a follow up move last turn
        self.feared = False  # failed a Fear test this turn
        self.snap = {}
        self._remember(self.model)
        for placed in self.characters:
            self._remember(placed.character)
            for part in getattr(placed.character, "mount_parts", []):
                self._remember(part)
        if self.champion:
            self._remember(self.champion)
        for part in self.parts:
            self._remember(part)

    # Stats are restored from a snapshot each turn, then spells are applied.
    _STATS = ("WeaponSkill", "Strength", "Toughness", "Initiative", "Attacks", "Leadership")

    def _remember(self, model):
        self.snap[id(model)] = (model, {s: getattr(model, s, None) for s in self._STATS},
                                list(model.SpecialRules or []), getattr(model, "Armor", None))

    def restore(self):
        for model, stats, rules, armour in self.snap.values():
            for stat, value in stats.items():
                setattr(model, stat, value)
                if hasattr(model, f"original_{stat}"):
                    setattr(model, f"original_{stat}", value)
            model.SpecialRules = list(rules)

    # -- composition ---------------------------------------------------------

    def fighters(self):
        """Characters still in the unit and able to fight."""
        return [p for p in self.characters if p.character.current_wounds > 0 and not p.retired]

    def all_models(self):
        """Every model whose rules and Leadership count for the unit."""
        found = [self.model] if self.models > 0 else []
        if self.champion is not None and self.models > 0:
            found.append(self.champion)
        return found + [p.character for p in self.fighters()]

    @property
    def alive(self):
        return self.models > 0 or any(p.character.current_wounds > 0 for p in self.characters)

    def bodies(self):
        return self.models + len([p for p in self.characters if p.character.current_wounds > 0])

    def ranks(self):
        return math.ceil(self.bodies() / self.frontage) if self.bodies() else 0

    def rank_sizes(self):
        left, sizes = self.bodies(), []
        while left > 0:
            sizes.append(min(self.frontage, left))
            left -= self.frontage
        return sizes

    def combat_order(self):
        return self.formation in ("close", "open") and self.frontage >= self.ranks()

    def unit_strength(self):
        per_rank, _max, per_model = troop_stats(self.model)
        each = self.wounds_each if per_model == "W" else per_model
        strength = self.models * each
        for placed in self.characters:
            if placed.character.current_wounds > 0:
                _pr, _mx, char_each = troop_stats(placed.character)
                strength += placed.character.Wounds if char_each == "W" else char_each
        return strength

    def rank_bonus(self, disrupted):
        if disrupted or self.formation == "skirmish" or not self.combat_order():
            return 0
        per_rank, maximum, _us = troop_stats(self.model)
        if per_rank is None:
            return 0
        if any(_has(m, "Horde") for m in (self.model,)):
            maximum += 1
        full = sum(1 for size in self.rank_sizes()[1:] if size >= per_rank)
        # Griffon Standard: +2 for each extra rank instead of +1.
        return min(full, maximum) * (2 if self.flag("rank_bonus_double") else 1)

    def leadership(self, rank_bonus, hexed_ld=0, inspiring=True):
        """The unit's Leadership: the highest among its models (Warband adds
        its Rank Bonus to Warband models), or a nearby General's. A standard
        may add to it, or make the unit ignore negative modifiers."""
        ignore = self.flag("ignore_negative_ld")
        if ignore:
            hexed_ld = 0
        best = 0
        for model in self.all_models():
            # Black Lotus losses last for the rest of the game.
            value = (model.Leadership or 0) - (0 if ignore else getattr(model, "ld_loss", 0))
            if self.flag("ld_bonus"):
                value = min(10, value + self.flag("ld_bonus"))
            if _has(model, Warband):
                value = min(10, value + rank_bonus)
            best = max(best, value)
        undisciplined = any(_has(self.model, r) for r in ("Undisciplined", "Levies", "Mercenaries"))
        if inspiring and self.setup.inspiring_leadership and not undisciplined:
            best = max(best, self.setup.inspiring_leadership)
        return max(2, best - hexed_ld) if hexed_ld else best

    def has_standard(self):
        """The standard bearer is only lost when it and the champion are the last models."""
        return self.standard and self.models > (1 if self.champion is not None else 0)

    def flag(self, key):
        """A magic standard's effect, while the standard is carried: True/number."""
        if not self.has_standard():
            return False
        found = [e[key] for e in self._banners if e.get(key)]
        if not found:
            return False
        if all(isinstance(v, bool) for v in found):
            return True
        if all(isinstance(v, int) for v in found):
            return sum(found)
        return found[0]

    def amounts(self, key):
        """Every value of a magic standard effect (dice strings kept as they are)."""
        return [e[key] for e in self._banners if e.get(key)] if self.has_standard() else []

    def has_battle_standard(self):
        return any(p.battle_standard for p in self.fighters()) or self.setup.battle_standard_nearby

    def slots(self):
        """Front-rank slot -> occupant: ("char", Placement), "standard",
        "champion", "musician" or "rf"."""
        front = min(self.frontage, self.bodies())
        taken = {}
        for placed in self.fighters():
            slot = placed.slot if placed.slot is not None and 0 <= placed.slot < front else None
            if slot is None or slot in taken:
                slot = _nearest_free(front, taken)
            if slot is not None:
                taken[slot] = ("char", placed)
        command = []
        if self.standard and self.models > (1 if self.champion else 0):
            command.append("standard")
        if self.champion is not None and self.models > 0:
            command.append("champion")
        if self.musician and self.models > (1 if self.champion else 0) + (1 if self.standard else 0):
            command.append("musician")
        for role in command:
            slot = _nearest_free(front, taken)
            if slot is not None:
                taken[slot] = role
        rf_front = front - len(taken)
        for slot in range(front):
            if slot not in taken and rf_front > 0:
                taken[slot] = "rf"
                rf_front -= 1
        return taken

    # -- damage --------------------------------------------------------------

    def lose_wounds(self, amount, killing_blow=False):
        """Rank and file lose `amount` Wounds on one model (no spill-over).
        Returns the Wounds actually lost."""
        if self.models <= 0:
            return 0
        remaining = self.wounds_each - self.damage
        lost = remaining if killing_blow else min(amount, remaining)
        self.damage += lost
        if self.damage >= self.wounds_each:
            self.damage = 0
            self.remove_model()
        return lost

    def remove_model(self):
        """Remove one rank-and-file model (the champion goes last)."""
        self.models -= 1
        if self.champion is not None and self.models <= 0:
            self.champion = None
        if self.models <= 0:
            self.models = 0
            self.champion = None


def _nearest_free(front, taken):
    centre = (front - 1) / 2
    for slot in sorted(range(front), key=lambda s: (abs(s - centre), s)):
        if slot not in taken:
            return slot
    return None


def _champion(model, row):
    champ = copy.copy(model)
    champ.name = f"{row.get('Name') or 'Champion'} ({model.name})"
    for stat in ("WeaponSkill", "Strength", "Toughness", "Initiative", "Attacks", "Leadership", "Wounds"):
        if isinstance(row.get(stat), int):
            setattr(champ, stat, row[stat])
    champ.SpecialRules = list(model.SpecialRules or [])
    champ.original_Strength = champ.Strength
    champ.current_wounds = champ.Wounds
    champ.mount_parts = []
    return champ


def _part(owner, row, count):
    from mounted import MountPart

    rules = [r for r in (owner.SpecialRules or []) if not re.match(r"(Impact Hits|Stomp Attacks)", r)]
    part = MountPart(owner, row.get("Name", "Mount"), dict(row, Attacks=row.get("Attacks")),
                     "Hand Weapon", rules, getattr(owner, "TroopType", None))
    part.Attacks = row.get("Attacks") or 0
    part.count = count
    label = re.sub(r"\s*\(x\d+\)$", "", row.get("Name") or "Mount")
    part.name = f"{label} ({owner.name})"
    return part


# -- geometry ---------------------------------------------------------------------


def _intervals(count, width):
    left = -count * width / 2
    return [(left + i * width, left + (i + 1) * width) for i in range(count)]


def _touching(a, b):
    return a[0] <= b[1] + EPS and a[1] >= b[0] - EPS


def contact(front_count, width, enemy_span):
    """Indices of a line of `front_count` bases of `width` mm that touch an
    enemy edge `enemy_span` mm long (both centred)."""
    edge = (-enemy_span / 2, enemy_span / 2)
    return {i for i, iv in enumerate(_intervals(front_count, width)) if _touching(iv, edge)}


# -- the fight ------------------------------------------------------------------------


class Fight:
    def __init__(self, setup: FightSetup, verbose=False):
        self.setup = setup
        self.units = [Unit(i, s) for i, s in enumerate(setup.sides)]
        self.verbose = verbose
        self.log = []
        self.arc = setup.arc if setup.charger is not None else "front"
        self.turn = 0
        self.charged = [False, False]  # charged during the current turn
        self.charge_distance = [0.0, 0.0]
        self.charged_arc = setup.arc if setup.charger is not None else "front"
        self.first_round = True
        self.challenge = None  # (placed-or-champion A, placed-or-champion B)
        self.caused = [0, 0]
        self.spells_cast_on = [[], []]  # active (spell name, caster side, expires) per unit

    def say(self, text):
        self.log.append(text)
        if self.verbose:
            print(text)

    # -- helpers ------------------------------------------------------------

    def other(self, index):
        return self.units[1 - index]

    def flanked(self, index):
        """Is unit `index` engaged in its flank or rear by the other?"""
        return self.arc in ("flank", "rear") and self.setup.charger == 1 - index

    def disrupted(self, index):
        unit, enemy = self.units[index], self.other(index)
        if self._first_charge_disrupts == index:
            return True
        if not self.flanked(index) or enemy.formation == "skirmish":
            return False
        needed = 10 if troop_key(unit.model) == "heavyinfantry" and unit.formation in ("close", "open") else 5
        return enemy.unit_strength() >= needed

    _first_charge_disrupts = None

    def engaged_span(self, index):
        """Length (mm) of unit `index`'s edge that the enemy is fighting."""
        unit = self.units[index]
        if self.flanked(index) and self.arc == "flank":
            return unit.ranks() * unit.base[1]
        return min(unit.frontage, unit.bodies()) * unit.base[0]

    def fighting_line(self, index):
        """(slots dict, set of slots in base contact) for unit `index`'s fighting rank."""
        unit, enemy = self.units[index], self.other(index)
        if self.flanked(index) and self.arc == "flank":
            # The file on the flank is the fighting rank; it counts as many
            # models as the unit's largest file (Incomplete Ranks).
            depth = unit.ranks()
            touching = contact(depth, unit.base[1], self.enemy_front_width(1 - index))
            slots = {i: "rf" for i in range(depth)}
            for n, placed in enumerate(unit.fighters()):  # characters move to the fight
                if n < depth:
                    slots[n] = ("char", placed)
            return slots, touching
        slots = unit.slots()
        front = len(slots)
        return slots, contact(front, unit.base[0], self.enemy_front_width(1 - index))

    def enemy_front_width(self, index):
        """Width (mm) of the edge unit `index` presents to its enemy."""
        return self.engaged_span(index)

    # -- spells ----------------------------------------------------------------

    def start_turn(self, active):
        import spells as sp

        for unit in self.units:
            unit.restore()
            unit.ld_penalty = 0
            unit.no_inspiring = unit.accursed_mirror = unit.ramparts = False
        for index, unit in enumerate(self.units):
            effects = []
            for names, caster in ((unit.setup.enchantments, index), (unit.setup.hexes, 1 - index)):
                for name in names:
                    if sp.active(name, caster_side=caster, active_side=active, turn=self.turn):
                        # Cast at the start of the caster's turn: this turn, or the last one.
                        cast_turn = self.turn if caster == active else self.turn - 1
                        if caster != index and self._deflected(unit, name, cast_turn):
                            continue
                        effects.append((name, cast_turn))
            unit.active_spells = [name for name, _t in effects]
            # Cry of War: a Death Hag in the enemy unit costs this unit 1 Leadership.
            if any(_has(m, "Cry of War") for m in self.other(index).all_models()):
                unit.ld_penalty += 1
            for name, cast_turn in effects:
                sp.apply(name, unit, self, cast_turn)
            if effects and self.turn <= 2:
                self.say(f"{unit.name} is under {', '.join(unit.active_spells)}")
        for index in (0, 1):
            self.apply_standard(index)
        charger = self.setup.charger
        if self.turn == 1 and charger is not None:
            target = self.units[1 - charger]
            # Earthen Ramparts: charging the unit counts as charging a defended obstacle.
            reason = "the Earthen Ramparts" if target.ramparts else None
            if self.arc == "front" and target.flag("front_charge_disordered"):
                reason = f"{target.name}'s standard"
            if reason and not self.setup.disordered:
                self.setup = copy.copy(self.setup)
                self.setup.disordered = True
                self.say(f"The charge is disordered by {reason}.")

    def _deflected(self, unit, name, cast_turn):
        """Dragon's Eye Banner, Rune Maw: an enemy spell aimed at the unit is
        not cast on a D6 of N+ (there is no other target in a two-unit fight)."""
        need = unit.flag("spell_deflect")
        if not need:
            return False
        key = ("deflect", name, cast_turn)
        if key not in unit.enemy_rolls:
            unit.enemy_rolls[key] = roll_d6() >= need
            if unit.enemy_rolls[key]:
                self.say(f"{unit.name}'s standard turns {name} aside")
        return unit.enemy_rolls[key]

    def charge_counts(self, index):
        """Whether unit `index` counts as having charged for its weapons and
        special rules (the Master Rune of Hesitation can deny it)."""
        return self.charged[index] and not (
            self.arc == "front" and self.setup.charger == index and self.other(index).flag("hesitation"))

    def apply_standard(self, index):
        """What the unit's magic standard does this turn, to it and to the enemy."""
        unit, enemy = self.units[index], self.other(index)
        if not unit.has_standard() or not unit._banners:
            return
        charged = self.charge_counts(index)
        models = list(unit.all_models()) + list(unit.parts)
        for placed in unit.fighters():
            models += list(getattr(placed.character, "mount_parts", []))
        riders = [m for m in models if not hasattr(m, "owner")]
        gains = [r for rules in unit.amounts("rules") for r in rules]
        if charged:
            gains += [r for rules in unit.amounts("charge_rules") for r in rules]
        if self.first_round:
            gains += [r for rules in unit.amounts("first_round_rules") for r in rules]
        for model in models:
            _add(model, gains)
        for model in riders:
            _add(model, [r for rules in unit.amounts("rules_not_mounts") for r in rules])
        if unit.flag("fear_or_terror"):
            for model in models:
                _add(model, ["Terror" if _has(model, "Fear") else "Fear"])
        for stats in unit.amounts("stats"):
            for model in models:
                for stat, change in stats.items():
                    _modify(model, stat, change)
        if charged and unit.flag("charge_strength"):
            for model in models:
                _modify(model, "Strength", unit.flag("charge_strength"))
        # Effects on the enemy; dice are rolled once per fight.
        for stats in unit.amounts("enemy_stats"):
            for stat, change in stats.items():
                key = (stat, str(change))
                if key not in unit.enemy_rolls:
                    unit.enemy_rolls[key] = change if isinstance(change, int) else -roll_amount(change.lstrip("-"))
                for model in list(enemy.all_models()) + list(enemy.parts):
                    _modify(model, stat, unit.enemy_rolls[key])
        for rules in unit.amounts("enemy_rules"):
            for model in list(enemy.all_models()) + list(enemy.parts):
                _add(model, rules)
        if unit.flag("enemy_ld"):
            enemy.ld_penalty += unit.flag("enemy_ld")
        if unit.flag("worse_armour_both"):
            for side in self.units:
                for model in side.all_models():
                    _add(model, [f"Worse Armour ({unit.flag('worse_armour_both')})"])

    # -- a turn ----------------------------------------------------------------

    def play(self):
        s = self.setup
        order = [s.charger if s.charger is not None else 0]
        order.append(1 - order[0])
        if s.charger is not None:
            self.charged[s.charger] = True
            self.charge_distance[s.charger] = s.charge_distance
            self.charged_arc = s.arc
            if _has(self.units[s.charger].model, "First Charge"):
                self._first_charge_disrupts = 1 - s.charger
            self.say(f"{self.units[s.charger].name} charges {self.other(s.charger).name} in the "
                     f"{s.arc} ({s.charge_distance:g}\")" + (" - disordered" if s.disordered else ""))
        while self.turn < s.max_turns:
            active = order[self.turn % 2]
            self.turn += 1
            self.say(f"\n=== Turn {self.turn} ({self.units[active].name}'s turn) ===")
            self.start_turn(active)
            outcome = self.round(active)
            if outcome is not None:
                return outcome
            self.first_round = False
            self._first_charge_disrupts = None
        self.say("\nThe fight is still going when time runs out.")
        return self.result(None, STALEMATE)

    def result(self, winner, outcome):
        return FightResult(winner=winner, outcome=outcome, turns=self.turn,
                           models_left=tuple(u.models for u in self.units),
                           wounds_caused=tuple(self.caused), log=self.log)

    def round(self, active):
        lost = [0, 0]  # Wounds each unit lost this round (for the combat result)
        overkill = [0, 0]
        casualties = [0, 0]  # rank-and-file models removed this round
        self.round_lost, self.round_overkill, self.round_casualties = lost, overkill, casualties
        # Who can fight is decided by the formation at the start of the round;
        # models lost during it come off that (We Can't All Fight).
        self.round_start = [(self.fighting_line(i), self.units[i].rank_sizes()) for i in (0, 1)]

        self.fear_tests()
        self.standard_hits()
        if self.over():
            return self.finish_wiped()
        self.impact_hits()
        if self.over():
            return self.finish_wiped()
        self.challenges(active)
        steps = self.strike_steps()
        for initiative, strikes in steps:
            rolled = []
            for strike in strikes:
                result = strike.roll(self)
                if result:
                    rolled.append(result)
            for apply in rolled:
                apply()
            if self.over():
                return self.finish_wiped()
        self.stomps()
        if self.over():
            return self.finish_wiped()
        return self.resolve(active)

    def over(self):
        return not self.units[0].alive or not self.units[1].alive

    def finish_wiped(self):
        a, b = self.units[0].alive, self.units[1].alive
        if not a and not b:
            self.say("\nBoth units are wiped out.")
            return self.result(None, MUTUAL)
        winner = 0 if a else 1
        self.say(f"\n{self.units[1 - winner].name} is wiped out.")
        return self.result(winner, DESTROYED)

    # -- fear --------------------------------------------------------------------

    def fear_tests(self):
        for index, unit in enumerate(self.units):
            unit.feared = False
            enemy = self.other(index)
            causes = any(_has(enemy.model, r) for r in ("Fear", "Terror"))
            if not causes or enemy.unit_strength() <= unit.unit_strength():
                continue
            if (any(_has(unit.model, r) for r in ("Fear", "Terror", ImmuneToPsychology))
                    or _frenzied(unit.model) or unit.flag("fearless")):
                continue
            ld = unit.leadership(unit.rank_bonus(self.disrupted(index)),
                                 self.hex_ld(unit) + (enemy.flag("enemy_fear_ld") or 0))
            passed, first, second = self._fear_test(unit, enemy, ld)
            if not passed and _has(unit.model, "Veteran"):  # re-roll a failed Leadership test
                passed, first, second = self._fear_test(unit, enemy, ld)
            unit.feared = not passed
            self.say(f"{unit.name} tests against Fear ({first}+{second} vs Ld {ld}): "
                     + ("passed" if passed else "failed, -1 To Hit"))

    def _fear_test(self, unit, enemy, ld):
        dice_ = [roll_d6(), roll_d6()]
        if unit.flag("fear_3d6"):  # Imperial Banner: 3D6, discard the highest
            dice_ = sorted(dice_ + [roll_d6()])[:2]
        if enemy.flag("enemy_fear_extra_die"):  # Screaming Banner: discard the lowest
            dice_ = sorted(dice_ + [roll_d6()])[-2:]
        first, second = dice_
        passed = (first + second <= ld or (first, second) == (1, 1)) and (first, second) != (6, 6)
        return passed, first, second

    def hex_ld(self, unit):
        return getattr(unit, "ld_penalty", 0)

    # -- impact hits ----------------------------------------------------------------

    def impact_hits(self):
        for index, unit in enumerate(self.units):
            if not self.charge_counts(index) or self.charge_distance[index] < 3:
                continue
            enemy = self.other(index)
            slots, touching = self.fighting_line(index)
            total = 0
            sources = []
            amounts = parse_impact_hits(unit.model.SpecialRules)
            if amounts:
                rf_touching = sum(1 for s in touching if slots.get(s) in ("rf", "standard", "champion", "musician"))
                for _ in range(rf_touching):
                    total += sum(roll_amount(a) for a in amounts)
                if rf_touching:
                    sources.append(unit.model)
            for s in touching:
                occupant = slots.get(s)
                if isinstance(occupant, tuple):
                    char = occupant[1].character
                    char_amounts = parse_impact_hits(char.SpecialRules)
                    if char_amounts:
                        total += sum(roll_amount(a) for a in char_amounts)
            if total <= 0:
                continue
            strength = unit.setup.impact_strength or getattr(unit.model, "mount_strength", None) \
                or unit.model.Strength
            ap = parse_impact_hits_ap(unit.model.SpecialRules)
            if troop_key(unit.model) == "heavychariot":
                ap = max(ap, 2)  # Scythed Wheels
            striker = _Striker(unit.model, strength, ap)
            if unit.flag("impact_reroll_wounds"):  # Bull Standard
                striker.SpecialRules.append("Reroll Failed Wounds")
            self.say(f"{unit.name} makes {total} Impact Hits (S{strength}"
                     + (f", AP -{ap}" if ap else "") + ")")
            wounds, flaming, magical = RollToWound(striker, enemy.model, total, verbose=False)
            unsaved = RollArmorSave(striker, enemy.model, wounds, verbose=False)
            self.wound_unit(1 - index, unsaved, flaming, magical, 1, False, strength)

    def standard_hits(self):
        """Hits a magic standard inflicts at the start of the Combat phase (Banner of Change)."""
        for index, unit in enumerate(self.units):
            for dice_, strength, ap in unit.amounts("start_hits"):
                enemy = self.other(index)
                if enemy.models <= 0:
                    continue
                count = roll_amount(dice_)
                striker = _Striker(unit.model, strength, ap)
                striker.SpecialRules = ["Magical Attacks"]
                wounds, flaming, magical = RollToWound(striker, enemy.model, count, verbose=False)
                unsaved = RollArmorSave(striker, enemy.model, wounds, verbose=False)
                self.say(f"{unit.name}'s standard: {count} S{strength} hits -> {len(unsaved)} unsaved")
                self.wound_unit(1 - index, unsaved, flaming, True, 1, False, strength)

    # -- challenges -----------------------------------------------------------------------

    def eligible(self, unit):
        """Characters first, then the champion."""
        found = [p for p in unit.fighters()]
        if unit.champion is not None and unit.models > 0:
            found.append("champion")
        return found

    def challenges(self, active):
        if self.challenge is not None:
            a, b = self.challenge
            if self._participant_alive(0, a) and self._participant_alive(1, b):
                return
            self.challenge = None
        for issuer in (active, 1 - active):
            unit, enemy = self.units[issuer], self.other(issuer)
            if not unit.setup.issue_challenges:
                continue
            mine = self.eligible(unit)
            if not mine:
                continue
            challenger = mine[0]
            theirs = self.eligible(enemy)
            if not theirs:
                self.say(f"{self._label(issuer, challenger)} issues a challenge; nobody can answer it")
                return
            if enemy.setup.accept_challenges or self._cannot_refuse(1 - issuer):
                accepter = theirs[0]
                pair = [None, None]
                pair[issuer], pair[1 - issuer] = challenger, accepter
                self.challenge = tuple(pair)
                self.say(f"{self._label(issuer, challenger)} issues a challenge; "
                         f"{self._label(1 - issuer, accepter)} accepts")
            else:
                hiding = theirs[0]
                if hiding == "champion":
                    self.say(f"The challenge is refused; {enemy.name}'s champion retires")
                    enemy.champion_retired = True
                else:
                    hiding.retired = True
                    self.say(f"The challenge is refused; {hiding.character.name} retires to the rear")
            return

    def _cannot_refuse(self, index):
        unit = self.units[index]
        return unit.bodies() <= 1

    def _participant_alive(self, index, who):
        unit = self.units[index]
        if who == "champion":
            return unit.champion is not None and unit.models > 0
        return who.character.current_wounds > 0

    def _label(self, index, who):
        unit = self.units[index]
        if who == "champion":
            return unit.champion.name if unit.champion else f"the champion ({unit.name})"
        return who.character.name

    def last_models(self, index):
        """With its rank and file gone, a unit's characters are what is left to fight."""
        unit = self.units[index]
        living = [p for p in unit.characters if p.character.current_wounds > 0]
        in_fight = [p for p in living if not p.retired]
        return (in_fight or living)[0].character if living else None

    def in_challenge(self, index, who):
        return self.challenge is not None and self.challenge[index] is who

    # -- strikes ---------------------------------------------------------------------------

    def initiative(self, index, model):
        unit = self.units[index]
        rules = _rules(model)
        first, last = StrikeFirst in rules, StrikeLast in rules
        value = model.Initiative or 0
        if first and not last:
            value = 10
        elif last and not first:
            value = 1
        value = effective_initiative(_Initiative(model, value), self.first_round)
        if self.charged[index] and not self.setup.disordered:
            limit = 4 if self.charged_arc in ("flank", "rear") else 3
            value += min(limit, int(self.charge_distance[index]))
        if (getattr(model, "Weapon", None) == "Thrusting Spear" and self.charged[1 - index]
                and self.charged_arc == "front" and not self.charged[index]):
            value += 1
        del unit
        return max(1, min(10, value))

    def strike_steps(self):
        strikes = []
        for index in (0, 1):
            strikes += self.unit_strikes(index)
        by_init = {}
        for strike in strikes:
            by_init.setdefault(strike.initiative, []).append(strike)
        return sorted(by_init.items(), key=lambda kv: -kv[0])

    def unit_strikes(self, index):
        unit = self.units[index]
        strikes = []
        if unit.models > 0:
            strikes.append(RankStrike(index, unit.model, self.initiative(index, unit.model)))
            for part in unit.parts:
                strikes.append(RankStrike(index, part, self.initiative(index, part), part=True))
            if unit.champion is not None and not getattr(unit, "champion_retired", False):
                strikes.append(ModelStrike(index, "champion", unit.champion,
                                           self.initiative(index, unit.champion)))
        for placed in unit.fighters():
            char = placed.character
            strikes.append(ModelStrike(index, placed, char, self.initiative(index, char)))
            for part in getattr(char, "mount_parts", []):
                strikes.append(ModelStrike(index, placed, part, self.initiative(index, part)))
            for spell in placed.spells:
                strikes.append(SpellStrike(index, placed, spell, self.initiative(index, char)))
        return strikes

    # -- counting attacks ----------------------------------------------------------------

    def rf_attackers(self, index, part=False):
        """(in contact, fighting rank not in contact, press / supporting) models
        of unit `index` still able to attack this round."""
        unit = self.units[index]
        start = getattr(self, "round_start", None)
        if start:
            (slots, touching), sizes = start[index]
        else:
            (slots, touching), sizes = self.fighting_line(index), unit.rank_sizes()
        rf = ("rf", "standard", "musician")
        contact_n = sum(1 for s, o in slots.items() if s in touching and o in rf)
        near_n = sum(1 for s, o in slots.items() if s not in touching and o in rf)
        extra = 0
        front_fight = not (self.flanked(index) or self.arc == "rear" and self.setup.charger == 1 - index)
        behind = 1
        if front_fight and troop_key(unit.model) in _BATTLE_LINE and unit.combat_order() \
                and not self.charge_counts(index) and len(sizes) > 1:
            extra += sizes[1]  # Press of Battle: the fighting rank is two ranks deep
            behind = 2
        support = 0
        if front_fight and len(sizes) > behind and self._can_support(unit.model, self.charge_counts(index)):
            support = sizes[behind]
            # Banner of Lothern: with thrusting spears, half the next rank back too.
            if unit.flag("lothern") and unit.model.Weapon == "Thrusting Spear" and len(sizes) > behind + 1:
                support += math.ceil(sizes[behind + 1] / 2)
        if part:  # a cavalry mount cannot make supporting attacks
            support = 0
            if troop_key(unit.model) in _CAVALRY:
                extra = 0
        # Casualties this round came off the ends of the fighting rank.
        dead = self.round_casualties[index]
        for pool in ("near", "extra", "contact", "support"):
            if dead <= 0:
                break
            if pool == "near":
                taken = min(dead, near_n); near_n -= taken
            elif pool == "extra":
                taken = min(dead, extra); extra -= taken
            elif pool == "contact":
                taken = min(dead, contact_n); contact_n -= taken
            else:
                taken = min(dead, support); support -= taken
            dead -= taken
        return contact_n, near_n, extra + support

    def _can_support(self, model, charged):
        if FIGHT_IN_EXTRA_RANK in (model.SpecialRules or []) or "Fight In Extra Rank" in (model.SpecialRules or []):
            return True
        return model.Weapon in SUPPORT_WEAPONS and not charged

    def attacks_per_model(self, index, model, part=False):
        """A model's attacks this round: Attacks + weapon and rule bonuses."""
        unit = self.units[index]
        extra = 0
        for amount in parse_extra_attacks(model.SpecialRules, get_weapon_special_rules(model.Weapon)):
            extra += roll_amount(amount)
        for rule in map(str, get_weapon_special_rules(model.Weapon)):
            if re.fullmatch(r"\+\d+A", rule):
                extra += int(rule[1:-1])
        charged = self.charge_counts(index)
        # Frenzy: +1 Attack in a turn the unit charged or after a follow up, for
        # the rider, crew or monster - never a steed or a chariot's beasts.
        if (_frenzied(model) and not unit.frenzy_lost and (charged or unit.followed_up)
                and frenzy_bonus_applies(model)):
            extra += 1
        if not part and charged and self.charge_distance[index] >= 3 and _has(model, FuriousCharge):
            extra += 1
        return max(0, (model.Attacks or 0) + extra)

    # -- damage ------------------------------------------------------------------------

    def wound_unit(self, target, unsaved, flaming, magical, multiple, deny_regen, strength):
        """Apply unsaved wounds to unit `target`'s rank and file."""
        unit = self.units[target]
        model = unit.model
        lost_total = 0
        before = unit.models
        mw = 1 if ImmuneToMultipleWounds in (model.SpecialRules or []) else multiple
        regen = parse_regeneration(model.SpecialRules)
        if regen is not None and unit.flag("improve_regen"):  # Drakenhof Banner
            regen = max(2, regen - unit.flag("improve_regen"))
        for wound in unsaved:
            if unit.models <= 0:
                break
            if attempt_ward_save(model, 1, flaming, False, is_killing_blow=wound.killing_blow,
                                 is_multiple_wounds=mw != 1, is_magical=magical, strength=strength):
                continue
            if wound.killing_blow and is_killing_blow_target(model):
                lost_total += unit.lose_wounds(0, killing_blow=True)
                continue
            amount = roll_amount(mw) if not isinstance(mw, int) else mw
            amount = min(amount, unit.wounds_each - unit.damage)
            can_regen = regen is not None and not (
                wound.killing_blow or wound.cleaving_blow or deny_regen or (flaming and _has(model, Flammable)))
            for _ in range(amount):
                lost_total += 1
                if can_regen and roll_d6() >= regen:
                    continue  # recovered, but still counted for the combat result
                unit.lose_wounds(1)
                if unit.models <= 0:
                    break
        self.round_lost[target] += lost_total
        self.caused[1 - target] += lost_total
        removed = before - unit.models
        self.round_casualties[target] += removed
        return lost_total, removed

    def wound_model(self, target, victim, unsaved, flaming, magical, multiple, deny_regen, strength,
                    source=None):
        """Apply unsaved wounds to a single model (a character or champion).
        Returns (Wounds lost, excess for Overkill). A Black Lotus `source`
        costs a character victim 1 Leadership per Wound for the rest of the game."""
        lost = excess = 0
        mw = 1 if ImmuneToMultipleWounds in (victim.SpecialRules or []) else multiple
        regen = parse_regeneration(victim.SpecialRules)
        for wound in unsaved:
            if attempt_ward_save(victim, 1, flaming, False, is_killing_blow=wound.killing_blow,
                                 is_multiple_wounds=mw != 1, is_magical=magical, strength=strength):
                continue
            if victim.current_wounds <= 0:
                excess += roll_amount(mw) if not isinstance(mw, int) else mw
                continue
            if wound.killing_blow and is_killing_blow_target(victim):
                lost += victim.current_wounds
                victim.current_wounds = 0
                continue
            amount = roll_amount(mw) if not isinstance(mw, int) else mw
            can_regen = regen is not None and not (
                wound.killing_blow or wound.cleaving_blow or deny_regen or (flaming and _has(victim, Flammable)))
            for _ in range(amount):
                if victim.current_wounds <= 0:
                    excess += 1
                    continue
                lost += 1
                if can_regen and roll_d6() >= regen:
                    continue
                victim.current_wounds -= 1
        self.round_lost[target] += lost
        self.caused[1 - target] += lost
        if (lost and source is not None and _has(source, "Black Lotus")
                and getattr(source, "owner", None) is None
                and getattr(victim, "UnitCategory", None) in ("Character", "NamedCharacter")):
            victim.ld_loss = getattr(victim, "ld_loss", 0) + lost
            self.say(f"Black Lotus: {victim.name} loses {lost} Leadership")
        return lost, excess

    # -- stomps ---------------------------------------------------------------------------

    def stomps(self):
        rolled = []
        for index, unit in enumerate(self.units):
            enemy = self.other(index)
            if unit.models <= 0:
                continue
            amounts = parse_stomp_attacks(unit.model.SpecialRules)
            if not amounts or enemy.flag("no_stomps_against"):  # Monster Hunter's Tapestry
                continue
            contact_n, _near, _extra = self.rf_attackers(index)
            total = sum(roll_amount(a) for _ in range(contact_n) for a in amounts)
            if total <= 0:
                continue
            ap = 2 if troop_key(unit.model) == "behemoth" and troop_key(enemy.model) not in _MONSTERS else 0
            strength = getattr(unit.model, "mount_strength", None) or unit.model.Strength
            striker = _Striker(unit.model, strength, ap)
            wounds, flaming, magical = RollToWound(striker, enemy.model, total, verbose=False)
            unsaved = RollArmorSave(striker, enemy.model, wounds, verbose=False)
            self.say(f"{unit.name} makes {total} Stomp Attacks: {len(unsaved)} unsaved")
            rolled.append((1 - index, unsaved, flaming, magical, strength))
        for target, unsaved, flaming, magical, strength in rolled:
            self.wound_unit(target, unsaved, flaming, magical, 1, False, strength)

    # -- combat result and break tests -------------------------------------------------

    def score(self, index):
        unit, enemy = self.units[index], self.other(index)
        parts = {"wounds": self.round_lost[1 - index]}
        if self.round_overkill[index]:
            parts["overkill"] = min(5, self.round_overkill[index])
        bonus = unit.rank_bonus(self.disrupted(index))
        if bonus:
            parts["ranks"] = bonus
        if unit.has_standard():
            parts["standard"] = 1
            bonus = sum(roll_amount(a) for a in unit.amounts("cr"))
            if self.charge_counts(index):
                bonus += sum(roll_amount(a) for a in unit.amounts("cr_charge"))
            if unit.flag("cr_once") and not unit.banner_used:
                unit.banner_used = True  # single use: spent in the first round
                bonus += unit.flag("cr_once")
            if bonus:
                parts["magic standard"] = bonus
        if any(p.battle_standard for p in unit.fighters()):
            parts["battle standard"] = 1
        if self.flanked(1 - index) and not (self.arc == "rear" and enemy.flag("no_rear_bonus")):
            parts["flank" if self.arc == "flank" else "rear"] = 1 if self.arc == "flank" else 2
        if unit.setup.high_ground and not enemy.setup.high_ground:
            parts["high ground"] = 1
        if unit.formation == "close" and unit.combat_order() and unit.unit_strength() >= 10:
            parts["close order"] = 1
        if troop_key(unit.model) in _BATTLE_LINE and unit.unit_strength() > enemy.unit_strength():
            parts["massed infantry"] = 1
        return parts

    def resolve(self, active):
        scores = [self.score(0), self.score(1)]
        totals = [sum(s.values()) for s in scores]
        if totals[0] == totals[1]:
            music = [self.units[i].musician and self.units[i].models > 0 for i in (0, 1)]
            if music[0] != music[1]:
                side = 0 if music[0] else 1
                scores[side]["musician"] = 1
                totals[side] += 1
        for i in (0, 1):
            detail = ", ".join(f"{k} {v}" for k, v in scores[i].items()) or "nothing"
            self.say(f"{self.units[i].name}: combat result {totals[i]} ({detail})")
        if totals[0] == totals[1]:
            self.say("The combat is a draw.")
            for unit in self.units:
                unit.followed_up = False
            self.charged = [False, False]
            return None
        winner = 0 if totals[0] > totals[1] else 1
        loser = 1 - winner
        margin = totals[winner] - totals[loser]
        win_unit, lose_unit = self.units[winner], self.units[loser]
        self.say(f"{win_unit.name} wins by {margin}.")
        # Frenzy is lost on losing a round - unless Witchbrew keeps the unit in a frenzy.
        if not (any(_has(m, "Witchbrew") for m in lose_unit.all_models()) or lose_unit.flag("keep_frenzy")):
            lose_unit.frenzy_lost = True

        if _has(lose_unit.model, "Unstable"):
            for _ in range(margin):
                if lose_unit.models <= 0:
                    break
                lose_unit.lose_wounds(1)
            self.say(f"{lose_unit.name} is Unstable and loses {margin} more Wound(s)")
            if not lose_unit.alive:
                return self.result(winner, DESTROYED)

        outcome = self.break_test(loser, winner, margin)
        return self.follow_up(winner, loser, outcome)

    def break_test(self, loser, winner, margin):
        unit, enemy = self.units[loser], self.units[winner]
        if _has(unit.model, "Unbreakable"):
            self.say(f"{unit.name} is Unbreakable and Gives Ground.")
            return GAVE_GROUND
        if _has(unit.model, Stubborn) and not unit.stubborn_used:
            unit.stubborn_used = True
            self.say(f"{unit.name} is Stubborn: it Falls Back in Good Order without testing.")
            return FELL_BACK
        rank_bonus = unit.rank_bonus(self.disrupted(loser))
        ld = unit.leadership(rank_bonus, self.hex_ld(unit), inspiring=not getattr(unit, "no_inspiring", False))
        terror = any(_has(m, "Terror") for m in enemy.all_models())
        immune = any(_has(m, "Terror") for m in unit.all_models())
        if terror and not immune and not unit.flag("ignore_negative_ld"):
            ld -= 1
        first, second = self._break_dice(unit)
        outcome = _break_outcome(first, second, margin, ld)
        text = f"{unit.name} takes a Break test: {first}+{second} (+{margin}) vs Ld {ld}"
        if outcome == FLED and unit.has_battle_standard() and not any(
                _has(unit.model, r) for r in ("Undisciplined", "Levies", "Mercenaries")):
            first, second = self._break_dice(unit)
            outcome = _break_outcome(first, second, margin, ld)
            text += f", re-rolled with the Battle Standard: {first}+{second}"
        if (outcome == FELL_BACK and enemy.unit_strength() > 2 * unit.unit_strength()
                and not unit.flag("steadfast")):
            outcome = FLED
            text += " (outnumbered more than two to one)"
        if (outcome == FELL_BACK and _has(unit.model, "Shieldwall") and not unit.shieldwall_used
                and self.charged[winner] and unit.model.Shield and unit.formation == "close"):
            unit.shieldwall_used = True
            outcome = GAVE_GROUND
            text += " - Shieldwall"
        self.say(f"{text}: {outcome}")
        return outcome

    def _break_dice(self, unit):
        """The two dice of a Break test. The Valorous Standard rolls 3D6 and
        discards the highest; the Cold-Blooded Banner, once, adds a D6 and
        discards the highest."""
        dice_ = [roll_d6(), roll_d6()]
        if unit.flag("break_3d6"):
            dice_.append(roll_d6())
        if unit.flag("cold_blooded") and not unit.cold_blooded_used:
            unit.cold_blooded_used = True
            dice_.append(roll_d6())
        return tuple(sorted(dice_)[:2]) if len(dice_) > 2 else tuple(dice_)

    def _move_roll(self, unit, dice_count, keep=None):
        """Flee or Pursuit dice: re-roll 1s with Da Banner of Da Nomadz; keep
        the highest `keep` dice if given."""
        rolls = [roll_d6() for _ in range(dice_count)]
        if unit.flag("reroll_move_ones"):
            rolls = [roll_d6() if r == 1 else r for r in rolls]
        if keep:
            rolls = sorted(rolls)[-keep:]
        return sum(rolls)

    def _pursuit(self, unit):
        style = unit.flag("pursuit_dice")
        if style == "one":  # Cannibal Totem
            roll = self._move_roll(unit, 1)
        elif style == "extra":  # Jaguar Standard: an extra D6, discard the lowest
            roll = self._move_roll(unit, 3, keep=2)
        else:
            roll = self._move_roll(unit, 2)
        return roll + (roll_d6() if _has(unit.model, "Swiftstride") else 0)

    def follow_up(self, winner, loser, outcome):
        win_unit, lose_unit = self.units[winner], self.units[loser]
        self.charged = [False, False]
        for unit in self.units:
            unit.followed_up = False
        must = _frenzied(win_unit.model) and not win_unit.frenzy_lost
        pursue = win_unit.setup.pursue or must
        if outcome == GAVE_GROUND:
            if not pursue:
                self.say(f"{win_unit.name} holds its ground; the units part.")
                return self.result(winner, GAVE_GROUND)
            win_unit.followed_up = True
            self.say(f"{win_unit.name} follows up.")
            return None
        swift_lose = _has(lose_unit.model, "Swiftstride")
        if outcome == FELL_BACK:  # two dice, keep the highest
            flee = self._move_roll(lose_unit, 2, keep=1) + (roll_d6() if swift_lose else 0)
        else:
            flee = self._move_roll(lose_unit, 2) + (roll_d6() if swift_lose else 0)
        if not pursue:
            self.say(f"{lose_unit.name} withdraws {flee}\"; {win_unit.name} does not pursue.")
            return self.result(winner, outcome)
        chase = self._pursuit(win_unit)
        if chase < flee and win_unit.flag("pursuit_reroll"):
            chase = self._pursuit(win_unit)
        caught = chase >= flee
        self.say(f"{lose_unit.name} retreats {flee}\"; {win_unit.name} pursues {chase}\" - "
                 + ("caught!" if caught else "escapes"))
        if not caught:
            return self.result(winner, outcome)
        if outcome == FLED:
            self.say(f"{lose_unit.name} is run down and destroyed.")
            lose_unit.models = 0
            for placed in lose_unit.characters:
                placed.character.current_wounds = 0
            return self.result(winner, RUN_DOWN)
        # Caught falling back: the combat goes on, the pursuer counting as charging.
        self.charged[winner] = True
        self.charge_distance[winner] = float(chase)
        self.charged_arc = "front"
        self.arc = "front"
        self.setup = _replace_charger(self.setup, winner)
        return None


def _add(model, rules):
    have = list(model.SpecialRules or [])
    model.SpecialRules = have + [r for r in rules if r not in have]


def _modify(model, stat, change):
    value = getattr(model, stat, None)
    if isinstance(value, int):
        setattr(model, stat, max(1, min(10, value + change)))
        if stat == "Strength":
            model.original_Strength = model.Strength


def _replace_charger(setup, charger):
    new = copy.copy(setup)
    new.charger = charger
    new.arc = "front"
    new.disordered = False
    return new


def _break_outcome(first, second, margin, ld):
    natural = first + second
    if (first, second) == (1, 1):
        return GAVE_GROUND
    if natural > ld:
        return FLED
    if natural + margin > ld:
        return FELL_BACK
    return GAVE_GROUND


class _Initiative:
    """Just enough of a model for effective_initiative()."""

    def __init__(self, model, value):
        self.Initiative = value
        self.SpecialRules = model.SpecialRules


class _Striker:
    """Impact Hits and Stomp Attacks: automatic hits at a fixed Strength."""

    _KEEP = ("Magical Attacks", "Magic", "Flaming Attacks")

    def __init__(self, model, strength, ap):
        self.name = model.name
        self.Strength = strength
        self.original_Strength = strength
        self.SpecialRules = [r for r in (model.SpecialRules or []) if r in self._KEEP]
        self.Weapon = None
        self.ArmourPiercing = ap
        self.TroopType = getattr(model, "TroopType", None)


# -- strikes ------------------------------------------------------------------------------


class _Strike:
    def __init__(self, index, initiative):
        self.index = index
        self.initiative = initiative


def _weapon_for_turn(model, charged):
    """A lance can only be used in a turn its wielder charged; otherwise the
    model fights with its hand weapon."""
    if model.Weapon in CHARGE_ONLY_WEAPONS and not charged:
        return "Hand Weapon"
    return model.Weapon


def _roll_attacks(fight, index, attacker, target, attacks, charged):
    """Roll `attacks` attacks; returns (unsaved wounds, flaming, magical,
    multiple wounds, deny regeneration, strength, natural ones)."""
    weapon = attacker.Weapon
    attacker.Weapon = _weapon_for_turn(attacker, charged)
    added = []
    if fight.units[index].feared:
        added.append("To Hit (-1)")
    if charged and attacker.Weapon == "Halberd":
        added.append("Improve Armour Piercing (1)")  # AP -2 against enemies it charged
    if charged and attacker.Weapon in ("Flail", "Morning Star"):
        added.append("AB1")  # Armour Bane (1) against enemies it charged
    attacker.SpecialRules = list(attacker.SpecialRules or []) + added
    try:
        apply_weapon_stats(attacker, is_first_round=charged, verbose=False)
        details = {}
        hits = RollToHit(attacker, target, verbose=False, is_first_round=fight.first_round,
                         details=details, attacks=attacks)
        rules = _rules(attacker)
        poisoned = details.get("natural_sixes", 0) if PoisonedAttacks in rules else 0
        wounds, flaming, magical = RollToWound(attacker, target, hits, verbose=False,
                                               is_first_round=charged, poisoned_hits=poisoned)
        unsaved = RollArmorSave(attacker, target, wounds, verbose=False)
        strength = attacker.Strength
        multiple = parse_multiple_wounds(get_weapon_special_rules(attacker.Weapon), attacker.SpecialRules)
        deny = NoRegeneration in get_weapon_special_rules(attacker.Weapon)
    finally:
        reset_weapon_stats(attacker)
        attacker.Weapon = weapon
        for rule in added:
            attacker.SpecialRules.remove(rule)
    return hits, unsaved, flaming, magical, multiple, deny, strength, details.get("natural_ones", 0)


class RankStrike(_Strike):
    """The rank and file (or their mounts / beasts) of a unit."""

    def __init__(self, index, model, initiative, part=False):
        super().__init__(index, initiative)
        self.model = model
        self.part = part

    def roll(self, fight):
        unit = fight.units[self.index]
        if unit.models <= 0:
            return None
        contact_n, near_n, extra_n = fight.rf_attackers(self.index, part=self.part)
        per = fight.attacks_per_model(self.index, self.model, part=self.part)
        if self.part:
            per *= getattr(self.model, "count", 1)
            attacks = contact_n * per
        else:
            per *= fight.units[self.index].setup.crew
            attacks = contact_n * per + near_n + extra_n
        if attacks <= 0:
            return None
        enemy_index = 1 - self.index
        enemy = fight.units[enemy_index]
        target = enemy.model if enemy.models > 0 else fight.last_models(enemy_index)
        if target is None:
            return None
        hits, unsaved, flaming, magical, multiple, deny, strength, ones = _roll_attacks(
            fight, self.index, self.model, target, attacks, fight.charge_counts(self.index))
        label = self.model.name if self.part else unit.name
        fight.say(f"{label}: {attacks} attacks (I{self.initiative}) -> {hits} hits -> {len(unsaved)} unsaved")
        mirror = getattr(unit, "accursed_mirror", False) and ones

        def apply():
            _hit(fight, enemy_index, target, unsaved, flaming, magical, multiple, deny, strength)
            if mirror:
                _mirror_hits(fight, self.index, ones)
        return apply


class ModelStrike(_Strike):
    """A character, a champion or a character's mount."""

    def __init__(self, index, who, model, initiative):
        super().__init__(index, initiative)
        self.who = who
        self.model = model

    def roll(self, fight):
        unit = fight.units[self.index]
        owner = self.who
        if owner == "champion":
            if unit.champion is None or unit.models <= 0:
                return None
        elif owner.character.current_wounds <= 0:
            return None
        enemy_index = 1 - self.index
        enemy = fight.units[enemy_index]
        attacks = fight.attacks_per_model(self.index, self.model, part=hasattr(self.model, "owner"))
        foe = None
        if fight.challenge is not None and fight.challenge[self.index] is owner:
            foe = fight.challenge[enemy_index]
        if foe is not None:
            target = enemy.champion if foe == "champion" else foe.character
            if target is None or target.current_wounds <= 0:
                return None
        else:
            target = enemy.model if enemy.models > 0 else fight.last_models(enemy_index)
            if target is None:
                return None
            if not self._in_contact(fight):
                attacks = min(attacks, 1)  # in the fighting rank but not in base contact
        if attacks <= 0:
            return None
        hits, unsaved, flaming, magical, multiple, deny, strength, _ones = _roll_attacks(
            fight, self.index, self.model, target, attacks, fight.charge_counts(self.index))
        fight.say(f"{self.model.name}: {attacks} attacks (I{self.initiative}) -> {hits} hits -> "
                  f"{len(unsaved)} unsaved" + (f" against {target.name}" if foe is not None else ""))

        def apply():
            if foe is None:
                _hit(fight, enemy_index, target, unsaved, flaming, magical, multiple, deny, strength)
                return
            _lost, excess = fight.wound_model(enemy_index, target, unsaved, flaming, magical,
                                              multiple, deny, strength, source=self.model)
            if target.current_wounds <= 0:
                fight.round_overkill[self.index] += excess
                fight.say(f"{target.name} is slain" + (f" (Overkill {excess})" if excess else ""))
                if foe == "champion":
                    enemy.champion = None
                    enemy.remove_model()
                    fight.round_casualties[enemy_index] += 1
        return apply

    def _in_contact(self, fight):
        if self.who == "champion":
            return True
        slots, touching = fight.fighting_line(self.index)
        for slot, occupant in slots.items():
            if isinstance(occupant, tuple) and occupant[1] is self.who:
                return slot in touching
        return True


class SpellStrike(_Strike):
    """A Wizard casting an Assailment spell at its Initiative."""

    def __init__(self, index, placed, spell, initiative):
        super().__init__(index, initiative)
        self.placed = placed
        self.spell = spell

    def roll(self, fight):
        import spells as sp

        if self.placed.character.current_wounds <= 0:
            return None
        return sp.cast_assailment(fight, self.index, self.placed, self.spell)


def _hit(fight, index, target, unsaved, flaming, magical, multiple, deny, strength):
    """Wounds on the rank and file, or on a character once they are all gone."""
    unit = fight.units[index]
    if target is unit.model and unit.models > 0:
        fight.wound_unit(index, unsaved, flaming, magical, multiple, deny, strength)
    elif target is not unit.model:
        fight.wound_model(index, target, unsaved, flaming, magical, multiple, deny, strength)


def _mirror_hits(fight, index, count):
    """Accursed Mirror: each natural 1 To Hit becomes a S3 AP -1 hit on the unit itself."""
    unit = fight.units[index]
    striker = _Striker(unit.model, 3, 1)
    wounds, flaming, magical = RollToWound(striker, unit.model, count, verbose=False)
    unsaved = RollArmorSave(striker, unit.model, wounds, verbose=False)
    fight.say(f"Accursed Mirror: {count} hit(s) rebound on {unit.name}")
    fight.wound_unit(index, unsaved, flaming, magical, 1, False, 3)


def fight(setup: FightSetup, verbose=False) -> FightResult:
    return Fight(setup, verbose=verbose).play()
