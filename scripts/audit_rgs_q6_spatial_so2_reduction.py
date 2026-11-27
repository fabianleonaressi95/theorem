#!/usr/bin/env python3
"""Audit the 3D spatial bundle and SO(2) reduction of the archived Q6 links.

Input is the recovered psu_fibre_connection_matrices.npz from A13.
This tests only the finite graph construction. It does not claim a continuum
spacetime tetrad, a Levi-Civita spin connection, or a continuum limit.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np


def fro(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord="fro"))


def audit(path: Path) -> dict:
    with np.load(path, allow_pickle=False) as z:
        required = ("X", "Q", "edges", "R_SO3", "U_SU2")
        missing = [k for k in required if k not in z.files]
        if missing:
            raise KeyError(f"Missing arrays: {missing}")
        X = np.asarray(z["X"], float)
        Q = np.asarray(z["Q"], float)
        edges = np.asarray(z["edges"], int)
        R = np.asarray(z["R_SO3"], float)
        U = np.asarray(z["U_SU2"], complex)

    if X.shape != (64, 3) or Q.shape != (192, 188):
        raise ValueError(f"Unexpected X/Q shapes: {X.shape}, {Q.shape}")
    if edges.shape != (192, 3) or R.shape != (192, 3, 3) or U.shape != (192, 2, 2):
        raise ValueError("Unexpected Q6 edge/transport shapes")

    radii = np.linalg.norm(X, axis=1)
    if np.any(radii <= 1e-14):
        raise ValueError("A zero vertex vector prevents defining n_g=X_g/|X_g|")
    n = X / radii[:, None]
    I3 = np.eye(3)
    sigma = np.array([
        [[0, 1], [1, 0]],
        [[0, -1j], [1j, 0]],
        [[1, 0], [0, -1]],
    ], dtype=complex)

    # Check the exact finite-graph transport law and induced transverse planes.
    orth = []
    det = []
    normal_transport = []
    plane_transport = []
    adjoint = []
    edge_lengths = []
    edge_map = {}
    for k, (g, h, axis) in enumerate(edges):
        Rk, Uk = R[k], U[k]
        orth.append(fro(Rk.T @ Rk - I3))
        det.append(abs(float(np.linalg.det(Rk)) - 1.0))
        normal_transport.append(float(np.linalg.norm(Rk @ n[g] - n[h])))
        Pg = I3 - np.outer(n[g], n[g])
        Ph = I3 - np.outer(n[h], n[h])
        plane_transport.append(fro(Rk @ Pg @ Rk.T - Ph))
        R_from_U = np.empty((3, 3))
        for j in range(3):
            transformed = Uk @ sigma[j] @ Uk.conj().T
            R_from_U[:, j] = [float(np.real(np.trace(sigma[i] @ transformed) / 2)) for i in range(3)]
        adjoint.append(fro(R_from_U - Rk))
        dx = X[h] - X[g]
        dr = radii[h] - radii[g]
        edge_lengths.append(float(np.linalg.norm(dx)))
        edge_map[(int(g), int(h))] = (Rk, Uk)
        edge_map[(int(h), int(g))] = (Rk.T, Uk.conj().T)

    # Q6 elementary square holonomies; each must fix the selected n at its base.
    holonomy_fix = []
    holonomy_plane = []
    holonomy_so3 = []
    holonomy_u1 = []
    for a in range(6):
        for b in range(a + 1, 6):
            for g in range(64):
                if ((g >> a) & 1) or ((g >> b) & 1):
                    continue
                i = g
                j = g ^ (1 << a)
                k = j ^ (1 << b)
                l = g ^ (1 << b)
                # Column-vector transport: the next edge acts on the left.
                H = (edge_map[(l, i)][0] @ edge_map[(k, l)][0]
                     @ edge_map[(j, k)][0] @ edge_map[(i, j)][0])
                Hu = (edge_map[(l, i)][1] @ edge_map[(k, l)][1]
                      @ edge_map[(j, k)][1] @ edge_map[(i, j)][1])
                P = np.outer(n[i], n[i])
                holonomy_so3.append(fro(H.T @ H - I3))
                holonomy_fix.append(float(np.linalg.norm(H @ n[i] - n[i])))
                holonomy_plane.append(fro(H @ P - P @ H))
                sigma_n = np.einsum("a,aij->ij", n[i], sigma)
                holonomy_u1.append(fro(Hu @ sigma_n - sigma_n @ Hu))

    # The augmented coframe is the edge secant of F(X)=(X, |X|).
    # Its differential has rank exactly 3 for X != 0:
    # DF^T DF = I_3 + n n^T, with eigenvalues (1,1,2).
    metric_eigs = np.array([1.0, 1.0, 2.0])
    spatial_edge_rank = int(np.linalg.matrix_rank(X[edges[:, 1]] - X[edges[:, 0]]))
    centered_rank = int(np.linalg.matrix_rank(X - X.mean(axis=0)))

    # Compare the graph connection's radial unit section with the A14
    # fixed-radius normal field, whose vertex blocks are X_g/||vec(X)||.
    global_radius = float(np.linalg.norm(X))
    A14_radial_parallel_defect = []
    for g, h, _ in edges:
        Rk = edge_map[(int(g), int(h))][0]
        A14_radial_parallel_defect.append(
            float(np.linalg.norm(X[h] - Rk @ X[g]) / global_radius)
        )

    residuals = {
        "centered_embedding_rank": centered_rank,
        "spatial_edge_displacement_rank": spatial_edge_rank,
        "SO3_orthogonality_max_fro": max(orth),
        "SO3_determinant_max_abs": max(det),
        "SO3_normal_section_transport_max": max(normal_transport),
        "SO3_transverse_plane_transport_max_fro": max(plane_transport),
        "SU2_adjoint_SO3_max_fro": max(adjoint),
        "plaquette_count": len(holonomy_fix),
        "plaquette_holonomy_fixes_n_max": max(holonomy_fix),
        "plaquette_holonomy_preserves_transverse_plane_max_fro": max(holonomy_plane),
        "SU2_plaquette_holonomy_U1_commutator_max_fro": max(holonomy_u1),
        "A14_fixed_radius_radial_section_parallel_defect_max": max(A14_radial_parallel_defect),
        "radius_min": float(radii.min()),
        "radius_max": float(radii.max()),
        "edge_spatial_length_min": min(edge_lengths),
        "edge_spatial_length_max": max(edge_lengths),
    }

    checks = {
        "3D_embedding_rank_3": centered_rank == 3,
        "spatial_edge_displacements_span_R3": spatial_edge_rank == 3,
        "SO3_links": residuals["SO3_orthogonality_max_fro"] < 1e-10 and residuals["SO3_determinant_max_abs"] < 1e-10,
        "unit_normal_is_parallel": residuals["SO3_normal_section_transport_max"] < 1e-10,
        "transverse_rank2_planes_are_preserved": residuals["SO3_transverse_plane_transport_max_fro"] < 1e-10,
        "SU2_is_lift_of_SO3": residuals["SU2_adjoint_SO3_max_fro"] < 1e-10,
        "all_240_plaquettes_fix_n": residuals["plaquette_count"] == 240 and residuals["plaquette_holonomy_fixes_n_max"] < 1e-9,
        "plaquette_holonomies_preserve_plane": residuals["plaquette_holonomy_preserves_transverse_plane_max_fro"] < 1e-9,
        "SU2_holonomies_reduce_to_U1": residuals["SU2_plaquette_holonomy_U1_commutator_max_fro"] < 1e-9,
    }

    return {
        "title": "RGS/Q6 finite-graph spatial bundle and SO(2) reduction audit",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": {
            "embedded_discrete_spatial_geometry_R3": "PASS" if checks["3D_embedding_rank_3"] and checks["spatial_edge_displacements_span_R3"] else "FAIL",
            "edgewise_SO3_connection_preserving_unit_normal": "PASS" if checks["unit_normal_is_parallel"] else "FAIL",
            "SO3_bundle_reduction_to_SO2": "PASS" if all(checks[k] for k in ("unit_normal_is_parallel", "transverse_rank2_planes_are_preserved", "all_240_plaquettes_fix_n")) else "FAIL",
            "SU2_lift_reduction_to_U1": "PASS" if checks["SU2_holonomies_reduce_to_U1"] else "FAIL",
            "A14_188D_constraint_sphere_Levi_Civita_identified_with_link_connection": "NOT_ESTABLISHED",
            "four_dimensional_Lorentzian_spacetime_or_time_direction": "NOT_ESTABLISHED",
            "continuum_limit": "NOT_TESTED",
        },
        "geometry": {
            "base_graph": "Q6 with 64 vertices, 192 edges, 240 square plaquettes",
            "spatial_embedding": "X: Q6 vertices -> R^3",
            "unit_normal_section": "n_g = X_g / ||X_g||",
            "link_law": "R_gh n_g = n_h",
            "fibre_decomposition": "R^3 = span(n_g) orthogonal_sum n_g_perp",
            "reduced_structure_group": "SO(2) on the transverse rank-2 planes",
            "spin_lift_stabilizer": "U(1) in SU(2)",
            "augmented_coframe_map": "F(X)=(X,||X||), X != 0; dF has rank 3 and metric I+n n^T",
            "dF_metric_eigenvalues": metric_eigs.tolist(),
            "A14_radial_normal": "vec(X)/||vec(X)||, not the vertexwise unit section n_g",
        },
        "residuals": residuals,
        "checks": checks,
        "scope": [
            "This is a finite-graph Euclidean rank-3 bundle reduction, not a continuum spacetime construction.",
            "The selected radial unit section is parallel for the declared minimal-rotation links.",
            "The link connection preserves the orthogonal rank-2 planes and all plaquette holonomies lie in the SO(2) stabilizer at their base vertex.",
            "The SU(2) lift correspondingly has U(1) plaquette holonomy stabilizer.",
            "The A14 fixed-radius normal field is not the same section as the vertexwise unit directions unless all vertex radii are equal.",
            "No identification with the induced Levi-Civita connection on S^188(sqrt(240)) is claimed.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path, help="psu_fibre_connection_matrices.npz")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit(args.archive)
    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
