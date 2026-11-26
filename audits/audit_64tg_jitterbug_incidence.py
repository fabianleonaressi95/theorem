#!/usr/bin/env python3
"""Exact integer audit separating the 64-TG FCC graph from Jitterbug rods.

The 12 points with sorted absolute coordinates (0,2,2) form a set
geometrically congruent to the unit-edge cuboctahedron after x(n)=a*n/(2√2).
The FCC graph edges in the canonical data have ||dn||²=2; Jitterbug rods
on this point set have ||dn||²=8. This script checks the incidence mismatch.
"""
from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "64tg_fcc_coordinates.json"


def key_edge(p, q):
    return tuple(sorted((tuple(p), tuple(q))))


def sqdist(p, q):
    return sum((int(p[k]) - int(q[k])) ** 2 for k in range(3))


def audit():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    points = [tuple(map(int, p)) for p in data["vertices_n"]]
    fcc_edges = {
        key_edge(e[0], e[1]) for e in data["edges"]
    }
    cuboct_points = [
        p for p in points
        if sorted(abs(x) for x in p) == [0, 2, 2]
    ]
    assert len(points) == 63
    assert len(data["edges"]) == 240
    assert len(cuboct_points) == 12

    jitterbug_rods = [
        key_edge(p, q)
        for p, q in combinations(cuboct_points, 2)
        if sqdist(p, q) == 8
    ]
    assert len(jitterbug_rods) == 24
    matches = sorted(set(jitterbug_rods) & fcc_edges)
    fcc_lengths = sorted({
        sqdist(e[0], e[1]) for e in data["edges"]
    })
    rod_lengths = sorted({
        sqdist(e[0], e[1]) for e in jitterbug_rods
    })
    degree = {p: 0 for p in cuboct_points}
    for p, q in jitterbug_rods:
        degree[p] += 1
        degree[q] += 1
    assert set(degree.values()) == {4}
    assert not matches
    assert fcc_lengths == [2]
    assert rod_lengths == [8]

    return {
        "vertices_64tg": len(points),
        "edges_64tg": len(data["edges"]),
        "cuboctahedral_point_set": len(cuboct_points),
        "jitterbug_rods": len(jitterbug_rods),
        "jitterbug_rod_degree": sorted(set(degree.values())),
        "fcc_edge_squared_distance_n": fcc_lengths,
        "jitterbug_rod_squared_distance_n": rod_lengths,
        "rod_edges_shared_with_fcc_graph": len(matches),
        "classification": "exact point-set congruence; no FCC/Jitterbug edge-incidence embedding",
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
