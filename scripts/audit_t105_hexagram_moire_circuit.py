#!/usr/bin/env python3
"""T105 audit: 64-site phase lift, Kirchhoff continuity, correlations, and response."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
from typing import Sequence

N, BITS = 64, 6
TAU = 2.0 * math.pi


def wrap(x: float) -> float:
    y = (float(x) + math.pi) % TAU - math.pi
    return math.pi if math.isclose(y, -math.pi, abs_tol=1e-14) else y


def edges() -> list[tuple[int, int, int]]:
    return [(h, h ^ (1 << bit), bit)
            for h in range(N) for bit in range(BITS)
            if not (h & (1 << bit))]


def hexagram_pair(h: int) -> tuple[int, int]:
    if not 0 <= h < N:
        raise ValueError("hexagram index must be in 0..63")
    return h & 7, (h >> 3) & 7


def phase_lift(plus: Sequence[float], minus: Sequence[float],
               offset: float = 0.0, orientation: int = 1) -> list[list[float]]:
    if len(plus) != 8 or len(minus) != 8:
        raise ValueError("exactly eight phases are required on each circle")
    if orientation not in (-1, 1):
        raise ValueError("orientation must be -1 or +1")
    if not all(math.isfinite(float(x)) for x in [*plus, *minus, offset]):
        raise ValueError("phases and offset must be finite")
    eps = [wrap(float(minus[t ^ 7]) - orientation * float(plus[t]) - offset)
            for t in range(8)]
    return [[eps[hexagram_pair(h)[0]], eps[hexagram_pair(h)[1]]]
            for h in range(N)]


def incidence_and_conductance(g: Sequence[float]):
    es = edges()
    if len(g) != len(es) or any(not math.isfinite(float(x)) or float(x) <= 0 for x in g):
        raise ValueError("provide 192 finite strictly positive edge conductances")
    B = [[0.0] * len(es) for _ in range(N)]
    for k, (tail, head, _) in enumerate(es):
        B[tail][k], B[head][k] = 1.0, -1.0
    return es, B


def branch_currents(V: Sequence[float], g: Sequence[float]) -> list[float]:
    if len(V) != N:
        raise ValueError("64 node potentials required")
    es, _ = incidence_and_conductance(g)
    return [float(g[k]) * (float(V[i]) - float(V[j]))
            for k, (i, j, _) in enumerate(es)]


def continuity_residual(dQ: Sequence[float], V: Sequence[float],
                        g: Sequence[float], source: Sequence[float]) -> list[float]:
    if len(dQ) != N or len(source) != N:
        raise ValueError("dQ and source must each contain 64 entries")
    es, _ = incidence_and_conductance(g)
    j = branch_currents(V, g)
    out = [float(dQ[h]) - float(source[h]) for h in range(N)]
    for k, (tail, head, _) in enumerate(es):
        out[tail] += j[k]
        out[head] -= j[k]
    return out


def charge_covariance(samples: Sequence[Sequence[float]]) -> list[list[float]]:
    if len(samples) < 2 or any(len(row) != N for row in samples):
        raise ValueError("charge samples must be at least 2 rows by exactly 64 columns")
    m = len(samples)
    means = [sum(float(row[h]) for row in samples) / m for h in range(N)]
    return [[sum((float(row[h])-means[h]) * (float(row[k])-means[k])
                 for row in samples) / (m-1)
             for k in range(N)] for h in range(N)]


def phase_charge_cross(samples: Sequence[Sequence[float]],
                       phase_pair: Sequence[Sequence[float]]) -> list[list[float]]:
    if len(samples) < 2 or any(len(row) != N for row in samples):
        raise ValueError("charge samples must be at least 2 by 64")
    if len(phase_pair) != N or any(len(row) != 2 for row in phase_pair):
        raise ValueError("phase lift must be 64 by 2")
    means = [sum(float(row[h]) for row in samples)/len(samples) for h in range(N)]
    return [[sum((float(row[h])-means[h]) *
                 math.sin(float(phase_pair[h][a]))
                 for row in samples)/(len(samples)-1)
             for a in range(2)] for h in range(N)]


def green_kubo_trapezoid(flux: Sequence[Sequence[float]], dt: float,
                         temperature: float, volume: float,
                         boltzmann: float = 1.0) -> list[list[float]]:
    if len(flux) < 2 or dt <= 0 or temperature <= 0 or volume <= 0:
        raise ValueError("need >=2 flux samples and positive dt, T, volume")
    dim = len(flux[0])
    if dim == 0 or any(len(row) != dim for row in flux):
        raise ValueError("flux must be a rectangular time-by-dimension array")
    m = len(flux)
    means = [sum(float(row[a]) for row in flux)/m for a in range(dim)]
    centered = [[float(row[a])-means[a] for a in range(dim)] for row in flux]
    # Biased finite-window estimator; integrates lagged covariance to the
    # final available lag. Reported as a finite-window estimate, not a limit.
    result = [[0.0]*dim for _ in range(dim)]
    for a in range(dim):
        for b in range(dim):
            vals = [sum(centered[t+lag][a]*centered[t][b]
                        for t in range(m-lag))/(m-lag)
                    for lag in range(m)]
            integ = dt * (0.5*vals[0] + sum(vals[1:-1]) + 0.5*vals[-1])
            result[a][b] = integ/(boltzmann*temperature*volume)
    return result


def audit() -> dict[str, object]:
    es = edges()
    assert len(es) == 192
    assert sum(bit < 3 for _, _, bit in es) == 96
    assert sum(bit >= 3 for _, _, bit in es) == 96
    assert len({hexagram_pair(h) for h in range(64)}) == 64
    phase = phase_lift([0.1*t for t in range(8)],
                       [0.2*t for t in range(8)], 0.03, 1)
    assert len(phase) == 64 and all(len(x) == 2 for x in phase)
    g = [1.0]*192
    V = [math.sin(h) for h in range(64)]
    j = branch_currents(V, g)
    # The sum of B j vanishes, so the source-free node derivative conserves total charge.
    residual = continuity_residual([-sum((1 if h == i else -1 if h == k else 0)*j[e]
                    for e,(i,k,_) in enumerate(es)) for h in range(64)],
                    V, g, [0.0]*64)
    assert max(abs(x) for x in residual) < 1e-10
    return {
        "vertices": 64, "edges": 192, "lower_edges": 96, "upper_edges": 96,
        "phase_lift_shape": [64, 2],
        "continuity_identity": "dot(Q) + B G B^T C^{-1} Q = s",
        "all_64_hexagrams_distinct": True,
        "physical_charge_law": "not inferred; requires 64 calibrated measurements or a derived constitutive model",
        "moire_embedding": "required; not inferred from Q6 adjacency",
        "green_kubo": "finite-window estimator only; compare independently with linear response",
        "status": "PASS"
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--plus", type=Path, help="JSON array of 8 measured phases")
    p.add_argument("--minus", type=Path, help="JSON array of 8 measured phases")
    p.add_argument("--offset", type=float, default=0.0)
    p.add_argument("--orientation", type=int, choices=(-1, 1), default=1)
    p.add_argument("--charges", type=Path, help="JSON array: time samples x 64 node charges")
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    if bool(a.plus) != bool(a.minus):
        p.error("--plus and --minus must be supplied together")
    result = audit()
    if a.plus:
        lift = phase_lift(json.loads(a.plus.read_text()), json.loads(a.minus.read_text()),
                          a.offset, a.orientation)
        result["phase_lift"] = lift
    if a.charges:
        samples = json.loads(a.charges.read_text())
        result["charge_covariance_64x64"] = charge_covariance(samples)
        if a.plus:
            result["phase_charge_cross_sine_moment_64x2"] = phase_charge_cross(
                samples, result["phase_lift"])
    rendered = json.dumps(result, indent=2)
    if a.output:
        a.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
