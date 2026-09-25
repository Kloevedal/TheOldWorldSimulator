"""The website: web_api (what the page calls), the site build, and the page's
safety rules."""

from __future__ import annotations

import json
import os
import re
import sys
import tempfile
import unittest
import zipfile

import support  # noqa: F401  (puts the project on sys.path)

import web_api
from web_api import MAX_LIST, MAX_NAME, call, clean_spec

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "web")
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_site  # noqa: E402

PRINCE = {"faction": "High Elf Realms", "profile": "Prince", "weapon": "Great Weapon",
          "armour": "Plate Armor"}
WARBOSS = {"faction": "Orc & Goblin Tribes", "profile": "Orc Warboss", "weapon": "Great Weapon"}


def result(name, *args):
    reply = json.loads(call(name, json.dumps(list(args))))
    if "error" in reply:
        raise AssertionError(reply["error"])
    return reply["result"]


class TestCall(unittest.TestCase):
    def test_only_listed_calls_run(self):
        self.assertIn("error", json.loads(call("clean_spec", "[]")))
        self.assertIn("error", json.loads(call("__import__", '["os"]')))

    def test_bad_arguments_are_errors_not_exceptions(self):
        for args in ("{}", "not json", '"x"', "[1, 2, 3, 4, 5, 6, 7]"):
            with self.subTest(args=args):
                self.assertIn("error", json.loads(call("describe", args)))

    def test_catalog_has_both_modes_under_official_names(self):
        catalog = result("catalog")
        self.assertIn("Prince", catalog["kinds"]["character"]["High Elf Realms"])
        self.assertTrue(catalog["kinds"]["unit"])
        self.assertEqual((catalog["default_runs"], catalog["default_rounds"]), (100, 6))


class TestCleanSpec(unittest.TestCase):
    def test_unknown_army_or_model_is_rejected(self):
        for data in ({}, [], "x", {"faction": "Atlantis", "profile": "King"},
                     {"faction": "High Elf Realms", "profile": "Emperor"}):
            with self.subTest(data=data), self.assertRaises(ValueError):
                clean_spec(data)

    def test_fields_are_bounded(self):
        spec = clean_spec(dict(PRINCE, name="x" * 500, magic_items=["Sword of Might"] * 100,
                               optional_rules="not a list", shield="yes", surprise=1))
        self.assertEqual(len(spec.name), MAX_NAME)
        self.assertEqual(len(spec.magic_items), MAX_LIST)
        self.assertEqual(spec.optional_rules, [])
        self.assertFalse(spec.shield)  # only a real true counts
        self.assertEqual(spec.models, 1)

    def test_unit_size_is_clamped(self):
        spec = clean_spec({"kind": "unit", "faction": "Empire of Man", "profile": "State Troops",
                           "models": 10 ** 9, "frontage": -3})
        self.assertEqual((spec.models, spec.frontage), (200, 1))

    def test_old_army_names_still_load(self):
        self.assertEqual(clean_spec(dict(PRINCE, faction="High Elves")).faction, "High Elf Realms")

    def test_names_are_data(self):
        info = result("describe", dict(PRINCE, name="<img src=x onerror=alert(1)>"))
        self.assertEqual(info["spec"]["name"], "<img src=x onerror=alert(1)>")


class TestPageCalls(unittest.TestCase):
    def test_describe(self):
        info = result("describe", PRINCE)
        self.assertTrue(info["ok"])
        self.assertEqual(info["points"], 130 + 4 + 6)
        self.assertIn({"name": "S", "value": 6, "bare": 4}, info["stats"])

    def test_an_illegal_loadout_is_reported(self):
        info = result("describe", dict(PRINCE, weapon="Sword of Hoeth"))
        self.assertFalse(info["ok"])
        self.assertIn("Invalid weapon", info["error"])

    def test_odds_default_to_the_death(self):
        stats = result("odds", PRINCE, WARBOSS, 50, "death", 3)
        self.assertEqual(stats["wins_a"] + stats["wins_b"] + stats["draws"], 50)
        self.assertEqual(stats["rounds"], "to the death")
        self.assertEqual(result("odds", PRINCE, WARBOSS, 50, "death", 3), stats)

    def test_runs_are_capped(self):
        seen = []
        web_api.odds(PRINCE, WARBOSS, runs=10 ** 9, rounds=1, seed=1, progress=seen.append)
        self.assertEqual(seen[-1], web_api.MAX_RUNS)

    def test_narrate(self):
        text = result("narrate", PRINCE, WARBOSS, 6, 7)
        self.assertIn("=== Round 1 ===", text)

    def test_shop_has_no_rules_text_and_safe_links(self):
        items = result("shop", "High Elf Realms", "Prince")
        self.assertTrue(items)
        for item in items:
            self.assertNotIn("text", item)
            if item["link"]:
                self.assertRegex(item["link"], r"^https://tow\.whfb\.app/magic-item/[a-z0-9-]+$")
        axe = next(i for i in items if i["name"] == "Headsman's Axe")
        self.assertIn("killing blow", axe["search"])

    def test_check_items(self):
        ok = result("check_items", "High Elf Realms", "Prince", ["Armour of Caledor"])
        self.assertEqual(ok["problem"], "")
        self.assertEqual(ok["spent"], {"Magic Items": 35})
        too_much = result("check_items", "High Elf Realms", "Prince", ["Armour of Caledor"] * 4)
        self.assertTrue(too_much["problem"])


class TestSiteBuild(unittest.TestCase):
    def test_strip_removes_rules_text_fields(self):
        source = 'X = {"a": {"text": "Long rules.", "rules": ["Frenzy"], "not_modelled": ["y"]}}\n'
        stripped, removed = build_site.strip(source)
        self.assertNotIn("Long rules", stripped)
        self.assertIn("Frenzy", stripped)
        self.assertEqual(sorted(removed), ["Long rules.", "y"])

    def test_leftover_quotes_are_caught_but_rule_names_are_not(self):
        text = ["A model with this special rule may re-roll failed To Hit rolls against "
                "Hatred (Warriors of Chaos & Daemonic models) enemies in the first round."]
        quote = 'S = "may re-roll failed To Hit rolls against Hatred"\n'
        name = 'S = "Hatred (Warriors of Chaos & Daemonic models)"\n'
        self.assertTrue(build_site.find_quotes({"q.py": quote}, text))
        self.assertFalse(build_site.find_quotes({"n.py": name}, text))

    def test_the_built_site_carries_no_rules_text(self):
        with tempfile.TemporaryDirectory() as out:
            version = build_site.build(out, verbose=False)
            with zipfile.ZipFile(os.path.join(out, "sim.zip")) as zf:
                names = zf.namelist()
                sources = {n: zf.read(n).decode() for n in names}
            with open(os.path.join(out, "index.html"), encoding="utf-8") as fh:
                html = fh.read()
        self.assertIn("web_api.py", names)
        self.assertFalse([n for n in names if n.startswith(("simulator_app", "ui_kit", "tools/", "tests/"))])
        for name, source in sources.items():
            self.assertNotRegex(source, r"['\"](text|not_modelled|weapon_note)['\"]\s*:", name)
        self.assertIn(f"app.js?v={version}", html)
        self.assertNotIn("__BUILD__", html)


class TestPageSafety(unittest.TestCase):
    def read(self, name):
        with open(os.path.join(WEB, name), encoding="utf-8") as fh:
            return fh.read()

    def test_scripts_never_write_html(self):
        # Fighter names come from share links; all text goes in as text.
        for name in ("app.js", "worker.js"):
            code = re.sub(r"//.*", "", self.read(name))
            with self.subTest(file=name):
                self.assertNotRegex(code, r"innerHTML|outerHTML|insertAdjacentHTML|document\.write|\beval\(|new Function")

    def test_the_page_has_a_strict_content_security_policy(self):
        html = self.read("index.html")
        self.assertIn("Content-Security-Policy", html)
        self.assertIn("script-src 'self'", html)
        self.assertNotIn("unsafe-inline", html)
        self.assertNotRegex(html, r"<script>|<style>| on[a-z]+=")

    def test_pyodide_is_pinned(self):
        self.assertRegex(self.read("worker.js"), r"cdn\.jsdelivr\.net/pyodide/v\d+\.\d+\.\d+/full/")


if __name__ == "__main__":
    unittest.main()
