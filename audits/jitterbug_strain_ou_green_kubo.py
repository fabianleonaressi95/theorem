"""Strain-derived OU Green--Kubo audit for the 3D cuboctahedral Jitterbug.

One central-force energy supplies the rigidity Hessian K, linear stress c,
and strain derivative A. All 12 zero modes (6 rigid + 6 mechanisms) are
removed by restricting the OU process to Ran(K); this is a conditional
finite-dimensional benchmark, not a physical viscosity.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from audits.jitterbug_gray_kinematics import cuboctahedron, edge_list


def strain_basis(d: int = 3):
    out = {}
    for i in range(d):
        S = np.zeros((d, d)); S[i, i] = 1.0
        out[(i, i)] = S
    for i in range(d):
        for j in range(i + 1, d):
            S = np.zeros((d, d)); S[i, j] = S[j, i] = 0.5
            out[(i, j)] = S
    return out


def assemble():
    X = cuboctahedron()
    edges = sorted(tuple(map(int, e)) for e in edge_list(X))
    n, d = len(X), 3
    ndof = n*d
    K = np.zeros((ndof, ndof))
    data = {key: {"c": np.zeros(ndof), "A": np.zeros((ndof, ndof))}
            for key in strain_basis()}
    for i, j in edges:
        b = np.zeros(n); b[i] = -1.0; b[j] = 1.0
        r = X[j] - X[i]
        ell = np.linalg.norm(r)
        nhat = r / ell
        bb = np.outer(b, b)
        K += np.kron(bb, np.outer(nhat, nhat))
        for key, S in strain_basis().items():
            q = float(nhat @ S @ nhat)
            m = S @ nhat - q*nhat
            data[key]["c"] -= ell*q*np.kron(b, nhat)
            block = (np.outer(m, nhat) + np.outer(nhat, m)
                     + q*(np.eye(d)-np.outer(nhat, nhat)))
            data[key]["A"] += np.kron(bb, block)
    return X, edges, K, data


def audit():
    X, edges, K, data = assemble()
    evals, evecs = np.linalg.eigh(K)
    tol = 1e-9
    pos = evals > tol
    lam = evals[pos]
    Q = evecs[:, pos]
    rank = int(pos.sum())
    if rank != 24 or len(evals)-rank != 12:
        raise AssertionError("Jitterbug Hessian nullity/rank changed")
    if np.min(lam) <= 0 or np.linalg.norm(K-K.T) > 1e-10:
        raise AssertionError("Hessian is not symmetric positive on its range")
    keys = list(data)
    cproj, Aproj = {}, {}
    for key in keys:
        cproj[key] = Q.T @ data[key]["c"]
        Aproj[key] = Q.T @ data[key]["A"] @ Q
        if not np.allclose(Aproj[key], Aproj[key].T, atol=1e-10):
            raise AssertionError("strain Hessian derivative is not symmetric")

    # kBT=mu=1. Integrated covariance of linear + centered quadratic stress.
    linear = np.zeros((len(keys), len(keys)))
    quadratic = np.zeros_like(linear)
    inv_lam2 = 1.0/(lam*lam)
    denom = lam[:, None]*lam[None, :]*(lam[:, None]+lam[None, :])
    for a, ka in enumerate(keys):
        for b, kb in enumerate(keys):
            linear[a,b] = float(np.sum(cproj[ka]*cproj[kb]*inv_lam2))
            quadratic[a,b] = float(0.5*np.sum(Aproj[ka]*Aproj[kb]/denom))
    total = linear + quadratic
    if np.min(np.linalg.eigvalsh((total+total.T)/2)) < -1e-8:
        raise AssertionError("integrated autocorrelation tensor is not PSD")

    components = []
    for idx, key in enumerate(keys):
        components.append({
            "strain": f"{key[0]}{key[1]}",
            "linear_c_norm": float(np.linalg.norm(data[key]["c"])),
            "linear_projected_norm": float(np.linalg.norm(cproj[key])),
            "A_projected_frobenius_squared": float(np.sum(Aproj[key]**2)),
            "GK_linear_kBT_over_mu": float(linear[idx,idx]),
            "GK_quadratic_kBT2_over_mu": float(quadratic[idx,idx]),
            "GK_total_kBT_mu1": float(total[idx,idx]),
        })
    return {
        "model": "cuboctahedral Jitterbug, 12 joints, 24 unit central-force rods",
        "parameters": {"spring_constant": 1.0, "rest_length": 1.0,
                       "kBT_for_report": 1.0, "mobility_for_report": 1.0},
        "dof": 36, "edges": len(edges), "rank_K": rank,
        "nullity_K": 12, "rigid_body_modes": 6, "internal_mechanisms": 6,
        "positive_eigenvalues": [float(v) for v in lam],
        "strain_components_order": [f"{i}{j}" for i,j in keys],
        "components": components,
        "integrated_GK_linear_matrix_kBT_over_mu": linear.tolist(),
        "integrated_GK_quadratic_matrix_kBT2_over_mu": quadratic.tolist(),
        "integrated_GK_total_matrix_kBT_mu1": total.tolist(),
        "interpretation": (
            "Finite OU result on Ran(K) only. The six internal zero mechanisms "
            "are excluded along with rigid-body modes; no stationary thermal "
            "law is defined on those free coordinates by this harmonic energy. "
            "Not a material viscosity or a phonon/phason identification."
        ),
    }


def main():
    print(json.dumps(audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
