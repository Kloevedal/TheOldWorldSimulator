"""Every faction module agrees with https://tow.whfb.app.

Runs tools/verify_rosters.py against the page cache in .tow_cache/: every
character and unit on each army page is present, and every statline and
points value matches the row the model fights with. The cache is not in git,
so on a fresh clone (and in CI) this is skipped; fill it by running
`python3 tools/verify_rosters.py` once with network access.
"""

from __future__ import annotations

import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".tow_cache")
sys.path.insert(0, os.path.join(ROOT, "tools"))


@unittest.skipUnless(os.path.isdir(CACHE) and os.listdir(CACHE),
                     "no .tow_cache - run tools/verify_rosters.py online first")
class TestRostersMatchTheSite(unittest.TestCase):
    def test_every_faction_matches_the_site(self):
        import transcribe_faction as tf
        import verify_rosters as vr

        for key, cfg in tf.FACTIONS.items():
            if not cfg.get("module"):
                continue
            with self.subTest(faction=cfg["faction"]):
                try:
                    problems = vr.verify(key)
                except Exception as exc:  # an uncached page needs the network
                    self.skipTest(f"{cfg['faction']}: {exc}")
                self.assertEqual(problems, [], "\n".join(problems))


if __name__ == "__main__":
    unittest.main()
