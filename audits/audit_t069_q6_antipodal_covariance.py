#!/usr/bin/env python3
"""Reproducible finite audit for T069: RGS seed, Q6 involutions and Walsh sectors.

The six-bit labels are big-endian. The recovered RGS seed is ordered as
8 base blocks (first three bits), each with 8 sign-fibre states (last three
bits). Therefore coordinate inversion flips the last three bits (v ^ 0b000111),
whereas the canonical Q6 graph antipode flips all six bits (v ^ 0b111111).
These are different involutions.
"""
from __future__ import annotations

from itertools import product
import json
import numpy as np


ORBIT_VALUES = {
    "cube_inner": 0.47863916086470326,
    "small_1": 0.48042984818593559,
    "small_2": 0.48230704367200045,
    "cube_outer": 0.95183963342906408,
    "large_1": 1.5073116806169751,
    "large_2": 1.9039106736116611,
}


def recovered_seed() -> np.ndarray:
    v = ORBIT_VALUES
    reps = np.asarray([
        (v["cube_inner"], v["cube_inner"], v["cube_inner"]),
        (v["large_1"], v["large_1"], v["small_1"]),
        (v["large_1"], v["small_1"], v["large_1"]),
        (v["small_1"], v["large_1"], v["large_1"]),
        (v["large_2"], v["small_2"], v["small_2"]),
        (v["small_2"], v["large_2"], v["small_2"]),
        (v["small_2"], v["small_2"], v["large_2"]),
        (v["cube_outer"], v["cube_outer"], v["cube_outer"]),
    ], dtype=np.float64)
    signs = np.asarray(list(product((-1.0, 1.0), repeat=3)))
    return np.asarray([s * p for p in reps for s in signs], dtype=np.float64)


def walsh_matrix() -> np.ndarray:
    labels = np.arange(64, dtype=np.int64)
    bits = ((labels[:, None] >> np.arange(5, -1, -1)) & 1).astype(np.int64)
    rows = []
    for mask in range(64):
        mask_bits = ((mask >> np.arange(5, -1, -1)) & 1).astype(np.int64)
        rows.append((-1.0) ** (bits @ mask_bits))
    return np.asarray(rows, dtype=np.float64)


def pair_covariance(x: np.ndarray, involution: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    labels = np.arange(64, dtype=np.int64)
    partner = labels ^ involution
    representatives = labels[labels < partner]
    paired = partner[representatives]
    means = (x[representatives] + x[paired]) / 2.0
    differences = (x[representatives] - x[paired]) / 2.0
    global_mean = means.mean(axis=0)
    within = differences.T @ differences / 32.0  # p=1/2 in each pair
    centered_means = means - global_mean
    between = centered_means.T @ centered_means / 32.0
    return means, within, between


def run_audit() -> dict[str, object]:
    x = recovered_seed()
    labels = np.arange(64, dtype=np.int64)
    q6_antipode = labels ^ 0b111111
    geometric_inversion = labels ^ 0b000111

    q6_residual = float(np.max(np.abs(x[q6_antipode] + x)))
    geometric_residual = float(np.max(np.abs(x[geometric_inversion] + x)))
    mean = x.mean(axis=0)
    centered = x - mean
    point_covariance = centered.T @ centered / 64.0

    _, q6_within, q6_between = pair_covariance(x, 0b111111)
    _, geom_within, geom_between = pair_covariance(x, 0b000111)

    H = walsh_matrix()
    coeff = H.T @ x / 64.0
    masks = np.arange(64, dtype=np.int64)
    q6_even = np.asarray([int(m).bit_count() % 2 == 0 for m in masks])
    geom_even = np.asarray([int(m & 0b000111).bit_count() % 2 == 0 for m in masks])
    q6_even_energy = float(np.sum(coeff[q6_even] ** 2))
    q6_odd_energy = float(np.sum(coeff[~q6_even] ** 2))
    geom_even_energy = float(np.sum(coeff[geom_even] ** 2))
    geom_odd_energy = float(np.sum(coeff[~geom_even] ** 2))

    report = {
        "audit": "T069_RGS_Q6_ANTIPODAL_WALSH_COVARIANCE_V1",
        "conventions": {
            "vertex_labels": "six-bit big-endian integers 0..63",
            "seed_order": "first three bits select one of 8 base blocks; last three bits select sign fibre",
            "Q6_graph_antipode": "v -> v XOR 0b111111",
            "RGS_coordinate_inversion": "v -> v XOR 0b000111",
            "pair_weights": "uniform over 32 unordered pairs; conditional sign probability p=1/2",
            "Walsh_coefficients": "H.T @ X / 64; H[v,S]=(-1)^(v dot S)",
        },
        "involution_checks": {
            "q6_global_antipode_coordinate_residual": q6_residual,
            "rgs_coordinate_inversion_residual": geometric_residual,
            "involutions_are_distinct": bool(q6_residual > 1e-12 and geometric_residual <= 1e-12),
        },
        "point_cloud": {
            "shape": list(x.shape),
            "mean": mean.tolist(),
            "covariance": point_covariance.tolist(),
            "covariance_eigenvalues": np.linalg.eigvalsh(point_covariance).tolist(),
            "covariance_rank": int(np.linalg.matrix_rank(point_covariance, tol=1e-12)),
        },
        "q6_global_antipodal_pairing": {
            "within_covariance": q6_within.tolist(),
            "between_pair_means_covariance": q6_between.tolist(),
            "total": (q6_within + q6_between).tolist(),
            "identity_residual": float(np.linalg.norm(q6_within + q6_between - point_covariance)),
        },
        "rgs_coordinate_inversion_pairing": {
            "within_covariance": geom_within.tolist(),
            "between_pair_means_covariance": geom_between.tolist(),
            "total": (geom_within + geom_between).tolist(),
            "identity_residual": float(np.linalg.norm(geom_within + geom_between - point_covariance)),
        },
        "walsh_energy": {
            "q6_even": q6_even_energy,
            "q6_odd": q6_odd_energy,
            "q6_total": q6_even_energy + q6_odd_energy,
            "geometric_inversion_even": geom_even_energy,
            "geometric_inversion_odd": geom_odd_energy,
            "geometric_inversion_total": geom_even_energy + geom_odd_energy,
        },
        "checks": {
            "64_by_3_seed": bool(x.shape == (64, 3)),
            "point_mean_zero": bool(np.max(np.abs(mean)) < 1e-12),
            "point_covariance_is_5_over_4_identity": bool(np.max(np.abs(point_covariance - 1.25 * np.eye(3))) < 1e-12),
            "coordinate_inversion_is_last_three_bit_flip": bool(geometric_residual < 1e-12),
            "global_q6_antipode_is_not_coordinate_inversion": bool(q6_residual > 1e-3),
            "global_q6_pair_covariance_law": bool(np.linalg.norm(q6_within + q6_between - point_covariance) < 1e-12),
            "geometric_pair_means_vanish": bool(np.max(np.abs(geom_between)) < 1e-12),
            "geometric_pair_covariance_matches_point_covariance": bool(np.linalg.norm(geom_within - point_covariance) < 1e-12),
            "walsh_geometric_even_sector_vanishes": bool(geom_even_energy < 1e-24),
            "walsh_total_energy_parseval": bool(abs(q6_even_energy + q6_odd_energy - np.sum(x * x) / 64.0) < 1e-12),
        },
        "scope": {
            "proved": [
                "Walsh parity under each explicitly defined bit-flip involution",
                "law of total covariance for the finite uniform pair partition",
            ],
            "numerically_verified": [
                "the archived RGS seed has coordinate inversion v XOR 0b000111",
                "the canonical Q6 graph antipode v XOR 0b111111 is not that coordinate inversion",
                "the seed point-cloud covariance is (5/4) I_3",
            ],
            "open": [
                "a canonical map from Q6 vertex observables to geometric cells and their within-cell covariance",
                "a dynamical phase or oscillation law",
                "a physical interpretation of the Bernoulli sign variable",
            ],
        },
    }
    if not all(report["checks"].values()):
        raise AssertionError("T069 finite audit failed")
    return report


def main() -> None:
    print(json.dumps(run_audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
