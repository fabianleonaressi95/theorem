#!/usr/bin/env python3
"""Exact cochain gauge-invariance audit for T089 on the canonical Q-ball mesh."""
from __future__ import annotations
import json
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from models.football_shell import build_football_shell


def main():
    rng = np.random.default_rng(20261111)
    mesh = build_football_shell()
    triangles = np.asarray(mesh["triangles"], dtype=int)
    nV = len(mesh["nodes"])
    edges = sorted(mesh["edge_triangles"])
    edge_id = {e: k for k, e in enumerate(edges)}
    nE, nF = len(edges), len(triangles)

    B1 = np.zeros((nV, nE), dtype=np.int64)
    B2 = np.zeros((nE, nF), dtype=np.int64)
    for k, (i, j) in enumerate(edges):
        B1[i, k] = -1
        B1[j, k] = 1

    for f, tri in enumerate(triangles):
        for u, v in zip(tri, np.roll(tri, -1)):
            key = tuple(sorted((int(u), int(v))))
            B2[edge_id[key], f] += 1 if u < v else -1

    chain_residual = int(np.max(np.abs(B1 @ B2)))
    theta = rng.normal(size=nV)
    chi = rng.normal(size=nV)
    a = rng.normal(size=nE)
    q = 1.7
    v = B1.T @ theta - q * a
    curvature = B2.T @ a

    theta_prime = theta + q * chi
    a_prime = a + B1.T @ chi
    v_prime = B1.T @ theta_prime - q * a_prime
    curvature_prime = B2.T @ a_prime

    # Add an arbitrary non-exact edge cochain: face curvature is then nonzero.
    a_nonflat = a.copy()
    a_nonflat[0] += 0.37
    curvature_nonflat = B2.T @ a_nonflat
    curvature_nonflat_prime = B2.T @ (a_nonflat + B1.T @ chi)

    result = {
        "mesh": {
            "vertices": nV,
            "edges": nE,
            "faces": nF,
            "physical_seams": len(mesh["physical_seams"])
        },
        "chain_identity": {
            "max_abs_B1B2": chain_residual,
            "exact_integer_identity": chain_residual == 0
        },
        "gauge_invariance": {
            "max_abs_velocity_cochain_change": float(np.max(np.abs(v_prime - v))),
            "max_abs_curvature_cochain_change": float(np.max(np.abs(curvature_prime - curvature))),
            "max_abs_nonflat_curvature_change": float(np.max(np.abs(curvature_nonflat_prime - curvature_nonflat))),
            "nonflat_curvature_norm": float(np.linalg.norm(curvature_nonflat))
        },
        "classification": "exact incidence identity plus floating-point gauge transformation audit; no continuum convergence"
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if chain_residual != 0:
        raise SystemExit("B1 B2 is not zero")
    if np.max(np.abs(v_prime - v)) > 1e-11:
        raise SystemExit("discrete velocity is not gauge invariant")
    if np.max(np.abs(curvature_prime - curvature)) > 1e-11:
        raise SystemExit("discrete curvature is not gauge invariant")
    if np.max(np.abs(curvature_nonflat_prime - curvature_nonflat)) > 1e-11:
        raise SystemExit("non-flat curvature is not gauge invariant")


if __name__ == "__main__":
    main()
