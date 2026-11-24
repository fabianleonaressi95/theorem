"""Exact 3D rigidity/Hessian audit of the cuboctahedral Jitterbug linkage.

Uses the repository's canonical 12-joint ordering, 24 unit rods and eight
sign-triple triangular panels. This is a central-force, stress-free linear
mechanics benchmark, not a material phonon/phason model.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from audits.jitterbug_gray_kinematics import cuboctahedron, edge_list, rigid_triangles


def rigidity_matrix(vertices: np.ndarray, edges: list[tuple[int, int]]) -> np.ndarray:
    """Linearized unit-rod extension map, one row per unoriented rod."""
    n = len(vertices)
    matrix = np.zeros((len(edges), 3 * n), dtype=float)
    for row, (i, j) in enumerate(edges):
        delta = vertices[i] - vertices[j]
        length = np.linalg.norm(delta)
        if not np.isclose(length, 1.0, atol=1e-12, rtol=0):
            raise ValueError("reference rods must have unit length")
        direction = delta / length
        matrix[row, 3*i:3*i+3] = direction
        matrix[row, 3*j:3*j+3] = -direction
    return matrix


def rigid_body_basis(vertices: np.ndarray) -> np.ndarray:
    """Orthonormal basis for three translations and three infinitesimal rotations."""
    centered = vertices - vertices.mean(axis=0)
    candidates = []
    for axis in np.eye(3):
        candidates.append(np.tile(axis, (len(vertices), 1)).reshape(-1))
    for axis in np.eye(3):
        candidates.append(np.cross(np.tile(axis, (len(vertices), 1)), centered).reshape(-1))
    q, r = np.linalg.qr(np.column_stack(candidates))
    return q[:, :6]


def audit() -> dict:
    vertices = cuboctahedron()
    edges = sorted(tuple(map(int, e)) for e in edge_list(vertices))
    panels = rigid_triangles(vertices)
    panel_edges = set()
    for indices in panels.values():
        for a, b in ((0, 1), (1, 2), (2, 0)):
            panel_edges.add(tuple(sorted((indices[a], indices[b]))))
    if panel_edges != set(edges):
        raise AssertionError("the eight triangular panels must cover the 24 rods exactly")

    R = rigidity_matrix(vertices, edges)
    K = R.T @ R
    singular = np.linalg.svd(R, compute_uv=False)
    rank = int(np.sum(singular > 1e-10 * singular[0]))
    eigenvalues = np.linalg.eigvalsh(K)
    positive = eigenvalues[eigenvalues > 1e-9]
    zero_count = int(np.sum(eigenvalues <= 1e-9))

    rigid = rigid_body_basis(vertices)
    rigid_residual = float(np.linalg.norm(R @ rigid, ord="fro"))
    projected = np.eye(36) - rigid @ rigid.T
    projected_rank = int(np.linalg.matrix_rank(R @ projected, tol=1e-9))

    panel_contacts = []
    labels = list(panels)
    for i, left in enumerate(labels):
        for j in range(i + 1, len(labels)):
            right = labels[j]
            shared = len(set(panels[left]) & set(panels[right]))
            if shared:
                panel_contacts.append((left, right, shared))
    contact_hamming = sorted(
        sum(a != b for a, b in zip(left, right))
        for left, right, shared in panel_contacts
    )
    if len(vertices) != 12 or len(edges) != 24 or len(panels) != 8:
        raise AssertionError("unexpected Jitterbug combinatorics")
    if rank != 24 or zero_count != 12 or projected_rank != 24:
        raise AssertionError("unexpected rigidity rank or mechanism count")
    if rigid_residual > 1e-10 or len(panel_contacts) != 12 or contact_hamming != [1] * 12:
        raise AssertionError("rigid-body or panel-contact certificate failed")

    expected = np.array(
        [2-np.sqrt(2)]*3 + [1.0]*5 + [2.0]*9 + [3.0]*3
        + [2+np.sqrt(2)]*3 + [4.0]
    )
    if not np.allclose(positive, expected, atol=2e-9, rtol=0):
        raise AssertionError("positive Hessian spectrum changed")

    return {
        "model": "12-joint cuboctahedral Jitterbug, 24 unit central-force rods",
        "classification": {
            "exact_combinatorics": "[P]",
            "linearized_spectrum": "[N]",
            "physical_phonon_phason_identification": "[O]",
        },
        "vertices": len(vertices),
        "rods": len(edges),
        "triangular_panels": len(panels),
        "panel_union_equals_rod_set": True,
        "panel_shared_vertex_contacts": len(panel_contacts),
        "panel_contact_hamming_distances": contact_hamming,
        "degrees_of_freedom": 36,
        "rigidity_rank": rank,
        "hessian_rank": rank,
        "nullity": zero_count,
        "rigid_body_zero_modes": 6,
        "internal_mechanisms": zero_count - 6,
        "rigid_body_residual_frobenius": rigid_residual,
        "positive_hessian_eigenvalues": [
            {"value": float(value), "multiplicity": int(np.sum(np.isclose(positive, value, atol=2e-9, rtol=0)))}
            for value in np.unique(np.round(positive, 10))
        ],
        "positive_spectrum_exact_form": {
            "2-sqrt(2)": 3, "1": 5, "2": 9, "3": 3,
            "2+sqrt(2)": 3, "4": 1,
        },
        "interpretation": (
            "The 24-rod framework has six non-rigid infinitesimal mechanisms "
            "in addition to six rigid-body modes. It is not a positive-definite "
            "phonon Hessian and supplies no physical phason sector or viscosity."
        ),
    }


def main() -> None:
    report = audit()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
