#!/usr/bin/env python3
"""Test the V4 restriction of the Q6 / actual C60 face-tangent representations.

This is an explicit, reproducible subgroup test. It:
  * builds the coordinate A4 subgroup and its Klein-four subgroup on Q6;
  * builds an A4 subgroup of the icosahedral rotation group and its V4;
  * matches the three nonidentity V4 elements by a documented deterministic
    matrix-order convention (any bijection is a V4 isomorphism);
  * tests Q6 graph-automorphism status;
  * constructs the 64x64 orthogonal intertwiner from simultaneous V4
    character projectors;
  * separately tests covariance of the archived 188D tangent operators.

An abstract representation intertwiner is not a canonical geometric face map,
and it does not define a C60 spectral operator.
"""
import argparse
import itertools
import json
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull

PHI = (1.0 + np.sqrt(5.0)) / 2.0
TOL = 1.0e-8


def matrix_key(M):
    return tuple(np.round(np.asarray(M).ravel(), 8))


def signed_permutations():
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            M = np.zeros((3, 3))
            M[np.arange(3), perm] = signs
            yield M


def permutation_parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def match_points(X, M):
    Y = X @ M.T
    D = np.linalg.norm(Y[:, None, :] - X[None, :, :], axis=2)
    p = D.argmin(axis=1)
    residual = float(D[np.arange(len(X)), p].max())
    if residual > TOL or len(set(map(int, p))) != len(X):
        raise RuntimeError(f"Point action not bijective: residual={residual}")
    return p


def coordinate_a4(X):
    records = []
    for M in signed_permutations():
        p = tuple(np.argmax(np.abs(M), axis=1))
        parity = permutation_parity(p)
        sign_product = int(round(np.prod(M[M != 0])))
        if parity == 0 and sign_product == 1:
            records.append((M, match_points(X, M)))
    if len(records) != 12:
        raise RuntimeError(f"Expected coordinate A4 order 12, got {len(records)}")
    return records


def v4_from_a4(records):
    I = np.eye(3)
    nontrivial = []
    for M, p in records:
        if np.allclose(M, I, atol=TOL):
            continue
        if np.allclose(M @ M, I, atol=TOL):
            nontrivial.append((M, p))
    if len(nontrivial) != 3:
        raise RuntimeError(f"Expected three nonidentity V4 elements, got {len(nontrivial)}")
    nontrivial.sort(key=lambda item: matrix_key(item[0]))
    identity = next((M, p) for M, p in records if np.allclose(M, I, atol=TOL))
    return [identity] + nontrivial


def ico_vertices():
    return np.asarray(
        [(0, a, b * PHI) for a in (-1, 1) for b in (-1, 1)]
        + [(a, b * PHI, 0) for a in (-1, 1) for b in (-1, 1)]
        + [(a * PHI, 0, b) for a in (-1, 1) for b in (-1, 1)],
        dtype=float,
    )


def icosahedral_rotations(V):
    src = next(t for t in itertools.combinations(range(12), 3)
               if abs(np.linalg.det(V[list(t)])) > 1e-8)
    S = V[list(src)]
    out = []
    for tgt in itertools.permutations(range(12), 3):
        T = V[list(tgt)]
        if not np.allclose(T @ T.T, S @ S.T):
            continue
        R = np.linalg.solve(S, T).T
        if np.linalg.det(R) < 0.999999:
            continue
        Y = V @ R.T
        ix = np.linalg.norm(Y[:, None, :] - V[None, :, :], axis=2).argmin(axis=1)
        if np.max(np.linalg.norm(Y - V[ix], axis=1)) < 1e-7:
            if not any(np.allclose(R, Q, atol=1e-7) for Q in out):
                out.append(R)
    if len(out) != 60:
        raise RuntimeError(f"Expected icosahedral rotation group order 60, got {len(out)}")
    return out


def a4_subgroup(rotations):
    keys = {matrix_key(M): i for i, M in enumerate(rotations)}
    n = len(rotations)
    mult = np.empty((n, n), dtype=int)
    for i, M in enumerate(rotations):
        for j, Q in enumerate(rotations):
            P = M @ Q
            k = keys.get(matrix_key(P))
            if k is None:
                k = min(range(n), key=lambda t: np.linalg.norm(rotations[t] - P))
            mult[i, j] = k
    e = next(i for i, M in enumerate(rotations) if np.allclose(M, np.eye(3)))

    def closure(gens):
        H = {e}
        changed = True
        while changed:
            changed = False
            for a in tuple(H):
                for b in tuple(H):
                    c = int(mult[a, b])
                    if c not in H:
                        H.add(c)
                        changed = True
            for g in gens:
                if g not in H:
                    H.add(g)
                    changed = True
        return H

    found = {}
    for i in range(n):
        for j in range(i + 1, n):
            H = closure((i, j))
            if len(H) == 12:
                found[tuple(sorted(H))] = H
    if not found:
        raise RuntimeError("Could not find an A4 subgroup in I")
    H = next(iter(found.values()))
    out = [rotations[i] for i in H]
    out.sort(key=lambda M: (0 if np.allclose(M, np.eye(3)) else 1, matrix_key(M)))
    return out


def c60_faces(V):
    hull = ConvexHull(V)
    edges = set()
    for tri in hull.simplices:
        for k in range(3):
            edges.add(tuple(sorted((int(tri[k]), int(tri[(k + 1) % 3])))))
    pts = []
    for a, b in sorted(edges):
        pts.extend(((2 * V[a] + V[b]) / 3.0, (V[a] + 2 * V[b]) / 3.0))
    X = np.asarray(pts)
    hull = ConvexHull(X)
    planes = {}
    for eq in hull.equations:
        n = eq[:3] / np.linalg.norm(eq[:3])
        d = eq[3] / np.linalg.norm(eq[:3])
        planes[matrix_key(np.r_[n, d])] = (n, d)
    faces = []
    for n, d in planes.values():
        ids = np.flatnonzero(np.abs(X @ n + d) < 1e-7)
        if len(ids) in (5, 6):
            faces.append((n, d, int(len(ids))))
    counts = Counter(f[2] for f in faces)
    if len(faces) != 32 or counts != {5: 12, 6: 20}:
        raise RuntimeError(f"C60 face inventory invalid: {len(faces)}, {dict(counts)}")
    faces.sort(key=lambda f: matrix_key(np.r_[f[0], f[1]]))
    return faces


def tangent_bases(normals):
    bases = []
    for n in normals:
        axis = np.eye(3)[np.argmin(np.abs(n))]
        u = axis - n * np.dot(axis, n)
        u /= np.linalg.norm(u)
        w = np.cross(n, u)
        bases.append(np.column_stack((u, w)))
    return np.asarray(bases)


def q6_state_representation(p):
    P = np.zeros((64, 64))
    P[p, np.arange(64)] = 1.0
    return P


def c60_fibre_representation(R, faces, bases):
    normals = np.asarray([f[0] for f in faces])
    target_normals = normals @ R.T
    D = np.linalg.norm(target_normals[:, None, :] - normals[None, :, :], axis=2)
    target = D.argmin(axis=1)
    residual = float(D[np.arange(32), target].max())
    if residual > 1e-6 or len(set(map(int, target))) != 32:
        raise RuntimeError(f"C60 face action not bijective: {residual}")
    F = np.zeros((64, 64))
    for i, j in enumerate(target):
        block = bases[j].T @ R @ bases[i]
        F[2*j:2*j+2, 2*i:2*i+2] = block
    return F


def character_projectors(reps):
    # reps ordered as identity, a, b, c with a,b,c the three V4 involutions.
    projectors = {}
    for sa, sb in itertools.product((-1.0, 1.0), repeat=2):
        character = np.asarray([1.0, sa, sb, sa * sb])
        P = sum(character[k] * reps[k] for k in range(4)) / 4.0
        P = (P + P.T) / 2.0
        vals, vecs = np.linalg.eigh(P)
        basis = vecs[:, vals > 0.5]
        projectors[f"{int(sa):+d},{int(sb):+d}"] = (P, basis)
    return projectors


def orthogonal_intertwiner(qreps, freps):
    qp = character_projectors(qreps)
    fp = character_projectors(freps)
    pieces = []
    multiplicities = {}
    for key in qp:
        Bq = qp[key][1]
        Bf = fp[key][1]
        multiplicities[key] = {"Q6": int(Bq.shape[1]), "C60": int(Bf.shape[1])}
        if Bq.shape[1] != Bf.shape[1]:
            raise RuntimeError(f"V4 character multiplicity mismatch in sector {key}")
        pieces.append(Bf @ Bq.T)
    O = sum(pieces)
    orth = float(np.linalg.norm(O.T @ O - np.eye(64)))
    residuals = [float(np.linalg.norm(O @ qreps[k] - freps[k] @ O)) for k in range(4)]
    if orth > 1e-8 or max(residuals) > 1e-8:
        raise RuntimeError(f"Intertwiner verification failed: orth={orth}, max={max(residuals)}")
    return O, multiplicities, orth, residuals


def relative_covariance(U, M):
    return float(np.linalg.norm(U.T @ M @ U - M) / max(np.linalg.norm(M), 1e-30))


def run(npz_path, out_path, matrix_path):
    z = np.load(npz_path, allow_pickle=False)
    X = np.asarray(z["X_Oh_reconstructed"], float)
    A = np.asarray(z["Q6_adjacency"], float)
    Q = np.asarray(z["Q_tangent"], float)
    if X.shape != (64, 3) or A.shape != (64, 64) or Q.shape != (192, 188):
        raise RuntimeError(f"Unexpected archive shapes X={X.shape}, A={A.shape}, Q={Q.shape}")

    q4 = v4_from_a4(coordinate_a4(X))
    qreps = [q6_state_representation(p) for M, p in q4]
    graph_residuals = [float(np.max(np.abs(A[np.ix_(p, p)] - A))) for M, p in q4]
    graph_preserved = [r < 1e-12 for r in graph_residuals]

    I = icosahedral_rotations(ico_vertices())
    a4 = a4_subgroup(I)
    v4rot = []
    eye = np.eye(3)
    for R in a4:
        if np.allclose(R, eye, atol=1e-7) or np.allclose(R @ R, eye, atol=1e-7):
            v4rot.append(R)
    if len(v4rot) != 4:
        raise RuntimeError(f"Expected C60 V4 of order 4, got {len(v4rot)}")
    v4rot.sort(key=lambda R: (0 if np.allclose(R, eye, atol=1e-7) else 1, matrix_key(R)))
    faces = c60_faces(ico_vertices())
    bases = tangent_bases(np.asarray([f[0] for f in faces]))
    freps = [c60_fibre_representation(R, faces, bases) for R in v4rot]

    # The nonidentity elements of V4 are interchangeable under any group
    # isomorphism. The deterministic matrix ordering fixes one explicit map.
    q_nonid = [matrix_key(M) for M, p in q4[1:]]
    c_nonid = [matrix_key(R) for R in v4rot[1:]]
    O, mults, orth, intertwiner_residuals = orthogonal_intertwiner(qreps, freps)

    qchars = [round(float(np.trace(P)), 8) for P in qreps]
    fchars = [round(float(np.trace(F)), 8) for F in freps]
    char_equal = bool(np.allclose(qchars, fchars, atol=1e-8))

    # Independently test the 188D tangent subspace and operators under this V4.
    Ptan = Q @ Q.T
    tangent_rows = []
    tangent_actions = []
    for (M, p) in q4:
        S = np.zeros((192, 192))
        for i in range(64):
            S[3*p[i]:3*p[i]+3, 3*i:3*i+3] = M
        U = Q.T @ S @ Q
        proj = float(np.linalg.norm(S @ Ptan @ S.T - Ptan))
        orthU = float(np.linalg.norm(U.T @ U - np.eye(188)))
        row = {"projector_invariance_residual": proj, "induced_orthogonality_residual": orthU}
        for name in ("K0", "R_geo_tangent", "P_G", "T_transport"):
            if name in z:
                row[name + "_relative_covariance_residual"] = relative_covariance(U, np.asarray(z[name], float))
        tangent_rows.append(row)
        tangent_actions.append(U)

    operator_summary = {}
    for name in ("K0", "R_geo_tangent", "P_G", "T_transport"):
        key = name + "_relative_covariance_residual"
        vals = [r[key] for r in tangent_rows if key in r]
        if vals:
            operator_summary[name] = {
                "preserved_count_tol_1e-10": int(sum(v < 1e-10 for v in vals)),
                "group_order": 4,
                "max_relative_covariance_residual": max(vals),
            }

    report = {
        "classification": "new numerical subgroup audit; representation-theoretic equivalence tested on V4",
        "source_archive": str(npz_path),
        "Q6_coordinate_A4_order": 12,
        "Q6_V4_order": len(q4),
        "C60_icosahedral_rotation_group_order": len(I),
        "C60_A4_order": 12,
        "C60_V4_order": len(v4rot),
        "V4_isomorphism_convention": "identity maps to identity; nonidentity elements paired in lexicographic rounded-matrix order in their respective Cartesian frames",
        "Q6_V4_nonidentity_matrix_keys": [list(x) for x in q_nonid],
        "C60_V4_nonidentity_matrix_keys": [list(x) for x in c_nonid],
        "Q6_V4_state_characters": qchars,
        "C60_V4_face_fibre_characters": fchars,
        "V4_characters_equal": char_equal,
        "V4_irrep_multiplicities": mults,
        "Q6_V4_graph_automorphism_residuals": graph_residuals,
        "all_Q6_V4_elements_preserve_adjacency": bool(all(graph_preserved)),
        "explicit_orthogonal_intertwiner": {
            "shape": list(O.shape),
            "orthogonality_residual": orth,
            "per_element_intertwining_residuals": intertwiner_residuals,
            "max_intertwining_residual": max(intertwiner_residuals),
            "interpretation": "An explicit orthogonal equivalence of V4 representations; not a canonical geometric face-to-state assignment."
        },
        "Q6_188D_tangent_action": {
            "per_element": tangent_rows,
            "operator_covariance": operator_summary,
            "interpretation": "These tests are separate from the 64D representation equivalence. Failure of an archived 188D operator to commute with V4 prevents treating its spectrum as V4-symmetry-resolved."
        },
        "spectral_comparison_authorized": False,
        "conclusion": (
            "The 64D Q6 state representation and actual C60 face-tangent representation "
            "are explicitly equivalent after restriction to V4 under the stated group isomorphism. "
            "This is an abstract finite-group intertwiner, not a canonical geometric map. "
            "Graph symmetry and 188D operator covariance are reported separately."
        ),
    }
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    Path(matrix_path).parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        matrix_path,
        intertwiner_Q6_to_C60=O,
        q6_state_actions=np.stack(qreps),
        c60_face_fibre_actions=np.stack(freps),
        q6_V4_coordinate_matrices=np.stack([x[0] for x in q4]),
        c60_V4_rotation_matrices=np.stack(v4rot),
        q6_188D_tangent_actions=np.stack(tangent_actions),
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("npz", nargs="?", default="data/RGS_PSU_all_matrices.npz")
    parser.add_argument("--out", default="audits/Q6_C60_V4_equivariance.json")
    parser.add_argument("--matrices", default="artifacts/Q6_C60_V4_intertwiner.npz")
    args = parser.parse_args()
    run(args.npz, args.out, args.matrices)
