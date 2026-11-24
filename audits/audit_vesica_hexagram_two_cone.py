#!/usr/bin/env python3
"""Finite audit of the two-null-cone realization of the 64 Q6 hexagrams.

Pure Python; no third-party dependencies.
Run from the repository root:
    python audits/audit_vesica_hexagram_two_cone.py
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

N = 8
TOL = 1e-11
THETA = [-math.pi / 3 + k * math.pi / 21 for k in range(N)]
PHI = [2 * math.pi / 3 + k * math.pi / 21 for k in range(N)]
Q_MINUS = [(math.cos(t), math.sin(t)) for t in THETA]
Q_PLUS = [(1 + math.cos(p), math.sin(p)) for p in PHI]


def inside_disk(point: tuple[float, float], center_x: float) -> bool:
    x, y = point
    return (x - center_x) ** 2 + y**2 <= 1.0 + TOL


def close_point(a: tuple[float, float], b: tuple[float, float]) -> bool:
    return math.dist(a, b) <= TOL


def main() -> dict:
    # Each selected arc is contained in the other unit disk.
    assert all(inside_disk(q, 1.0) for q in Q_MINUS)
    assert all(inside_disk(q, 0.0) for q in Q_PLUS)

    states = []
    midpoint_keys = set()
    diagonal_midpoints = []
    separation_sq = []

    for lower, upper in itertools.product(range(N), repeat=2):
        q_minus = Q_MINUS[lower]
        q_plus = Q_PLUS[upper]

        # Both endpoints lie in the Vesica lens; convexity puts the midpoint there.
        midpoint = ((q_minus[0] + q_plus[0]) / 2,
                    (q_minus[1] + q_plus[1]) / 2)
        assert inside_disk(midpoint, 0.0)
        assert inside_disk(midpoint, 1.0)

        displacement = (q_plus[0] - q_minus[0],
                        q_plus[1] - q_minus[1])
        recovered_minus = (midpoint[0] - displacement[0] / 2,
                           midpoint[1] - displacement[1] / 2)
        recovered_plus = (midpoint[0] + displacement[0] / 2,
                          midpoint[1] + displacement[1] / 2)
        assert close_point(recovered_minus, q_minus)
        assert close_point(recovered_plus, q_plus)

        # Null-cone equations at t=1.
        assert abs(q_minus[0] ** 2 + q_minus[1] ** 2 - 1.0) <= TOL
        assert abs((q_plus[0] - 1) ** 2 + q_plus[1] ** 2 - 1.0) <= TOL

        states.append((lower, upper, q_minus, q_plus))
        midpoint_keys.add((round(midpoint[0], 12), round(midpoint[1], 12)))
        if lower == upper:
            diagonal_midpoints.append(midpoint)
        separation_sq.append(displacement[0] ** 2 + displacement[1] ** 2)

    assert len(states) == 64
    assert len(midpoint_keys) == 57
    assert len(diagonal_midpoints) == 8
    assert all(close_point(diagonal_midpoints[0], m) for m in diagonal_midpoints[1:])

    # Q6 = Q3(lower) Cartesian-product Q3(upper): 192 undirected edges.
    edges = set()
    for lower, upper in itertools.product(range(N), repeat=2):
        for bit in range(3):
            other_lower = lower ^ (1 << bit)
            other_upper = upper ^ (1 << bit)
            edges.add(tuple(sorted(((lower, upper), (other_lower, upper)))))
            edges.add(tuple(sorted(((lower, upper), (lower, other_upper)))))
    assert len(edges) == 192
    assert all((a[0] == b[0]) ^ (a[1] == b[1]) for edge in edges
               for a, b in [edge])

    result = {
        "model": "two sampled future-null-cone patches in Minkowski 2+1",
        "radius": 1.0,
        "apex_separation": 1.0,
        "samples_per_sheet": 8,
        "hexagram_pair_states": len(states),
        "distinct_ordered_geometric_pairs": len(states),
        "distinct_vesica_midpoints_rounded_1e-12": len(midpoint_keys),
        "diagonal_pairs_sharing_midpoint": len(diagonal_midpoints),
        "q6_cartesian_product_edges": len(edges),
        "all_cone_null_equations_pass": True,
        "all_endpoints_and_midpoints_in_vesica": True,
        "midpoint_displacement_reconstruction_pass": True,
        "separation_squared": {
            "minimum": min(separation_sq),
            "maximum": max(separation_sq),
            "mean": sum(separation_sq) / len(separation_sq),
        },
        "interpretation": (
            "Finite geometric realization only; angular bijection is a model choice. "
            "No physical dynamics or GL(3,2) geometric equivariance is asserted."
        ),
    }
    out = Path("results/json/vesica_hexagram_two_cone_audit.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    main()
