#!/usr/bin/env python3
"""Reproducible convex-hull and metric-Laplacian audit for T139."""
from __future__ import annotations

from collections import Counter
import numpy as np
from scipy.spatial import ConvexHull


PSI_SG = 1.465571231876768
PHI = (1.0 + np.sqrt(5.0)) / 2.0


def vertices(t: float) -> np.ndarray:
    """Return the twelve vertices in a fixed, documented order."""
    return np.asarray(
        [(0.0, a, b * t) for a in (-1.0, 1.0) for b in (-1.0, 1.0)]
        + [(a, b * t, 0.0) for a in (-1.0, 1.0) for b in (-1.0, 1.0)]
        + [(a * t, 0.0, b) for a in (-1.0, 1.0) for b in (-1.0, 1.0)],
        dtype=float,
    )


def hull_data(t: float):
    x = vertices(t)
    hull = ConvexHull(x)
    faces = [tuple(sorted(map(int, face))) for face in hull.simplices]
    edges = sorted({
        tuple(sorted((face[i], face[(i + 1) % 3])))
        for face in faces for i in range(3)
    })
    return x, hull, faces, edges


def antipodal_permutation(x: np.ndarray) -> np.ndarray:
    """Return p with x[p[i]] = -x[i]."""
    p = []
    for point in x:
        matches = np.flatnonzero(np.linalg.norm(x + point, axis=1) < 1e-10)
        if len(matches) != 1:
            raise AssertionError("Antipodal vertex is not unique.")
        p.append(int(matches[0]))
    return np.asarray(p, dtype=int)


def audit(t: float = PSI_SG, verbose: bool = True) -> dict:
    x, hull, faces, edges = hull_data(t)
    lengths = {e: float(np.linalg.norm(x[e[0]] - x[e[1]])) for e in edges}
    edge_classes = Counter(round(value, 8) for value in lengths.values())
    face_classes = Counter(
        tuple(sorted(round(lengths[tuple(sorted((face[i], face[(i + 1) % 3])))], 8)
                     for i in range(3)))
        for face in faces
    )

    w = np.zeros((len(x), len(x)), dtype=float)
    for (i, j), ell in lengths.items():
        w[i, j] = w[j, i] = ell ** -2
    laplacian = np.diag(w.sum(axis=1)) - w

    p = antipodal_permutation(x)
    jmat = np.zeros_like(laplacian)
    jmat[np.arange(len(x)), p] = 1.0
    commutator_norm = float(np.linalg.norm(laplacian @ jmat - jmat @ laplacian))

    result = {
        "vertices": len(hull.vertices),
        "edges": len(edges),
        "faces": len(faces),
        "euler": len(hull.vertices) - len(edges) + len(faces),
        "edge_classes": edge_classes,
        "face_classes": face_classes,
        "area": float(hull.area),
        "volume": float(hull.volume),
        "spectrum": np.linalg.eigvalsh(laplacian),
        "antipodal_commutator_norm": commutator_norm,
        "laplacian": laplacian,
        "antipodal": jmat,
    }
    if verbose:
        print(f"t={t:.15f}")
        print(f"V={result['vertices']} E={result['edges']} F={result['faces']} "
              f"Euler={result['euler']}")
        print(f"edge classes (length: count): {dict(edge_classes)}")
        print(f"face classes (sorted side lengths: count): {dict(face_classes)}")
        print(f"area={result['area']:.12f} volume={result['volume']:.12f}")
        print("spectrum=" + np.array2string(result["spectrum"], precision=9))
        print(f"||[L,J]||_F={commutator_norm:.3e}")
    return result


if __name__ == "__main__":
    print("SUPERGOLDEN DEFORMATION")
    audit(PSI_SG)
    print("\nREGULAR ICOSAHEDRON CONTROL")
    audit(PHI)
