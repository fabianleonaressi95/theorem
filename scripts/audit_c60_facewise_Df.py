#!/usr/bin/env python3
"""Construct the facewise D_f field and candidate structured field on ideal C60.

This is an algebraic/geometric construction on the exact truncated icosahedron.
It does NOT establish Del Piero--Owen admissibility: the classical equal-dimension
determinant condition is not directly applicable to the 3x2 immersion gradients.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import deque
from pathlib import Path

import numpy as np

from audit_c60_mmff94s_relaxed_coulomb import c60_ideal
from audit_c60_icosahedral_connection import (
    reconstruct_faces, normals_for_faces, face_frames, connection_data, unit,
)


def dual_tree(face_count, transports, root=0):
    adjacency = [[] for _ in range(face_count)]
    for f, g in transports:
        adjacency[f].append(g)
    parent = {root: None}
    order = [root]
    queue = deque([root])
    while queue:
        f = queue.popleft()
        for g in sorted(adjacency[f]):
            if g not in parent:
                parent[g] = f
                order.append(g)
                queue.append(g)
    if len(order) != face_count:
        raise RuntimeError(f"Dual graph disconnected: reached {len(order)}/{face_count} faces.")
    return parent, order


def build_D(parent, order, transports):
    D = {order[0]: np.eye(2)}
    for g in order[1:]:
        f = parent[g]
        D[g] = transports[(f, g)] @ D[f]
    return D


def vertex_holonomies(x, faces, transports):
    incident = [[] for _ in range(len(x))]
    for fi, face in enumerate(faces):
        for v in face:
            incident[v].append(fi)
    rows = []
    for v, fs in enumerate(incident):
        if len(fs) != 3:
            raise RuntimeError(f"Vertex {v} has {len(fs)} incident faces, expected 3.")
        radial = unit(x[v])
        seed = np.eye(3)[int(np.argmin(np.abs(radial)))]
        e1 = unit(seed - radial * (seed @ radial))
        e2 = np.cross(radial, e1)
        center = x[v]
        ordered = sorted(
            fs,
            key=lambda f: np.arctan2(
                (np.mean(x[list(faces[f])], axis=0) - center) @ e2,
                (np.mean(x[list(faces[f])], axis=0) - center) @ e1,
            ),
        )
        f0, f1, f2 = ordered
        H = transports[(f2, f0)] @ transports[(f1, f2)] @ transports[(f0, f1)]
        angle = float(np.arctan2(H[1, 0], H[0, 0]))
        rows.append({
            "vertex": int(v),
            "faces_cycle": [int(f0), int(f1), int(f2)],
            "holonomy_matrix": H.tolist(),
            "angle_rad": angle,
            "angle_deg": float(np.degrees(angle)),
            "absolute_defect_error_deg": float(abs(abs(np.degrees(angle)) - 12.0)),
        })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="c60_facewise_Df_audit")
    args = ap.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    x, _ = c60_ideal()
    faces, _ = reconstruct_faces(x)
    normals = normals_for_faces(x, faces)
    incidence, frames, transports, L, edge_mismatch, det_res, J_res = connection_data(
        x, faces, normals
    )
    if len(faces) != 32 or len(x) != 60 or len(incidence) != 90:
        raise RuntimeError("Unexpected truncated-icosahedron topology.")

    root = 0
    parent, order = dual_tree(len(faces), transports, root=root)
    D = build_D(parent, order, transports)

    # Facewise immersion gradient: B_f is 3x2, rank two.
    # Candidate G_f = B_f D_f is therefore also 3x2.
    # M_f = grad(g)_f - G_f = B_f(I-D_f).
    records = []
    max_orth = 0.0
    max_tree_res = 0.0
    max_rank_res = 0.0
    for f in range(len(faces)):
        B = frames[f]
        Df = D[f]
        Gf = B @ Df
        Mf = B - Gf
        max_orth = max(max_orth, float(np.linalg.norm(Df.T @ Df - np.eye(2))))
        max_tree_res = max(max_tree_res, float(np.linalg.norm(B.T @ Gf - Df)))
        max_rank_res = max(max_rank_res, float(np.linalg.norm(B.T @ B - np.eye(2))))
        records.append({
            "face": f,
            "n_vertices": len(faces[f]),
            "parent": parent[f],
            "D11": Df[0, 0], "D12": Df[0, 1],
            "D21": Df[1, 0], "D22": Df[1, 1],
            "G11": Gf[0, 0], "G12": Gf[0, 1],
            "G21": Gf[1, 0], "G22": Gf[1, 1],
            "G31": Gf[2, 0], "G32": Gf[2, 1],
            "M11": Mf[0, 0], "M12": Mf[0, 1],
            "M21": Mf[1, 0], "M22": Mf[1, 1],
            "M31": Mf[2, 0], "M32": Mf[2, 1],
        })

    vertex_data = vertex_holonomies(x, faces, transports)
    max_vertex_error = max(row["absolute_defect_error_deg"] for row in vertex_data)
    if max_orth > 1e-10 or max_tree_res > 1e-10 or max_rank_res > 1e-10:
        raise RuntimeError("Matrix construction residual exceeds tolerance.")
    if max_vertex_error > 1e-6:
        raise RuntimeError(f"Vertex holonomy is not 12 degrees: max error {max_vertex_error}.")

    # Arrays use face index as first axis; preserve exact dimensions.
    Darr = np.stack([D[f] for f in range(len(faces))])
    Barr = np.stack(frames)
    Garr = np.einsum("fai,fij->faj", Barr, Darr)
    Marr = Barr - Garr
    np.savez_compressed(
        out / "C60_facewise_Df_Gf_Mf.npz",
        X=x,
        face_vertices=np.concatenate([np.asarray(f, int) for f in faces]),
        face_offsets=np.cumsum([0] + [len(f) for f in faces]),
        face_normals=normals,
        face_frames= Barr,
        D_f=Darr,
        grad_g=Barr,
        G_f=Garr,
        M_f=Marr,
        connection_laplacian=L,
    )
    with (out / "C60_facewise_Df_Gf_Mf.csv").open("w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    (out / "vertex_holonomies.json").write_text(json.dumps(vertex_data, indent=2) + "\n")

    report = {
        "status": "constructed_candidate_not_DPO_admissibility_proof",
        "geometry": {"vertices": 60, "edges": 90, "faces": 32, "pentagons": 12, "hexagons": 20},
        "tree": {"root_face": root, "reached_faces": len(order), "parent_by_face": parent},
        "dimensions": {"D_f": [32, 2, 2], "grad_g": [32, 3, 2], "G_f": [32, 3, 2], "M_f": [32, 3, 2]},
        "definitions": {
            "D_root": "I_2",
            "D_child": "A_parent,child @ D_parent",
            "grad_g_f": "B_f (3x2 face tangent frame)",
            "G_f": "B_f @ D_f",
            "M_f": "B_f - G_f = B_f @ (I_2 - D_f)",
        },
        "residuals": {
            "max_D_orthogonality": max_orth,
            "max_tree_transport_identity": max_tree_res,
            "max_face_frame_orthonormality": max_rank_res,
            "max_vertex_defect_error_degrees": max_vertex_error,
            "max_edge_transport_SO2_determinant": det_res,
            "max_edge_direction_mismatch": edge_mismatch,
            "connection_complex_structure_commutator": J_res,
        },
        "vertex_holonomies": vertex_data,
        "limitations": [
            "D_f depends on the chosen dual spanning tree and root; it is a gauge-dependent face field.",
            "The vertex holonomy is gauge invariant up to conjugacy; the facewise D_f matrices are not.",
            "grad(g), G and M are 3x2 because this is an immersion of a planar face into R3.",
            "The classical Del Piero-Owen equal-dimensional determinant accommodation condition cannot be copied to these rectangular matrices.",
            "No global injective planar development g or determining sequence of injective approximants is constructed here.",
            "Consequently this audit constructs candidate matrices and verifies the discrete connection, not a theorem of structured-deformation admissibility.",
        ],
    }
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
