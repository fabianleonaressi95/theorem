#!/usr/bin/env python3
"""Finite-mesh audit for T087: flat/non-flat transport and seam covariance."""
from __future__ import annotations
import json
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from models.football_shell import build_football_shell


def random_rotation(rng):
    q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1
    return q


def main():
    rng = np.random.default_rng(20261111)
    mesh = build_football_shell()
    nodes = mesh["nodes"]
    triangles = np.asarray(mesh["triangles"], dtype=int)
    n = len(nodes)
    frames = [random_rotation(rng) for _ in range(n)]

    # Flat transport induced by changes of local orthonormal frame.
    U = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                U[i, j] = frames[j] @ frames[i].T

    y = rng.normal(size=(n, 3))

    def edge_diff(u, v):
        return y[v] - U[u, v] @ y[u]

    def face_defect(tri):
        i, j, k = map(int, tri)
        qij, qjk, qki = edge_diff(i, j), edge_diff(j, k), edge_diff(k, i)
        lhs = U[j, k] @ qij + qjk + U[i, k] @ qki
        rhs = (U[i, k] - U[j, k] @ U[i, j]) @ y[i]
        return lhs, rhs

    flat_res = max(np.linalg.norm(face_defect(t)[0] - face_defect(t)[1])
                   for t in triangles)
    flat_holonomy = max(np.linalg.norm(U[int(t[0]), int(t[2])] -
                                       U[int(t[1]), int(t[2])] @ U[int(t[0]), int(t[1])])
                        for t in triangles)

    # Break flatness on one edge, preserving orthogonality and inverse transport.
    u0, v0 = sorted(tuple(map(int, next(iter(mesh["edge_triangles"])))))
    twist = random_rotation(rng)
    U[u0, v0] = twist @ U[u0, v0]
    U[v0, u0] = U[u0, v0].T
    nonflat_terms = []
    for tri in triangles:
        i, j, k = map(int, tri)
        lhs, rhs = face_defect(tri)
        nonflat_terms.append((lhs, rhs))
    curvature_identity = max(np.linalg.norm(a-b) for a, b in nonflat_terms)
    curvature_size = max(np.linalg.norm(b) for _, b in nonflat_terms)

    # Assemble A_U and test the finite-dimensional Hodge normal equation.
    edge_list = sorted(mesh["edge_triangles"])
    A = np.zeros((3 * len(edge_list), 3 * n))
    for e, (i, j) in enumerate(edge_list):
        A[3*e:3*e+3, 3*j:3*j+3] = np.eye(3)
        A[3*e:3*e+3, 3*i:3*i+3] = -U[i, j]
    G = rng.normal(size=3 * len(edge_list))
    ystar = np.linalg.lstsq(A, G, rcond=None)[0]
    D = A @ ystar - G
    hodge_residual = np.linalg.norm(A.T @ D)

    # Seam jump covariance under independent frame changes.
    Sminus, Splus = random_rotation(rng), random_rotation(rng)
    Rminusplus = random_rotation(rng)
    Gminus, Gplus = rng.normal(size=3), rng.normal(size=3)
    J = Gplus - Rminusplus @ Gminus
    Rprime = Splus @ Rminusplus @ Sminus.T
    Jprime = Splus @ Gplus - Rprime @ (Sminus @ Gminus)
    seam_covariance = abs(np.linalg.norm(Jprime) - np.linalg.norm(J))

    result = {
        "mesh": {"vertices": n, "edges": len(edge_list),
                 "faces": len(triangles), "physical_seams": len(mesh["physical_seams"])},
        "flat_connection": {
            "max_face_holonomy_defect": float(flat_holonomy),
            "max_curvature_identity_residual": float(flat_res)},
        "single_edge_twist": {
            "max_curvature_identity_residual": float(curvature_identity),
            "max_curvature_source_norm": float(curvature_size)},
        "covariant_hodge": {
            "normal_equation_residual": float(hodge_residual),
            "least_squares_energy": float(0.5 * D @ D)},
        "seam_frame_covariance": {
            "jump_norm_difference": float(seam_covariance)},
        "classification": "finite-mesh algebraic numerical audit; no continuum limit"
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
