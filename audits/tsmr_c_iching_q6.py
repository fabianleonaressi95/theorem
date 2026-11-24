"""Exact I Ching / golden Q6 coding audit.

Bit-string convention: the leftmost printed digit is the bottom line; 1=yang, 0=yin.
For integer codes, digits are read most-significant bit first, so the first
printed digit receives weight lambda**0. Golden values are exact pairs (a,b)
representing a+b*lambda, with lambda**2 = 1-lambda.
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
        if (state >> (n_lines - 1 - k)) & 1:
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
    return tuple(state ^ (1 << (5 - k)) for k in range(6))


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


def q6_walk_spectrum() -> tuple[tuple[int, int], ...]:
    """Exact eigenvalue/multiplicity pairs for adjacency(Q6)/6."""
    from math import comb
    from fractions import Fraction
    return tuple((Fraction(3 - k, 3), comb(6, k)) for k in range(7))


def golden_float(value: tuple[int, int]) -> float:
    """Numerical evaluation of an exact Z[lambda] pair."""
    from math import sqrt
    lam = (sqrt(5.0) - 1.0) / 2.0
    return value[0] + value[1] * lam


def graph_directed_hull(iterations: int = 24):
    """Approximate statewise support-hull endpoints by Bellman iteration.

    Returns lower and upper endpoint vectors. Each iteration contracts the
    previous endpoint uncertainty by lambda**6. These are convex-hull bounds,
    not claims that the graph-directed supports themselves are intervals.
    """
    from math import sqrt
    if iterations < 1:
        raise ValueError("iterations must be positive")
    lam = (sqrt(5.0) - 1.0) / 2.0
    ratio = lam ** 6
    shifts = [golden_float(golden_value(h, 6)) for h in range(64)]
    lower = [0.0] * 64
    upper = [0.0] * 64
    for _ in range(iterations):
        next_lower = [
            min(shifts[j] + ratio * lower[j] for j in q6_neighbors(i))
            for i in range(64)
        ]
        next_upper = [
            max(shifts[j] + ratio * upper[j] for j in q6_neighbors(i))
            for i in range(64)
        ]
        lower, upper = next_lower, next_upper
    return lower, upper


def first_level_hull_overlap_count(iterations: int = 24) -> int:
    """Count pairs of overlapping child convex hulls over all parent states.

    A pair is counted once for each parent state. Convex-hull overlap does
    not prove that the underlying fractal support sets intersect.
    """
    from math import sqrt
    lam = (sqrt(5.0) - 1.0) / 2.0
    ratio = lam ** 6
    shifts = [golden_float(golden_value(h, 6)) for h in range(64)]
    lower, upper = graph_directed_hull(iterations)
    count = 0
    for i in range(64):
        children = []
        for j in q6_neighbors(i):
            children.append((shifts[j] + ratio * lower[j],
                             shifts[j] + ratio * upper[j]))
        for a in range(6):
            for b in range(a + 1, 6):
                if max(children[a][0], children[b][0]) <= min(children[a][1], children[b][1]):
                    count += 1
    return count


def fourier_transfer_matrix(xi: float):
    """Return M(xi)=P diag(exp(i*xi*s_j)) as a complex 64x64 matrix.

    Fourier recursion for f_i(xi)=E[exp(i*xi*Y)|H_0=i] is
    f(xi)=M(xi) f(lambda**6 xi).
    """
    from cmath import exp
    shifts = [golden_float(golden_value(h, 6)) for h in range(64)]
    phases = [exp(1j * xi * shift) for shift in shifts]
    return [
        [phases[j] / 6.0 if (i ^ j).bit_count() == 1 else 0j
         for j in range(64)]
        for i in range(64)
    ]


def minimum_translation_gap_pair() -> tuple[int, int]:
    """Return the exact positive Z[lambda] pair for the smallest shift gap."""
    from decimal import Decimal, localcontext
    from math import sqrt
    values = sorted(set(golden_value(h, 6) for h in range(64)),
                    key=lambda ab: Decimal(ab[0]) +
                    Decimal(ab[1]) * ((Decimal(5).sqrt() - 1) / 2))
    gaps = []
    with localcontext() as ctx:
        ctx.prec = 70
        lam = (Decimal(5).sqrt() - 1) / 2
        for left, right in zip(values, values[1:]):
            diff = (right[0] - left[0], right[1] - left[1])
            numeric = Decimal(diff[0]) + Decimal(diff[1]) * lam
            gaps.append((abs(numeric), diff if numeric >= 0 else (-diff[0], -diff[1])))
        return min(gaps, key=lambda item: item[0])[1]


def translation_multiplicity_profile() -> tuple[tuple[int, int], ...]:
    """Return (class size, number of classes) for the 64 exact translations."""
    counts = Counter(len(states) for states in scalar_classes(6).values())
    return tuple(sorted(counts.items()))
