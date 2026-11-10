#!/usr/bin/env python3
"""Exact incidence/Stokes audit for the triangulated Q-ball shell.

The script constructs oriented cellular boundary matrices from the canonical
football_shell generator. It checks B1 @ B2 = 0 and the discrete Stokes
identity for vector-valued edge 1-cochains. It does NOT infer dislocations
from the mere existence of physical seams.
"""
from __future__ import annotations
import argparse
import json
import numpy as np
from models.football_shell import build_football_shell


def incidence(mesh):
    triangles = np.asarray(mesh["triangles"], dtype=int)
    n_vertices = len(mesh["nodes"])
    edge_set = set()
    for tri in triangles:
        for a, b in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])):
            edge_set.add(tuple(sorted((int(a), int(b)))))
    edges = sorted(edge_set)
    edge_id = {e: k for k, e in enumerate(edges)}
    B1 = np.zeros((n_vertices, len(edges)), dtype=np.int64)
    for k, (a, b) in enumerate(edges):
        B1[a, k], B1[b, k] = -1, 1
    B2 = np.zeros((len(edges), len(triangles)), dtype=np.int64)
    for f, tri in enumerate(triangles):
        for a, b in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])):
            e = tuple(sorted((int(a), int(b))))
            B2[edge_id[e], f] += 1 if a < b else -1
    return edges, B1, B2


def rank_integer_matrix(A):
    # Exact rank over Q using SymPy; the shell matrices are small (270 x 180).
    import sympy as sp
    return int(sp.Matrix(np.asarray(A, dtype=int).tolist()).rank())


def run(radius=1.0, cube_alpha=0.0, h4_alpha=0.0, seed=20261110):
    mesh = build_football_shell(radius=radius, cube_alpha=cube_alpha, h4_alpha=h4_alpha)
    edges, B1, B2 = incidence(mesh)
    chain_residual = B1 @ B2
    if np.any(chain_residual):
        raise AssertionError("Boundary-of-boundary is not zero")
    r1, r2 = rank_integer_matrix(B1), rank_integer_matrix(B2)
    b1 = len(edges) - r1 - r2
    chi = len(mesh["nodes"]) - len(edges) + len(mesh["triangles"])

    # Random R^3-valued edge 1-cochain and an arbitrary set of oriented faces.
    rng = np.random.default_rng(seed)
    d_edge = rng.normal(size=(len(edges), 3))
    face_mask = rng.integers(0, 2, size=len(mesh["triangles"]), dtype=np.int64)
    boundary_chain = B2 @ face_mask
    face_curl = B2.T @ d_edge
    lhs = np.einsum("e,ec->c", boundary_chain, d_edge)
    rhs = np.einsum("f,fc->c", face_mask, face_curl)
    stokes_residual = float(np.max(np.abs(lhs-rhs)))

    # A nodal macroscopic deformation induces an exact edge gradient.
    y = rng.normal(size=(len(mesh["nodes"]), 3))
    dy_edge = np.asarray([y[b]-y[a] for a, b in edges])
    # For any discrete microscopic edge field G, D = dy - G and
    # curl(D) = -curl(G), since B2^T dy = 0.
    G_edge = rng.normal(size=(len(edges), 3))
    D_edge = dy_edge - G_edge
    grad_curl_residual = float(np.max(np.abs(B2.T @ D_edge + B2.T @ G_edge)))

    seam_edges = {tuple(sorted(map(int, e))) for e in mesh["physical_seams"]}
    seam_count = sum(e in seam_edges for e in edges)
    result = {
        "mesh": {
            "vertices_in_triangulation_including_panel_centres": int(len(mesh["nodes"])),
            "physical_shell_vertices": int(len(mesh["vertices"])),
            "panels": int(len(mesh["panels"])),
            "triangles": int(len(mesh["triangles"])),
            "edges": int(len(edges)),
            "physical_seams": int(seam_count),
            "euler_characteristic": int(chi),
        },
        "incidence": {
            "rank_B1_over_Q": r1,
            "rank_B2_over_Q": r2,
            "first_betti_number": int(b1),
            "max_abs_B1B2": int(np.max(np.abs(chain_residual))),
        },
        "discrete_stokes": {
            "max_abs_residual_R3_edge_cochain": stokes_residual,
            "gradient_decomposition_curl_residual": grad_curl_residual,
        },
        "interpretation": [
            "B1 B2 = 0 is an exact chain-complex identity.",
            "The discrete Stokes identity is exact up to floating-point evaluation of the test cochain.",
            "For D = delta(y) - G, curl(D) = -curl(G), since curl(delta(y)) = 0.",
            "Physical seams are identified as a subset of mesh edges; no nonzero seam jump or dislocation is inferred."
        ],
    }
    if chi != 2 or b1 != 0 or seam_count != 90:
        raise AssertionError("Unexpected shell topology or seam count")
    if stokes_residual > 1e-11 or grad_curl_residual > 1e-11:
        raise AssertionError("Discrete Stokes/decomposition check failed")
    return result


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--radius", type=float, default=1.0)
    ap.add_argument("--cube-alpha", type=float, default=0.0)
    ap.add_argument("--h4-alpha", type=float, default=0.0)
    ap.add_argument("--out")
    args = ap.parse_args()
    result = run(args.radius, args.cube_alpha, args.h4_alpha)
    payload = json.dumps(result, indent=2)
    print(payload)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(payload + "\n")
