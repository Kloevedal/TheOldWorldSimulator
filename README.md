# The Old World Simulator

A dice-level simulator for **Warhammer: The Old World** combat.

## Intent

1. **Named characters** — build combatants from published profiles (Korhil, Ishaya Vess, …) with their real rules.
2. **Custom characters** — build your own within the constraints of the rulebook: legal profiles, legal equipment options, legal special-rule combinations.
3. **Duels** — resolve a fight between two characters by rolling actual dice, following the Old World combat sequence, and report the outcome.

Units, shooting, movement and psychology are out of scope for now — see [todo.txt](todo.txt).

## Layout

| File | Role |
| --- | --- |
| [character_model.py](character_model.py) | `Character`. Builds from a faction profile or from raw stats; validates equipment against the profile's legal options. |
| [factions/](factions/) | One module per faction: profiles, aliases, `FACTION_RULES` and (later) regular units. 165 characters across all 19 armies on the site. |
| [mounts.py](mounts.py) | Mount characteristics: all 93 mounts the profiles reference. Data only — the engine does not read it yet. |
| [faction_profiles.py](faction_profiles.py) | Assembles `FactionProfiles` from the `factions` package and provides `resolve_faction` / `resolve_profile`. Also holds `RACE_NAMES`. |
| [charts.py](charts.py) | `WeaponSkillChart` (to-hit) and `Wounds_vs_ToughnessChart` (to-wound), transcribed from the rulebook and pinned cell by cell. |
| [weapons.py](weapons.py) | `MeleeWeaponDict`: `(names…) -> [strength bonus, AP, special rules]`, plus lookup helpers. |
| [armor.py](armor.py) | `ArmourDict` and `get_armour_save`. |
| [special_rules.py](special_rules.py) | Rule-name constants, plus the parsers that turn rule strings into numbers. |
| [elven_honors.py](elven_honors.py) | High Elf Honours: stat mods, extra rules, extra weapon options. |
| [dice.py](dice.py) | Every D6 in the engine. Seedable and scriptable, so tests are deterministic. |
| [combat_simulations.py](combat_simulations.py) | The engine: rolls, strike order, and the duel driver. |
| [tests/](tests/) | 298 tests. `python3 -m unittest discover -s tests` |
| [tools/](tools/) | Development only: `tow_site.py` reads the site's page data, `transcribe_faction.py` drafts a faction module from it, `transcribe_mounts.py` does the same for mounts. |
| [simulator_app.py](simulator_app.py) | Desktop app (Tkinter). Launch with [run_app.command](run_app.command). |
| [app_model.py](app_model.py) | The app's display-free logic: `FighterSpec`, `CharacterStore`, `run_statistics`, `narrate_duel`. Tested in [tests/test_app_model.py](tests/test_app_model.py). |
| [testbench.ipynb](testbench.ipynb) | Scratch notebook. |

Data lives in dicts keyed by **tuples of synonyms** (`("Great Weapon", "GW", "GreatWeapon")`), so lookups go through helpers like `find_weapon_key` rather than direct indexing.

## How a duel resolves

`combat_simulation(c1, c2, rounds)` → per round:

1. `determine_strike_order` splits the fighters into **strike steps**. Strike First always precedes normal, which always precedes Strike Last; Initiative only breaks ties *within* a band. Both bands and Initiative equal → one step, i.e. simultaneous. Strike First and Strike Last on the same model cancel out. Weapon-granted Strike Last (a Great Weapon) counts as well as the character's own rules.
2. Every strike in a step is **rolled before any of it is applied**, so simultaneous fighters both get to swing.
   `OneRoundMeleeCombat` = `apply_weapon_stats` → `RollToHit` → `RollToWound` → `RollArmorSave`, returning a `StrikeResult` and applying no damage.
3. `resolve_strike` is the **single place** wards, regeneration and Killing Blow are resolved. Each unsaved wound gets a ward save, then a regeneration save; what survives either slays outright (Killing Blow) or costs one wound.
4. Deaths are checked after each step, so a fighter killed before it swings does not swing.

`Character.Wounds` is the profile maximum and is never mutated. All damage goes to `Character.current_wounds`.

### Rules implemented

Ithilmar Weapons, Ensorcelled Weapons, Gromril Weapons, Warpstone Weapons, Khopesh, Obsidian Blades, Gromril Armour, Flammable (no Regeneration save against a Flaming attack), Multiple Wounds with a dice value (`Multiple Wounds (D3)`, rolled per unsaved wound), the unarmoured 7+ armour value (a shield or Armoured Hide gives an unarmoured model a 6+), the named wards of the later lists (Arcane Shield, Blessed Knight, Favour of the Goddess, Celestial Forged Armour, Talismanic Tattoos, Ancestral Shield, Blessings of the Volcano God vs Flaming), Settra's Champion (Nekaph's Killing Blow on a 5+, since a duel is a challenge), Magical Attacks, Reroll Hits 1, Hatred(X) (plural-tolerant, so `Hatred (Dwarfs)` matches `Race: "Dwarf"`), Frenzy, Furious Charge, Choppas, Elven Reflexes, Ethereal, Killing Blow (character- or weapon-granted, with a parsed threshold), Armour Bane (`AB1` or `Armour Bane (1)`), Flaming, Magic, ward saves (WardX, Chaos Armour (X+), Witness to Destiny, Dragon Armour, Blessings of Asuryan vs Flaming — each recognised bare or with a `(6+ Ward)` gloss), Regeneration (`Regen5` or `Regeneration (5+)`), shields, armour bonuses (`AH1` or `Armoured Hide (1)`), Wound Stealing (the Bog-wood Staff), forced rerolls of a successful enemy hit (Mathlann's Ire), Strike First / Strike Last, and the first-round gating on lances, cavalry spears, flails and morning stars.

### Rules present in the data but inert

Army-, psychology- and movement-level rules that a one-on-one duel never exercises: Gaze of the Gods (a Command sub-phase roll, and there is no command phase), Marks of Chaos, Warp-spawned, Unstable, Unbreakable, Handler, Loner, Vanguard, Accomplished Archers, Arrows of Isha, Commanding Voice, Naval Discipline, Valour of Ages, Waaagh!, Warband, Da Boyz, Mob Rule, Ignore Panic, Ignore Goblin Panic, Fear of Elves, Rallying Cry, Impetuous, Quell Impetuosity, Animosity, Immune to Psychology, Stubborn, Unbreakable, Stupidity, Terror, Large Target, Close Order, Valour of Ages, Move Through Cover, Evasive, Ignores Cover, Ambushers, Fast Cavalry, Swiftstride, Hit & Run, All Sneaky Like, Chariot Runners, Warpaint.

Rules that a duel *would* exercise but that are not implemented yet: Lion Cloak, Poisoned Attacks, Stomp Attacks, Impact Hits, dice-valued Extra Attacks (Trickster's Blades, the Dolorous Blade's Rapid Strikes), Monster Slayer, Cloud of Flies, Beguiling Aura, Parry, Dry as Dust, Blessings of the Lady (a conditional 6+/5+ Ward), Tree Whack, Mighty Constitution, Precision Strikes, Ithilmar Armour, Stomp Attacks (D6), Motherly Love, Slimy Shanks, Indiscriminate Hunger, Timmm-berrr!, Lore of Gork, Lore of Mork, Lore of Saphery, Lileath's Blessing, Da Troll Calla, Protect Da Boss, Syphoned Strength.

All of them are carried verbatim on the profiles, so nothing is lost when they are implemented.

Also inert: mounts and `OptionalRules` are recorded on profiles but not yet used.

## Naming

Factions can be named by alias. `resolve_faction` accepts the army book's own
title as well as the internal key, matching case-insensitively and treating
`&` as `and`, so all of these reach the same roster:

```python
Character(name="Grimgor", faction_type="Orc & Goblin Tribes", profile_name="Black Orc Warboss")
Character(name="Grimgor", faction_type="O&G",                 profile_name="black orc warboss")
Character(name="Grimgor", faction_type="Orcs",                profile_name="Black Orc Warboss")
```

The internal key stays `"Orcs"`, which is what `FactionProfiles` is keyed on and
what a built character reports as `.faction`; the resolved profile name is on
`.profile_name`. Profile names are matched case-insensitively too, since the
published names mix `Orc BigBoss` with `Black Orc Bigboss`. Profiles take shorthand names too, via `PROFILE_ALIASES`: `"Korhil"` reaches
`"Korhil Lionmane"`, `"Handmaiden"` reaches `"Handmaiden of the Everqueen"`,
`"Kiknik"` reaches `"Kiknik Toofsnatcha"`. Add new aliases to `FACTION_ALIASES`
or `PROFILE_ALIASES` in [faction_profiles.py](faction_profiles.py) — tests check
that every alias points at something that exists.

## Adding a faction

Each faction is one module in [factions/](factions/), declaring:

| name | meaning |
| --- | --- |
| `FACTION` | the key it is filed under in `FactionProfiles` |
| `ALIASES` | other names that should resolve to it |
| `PROFILE_ALIASES` | shorthand names for individual profiles |
| `CHARACTERS` | character profiles |
| `UNITS` | regular unit profiles — empty for now |
| `PROFILES` | `CHARACTERS + UNITS`, which is what the registry reads |

Drop a module in the package, list it in `FACTION_MODULES` in
[factions/__init__.py](factions/__init__.py), and nothing else needs to change:
`faction_profiles.py` assembles the profiles and both alias tables from it.
`TestFactionPackage` checks every module declares the required names and that no
two factions claim the same alias.

`RACE_NAMES` stays central, because races cut across factions — a Goblin appears
in an Orc army, and Hatred (Orcs & Goblins) has to match both.

## Adding a profile

Profiles come from the army pages at `https://tow.whfb.app/army/<slug>` and the per-unit pages at `https://tow.whfb.app/unit/<slug>`, which carry points, wargear options and special rules.

The ten factions added last (Grand Cathay, Kingdom of Bretonnia, Lizardmen, Ogre Kingdoms, Realms of Men, Regiments of Renown, Skaven, Tomb Kings of Khemri, Vampire Counts, Wood Elf Realms) were drafted with `python3 tools/transcribe_faction.py <key> -w` and reviewed by hand. Corrections the site's own row cannot express (Settra's Wounds come from his chariot; the Anvil of Doom fights with its crew) are `overrides` in the generator's config, with the reason written into the profile comment, so re-running it is safe. Weapons with no melee profile (bows, pistols, breath and thrown weapons) are left out of the options and named in the profile comment.

Three things to watch when adding one:

- **Rule names must match the constants in [special_rules.py](special_rules.py) exactly.** A typo does not raise — it silently disables the rule. `TestOrcProfiles.test_rule_names_are_spelled_as_the_engine_expects` pins the important ones.
- **Paid upgrades are not base rules.** Frenzy and Warpaint on an Orc Warboss are bought, so they belong in `OptionalRules` (or get passed via `SpecialRules=` at construction), not in `base_profile["SpecialRules"]`.
- **The site writes statlines as M WS BS S T W I A Ld, but the profile dicts order Initiative before Wounds.** Transposing those two is easy and silent. `TestOrcProfiles.test_statlines_match_the_source` pins every statline against the source.

`TestOrcProfiles` also checks that every profile builds, fights, declares a Race that exists in `RACE_NAMES`, and that its own default weapon and armour satisfy its own `equipment_options`.

## Magic items

Named characters carry fixed wargear, so their items are applied automatically
at construction: `apply_magic_items` reads each name from the profile's
`equipment_options["items"]` and appends the special rules the item grants.
Korhil gets the Pelt of Charandis (+1 armour in combat, Regeneration 5+),
Ogdruz gets the Trollhide Shawl (+1 armour, Regeneration 5+, Flammable).

Two kinds of entry are deliberately quiet:

- **Magic weapons** (Chayal, Mathlann's Ire, Da Skull Smasha, Bog-wood Staff)
  are marked `is_weapon` and grant no character rules. They reach the model as
  its `Weapon`, and their profile lives in `MeleeWeaponDict`. Each named
  character defaults to their signature weapon.
- **Items with no duel effect** (Da Boss's Trophy Rack, which is Fear and
  combat result; the Lore Familiar, which is spell selection) carry an empty
  rules list and the rules text as a note, so they read as understood rather
  than forgotten.

An item that is not in `MagicItemDict` is reported rather than silently
ignored — `apply_magic_items` returns the unrecognised names and `Character`
prints a warning. A test asserts every named character's items are recognised.

Generic characters do **not** get free items: they are supposed to buy them
against a points allowance, which is not modelled yet.

## Scraping caveat

**Use `tools/tow_site.py`.** Every page on `tow.whfb.app` embeds the full
entry it renders as JSON (`<script id="__NEXT_DATA__">`), so the helper reads
that with `curl` instead of the rendered page, and caches it under
`.tow_cache/`. Either the entry is there or the helper raises — including for
the site's soft failure, where an unknown slug under a valid route returns
HTTP 200 with an empty entry. The notes below predate the helper and apply to
reading the *rendered* page.

The site's own data has errors too, which the tools report rather than copy:
the Saurus Oldblood and Scar-Veteran pages link "Cold One" to the Terradon
page, and the Goblin Warboss and Goblin Bigboss pages link a mount as "Gigantic Spide".

`tow.whfb.app` renders through JavaScript, and a fetch of it can come back
partial — several magic-item pages returned nothing but "Loading...". A partial
fetch is not always obvious: a page can yield its prose paragraph while its
**"Special Rules:" line is missing entirely**, which reads as a complete answer.

That happened here. Chayal was briefly recorded as having no Killing Blow and
no Requires Two Hands, and Mathlann's Ire as having no Armour Bane, because two
independent fetches of those pages both returned only the prose. Both are wrong;
the data now matches what the pages actually show.

So: **treat any rule list taken from a magic-item or special-rule page as
unverified until a human has looked at the page.** The unit/roster pages have
been more reliable — their statlines and special rules matched hand-entered data
everywhere they overlapped — but the item pages have not.

Items whose rules came from a single fetch and have not been eyeballed:
Storm's Wrath, Da Boss's Trophy Rack, Bog-wood Staff, Trollhide Shawl,
Lore Familiar, Pelt of Charandis.

Items whose pages **would not load at all** carry `"verified": False` and an
empty rules list, so they are recorded and testable but contribute nothing:
Armour of Skaldour, Furnace Hammer, Griffon Helm, Grudge-Settler, Grudgestone,
Judgement, Rivet Gun, Slayer Crown. `magic_items.unverified_items()` returns
that list and `TestUnverifiedItems` pins it, so the gap cannot grow unnoticed.
Where a weapon's profile was unavailable the character wields a plain hand
weapon rather than invented stats — Burlok Damminson and his Furnace Hammer.

## Edition

Everything here is **Warhammer: The Old World**, not an earlier edition of
Warhammer Fantasy. All profiles, points, weapon profiles and rules text come
from <https://tow.whfb.app> or from the Arcane Journals it cites.

The engine originally carried assumptions from an earlier edition. Those found
and corrected so far:

| what | was | The Old World |
| --- | --- | --- |
| To Hit chart | two wrong cells (WS4 v WS8, WS10 v WS5) | fixed and pinned |
| To Wound chart | four cells wrongly "cannot wound" (S2/T7, S3/T8, S4/T9, S5/T10) | a gap of 5 still wounds on a 6+ |
| Killing Blow | allowed an Armour save | permits **no** Armour save |
| Killing Blow | allowed a Regeneration save | permits **no** Regeneration save |
| Killing Blow | applied to every model | **Infantry and Cavalry only** |

The charts are the load-bearing ones — every roll goes through them, so six
wrong cells skewed every result. `tests/test_charts.py` now pins all 200 cells.

Still unverified against the rulebook: `BEST_POSSIBLE_ARMOUR_SAVE = 2`.

The generic weapon profiles (Great Weapon, Halberd, Flail, Morning Star, Lance,
Cavalry Spear, Whip, Two Hand Weapons) have now been checked against the
site. The Flail was missing Requires Two Hands and now has it. The Flail and
Morning Star also have Armour Bane (1) on the charge only. The engine cannot
limit Armour Bane to the first round, so it is left off both rather than
applied every round.

## Army-wide rules

Each faction module carries a `FACTION_RULES` dict giving its army-wide rules,
each with a `status` of `"implemented"`, `"partial"` or `None` (recorded only)
and the rules text where it could be read. That makes the gap between "the
faction has this rule" and "the engine does something with it" explicit and
testable rather than a matter of reading the engine.

## Known gaps

- `BEST_POSSIBLE_ARMOUR_SAVE` is 2 — confirm whether The Old World allows a 1+.
- Points costs are recorded on every Orc & Goblin profile as `points`, but nothing spends them yet — upgrade costs and the magic-item allowance are still missing, so "build a legal army list" is not enforceable.
- Every army on the site has its characters: the original nine plus Grand Cathay, Kingdom of Bretonnia, Lizardmen, Ogre Kingdoms, Realms of Men, Regiments of Renown, Skaven, Tomb Kings of Khemri, Vampire Counts and Wood Elf Realms. Regiments of Renown has one entry, Prince Ulther's Dragon Company, which the site files as a character; the profile is Prince Ulther's own row.
- **Mounts are data only.** [mounts.py](mounts.py) holds all 93 mounts the profiles reference (`mounts.missing_mounts(FactionProfiles)` is empty). Nothing in the engine reads the module, so a mounted character fights on foot. Mount names are the site's own names; where two armies share a name for different mounts they keep the site's qualifier (`Warhorse (Bretonnia)`, `Skeletal Steed (Vampire Counts)`).
- **Common magic items are recorded but not purchasable.** All 68 rulebook items are in `MagicItemDict` (`common: True`, with `cost`), and the magic weapons have profiles. `apply_magic_items` applies their rules, armour and shields, but nothing yet lets a generic character buy them. Army-specific magic items (Forces of Fantasy, Ravening Hordes, the Arcane Journals) are not transcribed, except the named characters' own.
- Only characters, no regular units — every faction module has an empty `UNITS`.
- Runic items are not modelled, so Dwarf characters fight without their runes. Thorgrim Ulleksson is worst hit: his armour *is* the Armour of Skaldour, so with that untranscribed he currently has no armour save at all.
- Magic is not simulated. `WizardLevel` and `Lores` are recorded on the twelve casters but nothing reads them, so an Archmage or a Weirdnob fights as a poor melee character.
- Mounts are recorded in `mount_options` but not simulated, so Kiknik Toofsnatcha fights on foot and the Dragon Mage fights without its Sun Dragon.
- Magic items are applied for **named characters only** — see below. Item *purchasing* for generic characters is not modelled, so a Noble's 50-point allowance buys nothing and the Handmaiden's optional Horn of Isha is never taken.
- Bows (Warbow, Bow of Avelorn) appear in equipment options but have no entry in `MeleeWeaponDict`, since shooting is not implemented. They are tolerated, not simulated.

## Desktop app

Double-click `run_app.command` in Finder, or run `./run_app.command`.

- **Pick two fighters.** For each, choose a faction, then a unit, then its gear. The weapon and armour lists show only that profile's legal options. The shield box is disabled when the profile can't take one. Paid upgrades (Frenzy, Warpaint) and Elven Honours appear as checkboxes where the profile allows them. The statline and special rules update as you choose.
- **Choose how to fight.** *Statistics* fights N duels and reports each side's wins, split into wins by slaying and wins on wounds, plus draws. *Narrated duel* fights one duel and shows the engine's round-by-round dice log. A **Seed** makes either mode reproducible. ⌘↩ runs.
- **Save a character.** *Save character…* stores the current loadout under a name. Saved characters appear under **★ Saved characters** in both panels' faction list, where they can also be deleted. They live in `~/Library/Application Support/TheOldWorldSimulator/custom_characters.json`. Set `TOW_SIM_CHARACTERS` to use a different file.

The launcher runs the app with uv's Python 3.13, which bundles Tk 8.6. It falls back to `python3`, but macOS's system Python ships Apple's deprecated Tk 8.5, which renders poorly.

## Running it

No dependencies — the engine is pure standard library, and works on Python 3.8+.

```bash
python3 -m unittest discover -s tests    # 298 tests
```

```python
import dice
from combat_simulations import *

dice.seed(42)                            # optional: reproducible duels
prince = Character(name="Aenarion", faction_type="High Elves", profile_name="Prince",
                   Armor="Plate Armor", Weapon="Great Weapon")
warboss = Character(name="Grimgor", faction_type="Orcs", profile_name="Black Orc Warboss",
                    Weapon="Great Weapon")
combat_simulation(prince, warboss, rounds=4, verbose=True)
```

To measure a matchup rather than watch one fight, loop with `verbose=False` and rebuild both characters each iteration.
