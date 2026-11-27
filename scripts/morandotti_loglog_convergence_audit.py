#!/usr/bin/env python3
"""Descriptive log-log and tensor-stability audit for Morandotti mesh reports.

This postprocessor does not run FEM. Fits are descriptive diagnostics over the
supplied finite set of meshes; they are not error estimates or continuum proofs.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

JUMP_METRICS = {
    "total": "interior_facet_traction_jump_L2",
    "frank": "interior_facet_traction_jump_frank_L2",
    "burgers": "interior_facet_traction_jump_burgers_L2",
}
TENSOR_METRICS = {
    "total": "interior_facet_traction_jump_second_moment_total_xy",
    "frank": "interior_facet_traction_jump_second_moment_frank_xy",
    "burgers": "interior_facet_traction_jump_second_moment_burgers_xy",
    "cross": "interior_facet_traction_jump_second_moment_cross_xy",
}


def _fit_power_law(h: np.ndarray, y: np.ndarray) -> dict:
    if len(h) < 2 or np.any(h <= 0) or np.any(y <= 0):
        raise ValueError("power-law fit requires at least two positive h and y values")
    xlog, ylog = np.log(h), np.log(y)
    slope, intercept = np.polyfit(xlog, ylog, 1)
    predicted = intercept + slope * xlog
    ss_res = float(np.sum((ylog - predicted) ** 2))
    ss_tot = float(np.sum((ylog - np.mean(ylog)) ** 2))
    return {
        "exponent": float(slope),
        "prefactor": float(np.exp(intercept)),
        "r_squared_log_space": float(1.0 - ss_res / ss_tot) if ss_tot else 1.0,
        "n_levels": int(len(h)),
        "interpretation": "descriptive log-log fit; not an a priori FEM error order",
    }


def _relative_change(a: float, b: float) -> float | None:
    return float((b - a) / abs(a)) if a != 0 else None


def analyze_report(report: dict) -> dict:
    levels = report.get("levels")
    if not isinstance(levels, list) or len(levels) < 2:
        raise ValueError("report must contain at least two mesh levels")

    levels = sorted(levels, key=lambda row: float(row["h_target"]), reverse=True)
    h = np.asarray([float(row["h_target"]) for row in levels], dtype=float)
    if np.any(h <= 0) or len(set(h.tolist())) != len(h):
        raise ValueError("mesh sizes must be positive and unique")
    case_names = set(levels[0].get("reconstruction_cases", {}))
    if not case_names:
        raise ValueError("levels contain no reconstruction_cases")
    if any(set(row.get("reconstruction_cases", {})) != case_names for row in levels):
        raise ValueError("all levels must contain the same reconstruction cases")

    output = {
        "title": "Morandotti traction-jump log-log and tensor-stability audit",
        "source_title": report.get("title"),
        "mesh_sizes_coarse_to_fine": [float(x) for x in h],
        "cells": [int(row.get("cells", 0)) for row in levels],
        "method": {
            "power_law": "fit log(y) = log(C) + p log(h) by ordinary least squares",
            "local_order": "p_i = log(y_fine/y_coarse) / log(h_fine/h_coarse)",
            "tensor_change": "relative Frobenius norm between adjacent levels",
            "scope": "descriptive finite-mesh audit only; no confidence interval or continuum claim",
        },
        "by_case": {},
    }

    for case_name in sorted(case_names):
        rows = [row["reconstruction_cases"][case_name] for row in levels]
        case_out = {"traction_jump_norms": {}, "tensor_relative_changes": {},
                    "additivity": {}}
        for metric, key in JUMP_METRICS.items():
            values = np.asarray([float(row[key]) for row in rows])
            if np.any(values <= 0):
                raise ValueError(f"{case_name}: {key} must be positive for log fit")
            local = [
                float(np.log(values[i + 1] / values[i]) /
                      np.log(h[i + 1] / h[i]))
                for i in range(len(h) - 1)
            ]
            case_out["traction_jump_norms"][metric] = {
                "values": [float(v) for v in values],
                "local_loglog_exponents_coarse_to_fine": local,
                "fit_all_levels": _fit_power_law(h, values),
                "fit_finest_three_levels": _fit_power_law(h[-3:], values[-3:])
                    if len(h) >= 3 else None,
                "coarse_to_fine_relative_change": _relative_change(values[0], values[-1]),
            }

        for metric, key in TENSOR_METRICS.items():
            tensors = [np.asarray(row[key], dtype=float) for row in rows]
            if any(t.shape != tensors[0].shape for t in tensors):
                raise ValueError(f"{case_name}: inconsistent tensor shape for {key}")
            changes = []
            for coarse, fine in zip(tensors[:-1], tensors[1:]):
                denom = float(np.linalg.norm(coarse, ord="fro"))
                changes.append(float(np.linalg.norm(fine - coarse, ord="fro") / denom)
                                if denom else None)
            case_out["tensor_relative_changes"][metric] = changes

        for decomposition_key in (
            "source_quadratic_decomposition",
            "interior_facet_traction_jump_squared_decomposition",
        ):
            records = [row.get(decomposition_key, {}) for row in rows]
            residuals = [float(rec.get("additivity_residual", np.nan)) for rec in records]
            scales = []
            for rec in records:
                terms = [float(v) for k, v in rec.items()
                         if k != "additivity_residual" and isinstance(v, (int, float))]
                scales.append(sum(abs(v) for v in terms))
            case_out["additivity"][decomposition_key] = {
                "absolute_residuals": residuals,
                "relative_residuals": [
                    abs(r) / s if s and np.isfinite(r) else None
                    for r, s in zip(residuals, scales)
                ],
            }
        output["by_case"][case_name] = case_out

    output["conclusion_guardrails"] = [
        "A decreasing jump norm is not evidence of a nonzero limiting jump.",
        "A fitted exponent is not a proven convergence order.",
        "Facet-jump norms and source quadratic energies are distinct observables.",
        "A continuum claim requires additional refinement, consistency/stability analysis, and independent mesh controls.",
    ]
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="five-level FEM report.json")
    parser.add_argument("--out", required=True, help="output audit JSON")
    args = parser.parse_args()
    report = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = analyze_report(report)
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
