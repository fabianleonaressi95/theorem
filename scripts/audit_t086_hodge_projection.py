#!/usr/bin/env python3
"""Numerical audit for T086 on the canonical Q-ball shell.

Uses M_ee = 1 / edge_length as a positive diagonal edge metric. This is a
declared numerical choice, not a calibrated constitutive law.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from models.football_shell import build_football_shell


def incidence(mesh):
    triangles = np.asarray(mesh["triangles"], dtype=int)
    edges = sorted({tuple(sorted((int(u), int(v))))
                    for tri in triangles
                    for u, v in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0]))})
    edge_id = {edge: k for k, edge in enumerate(edges)}
    B1 = np.zeros((len(mesh["nodes"]), len(edges)), dtype=np.int64)
    B2 = np.zeros((len(edges), len(triangles)), dtype=np.int64)
    for k, (u, v) in enumerate(edges):
        B1[u, k], B1[v, k] = -1, 1
    for f, tri in enumerate(triangles):
        for u, v in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])):
            key = tuple(sorted((int(u), int(v))))
            B2[edge_id[key], f] = 1 if u < v else -1
    return B1, B2, edges


def solve_gauge_fixed(B1, Mdiag, G):
    L = (B1 * Mdiag[None, :]) @ B1.T
    rhs = B1 @ (Mdiag[:, None] * G)
    y = np.zeros((B1.shape[0], G.shape[1]))
    y[1:] = np.linalg.solve(L[1:, 1:], rhs[1:])
    D = B1.T @ y - G
    return y, D, L


def main():
    rng = np.random.default_rng(20261111)
    mesh = build_football_shell()
    B1, B2, edges = incidence(mesh)
    lengths = np.asarray([np.linalg.norm(mesh["nodes"][v] - mesh["nodes"][u])
                          for u, v in edges])
    Mdiag = 1.0 / lengths

    # Exact cochain: recover nodal potential modulo a common translation.
    z = rng.normal(size=(len(mesh["nodes"]), 3))
    G_exact = B1.T @ z
    y_exact, D_exact, L = solve_gauge_fixed(B1, Mdiag, G_exact)
    exact_energy = 0.5 * np.sum(Mdiag[:, None] * D_exact**2)
    recovery = np.linalg.norm((y_exact - z) - (y_exact - z).mean(axis=0))
    exact_hodge = np.linalg.norm(B1 @ (Mdiag[:, None] * D_exact))

    # Non-exact edge impulse, supported on one edge and one ambient component.
    G = np.zeros((len(edges), 3))
    G[17, 0] = 1.0
    y, D, _ = solve_gauge_fixed(B1, Mdiag, G)
    curl_G = B2.T @ G
    curl_D = B2.T @ D
    hodge = np.linalg.norm(B1 @ (Mdiag[:, None] * D))
    curl_residual = np.linalg.norm(curl_D + curl_G)
    energy = 0.5 * np.sum(Mdiag[:, None] * D**2)

    # Independent Schur formula and the actual M-orthogonal projector.
    Lpinv = np.linalg.pinv(L, rcond=1e-12)
    P = np.eye(len(edges)) - B1.T @ Lpinv @ B1 @ np.diag(Mdiag)
    W = np.diag(Mdiag) @ P
    energy_schur = 0.5 * np.sum(G * (W @ G))
    projector_idempotence = np.linalg.norm(P @ P - P)
    projector_M_adjoint = np.linalg.norm(P.T @ np.diag(Mdiag) -
                                         np.diag(Mdiag) @ P)

    result = {
        "mesh": {"vertices": len(mesh["nodes"]), "edges": len(edges),
                 "faces": len(mesh["triangles"]),
                 "physical_seams": len(mesh["physical_seams"]),
                 "B1B2_max_abs": int(np.max(np.abs(B1 @ B2)))},
        "edge_metric": "M = diag(1 / edge_length), strictly positive",
        "exact_cochain": {
            "energy": float(exact_energy),
            "recovery_mod_translation": float(recovery),
            "hodge_residual": float(exact_hodge)},
        "non_exact_impulse": {
            "curl_G_norm": float(np.linalg.norm(curl_G)),
            "curl_identity_residual": float(curl_residual),
            "hodge_residual": float(hodge),
            "energy_direct": float(energy),
            "energy_schur": float(energy_schur),
            "energy_difference": float(abs(energy - energy_schur))},
        "weighted_projector": {
            "idempotence_residual": float(projector_idempotence),
            "M_self_adjoint_residual": float(projector_M_adjoint)},
        "classification": "finite-mesh numerical verification; not a continuum limit"
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
