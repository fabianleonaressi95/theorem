"""Faraday coupling for a circular coil rigidly mounted on one Jitterbug panel.

The panel pose is reconstructed frame-by-frame from its three labelled vertices
using a proper Kabsch fit. The coil is a rigid circle in the panel plane, centred
at the panel centroid. Its radius is constrained to lie inside the equilateral
panel's inradius. The Jitterbug path parameter is pseudo-arclength; a constant
physical arclength speed converts it to time. This is an explicit conditional
electromechanical model, not a claim that Gray's paper contains a coil.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from audits.jitterbug_gray_kinematics import (
    cuboctahedron, rigid_triangles, tetrahedral_group, orbit_data,
    jitterbug_path, configs,
)


def skew(v: np.ndarray) -> np.ndarray:
    x, y, z = v
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def exp_so3(rotvec: np.ndarray) -> np.ndarray:
    angle = float(np.linalg.norm(rotvec))
    K = skew(rotvec)
    if angle < 1e-10:
        return np.eye(3) + K + 0.5 * (K @ K)
    return np.eye(3) + (np.sin(angle) / angle) * K + (
        (1.0 - np.cos(angle)) / angle**2
    ) * (K @ K)


def log_so3(R: np.ndarray) -> np.ndarray:
    """Principal SO(3) logarithm for adjacent, small path increments."""
    cos_angle = float(np.clip((np.trace(R) - 1.0) / 2.0, -1.0, 1.0))
    angle = float(np.arccos(cos_angle))
    vee = np.array([R[2, 1] - R[1, 2],
                    R[0, 2] - R[2, 0],
                    R[1, 0] - R[0, 1]])
    if angle < 1e-8:
        return 0.5 * vee
    if np.pi - angle < 1e-6:
        vals, vecs = np.linalg.eigh((R + np.eye(3)) / 2.0)
        axis = vecs[:, int(np.argmax(vals))]
        return angle * axis
    return (angle / (2.0 * np.sin(angle))) * vee


def fit_panel_rotation(reference: np.ndarray, current: np.ndarray) -> tuple[np.ndarray, float]:
    """Return proper column-vector rotation and max rigid-fit residual."""
    X = np.asarray(reference, dtype=float)
    Y = np.asarray(current, dtype=float)
    if X.shape != (3, 3) or Y.shape != (3, 3):
        raise ValueError("reference and current panel vertices must have shape (3,3)")
    Xc = X - X.mean(axis=0)
    Yc = Y - Y.mean(axis=0)
    U, _, Vt = np.linalg.svd(Xc.T @ Yc)
    R_row = U @ Vt
    if np.linalg.det(R_row) < 0:
        U[:, -1] *= -1
        R_row = U @ Vt
    R = R_row.T
    fitted = (R @ Xc.T).T
    residual = float(np.max(np.linalg.norm(fitted - Yc, axis=1)))
    return R, residual


def panel_normal(reference: np.ndarray) -> np.ndarray:
    e1 = reference[1] - reference[0]
    e2 = reference[2] - reference[0]
    n = np.cross(e1, e2)
    return n / np.linalg.norm(n)


def coil_radius_limit(edge_length: float) -> float:
    """Inradius of an equilateral triangular panel."""
    if edge_length <= 0:
        raise ValueError("edge_length must be positive")
    return edge_length / (2.0 * np.sqrt(3.0))


def emf_from_rotations(rotations: np.ndarray, times: np.ndarray,
                       B_tesla: np.ndarray, turns: int, area_m2: float,
                       normal0: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return midpoint emf, midpoint times and flux linkage at frame times.

    Spatial angular velocity is log(R[k+1] R[k]^T)/dt. For a uniform static
    field, lambda=N*A*B.n and emf=-N*A*B.(omega x n).
    """
    Rseq = np.asarray(rotations, dtype=float)
    t = np.asarray(times, dtype=float)
    B = np.asarray(B_tesla, dtype=float)
    n0 = np.asarray(normal0, dtype=float)
    if len(Rseq) != len(t) or len(t) < 2:
        raise ValueError("need at least two rotations and matching times")
    if np.any(np.diff(t) <= 0):
        raise ValueError("times must be strictly increasing")
    if B.shape != (3,) or n0.shape != (3,):
        raise ValueError("B_tesla and normal0 must be 3-vectors")
    n0 = n0 / np.linalg.norm(n0)
    normals = np.einsum("nij,j->ni", Rseq, n0)
    flux_linkage = turns * area_m2 * (normals @ B)
    emf = np.empty(len(t) - 1)
    tm = 0.5 * (t[:-1] + t[1:])
    for k, dt in enumerate(np.diff(t)):
        rotvec = log_so3(Rseq[k + 1] @ Rseq[k].T)
        omega = rotvec / dt
        Rmid = exp_so3(0.5 * rotvec) @ Rseq[k]
        nmid = Rmid @ n0
        emf[k] = -turns * area_m2 * np.dot(B, np.cross(omega, nmid))
    return emf, tm, flux_linkage


def solve_series_rl_on_grid(emf: np.ndarray, frame_times: np.ndarray,
                            resistance_ohm: float, inductance_h: float,
                            initial_current_a: float = 0.0) -> np.ndarray:
    """Exact RL response for constant emf on each frame interval."""
    if resistance_ohm < 0 or inductance_h < 0:
        raise ValueError("R and L must be nonnegative")
    dt = np.diff(frame_times)
    if len(emf) != len(dt) or np.any(dt <= 0):
        raise ValueError("emf must have one value per positive frame interval")
    current = np.empty(len(emf) + 1)
    current[0] = initial_current_a
    for k, (e, h) in enumerate(zip(emf, dt)):
        if inductance_h == 0:
            if resistance_ohm == 0:
                raise ValueError("R=L=0 is an undefined ideal circuit")
            current[k + 1] = e / resistance_ohm
        elif resistance_ohm == 0:
            current[k + 1] = current[k] + e * h / inductance_h
        else:
            decay = np.exp(-resistance_ohm * h / inductance_h)
            current[k + 1] = (current[k] * decay
                              + (e / resistance_ohm) * (1.0 - decay))
    return current


def build_default_run(edge_length_m: float = 0.1,
                      arclength_speed_m_s: float = 0.01,
                      turns: int = 100,
                      coil_radius_m: float | None = None,
                      B_tesla=(0.0, 0.0, 0.1),
                      resistance_ohm: float = 10.0,
                      inductance_h: float = 0.01,
                      ds: float = 0.01) -> dict:
    """Generate the standard T-symmetric Jitterbug path and one attached coil."""
    if edge_length_m <= 0 or arclength_speed_m_s <= 0 or turns <= 0:
        raise ValueError("length, speed and turn count must be positive")
    V0 = cuboctahedron()
    T = tetrahedral_group()
    A, Qs = orbit_data(V0, T)
    path = jitterbug_path(V0, A, Qs, ds=ds)
    Wcfg = configs(path, A) * edge_length_m

    face_indices = rigid_triangles(V0)[(1, 1, 1)]
    reference = Wcfg[0, face_indices]
    inradius = coil_radius_limit(edge_length_m)
    radius = 0.8 * inradius if coil_radius_m is None else float(coil_radius_m)
    if not (0.0 < radius < inradius):
        raise ValueError(f"coil radius must be below panel inradius {inradius:.9g} m")
    area = np.pi * radius**2
    n0 = panel_normal(reference)

    rotations, fit_residuals = [], []
    for frame in Wcfg:
        R, residual = fit_panel_rotation(reference, frame[face_indices])
        rotations.append(R)
        fit_residuals.append(residual)
    rotations = np.asarray(rotations)

    # Pseudo-arclength is converted to physical time by a declared constant
    # traversal speed; no intrinsic clock is asserted by this model.
    ds_path = np.linalg.norm(np.diff(path, axis=0), axis=1) * edge_length_m
    frame_times = np.concatenate([[0.0], np.cumsum(ds_path / arclength_speed_m_s)])
    B = np.asarray(B_tesla, dtype=float)
    emf, midpoint_times, flux = emf_from_rotations(
        rotations, frame_times, B, turns, area, n0
    )
    current = solve_series_rl_on_grid(
        emf, frame_times, resistance_ohm, inductance_h
    )
    return {
        "model": "one circular coil rigidly mounted in the plane of Jitterbug face (1,1,1)",
        "face_vertex_indices": [int(i) for i in face_indices],
        "edge_length_m": edge_length_m,
        "coil_radius_m": radius,
        "panel_inradius_m": inradius,
        "turns": turns,
        "area_m2": area,
        "B_tesla": B.tolist(),
        "arclength_speed_m_s": arclength_speed_m_s,
        "resistance_ohm": resistance_ohm,
        "inductance_h": inductance_h,
        "frames": len(Wcfg),
        "duration_s": float(frame_times[-1]),
        "max_panel_rigidity_fit_residual_m": float(max(fit_residuals)),
        "flux_linkage_min_Wb_turn": float(flux.min()),
        "flux_linkage_max_Wb_turn": float(flux.max()),
        "max_abs_emf_V": float(np.max(np.abs(emf))),
        "max_abs_current_A": float(np.max(np.abs(current))),
        "time_s": frame_times.tolist(),
        "emf_midpoint_V": emf.tolist(),
        "current_A": current.tolist(),
        "flux_linkage_Wb_turn": flux.tolist(),
        "midpoint_time_s": midpoint_times.tolist(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edge-length-m", type=float, default=0.1)
    parser.add_argument("--speed-m-s", type=float, default=0.01)
    parser.add_argument("--turns", type=int, default=100)
    parser.add_argument("--coil-radius-m", type=float, default=None)
    parser.add_argument("--B-tesla", type=float, nargs=3, default=(0.0, 0.0, 0.1))
    parser.add_argument("--R-ohm", type=float, default=10.0)
    parser.add_argument("--L-h", type=float, default=0.01)
    parser.add_argument("--ds", type=float, default=0.01)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    report = build_default_run(
        edge_length_m=args.edge_length_m,
        arclength_speed_m_s=args.speed_m_s,
        turns=args.turns,
        coil_radius_m=args.coil_radius_m,
        B_tesla=args.B_tesla,
        resistance_ohm=args.R_ohm,
        inductance_h=args.L_h,
        ds=args.ds,
    )
    rendered = json.dumps(report, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
