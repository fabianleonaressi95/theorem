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

    def encode(self, vertex: Sequence[int]) -> int:
        """Row-major index for a five-coordinate periodic vertex."""
        if len(vertex) != DIMENSION:
            raise ValueError("vertex must have five coordinates")
        index = 0
        for coordinate, length in zip(vertex, self.lengths):
            if isinstance(coordinate, bool) or not isinstance(coordinate, (int, np.integer)):
                raise ValueError("vertex coordinates must be integers")
            if not 0 <= int(coordinate) < length:
                raise ValueError("vertex coordinate out of range")
            index = index * length + int(coordinate)
        return index

    def decode(self, index: int) -> tuple[int, ...]:
        """Inverse of encode, without allocating the graph."""
        if isinstance(index, bool) or not isinstance(index, (int, np.integer)):
            raise ValueError("index must be an integer")
        if not 0 <= int(index) < self.vertex_count:
            raise ValueError("index out of range")
        value = int(index)
        coordinates = [0] * DIMENSION
        for j in range(DIMENSION - 1, -1, -1):
            coordinates[j] = value % self.lengths[j]
            value //= self.lengths[j]
        return tuple(coordinates)

    def neighbor(self, vertex: Sequence[int], axis: int, step: int = 1) -> tuple[int, ...]:
        """Periodic nearest neighbour in one coordinate direction."""
        if len(vertex) != DIMENSION:
            raise ValueError("vertex must have five coordinates")
        if isinstance(axis, bool) or not isinstance(axis, (int, np.integer)) or not 0 <= int(axis) < DIMENSION:
            raise ValueError("axis must be an integer from 0 to 4")
        if step not in (-1, 1):
            raise ValueError("step must be -1 or 1")
        point = list(vertex)
        for j, (coordinate, length) in enumerate(zip(point, self.lengths)):
            if isinstance(coordinate, bool) or not isinstance(coordinate, (int, np.integer)):
                raise ValueError("vertex coordinates must be integers")
            if not 0 <= int(coordinate) < length:
                raise ValueError("vertex coordinate out of range")
            point[j] = int(coordinate)
        j = int(axis)
        point[j] = (point[j] + step) % self.lengths[j]
        return tuple(point)

    def positive_direction_edges(self):
        """Lazily yield each unoriented edge once as (tail, head, axis).

        This iterator is intended for small explicit audits. Do not materialize
        it for large levels: the exact edge count is DIMENSION * vertex_count.
        """
        import itertools
        for vertex in itertools.product(*(range(n) for n in self.lengths)):
            for axis in range(DIMENSION):
                yield vertex, self.neighbor(vertex, axis, 1), axis

    def mode_energy(self, mode: Sequence[int]) -> dict:
        """Exact energy and L2 norm of a sampled cosine Fourier mode.

        The cosine is f(x)=cos(2π k·x). The sampled mean-square is 1/2
        unless every component is constant-sign aliased; that exceptional
        case is rejected. The continuum energy is 2π² |k|².
        """
        k = self.validate_mode(mode)
        if all((2 * q) % n == 0 for q, n in zip(k, self.lengths)):
            raise ValueError("sampled cosine is aliased to a constant-sign pattern")
        norm_squared = 0.5
        discrete_eigenvalue = self.discrete_eigenvalue(k)
        discrete_energy = norm_squared * discrete_eigenvalue
        continuum_energy = 2.0 * math.pi**2 * sum(q * q for q in k)
        return {
            "mode": list(k),
            "mass_norm_squared": norm_squared,
            "discrete_energy": discrete_energy,
            "continuum_energy": continuum_energy,
            "relative_energy_error": abs(discrete_energy - continuum_energy) / max(1.0, continuum_energy),
        }

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
        energy_records = [graph.mode_energy(mode) for mode in modes]
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
            "smooth_mode_energies": energy_records,
            "checks": {
                "M0_vertex_edge_counts": graph.vertex_count == 69120 * int(level)**5
                    and graph.degree == 10
                    and graph.vertex_count * graph.degree // 2 == 5 * graph.vertex_count,
                "M1_flat_mesh_positive": all(h > 0.0 for h in graph.spacings),
                "M2_mass_weights_positive": graph.cell_volume > 0.0
                    and all(weight > 0.0 for weight in graph.conductances)
                    and math.isclose(graph.vertex_count * graph.cell_volume, 1.0, rel_tol=0.0, abs_tol=1e-14),
                "M3_index_roundtrip": all(
                    graph.decode(graph.encode(point)) == point
                    for point in ((0, 0, 0, 0, 0), tuple(n - 1 for n in graph.lengths),
                                  tuple(n // 2 for n in graph.lengths))
                ),
                "M4_fixed_mode_energy": all(
                    math.isfinite(item["discrete_energy"]) and item["relative_energy_error"] < 1.0
                    for item in energy_records
                ),
            },
        })
    return {
        "model": "C64_x_C6^3_x_C5_product_torus_refinement",
        "dimension": DIMENSION,
        "status": "flat_reference_refinement_not_curved_RGS_Mosco_theorem",
        "form": "sum_j sum_x (cell_volume/h_j^2) |u(x+e_j)-u(x)|^2",
        "measure": "cell_volume at each vertex",
        "identification": "piecewise-constant reconstruction on the unit flat five-torus",
        "milestone_checks": {
            key: all(row["checks"][key] for row in rows)
            for key in rows[0]["checks"]
        },
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
