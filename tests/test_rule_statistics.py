"""Special rules measured against their exact probabilities.

Scripted-dice tests pin a rule's mechanics roll by roll; these check the same
rules in aggregate, so a rule that fires at the wrong rate - rerolling twice,
applying in the wrong round, stacking when it should not - shows up as a
proportion outside its confidence band. Each expected value is worked out by
hand in the comment beside it.
"""

from __future__ import annotations

import unittest

from support import SAMPLES_LARGE, SAMPLES_SMALL, StatisticalCase, fighter, win_rates

import dice
from combat_simulations import (
    RollArmorSave,
    RollToHit,
    RollToWound,
    StrikeResult,
    Wound,
    resolve_strike,
)
from combat_simulations import test_primal_fury as roll_primal_fury

N = SAMPLES_LARGE * 5  # single dice are cheap, so sample generously


def hit_rate(attacker, defender, first_round=False, trials=N, seed=0):
    dice.seed(seed)
    hits = sum(
        RollToHit(attacker, defender, verbose=False, is_first_round=first_round)
        for _ in range(trials)
    )
    return hits / (trials * attacker.Attacks)


def wound_outcomes(attacker, defender, first_round=False, trials=N, seed=0):
    """(fraction wounding, fraction of wounds that are Killing Blows)."""
    dice.seed(seed)
    wounds = killing = 0
    for _ in range(trials):
        rolled, _, _ = RollToWound(attacker, defender, 1, verbose=False,
                                   is_first_round=first_round)
        wounds += len(rolled)
        killing += sum(w.killing_blow for w in rolled)
    return wounds / trials, (killing / wounds if wounds else 0.0)


def save_rate(attacker, defender, wound_rolls, trials=N, seed=0):
    dice.seed(seed)
    saved = 0
    for i in range(trials):
        wound = Wound(roll=wound_rolls[i % len(wound_rolls)])
        saved += not RollArmorSave(attacker, defender, [wound], verbose=False)
    return saved / trials


def damage_rate(defender, result, trials=N, seed=0):
    """Mean wounds taken per unsaved wound in `result`."""
    dice.seed(seed)
    total = 0
    for _ in range(trials):
        defender.current_wounds = 100
        taken, _ = resolve_strike(defender, result, verbose=False)
        total += taken
    return total / trials


class TestToHit(StatisticalCase):
    def test_equal_weapon_skill_hits_half_the_time(self):
        self.assertProportion(hit_rate(fighter(Attacks=1), fighter()), 1 / 2, N)

    def test_reroll_hits_of_one(self):
        # 1/2 + P(1) * 1/2 = 7/12
        a = fighter(Attacks=1, SpecialRules=["Reroll Hits 1"])
        self.assertProportion(hit_rate(a, fighter()), 7 / 12, N)

    def test_ithilmar_weapons_need_a_hand_weapon(self):
        elf = fighter(Attacks=1, SpecialRules=["Ithilmar Weapons"])
        self.assertProportion(hit_rate(elf, fighter()), 7 / 12, N)
        elf = fighter(Attacks=1, SpecialRules=["Ithilmar Weapons"], Weapon="Great Weapon")
        self.assertProportion(hit_rate(elf, fighter()), 1 / 2, N)

    def test_hatred_rerolls_misses_in_the_first_round_only(self):
        # 1/2 + 1/2 * 1/2 = 3/4 in the first round
        a = fighter(Attacks=1, SpecialRules=["Hatred (all enemies)"])
        self.assertProportion(hit_rate(a, fighter(), first_round=True), 3 / 4, N)
        self.assertProportion(hit_rate(a, fighter(), first_round=False), 1 / 2, N)

    def test_hatred_and_reroll_ones_combine(self):
        # A 1 is rerolled for Reroll Hits 1 (7/12 hit); Hatred then rerolls a
        # remaining miss, which may itself reroll a 1: 7/12 + 5/12 * 7/12.
        a = fighter(Attacks=1, SpecialRules=["Hatred (all enemies)", "Reroll Hits 1"])
        self.assertProportion(hit_rate(a, fighter(), first_round=True),
                              7 / 12 + 5 / 12 * 7 / 12, N)

    def test_a_forced_reroll_costs_the_first_hit_of_the_round(self):
        # One attack: it must hit twice, 1/2 * 1/2.
        defender = fighter(SpecialRules=["Force Reroll of One Successful Hit"])
        self.assertProportion(hit_rate(fighter(Attacks=1), defender), 1 / 4, N)
        # Two attacks: the first hits 1/4 of the time and uses up the reroll
        # whenever its first roll hit (1/2). The second then hits 1/2 if the
        # reroll is gone, else 1/4: 3/8. Mean per attack (1/4 + 3/8) / 2 = 5/16.
        self.assertProportion(hit_rate(fighter(Attacks=2), defender), 5 / 16, N)

    def test_primal_fury_passes_at_the_two_dice_rate(self):
        # Ld7 on 2D6: 21/36. Blood Rage frenzies on a passed double: 3/36.
        beast = fighter(Leadership=7, SpecialRules=["Primal Fury", "Blood Rage"])
        dice.seed(0)
        passes = frenzies = 0
        for _ in range(N):
            passed, frenzied = roll_primal_fury(beast, verbose=False)
            passes += passed
            frenzies += frenzied
        self.assertProportion(passes / N, 21 / 36, N)
        self.assertProportion(frenzies / N, 3 / 36, N)


class TestToWound(StatisticalCase):
    def test_equal_strength_and_toughness_wound_half_the_time(self):
        self.assertProportion(wound_outcomes(fighter(), fighter())[0], 1 / 2, N)

    def test_murderous_rerolls_ones_with_a_hand_weapon_only(self):
        a = fighter(SpecialRules=["Murderous"])
        self.assertProportion(wound_outcomes(a, fighter())[0], 7 / 12, N)
        a = fighter(SpecialRules=["Murderous"], Weapon="Halberd")
        self.assertProportion(wound_outcomes(a, fighter())[0], 1 / 2, N)

    def test_choppas_reroll_ones_on_the_charge_only(self):
        a = fighter(SpecialRules=["Choppas"])
        self.assertProportion(wound_outcomes(a, fighter(), first_round=True)[0], 7 / 12, N)
        self.assertProportion(wound_outcomes(a, fighter(), first_round=False)[0], 1 / 2, N)

    def test_a_third_of_wounds_are_killing_blows_at_s4_t4(self):
        # Wounds on 4, 5, 6 - one in three is a natural 6.
        a = fighter(SpecialRules=["Killing Blow"])
        rate, killing = wound_outcomes(a, fighter())
        self.assertProportion(rate, 1 / 2, N)
        self.assertProportion(killing, 1 / 3, int(N * rate))

    def test_killing_blow_five_up_is_two_thirds_of_wounds(self):
        a = fighter(SpecialRules=["Killing Blow 5+"])
        rate, killing = wound_outcomes(a, fighter())
        self.assertProportion(killing, 2 / 3, int(N * rate))

    def test_killing_blow_never_triggers_against_a_monster(self):
        a = fighter(SpecialRules=["Killing Blow"])
        monster = fighter()
        monster.TroopType = "Behemoth"
        self.assertEqual(wound_outcomes(a, monster, trials=SAMPLES_SMALL)[1], 0.0)

    def test_ethereal_is_only_wounded_by_magic(self):
        ghost = fighter(SpecialRules=["Ethereal"])
        self.assertEqual(wound_outcomes(fighter(), ghost, trials=SAMPLES_SMALL)[0], 0.0)
        wizard = fighter(SpecialRules=["Magical Attacks"])
        self.assertProportion(wound_outcomes(wizard, ghost)[0], 1 / 2, N)


class TestArmour(StatisticalCase):
    ORDINARY = [4, 5, 6]  # the wound rolls that succeed at S4 v T4

    def test_heavy_armour_saves_a_third(self):
        target = fighter(Armor="Heavy Armor")
        self.assertProportion(save_rate(fighter(), target, self.ORDINARY), 1 / 3, N)

    def test_a_shield_improves_heavy_armour_to_a_half(self):
        target = fighter(Armor="Heavy Armor", Shield=True)
        self.assertProportion(save_rate(fighter(), target, self.ORDINARY), 1 / 2, N)

    def test_gromril_armour_rerolls_ones(self):
        # 1/3 + 1/6 * 1/3 = 7/18
        dwarf = fighter(Armor="Heavy Armor", SpecialRules=["Gromril Armour"])
        self.assertProportion(save_rate(fighter(), dwarf, self.ORDINARY), 7 / 18, N)

    def test_armour_bane_only_bites_on_a_six(self):
        # Plate 4+; on a wound roll of 6, AB1 makes it 5+.
        # 2/3 * 1/2 + 1/3 * 1/3 = 4/9
        attacker = fighter(SpecialRules=["Armour Bane (1)"])
        target = fighter(Armor="Plate Armor")
        self.assertProportion(save_rate(attacker, target, self.ORDINARY), 4 / 9, N)

    def test_weapon_armour_piercing_is_applied_during_a_strike(self):
        # A Halberd is AP -1: plate 4+ becomes 5+, and its AB1 makes a 6 a 6+.
        from combat_simulations import apply_weapon_stats, reset_weapon_stats

        attacker = fighter(Weapon="Halberd")
        apply_weapon_stats(attacker, verbose=False)
        try:
            rate = save_rate(attacker, fighter(Armor="Plate Armor"), self.ORDINARY)
        finally:
            reset_weapon_stats(attacker)
        self.assertProportion(rate, 2 / 3 * 1 / 3 + 1 / 3 * 1 / 6, N)

    def test_killing_blow_allows_no_armour_save(self):
        target = fighter(Armor="Plate Armor", Shield=True)
        dice.seed(0)
        unsaved = RollArmorSave(fighter(), target,
                                [Wound(roll=6, killing_blow=True)] * 100, verbose=False)
        self.assertEqual(len(unsaved), 100)


class TestWardsAndRegeneration(StatisticalCase):
    def one_wound(self, **kwargs):
        return StrikeResult(unsaved=[Wound(roll=4)], **kwargs)

    def test_a_five_up_ward_saves_a_third(self):
        target = fighter(Wounds=100, SpecialRules=["Ward5"])
        self.assertProportion(damage_rate(target, self.one_wound()), 2 / 3, N)

    def test_ward_then_regeneration_both_apply(self):
        # Survives the ward 2/3 of the time, then regeneration 2/3: 4/9.
        target = fighter(Wounds=100, SpecialRules=["Ward5", "Regen5"])
        self.assertProportion(damage_rate(target, self.one_wound()), 4 / 9, N)

    def test_the_best_ward_is_used_not_both(self):
        target = fighter(Wounds=100, SpecialRules=["Ward6", "Ward4"])
        self.assertProportion(damage_rate(target, self.one_wound()), 1 / 2, N)

    def test_a_flaming_only_ward_ignores_ordinary_attacks(self):
        target = fighter(Wounds=100, SpecialRules=["Ward5 (Flaming)"])
        self.assertProportion(damage_rate(target, self.one_wound()), 1.0, N)
        self.assertProportion(damage_rate(target, self.one_wound(is_flaming=True)), 2 / 3, N)

    def test_the_daemonic_ward_ignores_magical_attacks(self):
        daemon = fighter(Wounds=100, SpecialRules=["Ward5 (non-magical)"])
        self.assertProportion(damage_rate(daemon, self.one_wound()), 2 / 3, N)
        self.assertProportion(damage_rate(daemon, self.one_wound(is_magical=True)), 1.0, N)

    def test_flammable_loses_regeneration_against_fire(self):
        troll = fighter(Wounds=100, SpecialRules=["Regen4", "Flammable"])
        self.assertProportion(damage_rate(troll, self.one_wound()), 1 / 2, N)
        self.assertProportion(damage_rate(troll, self.one_wound(is_flaming=True)), 1.0, N)

    def test_multiple_wounds_d3_averages_two(self):
        target = fighter(Wounds=100)
        rate = damage_rate(target, self.one_wound(multiple_wounds="D3"))
        # D3 has mean 2 and variance 2/3; allow four standard errors.
        self.assertAlmostEqual(rate, 2.0, delta=4 * (2 / 3 / N) ** 0.5)

    def test_multiple_wounds_ward_only_applies_to_multiple_wounds(self):
        # The Armour of Skaldour: Ward4 (Killing Blow, Multiple Wounds).
        king = fighter(Wounds=100, SpecialRules=["Ward4 (Killing Blow, Multiple Wounds)"])
        self.assertProportion(damage_rate(king, self.one_wound()), 1.0, N)
        rate = damage_rate(king, self.one_wound(multiple_wounds=2))
        self.assertAlmostEqual(rate, 1.0, delta=4 * (1 / N) ** 0.5)  # 1/2 of 2 wounds


class TestItemRules(StatisticalCase):
    """Rules introduced for magic items, runes and abilities."""

    def test_poisoned_attacks_add_two_to_wound_on_a_natural_six(self):
        # S3 v T4 wounds on 5+ (1/3). A poisoned hit needs 3+ (a natural 1
        # still fails): 2/3.
        a = fighter(Strength=3)
        dice.seed(0)
        plain = sum(len(RollToWound(a, fighter(), 1, verbose=False)[0]) for _ in range(N)) / N
        poisoned = sum(len(RollToWound(a, fighter(), 1, verbose=False, poisoned_hits=1)[0])
                       for _ in range(N)) / N
        self.assertProportion(plain, 1 / 3, N)
        self.assertProportion(poisoned, 2 / 3, N)

    def test_poison_does_not_work_with_a_magic_weapon(self):
        # RollToWound alone does not apply the weapon's S+1, so this is S3 v T4
        # (5+, 1/3); with the poison bonus it would be 2/3.
        a = fighter(Strength=3, Weapon="Sword of Might")
        dice.seed(0)
        rate = sum(len(RollToWound(a, fighter(), 1, verbose=False, poisoned_hits=1)[0])
                   for _ in range(N)) / N
        self.assertProportion(rate, 1 / 3, N)

    def test_poisoned_attacks_in_a_whole_strike(self):
        # WS4 v WS4, S3 v T4. Per attack: 1/6 poisoned hit wounding on 3+,
        # plus 2/6 ordinary hits wounding on 5+: 1/6*2/3 + 2/6*1/3 = 2/9.
        from combat_simulations import OneRoundMeleeCombat
        a = fighter(Strength=3, Attacks=1, SpecialRules=["Poisoned Attacks"])
        dice.seed(0)
        wounds = sum(OneRoundMeleeCombat(a, fighter(), verbose=False, is_first_round=False).raw_wounds
                     for _ in range(N)) / N
        self.assertProportion(wounds, 2 / 9, N)

    def test_to_hit_modifiers(self):
        self.assertProportion(hit_rate(fighter(Attacks=1, SpecialRules=["To Hit (+1)"]), fighter()),
                              2 / 3, N)
        target = fighter(SpecialRules=["Enemy To Hit (-1)"])
        self.assertProportion(hit_rate(fighter(Attacks=1), target), 1 / 3, N)

    def test_a_natural_six_always_hits_and_a_natural_one_always_misses(self):
        hopeless = fighter(SpecialRules=["Enemy To Hit (-1)", "Enemy To Hit (-1)", "Enemy To Hit (-1)"])
        self.assertProportion(hit_rate(fighter(Attacks=1, WeaponSkill=1), hopeless), 1 / 6, N)
        certain = fighter(Attacks=1, WeaponSkill=10, SpecialRules=["To Hit (+1)", "To Hit (+1)"])
        self.assertProportion(hit_rate(certain, fighter(WeaponSkill=1)), 5 / 6, N)

    def test_rerolling_failed_hits_and_wounds(self):
        self.assertProportion(
            hit_rate(fighter(Attacks=1, SpecialRules=["Reroll Failed Hits"]), fighter()), 3 / 4, N)
        self.assertProportion(
            wound_outcomes(fighter(SpecialRules=["Reroll Failed Wounds"]), fighter())[0], 3 / 4, N)
        self.assertProportion(
            wound_outcomes(fighter(SpecialRules=["Reroll Wounds 1"]), fighter())[0], 7 / 12, N)

    def test_enemies_reroll_their_successes(self):
        self.assertProportion(
            hit_rate(fighter(Attacks=1), fighter(SpecialRules=["Enemy Rerolls Successful Hits"])), 1 / 4, N)
        self.assertProportion(
            wound_outcomes(fighter(), fighter(SpecialRules=["Enemy Rerolls Successful Wounds"]))[0], 1 / 4, N)

    def test_cannot_be_wounded_on_a_two(self):
        # S6 v T3 would wound on 2+ (5/6); the rule makes it 3+ (2/3).
        self.assertProportion(
            wound_outcomes(fighter(Strength=6), fighter(Toughness=3,
                           SpecialRules=["Cannot Be Wounded On 2"]))[0], 2 / 3, N)

    def test_wounds_on_ignores_toughness(self):
        # S1 cannot wound T10 at all; Wounds On (2+) makes it 5/6.
        self.assertProportion(
            wound_outcomes(fighter(Strength=1, SpecialRules=["Wounds On (2+)"]), fighter(Toughness=10))[0],
            5 / 6, N)
        # It never makes an easier roll harder: S6 v T3 stays on 2+.
        self.assertProportion(
            wound_outcomes(fighter(Strength=6, SpecialRules=["Wounds On (4+)"]), fighter(Toughness=3))[0],
            5 / 6, N)

    def test_no_armour_saves(self):
        target = fighter(Armor="Plate Armor", Shield=True)
        self.assertEqual(save_rate(fighter(SpecialRules=["No Armour Saves"]), target, self_ordinary()), 0.0)

    def test_enemy_rerolls_successful_armour_saves(self):
        # Heavy armour 5+: 1/3, then again 1/3 -> 1/9.
        attacker = fighter(SpecialRules=["Enemy Rerolls Successful Armour Saves"])
        self.assertProportion(save_rate(attacker, fighter(Armor="Heavy Armor"), self_ordinary()), 1 / 9, N)

    def test_armour_that_cannot_be_improved_ignores_shields(self):
        target = fighter(Armor="Heavy Armor", Shield=True, SpecialRules=["Armour Cannot Be Improved"])
        self.assertProportion(save_rate(fighter(), target, self_ordinary()), 1 / 3, N)

    def test_armour_that_cannot_be_modified_ignores_armour_piercing(self):
        from combat_simulations import apply_weapon_stats, reset_weapon_stats
        attacker = fighter(Weapon="Great Weapon")  # AP -2 and Armour Bane (1)
        target = fighter(Armor="Heavy Armor", SpecialRules=["Armour Cannot Be Modified"])
        apply_weapon_stats(attacker, verbose=False)
        try:
            rate = save_rate(attacker, target, self_ordinary())
        finally:
            reset_weapon_stats(attacker)
        self.assertProportion(rate, 1 / 3, N)

    def test_large_models_cannot_beat_a_three_up(self):
        # Plate 4+, shield, Armoured Hide (2): 1+ before the cap.
        rules = ["Armoured Hide (2)"]
        infantry = fighter(Armor="Plate Armor", Shield=True, SpecialRules=rules)
        monster = fighter(Armor="Plate Armor", Shield=True, SpecialRules=rules)
        monster.TroopType = "Behemoth"
        self.assertProportion(save_rate(fighter(), infantry, self_ordinary()), 5 / 6, N)
        self.assertProportion(save_rate(fighter(), monster, self_ordinary()), 2 / 3, N)

    def test_immune_to_multiple_wounds_loses_one_wound(self):
        target = fighter(Wounds=100, SpecialRules=["Immune to Multiple Wounds"])
        rate = damage_rate(target, StrikeResult(unsaved=[Wound(roll=4)], multiple_wounds="D3"))
        self.assertEqual(rate, 1.0)

    def test_immunity_does_not_switch_off_a_ward_against_multiple_wounds(self):
        # Armour of Skaldour's ward still sees the attack as a Multiple Wounds one.
        target = fighter(Wounds=100, SpecialRules=["Immune to Multiple Wounds",
                                                   "Ward4 (Killing Blow, Multiple Wounds)"])
        rate = damage_rate(target, StrikeResult(unsaved=[Wound(roll=4)], multiple_wounds=2))
        self.assertProportion(rate, 1 / 2, N)


def self_ordinary():
    return TestArmour.ORDINARY


class TestCharacteristicsHelp(StatisticalCase):
    """Improving any characteristic should never make a fighter worse."""

    RUNS = SAMPLES_SMALL * 2

    def rate(self, **mine):
        me, _, _ = win_rates(
            lambda: fighter("Me", **mine), lambda: fighter("You"), self.RUNS, rounds=4, seed=11
        )
        return me

    def test_each_characteristic_improvement_helps(self):
        base = self.rate()
        for stat, value in [("WeaponSkill", 6), ("Strength", 5), ("Toughness", 5),
                            ("Wounds", 4), ("Attacks", 3), ("Initiative", 6)]:
            with self.subTest(stat=stat):
                self.assertNotWorse(self.rate(**{stat: value}), base, self.RUNS)

    def test_better_armour_helps(self):
        previous = self.rate()
        for armour in ("Light Armor", "Heavy Armor", "Plate Armor"):
            with self.subTest(armour=armour):
                current = self.rate(Armor=armour)
                self.assertNotWorse(current, previous, self.RUNS)
                previous = current

    def test_a_clearly_stronger_fighter_wins_most_duels(self):
        self.assertGreater(
            self.rate(WeaponSkill=7, Strength=5, Toughness=5, Attacks=4, Wounds=4), 0.8
        )

    def test_protective_rules_help(self):
        base = self.rate()
        for rules in (["Ward5"], ["Regen5"], ["Strike First"], ["Frenzy"],
                      ["Killing Blow"], ["Hatred (all enemies)"]):
            with self.subTest(rules=rules):
                self.assertNotWorse(self.rate(SpecialRules=rules), base, self.RUNS)


if __name__ == "__main__":
    unittest.main()
