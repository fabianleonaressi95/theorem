#!/usr/bin/env python3
"""Exact finite audit: canonical Q6 central-force model in R^6.

The model is deliberately a six-dimensional combinatorial control, not a
three-dimensional Jitterbug material.  It constructs the rigidity Hessian
and strain-Hessian derivative from one central-force energy, then evaluates
the quadratic-stress OU Green--Kubo sum on the positive Hessian subspace.
"""
from __future__ import annotations

import numpy as np


def build_q6():
    n, d = 64, 6
    edges = []
    for x in range(n):
        for k in range(d):
            if ((x >> k) & 1) == 0:
                edges.append((x, x | (1 << k), k))
    assert len(edges) == 192
    return edges


def main():
    n, d = 64, 6
    edges = build_q6()
    ndof = n * d
    K = np.zeros((ndof, ndof), dtype=float)
    shear_data = {}

    # Assemble the reference rigidity Hessian once.
    for v, w, k in edges:
        b = np.zeros(n)
        b[v], b[w] = -1.0, 1.0
        nn = np.zeros(d)
        nn[k] = 1.0
        K += np.kron(np.outer(b, b), np.outer(nn, nn))

    for i in range(d):
        for j in range(i + 1, d):
            S = np.zeros((d, d))
            S[i, j] = S[j, i] = 0.5
            A = np.zeros((ndof, ndof), dtype=float)
            c = np.zeros(ndof, dtype=float)
            for v, w, k in edges:
                b = np.zeros(n)
                b[v], b[w] = -1.0, 1.0
                nn = np.zeros(d)
                nn[k] = 1.0
                q = float(nn @ S @ nn)
                m = S @ nn - q * nn
                block = np.outer(m, nn) + np.outer(nn, m) + q * (np.eye(d) - np.outer(nn, nn))
                bb = np.outer(b, b)
                A += np.kron(bb, block)
                # Reference bond length a=1 and spring constant kappa=1.
                c -= q * np.kron(b, nn)
            shear_data[(i, j)] = (A, c)

    # The rigidity Hessian is a direct sum of six perfect-matching Laplacians.
    evals, evecs = np.linalg.eigh(K)
    tol = 1e-9
    positive = evals > tol
    rank = int(np.count_nonzero(positive))
    positive_evals = evals[positive]
    Q = evecs[:, positive]
    assert rank == 192
    assert np.max(np.abs(positive_evals - 2.0)) < 1e-9
    assert np.max(np.abs(evals[~positive])) < 1e-9

    results = []
    for (i, j), (A, c) in shear_data.items():
        AH = Q.T @ A @ Q
        fro2 = float(np.sum(AH * AH))
        lam_a = positive_evals[:, None]
        lam_b = positive_evals[None, :]
        denom_sum = float(np.sum((AH * AH) / (lam_a * lam_b * (lam_a + lam_b))))
        # For stress deltaPi=-1/2(u^T A u - kBT Tr(A K_H^-1)):
        # integral C(t)dt = (kBT)^2/(2 mu) * denom_sum.
        assert np.linalg.norm(c) < 1e-12
        assert abs(fro2 - 128.0) < 1e-8
        assert abs(denom_sum - 8.0) < 1e-8
        results.append((i, j, np.linalg.norm(c), fro2, denom_sum))

    print("Q6 canonical R^6 central-force / OU audit")
    print(f"vertices={n} edges={len(edges)} dof={ndof}")
    print(f"rank_K={rank} nullity_K={ndof-rank}")
    print(f"positive_eigenvalue_set={sorted(set(np.round(positive_evals, 10)))}")
    print("shear components (i,j): ||c_ij||, ||A_H||_F^2, sum |Aab|^2/[la*lb*(la+lb)]")
    for row in results:
        print(f"{row[0:2]}: {row[2]:.12g}, {row[3]:.12g}, {row[4]:.12g}")
    print("all 15 shear components: identical exact benchmark")
    print("C(t) = 16*(kB*T)^2*exp(-4*mu*t)")
    print("integral_C = 4*(kB*T)^2/mu")
    print("eta_GK = 4*kB*T/(mu*V)")
    print("scope: exact quadratic-stress OU toy model; not 3D material viscosity")


if __name__ == "__main__":
    main()
