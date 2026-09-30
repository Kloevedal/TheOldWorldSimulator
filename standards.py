"""What magic standards (and runic standards) do in a unit fight.

Written by hand from each standard's rules on tow.whfb.app. Every standard
in the item data is either in EFFECTS or in NOT_IN_A_FIGHT (tests check).
A standard only works while its unit still has its standard bearer.

Effect keys the unit fight reads (unit_combat):

    rules               special rules the unit gains
    rules_not_mounts    ... but not its mounts ("(but not its mounts)")
    stats               characteristic modifiers ({"Toughness": 1})
    fear_or_terror      the unit gains Fear, or Terror if it already has Fear
    charge_strength     +N Strength during a turn in which it charged
    charge_rules        rules gained during a turn in which it charged
    first_round_rules   rules gained in the first round of a combat
    cr                  combat result bonus: an int or a dice string ("D3")
    cr_charge           combat result bonus in a turn it charged
    cr_once             combat result bonus, once per fight (single use)
    rank_bonus_double   +2 per extra rank instead of +1
    lothern             with thrusting spears, half the next rank back (rounding
                        up) also makes supporting attacks
    steadfast           may Fall Back in Good Order even when outnumbered 2:1
    break_3d6           Break tests on 3D6, discarding the highest
    cold_blooded        once: an extra D6 on a Break test, discarding the highest
    ignore_negative_ld  negative Leadership modifiers do not apply
    ld_bonus            +N Leadership (to a maximum of 10)
    fearless            automatically passes Fear and Terror tests
    fear_3d6            Fear tests on 3D6, discarding the highest
    keep_frenzy         the unit cannot lose Frenzy
    improve_regen       Regeneration saves improve by N
    enemy_stats         enemy unit characteristic modifiers (dice rolled once per fight)
    enemy_ld            enemy unit Leadership penalty (to a minimum of 2)
    enemy_rules         rules the enemy unit gains ("all enemy models Hate the unit")
    enemy_fear_ld       enemy Leadership penalty on Fear tests
    enemy_fear_extra_die  enemy Fear tests roll an extra D6, discarding the lowest
    worse_armour_both   every model in the fight: armour save rolls -N
    front_charge_disordered  an enemy charging its front makes a disordered charge
    hesitation          an enemy charging its front does not count as charging for
                        weapons and special rules
    no_rear_bonus       enemies claim no bonus for its rear arc
    no_stomps_against   enemies may not make Stomp Attacks against it
    impact_reroll_wounds  re-roll failed To Wound rolls for its Impact Hits
    start_hits          (dice, Strength, AP) hits on the enemy at the start of each Combat phase
    spell_deflect       an enemy spell aimed at it is not cast on a D6 of N+
    enemy_casting       enemy Casting rolls suffer -N
    pursuit_dice        "one": Pursuit on one D6; "extra": 3D6 keep the two highest
    pursuit_reroll      may re-roll Pursuit rolls
    reroll_move_ones    re-roll natural 1s on Flee and Pursuit rolls
"""

from __future__ import annotations

EFFECTS = {
    # Combat result
    "War Banner": {"cr": 1},
    "Rune of Battle": {"cr": 1},
    "Master Rune of Stromni Redbeard": {"cr": 1},
    "The Jade Banner": {"cr": 2},
    "Battle Banner": {"cr": "D3"},
    "Banner of Unholy Victory": {"cr": "D3"},
    "Grand Banner of Superiority": {"cr": "D3"},
    "Standard of Slaughter": {"cr_charge": "D3"},
    "Banner of Renown": {"cr_once": 1},
    "Banner of Nagarythe": {"rules": ["Stubborn"], "cr": 1},
    "The Big Red Raggedy Flag": {"stats": {"WeaponSkill": 1}, "cr": 1},
    "Banner of the Wild Hunt": {"cr": 1, "pursuit_reroll": True},
    "Griffon Standard": {"rank_bonus_double": True},
    "The Banner of Lothern": {"lothern": True},
    # Rules the unit gains
    "Banner of Iron Resolve": {"rules": ["Stubborn"]},
    "Dwarf Hide Banner": {"rules": ["Hatred (Dwarfs)", "Stubborn"]},
    "The Banner of the Free State of Nuln": {"rules": ["Stubborn"]},
    "Banner of the Knights Panther": {"rules": ["Unbreakable"]},
    "Banner of Rage": {"rules": ["Frenzy"], "keep_frenzy": True},
    "Crusader's Tapestry": {"rules": ["Frenzy"]},
    "Da Angry Ladz Flag": {"rules": ["Frenzy"]},
    "Skavenpelt Banner": {"rules": ["Frenzy", "Hatred (Skaven)"]},
    "Shroud of the Ancestor": {"rules": ["Hatred (Dwarfs)"]},
    "The Soiled Tapestry": {"rules": ["Hatred (all enemies)"], "enemy_rules": ["Hatred (all enemies)"]},
    "Royal Standard of Settra": {"rules": ["Hatred (enemy characters)", "Terror"]},
    "Skull Totem": {"rules_not_mounts": ["Furious Charge"]},
    "Vitriolic Totem": {"rules": ["Poisoned Attacks"]},
    "Da Spider Banner": {"rules": ["Poisoned Attacks"]},
    "Razor Standard": {"rules": ["Armour Bane (2)"]},
    "The Blazing Banner": {"rules": ["Flaming Attacks"]},
    "Banner of the Dragon's Wrath": {"rules": ["Flaming Attacks", "Impact Hits (1)"]},
    "Dragonhide Banner": {"rules": ["Reroll Hits 1", "Flaming Attacks"]},
    "Banner of Har Ganeth": {"rules": ["Improve Armour Piercing (1)"]},
    "Standard of Seeping Decay": {"rules": ["Reroll Wounds 1"]},
    "The Banner of the Bold": {"rules": ["Veteran"]},
    "Banner of the Bastion": {"rules": ["Shieldwall"]},
    "Banner of Verminous Scurrying": {"rules": ["Swiftstride"]},
    "Master Rune of Grungni": {"rules": ["Ward5"]},
    "The Lammasu's Beard": {"rules": ["Ward6", "Magic Resistance (-2)"]},
    "Banner of Arcane Protection": {"rules": ["Magic Resistance (-3)"]},
    "Banner of Discord": {"rules": ["Magic Resistance (-3)"]},
    "Banner of the Dark Powers": {"rules": ["Magic Resistance (-3)"]},
    "Cannibal Totem": {"rules": ["Regeneration (5+)"], "pursuit_dice": "one"},
    "Rune of Fear": {"rules": ["Fear"]},
    "Totem of Prophecy": {"rules": ["Fear"]},
    "Standard of Wei-Jin": {"rules": ["Fear"], "enemy_fear_ld": 1},
    "Banner of the Wildwood": {"fear_or_terror": True},
    "Icon of Morr": {"fear_or_terror": True},
    "Sea Raider's Crest": {"fear_or_terror": True},
    "The Shroud of Shiyama": {"fear_or_terror": True},
    # Characteristics
    "Banner of Resilience": {"stats": {"Toughness": 1}},
    "Icon of the Sacred Eye": {"stats": {"WeaponSkill": 1}},
    # The charge
    "Da Banner of Butchery": {"charge_strength": 1},
    "Errantry Banner": {"charge_strength": 1, "rules": ["Impetuous"]},
    "Totem of Wrath": {"charge_rules": ["Improve Armour Piercing (1)", "Reroll Wounds 1"]},
    "Tapestry of Sigmar's Triumph": {"first_round_rules": ["Reroll Wounds 1"]},
    "Bull Standard": {"impact_reroll_wounds": True},
    "Rapturous Standard": {"front_charge_disordered": True},
    "Rune of Confusion": {"front_charge_disordered": True},
    "Master Rune of Hesitation": {"hesitation": True},
    # Leadership and Break tests
    "Valorous Standard": {"break_3d6": True},
    "Cold-Blooded Banner": {"cold_blooded": True},
    "Banner of the Steadfast": {"steadfast": True},
    "Banner of the Gods": {"ignore_negative_ld": True},
    "Banner of the Lady's Grace": {"ignore_negative_ld": True},
    "Tapestry of Talsyn": {"ld_bonus": 1},
    "Standard of Chaotic Glory": {"ld_bonus": 1},
    "Lion Standard": {"fearless": True},
    "Rune of Courage": {"fearless": True},
    "Imperial Banner": {"fear_3d6": True},
    "Doom Totem": {"enemy_ld": 1},
    "Manbane Standard": {"enemy_ld": 1},
    "The Screaming Banner": {"enemy_fear_extra_die": True},
    # The enemy
    "Banner of Acquiescence": {"enemy_stats": {"WeaponSkill": "-D3", "Initiative": "-D3"}},
    "Sigil of Centuries": {"enemy_stats": {"Initiative": -1}},
    "Totem of Rust": {"worse_armour_both": 1},
    "Rotten Icon": {"no_rear_bonus": True},
    "Monster Hunter's Tapestry": {"no_stomps_against": True},
    "Banner of Change": {"start_hits": ("3D6", 2, 0)},
    "Drakenhof Banner": {"improve_regen": 1},
    # Magic
    "Dragon's Eye Banner": {"spell_deflect": 4},
    "Rune Maw": {"spell_deflect": 3},
    "Great Standard of Sundering": {"enemy_casting": 1},
    # Pursuit
    "Jaguar Standard": {"pursuit_dice": "extra"},
    "Da Banner of Da Nomadz": {"reroll_move_ones": True},
}

# Why the other standards do nothing in a two-unit melee.
NOT_IN_A_FIGHT = {
    "Ashen Banner": "shooting",
    "Banner of Swirling Wind": "shooting",
    "Icon of Darkness": "shooting",
    "Mirage Banner": "shooting",
    "Sun Standard of Chotec": "Stand & Shoot and shooting",
    "Blasted Standard": "shooting",
    "Storm Banner": "shooting and flying",
    "Banner of Châlons": "Stand & Shoot",
    "Banner of Confidence": "Stand & Shoot",
    "The Banner of Xen Wun": "charge reactions",
    "Siren Standard": "charge reactions",
    "The Gore Banner": "declaring a charge",
    "Rampaging Banner": "charge range",
    "Waaagh! Banner": "charge range",
    "The Beast Banner": "charge range",
    "Icon of Endless War": "charge range",
    "Banner of Ellyrion": "movement",
    "Banner of the Wildz": "movement",
    "Banner of Midsummer's Eve": "shooting",
    "Banner of Springtide": "shooting",
    "Banner of the Hunter King": "deployment",
    "Banner of the Baying Hound": "deployment",
    "Banner of the Zealous Knight": "deployment",
    "Strollaz' Rune": "deployment",
    "Banner of the Desert Winds": "deployment and movement",
    "Standard of Hellish Vigour": "movement",
    "Icon of Rakaph": "movement",
    "Banner of the Warped Moon": "flying",
    "Icon of Heavenly Fury": "flying",
    "Banner of Duty": "rallying",
    "Guff's Windy Banner": "Panic tests",
    "The Gleaming Pennant": "Leadership tests outside combat (a Break test is not one)",
    "Banner of Outrage": "Primal Fury is not tested by rank and file yet",
    "Overseer's Sigil": "the Levies rule has no effect in a fight",
    "Conqueror's Tapestry": "victory points",
    "Tapestry of Conquered Lands": "victory points",
    "Standard of Morning's Chill": "a spell against shooting",
    "Icon of Sorcery": "Bound spells",
    "Totem of Eternal War": "Daemonic Instability is not simulated",
    "Banner of the Eternal Queen": "needs woodland terrain",
    "Banner of Honourable Warfare": "depends on the enemy carrying missile weapons",
    "Banner of Balance": "removing re-rolls is not simulated yet",
    "Banner of the Barrows": "To Hit rolls that always succeed on 3+ are not simulated yet",
    "Icon of Eternal Virulence": "counting Poisoned wounds is not simulated yet",
    "Standard of the Cursing Word": "not simulated yet",
}


def effect(name):
    return EFFECTS.get(name, {})
