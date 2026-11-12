#!/usr/bin/env python3
"""Separate mesh-resolution mean shifts from within-resolution remeshing spread.

Within-resolution spread combines seed, topology, and node-placement effects.
It is descriptive and is not interpreted as pure random-seed noise.
The within-resolution component combines seed, topology, and node-placement
variation; it is not interpreted as a pure random-seed error estimate.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

METRICS = ("signed_anisotropy_A_d", "normalized_coupling_C_d")


def analyze_report(report):
    runs = report.get("runs", [])
    if not runs:
        raise ValueError("report contains no realization records")

    distances = sorted({float(row["distance"]) for row in runs})
    output = {
        "title": "Morandotti resolution-versus-remeshing variability decomposition",
        "method": "balanced descriptive sum-of-squares decomposition by target mesh size",
        "interpretation": {
            "between_resolution": "variation of resolution-specific sample means",
            "within_resolution": "variation among independent remesh realizations at fixed resolution; combines seed, topology, and node-placement effects",
            "inferential_status": "descriptive only; no confidence intervals, hypothesis tests, or continuum-limit claim",
        },
        "by_distance": {},
    }

    for distance in distances:
        subset = [row for row in runs if float(row["distance"]) == distance]
        mesh_sizes = sorted({float(row["h_target"]) for row in subset})
        groups = {
            h: [row for row in subset if float(row["h_target"]) == h]
            for h in mesh_sizes
        }
        counts = {len(group) for group in groups.values()}
        if len(mesh_sizes) < 2 or any(count < 2 for count in counts):
            raise ValueError(
                f"d={distance}: need at least two resolutions and two remeshes per resolution"
            )
        if len(counts) != 1:
            raise ValueError(
                f"d={distance}: balanced decomposition requires equal remesh counts per resolution"
            )

    distances = sorted({float(row["distance"]) for row in runs})
    for distance in distances:
        subset = [row for row in runs if float(row["distance"]) == distance]
        mesh_sizes = sorted({float(row["h_target"]) for row in subset})
        groups = {h: [row for row in subset if float(row["h_target"]) == h] for h in mesh_sizes}
        if len(mesh_sizes) < 2 or any(len(group) < 2 for group in groups.values()):
            raise ValueError(f"d={distance}: need at least two resolutions and two remeshes per resolution")
        distance_result = {"realizations": len(subset), "mesh_sizes": {}}
        for h, group in groups.items():
            distance_result["mesh_sizes"][f"{h:.6f}"] = {
                "n": len(group),
                **{
                    metric: {
                        "mean": float(np.mean([row[metric] for row in group])),
                        "sample_std": float(np.std([row[metric] for row in group], ddof=1)),
                        "minimum": float(np.min([row[metric] for row in group])),
                        "maximum": float(np.max([row[metric] for row in group])),
                    }
                    for metric in METRICS
                },
            }

        distance_result["decomposition"] = {}
        for metric in METRICS:
            values = np.asarray([float(row[metric]) for row in subset])
            grand_mean = float(np.mean(values))
            ss_between = 0.0
            ss_within = 0.0
            all_means = []
            for h, group in groups.items():
                x = np.asarray([float(row[metric]) for row in group])
                mean = float(np.mean(x))
                ss_between += len(x) * (mean - grand_mean) ** 2
                ss_within += float(np.sum((x - mean) ** 2))
                all_means.append(mean)
            ss_total = ss_between + ss_within
            distance_result["decomposition"][metric] = {
                "grand_mean": grand_mean,
                "between_resolution_sd_component": float(np.sqrt(ss_between / len(values))),
                "pooled_within_resolution_sample_sd": float(
                    np.sqrt(ss_within / (len(values) - len(mesh_sizes)))
                ),
                "between_resolution_sum_squares_fraction": (
                    float(ss_between / ss_total) if ss_total else 0.0
                ),
                "within_resolution_sum_squares_fraction": (
                    float(ss_within / ss_total) if ss_total else 0.0
                ),
                "resolution_mean_range": float(max(all_means) - min(all_means)),
            }

                "pooled_within_resolution_sample_sd": float(np.sqrt(ss_within / (len(values) - len(mesh_sizes)))),
                "between_resolution_sum_squares_fraction": float(ss_between / ss_total) if ss_total else 0.0,
                "within_resolution_sum_squares_fraction": float(ss_within / ss_total) if ss_total else 0.0,
                "resolution_mean_range": float(max(all_means) - min(all_means)),
            }
        ordered_h = sorted(mesh_sizes)
        distance_result["adjacent_fine_resolution_mean_shifts"] = {}
        for metric in METRICS:
            shifts = []
            for coarse_h, fine_h in zip(ordered_h[1:], ordered_h[:-1]):
                coarse_mean = float(np.mean([row[metric] for row in groups[coarse_h]]))
                fine_mean = float(np.mean([row[metric] for row in groups[fine_h]]))
                coarse_mean = float(np.mean([r[metric] for r in groups[coarse_h]]))
                fine_mean = float(np.mean([r[metric] for r in groups[fine_h]]))
                shifts.append({
                    "from_h": coarse_h,
                    "to_h": fine_h,
                    "absolute_mean_change": fine_mean - coarse_mean,
                    "relative_mean_change": (
                        (fine_mean - coarse_mean) / abs(coarse_mean)
                        if coarse_mean else None
                    ),
                })
            distance_result["adjacent_fine_resolution_mean_shifts"][metric] = shifts

        output["by_distance"][f"{distance:.4f}"] = distance_result

                    "relative_mean_change": (fine_mean - coarse_mean) / abs(coarse_mean) if coarse_mean else None,
                })
            distance_result["adjacent_fine_resolution_mean_shifts"][metric] = shifts
        output["by_distance"][f"{distance:.4f}"] = distance_result
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    report = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = analyze_report(report)
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
