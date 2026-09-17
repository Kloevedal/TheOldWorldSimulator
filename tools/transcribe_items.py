"""Generate magic_items_data.py from every magic item on https://tow.whfb.app.

    python3 tools/transcribe_items.py          # report what was extracted
    python3 tools/transcribe_items.py -w       # write magic_items_data.py

Every item page (magic weapons, armour, talismans, enchanted and arcane items,
standards, and the "Ability" entries that hold Elven Honours, Knightly
Virtues, Wood Elf Kindreds, Daemonic Gifts, runes and the like) becomes one
entry with its cost, armies, type and rules text.

Effects are read sentence by sentence, conservatively. Only wording with a
single unconditional meaning is turned into something the engine reads:

    "is a suit of heavy armour"                      armour
    "is a shield"                                    shield
    "improves their armour value by 1"               Improve Armour (1)
    "a 5+ Ward save against any wounds suffered"     Ward5
      "... caused by a non-magical enemy attack"     Ward5 (non-magical)
      "... caused by an attack that has Flaming ..." Ward5 (Flaming)
    "the Regeneration (5+) special rule"             Regeneration (5+)
    "improves their Toughness characteristic by 1"   stat_mods {"Toughness": 1}
    "gains the Killing Blow special rule"            Killing Blow
    "is immune to the Killing Blow special rule"     Immune to Killing Blow

A sentence that is conditional (a charge turn, once per turn, a mount, a unit,
a particular enemy, single use) is never applied. Each entry's `status` says
how much of it reached the engine:

    "applied"        every effect sentence was converted
    "partial"        some were, the rest are in `not_modelled`
    "not modelled"   it would matter in a duel but nothing was converted
    "no duel effect" standards, arcane items, spells, movement, army rules

Hand-reviewed entries in magic_items.py take precedence over these.
"""

from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT, os.path.join(ROOT, "tests")]

import rule_catalogue as rc  # noqa: E402
import tow_site as site  # noqa: E402
import transcribe_weapons as tw  # noqa: E402

OUT = os.path.join(ROOT, "magic_items_data.py")

STAT_NAMES = {
    "weapon skill": "WeaponSkill", "ballistic skill": "BallisticSkill",
    "strength": "Strength", "toughness": "Toughness", "wounds": "Wounds",
    "initiative": "Initiative", "attacks": "Attacks", "leadership": "Leadership",
    "movement": "Movement",
}

ARMOUR = {"light": "Light Armor", "heavy": "Heavy Armor", "full plate": "Full Plate Armor"}

# Books that are not armies.
BOOKS = re.compile(r"^(Rulebook|Forces of Fantasy|Ravening Hordes|Arcane Journal|Battle March"
                   r"|Regiment of Renown)", re.I)

# Words that make a sentence's effect conditional, so it is never applied.
CONDITIONAL = re.compile(
    r"\b(turn in which|once per|single use|until the end|during the (?:command|shooting|movement)"
    r"|mount|unit (?:they|it) (?:has )?join|any unit|if (?:the|this|they|it)|when |whilst"
    r"|against (?:enemy|any enemy|models|a model|daemonic|undead|monster|chariot|cavalry)"
    r"|roll a d6|bound spell|may choose|instead of|(?<!furious )(?<!counter )charge|flee|shooting|missile|spell"
    r"|friendly|army of infamy|in base contact|re-roll|reroll|cannot be"
    r"|impact hits (?:caused|have)|this impact hit|for every wound|enemy (?:models?|units?) (?:that|engaged|must|suffer|cannot)"
    r"|directs? (?:its|their) attacks|unless)", re.I)

# A sentence that only describes hits made some other way ("These hits have
# the Killing Blow special rule") belongs to the sentence before it.
DEPENDENT = re.compile(r"^(these|this hit|those|such|each of these)\b", re.I)

# Sentences that only explain how an immunity the engine models works, or
# introduce a bulleted list.
EXPLANATORY = re.compile(
    r"(^if .*(?:struck (?:by )?a killing blow|unsaved wound from an attack with)"
    r"|^if the wound is unsaved|lose[s]? a single wound\.?$|:\.?$"
    r"|^if the (?:bearer|wearer) is wounded by an attack with this special rule)", re.I)

# A list heading that limits the bullets under it to some models only.
LIMITED_HEADING = re.compile(r"(grand master|chapter master|inner circle|or unit of|if |whilst).*:\.?$", re.I)

# Items for war machines only.
WAR_MACHINE = re.compile(r"\b(war machine|bolt thrower|cannon|organ gun|grudge thrower|stone thrower)s?\b", re.I)

# Sentences that plainly concern nothing a duel can use.
NO_DUEL = re.compile(
    r"\b(bound spell|casting|dispel|wizard|spell|lore of|power dice|move through cover|fly \(|"
    r"swiftstride|vanguard|scouts|ambush|break test|leadership test|panic|rally|combat result|"
    r"command range|deploy|first turn|unit strength|march|pursu|flee|shooting|missile|range|"
    r"magic resistance|immune to psychology|stupidity|stubborn|unbreakable|fear|terror|"
    r"impetuous|may be worn|may be purchased|without penalty|may only be taken|may not take|"
    r"may take|must be mounted|must be equipped|may be equipped|infamous origin|elven honour|"
    r"join a unit|issue and accept challenges|army.s general|cannot join|0-1 per)",
    re.I)

# Rule names the site writes differently from the engine.
GRANT_SPELLING = {"Dragon Armour": "Dragon Armour (6+ Ward)"}


def grant(rule):
    """(engine rule or None, is it something a duel would miss)."""
    rule = GRANT_SPELLING.get(rule, rule)
    if rc.engine_reads(rule) and rule not in rc.WEAPON_ONLY_RULES:
        return rule, False
    return None, rule not in rc.INERT


def clean_name(name):
    return name.rstrip("*").strip().replace("’", "'")


def sentences(text):
    body = re.sub(r"\*\s*(Extremely Common|Rule of Duplication)\b.*", "", text, flags=re.S)
    body = re.sub(r"\s+-\s+", ". ", " ".join(body.split()))
    parts = re.split(r"(?<=[.!?:])\s+", body)
    return [p.strip() for p in parts if p.strip()]


def restriction(first):
    """'Models whose troop type is infantry only.' -> kept as a note."""
    if re.search(r"\bonly\.?$", first) and len(first) < 160:
        return first.rstrip(".")
    return None


def ward_rules(sentence):
    """Every Ward save a sentence grants, or None if one is too specific."""
    found = []
    clauses = re.split(r"(?=\d\+ Ward save)", sentence)
    for clause in clauses:
        m = re.match(r"(\d)\+ Ward save against (.*)", clause, re.I)
        if not m:
            continue
        target, rest = m.group(1), m.group(2).lower()
        rest = re.split(r"\band (?:a|makes|is|gains)\b", rest)[0]
        if re.match(r"any wounds? suffered\W*$", rest) or (
                rest.startswith("any wound") and "caused by" not in rest
                and "during" not in rest and "phase" not in rest):
            found.append(f"Ward{target}")
        elif "caused by" in rest and "non-magical" in rest and "strength" not in rest:
            found.append(f"Ward{target} (non-magical)")
        elif "caused by" in rest and "magical" in rest and "strength" not in rest:
            found.append(f"Ward{target} (magical)")
        elif "caused by" in rest and "flaming attacks" in rest:
            found.append(f"Ward{target} (Flaming)")
        else:
            return None
    return found


# Whole-sentence wording with a fixed meaning the engine can model:
# (pattern, rules, stat_mods, armour).
SPECIAL_EFFECTS = [
    (r"(?:any )?(?:enemy )?models? that directs? (?:its|their) attacks against .* suffers? a -(\d) modifier to (?:its|their) rolls to hit",
     lambda m: (["Enemy To Hit (-%s)" % m.group(1)], {}, None)),
    (r"^whilst (?:this model is )?engaged in a challenge, its opponent .* suffers a -(\d) modifier to its rolls to hit",
     lambda m: (["Enemy To Hit (-%s)" % m.group(1)], {}, None)),
    (r"^however, enemy models that target this model during the combat phase also have a \+(\d) modifier to their rolls to hit",
     lambda m: (["Enemy To Hit (+%s)" % m.group(1)], {}, None)),
    (r"during the combat phase, has a \+(\d) modifier to (?:their|its) rolls to hit",
     lambda m: (["To Hit (+%s)" % m.group(1)], {}, None)),
    (r"(?:this (?:model|character)|a model with this [a-z ]+?) may re-roll any failed rolls to hit\.?$",
     lambda m: (["Reroll Failed Hits"], {}, None)),
    (r"(?:this (?:model|character)|a model with this [a-z ]+?) may re-roll any failed rolls to wound\.?$",
     lambda m: (["Reroll Failed Wounds"], {}, None)),
    (r"gains the armour bane \((\d)\) special rule and may re-roll any failed rolls to hit\.?$",
     lambda m: (["Armour Bane (%s)" % m.group(1), "Reroll Failed Hits"], {}, None)),
    (r"for each unsaved wound the wearer causes, they recover a single lost wound",
     lambda m: (["Wound Stealing"], {}, None)),
    (r"always has a (\d)\+ ward save, even if this model's army did not pray",
     lambda m: (["Ward%s" % m.group(1)], {}, None)),
    (r"(\d)\+ ward save against any wounds suffered that were caused by an attack with a strength of (\d+) or lower, and a (\d)\+ ward save against any wounds suffered that were caused by an attack with a strength of (\d+) or higher",
     lambda m: (["Ward%s (Strength %s-)" % (m.group(1), m.group(2)),
                 "Ward%s (Strength %s+)" % (m.group(3), m.group(4))], {}, None)),
    (r"^(?:this impact hit has|in addition, any impact hits caused by this model have) an armour piercing characteristic of -(\d)",
     lambda m: (["Impact Hits Armour Piercing (%s)" % m.group(1)], {}, None)),
    (r"cannot be wounded by a roll to wound of 2",
     lambda m: (["Cannot Be Wounded On 2"], {}, None)),
    (r"^the bearer is immune to the multiple wounds \(x\) special rule",
     lambda m: (["Immune to Multiple Wounds"], {}, None)),
    (r"^in addition, the wearer is immune to the multiple wounds \(x\) special rule",
     lambda m: (["Immune to Multiple Wounds"], {}, None)),
    (r"^in addition, enemy models must re-?roll successful rolls to wound made against the wearer",
     lambda m: (["Enemy Rerolls Successful Wounds"], {}, None)),
    (r"^in addition, during the combat phase, enemy models must re-?roll successful rolls to hit made against the wearer",
     lambda m: (["Enemy Rerolls Successful Hits"], {}, None)),
    (r"^no armour save is permitted against wounds caused by a weapon inscribed with",
     lambda m: (["No Armour Saves"], {}, None)),
    (r"^when making a roll to wound with a weapon inscribed with .*, a roll of (\d)\+ is always a success",
     lambda m: (["Wounds On (%s+)" % m.group(1)], {}, None)),
    (r"has \+(\d) wounds? on (?:their|its|his|her) profile",
     lambda m: ([], {"Wounds": int(m.group(1))}, None)),
    (r"^a character who adopts the aspect of the bear increases their strength and toughness characteristics by 1",
     lambda m: ([], {"Strength": 1, "Toughness": 1}, None)),
    (r"gives (?:its|their) wearer an armour value of (\d)\+ which cannot be improved in any way",
     lambda m: (["Armour Cannot Be Improved"], {}, "Armour Value %s+" % m.group(1))),
    (r"gives its wearer an armour value of (\d)\+, which cannot be improved in any way",
     lambda m: (["Armour Cannot Be Modified"], {}, {"5": "Heavy Armor"}.get(m.group(1)))),
    (r"has an armour value of 2\+, which cannot be improved in any way",
     lambda m: (["Armour Cannot Be Modified"], {}, "Armour Value 2+")),
    (r"^however, nor can this armour value be reduced in any way either",
     lambda m: ([], {}, None)),
    (r"^(?:the bearer of (?:the|a) .+?|a model with .+?|this (?:character|model)) (?:has|gains) the poisoned attacks special rule",
     lambda m: (["Poisoned Attacks"], {}, None)),
]


def special_effect(low):
    for pattern, make in SPECIAL_EFFECTS:
        m = re.search(pattern, low)
        if m:
            return make(m)
    return None


def effects(name, kind, text):
    """(armour, shield, rules, stat_mods, not_modelled, restriction, status)."""
    armour = None
    shield = False
    rules, mods, skipped = [], {}, []
    parts = sentences(text)
    note = restriction(parts[0]) if parts else None
    if note:
        parts = parts[1:]

    if (kind in ("Magic Standard", "Arcane Item") or "Casting Value" in text
            or WAR_MACHINE.search(note or "") or WAR_MACHINE.search(parts[0] if parts else "")):
        return None, False, [], {}, [], note, "no duel effect"
    if re.search(r"\bsingle use\b", text, re.I):
        return None, False, [], {}, parts, note, "not modelled"

    previous_skipped = False
    limited = False
    for sentence in parts:
        if LIMITED_HEADING.search(sentence):
            limited = True
            continue
        if limited:
            if not NO_DUEL.search(sentence):
                skipped.append(sentence)
            continue
        # "(but not their mount)" only says the mount is unaffected; the
        # engine never gives a mount the rider's rules, so it is safe to drop.
        sentence = re.sub(r"\s*\(but not (?:their|its|his|her) mount[^)]*\)", "", sentence)
        # A duel is fought as a challenge, so "during a challenge" always holds.
        sentence = re.sub(r"(?i)^(?:during|whilst (?:engaged )?in) a challenge, ", "", sentence)
        sentence = re.sub(r"(?i),? (?:during|whilst (?:engaged )?in|made during) a challenge\b", "", sentence)
        low = sentence.lower()
        converted = False
        fixed = special_effect(low)
        if fixed:
            new_rules, new_mods, new_armour = fixed
            rules.extend(new_rules)
            for key, value in new_mods.items():
                mods[key] = mods.get(key, 0) + value
            armour = new_armour or armour
            previous_skipped = False
            # The rest of the sentence may grant rules too ("gains the Frenzy
            # special rule and ... +1 To Hit"); anything else in it is covered.
            g = re.search(r"(?:gains?|has|have) the (.+?) special rules?", sentence, re.I)
            for name in re.split(r",\s*|\s+and\s+", g.group(1)) if g else []:
                rule, _missed = grant(name.strip())
                if rule:
                    rules.append(rule)
            continue
        m = re.search(r"is a suit of (light|heavy|full plate) armour", low)
        if m:
            armour = ARMOUR[m.group(1)]
            converted = True
        if re.search(r"\bis a shield\b", low):
            shield = True
            converted = True
        if converted:
            # The armour clause may carry an "only by X" restriction; an
            # "In addition" effect comes in its own sentence.
            previous_skipped = False
            continue
        if EXPLANATORY.search(sentence):
            continue
        if CONDITIONAL.search(sentence) or (previous_skipped and DEPENDENT.search(sentence)):
            if not NO_DUEL.search(sentence):
                skipped.append(sentence)
            previous_skipped = True
            continue
        previous_skipped = False
        m = re.search(r"improves? (?:their|its|his|her) armour value by (\d)", low)
        if m:
            rules.append(f"Improve Armour ({m.group(1)})")
            converted = True
        bare = re.search(r"\b(?:has|grants? \w+|gives? (?:its|their) \w+) an? (\d)\+ ward save(?:\.?$|,| and)", low)
        if bare:
            rules.append(f"Ward{bare.group(1)}")
            converted = True
        wards = [] if bare else ward_rules(sentence)
        if wards is None:
            skipped.append(sentence)
            continue
        if wards:
            rules.extend(wards)
            converted = True
        for m in re.finditer(
            r"(?:(?:improves?|increases?) (?:their|its|his|her) ([a-z ]+?) characteristics? by (\d)"
            r"|a ([+-])(\d) modifier to (?:their|its|his|her) ([a-z ,]+?) characteristics?)", low):
            names = m.group(1) or m.group(5) or ""
            value = int(m.group(2) or m.group(4))
            if m.group(3) == "-":
                value = -value
            for stat in re.split(r",\s*|\s+and\s+", names):
                stat = stat.strip()
                if stat in STAT_NAMES:
                    key = STAT_NAMES[stat]
                    mods[key] = mods.get(key, 0) + value
                    converted = True
        if "immune to the killing blow" in low:
            rules.append("Immune to Killing Blow")
            converted = True
            if "multiple wounds" in low:
                skipped.append("Immune to Multiple Wounds (X): not modelled.")
        g = re.search(r"(?:gains?|has|have|gives? (?:its|their) (?:wearer|bearer)) the (.+?) special rules?",
                      sentence, re.I)
        if g and "caused by" not in low and "attack that has" not in low:
            for name in re.split(r",\s*|\s+and\s+", g.group(1)):
                rule, missed = grant(name.strip())
                if rule:
                    rules.append(rule)
                    converted = True
                elif missed:
                    skipped.append(f"{name.strip()}: not modelled.")
        if not converted and not NO_DUEL.search(sentence):
            skipped.append(sentence)

    rules = list(dict.fromkeys(rules))
    touched = armour or shield or rules or mods
    if touched and not skipped:
        status = "applied"
    elif touched:
        status = "partial"
    elif skipped:
        status = "not modelled"
    else:
        status = "no duel effect"
    return armour, shield, rules, mods, skipped, note, status


_ARMOUR_NAMES = {"light armour": "Light Armor", "heavy armour": "Heavy Armor",
                 "full plate armour": "Full Plate Armor"}


def _singular(name):
    name = name.strip().lower()
    if name.endswith("es") and name[:-2].endswith(("sh", "ch")):
        return name[:-2]
    return name[:-1] if name.endswith("s") and not name.endswith("ss") else name


def _equipment_name(phrase):
    """('weapon'|'armour'|'ranged', canonical name) for an equipment phrase, or None."""
    from weapons import find_weapon_key

    phrase = re.sub(r"^(?:a|an|the)\s+", "", phrase.strip().lower())
    for candidate in (phrase, _singular(phrase)):
        if candidate in _ARMOUR_NAMES:
            return "armour", _ARMOUR_NAMES[candidate]
        for key in _weapon_keys():
            for alias in key:
                if alias.lower() == candidate:
                    return "weapon", key[0]
    if re.search(r"\b(bow|longbow|warbow|handgun|pistol|crossbow)s?\b", phrase):
        return "ranged", phrase
    return None


def _weapon_keys():
    from weapons import MeleeWeaponDict
    return list(MeleeWeaponDict)


def equipment_grants(text):
    """Weapons and armour an ability lets its bearer take, from its text."""
    grants = {"weapons": [], "armour": [], "ranged": []}
    phrases = []
    for pattern in (r"may be equipped with (.+?) for no additional points",
                    r"which they may replace with (.+?) for free",
                    r"must be (?:armed|equipped) with (?:either )?(.+?)(?: \(|,|\.|$)"):
        for m in re.finditer(pattern, text, re.I):
            phrases.extend(re.split(r"\s+or\s+|,\s*", m.group(1)))
    if re.search(r"may take an additional hand weapon", text, re.I):
        phrases.append("two hand weapons")
    for phrase in phrases:
        found = _equipment_name(phrase)
        if found:
            kind, name = found
            bucket = {"weapon": "weapons", "armour": "armour", "ranged": "ranged"}[kind]
            if name not in grants[bucket]:
                grants[bucket].append(name)
    return {k: v for k, v in grants.items() if v}


def armies(fields):
    names = [a["fields"]["name"] for a in fields.get("association", []) if "fields" in a]
    books = [n for n in names if BOOKS.match(n)]
    return [n for n in names if not BOOKS.match(n)], books


# Weapon notes with a fixed meaning: (pattern, weapon rules, wielder stat_mods).
WEAPON_NOTES = [
    (r"^(?:during the combat phase, )?the wielder of [^.]+? may re-roll any failed rolls to wound(?: made| during the combat phase)?\.?$",
     lambda m: (["Reroll Failed Wounds"], {})),
    (r"^(?:during the combat phase, )?the wielder of [^.]+? may re-roll any failed rolls to hit(?: made whilst using it| during the combat phase)?\.?$",
     lambda m: (["Reroll Failed Hits"], {})),
    (r"^the wielder of [^.]+? may re-roll any rolls to wound of a natural 1(?: made during the combat phase)?\.?$",
     lambda m: (["Reroll Wounds 1"], {})),
    (r"^the wielder of [^.]+? may re-roll any rolls to hit of a natural 1(?: made during the combat phase)?\.?$",
     lambda m: (["Reroll Hits 1"], {})),
    (r"a roll of (?:a )?(\d)\+ is always a success,? regardless of the target's toughness",
     lambda m: (["Wounds On (%s+)" % m.group(1)], {})),
    (r"^during the combat phase, the wielder of [^.]+? has a \+(\d) modifier to their rolls to hit",
     lambda m: (["To Hit (+%s)" % m.group(1)], {})),
    (r"strikes a killing blow if they roll a natural 5 or 6",
     lambda m: (["Killing Blow 5+"], {})),
    (r"^enemy models must re-roll any successful armour save rolls against wounds caused by this weapon",
     lambda m: (["Enemy Rerolls Successful Armour Saves"], {})),
    (r"^the wielder of [^.]+? has a \+(\d) modifier to (?:their|its) ([a-z ]+?) characteristics?\.?$",
     lambda m: ([], {STAT_NAMES[s.strip()]: int(m.group(1))
                     for s in re.split(r",\s*|\s+and\s+", m.group(2)) if s.strip() in STAT_NAMES})),
    (r"^the wielder of [^.]+? gains the regeneration \((\d)\+\) special rule",
     lambda m: ([], {}, ["Regeneration (%s+)" % m.group(1)])),
]


# Rules a weapon profile lists that the engine reads from the wielder instead.
WIELDER_RULES = {"Frenzy", "Furious Charge", "Terror", "Fear", "Impetuous",
                 "Immune to Psychology", "Magic Resistance (-1)", "Magic Resistance (-2)",
                 "Move Through Cover", "Stubborn", "Unbreakable"}

SITE_TYPOS = {"Amour Bane (1)": "Armour Bane (1)"}


def weapon_entry(name, item):
    """(MeleeWeaponDict profile, note, wielder stat_mods, not-modelled notes)."""
    for table in item["tables"]:
        if str(table.get("range", "")).strip().lower() == "combat":
            notes = tw.notes_of(item["text"])
            bonus, ap, rules, comment = tw.convert(table, notes)
            if "Magical Attacks" not in rules and "Magic" not in rules:
                rules.append("Magical Attacks")
            mods, skipped, wielder = {}, [], []
            for sentence in sentences(notes):
                low = sentence.lower()
                for pattern, make in WEAPON_NOTES:
                    m = re.search(pattern, low)
                    if m:
                        extra_rules, extra_mods, *extra_wielder = make(m)
                        rules.extend(r for r in extra_rules if r not in rules)
                        mods.update(extra_mods)
                        for granted in extra_wielder:
                            wielder.extend(granted)
                        break
                else:
                    if not NO_DUEL.search(sentence) and not restriction(sentence):
                        skipped.append(sentence)
            # Saves protect the wielder, not the weapon: the engine reads them
            # from the character.
            import special_rules as sr
            rules[:] = [SITE_TYPOS.get(r, r) for r in rules]
            for rule in list(rules):
                if (sr.parse_regeneration([rule]) or sr.parse_ward([rule], True, True, True)
                        or rule.startswith("Hatred") or rule in WIELDER_RULES):
                    rules.remove(rule)
                    # Only what the engine reads; the rest stays in the text.
                    if rc.engine_reads(rule) and rule not in wielder:
                        wielder.append(rule)
            return [bonus, ap, rules], comment, mods, skipped, wielder
    return None, None, {}, [], []


def build():
    items, weapons = {}, {}
    for shown, slug in sorted(site.magic_item_index().items()):
        entry = site.entry(f"magic-item/{slug}")
        f = entry["fields"]
        item = site.magic_item(slug)
        name = clean_name(shown)
        kind = f.get("type")
        army_names, books = armies(f)
        text = " ".join(item["text"].split())
        categories = [re.sub(r"\s+Type$", "", c["fields"]["name"])
                      for c in f.get("magicItemType", []) if "fields" in c]
        record = {
            "slug": slug,
            "type": kind,
            "category": categories[0] if categories else None,
            "cost": f.get("cost"),
            "armies": army_names,
            "books": books,
            "extremely_common": "Extremely Common" in text,
            "text": text,
        }
        profile, comment, wmods, wskipped, wielder_rules = (
            weapon_entry(name, item) if kind in ("Magic Weapon", "Ability") else (None, None, {}, [], []))
        if profile is not None:
            record["is_weapon"] = True
            record["status"] = "partial" if wskipped else "applied"
            if comment:
                record["weapon_note"] = comment
            if wmods:
                record["stat_mods"] = wmods
            if wielder_rules:
                record["rules"] = wielder_rules
            if wskipped:
                record["not_modelled"] = wskipped
            key = name if name not in weapons else f"{name} ({', '.join(army_names) or 'Rulebook'})"
            weapons[key] = profile
            record["weapon"] = key
        else:
            armour, shield, rules, mods, skipped, note, status = effects(name, kind, text)
            record.update(status=status)
            if armour:
                record["armour"] = armour
            if shield:
                record["shield"] = True
            if rules:
                record["rules"] = rules
            if mods:
                record["stat_mods"] = mods
            if skipped:
                record["not_modelled"] = skipped
            if note:
                record["restriction"] = note
        grants = equipment_grants(text)
        if grants:
            record["grants"] = grants
        if name in items:
            # Same item name in two armies (e.g. Crown of Horns); keep both.
            name = f"{name} ({', '.join(army_names) or 'Rulebook'})"
        items[name] = record
    return items, weapons


def render(items, weapons):
    lines = [
        '"""Every magic item and ability on https://tow.whfb.app.',
        "",
        "GENERATED by tools/transcribe_items.py - do not edit by hand. Put",
        "corrections in magic_items.py, whose entries take precedence.",
        '"""',
        "",
        "# fmt: off",
        "SITE_ITEMS = {",
    ]
    for name, rec in items.items():
        lines.append(f"    {name!r}: {{")
        for k, v in rec.items():
            lines.append(f"        {k!r}: {v!r},")
        lines.append("    },")
    lines.append("}")
    lines.append("")
    lines.append("# name -> [strength bonus, armour piercing, special rules], as MeleeWeaponDict.")
    lines.append("SITE_ITEM_WEAPONS = {")
    for name, profile in weapons.items():
        lines.append(f"    {name!r}: {profile!r},")
    lines.append("}")
    return "\n".join(lines) + "\n"


def main(argv):
    items, weapons = build()
    from collections import Counter

    print(Counter(r["status"] for r in items.values()))
    print(len(items), "items,", len(weapons), "weapon profiles")
    if "-v" in argv:
        for name, rec in items.items():
            if rec["status"] in ("partial", "applied") and not rec.get("is_weapon"):
                print(f"{name}: {rec.get('armour')} {rec.get('shield')} {rec.get('rules')} {rec.get('stat_mods')}")
    if "-w" in argv:
        with open(OUT, "w", encoding="utf-8") as fh:
            fh.write(render(items, weapons))
        print("wrote", OUT)


if __name__ == "__main__":
    main(sys.argv[1:])
