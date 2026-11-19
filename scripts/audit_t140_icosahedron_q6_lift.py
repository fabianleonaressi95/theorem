#!/usr/bin/env python3
"""Explicit two-step incidence lift of the T139 icosahedron graph into Q6."""
from __future__ import annotations
from collections import Counter
import numpy as np
from scipy.spatial import ConvexHull

# Fixed vertex order from T139.
Q6_CODES = (0, 3, 33, 5, 34, 39, 10, 45, 36, 6, 40, 9)


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


def lift():
    x, edges = hull_edges()
    assert len(x) == 12 and len(edges) == 30
    assert len(set(Q6_CODES)) == 12
    assert all(c.bit_count() % 2 == 0 for c in Q6_CODES)
    paths = {}
    directed_links = Counter()
    for u, v in edges:
        a, b = Q6_CODES[u], Q6_CODES[v]
        if (a ^ b).bit_count() != 2:
            raise AssertionError(f"edge {(u, v)} does not map to Hamming distance 2")
        mids = [z for z in range(64)
                if z.bit_count() % 2 == 1
                and (a ^ z).bit_count() == 1
                and (b ^ z).bit_count() == 1]
        if not mids:
            raise AssertionError(f"no Q6 two-step path for edge {(u, v)}")
        z = min(mids)
        paths[(u, v)] = (a, z, b)
        directed_links[tuple(sorted((a, z)))] += 1
        directed_links[tuple(sorted((z, b)))] += 1

    # Boundary of each lifted path is [b]-[a].
    for (u, v), (a, z, b) in paths.items():
        boundary = {a: -1, z: 0, b: 1}
        assert boundary == {a: -1, b: 1}
    return {
        "vertices": len(x), "edges": len(edges), "paths": paths,
        "unique_q6_links": len(directed_links),
        "reused_q6_links": sum(n > 1 for n in directed_links.values()),
        "max_link_multiplicity": max(directed_links.values()),
        "antipodal_equivariance": all(
            Q6_CODES[j] == (Q6_CODES[i] ^ 63)
            for i, j in enumerate((3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8))
        ),
    }


if __name__ == "__main__":
    r = lift()
    print(f"icosahedron V={r['vertices']} E={r['edges']}")
    print(f"lifted paths={len(r['paths'])}, unique Q6 links={r['unique_q6_links']}")
    print(f"reused links={r['reused_q6_links']}, max multiplicity={r['max_link_multiplicity']}")
    print(f"antipodal equivariance={r['antipodal_equivariance']}")
    for edge, path in sorted(r["paths"].items()):
        print(f"{edge}: " + " -> ".join(f"{v:06b}" for v in path))
