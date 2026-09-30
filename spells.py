"""What spells do in a unit fight.

spells_data.py (generated) says each spell's lore, type, casting value and
how long it lasts; this module says, in game terms, what it does. The effects
are written by hand from each spell's rules on tow.whfb.app.

Hexes and Enchantments are chosen per side as spells that are "up": the
caster is assumed to cast them successfully at the start of each of its
turns. How long each lasts decides when it is in effect:

    "turn"     until the end of the caster's turn: only in the caster's turns
    "phase"    until the end of the Combat phase: only in the caster's turns
    "round"    until the caster's next Start of Turn: every turn
    "rip"      Remains in Play: every turn

Where a spell's effect depends on the casting result, the lower result's
effect is used. Assailment spells are cast by a Wizard in the fight at its
Initiative: 2D6 plus half its Level (rounding up), less the target's Magic
Resistance, against the casting value; a natural double 1 is a miscast (not
cast; what a miscast does to the Wizard is not simulated) and a natural
double 6 a perfect invocation. The enemy attempts a Wizardly dispel with a
Wizard in its unit, or else a Fated dispel (once per turn).
"""

from __future__ import annotations

import math
import re

from dice import roll_amount, roll_d6
from spells_data import SPELLS
from special_rules import RerollArmourSaveSixes

# -- Hexes and Enchantments -----------------------------------------------------

# stats: characteristic -> modifier (an int, or a dice string like "-D3",
# rolled when the spell is cast); ld: Leadership penalty (to a minimum of 2);
# rules: special rules gained; flags: effects the unit fight reads.
EFFECTS = {
    # Hexes
    "Gathering Darkness": {"stats": {"Initiative": -2}, "ld": 2, "flags": ["no_inspiring"]},
    "Word of Pain": {"stats": {"Strength": -1, "Toughness": -1}},
    "Storm Call": {"stats": {"Initiative": -1}},
    "Plague of Rust": {"rules": ["Worse Armour (2)"]},
    "Acquiescence": {"rules": ["Strike Last"]},
    "Itchy Nuisance": {"stats": {"Toughness": "-D3", "Initiative": "-D3"}},
    "Usekhp's Incantation of Desiccation": {"stats": {"Strength": -1, "Toughness": -1}},
    "Sapping Blight": {"stats": {"Strength": "-D3"}},
    "Chains of Darkness": {"ld": 1},
    "Troll Brainz": {"ld": 1},
    "Curse of Years": {"stats": {"WeaponSkill": -1, "Toughness": -1}},
    "Spirit Leech": {"ld": 2, "flags": ["no_inspiring"]},
    "Bad Moon Rizin'": {"stats": {"WeaponSkill": "-D3", "Initiative": "-D3"}},
    "Accursed Mirror": {"flags": ["accursed_mirror"]},
    "Mork’s Curse": {"rules": [RerollArmourSaveSixes]},
    "Storm of Ash": {"rules": ["To Hit (-1)"]},
    "Cursing Word": {"stats": {"WeaponSkill": -1}},  # the caster picks Weapon Skill in combat
    # Enchantments
    "Oaken Shield": {"rules": ["Ward5"]},
    "Daemonic Vessel": {"stats": {"Strength": 1, "Attacks": 1}, "rules": ["Improve Armour Piercing (1)"]},
    "Daemonic Vigour": {"stats": {"Toughness": 1, "Initiative": 1}},
    "Battle Lust": {"rules": ["Frenzy", "Hatred (all enemies)"]},
    "Earthen Ramparts": {"rules": ["Ward5"], "flags": ["ramparts"]},
    "Fury of Khaine": {"rules": ["Extra Attacks (+1)"]},
    "Shield of Saphery": {"rules": ["Ward5"]},
    "Glittering Robe": {"rules": ["Enemy To Hit (-1)"]},
    "Fleshy Abundance": {"stats": {"Toughness": 1}, "max": {"Toughness": 7}},
    "Djaf's Incantation of Cursed Blades": {"rules": ["Reroll Hits 1"], "needs": "Nehekharan Undead"},
    "Fury of the Beast": {"rules": ["Fight in Extra Rank"]},
    "Courage of Aenarion": {"rules": ["Unbreakable"]},
    "Toothcracker": {"stats": {"Toughness": 1}},
    "Trollguts": {"rules": ["Regeneration (6+)"]},
    "The Lady's Gift": {"rules": ["Regeneration (6+)"]},
    "The Lady's Wrath": {"stats": {"Strength": 1}, "rules": ["Improve Armour Piercing (1)"]},
    "Ariel's Blessing": {"rules": ["Regeneration (5+)"]},
    "Rapid Regeneration": {"rules": ["Flammable", "Regeneration (5+)"]},
    "Great Bastion": {"rules": ["Ward6"]},
    "Might of Heaven & Earth": {"stats": {"WeaponSkill": 1, "Strength": 1}, "rules": ["Flaming Attacks"]},
    "Deathly Cabal": {"rules": ["Ward6 (non-magical)"], "flags": ["fear_or_terror"]},
    "Evil Sun Shinin'": {"rules": ["Reroll Hits 1", "Improve Armour Piercing (1)"]},
}

# Why the other Hexes and Enchantments have no effect in a unit fight.
NOT_IN_A_FIGHT = {
    "Curse of Arrow Attraction": "affects shooting",
    "Curse of Cowardly Flight": "a Panic test before the fight",
    "Drain Magic": "affects enemy casting values across the battlefield",
    "Confounding Convocation": "Stupidity is not tested in combat",
    "Cacophonic Hymn": "Stupidity is not tested in combat",
    "Miasmic Mirage": "affects movement",
    "Winds of Chaos": "affects movement",
    "Spirits of Wind & Shadow": "affects movement",
    "Khsar's Incantation of the Desert Wind": "affects movement",
    "Hellish Vigour": "affects movement",
    "'Ere We Go!": "affects charge range",
    "Veil of Gloom": "affects templates and shooting",
    "Swirling Mists": "affects shooting",
    "Big Smartz": "Stupidity is not tested in combat",
    "Raise Dead": "summons a new unit",
    "Vaul's Unmaking": "destroys a magic item",
    "Apotheosis": "targets a character",
    "Mantle of Ghorok": "affects only the caster",
    "Gift of Mutation": "the caster chooses characteristics (not simulated yet)",
    "Vanhal's Danse Macabre": "the caster chooses characteristics (not simulated yet)",
    "In the Gloaming Wildwood": "not simulated yet",
}


def hexes_and_enchantments():
    """{"Hex": [names], "Enchantment": [names]} that do something in a fight."""
    found = {"Hex": [], "Enchantment": []}
    for name, data in sorted(SPELLS.items()):
        if data["type"] in found and name in EFFECTS:
            found[data["type"]].append(name)
    return found


def active(name, caster_side, active_side, turn):
    duration = SPELLS.get(name, {}).get("duration", "round")
    if duration in ("turn", "phase", "instant"):
        return caster_side == active_side
    return True


def _roll(value):
    if isinstance(value, int):
        return value
    sign = -1 if value.startswith("-") else 1
    return sign * roll_amount(value.lstrip("+-"))


def apply(name, unit, fight, cast_turn=0):
    """Apply a Hex or Enchantment to every model of `unit` for this turn.
    `cast_turn` is the turn it was (last) cast in; dice modifiers are rolled
    once per cast."""
    effect = EFFECTS.get(name)
    if not effect:
        return
    if effect.get("needs") and effect["needs"] not in (unit.model.SpecialRules or []):
        return
    rolls = getattr(unit, "spell_rolls", None)
    if rolls is None:
        rolls = unit.spell_rolls = {}
    models = list(unit.all_models()) + list(unit.parts)
    for placed in unit.characters:
        models += list(getattr(placed.character, "mount_parts", []))
    stats = {}
    for stat, change in (effect.get("stats") or {}).items():
        # A dice modifier is rolled once per cast and kept while the spell lasts.
        key = (name, stat, cast_turn)
        if key not in rolls:
            rolls[key] = _roll(change)
        stats[stat] = rolls[key]
    for model in models:
        for stat, change in stats.items():
            value = getattr(model, stat, None)
            if isinstance(value, int):
                high = (effect.get("max") or {}).get(stat, 10)
                setattr(model, stat, max(1, min(high, value + change)))
                if stat == "Strength":
                    model.original_Strength = model.Strength
        for rule in effect.get("rules", []):
            if rule not in (model.SpecialRules or []):
                model.SpecialRules = list(model.SpecialRules or []) + [rule]
    if effect.get("ld"):
        unit.ld_penalty = getattr(unit, "ld_penalty", 0) + effect["ld"]
    for flag in effect.get("flags", []):
        if flag == "fear_or_terror":
            for model in models:
                have = model.SpecialRules or []
                extra = "Terror" if "Fear" in have else "Fear"
                if extra not in have:
                    model.SpecialRules = list(have) + [extra]
        else:
            setattr(unit, flag, True)


# -- Assailment spells ----------------------------------------------------------

# kind: "unit" (hits on the unit) or "model" (a single model); hits: dice;
# S, AP; flags: no_armour, no_regen, flaming, multiple (Multiple Wounds),
# armour_bane.
ASSAILMENT = {
    "Hammerhand": {"hits": "2D3", "S": 4, "AP": 2},
    "Daemonic Familiars": {"hits": "2D6", "S": 2, "no_armour": True},
    "Soul Eater": {"kind": "model", "hits": 1, "S": 3, "multiple": 3, "no_armour": True},
    "Flaming Sword": {"hits": "D6+1", "S": 3, "flaming": True},
    "Corporeal Unmaking": {"hits": "D3", "S": 5, "no_armour": True, "no_regen": True},
    "Spectral Doppelganger": {"hits": "2D6", "S": "caster"},
    "Brain Bursta": {"kind": "model", "hits": 1, "S": 6, "multiple": "D3", "no_armour": True, "no_regen": True},
    "Flames of Hashut": {"hits": "D3+1", "S": 4, "AP": 1, "flaming": True},
    "Hand of Khaine": {"kind": "model", "hits": 1, "S": 4, "no_armour": True},
    "Shadowed Assailants": {"hits": "3D6", "S": 1, "no_armour": True, "no_regen": True},
    "Durthu's Wrath": {"initiative_test": True, "hits": "D3", "S": 4, "no_armour": True},
    "Ancestral Warriors": {"hits": "2D3", "S": 2, "armour_bane": 2,
                           "better": (11, {"hits": "2D6", "S": 4, "AP": 1})},
}
ASSAILMENT_NOT_SIMULATED = {
    "Stream of Corruption": "a flame template",
    "Torrent of Filth": "a flame template",
    "Flock of Doom (Beastmen)": "a scattering blast template",
    "The Dwellers Below": "a scattering blast template",
    "Fist of Gork (or Mork)": "a scattering blast template",
}


def assailment_spells(lores):
    """Assailment spells a Wizard of these lores may know, simulated ones only."""
    return sorted(n for n, d in SPELLS.items()
                  if d["type"] == "Assailment" and d["lore"] in lores and n in ASSAILMENT)


def _magic_resistance(unit):
    best = 0
    for model in unit.all_models():
        for rule in model.SpecialRules or []:
            match = re.fullmatch(r"Magic Resistance \(-(\d)\)", str(rule))
            if match:
                best = max(best, int(match.group(1)))
    return best


def cast_assailment(fight, index, placed, name):
    """Cast one Assailment spell. Returns a function applying its damage, or None."""
    from combat_simulations import RollArmorSave, RollToWound

    spell = ASSAILMENT.get(name)
    data = SPELLS.get(name)
    if not spell or not data:
        return None
    casts = fight.casts = getattr(fight, "casts", {})
    key = (fight.turn, id(placed), name)
    if key in casts:  # each spell only once per turn
        return None
    casts[key] = True
    enemy_index = 1 - index
    enemy = fight.units[enemy_index]
    caster = placed.character
    if enemy.flag("spell_deflect") and roll_d6() >= enemy.flag("spell_deflect"):
        fight.say(f"{caster.name} cannot cast {name}: {enemy.name}'s standard turns it aside")
        return None
    first, second = roll_d6(), roll_d6()
    level = max(1, placed.wizard_level)
    result = (first + second + math.ceil(level / 2) - _magic_resistance(enemy)
              - (enemy.flag("enemy_casting") or 0))
    who = f"{caster.name} casts {name}"
    if (first, second) == (1, 1):
        fight.say(f"{who}: miscast (1+1) - not cast")
        return None
    perfect = (first, second) == (6, 6)
    if not perfect and result < (data.get("cv") or 99):
        fight.say(f"{who}: {first}+{second} -> {result}, needs {data['cv']} - fails")
        return None
    if not perfect and _dispelled(fight, enemy_index, result):
        return None
    fight.say(f"{who}: {'perfect invocation' if perfect else result} - cast")

    effect = dict(spell)
    better = effect.pop("better", None)
    if better and result >= better[0]:
        effect.update(better[1])
    strength = caster.Strength if effect["S"] == "caster" else effect["S"]
    if effect.get("initiative_test"):
        slots, _touching = fight.fighting_line(enemy_index)
        count = 0
        for _ in range(sum(1 for o in slots.values() if o in ("rf", "standard", "musician", "champion"))):
            roll = roll_d6()
            if roll == 6 or (roll != 1 and roll > (enemy.model.Initiative or 0)):
                count += roll_amount(effect["hits"])
    else:
        count = roll_amount(effect["hits"])
    rules = ["Magical Attacks"]
    if effect.get("flaming"):
        rules.append("Flaming Attacks")
    if effect.get("no_armour"):
        rules.append("No Armour Saves")
    if effect.get("armour_bane"):
        rules.append(f"AB{effect['armour_bane']}")
    weapon = caster.Weapon if effect["S"] == "caster" else None
    striker = type("SpellHits", (), {})()
    striker.name, striker.Strength, striker.original_Strength = name, strength, strength
    striker.SpecialRules = rules + (list(caster.SpecialRules or []) if effect["S"] == "caster" else [])
    striker.Weapon = weapon
    striker.ArmourPiercing = effect.get("AP", 0)
    striker.TroopType = None
    if enemy.models <= 0 or count <= 0:
        return None
    wounds, flaming, magical = RollToWound(striker, enemy.model, count, verbose=False)
    unsaved = RollArmorSave(striker, enemy.model, wounds, verbose=False)
    multiple = effect.get("multiple", 1)
    fight.say(f"{name}: {count} hit(s) -> {len(unsaved)} unsaved")

    def apply():
        fight.wound_unit(enemy_index, unsaved, flaming, True, multiple,
                         bool(effect.get("no_regen")), strength)
    return apply


def _dispelled(fight, index, casting_result):
    """The side `index` tries to dispel. True if it succeeds."""
    unit = fight.units[index]
    wizards = [p for p in unit.fighters() if p.wizard_level]
    first, second = roll_d6(), roll_d6()
    if wizards:
        level = max(p.wizard_level for p in wizards)
        result = first + second + math.ceil(level / 2)
        kind = "Wizardly dispel"
    else:
        fated = fight.fated = getattr(fight, "fated", set())
        if (fight.turn, index) in fated:
            return False
        fated.add((fight.turn, index))
        result = first + second
        kind = "Fated dispel"
    if (first, second) == (6, 6):
        fight.say(f"{unit.name}: {kind} {first}+{second} - unbinding, dispelled")
        return True
    dispelled = result > casting_result and (first, second) != (1, 1)
    fight.say(f"{unit.name}: {kind} {first}+{second} -> {result} "
              + ("- dispelled" if dispelled else "- fails"))
    return dispelled
