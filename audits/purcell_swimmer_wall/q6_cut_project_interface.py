"""Parameterized Q6/cut-and-project interface for the Purcell swimmer.

The six 6D coordinate directions are retained.  No pair of Q6 axes is
privileged.  A 2x3 calibration matrix is an explicit model input because
the 3D internal cut-and-project space has no canonical 2D subspace.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_ivp


PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_STAR = (1.0 - np.sqrt(5.0)) / 2.0


def icosahedral_axis_matrix(parameter: float) -> np.ndarray:
    p = float(parameter)
    return np.asarray([
        [0.0, 0.0, 1.0, -1.0, p, p],
        [1.0, -1.0, p, p, 0.0, 0.0],
        [p, p, 0.0, 0.0, 1.0, -1.0],
    ], dtype=float)


def golden_cut_project_frame() -> tuple[np.ndarray, np.ndarray]:
    """Return the recovered orthonormal 3x6 physical and internal maps."""
    p = icosahedral_axis_matrix(PHI) / np.sqrt(2.0 * (2.0 + PHI))
    q = icosahedral_axis_matrix(PHI_STAR) / np.sqrt(2.0 * (2.0 + PHI_STAR))
    return p, q


def q6_states() -> np.ndarray:
    """64 binary vertices, ordered by their integer labels 0,...,63."""
    return np.asarray([[(v >> (5 - j)) & 1 for j in range(6)]
                       for v in range(64)], dtype=np.int8)


def q6_edges() -> np.ndarray:
    """The 192 undirected Q6 edges, each stored once with u < v."""
    states = q6_states()
    lookup = {tuple(row.tolist()): i for i, row in enumerate(states)}
    edges = []
    for u, state in enumerate(states):
        for axis in range(6):
            target = state.copy()
            target[axis] ^= 1
            v = lookup[tuple(target.tolist())]
            if u < v:
                edges.append((u, v, axis))
    return np.asarray(edges, dtype=np.int64)


@dataclass(frozen=True)
class Q6ShapeMap:
    """A declared linear calibration from E_perp to two angle coordinates.

    calibration has shape (2,3), full row rank.  scale converts projected
    internal coordinates to radians.  Angles may optionally be reduced
    modulo 2*pi; unwrapped coordinates are preferable for local holonomy.
    """
    calibration: np.ndarray
    scale: float = 1.0
    offset: np.ndarray | None = None
    periodic: bool = False

    def __post_init__(self):
        c = np.asarray(self.calibration, dtype=float)
        if c.shape != (2, 3) or not np.all(np.isfinite(c)):
            raise ValueError("calibration must be a finite 2x3 matrix")
        if np.linalg.matrix_rank(c) != 2:
            raise ValueError("calibration must have rank two")
        if not np.isfinite(self.scale) or self.scale <= 0:
            raise ValueError("scale must be finite and positive")
        b = np.zeros(2) if self.offset is None else np.asarray(self.offset, dtype=float)
        if b.shape != (2,) or not np.all(np.isfinite(b)):
            raise ValueError("offset must be a finite 2-vector")
        object.__setattr__(self, "calibration", c.copy())
        object.__setattr__(self, "offset", b.copy())

    def coordinates(self, states: np.ndarray | None = None) -> np.ndarray:
        bits = q6_states() if states is None else np.asarray(states, dtype=float)
        if bits.ndim != 2 or bits.shape[1] != 6:
            raise ValueError("states must have shape (n,6)")
        _, p_internal = golden_cut_project_frame()
        centered = bits - 0.5
        angles = self.offset + self.scale * (centered @ p_internal.T @ self.calibration.T)
        return np.mod(angles, 2.0 * np.pi) if self.periodic else angles

    def edge_increments(self) -> np.ndarray:
        """Return all oriented (u<v) shape increments, retaining axis labels."""
        states = q6_states()
        edges = q6_edges()
        _, p_internal = golden_cut_project_frame()
        rows = []
        for u, v, axis in edges:
            delta_bits = states[v].astype(float) - states[u].astype(float)
            delta_internal = p_internal @ delta_bits
            delta_shape = self.scale * (self.calibration @ delta_internal)
            rows.append((u, v, axis, *delta_shape.tolist()))
        return np.asarray(rows, dtype=float)


def se2_pose_matrix(pose: np.ndarray) -> np.ndarray:
    x, y, theta = np.asarray(pose, dtype=float)
    c, s = np.cos(theta), np.sin(theta)
    return np.asarray([[c, -s, x], [s, c, y], [0.0, 0.0, 1.0]])


def integrate_shape_edge(
    body_pose: np.ndarray,
    shape_start: np.ndarray,
    shape_end: np.ndarray,
    connection,
    *,
    rtol: float = 1e-10,
    atol: float = 1e-12,
) -> tuple[np.ndarray, np.ndarray]:
    """Integrate the state-dependent swimmer connection along one shape edge.

    connection(shape, body_pose) must return A in R^(3x2), where
    body_dot = A @ shape_dot.  This formulation respects the wall dependence
    through y and theta; it does not pretend that one fixed U_e works for all
    swimmer states.  Returns the final body pose and relative SE(2) transport.
    """
    pose0 = np.asarray(body_pose, dtype=float)
    s0 = np.asarray(shape_start, dtype=float)
    s1 = np.asarray(shape_end, dtype=float)
    if pose0.shape != (3,) or s0.shape != (2,) or s1.shape != (2,):
        raise ValueError("expected body pose (3,) and shape endpoints (2,)")
    delta = s1 - s0

    def rhs(t, pose):
        shape = s0 + t * delta
        matrix = np.asarray(connection(shape, pose), dtype=float)
        if matrix.shape != (3, 2) or not np.all(np.isfinite(matrix)):
            raise ValueError("connection must return a finite 3x2 matrix")
        return matrix @ delta

    solution = solve_ivp(rhs, (0.0, 1.0), pose0, method="DOP853",
                         rtol=rtol, atol=atol)
    if not solution.success:
        raise RuntimeError(solution.message)
    pose1 = solution.y[:, -1]
    transport = se2_pose_matrix(pose1) @ np.linalg.inv(se2_pose_matrix(pose0))
    return pose1, transport


def audit_interface(calibration: np.ndarray) -> dict:
    """Finite exact-shape audit; no material or physical calibration claimed."""
    c = Q6ShapeMap(calibration)
    p_parallel, p_internal = golden_cut_project_frame()
    states = q6_states()
    edges = q6_edges()
    increments = c.edge_increments()
    projected_axis_vectors = c.scale * c.calibration @ p_internal
    return {
        "q6_vertices": int(len(states)),
        "q6_undirected_edges": int(len(edges)),
        "degree_each_vertex": 6,
        "physical_internal_orthogonality_residual":
            float(np.linalg.norm(p_parallel @ p_internal.T)),
        "physical_frame_orthogonality_residual":
            float(np.linalg.norm(p_parallel @ p_parallel.T - np.eye(3))),
        "internal_frame_orthogonality_residual":
            float(np.linalg.norm(p_internal @ p_internal.T - np.eye(3))),
        "shape_calibration_rank": int(np.linalg.matrix_rank(c.calibration)),
        "edge_axis_counts": [int(np.count_nonzero(edges[:, 2] == j)) for j in range(6)],
        "edge_increment_matrix_rank": int(np.linalg.matrix_rank(increments[:, 3:])),
        "projected_axis_vectors_2d": projected_axis_vectors.tolist(),
        "projected_axis_lengths": np.linalg.norm(projected_axis_vectors, axis=0).tolist(),
        "projected_axis_gram": (projected_axis_vectors.T @ projected_axis_vectors).tolist(),
        "six_axes_retained": bool(set(edges[:, 2].tolist()) == set(range(6))),
        "anisotropy_reported_not_constrained": True,
        "status": "PARAMETERIZED_FINITE_INTERFACE; CALIBRATION_OPEN",
    }
