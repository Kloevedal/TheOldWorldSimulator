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
    ("SwordofHoeth",):[2,-2,[Magic,RequiresTwoHands]], # Sword of Hoeth, +2 Strength, -2 Armor Piercing, Magic
    ("Handmaiden's Spear", "HandmaidensSpear"): [None, 0, [FirstRoundOnly]],  # Handmaiden's Spear, treated as a thrown/thrusting spear
    ("Ceremonial Halberd", "CeremonialHalberd"): [1, -1, ["AB1", Magic, RequiresTwoHands]],  # Ceremonial Halberd, +1 Strength, -1 Armor Piercing, Armour Bane 1, Magic
    ("Mansmasher",): [1, -1, [Magic, FirstRoundStr]],  # Mansmasher, +1 Strength on the charge round only, -1 Armor Piercing
    ("Darkforged Weapon", "DarkforgedWeapon"): [None, -1, None],  # Darkforged weapon, -1 Armor Piercing (Chaos Dwarf craftsmanship)
    ("Braystaff", "Bray Staff"): [None, 0, None],  # Braystaff, a Bray-Shaman's staff, no bonuses
    ("Grisly Totem", "GrislyTotem"): [None, 0, [Magic]],  # Grisly Totem, Kralmaw's Braystaff (full profile not yet transcribed)
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
    
}

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
