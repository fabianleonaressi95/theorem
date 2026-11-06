#!/usr/bin/env python3
"""Compare diagonal DEC and consistent tensor-product cubical FEEC masses."""
from __future__ import annotations
import argparse
import json
import numpy as np
import scipy.linalg as la
import scipy.sparse as sp

from ddr.mesh import CubicalMesh
from ddr.geometry import PullbackGeometry
from ddr.hodge import hodge_matrices, betti_numbers
from ddr.feec_mass import assemble_consistent_masses, consistent_hodge_matrices


def spectral_summary(B, M, beta):
    Bd = B.toarray() if sp.issparse(B) else np.asarray(B, float)
    Md = M.toarray() if sp.issparse(M) else np.asarray(M, float)
    asym = float(np.linalg.norm(Bd - Bd.T, ord=np.inf))
    mass_asym = float(np.linalg.norm(Md - Md.T, ord=np.inf))
    mass_eigs = la.eigvalsh(0.5 * (Md + Md.T))
    if mass_eigs[0] <= 0:
        raise ValueError(f"mass matrix is not SPD: min eigenvalue {mass_eigs[0]}")
    vals, vecs = la.eigh(0.5 * (Bd + Bd.T), 0.5 * (Md + Md.T))
    positive = vals[beta:]
    if len(positive) == 0:
        raise ValueError("no positive eigenvalue remains after the topological kernel")
    lam = float(positive[0])
    x = vecs[:, beta]
    residual = Bd @ x - lam * (Md @ x)
    denom = (np.linalg.norm(Bd, 2) * np.linalg.norm(x)
             + abs(lam) * np.linalg.norm(Md @ x))
    return {
        "lambda_min_positive": lam,
        "first_positive_eigenvalues": [float(v) for v in positive[:6]],
        "kernel_eigenvalues_abs_max": float(np.max(np.abs(vals[:beta]))) if beta else 0.0,
        "mass_min_eigenvalue": float(mass_eigs[0]),
        "mass_max_eigenvalue": float(mass_eigs[-1]),
        "mass_condition_number": float(mass_eigs[-1] / mass_eigs[0]),
        "mass_asymmetry_inf": mass_asym,
        "energy_matrix_asymmetry_inf": asym,
        "relative_generalized_eigen_residual": float(np.linalg.norm(residual) / max(denom, 1e-300)),
    }


def run(dim, N, amplitude=0.0, freq=1, nq=5, nqf=4):
    mesh = CubicalMesh(N, dim)
    map_spec = ({"type": "identity"} if amplitude == 0
                else {"type": "sinusoid", "amplitude": amplitude, "freq": freq})
    geometry = PullbackGeometry(mesh, map_spec, {"type": "identity"}, nq=nq, nqf=nqf)
    beta, ranks = betti_numbers(mesh)

    # Existing diagonal DEC / dual-volume inner products.
    Hdec = hodge_matrices(mesh, geometry.M)
    dec = {}
    for k in range(dim + 1):
        dec[k] = spectral_summary(Hdec["B"][k], sp.diags(geometry.M[k]), beta[k])

    # Consistent tensor-product cubical FEEC Gram matrices.
    Mfeec, mass_diagnostics = assemble_consistent_masses(mesh, geometry)
    Bfeec = consistent_hodge_matrices(mesh, Mfeec)
    feec = {}
    for k in range(dim + 1):
        feec[k] = spectral_summary(Bfeec[k], Mfeec[k], beta[k])

    comparison = {}
    for k in range(dim + 1):
        ld = dec[k]["lambda_min_positive"]
        lf = feec[k]["lambda_min_positive"]
        comparison[k] = {
            "DEC_lambda_min_positive": ld,
            "FEEC_lambda_min_positive": lf,
            "FEEC_over_DEC": lf / ld,
        }

    return {
        "dimension": dim, "N": N, "h": mesh.h_eff,
        "map": map_spec, "ambient_metric": {"type": "identity"},
        "quadrature": {"nq": nq, "nqf": nqf},
        "betti": beta, "incidence_ranks": ranks,
        "geometry": geometry.geo,
        "consistent_mass_diagnostics": mass_diagnostics,
        "DEC_diagonal": dec, "FEEC_consistent": feec,
        "comparison": comparison,
        "method": (
            "Same cubical mesh, oriented face DoFs, incidence matrices, "
            "domain map and quadrature. FEEC masses integrate the full "
            "tensor-product cubical de Rham basis with the exterior-power "
            "pullback metric; DEC masses are the existing diagonal "
            "dual-volume weights."
        ),
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--dim", type=int, choices=(2, 3), required=True)
    p.add_argument("--N", type=int, required=True)
    p.add_argument("--amplitude", type=float, default=0.0)
    p.add_argument("--freq", type=int, default=1)
    p.add_argument("--nq", type=int, default=5)
    p.add_argument("--nqf", type=int, default=4)
    p.add_argument("--out", default="")
    a = p.parse_args()
    result = run(a.dim, a.N, a.amplitude, a.freq, a.nq, a.nqf)
    payload = json.dumps(result, indent=2)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(payload + "\\n")
    print(payload)
