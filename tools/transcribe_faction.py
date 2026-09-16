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
    ),
    "ogres": dict(
        module="ogre_kingdoms", faction="Ogre Kingdoms", army="ogre-kingdoms",
        title="Ogre Kingdoms",
        aliases=["Ogres", "Ogre Kingdoms", "OK"],
        profile_aliases={"Ogre Tyrant": "Tyrant", "Ogre Bruiser": "Bruiser"},
        race="Ogre",
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
    ),
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


def build_character(slug, cfg, review):
    from weapons import find_weapon_key

    unit = site.unit(slug)
    raw = unit["raw"]
    name = unit["name"]
    main, others = profile_for(unit)
    # The site files a named character under either field.
    named = "Named Character" in unit["unit_category"] + unit["troop_type"]
    comments = [f"https://tow.whfb.app/unit/{slug} - {unit['cost']} pts"]
    for other in others:
        comments.append(f"Also has a profile for {other['Name']} ({statline(other)}); not simulated.")

    eq_text = site.text(raw.get("equipment")).strip()
    eq_lower = eq_text.lower()
    # Only the character's own equipment line counts, not its mount's.
    own_line = eq_text
    lines = [l for l in eq_text.splitlines() if l.strip()]
    if len(lines) > 1 and ":" in lines[0]:
        own_line = lines[0]
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
        if low == "shield":
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

    if magic_weapons:
        default_weapon = magic_weapons[0]
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

    armour_list = []
    for a in [armour] + armour_options:
        if a and a not in armour_list:
            armour_list.append(a)

    mounts = []
    for shown, link_slug, kind in unit["option_links"]:
        if kind != "armyListEntry":
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
                and shown.lower() not in ARMOUR and shown.lower() != "shield"]

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

    race = cfg.get("races", {}).get(name, cfg["race"])

    base = {
        "Movement": _int(main["M"]),
        "WeaponSkill": _int(main["WS"]),
        "BallisticSkill": _int(main["BS"]),
        "Strength": _int(main["S"]),
        "Toughness": _int(main["T"]),
        "Initiative": _int(main["I"]),
        "Wounds": _int(main["W"]),
        "Attacks": _int(main["A"]),
        "Leadership": _int(main["Ld"]),
        "Race": race,
        "Armor": armour,
        "Weapon": default_weapon,
        "Shield": shield,
        "SpecialRules": rules,
        "TroopType": troop[0].replace(" ", "") if troop else None,
        "UnitCategory": "NamedCharacter" if named else "Character",
    }
    if unit["wizard_level"] is not None and unit["lores"]:
        base["WizardLevel"] = int(unit["wizard_level"])
        base["Lores"] = [re.sub(r"\s+Lore$", "", l) for l in unit["lores"]]
    if optional:
        base["OptionalRules"] = optional

    override = cfg.get("overrides", {}).get(name, {})
    base.update(override.get("base_profile", {}))
    if override.get("comment"):
        comments.append(override["comment"])

    return name, {
        "comments": comments,
        "points": unit["cost"],
        "base_profile": base,
        "equipment_options": {
            "weapons": weapons,
            "armor": armour_list,
            "shield": shield_option,
            "items": items,
        },
        "mount_options": {"mounts": mounts},
        "rule_links": unit["rule_links"],
    }


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
    """FACTION_RULES from every rule on the faction's characters."""
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


def build(key):
    cfg = FACTIONS[key]
    review = []
    characters = {}
    for section, slug, _name in site.army_units(cfg["army"]):
        if "Character" not in section:
            continue
        if cfg.get("only") and slug not in cfg["only"]:
            continue
        name, entry = build_character(slug, cfg, review)
        characters[name] = entry
    return cfg, characters, faction_rules(characters), review


def render_module(cfg, characters, rules):
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

# Regular (non-character) units go here.
UNITS = {{}}


# Special rules carried by this faction's characters. `status` is how far the
# engine goes with each: "implemented", "partial", or None for recorded only.
# Texts longer than a paragraph are cut, marked "[...]"; `url` has the rest.
FACTION_RULES = {{
{render_rules(rules)}
}}

PROFILES = dict(CHARACTERS, **UNITS)
'''


def main(argv):
    key = argv[1]
    cfg, characters, rules, review = build(key)
    source = render_module(cfg, characters, rules)
    if "-w" in argv and cfg["module"]:
        path = os.path.join(ROOT, "factions", cfg["module"] + ".py")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(source)
        print(f"wrote {path}")
    elif "-w" not in argv:
        print(source)
    for line in review:
        print("REVIEW:", line, file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv)
