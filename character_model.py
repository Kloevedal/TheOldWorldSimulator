"""The Character model: a single combatant built from a profile or from raw stats."""

from __future__ import annotations

from elven_honors import apply_elven_honors
from magic_items import apply_magic_items
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
            self._validate_equipment(self.profile_name, options)
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

        self.SpecialRules = _as_rule_list(profile.get("SpecialRules")) + self.SpecialRules
        self.UnitCategory = profile.get("UnitCategory")
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

    def _validate_equipment(self, profile_name, options):
        if self.Weapon not in options["weapons"]:
            raise ValueError(
                f"Invalid weapon choice for {profile_name}: {self.Weapon}. "
                f"Legal options: {options['weapons']}"
            )
        if self.Armor and self.Armor not in options["armor"]:
            raise ValueError(
                f"Invalid armor choice for {profile_name}: {self.Armor}. "
                f"Legal options: {options['armor']}"
            )
        if self.Shield and not options["shield"]:
            raise ValueError(f"{profile_name} cannot use a shield")

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
