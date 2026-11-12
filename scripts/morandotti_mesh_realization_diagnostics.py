#!/usr/bin/env python3
"""Audit per-realization mesh quality and two-core exchange symmetry.

The triangle-quality statistic uses only the three corner vertices of each
P3 geometry cell. It is a corner-mesh diagnostic, not a bound on the full
curved-element Jacobian; the latter is separately sampled by the FEM solver.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np


def diagnose_run(row, root=Path(".")):
    path = Path(row["field_export"])
    if not path.is_absolute():
        path = root / path
    with np.load(path) as data:
        coordinates = np.asarray(data["geometry_coordinates"], dtype=float)
        dofmap = np.asarray(data["geometry_dofmap"], dtype=int)
        if dofmap.ndim != 2 or dofmap.shape[1] < 3:
            raise ValueError(f"{path}: expected at least three geometry nodes per cell")
        if not np.isfinite(coordinates).all():
            raise ValueError(f"{path}: non-finite geometry coordinates")

        corners = coordinates[dofmap[:, :3], :2]
        e01 = corners[:, 1] - corners[:, 0]
        e12 = corners[:, 2] - corners[:, 1]
        e20 = corners[:, 0] - corners[:, 2]
        signed_double_area = (
            e01[:, 0] * (corners[:, 2, 1] - corners[:, 0, 1])
            - e01[:, 1] * (corners[:, 2, 0] - corners[:, 0, 0])
        )
        area = 0.5 * signed_double_area
        edge_sq_sum = (
            np.sum(e01 * e01, axis=1)
            + np.sum(e12 * e12, axis=1)
            + np.sum(e20 * e20, axis=1)
        )
        quality = 4.0 * np.sqrt(3.0) * np.abs(area) / np.maximum(edge_sq_sum, 1e-300)

        M = np.asarray(data["M_laplacian"], dtype=float)
        MB = np.asarray(data["M_boundary_flux"], dtype=float)
        MI = np.asarray(data["M_interior_facet_flux"], dtype=float)
        if M.shape != (6, 6) or MB.shape != (6, 6) or MI.shape != (6, 6):
            raise ValueError(f"{path}: expected 6x6 interaction and flux matrices")
        if not (np.isfinite(M).all() and np.isfinite(MB).all() and np.isfinite(MI).all()):
            raise ValueError(f"{path}: non-finite matrix entries")

        self0 = M[1:3, 1:3]
        self1 = M[4:6, 4:6]
        cross01 = M[1:3, 4:6]
        cross10 = M[4:6, 1:3]
        n0, n1 = np.linalg.norm(self0), np.linalg.norm(self1)
        cross_norm = np.linalg.norm(cross01)
        scale = max(0.5 * (n0 + n1), 1e-300)
        reciprocity_scale = max(cross_norm, 1e-300)
        traction = row.get("interior_facet_traction_jump_L2", {})
        traction_values = [float(v) for v in traction.values()]

        return {
            "distance": float(row["distance"]),
            "h_target": float(row["h_target"]),
            "mesh_seed": int(row["mesh_seed"]),
            "cells": int(dofmap.shape[0]),
            "corner_quality_min": float(np.min(quality)),
            "corner_quality_p01": float(np.quantile(quality, 0.01)),
            "corner_quality_median": float(np.median(quality)),
            "minimum_signed_corner_area_from_export": float(np.min(area)),
            "self_block_0_frobenius": float(n0),
            "self_block_1_frobenius": float(n1),
            "self_block_relative_mismatch": float(np.linalg.norm(self0 - self1) / scale),
            "self_block_norm_ratio": float(max(n0, n1) / max(min(n0, n1), 1e-300)),
            "cross_block_frobenius": float(cross_norm),
            "cross_block_reciprocity_relative": float(
                np.linalg.norm(cross01 - cross10.T) / reciprocity_scale
            ),
            "laplacian_symmetry_relative": float(
                np.linalg.norm(M - M.T) / max(np.linalg.norm(M), 1e-300)
            ),
            "laplacian_frobenius": float(np.linalg.norm(M)),
            "boundary_flux_frobenius": float(np.linalg.norm(MB)),
            "interior_facet_flux_frobenius": float(np.linalg.norm(MI)),
            "maximum_interior_facet_traction_jump_L2": max(traction_values, default=None),
        }


def analyze_report(report, root=Path("."), mismatch_threshold=0.05):
    rows = report.get("runs", [])
    if not rows:
        raise ValueError("report contains no realization records")
    diagnostics = [diagnose_run(row, root=root) for row in rows]
    groups = defaultdict(list)
    for row in diagnostics:
        groups[(row["distance"], row["h_target"])].append(row)

    summaries = {}
    for (distance, h), samples in sorted(groups.items()):
        mismatch = np.asarray([x["self_block_relative_mismatch"] for x in samples])
        summaries[f"d{distance:.4f}_h{h:.4f}"] = {
            "realizations": len(samples),
            "self_block_relative_mismatch_median": float(np.median(mismatch)),
            "self_block_relative_mismatch_max": float(np.max(mismatch)),
            "corner_quality_min_over_ensemble": float(
                min(x["corner_quality_min"] for x in samples)
            ),
            "maximum_traction_jump_over_ensemble": float(
                max(x["maximum_interior_facet_traction_jump_L2"] for x in samples)
            ),
            "flagged_seeds_for_core_exchange_mismatch": [
                x["mesh_seed"] for x in samples
                if x["self_block_relative_mismatch"] > mismatch_threshold
            ],
        }

    return {
        "title": "Morandotti per-realization geometry and core-exchange diagnostics",
        "status": "descriptive finite-mesh diagnostics",
        "thresholds": {
            "self_block_relative_mismatch_flag": mismatch_threshold,
            "note": "flag threshold is a screening convention, not a pass/fail theorem",
        },
        "interpretation": {
            "corner_quality": "computed from the three corner vertices only; does not certify the curved P3 map",
            "self_block_relative_mismatch": "relative Frobenius difference between the two 2x2 core self-interaction blocks in the paired local basis ordering",
            "cross_block_reciprocity": "checks equality of the two cross blocks under transpose",
            "traction_jump": "reported interior-facet L2 jump diagnostic; not a continuum residual bound",
        },
        "group_summary": summaries,
        "realizations": diagnostics,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument("--mismatch-threshold", type=float, default=0.05)
    args = parser.parse_args()
    report = json.loads(Path(args.report).read_text(encoding="utf-8"))
    result = analyze_report(report, root=Path(args.root), mismatch_threshold=args.mismatch_threshold)
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
