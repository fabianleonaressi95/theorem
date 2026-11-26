"""Exact W2 on the admissible parallelogram subfamily of Q6 D4-orbit faces.

The construction is deliberately partial: only planar, nondegenerate
parallelograms receive a constant integrated 2-form mass 1/Area.
All arithmetic defining the incidence and squared areas is exact.
"""
from __future__ import annotations

import json
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
        raise ArithmeticError(f"expected D4 order 8, got {len(group)}")
    return tuple(sorted(group))


def _canonical_cycle(cycle):
    candidates = []
    for oriented in (tuple(cycle), tuple(reversed(cycle))):
        candidates.extend(oriented[i:] + oriented[:i] for i in range(4))
    return min(candidates)


def _area_squared_parallelogram(points):
    # For p0,p1,p2,p3 with p0+p2=p1+p3, area bivector is u wedge v.
    u = tuple(points[1][i] - points[0][i] for i in range(6))
    v = tuple(points[3][i] - points[0][i] for i in range(6))
    return sum((u[i]*v[j] - u[j]*v[i])**2
               for i, j in combinations(range(6), 2))


def run_audit():
    K = build_q6_complex()
    group = _group(K)
    cycles = {
        _canonical_cycle(tuple(g[v] for v in face))
        for g in group for face in K.faces
    }
    if len(cycles) != 384:
        raise ArithmeticError(f"expected 384 orbit faces, got {len(cycles)}")

    orbit_edges = sorted({
        tuple(sorted((g[u], g[v])))
        for g in group for u, v in K.edges
    })
    if len(orbit_edges) != 256:
        raise ArithmeticError(f"expected 256 orbit edges, got {len(orbit_edges)}")
    edge_index = {edge: i for i, edge in enumerate(orbit_edges)}

    admissible = []
    rejected = {"nonparallelogram": 0, "degenerate": 0}
    for cycle in sorted(cycles):
        points = tuple(tuple(int(x) for x in K.vertices[v]) for v in cycle)
        parallelogram = all(
            points[0][i] + points[2][i] == points[1][i] + points[3][i]
            for i in range(6)
        )
        if not parallelogram:
            rejected["nonparallelogram"] += 1
            continue
        area2 = _area_squared_parallelogram(points)
        if area2 == 0:
            rejected["degenerate"] += 1
            continue
        # A nondegenerate parallelogram is automatically planar and simple.
        admissible.append((cycle, points, int(area2)))

    B1 = sp.zeros(64, 256)
    for j, (u, v) in enumerate(orbit_edges):
        B1[u, j] = -1
        B1[v, j] = 1

    B2 = sp.zeros(256, len(admissible))
    masses = []
    for col, (cycle, points, area2) in enumerate(admissible):
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            edge = tuple(sorted((u, v)))
            B2[edge_index[edge], col] += 1 if u < v else -1
        masses.append(1 / sp.sqrt(area2))

    chain_zero = B1 * B2 == sp.zeros(64, len(admissible))
    if not chain_zero:
        raise ArithmeticError("B1 B2 != 0 for admissible face subcomplex")
    W2 = sp.diag(*masses) if masses else sp.zeros(0, 0)
    positive = all(mass.is_positive is True for mass in masses)

    return {
        "audit": "Q6_D4_ADMISSIBLE_PARALLELOGRAM_W2_V1",
        "embedding": "six-bit vertices in Euclidean R^6",
        "D4_order": len(group),
        "orbit_face_count": len(cycles),
        "orbit_edge_count": len(orbit_edges),
        "admissible_face_count": len(admissible),
        "rejected_face_counts": rejected,
        "B1_shape": [64, 256],
        "B2_admissible_shape": [256, len(admissible)],
        "B1B2_exact_zero": bool(chain_zero),
        "W2_shape": [len(admissible), len(admissible)],
        "W2_definition": "diagonal; W2_FF = 1/sqrt(area_squared_F)",
        "W2_positive_definite": bool(positive and len(admissible) > 0),
        "area_squared_values": sorted(set(area2 for _, _, area2 in admissible)),
        "faces": [
            {"cycle": list(cycle), "area_squared": area2,
             "W2_diagonal": str(mass)}
            for (cycle, _, area2), mass in zip(admissible, masses)
        ],
        "scope": (
            "W2 is defined only on the nondegenerate parallelogram subfamily. "
            "The excluded cyclic faces are not silently filled. This is a "
            "partial 2-complex, not a metric on all 384 orbit faces."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
