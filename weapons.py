from __future__ import annotations

from faction_profiles import *
from special_rules import *

# Special rules can include: "+1A" for +1 Attack
MeleeWeaponDict = {
    ("HW", "Hand Weapon", "HandWeapon"): [None, 0, None],  # Hand Weapon, no strength bonus, no armor piercing, no special rules
    ("Two Hand Weapons", "2xHW", "2HW"): [None, 0, ["+1A", RequiresTwoHands]],  # Two Hand Weapons, no strength bonus, no armor piercing, +1 Attack
    ("Flail",): [2, -2, [FirstRoundStr, RequiresTwoHands]],  # Flail, +2 Strength, -2 Armor Piercing, First Round Strength only, Requires Two Hands. The site also gives Armour Bane (1) on the charge only; Armour Bane cannot be gated to the first round yet, so it is left off
    ("Great Weapon", "GW", "GreatWeapon"): [2, -2, [StrikeLast, "AB1",RequiresTwoHands]],  # Great Weapon, +2 Strength, -2 Armor Piercing, Armour Bane 1, Strike Last
    ("Halberd",): [1, -1, ["AB1", RequiresTwoHands]],  # Halberd, +1 Strength, -1 Armor Piercing, Armour Bane 1
    ("Morning Star", "MorningStar","Morningstar"): [1, -1, [FirstRoundStr]],  # Morning Star, +1 Strength, -1 Armor Piercing, First Round Strength only. Armour Bane (1) on the charge only is left off, as for the Flail
    ("Whip",): [None, 0, [StrikeFirst]],  # Whip, Strike First
    ("Lance",): [2, 2, [FirstRoundOnly, "AB1"]],  # Lance, +2 Strength, +2 Armor Piercing, Armour Bane 1, First Round Only
    ("Cavalry Spear", "CavSpear", "CavalrySpear"): [1, -1, [FirstRoundOnly]],  # Cavalry Spear, +1 Strength, -1 armor piercing, First Round Only
    ("Throwing Spears", "ThrowingSpear"): [None, 0, [FirstRoundOnly]],  # Throwing Spears, No strength, no armor piercing, First Round Only
    ("Thrusting Spear", "ThrustingSpear", "Spear"): [None, 0, None],  # Thrusting Spear, no strength bonus, no armor piercing, no special rules
    ("Chayal",):[2,-3,[KillingBlow,RequiresTwoHands,Magic,RerollHits1]], # Chayal, +2 Strength, -3 Armor Piercing, Killing Blow, Requires Two Hands, Magic, Reroll Hits of 1
    ("Mathlann's Ire", "MathlannsIre"):[1,-2,["AB1",Magic,ForceRerollOneHit]], # Mathlann's Ire, +1 Strength, -2 Armor Piercing, Armour Bane 1, Magic, enemies reroll one successful hit
    ("Sword of Hoeth", "SwordofHoeth"):[2,-2,[Magic,RequiresTwoHands]], # Sword of Hoeth, +2 Strength, -2 Armor Piercing, Magic
    ("Handmaiden's Spear", "HandmaidensSpear"): [None, 0, [FirstRoundOnly]],  # Handmaiden's Spear, treated as a thrown/thrusting spear
    ("Ceremonial Halberd", "CeremonialHalberd"): [1, -1, ["AB1", Magic, RequiresTwoHands]],  # Ceremonial Halberd, +1 Strength, -1 Armor Piercing, Armour Bane 1, Magic
    ("Mansmasher",): [1, -1, [Magic, FirstRoundStr]],  # Mansmasher, +1 Strength on the charge round only, -1 Armor Piercing
    ("Darkforged Weapon", "DarkforgedWeapon"): [None, -1, None],  # Darkforged weapon, -1 Armor Piercing (Chaos Dwarf craftsmanship)
    # A Braystaff is used offensively (as a great weapon) or defensively (as a
    # hand weapon that gives an armour value of 5+), chosen each round.
    ("Braystaff", "Bray Staff", "Braystaff (Offensive)"): [2, -2, [StrikeLast, "AB1", RequiresTwoHands]],
    ("Braystaff (Defensive)",): [None, 0, None],  # also armour value 5+: pass Armor="Heavy Armor"
    ("Grisly Totem", "GrislyTotem"): [2, -2, [StrikeLast, "AB1", RequiresTwoHands]],  # Kralmaw's Braystaff, used offensively
    ("Judgement",): [2, -2, [MagicalAttacks, "Multiple Wounds (2)", RequiresTwoHands]],  # Judgement, +2 Strength, -2 Armor Piercing, Magical Attacks, Multiple Wounds (2), Requires Two Hands
    ("Beast Reaver", "BeastReaver"): [1, -1, [Magic, "Reroll Wounds (Beastmen Brayherds)"]],  # Beast Reaver, +1 Strength, -1 Armor Piercing, rerolls failed wounds vs Beastmen
    ("Axe of Dargo", "AxeOfDargo"): [2, -3, [Magic]],  # Axe of Dargo, +2 Strength, -3 Armor Piercing
    ("Grudge-Settler", "GrudgeSettler"): [2, -1, ["AB1", MagicalAttacks]],  # Grudge-Settler, +2 Strength, -1 Armor Piercing, Armour Bane 1, Magical Attacks (inscribed with the Master Rune of Smiting and the Rune of Parrying, which are not modelled)
    ("Furnace Hammer", "FurnaceHammer"): [None, -2, [FlamingAttacks, ArtilleryStrength]],  # Furnace Hammer, Strength rolled on an Artillery dice, -2 Armor Piercing, Flaming Attacks
    ("Storm's Wrath", "StormsWrath"): [2, -1, [Magic, FirstRoundStr]],  # Storm's Wrath, +2 Strength (charge round only), -1 Armor Piercing, Magic
    ("Da Skull Smasha", "DaSkullSmasha", "Da Skull Smasha (Hammer)"): [2, -1, [Magic]],  # Da Skull Smasha, hammer profile: +2 Strength, -1 Armor Piercing
    ("Da Skull Smasha (Pick)", "DaSkullSmashaPick"): [None, -2, [Magic]],  # Da Skull Smasha, pick profile: no Strength bonus, -2 Armor Piercing
    ("Bog-wood Staff", "BogwoodStaff"): [2, -1, [Magic, WoundStealing]],  # Bog-wood Staff, +2 Strength, -1 Armor Piercing, recovers a Wound per unsaved Wound
    ("Chracian Great Blade", "ChracianGreatBlade"):[2,-3,[RequiresTwoHands,StrikeLast]], # Chracian Great Blade, +2 Strength, -3 Armor Piercing, Requires Two Hands, Strike Last

    # Weapons from the later army lists. Profiles from https://tow.whfb.app,
    # read from each weapon's rules page. Rules the engine cannot use yet
    # (dice-valued Extra Attacks, Poisoned Attacks, Monster Slayer) are kept
    # verbatim so nothing is lost when they are implemented.
    ("Celestial Blade", "CelestialBlade"): [1, -1, [StrikeFirst]],  # Grand Cathay
    ("Cathayan Lance", "CathayanLance"): [1, -1, [FirstRoundStr, "AB1"]],  # Grand Cathay; its S and AP modifiers apply only against models it charged, and only cavalry, monsters and chariots may use one
    ("Iron Talons", "IronTalons"): [None, -1, [StrikeFirst]],  # Shugengan, Grand Cathay
    ("Ironfist",): [None, 0, ["+1A", RequiresTwoHands]],  # Ogre Kingdoms; also improves armour by 1 (not modelled), and neither bonus applies alongside a magic weapon
    ("Plague Censer", "PlagueCenser"): [2, -1, [FirstRoundStr, "Poisoned Attacks", RequiresTwoHands]],  # Skaven; S+2 in the first round only, and rerolls To Wound rolls of 1 in combat (not modelled)
    ("Spectral Scythe", "Spectral Scythe (Cairn Wraith)"): [None, -6, [MagicalAttacks, "Multiple Wounds (D3)"]],  # Vampire Counts; AP 'N/A' - no armour save is permitted, which AP -6 guarantees
    ("Asrai Spear", "AsraiSpear"): [None, -1, None],  # Wood Elf Realms
    ("Spear of Loec", "SpearOfLoec"): [1, -1, ["Armour Bane (2)", KillingBlow]],  # Shadowdancer, Wood Elf Realms
    ("Trickster's Blades", "Tricksters Blades"): [None, 0, ["Extra Attacks (+D3)", RequiresTwoHands]],  # Shadowdancer; the +D3 Attacks are not modelled yet
    ("Oaken Fists", "OakenFists"): [None, -2, None],  # Treeman Ancient, Wood Elf Realms

    # Named characters' magic weapons (Arcane Journal / army list profiles).
    ("Talons of the Storm", "TalonsOfTheStorm"): [None, -2, ["AB1", Magic, MagicalAttacks, StrikeFirst]],  # Miao Ying
    ("Sorrow's End", "Sorrows End"): [1, -1, [Magic, MagicalAttacks, "Monster Slayer", "Multiple Wounds (2)"]],  # Sir Cecil Gastonne
    ("The Dolorous Blade", "Dolorous Blade", "The Dolorous Blade (Deadly Blows)"): [2, -1, ["AB1", Magic, MagicalAttacks, "Multiple Wounds (2)"]],  # The Green Knight, Deadly Blows profile
    ("The Dolorous Blade (Rapid Strikes)",): [None, -1, ["Extra Attacks (+D6)", Magic, MagicalAttacks]],  # The Green Knight, Rapid Strikes profile; the +D6 Attacks are not modelled yet
    ("Dragonblade",): [2, -2, ["AB1", Magic, MagicalAttacks]],  # Prince Ulther; its Rune of Fury and Grudge Rune are not modelled
    ("The Flail of Conquered Kings", "Flail of Conquered Kings"): [2, -2, [FirstRoundStr, Magic, MagicalAttacks, "Multiple Wounds (2)", RequiresTwoHands]],  # Nekaph; S+2 only against models he charged
    ("The Blessed Blade of Ptra", "Blessed Blade of Ptra"): [None, -3, [FlamingAttacks, Magic, MagicalAttacks, RequiresTwoHands]],  # Settra; a model it wounds suffers -1 To Hit for the rest of the game (not modelled)
    ("Spear of Talsyn", "SpearOfTalsyn"): [None, -1, ["AB1", Magic, MagicalAttacks]],  # Araloth
    ("The Spear of Kurnous", "Spear of Kurnous"): [1, -2, [Magic, MagicalAttacks, "Multiple Wounds (D3)"]],  # Orion, combat profile

    # Common magic weapons from the rulebook. "Magic" marks each as a magic
    # weapon (so hand-weapon rules and Choppas do not apply), "Magical
    # Attacks" is the rule the profile itself grants.
    ("Berserker Blade",): [1, 0, ["+1A", "Impetuous", Magic, MagicalAttacks]],
    ("Biting Blade",): [None, -2, ["AB1", Magic, MagicalAttacks]],
    ("Burning Blade",): [None, 0, [FlamingAttacks, Magic, MagicalAttacks]],
    ("Diestro's Blade", "Diestros Blade"): [None, -1, [Magic, MagicalAttacks]],  # also +1 Initiative (not modelled)
    ("Dragon Slaying Sword",): [None, 0, [Magic, MagicalAttacks, "Monster Slayer"]],
    ("Duellist's Blades", "Duellists Blades"): [None, -1, ["+2A", Magic, MagicalAttacks, RequiresTwoHands]],
    ("Giant Blade",): [1, 0, ["Armour Bane (2)", Magic, MagicalAttacks, "Multiple Wounds (2)"]],
    ("Headsman's Axe", "Headsmans Axe"): [1, -1, [KillingBlow, Magic, MagicalAttacks, RequiresTwoHands]],
    ("Ogre Blade",): [2, -2, ["AB1", Magic, MagicalAttacks, "Multiple Wounds (D3)"]],
    ("Skirmisher's Blade", "Skirmishers Blade"): [None, -1, ["+1A", Magic, MagicalAttacks]],
    ("Spelleater Axe",): [None, -1, [Magic, MagicalAttacks, "Magic Resistance (-2)"]],
    ("Sword of Battle",): [1, -1, ["AB1", "+1A", Magic, MagicalAttacks]],
    ("Sword of Might",): [1, -1, [Magic, MagicalAttacks]],
    ("Sword of Striking",): [None, 0, [Magic, MagicalAttacks]],  # also +1 To Hit in combat (not modelled)
    ("Sword of Swiftness",): [None, 0, [Magic, MagicalAttacks, StrikeFirst]],
    ("Thornspitter Stave",): [1, 0, ["AB1", Magic, MagicalAttacks]],  # combat profile
    ("Trailblazer's Hatchet", "Trailblazers Hatchet"): [1, -1, [FlamingAttacks, Magic, MagicalAttacks, MoveThroughCover]],
    
    # Unit and monster weapons, drafted by tools/transcribe_weapons.py from each
    # weapon's rules page. "Secondary Attack" marks a weapon used for one extra
    # attack (or one of several) each turn - a tail, a maw, Troll Vomit - which
    # is never a unit's default weapon. "Strength (N)" is a weapon with its own
    # Strength. Rules the engine does not use yet are kept verbatim.
    ('Bilesword',): [None, -2, ['Armour Bane (1)', 'Strike Last', 'No Regeneration Saves']],  # Regeneration saves are not permitted against wounds caused by this weapon (armour and Ward saves can be attempted as normal).
    ('Bloodflail',): [2, -2, ['1st round strength only', 'Armour Bane (1)', 'Multiple Wounds (D3)']],  # A Bloodflail's Strength modifier applies only during the first round of combat.
    ("Bonegrinder Giant's Club", 'Bonegrinder Giants Club'): [None, 0, []],  # Strength '*' has no fixed value; AP '*' has no fixed value
    ('Brass Bound Hooves',): [None, -2, []],
    ('Cavernous Maw',): [None, -2, ['Armour Bane (1)', 'Killing Blow', 'Secondary Attack']],  # In combat, this model must make one of its attacks each turn with this weapon.
    ('Cleaver-limbs',): [None, -2, ['Killing Blow', 'Monster Slayer']],
    ('Cleaving Blades',): [None, -1, ['Killing Blow']],
    ('Colossal Fang-filled Gob',): [None, -2, ['Killing Blow']],
    ('Crown of Horns (Grand Cathay)',): [None, -1, ['Armour Bane (1)']],
    ('Daemonic Talons',): [None, -1, []],
    ('Decapitating Claws',): [None, -2, ['Killing Blow', 'Monster Slayer']],
    ('Decapitating Strike',): [5, -4, ['Killing Blow', 'Monster Slayer', 'Strike Last', 'Secondary Attack']],  # This model may make one additional attack each turn with this weapon.
    ('Distensible Jaw',): [None, 0, ['Killing Blow', 'Secondary Attack']],  # In combat, this model must make one of its attacks each turn with this weapon.
    ('Doom-Flayer',): [None, -1, ['Strength (4)', 'Counter Charge', 'Extra Attacks (+D6)', 'Impact Hits (D6+1)']],  # Impact Hits caused by this weapon have an Armour Piercing characteristic of -2.
    ('Dread Halberd',): [1, -1, ['Armour Bane (1)', 'Fight in Extra Rank', 'Requires Two Hands']],  # A model wielding a dread halberd cannot make a supporting attack during a turn in which it charged.
    ('Ensorcelled Weapon',): [None, -1, []],
    ('Envenomed Sting',): [None, 0, ['Poisoned Attacks', 'Strike First', 'Secondary Attack']],  # In combat, this model may choose to make one of its attacks each turn with this weapon.
    ('Fiend Tail',): [None, -1, ['Extra Attacks (+D3)', 'Secondary Attack']],  # In combat, a Chimera with a fiend tail may make an additional D3 attacks each turn, each of which must be made with this weapon.
    ('Filth-Encrusted Claws',): [None, -1, ['Poisoned Attacks']],
    ('Filth-Encrusted Talons',): [None, -1, ['Armour Bane (1)', 'Poisoned Attacks']],
    ("Giant's Club", 'Giants Club'): [None, 0, []],  # Strength '*' has no fixed value; AP '*' has no fixed value
    ('Gnashing Maws',): [None, -2, ['Strike Last', 'Secondary Attack']],  # In combat, this model may choose to make one of its attacks each turn with this weapon. For each Wound an enemy unit loses as a result of an attack made with th...
    ('Goring Horns',): [1, -3, ['Flaming Attacks', 'Strike First', 'Secondary Attack']],  # In combat, this model may make one of its attacks each turn with this weapon.
    ('Great Axe',): [2, -3, ['Armour Bane (2)', 'Monster Slayer', 'Requires Two Hands', 'Strike Last']],
    ('Great Hammer',): [2, -2, ['Armour Bane (2)', 'Magical Attacks', 'Requires Two Hands']],
    ('Great Horns',): [None, -3, []],
    ('Great Tusks',): [None, -1, ['Armour Bane (2)']],
    ('Grimfrost Weapon',): [None, -1, ['Armour Bane (1)', 'Magical Attacks']],
    ('Gromril Great Axe',): [2, -3, ['Requires Two Hands', 'Strike Last']],
    ('Har Ganeth Greatsword',): [2, -1, ['Cleaving Blow', 'Requires Two Hands']],
    ('Hellblade',): [None, -1, ['Cleaving Blow']],
    ('Horns of Stone',): [None, -2, []],
    ('Huge Gob',): [None, -1, ['Armour Bane (1)']],
    ('Hunting Spear',): [1, -2, ['First Round Only', 'Armour Bane (1)']],  # A hunting spear can only be used during a turn in which the wielder charged. In subsequent turns (or if the wielder did not charge) the model must use its hand ...
    ('Impaling Claws',): [None, -2, ['Killing Blow', 'Strike First']],
    ('Iron Claw',): [None, -3, ['Killing Blow']],
    ("Lamprey's Bite", 'Lampreys Bite'): [None, -1, ['Multiple Wounds (D3, against monsters)']],  # The Multiple Wounds (D3) special rule only applies against enemy models whose troop type is monster.
    ('Lash & Buckler', 'Lash and Buckler'): [None, -1, ['Armour Bane (1)', 'Fight in Extra Rank', 'Requires Two Hands']],  # A model equipped with a lash & buckler improves its armour value by 1.
    ('Lash of Khorne',): [None, -2, ['Armour Bane (1)', 'Strike First']],
    ('Lashing Talons',): [None, -1, ['Armour Bane (1)']],
    ('Long Spear',): [None, 0, ['Fight in Extra Rank', 'Strike First (against chargers)']],  # Models whose troop type is infantry only. A model wielding a long spear cannot make a supporting attack during a turn in which it charged. A long spear's Strike...
    ('Mace Tail',): [1, -2, ['Secondary Attack']],  # A Lammasu may make one additional attack each turn with this weapon.
    ('Monstrous Tusks',): [None, -1, ['Armour Bane (1)']],
    ('Paired Great Khopeshes',): [None, -2, ['Killing Blow', 'Requires Two Hands']],
    ('Piercing Claws',): [None, -1, ['Armour Bane (2)', '+1A', 'Requires Two Hands']],
    ('Plagueflail',): [2, -3, ['1st round strength only', 'Multiple Wounds (D3)']],  # A Plagueflail's Strength modifier applies only during the first round of combat.
    ('Plaguesword',): [None, 0, ['Armour Bane (1)', 'No Regeneration Saves']],  # Regeneration saves are not permitted against wounds caused by this weapon (armour and Ward saves can be attempted as normal).
    ('Poisonous Tail',): [None, 0, ['Poisoned Attacks', 'Strike First', 'Secondary Attack']],  # In combat, this model may make one of its attacks each turn with this weapon.
    ('Polearm Single-Handed',): [None, 0, ['Fight in Extra Rank']],  # A polearm has two profiles. You must choose which the unit will use when its combat is chosen during Step 1.1 of the Choose & Fight Combat sub-phase. A model wi...
    ('Rancid Maw',): [None, -2, ['Armour Bane (1)', 'Multiple Wounds (2)', 'Secondary Attack']],  # In combat, this model must make one of its attacks each turn with this weapon.
    ("Ranger's Glaive", 'Rangers Glaive'): [2, -2, ['Requires Two Hands']],
    ('Ritual Blade',): [2, -3, ['Requires Two Hands', 'Strike Last']],
    ('Scything Blow',): [None, -2, ['Armour Bane (1)', 'Extra Attacks (+2D3)', 'Strike Last']],  # This weapon has two profiles, representing the different ways it can be used in combat. You must choose which profile the wielder will use at the start of each ...
    ('Serpentine Tail',): [2, -2, ['Strike Last', 'Secondary Attack']],  # In combat, this model must make one of its attacks each turn with this weapon.
    ('Serrated Maw',): [None, 0, ['Armour Bane (2)', 'Multiple Wounds (2)', 'Secondary Attack']],  # In combat, this model must make one of its attacks each turn with this weapon. If this model has Two Heads, it must make two of its attacks each turn with this ...
    ('Serrated Maws',): [None, 0, ['Armour Bane (1)', 'Multiple Wounds (2)', 'Secondary Attack']],  # In combat, this model must make each attack granted by the Extra Attacks (+remaining Wounds) special rule with this weapon.
    ('Slashing Talons',): [None, -1, []],
    ('Slashing Talons (Lizardmen)',): [None, -3, ['Multiple Wounds (D3, against monsters)']],  # The Multiple Wounds (D3) special rule only applies against enemy models whose troop type is monster.
    ('Spectral Scythe (Black Coach)',): [None, -6, ['Magical Attacks']],  # AP 'N/A': no armour save is permitted, which AP -6 guarantees
    ('Steam Drill',): [3, -3, ['Furious Charge', 'Requires Two Hands', 'Strike Last']],  # A unit of Miners held in reserve that includes a Prospector equipped with a steam drill may re-roll the D6 when rolling to determine if they arrive on the battl...
    ('Things-catcher',): [None, -1, ['Fight in Extra Rank', 'Killing Blow', 'Requires Two Hands']],
    ('Throwing Spear',): [None, 0, ['First Round Only', 'Fight in Extra Rank']],  # A throwing spear can only be used during a turn in which the wielder charged. In subsequent turns (or if the wielder did not charge) the model must use its hand...
    ('Thunderous Bludgeon',): [None, -3, ['Strike Last']],
    ('Trampling Hooves',): [None, -1, ['Flaming Attacks']],
    ('Troll Vomit',): [None, -2, ['Strength (3)', 'Secondary Attack']],  # A Troll that is in base contact with an enemy model may make one additional attack each turn with this weapon. This attack must be made last, after all other at...
    ('Twisted Antlers',): [None, -2, ['Armour Bane (1)']],
    ('Venom Sting',): [None, -1, ['Armour Bane (1)', 'Secondary Attack']],  # In combat, a Rot Fly makes one of its attacks each turn with this weapon.
    ('Venom Surge',): [None, -2, ['Multiple Wounds (D6)', 'Poisoned Attacks', 'Strike First', 'Secondary Attack']],  # In combat, this model may choose to make one of its attacks each turn with this weapon.
    ('Venomous Tail',): [None, 0, ['Poisoned Attacks', 'Strike First']],
    ('Venomous Talons',): [None, -2, ['Poisoned Attacks']],
    ('Warp Grinder',): [None, -3, ['Strength (5)', 'Ambushers', 'Killing Blow', 'Requires Two Hands']],  # If a Weapon Team is equipped with a Warp Grinder, both it and its parent unit gain the Ambushers special rule.
    ('Warpstone Claws',): [None, -1, ['Armour Bane (1)', 'Magical Attacks']],
    ('Wicked Claws',): [None, -2, []],
    ('Wolf Hammer',): [1, -2, ['Requires Two Hands']],  # If the wielder of a wolf hammer uses it during a turn in which they made a charge move of 3" or more, they have a +2 modifier to their Strength characteristic, ...
    ('Writhing Tail',): [None, -1, ['Extra Attacks (+D3)', 'Secondary Attack']],  # In combat, a Sepulchral Stalker may make an additional D3 attacks each turn, each of which must be made with this weapon (roll separately for each model in the ...
    ('Writhing Tentacles (Daemons of Chaos)',): [None, -1, ['Armour Bane (1)']],
    ('Writhing Tentacles (Dark Elves)',): [None, -2, ['Poisoned Attacks']],
}

# Magic weapons transcribed from every magic-item page. Hand-entered profiles
# above take precedence; a site profile is only added under a new name.
def _merge_site_weapons():
    from magic_items_data import SITE_ITEM_WEAPONS

    known = {name.lower() for key in MeleeWeaponDict for name in key}
    for name, profile in SITE_ITEM_WEAPONS.items():
        plain = name[4:] if name.lower().startswith("the ") else name
        if name.lower() in known or plain.lower() in known:
            continue
        aliases = tuple(dict.fromkeys(n for n in (name, plain) if n))
        MeleeWeaponDict[aliases] = list(profile)
        known.update(a.lower() for a in aliases)


_merge_site_weapons()


def find_weapon_key(weapon):
    """Return the MeleeWeaponDict key tuple that contains the given weapon name, or None."""
    for key in MeleeWeaponDict:
        if weapon in key:
            return key
    return None


def get_weapon_stats(weapon, raise_on_missing=True):
    """Return (strength_bonus, armour_piercing, special_rules) for a weapon name.
    If raise_on_missing is True, raise ValueError when weapon not found.
    """
    key = find_weapon_key(weapon)
    if key is None:
        if raise_on_missing:
            raise ValueError(f"Weapon '{weapon}' not found in MeleeWeaponDict")
        return (None, 0, [])
    data = MeleeWeaponDict[key]
    strength_bonus = data[0]
    armour_piercing = data[1]
    rules = data[2] if data[2] else []
    return (strength_bonus, armour_piercing, rules)


def get_weapon_special_rules(weapon):
    # Return normalized list of special rules, don't raise on missing by default
    try:
        _, _, rules = get_weapon_stats(weapon, raise_on_missing=False)
        return rules
    except Exception:
        return []

def get_weapon_strength_bonus(weapon, raise_on_missing=True):
    """Return the weapon's strength bonus (or None)."""
    strength, _, _ = get_weapon_stats(weapon, raise_on_missing=raise_on_missing)
    return strength


def get_weapon_ap(weapon, raise_on_missing=True):
    """Return the weapon's armour-piercing value (int, may be negative or 0)."""
    _, ap, _ = get_weapon_stats(weapon, raise_on_missing=raise_on_missing)
    return ap
