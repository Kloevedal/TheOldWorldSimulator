from special_rules import *

ElvenHonors = {
    "Loremaster": {
        "stat_mods": {},
        "special_rules": ["IthilmarArmor", "LileathsBlessing","LoreofSaphery"],
        "equipment_options": {"weapons": ["SwordofHoeth"]}
    },
    "ShadowStalker": {
        "stat_mods": {},
        "special_rules": ["Ambushers", "Evasive","Fire&Flee","MoveThroughCover","Scouts"],
        "equipment_options": {"weapons": ["BowofAvelorn"]}
    },
    "AnointedofAsuryan": {
        "stat_mods": {},
        "special_rules": [BlessingsofAsuryan,"Fear","WitnesstoDestiny","Veteran"],
        "equipment_options": {"weapons": ["CeremonialHalberd"]}
    },
    
    "BloodofCaledor":{
        "stat_mods": {+1:"WeaponSkill"},
        "special_rules":[DragonArmour,"Impetous","FreeFullPlate"],
        "equipment_options": {"weapons": []}
    },
    
    "ChracianHunter":{
        "stat_mods": {},
        "special_rules":["MoveThroughCover","Stubborn","LionCloak"],
        "equipment_options": {"weapons": ["ChracianGreatBlade"]}
    },
    
    "WardenofSaphery":{
        "stat_mods": {},
        "special_rules":["DeflectShots","IthilmarArmor","KillingBlow"],
        "equipment_options":{"weapons": ["SwordofHoeth"]}
    },
    "PureofHeart":{
        "stat_mods": {},
        "special_rules":["PureofHeart"],
        "equipment_options":{"weapons": []}
    },
    "SeaGuard":{
        "stat_mods":{},
        "special_rules":["NavalDiscipline","RallyingCry"],
        "equipment_options":{"weapons": ["Warbow"]}
    }
}

def apply_elven_honors(character, honors):
    for honor in honors:
        if honor in ElvenHonors:
            honor_data = ElvenHonors[honor]
            # Apply stat modifications
            for stat, mod in honor_data.get("stat_mods", {}).items():
                if hasattr(character, stat):
                    setattr(character, stat, getattr(character, stat) + mod)
            # Add special rules
            if honor_data.get("special_rules"):
                character.SpecialRules.extend(honor_data["special_rules"])
            # Update equipment options (if needed)
            if hasattr(character, "equipment_options") and honor_data.get("equipment_options"):
                for k, v in honor_data["equipment_options"].items():
                    character.equipment_options[k] = v