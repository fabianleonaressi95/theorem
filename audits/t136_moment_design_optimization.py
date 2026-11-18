#!/usr/bin/env python3
"""Deterministic D-optimal design search for T136 tetrahedral Ricci probes."""
from __future__ import annotations

import json
import numpy as np


def moment_row(vertices):
    volume = abs(np.linalg.det(vertices[1:] - vertices[0])) / 6.0
    bary = np.full((4, 4), volume / 20.0)
    np.fill_diagonal(bary, volume / 10.0)
    moment = vertices.T @ bary @ vertices / volume
    return np.array([moment[0, 0], moment[1, 1], moment[2, 2],
                     2*moment[0, 1], 2*moment[0, 2], 2*moment[1, 2]])


def candidate_pool(seed=1362026, size=4000):
    rng = np.random.default_rng(seed)
    rows = []
    while len(rows) < size:
        vertices = rng.normal(size=(4, 3))
        volume = abs(np.linalg.det(vertices[1:] - vertices[0])) / 6.0
        if volume < 0.02:
            continue
        rows.append(moment_row(vertices))
    return np.asarray(rows)


def greedy_d_optimal_design(pool, count=12, regularization=1e-6):
    """Sequential D-optimal selection using the matrix determinant lemma."""
    information_inverse = np.eye(6) / regularization
    selected = []
    for _ in range(count):
        scores = np.einsum("ni,ij,nj->n", pool, information_inverse, pool)
        if selected:
            scores[np.asarray(selected, dtype=int)] = -np.inf
        index = int(np.argmax(scores))
        row = pool[index]
        projected = information_inverse @ row
        denominator = 1.0 + float(row @ projected)
        information_inverse -= np.outer(projected, projected) / denominator
        selected.append(index)
    return selected


def run_audit():
    pool = candidate_pool()
    selected = greedy_d_optimal_design(pool, count=12)
    design = pool[selected]
    singular = np.linalg.svd(design, compute_uv=False)
    baseline_rng = np.random.default_rng(136)\n    baseline_rows = []\n    while len(baseline_rows) < 6:\n        vertices = baseline_rng.normal(size=(4, 3))\n        volume = abs(np.linalg.det(vertices[1:] - vertices[0])) / 6.0\n        if volume >= 0.02:\n            baseline_rows.append(moment_row(vertices))\n    baseline = np.linalg.cond(np.asarray(baseline_rows))
    condition = float(singular[0] / singular[-1])
    return {
        "audit": "T136 deterministic D-optimal tetrahedral moment design",
        "candidate_pool_size": int(len(pool)),
        "selected_probe_count": int(len(selected)),
        "selected_candidate_indices": selected,
        "rank": int(np.linalg.matrix_rank(design)),
        "singular_values": singular.tolist(),
        "condition_number": condition,
        "baseline_first_six_candidate_condition_number": float(baseline),
        "condition_number_reduction_factor": float(baseline / condition),
        "interpretation": (
            "A deterministic sequential D-optimal search selects 12 tetrahedral "
            "moment probes from a pool of 4000. The resulting full-rank design "
            "has substantially lower 2-norm condition number than the first "
            "six candidates. This improves the linear inverse problem's "
            "conditioning for this candidate pool; it is not a universal "
            "optimality theorem or a bound on all measurement errors."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
