#!/usr/bin/env python3
"""T113 metric/spectral controls; deliberately not a quasicrystal mass solver.

The module audits generalized-eigenvalue sensitivities for fluid, isotropic
solid, uncoupled phonon/phason, and coupled two-sector toy kernels.  It also
checks what the quadratic wave action alone contributes under a lapse
variation.  That last quantity is the canonical quadratic energy, NOT the
Esposito–Krichevsky–Nicolis packet gravitational mass: medium back-reaction,
constitutive metric dependence, and boundary terms are absent.
"""
from __future__ import annotations

import argparse
import json
import math
from typing import Callable

import numpy as np


def _positive_definite(matrix: np.ndarray, name: str) -> None:
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"{name} must be square")
    if not np.allclose(matrix, matrix.T, atol=1e-12, rtol=1e-12):
        raise ValueError(f"{name} must be symmetric")
    if np.linalg.eigvalsh(matrix)[0] <= 0:
        raise ValueError(f"{name} must be positive definite")


def generalized_modes(K: np.ndarray, M: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return ascending omega^2 and M-orthonormal eigenvectors."""
    K, M = np.asarray(K, float), np.asarray(M, float)
    _positive_definite(K, "K")
    _positive_definite(M, "M")
    # Cholesky reduction M=L L^T, then diagonalize L^-1 K L^-T.
    L = np.linalg.cholesky(M)
    Linv = np.linalg.inv(L)
    A = Linv @ K @ Linv.T
    values, y = np.linalg.eigh((A + A.T) / 2)
    q = np.linalg.solve(L.T, y)
    return values, q


def hellmann_feynman(
    K: np.ndarray, M: np.ndarray, dK: np.ndarray, dM: np.ndarray,
    mode: int = 0,
) -> float:
    """Exact first derivative of a simple generalized eigenvalue."""
    values, q = generalized_modes(K, M)
    v = q[:, mode]
    denominator = float(v.T @ M @ v)
    return float(v.T @ (dK - values[mode] * dM) @ v / denominator)


def logarithmic_sensitivity(
    matrices: Callable[[float], tuple[np.ndarray, np.ndarray]],
    rho: float = 1.0,
    step: float = 1e-5,
) -> dict:
    """Finite-difference d log(omega^2)/d log(rho), with HF cross-check."""
    if rho <= 0 or step <= 0:
        raise ValueError("rho and step must be positive")
    Km, Mm = matrices(rho * math.exp(-step))
    K0, M0 = matrices(rho)
    Kp, Mp = matrices(rho * math.exp(step))
    wm, _ = generalized_modes(Km, Mm)
    w0, q0 = generalized_modes(K0, M0)
    wp, _ = generalized_modes(Kp, Mp)
    if np.any(wm <= 0) or np.any(w0 <= 0) or np.any(wp <= 0):
        raise ValueError("all squared frequencies must be positive")
    fd = (np.log(wp) - np.log(wm)) / (2 * step)
    # Derivatives with respect to log(rho), using a centered matrix difference.
    dK = (Kp - Km) / (2 * step)
    dM = (Mp - Mm) / (2 * step)
    hf = np.array([
        hellmann_feynman(K0, M0, dK, dM, j) / w0[j]
        for j in range(len(w0))
    ])
    return {
        "omega_squared": w0.tolist(),
        "dlog_omega2_dlogrho_fd": fd.tolist(),
        "dlog_omega2_dlogrho_hf": hf.tolist(),
        "max_hf_fd_error": float(np.max(np.abs(fd - hf))),
        "candidate_log_speed_slope": (0.5 * fd).tolist(),
        "candidate_mass_per_energy_over_c2": (-0.5 * fd).tolist(),
    }


def power_law_sector(alpha: float, inertia_exponent: float = 1.0):
    """Scalar acoustic sector with c(rho) proportional to rho**alpha."""
    def matrices(rho: float):
        mass = np.array([[rho ** inertia_exponent]])
        stiffness = np.array([[rho ** (inertia_exponent + 2 * alpha)]])
        return stiffness, mass
    return matrices


def coupled_sectors(alpha_phonon: float, alpha_phason: float, coupling: float):
    """Positive two-sector toy kernel; coupling=0 is the decoupled control."""
    def matrices(rho: float):
        p = 1.5 * rho ** (1.0 + 2.0 * alpha_phonon)
        s = 0.7 * rho ** (1.0 + 2.0 * alpha_phason)
        cross = coupling * math.sqrt(p * s)
        K = np.array([[p, cross], [cross, s]])
        M = np.diag([rho, rho])
        return K, M
    return matrices


def lapse_variation_energy(q: np.ndarray, velocity: np.ndarray,
                           M: np.ndarray, K: np.ndarray) -> float:
    """Energy from N-variation of L_N=(qdot M qdot)/(2N)-N(qKq)/2."""
    q, velocity = np.asarray(q, float), np.asarray(velocity, float)
    return float(0.5 * (velocity.T @ M @ velocity + q.T @ K @ q))


def audit() -> dict:
    cases = {
        "fluid_control": power_law_sector(alpha=0.25),
        "solid_longitudinal_control": power_law_sector(alpha=0.20),
        "solid_transverse_control": power_law_sector(alpha=-0.10),
        "phonon_phason_R_zero": coupled_sectors(0.20, -0.10, 0.0),
        "phonon_phason_R_nonzero": coupled_sectors(0.20, -0.10, 0.20),
    }
    results = {name: logarithmic_sensitivity(model) for name, model in cases.items()}
    # A finite-dimensional lapse check: dL_N/dN at N=1 gives -E for
    # L_N=T/N-NV, so the positive Hamiltonian energy is -dL_N/dN.
    q = np.array([0.3, -0.2])
    velocity = np.array([0.4, 0.1])
    M = np.diag([2.0, 1.5])
    K = np.array([[3.0, 0.2], [0.2, 2.0]])
    energy = lapse_variation_energy(q, velocity, M, K)
    eps = 1e-6
    lagrangian = lambda N: (velocity @ M @ velocity) / (2*N) - N*(q @ K @ q)/2
    lapse_energy_fd = -(lagrangian(1+eps)-lagrangian(1-eps))/(2*eps)
    return {
        "classification": "numerical regression controls only; no quasicrystal gravitational mass derived",
        "cases": results,
        "lapse_variation": {
            "quadratic_hamiltonian_energy": energy,
            "minus_dL_dN_at_N1_fd": lapse_energy_fd,
            "absolute_error": abs(energy-lapse_energy_fd),
            "interpretation": "quadratic wave-action contribution only; excludes medium response and packet boundary terms",
        },
        "acceptance": {
            "all_hf_fd_errors_below_1e-7": all(
                item["max_hf_fd_error"] < 1e-7 for item in results.values()
            ),
            "R_zero_spectrum_is_sector_union": np.allclose(
                results["phonon_phason_R_zero"]["omega_squared"], [0.7, 1.5], atol=1e-12
            ),
            "lapse_variation_consistent": abs(energy-lapse_energy_fd) < 1e-9,
        },
        "scope_limit": (
            "The speed-derivative candidate is not identified with metric-derived "
            "packet mass. EKN recovery requires the induced medium response, "
            "constitutive metric dependence, nonlinear terms, and boundary terms."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pretty", action="store_true")
    parser.parse_args()
    print(json.dumps(audit(), indent=2))


if __name__ == "__main__":
    main()
