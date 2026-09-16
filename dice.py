"""Central dice source for the simulator.

Every roll in the engine goes through :func:`roll_d6`, so that tests can either
seed the generator for reproducible runs or script exact sequences of rolls.

    >>> import dice
    >>> dice.seed(1)                      # reproducible random rolls
    >>> with dice.scripted_dice([6, 6, 1]):
    ...     roll_d6(), roll_d6(), roll_d6()
    (6, 6, 1)
"""

from __future__ import annotations

import random
from collections import deque
from contextlib import contextmanager

_rng = random.Random()
_scripted: deque | None = None
_constant: int | None = None


def roll_d6() -> int:
    """Roll a single D6, honouring any active scripted/constant override."""
    if _constant is not None:
        return _constant
    if _scripted is not None:
        if not _scripted:
            raise AssertionError(
                "scripted_dice ran out of rolls - the engine asked for more "
                "dice than the test provided"
            )
        return _scripted.popleft()
    return _rng.randint(1, 6)


# The Artillery dice: four numbers and a Misfire.
ARTILLERY_FACES = (2, 4, 6, 8, 10, MISFIRE := "Misfire")


def roll_artillery():
    """Roll an Artillery dice. Returns an int, or the string "Misfire"."""
    return ARTILLERY_FACES[roll_d6() - 1]


def roll_amount(amount) -> int:
    """Resolve a characteristic that may be a dice value.

    Accepts an int (returned as is) or a string such as "D3", "D6", "2D3" or
    "D3+1". A D3 is a D6 halved, rounding up.
    """
    if isinstance(amount, int):
        return amount
    import re

    match = re.fullmatch(r"(\d+)?D(3|6)(?:\+(\d+))?", str(amount).replace(" ", "").upper())
    if not match:
        raise ValueError(f"Cannot roll {amount!r}")
    total = int(match.group(3) or 0)
    for _ in range(int(match.group(1) or 1)):
        roll = roll_d6()
        total += (roll + 1) // 2 if match.group(2) == "3" else roll
    return total


def seed(value: int | None) -> None:
    """Seed the underlying RNG so a whole simulation is reproducible."""
    _rng.seed(value)


@contextmanager
def scripted_dice(rolls):
    """Return the given rolls in order instead of rolling randomly.

    Raises AssertionError if the engine asks for more dice than supplied, which
    makes a test fail loudly rather than silently drifting.
    """
    global _scripted
    previous, _scripted = _scripted, deque(rolls)
    try:
        yield
    finally:
        _scripted = previous


@contextmanager
def constant_dice(value: int):
    """Make every D6 come up as `value`. Useful for 'always hits' style tests."""
    global _constant
    previous, _constant = _constant, value
    try:
        yield
    finally:
        _constant = previous
