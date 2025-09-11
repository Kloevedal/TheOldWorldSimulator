import numpy as np

from armor import *
from elven_honors import *
from faction_profiles import *
from magic_items import *
from weapons import get_weapon_special_rules


class Character:
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
        Weapon="HW",
        Shield=None,
        SpecialRules=None,
        faction_type=None,
        profile_name=None,
        elven_honors=None
    ):
        if faction_type and profile_name:
            if faction_type not in FactionProfiles:
                raise ValueError(f"Unknown faction: {faction_type}")
            if profile_name not in FactionProfiles[faction_type]:
                raise ValueError(f"Unknown {faction_type} profile: {profile_name}")
                
            # Load base profile
            profile = FactionProfiles[faction_type][profile_name]["base_profile"]
            
            # Allow overriding specific stats while using defaults for others
            self.name = name
            self.Movement = Movement if Movement is not None else profile["Movement"]
            self.WeaponSkill = WeaponSkill if WeaponSkill is not None else profile["WeaponSkill"]
            self.BallisticSkill = BallisticSkill if BallisticSkill is not None else profile["BallisticSkill"]
            self.Strength = Strength if Strength is not None else profile["Strength"]
            self.Toughness = Toughness if Toughness is not None else profile["Toughness"]
            self.Initiative = Initiative if Initiative is not None else profile["Initiative"]
            self.Wounds = Wounds if Wounds is not None else profile["Wounds"]
            self.Attacks = Attacks if Attacks is not None else profile["Attacks"]
            self.Leadership = Leadership if Leadership is not None else profile["Leadership"]
            self.Race = Race if Race is not None else profile["Race"]
            self.Armor = Armor if Armor is not None else profile["Armor"]
            self.Weapon = Weapon if Weapon != "HW" else profile["Weapon"]
            self.Shield = Shield if Shield is not None else profile["Shield"]
            # Always store SpecialRules as a list
            base_rules = profile["SpecialRules"] if profile["SpecialRules"] else []
            if SpecialRules is not None:
                if isinstance(SpecialRules, list):
                    self.SpecialRules = base_rules + SpecialRules
                else:
                    self.SpecialRules = base_rules + [SpecialRules]
            else:
                self.SpecialRules = base_rules
            
            # Validate equipment options
            options = FactionProfiles[faction_type][profile_name]["equipment_options"]
            if self.Weapon not in options["weapons"]:
                raise ValueError(f"Invalid weapon choice for {profile_name}: {self.Weapon}")
            if self.Armor and self.Armor not in options["armor"]:
                raise ValueError(f"Invalid armor choice for {profile_name}: {self.Armor}")
            if self.Shield and not options["shield"]:
                raise ValueError(f"{profile_name} cannot use a shield")

            # Enforce 'RequiresTwoHands' rule: cannot use shield with such weapons
            # Use helper to fetch weapon special rules (avoids iterating MeleeWeaponDict)
            weapon_special_rules = get_weapon_special_rules(self.Weapon)
            if weapon_special_rules and "RequiresTwoHands" in weapon_special_rules and self.Shield:
                raise ValueError(f"Weapon {self.Weapon} requires two hands and cannot be used with a shield")
        else:
            # Original initialization for custom characters
            self.name = name
            self.Movement = Movement
            self.WeaponSkill = WeaponSkill
            self.BallisticSkill = BallisticSkill
            self.Strength = Strength
            self.Toughness = Toughness
            self.Initiative = Initiative
            self.Wounds = Wounds
            self.Attacks = Attacks
            self.Leadership = Leadership
            self.Race = Race
            self.Armor = Armor
            self.Weapon = Weapon
            self.Shield = Shield
            # Always store SpecialRules as a list
            if SpecialRules:
                if isinstance(SpecialRules, list):
                    self.SpecialRules = SpecialRules
                else:
                    self.SpecialRules = [SpecialRules]
            else:
                self.SpecialRules = []

            # Enforce 'RequiresTwoHands' rule: cannot use shield with such weapons
            # Use helper to fetch weapon special rules (avoids iterating MeleeWeaponDict)
            weapon_special_rules = get_weapon_special_rules(self.Weapon)
            if weapon_special_rules and "RequiresTwoHands" in weapon_special_rules and self.Shield:
                raise ValueError(f"Weapon {self.Weapon} requires two hands and cannot be used with a shield")
            
        # Common initialization
        self.original_Strength = self.Strength
        self.original_Initiative = self.Initiative
        self.original_Weapon = self.Weapon
        self.ArmourPiercing = 0
        self.original_ArmourPiercing = 0

        # Apply Elven Honors if High Elf and honors are provided
        # Use centralized helper to apply stat mods, add special rules, and update equipment options
        if self.Race in RACE_NAMES["HIGH_ELVES"] and elven_honors:
            apply_elven_honors(self, elven_honors)
