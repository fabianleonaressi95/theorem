#!/usr/bin/env python3
"""Finite Q6 golden-vector, PSU non-overlap and SU(2) spin-lift audit.

This audit does NOT identify the 64 Q6 vectors with the 64 tetrahedra of the
ISF/Haramein IVM illustration: a coordinate/incidence dataset for that grid
must be supplied before an equivariant comparison can be made.
Only NumPy is required.
"""
from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

import numpy as np

PHI = (1.0 + np.sqrt(5.0)) / 2.0
I2 = np.eye(2, dtype=np.complex128)
SIGMA = np.asarray([
    [[0, 1], [1, 0]],
    [[0, -1j], [1j, 0]],
    [[1, 0], [0, -1]],
], dtype=np.complex128)


def golden_axes(parameter: float = PHI) -> np.ndarray:
    """Six normalized icosahedral axes, with algebraic conjugate parameter allowed."""
    p = float(parameter)
    raw = np.asarray([
        (0, 1, p), (0, 1, -p),
        (1, p, 0), (1, -p, 0),
        (p, 0, 1), (p, 0, -1),
    ], dtype=float)
    return raw / np.linalg.norm(raw, axis=1)[:, None]


def golden_projection_matrices() -> tuple[np.ndarray, np.ndarray]:
    """Return the T129 physical/internal 3x6 golden projections."""
    phi_star = (1.0 - np.sqrt(5.0)) / 2.0

    def A(p: float) -> np.ndarray:
        return np.asarray([
            [0.0, 0.0, 1.0, -1.0, p, p],
            [1.0, -1.0, p, p, 0.0, 0.0],
            [p, p, 0.0, 0.0, 1.0, -1.0],
        ], dtype=float)

    p_parallel = A(PHI) / np.sqrt(2.0 * (2.0 + PHI))
    p_internal = A(phi_star) / np.sqrt(2.0 * (2.0 + phi_star))
    return p_parallel, p_internal


def q6_vectors() -> tuple[np.ndarray, np.ndarray]:
    """Return bit labels and F(b)=sum_i (-1)^b_i n_i, in binary order."""
    bits = np.asarray([[(v >> i) & 1 for i in range(6)]
                       for v in range(64)], dtype=np.int8)
    signs = 1.0 - 2.0 * bits
    return bits, signs @ golden_axes()


def q6_edges() -> list[tuple[int, int, int]]:
    return [(g, g ^ (1 << axis), axis)
            for g in range(64) for axis in range(6)
            if ((g >> axis) & 1) == 0]


def qmul(q: np.ndarray, p: np.ndarray) -> np.ndarray:
    a, u = float(q[0]), q[1:]
    b, v = float(p[0]), p[1:]
    return np.r_[a*b - np.dot(u, v), a*v + b*u + np.cross(u, v)]


def qconj(q: np.ndarray) -> np.ndarray:
    return np.r_[q[0], -q[1:]]


def qnormalize(q: np.ndarray) -> np.ndarray:
    n = float(np.linalg.norm(q))
    if n < 1e-14:
        raise ValueError("zero quaternion")
    return q / n


def shortest_spin_lift(source: np.ndarray, target: np.ndarray) -> np.ndarray:
    """Canonical SU(2) lift of the shortest rotation source -> target.

    q=(cos(theta/2), axis*sin(theta/2)); q0 >= 0 selects the shortest lift.
    Antipodal directions have no unique shortest axis and are rejected.
    """
    a = source / np.linalg.norm(source)
    b = target / np.linalg.norm(target)
    c = float(np.clip(np.dot(a, b), -1.0, 1.0))
    if 1.0 + c < 1e-12:
        raise ValueError("antipodal edge directions: shortest lift is ambiguous")
    q0 = np.sqrt((1.0 + c) / 2.0)
    qv = np.cross(a, b) / np.sqrt(2.0 * (1.0 + c))
    return qnormalize(np.r_[q0, qv])


def quaternion_to_so3(q: np.ndarray) -> np.ndarray:
    w, x, y, z = qnormalize(q)
    return np.asarray([
        [1-2*(y*y+z*z), 2*(x*y-z*w), 2*(x*z+y*w)],
        [2*(x*y+z*w), 1-2*(x*x+z*z), 2*(y*z-x*w)],
        [2*(x*z-y*w), 2*(y*z+x*w), 1-2*(x*x+y*y)],
    ])


def spinor_matrix(q: np.ndarray) -> np.ndarray:
    q = qnormalize(q)
    return q[0] * I2 - 1j * np.einsum("a,aij->ij", q[1:], SIGMA)


def q6_squares() -> list[tuple[int, int, int, int]]:
    faces = []
    for a in range(6):
        for b in range(a + 1, 6):
            for g in range(64):
                if ((g >> a) & 1) or ((g >> b) & 1):
                    continue
                j = g ^ (1 << a)
                k = j ^ (1 << b)
                ell = g ^ (1 << b)
                faces.append((g, j, k, ell))
    return faces


def _distance_spectrum(points: np.ndarray) -> np.ndarray:
    return np.asarray([np.linalg.norm(points[i] - points[j])
                       for i, j in combinations(range(len(points)), 2)])


def run_audit() -> dict:
    bits, points = q6_vectors()
    edges = q6_edges()

    # Exact bridge to T129: signed golden vectors are the physical/internal
    # projections of the centred Q6 cube, up to scale and a fixed bit relabelling.
    p_parallel, p_internal = golden_projection_matrices()
    centred = bits.astype(float) - 0.5
    x_parallel = centred @ p_parallel.T
    x_internal = centred @ p_internal.T
    bit_relabel_mask = 53  # axes 0,2,4,5 are complemented in this convention
    relabel = np.arange(64, dtype=np.int64) ^ bit_relabel_mask
    phi_star = (1.0 - np.sqrt(5.0)) / 2.0
    internal_points = (1.0 - 2.0 * bits) @ golden_axes(phi_star)
    projection_scale = 1.0 / (2.0 * np.sqrt(2.0))
    physical_projection_residual = float(np.max(
        np.linalg.norm(x_parallel - projection_scale * points[relabel], axis=1)
    ))
    internal_projection_residual = float(np.max(
        np.linalg.norm(x_internal - projection_scale * internal_points[relabel], axis=1)
    ))
    projected_distances = _distance_spectrum(x_parallel)
    radii = np.linalg.norm(points, axis=1)
    rounded_radii, shell_counts = np.unique(np.round(radii, 10), return_counts=True)
    distances = _distance_spectrum(points)
    edge_lengths = np.asarray([np.linalg.norm(points[h] - points[g])
                               for g, h, _ in edges])

    # The antipodal involution is bitwise complement b -> 1-b.
    antipodal_residual = max(float(np.linalg.norm(points[g] + points[g ^ 63]))
                             for g in range(64))
    unique_count = len(np.unique(np.round(points, 10), axis=0))

    # Lift each oriented Q6 edge; reverse links are quaternion inverses.
    links: dict[tuple[int, int], np.ndarray] = {}
    edge_unitarity = 0.0
    edge_adjoint = 0.0
    edge_angles = []
    for g, h, _ in edges:
        q = shortest_spin_lift(points[g], points[h])
        links[(g, h)] = q
        links[(h, g)] = qconj(q)
        U = spinor_matrix(q)
        edge_unitarity = max(edge_unitarity, float(np.linalg.norm(U.conj().T @ U - I2)))
        R = quaternion_to_so3(q)
        a = points[g] / np.linalg.norm(points[g])
        b = points[h] / np.linalg.norm(points[h])
        edge_adjoint = max(edge_adjoint, float(np.linalg.norm(R @ a - b)))
        edge_angles.append(2.0 * np.arctan2(np.linalg.norm(q[1:]), q[0]))

    # Compare SU(2) face products with their SO(3) projections on all 240 squares.
    face_projection_residual = 0.0
    face_spin_unitarity = 0.0
    face_identity_plus = 0
    face_identity_minus = 0
    face_count = 0
    for face in q6_squares():
        qface = np.asarray([1.0, 0.0, 0.0, 0.0])
        Rface = np.eye(3)
        loop = face + (face[0],)
        for u, v in zip(loop[:-1], loop[1:]):
            qlink = links[(u, v)]
            qface = qmul(qlink, qface)
            Rface = quaternion_to_so3(qlink) @ Rface
        qface = qnormalize(qface)
        face_projection_residual = max(
            face_projection_residual,
            float(np.linalg.norm(quaternion_to_so3(qface) - Rface)),
        )
        Uface = spinor_matrix(qface)
        face_spin_unitarity = max(
            face_spin_unitarity, float(np.linalg.norm(Uface.conj().T @ Uface - I2))
        )
        if np.linalg.norm(Rface - np.eye(3)) < 1e-9:
            if np.linalg.norm(qface - np.asarray([1., 0., 0., 0.])) < 1e-9:
                face_identity_plus += 1
            elif np.linalg.norm(qface + np.asarray([1., 0., 0., 0.])) < 1e-9:
                face_identity_minus += 1
        face_count += 1

    # PSU radius is l_P/2, hence non-overlap requires centre separation >= l_P.
    min_pair_distance = float(distances.min())
    lambda_min_over_lP = 1.0 / min_pair_distance
    min_projected_pair_distance = float(projected_distances.min())
    lambda_min_projected_over_lP = 1.0 / min_projected_pair_distance

    # Fundamental spin-1/2 representation: 2pi -> -I, 4pi -> +I.
    q_2pi = np.asarray([np.cos(np.pi), 0.0, 0.0, np.sin(np.pi)])
    q_4pi = np.asarray([np.cos(2*np.pi), 0.0, 0.0, np.sin(2*np.pi)])
    two_pi_residual = float(np.linalg.norm(spinor_matrix(q_2pi) + I2))
    four_pi_residual = float(np.linalg.norm(spinor_matrix(q_4pi) - I2))

    checks = {
        "64_distinct_vectors": unique_count == 64,
        "exact_T129_physical_projection_identity": physical_projection_residual < 1e-12,
        "exact_T129_internal_projection_identity": internal_projection_residual < 1e-12,
        "32_antipodal_pairs": antipodal_residual < 1e-12,
        "q6_has_192_edges": len(edges) == 192,
        "four_radial_shells_12_20_20_12": list(shell_counts) == [12, 20, 20, 12],
        "spin_links_unitary": edge_unitarity < 1e-12,
        "spin_links_project_to_so3": edge_adjoint < 1e-12,
        "all_240_faces_lifted": face_count == 240,
        "face_spin_products_project_correctly": face_projection_residual < 1e-12,
        "two_pi_spinor_sign": two_pi_residual < 1e-12,
        "four_pi_spinor_periodicity": four_pi_residual < 1e-12,
    }
    return {
        "status": "FINITE_Q6_GOLDEN_VECTOR_AND_SPIN_LIFT_AUDITED",
        "cut_project_correspondence": {
            "source": "T129 golden 6D -> physical/internal 3D projections of centred Q6 cube",
            "bit_relabel_mask_low_bit_first": bit_relabel_mask,
            "identity": "P_parallel*(b-1/2) = F_phi(b XOR 53)/(2*sqrt(2))",
            "internal_identity": "P_internal*(b-1/2) = F_phi_star(b XOR 53)/(2*sqrt(2))",
            "projection_scale": projection_scale,
            "physical_projection_residual_max": physical_projection_residual,
            "internal_projection_residual_max": internal_projection_residual,
        },
        "construction": {
            "carrier": "64 six-bit I Ching states; Hamming-1 Q6 adjacency",
            "vector_rule": "F(b)=sum_i (-1)^b_i n_i; n_i are six normalized icosahedral axes",
            "phi": float(PHI),
            "vertices": 64,
            "edges": len(edges),
            "square_faces": face_count,
            "distinct_vectors": unique_count,
            "antipodal_pairs": 32,
            "antipodal_residual_max": antipodal_residual,
        },
        "radial_shells": {
            "radii": [float(x) for x in rounded_radii],
            "counts": [int(x) for x in shell_counts],
        },
        "metric": {
            "all_pair_distance_min": min_pair_distance,
            "all_pair_distance_max": float(distances.max()),
            "q6_edge_length_min": float(edge_lengths.min()),
            "q6_edge_length_max": float(edge_lengths.max()),
            "q6_edge_length_mean": float(edge_lengths.mean()),
        },
        "psu_nonoverlap": {
            "psu_radius": "l_P/2 (Haramein 2013 convention)",
            "condition": "centre distance >= l_P",
            "scale_rule": "P_b=lambda*F(b)",
            "lambda_min_over_lP_for_F_coordinates": lambda_min_over_lP,
            "minimum_pair_distance_in_T129_physical_coordinates": min_projected_pair_distance,
            "lambda_min_over_lP_for_T129_physical_coordinates": lambda_min_projected_over_lP,
            "interpretation": "necessary non-overlap scale only; not a space-filling or physical derivation",
        },
        "spinorial_lift": {
            "group": "Spin(3)=SU(2), double cover of SO(3)",
            "representation": "U(q)=q0*I-i*q.sigma",
            "edge_link_unitarity_residual_max": edge_unitarity,
            "edge_adjoint_residual_max": edge_adjoint,
            "edge_rotation_angle_min_rad": float(np.min(edge_angles)),
            "edge_rotation_angle_max_rad": float(np.max(edge_angles)),
            "face_count": face_count,
            "face_SU2_to_SO3_projection_residual_max": face_projection_residual,
            "face_spinor_unitarity_residual_max": face_spin_unitarity,
            "identity_SO3_faces_with_plus_lift": face_identity_plus,
            "identity_SO3_faces_with_minus_lift": face_identity_minus,
            "two_pi_minus_identity_residual": two_pi_residual,
            "four_pi_plus_identity_residual": four_pi_residual,
        },
        "fuller_haramein_comparison": {
            "64_tetrahedron_grid_reported_in_ISF_presentation": True,
            "coordinate_dataset_for_64_tetrahedra_supplied": False,
            "equivariant_Q6_to_tetra_grid_match": "NOT_TESTED",
            "reason": "No machine-readable 64-tetrahedron vertex/centroid/incidence dataset was available in the inspected repository/source material.",
            "required_next_input": "64 tetrahedron centroids or vertices plus tetrahedron incidence/adjacency, with a declared coordinate convention.",
        },
        "checks": checks,
        "pass": all(checks.values()),
        "epistemic_limits": [
            "The 64 signed golden vectors are exactly the T129 physical projection of the centred Q6 cube, up to the stated scale and bit relabelling; they are not the 64 tetrahedron cells themselves.",
            "The reported 64-tetrahedron IVM grid is a distinct geometric construction; equivariance is untested.",
            "PSU non-overlap is a geometric necessary condition, not a packing, holographic, or quantum-gravity theorem.",
            "This is a spatial Spin(3) lift, not a Lorentzian Spin(1,3)=SL(2,C) spin bundle.",
            "No Dirac operator, fermionic dynamics, spin-statistics result, or physical particle interpretation is established.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="audits/Q6_IVM_PSU_SPINOR_AUDIT.json")
    args = parser.parse_args()
    result = run_audit()
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
