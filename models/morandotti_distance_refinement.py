"""Pure post-processing for mesh-refined two-core Morandotti distance sweeps.
The FE solve is performed by scripts/rgs_morandotti_two_core_c0_ipdg.py.
"""
from __future__ import annotations
import numpy as np

def summarize_distance_refinement(records):
    """Summarize records with h, distance and a 6x6 interaction matrix."""
    if not records:
        raise ValueError("at least one refinement record is required")
    normalized = []
    for item in records:
        h, distance = float(item["h"]), float(item["distance"])
        matrix = np.asarray(item["M_laplacian"], dtype=float)
        if not np.isfinite(h) or h <= 0 or not np.isfinite(distance) or distance <= 0:
            raise ValueError("mesh size and core separation must be finite and positive")
        if matrix.shape != (6, 6) or not np.isfinite(matrix).all():
            raise ValueError("each interaction matrix must be finite and 6x6")
        symmetry_relative = float(np.linalg.norm(matrix-matrix.T, "fro") /
                                  max(np.linalg.norm(matrix, "fro"), 1e-300))
        if symmetry_relative > 1e-8:
            raise ValueError(f"interaction matrix is not symmetric: {symmetry_relative:g}")
        cross, self_block = matrix[1:3, 4:6], matrix[1:3, 1:3]
        parallel, transverse = float(cross[0, 0]), float(cross[1, 1])
        denominator = abs(parallel) + abs(transverse)
        normalized.append({
            "h": h, "distance": distance, "M_laplacian": matrix,
            "M_parallel_01": parallel, "M_transverse_01": transverse,
            "signed_anisotropy_A_d": (parallel-transverse)/denominator if denominator else 0.0,
            "normalized_coupling_C_d": float(np.linalg.norm(cross, "fro") /
                max(np.linalg.norm(self_block, "fro"), 1e-300)),
            "cross_block_frobenius": float(np.linalg.norm(cross, "fro")),
            "self_block_frobenius_core0": float(np.linalg.norm(self_block, "fro")),
            "matrix_symmetry_relative": symmetry_relative,
            "minimum_eigenvalue_symmetric_part": float(np.linalg.eigvalsh(0.5*(matrix+matrix.T)).min()),
        })
    distances = sorted({x["distance"] for x in normalized})
    levels = sorted({x["h"] for x in normalized}, reverse=True)
    expected = {(h, d) for h in levels for d in distances}
    observed = {(x["h"], x["distance"]) for x in normalized}
    if observed != expected or len(normalized) != len(expected):
        raise ValueError("records must contain exactly one result for every (h, distance) pair")
    by_pair = {(x["h"], x["distance"]): x for x in normalized}
    convergence = []
    for distance in distances:
        for coarse, fine in zip(levels, levels[1:]):
            Mc = by_pair[(coarse, distance)]["M_laplacian"]
            Mf = by_pair[(fine, distance)]["M_laplacian"]
            convergence.append({
                "distance": distance, "from_h": coarse, "to_h": fine,
                "relative_interaction_matrix_change": float(np.linalg.norm(Mf-Mc, "fro") /
                    max(np.linalg.norm(Mf, "fro"), 1e-300)),
            })
    rows = [{k: v for k, v in x.items() if k != "M_laplacian"}
            for x in sorted(normalized, key=lambda q: (q["distance"], -q["h"]))]
    return {
        "distances": distances, "mesh_sizes_coarse_to_fine": levels,
        "results": rows, "matrix_refinement_comparisons": convergence,
        "interpretation": "Finite-mesh diagnostics only; no continuum decay law, mesh-independent limit, force law, or material calibration is inferred.",
    }
