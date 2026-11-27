#!/usr/bin/env python3
"""Exact non-Abelian curvature Bianchi identity on one oriented tetrahedron.

The identity is an algebraic boundary-of-boundary cancellation for arbitrary
SE(3) edge transports. It is not the discrete torsion Bianchi identity.
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
# Oriented tetrahedron boundary: [123] - [023] + [013] - [012].
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
    return (np.eye(3) + (np.sin(theta) / theta) * W
            + ((1. - np.cos(theta)) / theta**2) * (W @ W))


def compose(A, B):
    """A after B; (R,t) acts by x |-> R x + t."""
    RA, tA = A
    RB, tB = B
    return RA @ RB, RA @ tB + tA


def inverse(A):
    R, t = A
    Rt = R.T
    return Rt, -Rt @ t


def identity():
    return np.eye(3), np.zeros(3)


def group_error(A, B):
    return max(float(np.linalg.norm(A[0] - B[0])),
               float(np.linalg.norm(A[1] - B[1])))


def edge_transport(raw, i, j):
    """Transport i -> j; reverse orientation uses the group inverse."""
    return raw[(i, j)] if i < j else inverse(raw[(j, i)])


def face_holonomy(raw, face):
    """H_ijk = G_ki G_jk G_ij, based at i."""
    i, j, k = face
    return compose(edge_transport(raw, k, i),
                   compose(edge_transport(raw, j, k),
                           edge_transport(raw, i, j)))


def gauge_transform(raw, gauges):
    """G_ij -> h_j G_ij h_i^{-1}, storing i < j."""
    return {
        (i, j): compose(gauges[j],
                        compose(raw[(i, j)], inverse(gauges[i])))
        for i, j in EDGES
    }


def random_se3(rng, rotation_scale=0.45, translation_scale=0.4):
    return (exp_so3(rotation_scale * rng.normal(size=3)),
            translation_scale * rng.normal(size=3))


def bianchi_product(raw):
    """All factors are based at vertex 0.

    K_123 = G_01^{-1} H_123 G_01 transports the (1-based) face
    holonomy to the fibre at 0. The ordered boundary product is
        H_013 K_123 H_012^{-1} H_023^{-1} = identity.
    """
    H012 = face_holonomy(raw, (0, 1, 2))
    H013 = face_holonomy(raw, (0, 1, 3))
    H023 = face_holonomy(raw, (0, 2, 3))
    H123 = face_holonomy(raw, (1, 2, 3))
    G01 = raw[(0, 1)]
    K123 = compose(inverse(G01), compose(H123, G01))
    product = compose(H013,
                      compose(K123,
                              compose(inverse(H012), inverse(H023))))
    return product, (H012, H013, H023, H123), K123


def main():
    rng = np.random.default_rng(SEED)
    max_bianchi_error = 0.0
    max_face_covariance_error = 0.0
    max_bianchi_gauge_covariance_error = 0.0
    max_inverse_error = 0.0

    for _ in range(SAMPLES):
        raw = {edge: random_se3(rng) for edge in EDGES}
        gauges = {v: random_se3(rng, 0.35, 0.5) for v in VERTICES}

        # Group inverse sanity check on both sides.
        for G in raw.values():
            max_inverse_error = max(
                max_inverse_error,
                group_error(compose(G, inverse(G)), identity()),
                group_error(compose(inverse(G), G), identity()))

        product, face_H, _ = bianchi_product(raw)
        max_bianchi_error = max(max_bianchi_error,
                                group_error(product, identity()))

        transformed = gauge_transform(raw, gauges)
        transformed_product, transformed_H, _ = bianchi_product(transformed)

        # Each face holonomy is compared in its own base-point fibre.
        for face, H, Hp in zip(FACES, face_H, transformed_H):
            base = face[0]
            expected = compose(gauges[base],
                               compose(H, inverse(gauges[base])))
            max_face_covariance_error = max(
                max_face_covariance_error, group_error(Hp, expected))

        # Since every factor in the ordered Bianchi product is based at 0,
        # the full product transforms by conjugation with h_0.
        expected_product = compose(
            gauges[0], compose(product, inverse(gauges[0])))
        max_bianchi_gauge_covariance_error = max(
            max_bianchi_gauge_covariance_error,
            group_error(transformed_product, expected_product))

    residuals = {
        "group_inverse_max_error": max_inverse_error,
        "ordered_bianchi_identity_max_error": max_bianchi_error,
        "face_holonomy_gauge_covariance_max_error":
            max_face_covariance_error,
        "bianchi_product_gauge_covariance_max_error":
            max_bianchi_gauge_covariance_error,
    }
    failures = {name: value for name, value in residuals.items()
                if value > TOL}
    result = {
        "fixture": "oriented tetrahedron with arbitrary SE(3) edge transports",
        "vertices": list(VERTICES),
        "edges": [list(e) for e in EDGES],
        "oriented_boundary": ["+[123]", "-[023]", "+[013]", "-[012]"],
        "samples": SAMPLES,
        "seed": SEED,
        "tolerance": TOL,
        "identity": (
            "H_013 (G_01^-1 H_123 G_01) H_012^-1 H_023^-1 = I"
        ),
        "residuals": residuals,
        "status": {
            "SE3_inverse": "numerically_verified",
            "face_holonomy_gauge_covariance": "numerically_verified",
            "transported_nonabelian_curvature_bianchi":
                "numerically_verified",
            "bianchi_gauge_covariance": "numerically_verified",
            "discrete_torsion_bianchi": "not_defined_not_tested",
            "Cartan_torsion_identification": "open",
            "deWit_Nye_limit": "open",
        },
        "interpretation": (
            "The identity is exact by cancellation of oriented edge "
            "transports. Random numerical tests check implementation and "
            "conventions; they are not an independent proof."
        ),
        "failures": failures,
    }

    out = Path("audits/SE3_TETRAHEDRAL_BIANCHI_2026-11-26.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if failures:
        raise AssertionError(f"Residuals exceed tolerance: {failures}")


if __name__ == "__main__":
    main()
