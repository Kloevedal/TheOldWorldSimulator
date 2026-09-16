from __future__ import annotations

# Special Rule Names
FirstRoundStr = "1st round strength only"
FirstRoundOnly = "First Round Only"
StrikeFirst = "Strike First"
StrikeLast = "Strike Last"
Evasive = "Evasive"
IgnoresCover = "Ignores Cover"
ImmuneToPsychology = "Immune to Psychology"
FuriousCharge = "Furious Charge"
MoveThroughCover = "Move Through Cover"
Stubborn = "Stubborn"
RallyingCry = "Rallying Cry"
RerollHits1 = "Reroll Hits 1"
FlamingAttacks = "Flaming Attacks"
Magic = "Magic"
Ethereal = "Ethereal"
Frenzy = "Frenzy"
Hatred = "Hatred"
RequiresTwoHands = "Requires Two Hands"
KillingBlow = "Killing Blow"
KillingBlow6 = "Killing Blow 6+"


# Orc & Goblin Special Rules
Choppas = "Choppas"
DaBoyz = "Da Boyz"
IgnorePanic = "Ignore Panic"
IgnoreGoblinPanic = "Ignore Goblin Panic"
Impetuous = "Impetuous"
QuellImpetuosity = "Quell Impetuosity"
Waaagh = "Waaagh!"
Warband = "Warband"
Warpaint = "Warpaint"
Animosity = "Animosity"

# Derived Special Rules
ImproveArmor1InCombat = "Improve Armor 1 in Combat"
ImproveArmor2InShooting = "Improve Armor 2 in Shooting"
Flammable = "Flammable"
# For each unsaved Wound this model inflicts, it recovers a lost Wound.
WoundStealing = "Wound Stealing"
# Re-roll Armour Save rolls of a natural 1 (the Dawnstone; Gromril Armour does
# the same under its own name).
RerollArmourSaves1 = "Reroll Armour Saves 1"
# Enemies must re-roll a single successful To Hit roll made against this model
# in each round of combat.
ForceRerollOneHit = "Force Reroll of One Successful Hit"


# High Elf Specific Special Rules
IthilmarWeapons = "Ithilmar Weapons"
ValourOfAges = "Valour of Ages"
ArrowsOfIsha = "Arrows of Isha"
IthilmarArmour = "Ithilmar Armour"
MightyConstitution = "Mighty Constitution" ### improves str by one if moved and nullifies poison attacks 
CommandingVoice = "Commanding Voice"
NavalDiscipline = "Naval Discipline"
PrecisionStrikes = "Precision Strikes"
BlessingsofAsuryan = "Blessings of Asuryan (5+ Ward vs Flaming)"
WitnesstoDestiny = "Witness to Destiny (6+ Ward)"
DragonArmour = "Dragon Armour (6+ Ward)"
ElvenReflexes = "Elven Reflexes"
LileathsBlessing = "Lileath's Blessing"
LoreOfSaphery = "Lore of Saphery"
AccomplishedArchers = "Accomplished Archers"
LionCloak = "Lion Cloak"

# Dwarfen Mountain Holds
GromrilArmour = "Gromril Armour"
GromrilWeapons = "Gromril Weapons"
AncestralGrudge = "Ancestral Grudge"
Resolute = "Resolute"

# Dark Elves
Murderous = "Murderous"

# Hand-weapon rules from the later army lists. Each gives a single, ordinary
# hand weapon AP -1, exactly like Gromril Weapons; Warpstone Weapons also makes
# its attacks magical, like Ensorcelled Weapons.
Khopesh = "Khopesh"  # Tomb Kings of Khemri
ObsidianBlades = "Obsidian Blades"  # Lizardmen
WarpstoneWeapons = "Warpstone Weapons"  # Skaven

# Beastmen Brayherds
PrimalFury = "Primal Fury"
BloodRage = "Blood Rage"
EternalHatred = "Eternal Hatred"

# Warriors of Chaos
EnsorcelledWeapons = "Ensorcelled Weapons"
MagicalAttacks = "Magical Attacks"
# A model that cannot be slain outright by Killing Blow; it takes one Wound.
ImmuneToKillingBlow = "Immune to Killing Blow"
# The weapon's Strength is rolled on an Artillery dice before it attacks.
ArtilleryStrength = "Artillery Dice Strength"

# Daemons of Chaos. Daemonic is a bundle: a 5+ Ward against non-magical attacks
# plus a set of universal rules, so it is expanded into its parts on a profile.
Daemonic = "Daemonic"
DaemonicWard = "Ward5 (non-magical)"
InfernalFavour = "Infernal Favour"  # reduces Daemonic Instability, not a Ward
BlackshardArmour = "Ward5 (Flaming)"  # Chaos Dwarf armour, a Flaming-only Ward
GazeOfTheGods = "Gaze of the Gods"
MarkOfChaosUndivided = "Mark of Chaos Undivided"
MarkOfKhorne = "Mark of Khorne"
MarkOfNurgle = "Mark of Nurgle"
MarkOfSlaanesh = "Mark of Slaanesh"
MarkOfTzeentch = "Mark of Tzeentch"
MARKS_OF_CHAOS = [
    MarkOfChaosUndivided,
    MarkOfKhorne,
    MarkOfNurgle,
    MarkOfSlaanesh,
    MarkOfTzeentch,
]



# ---------------------------------------------------------------------------
# Rule parsing helpers
#
# Special rules are stored as plain strings on characters and weapons. These
# helpers turn those strings into numbers the combat engine can use, so that
# parsing lives in one place instead of being re-derived at each call site.
# ---------------------------------------------------------------------------

import re


def _as_list(rules):
    """Normalise a rules field (None / str / list) into a list of strings."""
    if not rules:
        return []
    if isinstance(rules, str):
        return [rules]
    return [str(r) for r in rules]


def parse_armour_bane(*rule_sources) -> int:
    """Highest Armour Bane value across the given rule lists ("AB1" -> 1).

    Accepts "AB1" and "Armour Bane (1)". A qualified rule such as
    "Armour Bane (1, Chompa only)" deliberately does not match, because the
    qualifier means it belongs to something the engine is not simulating.

    Armour Bane increases the attack's armour piercing on a to-wound roll of 6.
    """
    best = 0
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = re.fullmatch(
                r"(?:AB|Armou?r\s*Bane)\s*\(?(\d+)\)?", rule.strip(), re.IGNORECASE
            )
            if match:
                best = max(best, int(match.group(1)))
    return best


def parse_killing_blow(*rule_sources) -> int | None:
    """Lowest Killing Blow threshold across the given rule lists, or None.

    Accepts "Killing Blow", "KillingBlow", "Killing Blow 6+" and "KillingBlow5".
    A bare Killing Blow defaults to 6+.
    """
    best = None
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = re.fullmatch(
                r"Killing\s*Blow\s*(\d+)?\+?", rule.strip(), re.IGNORECASE
            )
            if match:
                threshold = int(match.group(1)) if match.group(1) else 6
                best = threshold if best is None else min(best, threshold)
    return best


def parse_armour_bonus(*rule_sources) -> int:
    """Total improvement to an armour save from rules ("AH1" -> 1).

    Also counts Improve Armor 1 in Combat, which is worth a flat +1.
    """
    bonus = 0
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = re.fullmatch(
                r"(?:AH|Armou?red\s*Hide)\s*\(?(\d+)\)?", rule.strip(), re.IGNORECASE
            )
            if match:
                bonus += int(match.group(1))
            elif rule == ImproveArmor1InCombat:
                bonus += 1
    return bonus


def parse_regeneration(*rule_sources) -> int | None:
    """Best (lowest) Regeneration target across the given rule lists ("Regen5" -> 5)."""
    best = None
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = re.fullmatch(r"Regen(?:eration)?\s*\(?(\d+)\+?\)?", rule.strip())
            if match:
                target = int(match.group(1))
                best = target if best is None else min(best, target)
    return best


# Named ward sources -> (target, flaming_only). Keyed on the rule name with any
# trailing "(6+ Ward)" gloss removed, so both the bare name used by the army
# lists and the annotated constants above resolve to the same entry.
_NAMED_WARDS = {
    "witness to destiny": (6, False),
    "dragon armour": (6, False),
    "dragon armor": (6, False),
    "blessings of asuryan": (5, True),
}


def _base_name(rule: str) -> str:
    """Rule name with any parenthetical gloss stripped, lowercased."""
    return re.sub(r"\s*\(.*?\)\s*", " ", rule).strip().lower()


# Conditions a Ward save can be limited to, as written inside its brackets.
_WARD_CONDITIONS = ("flaming", "killing blow", "multiple wounds", "non-magical")


_DICE_AMOUNT = re.compile(r"(\d+)?D(3|6)(?:\s*\+\s*(\d+))?", re.IGNORECASE)


def _amount_value(text):
    """'2' -> 2, 'D3' -> 'D3', 'D3+1' -> 'D3+1'; None if unreadable."""
    text = text.strip()
    if text.isdigit():
        return int(text)
    if _DICE_AMOUNT.fullmatch(text):
        return text.upper().replace(" ", "")
    return None


def parse_multiple_wounds(*rule_sources):
    """Multiple Wounds value across the given rule lists, else 1.

    "Multiple Wounds (2)" means each unsaved Wound costs the target 2 Wounds.
    A dice value such as "Multiple Wounds (D3)" is returned as the string
    "D3", to be rolled per wound with `dice.roll_amount`. A fixed value beats a
    dice value only if it is higher than the dice value's average.
    """
    best = 1
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = re.fullmatch(
                r"Multiple\s*Wounds\s*\(?([^)]*?)\)?", rule.strip(), re.IGNORECASE
            )
            if not match:
                continue
            value = _amount_value(match.group(1))
            if value is not None and _average(value) > _average(best):
                best = value
    return best


def _average(amount):
    if isinstance(amount, int):
        return amount
    match = _DICE_AMOUNT.fullmatch(amount)
    count = int(match.group(1) or 1)
    sides = int(match.group(2))
    return count * (sides + 1) / 2 + int(match.group(3) or 0)


def parse_ward(
    rules,
    is_flaming: bool = False,
    is_killing_blow: bool = False,
    is_multiple_wounds: bool = False,
    is_magical: bool = False,
) -> int | None:
    """Best (lowest) Ward save target for a character, or None.

    Recognises the generic "WardX" form, "Chaos Armour (X+)" (which is a Ward
    save, not an armour save), and the named High Elf sources, whether written
    bare ("Dragon Armour") or annotated ("Dragon Armour (6+ Ward)").

    A ward can be limited to particular wounds by naming the conditions in
    brackets - "Ward4 (Killing Blow, Multiple Wounds)" is the Armour of
    Skaldour. Blessings of Asuryan is the same idea under a named rule.
    """
    targets = []
    for rule in _as_list(rules):
        rule = rule.strip()
        # "Ward5", or "Ward4 (Killing Blow, Multiple Wounds)" for a ward that
        # only applies against particular kinds of wound.
        match = re.fullmatch(
            r"Ward\s*(\d+)\+?\s*(?:\((?P<conditions>[^)]*)\))?", rule
        )
        if match:
            conditions = match.group("conditions")
            if conditions is None:
                targets.append(int(match.group(1)))
            else:
                active = {
                    "flaming": is_flaming,
                    "killing blow": is_killing_blow,
                    "multiple wounds": is_multiple_wounds,
                    "non-magical": not is_magical,
                }
                wanted = [c.strip().lower() for c in conditions.split(",")]
                unknown = [c for c in wanted if c not in _WARD_CONDITIONS]
                if unknown:
                    raise ValueError(
                        f"Unknown Ward condition(s) {unknown} in rule {rule!r}; "
                        f"expected any of {list(_WARD_CONDITIONS)}"
                    )
                if any(active[c] for c in wanted):
                    targets.append(int(match.group(1)))
            continue
        match = re.fullmatch(
            r"Chaos\s*Armou?r\s*\(?(\d+)\+?\)?", rule, re.IGNORECASE
        )
        if match:
            targets.append(int(match.group(1)))
            continue
        named = _NAMED_WARDS.get(_base_name(rule))
        if named:
            target, flaming_only = named
            if is_flaming or not flaming_only:
                targets.append(target)
    return min(targets) if targets else None
