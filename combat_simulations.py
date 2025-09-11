import numpy as np

from armor import *
from character_model import *
from charts import *
from elven_honors import *
from faction_profiles import *
from magic_items import *
from weapons import get_weapon_special_rules, get_weapon_stats


def RollToHit(attacker, defender, verbose=False, is_first_round=False):
    """
    Roll dice to hit based on the attacker's Weapon Skill and defender's Weapon Skill.
    Returns the number of successful hits.
    Handles Ithilmar Weapons special rule (reroll 1s with Hand Weapons),
    RerollHits1 special rule (reroll 1s with any weapon),
    and Hatred(X) special rule (reroll all failed hits vs hated enemies in first round).
    """
    to_hit_target = WeaponSkillChart[attacker.WeaponSkill - 1][defender.WeaponSkill - 1]
    successful_hits = 0

    # Check for reroll abilities
    has_reroll = False
    has_ithilmar = False
    has_hatred = False
    hatred_target = None
    if attacker.SpecialRules:
        has_reroll = "RerollHits1" in attacker.SpecialRules
        has_ithilmar = IthilmarWeapons in attacker.SpecialRules
        for rule in attacker.SpecialRules:
            if str(rule).startswith("Hatred"):
                has_hatred = True
                hatred_target = rule

    # Determine if defender is hated
    is_hated_enemy = False
    if has_hatred and hatred_target:
        # Hatred (all) or Hatred (X)
        if hatred_target.strip().lower() == "hatred (all)":
            is_hated_enemy = True
        elif "(" in hatred_target and ")" in hatred_target:
            # Extract the race or type from Hatred (X)
            hated_str = hatred_target[hatred_target.find("(")+1:hatred_target.find(")")].strip().lower()
            # Defender's race or name
            defender_race = getattr(defender, "Race", "").lower() if getattr(defender, "Race", None) else ""
            defender_name = getattr(defender, "name", "").lower() if getattr(defender, "name", None) else ""
            if hated_str and (hated_str in defender_race or hated_str in defender_name):
                is_hated_enemy = True

    for attack in range(attacker.Attacks):
        roll = np.random.randint(1, 7)  # Roll a D6
        # Check if a reroll is allowed
        can_reroll_1 = has_reroll or (has_ithilmar and attacker.Weapon == "HW")
        # If roll is 1 and has reroll ability, reroll
        if roll == 1 and can_reroll_1:
            old_roll = roll
            roll = np.random.randint(1, 7)  # Reroll
            if verbose:
                if has_reroll:
                    print(f"RerollHits1: Rerolling hit roll of 1 -> New roll: {roll}")
                else:
                    print(f"Ithilmar Weapons: Rerolling hit roll of 1 -> New roll: {roll}")
        if roll >= to_hit_target:
            successful_hits += 1
            if verbose:
                print(f"Hit roll: {roll} vs target {to_hit_target} - Hit!")
        elif is_first_round and is_hated_enemy:
            # Hatred: reroll failed hit in first round
            reroll = np.random.randint(1, 7)
            if verbose:
                print(f"Hatred: Rerolling failed hit roll of {roll} -> New roll: {reroll}")
            # Reroll 1s if reroll abilities apply
            if reroll == 1 and can_reroll_1:
                old_reroll = reroll
                reroll = np.random.randint(1, 7)
                if verbose:
                    if has_reroll:
                        print(f"RerollHits1: Rerolling hit roll of 1 on hatred reroll -> New roll: {reroll}")
                    else:
                        print(f"Ithilmar Weapons: Rerolling hit roll of 1 on hatred reroll -> New roll: {reroll}")
            if reroll >= to_hit_target:
                successful_hits += 1
                if verbose:
                    print(f"Hatred reroll: {reroll} vs target {to_hit_target} - Hit!")
            elif verbose:
                print(f"Hatred reroll: {reroll} vs target {to_hit_target} - Miss!")
        elif verbose:
            print(f"Hit roll: {roll} vs target {to_hit_target} - Miss!")
    return successful_hits


def RollToWound(attacker, defender, num_hits, verbose=False):
    """
    Roll dice to wound based on the attacker's Strength and defender's Toughness.
    Returns a tuple of (total wounds, list of wound rolls that were 6s, killing_blow_triggered, killing_blow_value).
    Handles Ethereal rule: only magical attacks can wound Ethereal targets.
    """
    # Check for Ethereal rule on defender
    is_ethereal = False
    if defender.SpecialRules:
        is_ethereal = "Ethereal" in defender.SpecialRules

    # Check if attack is magical
    is_magical = False
    # Check if attack is flaming
    is_flaming = False
    # Check attacker's special rules
    if attacker.SpecialRules:
        is_magical = "Magic" in attacker.SpecialRules
        is_flaming = "Flaming" in attacker.SpecialRules
    # Check weapon's special rules
    weapon_rules = get_weapon_special_rules(attacker.Weapon)
    if weapon_rules:
        # set flags based on canonical tokens
        if "Magic" in weapon_rules:
            is_magical = True
        if "Flaming Attacks" in weapon_rules or "Flaming" in weapon_rules:
            is_flaming = True

    # If defender is Ethereal and attack is not magical, no wounds can be caused
    if is_ethereal and not is_magical:
        if verbose:
            print(f"{defender.name} is Ethereal and can only be wounded by magical attacks!")
        return 0, [], False, None

    to_wound_target = Wounds_vs_ToughnessChart[attacker.Strength - 1][
        defender.Toughness - 1
    ]
    if to_wound_target is None:
        if verbose:
            print(f"{attacker.name} is too weak to wound {defender.name}!")
        return 0, [], False, None

    successful_wounds = 0
    wound_rolls = []  # Store the roll value for each successful wound
    killing_blow_triggered = False
    killing_blow_value = None

    # Check if weapon has Armor Bane
    weapon_rules = get_weapon_special_rules(attacker.Weapon)
    has_armor_bane = any(str(r).startswith("AB") for r in weapon_rules) if weapon_rules else False
    
    
    # Check character special rules for Armor Bane and Killing Blow
    killing_blow_rule = None
    if attacker.SpecialRules:
        if isinstance(attacker.SpecialRules, list):
            for rule in attacker.SpecialRules:
                if str(rule).startswith('KillingBlow'):
                    killing_blow_rule = rule
            has_armor_bane = has_armor_bane or any(str(rule).startswith('AB') for rule in attacker.SpecialRules)
        elif isinstance(attacker.SpecialRules, str):
            if attacker.SpecialRules.startswith('KillingBlow'):
                killing_blow_rule = attacker.SpecialRules
            has_armor_bane = has_armor_bane or str(attacker.SpecialRules).startswith('AB')

    if killing_blow_rule:
        try:
            killing_blow_value = int(str(killing_blow_rule).replace('KillingBlow',''))
        except Exception:
            killing_blow_value = 6  # fallback

    for hit in range(num_hits):
        roll = np.random.randint(1, 7)  # Roll a D6
        if roll >= to_wound_target:
            successful_wounds += 1
            wound_rolls.append(roll)  # Store the roll value
            # Check for Killing Blow
            if killing_blow_value and roll == 6:
                killing_blow_triggered = True
                if verbose:
                    print(f"Killing Blow triggered! Wound roll: 6. {defender.name} will be instantly killed unless a Ward save is made.")
            else:
                if verbose:
                    ab_text = " (Armor Bane triggered!)" if (roll == 6 and has_armor_bane) else ""
                    print(
                        f"Wound roll: {roll} vs target {to_wound_target} - Wounded!{ab_text}"
                    )
        elif verbose:
            print(
                f"Wound roll : {roll} vs target {to_wound_target} - Failed to wound!"
            )

    return successful_wounds, wound_rolls, killing_blow_triggered, killing_blow_value


def RollArmorSave(attacker, defender, num_wounds, wound_rolls=None, verbose=False):
    """
    Roll dice for armor saves.
    Returns the number of wounds saved by armor.
    Takes into account Armor Bane (AB) special rule when wound roll was 6.
    Also applies 'AHX' special rule (improves armor save by X).
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
            print(f"{defender.name} has unknown armor type: {defender.Armor}")
        return 0

    armor_save_target = ArmourDict[armor_key]
    if defender.Shield is not None:
        armor_save_target -= 1  # Shield improves armor save by 1

    # Check for 'AHX' special rule (improves armor save by X)
    ah_bonus = 0
    if defender.SpecialRules:
        for rule in defender.SpecialRules:
            if str(rule).startswith('AH'):
                try:
                    ah_bonus += int(str(rule).replace('AH',''))
                except Exception:
                    pass
    armor_save_target -= ah_bonus  # Lower is better

    # Get base armor piercing and AB value if weapon has it
    base_ap = np.abs(attacker.ArmourPiercing)
    ab_value = 0

    # Use helper to inspect weapon stats and rules for AB and Killing Blow parsing
    try:
        strength_bonus, ap_bonus, weapon_rules = get_weapon_stats(attacker.Weapon)
    except ValueError:
        # If weapon not found, fall back to defaults and continue (warn)
        print(f"Warning: Weapon '{getattr(attacker, 'Weapon', None)}' not found; using defaults")
        strength_bonus, ap_bonus, weapon_rules = (None, 0, [])
                
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
    Apply any special rules from the character's weapon or profile.
    Returns the modified number of attacks.
    """
    extra_attacks = 0
    # Check weapon for special rules that grant extra attacks
    weapon_rules = get_weapon_special_rules(character.Weapon)
    if weapon_rules:
        # Example: "+1A" tokens
        for r in weapon_rules:
            if isinstance(r, str) and r.startswith("+") and r.endswith("A"):
                try:
                    extra_attacks += int(r[1:-1])
                except ValueError:
                    pass
    # Check for Frenzy special rule
    if character.SpecialRules:
        if 'Frenzy' in character.SpecialRules:
            extra_attacks += 1
    return character.Attacks + extra_attacks


def apply_weapon_stats(character, is_first_round=False, verbose=False):
    """Apply weapon-derived temporary stats (strength bonus, AP) to character for a round."""
    try:
        strength_bonus, ap_bonus, weapon_rules = get_weapon_stats(character.Weapon)
    except ValueError:
        # missing weapon — treat as no bonus
        strength_bonus, ap_bonus, weapon_rules = (None, 0, [])
    # Apply strength bonus if present
    if strength_bonus is not None:
        character.Strength = (character.Strength or 0) + strength_bonus
    # Apply armour piercing as negative to ArmourPiercing field
    character.ArmourPiercing = (character.ArmourPiercing or 0) + ap_bonus
    # Handle first round only tokens
    if is_first_round and weapon_rules and 'First Round Only' in weapon_rules:
        # Already handled via weapon rules presence; no-op here unless more logic desired
        pass


def reset_weapon_stats(character):
    # Reset any temporary modifications applied by apply_weapon_stats
    character.Strength = getattr(character, 'original_Strength', character.Strength)
    character.ArmourPiercing = getattr(character, 'original_ArmourPiercing', 0)
    character.Weapon = getattr(character, 'original_Weapon', character.Weapon)


def OneRoundMeleeCombat(
    attacker: Character,
    defender: Character,
    verbose=True,
    is_first_round=True,
):
    # Minimal skeleton that applies weapon stats, computes hits/wounds/saves
    apply_weapon_stats(attacker, is_first_round=is_first_round)
    hits = RollToHit(attacker, defender, verbose=verbose, is_first_round=is_first_round)
    wounds_info = RollToWound(attacker, defender, hits, verbose=verbose)
    # Unpack minimal expected tuple safely
    if wounds_info is None:
        total_wounds = 0
        wound_rolls = []
    else:
        total_wounds = wounds_info[0] if isinstance(wounds_info, tuple) else 0
        wound_rolls = wounds_info[1] if isinstance(wounds_info, tuple) and len(wounds_info) > 1 else []
    saves = RollArmorSave(attacker, defender, total_wounds, wound_rolls, verbose=verbose)
    reset_weapon_stats(attacker)
    return {'hits': hits, 'wounds': total_wounds, 'saves': saves}


# Making a simple combat simulation function
def combat_simulation(
    character_1: Character,
    character_2: Character,
    rounds=2,
    Shooting=False,
    verbose=True,
):
    # Very small simulation loop
    for r in range(rounds):
        if verbose:
            print(f"Round {r+1}")
        OneRoundMeleeCombat(character_1, character_2, verbose=verbose, is_first_round=(r==0))
        OneRoundMeleeCombat(character_2, character_1, verbose=verbose, is_first_round=(r==0))
    return True
