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
# Killing Blow's relatives. A natural 6 To Wound with Monster Slayer is a
# Killing Blow against a monster; with Cleaving Blow it denies armour and
# Regeneration saves to infantry, cavalry and war beasts, without slaying.
MonsterSlayer = "Monster Slayer"
CleavingBlow = "Cleaving Blow"
# A weapon whose wounds permit no Regeneration save (Bilesword, Plaguesword).
NoRegeneration = "No Regeneration Saves"
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
AccursedWeapons = "Accursed Weapons"  # Vampire Counts (Blood Knights)

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

# A barded mount improves its rider's armour value by 1.
Barding = "Barding"

# Kingdom of Bretonnia. The Grail Vow always has the Blessings of the Lady.
BlessingsOfTheLady = "Blessings of the Lady"
GrailVow = "The Grail Vow"

# Effects granted by magic items, runes and abilities. Parameterised ones are
# read by the parsers below: "Improve Armour (1)", "To Hit (+1)",
# "Enemy To Hit (-1)", "Wounds On (2+)".
# A natural 6 To Hit adds +2 to that hit's roll To Wound (not with a magic weapon).
PoisonedAttacks = "Poisoned Attacks"
# An unsaved wound from a Multiple Wounds attack costs this model a single Wound.
ImmuneToMultipleWounds = "Immune to Multiple Wounds"
# No armour save is permitted against this model's (or weapon's) wounds.
NoArmourSaves = "No Armour Saves"
RerollFailedHits = "Reroll Failed Hits"
RerollFailedWounds = "Reroll Failed Wounds"
RerollWounds1 = "Reroll Wounds 1"
# Virtue of Audacity: re-roll failed hits against a higher Weapon Skill.
RerollHitsVsHigherWS = "Reroll Failed Hits (against higher Weapon Skill)"
# +1 Initiative during the first round of any combat, whatever the source.
FirstRoundInitiative = "+1 Initiative in the First Round"
# Beguile, Allure of Slaanesh: an enemy must pass a Leadership test before
# rolling To Hit against this model, or it hits only on natural 6s.
BeguilingPresence = "Enemy Must Pass Leadership To Hit"
# Enemy models must re-roll successful armour saves against this weapon's wounds.
EnemyRerollsArmourSaves = "Enemy Rerolls Successful Armour Saves"
# Enemy models must re-roll successful rolls To Hit / To Wound against this model.
EnemyRerollsHits = "Enemy Rerolls Successful Hits"
EnemyRerollsWounds = "Enemy Rerolls Successful Wounds"
# A roll To Wound of 2 never wounds this model (Daemon-flesh, Daemonic Robes).
CannotBeWoundedOn2 = "Cannot Be Wounded On 2"
# The armour value cannot be improved (Armour of Silvered Steel), or cannot be
# improved or reduced in any way (Armour of Meteoric Iron, Master Rune of Gromril).
ArmourCannotBeImproved = "Armour Cannot Be Improved"
ArmourCannotBeModified = "Armour Cannot Be Modified"



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


def parse_fixed_strength(*rule_sources) -> int | None:
    """A weapon's own Strength ("Strength (4)"), which replaces the wielder's."""
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = re.fullmatch(r"Strength\s*\((\d+)\)", rule.strip(), re.IGNORECASE)
            if match:
                return int(match.group(1))
    return None


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
                continue
            match = re.fullmatch(r"Improve\s*Armou?r\s*\((\d+)\)", rule.strip(), re.IGNORECASE)
            if match:
                bonus += int(match.group(1))
            elif rule in (ImproveArmor1InCombat, Barding):
                bonus += 1
    return bonus


def _signed_modifiers(prefix, rule_sources):
    total = 0
    pattern = re.compile(re.escape(prefix) + r"\s*\(([+-]\d+)\)$", re.IGNORECASE)
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = pattern.fullmatch(rule.strip())
            if match:
                total += int(match.group(1))
    return total


def parse_armour_piercing_bonus(*rule_sources) -> int:
    """Improvement to the Armour Piercing of every weapon ("Improve Armour Piercing (1)")."""
    total = 0
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = re.fullmatch(r"Improve\s*Armou?r\s*Piercing\s*\((\d+)\)", rule.strip(), re.IGNORECASE)
            if match:
                total += int(match.group(1))
    return total


_AMOUNT = r"(\d+|\d*D[36](?:\s*\+\s*\d+)?)"


def _amount_rule(name, rule_sources):
    """Sum of "Name (X)" amounts; each is an int or a dice string such as "D3+1"."""
    found = []
    pattern = re.compile(re.escape(name) + r"\s*\(\+?" + _AMOUNT + r"\)", re.IGNORECASE)
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = pattern.fullmatch(rule.strip())
            if match:
                value = match.group(1).upper().replace(" ", "")
                found.append(int(value) if value.isdigit() else value)
    return found


def parse_impact_hits(*rule_sources):
    """Impact Hits amounts: "Impact Hits (D3+1)" -> ["D3+1"]. Qualified forms
    ("Impact Hits (D3) (Dragon Form only)") are not matched."""
    return _amount_rule("Impact Hits", rule_sources)


def parse_stomp_attacks(*rule_sources):
    """Stomp Attacks amounts: "Stomp Attacks (D6)" -> ["D6"]."""
    return _amount_rule("Stomp Attacks", rule_sources)


def parse_extra_attacks(*rule_sources):
    """Extra Attacks amounts: "Extra Attacks (+D3)" -> ["D3"]; "+1A" is read elsewhere."""
    return _amount_rule("Extra Attacks", rule_sources)


def parse_impact_hits_ap(*rule_sources) -> int:
    """Armour Piercing of this model's Impact Hits ("Impact Hits Armour Piercing (2)")."""
    total = 0
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = re.fullmatch(r"Impact\s*Hits\s*Armou?r\s*Piercing\s*\((\d+)\)", rule.strip(), re.I)
            if match:
                total += int(match.group(1))
    return total


def parse_to_hit_modifier(*rule_sources) -> int:
    """Sum of this model's own To Hit modifiers ("To Hit (+1)" -> +1)."""
    return _signed_modifiers("To Hit", rule_sources)


def parse_enemy_to_hit_modifier(*rule_sources) -> int:
    """Sum of modifiers enemies suffer To Hit this model ("Enemy To Hit (-1)" -> -1)."""
    return _signed_modifiers("Enemy To Hit", rule_sources)


def parse_wounds_on(*rule_sources) -> int | None:
    """Best "Wounds On (N+)": a roll of N+ always wounds, whatever the Toughness."""
    best = None
    for rules in rule_sources:
        for rule in _as_list(rules):
            match = re.fullmatch(r"Wounds\s*On\s*\((\d)\+\)", rule.strip(), re.IGNORECASE)
            if match:
                value = int(match.group(1))
                best = value if best is None else min(best, value)
    return best


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
_WARD_CONDITIONS = ("flaming", "killing blow", "multiple wounds", "non-magical", "magical")


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
    strength: int | None = None,
) -> int | None:
    """Best (lowest) Ward save target for a character, or None.

    `strength` is the Strength of the attack being saved against, for wards
    limited by it: "Ward5 (Strength 5+)", "Ward5 (Strength 4-)", and the
    Blessings of the Lady (6+, or 5+ against Strength 5 or higher). The
    Blessing assumes the Bretonnian army knelt to pray for it, as it almost
    always does; the Grail Vow grants it regardless.

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
                    "magical": is_magical,
                }
                wanted = [c.strip().lower() for c in conditions.split(",")]
                for c in wanted:
                    limit = re.fullmatch(r"strength (\d+)([+-])", c)
                    if limit:
                        value = int(limit.group(1))
                        active[c] = strength is not None and (
                            strength >= value if limit.group(2) == "+" else strength <= value)
                unknown = [c for c in wanted if c not in _WARD_CONDITIONS and c not in active]
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
        if rule in (BlessingsOfTheLady, GrailVow):
            targets.append(5 if strength is not None and strength >= 5 else 6)
            continue
        named = _NAMED_WARDS.get(_base_name(rule))
        if named:
            target, flaming_only = named
            if is_flaming or not flaming_only:
                targets.append(target)
    return min(targets) if targets else None
