#!/usr/bin/env python3
"""Diagnostic: characterize the small-eigenvalue ('pollution') modes of the
discrete Hodge Laplacian on 1-forms (and (d-1)-forms in 3D).

For each configuration we compute the smallest eigenpairs of B_k and report
  * lambda,
  * ||delta_k x||  (co-closedness defect; delta_k x = M_{k-1}^{-1} d_{k-1}^T M_k x),
  * dist(x, im d_{k-1})  (exactness defect),
  * |x|_inf / |x|_2  (localization),
  * Rayleigh quotient split into curl vs grad parts.

Output: results/pollution.json
"""
import json
import os
import sys

import numpy as np
import scipy.linalg as sla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ddr.mesh import CubicalMesh
from ddr.geometry import PullbackGeometry
from ddr import hodge


def diagnose(dim, N, map_spec, metric_spec=None, k=1, nvec=4):
    metric_spec = metric_spec or {"type": "identity"}
    m = CubicalMesh(N, dim)
    g = PullbackGeometry(m, map_spec, metric_spec, nq=4, nqf=3)
    H = hodge.hodge_matrices(m, g.M)
    B = H["B"][k]
    n = m.nk[k]
    if n > 1200:
        return {"skipped": "too large", "n": n}
    w, V = sla.eigh(B.toarray(), np.diag(g.M[k]))
    order = np.argsort(w)[:nvec]
    rows = []
    for idx in order:
        x = V[:, idx]
        lam = float(w[idx])
        # delta_k x
        if k > 0:
            dk_x = H["delta"][k] @ x
            n_delta = float(np.linalg.norm(dk_x))
        else:
            n_delta = 0.0
        # distance to im d_{k-1}: least squares
        if k > 0:
            A = m.dmat[k - 1].toarray()
            coef, *_ = np.linalg.lstsq(A, x, rcond=None)
            dist_exact = float(np.linalg.norm(x - A @ coef)
                               / np.linalg.norm(x))
        else:
            dist_exact = 1.0
        # Rayleigh parts: grad part x^T M_k d_{k-1} Minv d^T M_k x ; curl part
        Mk = g.M[k]
        grad = 0.0
        curl = 0.0
        if k > 0:
            t = m.dmat[k - 1].T @ (Mk * x)
            grad = float(np.sum(t ** 2 / g.M[k - 1]))
        if k < dim:
            dxc = m.dmat[k] @ x
            curl = float(np.sum(g.M[k + 1] * dxc ** 2))
        denom = float(x @ (Mk * x))
        loc = float(np.abs(x).max() / np.linalg.norm(x))
        rows.append({
            "lambda": lam,
            "norm_delta_k_x": n_delta,
            "rel_dist_to_im_d": dist_exact,
            "rayleigh_grad_part": grad / denom,
            "rayleigh_curl_part": curl / denom,
            "loc_inf_over_l2": loc,
        })
    return {"n": n, "eigenpairs": rows}


def main(outdir="results"):
    os.makedirs(outdir, exist_ok=True)
    cases = []
    for N in [4, 8, 16, 32]:
        cases.append((f"2d_affine_N{N}", 2, N,
                      {"type": "identity"}, {"type": "identity"}, 1))
    for N in [4, 8, 16]:
        cases.append((f"2d_sin015_N{N}", 2, N,
                      {"type": "sinusoid", "amplitude": 0.15, "freq": 1,
                       "direction": [1.0, -0.6]}, {"type": "identity"}, 1))
    for N in [2, 3, 4, 5]:
        cases.append((f"3d_affine_N{N}", 3, N,
                      {"type": "identity"}, {"type": "identity"}, 1))
        cases.append((f"3d_affine_N{N}_k2", 3, N,
                      {"type": "identity"}, {"type": "identity"}, 2))
    out = {}
    for name, dim, N, ms, mts, k in cases:
        print("diag", name, flush=True)
        try:
            out[name] = diagnose(dim, N, ms, mts, k=k)
        except Exception as e:
            out[name] = {"error": repr(e)}
    path = os.path.join(outdir, "pollution.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print("wrote", path)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "results")
