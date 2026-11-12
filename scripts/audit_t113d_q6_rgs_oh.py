#!/usr/bin/env python3
"""Exact-label Q6/RGS O_h action audit for T113-D.

Uses the repository's hash-checked 64x3 RGS seed. It keeps the six-cube
Q6 graph distinct from the induced O_h action on the embedded point cloud.
"""
from __future__ import annotations
from itertools import permutations, product
import hashlib
import json
import numpy as np

from src.rgs_seed_64_reconstruction import load_rgs_seed_data, EXPECTED_X_SHA256


def signed_permutation_matrices():
    out = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            g = np.zeros((3, 3), dtype=np.int64)
            for row, col in enumerate(perm):
                g[row, col] = signs[row]
            out.append(g)
    out.sort(key=lambda g: tuple(int(x) for x in g.ravel()))
    return out


def q6_adjacency():
    a = np.zeros((64, 64), dtype=np.int64)
    for v in range(64):
        for bit in range(6):
            a[v, v ^ (1 << bit)] = 1
    return a


def audit():
    x = load_rgs_seed_data().coordinates
    digest = hashlib.sha256(np.ascontiguousarray(x, dtype="<f8").tobytes()).hexdigest()
    if digest != EXPECTED_X_SHA256:
        raise AssertionError("RGS seed hash mismatch")
    lookup = {tuple(row.tolist()): i for i, row in enumerate(x)}
    if len(lookup) != 64:
        raise AssertionError("RGS coordinates are not distinct")

    groups = signed_permutation_matrices()
    group_set = {tuple(g.ravel()) for g in groups}
    if len(groups) != 48:
        raise AssertionError("signed-permutation group must have order 48")

    perms = []
    for g in groups:
        p = np.empty(64, dtype=np.int64)
        for i, row in enumerate(x):
            key = tuple((g @ row).tolist())
            if key not in lookup:
                raise AssertionError("O_h does not preserve the recovered 64-point seed")
            p[i] = lookup[key]
        if len(set(p.tolist())) != 64:
            raise AssertionError("induced action is not a permutation")
        perms.append(p)

    # Verify the signed-permutation matrices form a group.
    closure = all(tuple((g @ h).ravel()) in group_set for g in groups for h in groups)
    if not closure:
        raise AssertionError("signed permutation matrices are not closed")

    a = q6_adjacency()
    lap = 6 * np.eye(64) - a
    residuals = []
    automorphisms = 0
    conjugates = []
    for p in perms:
        P = np.zeros((64, 64), dtype=np.int64)
        P[p, np.arange(64)] = 1
        conjugate = P @ lap @ P.T
        residual = float(np.linalg.norm(conjugate - lap, ord="fro"))
        residuals.append(residual)
        automorphisms += int(residual == 0.0)
        conjugates.append(conjugate)

    # Reynolds average of the Q6 Laplacian under the actual induced O_h action.
    # It is a new O_h-invariant weighted graph operator, not the original Q6 graph.
    lbar = sum(conjugates) / 48.0
    off = lbar[np.triu_indices(64, 1)]
    weights, counts = np.unique(np.round(-off, 12), return_counts=True)
    eig = np.linalg.eigvalsh(lbar)
    inv_residuals = []
    for p in perms:
        P = np.zeros((64, 64), dtype=np.int64)
        P[p, np.arange(64)] = 1
        inv_residuals.append(float(np.linalg.norm(P @ lbar @ P.T - lbar, ord="fro")))

    # Two involutions must remain distinct: graph antipode XOR 63 and
    # coordinate inversion of this particular RGS seed XOR 7.
    rgs_inversion_residual = float(np.max(np.abs(x[np.arange(64) ^ 7] + x)))
    graph_antipode_residual = float(np.max(np.abs(x[np.arange(64) ^ 63] + x)))

    checks = {
        "seed_shape_64x3": x.shape == (64, 3),
        "seed_hash": digest == EXPECTED_X_SHA256,
        "Oh_order_48": len(groups) == 48,
        "Oh_group_closure": closure,
        "q6_64_vertices": a.shape == (64, 64),
        "q6_192_undirected_edges": int(a.sum() // 2) == 192,
        "q6_degree_six": bool(np.all(a.sum(axis=1) == 6)),
        "induced_Oh_action_permutations": len(perms) == 48,
        "only_16_of_48_preserve_Q6_adjacency": automorphisms == 16,
        "Reynolds_operator_symmetric": float(np.linalg.norm(lbar-lbar.T)) < 1e-12,
        "Reynolds_operator_row_sum_zero": float(np.linalg.norm(lbar @ np.ones(64))) < 1e-10,
        "Reynolds_operator_psd": float(eig.min()) > -1e-10,
        "Reynolds_operator_Oh_invariant": max(inv_residuals) < 1e-10,
        "RGS_coordinate_inversion_xor7": rgs_inversion_residual < 1e-12,
        "Q6_graph_antipode_is_not_RGS_inversion": graph_antipode_residual > 1e-6,
    }
    return {
        "schema": "t113d-q6-rgs-oh-audit/v1",
        "seed_sha256": digest,
        "group_order": len(groups),
        "q6": {"vertices": 64, "undirected_edges": int(a.sum() // 2),
               "degree": 6, "laplacian_spectrum": [0, 2, 4, 6, 8, 10, 12]},
        "induced_Oh_action": {
            "permutations": len(perms),
            "Q6_graph_automorphisms": automorphisms,
            "non_automorphisms": len(perms)-automorphisms,
            "Frobenius_residual_values": sorted(set(round(r, 12) for r in residuals)),
        },
        "Oh_Reynolds_Q6_laplacian": {
            "is_original_Q6_laplacian": False,
            "off_diagonal_conductance_values": [float(w) for w in weights if w > 0],
            "unordered_edge_counts_by_weight": {
                str(float(w)): int(c) for w, c in zip(weights, counts) if w > 0
            },
            "weighted_edges": int(np.count_nonzero(np.triu(lbar, 1))),
            "min_eigenvalue": float(eig.min()),
            "max_Oh_invariance_residual": max(inv_residuals),
            "distance_from_original_Q6_laplacian": float(np.linalg.norm(lbar-lap, ord="fro")),
        },
        "involutions": {
            "RGS_coordinate_inversion_mask": 7,
            "Q6_graph_antipode_mask": 63,
            "RGS_inversion_residual": rgs_inversion_residual,
            "Q6_antipode_coordinate_residual": graph_antipode_residual,
        },
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "interpretation": (
            "The O_h action preserves the recovered 64-point RGS seed but is not "
            "an automorphism of the canonical six-cube Q6 graph for 32 of 48 elements. "
            "The Reynolds-averaged Laplacian is a distinct O_h-invariant weighted "
            "operator, not the original 192-edge Q6 Laplacian."
        ),
    }


if __name__ == "__main__":
    report = audit()
    print(json.dumps(report, indent=2, sort_keys=True))
    if not report["all_checks_pass"]:
        raise SystemExit(1)
