"""Unit fights: geometry, charges, ranks, casualties, combat result, Break
tests, pursuit, challenges, characters in units and spells.

Each mechanic is checked against the rules text it implements (The Combat
Phase, Characters, Command Groups and Troop Types in Detail on tow.whfb.app).
"""

from __future__ import annotations

import math
import unittest

from support import FULL, StatisticalCase

import dice
import spells as sp
import unit_combat as uc
import unit_model as um
from app_model import FighterSpec, UNIT, faction_names, gear_options, profile_names


def unit(faction, profile, models=20, frontage=5, name=None, **gear):
    defaults = gear_options(faction, profile)["defaults"]
    spec = FighterSpec(name=name or profile, faction=faction, profile=profile,
                       weapon=gear.pop("weapon", defaults["weapon"]),
                       armour=gear.pop("armour", defaults["armour"]),
                       shield=gear.pop("shield", defaults["shield"]),
                       kind=UNIT, models=models, frontage=frontage)
    return um.UnitSide(unit=spec.to_dict(), **gear)


def character(faction, profile, **fields):
    defaults = gear_options(faction, profile)["defaults"]
    spec = FighterSpec(name=fields.pop("name", profile), faction=faction, profile=profile,
                       weapon=fields.pop("weapon", defaults["weapon"]),
                       armour=fields.pop("armour", defaults["armour"]),
                       shield=fields.pop("shield", defaults["shield"]),
                       mount=fields.pop("mount", None))
    return um.JoinedCharacter(spec=spec.to_dict(), **fields)


def troops(**kw):
    return unit("Empire of Man", "State Troops", **kw)


def orcs(**kw):
    return unit("Orc & Goblin Tribes", "Orc Mob", **kw)


def make_fight(a, b, **fight):
    return uc.Fight(um.build_fight(a, b, um.UnitFight(**fight)))


class TestGeometry(unittest.TestCase):
    def test_equal_bases_all_touch(self):
        self.assertEqual(uc.contact(5, 25, 125), {0, 1, 2, 3, 4})

    def test_a_wider_unit_touches_with_the_models_facing_the_enemy_and_at_the_corners(self):
        # 7 x 25 mm against a 5 x 25 mm front: the end models touch the enemy's
        # end models at the corner, which counts as base contact.
        self.assertEqual(uc.contact(7, 25, 125), set(range(7)))
        # 9 wide against 5: the outermost model on each side does not touch.
        self.assertEqual(uc.contact(9, 25, 125), set(range(1, 8)))

    def test_cavalry_against_infantry(self):
        # Three 30 mm knights (90 mm) against five 25 mm infantry (125 mm):
        # every infantry model touches the knights' front.
        self.assertEqual(uc.contact(5, 25, 90), {0, 1, 2, 3, 4})
        self.assertEqual(uc.contact(3, 30, 125), {0, 1, 2})

    def test_a_chariot_touches_three_infantry(self):
        self.assertEqual(len(uc.contact(5, 25, 50)), 3)


class TestUnitShape(unittest.TestCase):
    def setUp(self):
        self.fight = make_fight(troops(models=23, frontage=5), orcs())
        self.unit = self.fight.units[0]

    def test_ranks_and_incomplete_rear_rank(self):
        self.assertEqual(self.unit.rank_sizes(), [5, 5, 5, 5, 3])
        self.assertEqual(self.unit.ranks(), 5)

    def test_rank_bonus_is_capped_by_troop_type_and_horde(self):
        # Regular infantry: +2 at most; State Troops are a Horde (+1 more).
        self.assertEqual(self.unit.rank_bonus(False), 3)
        self.assertEqual(self.unit.rank_bonus(True), 0)  # a Disrupted unit claims none

    def test_a_rear_rank_below_five_models_does_not_count(self):
        unit = make_fight(orcs(models=14, frontage=5), troops()).units[0]
        self.assertEqual(unit.rank_sizes(), [5, 5, 4])
        self.assertEqual(unit.rank_bonus(False), 1)

    def test_a_column_is_not_in_combat_order(self):
        unit = make_fight(orcs(models=20, frontage=3), troops()).units[0]
        self.assertFalse(unit.combat_order())
        self.assertEqual(unit.rank_bonus(False), 0)

    def test_unit_strength(self):
        self.assertEqual(self.unit.unit_strength(), 23)
        knights = make_fight(unit("Kingdom of Bretonnia", "Mounted Knights of the Realm",
                                  models=6, frontage=3), orcs()).units[0]
        self.assertEqual(knights.unit_strength(), 12)  # heavy cavalry: 2 each

    def test_a_character_adds_its_unit_strength_and_a_body(self):
        side = troops(models=20, frontage=5,
                      characters=[character("Empire of Man", "General of the Empire")])
        unit = make_fight(side, orcs()).units[0]
        self.assertEqual(unit.unit_strength(), 21)
        self.assertEqual(unit.rank_sizes(), [5, 5, 5, 5, 1])

    def test_command_group_stands_in_the_centre(self):
        slots = self.unit.slots()
        self.assertEqual(slots[2], "standard")
        self.assertIn("champion", (slots[1], slots[3]))
        self.assertIn("musician", (slots[1], slots[3]))

    def test_a_character_takes_the_slot_it_was_placed_in(self):
        side = troops(characters=[character("Empire of Man", "General of the Empire", slot=0)])
        slots = make_fight(side, orcs()).units[0].slots()
        self.assertEqual(slots[0][0], "char")


class TestCharging(unittest.TestCase):
    def test_charge_initiative_bonus_per_inch_to_three_in_front(self):
        f = make_fight(troops(), orcs(), charger="A", charge_distance=2)
        f.charged[0] = True
        f.charge_distance[0] = 2
        model = f.units[0].model
        self.assertEqual(f.initiative(0, model), model.Initiative + 2)
        f.charge_distance[0] = 9
        self.assertEqual(f.initiative(0, model), model.Initiative + 3)

    def test_up_to_four_into_a_flank_and_none_when_disordered(self):
        f = make_fight(troops(), orcs(), charger="A", charge_distance=9, arc="flank")
        f.charged[0], f.charge_distance[0] = True, 9
        base = f.units[0].model.Initiative
        self.assertEqual(f.initiative(0, f.units[0].model), base + 4)
        g = make_fight(troops(), orcs(), charger="A", charge_distance=9, disordered=True)
        g.charged[0], g.charge_distance[0] = True, 9
        self.assertEqual(g.initiative(0, g.units[0].model), base)

    def test_strike_first_is_initiative_ten_and_strike_last_one(self):
        f = make_fight(troops(), orcs())
        model = f.units[0].model
        model.SpecialRules.append("Strike First")
        self.assertEqual(f.initiative(0, model), 10)
        model.SpecialRules.append("Strike Last")  # the two cancel out
        self.assertEqual(f.initiative(0, model), model.Initiative)

    def test_thrusting_spears_gain_initiative_when_charged_in_front(self):
        f = make_fight(orcs(), troops(weapon="Thrusting Spear"), charger="A", charge_distance=5)
        f.charged[0] = True
        spears = f.units[1].model
        self.assertEqual(f.initiative(1, spears), spears.Initiative + 1)

    def test_impact_hits_need_a_charge_of_three_inches(self):
        chariot = unit("Orc & Goblin Tribes", "Orc Boar Chariot", models=1, frontage=1)
        for distance, expect_hits in ((2, False), (3, True)):
            f = make_fight(chariot, troops(), charger="A", charge_distance=distance)
            f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
            f.charged[0], f.charge_distance[0] = True, distance
            dice.seed(1)
            f.impact_hits()
            self.assertEqual(any("Impact Hits" in line for line in f.log), expect_hits, distance)

    def test_heavy_chariot_impact_hits_are_ap_minus_two(self):
        chariot = unit("Orc & Goblin Tribes", "Orc Boar Chariot", models=1, frontage=1)
        f = make_fight(chariot, troops(), charger="A", charge_distance=6)
        f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
        f.charged[0], f.charge_distance[0] = True, 6
        dice.seed(2)
        f.impact_hits()
        self.assertTrue(any("S5, AP -2" in line for line in f.log), f.log)

    def test_a_lance_is_only_used_in_the_turn_it_charged(self):
        from unit_combat import _weapon_for_turn

        knights = make_fight(unit("Kingdom of Bretonnia", "Mounted Knights of the Realm",
                                  models=6, frontage=3, weapon="Lance"), troops()).units[0].model
        self.assertEqual(_weapon_for_turn(knights, True), "Lance")
        self.assertEqual(_weapon_for_turn(knights, False), "Hand Weapon")

    def test_frenzy_and_furious_charge_only_add_attacks_on_the_charge(self):
        f = make_fight(troops(), orcs(), charger="A", charge_distance=5)
        model = f.units[0].model
        model.SpecialRules += ["Frenzy", "Furious Charge"]
        base = model.Attacks
        self.assertEqual(f.attacks_per_model(0, model), base)
        f.charged[0], f.charge_distance[0] = True, 5
        self.assertEqual(f.attacks_per_model(0, model), base + 2)
        f.units[0].frenzy_lost = True  # lost a round of combat
        self.assertEqual(f.attacks_per_model(0, model), base + 1)

    def test_frenzy_after_a_follow_up_and_never_for_steeds(self):
        knights = unit("Kingdom of Bretonnia", "Mounted Knights of the Realm", models=6, frontage=3)
        f = make_fight(knights, troops())
        rider, horse = f.units[0].model, f.units[0].parts[0]
        for model in (rider, horse):
            model.SpecialRules = list(model.SpecialRules) + ["Frenzy"]
        f.units[0].followed_up = True  # the turn after a follow up move
        self.assertEqual(f.attacks_per_model(0, rider), rider.Attacks + 1)
        self.assertEqual(f.attacks_per_model(0, horse, part=True), horse.Attacks)

    def test_losing_a_round_loses_frenzy_unless_witchbrew(self):
        for rules, lost in (([], True), (["Witchbrew"], False)):
            f = make_fight(troops(), orcs())
            f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
            f.units[0].model.SpecialRules += ["Frenzy"] + rules
            f.score = lambda i: {"wounds": 0 if i == 0 else 3}
            with dice.scripted_dice([1, 1]):  # a double 1: Gives Ground
                f.resolve(0)
            self.assertEqual(f.units[0].frenzy_lost, lost, rules)


class TestWhoFights(unittest.TestCase):
    def setUp(self):
        dice.seed(0)

    def attackers(self, fight, index):
        fight.round_casualties = [0, 0]
        return fight.rf_attackers(index)

    def test_press_of_battle_adds_the_second_rank_except_when_charging(self):
        f = make_fight(troops(champion=False, standard=False, musician=False), orcs(), charger="B")
        self.assertEqual(self.attackers(f, 0), (5, 0, 5))
        f.charged[0] = True
        self.assertEqual(self.attackers(f, 0), (5, 0, 0))

    def test_spears_support_from_the_rank_behind(self):
        side = troops(champion=False, standard=False, musician=False, weapon="Thrusting Spear")
        f = make_fight(side, orcs(), charger="B")
        # Rank 2 fights through Press of Battle, rank 3 supports.
        self.assertEqual(self.attackers(f, 0), (5, 0, 10))
        f.charged[0] = True  # no Press of Battle and no spear support on the charge
        self.assertEqual(self.attackers(f, 0), (5, 0, 0))

    def test_models_beyond_the_enemy_make_one_attack(self):
        f = make_fight(troops(models=27, frontage=9, champion=False, standard=False, musician=False),
                       orcs(models=20, frontage=5), charger="B")
        contact, near, _extra = self.attackers(f, 0)
        self.assertEqual((contact, near), (7, 2))

    def test_casualties_come_off_the_fighting_rank_before_it_strikes(self):
        f = make_fight(troops(champion=False, standard=False, musician=False), orcs(), charger="B")
        f.round_start = [(f.fighting_line(i), f.units[i].rank_sizes()) for i in (0, 1)]
        for _ in range(3):  # the unit shrinks, but the round was counted at its start
            f.units[0].remove_model()
        f.round_casualties = [3, 0]
        # Press of Battle models go first, then those in contact.
        self.assertEqual(f.rf_attackers(0), (5, 0, 2))
        for _ in range(4):
            f.units[0].remove_model()
        f.round_casualties = [7, 0]
        self.assertEqual(f.rf_attackers(0), (3, 0, 0))

    def test_cavalry_mounts_neither_support_nor_press(self):
        knights = unit("Kingdom of Bretonnia", "Mounted Knights of the Realm", models=8, frontage=4,
                       champion=False, standard=False, musician=False)
        f = make_fight(knights, troops())
        f.round_casualties = [0, 0]
        self.assertEqual(f.rf_attackers(0, part=True), (4, 0, 0))


class TestDamage(unittest.TestCase):
    def fight(self, a, b):
        f = make_fight(a, b)
        f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
        return f

    def test_wounds_do_not_spill_over_between_models(self):
        ogres = unit("Ogre Kingdoms", "Ogre Bulls", models=6, frontage=3)
        f = self.fight(ogres, troops())
        with dice.scripted_dice([]):
            lost, removed = f.wound_unit(0, [uc.Wound(roll=4)], False, False, 5, False, 5)
        self.assertEqual((lost, removed), (3, 1))  # Multiple Wounds (5) on a 3-Wound Ogre

    def test_a_killing_blow_takes_all_remaining_wounds(self):
        ogres = unit("Ogre Kingdoms", "Ogre Bulls", models=6, frontage=3)
        f = self.fight(ogres, troops())
        f.units[0].damage = 1
        with dice.scripted_dice([]):
            lost, removed = f.wound_unit(0, [uc.Wound(roll=6, killing_blow=True)], False, False, 1, False, 4)
        self.assertEqual((lost, removed), (2, 1))

    def test_regenerated_wounds_still_count_for_the_combat_result(self):
        f = self.fight(troops(enchantments=["Ariel's Blessing"]), orcs())
        f.start_turn(0)
        with dice.scripted_dice([5, 2]):  # first regenerates (5+), second does not
            lost, removed = f.wound_unit(0, [uc.Wound(roll=4), uc.Wound(roll=4)], False, False, 1, False, 3)
        self.assertEqual((lost, removed), (2, 1))

    def test_the_champion_is_the_last_model_removed(self):
        f = self.fight(troops(models=3, frontage=3), orcs())
        unit_ = f.units[0]
        for _ in range(2):
            unit_.remove_model()
        self.assertIsNotNone(unit_.champion)
        unit_.remove_model()
        self.assertIsNone(unit_.champion)


class TestCombatResult(unittest.TestCase):
    def fight(self, a, b, **kw):
        f = make_fight(a, b, **kw)
        f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
        return f

    def test_the_score_adds_up(self):
        f = self.fight(troops(models=25), orcs(models=15), charger="A", arc="flank")
        f.round_lost = [1, 3]  # troops lost 1, orcs lost 3
        f.round_overkill = [7, 0]
        score = f.score(0)
        self.assertEqual(score["wounds"], 3)
        self.assertEqual(score["overkill"], 5)  # at most +5
        self.assertEqual(score["ranks"], 3)
        self.assertEqual(score["standard"], 1)
        self.assertEqual(score["flank"], 1)
        self.assertEqual(score["close order"], 1)
        self.assertEqual(score["massed infantry"], 1)
        # The flanked orcs are Disrupted: no Rank Bonus.
        self.assertNotIn("ranks", f.score(1))

    def test_rear_attack_is_worth_two(self):
        f = self.fight(troops(), orcs(), charger="A", arc="rear")
        self.assertEqual(f.score(0)["rear"], 2)

    def test_battle_standard_and_high_ground(self):
        side = troops(high_ground=True,
                      characters=[character("Empire of Man", "Captain of the Empire", battle_standard=True)])
        f = self.fight(side, orcs())
        score = f.score(0)
        self.assertEqual((score["battle standard"], score["high ground"]), (1, 1))

    def test_a_musician_breaks_a_draw(self):
        f = self.fight(troops(musician=True), orcs(musician=False, standard=False, champion=False))
        f.round_lost = [0, 0]
        # Make the base scores equal, then resolve.
        f.score = lambda i: {"wounds": 1}
        dice.seed(0)
        f.resolve(0)
        self.assertTrue(any("musician 1" in line for line in f.log), f.log)


class TestBreakTests(unittest.TestCase):
    def test_the_three_outcomes(self):
        o = uc._break_outcome
        self.assertEqual(o(5, 4, 1, 8), uc.FLED)          # natural 9 > 8
        self.assertEqual(o(4, 3, 2, 8), uc.FELL_BACK)      # natural 7, modified 9
        self.assertEqual(o(3, 3, 2, 8), uc.GAVE_GROUND)    # modified 8
        self.assertEqual(o(1, 1, 9, 5), uc.GAVE_GROUND)    # a double 1

    def break_test(self, loser_side, winner_side, rolls, margin=2):
        f = make_fight(loser_side, winner_side)
        f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
        f.start_turn(0)
        with dice.scripted_dice(rolls):
            return f.break_test(0, 1, margin), f

    def test_falling_back_becomes_a_break_when_outnumbered_two_to_one(self):
        outcome, _f = self.break_test(troops(models=10), orcs(models=25), [4, 3], margin=3)
        self.assertEqual(outcome, uc.FLED)
        outcome, _f = self.break_test(troops(models=20), orcs(models=25), [4, 3], margin=3)
        self.assertEqual(outcome, uc.FELL_BACK)

    def test_stubborn_falls_back_without_testing_the_first_time(self):
        side = troops(models=10)
        f = make_fight(side, orcs(models=40))
        f.units[0].model.SpecialRules.append("Stubborn")
        f.units[0]._remember(f.units[0].model)
        f.start_turn(0)
        self.assertEqual(f.break_test(0, 1, 6), uc.FELL_BACK)
        with dice.scripted_dice([6, 6]):
            self.assertEqual(f.break_test(0, 1, 6), uc.FLED)

    def test_unbreakable_gives_ground(self):
        f = make_fight(troops(enchantments=["Courage of Aenarion"]), orcs())
        f.start_turn(0)
        with dice.scripted_dice([]):
            self.assertEqual(f.break_test(0, 1, 9), uc.GAVE_GROUND)

    def test_terror_costs_one_leadership(self):
        f = make_fight(troops(), orcs())
        f.units[1].model.SpecialRules.append("Terror")
        f.units[1]._remember(f.units[1].model)
        f.start_turn(0)
        with dice.scripted_dice([4, 3]):  # 7 vs Ld 7 - 1 = 6: breaks
            self.assertEqual(f.break_test(0, 1, 1), uc.FLED)

    def test_warband_adds_its_rank_bonus_to_leadership(self):
        f = make_fight(orcs(models=15, champion=False), troops())
        f.start_turn(0)
        self.assertEqual(f.units[0].leadership(2), min(10, f.units[0].model.Leadership + 2))

    def test_a_battle_standard_rerolls_a_break(self):
        side = troops(characters=[character("Empire of Man", "Captain of the Empire", battle_standard=True)])
        with dice.scripted_dice([6, 5, 2, 2]):  # 11 breaks; the re-roll of 4 gives ground
            outcome, f = self.break_test(side, orcs(), [6, 5, 2, 2], margin=1)
        self.assertEqual(outcome, uc.GAVE_GROUND)

    def test_a_death_hags_cry_of_war_costs_the_enemy_unit_leadership(self):
        hag = um.JoinedCharacter(spec=FighterSpec(
            name="Hag", faction="Dark Elves", profile="Death Hag", weapon="Two Hand Weapons",
            armour="None", optional_rules=["Cry of War"]).to_dict())
        witches = unit("Dark Elves", "Witch Elves", characters=[hag])
        f = make_fight(witches, troops())
        f.start_turn(0)
        self.assertEqual(f.units[1].ld_penalty, 1)
        self.assertEqual(f.units[0].ld_penalty, 0)

    def test_hexed_leadership_never_drops_below_two(self):
        f = make_fight(troops(hexes=["Spirit Leech", "Gathering Darkness"]), orcs())
        f.start_turn(1)  # the caster's turn: both are in effect
        self.assertEqual(f.units[0].leadership(0, f.hex_ld(f.units[0])), 3)  # Ld 7 - 4
        f.start_turn(0)  # Spirit Leech only lasts until the end of the caster's turn
        self.assertEqual(f.units[0].leadership(0, f.hex_ld(f.units[0])), 5)


class TestPursuit(unittest.TestCase):
    def after(self, outcome, rolls, pursue=True):
        f = make_fight(orcs(pursue=pursue), troops())
        f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
        with dice.scripted_dice(rolls):
            return f.follow_up(0, 1, outcome), f

    def test_a_fleeing_unit_caught_is_destroyed(self):
        result, _f = self.after(uc.FLED, [3, 4, 4, 3])  # flees 7, pursuit 7
        self.assertEqual(result.outcome, uc.RUN_DOWN)
        self.assertEqual(result.models_left[1], 0)

    def test_a_fleeing_unit_that_outruns_the_pursuit_escapes(self):
        result, _f = self.after(uc.FLED, [5, 4, 4, 3])  # flees 9, pursuit 7
        self.assertEqual(result.outcome, uc.FLED)

    def test_falling_back_rolls_two_dice_and_keeps_the_highest(self):
        # 2 and 5: falls back 5"; pursuit 2+2 = 4 does not reach it.
        result, _f = self.after(uc.FELL_BACK, [2, 5, 2, 2])
        self.assertEqual(result.outcome, uc.FELL_BACK)

    def test_catching_a_unit_that_fell_back_continues_the_fight_as_a_charge(self):
        result, f = self.after(uc.FELL_BACK, [2, 3, 4, 4])  # 3" against 8"
        self.assertIsNone(result)
        self.assertTrue(f.charged[0])
        self.assertEqual(f.charge_distance[0], 8)

    def test_a_unit_that_gives_ground_is_followed_up(self):
        result, f = self.after(uc.GAVE_GROUND, [])
        self.assertIsNone(result)
        self.assertTrue(f.units[0].followed_up)

    def test_restraint_ends_the_fight(self):
        result, _f = self.after(uc.GAVE_GROUND, [], pursue=False)
        self.assertEqual(result.outcome, uc.GAVE_GROUND)


class TestChallenges(unittest.TestCase):
    def test_the_champions_fight_each_other(self):
        f = make_fight(troops(), orcs())
        f.challenges(0)
        self.assertEqual(f.challenge, ("champion", "champion"))

    def test_a_refused_challenge_retires_the_character(self):
        side = troops(accept_challenges=False,
                      characters=[character("Empire of Man", "Captain of the Empire")])
        f = make_fight(orcs(), side)
        f.challenges(0)
        self.assertIsNone(f.challenge)
        self.assertTrue(f.units[1].characters[0].retired)
        self.assertEqual(f.units[1].fighters(), [])

    def test_overkill_counts_excess_wounds(self):
        side_a = troops(characters=[character("Empire of Man", "General of the Empire")])
        f = make_fight(side_a, orcs(champion=True))
        f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
        boss = f.units[1].champion
        with dice.scripted_dice([]):
            lost, excess = f.wound_model(1, boss, [uc.Wound(roll=4)] * 4, False, False, 1, False, 4)
        self.assertEqual((lost, excess), (boss.Wounds, 4 - boss.Wounds))


class TestSpells(unittest.TestCase):
    def test_durations(self):
        # Battle Lust lasts until the end of the caster's turn; Word of Pain
        # until its next Start of Turn; Courage of Aenarion Remains in Play.
        self.assertTrue(sp.active("Battle Lust", 0, 0, 1))
        self.assertFalse(sp.active("Battle Lust", 0, 1, 2))
        self.assertTrue(sp.active("Word of Pain", 0, 1, 2))
        self.assertTrue(sp.active("Courage of Aenarion", 1, 0, 5))

    def test_a_hex_lowers_characteristics_and_expires(self):
        f = make_fight(troops(hexes=["Word of Pain"]), orcs())
        before = f.units[0].model.Strength
        f.turn = 1
        f.start_turn(1)
        self.assertEqual(f.units[0].model.Strength, before - 1)

    def test_a_turn_long_enchantment_only_works_in_the_casters_turn(self):
        f = make_fight(troops(enchantments=["Battle Lust"]), orcs())
        f.turn = 1
        f.start_turn(0)
        self.assertIn("Frenzy", f.units[0].model.SpecialRules)
        f.turn = 2
        f.start_turn(1)
        self.assertNotIn("Frenzy", f.units[0].model.SpecialRules)

    def test_an_assailment_spell_is_cast_and_can_be_dispelled(self):
        wizard = character("Empire of Man", "Wizard Lord", wizard_level=3, spells=["Hammerhand"])
        f = make_fight(troops(characters=[wizard]), orcs())
        f.turn = 1
        f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
        placed = f.units[0].characters[0]
        # Cast 3+3+2 = 8 (needs 7); Fated dispel 4+4 = 8 does not exceed it.
        with dice.scripted_dice([3, 3, 4, 4] + [2, 2] + [4] * 6 + [3] * 6):
            apply = sp.cast_assailment(f, 0, placed, "Hammerhand")
        self.assertIsNotNone(apply)
        f2 = make_fight(troops(characters=[wizard]), orcs())
        f2.turn = 1
        with dice.scripted_dice([3, 3, 5, 4]):  # dispel 9 beats 8
            self.assertIsNone(sp.cast_assailment(f2, 0, f2.units[0].characters[0], "Hammerhand"))

    def test_a_miscast_is_not_cast(self):
        wizard = character("Empire of Man", "Wizard Lord", wizard_level=3, spells=["Hammerhand"])
        f = make_fight(troops(characters=[wizard]), orcs())
        f.turn = 1
        with dice.scripted_dice([1, 1]):
            self.assertIsNone(sp.cast_assailment(f, 0, f.units[0].characters[0], "Hammerhand"))

    def test_every_modelled_spell_exists(self):
        from spells_data import SPELLS

        for name in list(sp.EFFECTS) + list(sp.ASSAILMENT) + list(sp.NOT_IN_A_FIGHT):
            self.assertIn(name, SPELLS, name)
        hexes = [n for n, d in SPELLS.items() if d["type"] in ("Hex", "Enchantment")]
        for name in hexes:
            self.assertTrue(name in sp.EFFECTS or name in sp.NOT_IN_A_FIGHT, f"{name} is unclassified")
        for name in (n for n, d in SPELLS.items() if d["type"] == "Assailment"):
            self.assertTrue(name in sp.ASSAILMENT or name in sp.ASSAILMENT_NOT_SIMULATED, name)


class TestCommandGroups(unittest.TestCase):
    def test_each_unit_may_take_what_its_page_offers(self):
        self.assertEqual(um.unit_options("Empire of Man", "State Troops")["command"],
                         ["champion", "standard", "musician"])
        self.assertEqual(um.unit_options("Empire of Man", "Empire Archers")["command"], ["champion"])
        self.assertEqual(um.unit_options("Orc & Goblin Tribes", "Orc Boar Chariot")["command"], [])

    def test_a_command_model_the_unit_cannot_take_is_left_out(self):
        side = unit("Empire of Man", "Empire Archers", models=10, frontage=5,
                    standard=True, musician=True)
        setup = um.build_side(side)
        self.assertFalse(setup.standard)
        self.assertFalse(setup.musician)
        self.assertIsNotNone(setup.champion)

    def test_budgets_for_the_champion_and_standard_bearer(self):
        options = um.unit_options("Dark Elves", "Cold One Knights")
        self.assertEqual(options["champion"], "Dread Knight")
        self.assertEqual(options["champion_items"], {"Magic Items": 50})
        self.assertEqual(options["standard_items"], {"Magic Items": 50})
        self.assertEqual(um.unit_options("Dwarfen Mountain Holds", "Longbeards")["standard_items"],
                         {"Runes": 50})

    def test_what_each_may_carry(self):
        from magic_items import check_unit_purchase

        check_unit_purchase("Dark Elves", "Cold One Knights", "standard", ["War Banner"])
        check_unit_purchase("Dark Elves", "Cold One Knights", "champion", ["Sword of Might"])
        for role, items, message in (
            ("champion", ["War Banner"], "cannot carry a magic standard"),
            ("standard", ["Sword of Might"], "only a magic standard"),
            ("standard", ["War Banner", "Banner of Iron Resolve"], "cannot carry both|may spend"),
            ("standard", ["Griffon Standard"], "not available"),
        ):
            with self.subTest(items=items), self.assertRaisesRegex(ValueError, message):
                check_unit_purchase("Dark Elves", "Cold One Knights", role, items)
        with self.assertRaisesRegex(ValueError, "cannot include"):
            check_unit_purchase("Empire of Man", "Empire Archers", "standard", ["War Banner"])

    def test_the_champion_fights_with_its_magic_weapon(self):
        side = unit("Dark Elves", "Cold One Knights", models=6, frontage=3, weapon="Lance",
                    champion_items=["Sword of Might"])
        champion = make_fight(side, troops()).units[0].champion
        self.assertEqual(champion.Weapon, "Sword of Might")

    def test_points_include_command_models_and_items(self):
        side = unit("Dark Elves", "Cold One Knights", models=6, frontage=3, weapon="Lance",
                    champion_items=["Sword of Might"], standard_items=["War Banner"])
        lines = dict(um.side_points(side))
        self.assertEqual((lines["Dread Knight"], lines["Sword of Might"], lines["War Banner"]), (7, 20, 25))


class TestMagicStandards(unittest.TestCase):
    def banner(self, a, b, items, side=0, start=True, **kw):
        """A fight in which unit `side` carries `items` as its standard. The
        purchase rules are tested in TestCommandGroups; these tests check
        what each standard does."""
        setup = um.build_fight(a, b, um.UnitFight(**kw))
        setup.sides[side].standard = True
        setup.sides[side].standard_items = list(items)
        f = uc.Fight(setup)
        f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
        if start:
            f.start_turn(0)
        return f

    def test_every_standard_is_classified(self):
        import standards
        from magic_items import MagicItemDict, is_standard_item

        names = {n for n in MagicItemDict if is_standard_item(n)}
        self.assertEqual(names - set(standards.EFFECTS) - set(standards.NOT_IN_A_FIGHT), set())
        self.assertEqual((set(standards.EFFECTS) | set(standards.NOT_IN_A_FIGHT)) - names, set())
        self.assertFalse(set(standards.EFFECTS) & set(standards.NOT_IN_A_FIGHT))

    def test_combat_result_bonuses(self):
        f = self.banner(troops(), orcs(), ["War Banner"])
        self.assertEqual(f.score(0)["magic standard"], 1)
        f = self.banner(troops(), orcs(), ["Banner of Renown"])
        self.assertEqual(f.score(0)["magic standard"], 1)
        self.assertNotIn("magic standard", f.score(0))  # single use

    def test_a_dice_bonus_is_rolled_each_round(self):
        f = self.banner(troops(), orcs(), ["Battle Banner"])
        with dice.constant_dice(6):  # a D3 of 3
            self.assertEqual(f.score(0)["magic standard"], 3)
        with dice.constant_dice(1):
            self.assertEqual(f.score(0)["magic standard"], 1)

    def test_the_standard_stops_working_when_its_bearer_is_lost(self):
        f = self.banner(troops(models=3, frontage=3), orcs(), ["War Banner"])
        f.units[0].remove_model()
        f.units[0].remove_model()  # only the champion is left: the bearer is gone
        self.assertNotIn("magic standard", f.score(0))
        self.assertNotIn("standard", f.score(0))

    def test_griffon_standard_doubles_the_rank_bonus(self):
        f = self.banner(troops(models=20), orcs(), ["Griffon Standard"])
        self.assertEqual(f.units[0].rank_bonus(False), 2 * 3)

    def test_rules_and_characteristics(self):
        f = self.banner(orcs(), troops(), ["Da Angry Ladz Flag"])
        self.assertIn("Frenzy", f.units[0].model.SpecialRules)
        f = self.banner(troops(), orcs(), ["Icon of the Sacred Eye"])
        self.assertEqual(f.units[0].model.WeaponSkill, 3 + 1)

    def test_charge_effects_only_on_the_charge(self):
        f = self.banner(orcs(), troops(), ["Da Banner of Butchery"], start=False, charger="A")
        strength = f.units[0].model.Strength
        f.charged[0] = True
        f.start_turn(0)
        self.assertEqual(f.units[0].model.Strength, strength + 1)
        f.charged[0] = False
        f.start_turn(1)
        self.assertEqual(f.units[0].model.Strength, strength)

    def test_break_test_standards(self):
        f = self.banner(troops(), orcs(models=45), ["Banner of the Steadfast"])
        with dice.scripted_dice([3, 3]):  # 6 + 2 = 8 > Ld 7: falls back, even outnumbered
            self.assertEqual(f.break_test(0, 1, 2), uc.FELL_BACK)
        f = self.banner(troops(), orcs(), ["Valorous Standard"])
        with dice.scripted_dice([6, 6, 1]):  # 3D6, the highest discarded
            self.assertEqual(f._break_dice(f.units[0]), (1, 6))

    def test_banner_of_rage_never_loses_frenzy(self):
        f = self.banner(troops(), orcs(), ["Banner of Rage"])
        f.score = lambda i: {"wounds": 0 if i == 0 else 3}
        with dice.scripted_dice([1, 1]):
            f.resolve(0)
        self.assertFalse(f.units[0].frenzy_lost)

    def test_no_rear_bonus_against_the_rotten_icon(self):
        f = self.banner(troops(), orcs(), ["Rotten Icon"], side=1, charger="A", arc="rear")
        self.assertNotIn("rear", f.score(0))

    def test_a_charge_into_the_front_of_a_rune_of_confusion_is_disordered(self):
        f = self.banner(orcs(), troops(), ["Rune of Confusion"], side=1, start=False,
                        charger="A", charge_distance=6)
        f.turn = 1
        f.start_turn(0)
        self.assertTrue(f.setup.disordered)

    def test_the_rune_of_hesitation_denies_the_charge_to_weapons_and_rules(self):
        f = self.banner(orcs(), troops(), ["Master Rune of Hesitation"], side=1, start=False,
                        charger="A", charge_distance=6)
        f.charged[0], f.charge_distance[0] = True, 6
        self.assertFalse(f.charge_counts(0))
        # The Initiative bonus for charging is not a special rule: it stays.
        self.assertEqual(f.initiative(0, f.units[0].model), f.units[0].model.Initiative + 3)

    def test_an_enemy_spell_can_be_turned_aside(self):
        wizard = character("Empire of Man", "Wizard Lord", wizard_level=3, spells=["Hammerhand"])
        f = self.banner(troops(characters=[wizard]), orcs(), ["Rune Maw"], side=1)
        f.turn = 1
        with dice.scripted_dice([3]):  # 3+: the spell cannot be cast
            self.assertIsNone(sp.cast_assailment(f, 0, f.units[0].characters[0], "Hammerhand"))

    def test_banner_of_lothern_adds_half_the_third_rank(self):
        spears = troops(models=25, weapon="Thrusting Spear", champion=False, musician=False)
        f = self.banner(spears, orcs(), ["The Banner of Lothern"], start=False, charger="B")
        f.start_turn(1)
        f.round_casualties = [0, 0]
        # Front rank in contact; Press of Battle rank 2; spears support from
        # rank 3; and half of rank 4, rounding up.
        self.assertEqual(f.rf_attackers(0), (5, 0, 5 + 5 + 3))

    def test_enemy_characteristics_roll_once_per_fight(self):
        f = self.banner(orcs(), troops(), ["Banner of Acquiescence"], start=False)
        ws = f.units[1].model.WeaponSkill
        with dice.constant_dice(6):  # -D3 = -3, to a minimum of 1
            f.start_turn(0)
        first = f.units[1].model.WeaponSkill
        f.start_turn(1)
        self.assertEqual(f.units[1].model.WeaponSkill, first)
        self.assertEqual(first, max(1, ws - 3))


class TestRosterGapsInUnitFights(unittest.TestCase):
    def fresh(self, f):
        f.round_lost, f.round_overkill, f.round_casualties = [0, 0], [0, 0], [0, 0]
        return f

    def test_big_stabbas_are_d3_impact_hits_for_the_whole_unit(self):
        mob = orcs()
        mob.unit["optional_rules"] = ["Frenzy", "Big Stabbas"]
        f = self.fresh(make_fight(mob, troops(), charger="A", charge_distance=5))
        f.charged[0], f.charge_distance[0] = True, 5
        with dice.constant_dice(6):  # one D3 of 3, not one per model
            f.impact_hits()
        self.assertTrue(any("3 Impact Hits" in line for line in f.log), f.log)

    def test_cavalry_impact_hits_use_the_mounts_strength(self):
        boars = unit("Orc & Goblin Tribes", "Orc Boar Boy Mob", models=5, frontage=5)
        f = self.fresh(make_fight(boars, troops(), charger="A", charge_distance=6))
        f.units[0].model.SpecialRules.append("Impact Hits (1)")
        f.charged[0], f.charge_distance[0] = True, 6
        with dice.constant_dice(4):
            f.impact_hits()
        boar_strength = f.units[0].parts[0].Strength
        self.assertTrue(any(f"(S{boar_strength}" in line for line in f.log), f.log)

    def test_a_fiend_tail_adds_d3_attacks_at_ap_minus_one(self):
        chimera = unit("Warriors of Chaos", "Chimera", models=1, frontage=1)
        chimera.unit["optional_rules"] = ["Fiend Tail"]
        f = make_fight(chimera, troops())
        tail = [p for p in f.units[0].parts if p.Weapon == "Fiend Tail"]
        self.assertEqual(len(tail), 1)
        with dice.constant_dice(6):
            self.assertEqual(f.attacks_per_model(0, tail[0], part=True), 3)
        from weapons import get_weapon_ap

        self.assertEqual(abs(get_weapon_ap("Fiend Tail")), 1)

    def test_an_oathstone_challenge_cannot_be_refused(self):
        thane = character("Dwarfen Mountain Holds", "Thane")
        thane.spec["optional_rules"] = ["Oathstone"]
        dwarfs = unit("Dwarfen Mountain Holds", "Longbeards", models=20, frontage=5, characters=[thane])
        f = make_fight(dwarfs, troops(accept_challenges=False))
        f.challenges(0)
        self.assertIsNotNone(f.challenge)

    def test_daemons_of_slaanesh_pursue_one_inch_further(self):
        f = make_fight(troops(), orcs())
        with dice.constant_dice(3):
            plain = f._pursuit(f.units[0])
        f.units[0].model.SpecialRules.append("Daemons of Slaanesh")
        with dice.constant_dice(3):
            self.assertEqual(f._pursuit(f.units[0]), plain + 1)

    def test_the_horn_of_isha_in_a_unit(self):
        handmaiden = character("High Elf Realms", "Handmaiden of the Everqueen")
        handmaiden.spec["optional_rules"] = ["Horn of Isha"]
        f = make_fight(unit("High Elf Realms", "Lothern Sea Guard", models=15, frontage=5,
                            characters=[handmaiden]), orcs())
        f.turn = 1
        with dice.scripted_dice([1, 2]):
            f.start_turn(0)
        self.assertIn("To Wound (+1)", f.units[0].model.SpecialRules)
        f.turn = 2
        f.start_turn(1)  # the enemy's turn: still in effect
        self.assertIn("To Hit (+1)", f.units[0].model.SpecialRules)
        f.turn = 3
        f.start_turn(0)  # her next turn: over, and single use
        self.assertNotIn("To Hit (+1)", f.units[0].model.SpecialRules)

    def test_a_tzeentch_wizard_casts_with_plus_one(self):
        from spells import cast_assailment

        wizard = character("Empire of Man", "Wizard Lord", wizard_level=1, spells=["Hammerhand"])
        f = make_fight(troops(characters=[wizard]), orcs())
        f.turn = 1
        placed = f.units[0].characters[0]
        placed.character.SpecialRules.append("Daemon of Tzeentch")
        # 3+2 +1 (Level 1) +1 (Tzeentch) = 7: just enough for Hammerhand; no dispel.
        with dice.scripted_dice([3, 2, 1, 2] + [1] * 20):
            self.assertIsNotNone(cast_assailment(f, 0, placed, "Hammerhand"))

    def test_formation_swaps_are_formations(self):
        self.assertEqual(um.unit_options("Kingdom of Bretonnia", "Peasant Bowmen")["formations"],
                         ["close", "skirmish"])
        self.assertNotIn("Skirmishers", gear_options("Kingdom of Bretonnia", "Peasant Bowmen")["optional_rules"])


class TestRuleCoverage(unittest.TestCase):
    def test_unit_rules_are_read_by_the_unit_engine(self):
        import os
        from rule_catalogue import UNIT_ENGINE_RULES

        import special_rules

        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        source = "".join(open(os.path.join(root, f), encoding="utf-8").read()
                         for f in ("unit_combat.py", "unit_model.py", "spells.py"))
        constants = {v for k, v in vars(special_rules).items() if isinstance(v, str)}
        for rule in UNIT_ENGINE_RULES:
            named = [k for k, v in vars(special_rules).items() if v == rule]
            with self.subTest(rule=rule):
                self.assertTrue(f'"{rule}"' in source or any(n in source for n in named),
                                f"{rule} is not read by the unit engine")
        self.assertTrue(constants)


class TestWholeFights(StatisticalCase):
    def test_identical_units_win_equally_often(self):
        runs = 1500 if FULL else 400
        stats = um.run_unit_statistics(troops(name="Left"), troops(name="Right"),
                                       um.UnitFight(charger=None), runs=runs, seed=5)
        a, b = stats.wins
        band = 4 * math.sqrt(max(a + b, 1)) + 5
        self.assertAlmostEqual(a, b, delta=band, msg=stats.summary())

    def test_seeded_runs_repeat(self):
        first = um.narrate_unit_fight(orcs(), troops(), seed=9)
        self.assertEqual(first, um.narrate_unit_fight(orcs(), troops(), seed=9))
        self.assertIn("Result:", first)

    def test_every_unit_can_fight(self):
        step = 1 if FULL else 7
        foe = troops()
        count = 0
        for faction in faction_names(UNIT):
            for profile in profile_names(faction, UNIT)[::step]:
                side = unit(faction, profile, models=10, frontage=5)
                with self.subTest(unit=profile):
                    dice.seed(count)
                    result = uc.fight(um.build_fight(side, foe, um.UnitFight(charger="A")))
                    self.assertIn(result.outcome, (uc.DESTROYED, uc.RUN_DOWN, uc.FLED, uc.FELL_BACK,
                                                   uc.GAVE_GROUND, uc.STALEMATE, uc.MUTUAL))
                count += 1


if __name__ == "__main__":
    unittest.main()
