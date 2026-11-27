#!/usr/bin/env python3
"""Audit the carrier-derived coframe on all 192 archived Q6 edges.

Inputs are the original PSU fibre archive and the RGS embedding archive.
The script uses archived SO(3) links after checking their normal-based
minimal-rotation formula fit. It does not use Q_tangent as an edge list.
The square quantity is a gauge-covariant path-sum candidate, not a
continuum Cartan torsion theorem.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

N = 64
TOL = 1.0e-10
SAMPLES = 1000
SEED = 20261127
E3 = np.array([0.0, 0.0, 1.0])


def fro(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord="fro"))


def skew(v: np.ndarray) -> np.ndarray:
    x, y, z = v
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def radial_frame(x: np.ndarray) -> np.ndarray:
    n = np.asarray(x, dtype=float) / np.linalg.norm(x)
    reference = np.array([0.0, 0.0, 1.0])
    if abs(float(reference @ n)) > 0.9:
        reference = np.array([1.0, 0.0, 0.0])
    e1 = np.cross(reference, n)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    return np.column_stack((e1, e2, n))


def minimal_rotation(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    a = np.asarray(a, dtype=float) / np.linalg.norm(a)
    b = np.asarray(b, dtype=float) / np.linalg.norm(b)
    c = float(a @ b)
    if 1.0 + c <= 1.0e-12:
        raise ValueError("Antipodal radial pair: minimal rotation is non-unique")
    w = skew(np.cross(a, b))
    return np.eye(3) + w + (w @ w) / (1.0 + c)


def build_edge_lookup(edges: np.ndarray) -> dict[tuple[int, int], int]:
    lookup = {}
    degree = np.zeros(N, dtype=int)
    for k, (g0, h0, _d) in enumerate(edges):
        g, h = int(g0), int(h0)
        if g == h or (g, h) in lookup or (h, g) in lookup:
            raise ValueError(f"duplicate or loop edge {(g, h)}")
        lookup[(g, h)] = k
        degree[g] += 1
        degree[h] += 1
    if len(lookup) != 192 or not np.all(degree == 6):
        raise ValueError(f"Expected 192 edges and degree 6; got {len(lookup)}, {degree.tolist()}")
    return lookup


def q6_coordinate_squares(edges: np.ndarray, lookup: dict[tuple[int, int], int]):
    squares = []
    for i in range(6):
        for j in range(i + 1, 6):
            for g in range(N):
                if ((g >> i) & 1) or ((g >> j) & 1):
                    continue
                gi = g ^ (1 << i)
                gij = gi ^ (1 << j)
                gj = g ^ (1 << j)
                cycle = (g, gi, gij, gj)
                for a, b in zip(cycle, cycle[1:] + cycle[:1]):
                    if (a, b) not in lookup and (b, a) not in lookup:
                        raise ValueError(f"missing coordinate-square edge {(a, b)}")
                squares.append(cycle)
    if len(squares) != 240 or len({tuple(sorted(c)) for c in squares}) != 240:
        raise ValueError("Q6 coordinate-square enumeration did not yield 240 faces")
    return np.asarray(squares, dtype=int)


def directed_rotation(a: int, b: int, rotations: np.ndarray,
                      edges: np.ndarray, lookup: dict[tuple[int, int], int]) -> np.ndarray:
    if (a, b) in lookup:
        return rotations[lookup[(a, b)]]
    if (b, a) in lookup:
        return rotations[lookup[(b, a)]].T
    raise KeyError((a, b))


def directed_coframe(a: int, b: int, points: np.ndarray, frames: np.ndarray,
                     rotations: np.ndarray, edges: np.ndarray,
                     lookup: dict[tuple[int, int], int]) -> np.ndarray:
    rab = directed_rotation(a, b, rotations, edges, lookup)
    delta = points[b] - points[a]
    return 0.5 * (frames[a].T @ delta + rab.T @ frames[b].T @ delta)


def cycle_torsion(cycle: np.ndarray, points: np.ndarray, frames: np.ndarray,
                  rotations: np.ndarray, edges: np.ndarray,
                  lookup: dict[tuple[int, int], int]) -> np.ndarray:
    """Transport every edge increment back to the cycle's initial fibre."""
    total = np.zeros(3)
    prefix = np.eye(3)
    vertices = [int(v) for v in cycle]
    for a, b in zip(vertices, vertices[1:] + vertices[:1]):
        total += prefix.T @ directed_coframe(
            a, b, points, frames, rotations, edges, lookup
        )
        prefix = directed_rotation(a, b, rotations, edges, lookup) @ prefix
    return total


def random_rotation(rng: np.random.Generator) -> np.ndarray:
    w = rng.normal(size=3)
    theta = float(np.linalg.norm(w))
    if theta < 1.0e-14:
        return np.eye(3)
    W = skew(w)
    return (np.eye(3) + np.sin(theta) / theta * W
            + (1.0 - np.cos(theta)) / theta**2 * (W @ W))


def run(fibre_path: Path, embedding_path: Path, output_path: Path) -> dict:
    with np.load(fibre_path, allow_pickle=False) as fz, np.load(
        embedding_path, allow_pickle=False
    ) as ez:
        edges = np.asarray(fz["edges"], dtype=int)
        normals = np.asarray(fz["normals"], dtype=float)
        r_stored = np.asarray(fz["R_SO3"], dtype=float)
        points = np.asarray(ez["X_Oh_reconstructed"], dtype=float)
        states = np.asarray(ez["Q6_states"], dtype=int)

    if edges.shape != (192, 3) or normals.shape != (64, 3):
        raise ValueError("Unexpected Q6 edge/normal archive shapes")
    if r_stored.shape != (192, 3, 3) or points.shape != (64, 3):
        raise ValueError("Unexpected archived transport/embedding shapes")
    expected_states = np.array([[(g >> (5-j)) & 1 for j in range(6)]
                                for g in range(N)], dtype=int)
    if states.shape != (64, 6) or not np.array_equal(states, expected_states):
        raise ValueError("Q6_states do not match binary vertex-label convention")
    for g0, h0, d0 in edges:
        g, h, d = int(g0), int(h0), int(d0)
        if d not in range(6) or h != (g ^ (1 << d)):
            raise ValueError(f"edge direction metadata mismatch: {(g, h, d)}")

    lookup = build_edge_lookup(edges)
    squares = q6_coordinate_squares(edges, lookup)
    radii = np.linalg.norm(points, axis=1)
    if np.any(radii <= 1.0e-14):
        raise ValueError("RGS carrier contains a zero-radius vertex")
    x_normals = points / radii[:, None]
    normal_fit = float(np.max(np.linalg.norm(normals - x_normals, axis=1)))
    if normal_fit > TOL:
        raise AssertionError(f"Archived normals do not match embedding: {normal_fit}")

    canonical = np.asarray([
        minimal_rotation(normals[int(g)], normals[int(h)])
        for g, h, _d in edges
    ])
    formula_residuals = np.linalg.norm(r_stored - canonical, axis=(1, 2))
    formula_fit = float(formula_residuals.max())
    if formula_fit > TOL:
        raise AssertionError(f"Archived SO(3) links fail minimal-rotation fit: {formula_fit}")

    frames = np.asarray([radial_frame(x) for x in points])
    local_rotations = np.asarray([
        frames[int(h)].T @ r_stored[k] @ frames[int(g)]
        for k, (g, h, _d) in enumerate(edges)
    ])
    local_coframes = np.asarray([
        0.5 * (
            frames[int(g)].T @ (points[int(h)] - points[int(g)])
            + local_rotations[k].T @ frames[int(h)].T
              @ (points[int(h)] - points[int(g)])
        )
        for k, (g, h, _d) in enumerate(edges)
    ])

    rotation_orthogonality = max(
        fro(r.T @ r - np.eye(3)) for r in local_rotations
    )
    rotation_determinant = max(
        abs(float(np.linalg.det(r)) - 1.0) for r in local_rotations
    )
    radial_axis_residual = max(
        float(np.linalg.norm(r @ E3 - E3)) for r in local_rotations
    )

    reverse_error = 0.0
    norm_bound_excess = 0.0
    norm_ratios = []
    for k, (g0, h0, _d) in enumerate(edges):
        g, h = int(g0), int(h0)
        e_forward = local_coframes[k]
        e_reverse_direct = directed_coframe(
            h, g, points, frames, local_rotations, edges, lookup
        )
        reverse_error = max(
            reverse_error,
            float(np.linalg.norm(e_reverse_direct + local_rotations[k] @ e_forward))
        )
        ratio = float(np.linalg.norm(e_forward) / np.linalg.norm(points[h] - points[g]))
        norm_ratios.append(ratio)
        norm_bound_excess = max(norm_bound_excess, max(0.0, ratio - 1.0))

    torsions = np.asarray([
        cycle_torsion(cycle, points, frames, local_rotations, edges, lookup)
        for cycle in squares
    ])
    torsion_norms = np.linalg.norm(torsions, axis=1)

    rng = np.random.default_rng(SEED)
    gauge_covariance_error = 0.0
    base_torsions = torsions
    for _ in range(SAMPLES):
        gauges = np.asarray([random_rotation(rng) for _ in range(N)])
        rotated_links = np.asarray([
            gauges[int(h)] @ local_rotations[k] @ gauges[int(g)].T
            for k, (g, h, _d) in enumerate(edges)
        ])
        rotated_coframes = np.asarray([
            gauges[int(g)] @ local_coframes[k]
            for k, (g, _h, _d) in enumerate(edges)
        ])
        # Evaluate the transformed coframe directly, preserving the local gauge action.
        transformed_direct = []
        for cycle in squares:
            total = np.zeros(3)
            prefix = np.eye(3)
            vv = [int(v) for v in cycle]
            for a, b in zip(vv, vv[1:] + vv[:1]):
                if (a, b) in lookup:
                    k = lookup[(a, b)]
                    eab = rotated_coframes[k]
                    rab = rotated_links[k]
                else:
                    k = lookup[(b, a)]
                    rab = rotated_links[k].T
                    eab = -rab.T @ rotated_coframes[k]
                total += prefix.T @ eab
                prefix = rab @ prefix
            transformed_direct.append(total)
        transformed_direct = np.asarray(transformed_direct)
        for idx, cycle in enumerate(squares):
            gauge_covariance_error = max(
                gauge_covariance_error,
                float(np.linalg.norm(
                    transformed_direct[idx] - gauges[int(cycle[0])] @ base_torsions[idx]
                ))
            )

    # Ambient rotations are tested by transporting the chosen frames along
    # with the carrier; this avoids conflating a frame gauge with a new
    # deterministic reference-axis choice.
    ambient_invariance_error = 0.0
    for _ in range(100):
        q = random_rotation(rng)
        points_q = points @ q.T
        frames_q = np.asarray([q @ f for f in frames])
        ambient_links_q = np.asarray([q @ r @ q.T for r in r_stored])
        local_q = np.asarray([
            frames_q[int(h)].T @ ambient_links_q[k] @ frames_q[int(g)]
            for k, (g, h, _d) in enumerate(edges)
        ])
        coframe_q = np.asarray([
            0.5 * (
                frames_q[int(g)].T @ (points_q[int(h)] - points_q[int(g)])
                + local_q[k].T @ frames_q[int(h)].T
                  @ (points_q[int(h)] - points_q[int(g)])
            )
            for k, (g, h, _d) in enumerate(edges)
        ])
        ambient_invariance_error = max(
            ambient_invariance_error,
            float(np.linalg.norm(local_q - local_rotations)),
            float(np.linalg.norm(coframe_q - local_coframes)),
        )

    residuals = {
        "normal_embedding_alignment_max": normal_fit,
        "archived_SO3_minimal_rotation_fit_max": formula_fit,
        "local_SO3_orthogonality_max": float(rotation_orthogonality),
        "local_SO3_determinant_max": float(rotation_determinant),
        "local_radial_axis_fixed_max": float(radial_axis_residual),
        "direct_reverse_coframe_identity_max": float(reverse_error),
        "coframe_norm_bound_excess_max": float(norm_bound_excess),
        "plaquette_torsion_local_gauge_covariance_max": float(gauge_covariance_error),
        "ambient_SO3_covariance_max": float(ambient_invariance_error),
    }
    failures = {name: value for name, value in residuals.items() if value > TOL}
    report = {
        "title": "Q6 archived-connection carrier coframe and square path-sum audit",
        "classification": {
            "archived_connection_alignment": "numerically_verified_if_run_passes",
            "all_192_edge_coframes": "explicit_finite_construction",
            "240_square_path_sum": "gauge_covariant_discrete_candidate",
            "continuum_Cartan_limit": "open",
            "discrete_torsion_Bianchi": "not_defined_not_tested",
            "deWit_Nye_Burgers_identification": "open",
            "Q_tangent_edge_interpretation": "explicitly_not_used",
        },
        "source": {
            "fibre_archive": str(fibre_path),
            "embedding_archive": str(embedding_path),
            "coordinate_order": "Q6_states verified against integer bit labels g=0,...,63",
            "edge_order": "stored edges[g,h,d], validated by h=g xor (1<<d)",
        },
        "counts": {
            "vertices": N,
            "edges": int(len(edges)),
            "coordinate_square_faces": int(len(squares)),
            "degree_min": 6,
            "degree_max": 6,
        },
        "definitions": {
            "local_connection": "Rloc_gh = F_h^T R_SO3_gh F_g",
            "carrier_coframe": "E_gh = 1/2 (F_g^T (X_h-X_g) + Rloc_gh^-1 F_h^T (X_h-X_g))",
            "square_path_sum": "T_v0v1v2v3 = sum_r (R_{r-1}...R_0)^-1 E_{v_r v_{r+1}}",
            "reverse_orientation": "E_hg = -Rloc_gh E_gh",
            "gauge_action": "R'_gh=S_h R_gh S_g^-1; E'_gh=S_g E_gh; T'_square=S_v0 T_square",
        },
        "statistics": {
            "coframe_to_chord_norm_ratio_min": float(min(norm_ratios)),
            "coframe_to_chord_norm_ratio_max": float(max(norm_ratios)),
            "square_path_sum_norm_min": float(torsion_norms.min()),
            "square_path_sum_norm_mean": float(torsion_norms.mean()),
            "square_path_sum_norm_max": float(torsion_norms.max()),
        },
        "residuals": residuals,
        "samples": {"independent_vertex_gauges": SAMPLES, "ambient_rotations": 100},
        "seed": SEED,
        "tolerance": TOL,
        "failures": failures,
        "evidence_boundary": [
            "The square path sum is a finite gauge-covariant cochain candidate.",
            "It is not identified with continuum Cartan torsion without a refinement/convergence theorem.",
            "No torsion Bianchi identity, deWit-Nye density, or Burgers vector is asserted.",
            "The four-point tetrahedron fixture in the preceding audit is not used as a Q6 incidence cell.",
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    if failures:
        raise AssertionError(f"Q6 coframe audit failures: {failures}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fibre", type=Path,
                        default=Path("data/psu_fibre_connection_matrices.npz"))
    parser.add_argument("--embedding", type=Path,
                        default=Path("data/RGS_PSU_all_matrices.npz"))
    parser.add_argument("--out", type=Path,
                        default=Path("audits/Q6_ARCHIVED_CARRIER_COFRAME_2026-11-27.json"))
    args = parser.parse_args()
    run(args.fibre, args.embedding, args.out)


if __name__ == "__main__":
    main()
