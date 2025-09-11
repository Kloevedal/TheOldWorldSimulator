import numpy as np

from armor import *
from elven_honors import *
from game_data import *
from magic_items import *
from weapons import *


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
            self.SpecialRules = SpecialRules if SpecialRules is not None else profile["SpecialRules"]
            
            # Validate equipment options
            options = FactionProfiles[faction_type][profile_name]["equipment_options"]
            if self.Weapon not in options["weapons"]:
                raise ValueError(f"Invalid weapon choice for {profile_name}: {self.Weapon}")
            if self.Armor and self.Armor not in options["armor"]:
                raise ValueError(f"Invalid armor choice for {profile_name}: {self.Armor}")
            if self.Shield and not options["shield"]:
                raise ValueError(f"{profile_name} cannot use a shield")

            # Enforce 'RequiresTwoHands' rule: cannot use shield with such weapons
            weapon_special_rules = None
            for key in MeleeWeaponDict:
                if self.Weapon == key or (isinstance(key, tuple) and self.Weapon in key):
                    weapon_special_rules = MeleeWeaponDict[key][2]
                    break
            if weapon_special_rules and "RequiresTwoHands" in weapon_special_rules and self.Shield:
                raise ValueError(f"Cannot use a shield with a two-handed weapon: {self.Weapon}")
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
            self.SpecialRules = SpecialRules if SpecialRules else None

            # Enforce 'RequiresTwoHands' rule: cannot use shield with such weapons
            from weapons import MeleeWeaponDict
            weapon_special_rules = None
            for key in MeleeWeaponDict:
                if self.Weapon == key or (isinstance(key, tuple) and self.Weapon in key):
                    weapon_special_rules = MeleeWeaponDict[key][2]
                    break
            if weapon_special_rules and "RequiresTwoHands" in weapon_special_rules and self.Shield:
                raise ValueError(f"Cannot use a shield with a two-handed weapon: {self.Weapon}")
            
        # Common initialization
        self.original_Strength = self.Strength
        self.original_Initiative = self.Initiative
        self.original_Weapon = self.Weapon
        self.ArmourPiercing = 0
        self.original_ArmourPiercing = 0

        # Apply Elven Honors if High Elf and honors are provided
        if self.Race in RACE_NAMES["HIGH_ELVES"] and elven_honors:
            for honor in elven_honors:
                if honor in ElvenHonors:
                    honor_data = ElvenHonors[honor]
                    # Apply stat modifications
                    for stat, mod in honor_data.get("stat_mods", {}).items():
                        if hasattr(self, stat):
                            setattr(self, stat, getattr(self, stat) + mod)
                    # Add special rules
                    if honor_data.get("special_rules"):
                        if isinstance(self.SpecialRules, list):
                            self.SpecialRules.extend(honor_data["special_rules"])
                        elif self.SpecialRules:
                            self.SpecialRules = [self.SpecialRules] + honor_data["special_rules"]
                        else:
                            self.SpecialRules = honor_data["special_rules"]
                    # Update equipment options
                    # (You may want to store these in the character for validation)
                    if hasattr(self, "equipment_options"):
                        for k, v in honor_data.get("equipment_options", {}).items():
                            self.equipment_options[k] = v
