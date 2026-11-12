"""Calibrated Q6-to-Purcell shape map and local SE(2) transport.

The golden 3+3 frame is copied algebraically from the recovered RGS–PSU
cut-and-project convention. No pair of Q6 axes is privileged: all six
coordinate-flip directions contribute through a user-supplied orthonormal
2-frame in E_perp. The frame and angular scale are calibration inputs, not
derived physical constants.

The edge transport is a one-step midpoint approximation to the continuous
Purcell connection A = -R_bb^{-1} R_bs. It is a finite-graph candidate,
not a refinement/convergence theorem.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from scipy.spatial import ConvexHull

from audits.purcell_swimmer_wall.benchmark import resistance_matrix

PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_STAR = (1.0 - np.sqrt(5.0)) / 2.0


def icosahedral_projection_frames():
    """Return the recovered orthonormal physical/internal 3x6 projections."""
    def axis_matrix(p):
        return np.asarray([
            [0.0, 0.0, 1.0, -1.0, p, p],
            [1.0, -1.0, p, p, 0.0, 0.0],
            [p, p, 0.0, 0.0, 1.0, -1.0],
        ], dtype=float)
    p_parallel = axis_matrix(PHI) / np.sqrt(2.0 * (2.0 + PHI))
    p_internal = axis_matrix(PHI_STAR) / np.sqrt(2.0 * (2.0 + PHI_STAR))
    return p_parallel, p_internal


def q6_centered_states():
    """Canonical 64 Q6 vertices in {-1/2,+1/2}^6, in integer bit order."""
    return np.asarray([
        [((v >> (5 - j)) & 1) - 0.5 for j in range(6)]
        for v in range(64)
    ], dtype=float)


def q6_edges():
    """Return each of the 192 coordinate-flip edges once, oriented 0 -> 1."""
    edges = []
    for vertex in range(64):
        for axis in range(6):
            bit = 1 << (5 - axis)
            if not (vertex & bit):
                edges.append((vertex, vertex | bit, axis))
    return np.asarray(edges, dtype=int)


def validate_calibration_frame(frame, atol=1e-10):
    """Validate a 2x3 orthonormal row frame in the internal 3-space."""
    b = np.asarray(frame, dtype=float)
    if b.shape != (2, 3) or not np.all(np.isfinite(b)):
        raise ValueError("calibration_frame must be a finite 2x3 matrix")
    if not np.allclose(b @ b.T, np.eye(2), atol=atol, rtol=0.0):
        raise ValueError("calibration_frame rows must be orthonormal")
    return b


@dataclass(frozen=True)
class Q6ShapeMap:
    internal_projection: np.ndarray
    internal_coordinates: np.ndarray
    shape_coordinates_unwrapped: np.ndarray
    shape_coordinates: np.ndarray
    edges: np.ndarray
    edge_shape_increments: np.ndarray
    calibration_frame: np.ndarray
    angle_scale: float


def build_q6_shape_map(calibration_frame, *, angle_scale):
    """Build Phi_{B,kappa}(v)=kappa B P_perp (v-1/2) mod 2pi.

    calibration_frame and angle_scale must be calibrated externally.
    Keeping them explicit prevents an arbitrary axis assignment from being
    misreported as a canonical consequence of Q6.
    """
    b = validate_calibration_frame(calibration_frame)
    kappa = float(angle_scale)
    if not np.isfinite(kappa) or kappa <= 0.0:
        raise ValueError("angle_scale must be finite and positive")
    _, p_internal = icosahedral_projection_frames()
    states = q6_centered_states()
    internal = states @ p_internal.T
    unwrapped = kappa * (internal @ b.T)
    wrapped = (unwrapped + np.pi) % (2.0 * np.pi) - np.pi
    edges = q6_edges()
    increments = unwrapped[edges[:, 1]] - unwrapped[edges[:, 0]]
    return Q6ShapeMap(
        internal_projection=p_internal,
        internal_coordinates=internal,
        shape_coordinates_unwrapped=unwrapped,
        shape_coordinates=wrapped,
        edges=edges,
        edge_shape_increments=increments,
        calibration_frame=b,
        angle_scale=kappa,
    )


def window_diameter():
    """Diameter of the canonical projected-cube acceptance window."""
    _, p_internal = icosahedral_projection_frames()
    y = q6_centered_states() @ p_internal.T
    hull = ConvexHull(y)
    vertices = y[hull.vertices]
    differences = vertices[:, None, :] - vertices[None, :, :]
    return float(np.linalg.norm(differences, axis=2).max())


def se2_exp(twist):
    """Exponential map SE(2) for an integrated body twist (vx, vy, omega)."""
    vx, vy, omega = np.asarray(twist, dtype=float)
    if not np.all(np.isfinite([vx, vy, omega])):
        raise ValueError("twist must be finite")
    if abs(omega) < 1e-8:
        a = 1.0 - omega**2 / 6.0
        b = omega / 2.0 - omega**3 / 24.0
    else:
        a = np.sin(omega) / omega
        b = (1.0 - np.cos(omega)) / omega
    v_matrix = np.asarray([[a, -b], [b, a]])
    rotation = np.asarray([
        [np.cos(omega), -np.sin(omega)],
        [np.sin(omega), np.cos(omega)],
    ])
    transform = np.eye(3)
    transform[:2, :2] = rotation
    transform[:2, 2] = v_matrix @ np.asarray([vx, vy])
    return transform


def local_edge_transport(
    shape_map: Q6ShapeMap,
    edge_index: int,
    *,
    body_state=(0.0, 1e-2, 0.0),
    length=1.0,
    lam=1.0,
    radius=1e-4,
    viscosity=1.0,
    quadrature_order=64,
):
    """Midpoint SE(2) transport for one oriented Q6 edge.

    The swimmer body state (x,y,theta) is a declared base configuration.
    The shape path is the straight lift between the two unwrapped Q6 shape
    coordinates. The returned transform is a local midpoint approximation;
    path-ordered refinement and wall-dependent global propagation remain open.
    """
    if not 0 <= int(edge_index) < len(shape_map.edges):
        raise IndexError("edge_index is outside the 192-edge Q6 graph")
    x, y, theta = np.asarray(body_state, dtype=float)
    u, v, _axis = shape_map.edges[int(edge_index)]
    alpha0 = shape_map.shape_coordinates_unwrapped[u]
    delta_alpha = shape_map.edge_shape_increments[int(edge_index)]
    alpha_mid = alpha0 + 0.5 * delta_alpha
    q_mid = np.asarray([x, y, theta, alpha_mid[0], alpha_mid[1]])
    r = resistance_matrix(
        q_mid, length=length, lam=lam, radius=radius,
        viscosity=viscosity, quadrature_order=quadrature_order,
    )
    connection = -np.linalg.solve(r[:3, :3], r[:3, 3:])
    integrated_body_twist = connection @ delta_alpha
    return se2_exp(integrated_body_twist)


def audit_q6_shape_map(shape_map: Q6ShapeMap):
    """Return finite combinatorial, calibration and edge-direction checks."""
    edges = shape_map.edges
    counts = np.bincount(edges[:, 2], minlength=6)
    increments = shape_map.edge_shape_increments
    singular = np.linalg.svd(increments, compute_uv=False)
    return {
        "vertices": int(len(shape_map.internal_coordinates)),
        "edges": int(len(edges)),
        "degree_min": 6,
        "degree_max": 6,
        "edge_count_by_cut_project_axis": counts.tolist(),
        "shape_map_rank": int(np.linalg.matrix_rank(shape_map.shape_coordinates_unwrapped)),
        "edge_increment_rank": int(np.linalg.matrix_rank(increments)),
        "edge_increment_singular_values": singular.tolist(),
        "all_six_cut_project_axes_retained": bool(np.all(counts == 32)),
        "calibration_frame_orthonormal": bool(np.allclose(
            shape_map.calibration_frame @ shape_map.calibration_frame.T,
            np.eye(2), atol=1e-10,
        )),
        "angle_scale": float(shape_map.angle_scale),
        "status": "CALIBRATED_FINITE_GRAPH_CANDIDATE",
    }
