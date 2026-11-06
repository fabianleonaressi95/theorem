"""Exact-symbol calibration for a refining C64 x C6^3 x C5 product torus.

At level m the graph is C_(64m) □ C_(6m)^3 □ C_(5m).
This is a flat five-torus reference refinement, not yet the curved RGS
cell complex. No full adjacency matrix is assembled; all checks use the
exact Fourier symbol and geometric weights.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from typing import Sequence

import numpy as np

BASE_LENGTHS = (64, 6, 6, 6, 5)
DIMENSION = len(BASE_LENGTHS)


@dataclass(frozen=True)
class PrismProductRefinement:
    level: int

    def __post_init__(self) -> None:
        if isinstance(self.level, bool) or not isinstance(self.level, (int, np.integer)) or self.level < 1:
            raise ValueError("level must be a positive integer")

    @property
    def lengths(self) -> tuple[int, ...]:
        return tuple(n * int(self.level) for n in BASE_LENGTHS)

    @property
    def vertex_count(self) -> int:
        return math.prod(self.lengths)

    @property
    def degree(self) -> int:
        return 2 * DIMENSION

    @property
    def spacings(self) -> tuple[float, ...]:
        return tuple(1.0 / n for n in self.lengths)

    @property
    def cell_volume(self) -> float:
        return 1.0 / self.vertex_count

    @property
    def conductances(self) -> tuple[float, ...]:
        return tuple(self.cell_volume / (h * h) for h in self.spacings)

    @property
    def intrinsic_edge_lengths(self) -> tuple[float, ...]:
        # For each direction j, two incident edges contribute:
        # 2 * (cell_volume/h_j^2) * (h_j^2/(2d)) = cell_volume/d.
        return tuple(h / math.sqrt(2.0 * DIMENSION) for h in self.spacings)

    def validate_mode(self, mode: Sequence[int]) -> tuple[int, ...]:
        if len(mode) != DIMENSION:
            raise ValueError(f"mode must have {DIMENSION} integer components")
        out = []
        for k, n in zip(mode, self.lengths):
            if isinstance(k, bool) or not isinstance(k, (int, np.integer)):
                raise ValueError("Fourier mode components must be integers")
            if abs(int(k)) > n // 2:
                raise ValueError("mode component lies outside the canonical frequency range")
            out.append(int(k))
        return tuple(out)

    def discrete_eigenvalue(self, mode: Sequence[int]) -> float:
        k = self.validate_mode(mode)
        return float(4.0 * sum(
            n * n * math.sin(math.pi * q / n) ** 2
            for n, q in zip(self.lengths, k)
        ))

    @staticmethod
    def continuum_eigenvalue(mode: Sequence[int]) -> float:
        if len(mode) != DIMENSION:
            raise ValueError(f"mode must have {DIMENSION} integer components")
        values = []
        for q in mode:
            if isinstance(q, bool) or not isinstance(q, (int, np.integer)):
                raise ValueError("Fourier mode components must be integers")
            values.append(int(q))
        return float(4.0 * math.pi**2 * sum(q * q for q in values))

    def intrinsic_metric_residual(self) -> float:
        lhs = sum(
            2.0 * b * ell * ell
            for b, ell in zip(self.conductances, self.intrinsic_edge_lengths)
        )
        return abs(lhs - self.cell_volume)

    def mode_record(self, mode: Sequence[int]) -> dict:
        k = self.validate_mode(mode)
        discrete = self.discrete_eigenvalue(k)
        continuum = self.continuum_eigenvalue(k)
        return {
            "mode": list(k),
            "discrete_eigenvalue": discrete,
            "continuum_eigenvalue": continuum,
            "absolute_error": abs(discrete - continuum),
            "relative_error": abs(discrete - continuum) / max(1.0, continuum),
        }


def audit_refinements(
    levels: Sequence[int],
    modes: Sequence[Sequence[int]] = ((1, 0, 0, 0, 0), (0, 1, 0, 0, 0),
                                      (1, 1, 0, 0, 0), (1, 1, 1, 1, 1)),
) -> dict:
    rows = []
    for level in levels:
        graph = PrismProductRefinement(level)
        records = [graph.mode_record(mode) for mode in modes]
        rows.append({
            "level": int(level),
            "lengths": list(graph.lengths),
            "vertices": graph.vertex_count,
            "degree": graph.degree,
            "mesh_max": max(graph.spacings),
            "cell_volume": graph.cell_volume,
            "total_mass": graph.vertex_count * graph.cell_volume,
            "conductances": list(graph.conductances),
            "intrinsic_metric_residual": graph.intrinsic_metric_residual(),
            "modes": records,
        })
    return {
        "model": "C64_x_C6^3_x_C5_product_torus_refinement",
        "dimension": DIMENSION,
        "status": "flat_reference_refinement_not_curved_RGS_Mosco_theorem",
        "form": "sum_j sum_x (cell_volume/h_j^2) |u(x+e_j)-u(x)|^2",
        "measure": "cell_volume at each vertex",
        "identification": "piecewise-constant reconstruction on the unit flat five-torus",
        "rows": rows,
    }


def parse_mode(raw: str) -> tuple[int, ...]:
    try:
        values = tuple(int(part.strip()) for part in raw.split(","))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("mode must be comma-separated integers") from exc
    if len(values) != DIMENSION:
        raise argparse.ArgumentTypeError(f"mode must contain {DIMENSION} integers")
    return values


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--levels", type=int, nargs="+", default=[1, 2, 4, 8, 16])
    parser.add_argument("--mode", type=parse_mode, action="append", default=None)
    args = parser.parse_args()
    modes = args.mode or [
        (1, 0, 0, 0, 0), (0, 1, 0, 0, 0),
        (1, 1, 0, 0, 0), (1, 1, 1, 1, 1),
    ]
    print(json.dumps(audit_refinements(args.levels, modes), indent=2))


if __name__ == "__main__":
    main()
