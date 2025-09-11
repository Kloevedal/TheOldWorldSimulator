
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