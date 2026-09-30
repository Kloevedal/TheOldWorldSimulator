"""Build the website into site/ (for GitHub Pages, or any static host).

    python3 tools/build_site.py            # build and verify
    python3 tools/build_site.py --serve    # ... then serve on http://localhost:8000

The site runs the simulator in the visitor's browser with Pyodide. This
script packs the Python modules the simulator needs into site/sim.zip,
next to the static page in web/.

Rules text stays out of the site. The rosters and item data carry rules text
copied from tow.whfb.app (`text`, `not_modelled`, `weapon_note`,
`restriction`); the packed copies have those fields removed. The build then
fails if any remaining string is a piece of that text, and checks that the
stripped simulator gives exactly the same results as the full one.
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WEB = os.path.join(ROOT, "web")
OUT = os.path.join(ROOT, "site")
STRIP = {"text", "not_modelled", "weapon_note", "restriction"}
# A remaining string this long that appears inside the rules text fails the build,
# unless it is a rule's name ("Hatred (Warriors of Chaos & Daemonic models)").
MIN_QUOTE = 40
_RULE_NAME = re.compile(r"^[^.]{1,80}\([^()]*\)$")


def modules():
    """Repo files the site needs: everything loaded while every call the page
    makes runs once (some modules are only imported inside functions)."""
    code = ("import contextlib, io, json, os, sys\n"
            "with contextlib.redirect_stdout(io.StringIO()):\n"
            + "".join("    " + line + "\n" for line in _EQUIVALENCE_CHECK.strip().splitlines())
            + "root = os.getcwd()\n"
            "print(json.dumps(sorted(os.path.relpath(m.__file__, root) for m in list(sys.modules.values()) "
            "if getattr(m, '__file__', None) and m.__file__.startswith(root + os.sep))))")
    out = subprocess.run([sys.executable, "-c", code], cwd=ROOT, capture_output=True, text=True)
    if out.returncode:
        raise SystemExit(out.stderr[-3000:])
    return json.loads(out.stdout)


class _StripRulesText(ast.NodeTransformer):
    def __init__(self):
        self.removed = []

    def visit_Dict(self, node):
        self.generic_visit(node)
        keep_keys, keep_values = [], []
        for key, value in zip(node.keys, node.values):
            if isinstance(key, ast.Constant) and key.value in STRIP:
                self.removed.append(value)
                continue
            keep_keys.append(key)
            keep_values.append(value)
        node.keys, node.values = keep_keys, keep_values
        return node


def _strings(node):
    """Every string an expression can produce (constants and literal pieces)."""
    return [n.value for n in ast.walk(node) if isinstance(n, ast.Constant) and isinstance(n.value, str)]


def _fold(text):
    return " ".join(text.lower().split())


def strip(source):
    """(stripped source, rules strings removed)."""
    tree = ast.parse(source)
    stripper = _StripRulesText()
    tree = stripper.visit(tree)
    removed = [s for value in stripper.removed for s in _strings(value)]
    return ast.unparse(ast.fix_missing_locations(tree)) + "\n", removed


def find_quotes(stripped_sources, rules_text):
    """Remaining strings that are pieces of the removed rules text."""
    corpus = "\n".join(_fold(t) for t in rules_text)
    found = []
    for path, source in stripped_sources.items():
        for s in _strings(ast.parse(source)):
            if len(s) >= MIN_QUOTE and not _RULE_NAME.match(s) and _fold(s) in corpus:
                found.append((path, s[:80]))
    return found


# Run in both the full and the stripped tree; the outputs must match.
_EQUIVALENCE_CHECK = r"""
import json, sys
import web_api as w
out = {}
cat = w.catalog()
for kind, armies in cat["kinds"].items():
    for faction, profiles in armies.items():
        for profile in profiles:
            opts = w.options(faction, profile)
            d = opts["defaults"]
            spec = {"kind": kind, "faction": faction, "profile": profile, "weapon": d["weapon"],
                    "armour": d["armour"], "shield": d["shield"]}
            out[f"{kind}/{faction}/{profile}"] = [opts, w.describe(spec)]
        out[f"shop/{faction}/{profiles[0]}"] = w.shop(faction, profiles[0])
a = {"faction": "High Elf Realms", "profile": "Prince", "weapon": "Great Weapon", "armour": "Plate Armor"}
b = {"faction": "Orc & Goblin Tribes", "profile": "Orc Warboss", "weapon": "Great Weapon"}
out["odds"] = w.odds(a, b, 200, None, 7)
ua = {"kind": "unit", "faction": "Empire of Man", "profile": "State Troops", "weapon": "Halberd",
      "armour": "Light Armor", "models": 20, "frontage": 5}
ub = {"kind": "unit", "faction": "Orc & Goblin Tribes", "profile": "Orc Mob", "models": 20, "frontage": 5}
out["unit odds"] = w.odds(ua, ub, 100, None, 3)
out["unit narrate"] = w.narrate(ua, ub, 6, 3)
out["narrate"] = w.narrate(a, b, 6, 7)
print(json.dumps(out, sort_keys=True))
"""


def _run_check(path, isolated):
    args = [sys.executable] + (["-I", "-S"] if isolated else []) + ["-c",
            "import sys; sys.path.insert(0, %r)\n" % path + _EQUIVALENCE_CHECK]
    result = subprocess.run(args, cwd=path, capture_output=True, text=True)
    if result.returncode:
        raise SystemExit(f"simulator failed in {path}:\n{result.stderr[-3000:]}")
    return result.stdout


def build(out=OUT, verbose=True):
    if os.path.isdir(out):
        shutil.rmtree(out)
    pack = os.path.join(out, "_py")
    os.makedirs(pack)
    stripped, rules_text = {}, []
    for rel in modules():
        with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
            source, removed = strip(fh.read())
        stripped[rel] = source
        rules_text += removed
        target = os.path.join(pack, rel)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as fh:
            fh.write(source)

    quotes = find_quotes(stripped, rules_text)
    if quotes:
        listing = "\n".join(f"  {p}: {s!r}" for p, s in quotes[:20])
        raise SystemExit(f"rules text would be published ({len(quotes)} strings):\n{listing}")

    if _run_check(ROOT, isolated=False) != _run_check(pack, isolated=True):
        raise SystemExit("the stripped simulator does not match the full one")

    archive = os.path.join(out, "sim.zip")
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for rel in sorted(stripped):
            info = zipfile.ZipInfo(rel, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, stripped[rel])
    shutil.rmtree(pack)
    # The version (for cache busting) covers the simulator and every page file.
    web_files = sorted(n for n in os.listdir(WEB) if os.path.isfile(os.path.join(WEB, n)))
    digest = hashlib.sha256()
    for path in [archive] + [os.path.join(WEB, n) for n in web_files]:
        with open(path, "rb") as fh:
            digest.update(fh.read())
    version = digest.hexdigest()[:12]

    for name in web_files:
        with open(os.path.join(WEB, name), "rb") as fh:
            data = fh.read()
        if name.endswith((".html", ".js")):
            data = data.replace(b"__BUILD__", version.encode())
        with open(os.path.join(out, name), "wb") as fh:
            fh.write(data)
    open(os.path.join(out, ".nojekyll"), "w").close()
    if verbose:
        size = os.path.getsize(archive) // 1024
        print(f"built {out}: {len(stripped)} modules, {len(rules_text)} rules-text strings removed, "
              f"sim.zip {size} KB, version {version}")
    return version


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import http.server
        import functools

        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=OUT)
        print("serving http://localhost:8000  (Ctrl-C to stop)")
        http.server.ThreadingHTTPServer(("127.0.0.1", 8000), handler).serve_forever()
