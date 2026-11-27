#!/usr/bin/env python3
"""Measure face-graph locality of the existing Q6 -> C60 V4 intertwiner.

This is a diagnostic of the deterministic projector-built intertwiner from the
V4 audit. It does not optimize over the O(16)^4 freedom in the four isotypic
sectors, so a dense result is not a no-go theorem for every possible
V4-equivariant intertwiner.
"""
import argparse
import json
from pathlib import Path
import sys

import numpy as np
from scipy.spatial import ConvexHull

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_q6_c60_v4_equivariance import (  # noqa: E402
    PHI, TOL, a4_subgroup, coordinate_a4, c60_faces, ico_vertices,
    icosahedral_rotations, matrix_key, orthogonal_intertwiner,
    q6_state_representation, tangent_bases, v4_from_a4,
)


def truncated_c60_face_vertex_sets(V):
    hull = ConvexHull(V)
    edges = set()
    for tri in hull.simplices:
        for k in range(3):
            edges.add(tuple(sorted((int(tri[k]), int(tri[(k + 1) % 3])))))
    points = []
    for a, b in sorted(edges):
        points.extend(((2 * V[a] + V[b]) / 3.0, (V[a] + 2 * V[b]) / 3.0))
    points = np.asarray(points)
    hull = ConvexHull(points)
    planes = {}
    for eq in hull.equations:
        n = eq[:3] / np.linalg.norm(eq[:3])
        d = eq[3] / np.linalg.norm(eq[:3])
        planes[matrix_key(np.r_[n, d])] = (n, d)
    faces = []
    for n, d in planes.values():
        ids = tuple(np.flatnonzero(np.abs(points @ n + d) < 1e-7).tolist())
        if len(ids) in (5, 6):
            faces.append((n, d, ids))
    faces.sort(key=lambda f: matrix_key(np.r_[f[0], f[1]]))
    if len(faces) != 32:
        raise RuntimeError(f"Expected 32 C60 faces, got {len(faces)}")
    return points, faces


def face_adjacency(faces):
    A = np.zeros((len(faces), len(faces)), dtype=np.int8)
    for i in range(len(faces)):
        si = set(faces[i][2])
        for j in range(i + 1, len(faces)):
            # Two truncated-icosahedron faces are adjacent iff they share
            # exactly one polygon edge (two vertices).
            if len(si.intersection(faces[j][2])) == 2:
                A[i, j] = A[j, i] = 1
    return A


def main(npz_path, out_path, matrices_path):
    z = np.load(npz_path, allow_pickle=False)
    X = np.asarray(z["X_Oh_reconstructed"], float)
    Aq = np.asarray(z["Q6_adjacency"], float)
    if X.shape != (64, 3) or Aq.shape != (64, 64):
        raise RuntimeError(f"Unexpected Q6 shapes: X={X.shape}, adjacency={Aq.shape}")

    q4 = v4_from_a4(coordinate_a4(X))
    qreps = [q6_state_representation(p) for _, p in q4]
    rotations = icosahedral_rotations(ico_vertices())
    a4 = a4_subgroup(rotations)
    eye = np.eye(3)
    v4rot = [R for R in a4 if np.allclose(R, eye, atol=1e-7)
             or np.allclose(R @ R, eye, atol=1e-7)]
    v4rot.sort(key=lambda R: (0 if np.allclose(R, eye, atol=1e-7) else 1,
                              matrix_key(R)))
    if len(v4rot) != 4:
        raise RuntimeError(f"Expected C60 V4, got {len(v4rot)}")

    V = ico_vertices()
    points, faces = truncated_c60_face_vertex_sets(V)
    face_normals = np.asarray([f[0] for f in faces])
    face_basis = tangent_bases(face_normals)
    # Rebuild the C60 face-fibre representation using the same ordered faces.
    freps = []
    for R in v4rot:
        moved = face_normals @ R.T
        dist = np.linalg.norm(moved[:, None, :] - face_normals[None, :, :], axis=2)
        target = dist.argmin(axis=1)
        if dist[np.arange(32), target].max() > 1e-6 or len(set(target.tolist())) != 32:
            raise RuntimeError("C60 V4 does not permute the 32 face normals")
        F = np.zeros((64, 64))
        for i, j in enumerate(target):
            F[2*j:2*j+2, 2*i:2*i+2] = face_basis[j].T @ R @ face_basis[i]
        freps.append(F)

    O, multiplicities, orth_res, intertwine_res = orthogonal_intertwiner(qreps, freps)
    Af = face_adjacency(faces)
    degrees = Af.sum(axis=1)
    if sorted(degrees.tolist()).count(5) != 12 or sorted(degrees.tolist()).count(6) != 20:
        raise RuntimeError(f"Unexpected C60 face adjacency degrees: {degrees.tolist()}")

    # Conjugate the archived Q6 graph adjacency into the C60 face-fibre basis.
    Df = O @ Aq @ O.T
    block_norms = np.zeros((32, 32))
    for i in range(32):
        for j in range(32):
            block_norms[i, j] = np.linalg.norm(Df[2*i:2*i+2, 2*j:2*j+2], ord="fro")

    thresholds = [1e-12, 1e-10, 1e-8, 1e-6, 1e-4, 1e-2]
    sparsity = {}
    offdiag_energy = float(np.sum(block_norms**2) - np.sum(np.diag(block_norms)**2))
    nonadj_energy = float(np.sum(block_norms[Af == 0]**2) - np.sum(np.diag(block_norms)**2))
    adjacent_energy = float(np.sum(block_norms[Af == 1]**2))
    for tol in thresholds:
        support = block_norms > tol
        total = int(support.sum())
        adjacent = int(np.sum(support * Af))
        nonadjacent = int(np.sum(support * (1 - Af - np.eye(32, dtype=np.int8))))
        sparsity[f"{tol:.0e}"] = {
            "nonzero_2x2_blocks": total,
            "diagonal_blocks": int(np.trace(support)),
            "adjacent_face_blocks": adjacent,
            "nonadjacent_offdiagonal_blocks": nonadjacent,
            "adjacent_edge_coverage": float(adjacent / Af.sum()),
            "nonadjacent_fraction_of_offdiagonal_support": float(
                nonadjacent / max(total - int(np.trace(support)), 1)
            ),
        }

    report = {
        "classification": "numerical locality diagnostic for one explicit V4 intertwiner",
        "source_archive": str(npz_path),
        "Q6_operator": "archived Q6_adjacency (64x64)",
        "transport": "D_C60 = Phi D_Q6 Phi^T, with Phi the projector-built orthogonal V4 intertwiner",
        "face_inventory": {
            "faces": 32,
            "pentagons": int(sum(len(f[2]) == 5 for f in faces)),
            "hexagons": int(sum(len(f[2]) == 6 for f in faces)),
            "face_adjacency_edges": int(Af.sum() // 2),
            "degree_counts": {"5": int(np.sum(degrees == 5)), "6": int(np.sum(degrees == 6))},
        },
        "intertwiner": {
            "shape": list(O.shape),
            "orthogonality_residual": orth_res,
            "max_V4_intertwining_residual": max(intertwine_res),
            "isotypic_multiplicities": multiplicities,
        },
        "transported_operator": {
            "shape": list(Df.shape),
            "symmetry_residual": float(np.linalg.norm(Df - Df.T)),
            "frobenius_norm": float(np.linalg.norm(Df)),
            "block_support_thresholds": sparsity,
            "adjacent_block_frobenius_energy_fraction": float(
                adjacent_energy / max(adjacent_energy + nonadj_energy, 1e-30)
            ),
            "nonadjacent_offdiagonal_frobenius_energy_fraction": float(
                nonadj_energy / max(offdiag_energy, 1e-30)
            ),
            "max_block_norm": float(block_norms.max()),
            "median_nonadjacent_block_norm": float(np.median(block_norms[Af == 0])),
        },
        "basis_dependence": (
            "The four V4 isotypic sectors each have multiplicity 16. The reported "
            "intertwiner is the deterministic eigensolver/projector choice from the "
            "previous audit; this run does not optimize over the O(16)^4 freedom. "
            "Therefore observed nonlocality is a property of this explicit intertwiner, "
            "not a no-go theorem for all V4 intertwiners."
        ),
        "conclusion": (
            "The current explicit V4 intertwiner transports Q6 adjacency to a 64D "
            "operator on C60 face fibres. Locality is quantified against actual "
            "truncated-icosahedron face adjacency. No canonical or optimized local "
            "intertwiner is established by this diagnostic."
        ),
    }
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    Path(matrices_path).parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(matrices_path, face_adjacency=Af, transported_Q6_adjacency=Df,
                        face_block_frobenius_norms=block_norms,
                        intertwiner_Q6_to_C60=O)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("npz", nargs="?", default="data/RGS_PSU_all_matrices.npz")
    parser.add_argument("--out", default="audits/Q6_C60_V4_locality.json")
    parser.add_argument("--matrices", default="artifacts/Q6_C60_V4_locality.npz")
    args = parser.parse_args()
    main(args.npz, args.out, args.matrices)
