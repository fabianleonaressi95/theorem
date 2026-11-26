"""Eight-coil Jitterbug coupling model.

Conditional engineering model built on the existing Gray/Jitterbug rigid-panel
kinematics.  Each of the eight triangular panels carries a circular multi-turn
coil. Mutual inductances use a regularized polygonal Neumann integral; self
inductances use the thin-wire circular-loop approximation. These are explicit
approximations, not measured apparatus data.
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
from audits.jitterbug_coil_coupling import (
    fit_panel_rotation, panel_normal, coil_radius_limit,
)

MU0 = 4.0e-7 * np.pi


def coil_polygon(center, rotation, normal0, radius, segments=96):
    """Return vertices and oriented segment vectors for a panel-local circle."""
    if segments < 16 or radius <= 0:
        raise ValueError("segments >= 16 and positive radius required")
    n0 = np.asarray(normal0, float)
    n0 /= np.linalg.norm(n0)
    trial = np.array([1.0, 0.0, 0.0])
    if abs(np.dot(trial, n0)) > 0.9:
        trial = np.array([0.0, 1.0, 0.0])
    u0 = np.cross(n0, trial)
    u0 /= np.linalg.norm(u0)
    v0 = np.cross(n0, u0)
    angles = 2 * np.pi * np.arange(segments) / segments
    local = radius * (np.cos(angles)[:, None] * u0 + np.sin(angles)[:, None] * v0)
    vertices = np.asarray(center) + (np.asarray(rotation) @ local.T).T
    return vertices, np.roll(vertices, -1, axis=0) - vertices


def neumann_mutual(loop_i, loop_j, turns_i, turns_j, softening_m):
    """Regularized polygonal Neumann integral for two distinct filament loops."""
    ri, dli = loop_i
    rj, dlj = loop_j
    delta = ri[:, None, :] - rj[None, :, :]
    distance = np.sqrt(np.sum(delta * delta, axis=2) + softening_m**2)
    dots = dli @ dlj.T
    return float(MU0 * turns_i * turns_j / (4*np.pi)
                 * np.sum(dots / distance))


def self_inductance_circular(turns, radius_m, wire_radius_m):
    """Thin-wire circular-loop approximation; requires wire radius << loop radius."""
    if not (0 < wire_radius_m < radius_m * 0.1):
        raise ValueError("wire radius must be positive and < 0.1 * loop radius")
    return float(MU0 * turns**2 * radius_m
                 * (np.log(8.0 * radius_m / wire_radius_m) - 2.0))


def panel_frames(Wcfg, V0, face_indices):
    reference = Wcfg[0, face_indices]
    rotations, centers, residuals = [], [], []
    n0 = panel_normal(reference)
    for frame in Wcfg:
        tri = frame[face_indices]
        R, residual = fit_panel_rotation(reference, tri)
        rotations.append(R)
        centers.append(tri.mean(axis=0))
        residuals.append(residual)
    return np.asarray(rotations), np.asarray(centers), n0, np.asarray(residuals)


def inductance_matrix(loops, turns, radii, wire_radius, softening):
    n = len(loops)
    L = np.zeros((n, n), dtype=float)
    for i in range(n):
        L[i, i] = self_inductance_circular(turns[i], radii[i], wire_radius[i])
        for j in range(i):
            m = neumann_mutual(loops[i], loops[j], turns[i], turns[j], softening)
            L[i, j] = L[j, i] = m
    return L


def midpoint_coupled_rl(Lseq, emf_ext, times, resistance):
    """Implicit-midpoint solution of d(Li)/dt + R i = emf_ext."""
    Lseq = np.asarray(Lseq, float)
    e = np.asarray(emf_ext, float)
    t = np.asarray(times, float)
    R = np.asarray(resistance, float)
    nframe, ncoil, _ = Lseq.shape
    if e.shape != (nframe - 1, ncoil) or R.shape != (ncoil, ncoil):
        raise ValueError("incompatible L, emf or resistance dimensions")
    if np.any(np.diff(t) <= 0):
        raise ValueError("times must increase")
    currents = np.zeros((nframe, ncoil))
    for k, dt in enumerate(np.diff(t)):
        L0, L1 = Lseq[k], Lseq[k + 1]
        Lmid = 0.5 * (L0 + L1)
        dL = (L1 - L0) / dt
        lhs = Lmid / dt + 0.5 * dL + 0.5 * R
        rhs = (Lmid / dt - 0.5 * dL - 0.5 * R) @ currents[k] + e[k]
        currents[k + 1] = np.linalg.solve(lhs, rhs)
    return currents


def build_run(edge_length_m=0.1, speed_m_s=0.01, turns=100,
              radius_fraction=0.65, wire_radius_m=1e-4,
              B_tesla=(0.0, 0.0, 0.1), resistance_ohm=10.0,
              segments=96, ds=0.02, softening_m=2e-4):
    if edge_length_m <= 0 or speed_m_s <= 0 or turns <= 0:
        raise ValueError("edge length, speed and turns must be positive")
    V0 = cuboctahedron()
    T = tetrahedral_group()
    A, Qs = orbit_data(V0, T)
    path = jitterbug_path(V0, A, Qs, ds=ds)
    Wcfg = configs(path, A) * edge_length_m
    tris = rigid_triangles(V0)
    labels = list(tris.keys())
    inradius = coil_radius_limit(edge_length_m)
    radius = radius_fraction * inradius
    if not 0 < radius < inradius:
        raise ValueError("radius_fraction must lie in (0,1)")
    rotations, centers, n0s, residuals = [], [], [], []
    for label in labels:
        R, c, n0, res = panel_frames(Wcfg, V0, tris[label])
        rotations.append(R)
        centers.append(c)
        n0s.append(n0)
        residuals.append(res)
    rotations = np.stack(rotations, axis=1)
    centers = np.stack(centers, axis=1)
    residuals = np.stack(residuals, axis=1)
    frame_times = np.concatenate([[0.0], np.cumsum(
        np.linalg.norm(np.diff(path, axis=0), axis=1) * edge_length_m / speed_m_s
    )])
    B = np.asarray(B_tesla, float)
    N = np.full(8, int(turns), dtype=int)
    radii = np.full(8, radius)
    wire = np.full(8, wire_radius_m)
    area = np.pi * radius**2
    flux = np.empty((len(frame_times), 8))
    Lseq = np.empty((len(frame_times), 8, 8))
    for k in range(len(frame_times)):
        loops = []
        for j in range(8):
            loops.append(coil_polygon(centers[k, j], rotations[k, j], n0s[j],
                                      radius, segments))
            normal = rotations[k, j] @ n0s[j]
            flux[k, j] = N[j] * area * np.dot(B, normal)
        Lseq[k] = inductance_matrix(loops, N, radii, wire, softening_m)
    emf_ext = -np.diff(flux, axis=0) / np.diff(frame_times)[:, None]
    Rmat = np.eye(8) * resistance_ohm
    currents = midpoint_coupled_rl(Lseq, emf_ext, frame_times, Rmat)
    return {
        "model": "eight circular coils, one rigidly attached to each Jitterbug triangular panel",
        "status": "conditional numerical model; no measured apparatus validation",
        "panel_labels": [list(x) for x in labels],
        "edge_length_m": edge_length_m, "speed_m_s": speed_m_s,
        "turns_per_coil": int(turns), "coil_radius_m": radius,
        "wire_radius_m": wire_radius_m, "segments_per_loop": segments,
        "softening_m": softening_m, "B_tesla": B.tolist(),
        "resistance_ohm_per_coil": resistance_ohm,
        "frames": len(frame_times), "duration_s": float(frame_times[-1]),
        "max_panel_fit_residual_m": float(np.max(residuals)),
        "max_inductance_reciprocity_residual_H": float(np.max(
            np.abs(Lseq - np.swapaxes(Lseq, 1, 2)))),
        "min_inductance_eigenvalue_H": float(min(
            np.linalg.eigvalsh(x).min() for x in Lseq)),
        "max_abs_external_emf_V": float(np.max(np.abs(emf_ext))),
        "max_abs_current_A": float(np.max(np.abs(currents))),
        "flux_linkage_Wb_turn": flux.tolist(),
        "external_emf_V": emf_ext.tolist(),
        "currents_A": currents.tolist(),
        "times_s": frame_times.tolist(),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, default=None)
    p.add_argument("--segments", type=int, default=96)
    p.add_argument("--ds", type=float, default=0.02)
    p.add_argument("--B-tesla", type=float, nargs=3, default=(0, 0, 0.1))
    args = p.parse_args()
    report = build_run(segments=args.segments, ds=args.ds, B_tesla=args.B_tesla)
    rendered = json.dumps(report, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
