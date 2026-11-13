#!/usr/bin/env python3
"""Reproduce the local MQM-1 determinant backreaction on the archived A13 bundle.

Usage:
  python audits/morphodynamics/mqm_a13_local_backreaction.py \
      --bundle /path/to/A13_RGS_PSU_QLG_KAGGLE_BUNDLE.zip \
      --output audits/morphodynamics/mqm_a13_local_backreaction.json

The bundle is an external input; it is not copied into this repository.
Only NumPy and the repository's MQM local-field modules are required.
"""
from __future__ import annotations
import argparse
from io import BytesIO
import json
from pathlib import Path
import zipfile
import numpy as np

from models.mqm_local_scalar import (
    incidence_matrix, metric_weights, scalar_action,
    scalar_gradient, scalar_hessian,
)
from models.mqm_local_determinants import LocalDeterminantCoupling


def load_npz_from_zip(zf, suffix):
    matches = [n for n in zf.namelist() if n.endswith(suffix)]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one {suffix}, found {len(matches)}")
    return np.load(BytesIO(zf.read(matches[0])))


def build_a13_model(zf):
    fibre = load_npz_from_zip(zf, "psu_fibre_connection_matrices.npz")
    sea = load_npz_from_zip(zf, "sea_operators.npz")
    geom = load_npz_from_zip(zf, "RGS_PSU_all_matrices.npz")
    X = np.asarray(fibre["X"], dtype=float)
    edges = np.asarray(fibre["edges"], dtype=int)
    U = np.asarray(fibre["U_SU2"], dtype=complex)
    coframe = np.asarray(sea["edge_coframe"], dtype=float)
    tau = np.asarray(sea["tau"], dtype=float)
    adjacency = np.asarray(geom["Q6_adjacency"], dtype=float)
    n = len(X)
    if (X.shape != (64, 3) or edges.shape != (192, 3)
            or U.shape != (192, 2, 2) or coframe.shape != (192, 4)
            or tau.shape != (64,) or adjacency.shape != (64, 64)):
        raise ValueError("A13 archive dimensions do not match the frozen Q6 convention")

    # Four Hermitian Euclidean Clifford matrices, exactly as in the archived
    # SEA derivation. The link block is anti-Hermitian after orientation pairing.
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    gammas = [np.kron(s1, I2), np.kron(s2, I2),
              np.kron(s3, s1), np.kron(s3, s2)]
    spin_dof = 8  # four Clifford components times two SU(2) fibre components
    Dkin = np.zeros((n * spin_dof, n * spin_dof), dtype=complex)
    for k, (i, j, _axis) in enumerate(edges):
        G = sum(coframe[k, a] * gammas[a] for a in range(4))
        block = np.kron(G, U[k])
        si = slice(i * spin_dof, (i + 1) * spin_dof)
        sj = slice(j * spin_dof, (j + 1) * spin_dof)
        Dkin[si, sj] += block
        Dkin[sj, si] += -block.conj().T

    # Two-sheet bosonic Hessian from Q6 Laplacian + mass + torsion-weighted
    # antipodal exchange. This is the archived A13 construction, not a fit.
    lap = np.diag(adjacency.sum(axis=1)) - adjacency
    antipode = np.argmin(
        np.linalg.norm(X[:, None, :] + X[None, :, :], axis=2), axis=1
    )
    J = np.eye(n)[antipode]
    Hdim = np.diag(tau) @ J
    Hcross = np.block([[np.zeros((n, n)), Hdim],
                       [Hdim.T, np.zeros((n, n))]])
    mB, mu = 0.6, 0.2
    KB0 = np.block([
        [lap + mB**2 * np.eye(n), np.zeros((n, n))],
        [np.zeros((n, n)), lap + mB**2 * np.eye(n)],
    ]) + mu * Hcross

    mF, gF, lambdaB = 0.5, 0.35, 0.4
    model = LocalDeterminantCoupling(
        Dkin, KB0, tau, spin_dof, mF=mF, gF=gF, lambdaB=lambdaB
    )

    # Metric-edge Dirichlet action uses the raw four-coframe edge lengths.
    radii = np.linalg.norm(X, axis=1)
    raw = np.column_stack([
        X[edges[:, 1]] - X[edges[:, 0]],
        radii[edges[:, 1]] - radii[edges[:, 0]],
    ])
    lengths = np.linalg.norm(raw, axis=1)
    B = incidence_matrix(edges, n)
    weights = metric_weights(lengths)
    return model, B, weights, {
        "vertices": n, "edges": len(edges), "fermion_dimension": n * spin_dof,
        "boson_dimension": 2 * n, "spin_dof_per_vertex": spin_dof,
        "mF": mF, "gF": gF, "mB": mB, "lambdaB": lambdaB,
        "mu_sheet": mu, "kappa": 1.0,
        "Dkin_antihermiticity_residual": float(
            np.linalg.norm(Dkin + Dkin.conj().T)
        ),
        "tau_min": float(tau.min()), "tau_mean": float(tau.mean()),
        "tau_max": float(tau.max()), "tau_std": float(tau.std()),
        "tau_antipodal_residual": float(np.max(np.abs(tau - tau[antipode]))),
        "bosonic_KB0_min_eigenvalue": float(np.linalg.eigvalsh(KB0)[0]),
    }


def total_value_gradient_hessian(model, phi, B, weights):
    det_value, det_grad, det_hess = model.determinant_gradient_hessian(phi)
    scalar_value = scalar_action(phi, B, weights, lam=1.0, phi_v=1.0)
    grad = scalar_gradient(phi, B, weights, lam=1.0, phi_v=1.0) + det_grad
    hess = scalar_hessian(phi, B, weights, lam=1.0, phi_v=1.0) + det_hess
    return scalar_value + det_value, grad, hess


def newton_minimize(model, B, weights, initial, max_iter=30):
    phi = np.asarray(initial, dtype=float).copy()
    for iteration in range(max_iter):
        value, grad, hess = total_value_gradient_hessian(model, phi, B, weights)
        if np.linalg.norm(grad) < 1e-10:
            return phi, iteration, value, grad
        step = np.linalg.solve(hess, grad)
        directional = float(grad @ step)
        alpha = 1.0
        accepted = False
        while alpha > 1e-8:
            candidate = phi - alpha * step
            try:
                candidate_value = model.local_scalar_effective_action(
                    candidate, B, weights, lam=1.0, phi_v=1.0
                )
            except ValueError:
                candidate_value = np.inf
            if (np.isfinite(candidate_value)
                    and candidate_value < value - 1e-4 * alpha * directional):
                phi = candidate
                accepted = True
                break
            alpha *= 0.5
        if not accepted:
            raise RuntimeError("damped Newton line search failed")
    raise RuntimeError("damped Newton did not converge")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    with zipfile.ZipFile(args.bundle) as zf:
        model, B, weights, meta = build_a13_model(zf)

    n = len(model.tau)
    samples = {}
    for q in (0.0, 0.25, 0.5, 0.75, 1.0, 1.25):
        phi = np.full(n, q)
        value, grad, hess = total_value_gradient_hessian(model, phi, B, weights)
        boson_min = float(np.linalg.eigvalsh(model.boson_matrix(phi))[0])
        fermion_min_sv = float(np.linalg.svd(
            model.fermion_matrix(phi), compute_uv=False
        ).min())
        samples[str(q)] = {
            "total_action": float(value),
            "gradient_norm": float(np.linalg.norm(grad)),
            "gradient_mean": float(grad.mean()),
            "gradient_nonuniform_rms": float(np.std(grad)),
            "hessian_min_eigenvalue": float(np.linalg.eigvalsh(hess)[0]),
            "uniform_direction_curvature": float(np.ones(n) @ hess @ np.ones(n) / n),
            "boson_min_eigenvalue": boson_min,
            "fermion_min_singular_value": fermion_min_sv,
        }

    # Full 64-field finite-difference audit at a deterministic nonuniform field.
    phi_test = 0.35 + 0.04 * np.sin(np.arange(n) * 0.71)
    value, grad, hess = total_value_gradient_hessian(model, phi_test, B, weights)
    eps = 2e-5
    fd_grad = np.zeros(n)
    fd_hess = np.zeros((n, n))
    for i in range(n):
        direction = np.eye(n)[i] * eps
        vp = model.local_scalar_effective_action(
            phi_test + direction, B, weights, lam=1.0, phi_v=1.0
        )
        vm = model.local_scalar_effective_action(
            phi_test - direction, B, weights, lam=1.0, phi_v=1.0
        )
        fd_grad[i] = (vp - vm) / (2 * eps)
        gp = total_value_gradient_hessian(model, phi_test + direction, B, weights)[1]
        gm = total_value_gradient_hessian(model, phi_test - direction, B, weights)[1]
        fd_hess[:, i] = (gp - gm) / (2 * eps)

    # Uniform initial field: determine whether the local 64-component field is stationary.
    phi_star, iterations, star_value, star_grad = newton_minimize(
        model, B, weights, np.ones(n)
    )
    star_value, star_grad, star_hess = total_value_gradient_hessian(
        model, phi_star, B, weights
    )
    star_hess_eigs = np.linalg.eigvalsh(star_hess)
    star_boson_min = float(np.linalg.eigvalsh(model.boson_matrix(phi_star))[0])
    star_fermion_min_sv = float(np.linalg.svd(
        model.fermion_matrix(phi_star), compute_uv=False
    ).min())

    report = {
        "status": "REPRODUCED_ON_ARCHIVED_A13_MATRICES; FINITE_GRAPH_DIMENSIONLESS_MODEL",
        "input_bundle": args.bundle.name,
        "operator_construction": meta,
        "local_scalar_parameters": {"lambda": 1.0, "phi_v": 1.0, "V0": 0.0},
        "uniform_field_samples": samples,
        "finite_difference_audit": {
            "field": "0.35 + 0.04 sin(0.71*g)",
            "gradient_max_abs_error": float(np.max(np.abs(grad - fd_grad))),
            "gradient_relative_l2_error": float(
                np.linalg.norm(grad - fd_grad) / max(1.0, np.linalg.norm(fd_grad))
            ),
            "hessian_max_abs_error": float(np.max(np.abs(hess - fd_hess))),
            "hessian_relative_frobenius_error": float(
                np.linalg.norm(hess - fd_hess) / max(1.0, np.linalg.norm(fd_hess))
            ),
            "hessian_symmetry_error": float(np.linalg.norm(hess - hess.T)),
        },
        "stationary_local_field": {
            "solver": "damped Newton with exact analytic Hessian and backtracking",
            "initial_field": 1.0,
            "iterations": int(iterations),
            "action": float(star_value),
            "gradient_norm": float(np.linalg.norm(star_grad)),
            "phi_min": float(phi_star.min()),
            "phi_max": float(phi_star.max()),
            "phi_mean": float(phi_star.mean()),
            "phi_std": float(phi_star.std()),
            "correlation_phi_tau": float(np.corrcoef(phi_star, model.tau)[0, 1]),
            "hessian_min_eigenvalue": float(star_hess_eigs[0]),
            "hessian_max_eigenvalue": float(star_hess_eigs[-1]),
            "negative_hessian_modes": int(np.sum(star_hess_eigs < -1e-8)),
            "boson_min_eigenvalue": star_boson_min,
            "fermion_min_singular_value": star_fermion_min_sv,
            "phi_by_q6_vertex": phi_star.tolist(),
        },
        "interpretation": [
            "The uniform q=1 field is not a stationary point of the full 64-field action: its local gradient has a nonzero nonuniform component.",
            "For the stated dimensionless parameters and the archived A13 operators, damped Newton converges from phi=1 to a nonuniform stationary point with positive Hessian spectrum.",
            "This is a finite-graph model result conditional on the explicit q-to-phi promotion and the local two-sheet bosonic coupling; it is not a calibrated physical prediction.",
        ],
        "limitations": [
            "The stored SU(2) links are geometric spin-fibre transport, not SU(3) QCD colour links.",
            "The radial coframe component is delta(norm(X)); its physical uniqueness remains open.",
            "No continuum limit, renormalization, four-dimensional FEEC/DEC convergence, or physical-unit calibration is established by one Q6 graph.",
        ],
    }
    encoded = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded + "\n")
    print(encoded)


if __name__ == "__main__":
    main()
