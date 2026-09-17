"""The combat engine: rolling dice for a duel between two Characters.

The resolution order for a single strike is:

    apply_weapon_stats -> RollToHit -> RollToWound -> RollArmorSave
        -> resolve_strike (ward / regeneration / killing blow / wounds)

`Character.Wounds` is the profile maximum and is never modified here.
All damage is applied to `Character.current_wounds`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from types import SimpleNamespace

from armor import NO_ARMOUR, UNARMOURED_SAVE, ArmourDict, get_armour_save
from character_model import Character
from charts import WeaponSkillChart, Wounds_vs_ToughnessChart
from dice import MISFIRE, roll_amount, roll_artillery, roll_d6
from elven_honors import ElvenHonors
from faction_profiles import RACE_NAMES, FactionProfiles
from magic_items import MagicItemDict
from special_rules import (
    AccursedWeapons,
    BeguilingPresence,
    FirstRoundInitiative,
    RerollHitsVsHigherWS,
    ArmourCannotBeImproved,
    ArmourCannotBeModified,
    ArtilleryStrength,
    CannotBeWoundedOn2,
    EnemyRerollsArmourSaves,
    EnemyRerollsHits,
    EnemyRerollsWounds,
    ImmuneToMultipleWounds,
    NoArmourSaves,
    PoisonedAttacks,
    RerollFailedHits,
    RerollFailedWounds,
    RerollWounds1,
    BloodRage,
    Choppas,
    CleavingBlow,
    ElvenReflexes,
    EnsorcelledWeapons,
    Ethereal,
    FirstRoundOnly,
    FirstRoundStr,
    FlamingAttacks,
    Flammable,
    ForceRerollOneHit,
    Frenzy,
    FuriousCharge,
    GrailVow,
    GromrilArmour,
    MarkOfKhorne,
    MarkOfNurgle,
    MarkOfSlaanesh,
    MarkOfTzeentch,
    GromrilWeapons,
    Hatred,
    ImmuneToKillingBlow,
    IthilmarWeapons,
    Khopesh,
    Magic,
    MagicalAttacks,
    MonsterSlayer,
    Murderous,
    NoRegeneration,
    ObsidianBlades,
    PrimalFury,
    RerollArmourSaves1,
    RerollHits1,
    StrikeFirst,
    StrikeLast,
    WarpstoneWeapons,
    WoundStealing,
    parse_armour_bane,
    parse_armour_bonus,
    parse_armour_piercing_bonus,
    parse_extra_attacks,
    parse_impact_hits,
    parse_impact_hits_ap,
    parse_stomp_attacks,
    parse_enemy_to_hit_modifier,
    parse_fixed_strength,
    parse_killing_blow,
    parse_multiple_wounds,
    parse_regeneration,
    parse_to_hit_modifier,
    parse_ward,
    parse_wounds_on,
)
from weapons import MeleeWeaponDict, get_weapon_special_rules, get_weapon_stats

# The charts are 10x10; clamp lookups so an over-buffed stat cannot index off
# the end of the table.
_CHART_MAX = 10

# Maximum Armour Value: infantry and cavalry can never have an armour value
# better than 2+; chariots, monsters and war machines never better than 3+.
BEST_POSSIBLE_ARMOUR_SAVE = 2
BEST_LARGE_MODEL_ARMOUR_SAVE = 3
_LARGE_TROOP_TYPES = ("chariot", "monster", "monstrouscreature", "behemoth", "warmachine")


def best_armour_save(character: Character) -> int:
    """The best armour value this model's troop type allows."""
    troop = str(getattr(character, "TroopType", "") or "").lower().replace(" ", "")
    if any(kind in troop for kind in _LARGE_TROOP_TYPES):
        return BEST_LARGE_MODEL_ARMOUR_SAVE
    return BEST_POSSIBLE_ARMOUR_SAVE


# A natural 1 To Hit always fails and a natural 6 always hits in combat,
# whatever the modifiers.
_BEST_TO_HIT, _WORST_TO_HIT = 2, 6


def _clamp(value: int | None, low: int = 1, high: int = _CHART_MAX) -> int:
    return max(low, min(high, value or low))


@dataclass
class Wound:
    """A single wound that got past the to-wound roll."""

    roll: int
    killing_blow: bool = False
    # A Cleaving Blow: no armour or Regeneration save, but not slain outright.
    cleaving_blow: bool = False


@dataclass
class StrikeResult:
    """Everything one character's attacks produced in one round."""

    attacks: int = 0
    hits: int = 0
    raw_wounds: int = 0
    saves: int = 0
    unsaved: list[Wound] = field(default_factory=list)
    is_flaming: bool = False
    is_magical: bool = False
    multiple_wounds: int | str = 1  # a dice value such as "D3" is rolled per wound
    denies_regeneration: bool = False
    strength: int | None = None  # the attack's Strength, for Strength-limited wards
    self_wounds: int = 0

    @property
    def wounds(self) -> int:
        """Wounds that got past armour, before wards and regeneration."""
        return len(self.unsaved)


# ---------------------------------------------------------------------------
# Attack characteristics
# ---------------------------------------------------------------------------


def apply_extra_attacks(character: Character, is_first_round: bool = False) -> int:
    """Total attacks for the round: base profile plus weapon and rule bonuses.

    Special Rules Handled:
        - "+XA" weapon rule: adds X attacks (e.g. Two Hand Weapons)
        - Frenzy: +1 attack
        - Furious Charge: +1 attack on the charge round only
        - Extra Attacks (+X) on the model or weapon; a dice value is rolled
          each time this is called, so call it once per round
    """
    extra = 0
    for amount in parse_extra_attacks(
        character.SpecialRules, get_weapon_special_rules(character.Weapon)
    ):
        extra += roll_amount(amount)
    for rule in get_weapon_special_rules(character.Weapon):
        rule = str(rule)
        if rule.startswith("+") and rule.endswith("A"):
            try:
                extra += int(rule[1:-1])
            except ValueError:
                pass
    rules = character.SpecialRules or []
    # The Mark of Khorne gives its bearer the Frenzy special rule.
    frenzied = Frenzy in rules or MarkOfKhorne in rules
    if frenzied:
        extra += 1
    if is_first_round and FuriousCharge in rules:
        extra += 1
    # Blood Rage can make a Beastman Frenzied part-way through a fight.
    if getattr(character, "blood_rage_frenzied", False) and not frenzied:
        extra += 1
    return (character.Attacks or 0) + extra


def apply_weapon_stats(
    character: Character, is_first_round: bool = False, verbose: bool = True
) -> None:
    """Apply the equipped weapon's temporary Strength and AP modifiers.

    Weapons flagged FirstRoundOnly (lances, cavalry spears) or
    FirstRoundStr (flails, morning stars) only contribute on the charge round,
    as does the Orc Choppas rule. Call reset_weapon_stats afterwards to revert.
    """
    strength_bonus, ap_bonus, weapon_rules = _weapon_stats_or_default(character.Weapon)

    first_round_gated = FirstRoundOnly in weapon_rules
    strength_gated = first_round_gated or FirstRoundStr in weapon_rules

    fixed = parse_fixed_strength(weapon_rules)
    if fixed is not None:
        character.Strength = fixed  # the weapon's own Strength replaces the wielder's
    elif strength_bonus is not None and (is_first_round or not strength_gated):
        character.Strength = (character.Strength or 0) + strength_bonus
    # Weapon AP is stored as a magnitude; RollArmorSave adds it to the save target.
    if ap_bonus and (is_first_round or not first_round_gated):
        character.ArmourPiercing = (character.ArmourPiercing or 0) + abs(ap_bonus)

    # Ensorcelled, Gromril, Warpstone Weapons, Khopesh and Obsidian Blades each
    # give a plain hand weapon AP -1.
    if has_ensorcelled_hand_weapon(character) or has_gromril_hand_weapon(character):
        character.ArmourPiercing = (character.ArmourPiercing or 0) + 1

    # Rules that improve the AP of every weapon the model uses (Gouge-tusks).
    character.ArmourPiercing = (character.ArmourPiercing or 0) + parse_armour_piercing_bonus(
        character.SpecialRules
    )

    # Choppas improves the weapon's AP by 1 on the charge round, but does
    # nothing for a magic weapon.
    if (
        is_first_round
        and Choppas in (character.SpecialRules or [])
        and Magic not in weapon_rules
    ):
        character.ArmourPiercing = (character.ArmourPiercing or 0) + 1


def reset_weapon_stats(character: Character) -> None:
    """Undo apply_weapon_stats, restoring the character's own characteristics."""
    character.Strength = getattr(character, "original_Strength", character.Strength)
    character.ArmourPiercing = getattr(character, "original_ArmourPiercing", 0)
    character.Weapon = getattr(character, "original_Weapon", character.Weapon)


# Hand weapon names, for rules that only apply to a plain hand weapon.
_HAND_WEAPONS = ("HW", "Hand Weapon", "HandWeapon")


# Killing Blow only affects models whose troop type is infantry or cavalry.
# A custom character with no troop type is treated as infantry, that being the
# common case for a hand-built fighter.
def is_killing_blow_target(character: Character) -> bool:
    """Whether Killing Blow can slay this model outright."""
    if ImmuneToKillingBlow in (character.SpecialRules or []):
        return False
    troop_type = getattr(character, "TroopType", None)
    if not troop_type:
        return True
    troop_type = str(troop_type).lower()
    return "infantry" in troop_type or "cavalry" in troop_type


# Troop types a Cleaving Blow affects, and those that count as monsters.
_CLEAVABLE = ("regularinfantry", "heavyinfantry", "lightcavalry", "heavycavalry", "warbeast")
_MONSTERS = ("behemoth", "monstrouscreature", "monster")


def _troop_type(character: Character) -> str:
    return str(getattr(character, "TroopType", "") or "").replace(" ", "").lower()


def is_monster(character: Character) -> bool:
    return _troop_type(character) in _MONSTERS


def is_cleaving_blow_target(character: Character) -> bool:
    # A custom fighter with no troop type counts as infantry, as for Killing Blow.
    troop_type = _troop_type(character)
    return not troop_type or troop_type in _CLEAVABLE


def _upgrades_plain_hand_weapon(character: Character, *rules: str) -> bool:
    """Whether a hand-weapon-only rule applies to what this model is wielding.

    These rules (Ensorcelled Weapons, Gromril Weapons and their equivalents)
    only work with a single ordinary hand weapon: not two hand weapons, not
    another weapon type, and not a hand weapon that is already magical or runed.
    The model needs any one of `rules`.
    """
    if not any(rule in (character.SpecialRules or []) for rule in rules):
        return False
    if character.Weapon not in _HAND_WEAPONS:
        return False
    return Magic not in get_weapon_special_rules(character.Weapon)


def has_ensorcelled_hand_weapon(character: Character) -> bool:
    """A plain hand weapon gets Magical Attacks and AP -1.

    Ensorcelled Weapons (Warriors of Chaos), Warpstone Weapons (Skaven) and
    Accursed Weapons (Vampire Counts).
    """
    return _upgrades_plain_hand_weapon(
        character, EnsorcelledWeapons, WarpstoneWeapons, AccursedWeapons
    )


def has_gromril_hand_weapon(character: Character) -> bool:
    """A plain hand weapon gets AP -1 (no magic).

    Gromril Weapons (Dwarfs), Khopesh (Tomb Kings) and Obsidian Blades
    (Lizardmen) all read the same.
    """
    return _upgrades_plain_hand_weapon(character, GromrilWeapons, Khopesh, ObsidianBlades)


def has_murderous_hand_weapon(character: Character) -> bool:
    """Murderous: reroll to-wound rolls of 1 with a plain hand weapon."""
    return _upgrades_plain_hand_weapon(character, Murderous)


def _weapon_stats_or_default(weapon):
    """Weapon stats, tolerating weapons that have no melee profile (e.g. bows)."""
    try:
        return get_weapon_stats(weapon)
    except ValueError:
        return (None, 0, [])


# ---------------------------------------------------------------------------
# The dice rolls
# ---------------------------------------------------------------------------


def RollToHit(
    attacker: Character,
    defender: Character,
    verbose: bool = True,
    is_first_round: bool = False,
    details: dict | None = None,
    attacks: int | None = None,
) -> int:
    """Roll to hit, comparing the two Weapon Skills. Returns the number of hits.

    If `details` is given, details["natural_sixes"] is set to how many of the
    hits were a natural 6 (for Poisoned Attacks). `attacks` is the number of
    attacks if already worked out this round (dice-based extra attacks must
    only be rolled once).

    Special Rules Handled:
        - Ithilmar Weapons: reroll hit rolls of 1 when using a Hand Weapon
        - Reroll Hits 1: reroll hit rolls of 1 with any weapon
        - Reroll Failed Hits: reroll any failed hit
        - Hatred(X): reroll failed hits in the first round against a hated foe
        - Primal Fury: reroll hit rolls of 1 once its Leadership test is passed
        - To Hit (+N) on the attacker, Enemy To Hit (-N) on the defender;
          a natural 1 always misses and a natural 6 always hits
        - Force Reroll of One Successful Hit (on the defender, e.g. Mathlann's
          Ire): the first hit scored against them each round is rerolled once
        - Enemy Rerolls Successful Hits (on the defender): every hit is rerolled
    """
    chart_target = WeaponSkillChart[_clamp(attacker.WeaponSkill) - 1][
        _clamp(defender.WeaponSkill) - 1
    ]
    rules = attacker.SpecialRules or []
    attacker_weapon_rules = get_weapon_special_rules(attacker.Weapon)
    modifier = parse_to_hit_modifier(rules, attacker_weapon_rules) + (
        parse_enemy_to_hit_modifier(defender.SpecialRules)
    )
    to_hit_target = max(_BEST_TO_HIT, min(_WORST_TO_HIT, chart_target - modifier))

    # Beguile / Allure of Slaanesh: fail a Leadership test and only 6s hit.
    if BeguilingPresence in (defender.SpecialRules or []):
        first, second = roll_d6(), roll_d6()
        if first + second > (attacker.Leadership or 0):
            to_hit_target = _WORST_TO_HIT
            if verbose:
                print(f"{attacker.name} is beguiled ({first}+{second} vs Ld"
                      f"{attacker.Leadership}) and hits only on a 6")

    can_reroll_1 = (
        RerollHits1 in rules
        or getattr(attacker, "primal_fury_active", False)
        or (
            IthilmarWeapons in rules
            and attacker.Weapon in ("HW", "Hand Weapon", "HandWeapon")
        )
    )
    hated = is_first_round and _is_hated_enemy(rules, defender)
    reroll_misses = (
        hated
        or RerollFailedHits in rules
        or RerollFailedHits in attacker_weapon_rules
        or (RerollHitsVsHigherWS in rules
            and (defender.WeaponSkill or 0) > (attacker.WeaponSkill or 0))
    )

    # A defender may force one successful hit per round, or every one, to be rerolled.
    defender_rules = list(defender.SpecialRules or []) + list(
        get_weapon_special_rules(defender.Weapon)
    )
    forced_reroll_available = ForceRerollOneHit in defender_rules
    reroll_every_hit = EnemyRerollsHits in defender_rules
    # Mark of Nurgle: enemies re-roll any To Hit roll of a natural 6 against it.
    reroll_sixes = MarkOfNurgle in defender_rules

    if attacks is None:
        attacks = apply_extra_attacks(attacker, is_first_round=is_first_round)
    hits = natural_sixes = 0
    for _ in range(attacks):
        roll = _hit_roll(can_reroll_1, verbose)
        if roll == 6 and reroll_sixes:
            roll = roll_d6()
            if verbose:
                print(f"{defender.name}'s Mark of Nurgle forces a 6 to be rerolled -> {roll}")
        if roll >= to_hit_target and (forced_reroll_available or reroll_every_hit):
            forced_reroll_available = False
            roll = _hit_roll(can_reroll_1, verbose)
            if verbose:
                print(
                    f"{defender.name} forces the successful hit to be rerolled "
                    f"-> {roll}"
                )
        if roll >= to_hit_target:
            hits += 1
            natural_sixes += roll == 6
            if verbose:
                print(f"Hit roll: {roll} vs target {to_hit_target}+ - Hit!")
            continue

        if reroll_misses:
            roll = _hit_roll(can_reroll_1, verbose)
            if verbose:
                reason = "Hatred" if hated else "Reroll"
                print(f"{reason}: rerolling the failed hit -> {roll}")
            if roll >= to_hit_target:
                hits += 1
                natural_sixes += roll == 6
                if verbose:
                    print(f"{reason} reroll: {roll} vs target {to_hit_target}+ - Hit!")
                continue

        if verbose:
            print(f"Hit roll: {roll} vs target {to_hit_target}+ - Miss!")
    if details is not None:
        details["natural_sixes"] = natural_sixes
    return hits


def test_primal_fury(character: Character, verbose: bool = True) -> tuple[bool, bool]:
    """Roll the Primal Fury Leadership test. Returns (furious, frenzied).

    Per the rule, the test is taken when this model's combat is chosen. Passing
    it lets the model reroll To Hit rolls of a natural 1 for the rest of the
    Combat phase. Blood Rage adds: a pass on a natural double also makes the
    model Frenzied.
    """
    rules = character.SpecialRules or []
    if PrimalFury not in rules:
        return False, False

    first, second = roll_d6(), roll_d6()
    total = first + second
    passed = total <= (character.Leadership or 0)
    frenzied = passed and BloodRage in rules and first == second
    if verbose:
        outcome = "passed" if passed else "failed"
        print(
            f"Primal Fury: {character.name} rolls {first}+{second}={total} vs "
            f"Ld{character.Leadership} - {outcome}"
            + (" and works itself into a Frenzy!" if frenzied else "")
        )
    return passed, frenzied


def _hit_roll(can_reroll_1: bool, verbose: bool) -> int:
    roll = roll_d6()
    if roll == 1 and can_reroll_1:
        roll = roll_d6()
        if verbose:
            print(f"Rerolling a hit roll of 1 -> {roll}")
    return roll


# Rule text names races in the plural ("Hatred (Dwarfs)") while profiles name
# them in the singular (Race: "Dwarf"), so both are reduced to a stem first.
_IRREGULAR_PLURALS = {
    "elves": "elf",
    "dwarves": "dwarf",
    "wolves": "wolf",
    "men": "man",
}


def _stem(word: str) -> str:
    word = word.strip().lower()
    if word in _IRREGULAR_PLURALS:
        return _IRREGULAR_PLURALS[word]
    # "beastmen" -> "beastman", "marauders" -> "marauder".
    if word.endswith("men") and len(word) > 3:
        return word[:-3] + "man"
    return word[:-1] if word.endswith("s") and len(word) > 3 else word


# Words that carry no identifying weight in a Hatred target.
_HATRED_STOPWORDS = {"of", "the", "and", "models", "model", "&"}


def _significant_stems(text: str) -> set:
    return {_stem(w) for w in text.split()} - _HATRED_STOPWORDS


def _names_match(target: str, candidate: str) -> bool:
    """Whether a rule's target names the same thing as a Race or model name.

    A target may list several foes - "Orcs & Goblins", or "Warriors of Chaos,
    Beastmen Brayherds & Daemonic models" - so it is split into alternatives
    first. An alternative matches only if *every* significant word in it is
    present, which is what keeps "Hatred (High Elves)" off a Dark Elf.
    """
    if not target or not candidate:
        return False
    if target in candidate:
        return True

    candidate_stems = _significant_stems(candidate)
    if not candidate_stems:
        return False

    for alternative in re.split(r"[,&]|\band\b", target):
        wanted = _significant_stems(alternative)
        if not wanted:
            continue
        # Either the target fully describes the candidate ("Orcs" vs an Orc), or
        # the candidate is one part of a longer army name ("Beastmen Brayherds"
        # vs a Beastman). Both directions are a match; a partial overlap in
        # neither direction is not, which is what excludes a Dark Elf from
        # "Hatred (High Elves)".
        if wanted <= candidate_stems or candidate_stems <= wanted:
            return True
    return False


def _is_hated_enemy(rules, defender: Character) -> bool:
    """Whether any Hatred(X) rule on the attacker applies to this defender."""
    for rule in rules:
        rule = str(rule)
        if not rule.lower().startswith(Hatred.lower()):
            continue
        if "(" not in rule or ")" not in rule:
            continue  # bare "Hatred" with no target
        target = rule[rule.find("(") + 1 : rule.find(")")].strip().lower()
        if target.startswith("all"):  # "all", "all enemies"
            return True
        race = (getattr(defender, "Race", "") or "").lower()
        name = (getattr(defender, "name", "") or "").lower()
        if _names_match(target, race) or _names_match(target, name):
            return True
    return False


def RollToWound(
    attacker: Character,
    defender: Character,
    num_hits: int,
    verbose: bool = True,
    is_first_round: bool = False,
    poisoned_hits: int = 0,
) -> tuple[list[Wound], bool, bool]:
    """Roll to wound, comparing Strength against Toughness.

    Returns (wounds, is_flaming, is_magical). Each Wound records its natural
    roll (for Armour Bane and Killing Blow) and what it triggered.

    `poisoned_hits` is how many of the hits were natural 6s from a model with
    Poisoned Attacks; each of those rolls To Wound with a +2 modifier (a
    natural 1 still fails). Rules keyed to "a natural 6" use the unmodified roll.

    Special Rules Handled:
        - Ethereal: only magical attacks can wound
        - Ensorcelled Weapons: a plain hand weapon counts as magical
        - Killing Blow (from the character or the weapon)
        - Choppas: reroll to-wound rolls of 1 on the charge round
        - Murderous: reroll to-wound rolls of 1 with a plain hand weapon
        - Killing Blow only applies to infantry and cavalry targets
        - Magic / Flaming: tracked for ward save interactions
        - Poisoned Attacks: +2 To Wound for a natural 6 To Hit
        - Wounds On (N+): a roll of N+ always wounds, whatever the Toughness
        - Cannot Be Wounded On 2 (defender): a roll of 2 never wounds
        - Reroll Failed Wounds; Enemy Rerolls Successful Wounds (defender)
    """
    weapon_rules = get_weapon_special_rules(attacker.Weapon)
    attacker_rules = attacker.SpecialRules or []

    is_magical = (
        Magic in attacker_rules
        or MagicalAttacks in attacker_rules
        or Magic in weapon_rules
        or MagicalAttacks in weapon_rules
        or has_ensorcelled_hand_weapon(attacker)
        or GrailVow in attacker_rules
    )
    is_flaming = (
        FlamingAttacks in attacker_rules
        or FlamingAttacks in weapon_rules
        or MarkOfTzeentch in attacker_rules
    )

    if Ethereal in (defender.SpecialRules or []) and not is_magical:
        if verbose:
            print(
                f"{defender.name} is Ethereal and can only be wounded by "
                "magical attacks!"
            )
        return [], is_flaming, is_magical

    to_wound_target = Wounds_vs_ToughnessChart[_clamp(attacker.Strength) - 1][
        _clamp(defender.Toughness) - 1
    ]
    always_wounds_on = parse_wounds_on(attacker_rules, weapon_rules)
    if always_wounds_on is not None:
        to_wound_target = min(to_wound_target or 7, always_wounds_on)
    defender_rules = defender.SpecialRules or []
    if to_wound_target is not None and CannotBeWoundedOn2 in defender_rules:
        to_wound_target = max(to_wound_target, 3)
    if to_wound_target is None:
        if verbose:
            print(f"{attacker.name} is too weak to wound {defender.name}!")
        return [], is_flaming, is_magical

    killing_blow_target = parse_killing_blow(attacker_rules, weapon_rules)
    if not is_killing_blow_target(defender):
        # Against anything but infantry or cavalry - or a model immune to it -
        # a Killing Blow is just an ordinary wound.
        killing_blow_target = None
    all_rules = list(attacker_rules) + list(weapon_rules)
    if MonsterSlayer in all_rules and is_monster(defender):
        # A Monster Slaying Blow is a Killing Blow against a monster.
        killing_blow_target = 6 if killing_blow_target is None else killing_blow_target
    cleaves = CleavingBlow in all_rules and is_cleaving_blow_target(defender)
    armour_bane = parse_armour_bane(weapon_rules, attacker_rules)

    # Choppas lets an Orc reroll to-wound rolls of a natural 1 when it charged,
    # but only with a non-magical weapon.
    reroll_wound_1s = (
        (is_first_round and Choppas in attacker_rules and Magic not in weapon_rules)
        or has_murderous_hand_weapon(attacker)
        or RerollWounds1 in attacker_rules
        or RerollWounds1 in weapon_rules
    )

    reroll_failed = RerollFailedWounds in attacker_rules or RerollFailedWounds in weapon_rules
    reroll_successes = EnemyRerollsWounds in defender_rules
    # Poisoned Attacks does not work with a magic weapon.
    if Magic in weapon_rules or MagicalAttacks in weapon_rules:
        poisoned_hits = 0

    def succeeds(natural, bonus):
        return natural != 1 and natural + bonus >= to_wound_target

    wounds = []
    for index in range(num_hits):
        bonus = 2 if index < poisoned_hits else 0
        roll = roll_d6()
        if roll == 1 and reroll_wound_1s:
            roll = roll_d6()
            if verbose:
                print(f"Rerolling a to-wound roll of 1 -> {roll}")
        if not succeeds(roll, bonus) and reroll_failed:
            roll = roll_d6()
            if verbose:
                print(f"Rerolling a failed to-wound roll -> {roll}")
        elif succeeds(roll, bonus) and reroll_successes:
            roll = roll_d6()
            if verbose:
                print(f"{defender.name} forces the wound to be rerolled -> {roll}")
        if not succeeds(roll, bonus):
            if verbose:
                shown = f"{roll}+{bonus}" if bonus else f"{roll}"
                print(f"Wound roll: {shown} vs target {to_wound_target}+ - Failed!")
            continue

        is_killing_blow = killing_blow_target is not None and roll >= killing_blow_target
        is_cleaving = cleaves and roll == 6 and not is_killing_blow
        wounds.append(Wound(roll=roll, killing_blow=is_killing_blow, cleaving_blow=is_cleaving))
        if verbose:
            notes = ""
            if is_killing_blow:
                notes += " (Killing Blow!)"
            if is_cleaving:
                notes += " (Cleaving Blow!)"
            if roll == 6 and armour_bane:
                notes += f" (Armour Bane {armour_bane}!)"
            print(f"Wound roll: {roll} vs target {to_wound_target}+ - Wounded!{notes}")
    return wounds, is_flaming, is_magical


def RollArmorSave(
    attacker: Character, defender: Character, wounds: list[Wound], verbose: bool = True
) -> list[Wound]:
    """Roll armour saves. Returns the wounds that were NOT saved.

    Special Rules Handled:
        - Armour Bane (ABX): extra armour piercing on a wound roll of 6
        - AHX / Improve Armor 1 in Combat: improve the save
        - Gromril Armour / Reroll Armour Saves 1: reroll armour saves of a natural 1
        - Killing Blow: permits no armour save
        - Shield: improves the save by 1
        - No Armour Saves (attacker or weapon): permits no armour save
        - Maximum Armour Value: 2+ for infantry and cavalry, 3+ for chariots,
          monsters and war machines
        - Armour Cannot Be Improved / Armour Cannot Be Modified (defender)
    """
    attacker_rules = list(attacker.SpecialRules or []) + list(
        get_weapon_special_rules(attacker.Weapon)
    )
    if NoArmourSaves in attacker_rules:
        if verbose and wounds:
            print(f"No armour save is permitted against {attacker.name}'s attacks")
        return list(wounds)
    defender_rules = defender.SpecialRules or []
    fixed = ArmourCannotBeModified in defender_rules
    unimprovable = fixed or ArmourCannotBeImproved in defender_rules
    base_save = get_armour_save(defender.Armor)
    if base_save is None:
        if defender.Armor not in NO_ARMOUR:
            if verbose:
                print(f"{defender.name} has unknown armor type: {defender.Armor}")
            return list(wounds)
        # An unarmoured model has an armour value of 7+ for the purposes of
        # rules that improve it, so a shield or Armoured Hide gives it a 6+.
        base_save = UNARMOURED_SAVE

    save_target = base_save
    if not unimprovable:
        if defender.Shield:
            save_target -= 1
        save_target -= parse_armour_bonus(defender.SpecialRules)
    if save_target > 6:
        return list(wounds)  # no armour, and nothing improving it

    rerolls_armour_ones = any(
        rule in (defender.SpecialRules or [])
        for rule in (GromrilArmour, RerollArmourSaves1)
    )
    reroll_saves = EnemyRerollsArmourSaves in attacker_rules
    armour_piercing = 0 if fixed else abs(attacker.ArmourPiercing or 0)
    armour_bane = 0 if fixed else parse_armour_bane(
        get_weapon_special_rules(attacker.Weapon), attacker.SpecialRules
    )
    best_save = best_armour_save(defender)

    unsaved = []
    for index, wound in enumerate(wounds, start=1):
        # A Killing Blow or a Cleaving Blow permits no Armour save at all.
        if wound.killing_blow or wound.cleaving_blow:
            if verbose:
                print(f"Armor save {index}: no save against a Killing or Cleaving Blow")
            unsaved.append(wound)
            continue
        current = save_target + armour_piercing
        if wound.roll == 6 and armour_bane:
            current += armour_bane
        current = max(best_save, current)

        if current > 6:
            if verbose:
                print(f"Armor save {index}: no save possible ({current}+ needed)")
            unsaved.append(wound)
            continue

        roll = roll_d6()
        if roll == 1 and rerolls_armour_ones:
            roll = roll_d6()
            if verbose:
                print(f"Rerolling an armour save of 1 -> {roll}")
        if roll >= current and reroll_saves:
            roll = roll_d6()
            if verbose:
                print(f"{attacker.name} forces the armour save to be rerolled -> {roll}")
        if roll >= current:
            if verbose:
                print(f"Armor save {index}: {roll} vs {current}+ - Saved!")
        else:
            if verbose:
                print(f"Armor save {index}: {roll} vs {current}+ - Failed!")
            unsaved.append(wound)
    return unsaved


def attempt_ward_save(
    defender: Character,
    num_wounds: int,
    is_flaming: bool = False,
    verbose: bool = False,
    is_killing_blow: bool = False,
    is_multiple_wounds: bool = False,
    is_magical: bool = False,
    strength: int | None = None,
) -> int:
    """Roll ward saves against `num_wounds`. Returns the number saved.

    Ward sources (best target wins): WardX, Chaos Armour, Witness to Destiny,
    Dragon Armour, and conditional wards such as Blessings of Asuryan (Flaming
    only), the Armour of Skaldour (Killing Blow or Multiple Wounds only) or the
    Daemonic 5+ (non-magical attacks only), so the kind of wound being saved
    against has to be passed in.
    """
    ward_target = parse_ward(
        defender.SpecialRules,
        is_flaming,
        is_killing_blow=is_killing_blow,
        is_multiple_wounds=is_multiple_wounds,
        is_magical=is_magical,
        strength=strength,
    )
    if ward_target is None or num_wounds <= 0:
        return 0

    if verbose:
        print(f"Attempting ward saves: {ward_target}+ required")

    saved = 0
    for _ in range(num_wounds):
        roll = roll_d6()
        if roll >= ward_target:
            saved += 1
            defender.ward_applied = True
            if verbose:
                print(f"Ward save: {roll} vs {ward_target}+ - Saved!")
        elif verbose:
            print(f"Ward save: {roll} vs {ward_target}+ - Failed!")
    return saved


def attempt_regeneration_save(
    defender: Character, num_wounds: int, verbose: bool = True
) -> int:
    """Roll regeneration saves against `num_wounds`. Returns the number saved."""
    regen_target = parse_regeneration(defender.SpecialRules)
    if regen_target is None or num_wounds <= 0:
        return 0

    if verbose:
        print(f"Attempting regeneration saves: {regen_target}+ required")

    saved = 0
    for _ in range(num_wounds):
        roll = roll_d6()
        if roll >= regen_target:
            saved += 1
            if verbose:
                print(f"Regeneration: {roll} vs {regen_target}+ - Regenerated!")
        elif verbose:
            print(f"Regeneration: {roll} vs {regen_target}+ - Failed!")
    return saved


# ---------------------------------------------------------------------------
# Resolving a strike
# ---------------------------------------------------------------------------


def OneRoundMeleeCombat(
    attacker: Character,
    defender: Character,
    verbose: bool = True,
    is_first_round: bool = True,
) -> StrikeResult:
    """Roll one character's attacks for one round. Applies no damage.

    Damage is left to resolve_strike so that simultaneous combat can roll both
    sides before either takes a wound.
    """
    furious, frenzied = test_primal_fury(attacker, verbose=verbose)
    attacker.primal_fury_active = furious
    if frenzied:
        attacker.blood_rage_frenzied = True

    apply_weapon_stats(attacker, is_first_round=is_first_round, verbose=verbose)
    weapon_rules = get_weapon_special_rules(attacker.Weapon)

    # A weapon whose Strength is rolled on an Artillery dice, such as Burlok
    # Damminson's Furnace Hammer. A Misfire costs its wielder a Wound and all
    # of its attacks.
    if ArtilleryStrength in weapon_rules:
        rolled = roll_artillery()
        if rolled == MISFIRE:
            if verbose:
                print(f"{attacker.name}'s weapon misfires! No attacks, and a Wound lost.")
            reset_weapon_stats(attacker)
            return StrikeResult(self_wounds=1)
        attacker.Strength = rolled
        if verbose:
            print(f"Artillery dice: {attacker.name} strikes at Strength {rolled}")

    try:
        attacks = apply_extra_attacks(attacker, is_first_round=is_first_round)
        details = {}
        hits = RollToHit(
            attacker, defender, verbose=verbose, is_first_round=is_first_round,
            details=details, attacks=attacks,
        )
        poisoned = (
            details["natural_sixes"]
            if PoisonedAttacks in (attacker.SpecialRules or []) or PoisonedAttacks in weapon_rules
            else 0
        )
        wounds, is_flaming, is_magical = RollToWound(
            attacker, defender, hits, verbose=verbose, is_first_round=is_first_round,
            poisoned_hits=poisoned,
        )
        unsaved = RollArmorSave(attacker, defender, wounds, verbose=verbose)
        strength = attacker.Strength
    finally:
        reset_weapon_stats(attacker)

    return StrikeResult(
        attacks=attacks,
        hits=hits,
        raw_wounds=len(wounds),
        saves=len(wounds) - len(unsaved),
        unsaved=unsaved,
        is_flaming=is_flaming,
        is_magical=is_magical,
        multiple_wounds=parse_multiple_wounds(weapon_rules, attacker.SpecialRules),
        denies_regeneration=NoRegeneration in weapon_rules,
        strength=strength,
    )


# Rules an Impact Hit or Stomp Attack keeps: "any attack made or hits caused"
# by the model. Weapon rules and to-hit or to-wound rules do not apply.
_HIT_RULES = (Magic, MagicalAttacks, FlamingAttacks, MarkOfTzeentch, GrailVow)


def AutomaticHits(
    attacker: Character,
    defender: Character,
    amounts,
    verbose: bool = True,
    kind: str = "Impact Hits",
    armour_piercing: int = 0,
    strength: int | None = None,
) -> StrikeResult:
    """Roll automatic hits (Impact Hits, Stomp Attacks). Applies no damage.

    They hit automatically and use the model's unmodified Strength - its own,
    with no weapon modifier - so only rules about the model's hits in general
    (Magical Attacks, Flaming Attacks) carry over.
    """
    count = sum(roll_amount(amount) for amount in amounts)
    if count <= 0:
        return StrikeResult()
    striker = SimpleNamespace(
        name=attacker.name,
        Strength=strength if strength is not None else getattr(
            attacker, "original_Strength", attacker.Strength),
        SpecialRules=[r for r in (attacker.SpecialRules or []) if r in _HIT_RULES],
        Weapon=None,
        ArmourPiercing=armour_piercing,
    )
    if verbose:
        ap = f", AP -{armour_piercing}" if armour_piercing else ""
        print(f"\n{attacker.name} makes {count} {kind} (S{striker.Strength}{ap})!")
    wounds, is_flaming, is_magical = RollToWound(striker, defender, count, verbose=verbose)
    unsaved = RollArmorSave(striker, defender, wounds, verbose=verbose)
    return StrikeResult(
        attacks=count, hits=count, raw_wounds=len(wounds),
        saves=len(wounds) - len(unsaved), unsaved=unsaved,
        is_flaming=is_flaming, is_magical=is_magical, strength=striker.Strength,
    )


def _thunderstomp_ap(attacker: Character, defender: Character) -> int:
    """A behemoth's Stomp Attacks have AP -2, except against another monster."""
    if "behemoth" in _troop_type(attacker) and not is_monster(defender):
        return 2
    return 0


def resolve_strike(
    defender: Character, result: StrikeResult, verbose: bool = True
) -> tuple[int, bool]:
    """Apply one StrikeResult to the defender. Returns (wounds_taken, slain).

    This is the single place where wards, regeneration, Killing Blow and
    Multiple Wounds are resolved, so sequential and simultaneous combat behave
    identically.

    Per The Old World, a Killing Blow permits a Ward save but no Armour or
    Regeneration save, and slays an infantry or cavalry model outright. An
    ordinary wound may be warded, then regenerated; whatever survives costs the
    defender the attack's Multiple Wounds value, normally 1.
    """
    wounds_taken = 0
    slain = False
    multiplier = result.multiple_wounds
    if isinstance(multiplier, int):
        multiplier = max(1, multiplier)
    is_multiple_wounds = multiplier != 1
    if is_multiple_wounds and ImmuneToMultipleWounds in (defender.SpecialRules or []):
        multiplier = 1

    for wound in result.unsaved:
        warded = attempt_ward_save(
            defender,
            1,
            result.is_flaming,
            verbose,
            is_killing_blow=wound.killing_blow,
            is_multiple_wounds=is_multiple_wounds,
            is_magical=result.is_magical,
            strength=result.strength,
        )
        if warded:
            if verbose and wound.killing_blow:
                print(f"{defender.name} wards off the Killing Blow!")
            continue

        # A Killing Blow allows no Regeneration save, and neither does a
        # Flaming attack against a Flammable model.
        can_regenerate = not (
            wound.killing_blow
            or wound.cleaving_blow
            or result.denies_regeneration
            or (result.is_flaming and Flammable in (defender.SpecialRules or []))
        )
        if can_regenerate and attempt_regeneration_save(defender, 1, verbose):
            continue

        if wound.killing_blow:
            if verbose:
                print(f"Killing Blow strikes {defender.name} down!")
            slain = True
            break
        lost = roll_amount(multiplier)
        if verbose and not isinstance(multiplier, int):
            print(f"Multiple Wounds ({multiplier}): {lost} wound(s)")
        wounds_taken += lost

    if slain:
        defender.current_wounds = 0
    elif wounds_taken:
        defender.current_wounds = max(0, defender.current_wounds - wounds_taken)

    if verbose and (wounds_taken or slain):
        print(
            f"{defender.name} suffers {wounds_taken} wound(s). "
            f"Remaining: {defender.current_wounds}/{defender.Wounds}"
        )
    return wounds_taken, slain


# ---------------------------------------------------------------------------
# Strike order
# ---------------------------------------------------------------------------

# Lower sorts earlier. Strike First always precedes normal, which always
# precedes Strike Last; Initiative only breaks ties within the same band.
_STRIKE_FIRST, _STRIKE_NORMAL, _STRIKE_LAST = 0, 1, 2


def _strike_band(character: Character) -> int:
    # Strike First/Last can come from the fighter or from the weapon - a Great
    # Weapon carries Strike Last, which is not copied onto the character.
    rules = list(character.SpecialRules or []) + list(
        get_weapon_special_rules(character.Weapon)
    )
    first = StrikeFirst in rules
    last = StrikeLast in rules
    if first and last:
        return _STRIKE_NORMAL  # the two cancel out
    if first:
        return _STRIKE_FIRST
    if last:
        return _STRIKE_LAST
    return _STRIKE_NORMAL


def effective_initiative(character: Character, is_first_round: bool = False) -> int:
    """Initiative for this round, after rules that modify it.

    Special Rules Handled:
        - Elven Reflexes: +1 Initiative (to a maximum of 10) in the first round
        - Mark of Slaanesh: +1 Initiative in the first round of any combat
    """
    initiative = character.Initiative or 0
    rules = character.SpecialRules or []
    if is_first_round:
        for rule in (ElvenReflexes, MarkOfSlaanesh, FirstRoundInitiative):
            if rule in rules:
                initiative = min(10, initiative + 1)
    return initiative


def determine_strike_order(
    character_1: Character,
    character_2: Character,
    verbose: bool = True,
    is_first_round: bool = False,
) -> list[list[tuple[Character, Character]]]:
    """Group the two fighters - and their mounts - into strike steps.

    Returns a list of steps; each step is a list of (attacker, defender) pairs
    that strike together. Two steps means one fighter strikes before the other,
    one step means they strike simultaneously. A mount strikes at its own
    Initiative and always attacks the other fighter (Challenges & Mounts).
    """
    if getattr(character_1, "mount_parts", None) or getattr(character_2, "mount_parts", None):
        return _strike_steps_with_mounts(character_1, character_2, verbose, is_first_round)

    key_1 = (_strike_band(character_1), -effective_initiative(character_1, is_first_round))
    key_2 = (_strike_band(character_2), -effective_initiative(character_2, is_first_round))

    if key_1 == key_2:
        if verbose:
            print(
                f"{character_1.name} and {character_2.name} strike "
                "simultaneously."
            )
        return [[(character_1, character_2), (character_2, character_1)]]

    first, second = (
        (character_1, character_2) if key_1 < key_2 else (character_2, character_1)
    )
    if verbose:
        print(f"{first.name} strikes before {second.name}.")
    return [[(first, second)], [(second, first)]]


def _strike_steps_with_mounts(character_1, character_2, verbose, is_first_round):
    attackers = []
    for model, enemy in ((character_1, character_2), (character_2, character_1)):
        for striker in [model] + list(getattr(model, "mount_parts", [])):
            key = (_strike_band(striker), -effective_initiative(striker, is_first_round))
            attackers.append((key, striker, enemy))
    steps = []
    for key in sorted({k for k, _s, _e in attackers}):
        steps.append([(s, e) for k, s, e in attackers if k == key])
    if verbose:
        order = " / ".join(" + ".join(s.name for s, _e in step) for step in steps)
        print(f"Strike order: {order}")
    return steps


# ---------------------------------------------------------------------------
# The duel
# ---------------------------------------------------------------------------


def combat_simulation(
    character_1: Character,
    character_2: Character,
    rounds: int = 2,
    Shooting: bool = False,
    verbose: bool = True,
) -> Character | None:
    """Fight a duel between two characters. Returns the winner, or None on a draw.

    Each round: in the first (the charge) round, Impact Hits land before any
    blow; then the strike steps, in strike order; then Stomp Attacks, which
    come after every other attack. Each step is rolled in full before any of
    it is applied, and the duel stops as soon as a fighter is down. If both
    survive all rounds, whoever has more wounds remaining wins.

    The engine does not track who charged: like Furious Charge and lances,
    Impact Hits count both fighters as charging in the first round.
    """
    if Shooting:
        raise NotImplementedError("Shooting is not implemented yet")

    fighters = (character_1, character_2)
    character_1.current_wounds = character_1.Wounds
    character_2.current_wounds = character_2.Wounds

    for round_number in range(1, rounds + 1):
        is_first_round = round_number == 1
        if verbose:
            print(f"\n=== Round {round_number} ===")

        if is_first_round:
            impacts = [
                hit for a, d in ((character_1, character_2), (character_2, character_1))
                if (hit := _automatic_hits(a, d, parse_impact_hits, "Impact Hits", verbose,
                                           parse_impact_hits_ap(a.SpecialRules)))
            ]
            if impacts:
                _apply_step(impacts, verbose, heal=False)
                over, winner = _fallen(fighters, verbose)
                if over:
                    return winner

        for step in determine_strike_order(
            character_1, character_2, verbose, is_first_round=is_first_round
        ):
            # Roll every strike in this step before applying any of it, so that
            # simultaneous fighters both get to swing.
            rolled = []
            for attacker, defender in step:
                if verbose:
                    print(f"\n{attacker.name} strikes at {defender.name}!")
                rolled.append(
                    (
                        attacker,
                        defender,
                        OneRoundMeleeCombat(
                            attacker,
                            defender,
                            verbose=verbose,
                            is_first_round=is_first_round,
                        ),
                    )
                )
            _apply_step(rolled, verbose)
            over, winner = _fallen(fighters, verbose)
            if over:
                return winner

        stomps = [
            hit for a, d in ((character_1, character_2), (character_2, character_1))
            if (hit := _automatic_hits(a, d, parse_stomp_attacks, "Stomp Attacks", verbose,
                                       _thunderstomp_ap(a, d)))
        ]
        if stomps:
            _apply_step(stomps, verbose, heal=False)
            over, winner = _fallen(fighters, verbose)
            if over:
                return winner

    if character_1.current_wounds > character_2.current_wounds:
        return _declare(character_1, character_2, verbose)
    if character_2.current_wounds > character_1.current_wounds:
        return _declare(character_2, character_1, verbose)

    if verbose:
        print("\nThe battle ends in a bloody stalemate.")
    return None


def _apply_step(rolled, verbose, heal=True):
    """Apply a step's rolled results: all damage first, then any healing.

    Treating simultaneous fighters alike, whichever was passed first: a Wound
    Stealing model can win back Wounds it lost in this same step, and one
    reduced to 0 is slain rather than healed.
    """
    inflicted_by = []
    for attacker, defender, result in rolled:
        if result.self_wounds:
            attacker.current_wounds = max(0, attacker.current_wounds - result.self_wounds)
        inflicted, _ = resolve_strike(defender, result, verbose=verbose)
        inflicted_by.append((attacker, inflicted))
    if heal:
        for attacker, inflicted in inflicted_by:
            if attacker.current_wounds > 0:
                recover_wounds(attacker, inflicted, verbose=verbose)


def _automatic_hits(model, enemy, parse, kind, verbose, armour_piercing):
    """Impact Hits or Stomp Attacks for a model, at its mount's Strength if it has one."""
    amounts = parse(model.SpecialRules)
    if not amounts:
        return None
    return (model, enemy, AutomaticHits(model, enemy, amounts, verbose, kind, armour_piercing,
                                        strength=getattr(model, "mount_strength", None)))


def _fallen(fighters, verbose):
    """(duel over, winner or None) after a step."""
    down = [c for c in fighters if c.current_wounds <= 0]
    if not down:
        return False, None
    if len(down) == 2:
        if verbose:
            print("\nBoth fighters fall together.")
        return True, None
    winner = fighters[1] if down[0] is fighters[0] else fighters[0]
    return True, _declare(winner, down[0], verbose)


def recover_wounds(character: Character, wounds_inflicted: int, verbose: bool = True) -> int:
    """Heal a Wound Stealing model for each unsaved Wound it inflicted.

    Never takes the model above its profile Wounds. Returns the number healed.
    """
    if wounds_inflicted <= 0:
        return 0
    rules = list(character.SpecialRules or []) + list(
        get_weapon_special_rules(character.Weapon)
    )
    if WoundStealing not in rules:
        return 0

    missing = (character.Wounds or 0) - character.current_wounds
    healed = min(wounds_inflicted, max(0, missing))
    if healed:
        character.current_wounds += healed
        if verbose:
            print(
                f"{character.name} drains {healed} Wound(s) back. "
                f"Remaining: {character.current_wounds}/{character.Wounds}"
            )
    return healed


def _declare(winner: Character, loser: Character, verbose: bool) -> Character:
    if verbose:
        print(
            f"\n{winner.name} stands victorious, the blood of {loser.name} "
            "stains the field of battle"
        )
    return winner
