#!/usr/bin/env python3
"""Reproducible audit of the anisotropic Vesica multimode reduction.

Model:
    -div(A grad u) = lambda u on an interior strip of the full Vesica,
    A = [[11/4, sqrt(3)/4], [sqrt(3)/4, 9/4]],
with Dirichlet conditions on the two moving lateral arcs.

The script assembles the moving-basis matrices by Gauss-Legendre quadrature,
checks the variational identities, and integrates the first-order transfer
system. It deliberately reports conditioning/symplectic residuals; a large
residual is a warning, not a certified DtN result.
"""
from __future__ import annotations

import argparse
from functools import lru_cache

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp

KAPPA_X = 11.0 / 4.0
KAPPA_Y = 9.0 / 4.0
A_XY = np.sqrt(3.0) / 4.0


@lru_cache(maxsize=8)
def _quadrature(order: int) -> tuple[np.ndarray, np.ndarray]:
    """Gauss-Legendre nodes and weights on (0,1)."""
    x, weights = leggauss(order)
    return (x + 1.0) / 2.0, weights / 2.0


def vesica_width(y: float) -> tuple[float, float]:
    """Return w(y) and w'(y), for |y| < sqrt(3)/2."""
    if not abs(y) < np.sqrt(3.0) / 2.0:
        raise ValueError("y must lie strictly inside the Vesica tips")
    root = np.sqrt(1.0 - y * y)
    return root - 0.5, -y / root


def geometric_matrices(y: float, modes: int, quadrature_order: int | None = None):
    """Return C,G,B,D and the transverse stiffness matrix.

    phi_n = w^(-1/2) sin(n*pi*t), t=(X+w)/(2w), X in (-w,w).

    Index conventions:
      C_mn = integral phi_m phi_{n,y} dX
      G_mn = integral phi_{m,y} phi_{n,y} dX
      B_mn = integral phi_{m,X} phi_n dX
      D_mn = integral phi_{m,X} phi_{n,y} dX
    """
    if modes < 1:
        raise ValueError("modes must be >= 1")
    w, wp = vesica_width(float(y))
    order = quadrature_order or max(160, 12 * modes + 64)
    t, weights = _quadrature(order)
    n = np.arange(1, modes + 1, dtype=float)[:, None]

    sn = np.sin(n * np.pi * t)
    cn = np.cos(n * np.pi * t)
    phi = sn / np.sqrt(w)
    phi_x = n * np.pi * cn / (2.0 * w ** 1.5)
    phi_y = (
        -wp * sn / (2.0 * w ** 1.5)
        - n * np.pi * wp * (t - 0.5) * cn / (w ** 1.5)
    )

    dx_weights = 2.0 * w * weights
    C = (phi * dx_weights) @ phi_y.T
    G = (phi_y * dx_weights) @ phi_y.T
    B = (phi_x * dx_weights) @ phi.T
    D = (phi_x * dx_weights) @ phi_y.T
    transverse = np.diag((np.arange(1, modes + 1) * np.pi / (2.0 * w)) ** 2)
    return C, G, B, D, transverse


def coefficient_matrices(y: float, modes: int):
    """Return H,K,W for L=f'^T H f' + 2 f'^T K f + f^T W f.

    Direct index contraction gives
      int u_y^2 = |f'|^2 + 2 f'^T C f + f^T G f,
      int u_X u_y = f'^T B^T f + f^T D f.
    Since C and B are skew, K=(9/4)C-(sqrt(3)/4)B.
    """
    C, G, B, D, transverse = geometric_matrices(y, modes)
    H = KAPPA_Y * np.eye(modes)
    K = KAPPA_Y * C - A_XY * B
    W = KAPPA_X * transverse + KAPPA_Y * G + A_XY * (D + D.T)
    return H, K, W


def direct_energy(y: float, f: np.ndarray, fp: np.ndarray, modes: int) -> float:
    """Evaluate the original two-dimensional energy on one section."""
    w, _ = vesica_width(float(y))
    order = max(200, 16 * modes + 80)
    t, weights = _quadrature(order)
    n = np.arange(1, modes + 1, dtype=float)[:, None]
    sn, cn = np.sin(n * np.pi * t), np.cos(n * np.pi * t)
    phi = sn / np.sqrt(w)
    phi_x = n * np.pi * cn / (2.0 * w ** 1.5)
    _, wp = vesica_width(float(y))
    phi_y = (
        -wp * sn / (2.0 * w ** 1.5)
        - n * np.pi * wp * (t - 0.5) * cn / (w ** 1.5)
    )
    dx_weights = 2.0 * w * weights
    u_x = f @ phi_x
    u_y = fp @ phi + f @ phi_y
    integrand = KAPPA_X * u_x**2 + 2.0 * A_XY * u_x * u_y + KAPPA_Y * u_y**2
    return float(np.dot(dx_weights, integrand))


def reduced_energy(y: float, f: np.ndarray, fp: np.ndarray, modes: int) -> float:
    H, K, W = coefficient_matrices(y, modes)
    return float(fp @ H @ fp + 2.0 * fp @ K @ f + f @ W @ f)


def hamiltonian_matrix(y: float, modes: int, lam: float) -> np.ndarray:
    """First-order generator for state (f,p), p=H f' + K f."""
    H, K, W = coefficient_matrices(y, modes)
    Hinv = np.linalg.inv(H)
    return np.block(
        [
            [-Hinv @ K, Hinv],
            [W - lam * np.eye(modes) - K.T @ Hinv @ K, K.T @ Hinv],
        ]
    )


def transfer_dtn(
    modes: int,
    a: float = -0.25,
    b: float = 0.25,
    lam: float = 0.0,
    rtol: float = 2e-10,
    atol: float = 2e-12,
):
    """Integrate the fundamental matrix and return M, DtN, and diagnostics."""
    if not (-np.sqrt(3.0) / 2.0 < a < b < np.sqrt(3.0) / 2.0):
        raise ValueError("the interval must be strictly inside the Vesica")
    size = 2 * modes

    def rhs(y, flat):
        fundamental = flat.reshape(size, size)
        return (hamiltonian_matrix(y, modes, lam) @ fundamental).ravel()

    sol = solve_ivp(
        rhs,
        (a, b),
        np.eye(size).ravel(),
        method="DOP853",
        rtol=rtol,
        atol=atol,
    )
    if not sol.success:
        raise RuntimeError(sol.message)

    M = sol.y[:, -1].reshape(size, size)
    A, B, C, D = M[:modes, :modes], M[:modes, modes:], M[modes:, :modes], M[modes:, modes:]
    if np.linalg.cond(B) > 1e13:
        raise np.linalg.LinAlgError("transfer B block is too ill-conditioned for a reliable DtN")

    Binv = np.linalg.inv(B)
    dtn = np.block(
        [
            [Binv @ A, -Binv],
            [C - D @ Binv @ A, D @ Binv],
        ]
    )
    J = np.block(
        [
            [np.zeros((modes, modes)), np.eye(modes)],
            [-np.eye(modes), np.zeros((modes, modes))],
        ]
    )
    symplectic_residual = float(np.linalg.norm(M.T @ J @ M - J, ord=2))
    dtn_symmetry_residual = float(np.linalg.norm(dtn - dtn.T, ord=2))
    return M, dtn, symplectic_residual, dtn_symmetry_residual, sol.nfev


def run_audit(max_modes: int = 4) -> None:
    rng = np.random.default_rng(20261118)
    y = 0.137
    print("A = [[11/4, sqrt(3)/4], [sqrt(3)/4, 9/4]], det(A) = 6")
    for modes in (1, 2, 3, 4):
        if modes > max_modes:
            continue
        C, G, B, D, _ = geometric_matrices(y, modes)
        print(
            f"N={modes}: ||C+C.T||={np.linalg.norm(C+C.T):.3e}, "
            f"||B+B.T||={np.linalg.norm(B+B.T):.3e}, "
            f"||G-G.T||={np.linalg.norm(G-G.T):.3e}"
        )
        f = rng.normal(size=modes)
        fp = rng.normal(size=modes)
        q2d = direct_energy(y, f, fp, modes)
        qred = reduced_energy(y, f, fp, modes)
        print(f"    energy identity residual={abs(q2d-qred):.3e}")

    for modes in (1, 2, 4, 8):
        if modes > max_modes:
            continue
        _, dtn, symp, symmetry, nfev = transfer_dtn(modes)
        print(
            f"DtN N={modes}: ||Lambda-Lambda.T||_2={symmetry:.3e}, "
            f"symplectic residual={symp:.3e}, nfev={nfev}"
        )
        if symp > 1e-5:
            print("    WARNING: transfer conditioning limits certification at this N")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-modes", type=int, default=4)
    args = parser.parse_args()
    run_audit(args.max_modes)
