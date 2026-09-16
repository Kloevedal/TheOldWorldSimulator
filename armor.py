"""Armour types and their base save targets (lower is better)."""

from __future__ import annotations

ArmourDict = {
    ("Light Armor", "LA", "Light"): 6,
    ("Heavy Armor", "HA", "Heavy"): 5,
    ("Plate Armor", "PA", "Plate", "Full Plate Armor", "Full Plate"): 4,
}

# The armour value of a model wearing no armour, for rules that improve it
# (a shield, Armoured Hide). 7+ is no save until something improves it.
UNARMOURED_SAVE = 7

# Values that all mean "not wearing armour".
NO_ARMOUR = (None, "", "None", "No Armor", "No Armour")


def get_armour_save(armour) -> int | None:
    """Base save target for an armour name, or None if unarmoured/unknown."""
    if armour in NO_ARMOUR:
        return None
    for names, save in ArmourDict.items():
        if armour in names:
            return save
    return None
