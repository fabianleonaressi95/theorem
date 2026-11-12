#!/usr/bin/env python3
"""Audit eight trigram phases on T^2 and all Q6 edge/plaquette holonomies."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
from typing import Sequence

N_TRIGRAMS = 8
N_VERTICES = 64
TAU = 2.0 * math.pi


def wrap(angle: float) -> float:
    """Principal representative in (-pi, pi]."""
    value = (float(angle) + math.pi) % TAU - math.pi
    return math.pi if math.isclose(value, -math.pi, abs_tol=1e-14) else value


def validate_phases(phases: Sequence[float]) -> list[float]:
    if len(phases) != N_TRIGRAMS:
        raise ValueError("exactly eight trigram phases (radians) are required")
    values = [float(x) for x in phases]
    if not all(math.isfinite(x) for x in values):
        raise ValueError("all phases must be finite")
    return values


def phase_point(h: int, phases: Sequence[float]) -> tuple[float, float]:
    if not 0 <= h < N_VERTICES:
        raise ValueError("hexagram label must lie in {0,...,63}")
    lower, upper = h & 7, (h >> 3) & 7
    return phases[lower] % TAU, phases[upper] % TAU


def complement_residuals(phases: Sequence[float]) -> list[float]:
    p = validate_phases(phases)
    return [wrap(p[t ^ 7] - p[t] - math.pi) for t in range(8)]


def complement_displacements(phases: Sequence[float]) -> list[list[float]]:
    p = validate_phases(phases)
    out = []
    for h in range(N_VERTICES):
        lo, hi = h & 7, (h >> 3) & 7
        out.append([wrap(p[lo ^ 7] - p[lo]),
                    wrap(p[hi ^ 7] - p[hi])])
    return out


def edge_increment(h: int, hp: int, bit: int,
                   phases: Sequence[float]) -> float:
    lo, hi = h & 7, (h >> 3) & 7
    lop, hip = hp & 7, (hp >> 3) & 7
    if bit < 3:
        return wrap(phases[lop] - phases[lo])
    return wrap(phases[hip] - phases[hi])


def enumerate_edges() -> list[tuple[int, int, int]]:
    return [(h, h ^ (1 << bit), bit)
            for h in range(N_VERTICES) for bit in range(6)
            if not (h & (1 << bit))]


def enumerate_plaquettes() -> list[tuple[int, int, int, int, int, int]]:
    squares = []
    for i in range(6):
        for j in range(i + 1, 6):
            for h in range(N_VERTICES):
                if h & (1 << i) or h & (1 << j):
                    continue
                hi, hij, hj = h ^ (1 << i), h ^ (1 << i) ^ (1 << j), h ^ (1 << j)
                squares.append((h, hi, hij, hj, i, j))
    return squares


def plaquette_audit(phases: Sequence[float]) -> list[dict[str, float | int]]:
    p = validate_phases(phases)
    records = []
    for h, hi, hij, hj, i, j in enumerate_plaquettes():
        increments = (
            edge_increment(h, hi, i, p),
            edge_increment(hi, hij, j, p),
            edge_increment(hij, hj, i, p),
            edge_increment(hj, h, j, p),
        )
        raw = sum(increments)
        winding = int(round(raw / TAU))
        records.append({
            "base_vertex": h, "directions": [i, j],
            "raw_phase_sum": raw, "branch_winding": winding,
            "holonomy_real": math.cos(raw), "holonomy_imag": math.sin(raw),
            "circulation_mod_2pi": wrap(raw),
        })
    return records


def audit(phases: Sequence[float], tolerance: float = 1e-10) -> dict[str, object]:
    p = validate_phases(phases)
    edges = enumerate_edges()
    plaquettes = plaquette_audit(p)
    max_holonomy_error = max(
        math.hypot(float(x["holonomy_real"]) - 1.0,
                   float(x["holonomy_imag"])) for x in plaquettes
    )
    max_circulation = max(abs(float(x["circulation_mod_2pi"]))
                          for x in plaquettes)
    return {
        "vertices": N_VERTICES,
        "torus_points": [list(phase_point(h, p)) for h in range(N_VERTICES)],
        "edges": len(edges),
        "lower_trigram_edges": sum(bit < 3 for _, _, bit in edges),
        "upper_trigram_edges": sum(bit >= 3 for _, _, bit in edges),
        "plaquettes": len(plaquettes),
        "complement_residuals_radians": complement_residuals(p),
        "complement_displacements_radians": complement_displacements(p),
        "plaquette_records": plaquettes,
        "max_u1_holonomy_error": max_holonomy_error,
        "max_circulation_mod_2pi": max_circulation,
        "pure_gauge_holonomy_pass": max_holonomy_error <= tolerance,
        "interpretation": (
            "Endpoint phases define a pure-gauge connection. Nonzero integer "
            "branch winding is not, by itself, a disclination. Physical Frank "
            "or Burgers data require independent frame transport or spatial "
            "registration."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phases", type=Path, required=True,
                        help="JSON array of 8 measured trigram phases in radians")
    parser.add_argument("--output", type=Path,
                        help="optional path for the JSON audit report")
    args = parser.parse_args()
    result = audit(json.loads(args.phases.read_text(encoding="utf-8")))
    rendered = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
