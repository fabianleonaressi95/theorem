#!/usr/bin/env python3
"""Deterministic SE(3) tetrahedron fixture.

Tests group composition/inversion, vertex-gauge covariance, a pure-gauge flat
connection, and a controlled translational face-holonomy defect.

This is NOT a proof or numerical test of a 3-cell Bianchi identity.
Requires numpy.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

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
    return np.eye(3) + (np.sin(theta) / theta) * W + (
        (1. - np.cos(theta)) / theta**2
    ) * (W @ W)


def compose(A, B):
    """A after B; both are (R,t) with x |-> R x + t."""
    RA, tA = A
    RB, tB = B
    return RA @ RB, RA @ tB + tA


def inverse(A):
    R, t = A
    Rt = R.T
    return Rt, -Rt @ t


def identity():
    return np.eye(3), np.zeros(3)


def edge_transport(raw, i, j):
    """Return transport i->j, using inverse for reversed orientation."""
    return raw[(i, j)] if i < j else inverse(raw[(j, i)])


def holonomy(raw, face):
    """Oriented loop i->j->k->i, based at i."""
    i, j, k = face
    return compose(edge_transport(raw, k, i),
                   compose(edge_transport(raw, j, k),
                           edge_transport(raw, i, j)))


def gauge_transform(raw, gauges):
    """G_ij -> h_j G_ij h_i^{-1}; store only i<j."""
    out = {}
    for i, j in EDGES:
        out[(i, j)] = compose(gauges[j],
                              compose(raw[(i, j)], inverse(gauges[i])))
    return out


def pure_gauge(gauges):
    """Flat connection G_ij = h_j h_i^{-1}."""
    return {(i, j): compose(gauges[j], inverse(gauges[i]))
            for i, j in EDGES}


def random_gauges(seed):
    rng = np.random.default_rng(seed)
    result = {}
    for i in VERTICES:
        result[i] = (exp_so3(0.35 * rng.normal(size=3)),
                     0.4 * rng.normal(size=3))
    return result


def random_connection(seed):
    rng = np.random.default_rng(seed)
    return {(i, j): (exp_so3(0.2 * rng.normal(size=3)),
                     0.3 * rng.normal(size=3))
            for i, j in EDGES}


def max_group_error(A, B):
    return max(float(np.linalg.norm(A[0] - B[0])),
               float(np.linalg.norm(A[1] - B[1])))


def rotation_angle(R):
    c = np.clip((np.trace(R) - 1.) / 2., -1., 1.)
    return float(np.arccos(c))


def main():
    # Algebraic sanity checks on every stored edge.
    raw = random_connection(20261121)
    inverse_error = max(max_group_error(compose(inverse(g), g), identity())
                        for g in raw.values())

    # Gauge covariance: H'_ijk = h_i H_ijk h_i^{-1}.
    gauges = random_gauges(314159)
    transformed = gauge_transform(raw, gauges)
    covariance_error = 0.
    for face in FACES:
        i = face[0]
        expected = compose(gauges[i],
                           compose(holonomy(raw, face), inverse(gauges[i])))
        covariance_error = max(
            covariance_error,
            max_group_error(holonomy(transformed, face), expected))

    # Pure-gauge connection must have identity holonomy on every 2-face.
    flat = pure_gauge(gauges)
    flat_error = max(max_group_error(holonomy(flat, f), identity())
                     for f in FACES)

    # A controlled translational perturbation on one oriented edge.
    # The perturbation is intentionally not called a Burgers vector:
    # that interpretation needs a material/coframe convention.
    defective = {e: (g[0].copy(), g[1].copy()) for e, g in flat.items()}
    defective[(0, 1)] = compose((np.eye(3), np.array([0.125, -0.05, 0.02])),
                                defective[(0, 1)])
    defects = {str(f): holonomy(defective, f) for f in FACES}
    translational_norms = {
        str(f): float(np.linalg.norm(H[1])) for f, H in
        ((f, defects[str(f)]) for f in FACES)
    }
    affected = sum(v > 1.e-8 for v in translational_norms.values())

    # Gauge transform the defective connection and verify norm invariance.
    defective_gauged = gauge_transform(defective, gauges)
    gauge_defect_error = 0.
    for face in FACES:
        before = holonomy(defective, face)
        after = holonomy(defective_gauged, face)
        expected = compose(gauges[face[0]],
                           compose(before, inverse(gauges[face[0]])))
        gauge_defect_error = max(gauge_defect_error,
                                 max_group_error(after, expected))
        if abs(np.linalg.norm(before[1]) - np.linalg.norm(after[1])) > TOL:
            raise AssertionError("translational defect norm is not gauge invariant")

    results = {
        "fixture": "single oriented tetrahedron boundary",
        "vertices": list(VERTICES),
        "edges": [list(e) for e in EDGES],
        "faces": [list(f) for f in FACES],
        "tolerance": TOL,
        "inverse_identity_max_error": inverse_error,
        "face_holonomy_gauge_covariance_max_error": covariance_error,
        "pure_gauge_flatness_max_error": flat_error,
        "controlled_edge_translation": [0.125, -0.05, 0.02],
        "face_translation_defect_norms": translational_norms,
        "number_of_faces_with_nonzero_translation_defect": affected,
        "defect_gauge_covariance_max_error": gauge_defect_error,
        "status": {
            "SE3_group_law": "numerically_verified",
            "vertex_gauge_covariance": "numerically_verified",
            "pure_gauge_flatness": "numerically_verified",
            "controlled_translational_face_holonomy": "numerically_verified",
            "3_cell_Bianchi_identity": "not_tested",
            "Cartan_torsion_identification": "open",
            "Burgers_vector_interpretation": "not_assigned"
        }
    }

    for key in ("inverse_identity_max_error",
                "face_holonomy_gauge_covariance_max_error",
                "pure_gauge_flatness_max_error",
                "defect_gauge_covariance_max_error"):
        if results[key] > TOL:
            raise AssertionError(f"{key}={results[key]} exceeds {TOL}")
    if affected == 0:
        raise AssertionError("controlled translation produced no face defect")

    out = Path("audits/SE3_TETRAHEDRON_FIXTURE_2026-11-21.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
