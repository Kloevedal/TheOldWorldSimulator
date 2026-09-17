"""The Character model: a single combatant built from a profile or from raw stats."""

from __future__ import annotations

from elven_honors import apply_elven_honors
from elven_honors import ElvenHonors
from magic_items import apply_magic_items, check_purchase, get_magic_item, granted_equipment
from faction_profiles import (
    RACE_NAMES,
    FactionProfiles,
    resolve_faction,
    resolve_profile,
)
from special_rules import RequiresTwoHands
from weapons import get_weapon_special_rules

# Stats that a profile supplies and the caller may override individually.
_PROFILE_STATS = (
    "Movement",
    "WeaponSkill",
    "BallisticSkill",
    "Strength",
    "Toughness",
    "Initiative",
    "Wounds",
    "Attacks",
    "Leadership",
    "Race",
    "Armor",
    "Shield",
)

_DEFAULT_WEAPON = "HW"

# Options that replace one another: choosing one removes whichever the profile
# carries by default (a Chaos Lord's Mark of Chaos Undivided, a Knight's Vow).
EXCLUSIVE_OPTIONS = (
    ("Mark of Chaos Undivided", "Mark of Khorne", "Mark of Nurgle",
     "Mark of Slaanesh", "Mark of Tzeentch"),
    ("The Knight's Vow", "The Questing Vow", "The Grail Vow"),
)


def offered_options(profile):
    """Rules a profile may add: its OptionalRules and any Marks of Chaos."""
    return list(profile.get("OptionalRules") or []) + list(profile.get("MarksOfChaos") or [])


class Character:
    """A single fighter.

    Pass `faction_type` and `profile_name` to build from a published profile —
    stats default to the profile and equipment is validated against that
    profile's legal options. Pass raw stats instead to build a custom fighter
    with no validation beyond the two-handed weapon check.
    """

    def __init__(
        self,
        name,
        Movement=None,
        WeaponSkill=None,
        BallisticSkill=None,
        Strength=None,
        Toughness=None,
        Initiative=None,
        Wounds=None,
        Attacks=None,
        Leadership=None,
        Race=None,
        Armor=None,
        Weapon=_DEFAULT_WEAPON,
        Shield=None,
        SpecialRules=None,
        faction_type=None,
        profile_name=None,
        elven_honors=None,
        magic_items=None,
        mount=None,
    ):
        supplied = {
            "Movement": Movement,
            "WeaponSkill": WeaponSkill,
            "BallisticSkill": BallisticSkill,
            "Strength": Strength,
            "Toughness": Toughness,
            "Initiative": Initiative,
            "Wounds": Wounds,
            "Attacks": Attacks,
            "Leadership": Leadership,
            "Race": Race,
            "Armor": Armor,
            "Shield": Shield,
        }

        self.name = name
        self.SpecialRules = _as_rule_list(SpecialRules)
        self.UnitCategory = None
        self.TroopType = None

        if faction_type and profile_name:
            options = self._load_profile(
                faction_type, profile_name, supplied, Weapon
            )
        else:
            for stat in _PROFILE_STATS:
                setattr(self, stat, supplied[stat])
            self.Weapon = Weapon
            options = None

        # A shield is present or it is not; `Shield=False` must not count as
        # "wearing a shield" the way a bare `is not None` test would.
        self.Shield = bool(self.Shield)

        if options is not None:
            granted = granted_equipment(magic_items)
            for honour in elven_honors or []:
                # The original Elven Honour option names its weapons too.
                granted["weapons"] += ElvenHonors.get(honour, {}).get(
                    "equipment_options", {}).get("weapons", [])
            self._validate_equipment(self.profile_name, options, granted)

        # Bought magic items, runes and abilities. A profile-based character is
        # held to its army's list and its points allowance; a custom fighter
        # may take anything that exists.
        self.magic_items = list(magic_items or [])
        if self.magic_items:
            if options is not None:
                check_purchase(self.faction, self.profile_name, self.magic_items)
            self._equip_magic_items(self.magic_items)
        self._validate_two_handed()

        # Named characters carry fixed wargear, so their magic items are applied
        # automatically. Everyone else buys items, which is not modelled yet.
        if options is not None and self.UnitCategory == "NamedCharacter":
            unknown = apply_magic_items(self, options.get("items"))
            if unknown:
                print(
                    f"Warning: {self.name} carries unrecognised magic item(s): "
                    f"{', '.join(unknown)}"
                )

        # Apply Elven Honours before snapshotting originals, so that an honour
        # which modifies a stat is not wiped by the first reset_weapon_stats.
        if self.Race in RACE_NAMES["HIGH_ELVES"] and elven_honors:
            apply_elven_honors(self, elven_honors)

        # A mount comes last: it reads the rider's finished rules and armour.
        self.mount = None
        self.mount_parts = []
        self.mount_strength = None
        from mounted import apply_mount, check_mount, integral_mount

        fixed = integral_mount(getattr(self, "faction", None), getattr(self, "profile_name", None))
        if fixed and mount and mount != fixed:
            raise ValueError(f"{self.profile_name} always rides {fixed}")
        if mount or fixed:
            from magic_items import get_magic_item

            if not fixed:
                check_mount(self, mount, list(self.magic_items) + list(elven_honors or []),
                            self._mount_options if options is not None else None)
            item_rules = [r for name in self.magic_items
                          for r in (get_magic_item(name) or {}).get("rules", [])]
            apply_mount(self, fixed or mount, item_rules, getattr(self, "faction", None),
                        integral=bool(fixed))

        self.original_Strength = self.Strength
        self.original_Initiative = self.Initiative
        self.original_Weapon = self.Weapon
        self.ArmourPiercing = 0
        self.original_ArmourPiercing = 0

        # Combat state. `Wounds` is the profile maximum and is never mutated by
        # the engine; `current_wounds` is the damage tracker.
        self.current_wounds = self.Wounds
        self.ward_applied = False
        self.primal_fury_active = False
        self.blood_rage_frenzied = False

    # -- construction helpers -------------------------------------------------

    def _load_profile(self, faction_type, profile_name, supplied, weapon):
        faction = resolve_faction(faction_type)
        if faction is None:
            raise ValueError(
                f"Unknown faction: {faction_type}. "
                f"Known: {sorted(FactionProfiles)}"
            )

        profiles = FactionProfiles[faction]
        resolved = resolve_profile(faction, profile_name)
        if resolved is None:
            raise ValueError(
                f"Unknown {faction} profile: {profile_name}. "
                f"Known: {sorted(profiles)}"
            )
        self.faction = faction
        self.profile_name = resolved

        entry = profiles[resolved]
        profile = entry["base_profile"]
        options = entry["equipment_options"]

        # Named-character profiles omit keys like Armor/Weapon/Shield, so read
        # them defensively rather than assuming every profile is complete.
        for stat in _PROFILE_STATS:
            value = supplied[stat]
            setattr(self, stat, value if value is not None else profile.get(stat))

        chosen = self.SpecialRules
        base_rules = _as_rule_list(profile.get("SpecialRules"))
        offered = set(offered_options(profile))
        for group in EXCLUSIVE_OPTIONS:
            picks = [rule for rule in chosen if rule in group]
            if not picks:
                continue
            if len(picks) > 1:
                raise ValueError(f"{resolved} can only have one of {picks}")
            if picks[0] not in offered and picks[0] not in base_rules:
                raise ValueError(
                    f"{resolved} cannot take {picks[0]}. Offered: {sorted(offered) or 'nothing'}"
                )
            base_rules = [rule for rule in base_rules if rule not in group]
        self.SpecialRules = base_rules + chosen
        self.UnitCategory = profile.get("UnitCategory")
        self._mount_options = list(entry.get("mount_options", {}).get("mounts", []))
        self.TroopType = profile.get("TroopType")

        if weapon != _DEFAULT_WEAPON:
            self.Weapon = weapon
        elif profile.get("Weapon"):
            self.Weapon = profile["Weapon"]
        elif "Hand Weapon" in options["weapons"]:
            self.Weapon = "Hand Weapon"
        else:
            raise ValueError(
                f"{profile_name} has no default weapon - pass one of: "
                f"{options['weapons']}"
            )
        return options

    def _validate_equipment(self, profile_name, options, granted=None):
        """The weapon, armour and shield must be offered by the profile, or
        unlocked by a bought ability (`granted`, e.g. an Elven Honour's sword of
        Hoeth). Names are compared through their synonyms."""
        from armor import ArmourDict
        from weapons import find_weapon_key

        granted = granted or {}
        weapons = list(options["weapons"]) + list(granted.get("weapons", []))
        wanted = find_weapon_key(self.Weapon) or self.Weapon
        if self.Weapon not in weapons and wanted not in {find_weapon_key(w) for w in weapons}:
            raise ValueError(
                f"Invalid weapon choice for {profile_name}: {self.Weapon}. "
                f"Legal options: {weapons}"
            )

        def armour_key(name):
            return next((key for key in ArmourDict if name in key), name)

        armours = list(options["armor"]) + list(granted.get("armour", []))
        if self.Armor and armour_key(self.Armor) not in {armour_key(a) for a in armours}:
            raise ValueError(
                f"Invalid armor choice for {profile_name}: {self.Armor}. "
                f"Legal options: {armours}"
            )
        if self.Shield and not options["shield"]:
            raise ValueError(f"{profile_name} cannot use a shield")

    def _equip_magic_items(self, items):
        for name in items:
            entry = get_magic_item(name)
            if entry is None:
                raise ValueError(f"Unknown magic item: {name!r}")
            if entry.get("is_weapon"):
                self.Weapon = entry.get("weapon", name)
        apply_magic_items(self, items)

    def _validate_two_handed(self):
        weapon_rules = get_weapon_special_rules(self.Weapon)
        if self.Shield and RequiresTwoHands in weapon_rules:
            raise ValueError(
                f"Weapon {self.Weapon} requires two hands and cannot be used "
                "with a shield"
            )

    def __repr__(self):
        return (
            f"<Character {self.name}: WS{self.WeaponSkill} S{self.Strength} "
            f"T{self.Toughness} I{self.Initiative} A{self.Attacks} "
            f"W{self.current_wounds}/{self.Wounds}>"
        )


def _as_rule_list(rules):
    """Special rules are always stored as a list, whatever the caller passed."""
    if not rules:
        return []
    if isinstance(rules, str):
        return [rules]
    return list(rules)
