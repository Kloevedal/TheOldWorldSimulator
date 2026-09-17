"""Every special-rule string in the data, and what the engine does with it.

A misspelt rule never raises - it just silently does nothing - so the suite
insists that every rule string reachable from a profile, weapon, magic item or
Elven Honour is accounted for here, in exactly one of:

    engine_reads(rule)  the combat engine acts on this exact string
    LABELS              a named rule whose duel effect is carried by a
                        parseable companion rule on the same model
                        ("Blackshard Armour" + "Ward5 (Flaming)")
    NOT_SIMULATED       would matter in a one-on-one melee duel, but the engine
                        does not model it yet - the known-gaps list
    INERT               has no bearing on a one-on-one melee duel (movement,
                        shooting, magic, psychology, army composition, ...)

test_rule_catalogue.py checks both directions: rules in LABELS, NOT_SIMULATED
and INERT must leave a seeded duel byte-for-byte unchanged, and rules the
engine reads must change *something* in at least one probe scenario.

When you add a rule to the data: if the engine should act on it, implement it
(and add its constant to ENGINE_RULES if it is a plain flag); otherwise file it
under the right heading below.
"""

from __future__ import annotations

import re

import special_rules as sr

# Plain flag rules that the engine (or Character construction) checks by name.
ENGINE_RULES = {
    sr.AccursedWeapons,
    sr.Barding,
    sr.BeguilingPresence,
    sr.BlessingsOfTheLady,
    sr.FirstRoundInitiative,
    sr.RerollHitsVsHigherWS,
    sr.GrailVow,
    sr.MarkOfKhorne,
    sr.MarkOfNurgle,
    sr.MarkOfSlaanesh,
    sr.MarkOfTzeentch,
    sr.ArmourCannotBeImproved,
    sr.ArmourCannotBeModified,
    sr.CannotBeWoundedOn2,
    sr.EnemyRerollsArmourSaves,
    sr.EnemyRerollsHits,
    sr.EnemyRerollsWounds,
    sr.ImmuneToMultipleWounds,
    sr.NoArmourSaves,
    sr.PoisonedAttacks,
    sr.RerollFailedHits,
    sr.RerollFailedWounds,
    sr.RerollWounds1,
    sr.ArtilleryStrength,
    sr.BloodRage,
    sr.Choppas,
    sr.CleavingBlow,
    sr.ElvenReflexes,
    sr.EnsorcelledWeapons,
    sr.Ethereal,
    sr.FirstRoundOnly,
    sr.FirstRoundStr,
    sr.FlamingAttacks,
    sr.Flammable,
    sr.ForceRerollOneHit,
    sr.Frenzy,
    sr.FuriousCharge,
    sr.GromrilArmour,
    sr.GromrilWeapons,
    sr.ImmuneToKillingBlow,
    sr.ImproveArmor1InCombat,
    sr.IthilmarWeapons,
    sr.Khopesh,
    sr.Magic,
    sr.MagicalAttacks,
    sr.MonsterSlayer,
    sr.Murderous,
    sr.NoRegeneration,
    sr.ObsidianBlades,
    sr.PrimalFury,
    sr.RequiresTwoHands,
    sr.RerollArmourSaves1,
    sr.RerollHits1,
    sr.StrikeFirst,
    sr.StrikeLast,
    sr.WarpstoneWeapons,
    sr.WoundStealing,
}

# Rules that only mean something on a weapon profile, so putting them on a
# character is (correctly) a no-op. The "has an effect" probe skips these.
WEAPON_ONLY_RULES = {
    sr.ArtilleryStrength,
    sr.NoRegeneration,
    sr.FirstRoundOnly,
    sr.FirstRoundStr,
    sr.RequiresTwoHands,
}


def mount_scoped(rule: str) -> bool:
    """A rule a rider's or mount's entry gives to one mount: "Armour Bane (1, Chompa only)".

    mounted.apply_mount gives it to that mount's attacks alone, so on a plain
    fighter it does nothing.
    """
    from mounts import Mounts

    noted = re.fullmatch(r"(.+?) \((.+?), (.+?) only\)", rule)
    return bool(noted and noted.group(3) in Mounts
                and engine_reads(f"{noted.group(1)} ({noted.group(2)})"))


def engine_reads(rule: str) -> bool:
    """Whether the engine acts on this exact rule string."""
    if rule in ENGINE_RULES or mount_scoped(rule):
        return True
    if re.fullmatch(r"\+\d+A", rule):  # weapon extra attacks
        return True
    if sr.parse_fixed_strength([rule]) is not None:  # a weapon's own Strength
        return True
    if (sr.parse_to_hit_modifier([rule]) or sr.parse_enemy_to_hit_modifier([rule])
            or sr.parse_wounds_on([rule]) is not None
            or sr.parse_armour_piercing_bonus([rule])
            or sr.parse_impact_hits([rule]) or sr.parse_stomp_attacks([rule])
            or sr.parse_extra_attacks([rule]) or sr.parse_impact_hits_ap([rule])):
        return True
    if re.fullmatch(r"Hatred \((?!\s*\))(?!enemy wizards).+\)", rule, re.I):
        return True
    if (
        sr.parse_armour_bane([rule])
        or sr.parse_killing_blow([rule])
        or sr.parse_armour_bonus([rule])
        or sr.parse_regeneration([rule])
        or sr.parse_multiple_wounds([rule]) != 1
    ):
        return True
    try:
        return any(
            sr.parse_ward([rule], *flags) is not None
            for flags in ((False, False, False, False), (True, True, True, False),
                          (False, False, False, True))
        ) or any(
            sr.parse_ward([rule], strength=strength) is not None for strength in (1, 10)
        )
    except ValueError:  # a Ward with an unknown condition
        return False


# Named rule -> the parseable rule that must accompany it on the same model.
LABELS = {
    "Ancestral Shield": "Ward5",
    "Arcane Shield": "Ward5",
    "Blackshard Armour": sr.BlackshardArmour,
    "Blessed Knight": "Ward5",
    "Blessings of the Volcano God": "Ward4 (Flaming)",
    "Celestial Forged Armour (5+)": "Ward5",
    "Daemonic": sr.DaemonicWard,
    "Favour of the Goddess": "Ward5",
    "Talismanic Tattoos": "Ward6",
    "Born of Fire": "Ward3 (Flaming)",
    "Ghoulish Glamour": "Enemy Must Pass Leadership To Hit",
    # Unit rules
    "Blessings of Ulric": "Ward6 (Flaming)",
    "Blessings of the Horned Rat": "Ward5 (non-magical)",
    "Dark Runes": "Ward5 (non-magical)",
    "Daughters of Eternity": "Ward4",
    "Inner Circle": sr.RerollHits1,
    "Relentless Warriors": "Ward6 (non-magical)",
    "Runes of Protection": "Ward6 (non-magical)",
    "Runes of Warding": "Ward5 (Flaming)",
}

# Rule families FACTION_RULES names generically; the data carries them with a
# value ("Armour Bane (1)", "Regeneration (5+)"), which is what the engine reads.
FAMILIES = {
    "Armour Bane": "Armour Bane (1)",
    "Armoured Hide": "Armoured Hide (1)",
    "Chaos Armour (X+)": "Chaos Armour (5+)",
    "Hatred": "Hatred (all enemies)",
    "Regeneration": "Regeneration (5+)",
    "Impact Hits": "Impact Hits (D3)",
    "Impact Hits (X)": "Impact Hits (D3)",
    "Stomp Attacks": "Stomp Attacks (D3)",
    "Extra Attacks": "Extra Attacks (+D3)",
}

# Would affect a one-on-one melee duel; not modelled yet. Keep this honest -
# it is the engine's to-do list, and run_tests.py prints it.
NOT_SIMULATED = {
    # Extra attacks, hits and damage
    
    
    
    
    
    "Deathblow", "Slayer",
    "Killing Blow (Flammable units)",
    "Slayer of Daemons", "Slayer of Dragons", "The Wyrm Slayer", "Foe Render",
    "Precision Strikes", "Reroll Wounds (Beastmen Brayherds)",
    "Bull Charge", "Ogre Charge", "Daemonic Charge", "Two-headed Dragon",
    "Timmm-berrr!", "Tree Whack", "Syphoned Strength", "The Hunger",
    "Eternal Hatred", "Skilled Duellist", "Blood Greed",
    # Defence
    "Ithilmar Armour", "Mighty Constitution", "Parry",
    "Ancestral Grudge",  # Hatred of enemy characters; needs category matching
    "Feel No Pain", "Dwarf Crafted", "Free Full Plate Armour",
    "Chaos Armour",  # no value recorded on the Daemons of Chaos Daemon Prince
    "Aura of the Fay", "Aura of the Lady",
    "Shield of the Lady", "Beguiling Aura", "Cloud of Flies",
    "Harmony of Stone & Steel", "Immovable Object", "Scarab Prince",
    "Spirit of Galrauch", "Dark Vitality", "Motherly Love", "Slimy Shanks",
    "Indiscriminate Hunger", "Vampiric Powers", "Knightly Virtue",
    "Zealot",
    "Warpaint",  # rules text not transcribed; may be a Ward save
    # Rules scoped to a mount or alternate form the engine does not simulate
    "Blood Frenzy", "Wilful Beast", "Carrion Feeders", "Gorefeast", "Great Censer",
    "Sorcerous Miasma", "Random Attacks (Spirit Horde only)",
    "Stomp Attacks (D6) (Dragon Form only)",
}

# No bearing on a one-on-one melee duel.
INERT = {
    # Mount rules: spells, command range, shooting
    "Accursed Reliquary", "Blasphemous Tome", "Blessings of Khaine", "Borne Aloft",
    "Cloud of Dust", "Holy Fervour", "Mark of Chaos (as rider)", "Scrying Pool",
    "Symbol of Might", "Totem of Endless Bloodletting", "Witch Bane",
    # Movement, deployment and terrain
    "Ambushers", "Aquatic", "Chariot Runners", "Close Order", "Dig In!",
    "Entrenchment", "Eshin Infiltration", "Evasive", "Fast Cavalry",
    "Feigned Flight", "Fire & Flee", "First Charge", "Fly (8)", "Fly (9)",
    "Fly (10)", "Fly (9) (Dragon Form only)", "Forest Spites",
    "From Beneath the Sands", "Hidden", "Hit & Run", "Hostile Terrain",
    "Move Through Cover", "Open Order*", "Prepared Positions", "Scouts",
    "Scurry Away", "Skirmishers", "Stampede", "Swiftstride",
    "Swiftstride (Dragon Form only)", "Vanguard", "Counter Charge",
    "All Sneaky Like", "Running with the Pack",
    # Shooting and war machines
    "Accomplished Archers", "Arcane bodkins", "Arrows of Isha",
    "Artillery Master", "Deflect Shots", "Hagbane tips", "Hawk-eyed Archer",
    "Ignores Cover", "Improve Armor 2 in Shooting", "Master of Ballistics",
    "Moonfire shot", "Range Finding Optics", "Swiftshiver shards",
    "The Arrow of Kurnous", "Trueflight arrows", "Clouds of Soot & Smoke",
    "Forgefire", "Infernal Engineer", "Chainmaker",
    # Magic
    "Arcane Backlash", "Arcane Vassal", "Arise!", "Breath of Change",
    "Curse of the Necropolis", "Future Sight", "Hekarti's Blessing",
    "Incantation Scroll", "Incantation Scrolls", "Invocation of Nehek",
    "Lileath's Blessing", "Lore of Athel Loren", "Lore of Beasts",
    "Lore of Chaos", "Lore of Daemons", "Lore of Gork", "Lore of Hashut",
    "Lore of Lustria", "Lore of Mork", "Lore of Naggaroth",
    "Lore of Nehekhara", "Lore of Saphery", "Lore of Undeath", "Lore of Yang",
    "Lore of Yin", "Lore of the Great Maw", "Lore of the Horned Rat",
    "Lore of the Lady", "Magic Resistance (-1)", "Magic Resistance (-2)",
    "Magic Resistance (-3)", "Mastery of the Elemental Winds",
    "Mastery of the Storm Winds", "Prayer of the Damned", "Prayers of Sigmar",
    "Prayers of Ulric", "Rune Lore", "Sorcerer's Curse", "Stone Shaper",
    "Strike the Runes", "Transformation of the Dragon", "Untutored Arcanist",
    "Wailing Dirge", "Wrath of the Storm", "Grudgelore", "Da Troll Calla",
    "Leering Spirit", "Skaryn the Eye Thief",
    # Psychology, Leadership and combat result
    "Boldest of the Bold",
    "Lion Cloak",  # +1 armour against non-magical shooting only
    "Courage Beyond Compare", "Daemonic Instability", "Drunken", "Fear",
    "Fear of Elves", "Hold the Line!", "Ignore Goblin Panic", "Ignore Panic",
    "Immune to Psychology", "Impetuous", "Indomitable (1)", "Indomitable (2)",
    "Indomitable (3)", "Infernal Favour (1)", "Infernal Favour (2)", "Loner",
    "Mob Rule", "Pure of Heart", "Quell Impetuosity", "Resolute", "Stubborn",
    "Stupidity", "Terror", "Terror (Dragon Form only)", "Unbreakable",
    "Unstable", "Valour of Ages", "Verminous Valour", "Veteran", "Warp-spawned",
    "Cold Blooded", "Dry as Dust", "Necromantic Undead", "Nehekharan Undead",
    "Herald of Despair", "Drilled", "Levies", "Peasantry", "Peasant's Duty",
    "Settra Does Not Kneel!", "Suffer Not...", "Slaughterer's Call",
    # Command, army composition and challenges
    "Banner of the Count", "Banner of the King", "Big Name",
    "Brayhorn (General only)", "Bull-gors", "Butcher's Cauldron",
    "Commander & Captain", "Commander of Legions", "Commanding Voice",
    "Da Boyz", "Discipline of the Old Ones", "Disdain of the Dragons",
    "Eternal Taskmaster", "Father of Beasts", "Gaze of the Gods",
    "Goad Beast", "Grand Master of the Knights Panther", "Grand Strategist",
    "Guardian of the Sacred Sites", "Handler", "Immortal Overseer",
    "King of the Slayer Hold", "Large Target",
    "Large Target (Dragon Form only)", "Master of Battle",
    "Mercenary Commander", "My Will Be Done", "Naval Discipline",
    "Peerless Raider", "Protect Da Boss", "Rallying Cry",
    "Rallying Cry (Human Form only)", "Settra the Great", "Settra's Champion",
    "Stand Back Chief", "Strategic Mastery", "Supreme Matriarch of Nan-Gau",
    "Sworn Protector", "The Exile's Vow", "The Knight's Vow",
    "The Questing Vow", "The Sons of Ghorros", "Tree Spirit",
    "Troubadour of Loec", "Waaagh!", "Warband", "Wight Banner",
    "Will of the Dragons", "Backstab", "Usirian's Reaper",
    "Daemon of Nurgle", "Daemon of Slaanesh", "Daemon of Tzeentch",
    "Daemons of Khorne",
    # Marks of Chaos carry no duel effect of their own in this edition's data
    "Mark of Chaos Undivided",
}


# -- Regular units ------------------------------------------------------------

NOT_SIMULATED |= {
    # Attacks the engine cannot count or resolve yet
    "Extra Attacks (+remaining Wounds)",
    "Random Attacks", "Random Attacks (Rats only)",
    "Random Attacks (The Restless Dead only)",
    
    
    "Impact Hits (D6+1, Chariot only)", "Impact Hits (D6+1, War Wagon only)",
    
    
    "Abominable Attacks", "Bonegrinder Giant Attacks", "Giant Attacks",
    "Pick Up And…", "Swallow Whole", "Unstoppable Assault",
    "Blazing Body", "Stony Stare", "Spurting Bile Blood",
    "Brazen Wheels", "Crushing Bulk", "Crushing Weight", "Grinding Wheels",
    "Crown of Antlers", "Mournfang Charge", "Spiked Ball & Chains",
    "Thunderous Charge", "Whirlwind of Death",
    # Characteristic changes and rerolls in combat
    "Bestial Charge", "Slavering Charge", "Razor Tusks", "Tusker Charge",
    "Stoic Defenders", "Martial Prowess", "Guardians of the Wildwood",
    "Ghostsight", "Soul Reaper", "Defensive Stance",
    "Blizzard Aura", "Enfeebling Cold", "Numbing Chill", "Soporific Musk",
    "Blessing of Chaos", "Rampant Mutation", "Warped Form", "Dances of Loec",
    "Strike First (against chargers)",
    # Defence
    "Stone Skeleton", "Fire & Chaos", "Warpfire Aura", "Spectral Coach",
    "Blessings of the Lady (Grail Reliquae)",
    "Multiple Wounds (D3, against monsters)",
    # Rules that belong to one part of a split profile (a mount, the crew)
    "Armour Bane (1 Razorgor only)", "Armour Bane (1, Chracian Lions only)",
    "Armour Bane (1, Cold One only)", "Armour Bane (1, Gorebeast only)",
    "Armour Bane (2, Rat Ogre only)",
    "Armour Bane (2, Rhinox only)", "Armour Bane (2, Rot Fly only)",
    "Armour Bane (2, claws and fangs only)",
    "Armour Bane (3, Pump Wagon Impact Hits only)",
    "Bestial Charge (Gors only)", "Blessings of Grimnir (Shrine Keeper only)",
    "Cleaving Blow (Riders only)",
    "Cleaving Blow (Ripperdactyl only)", "Cleaving Blow (Tomb Guard Crew only)",
    "Elven Reflexes (Crew only)", "Foe Render (Razorgor only)",
    "Furious Charge (Black Orc Crew only)", "Furious Charge (Gors only)",
    "Furious Charge (Riders only)", "Furious Charge (Ripperdactyl only)",
    "Khopesh (Tomb Guard Crew only)", "Killing Blow (Gorebeast only)",
    "Poisoned Attacks (Necroserpent only)", "Poisoned Attacks (Riders only)",
    "Poisoned Attacks (Steed of Slaanesh only)",
    "Poisoned Attacks (javelins only)",
}

INERT |= {
    # Weapon markers and weapon rules with no duel meaning
    "Secondary Attack", "Fight in Extra Rank", "Quick Shot",
    # Formation, movement and deployment
    "Open Order", "Horde", "Howdah", "Detachment", "Regimental Unit",
    "Motley Crew", "Motley Crew*", "Mixed Unit", "Reserve Move", "Shieldwall",
    "Lance Formation", "Dispersed Formation", "Fly (7)", "Disengage",
    "Dragged Along", "Carriage Hauler", "Lumbering Destruction", "Steam Power",
    "Temperamental", "Random Movement", "Ker-splat", "Finest Warhorses",
    "First to the Fray", "Ravenous Hunger", "Implacable", "Traps & Snares",
    "Skirmish Screen", "Skulking Menace", "Deploying Weapon Teams",
    "Cathayan Cataphracts", "Leader of the Pack", "Run with the Pack",
    "Squigs Go Wild", "Ithilmar Barding", "Monster Handlers", "Toad Rage",
    # Shooting, war machines and flying attacks
    "Arrows of Asaph", "Abyssal Cloak", "Beast Handlers", "Safe from Harm",
    "Sea Dragon Cloak", "Stable Firing Platform", "Steadfast Discipline",
    "Targeting Weapon Teams", "Eye of the Dragon", "Doom Diver", "Caged Fury",
    "Bombing Run", "Dive Bomb", "Drop Rocks", "Slashing Attack",
    "Slashing Attack (Screamers only)", "Spectral Reapers", "Wake of Fire",
    "Zzzzap!", "Enough for Everyone", "Mercenary Crew", "Bully",
    # Magic
    "Covenant of Power", "Vortex of Souls", "Cursed Coven", "Deepwood Coven",
    "Scintillating Sorcery", "Storm Call", "Soul-eater", "The Quickening Storm",
    "Lore of Daemons (Exalted Flamer only)", "Tolling the Bell",
    # Leadership, psychology, combat result and challenges
    "Abyssal Howl", "Maddening Aura", "Endless Malice", "Primeval Roar",
    "Heavenly Beacon", "Venerable", "Quell Panic", "Largely Insignificant",
    "Scurrying Masses", "Weapon Team Leadership", "Bound Spirits",
    "Bestial Fury", "Impervious Defence", "Slime Trail", "Dance of Death",
    "Attention Seeker", "Champions of Chrace", "King's Guard", "Living Saints",
    "Martial Pride", "Royal Guard", '"Fight Me!" (Giant Slayers only)',
    "Infernal Favour (1, Exalted Flamer only)",
    # Death throes: they strike only once this model is already dead
    "Explosive Demise", "Infested", "Too Horrible to Die", "From the Ashes",
    "Unbound Spirits",
    # Army composition, joining and scoring
    "Chracian Warriors", "Sons of Caledor", "Warriors of Nagarythe",
    "Warriors of the White Tower", "Fanatical Zeal", "Guardians",
    "Mercenaries", "Nuln State Troops", "Doomseeker", "The Newly Dead",
    "Grail Reliquae", "Retinue of the Saints (Grail Reliquae)",
    "Daemon of Khorne", "Daemons of Nurgle", "Daemons of Slaanesh",
    "Daemons of Tzeentch",
    # Unit upgrades offered as options. Optional rules are never applied to a
    # profile, and most have no rules page of their own.
    "Ark of Sotek", "Balefire Brazier", "Big 'Uns", "Big Stabbas",
    "Blessed Triptych", "Chaos Mutations", "Chaotic Cult", "Chaotic Trait",
    "Chaotic Traits", "Cult of the Bloodied Hound", "Cult of the Carrion Crow",
    "Cult of the Fell Raptor", "Cult of the Slithering Serpent",
    "Daemonic Gifts", "Daemonic Icon", "Engine of the Gods",
    "Engineering runes", "Forsaken by Khorne", "Forsaken by Nurgle",
    "Forsaken by Slaanesh", "Forsaken by Tzeentch",
    "Gigantic Spawn of Khorne", "Gigantic Spawn of Nurgle",
    "Gigantic Spawn of Slaanesh", "Gigantic Spawn of Tzeentch", "Grail Monk",
    "Granite Sentinel", "Guardians of the Temple", "Hellbound",
    "Implacable Defence", "Jade Sentinel", "Look-out Gnoblar",
    "Nehekharan Phalanx", "Netters", "Obsidian Sentinel", "Pigeon bombs",
    "Plague Proboscis", "Skullcracker", "Skulls of the Foe", "Solar Engine",
    "Spawn of Khorne", "Spawn of Nurgle", "Spawn of Slaanesh",
    "Spawn of Tzeentch", "Standard runes", "Steam Carriage",
    "Talismanic runes", "Terracotta Sentinel", "Warped Tintinnabulation",
    "Warpstone Sentinel", "Weapon runes", "burning braziers",
    "defensive stakes", "runic tattoos",
}


def classify(rule: str) -> str | None:
    """'engine', 'label', 'not simulated', 'inert', or None if unaccounted for."""
    if engine_reads(rule):
        return "engine"
    if rule in LABELS:
        return "label"
    if rule in NOT_SIMULATED:
        return "not simulated"
    if rule in INERT:
        return "inert"
    return None


def rule_sources():
    """{rule string: sorted list of places it appears}."""
    from elven_honors import ElvenHonors
    from faction_profiles import FactionProfiles
    from magic_items import MagicItemDict
    from weapons import MeleeWeaponDict

    found = {}

    def add(rule, where):
        found.setdefault(rule, set()).add(where)

    for faction, profiles in FactionProfiles.items():
        for name, entry in profiles.items():
            base = entry["base_profile"]
            for rule in (base.get("SpecialRules") or []) + (base.get("OptionalRules") or []):
                add(rule, f"{faction}/{name}")
    for names, data in MeleeWeaponDict.items():
        for rule in data[2] or []:
            add(rule, f"weapon {names[0]}")
    for name, item in MagicItemDict.items():
        for rule in item.get("rules") or []:
            add(rule, f"item {name}")
    for name, honour in ElvenHonors.items():
        for rule in honour["special_rules"]:
            add(rule, f"honour {name}")
    from mounts import Mounts

    for name, mount in Mounts.items():
        for rule in mount.get("SpecialRules") or []:
            add(rule, f"mount {name}")
    return {rule: sorted(where) for rule, where in found.items()}
