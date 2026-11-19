#!/usr/bin/env python3
"""Antipodally equivariant path lift of the T139 icosahedron graph into Q6."""
from __future__ import annotations
from collections import Counter
import numpy as np
from scipy.spatial import ConvexHull

# T139 coordinate order: (0, ±1, ±t), (±1, ±t, 0), (±t, 0, ±1).
ANTIPODES = (3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8)
# Six representatives receive distinct weight-two words; partners receive complements.
Q6_CODES = (3, 5, 58, 60, 9, 17, 46, 54, 33, 6, 57, 30)
Q6_MASK = 63


def hull_edges(t: float = 1.465571231876768):
    x = np.asarray(
        [(0., a, b*t) for a in (-1., 1.) for b in (-1., 1.)]
        + [(a, b*t, 0.) for a in (-1., 1.) for b in (-1., 1.)]
        + [(a*t, 0., b) for a in (-1., 1.) for b in (-1., 1.)],
        dtype=float,
    )
    hull = ConvexHull(x)
    edges = set()
    for face in hull.simplices:
        for k in range(3):
            edges.add(tuple(sorted((int(face[k]), int(face[(k+1) % 3])))))
    return x, sorted(edges)


def q6_path(u: int, v: int):
    """Directed shortest Q6 path, flipping differing coordinates in ascending order."""
    current = Q6_CODES[u]
    target = Q6_CODES[v]
    bits = [i for i in range(6) if ((current ^ target) >> i) & 1]
    path = [current]
    for bit in bits:
        current ^= 1 << bit
        path.append(current)
    assert current == target
    return tuple(path)


def audit():
    vertices, edges = hull_edges()
    assert len(vertices) == 12 and len(edges) == 30
    assert len(set(Q6_CODES)) == 12
    assert all(code.bit_count() % 2 == 0 for code in Q6_CODES)
    assert all(Q6_CODES[ANTIPODES[v]] == (Q6_CODES[v] ^ Q6_MASK)
               for v in range(12))

    link_use = Counter()
    lengths = Counter()
    for u, v in edges:
        assert ANTIPODES[u] != v
        path = q6_path(u, v)
        length = len(path) - 1
        assert length in (2, 4)
        assert all((a ^ b).bit_count() == 1 for a, b in zip(path, path[1:]))
        lengths[length] += 1
        for a, b in zip(path, path[1:]):
            link_use[tuple(sorted((a, b)))] += 1

        antipodal_path = q6_path(ANTIPODES[u], ANTIPODES[v])
        assert antipodal_path == tuple(x ^ Q6_MASK for x in path)

        # The oriented path boundary telescopes to target minus source.
        boundary = Counter()
        for a, b in zip(path, path[1:]):
            boundary[a] -= 1
            boundary[b] += 1
        assert {x: n for x, n in boundary.items() if n} == {
            Q6_CODES[u]: -1, Q6_CODES[v]: 1
        }

    return {
        "vertices": len(vertices),
        "edges": len(edges),
        "path_lengths": dict(sorted(lengths.items())),
        "unique_q6_links": len(link_use),
        "reused_q6_links": sum(n > 1 for n in link_use.values()),
        "max_link_multiplicity": max(link_use.values()),
        "antipodal_equivariance": True,
    }


if __name__ == "__main__":
    result = audit()
    for key, value in result.items():
        print(f"{key}: {value}")
