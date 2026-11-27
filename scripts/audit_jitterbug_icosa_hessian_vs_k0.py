#!/usr/bin/env python3
"""Spectral comparison: Jitterbug mechanical Hessian at the icosahedron
vs the archived K0 ladder.

The Gray Jitterbug path (audits/jitterbug_gray_kinematics.py) passes
through a regular icosahedron at gamma_I.  At that configuration the
12 joints form the icosahedron vertices; the same 24 unit rods define
the rigidity matrix.  We compute the elastic Hessian spectrum there
and compare its spacing signature with K0's arithmetic ladder
0.5,0.6,...,12.8 on 124 positive modes.

Honest scope: different dimensions (36 vs 188), different operators.
The test asks only whether the icosahedral point produces a comparable
spectral signature (equispaced vs Laplacian-like).
"""
from pathlib import Path
import json
import sys

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from audits.jitterbug_gray_kinematics import (
    cuboctahedron, edge_list, rigid_triangles, tetrahedral_group,
    orbit_data, jitterbug_path, find_icosahedron,
)
from audits.jitterbug_mechanical_hessian import (
    rigidity_matrix, rigid_body_basis,
)

OUT = ROOT / "audits" / "JITTERBUG_ICOSA_HESSIAN_VS_K0.json"


def main() -> None:
    V0 = cuboctahedron()
    edges = sorted(tuple(map(int, e)) for e in edge_list(V0))
    TRIS = rigid_triangles(V0)
    T = tetrahedral_group()
    A, Qs = orbit_data(V0, T)
    path = jitterbug_path(V0, A, Qs)
    w_ico, pair = find_icosahedron(path, A, Qs, TRIS)
    if w_ico is None:
        raise RuntimeError("icosahedron point not found")

    # 12 joint positions at the icosahedron = orbit of w_ico under T
    W = np.array([Mi @ w_ico for Mi in A])  # 12 x 3

    # check: do these form a regular icosahedron? all pairwise distances
    D = np.linalg.norm(W[:, None] - W[None, :], axis=-1)
    dmin = D[np.triu_indices(12, 1)].min()
    ico_edges = int(np.sum(np.isclose(D, dmin, rtol=1e-6)))

    # rods of the linkage are still unit length at this config?
    rod_err = max(
        abs(np.linalg.norm(W[i] - W[j]) - 1.0) for i, j in edges
    )

    R = rigidity_matrix(W, edges)          # 24 x 36
    H = R.T @ R                              # elastic Hessian (central-force)
    # kernel = rigid motions (6) + mechanism flex direction(s); keep > tol
    ev_all = np.linalg.eigvalsh((H + H.T) / 2)
    ev = np.sort(ev_all[ev_all > 1e-8])
    n_zero = int(np.sum(ev_all <= 1e-8))

    # K0 ladder for comparison
    K = np.load(ROOT / "artifacts" / "K0.npy")
    wk = np.linalg.eigvalsh(K)
    kpos = np.sort(wk[wk > 1e-8])

    # spacing signatures
    def spacing_stats(x):
        d = np.diff(x)
        return {
            "n": int(len(x)),
            "min": float(x[0]), "max": float(x[-1]),
            "mean_gap": float(d.mean()),
            "gap_cv": float(d.std() / d.mean()) if d.mean() else None,
        }

    report = {
        "title": "Jitterbug icosahedron-point Hessian vs K0 ladder",
        "icosahedron_config": {
            "vertex_count": 12,
            "nearest_distance": float(dmin),
            "nearest_neighbor_edges": ico_edges,
            "rod_unit_length_max_err": float(rod_err),
        },
        "mechanical_hessian": spacing_stats(ev),
        "zero_modes": n_zero,
        "positive_eigenvalues_first10": [float(x) for x in ev[:10]],
        "k0_ladder": spacing_stats(kpos),
        "k0_ladder_first10": [float(x) for x in kpos[:10]],
        "comparison": {
            "both_equispaced": bool(
                spacing_stats(ev)["gap_cv"] < 1e-6
                and spacing_stats(kpos)["gap_cv"] < 1e-6
            ),
            "note": (
                "gap_cv << 1 means arithmetic (number-operator) spectrum; "
                "gap_cv ~ O(1) means Laplacian-like growth. Different "
                "dimensions (36 vs 188) -- signature comparison only."
            ),
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
