"""Finite-dimensional Airy reconstruction for Morandotti cell fields.

The cell fields are ordered (kappa_0^1, kappa_1^1, kappa_2^1, ...).
The interaction matrix must be the Laplacian-product matrix used by the
published postprocessor: M_ij = integral Delta(kappa_i) Delta(kappa_j).
"""
from __future__ import annotations

import numpy as np


def build_defect_vector(centers: np.ndarray, frank_angles: np.ndarray,
                        burgers_vectors: np.ndarray) -> np.ndarray:
    """Build Phi=(s_i, s_i*x_i+b_i2, s_i*y_i-b_i1)_{i=1}^N."""
    x = np.asarray(centers, dtype=float)
    s = np.asarray(frank_angles, dtype=float)
    b = np.asarray(burgers_vectors, dtype=float)
    if x.ndim != 2 or x.shape[1] != 2 or x.shape[0] == 0:
        raise ValueError("centers must have shape (N, 2), with N >= 1")
    n = x.shape[0]
    if s.shape != (n,):
        raise ValueError("frank_angles must have shape (N,)")
    if b.shape != (n, 2):
        raise ValueError("burgers_vectors must have shape (N, 2)")
    if not (np.isfinite(x).all() and np.isfinite(s).all() and np.isfinite(b).all()):
        raise ValueError("defect data must be finite")
    phi = np.empty((n, 3), dtype=float)
    phi[:, 0] = s
    phi[:, 1] = s * x[:, 0] + b[:, 1]
    phi[:, 2] = s * x[:, 1] - b[:, 0]
    return phi.reshape(3 * n)


def build_defect_components(centers: np.ndarray, frank_angles: np.ndarray,
                            burgers_vectors: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return separate Frank, Burgers, and total source vectors in the model convention."""
    x = np.asarray(centers, dtype=float)
    s = np.asarray(frank_angles, dtype=float)
    b = np.asarray(burgers_vectors, dtype=float)
    if x.ndim != 2 or x.shape[1] != 2 or x.shape[0] == 0:
        raise ValueError("centers must have shape (N, 2), with N >= 1")
    n = x.shape[0]
    if s.shape != (n,) or b.shape != (n, 2):
        raise ValueError("Frank and Burgers arrays must have shapes (N,) and (N, 2)")
    zero_b = np.zeros_like(b)
    zero_s = np.zeros_like(s)
    phi_frank = build_defect_vector(x, s, zero_b)
    phi_burgers = build_defect_vector(x, zero_s, b)
    return phi_frank, phi_burgers, phi_frank + phi_burgers


def rotate_defect_vector_to_frame(defect_vector: np.ndarray,
                                  rotation: np.ndarray) -> np.ndarray:
    """Express each (scalar, x, y) source block in a rotated translational frame."""
    phi = np.asarray(defect_vector, dtype=float)
    R = np.asarray(rotation, dtype=float)
    if phi.ndim != 1 or phi.size == 0 or phi.size % 3:
        raise ValueError("defect_vector must be a non-empty vector with 3 entries per core")
    if R.shape != (2, 2) or not np.isfinite(R).all():
        raise ValueError("rotation must be a finite 2x2 matrix")
    if not np.isfinite(phi).all():
        raise ValueError("defect_vector must be finite")
    blocks = phi.reshape(-1, 3).copy()
    blocks[:, 1:3] = blocks[:, 1:3] @ R
    return blocks.reshape(-1)


def deformation_metric(reference_jacobians: np.ndarray,
                       current_jacobians: np.ndarray) -> dict[str, np.ndarray]:
    """Compute F, G=F.T F and metric anisotropy from paired element Jacobians.

    Jacobians must be sampled at identical reference-element points. The
    resulting metric describes the mesh-coordinate deformation only; it is
    not the defect stress, material constitutive tensor, or a topological
    defect invariant.
    """
    J0 = np.asarray(reference_jacobians, dtype=float)
    J1 = np.asarray(current_jacobians, dtype=float)
    if J0.shape != J1.shape or J0.ndim < 2 or J0.shape[-2:] != (2, 2):
        raise ValueError("reference and current Jacobians must have matching (..., 2, 2) shapes")
    if not np.isfinite(J0).all() or not np.isfinite(J1).all():
        raise ValueError("Jacobian samples must be finite")
    det0 = np.linalg.det(J0)
    det1 = np.linalg.det(J1)
    scale = max(float(np.max(np.abs(det0))), 1.0)
    if np.any(np.abs(det0) <= 1e-13 * scale):
        raise ValueError("reference Jacobian samples must be nonsingular")
    if np.any(det1 <= 0.0):
        raise ValueError("current Jacobian samples must preserve positive orientation")
    F = J1 @ np.linalg.inv(J0)
    G = np.swapaxes(F, -1, -2) @ F
    eigenvalues = np.linalg.eigvalsh(G)
    if np.any(eigenvalues[..., 0] <= 0.0):
        raise FloatingPointError("deformation metric is not positive definite")
    anisotropy = ((eigenvalues[..., 1] - eigenvalues[..., 0]) /
                  (eigenvalues[..., 1] + eigenvalues[..., 0]))
    return {"deformation_gradient": F, "metric": G,
            "eigenvalues": eigenvalues, "anisotropy": anisotropy}


def defect_quadratic_decomposition(interaction_matrix: np.ndarray,
                                   phi_frank: np.ndarray,
                                   phi_burgers: np.ndarray) -> dict[str, float]:
    """Split 1/2 Phi.T M^-1 Phi into Frank, Burgers and mixed terms.

    These are algebraic source-quadratic diagnostics for the current
    interaction matrix, not calibrated physical energies.
    """
    M = np.asarray(interaction_matrix, dtype=float)
    f = np.asarray(phi_frank, dtype=float)
    b = np.asarray(phi_burgers, dtype=float)
    if f.ndim != 1 or b.shape != f.shape:
        raise ValueError("Frank and Burgers source vectors must be matching 1D arrays")
    af = solve_interaction_system(M, f)
    ab = solve_interaction_system(M, b)
    qf = 0.5 * float(f @ af)
    qb = 0.5 * float(b @ ab)
    qfb = float(f @ ab)
    qt = 0.5 * float((f + b) @ (af + ab))
    return {"frank_quadratic": qf, "burgers_quadratic": qb,
            "mixed_cross_term": qfb, "total_quadratic": qt,
            "additivity_residual": float(qt - qf - qb - qfb)}


def two_core_support_radius(core_radius: float, reference_separation: float,
                            maximum_support_radius: float) -> float:
    """Support radius vanishing on the other core's reference boundary."""
    a, separation, maximum = map(float, (core_radius, reference_separation, maximum_support_radius))
    if not (np.isfinite(a) and np.isfinite(separation) and np.isfinite(maximum)):
        raise ValueError("support radii and separation must be finite")
    if not (0.0 < a and 2.0*a < separation and maximum > a):
        raise ValueError("require 0 < core_radius, 2*core_radius < reference_separation and maximum_support_radius > core_radius")
    local_radius = min(maximum, separation-a)
    if local_radius <= a:
        raise ValueError("core separation is too small for disjoint boundary weights")
    return float(local_radius)


def deform_two_core_coordinates(coordinates: np.ndarray,
                                reference_centers: np.ndarray,
                                target_centers: np.ndarray,
                                core_radius: float,
                                support_radius: float) -> np.ndarray:
    """Move two circular cores on a fixed mesh using compact radial weights.

    The Wendland C2 weight is normalized to one at the core boundary and
    vanishes outside support_radius. Thus core-boundary nodes follow their
    assigned centre while sufficiently distant outer-boundary nodes stay put.
    The caller remains responsible for checking element quality after mapping.
    """
    x = np.asarray(coordinates, dtype=float)
    source = np.asarray(reference_centers, dtype=float)
    target = np.asarray(target_centers, dtype=float)
    a, radius = float(core_radius), float(support_radius)
    if x.ndim != 2 or x.shape[1] != 2:
        raise ValueError("coordinates must have shape (N, 2)")
    if source.shape != (2, 2) or target.shape != (2, 2):
        raise ValueError("reference_centers and target_centers must have shape (2, 2)")
    if not (np.isfinite(x).all() and np.isfinite(source).all() and np.isfinite(target).all()):
        raise ValueError("coordinates and centres must be finite")
    if not (np.isfinite(a) and np.isfinite(radius) and 0.0 < a < radius):
        raise ValueError("radii must satisfy 0 < core_radius < support_radius")
    separation = float(np.linalg.norm(source[1]-source[0]))
    # Use the FIXED REFERENCE separation, not the target distance. Thus each
    # reference core-boundary node receives zero displacement from the other
    # core's radial field throughout the distance sweep.
    local_radius = two_core_support_radius(a, separation, radius)
    moved = x.copy()
    displacement = np.zeros_like(x)
    for centre, shift in zip(source, target-source):
        q0 = a / local_radius
        normalizer = (1.0-q0)**4 * (4.0*q0+1.0)
        q = np.linalg.norm(x-centre, axis=1) / local_radius
        weight = np.zeros_like(q)
        active = q < 1.0
        weight[active] = (1.0-q[active])**4 * (4.0*q[active]+1.0)
        weight /= normalizer
        displacement += weight[:, None] * shift[None, :]
    moved += displacement
    return moved


def solve_interaction_system(interaction_matrix: np.ndarray,
                             defect_vector: np.ndarray) -> np.ndarray:
    """Solve M a = Phi after symmetry and positive-definiteness checks."""
    M = np.asarray(interaction_matrix, dtype=float)
    phi = np.asarray(defect_vector, dtype=float)
    if M.ndim != 2 or M.shape[0] != M.shape[1] or M.shape[0] == 0:
        raise ValueError("interaction_matrix must be non-empty and square")
    if phi.shape != (M.shape[0],):
        raise ValueError("defect_vector length must match interaction_matrix")
    if not (np.isfinite(M).all() and np.isfinite(phi).all()):
        raise ValueError("interaction system must be finite")
    scale = max(float(np.linalg.norm(M, ord="fro")), 1.0)
    if np.linalg.norm(M - M.T, ord="fro") > 1e-10 * scale:
        raise ValueError("interaction_matrix must be symmetric")
    M = 0.5 * (M + M.T)
    try:
        np.linalg.cholesky(M)
    except np.linalg.LinAlgError as exc:
        raise ValueError("interaction_matrix must be positive definite") from exc
    coeff = np.linalg.solve(M, phi)
    if not np.isfinite(coeff).all():
        raise FloatingPointError("interaction solve produced non-finite coefficients")
    return coeff


def reconstruct_airy_potential(cell_fields: np.ndarray, coefficients: np.ndarray,
                               young_modulus: float, poisson_ratio: float) -> np.ndarray:
    """Reconstruct v_h = -E/(1-nu^2) sum_i a_i kappa_i^h pointwise."""
    fields = np.asarray(cell_fields, dtype=float)
    a = np.asarray(coefficients, dtype=float)
    E, nu = float(young_modulus), float(poisson_ratio)
    if fields.ndim < 2 or fields.shape[0] == 0:
        raise ValueError("cell_fields must have shape (3N, ...), with at least one point axis")
    if a.shape != (fields.shape[0],):
        raise ValueError("coefficients length must match the number of cell fields")
    if not np.isfinite(fields).all() or not np.isfinite(a).all():
        raise ValueError("cell fields and coefficients must be finite")
    if not np.isfinite(E) or E <= 0.0:
        raise ValueError("young_modulus must be finite and positive")
    if not np.isfinite(nu) or not (-1.0 < nu < 0.5):
        raise ValueError("poisson_ratio must lie in (-1, 1/2) for the plane-strain model")
    return -(E / (1.0 - nu**2)) * np.tensordot(a, fields, axes=(0, 0))
