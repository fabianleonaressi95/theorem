"""Exact I Ching / golden Q6 coding audit.

Bit convention: bit k is line k+1 counted from the bottom; 1=yang, 0=yin.
All golden values are represented exactly as (a,b) for a+b*lambda,
where lambda**2 = 1-lambda.
"""
from __future__ import annotations

from collections import Counter, defaultdict

GOLDEN_POWERS = (
    (1, 0),
    (0, 1),
    (1, -1),
    (-1, 2),
    (2, -3),
    (-3, 5),
)

TRIGRAM_NAMES = {
    0b000: "Kun",
    0b001: "Gen",
    0b010: "Kan",
    0b011: "Xun",
    0b100: "Zhen",
    0b101: "Li",
    0b110: "Dui",
    0b111: "Qian",
}


def golden_value(state: int, n_lines: int = 6) -> tuple[int, int]:
    """Return exact a,b for sum_{k=0}^{n_lines-1} d_k*lambda**k."""
    if n_lines < 1 or n_lines > 6:
        raise ValueError("n_lines must be between 1 and 6")
    if state < 0 or state >= (1 << n_lines):
        raise ValueError("state does not fit the requested number of lines")
    a = b = 0
    for k in range(n_lines):
        if (state >> k) & 1:
            pa, pb = GOLDEN_POWERS[k]
            a += pa
            b += pb
    return a, b


def trigram_name(code: int) -> str:
    if code not in TRIGRAM_NAMES:
        raise ValueError("trigram code must be in 0..7")
    return TRIGRAM_NAMES[code]


def q6_neighbors(state: int) -> tuple[int, ...]:
    if state < 0 or state >= 64:
        raise ValueError("hexagram code must be in 0..63")
    return tuple(state ^ (1 << k) for k in range(6))


def scalar_classes(n_lines: int = 6) -> dict[tuple[int, int], tuple[int, ...]]:
    classes: dict[tuple[int, int], list[int]] = defaultdict(list)
    for state in range(1 << n_lines):
        classes[golden_value(state, n_lines)].append(state)
    return {value: tuple(states) for value, states in classes.items()}


def transition_profile(state: int, n_lines: int = 6) -> Counter:
    """Count one-line-flip neighbors by exact golden scalar class."""
    return Counter(golden_value(neighbor, n_lines)
                   for neighbor in q6_neighbors(state) if neighbor < (1 << n_lines))


def non_lumpable_classes(n_lines: int = 6) -> dict[tuple[int, int], tuple[int, ...]]:
    """Classes containing states with unequal transition profiles."""
    result = {}
    for value, states in scalar_classes(n_lines).items():
        profiles = {tuple(sorted(transition_profile(s, n_lines).items()))
                    for s in states}
        if len(profiles) > 1:
            result[value] = states
    return result


def q6_edge_count() -> int:
    return (64 * 6) // 2
