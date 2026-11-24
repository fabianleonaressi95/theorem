#!/usr/bin/env python3
"""Exact finite audit for the C3 x C3 equivariant two-sheet construction.

Uses only the Python standard library. Run:
    python audits/audit_c3x_c3_two_sheet_equivariance.py
"""
from __future__ import annotations

import itertools
import json
import math
from collections import Counter
from pathlib import Path

BITS = list(itertools.product((0, 1), repeat=3))
INDEX = {x: i for i, x in enumerate(BITS)}


def T(x):
    a, b, c = x
    return (b, a ^ b, c)


def iterate(x, n):
    for _ in range(n):
        x = T(x)
    return x


assert all(iterate(x, 3) == x for x in BITS)
assert any(T(x) != x for x in BITS)
fixed = [x for x in BITS if T(x) == x]
assert set(fixed) == {(0, 0, 0), (0, 0, 1)}

orbits = []
seen = set()
for x in BITS:
    if x not in seen:
        orb = []
        y = x
        while y not in orb:
            orb.append(y)
            y = T(y)
        assert y == x
        seen.update(orb)
        orbits.append(orb)
assert sorted(map(len, orbits)) == [1, 1, 3, 3]

# Product action: enumerate all 64 hexagrams and orbit sizes.
HEX = list(itertools.product(BITS, BITS))


def product_action(h, i, j):
    return (iterate(h[0], i), iterate(h[1], j))


def product_orbit(h):
    return {product_action(h, i, j) for i in range(3) for j in range(3)}


seen_h = set()
product_orbits = []
for h in HEX:
    if h not in seen_h:
        orb = product_orbit(h)
        product_orbits.append(orb)
        seen_h.update(orb)
assert len(seen_h) == 64
orbit_hist = Counter(map(len, product_orbits))
assert orbit_hist == Counter({1: 4, 3: 8, 9: 4})

# Q3 cube edges and their C3-conjugate union.
q3_edges = set()
for x in BITS:
    for k in range(3):
        y = list(x)
        y[k] ^= 1
        y = tuple(y)
        if INDEX[x] < INDEX[y]:
            q3_edges.add((INDEX[x], INDEX[y]))
assert len(q3_edges) == 12


def permuted_edges(power):
    perm = {INDEX[x]: INDEX[iterate(x, power)] for x in BITS}
    return {tuple(sorted((perm[a], perm[b]))) for a, b in q3_edges}


edge_counts = Counter()
for power in range(3):
    edge_counts.update(permuted_edges(power))
edge_union = set(edge_counts)
assert len(edge_union) == 16
multiplicity_hist = Counter(edge_counts.values())
assert multiplicity_hist == Counter({2: 12, 3: 4})
assert permuted_edges(1) != q3_edges

# Sphere embedding: two fixed states at the poles; two 3-cycles
# on distinct latitude circles. T acts as a 120-degree z rotation.
sqrt3 = math.sqrt(3.0)


def sphere_point(x):
    a, b, c = x
    if (a, b, c) == (0, 0, 0):
        return (0.0, 0.0, 1.0)
    if (a, b, c) == (0, 0, 1):
        return (0.0, 0.0, -1.0)
    if c == 0:
        cycle_index = {(0, 1, 0): 0, (1, 1, 0): 1, (1, 0, 0): 2}[x]
        z = 0.5
    else:
        cycle_index = {(0, 1, 1): 0, (1, 1, 1): 1, (1, 0, 1): 2}[x]
        z = -0.5
    angle = 2.0 * math.pi * cycle_index / 3.0
    return (sqrt3 / 2.0 * math.cos(angle),
            sqrt3 / 2.0 * math.sin(angle), z)


points = {x: sphere_point(x) for x in BITS}
assert len({tuple(round(v, 12) for v in p) for p in points.values()}) == 8
assert all(abs(sum(v*v for v in p) - 1.0) < 1e-12 for p in points.values())


def rotate120(p):
    x, y, z = p
    c, s = -0.5, sqrt3 / 2.0
    return (c*x - s*y, s*x + c*y, z)


equivariance_residual = max(
    math.dist(points[T(x)], rotate120(points[x])) for x in BITS
)
assert equivariance_residual < 1e-12

# The Reynolds-averaged Q3 Laplacian is C3 invariant by construction.
# Its off-diagonal conductance on an unordered pair is multiplicity/3.
# The Q6 product operator has two copies of this factor operator.
weighted_edge_sum = sum(m / 3.0 for m in edge_counts.values())
assert abs(weighted_edge_sum - 12.0) < 1e-12

result = {
    "status": "all assertions passed",
    "trigram_states": 8,
    "trigram_orbit_sizes": sorted(map(len, orbits)),
    "hexagram_states": 64,
    "C3xC3_orbit_histogram": {
        str(k): orbit_hist[k] for k in sorted(orbit_hist)
    },
    "Q3_standard_edges": len(q3_edges),
    "Q3_C3_invariant_union_edges": len(edge_union),
    "Q3_invariant_edge_multiplicity_histogram": {
        str(k): multiplicity_hist[k] for k in sorted(multiplicity_hist)
    },
    "Q6_standard_edges": 192,
    "Q6_C3xC3_invariant_union_edges": 256,
    "sphere_embedding_distinct_points": len(points),
    "sphere_embedding_radius_residual_max": max(
        abs(sum(v*v for v in p) - 1.0) for p in points.values()
    ),
    "equivariance_residual_max": equivariance_residual,
    "reynolds_Q3_total_edge_conductance": weighted_edge_sum,
    "geometry_scope": "S2 sections of 3+1D null cones; not the previous 2+1D Vesica lens arcs",
}
out = Path("results/json/c3x_c3_two_sheet_equivariance_audit.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
