"""Impact Hits, Stomp Attacks, Thunderstomp and Extra Attacks.

Impact Hits land before any other blow in the first (charge) round; Stomp
Attacks come after every other attack, each round. Both hit automatically and
use the model's unmodified Strength.
"""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from support import SAMPLES_LARGE, StatisticalCase, all_profiles, build, fighter

import dice
from combat_simulations import (
    AutomaticHits,
    OneRoundMeleeCombat,
    combat_simulation,
)
from special_rules import parse_impact_hits, parse_stomp_attacks

N = SAMPLES_LARGE * 2


def narrate(a, b, rounds=2):
    out = io.StringIO()
    with redirect_stdout(out):
        winner = combat_simulation(a, b, rounds=rounds, verbose=True)
    return out.getvalue(), winner


class TestOrdering(unittest.TestCase):
    def test_impact_hits_land_before_the_first_blow(self):
        rhino = fighter("Rhino", Attacks=0, SpecialRules=["Impact Hits (1)"])
        victim = fighter("Victim", Wounds=1, Initiative=10, SpecialRules=["Strike First"])
        with dice.constant_dice(6):
            text, winner = narrate(rhino, victim)
        self.assertIs(winner, rhino)
        self.assertNotIn("Victim strikes", text)

    def test_impact_hits_only_in_the_first_round(self):
        rhino = fighter("Rhino", Attacks=0, SpecialRules=["Impact Hits (1)"])
        wall = fighter("Wall", Attacks=0, Toughness=10, Wounds=5)
        with dice.constant_dice(4):
            text, _ = narrate(rhino, wall, rounds=3)
        self.assertEqual(text.count("Impact Hits"), 1)

    def test_stomps_come_after_every_other_attack_each_round(self):
        giant = fighter("Giant", Attacks=0, Toughness=10, Wounds=5,
                        SpecialRules=["Stomp Attacks (1)"])
        wall = fighter("Wall", Attacks=1, Toughness=10, Wounds=5, Initiative=1,
                       SpecialRules=["Strike Last"])
        with dice.constant_dice(4):
            text, _ = narrate(giant, wall, rounds=3)
        self.assertEqual(text.count("Stomp Attacks"), 3)
        for round_text in text.split("=== Round")[1:]:
            self.assertLess(round_text.index("Wall strikes"), round_text.index("Stomp Attacks"))

    def test_a_slain_model_does_not_stomp(self):
        giant = fighter("Giant", Attacks=0, Wounds=1, SpecialRules=["Stomp Attacks (3)"])
        killer = fighter("Killer", Attacks=5)
        with dice.constant_dice(6):
            text, winner = narrate(giant, killer)
        self.assertIs(winner, killer)
        self.assertNotIn("Stomp Attacks", text)

    def test_simultaneous_impact_kills_are_a_draw(self):
        a = fighter("A", Wounds=1, SpecialRules=["Impact Hits (1)"])
        b = fighter("B", Wounds=1, SpecialRules=["Impact Hits (1)"])
        with dice.constant_dice(6):
            _, winner = narrate(a, b)
        self.assertIsNone(winner)
        self.assertEqual((a.current_wounds, b.current_wounds), (0, 0))


class TestAutomaticHits(StatisticalCase):
    def test_they_use_unmodified_strength(self):
        brute = fighter("Brute", Strength=3, Weapon="Great Weapon",
                        SpecialRules=["Stomp Attacks (1)"])
        with dice.constant_dice(4):
            text, _ = narrate(brute, fighter("Wall", Toughness=10, Wounds=9), rounds=1)
        self.assertIn("1 Stomp Attacks (S3)", text)

    def test_weapon_rules_do_not_carry_over(self):
        # A Killing Blow weapon does not make impact hits Killing Blows.
        killer = fighter(Weapon="Hand Weapon", SpecialRules=["Killing Blow"])
        with dice.constant_dice(6):
            result = AutomaticHits(killer, fighter(), ["D3"], verbose=False)
        self.assertTrue(result.unsaved)
        self.assertFalse(any(w.killing_blow for w in result.unsaved))

    def test_magical_and_flaming_attacks_do_carry_over(self):
        caster = fighter(SpecialRules=["Magical Attacks", "Flaming Attacks"])
        with dice.constant_dice(6):
            result = AutomaticHits(caster, fighter(), [1], verbose=False)
        self.assertTrue(result.is_magical and result.is_flaming)

    def test_a_behemoths_stomps_have_armour_piercing_except_against_monsters(self):
        from combat_simulations import _thunderstomp_ap

        behemoth = fighter()
        behemoth.TroopType = "Behemoth"
        other = fighter()
        other.TroopType = "MonstrousCreature"
        self.assertEqual(_thunderstomp_ap(behemoth, fighter()), 2)
        self.assertEqual(_thunderstomp_ap(behemoth, other), 0)
        self.assertEqual(_thunderstomp_ap(fighter(), fighter()), 0)

    def test_thunderstomp_affects_the_save(self):
        # Heavy armour 5+ becomes 7+: no save at all.
        behemoth = fighter(SpecialRules=["Stomp Attacks (1)"])
        with dice.constant_dice(6):
            result = AutomaticHits(behemoth, fighter(Armor="Heavy Armor"), [1],
                                   verbose=False, armour_piercing=2)
        self.assertEqual(result.saves, 0)
        self.assertEqual(len(result.unsaved), 1)

    def test_impact_hit_armour_piercing_from_an_item(self):
        rider = fighter(magic_items=["Crown of Antlers"])
        self.assertIn("Impact Hits Armour Piercing (2)", rider.SpecialRules)

    def test_dice_amounts_average_out(self):
        for amount, mean in (("D3", 2), ("D6", 3.5), ("D3+1", 3), ("2D3", 4), (2, 2)):
            with self.subTest(amount=amount):
                dice.seed(0)
                total = sum(AutomaticHits(fighter(), fighter(), [amount], verbose=False).hits
                            for _ in range(N))
                self.assertAlmostEqual(total / N, mean, delta=0.08)

    def test_expected_wounds_from_impact_hits(self):
        # D3 hits at S4 v T4 (1/2), no armour: 1 wound on average.
        dice.seed(0)
        total = sum(len(AutomaticHits(fighter(), fighter(), ["D3"], verbose=False).unsaved)
                    for _ in range(N))
        self.assertAlmostEqual(total / N, 1.0, delta=0.06)


class TestExtraAttacks(StatisticalCase):
    def test_dice_extra_attacks_are_rolled_once_per_round(self):
        frenzy = fighter(Attacks=1, SpecialRules=["Extra Attacks (+D3)"])
        dice.seed(0)
        total_attacks = 0
        for _ in range(N):
            result = OneRoundMeleeCombat(frenzy, fighter(), verbose=False, is_first_round=False)
            total_attacks += result.attacks
            self.assertLessEqual(result.hits, result.attacks)
        self.assertAlmostEqual(total_attacks / N, 3.0, delta=0.05)

    def test_a_scripted_round_uses_the_rolled_count(self):
        # Extra Attacks (+D3): a roll of 1 gives +1, so 2 attacks in all.
        frenzy = fighter(Attacks=1, SpecialRules=["Extra Attacks (+D3)"])
        target = fighter(Toughness=10)  # S4 cannot wound T10: no more dice
        with dice.scripted_dice([1, 6, 6]):
            result = OneRoundMeleeCombat(frenzy, target, verbose=False, is_first_round=False)
        self.assertEqual((result.attacks, result.hits), (2, 2))

    def test_a_weapon_with_extra_attacks(self):
        from weapons import get_weapon_stats

        weapon = next(name for name in ("Blades of Loec", "Pearl Daggers")
                      if "Extra Attacks (+D3)" in get_weapon_stats(name)[2])
        wielder = fighter(Attacks=1, Weapon=weapon)
        dice.seed(1)
        total = sum(OneRoundMeleeCombat(wielder, fighter(), verbose=False,
                                        is_first_round=False).attacks for _ in range(N))
        self.assertAlmostEqual(total / N, 3.0, delta=0.05)


class TestMonstrousProfiles(unittest.TestCase):
    def test_every_profile_with_impact_or_stomps_fights(self):
        dice.seed(9)
        found = 0
        for kind in ("characters", "units"):
            for faction, profile in all_profiles(kind):
                model = build(faction, profile, name="Monster")
                if not (parse_impact_hits(model.SpecialRules) or parse_stomp_attacks(model.SpecialRules)):
                    continue
                found += 1
                with self.subTest(profile=profile):
                    foe = build(faction, profile, name="Foe")
                    with redirect_stdout(io.StringIO()):
                        winner = combat_simulation(model, foe, rounds=3, verbose=False)
                    self.assertIn(winner, (model, foe, None))
                    self.assertGreaterEqual(model.current_wounds, 0)
        self.assertGreater(found, 20)


if __name__ == "__main__":
    unittest.main()
