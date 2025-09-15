import numpy as np

from armor import *
from character_model import *
from charts import *
from elven_honors import *
from faction_profiles import *
from magic_items import *
from special_rules import FirstRoundOnly, StrikeFirst, StrikeLast
from weapons import get_weapon_special_rules, get_weapon_stats


def RollToHit(attacker: Character, defender: Character, verbose: bool = True, is_first_round: bool = False) -> int:
    """Roll dice for attacker to hit defender based on Weapon Skill comparison.
    
    Args:
        attacker: The attacking Character making the hit rolls
        defender: The defending Character being attacked
        verbose: Whether to print detailed roll results
        is_first_round: Whether this is the first round of combat (affects Hatred)
    
    Returns:
        int: Number of successful hits scored

    Special Rules Handled:
        - Ithilmar Weapons: Reroll hit rolls of 1 when using Hand Weapons
        - RerollHits1: Reroll hit rolls of 1 with any weapon
        - Hatred(X): In first round only, reroll all failed hits vs specified enemy type
    """
    to_hit_target = WeaponSkillChart[attacker.WeaponSkill - 1][defender.WeaponSkill - 1]
    successful_hits = 0

    # Check for reroll abilities
    has_reroll = False
    has_ithilmar = False
    has_hatred = False
    hatred_target = None
    if attacker.SpecialRules:
        has_reroll = RerollHits1 in attacker.SpecialRules
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


def RollToWound(attacker: Character, defender: Character, num_hits: int, verbose: bool = True) -> tuple[int, list[int], bool, int | None, bool, bool]:
    """Roll dice to wound based on Strength vs Toughness comparison.
    
    Args:
        attacker: The attacking Character making wound rolls
        defender: The defending Character being wounded
        num_hits: Number of successful hits to roll for wounds
        verbose: Whether to print detailed roll results
    
    Returns:
        tuple containing:
        - int: Number of wounds caused
        - list[int]: List of successful wound roll values (for Armor Bane)
        - bool: Whether a Killing Blow was triggered
        - int | None: Target number for Killing Blow (usually 6) or None
        - bool: Whether the attack is considered Flaming
        - bool: Whether the attack is considered Magical

    Special Rules Handled:
        - Ethereal: Only magical attacks can wound
        - Killing Blow: Wound rolls of 6 trigger instant death (unless warded)
        - Armor Bane: Track 6s for increased AP
        - Magic/Flaming: Track for ward save interactions
    """
    # Check for Ethereal rule on defender
    is_ethereal = False
    if defender.SpecialRules:
        is_ethereal = Ethereal in defender.SpecialRules

    # Check if attack is magical
    is_magical = False
    # Check if attack is flaming
    is_flaming = False
    # Check attacker's special rules
    if attacker.SpecialRules:
        is_magical = "Magic" in attacker.SpecialRules
        is_flaming = FlamingAttacks in attacker.SpecialRules
    # Check weapon's special rules
    weapon_rules = get_weapon_special_rules(attacker.Weapon)
    if weapon_rules:
        # set flags based on canonical tokens
        if Magic in weapon_rules:
            is_magical = True
        if FlamingAttacks in weapon_rules:
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
            if KillingBlow in attacker.SpecialRules:
                killing_blow_rule = KillingBlow in attacker.SpecialRules
            has_armor_bane = has_armor_bane or any(str(rule).startswith('AB') for rule in attacker.SpecialRules)
        elif isinstance(attacker.SpecialRules, str):
            if attacker.SpecialRules.startswith('KillingBlow'):
                killing_blow_rule = attacker.SpecialRules
            has_armor_bane = has_armor_bane or str(attacker.SpecialRules).startswith('AB')

    if killing_blow_rule:
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

    return successful_wounds, wound_rolls, killing_blow_triggered, killing_blow_value, is_flaming, is_magical


def RollArmorSave(attacker: Character, defender: Character, num_wounds: int, wound_rolls: list[int] | None = None, verbose: bool = True) -> int:
    """Roll armor saves for wounds, accounting for AP and save modifiers.
    
    Args:
        attacker: The attacking Character (for AP and special rules)
        defender: The defending Character making armor saves
        num_wounds: Number of wounds to attempt to save
        wound_rolls: List of the original wound roll values (for Armor Bane)
        verbose: Whether to print detailed roll results
    
    Returns:
        int: Number of wounds successfully saved by armor

    Special Rules Handled:
        - Armor Bane (AB): Increases AP when wound roll was 6
        - AHX: Improves armor save by X
        - ImproveArmor1InCombat: +1 to armor saves in combat
        - Shield: +1 to armor saves if equipped
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
            if ImproveArmor1InCombat in defender.SpecialRules:
                ah_bonus += 1
                
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


def apply_extra_attacks(character: Character) -> int:
    """Calculate total attacks including bonuses from weapon rules and special rules.
    
    Args:
        character: The Character whose attacks are being calculated
    
    Returns:
        int: Total number of attacks (base + bonuses)

    Special Rules Handled:
        - +XA weapon rule: Adds X additional attacks
        - Frenzy: +1 attack
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


def apply_weapon_stats(character: Character, is_first_round: bool = False, verbose: bool = True) -> None:
    """Apply temporary stat modifications from equipped weapon.
    
    Args:
        character: The Character to modify
        is_first_round: Whether this is first round (affects FirstRoundOnly rules)
        verbose: Whether to print modification details

    Effects:
        - Applies weapon strength bonus
        - Applies weapon AP bonus
        - Respects FirstRoundOnly restrictions
        
    Note: Use reset_weapon_stats to revert these changes after combat round.
    """
    try:
        strength_bonus, ap_bonus, weapon_rules = get_weapon_stats(character.Weapon)
    except ValueError:
        # missing weapon — treat as no bonus
        strength_bonus, ap_bonus, weapon_rules = (None, 0, [])
    # Apply strength bonus only if not FirstRoundOnly or if it's the first round
    if strength_bonus is not None:
        if FirstRoundOnly in weapon_rules:
            if is_first_round:
                character.Strength = (character.Strength or 0) + strength_bonus
        else:
            character.Strength = (character.Strength or 0) + strength_bonus
    # Apply armour piercing similarly
    if ap_bonus:
        if FirstRoundOnly in weapon_rules:
            if is_first_round:
                character.ArmourPiercing = (character.ArmourPiercing or 0) + ap_bonus
        else:
            character.ArmourPiercing = (character.ArmourPiercing or 0) + ap_bonus
    # Handle first round only tokens
    if is_first_round and weapon_rules and 'First Round Only' in weapon_rules:
        # Already handled via weapon rules presence; no-op here unless more logic desired
        pass


def reset_weapon_stats(character: Character) -> None:
    """Reset character stats to their original values after weapon modifications.
    
    Args:
        character: The Character whose stats should be reset
        
    Effects:
        - Restores original Strength
        - Restores original ArmourPiercing
        - Restores original Weapon
    """
    character.Strength = getattr(character, 'original_Strength', character.Strength)
    character.ArmourPiercing = getattr(character, 'original_ArmourPiercing', 0)
    character.Weapon = getattr(character, 'original_Weapon', character.Weapon)


def attempt_regeneration_save(defender: Character, num_wounds: int, verbose: bool = True) -> int:
    """Attempt regeneration saves against wounds using best available regeneration.
    
    Args:
        defender: The Character attempting regeneration
        num_wounds: Number of wounds to attempt to regenerate
        verbose: Whether to print detailed roll results
    
    Returns:
        int: Number of wounds successfully regenerated

    Regeneration Sources:
        - RegenX special rule: Regenerate on X+
        Uses the lowest (best) regeneration target if multiple sources exist.
    """
    if not defender.SpecialRules:
        return 0

    # Find regeneration target if any
    regen_target = None
    for rule in defender.SpecialRules:
        rule_str = str(rule)
        if rule_str.startswith('Regen'):
            try:
                target = int(rule_str.replace('Regen', ''))
                if regen_target is None or target < regen_target:
                    regen_target = target
            except ValueError:
                pass

    if regen_target is None:
        return 0

    if verbose:
        print(f"Attempting regeneration save: {regen_target}+ required")

    successful_regens = 0
    for _ in range(num_wounds):
        roll = np.random.randint(1, 7)  # Roll D6
        if roll >= regen_target:
            successful_regens += 1
            if verbose:
                print(f"Regeneration save roll: {roll} vs target {regen_target}+ - Regenerated!")
        elif verbose:
            print(f"Regeneration save roll: {roll} vs target {regen_target}+ - Failed!")

    return successful_regens


def attempt_ward_save(defender: Character, num_wounds: int, is_flaming: bool = False, verbose: bool = False) -> int:
    """Attempt ward saves against wounds using best available ward save.
    
    Args:
        defender: The Character attempting ward saves
        num_wounds: Number of wounds to attempt to save
        is_flaming: Whether the wounds are from a Flaming attack
        verbose: Whether to print detailed roll results
    
    Returns:
        int: Number of wounds successfully saved by wards

    Ward Save Sources (uses lowest applicable target):
        - WardX special rule: Save on X+
        - Witness to Destiny: Save on 6+
        - Dragon Armour: Save on 6+
        - Blessings of Asuryan: Save on 5+ vs Flaming only

    Effects:
        - Sets defender.ward_applied when any ward save succeeds
    """
    if not defender.SpecialRules:
        return 0

    # Find all ward save targets
    ward_targets = []
    for rule in defender.SpecialRules:
        # Check for WardX format
        rule_str = str(rule)
        if rule_str.startswith('Ward'):
            try:
                target = int(rule_str.replace('Ward', ''))
                ward_targets.append(target)
            except ValueError:
                pass
        # Check named ward sources
        elif rule_str == "Witness to Destiny (6+ Ward)" or rule_str == "Dragon Armour (6+ Ward)":
            ward_targets.append(6)
        elif rule_str == "Blessings of Asuryan (5+ Ward vs Flaming)" and is_flaming:
            ward_targets.append(5)

    if not ward_targets:
        return 0  # No applicable ward saves

    # Use lowest valid target
    ward_target = min(ward_targets)
    if verbose:
        print(f"Attempting ward save: {ward_target}+ required")

    successful_wards = 0
    for _ in range(num_wounds):
        roll = np.random.randint(1, 7)  # Roll D6
        if roll >= ward_target:
            successful_wards += 1
            if verbose:
                print(f"Ward save roll: {roll} vs target {ward_target}+ - Saved!")
                defender.ward_applied = True  # Flag that a ward succeeded
        elif verbose:
            print(f"Ward save roll: {roll} vs target {ward_target}+ - Failed!")

    return successful_wards


def OneRoundMeleeCombat(
    attacker: Character,
    defender: Character,
    verbose: bool = True,
    is_first_round: bool = True,
) -> dict[str, int | bool | list[int] | None]:
    """Execute one round of melee combat between two characters.
    
    Args:
        attacker: The Character making the attack
        defender: The Character being attacked
        verbose: Whether to print detailed combat results
        is_first_round: Whether this is first round (affects various rules)
    
    Returns:
        dict containing:
        - hits (int): Number of successful hits
        - wounds (int): Number of wounds after armor saves
        - raw_wounds (int): Number of wounds before armor saves
        - saves (int): Number of successful armor saves
        - killing_blow_triggered (bool): Whether a Killing Blow occurred
        - killing_blow_value (int | None): Target number for Killing Blow
        - is_flaming (bool): Whether the attack was Flaming
        - is_magical (bool): Whether the attack was Magical

    Effects:
        - Temporarily modifies attacker's stats based on weapon
        - Resets attacker's stats after combat
    """
    apply_weapon_stats(attacker, is_first_round=is_first_round)
    hits = RollToHit(attacker, defender, verbose=verbose, is_first_round=is_first_round)
    wounds_info = RollToWound(attacker, defender, hits, verbose=verbose)
    # Unpack minimal expected tuple safely
    if wounds_info is None:
        total_wounds = 0
        wound_rolls = []
        killing_blow_triggered = False
        killing_blow_value = None
        is_flaming = False
        is_magical = False
    else:
        total_wounds = wounds_info[0] if isinstance(wounds_info, tuple) else 0
        wound_rolls = wounds_info[1] if isinstance(wounds_info, tuple) and len(wounds_info) > 1 else []
        killing_blow_triggered = wounds_info[2] if isinstance(wounds_info, tuple) and len(wounds_info) > 2 else False
        killing_blow_value = wounds_info[3] if isinstance(wounds_info, tuple) and len(wounds_info) > 3 else None,
        is_flaming = wounds_info[4] if isinstance(wounds_info, tuple) and len(wounds_info) > 4 else False
        is_magical = wounds_info[5] if isinstance(wounds_info, tuple) and len(wounds_info) > 5 else False


    # Do not auto-kill here; return killing blow info for higher-level resolution
    saves = RollArmorSave(attacker, defender, total_wounds, wound_rolls, verbose=verbose)
    
    # Effective wounds after saves
    effective_wounds = max(0, total_wounds - saves)
    reset_weapon_stats(attacker)
    # Determine if the attack was flaming (weapon or attacker rules)
    is_flaming = False
    try:
        # Check attacker and weapon for flaming
        if attacker.SpecialRules and FlamingAttacks in attacker.SpecialRules:
            is_flaming = True
    except Exception:
        pass
    weapon_rules = get_weapon_special_rules(attacker.Weapon)
    if weapon_rules and FlamingAttacks in weapon_rules:
        is_flaming = True
        
    if weapon_rules and Magic in weapon_rules:
        is_magical = True


    return {
        'hits': hits,
        'wounds': effective_wounds,
        'raw_wounds': total_wounds,
        'saves': saves,
        'killing_blow_triggered': killing_blow_triggered,
        'killing_blow_value': killing_blow_value,
        'is_flaming': is_flaming,
        'magical': is_magical
    }


def combat_simulation(
    character_1: Character,
    character_2: Character,
    rounds: int = 2,
    Shooting: bool = False,
    verbose: bool = True,
) -> Character | None:
    """Simulate a full combat between two characters.
    
    Args:
        character_1: First combatant
        character_2: Second combatant
        rounds: Maximum number of combat rounds
        Shooting: Whether this is a shooting phase (not yet implemented)
        verbose: Whether to print detailed combat results
    
    Returns:
        Character | None: Winning character, or None if combat was a draw
        
    Combat Flow:
        1. Determine strike order (StrikeFirst/Last, Initiative)
        2. Each character attacks in order
        3. For each attack:
            - Roll to hit
            - Roll to wound
            - Apply armor saves
            - Apply ward saves
            - Apply regeneration saves
        4. Apply remaining wounds
        5. Check for victory conditions
    
    Victory Conditions:
        - Instant win on successful Killing Blow (after saves)
        - Win when opponent reaches 0 wounds
        - Most wounds remaining after all rounds
        - Draw if equal wounds remaining
    """
    # Initialize current wounds at start of combat
    character_1.current_wounds = character_1.Wounds
    character_2.current_wounds = character_2.Wounds
    for r in range(rounds):
        if verbose:
            print(f"Round {r+1}")

        # Determine strike order: check StrikeFirst/StrikeLast rules and Initiative
        c1_rules = character_1.SpecialRules if character_1.SpecialRules else []
        c2_rules = character_2.SpecialRules if character_2.SpecialRules else []

        # Decide strike timing this round
        simultaneous_combat = False
        c1_first = False
        c2_first = False
        
        if verbose:
            print("\nDetermining strike order...")

        # Check for Strike First/Last
        c1_strikes_first = 'Strike First' in c1_rules
        c2_strikes_first = 'Strike First' in c2_rules
        c1_strikes_last = 'Strike Last' in c1_rules
        c2_strikes_last = 'Strike Last' in c2_rules

        if c1_strikes_first and c2_strikes_first:
            # Both have Strike First - simultaneous based on Initiative
            if verbose:
                print(f"Both {character_1.name} and {character_2.name} have Strike First")
            if character_1.Initiative == character_2.Initiative:
                simultaneous_combat = True
                if verbose:
                    print("Equal Initiative - both strike simultaneously")
            elif character_1.Initiative > character_2.Initiative:
                c1_first = True
                if verbose:
                    print(f"{character_1.name} has higher Initiative and strikes first")
            else:
                c2_first = True
                if verbose:
                    print(f"{character_2.name} has higher Initiative and strikes first")
        elif c1_strikes_last and c2_strikes_last:
            # Both have Strike Last - simultaneous based on Initiative
            if verbose:
                print(f"Both {character_1.name} and {character_2.name} have Strike Last")
            if character_1.Initiative == character_2.Initiative:
                simultaneous_combat = True
                if verbose:
                    print("Equal Initiative - both strike simultaneously")
            elif character_1.Initiative > character_2.Initiative:
                c1_first = True
                if verbose:
                    print(f"{character_1.name} has higher Initiative and strikes first")
            else:
                c2_first = True
                if verbose:
                    print(f"{character_2.name} has higher Initiative and strikes first")
        elif c1_strikes_first and not c2_strikes_first:
            c1_first = True
            if verbose:
                print(f"{character_1.name} has Strike First and {character_2.name} doesn't - {character_1.name} strikes first")
        elif c2_strikes_first and not c1_strikes_first:
            c2_first = True
            if verbose:
                print(f"{character_2.name} has Strike First and {character_1.name} doesn't - {character_2.name} strikes first")
        elif c1_strikes_last and not c2_strikes_last:
            c1_first = False
            if verbose:
                print(f"{character_1.name} has Strike Last and must strike after {character_2.name}")
        elif c2_strikes_last and not c1_strikes_last:
            c2_first = False
            if verbose:
                print(f"{character_2.name} has Strike Last and must strike after {character_1.name}")
        else:
            # No Strike First/Last - fall back to Initiative
            if verbose:
                print("No Strike First/Last rules - comparing Initiative values")
                print(f"{character_1.name}: Initiative {character_1.Initiative}")
                print(f"{character_2.name}: Initiative {character_2.Initiative}")
            
            if character_1.Initiative == character_2.Initiative:
                simultaneous_combat = True
                if verbose:
                    print("Equal Initiative - both strike simultaneously")
            elif character_1.Initiative > character_2.Initiative:
                c1_first = True
                if verbose:
                    print(f"{character_1.name} has higher Initiative and strikes first")
            else:
                c2_first = True
                if verbose:
                    print(f"{character_2.name} has higher Initiative and strikes first")

        # Create list of attackers and track pending strikes
        order = []
        if simultaneous_combat:
            # Both strike at once - calculate all results before applying any
            pending_results = []
            
            # Both characters strike
            if verbose:
                print(f"\nSimultaneous combat round - both fighters strike before wounds are applied")
            
            # First character strikes
            if verbose:
                print(f"\n{character_1.name} strikes:")
            result1 = OneRoundMeleeCombat(character_1, character_2, verbose=verbose, is_first_round=(r==0))
            pending_results.append((character_1, character_2, result1))
            
            # Second character strikes
            if verbose:
                print(f"\n{character_2.name} strikes:")
            result2 = OneRoundMeleeCombat(character_2, character_1, verbose=verbose, is_first_round=(r==0))
            pending_results.append((character_2, character_1, result2))
            
            if verbose:
                print("\nApplying all combat results:")
            
            # Now apply all results
            for attacker, defender, result in pending_results:
                if verbose:
                    print(f"{attacker.name} vs {defender.name}: {result}")
                if result:
                    defender.current_wounds = max(0, defender.current_wounds - result)
        else:
            # Normal sequential combat
            if c1_first:
                order = [(character_1, character_2), (character_2, character_1)]
            else:
                order = [(character_2, character_1), (character_1, character_2)]
                
            # Execute strikes in order
            for attacker, defender in order:
                if verbose:
                    print(f"\n{attacker.name} strikes at {defender.name}!")
                result = OneRoundMeleeCombat(attacker, defender, verbose=verbose, is_first_round=(r==0))
                if result:
                    wounds = result['wounds'] if isinstance(result, dict) else result
                    if wounds and verbose:
                        print(f"{defender.name} takes {wounds} wounds!")
                    defender.current_wounds = max(0, defender.current_wounds - wounds)
            if verbose:
                print(f"{attacker.name} strikes at {defender.name}!")
            result = OneRoundMeleeCombat(attacker, defender, verbose=verbose, is_first_round=(r==0))
            # Process wounds and killing blows
            wounds = result.get('wounds', 0) if isinstance(result, dict) else 0
            is_flaming = result.get('is_flaming', False) if isinstance(result, dict) else False
            killing_blow = result.get('killing_blow_triggered', False) if isinstance(result, dict) else False

            # First handle potential killing blow
            if killing_blow:
                if verbose:
                    print(f"Killing Blow triggered against {defender.name}!")
                # First attempt ward save against the killing blow
                wards_vs_killing = attempt_ward_save(defender, 1, is_flaming, verbose)
                if wards_vs_killing:
                    if verbose:
                        print(f"{defender.name} wards off the Killing Blow!")
                    # Killing blow warded; proceed with normal wound resolution
                else:
                    # Attempt regeneration save against the killing blow
                    regen_vs_killing = attempt_regeneration_save(defender, 1, verbose)
                    if regen_vs_killing:
                        if verbose:
                            print(f"{defender.name} regenerates from the Killing Blow!")
                        # Killing blow regenerated; proceed with normal wound resolution
                    else:
                        # Neither ward nor regeneration succeeded - instant death
                        defender.Wounds = 0
                        winner = attacker
                        loser = defender
                        print(f"{winner.name} stands victorious, the blood of {loser.name} stains the field of battle")
                        return winner

            # Handle regular wounds (if no killing blow or it was warded)
            if wounds:
                # First attempt ward saves against regular wounds
                wounds_after_wards = wounds - attempt_ward_save(defender, wounds, is_flaming, verbose)
                
                # Then attempt regeneration for any wounds that weren't warded
                if wounds_after_wards > 0:
                    wounds_after_regen = wounds_after_wards - attempt_regeneration_save(defender, wounds_after_wards, verbose)
                    
                    # Apply any wounds that weren't warded or regenerated
                    if wounds_after_regen > 0:
                        defender.Wounds = max(0, defender.Wounds - wounds_after_regen)
                        if verbose:
                            saved_wounds = wounds - wounds_after_regen
                            if saved_wounds > 0:
                                print(f"{defender.name} saved {saved_wounds} wound(s) through wards/regeneration.")
                            print(f"{defender.name} suffers {wounds_after_regen} wound(s). Remaining Wounds: {defender.Wounds}")

            # Check if defender died from regular wounds
            if defender.Wounds <= 0:
                winner = attacker
                loser = defender
                print(f"{winner.name} stands victorious, the blood of {loser.name} stains the field of battle")
                return winner

    # No decisive winner after rounds
    if character_1.current_wounds > character_2.current_wounds:
        winner = character_1
        loser = character_2
    elif character_2.current_wounds > character_1.current_wounds:
        winner = character_2
        loser = character_1
    else:
        # Tie -> no one stands victorious
        if verbose:
            print("The battle ends in a bloody stalemate.")
        return None

    print(f"{winner.name} stands victorious, the blood of {loser.name} stains the field of battle")
    return winner
