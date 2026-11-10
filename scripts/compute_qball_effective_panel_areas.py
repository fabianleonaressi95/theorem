#!/usr/bin/env python3
"""Compute panel areas for the parameterized 60-vertex Q-ball shell geometry.

This computes the polygon areas from models.football_shell.build_football_shell.
It does not pretend the default regularized geometry is an experimental scan.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
from models.football_shell import build_football_shell


def polygon_area(points: np.ndarray) -> float:
    """Area of a planar polygon from its oriented boundary vector."""
    p = np.asarray(points, dtype=float)
    area_vector = sum(
        (np.cross(x, y) for x, y in zip(p, np.roll(p, -1, axis=0))),
        np.zeros(3),
    )
    return 0.5 * float(np.linalg.norm(area_vector))


def compute(radius: float, cube_alpha: float, h4_alpha: float) -> dict:
    mesh = build_football_shell(
        radius=radius, cube_alpha=cube_alpha, h4_alpha=h4_alpha
    )
    vertices = np.asarray(mesh["vertices"], dtype=float)
    rows = []
    for i, face in enumerate(mesh["panels"]):
        typ = str(mesh["panel_types"][i])
        area = polygon_area(vertices[np.asarray(face, dtype=int)])
        rows.append({"panel": i, "type": typ, "area": area,
                     "vertex_count": len(face)})
    by_type = {}
    for typ in ("pentagon", "hexagon"):
        values = np.asarray([r["area"] for r in rows if r["type"] == typ])
        by_type[typ] = {
            "count": int(len(values)),
            "area_min": float(values.min()),
            "area_max": float(values.max()),
            "area_mean": float(values.mean()),
            "area_sum": float(values.sum()),
        }
    return {
        "status": "COMPUTED_FROM_PARAMETERIZED_REPOSITORY_SHELL",
        "geometry_parameters": {
            "radius": float(radius), "cube_alpha": float(cube_alpha),
            "h4_alpha": float(h4_alpha),
        },
        "panel_count": len(rows),
        "effective_area_isotropic": float(sum(r["area"] for r in rows)),
        "panel_area_by_type": by_type,
        "panels": rows,
        "anisotropic_area": {
            "status": "NOT_COMPUTED",
            "reason": (
                "Requires a supplied positive tangent tensor field A_T(x) "
                "and a connection-compatible interpolation on each panel. "
                "The 216 canonical PRISM triplett matrices are not present "
                "in the audited repository data."
            ),
            "definition": (
                "A_f(epsilon)=integral_f sqrt(det(I+epsilon*A_T(x))) dA"
            ),
        },
        "physical_validation": {
            "status": "NOT_EXPERIMENTALLY_VALIDATED",
            "reason": (
                "No measured Q-ball surface scan is supplied to this script; "
                "these are areas of the parameterized model geometry."
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--radius", type=float, default=1.0)
    parser.add_argument("--cube-alpha", type=float, default=0.0)
    parser.add_argument("--h4-alpha", type=float, default=0.0)
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    report = compute(args.radius, args.cube_alpha, args.h4_alpha)
    rendered = json.dumps(report, indent=2) + "\n"
    if args.out:
        out = ROOT / args.out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(rendered)
    print(rendered)


if __name__ == "__main__":
    main()
