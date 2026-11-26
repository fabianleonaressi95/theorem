"""Exact geometric classification of the 384 cyclic Q6 D4-orbit faces.

Coordinates are the canonical six-bit labels in R^6.  The audit deliberately
does not assign W2: planarity and nonzero area are necessary but a chosen
face finite-element basis and a simple polygon filling must also be specified.
"""
from __future__ import annotations

import json
from collections import Counter
from itertools import combinations

import sympy as sp

from models.q6_topological_synchronization import build_q6_complex


def _r(v):
    b1, b2, b3, s1, s2, s3 = v
    return (b1, b2, b3 ^ b1 ^ b2, s2, 1 ^ s1, s3)


def _s(v):
    b1, b2, b3, s1, s2, s3 = v
    return (b1, b2, b3, 1 ^ s1, s2, s3)


def _compose(g, h):
    return tuple(g[h[i]] for i in range(64))


def _group(K):
    R = tuple(K.vertex_index[_r(v)] for v in K.vertices)
    S = tuple(K.vertex_index[_s(v)] for v in K.vertices)
    identity = tuple(range(64))
    group, todo = {identity}, [identity]
    while todo:
        g = todo.pop()
        for generator in (R, S):
            for product in (_compose(generator, g), _compose(g, generator)):
                if product not in group:
                    group.add(product)
                    todo.append(product)
    if len(group) != 8:
        raise ArithmeticError(f"expected D4 of order 8, got {len(group)}")
    return tuple(sorted(group))


def _canonical_cycle(cycle):
    cycle = tuple(cycle)
    candidates = []
    for oriented in (cycle, tuple(reversed(cycle))):
        candidates.extend(oriented[i:] + oriented[:i] for i in range(4))
    return min(candidates)


def _wedge_area_squared(points):
    """Squared norm of the oriented polygon area bivector; exact integer."""
    bivector = {}
    for p, q in zip(points, points[1:] + points[:1]):
        for i, j in combinations(range(6), 2):
            bivector[(i, j)] = bivector.get((i, j), 0) + p[i]*q[j] - p[j]*q[i]
    return sp.Rational(1, 4) * sum(value**2 for value in bivector.values())


def run_audit():
    K = build_q6_complex()
    group = _group(K)

    cycles = {
        _canonical_cycle(tuple(g[v] for v in face))
        for g in group
        for face in K.faces
    }
    if len(cycles) != 384:
        raise ArithmeticError(f"expected 384 distinct cyclic faces, got {len(cycles)}")

    counts = Counter()
    records = []
    for cycle in sorted(cycles):
        points = tuple(tuple(int(x) for x in K.vertices[v]) for v in cycle)
        base = points[0]
        differences = sp.Matrix.hstack(*[
            sp.Matrix([points[i][j] - base[j] for j in range(6)])
            for i in (1, 2, 3)
        ])
        affine_rank = int(differences.rank())
        planar = affine_rank == 2
        parallelogram = all(
            points[0][j] + points[2][j] == points[1][j] + points[3][j]
            for j in range(6)
        )
        area_squared = _wedge_area_squared(points) if planar else None
        nonzero_area = bool(planar and area_squared > 0)
        category = (
            "planar_nonzero_area" if nonzero_area else
            "planar_degenerate" if planar else
            "nonplanar"
        )
        counts[category] += 1
        if parallelogram:
            counts["parallelogram"] += 1
        records.append({
            "cycle": list(cycle),
            "affine_rank": affine_rank,
            "planar": planar,
            "parallelogram": parallelogram,
            "oriented_area_squared": str(area_squared) if area_squared is not None else None,
            "category": category,
        })

    if sum(counts[k] for k in (
        "planar_nonzero_area", "planar_degenerate", "nonplanar"
    )) != 384:
        raise ArithmeticError("face categories do not partition the orbit")

    return {
        "audit": "Q6_D4_ORBIT_FACE_GEOMETRY_EXACT_V1",
        "embedding": "six-bit labels as vertices of [0,1]^6 in R^6",
        "arithmetic": "exact integer/rational arithmetic (SymPy)",
        "D4_order": len(group),
        "face_count": len(cycles),
        "classification_counts": {
            key: int(counts[key]) for key in (
                "planar_nonzero_area", "planar_degenerate", "nonplanar",
                "parallelogram"
            )
        },
        "records": records,
        "area_convention": (
            "For a planar ordered cycle, area_squared is the squared norm "
            "of (1/2) sum_i x_i wedge x_(i+1). It is an oriented polygon "
            "area certificate, not by itself a proof of a simple filling."
        ),
        "W2": {
            "assigned": False,
            "reason": (
                "A positive oriented area is necessary but not sufficient: "
                "simplicity of the polygon, a face basis, orientation "
                "conventions, and compatibility with the chosen cochain "
                "representation must be fixed before assembling a face mass."
            ),
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
