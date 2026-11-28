#!/usr/bin/env python3
"""Audit the Euclidean Cl(6) spinor module and golden 3+3 frame.

This verifies Clifford algebra, chirality, Spin(6) plane-rotation lifts and
the recovered orthogonal cut-and-project frame. It does not construct a
Lorentzian Spin(1,3) connection or a dynamical Dirac operator.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np


def pauli() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return (
        np.asarray([[0, 1], [1, 0]], dtype=complex),
        np.asarray([[0, -1j], [1j, 0]], dtype=complex),
        np.asarray([[1, 0], [0, -1]], dtype=complex),
    )


def clifford6() -> tuple[np.ndarray, ...]:
    sx, sy, sz = pauli()
    eye = np.eye(2, dtype=complex)
    kron3 = lambda a, b, c: np.kron(np.kron(a, b), c)
    return (
        kron3(sx, eye, eye),
        kron3(sy, eye, eye),
        kron3(sz, sx, eye),
        kron3(sz, sy, eye),
        kron3(sz, sz, sx),
        kron3(sz, sz, sy),
    )


def chirality_matrix(gamma: tuple[np.ndarray, ...]) -> np.ndarray:
    product = np.eye(8, dtype=complex)
    for g in gamma:
        product = product @ g
    return 1j * product  # (-i)^3 = i in this convention.


def plane_spin_lift(i: int, j: int, theta: float,
                    gamma: tuple[np.ndarray, ...] | None = None) -> np.ndarray:
    """Spin(6) lift of the active SO(6) rotation e_i -> cos e_i + sin e_j."""
    if i == j or not (0 <= i < 6 and 0 <= j < 6):
        raise ValueError("choose distinct Clifford indices in range 0..5")
    g = clifford6() if gamma is None else gamma
    bivector = g[i] @ g[j]
    return np.cos(theta / 2.0) * np.eye(8) - np.sin(theta / 2.0) * bivector


def golden_cut_project_frame() -> np.ndarray:
    phi = (1.0 + np.sqrt(5.0)) / 2.0
    phi_star = (1.0 - np.sqrt(5.0)) / 2.0

    def A(p: float) -> np.ndarray:
        return np.asarray([
            [0., 0., 1., -1., p, p],
            [1., -1., p, p, 0., 0.],
            [p, p, 0., 0., 1., -1.],
        ])

    p_parallel = A(phi) / np.sqrt(2.0 * (2.0 + phi))
    p_internal = A(phi_star) / np.sqrt(2.0 * (2.0 + phi_star))
    return np.vstack((p_parallel, p_internal))


def run_audit() -> dict:
    gamma = clifford6()
    eye8 = np.eye(8, dtype=complex)
    anti = []
    for i in range(6):
        for j in range(6):
            target = 2.0 * eye8 if i == j else np.zeros((8, 8), dtype=complex)
            anti.append(float(np.linalg.norm(gamma[i] @ gamma[j]
                                             + gamma[j] @ gamma[i] - target)))
    chir = chirality_matrix(gamma)
    chirality_hermitian = float(np.linalg.norm(chir - chir.conj().T))
    chirality_square = float(np.linalg.norm(chir @ chir - eye8))
    chirality_anticomm = max(float(np.linalg.norm(chir @ g + g @ chir))
                             for g in gamma)
    chirality_trace = float(abs(np.trace(chir)))

    theta = 0.731
    S = plane_spin_lift(0, 1, theta, gamma)
    R_i = np.cos(theta) * gamma[0] + np.sin(theta) * gamma[1]
    R_j = -np.sin(theta) * gamma[0] + np.cos(theta) * gamma[1]
    plane_covariance = max(
        float(np.linalg.norm(S @ gamma[0] @ S.conj().T - R_i)),
        float(np.linalg.norm(S @ gamma[1] @ S.conj().T - R_j)),
    )
    spin_unitarity = float(np.linalg.norm(S.conj().T @ S - eye8))
    spin_chirality = float(np.linalg.norm(S @ chir @ S.conj().T - chir))
    S2pi = plane_spin_lift(0, 1, 2.0 * np.pi, gamma)
    S4pi = plane_spin_lift(0, 1, 4.0 * np.pi, gamma)
    two_pi_sign = float(np.linalg.norm(S2pi + eye8))
    four_pi_period = float(np.linalg.norm(S4pi - eye8))

    frame = golden_cut_project_frame()
    frame_orthogonal = float(np.linalg.norm(frame @ frame.T - np.eye(6)))
    frame_det = float(np.linalg.det(frame))

    checks = {
        "Cl6_anticommutator": max(anti) < 1e-12,
        "chirality_hermitian_and_involutive": chirality_hermitian < 1e-12
            and chirality_square < 1e-12,
        "chirality_anticommutes_with_generators": chirality_anticomm < 1e-12,
        "chirality_trace_zero": chirality_trace < 1e-12,
        "Spin6_plane_lift_unitary": spin_unitarity < 1e-12,
        "Spin6_adjoint_rotation": plane_covariance < 1e-12,
        "Spin6_preserves_chirality": spin_chirality < 1e-12,
        "2pi_spin_sign": two_pi_sign < 1e-12,
        "4pi_spin_period": four_pi_period < 1e-12,
        "golden_frame_in_SO6": frame_orthogonal < 1e-12 and abs(frame_det - 1.0) < 1e-12,
    }
    return {
        "status": "FINITE_CL6_AND_SPIN6_REPRESENTATION_AUDITED",
        "clifford_module": {
            "algebra": "Euclidean Cl(6)",
            "Dirac_spinor_dimension_complex": 8,
            "Weyl_spinor_dimensions_complex": [4, 4],
            "gamma_anticommutator_residual_max": max(anti),
            "chirality_hermitian_residual": chirality_hermitian,
            "chirality_square_residual": chirality_square,
            "chirality_anticommutator_residual_max": chirality_anticomm,
            "chirality_trace_abs": chirality_trace,
        },
        "spin6": {
            "plane_rotation_angle_rad": theta,
            "spin_lift_unitarity_residual": spin_unitarity,
            "adjoint_rotation_residual": plane_covariance,
            "chirality_covariance_residual": spin_chirality,
            "two_pi_minus_identity_residual": two_pi_sign,
            "four_pi_plus_identity_residual": four_pi_period,
            "convention": "S_ij(theta)=cos(theta/2)I-sin(theta/2)Gamma_i Gamma_j",
        },
        "golden_cut_project_frame": {
            "shape": [6, 6],
            "orthogonality_residual": frame_orthogonal,
            "determinant": frame_det,
            "group": "SO(6); exactly two Spin(6) lifts, related by sign",
        },
        "checks": checks,
        "pass": all(checks.values()),
        "epistemic_limits": [
            "The 6D module is Euclidean Spin(6), not Lorentzian Spin(1,3).",
            "The 3+3 restriction identifies two spatial SU(2) factors; it does not select physical time.",
            "No Q6 Dirac operator, fermion spectrum, or Nielsen-Ninomiya resolution is claimed.",
            "No coupling to Cartan torsion, Maxwell U(1), or Anti-Twin sheets is dynamically derived.",
        ],
    }


def main() -> None:
    result = run_audit()
    output = Path("audits/Q6_SPIN6_CLIFFORD_AUDIT.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
