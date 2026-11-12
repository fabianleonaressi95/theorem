#!/usr/bin/env python3
"""Audit opposite-circle trigram mismatch and Q6 phase-winding indices."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
from typing import Sequence

N_TRIGRAMS, N_VERTICES = 8, 64
TAU = 2.0 * math.pi


def wrap(angle: float) -> float:
    """Principal representative in (-pi, pi]."""
    value = (float(angle) + math.pi) % TAU - math.pi
    return math.pi if math.isclose(value, -math.pi, abs_tol=1e-14) else value


def validate(phases: Sequence[float]) -> list[float]:
    if len(phases) != N_TRIGRAMS:
        raise ValueError("exactly eight trigram phases (radians) are required per circle")
    values = [float(x) for x in phases]
    if not all(math.isfinite(x) for x in values):
        raise ValueError("all phases must be finite")
    return values


def phase_point(h: int, phases: Sequence[float]) -> tuple[float, float]:
    if not 0 <= h < N_VERTICES:
        raise ValueError("hexagram label must lie in {0,...,63}")
    return phases[h & 7] % TAU, phases[(h >> 3) & 7] % TAU


def complement_residuals(plus: Sequence[float], minus: Sequence[float],
                         offset: float = 0.0, orientation: int = 1) -> list[float]:
    p, m = validate(plus), validate(minus)
    if orientation not in (-1, 1):
        raise ValueError("orientation must be +1 or -1")
    return [wrap(m[t ^ 7] - orientation * p[t] - offset) for t in range(8)]


def hexagram_complement_mismatches(plus: Sequence[float], minus: Sequence[float],
                                   offset: float = 0.0,
                                   orientation: int = 1) -> list[list[float]]:
    eps = complement_residuals(plus, minus, offset, orientation)
    return [[eps[h & 7], eps[(h >> 3) & 7]] for h in range(N_VERTICES)]


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


def edge_increment(h: int, hp: int, bit: int,
                   phases: Sequence[float]) -> float:
    lo, up = h & 7, (h >> 3) & 7
    lop, upp = hp & 7, (hp >> 3) & 7
    return wrap(phases[lop] - phases[lo]) if bit < 3 else wrap(phases[upp] - phases[up])


def layer_plaquette_audit(phases: Sequence[float]) -> list[dict[str, float | int]]:
    """Wilson audit of endpoint phases; all plaquette products are pure gauge."""
    p = validate(phases)
    records = []
    for h, hi, hij, hj, i, j in enumerate_plaquettes():
        increments = (edge_increment(h, hi, i, p),
                      edge_increment(hi, hij, j, p),
                      edge_increment(hij, hj, i, p),
                      edge_increment(hj, h, j, p))
        raw = sum(increments)
        records.append({
            "base_vertex": h, "directions": [i, j],
            "raw_phase_sum": raw, "branch_winding": int(round(raw / TAU)),
            "holonomy_real": math.cos(raw), "holonomy_imag": math.sin(raw),
            "circulation_mod_2pi": wrap(raw),
        })
    return records


def mismatch_plaquette_audit(plus: Sequence[float], minus: Sequence[float],
                             offset: float = 0.0,
                             orientation: int = 1) -> list[dict[str, int | float]]:
    """Winding of the cross-circle complement-mismatch field on all Q6 squares."""
    eps = complement_residuals(plus, minus, offset, orientation)
    records = []
    for h, hi, hij, hj, i, j in enumerate_plaquettes():
        increments = (edge_increment(h, hi, i, eps),
                      edge_increment(hi, hij, j, eps),
                      edge_increment(hij, hj, i, eps),
                      edge_increment(hj, h, j, eps))
        raw = sum(increments)
        winding = int(round(raw / TAU))
        records.append({
            "base_vertex": h, "directions": [i, j],
            "raw_phase_sum": raw, "winding_number": winding,
            "quantization_residual": raw - TAU * winding,
            "candidate_phase_vortex": winding != 0,
        })
    return records


def audit(plus: Sequence[float], minus: Sequence[float],
          offset: float = 0.0, orientation: int = 1,
          tolerance: float = 1e-10) -> dict[str, object]:
    p, m = validate(plus), validate(minus)
    edges = enumerate_edges()
    plus_faces, minus_faces = layer_plaquette_audit(p), layer_plaquette_audit(m)
    mismatch_faces = mismatch_plaquette_audit(p, m, offset, orientation)

    def layer_summary(faces: list[dict[str, float | int]]) -> dict[str, object]:
        error = max(math.hypot(float(x["holonomy_real"]) - 1.0,
                               float(x["holonomy_imag"])) for x in faces)
        circulation = max(abs(float(x["circulation_mod_2pi"])) for x in faces)
        return {"plaquettes": len(faces), "records": faces,
                "max_u1_holonomy_error": error,
                "max_circulation_mod_2pi": circulation,
                "pure_gauge_holonomy_pass": error <= tolerance}

    return {
        "vertices_per_layer": N_VERTICES,
        "plus_torus_points": [list(phase_point(h, p)) for h in range(N_VERTICES)],
        "minus_torus_points": [list(phase_point(h, m)) for h in range(N_VERTICES)],
        "edges_per_layer": len(edges),
        "lower_trigram_edges_per_layer": sum(bit < 3 for _, _, bit in edges),
        "upper_trigram_edges_per_layer": sum(bit >= 3 for _, _, bit in edges),
        "complement_frame_registration": {"offset_radians": offset,
                                          "orientation": orientation},
        "trigram_complement_residuals": complement_residuals(p, m, offset, orientation),
        "hexagram_complement_mismatches": hexagram_complement_mismatches(
            p, m, offset, orientation),
        "plus_layer": layer_summary(plus_faces),
        "minus_layer": layer_summary(minus_faces),
        "complement_mismatch_plaquettes": mismatch_faces,
        "candidate_phase_vortex_count": sum(
            int(bool(x["candidate_phase_vortex"])) for x in mismatch_faces),
        "interpretation": (
            "Cross-circle mismatch winding is a candidate phase-vortex index. "
            "It becomes a Frank/disclination or Burgers/dislocation observable "
            "only after the phase is calibrated as an orientation or translational "
            "density-wave phase. Endpoint Wilson holonomy within either layer "
            "remains pure gauge."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plus", type=Path, required=True,
                        help="JSON array of 8 measured phases on C+ (radians)")
    parser.add_argument("--minus", type=Path, required=True,
                        help="JSON array of 8 measured phases on C- (radians)")
    parser.add_argument("--frame-offset", type=float, default=0.0,
                        help="calibrated relative angular-frame offset chi (radians)")
    parser.add_argument("--orientation", type=int, choices=(-1, 1), default=1,
                        help="relative angular orientation sigma of the circle frames")
    parser.add_argument("--output", type=Path, help="optional JSON report path")
    args = parser.parse_args()
    result = audit(json.loads(args.plus.read_text(encoding="utf-8")),
                   json.loads(args.minus.read_text(encoding="utf-8")),
                   args.frame_offset, args.orientation)
    rendered = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
