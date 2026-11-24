"""Exact finite-type overlap automaton for the golden Q6 Markov measure.

All translations and difference states are represented in Z[lambda],
lambda=(sqrt(5)-1)/2, lambda**2=1-lambda. No floating-point arithmetic is
used in the automaton construction or in its path-count certificate.
"""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from math import log, sqrt

from audits.tsmr_c_iching_q6 import golden_value, q6_neighbors

Pair = tuple[Fraction | int, Fraction | int]
R: Pair = (5, -8)          # lambda**6
R_INV: Pair = (13, 8)      # lambda**(-6), since lambda is a unit
GOLDEN_POWERS = (
    (1, 0), (0, 1), (1, -1), (-1, 2), (2, -3), (-3, 5)
)


def p_add(x: Pair, y: Pair) -> Pair:
    return (x[0] + y[0], x[1] + y[1])


def p_sub(x: Pair, y: Pair) -> Pair:
    return (x[0] - y[0], x[1] - y[1])


def p_mul(x: Pair, y: Pair) -> Pair:
    a, b = x
    c, d = y
    return (a*c + b*d, a*d + b*c - b*d)


def p_pow(x: Pair, n: int) -> Pair:
    out: Pair = (1, 0)
    for _ in range(n):
        out = p_mul(out, x)
    return out


def p_inv(x: Pair) -> Pair:
    a, b = x
    norm = a*a - a*b - b*b
    if norm == 0:
        raise ZeroDivisionError("zero norm in Q(sqrt(5))")
    return (Fraction(a-b, norm), Fraction(-b, norm))


def p_sign(x: Pair) -> int:
    """Exact sign of a+b*lambda, using lambda=(sqrt(5)-1)/2."""
    a, b = x
    A, B = 2*a-b, b
    if B == 0:
        return (A > 0) - (A < 0)
    if A == 0:
        return (B > 0) - (B < 0)
    if A > 0 and B > 0:
        return 1
    if A < 0 and B < 0:
        return -1
    if A > 0 and B < 0:
        value = A*A - 5*B*B
    else:
        value = 5*B*B - A*A
    return (value > 0) - (value < 0)


def p_cmp(x: Pair, y: Pair) -> int:
    return p_sign(p_sub(x, y))


def p_abs_le(x: Pair, bound: Pair) -> bool:
    return p_cmp(x, bound) <= 0 and p_cmp(x, (-bound[0], -bound[1])) >= 0


def conjugate_abs_le_phi(x: Pair) -> bool:
    """Check |a+b*lambda'| <= phi exactly, lambda'=-1-lambda."""
    a, b = x
    conjugate_as_pair = (a-b, -b)
    phi = (1, 1)
    return p_abs_le(conjugate_as_pair, phi)


def translations() -> tuple[Pair, ...]:
    return tuple(golden_value(h, 6) for h in range(64))


def _solve_policy(policy: list[int], shifts: tuple[Pair, ...]) -> list[Pair]:
    """Solve V_i=s(policy_i)+r V_policy_i exactly for a deterministic policy."""
    values: list[Pair | None] = [None] * 64
    for start in range(64):
        if values[start] is not None:
            continue
        path: list[int] = []
        seen: dict[int, int] = {}
        current = start
        while values[current] is None and current not in seen:
            seen[current] = len(path)
            path.append(current)
            current = policy[current]
        if current in seen:
            cycle_start = seen[current]
            cycle = path[cycle_start:]
            length = len(cycle)
            acc: Pair = (Fraction(0), Fraction(0))
            for power, node in enumerate(cycle):
                acc = p_add(acc, p_mul(p_pow(R, power), shifts[policy[node]]))
            cycle_value = p_mul(
                acc, p_inv(p_sub((1, 0), p_pow(R, length)))
            )
            values[cycle[0]] = cycle_value
            for node in reversed(cycle[1:]):
                values[node] = p_add(
                    shifts[policy[node]], p_mul(R, values[policy[node]])
                )
            for node in reversed(path[:cycle_start]):
                values[node] = p_add(
                    shifts[policy[node]], p_mul(R, values[policy[node]])
                )
        else:
            for node in reversed(path):
                values[node] = p_add(
                    shifts[policy[node]], p_mul(R, values[policy[node]])
                )
    return [value for value in values if value is not None]


def exact_hull_endpoints(mode: str) -> tuple[Pair, ...]:
    """Compute the unique Bellman min/max fixed point by exact policy iteration."""
    if mode not in ("min", "max"):
        raise ValueError("mode must be 'min' or 'max'")
    shifts = translations()
    policy = [q6_neighbors(i)[0] for i in range(64)]
    for _ in range(256):
        values = _solve_policy(policy, shifts)
        improved: list[int] = []
        for i in range(64):
            candidates = q6_neighbors(i)
            best = candidates[0]
            best_value = p_add(shifts[best], p_mul(R, values[best]))
            for child in candidates[1:]:
                candidate = p_add(shifts[child], p_mul(R, values[child]))
                comparison = p_cmp(candidate, best_value)
                if (mode == "min" and comparison < 0) or (
                    mode == "max" and comparison > 0
                ):
                    best, best_value = child, candidate
            improved.append(best)
        if improved == policy:
            # Exact Bellman verification, independent of policy stability.
            for i in range(64):
                candidates = [
                    p_add(shifts[j], p_mul(R, values[j]))
                    for j in q6_neighbors(i)
                ]
                target = candidates[0]
                for candidate in candidates[1:]:
                    comparison = p_cmp(candidate, target)
                    if (mode == "min" and comparison < 0) or (
                        mode == "max" and comparison > 0
                    ):
                        target = candidate
                if p_cmp(values[i], target) != 0:
                    raise AssertionError("Bellman fixed-point verification failed")
            return tuple(values)
        policy = improved
    raise RuntimeError("exact policy iteration did not stabilize")


def exact_global_diameter() -> Pair:
    lower = exact_hull_endpoints("min")
    upper = exact_hull_endpoints("max")
    left = min(lower, key=lambda x: (float(x[0]) + float(x[1])*(sqrt(5)-1)/2))
    right = max(upper, key=lambda x: (float(x[0]) + float(x[1])*(sqrt(5)-1)/2))
    # The selected extrema are then checked by exact comparison against all states.
    if any(p_cmp(left, value) > 0 for value in lower):
        raise AssertionError("lower endpoint selection failed")
    if any(p_cmp(right, value) < 0 for value in upper):
        raise AssertionError("upper endpoint selection failed")
    return p_sub(right, left)


def _within_twice_diameter(delta: Pair, diameter: Pair) -> bool:
    return p_abs_le(delta, p_mul((2, 0), diameter))


def build_overlap_automaton():
    """Build all reachable pair states (p,q,delta) satisfying both embeddings.

    Starts are all 64^2 ordered pairs (p,q,0). A transition chooses one Q6
    neighbor on each side and updates delta'=(delta+s(j)-s(k))/r.
    The real bound is |delta|<=2*diam(support hull); the conjugate bound is
    |delta'|<=phi. Both are necessary for close pairs at the target scale.
    """
    shifts = translations()
    diameter = exact_global_diameter()
    initial = {
        (p, q, 0, 0) for p in range(64) for q in range(64)
    }
    seen = set(initial)
    queue = deque(initial)
    outgoing: dict[tuple[int, int, int, int], tuple] = {}
    while queue:
        state = queue.popleft()
        p, q, a, b = state
        children = []
        for j in q6_neighbors(p):
            for k in q6_neighbors(q):
                difference = p_sub(shifts[j], shifts[k])
                next_delta = p_mul(p_add((a, b), difference), R_INV)
                if not _within_twice_diameter(next_delta, diameter):
                    continue
                if not conjugate_abs_le_phi(next_delta):
                    continue
                target = (j, k, int(next_delta[0]), int(next_delta[1]))
                children.append(target)
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
        outgoing[state] = tuple(children)
    return seen, outgoing, diameter


def max_row_sum_power(outgoing, power: int = 20) -> int:
    """Exact ||A**power||_infinity for the automaton adjacency matrix."""
    states = tuple(outgoing)
    index = {state: i for i, state in enumerate(states)}
    rows = [tuple(index[target] for target in outgoing[state]) for state in states]
    vector = [1] * len(states)
    for _ in range(power):
        vector = [sum(vector[j] for j in row) for row in rows]
    return max(vector)


def overlap_dimension_audit(power: int = 20) -> dict:
    states, outgoing, diameter = build_overlap_automaton()
    edge_count = sum(len(row) for row in outgoing.values())
    max_row_sum = max_row_sum_power(outgoing, power)
    root_bound = max_row_sum ** (1 / power)
    lam = (sqrt(5.0) - 1) / 2
    ratio = lam ** 6
    lower_bound = log(36 / root_bound) / log(1 / ratio)
    return {
        "states": len(states),
        "edges": edge_count,
        "distinct_differences": len({(s[2], s[3]) for s in states}),
        "max_row_sum_power": power,
        "max_row_sum": max_row_sum,
        "root_bound": root_bound,
        "correlation_dimension_lower_bound": lower_bound,
        "diameter_pair": diameter,
    }
