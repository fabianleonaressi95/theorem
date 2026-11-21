#!/usr/bin/env python3
"""Reconstruct the C60 face connection and decompose its spectrum under I_h.

The ideal cage is reconstructed from the icosahedron coordinates already used
by audit_c60_mmff94s_relaxed_coulomb.py. Coplanar ConvexHull triangles are
merged into the 12 pentagons and 20 hexagons. No precomputed face list is used.

The connection Laplacian acts on the 2D tangent fibre of each of the 32 faces
(64 real degrees of freedom). The full 120-element orthogonal group I_h acts
by permuting faces and transporting their tangent coordinates.

This is a numerical audit script. Its output, not this source file alone,
determines whether each test passes.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from itertools import permutations
from pathlib import Path

import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial import ConvexHull
from scipy.spatial.distance import cdist

from audit_c60_mmff94s_relaxed_coulomb import ico_vertices, c60_ideal

PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_BAR = (1.0 - np.sqrt(5.0)) / 2.0


def unit(x):
    x = np.asarray(x, float)
    n = np.linalg.norm(x)
    if n < 1.0e-14:
        raise ValueError("Cannot normalize a zero vector.")
    return x / n


def reconstruct_faces(x):
    """Merge coplanar triangular hull facets into polygonal C60 faces."""
    hull = ConvexHull(x)
    groups = []
    for tri in hull.simplices:
        pts = x[np.asarray(tri, int)]
        normal = unit(np.cross(pts[1] - pts[0], pts[2] - pts[0]))
        offset = float(normal @ pts[0])
        if offset < 0:
            normal, offset = -normal, -offset
        found = None
        for k, (n0, d0, verts) in enumerate(groups):
            if np.linalg.norm(normal - n0) < 1.0e-8 and abs(offset - d0) < 1.0e-8:
                found = k
                break
        if found is None:
            groups.append([normal, offset, set(map(int, tri))])
        else:
            groups[found][2].update(map(int, tri))

    faces = []
    normals = []
    for normal, offset, ids in groups:
        ids = sorted(ids)
        center = x[ids].mean(axis=0)
        # Construct a deterministic orthonormal frame in the face plane.
        seed = np.eye(3)[int(np.argmin(np.abs(normal)))]
        e1 = unit(seed - normal * (seed @ normal))
        e2 = np.cross(normal, e1)
        angles = [np.arctan2((x[i] - center) @ e2, (x[i] - center) @ e1) for i in ids]
        cycle = [ids[i] for i in np.argsort(angles)]
        poly_n = np.zeros(3)
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            poly_n += np.cross(x[a] - center, x[b] - center)
        if poly_n @ normal < 0:
            cycle.reverse()
        faces.append(tuple(cycle))
        normals.append(unit(normal))

    order = sorted(range(len(faces)), key=lambda i: (len(faces[i]), tuple(sorted(faces[i]))))
    faces = [faces[i] for i in order]
    normals = np.asarray([normals[i] for i in order])
    return faces, normals


def edge_face_incidence(faces):
    incidence = defaultdict(list)
    for fi, face in enumerate(faces):
        for a, b in zip(face, face[1:] + face[:1]):
            incidence[tuple(sorted((int(a), int(b))))].append(fi)
    return incidence


def normals_for_faces(x, faces):
    """Best-fit outward normals for fixed face cycles on a possibly relaxed cage."""
    out = []
    for face in faces:
        pts = x[np.asarray(face, int)]
        center = pts.mean(axis=0)
        _, _, vh = np.linalg.svd(pts - center, full_matrices=False)
        n = unit(vh[-1])
        if n @ center < 0:
            n = -n
        out.append(n)
    return np.asarray(out)


def face_frames(normals):
    frames = []
    for n in normals:
        seed = np.eye(3)[int(np.argmin(np.abs(n)))]
        b1 = unit(seed - n * (seed @ n))
        b2 = unit(np.cross(n, b1))
        frames.append(np.column_stack((b1, b2)))
    return frames


def connection_data(x, faces, normals):
    incidence = edge_face_incidence(faces)
    if len(incidence) != 90 or any(len(v) != 2 for v in incidence.values()):
        raise RuntimeError("C60 must have 90 edges, each incident to exactly two faces.")
    frames = face_frames(normals)
    transports = {}
    max_projected_edge_mismatch = 0.0
    for edge, fs in incidence.items():
        f, g = sorted(fs)
        a, b = edge
        edge_vector = x[b] - x[a]
        # For an ideal planar cage both projections coincide with the edge
        # tangent. On a relaxed, slightly non-planar face, project the same
        # physical edge direction into each best-fit face plane separately.
        Pf = np.eye(3) - np.outer(normals[f], normals[f])
        Pg = np.eye(3) - np.outer(normals[g], normals[g])
        tf = unit(Pf @ edge_vector)
        tg = unit(Pg @ edge_vector)
        max_projected_edge_mismatch = max(
            max_projected_edge_mismatch, float(np.linalg.norm(tf - tg))
        )
        mf = unit(np.cross(normals[f], tf))
        mg = unit(np.cross(normals[g], tg))
        T = np.outer(tg, tf) + np.outer(mg, mf)
        # Ambient partial-isometry identities.
        if np.linalg.norm(T.T @ T - Pf) > 2.0e-7:
            raise RuntimeError("Source-fibre isometry identity failed.")
        if np.linalg.norm(T @ T.T - Pg) > 2.0e-7:
            raise RuntimeError("Target-fibre isometry identity failed.")
        A = frames[g].T @ T @ frames[f]
        if np.linalg.norm(A.T @ A - np.eye(2)) > 2.0e-7:
            raise RuntimeError("Two-dimensional transport is not orthogonal.")
        transports[(f, g)] = A
        transports[(g, f)] = A.T

    # Connection Laplacian from sum_edges ||A_fg u_f-u_g||^2.
    L = np.zeros((2 * len(faces), 2 * len(faces)))
    for (f, g), A in transports.items():
        if f > g:
            continue
        sf, sg = slice(2*f, 2*f+2), slice(2*g, 2*g+2)
        L[sf, sf] += A.T @ A
        L[sg, sg] += np.eye(2)
        L[sf, sg] -= A.T
        L[sg, sf] -= A
    J2 = np.array([[0.0, -1.0], [1.0, 0.0]])
    J = np.kron(np.eye(len(faces)), J2)
    max_rotation_det_residual = max(
        abs(float(np.linalg.det(A)) - 1.0)
        for (f, g), A in transports.items() if f < g
    )
    complex_structure_residual = float(np.linalg.norm(L @ J - J @ L))
    return (incidence, frames, transports, L, max_projected_edge_mismatch,
            max_rotation_det_residual, complex_structure_residual)


def icosahedral_orthogonal_group():
    """Recover 120 I_h matrices from the Gram geometry of the icosahedron."""
    v = ico_vertices()
    src = v[[0, 1, 4]]
    gram = src @ src.T
    mats = []
    for idx in permutations(range(len(v)), 3):
        dst = v[list(idx)]
        if np.max(np.abs(dst @ dst.T - gram)) > 1.0e-8:
            continue
        u, _, vt = np.linalg.svd(src.T @ dst)
        O = u @ vt
        if np.max(np.min(cdist(v @ O, v), axis=1)) > 1.0e-7:
            continue
        if not any(np.linalg.norm(O - M, ord="fro") < 1.0e-7 for M in mats):
            mats.append(O)
    if len(mats) != 120:
        raise RuntimeError(f"Expected 120 I_h matrices; reconstructed {len(mats)}.")
    return mats


def classify_proper_rotation(R):
    """A5 class: identity, pi, 2pi/3, 2pi/5, or 4pi/5."""
    tr = float(np.trace(R))
    targets = np.array([3.0, -1.0, 0.0, 1.0 + 2.0*np.cos(2*np.pi/5),
                        1.0 + 2.0*np.cos(4*np.pi/5)])
    k = int(np.argmin(np.abs(targets - tr)))
    if abs(targets[k] - tr) > 2.0e-6:
        raise RuntimeError(f"Unclassified proper rotation trace {tr}.")
    return k


A5_CHARACTERS = {
    "1":  (1, np.array([1, 1, 1, 1, 1], float)),
    "3":  (3, np.array([3, -1, 0, PHI, PHI_BAR], float)),
    "3p": (3, np.array([3, -1, 0, PHI_BAR, PHI], float)),
    "4":  (4, np.array([4, 0, 1, -1, -1], float)),
    "5":  (5, np.array([5, 1, -1, 0, 0], float)),
}


def group_action(O, faces, centroids, frames):
    """Return the 64x64 orthogonal action in the chosen face frames."""
    # Face centroids identify the induced permutation unambiguously.
    transformed = centroids @ O
    d = cdist(transformed, centroids)
    rows, cols = linear_sum_assignment(d)
    perm = np.empty(len(faces), int)
    perm[rows] = cols
    max_res = float(np.max(d[rows, cols]))
    if max_res > 2.0e-6:
        raise RuntimeError(f"I_h operation does not preserve face set: {max_res}.")
    U = np.zeros((2*len(faces), 2*len(faces)))
    for f, g in enumerate(perm):
        U[2*g:2*g+2, 2*f:2*f+2] = frames[g].T @ O.T @ frames[f]
    return U, perm, max_res


def representation_decomposition(group, faces, centroids, frames, L):
    dim = 2 * len(faces)
    eye = np.eye(dim)
    sectors = {}
    actions = []
    class_counts = np.zeros(5, int)
    improper_count = 0
    equivariance_max = 0.0
    orthogonality_max = 0.0
    for O in group:
        U, perm, face_res = group_action(O, faces, centroids, frames)
        actions.append((O, U))
        orthogonality_max = max(orthogonality_max, float(np.linalg.norm(U.T @ U - eye)))
        equivariance_max = max(equivariance_max, float(np.linalg.norm(L @ U - U @ L)))
        if np.linalg.det(O) > 0:
            R = O
            parity = 1
        else:
            R = -O
            parity = -1
            improper_count += 1
        if parity == 1:
            class_counts[classify_proper_rotation(R)] += 1

    for name, (d, chi) in A5_CHARACTERS.items():
        for parity_label, parity_sign in (("g", 1), ("u", -1)):
            P = np.zeros((dim, dim))
            for O, U in actions:
                if np.linalg.det(O) > 0:
                    R, p = O, 1
                else:
                    R, p = -O, -1
                cls = classify_proper_rotation(R)
                character = chi[cls] * (parity_sign ** (p == -1))
                # parity_sign is the inversion character: multiply once for -I coset.
                if p == -1:
                    character = chi[cls] * parity_sign
                P += character * U
            P *= d / 120.0
            P = (P + P.T) / 2.0
            evals, evecs = np.linalg.eigh(P)
            Q = evecs[:, evals > 0.5]
            rank = int(Q.shape[1])
            idem = float(np.linalg.norm(P @ P - P))
            sectors[f"{name}{parity_label}"] = {
                "dimension_irrep": d,
                "isotypic_rank": rank,
                "multiplicity": rank // d if rank % d == 0 else None,
                "projector_idempotence_residual": idem,
                "restricted_eigenvalues": np.linalg.eigvalsh(Q.T @ L @ Q).tolist() if rank else [],
            }
    # Independently verify completeness and pairwise orthogonality of central projectors.
    projectors = {}
    for label, info in sectors.items():
        d = info["dimension_irrep"]
        chi = A5_CHARACTERS[label[:-1]][1]
        parity_sign = 1 if label.endswith("g") else -1
        P = np.zeros((dim, dim))
        for O, U in actions:
            if np.linalg.det(O) > 0:
                R, p = O, 1
            else:
                R, p = -O, -1
            char = chi[classify_proper_rotation(R)] * (parity_sign if p == -1 else 1)
            P += char * U
        projectors[label] = (d / 120.0) * P
    sumP = sum(projectors.values(), np.zeros((dim, dim)))
    completeness = float(np.linalg.norm(sumP - eye))
    orth_projector = 0.0
    labels = list(projectors)
    for i, a in enumerate(labels):
        for b in labels[i+1:]:
            orth_projector = max(orth_projector, float(np.linalg.norm(projectors[a] @ projectors[b])))
    return {
        "group_order": len(group),
        "proper_rotation_class_counts_identity_pi_2pi3_2pi5_4pi5": class_counts.tolist(),
        "improper_operations": improper_count,
        "max_action_orthogonality_residual": orthogonality_max,
        "max_connection_laplacian_commutator_frobenius": equivariance_max,
        "irreducible_isotypic_sectors": sectors,
        "projector_completeness_residual": completeness,
        "max_pairwise_projector_product_residual": orth_projector,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="c60_icosahedral_connection_audit")
    ap.add_argument("--mmff-npz", default=None,
                    help="Optional first-stage MMFF audit NPZ containing X_relaxed.")
    args = ap.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    x_ideal, _ = c60_ideal()
    faces, _ = reconstruct_faces(x_ideal)
    if args.mmff_npz:
        data = np.load(args.mmff_npz)
        x = np.asarray(data["X_relaxed"], float)
        source = "MMFF94s-relaxed coordinates; face cycles inherited by atom index from ideal C60"
    else:
        x = x_ideal
        source = "ideal truncated icosahedron reconstructed from icosahedron"
    if x.shape != (60, 3):
        raise RuntimeError(f"Expected coordinate array (60,3), got {x.shape}.")
    normals = normals_for_faces(x, faces)
    face_sizes = sorted(len(f) for f in faces)
    if len(faces) != 32 or face_sizes.count(5) != 12 or face_sizes.count(6) != 20:
        raise RuntimeError(f"Expected 12 pentagons and 20 hexagons; got {face_sizes}.")
    (incidence, frames, transports, L, edge_mismatch,
     rotation_det_residual, complex_residual) = connection_data(x, faces, normals)
    centroids = np.asarray([x[list(f)].mean(axis=0) for f in faces])
    group = icosahedral_orthogonal_group()
    decomp = None
    symmetry_note = None
    if args.mmff_npz:
        symmetry_note = (
            "I_h decomposition intentionally not imposed on relaxed coordinates. "
            "The connection spectrum is computed on the relaxed geometry, while "
            "the ideal-geometry run supplies the exact I_h representation audit."
        )
    else:
        decomp = representation_decomposition(group, faces, centroids, frames, L)

    # Scalar dual graph Laplacian, built from the same face-edge incidence.
    A = np.zeros((len(faces), len(faces)))
    for fs in incidence.values():
        f, g = fs
        A[f, g] = A[g, f] = 1.0
    Ls = np.diag(A.sum(axis=1)) - A
    report = {
        "source_geometry": source,
        "topology": {
            "vertices": int(len(x)),
            "edges": int(len(incidence)),
            "faces": int(len(faces)),
            "pentagons": int(face_sizes.count(5)),
            "hexagons": int(face_sizes.count(6)),
            "euler_characteristic": int(len(x) - len(incidence) + len(faces)),
            "dual_graph_degree_histogram": {
                str(k): int(v) for k, v in zip(*np.unique(A.sum(axis=1), return_counts=True))
            },
        },
        "connection": {
            "fibre_rank": 2,
            "total_dimension": int(L.shape[0]),
            "transport_edges": int(len(incidence)),
            "max_projected_edge_direction_mismatch": edge_mismatch,
            "max_transport_SO2_determinant_residual": rotation_det_residual,
            "complex_structure_commutator_frobenius": complex_residual,
            "max_laplacian_asymmetry": float(np.linalg.norm(L - L.T)),
            "min_eigenvalue": float(np.linalg.eigvalsh((L + L.T)/2)[0]),
            "max_eigenvalue": float(np.linalg.eigvalsh((L + L.T)/2)[-1]),
            "eigenvalues": np.linalg.eigvalsh((L + L.T)/2).tolist(),
        },
        "scalar_dual_laplacian": {
            "dimension": int(Ls.shape[0]),
            "eigenvalues": np.linalg.eigvalsh(Ls).tolist(),
        },
        "icosahedral_representation": decomp,
        "symmetry_note": symmetry_note,
        "limitations": [
            "The MMFF-relaxed option tests coordinate preservation only if the same ideal I_h group maps the relaxed cage onto itself; generic relaxation may break that symmetry.",
            "If relaxed coordinates break I_h, face reconstruction remains meaningful but the ideal-group action is expected to fail its face-set preservation check; this is reported as a symmetry obstruction, not silently repaired.",
            "The irreducible projectors use the A5 character table and inversion parity for I_h=A5 x C2.",
            "A successful ideal-geometry run does not imply that the relaxed molecular geometry has exact I_h symmetry.",
        ],
    }
    np.savez_compressed(
        out / "C60_icosahedral_connection_spectrum.npz",
        X=x, face_vertices=np.concatenate([np.asarray(f, int) for f in faces]),
        face_offsets=np.cumsum([0] + [len(f) for f in faces]),
        normals=normals, L_connection=L, L_scalar=Ls,
    )
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
