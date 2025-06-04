import numpy as np
from game_data import (RACE_NAMES, ArmourDict, FactionProfiles, FirstRoundOnly,
                       FirstRoundStr, IthilmarWeapons, MeleeWeaponDict,
                       StrikeFirst, StrikeLast, WeaponSkillChart,
                       Wounds_vs_ToughnessChart)


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
        profile_name=None
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
            
        # Common initialization
        self.original_Strength = self.Strength
        self.original_Initiative = self.Initiative
        self.original_Weapon = self.Weapon
        self.ArmourPiercing = 0
        self.original_ArmourPiercing = 0


def RollToHit(attacker, defender, verbose=False):
    """
    Roll dice to hit based on the attacker's Weapon Skill and defender's Weapon Skill.
    Returns the number of successful hits.
    Handles Ithilmar Weapons special rule that allows rerolls of 1s.
    """
    to_hit_target = WeaponSkillChart[attacker.WeaponSkill - 1][defender.WeaponSkill - 1]
    successful_hits = 0

    # Check if attacker has Ithilmar Weapons
    has_ithilmar = False
    if attacker.SpecialRules:
        if isinstance(attacker.SpecialRules, list):
            has_ithilmar = IthilmarWeapons in attacker.SpecialRules
        else:
            has_ithilmar = attacker.SpecialRules == IthilmarWeapons

    for attack in range(attacker.Attacks):
        roll = np.random.randint(1, 7)  # Roll a D6
        
        # If roll is 1 and has Ithilmar Weapons, reroll
        if roll == 1 and has_ithilmar:
            old_roll = roll
            roll = np.random.randint(1, 7)  # Reroll
            if verbose:
                print(f"Ithilmar Weapons: Rerolling hit roll of 1 -> New roll: {roll}")
        
        if roll >= to_hit_target:
            successful_hits += 1
            if verbose:
                print(f"Hit roll: {roll} vs target {to_hit_target} - Hit!")
        elif verbose:
            print(f"Hit roll: {roll} vs target {to_hit_target} - Miss!")

    return successful_hits


def RollToWound(attacker, defender, num_hits, verbose=False):
    """
    Roll dice to wound based on the attacker's Strength and defender's Toughness.
    Returns a tuple of (total wounds, list of wound rolls that were 6s).
    """
    to_wound_target = Wounds_vs_ToughnessChart[attacker.Strength - 1][
        defender.Toughness - 1
    ]
    if to_wound_target is None:
        if verbose:
            print(f"{attacker.name} is too weak to wound {defender.name}!")
        return 0, []

    successful_wounds = 0
    wound_rolls = []  # Store the roll value for each successful wound
    
    # Check if weapon has Armor Bane
    has_armor_bane = False
    if attacker.Weapon in MeleeWeaponDict:
        special_rules = MeleeWeaponDict[attacker.Weapon][2]
        if special_rules:
            has_armor_bane = any(rule.startswith('AB') for rule in special_rules)
    
    # Check character special rules for Armor Bane
    if attacker.SpecialRules:
        if isinstance(attacker.SpecialRules, list):
            has_armor_bane = has_armor_bane or any(str(rule).startswith('AB') for rule in attacker.SpecialRules)
        elif isinstance(attacker.SpecialRules, str):
            has_armor_bane = has_armor_bane or str(attacker.SpecialRules).startswith('AB')
    
    for hit in range(num_hits):
        roll = np.random.randint(1, 7)  # Roll a D6
        if roll >= to_wound_target:
            successful_wounds += 1
            wound_rolls.append(roll)  # Store the roll value
            if verbose:
                ab_text = " (Armor Bane triggered!)" if (roll == 6 and has_armor_bane) else ""
                print(
                    f"Wound roll: {roll} vs target {to_wound_target} - Wounded!{ab_text}"
                )
        elif verbose:
            print(
                f"Wound roll : {roll} vs target {to_wound_target} - Failed to wound!"
            )

    return successful_wounds, wound_rolls


def RollArmorSave(attacker, defender, num_wounds, wound_rolls=None, verbose=False):
    """
    Roll dice for armor saves.
    Returns the number of wounds saved by armor.
    Takes into account Armor Bane (AB) special rule when wound roll was 6.
    """
    if defender.Armor is None:
        return 0  # No armor, no saves possible

    # Find matching armor key in ArmourDict
    armor_key = None
    for key in ArmourDict:
        if isinstance(key, tuple):
            if defender.Armor in key:
                armor_key = key
                break
        elif defender.Armor == key:
            armor_key = key
            break
    
    if armor_key is None:
        if verbose:
            print(f"Warning: Armor type '{defender.Armor}' not found in ArmourDict")
        return 0
        
    armor_save_target = ArmourDict[armor_key]
    if defender.Shield is not None:
        armor_save_target -= 1  # Shield improves armor save by 1
    
    # Get base armor piercing and AB value if weapon has it
    base_ap = np.abs(attacker.ArmourPiercing)
    ab_value = 0
    
    # Find weapon in MeleeWeaponDict
    weapon_key = None
    for key in MeleeWeaponDict:
        if isinstance(key, tuple):
            if attacker.Weapon in key:
                weapon_key = key
                break
        elif attacker.Weapon == key:
            weapon_key = key
            break
            
    if weapon_key:
        special_rules = MeleeWeaponDict[weapon_key][2]
        if special_rules:
            for rule in special_rules:
                print(rule)
                if rule.startswith('AB'):
                    ab_value = int(rule[2:])  # Extract number from AB1, AB2, etc.
                    
    
    successful_saves = 0
    wound_rolls = wound_rolls if wound_rolls else [0] * num_wounds  # Default to 0 if no wound rolls provided
    
    for wound_index in range(num_wounds):
        current_ap = base_ap
        # If this wound was from a 6 and weapon has Armor Bane, increase AP
        if wound_rolls[wound_index] == 6:
            current_ap += ab_value
        current_save_target = armor_save_target  # Start with base save
        current_save_target += current_ap  # AP makes save harder by increasing target
        
        # Cap minimum save at 2+
        current_save_target = max(2, current_save_target)
            
        if current_save_target > 6:  # No save possible
            if verbose:
                print(f"Armor save roll {wound_index + 1}: No save possible! (Save of {current_save_target}+ required)")
            continue
            
        roll = np.random.randint(1, 7)  # Roll a D6
        if roll >= current_save_target:
            successful_saves += 1
            if verbose:
                print(f"Armor save roll {wound_index + 1}: {roll} vs target {current_save_target}+ - Saved!")
        elif verbose:
            print(f"Armor save roll {wound_index + 1}: {roll} vs target {current_save_target}+ - Failed!")
            
    return successful_saves


def apply_extra_attacks(character):
    """
    Apply any special rules from the character's weapon.
    Returns the modified number of attacks.
    """
    #check weapon for special rules that grant extra attacks
    if character.Weapon in MeleeWeaponDict:
        special_rules = MeleeWeaponDict[character.Weapon][2]
        if special_rules is not None and "+1A" in special_rules:
            return character.Attacks + 1
    return character.Attacks


def apply_weapon_stats(character, is_first_round=False, verbose=False):
    """
    Apply weapon stats and handle special rules based on the round.
    """
    # Find matching armor key in MeleeWeaponDict
    weapon_key = None
    for key in MeleeWeaponDict:
        if isinstance(key, tuple):
            if character.Weapon in key:
                weapon_key = key
                break
        elif character.Weapon == key:
            weapon_key = key
            break
    
    if weapon_key is None:
        if verbose:
            print(f"Warning: Weapon type '{character.Weapon}' not found in MeleeWeaponDict")
        return
    
    weapon_stats = MeleeWeaponDict[weapon_key]
    strength_bonus = weapon_stats[0]
    armor_piercing = weapon_stats[1]
    special_rules = weapon_stats[2] or []

    # Add any character's special rules to the weapon stats
    if character.SpecialRules:
        if isinstance(character.SpecialRules, list):
            special_rules.extend(character.SpecialRules)
        elif isinstance(character.SpecialRules, str):
            special_rules.append(character.SpecialRules)
    
    # Reset to original stats first
    character.Strength = character.original_Strength
    character.ArmourPiercing = character.original_ArmourPiercing
    character.Initiative = character.original_Initiative

    # Handle FirstRoundOnly rule first
    if not is_first_round and FirstRoundOnly in special_rules:
        character.Weapon = "HW"
        if verbose:
            print(f"{character.name} switches to a Hand Weapon after first round.")
        # Recursively apply Hand Weapon stats
        apply_weapon_stats(character, is_first_round, verbose)
        return

    # Apply basic weapon stats
    if strength_bonus:
        character.Strength += strength_bonus
        if verbose:
            print(f"{character.name}'s {character.Weapon} grants +{strength_bonus} Strength")
    
    if armor_piercing:
        character.ArmourPiercing = armor_piercing
        if verbose:
            print(f"{character.name}'s {character.Weapon} has {armor_piercing} Armor Piercing")

    # Handle other special rules
    if special_rules:
        # Handle FirstRoundStr rule
        if FirstRoundStr in special_rules and is_first_round:
            if strength_bonus:
                character.Strength += strength_bonus
                if verbose:
                    print(f"{character.name}'s {character.Weapon} grants additional +{strength_bonus} Strength in the first round!")
        
        # Handle StrikeFirst and StrikeLast
        if StrikeFirst in special_rules and StrikeLast not in special_rules:
            if verbose:
                print(f"{character.name} strikes first with blinding speed using {character.Weapon}!")
            character.Initiative = 10
        elif StrikeLast in special_rules and StrikeFirst not in special_rules:
            if verbose:
                print(f"{character.name} strikes last with {character.Weapon}!")
            character.Initiative = 1
        elif StrikeFirst in special_rules and StrikeLast in special_rules:
            pass  # Both strikes first and last, no change needed
        # No special rules or already handled by base stats above
                    
                    

def reset_weapon_stats(character):
    """
    Reset character stats to their original values and handle weapon transitions.
    """
    weapon_key = None
    for key in MeleeWeaponDict:
        if isinstance(key, tuple):
            if character.Weapon in key:
                weapon_key = key
                break
        elif character.Weapon == key:
            weapon_key = key
            break

    # Check for FirstRoundOnly before resetting stats
    if weapon_key and FirstRoundOnly in MeleeWeaponDict[weapon_key][2]:
        character.Weapon = "HW"  # Switch to Hand Weapon
    
    # Reset stats to original values
    character.Strength = character.original_Strength
    character.ArmourPiercing = character.original_ArmourPiercing
    character.Initiative = character.original_Initiative


def OneRoundMeleeCombat(
    attacker: Character,
    defender: Character,
    verbose=True,
):
    # Apply any special rules that affect number of attacks, armor piercing or strength
    effective_attacks = apply_extra_attacks(attacker)
    attacker.Attacks = effective_attacks

    if verbose:
        print(f"\n{attacker.name} attacks with {attacker.Attacks} attacks!")

    # Roll for hits
    hits = RollToHit(attacker, defender, verbose)
    if verbose:
        print(f"Total hits: {hits}")

    if hits == 0:
        if verbose:
            print(f"{attacker.name} missed all attacks!")

    # Roll for wounds
    wounds, wound_rolls = RollToWound(attacker, defender, hits, verbose)
    if verbose:
        print(f"Total wounds: {wounds}")
    if wounds == 0:
        if verbose:
            print(f"{attacker.name} failed to wound with any hits!")
            return

    # Roll for armor saves
    saves = RollArmorSave(attacker, defender, wounds, wound_rolls, verbose)
    if verbose:
        print(f"Total saves: {saves}")

    # Apply final wounds
    final_wounds = wounds - saves
    if verbose:
        print(f"Final wounds after saves: {final_wounds}")

    defender.Wounds -= final_wounds
    if verbose:
        print(f"{defender.name} has {defender.Wounds} wounds remaining!")


# Making a simple combat simulation function
def combat_simulation(
    character_1: Character,
    character_2: Character,
    rounds=2,
    Shooting=False,
    verbose=True,
):
    # Store original stats
    character_1.original_Strength = character_1.Strength
    character_1.original_Initiative = character_1.Initiative
    character_1.original_Weapon = character_1.Weapon
    character_2.original_Strength = character_2.Strength
    character_2.original_Initiative = character_2.Initiative
    character_2.original_Weapon = character_2.Weapon

    for i in range(rounds):
        is_first_round = (i == 0)
        
        # Apply weapon stats for the current round
        apply_weapon_stats(character_1, is_first_round, verbose)
        apply_weapon_stats(character_2, is_first_round, verbose)
        
        if verbose:
            print("\nThe combat begins!")
            print(f"Round {i + 1} of combat:")
        Simoultaneous = False
        
        # Check for Elf Initiative bonus in first round
        if is_first_round:
            # Check if character_1 is any type of elf
            is_elf_1 = character_1.Race in RACE_NAMES["HIGH_ELVES"] or \
                      character_1.Race in RACE_NAMES["DARK_ELVES"]
            if is_elf_1:
                if character_1.Initiative < 10:  # Ensure Initiative doesn't exceed 10
                    character_1.Initiative += 1
                    if verbose:
                        print(f"{character_1.name} is an Elf, Initiative increased to {character_1.Initiative}")
            
            # Check if character_2 is any type of elf
            is_elf_2 = character_2.Race in RACE_NAMES["HIGH_ELVES"] or \
                      character_2.Race in RACE_NAMES["DARK_ELVES"]
            if is_elf_2:
                if character_2.Initiative < 10:  # Ensure Initiative doesn't exceed 10
                    character_2.Initiative += 1
                    if verbose:
                        print(f"{character_2.name} is an Elf, Initiative increased to {character_2.Initiative}")

        if character_1.Initiative >= character_2.Initiative:
            attacker, defender = character_1, character_2

        elif character_1.Initiative == character_2.Initiative:
            Simoultaneous = True
        else:
            attacker, defender = character_2, character_1

        # If both characters have the same Initiative, they strike at the same time
        if Simoultaneous:
            OneRoundMeleeCombat(defender, attacker, verbose)
            if attacker.Wounds <= 0:
                if verbose:
                    print(
                        f"The warriors strike at the same time:{attacker.name} has been defeated!"
                    )
                break
            elif verbose:
                print(f"{attacker.name} has {attacker.Wounds} wounds remaining!")
                print(f"{defender.name} has {defender.Wounds} wounds remaining!")

        # The attacker attacks first
        OneRoundMeleeCombat(attacker, defender, verbose)
        if defender.Wounds <= 0:
            if verbose:
                print(f"{defender.name} has been defeated, their blood coats the battlefield!")
                print(f"{attacker.name} stands victorious!")
            break
        if verbose:
            print(f"{defender.name} has {defender.Wounds} wounds remaining!")

        # The defender strikes back
        OneRoundMeleeCombat(defender, attacker, verbose)
        if attacker.Wounds <= 0:
            if verbose:
                print(f"{attacker.name} has been defeated, their blood coats the battlefield!")
                print(f"{defender.name} stands victorious!")
            break

        if verbose:
            print("The defender strikes back!")
