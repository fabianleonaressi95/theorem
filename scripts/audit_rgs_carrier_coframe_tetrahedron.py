#!/usr/bin/env python3
"""Build a gauge-covariant edge coframe from the hash-checked RGS 64-site seed.

This is a four-vertex geometric fixture extracted from that carrier. It does
not assert that the selected tetrahedron is a Q6 subcomplex.
Requires NumPy; run from any working directory.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.rgs_seed_64_reconstruction import load_rgs_seed_data  # noqa: E402

SEED = 20261126
SAMPLES = 1000
TOL = 2.0e-11
VERTEX_IDS = (0, 8, 32, 56)
FACES = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))


def minimal_rotation(n_i: np.ndarray, n_j: np.ndarray) -> np.ndarray:
    """Shortest SO(3) rotation taking unit radial n_i to unit radial n_j."""
    a = np.array(n_i, dtype=float, copy=True)
    b = np.array(n_j, dtype=float, copy=True)
    a /= np.linalg.norm(a)
    b /= np.linalg.norm(b)
    v = np.cross(a, b)
    c = float(np.dot(a, b))
    s = float(np.linalg.norm(v))
    if s < 1.0e-13:
        if c > 0.0:
            return np.eye(3)
        raise ValueError("Antipodal radial normals: minimal rotation is non-unique")
    K = np.array([[0.0, -v[2], v[1]],
                  [v[2], 0.0, -v[0]],
                  [-v[1], v[0], 0.0]])
    return np.eye(3) + K + (K @ K) * ((1.0 - c) / (s * s))


def radial_frame(x: np.ndarray) -> np.ndarray:
    """Deterministic oriented frame F=[e1,e2,n], with third leg radial."""
    n = np.asarray(x, dtype=float) / np.linalg.norm(x)
    reference = np.array([0.0, 0.0, 1.0])
    if abs(float(reference @ n)) > 0.9:
        reference = np.array([1.0, 0.0, 0.0])
    e1 = np.cross(reference, n)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    return np.column_stack((e1, e2, n))


def edge_data(points: np.ndarray):
    frames = [radial_frame(x) for x in points]
    ambient_R, R, E = {}, {}, {}
    for i in range(4):
        for j in range(i + 1, 4):
            Rg = minimal_rotation(points[i], points[j])
            ambient_R[(i, j)] = Rg
            R[(i, j)] = frames[j].T @ Rg @ frames[i]
            delta = points[j] - points[i]
            source_chord = frames[i].T @ delta
            target_chord = frames[j].T @ delta
            E[(i, j)] = 0.5 * (source_chord + R[(i, j)].T @ target_chord)
    return frames, ambient_R, R, E


def edge_rotation(R, i: int, j: int) -> np.ndarray:
    return R[(i, j)] if i < j else R[(j, i)].T


def edge_coframe(R, E, i: int, j: int) -> np.ndarray:
    if i < j:
        return E[(i, j)]
    return -edge_rotation(R, j, i) @ E[(j, i)]


def directed_edge_coframe(points, frames, R, i: int, j: int) -> np.ndarray:
    """Evaluate the symmetric chord average directly in either orientation."""
    delta = points[j] - points[i]
    Rij = edge_rotation(R, i, j)
    return 0.5 * (frames[i].T @ delta + Rij.T @ frames[j].T @ delta)


def face_torsion(R, E, face) -> np.ndarray:
    i, j, k = face
    Rij = edge_rotation(R, i, j)
    Rjk = edge_rotation(R, j, k)
    return (edge_coframe(R, E, i, j)
            + Rij.T @ edge_coframe(R, E, j, k)
            + Rij.T @ Rjk.T @ edge_coframe(R, E, k, i))


def random_rotation(rng: np.random.Generator) -> np.ndarray:
    w = rng.normal(size=3)
    theta = float(np.linalg.norm(w))
    if theta < 1.0e-14:
        return np.eye(3)
    W = np.array([[0.0, -w[2], w[1]],
                  [w[2], 0.0, -w[0]],
                  [-w[1], w[0], 0.0]])
    return (np.eye(3) + np.sin(theta) / theta * W
            + (1.0 - np.cos(theta)) / theta**2 * (W @ W))


def main() -> None:
    X = load_rgs_seed_data().coordinates
    points = X[list(VERTEX_IDS)].copy()
    if points.shape != (4, 3):
        raise RuntimeError("Unexpected selected RGS carrier shape")
    volume = float(np.linalg.det(np.column_stack((
        points[1] - points[0], points[2] - points[0], points[3] - points[0]
    ))) / 6.0)
    if abs(volume) < 1.0e-10:
        raise RuntimeError("Selected RGS carrier vertices are coplanar")

    frames, ambient_R, R, E = edge_data(points)
    torsions = {str(face): face_torsion(R, E, face) for face in FACES}
    torsion_norms = {key: float(np.linalg.norm(value))
                     for key, value in torsions.items()}

    orientation_error = 0.0
    coframe_norm_bound_excess = 0.0
    coframe_norm_ratios = {}
    rotation_orthogonality_error = 0.0
    rotation_determinant_error = 0.0
    radial_transport_error = 0.0
    for (i, j), e in E.items():
        reverse_direct = directed_edge_coframe(points, frames, R, j, i)
        orientation_error = max(
            orientation_error,
            float(np.linalg.norm(reverse_direct + R[(i, j)] @ e)))
        ratio = float(np.linalg.norm(e) / np.linalg.norm(points[j] - points[i]))
        coframe_norm_ratios[str((i, j))] = ratio
        coframe_norm_bound_excess = max(coframe_norm_bound_excess, max(0.0, ratio - 1.0))
        rij = R[(i, j)]
        rotation_orthogonality_error = max(
            rotation_orthogonality_error,
            float(np.linalg.norm(rij.T @ rij - np.eye(3))))
        rotation_determinant_error = max(
            rotation_determinant_error, abs(float(np.linalg.det(rij) - 1.0)))
        ni = points[i] / np.linalg.norm(points[i])
        nj = points[j] / np.linalg.norm(points[j])
        radial_transport_error = max(
            radial_transport_error,
            float(np.linalg.norm(ambient_R[(i, j)] @ ni - nj)))

    rng = np.random.default_rng(SEED)
    max_gauge_covariance = 0.0
    max_global_rotation_invariance = 0.0
    for _ in range(SAMPLES):
        gauges = {v: random_rotation(rng) for v in range(4)}
        Rp = {(i, j): gauges[j] @ R[(i, j)] @ gauges[i].T for i, j in R}
        Ep = {(i, j): gauges[i] @ E[(i, j)] for i, j in E}
        for face in FACES:
            base = face[0]
            residual = (face_torsion(Rp, Ep, face)
                        - gauges[base] @ face_torsion(R, E, face))
            max_gauge_covariance = max(
                max_gauge_covariance, float(np.linalg.norm(residual)))

        Q = random_rotation(rng)
        rotated_points = points @ Q.T
        rotated_frames = [Q @ frame for frame in frames]
        for i, j in E:
            Rg2 = minimal_rotation(rotated_points[i], rotated_points[j])
            R2 = rotated_frames[j].T @ Rg2 @ rotated_frames[i]
            delta2 = rotated_points[j] - rotated_points[i]
            E2 = 0.5 * (rotated_frames[i].T @ delta2
                        + R2.T @ rotated_frames[j].T @ delta2)
            max_global_rotation_invariance = max(
                max_global_rotation_invariance,
                float(np.linalg.norm(R2 - R[(i, j)])),
                float(np.linalg.norm(E2 - E[(i, j)])))

    residuals = {
        "coframe_orientation_max_error": orientation_error,
        "coframe_norm_upper_bound_max_excess": coframe_norm_bound_excess,
        "local_SO3_orthogonality_max_error": rotation_orthogonality_error,
        "local_SO3_determinant_max_error": rotation_determinant_error,
        "ambient_radial_transport_max_error": radial_transport_error,
        "face_torsion_gauge_covariance_max_error": max_gauge_covariance,
        "global_SO3_invariance_max_error": max_global_rotation_invariance,
    }
    failures = {name: value for name, value in residuals.items()
                if value > TOL}
    if min(torsion_norms.values()) <= 1.0e-10:
        failures["unexpected_zero_geometric_face_torsion"] = min(torsion_norms.values())

    result = {
        "fixture": "RGS 64-site seed; selected four-point tetrahedron",
        "source": "src.rgs_seed_64_reconstruction.load_rgs_seed_data",
        "source_coordinate_sha256": "6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf",
        "selected_carrier_vertex_ids": list(VERTEX_IDS),
        "points": points.tolist(),
        "radii": np.linalg.norm(points, axis=1).tolist(),
        "oriented_tetrahedron_volume": volume,
        "edge_pairs_local": [list(e) for e in E],
        "edge_lengths": {str(e): float(np.linalg.norm(points[e[1]] - points[e[0]])) for e in E},
        "coframe_to_chord_norm_ratios": coframe_norm_ratios,
        "radial_increments": {
            str((i, j)): float(np.linalg.norm(points[j]) - np.linalg.norm(points[i]))
            for i, j in E
        },
        "face_torsion_vectors": {k: v.tolist() for k, v in torsions.items()},
        "face_torsion_norms": torsion_norms,
        "samples": SAMPLES,
        "seed": SEED,
        "tolerance": TOL,
        "definition": {
            "n_i": "X_i / ||X_i||",
            "ambient_transport": "shortest SO(3) rotation taking n_i to n_j",
            "local_transport": "R_ij = F_j^T Rg_ij F_i",
            "geometric_coframe": "E_ij = 1/2 (F_i^T deltaX_ij + R_ij^-1 F_j^T deltaX_ij)",
            "face_torsion": "E_ij + R_ij^-1 E_jk + (R_jk R_ij)^-1 E_ki",
            "reverse_orientation": "E_ji = -R_ij E_ij",
        },
        "gauge_action": "R'_ij=S_j R_ij S_i^-1; E'_ij=S_i E_ij",
        "residuals": residuals,
        "failures": failures,
        "classification": {
            "hash_checked_RGS_coordinates": "source_verified",
            "carrier_derived_edge_coframe": "explicit_finite_construction",
            "face_torsion_gauge_covariance": "numerically_verified",
            "global_SO3_invariance": "numerically_verified",
            "Q6_incidence_alignment": "not_claimed_not_tested",
            "continuum_Cartan_limit": "open",
            "discrete_torsion_Bianchi": "not_defined_not_tested",
            "deWit_Nye_Burgers_identification": "open",
        },
    }
    out = ROOT / "audits" / "RGS_CARRIER_DERIVED_COFRAME_TETRAHEDRON_2026-11-26.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if failures:
        raise AssertionError(f"Audit failures: {failures}")


if __name__ == "__main__":
    main()
