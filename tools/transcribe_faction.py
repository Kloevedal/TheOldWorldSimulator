"""Draft a faction module from https://tow.whfb.app.

    python3 tools/transcribe_faction.py <config key>      # print the module
    python3 tools/transcribe_faction.py <config key> -w   # write factions/<module>.py

The output follows the layout of the hand-written modules: character profiles
with statlines, points, equipment options and mounts, plus FACTION_RULES with
each rule's text as the site gives it. What the engine can do with a rule is
decided by `ENGINE_RULES` below, not guessed per faction.

Weapons that have no melee profile (bows, pistols, breath weapons, thrown
weapons) are left out of the equipment options - shooting is not simulated -
and listed in the profile's comment instead. Melee weapons missing from
`MeleeWeaponDict` are reported, so their profiles can be added by hand.

The draft is a starting point: named characters' magic items and anything the
generator reports under "REVIEW" still need a human pass.
"""

from __future__ import annotations

import os
import re
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

import tow_site as site  # noqa: E402
import transcribe_mounts as mount_names  # noqa: E402

# Site rule name -> extra rule strings the engine parses, appended after the
# rule itself (the way Blackshard Armour carries "Ward5 (Flaming)").
RULE_COMPANIONS = {
    # Daemonic is a bundle; the Daemons of Chaos characters carry it expanded.
    "Daemonic": ["Ward5 (non-magical)", "Daemonic Instability", "Fear",
                 "Immune to Psychology", "Magical Attacks", "Unbreakable",
                 "Warp-spawned"],
    "Blackshard Armour": ["Ward5 (Flaming)"],
    "Blessings of Ulric": ["Ward6 (Flaming)"],
    "Blessings of the Horned Rat": ["Ward5 (non-magical)"],
    "Dark Runes": ["Ward5 (non-magical)"],
    "Daughters of Eternity": ["Ward4"],
    "Relentless Warriors": ["Ward6 (non-magical)"],
    "Runes of Protection": ["Ward6 (non-magical)"],
    "Runes of Warding": ["Ward5 (Flaming)"],
    "Inner Circle": ["Reroll Hits 1"],
    "Ancestral Shield": ["Ward5"],
    "Arcane Shield": ["Ward5"],
    "Blessed Knight": ["Ward5"],
    "Favour of the Goddess": ["Ward5"],
    "Talismanic Tattoos": ["Ward6"],
    "Celestial Forged Armour (5+)": ["Ward5"],
    "Blessings of the Volcano God": ["Ward4 (Flaming)"],
    # A duel is fought as a challenge, which is when this rule applies.
    "Settra's Champion": ["Killing Blow 5+"],
}

# Base rule name -> engine status. Anything else is recorded only (None).
ENGINE_RULES = {
    "Accursed Weapons": "implemented",
    "Blessings of Ulric": "implemented",
    "Blessings of the Horned Rat": "implemented",
    "Dark Runes": "implemented",
    "Daughters of Eternity": "implemented",
    "Relentless Warriors": "implemented",
    "Runes of Protection": "implemented",
    "Runes of Warding": "implemented",
    "Inner Circle": "implemented",
    "Daemonic": "implemented",
    "Blackshard Armour": "implemented",
    "Blood Rage": "implemented",
    "Primal Fury": "implemented",
    "Ensorcelled Weapons": "implemented",
    "Murderous": "implemented",
    "Ithilmar Weapons": "implemented",
    "Choppas": "implemented",
    "Gromril Armour": "implemented",
    "Monster Slayer": "implemented",
    "Cleaving Blow": "implemented",
    "Ancestral Shield": "implemented",
    "Strike First": "implemented",
    "Strike Last": "implemented",
    "Killing Blow": "implemented",
    "Armour Bane": "implemented",
    "Armoured Hide": "implemented",
    "Regeneration": "implemented",
    "Frenzy": "implemented",
    "Furious Charge": "implemented",
    "Hatred": "implemented",
    "Ethereal": "implemented",
    "Magical Attacks": "implemented",
    "Flaming Attacks": "implemented",
    "Elven Reflexes": "implemented",
    "Gromril Weapons": "implemented",
    "Arcane Shield": "implemented",
    "Blessed Knight": "implemented",
    "Favour of the Goddess": "implemented",
    "Talismanic Tattoos": "implemented",
    "Celestial Forged Armour": "implemented",
    "Blessings of the Volcano God": "implemented",
    "Khopesh": "implemented",
    "Obsidian Blades": "implemented",
    "Warpstone Weapons": "implemented",
    "Settra's Champion": "partial",
    "Flammable": "implemented",
    "Poisoned Attacks": "implemented",
    "Impact Hits": "implemented",
    "Stomp Attacks": "implemented",
    "Extra Attacks": "implemented",
    "Blessings of the Lady": "implemented",
    "The Grail Vow": "implemented",
    "Mark of Khorne": "implemented",
    "Mark of Nurgle": "implemented",
    "Mark of Slaanesh": "implemented",
    "Mark of Tzeentch": "implemented",
}

# A model's printed armour value -> the ArmourDict name that gives it.
ARMOUR_VALUES = {
    "6+": "Light Armor",
    "5+": "Heavy Armor",
    "4+": "Full Plate Armor",
    "3+": "Armour Value 3+",
    "2+": "Armour Value 2+",
}

ARMOUR = {
    "light armour": "Light Armor",
    "heavy armour": "Heavy Armor",
    "full plate armour": "Full Plate Armor",
}

# Site weapon name -> MeleeWeaponDict name, where they differ.
WEAPON_NAMES = {
    "Two Hand Weapons/Additional Hand Weapon": "Two Hand Weapons",
    "Spectral Scythe (Cairn Wraith)": "Spectral Scythe",
}

TROOP_TYPES = {"Character", "Named Character"}

# Per-faction settings. `race` is the default; `races` overrides by profile.
# `overrides` corrects a profile where the site's own row cannot be used as is,
# and says why in the profile's comment.
FACTIONS = {
    "cathay": dict(
        module="grand_cathay", faction="Grand Cathay", army="grand-cathay",
        title="Grand Cathay",
        aliases=["Cathay", "Empire of Grand Cathay", "Grand Cathay"],
        profile_aliases={"Miao": "Miao Ying", "Storm Dragon": "Miao Ying"},
        race="Cathayan",
        unit_races=[("ogre", "Ogre")],
    ),
    "bretonnia": dict(
        module="kingdom_of_bretonnia", faction="Kingdom of Bretonnia",
        army="kingdom-of-bretonnia", title="Kingdom of Bretonnia",
        aliases=["Bretonnia", "Bretonnians", "Kingdom of Bretonnia"],
        profile_aliases={
            "Elisse": "Lady Élisse Duchaard",
            "Lady Elisse Duchaard": "Lady Élisse Duchaard",
            "Cecil Gastonne": "Sir Cecil Gastonne",
            "Green Knight": "The Green Knight",
        },
        race="Bretonnian",
        overrides={
            "Lady Élisse Duchaard": {
                "comment": ("Armour Bane (2) is Ariandir's; Armoured Hide (1) "
                            "improves her unarmoured 7+ to a 6+ save."),
            },
        },
    ),
    "lizardmen": dict(
        module="lizardmen", faction="Lizardmen", army="lizardmen",
        title="Lizardmen",
        aliases=["Lizardmen", "Lizardman", "Seraphon"],
        profile_aliases={"Oldblood": "Saurus Oldblood", "Scar-Veteran": "Saurus Scar-Veteran",
                         "Slann": "Slann Mage-Priest"},
        race="Lizardman",
        races={"Saurus Oldblood": "Saurus", "Saurus Scar-Veteran": "Saurus",
               "Skink Chief": "Skink", "Skink Priest": "Skink",
               "Slann Mage-Priest": "Slann"},
        unit_races=[("skink", "Skink"), ("saurus|temple guard|cold one", "Saurus")],
    ),
    "ogres": dict(
        module="ogre_kingdoms", faction="Ogre Kingdoms", army="ogre-kingdoms",
        title="Ogre Kingdoms",
        aliases=["Ogres", "Ogre Kingdoms", "OK"],
        profile_aliases={"Ogre Tyrant": "Tyrant", "Ogre Bruiser": "Bruiser"},
        race="Ogre",
        unit_races=[("gnoblar", "Gnoblar"), ("giant", "Giant")],
    ),
    "realms_of_men": dict(
        module="realms_of_men", faction="Realms of Men", army="realms-of-men",
        title="Realms of Men",
        aliases=["Realms of Men", "Renegades"],
        profile_aliases={},
        race="Human",
    ),
    "renown": dict(
        module="regiments_of_renown", faction="Regiments of Renown",
        army="regiments-of-renown", title="Regiments of Renown",
        aliases=["Regiments of Renown", "Dogs of War"],
        profile_aliases={"Prince Ulther": "Prince Ulther's Dragon Company",
                         "Ulther": "Prince Ulther's Dragon Company"},
        race="Dwarf",
    ),
    "skaven": dict(
        module="skaven", faction="Skaven", army="skaven", title="Skaven",
        aliases=["Skaven", "Ratmen", "Clans of Skaven"],
        profile_aliases={"Warlord": "Skaven Warlord", "Chieftain": "Skaven Chieftain",
                         "Assassin": "Master Assassin"},
        race="Skaven",
    ),
    "tomb_kings": dict(
        module="tomb_kings_of_khemri", faction="Tomb Kings of Khemri",
        army="tomb-kings-of-khemri", title="Tomb Kings of Khemri",
        aliases=["Tomb Kings", "TK", "Khemri", "Tomb Kings of Khemri"],
        profile_aliases={"Settra": "Settra the Imperishable",
                         "Apophas": "Prince Apophas"},
        race="Tomb King",
        overrides={
            "Settra the Imperishable": {
                "base_profile": {"Wounds": 8},
                "comment": ("Settra's own Wounds are '-': he uses the Chariot "
                            "of the Gods' W8 (and its T5, the same as his)."),
            },
        },
    ),
    "vampires": dict(
        module="vampire_counts", faction="Vampire Counts", army="vampire-counts",
        title="Vampire Counts",
        aliases=["Vampire Counts", "VC", "Vampires", "Undead"],
        profile_aliases={"Necromancer": "Master Necromancer",
                         "Acolyte": "Necromantic Acolyte",
                         "Banshee": "Tomb Banshee",
                         "Ghoul King": "Strigoi Ghoul King"},
        race="Vampire",
        races={"Master Necromancer": "Necromancer",
               "Necromantic Acolyte": "Necromancer",
               "Cairn Wraith": "Spirit", "Tomb Banshee": "Spirit",
               "Wight King": "Wight", "Wight Lord": "Wight",
               "Strigoi Ghoul King": "Vampire"},
        unit_race="Undead",
        unit_races=[("ghoul|crypt horror", "Ghoul"),
                    ("vargheist|blood knight|varghulf|coven throne", "Vampire")],
    ),
    "wood_elves": dict(
        module="wood_elf_realms", faction="Wood Elf Realms",
        army="wood-elf-realms", title="Wood Elf Realms",
        aliases=["Wood Elves", "Wood Elf", "Asrai", "Wood Elf Realms"],
        profile_aliases={"Araloth": "Araloth, Lord of Talsyn",
                         "Orion": "Orion, the King in the Woods"},
        race="Wood Elf",
        races={"Branchwraith": "Forest Spirit",
               "Treeman Ancient": "Forest Spirit"},
        unit_races=[("dryad|tree", "Forest Spirit")],
    ),
    # The factions whose characters were hand-transcribed. Only their UNITS
    # (and any FACTION_RULES entries those units add) are generated.
    "high_elves": dict(module="high_elves", faction="High Elves",
                       army="high-elf-realms", race="High Elf", legacy=True),
    "orcs": dict(module="orc_and_goblin_tribes", faction="Orcs",
                 army="orc-and-goblin-tribes", race="Orc", legacy=True,
                 unit_races=[("night goblin|fanatic", "Night Goblin"),
                             ("snotling", "Snotling"), ("squig", "Squig"),
                             ("goblin|skulker|arachnarok|doom diver|throwa|lobber", "Goblin"),
                             ("troll", "Troll"), ("giant", "Giant"), ("ogre", "Ogre")]),
    "chaos": dict(module="warriors_of_chaos", faction="Warriors of Chaos",
                  army="warriors-of-chaos", race="Chaos Warrior", legacy=True,
                  unit_races=[("marauder|skin wolves", "Chaos Marauder"),
                              ("ogre", "Ogre"), ("troll", "Troll")]),
    "empire": dict(module="empire_of_man", faction="Empire of Man",
                   army="empire-of-man", race="Human", legacy=True,
                   unit_races=[("ogre", "Ogre")]),
    "dwarfs": dict(module="dwarfen_mountain_holds", faction="Dwarfen Mountain Holds",
                   army="dwarfen-mountain-holds", race="Dwarf", legacy=True),
    "beastmen": dict(module="beastmen_brayherds", faction="Beastmen Brayherds",
                     army="beastmen-brayherds", race="Beastman", legacy=True,
                     unit_races=[("centigor", "Centigor"), ("minotaur", "Minotaur"),
                                 ("giant", "Giant")]),
    "chaos_dwarfs": dict(module="chaos_dwarfs", faction="Chaos Dwarfs",
                         army="chaos-dwarfs", race="Chaos Dwarf", legacy=True,
                         unit_races=[("hobgoblin|sneaky gits", "Hobgoblin"),
                                     ("bull centaur", "Bull Centaur")]),
    "daemons": dict(module="daemons_of_chaos", faction="Daemons of Chaos",
                    army="daemons-of-chaos", race="Daemon", legacy=True),
    "dark_elves": dict(module="dark_elves", faction="Dark Elves",
                       army="dark-elves", race="Dark Elf", legacy=True),
    "dwarfs_anvil": dict(
        module=None, faction="Dwarfen Mountain Holds",
        army="dwarfen-mountain-holds", title="Dwarfen Mountain Holds",
        aliases=[], profile_aliases={}, race="Dwarf",
        only=["anvil-of-doom"],
        overrides={
            "Anvil of Doom": {
                # Split Profile (War Machine): in combat the model uses the
                # crew's Toughness and Wounds, and the crew does the fighting.
                "base_profile": {
                    "Movement": 3, "WeaponSkill": 6, "BallisticSkill": 4,
                    "Strength": 4, "Toughness": 5, "Initiative": 3,
                    "Wounds": 4, "Attacks": 5, "Leadership": 9,
                },
                "comment": ("Uses the Forgefather & Anvil Guard row: a war "
                            "machine fights with its crew's characteristics, "
                            "including T and W. The crew losing -1 Attack per "
                            "Wound lost is not modelled."),
            },
        },
    ),
}


def _int(value):
    value = str(value).strip()
    return int(value) if value.isdigit() else None


def base_rule_name(rule):
    """'Regeneration (5+)' -> 'Regeneration'; 'Fly (9) (Dragon Form only)' -> 'Fly'."""
    return re.sub(r"\s*\(.*$", "", rule).rstrip("*").strip()


_WEAPON_CACHE = {}


def classify(slug):
    """'melee', 'ranged' or None for a linked rule, with its profile table."""
    if slug in _WEAPON_CACHE:
        return _WEAPON_CACHE[slug]
    try:
        page = site.rule(slug)
    except site.PageNotFound:
        _WEAPON_CACHE[slug] = (None, None)
        return _WEAPON_CACHE[slug]
    tables = [t for t in page["tables"] if "range" in t]
    if not tables:
        result = (None, None)
    elif tables[0]["range"].strip().lower() == "combat":
        result = ("melee", tables[0])
    else:
        result = ("ranged", tables[0])
    _WEAPON_CACHE[slug] = result
    return result


def item_weapon_table(slug):
    """A magic item's melee profile, or None if it is not a melee weapon."""
    try:
        item = site.magic_item(slug)
    except site.PageNotFound:
        return None
    for table in item["tables"]:
        if str(table.get("range", "")).strip().lower() == "combat":
            return table
    return None


def weapon_name(table):
    """MeleeWeaponDict name for a weapon profile table."""
    name = re.sub(r"\s*\(?Profile\)?$", "", table["name"]).replace("\u2019", "'")
    return WEAPON_NAMES.get(name, name)


def profile_for(unit):
    """The statline row for the character itself, plus the other rows."""
    rows = unit["profiles"]
    main = next((r for r in rows if r["Name"] == unit["name"]), rows[0])
    return main, [r for r in rows if r is not main]


def statline(row):
    return " ".join(f"{k}{row[k]}" for k in ("M", "WS", "BS", "S", "T", "W", "I", "A", "Ld"))


def _numeric(row, key):
    return str(row.get(key, "")).strip().isdigit()


def unit_rows(unit):
    """(fighting row, champion row or None, body row or None, other rows).

    The fighting row is the first rank-and-file row with its own Weapon Skill
    and Attacks - the rider of a cavalry model, the crew of a chariot or war
    machine, the monster itself. The champion is the row the options let one
    model be upgraded to. The body is the row a crew or rider borrows
    Toughness and Wounds from (a chariot, a war machine).
    """
    rows = unit["profiles"]
    options = unit["options"].lower()
    champion = None
    for row in rows:
        label = re.sub(r"\s*\(.*\)$", "", row["Name"]).strip().lower()
        if "champion" in label or re.search(
            r"upgrade one model to an? " + re.escape(label) + r"\b", options
        ):
            champion = row
            break
    fighters = [r for r in rows if r is not champion and _numeric(r, "WS")]
    fighters.sort(key=lambda r: not _numeric(r, "A"))  # stable: prefer real Attacks
    main = fighters[0] if fighters else rows[0]
    body = None
    if not (_numeric(main, "T") and _numeric(main, "W")):
        body = next((r for r in rows if _numeric(r, "T") and _numeric(r, "W")), None)
    others = [r for r in rows if r is not main and r is not champion]
    return main, champion, body, others


def _unit_race(cfg, name):
    for pattern, race in cfg.get("unit_races", []):
        if re.search(pattern, name, re.IGNORECASE):
            return race
    return cfg.get("unit_race", cfg["race"])


def _stats(row, body=None):
    stats = {}
    for key, col in (("Movement", "M"), ("WeaponSkill", "WS"), ("BallisticSkill", "BS"),
                     ("Strength", "S"), ("Toughness", "T"), ("Initiative", "I"),
                     ("Wounds", "W"), ("Attacks", "A"), ("Leadership", "Ld")):
        value = _int(row[col])
        if value is None and body is not None and col in ("T", "W"):
            value = _int(body[col])
        stats[key] = value
    return stats


def build_character(slug, cfg, review):
    return build_entry(slug, cfg, review, is_unit=False)


def build_unit(slug, cfg, review):
    return build_entry(slug, cfg, review, is_unit=True)


def build_entry(slug, cfg, review, is_unit):
    from weapons import find_weapon_key

    unit = site.unit(slug)
    raw = unit["raw"]
    name = unit["name"]
    champion = body = None
    if is_unit:
        main, champion, body, others = unit_rows(unit)
        named = False
        size = str(raw.get("unitSize") or "").strip()
        per = "model" if size != "1" else "unit"
        comments = [f"https://tow.whfb.app/unit/{slug} - {unit['cost']} pts per {per}"
                    + (f", unit size {size}" if size and size != "1" else "")]
        fighter = main["Name"]
        if not _numeric(main, "A") and str(main["A"]).strip() not in ("-", ""):
            comments.append(f"Its Attacks are {main['A']}, a dice value the engine cannot use yet; "
                            "recorded as None, so it makes no attacks.")
        if not size:
            size = "not given"
            comments.append("The site gives no unit size.")
        comments.append(f"Fights with the {fighter} row"
                        + (f", using the {body['Name']} row's Toughness and Wounds" if body else "")
                        + ".")
    else:
        main, others = profile_for(unit)
        # The site files a named character under either field.
        named = "Named Character" in unit["unit_category"] + unit["troop_type"]
        comments = [f"https://tow.whfb.app/unit/{slug} - {unit['cost']} pts"]
    for other in others:
        comments.append(f"Also has a profile for {other['Name']} ({statline(other)}); not simulated.")

    eq_text = site.text(raw.get("equipment")).strip()
    eq_lower = eq_text.lower()
    # Only the fighting model's own equipment line counts, not its mount's.
    own_line = eq_text
    lines = [l.lstrip("- ").strip() for l in eq_text.splitlines() if l.strip()]
    if len(lines) > 1 and ":" in lines[0]:
        own_line = lines[0]
        if is_unit:
            wanted = mount_names._fold(re.sub(r"\s*\(.*\)$", "", main["Name"]))
            for line in lines:
                label = mount_names._fold(line.split(":", 1)[0])
                if label and (label in wanted or wanted in label
                              or label.rstrip("s") in wanted or wanted.rstrip("s") in label):
                    own_line = line
                    break
    own_lower = own_line.lower()

    weapons, ranged, armour_options = [], [], []
    default_weapon = None
    armour = None
    shield = "shield" in own_lower and "shield of" not in own_lower
    shield_option = shield
    items = []
    magic_weapons = []

    for shown, link_slug, kind in unit["equipment_links"]:
        if shown.lower() not in own_lower and (kind != "magicItem" or shown.lower() not in eq_lower):
            continue
        if kind == "magicItem":
            item = site.magic_item(link_slug)["name"].rstrip("*")
            if item not in items:
                items.append(item)
            table = item_weapon_table(link_slug)
            if table is not None and item not in weapons:
                weapons.append(item)
                magic_weapons.append(item)
            continue
        low = shown.lower()
        if low in ARMOUR:
            if shown.lower() in own_lower:
                armour = ARMOUR[low]
            continue
        category, table = classify(link_slug)
        if category == "melee":
            wname = weapon_name(table)
            if wname not in weapons:
                weapons.append(wname)
        elif category == "ranged":
            ranged.append(shown)

    equipment_weapons = list(weapons)
    counts_as = re.search(r"counts as (?:an? )?(light|heavy|full plate) armour", own_lower)
    if counts_as and armour is None:
        armour = ARMOUR[counts_as.group(1) + " armour"]

    # A named character's first magic weapon is their default weapon.
    for shown, link_slug, kind in unit["option_links"]:
        low = shown.lower()
        if kind == "armyListEntry":
            continue
        if low in ARMOUR:
            armour_options.append(ARMOUR[low])
            continue
        if low in ("shield", "shields"):
            shield_option = True
            continue
        if kind != "rule":
            continue
        category, table = classify(link_slug)
        if category == "melee":
            wname = weapon_name(table)
            if wname not in weapons:
                weapons.append(wname)
        elif category == "ranged":
            if shown not in ranged:
                ranged.append(shown)

    from weapons import get_weapon_special_rules

    # Tails, maws and the like make one extra attack; they are never the
    # weapon a model fights with.
    equipped = [w for w in equipment_weapons if w != "Hand Weapon"
                and "Secondary Attack" not in get_weapon_special_rules(w)]
    if magic_weapons:
        default_weapon = magic_weapons[0]
    elif is_unit and equipped:
        # A unit carrying a hand weapon and a special weapon fights with the
        # special one by default (White Lions with their great blades).
        default_weapon = equipped[0]
    elif "Hand Weapon" in weapons:
        default_weapon = "Hand Weapon"
    elif weapons:
        default_weapon = weapons[0]
    if "Hand Weapon" not in weapons and default_weapon is None:
        weapons.insert(0, "Hand Weapon")
        default_weapon = "Hand Weapon"
        review.append(f"{name}: no melee weapon on the page; defaulted to a hand weapon")
    if "Hand Weapon" in weapons:
        weapons.remove("Hand Weapon")
        weapons.insert(0, "Hand Weapon")

    for w in weapons:
        if find_weapon_key(w) is None:
            review.append(f"{name}: melee weapon {w!r} has no MeleeWeaponDict entry")

    from special_rules import RequiresTwoHands

    if shield and default_weapon and RequiresTwoHands in get_weapon_special_rules(default_weapon):
        # It carries a shield, but cannot use it with this weapon.
        shield = False
        comments.append(f"Carries a shield, which it cannot use with its {default_weapon}; "
                        "pass Shield=True with a one-handed weapon.")

    printed = str(raw.get("armourValue") or "").strip()
    if printed:
        # The site prints this model's armour value outright (a chariot, a
        # monster, Settra); it already includes any barding, so the crew's own
        # armour and shields do not add to it.
        armour = ARMOUR_VALUES[printed]
        armour_options = []
        shield = shield_option = False
        comments.append(f"Armour value {printed} as printed on the site.")

    armour_list = []
    for a in [armour] + armour_options:
        if a and a not in armour_list:
            armour_list.append(a)

    mounts = []
    for shown, link_slug, kind in unit["option_links"]:
        if kind != "armyListEntry" or is_unit:
            continue
        target = mount_names.canonical(site.unit(link_slug)["name"])
        shown_words = set(mount_names._fold(re.sub(r"\s*\(.*$", "", shown)).split())
        if not shown_words <= set(mount_names._fold(target).split()):
            # A site link whose text and target disagree ("Cold One" -> Terradon).
            fixed = mount_names.find_in_army(cfg["army"], shown)
            review.append(f"{name}: site links mount {shown!r} to {link_slug!r}; using {fixed!r}")
            if fixed is None:
                continue
            target = mount_names.canonical(site.unit(fixed)["name"])
        mounts.append(target)

    optional = [shown for shown, _s, kind in unit["option_links"]
                if kind == "rule" and classify(_s)[0] is None
                and shown.lower() not in ARMOUR and shown.lower() not in ("shield", "shields")]

    if ranged:
        comments.append(
            "Shooting is not simulated, so these are left out of the options: "
            + ", ".join(sorted(set(ranged))) + "."
        )

    rules = []
    for rule in unit["special_rules"]:
        rules.append(rule)
        for extra in RULE_COMPANIONS.get(rule, []):
            if extra not in rules:
                rules.append(extra)

    troop = [t for t in unit["troop_type"] if t not in TROOP_TYPES]
    if len(troop) > 1:
        comments.append(f"Troop type by form: {', '.join(troop)}; the first is used.")

    if is_unit:
        race = _unit_race(cfg, name)
    else:
        race = cfg.get("races", {}).get(name, cfg["race"])

    base = dict(_stats(main, body))
    base.update({
        "Race": race,
        "Armor": armour,
        "Weapon": default_weapon,
        "Shield": shield,
        "SpecialRules": rules,
        "TroopType": troop[0].replace(" ", "") if troop else None,
        "UnitCategory": "Unit" if is_unit else ("NamedCharacter" if named else "Character"),
    })
    if unit["wizard_level"] is not None and unit["lores"]:
        base["WizardLevel"] = int(unit["wizard_level"])
        base["Lores"] = [re.sub(r"\s+Lore$", "", l) for l in unit["lores"]]
    if optional:
        base["OptionalRules"] = optional

    override = cfg.get("overrides", {}).get(name, {})
    base.update(override.get("base_profile", {}))
    if override.get("comment"):
        comments.append(override["comment"])

    points = unit["cost"]
    note = str(raw.get("costOverride") or "").strip()
    if points is None and note:
        match = re.search(r"\d+", note)
        points = int(match.group(0)) if match else None
    entry = {
        "comments": comments,
        "points": points,
    }
    if note:
        entry["points_note"] = note
    if is_unit:
        entry["points_per"] = per
        entry["unit_size"] = size or None
        if champion is not None:
            entry["champion"] = dict({"Name": champion["Name"]}, **_stats(champion, body))
        entry["other_profiles"] = [dict({"Name": r["Name"]}, **_stats(r)) for r in others]
    entry.update({
        "base_profile": base,
        "equipment_options": {
            "weapons": weapons,
            "armor": armour_list,
            "shield": shield_option,
            "items": items,
        },
        "mount_options": {"mounts": mounts},
        "rule_links": unit["rule_links"],
    })
    return name, entry


def _py(value):
    if isinstance(value, str):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    if isinstance(value, list):
        return "[" + ", ".join(_py(v) for v in value) + "]"
    return repr(value)


def render_character(name, entry):
    out = [f"    {_py(name)}: {{"]
    for c in entry["comments"]:
        for line in textwrap.wrap(c, 76):
            out.append(f"        # {line}")
    out.append(f'        "points": {entry["points"]},')
    for key in ("points_note", "points_per", "unit_size"):
        if key in entry:
            out.append(f'        "{key}": {_py(entry[key])},')
    if entry.get("champion"):
        out.append(f'        "champion": {entry["champion"]!r},')
    if "other_profiles" in entry:
        if entry["other_profiles"]:
            out.append('        "other_profiles": [')
            for row in entry["other_profiles"]:
                out.append(f"            {row!r},")
            out.append("        ],")
        else:
            out.append('        "other_profiles": [],')
    out.append('        "base_profile": {')
    for k, v in entry["base_profile"].items():
        out.append(f'            "{k}": {_py(v)},')
    out.append("        },")
    out.append('        "equipment_options": {')
    for k, v in entry["equipment_options"].items():
        out.append(f'            "{k}": {_py(v)},')
    out.append("        },")
    out.append('        "mount_options": {')
    out.append(f'            "mounts": {_py(entry["mount_options"]["mounts"])}')
    out.append("        }")
    out.append("    },")
    return "\n".join(out)


def faction_rules(characters):
    """FACTION_RULES from every rule on the given profiles."""
    seen = {}
    for entry in characters.values():
        for shown, slug, _kind in entry["rule_links"]:
            base = base_rule_name(shown)
            if base not in seen and slug:
                seen[base] = slug
    rules = {}
    for base in sorted(seen):
        try:
            text = site.rule(seen[base])["text"]
        except site.PageNotFound:
            text = "Not transcribed - the site has no page for this rule."
        text = " ".join(text.split())
        if len(text) > 700:
            text = text[:700].rsplit(" ", 1)[0] + " [...]"
        rules[base] = {
            "status": ENGINE_RULES.get(base),
            "text": text,
            "url": f"https://tow.whfb.app/{site.rule_path(seen[base])}",
        }
    return rules


def render_rules(rules):
    out = []
    for name, entry in rules.items():
        out.append(f"    {_py(name)}: {{")
        out.append(f'        "status": {_py(entry["status"])},')
        out.append(f'        "url": {_py(entry["url"])},')
        out.append('        "text": (')
        lines = textwrap.wrap(entry["text"], 70)
        for i, line in enumerate(lines):
            out.append(f"            {_py(line + (' ' if i < len(lines) - 1 else ''))}")
        out.append("        ),")
        out.append("    },")
    return "\n".join(out)


def legacy_characters(cfg):
    import importlib

    return importlib.import_module(f"factions.{cfg['module']}").CHARACTERS


def build(key):
    """(cfg, characters, units, rules, review) for one faction."""
    cfg = FACTIONS[key]
    review = []
    characters, units = {}, {}
    for section, slug, _name in site.army_units(cfg["army"]):
        if cfg.get("only"):
            if slug in cfg["only"]:
                name, entry = build_character(slug, cfg, review)
                characters[name] = entry
            continue
        if section == "Mount":
            continue  # mounts.py
        if "Character" in section:
            if cfg.get("legacy"):
                continue
            name, entry = build_character(slug, cfg, review)
            characters[name] = entry
        else:
            page = site.unit(slug)
            if not page["profiles"]:
                review.append(f"{_name}: the site page has no statline; skipped")
                continue
            body_text = site.text(page["raw"].get("bodyBefore"))
            if "only be included in your army as a character's mount" in body_text:
                continue  # mounts.py
            if not any(_numeric(r, "WS") for r in page["profiles"]):
                review.append(f"{_name}: no row that fights; skipped")
                continue
            name, entry = build_unit(slug, cfg, review)
            base = entry["base_profile"]
            if not (base["Toughness"] and base["Wounds"]):
                review.append(f"{name}: no Toughness/Wounds of its own; skipped")
                continue
            if cfg.get("legacy") and name in legacy_characters(cfg):
                continue  # already hand-transcribed as a character
            units[name] = entry
    for name in set(characters) & set(units):
        review.append(f"{name}: both a character and a unit")
    rules = faction_rules(dict(characters, **units))
    return cfg, characters, units, rules, review


def render_units(units):
    body = "\n".join(render_character(n, e) for n, e in units.items())
    return f"""# Regular (non-character) units. `points` is per model unless `points_per`
# says "unit"; `unit_size` is the minimum ("10+") or fixed size. Each unit
# fights with the row named in its comment; its champion's statline is under
# `champion` and any mount, crew or beast rows under `other_profiles`.
UNITS = {{
{body}
}}"""


def render_module(cfg, characters, units, rules):
    aliases = "\n".join(f"    {_py(a)}," for a in cfg["aliases"])
    profile_aliases = "\n".join(
        f"    {_py(k)}: {_py(v)}," for k, v in cfg["profile_aliases"].items()
    )
    body = "\n".join(render_character(n, e) for n, e in characters.items())
    return f'''"""{cfg["title"]}.

Profiles from https://tow.whfb.app/army/{cfg["army"]}, read from the page data
by tools/transcribe_faction.py and reviewed by hand.
"""

from __future__ import annotations

# The key this faction is filed under in FactionProfiles.
FACTION = {_py(cfg["faction"])}

# Other names that should resolve to this faction.
ALIASES = [
{aliases}
]

# Shorthand names for individual profiles.
PROFILE_ALIASES = {{
{profile_aliases}
}}

CHARACTERS = {{
{body}
}}

{render_units(units)}


# Special rules carried by this faction's characters and units. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {{
{render_rules(rules)}
}}

PROFILES = dict(CHARACTERS, **UNITS)
'''


_UNITS_BLOCK = re.compile(
    r"(?:# Regular \(non-character\) units[^\n]*\n(?:#[^\n]*\n)*)?"
    r"UNITS = \{(?:\}|\n.*?\n\})\n", re.S)


def update_legacy_module(path, units, rules):
    """Replace UNITS in a hand-written module, and add missing FACTION_RULES."""
    source = open(path, encoding="utf-8").read()
    match = _UNITS_BLOCK.search(source)
    if match is None:
        match = re.search(r"# Regular \(non-character\) units go here\.\nUNITS = \{\}\n", source)
    if match is None:
        raise ValueError(f"{path}: no UNITS block found")
    source = source[:match.start()] + render_units(units) + "\n" + source[match.end():]

    start = source.index("FACTION_RULES = {")
    end = source.index("\n}\n", start)
    existing = source[start:end]
    known = {base_rule_name(k) for k in re.findall(r"^    ['\"](.+?)['\"]: \{", existing, re.M)}
    missing = {k: v for k, v in rules.items() if k not in known}
    if missing:
        source = source[:end] + "\n" + render_rules(missing) + source[end:]

    # Entries this tool wrote (they carry a "url") take their status from
    # ENGINE_RULES, so a rule implemented later is not left marked as missing.
    def refresh(match):
        return f'{match.group(1)}"status": {_py(ENGINE_RULES.get(match.group(2)))},\n{match.group(3)}'
    source = re.sub(
        r'(\n    "([^"\n]+)": \{\n        )"status": [^\n]*,\n(        "url": )',
        refresh, source)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(source)
    return sorted(missing)


def main(argv):
    key = argv[1]
    cfg, characters, units, rules, review = build(key)
    path = os.path.join(ROOT, "factions", (cfg["module"] or "") + ".py")
    if cfg.get("legacy"):
        if "-w" in argv:
            added = update_legacy_module(path, units, rules)
            print(f"updated {path}: {len(units)} units, rules added: {added}")
        else:
            print(render_units(units))
    else:
        source = render_module(cfg, characters, units, rules)
        if "-w" in argv and cfg["module"]:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(source)
            print(f"wrote {path}")
        elif "-w" not in argv:
            print(source)
    for line in review:
        print("REVIEW:", line, file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv)
