# The Old World Simulator

Dice-level combat simulator for Warhammer: The Old World. Pure standard-library Python (3.9+). See README.md for layout and rules coverage.

## Testing is mandatory

- Run `python3 run_tests.py` before every commit (the `.githooks/pre-commit` hook does this; enable it with `git config core.hooksPath .githooks`).
- After any major addition (a new faction or unit batch, a new or changed special rule, an engine change, new weapons or items), run `python3 run_tests.py --full` and add tests in the same change:
  - Rosters: a `RosterCase` pinning statlines and points against the source.
  - A rule string in the data: implement it or file it in `tests/rule_catalogue.py` (ENGINE_RULES, LABELS, NOT_SIMULATED or INERT). Never leave one unclassified.
  - Engine rules: scripted-dice tests for the mechanics, plus an exact-probability test in `tests/test_rule_statistics.py`.
  - Edge cases and mirror matches: extend `tests/test_edge_cases.py` / `tests/test_mirror_matches.py` when a change touches strike order, saves or damage.
- Don't weaken a failing test to make it pass. A failure in the catalogue or invariant sweeps usually means a data typo or an illegal default loadout.

## Data generated from tow.whfb.app

- `magic_items_data.py`, `item_allowances.py` and `option_costs.py` are generated (`python3 tools/transcribe_items.py -w`, `python3 tools/transcribe_allowances.py -w`, `python3 tools/transcribe_costs.py -w`); never hand-edit them. A priced option the roster doesn't offer fails `tests/test_points.py`: fix the roster's `equipment_options`. Put corrections in `magic_items.py` (hand-reviewed entries and `CURATED_ABILITIES` win).
- After any roster or statline change run `python3 tools/verify_rosters.py` (offline from `.tow_cache/`); it must report 0 problems.
- Item effects are converted conservatively: conditional wording is never applied, and "during a challenge" counts as always true (a duel is a challenge).

## Conventions

- Rule strings must match the constants in `special_rules.py` exactly, with spaces (`"Witness to Destiny"`, not `"WitnesstoDestiny"`).
- `Character.Wounds` is the profile maximum; damage goes to `current_wounds`.
- Every die goes through `dice.roll_d6`; tests use `dice.seed`, `scripted_dice` or `constant_dice`.
- Each faction module has `CHARACTERS` and `UNITS`; `UnitCategory` is `Character`/`NamedCharacter` or `Unit`.
- Marks of Chaos and Chivalrous Vows are exclusive options (`character_model.EXCLUSIVE_OPTIONS`); bought items and abilities go through `Character(magic_items=...)` and `magic_items.check_purchase`.
- The GUI (`simulator_app.py`, `ui_kit.py`) is Tkinter with a clean native look: use ttk widgets, draw only what ttk lacks in `ui_kit.py`, and keep logic in `app_model.py`, which is tested.
- Mounts go through `Character(mount=...)` and `mounted.py`; follow the Split Profile rules text, and keep a rule with the rider when the text says "(but not its mount)".
