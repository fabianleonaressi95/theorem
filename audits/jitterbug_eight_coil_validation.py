"""Independent numerical validation for the eight-coil Jitterbug model.

Checks polygonal Neumann quadrature against the exact coaxial-loop formula,
then drives an eight-loop test fixture through a prescribed angular motion in
a static uniform field. The driven fixture is a controlled excitation test,
not a claim that the present Jitterbug kinematics already produce this motion.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import argparse
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from audits.jitterbug_eight_coil_coupling import (
    MU0, coil_polygon, neumann_mutual, inductance_matrix,
    midpoint_coupled_rl,
)


def elliptic_ke_agm(m: float) -> tuple[float, float]:
    """Complete elliptic integrals K(m), E(m), using the AGM."""
    if not 0.0 <= m < 1.0:
        raise ValueError("elliptic parameter m must be in [0, 1)")
    a, b = 1.0, math.sqrt(1.0 - m)
    summation, factor = 0.5 * m, 1.0
    for _ in range(64):
        c = 0.5 * (a - b)
        if abs(c) < 2e-16:
            break
        summation += factor * c * c
        a, b = 0.5 * (a + b), math.sqrt(a * b)
        factor *= 2.0
    K = math.pi / (2.0 * a)
    E = K * (1.0 - summation)
    return K, E


def coaxial_mutual_exact(a: float, b: float, separation: float,
                         turns_a: int = 1, turns_b: int = 1) -> float:
    """Exact mutual inductance of two separated coaxial circular filaments."""
    if min(a, b, separation) <= 0:
        raise ValueError("radii and separation must be positive")
    m = 4.0 * a * b / ((a + b) ** 2 + separation**2)
    k = math.sqrt(m)
    K, E = elliptic_ke_agm(m)
    return float(MU0 * turns_a * turns_b * math.sqrt(a * b)
                 * ((2.0 / k - k) * K - (2.0 / k) * E))


def coaxial_polygon_loop(radius: float, z: float, segments: int):
    angles = 2.0 * np.pi * np.arange(segments) / segments
    vertices = np.column_stack((radius * np.cos(angles),
                                radius * np.sin(angles),
                                np.full(segments, z)))
    return vertices, np.roll(vertices, -1, axis=0) - vertices


def convergence_audit(segment_counts=(48, 96, 192, 384),
                      softening_m=1e-7):
    a, b, z = 0.03, 0.025, 0.04
    exact = coaxial_mutual_exact(a, b, z, 100, 80)
    rows = []
    for n in segment_counts:
        la = coaxial_polygon_loop(a, 0.0, n)
        lb = coaxial_polygon_loop(b, z, n)
        value = neumann_mutual(la, lb, 100, 80, softening_m)
        rows.append({"segments": n, "mutual_H": value,
                     "relative_error": abs(value - exact) / abs(exact)})
    soft_rows = []
    for delta in (1e-7, 1e-5, 1e-4, 1e-3):
        la = coaxial_polygon_loop(a, 0.0, 192)
        lb = coaxial_polygon_loop(b, z, 192)
        value = neumann_mutual(la, lb, 100, 80, delta)
        soft_rows.append({"softening_m": delta, "mutual_H": value,
                          "relative_error": abs(value - exact) / abs(exact)})
    return {"reference": "exact coaxial circular-filament formula (complete elliptic K,E)",
            "radii_m": [a, b], "separation_m": z,
            "turns": [100, 80], "exact_mutual_H": exact,
            "segment_convergence": rows, "softening_sensitivity": soft_rows}


def rotation_y(angle: float) -> np.ndarray:
    c, s = math.cos(angle), math.sin(angle)
    return np.array([[c, 0.0, s], [0.0, 1.0, 0.0], [-s, 0.0, c]])


def driven_eight_coil_probe(frames=41, segments=48, B_tesla=0.1,
                            angular_frequency=2.0 * math.pi):
    """Eight separated coils with prescribed angular motion in static Bz."""
    if frames < 3 or segments < 16:
        raise ValueError("frames >= 3 and segments >= 16 required")
    ncoil, turns, radius, wire = 8, 100, 0.02, 1e-4
    resistance = np.eye(ncoil) * 10.0
    times = np.linspace(0.0, 1.0, frames)
    phase = np.arange(ncoil) * (math.pi / 16.0)
    centers = np.column_stack((np.arange(ncoil) * 0.055, np.zeros(ncoil),
                               np.zeros(ncoil)))
    area = math.pi * radius**2
    flux = np.empty((frames, ncoil))
    Lseq = np.empty((frames, ncoil, ncoil))
    for k, t in enumerate(times):
        loops = []
        for j in range(ncoil):
            angle = (math.pi / 3.0) * (0.5 - 0.5 * math.cos(
                angular_frequency * t + phase[j]))
            R = rotation_y(angle)
            loops.append(coil_polygon(centers[j], R, np.array([0., 0., 1.]),
                                      radius, segments))
            normal = R @ np.array([0., 0., 1.])
            flux[k, j] = turns * area * B_tesla * normal[2]
        Lseq[k] = inductance_matrix(
            loops, [turns] * ncoil, [radius] * ncoil, [wire] * ncoil, 1e-5)
    dt = np.diff(times)
    emf = -np.diff(flux, axis=0) / dt[:, None]
    currents = midpoint_coupled_rl(Lseq, emf, times, resistance)
    return {
        "fixture": "eight separated circular coils, prescribed panel-like rotations",
        "field": [0.0, 0.0, B_tesla],
        "motion": "angle_j(t)=(pi/3)*(1-cos(2*pi*t+phase_j))/2",
        "frames": frames, "segments_per_loop": segments,
        "max_abs_emf_V": float(np.max(np.abs(emf))),
        "max_abs_current_A": float(np.max(np.abs(currents))),
        "min_inductance_eigenvalue_H": float(min(
            np.linalg.eigvalsh(L).min() for L in Lseq)),
        "max_reciprocity_residual_H": float(np.max(
            np.abs(Lseq - np.swapaxes(Lseq, 1, 2)))),
        "times_s": times.tolist(), "emf_V": emf.tolist(),
        "currents_A": currents.tolist(),
    }


def run_validation():
    conv = convergence_audit()
    driven = driven_eight_coil_probe()
    return {
        "status": "numerical validation fixtures; driven probe is not measured hardware",
        "coaxial_benchmark": conv,
        "nonzero_flux_drive": driven,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    report = run_validation()
    rendered = json.dumps(report, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
