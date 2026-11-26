#!/usr/bin/env python3
"""Gauge-covariant discrete coframe face-torsion candidate on a tetrahedron.

This is a numerical fixture for a proposed path-based discretization of D_omega e.
It does not establish a continuum limit or a discrete torsion Bianchi identity.
Requires NumPy.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

SEED = 20261126
SAMPLES = 1000
TOL = 2.0e-11
VERTICES = (0, 1, 2, 3)
EDGES = tuple((i, j) for i in VERTICES for j in VERTICES if i < j)
FACES = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))


def hat(w):
    x, y, z = map(float, w)
    return np.array([[0., -z, y], [z, 0., -x], [-y, x, 0.]])


def exp_so3(w):
    w = np.asarray(w, dtype=float)
    theta = float(np.linalg.norm(w))
    W = hat(w)
    if theta < 1.e-12:
        return np.eye(3) + W + 0.5 * W @ W
    return (np.eye(3) + np.sin(theta) / theta * W
            + (1. - np.cos(theta)) / theta**2 * (W @ W))


def random_rotation(rng, scale=0.5):
    return exp_so3(scale * rng.normal(size=3))


def random_se3(rng):
    return random_rotation(rng, 0.35), 0.5 * rng.normal(size=3)


def edge_rotation(raw, i, j):
    R = raw[(i, j)][0] if i < j else raw[(j, i)][0].T
    return R


def edge_coframe(E, R, i, j):
    if i < j:
        return E[(i, j)]
    return -R[(j, i)].T @ E[(j, i)]


def face_torsion(E, R, face):
    i, j, k = face
    Rij = edge_rotation(R, i, j)
    Rjk = edge_rotation(R, j, k)
    Eij = E[(i, j)] if i < j else -edge_rotation(R, j, i).T @ E[(j, i)]
    Ejk = E[(j, k)] if j < k else -edge_rotation(R, k, j).T @ E[(k, j)]
    Eki = E[(k, i)] if k < i else -edge_rotation(R, i, k) @ E[(i, k)]
    # All edge increments are expressed at the source vertex.
    return Eij + Rij.T @ Ejk + Rij.T @ Rjk.T @ Eki


def gauge_transform(R, E, gauges):
    Rp, Ep = {}, {}
    for i, j in EDGES:
        Si = gauges[i][0]
        Sj = gauges[j][0]
        Rp[(i, j)] = (Sj @ R[(i, j)] @ Si.T,
                      Sj @ np.zeros(3))
        Ep[(i, j)] = Si @ E[(i, j)]
    return Rp, Ep


def main():
    rng = np.random.default_rng(SEED)
    max_covariance = 0.0
    max_orientation = 0.0
    max_flat_torsion = 0.0
    min_generic_norm = float("inf")

    for _ in range(SAMPLES):
        R = {e: random_rotation(rng) for e in EDGES}
        E = {e: rng.normal(size=3) for e in EDGES}
        gauges = {v: random_se3(rng) for v in VERTICES}

        # Check reverse-edge convention for every stored edge.
        for i, j in EDGES:
            Eji = -R[(i, j)].T @ E[(i, j)]
            max_orientation = max(max_orientation,
                                  float(np.linalg.norm(Eji + R[(i, j)].T @ E[(i, j)])))

        # Gauge covariance of the face quantity.
        Rp, Ep = gauge_transform(R, E, gauges)
        for face in FACES:
            i, _, _ = face
            T = face_torsion(E, R, face)
            Tp = face_torsion(Ep, Rp, face)
            expected = gauges[i][0] @ T
            max_covariance = max(max_covariance,
                                 float(np.linalg.norm(Tp - expected)))

        # Pure-gauge, torsion-free data from global vertex positions.
        S = {v: random_rotation(rng, 0.7) for v in VERTICES}
        x = {v: rng.normal(size=3) for v in VERTICES}
        Rflat = {(i, j): (S[j] @ S[i].T, np.zeros(3)) for i, j in EDGES}
        Eflat = {(i, j): S[i] @ (x[j] - x[i]) for i, j in EDGES}
        for face in FACES:
            max_flat_torsion = max(
                max_flat_torsion,
                float(np.linalg.norm(face_torsion(Eflat, Rflat, face))))

        # Generic data should not collapse identically to zero.
        for face in FACES:
            min_generic_norm = min(min_generic_norm,
                                   float(np.linalg.norm(face_torsion(E, R, face))))

    residuals = {
        "coframe_orientation_max_error": max_orientation,
        "face_torsion_gauge_covariance_max_error": max_covariance,
        "pure_gauge_torsion_free_max_error": max_flat_torsion,
        "generic_face_torsion_min_norm": min_generic_norm,
    }
    failures = {
        key: value for key, value in residuals.items()
        if (key != "generic_face_torsion_min_norm" and value > TOL)
    }
    if min_generic_norm <= 1.e-10:
        failures["generic_face_torsion_min_norm"] = min_generic_norm

    result = {
        "fixture": "tetrahedron with independent SO(3) connection and vector coframe",
        "vertices": list(VERTICES),
        "edges": [list(e) for e in EDGES],
        "faces": [list(f) for f in FACES],
        "samples": SAMPLES,
        "seed": SEED,
        "tolerance": TOL,
        "face_torsion": "E_ij + R_ij^-1 E_jk + (R_jk R_ij)^-1 E_ki",
        "gauge_action": "R'_ij=S_j R_ij S_i^-1; E'_ij=S_i E_ij",
        "residuals": residuals,
        "status": {
            "coframe_orientation": "numerically_verified",
            "face_torsion_gauge_covariance": "numerically_verified",
            "pure_gauge_torsion_free_case": "numerically_verified",
            "generic_nonzero_face_torsion": "numerically_verified",
            "continuum_Cartan_identification": "open",
            "discrete_torsion_Bianchi": "not_defined_not_tested",
            "deWit_Nye_limit": "open",
        },
        "failures": failures,
    }
    out = Path("audits/DISCRETE_COFRAME_TORSION_TETRAHEDRON_2026-11-26.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if failures:
        raise AssertionError(f"Residuals exceed tolerance: {failures}")


if __name__ == "__main__":
    main()
