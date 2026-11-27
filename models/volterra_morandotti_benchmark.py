"""Matched Volterra dipole / edge source data for the Morandotti C0-IPDG cell method.

The three-core geometry is shared by both configurations: two outer cores carry
opposite Frank charges in the dipole case; the central core carries the matched
Burgers vector in the edge case. This keeps the perforated domain and cell
interaction matrix identical at each fixed (d, a, h).
"""
from __future__ import annotations

import numpy as np

from models.morandotti_cell_reconstruction import build_defect_components


def volterra_three_core_data(separation: float, core_radius: float,
                             frank_magnitude: float = 0.01) -> dict:
    """Return a non-overlapping three-core geometry and matched defect data.

    Core order: upper dipole core, lower dipole core, central edge core.
    The convention of build_defect_vector is
        Phi_i = (s_i, s_i*x_i + b_i,y, s_i*y_i - b_i,x).
    Hence (+Omega at y=+d/2, -Omega at y=-d/2) has the same *global*
    first-moment vector as an edge defect at the origin with b=(-Omega*d,0).

    The local 3N source vectors are intentionally not equal at finite d:
    their distinction is what the C0-IPDG cell matrix resolves.
    """
    d = float(separation)
    a = float(core_radius)
    omega = float(frank_magnitude)
    if not (np.isfinite(d) and np.isfinite(a) and np.isfinite(omega)):
        raise ValueError("separation, core_radius and frank_magnitude must be finite")
    if a <= 0.0 or d <= 4.0*a:
        raise ValueError("three cores must be disjoint: separation must exceed 4*core_radius")
    if omega == 0.0:
        raise ValueError("frank_magnitude must be nonzero")

    centers = np.array([[0.0, 0.5*d], [0.0, -0.5*d], [0.0, 0.0]])
    frank_dipole = np.array([omega, -omega, 0.0])
    burgers_dipole = np.zeros((3, 2))
    frank_edge = np.zeros(3)
    burgers_edge = np.array([[-omega*d, 0.0], [0.0, 0.0], [0.0, 0.0]])

    phi_dipole = build_defect_components(
        centers, frank_dipole, burgers_dipole)[2]
    phi_edge = build_defect_components(
        centers, frank_edge, burgers_edge)[2]

    def global_moments(frank: np.ndarray, burgers: np.ndarray) -> np.ndarray:
        return np.array([
            np.sum(frank),
            np.sum(frank*centers[:, 0] + burgers[:, 1]),
            np.sum(frank*centers[:, 1] - burgers[:, 0]),
        ], dtype=float)

    moments_dipole = global_moments(frank_dipole, burgers_dipole)
    moments_edge = global_moments(frank_edge, burgers_edge)
    distances = np.linalg.norm(centers[:, None, :] - centers[None, :, :], axis=-1)
    distances += np.eye(3)*np.inf
    if np.min(distances) <= 2.0*a:
        raise ValueError("core disks overlap")

    return {
        "centers": centers,
        "core_radius": a,
        "separation": d,
        "frank_magnitude": omega,
        "burgers_vector": np.array([-omega*d, 0.0]),
        "frank_dipole": frank_dipole,
        "burgers_dipole": burgers_dipole,
        "frank_edge": frank_edge,
        "burgers_edge": burgers_edge,
        "phi_dipole": phi_dipole,
        "phi_edge": phi_edge,
        "global_moments_dipole": moments_dipole,
        "global_moments_edge": moments_edge,
        "global_moment_residual": moments_dipole - moments_edge,
        "local_source_vector_difference": phi_dipole - phi_edge,
    }
