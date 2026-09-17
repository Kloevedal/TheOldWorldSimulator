"""Draft MeleeWeaponDict entries for weapons the faction modules need.

    python3 tools/transcribe_weapons.py        # print entries for missing weapons

Reads each weapon's profile table and notes from its rules page. The notes
decide a few flags the table cannot show:

- a Strength modifier that applies only on the charge -> "1st round strength only"
- a weapon usable only on the charge -> "First Round Only"
- "Regeneration saves are not permitted" -> "No Regeneration Saves"
- "No armour save is permitted" (AP 'N/A') -> AP -6
- a weapon that makes one extra or one of several attacks each turn
  (tails, maws, Troll Vomit) -> "Secondary Attack", which keeps the
  faction generator from choosing it as a unit's weapon
- a rule limited to monsters is kept qualified, so the engine does not apply it

Print, review, then paste into weapons.py.
"""

from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))

import tow_site as site  # noqa: E402

SECONDARY = "Secondary Attack"

_CHARGE_STRENGTH = re.compile(
    r"strength modifier applies only (?:during the first round|against enemy models the wielder charged"
    r"|during a turn in which)", re.I)
_CHARGE_ONLY = re.compile(r"can only be used during a turn in which the wielder charged", re.I)
_SECONDARY = re.compile(r"(one of its attacks each turn|one additional attack|additional D3 attacks"
                        r"|each attack granted by the Extra Attacks)", re.I)


def notes_of(page_text):
    return " ".join(page_text.split("Notes:", 1)[1].split()) if "Notes:" in page_text else ""


def convert(table, notes):
    """(strength bonus, AP, rules, comment) for one profile table."""
    comment = []
    rules = []
    strength = str(table.get("strength") or "").strip()
    bonus = None
    if strength.upper() == "S":
        pass
    elif re.fullmatch(r"S[+-]\d+", strength, re.I):
        bonus = int(strength[1:])
    elif strength.isdigit():
        rules.append(f"Strength ({strength})")
    else:
        comment.append(f"Strength '{strength}' has no fixed value")

    ap_text = str(table.get("armourPiercing") or "-").strip()
    match = re.match(r"-(\d+)", ap_text)
    if match:
        ap = -int(match.group(1))
        if ap_text != match.group(0):
            comment.append(f"AP {ap_text} on the site")
    elif ap_text.upper() == "N/A" and "no armour save" in notes.lower():
        ap = -6
        comment.append("AP 'N/A': no armour save is permitted, which AP -6 guarantees")
    elif ap_text in ("-", "", "None"):
        ap = 0
    else:
        ap = 0
        comment.append(f"AP '{ap_text}' has no fixed value")

    only_monsters = "only applies against enemy models whose troop type is monster" in notes
    for rule in site.linked_names(table.get("specialRules")):
        extra = re.fullmatch(r"Extra Attacks \(\+(\d+)\)", rule)
        if extra:
            rules.append(f"+{extra.group(1)}A")
        elif only_monsters and rule.startswith("Multiple Wounds"):
            rules.append(rule[:-1] + ", against monsters)")
        elif rule.startswith("Strike First") and "applies only against charging" in notes:
            rules.append("Strike First (against chargers)")
        elif rule not in ("-",):
            rules.append(rule)
    if _CHARGE_ONLY.search(notes):
        rules.insert(0, "First Round Only")
    elif _CHARGE_STRENGTH.search(notes):
        rules.insert(0, "1st round strength only")
    if "Regeneration saves are not permitted" in notes:
        rules.append("No Regeneration Saves")
    if _SECONDARY.search(notes):
        rules.append(SECONDARY)
    if notes and not comment:
        comment.append(notes[:160] + ("..." if len(notes) > 160 else ""))
    return bonus, ap, rules, "; ".join(comment)


def missing_weapons():
    """{weapon name: (rule slug, table)} referenced by units and not in MeleeWeaponDict."""
    import transcribe_faction as tf
    from weapons import find_weapon_key

    found = {}
    for key, cfg in tf.FACTIONS.items():
        for section, slug, _name in site.army_units(cfg["army"]):
            if section == "Mount":
                continue
            unit = site.unit(slug)
            for _shown, link, kind in unit["equipment_links"] + unit["option_links"]:
                if kind != "rule" or not link:
                    continue
                category, table = tf.classify(link)
                if category != "melee":
                    continue
                name = tf.weapon_name(table)
                if find_weapon_key(name) is None and name not in found:
                    found[name] = (link, table)
    return found


def render(name, link, table):
    notes = notes_of(site.rule(link)["text"])
    bonus, ap, rules, comment = convert(table, notes)
    aliases = [name]
    plain = name.replace("'", "").replace("&", "and")
    if plain != name:
        aliases.append(plain)
    key = "(" + ", ".join(repr(a) for a in aliases) + ("," if len(aliases) == 1 else "") + ")"
    body = f"    {key}: [{bonus!r}, {ap}, {rules!r}],"
    return body + (f"  # {comment}" if comment else "")


if __name__ == "__main__":
    for name, (link, table) in sorted(missing_weapons().items()):
        print(render(name, link, table))
