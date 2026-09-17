"""Mounted characters: a rider and its mount fighting as one model.

From the rules (Characters & Cavalry Mounts, Characters & Chariot Mounts,
Characters & Ridden Monsters, the Split Profile rules and Challenges & Mounts):

* The model takes the mount's troop type.
* Special rules on one element apply to the other as well, unless noted - so
  rules marked "(but not its mount)" and hand-weapon rules stay with the rider,
  as do the rider's magic items.
* Rider and mount each use their own WS, S, I and A and their own weapons, and
  in a challenge the mount attacks the other participant.
* Enemy rolls To Hit use the rider's Weapon Skill.
* Impact Hits and Stomp Attacks use the mount's (or chariot's) Strength.
* Cavalry: the rider's armour value; barding improves it by 1. A mount can
  raise the rider's Toughness and Wounds ("+1" on its profile).
* Ridden monsters: the better of the mount's and the rider's armour value; the
  mount raises Toughness and Wounds.
* Chariots: the better armour value, the higher Toughness, and the character's
  Wounds are added to the chariot's. Crew and beasts attack as well.

The combined model is still one Character: its Toughness, Wounds, armour and
troop type are adjusted here, and the mount's attackers are listed in
`character.mount_parts`, which the engine adds to the strike order.
"""

from __future__ import annotations

import re

from armor import get_armour_save
from mounts import HONOUR_MOUNTS, Mounts
from special_rules import ArmourCannotBeImproved, Barding, parse_armour_bonus

# Armour names for a printed or "counts as" armour value.
_ARMOUR_BY_VALUE = {6: "Light Armor", 5: "Heavy Armor", 4: "Full Plate Armor",
                    3: "Armour Value 3+", 2: "Armour Value 2+"}
_COUNTS_AS = {"light": 6, "heavy": 5, "full plate": 4}

# Rules that belong to the rider alone: those the rules text marks "(but not
# its mount)", and rules about the rider's own hand weapon.
RIDER_ONLY = {
    "Bull Charge", "Daemons of Khorne", "Elven Reflexes", "Ensorcelled Weapons",
    "Eternal Hatred", "Foe Render", "Inner Circle", "Khopesh", "Obsidian Blades",
    "Ogre Charge", "Gromril Weapons", "Warpstone Weapons", "Accursed Weapons",
    "Murderous", "Ithilmar Weapons", "Choppas",
}
# Per army, where the profiles say so ("Strike First does not apply to this
# model's mount" on the High Elf characters).
RIDER_ONLY_BY_FACTION = {"High Elf Realms": {"Strike First"}}

# Impact Hits and Stomp Attacks belong to the model but use the mount's
# Strength; the engine reads them from the model, not from each attacker.
_MODEL_RULES = re.compile(r"^(Impact Hits|Stomp Attacks)\b")

# Elven Honours that limit a character's mounts ("may only be mounted on",
# "cannot be mounted"). An honour not listed places no limit.
HONOUR_MOUNT_LIMITS = {
    "Chracian Hunter": {"Lion Chariot of Chrace"},
    "Sea Guard": {"Lothern Skycutter"},
    "Anointed of Asuryan": {"Flamespyre Phoenix", "Frostheart Phoenix"},
    "Blood of Caledor": {"Barded Elven Steed", "Sun Dragon", "Moon Dragon", "Star Dragon"},
    "Loremaster": set(),
    "Warden of Saphery": set(),
    "Shadow Stalker": set(),
}

# Characters whose own page includes their mount: they always ride it, and
# their printed Toughness and Wounds already include its bonuses.
INTEGRAL_MOUNTS = {
    ("High Elf Realms", "Dragon Mage"): "Sun Dragon",
    ("Orc & Goblin Tribes", "Kiknik Toofsnatcha"): "Chompa",
    ("Empire of Man", "Harald Gemunsen"): "Barded Warhorse",
    ("Grand Cathay", "Shugengan Lord"): "Great Spirit Longma",
    ("Grand Cathay", "Shugengan General"): "Great Spirit Longma",
    ("Kingdom of Bretonnia", "Lady Élisse Duchaard"): "Ariandir",
    ("Kingdom of Bretonnia", "The Green Knight"): "The Shadow Steed",
    ("Tomb Kings of Khemri", "Settra the Imperishable"): "Chariot of the Gods",
}


def integral_mount(faction, profile):
    return INTEGRAL_MOUNTS.get((faction, profile))


# The original elven_honors= option names honours without spaces.
LEGACY_HONOURS = {
    "ChracianHunter": "Chracian Hunter", "SeaGuard": "Sea Guard",
    "AnointedofAsuryan": "Anointed of Asuryan", "BloodofCaledor": "Blood of Caledor",
    "Loremaster": "Loremaster", "WardenofSaphery": "Warden of Saphery",
    "ShadowStalker": "Shadow Stalker", "PureofHeart": "Pure of Heart",
}


def mount_kind(mount):
    troop = (mount.get("troop_type") or "").lower()
    if "chariot" in troop:
        return "chariot"
    if troop in ("monstrouscreature", "behemoth"):
        return "monster"
    return "cavalry"


def _bonus(value):
    """'+2' -> 2; a plain number or None -> 0."""
    return int(value) if isinstance(value, str) and re.fullmatch(r"[+-]\d+", value) else 0


def _count(row_name):
    match = re.search(r"\(x(\d+)\)", row_name or "")
    return int(match.group(1)) if match else 1


def _row_weapon(mount, row_name):
    """The melee weapon a mount row fights with, read from the equipment text."""
    from weapons import find_weapon_key

    text = mount.get("equipment") or ""
    lines = [l.lstrip("- ").strip() for l in text.splitlines() if l.strip()]
    base = re.sub(r"\s*\(x\d+\)$", "", row_name or "").lower()
    line = text
    if len(lines) > 1:
        line = next((l for l in lines
                     if base and (base.split()[0] in l.split(":")[0].lower()
                                  or l.split(":")[0].lower().rstrip("s") in base)), lines[-1])
    if "counts as a hand weapon" in line.lower() or "counts as hand weapon" in line.lower():
        return "Hand Weapon"
    for part in re.split(r",\s*|\s+and\s+|:\s*", line):
        part = re.sub(r"\s*\(.*?\)", "", part).strip()
        for candidate in (part, part.rstrip("s"), part.title(), part.title().rstrip("s")):
            if candidate and find_weapon_key(candidate) and candidate.lower() not in ("hand weapon",):
                key = find_weapon_key(candidate)
                return key[0]
    return "Hand Weapon"


def _mount_armour_value(mount):
    printed = re.match(r"(\d)\+", str(mount.get("armour_value") or ""))
    if printed:
        return int(printed.group(1))
    counts = re.search(r"counts as (light|heavy|full plate) armour", (mount.get("equipment") or "").lower())
    return _COUNTS_AS[counts.group(1)] if counts else None


def _has_barding(mount):
    text = (mount.get("equipment") or "").lower()
    return "barding" in text or any("Barding" in r for r in mount.get("SpecialRules", []))


class MountPart:
    """One attacking element of a mount: a steed, a monster, a chariot's crew or beasts.

    It strikes with its own characteristics and weapon; damage and healing go
    to the model it belongs to (`owner`).
    """

    def __init__(self, owner, name, row, weapon, rules, troop_type):
        self.owner = owner
        label = re.sub(r"\s*\(x\d+\)$", "", name)
        self.name = f"{owner.name}'s {label}"
        self.WeaponSkill = row.get("WeaponSkill")
        self.BallisticSkill = row.get("BallisticSkill")
        self.Strength = row.get("Strength")
        self.Toughness = owner.Toughness
        self.Initiative = row.get("Initiative")
        self.Attacks = (row.get("Attacks") or 0) * _count(name)
        self.Leadership = owner.Leadership
        self.Race = owner.Race
        self.Armor, self.Shield = owner.Armor, owner.Shield
        self.Weapon = weapon
        self.SpecialRules = list(rules)
        self.TroopType = troop_type
        self.UnitCategory = "Mount"
        self.original_Strength = self.Strength
        self.original_Initiative = self.Initiative
        self.original_Weapon = weapon
        self.ArmourPiercing = 0
        self.original_ArmourPiercing = 0
        self.primal_fury_active = False
        self.blood_rage_frenzied = False

    @property
    def current_wounds(self):
        return self.owner.current_wounds

    @current_wounds.setter
    def current_wounds(self, value):
        self.owner.current_wounds = value

    @property
    def Wounds(self):
        return self.owner.Wounds

    def __repr__(self):
        return f"<MountPart {self.name}: WS{self.WeaponSkill} S{self.Strength} I{self.Initiative} A{self.Attacks}>"


def check_mount(character, mount_name, honours, options_mounts):
    """Raise ValueError if the character may not ride this mount."""
    if mount_name not in Mounts:
        raise ValueError(f"Unknown mount: {mount_name!r}")
    if options_mounts is not None and mount_name not in options_mounts:
        raise ValueError(
            f"{character.profile_name} cannot ride a {mount_name}. "
            f"Mounts: {options_mounts or 'none'}")
    taken = {LEGACY_HONOURS.get(h, h) for h in honours}
    needed = HONOUR_MOUNTS.get(mount_name)
    if needed and needed not in taken:
        raise ValueError(f"A {mount_name} needs the {needed} Elven Honour")
    for honour in taken:
        allowed = HONOUR_MOUNT_LIMITS.get(honour)
        if allowed is not None and mount_name not in allowed:
            limit = ", ".join(sorted(allowed)) or "no mount"
            raise ValueError(f"With {honour} the character may only ride: {limit}")


def apply_mount(character, mount_name, item_rules=(), faction=None, integral=False):
    """Turn `character` into the combined rider-and-mount model.

    `integral` means the rider's statline already includes the mount's
    Toughness and Wounds, so they are not added again.
    """
    mount = Mounts[mount_name]
    kind = mount_kind(mount)
    rows = mount.get("profiles") or [dict(mount, Name=mount_name)]
    mount_rules = list(mount.get("SpecialRules") or [])

    character.mount = mount_name
    character.TroopType = mount.get("troop_type")

    # Toughness and Wounds.
    if integral:
        body = next((r for r in rows if r.get("WeaponSkill") is None and r.get("Strength")), None)
        character.mount_strength = (body or mount).get("Strength")
    elif kind == "chariot":
        body = next((r for r in rows if r.get("WeaponSkill") is None and r.get("Wounds")), None)
        if body:
            character.Toughness = max(character.Toughness or 0, body.get("Toughness") or 0)
            character.Wounds = (character.Wounds or 0) + (body.get("Wounds") or 0)
        character.mount_strength = (body or {}).get("Strength")
    else:
        character.Toughness = min(10, (character.Toughness or 0) + _bonus(mount.get("Toughness")))
        character.Wounds = (character.Wounds or 0) + _bonus(mount.get("Wounds"))
        character.mount_strength = mount.get("Strength")

    # Rules: the mount's apply to the model; the rider's (except rider-only ones
    # and items) apply to the mount's attackers too.
    rider_only = RIDER_ONLY | RIDER_ONLY_BY_FACTION.get(faction, set()) | set(item_rules)
    shared = [r for r in character.SpecialRules if r not in rider_only and not _MODEL_RULES.match(r)]
    # A rider's profile can say a mount's rule is its own: "Armour Bane (1, Chompa only)".
    mount_only = set()
    for rule in character.SpecialRules:
        noted = re.fullmatch(r"(.+?) \((.+?), (.+?) only\)", rule)
        if noted and noted.group(3) == mount_name:
            mount_only.add(f"{noted.group(1)} ({noted.group(2)})")
    # ...or the mount's own entry can: "Armour Bane (1, Unicorn only)".
    scoped = []
    for rule in mount_rules:
        noted = re.fullmatch(r"(.+?) \((.+?), (.+?) only\)", rule)
        if noted and noted.group(3) == mount_name:
            plain = f"{noted.group(1)} ({noted.group(2)})"
            mount_only.add(plain)
            scoped.append((rule, plain))
    for old, new in scoped:
        mount_rules[mount_rules.index(old)] = new
    # Impact Hits and Stomp Attacks always belong to the whole model.
    mount_only = {r for r in mount_only if not _MODEL_RULES.match(r)}
    for rule in mount_rules:
        if rule not in character.SpecialRules and rule not in mount_only:
            character.SpecialRules.append(rule)

    # Armour.
    if kind == "cavalry":
        if _has_barding(mount) and Barding not in character.SpecialRules:
            character.SpecialRules.append(Barding)
    else:
        mount_value = _mount_armour_value(mount)
        rider_base = get_armour_save(character.Armor) or 7
        rider_value = rider_base - (1 if character.Shield else 0) - parse_armour_bonus(character.SpecialRules)
        if mount_value is not None and mount_value < rider_value:
            # The mount's printed value is final: the rider's shield and armour
            # bonuses belong to the rider's own armour.
            character.Armor = _ARMOUR_BY_VALUE[mount_value]
            character.Shield = False
            character.SpecialRules.append(ArmourCannotBeImproved)

    # The mount's attackers.
    parts = []
    for row in rows:
        if not isinstance(row.get("WeaponSkill"), int) or not isinstance(row.get("Attacks"), int):
            continue
        rules = [r for r in mount_rules if not _MODEL_RULES.match(r)] + [
            r for r in shared if r not in mount_rules]
        parts.append(MountPart(character, row.get("Name", mount_name), row,
                               _row_weapon(mount, row.get("Name")), rules, mount.get("troop_type")))
    character.mount_parts = parts
    return character
