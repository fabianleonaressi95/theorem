#!/usr/bin/env python3
"""Reproducible filamentary Biot–Savart audit for a toroidal 5x12 winding.

This is a PARAMETRIC IDEALIZATION, not a reconstruction certified against a
manufactured Rodin coil. A phase-shifted path is a distinct parallel curve on
the torus; merely replacing t by t+delta in the same closed path only
reparameterizes that path and must not be counted as a second conductor.
"""
from __future__ import annotations
import argparse
import json
from dataclasses import dataclass
from typing import Iterable
import numpy as np

MU0 = 4.0e-7 * np.pi

@dataclass(frozen=True)
class Winding:
    major_radius_m: float = 0.03525
    minor_radius_m: float = 0.0145
    toroidal_turns: int = 5
    poloidal_turns: int = 12
    phase_rad: float = 0.0
    current_a: float = 1.6

def centreline(w: Winding, n_segments: int) -> tuple[np.ndarray, np.ndarray]:
    """Return midpoint samples r(t) and oriented dl for one closed filament."""
    if n_segments < 32:
        raise ValueError("n_segments must be >= 32")
    if w.major_radius_m <= w.minor_radius_m or w.minor_radius_m <= 0:
        raise ValueError("Require major_radius > minor_radius > 0")
    if w.toroidal_turns < 1 or w.poloidal_turns < 1:
        raise ValueError("Turn counts must be positive integers")
    t = (np.arange(n_segments, dtype=float) + 0.5) * (2.0 * np.pi / n_segments)
    p, q = w.toroidal_turns, w.poloidal_turns
    v, u = q * t + w.phase_rad, p * t
    cv, sv, cu, su = np.cos(v), np.sin(v), np.cos(u), np.sin(u)
    rho = w.major_radius_m + w.minor_radius_m * cv
    xyz = np.column_stack((rho * cu, rho * su, w.minor_radius_m * sv))
    drho = -q * w.minor_radius_m * sv
    deriv = np.column_stack((
        drho * cu - p * rho * su,
        drho * su + p * rho * cu,
        q * w.minor_radius_m * cv,
    ))
    return xyz, deriv * (2.0 * np.pi / n_segments)

def biot_savart(points_m: np.ndarray, windings: Iterable[Winding],
                n_segments: int = 20000, chunk_size: int = 2048) -> np.ndarray:
    """Evaluate B at points (metres); returns tesla, shape (n_points, 3)."""
    points = np.atleast_2d(np.asarray(points_m, dtype=float))
    if points.ndim != 2 or points.shape[1] != 3:
        raise ValueError("points_m must have shape (n_points, 3)")
    if chunk_size < 1:
        raise ValueError("chunk_size must be positive")
    total = np.zeros((len(points), 3), dtype=float)
    prefactor = MU0 / (4.0 * np.pi)
    for w in windings:
        src, dl = centreline(w, n_segments)
        for start in range(0, len(points), chunk_size):
            stop = min(start + chunk_size, len(points))
            rvec = points[start:stop, None, :] - src[None, :, :]
            rnorm = np.linalg.norm(rvec, axis=2)
            if np.any(rnorm < 1.0e-12):
                raise ValueError("Observation point lies on the ideal filament")
            cross = np.cross(dl[None, :, :], rvec)
            integral = np.sum(cross / rnorm[:, :, None] ** 3, axis=1)
            total[start:stop] += prefactor * w.current_a * integral
    return total

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--major-radius-mm", type=float, default=35.25)
    p.add_argument("--minor-radius-mm", type=float, default=14.5)
    p.add_argument("--current-a", type=float, default=1.6)
    p.add_argument("--segments", type=int, default=20000)
    p.add_argument("--pair-phase-deg", type=float, default=None,
                   help="add a distinct path at this poloidal phase, with opposite current")
    return p.parse_args()

def main() -> None:
    args = parse_args()
    base = Winding(major_radius_m=args.major_radius_mm * 1e-3,
                   minor_radius_m=args.minor_radius_mm * 1e-3,
                   current_a=args.current_a)
    windings = [base]
    if args.pair_phase_deg is not None:
        windings.append(Winding(
            major_radius_m=base.major_radius_m,
            minor_radius_m=base.minor_radius_m,
            toroidal_turns=base.toroidal_turns,
            poloidal_turns=base.poloidal_turns,
            phase_rad=np.deg2rad(args.pair_phase_deg),
            current_a=-args.current_a,
        ))
    points = np.array([[0., 0., 0.], [0., 0., .010], [.010, 0., 0.],
                       [0., .010, 0.], [.020, 0., 0.]])
    field_t = biot_savart(points, windings, n_segments=args.segments)
    print(json.dumps({
        "model": "ideal torus-knot filament; not a validated coil reconstruction",
        "major_radius_mm": args.major_radius_mm,
        "minor_radius_mm": args.minor_radius_mm,
        "toroidal_turns": base.toroidal_turns,
        "poloidal_turns": base.poloidal_turns,
        "currents_a": [w.current_a for w in windings],
        "phases_deg": [float(np.rad2deg(w.phase_rad)) for w in windings],
        "segments_per_path": args.segments,
        "points_mm": (points * 1000.).tolist(),
        "B_mT": (field_t * 1000.).tolist(),
        "B_norm_mT": (np.linalg.norm(field_t, axis=1) * 1000.).tolist(),
    }, indent=2))

if __name__ == "__main__":
    main()
