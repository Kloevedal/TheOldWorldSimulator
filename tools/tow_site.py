"""Read army, unit, rule and magic-item pages from https://tow.whfb.app.

The site is a Next.js app. Its pages render through JavaScript, but every page
also embeds the full Contentful entry it renders as JSON in a
`<script id="__NEXT_DATA__">` tag, so the data can be read without a browser.
Reading that JSON avoids the partial-render problem described in the README
(a fetch that returns "Loading..." or drops the "Special Rules:" line): either
the entry is there in full or the page raises.

Pages are cached under `.tow_cache/` so re-running a transcription does not
refetch. Delete that directory to pick up site changes.

This is a development tool, not part of the engine. It uses curl rather than
urllib because the site's TLS setup trips some Python installs.
"""

from __future__ import annotations

import json
import os
import re
import subprocess

BASE = "https://tow.whfb.app"
CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".tow_cache")

_NEXT_DATA = re.compile(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', re.S)


class PageNotFound(LookupError):
    pass


def page(path):
    """pageProps for a site path such as "unit/infernal-castellan"."""
    path = path.strip("/")
    cached = os.path.join(CACHE, path.replace("/", "__") + ".json")
    if os.path.exists(cached):
        with open(cached, encoding="utf-8") as fh:
            data = json.load(fh)
    else:
        html = subprocess.run(
            ["curl", "-sL", "--fail", "--max-time", "60", f"{BASE}/{path}"],
            check=True, capture_output=True, text=True,
        ).stdout
        match = _NEXT_DATA.search(html)
        if not match:
            raise RuntimeError(f"{path}: no __NEXT_DATA__ in page")
        data = json.loads(match.group(1))
        os.makedirs(CACHE, exist_ok=True)
        with open(cached, "w", encoding="utf-8") as fh:
            json.dump(data, fh)
    if data.get("page") == "/404":
        raise PageNotFound(path)
    return data["props"]["pageProps"]


def army_units(slug):
    """[(section name, unit slug, unit name)] for an army page, in site order."""
    props = page(f"army/{slug}")
    out = []
    for group in props["unitsByType"]:
        section = group["section"]["fields"]["name"]
        for unit in group["units"]:
            out.append((section, unit["fields"]["slug"], unit["fields"]["name"]))
    return out


def army_rules(slug):
    """{rule type name: [(rule name, rule slug)]} listed on an army page."""
    props = page(f"army/{slug}")
    return {
        group["fields"]["name"]: [
            (r["fields"]["name"], r["fields"]["slug"]) for r in group["rules"]
        ]
        for group in props["rulesByType"]
    }


def text(node, _depth=0):
    """Plain text of a Contentful rich-text node.

    Links to rules, weapons and items are rendered as their displayed text,
    which carries any parameter ("Regeneration (5+)" rather than the linked
    rule's generic "Regeneration (X+)"). Nested list items are indented two
    spaces per level, so option groups keep their structure.
    """
    if node is None:
        return ""
    if isinstance(node, str):
        return node
    if isinstance(node, list):
        return "".join(text(n, _depth) for n in node)
    kind = node.get("nodeType")
    if kind == "text":
        return node.get("value", "")
    if kind in ("embedded-entry-inline", "embedded-entry-block"):
        fields = node.get("data", {}).get("target", {}).get("fields") or {}
        label = fields.get("name", "")
        return label + ("\n" if kind == "embedded-entry-block" else "")
    if kind in ("unordered-list", "ordered-list"):
        return "".join(text(n, _depth + 1) for n in node.get("content", []))
    if kind == "list-item":
        own, nested = [], []
        for child in node.get("content", []):
            (nested if child.get("nodeType", "").endswith("list") else own).append(child)
        line = " ".join(text(c, _depth).strip() for c in own).strip()
        return "  " * (_depth - 1) + "- " + line + "\n" + "".join(text(c, _depth) for c in nested)
    inner = text(node.get("content", []), _depth)
    if kind in ("paragraph", "heading-1", "heading-2", "heading-3", "heading-4", "heading-5", "heading-6"):
        return inner.strip() + "\n"
    if kind == "table-row":
        cells = [text(c, _depth).strip() for c in node.get("content", [])]
        return " | ".join(cells) + "\n"
    return inner


def linked_names(node):
    """Displayed text of every link in a rich-text node, in order."""
    return [shown for shown, _slug, _kind in linked(node)]


def linked(node):
    """(displayed text, target slug, target content type) for every link."""
    names = []

    def walk(n):
        if isinstance(n, list):
            for item in n:
                walk(item)
            return
        if not isinstance(n, dict):
            return
        kind = n.get("nodeType", "")
        if kind.startswith(("embedded-entry", "entry-hyperlink")):
            target = n.get("data", {}).get("target", {})
            fields = target.get("fields") or {}
            kind = target.get("sys", {}).get("contentType", {}).get("sys", {}).get("id")
            shown = text(n.get("content")).strip() or fields.get("name", "")
            if shown:
                names.append((shown, fields.get("slug"), kind))
            return
        walk(n.get("content", []))

    walk(node)
    return names


def split_items(node):
    """Comma/newline separated items of a rich-text list field, as plain text."""
    raw = text(node)
    parts = re.split(r"[\n,]+", raw)
    return [p.strip(" .-") for p in parts if p.strip(" .-")]


def unit(slug):
    """Normalised view of a unit page."""
    f = entry(f"unit/{slug}")["fields"]
    return {
        "slug": slug,
        "name": f["name"],
        "cost": f.get("cost"),
        "profiles": f.get("unitProfile") or [],
        "unit_category": [c["fields"]["name"] for c in f.get("unitCategory", []) if "fields" in c],
        "troop_type": [c["fields"]["name"] for c in f.get("troopType", []) if "fields" in c],
        "equipment": split_items(f.get("equipment")),
        "special_rules": linked_names(f.get("specialRules")) or split_items(f.get("specialRules")),
        "optional_rules": linked_names(f.get("optionalRules")),
        "rule_links": linked(f.get("specialRules")),
        "option_links": linked(f.get("options")),
        "equipment_links": linked(f.get("equipment")),
        "options": text(f.get("options")),
        "notes": text(f.get("notes")),
        "wizard_level": f.get("wizardLevel"),
        "lores": [l["fields"]["name"] for l in f.get("magicLore", []) or [] if "fields" in l],
        "raw": f,
    }


def entry(path):
    """The Contentful entry a page renders.

    An unknown slug under a valid route still returns HTTP 200 with an empty
    entry - the site's version of a blank screen - so that is an error here.
    """
    found = page(path).get("entry") or {}
    if not found.get("fields"):
        raise PageNotFound(f"{path}: page rendered no entry")
    return found


_RULE_PATHS = None


def rule_path(slug):
    """Site path of a rule, which lives under its rule type's slug."""
    global _RULE_PATHS
    if _RULE_PATHS is None:
        _RULE_PATHS = {}
        for r in page("sitemap/rules")["rules"]:
            types = r["fields"].get("ruleType") or []
            if types and "fields" in types[0]:
                _RULE_PATHS[r["fields"]["slug"]] = f"{types[0]['fields']['slug']}/{r['fields']['slug']}"
    if slug not in _RULE_PATHS:
        raise PageNotFound(f"rule {slug!r} is not in the site's rule index")
    return _RULE_PATHS[slug]


def rule_index():
    """{rule name: slug} for every rule on the site."""
    return {
        r["fields"]["name"]: r["fields"]["slug"]
        for r in page("sitemap/rules")["rules"]
    }


def rule(slug):
    """Normalised view of a rule page: name, plain text and any profile tables."""
    e = entry(rule_path(slug))
    f = e["fields"]
    return {
        "name": f["name"],
        "slug": slug,
        "text": text(f.get("body")).strip(),
        "tables": embedded_tables(f.get("body")),
        "fields": f,
    }


def embedded_tables(node):
    """Resolved embedded entries (weapon profiles and the like) in a body."""
    found = []

    def walk(n):
        if isinstance(n, list):
            for item in n:
                walk(item)
        elif isinstance(n, dict):
            if n.get("nodeType", "").startswith("embedded-entry"):
                target = n.get("data", {}).get("target", {})
                if target.get("fields"):
                    found.append(target["fields"])
            walk(n.get("content", []))

    walk(node)
    return found


_ITEM_INDEX = None


def magic_item_index():
    """{item name: slug} for every magic item on the site."""
    global _ITEM_INDEX
    if _ITEM_INDEX is None:
        _ITEM_INDEX = {
            i["fields"]["name"]: i["fields"]["slug"]
            for i in page("sitemap/magic-items")["magicItems"]
        }
    return _ITEM_INDEX


def magic_item(slug):
    """Normalised view of a magic-item page."""
    f = entry(f"magic-item/{slug}")["fields"]
    return {
        "name": f["name"],
        "slug": slug,
        "text": text(f.get("body") or f.get("description")).strip(),
        "tables": embedded_tables(f.get("body") or f.get("description")),
        "fields": f,
    }


if __name__ == "__main__":
    import sys

    print(json.dumps(page(sys.argv[1]), indent=1)[:20000])
