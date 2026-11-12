#!/usr/bin/env python3
"""Manufactured-order-parameter audit: plaquette phase winding vs a GP zero.

This is a topological/refinement benchmark, not a time-dependent GP solver.
"""
from __future__ import annotations
import argparse, json, math
from dataclasses import asdict, dataclass
import numpy as np

@dataclass
class Result:
    cells_per_axis: int
    plaquette_charge: int
    detected_cells: int
    max_abs_charge: int
    zero_x: float
    zero_y: float
    detected_cell_center_x: float
    detected_cell_center_y: float
    localization_error: float
    grid_spacing: float

def wrap(angle):
    return np.arctan2(np.sin(angle), np.cos(angle))

def audit_one(n, zero=(0.137, -0.219)):
    if n < 4:
        raise ValueError("n must be >= 4")
    x0, y0 = zero
    axis = np.linspace(-1.0, 1.0, n + 1)
    x, y = np.meshgrid(axis, axis, indexing="ij")
    r2 = (x-x0)**2 + (y-y0)**2
    Psi_GP = ((x-x0) + 1j*(y-y0)) * np.exp(-2.0*r2)
    phase = np.angle(psi)
    # Counter-clockwise plaquette boundary.
    circulation = (
        wrap(phase[1:, :-1] - phase[:-1, :-1])
        + wrap(phase[1:, 1:] - phase[1:, :-1])
        + wrap(phase[:-1, 1:] - phase[1:, 1:])
        + wrap(phase[:-1, :-1] - phase[:-1, 1:])
    )
    q = np.rint(circulation/(2*np.pi)).astype(int)
    hits = np.argwhere(q != 0)
    if len(hits) != 1:
        raise AssertionError(f"expected one charged plaquette, found {len(hits)}")
    i, j = map(int, hits[0])
    cx, cy = float((axis[i]+axis[i+1])/2), float((axis[j]+axis[j+1])/2)
    h = 2.0/n
    return Result(n, int(q[i,j]), int(len(hits)), int(np.max(np.abs(q))),
                  float(x0), float(y0), cx, cy,
                  float(math.hypot(cx-x0, cy-y0)), float(h))


def audit_extruded_3d(n_xy=32, n_z=8, zero=(0.137, -0.219)):
    """Straight GP zero line, periodic in z; returns T110 dual-link flux checks."""
    if n_z < 2:
        raise ValueError("n_z must be >= 2")
    x0, y0 = zero
    axis = np.linspace(-1.0, 1.0, n_xy + 1)
    x, y = np.meshgrid(axis, axis, indexing="ij")
    r2 = (x-x0)**2 + (y-y0)**2
    # z-independent complex field: its zero is a straight line parallel to z.
    Psi_GP = ((x-x0) + 1j*(y-y0)) * np.exp(-2.0*r2)
    phase = np.angle(psi)
    circulation = (
        wrap(phase[1:, :-1] - phase[:-1, :-1])
        + wrap(phase[1:, 1:] - phase[1:, :-1])
        + wrap(phase[:-1, 1:] - phase[1:, 1:])
        + wrap(phase[:-1, :-1] - phase[:-1, 1:])
    )
    q_xy = np.rint(circulation/(2*np.pi)).astype(int)
    qx = np.zeros((n_xy, n_xy, n_z), dtype=int)  # q_23
    qy = np.zeros((n_xy, n_xy, n_z), dtype=int)  # q_31
    qz = np.repeat(q_xy[:, :, None], n_z, axis=2)  # q_12: dual z-links
    # Discrete dual divergence; z is periodic and qz is z-independent.
    divergence = (
        qx - np.roll(qx, 1, axis=0)
        + qy - np.roll(qy, 1, axis=1)
        + qz - np.roll(qz, 1, axis=2)
    )
    hits = np.argwhere(q_xy != 0)
    return {
        "xy_cells_per_axis": int(n_xy),
        "periodic_z_links": int(n_z),
        "charged_xy_plaquettes": int(len(hits)),
        "plaquette_charge": int(q_xy[tuple(hits[0])]) if len(hits) else 0,
        "dual_z_flux_links": int(np.sum(np.abs(qz))),
        "max_abs_dual_divergence": int(np.max(np.abs(divergence))),
        "interpretation": "one straight unit-flux vortex line winding once around periodic z"
    }

def run(sizes):
    rows = [asdict(audit_one(n)) for n in sizes]
    errors = [r["localization_error"] for r in rows]
    hs = [r["grid_spacing"] for r in rows]
    rates = [math.log(errors[k-1]/errors[k], hs[k-1]/hs[k])
             if errors[k] > 0 and errors[k-1] > 0 else None
             for k in range(1, len(rows))]
    return {
        "status": "manufactured static topological benchmark; not a GP time integrator",
        "sizes": rows,
        "extruded_3d_line": audit_extruded_3d(),
        "observed_localization_orders": rates,
        "acceptance": {
            "one_unit_positive_plaquette_per_grid": all(
                r["plaquette_charge"] == 1 and r["detected_cells"] == 1
                and r["max_abs_charge"] == 1 for r in rows),
            "localization_error_bounded_by_sqrt2_h_over_2": all(
                r["localization_error"] <= math.sqrt(2)*r["grid_spacing"]/2 + 1e-12
                for r in rows),
            "3d_dual_flux_is_closed": audit_extruded_3d()["max_abs_dual_divergence"] == 0
                and audit_extruded_3d()["plaquette_charge"] == 1
        }
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="+", type=int, default=[8,16,32,64,128])
    args = parser.parse_args()
    print(json.dumps(run(args.sizes), indent=2))

if __name__ == "__main__":
    main()
