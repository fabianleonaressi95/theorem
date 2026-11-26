#!/usr/bin/env python3
"""Run the RGS–PRISM pentagon/hexagon football anisotropy audit."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from models.football_anisotropy import run_audit, solve_panel_model


def write_svg(path: Path, displacement: np.ndarray, panel_types: np.ndarray):
    width, height = 960, 420
    left, right, top, bottom = 64, 24, 40, 64
    plot_w, plot_h = width - left - right, height - top - bottom
    low, high = float(displacement.min()), float(displacement.max())
    span = max(high - low, 1e-12)
    bar_w = plot_w / len(displacement)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="64" y="24" font-family="sans-serif" font-size="17">Panel-normal displacement by face (pentagons and hexagons)</text>',
        f'<line x1="{left}" y1="{top + plot_h}" x2="{width-right}" y2="{top + plot_h}" stroke="#333"/>',
    ]
    for index, (value, kind) in enumerate(zip(displacement, panel_types)):
        bar_h = (float(value) - low) / span * (plot_h * 0.78) + plot_h * 0.12
        x = left + index * bar_w + 1
        y = top + plot_h - bar_h
        fill = "#d97706" if kind == "pentagon" else "#2563eb"
        parts.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{max(1, bar_w-2):.2f}" '
            f'height="{bar_h:.2f}" fill="{fill}"/>'
        )
    parts.extend([
        f'<text x="{left}" y="{height-22}" font-family="sans-serif" font-size="12">Panel index (12 pentagons, then 20 hexagons)</text>',
        f'<text x="{left}" y="{height-42}" font-family="sans-serif" font-size="12">min={low:.6g}; max={high:.6g}; displacement units are model units</text>',
        '<rect x="690" y="34" width="12" height="12" fill="#d97706"/><text x="708" y="45" font-family="sans-serif" font-size="12">Pentagon</text>',
        '<rect x="790" y="34" width="12" height="12" fill="#2563eb"/><text x="808" y="45" font-family="sans-serif" font-size="12">Hexagon</text>',
        '</svg>',
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pressure", type=float, default=0.01)
    parser.add_argument("--C5", type=float, default=1.25)
    parser.add_argument("--C6", type=float, default=1.0)
    parser.add_argument("--coupling", type=float, default=0.15)
    parser.add_argument("--json", type=Path, default=Path("reports/football_anisotropy_audit.json"))
    parser.add_argument("--svg", type=Path, default=Path("reports/football_anisotropy_displacement.svg"))
    args = parser.parse_args()

    mesh, displacement, _, report = run_audit(
        args.pressure, args.C5, args.C6, args.coupling
    )
    sweep = []
    for ratio in (1.0, 1.1, 1.25, 1.5, 2.0):
        _, _, local = solve_panel_model(
            mesh, args.pressure, args.C6 * ratio, args.C6, args.coupling
        )
        sweep.append({
            "C5_over_C6": ratio,
            "pentagon_hexagon_displacement_contrast": local["solution"][
                "pentagon_hexagon_displacement_contrast"
            ],
            "panel_center_radial_rms_anisotropy": local["solution"][
                "panel_center_radial_rms_anisotropy"
            ],
            "linear_system_relative_residual": local["solution"][
                "linear_system_relative_residual"
            ],
        })
    report["sensitivity_sweep"] = sweep
    report["reproducibility"] = {
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "command": (
            "python scripts/run_football_anisotropy_audit.py "
            f"--pressure {args.pressure} --C5 {args.C5} --C6 {args.C6} "
            f"--coupling {args.coupling}"
        ),
    }

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    write_svg(args.svg, displacement, mesh["panel_types"])
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
