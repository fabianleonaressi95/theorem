"""Weak discrete Saint-Venant incompatibility operator in 2D.

This module assembles the dual pairing
    <Inc eps, phi> = integral eps : cof(D2 phi)
for a symmetric strain basis and an H2-conforming test basis.
It deliberately does not implement the curved-shell operator or the
SU(2) connection-to-source calibration.
"""
from __future__ import annotations

import numpy as np


def cofactor_hessian_2d(hessians: np.ndarray) -> np.ndarray:
    """Return cof(H) for arrays whose final axes are (2, 2)."""
    H = np.asarray(hessians, dtype=float)
    if H.shape[-2:] != (2, 2):
        raise ValueError("Hessians must have trailing shape (2, 2)")
    out = np.empty_like(H)
    out[..., 0, 0] = H[..., 1, 1]
    out[..., 0, 1] = -H[..., 0, 1]
    out[..., 1, 0] = -H[..., 1, 0]
    out[..., 1, 1] = H[..., 0, 0]
    return out


def assemble_inc_weak(
    strain_basis: np.ndarray,
    test_hessians: np.ndarray,
    quadrature_weights: np.ndarray,
) -> np.ndarray:
    """Assemble the weak Inc matrix.

    Parameters
    ----------
    strain_basis:
        Array (ncell, nq, nstrain, 2, 2), symmetric strain basis values.
    test_hessians:
        Array (ntest, ncell, nq, 2, 2), Hessians of globally H2-conforming
        scalar test functions evaluated at the same quadrature points.
    quadrature_weights:
        Array (ncell, nq), including physical Jacobian/area weights.

    Returns
    -------
    A:
        Matrix (ntest, nstrain) representing
        A[i,a] = sum_K int_K eps_a : cof(D2 phi_i).
    """
    E = np.asarray(strain_basis, dtype=float)
    H = np.asarray(test_hessians, dtype=float)
    w = np.asarray(quadrature_weights, dtype=float)
    if E.ndim != 5 or E.shape[-2:] != (2, 2):
        raise ValueError("strain_basis must have shape (ncell,nq,nstrain,2,2)")
    if H.ndim != 5 or H.shape[-2:] != (2, 2):
        raise ValueError("test_hessians must have shape (ntest,ncell,nq,2,2)")
    if H.shape[1:3] != E.shape[:2] or w.shape != E.shape[:2]:
        raise ValueError("cell/quadrature dimensions do not match")
    if not (np.isfinite(E).all() and np.isfinite(H).all() and np.isfinite(w).all()):
        raise ValueError("all assembly inputs must be finite")
    if np.any(w <= 0):
        raise ValueError("quadrature weights must be positive")
    cofH = cofactor_hessian_2d(H)
    return np.einsum("tkqij,kqaij,kq->ta", cofH, E, w, optimize=True)


def p1_triangle_symmetric_strain(
    nodes: np.ndarray, triangles: np.ndarray, nodal_displacement: np.ndarray
) -> np.ndarray:
    """Compute the constant symmetric gradient on each P1 triangle.

    Returns an array (ntriangle, 2, 2). The nodal field is globally C0,
    hence its distributional symmetric gradient is the piecewise field
    returned here.
    """
    X = np.asarray(nodes, dtype=float)
    tri = np.asarray(triangles, dtype=int)
    u = np.asarray(nodal_displacement, dtype=float)
    if X.ndim != 2 or X.shape[1] != 2:
        raise ValueError("nodes must have shape (nnode,2)")
    if tri.ndim != 2 or tri.shape[1] != 3:
        raise ValueError("triangles must have shape (ntriangle,3)")
    if u.shape != X.shape:
        raise ValueError("nodal_displacement must have the same shape as nodes")
    strains = np.empty((len(tri), 2, 2), dtype=float)
    for k, ids in enumerate(tri):
        DX = X[ids[1:]] - X[ids[0]]
        DU = u[ids[1:]] - u[ids[0]]
        det = np.linalg.det(DX)
        if abs(det) < 1e-14:
            raise ValueError(f"degenerate triangle at index {k}")
        grad_u = DU.T @ np.linalg.inv(DX)
        strains[k] = 0.5 * (grad_u + grad_u.T)
    return strains


def assemble_burgers_frank_load(
    test_values_at_dislocations: np.ndarray,
    test_gradients_at_dislocations: np.ndarray,
    burgers_vectors: np.ndarray,
    test_values_at_disclinations: np.ndarray,
    frank_angles: np.ndarray,
) -> np.ndarray:
    """Assemble the weak point-defect load for the planar Airy source.

    Arrays of test values/gradients are evaluated at the prescribed defect
    positions. With n_j = (b_j)^perp/|b_j| and
       zeta = sum_j |b_j| partial_{n_j} delta_{x_j} - sum_k s_k delta_{y_k},
    the distributional pairing is
       <zeta,phi_i> = -sum_j |b_j| grad(phi_i)(x_j).n_j
                      -sum_k s_k phi_i(y_k).

    The sign convention matches the source in the Morandotti dossier.
    """
    Vd = np.asarray(test_values_at_dislocations, dtype=float)
    Gd = np.asarray(test_gradients_at_dislocations, dtype=float)
    B = np.asarray(burgers_vectors, dtype=float)
    Vf = np.asarray(test_values_at_disclinations, dtype=float)
    S = np.asarray(frank_angles, dtype=float)
    if B.ndim != 2 or B.shape[1] != 2:
        raise ValueError("burgers_vectors must have shape (ndislocation,2)")
    nd = len(B)
    if Vd.ndim != 2 or Gd.shape != (Vd.shape[0], nd, 2):
        raise ValueError("dislocation values/gradients have inconsistent shapes")
    if Vd.shape[1] != nd:
        raise ValueError("one test-value column is required per dislocation")
    if Vf.ndim != 2 or S.ndim != 1 or Vf.shape != (Vd.shape[0], len(S)):
        raise ValueError("disclination values/Frank angles have inconsistent shapes")
    norms = np.linalg.norm(B, axis=1)
    if np.any(norms < 1e-14):
        raise ValueError("Burgers vectors must be nonzero")
    n_perp = np.column_stack((-B[:, 1], B[:, 0])) / norms[:, None]
    dislocation = -np.einsum("ijd,jd,j->i", Gd, n_perp, norms)
    disclination = -(Vf @ S)
    return dislocation + disclination
