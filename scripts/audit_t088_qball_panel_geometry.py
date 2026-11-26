#!/usr/bin/env python3
"""Geometric audit for T088: Q-ball panel frames, seam transport, holonomy.

The anisotropy alpha is dimensionless and illustrative, not material-calibrated.
"""
from __future__ import annotations
import json
from itertools import combinations
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from models.football_shell import build_football_shell, _panel_frame


def shortest_rotation(n0, n1):
    n0 = np.asarray(n0, float); n1 = np.asarray(n1, float)
    n0 /= np.linalg.norm(n0); n1 /= np.linalg.norm(n1)
    a = np.cross(n0, n1)
    s = np.linalg.norm(a)
    c = float(np.clip(n0 @ n1, -1.0, 1.0))
    if s < 1e-13:
        if c > 0:
            return np.eye(3)
        raise ValueError("antipodal adjacent panel normals: shortest rotation is not unique")
    A = np.array([[0., -a[2], a[1]],
                  [a[2], 0., -a[0]],
                  [-a[1], a[0], 0.]])
    return np.eye(3) + A + (A @ A) / (1.0 + c)


def random_o2(rng):
    theta = rng.uniform(-np.pi, np.pi)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s], [s, c]])
    if rng.integers(2):
        R[:, 0] *= -1
    return R


def main():
    rng = np.random.default_rng(20261111)
    alpha = 0.2
    mesh = build_football_shell()
    X = mesh["nodes"]
    panels = mesh["panels"]
    panel_count = len(panels)

    frames, normals, directions = [], [], []
    for face in panels:
        e1, e2, normal = _panel_frame(X, face, 0.0)
        Q = np.column_stack((e1, e2))
        frames.append(Q)
        normals.append(normal)
        centre = X[list(face)].mean(axis=0)
        directions.append(centre / np.linalg.norm(centre))
    frames = np.asarray(frames)
    normals = np.asarray(normals)
    directions = np.asarray(directions)

    # Map each physical seam to its two adjacent panel indices.
    seam_to_panels = {}
    for edge in sorted(mesh["physical_seams"]):
        tids = mesh["edge_triangles"][edge]
        pids = tuple(sorted(int(mesh["triangle_panels"][ti]) for ti in tids))
        if len(pids) != 2 or pids[0] == pids[1]:
            raise RuntimeError(f"invalid panel adjacency at seam {edge}: {pids}")
        seam_to_panels[edge] = pids

    U = {}
    adjacency = {p: set() for p in range(panel_count)}
    for edge, (p, q) in seam_to_panels.items():
        R3 = shortest_rotation(normals[p], normals[q])
        Upq = frames[q].T @ R3 @ frames[p]
        U[p, q] = Upq
        U[q, p] = Upq.T
        adjacency[p].add(q)
        adjacency[q].add(p)

    orth = [np.linalg.norm(U[p, q].T @ U[p, q] - np.eye(2))
            for p, q in U]
    reverse = [np.linalg.norm(U[q, p] - U[p, q].T) for p, q in U]

    # H4 spherical gradient and its tangent-frame anisotropy tensor.
    A = []
    grad_norms = []
    for p, n in enumerate(directions):
        h40 = float(np.sum(n**4))
        grad = 4.0 * (n**3 - h40 * n)
        gp = frames[p].T @ grad
        ng = np.linalg.norm(gp)
        grad_norms.append(ng)
        if ng > 1e-12:
            gh = gp / ng
            Ap = np.eye(2) + alpha * np.outer(gh, gh)
        else:
            Ap = np.eye(2)
        A.append(Ap)
    A = np.asarray(A)
    eigs = np.linalg.eigvalsh(A)

    # Enumerate 3-cycles in the panel adjacency graph.
    cycles = []
    for p, q, r in combinations(range(panel_count), 3):
        if q in adjacency[p] and r in adjacency[q] and p in adjacency[r]:
            H = U[r, p] @ U[q, r] @ U[p, q]
            angle = float(np.arctan2(H[1, 0] - H[0, 1],
                                     H[0, 0] + H[1, 1]))
            cycles.append((p, q, r, H, angle))
    holonomy_angles = [x[4] for x in cycles]

    # Check covariance under independent panel-frame changes Q'_p=Q_p S_p.
    S = [random_o2(rng) for _ in range(panel_count)]
    cov_U = []
    cov_A = []
    for p, q in U:
        Uprime = S[q].T @ U[p, q] @ S[p]
        cov_U.append(np.linalg.norm(Uprime - S[q].T @ U[p, q] @ S[p]))
    for p in range(panel_count):
        Aprime = S[p].T @ A[p] @ S[p]
        cov_A.append(np.linalg.norm(Aprime - S[p].T @ A[p] @ S[p]))

    # Seam anisotropy mismatch after transporting p's tensor to q's frame.
    seam_mismatch = []
    for p, q in seam_to_panels.values():
        transported = U[p, q] @ A[p] @ U[p, q].T
        seam_mismatch.append(np.linalg.norm(A[q] - transported, ord="fro"))

    result = {
        "mesh": {
            "panels": panel_count,
            "physical_seams": len(seam_to_panels),
            "panel_adjacency_edges": len(seam_to_panels),
            "three_panel_cycles": len(cycles)
        },
        "seam_transitions": {
            "max_orthogonality_residual": float(max(orth)),
            "max_reverse_transition_residual": float(max(reverse)),
            "minimum_normal_dot_adjacent": float(min(
                normals[p] @ normals[q] for p, q in seam_to_panels.values()))
        },
        "panel_holonomy": {
            "angle_min": float(min(holonomy_angles)) if holonomy_angles else None,
            "angle_max": float(max(holonomy_angles)) if holonomy_angles else None,
            "angle_rms": float(np.sqrt(np.mean(np.square(holonomy_angles)))) if holonomy_angles else None,
            "interpretation": "discrete panel-graph holonomy; not yet a Gaussian-curvature convergence result"
        },
        "H4_anisotropy": {
            "alpha": alpha,
            "gradient_norm_min": float(min(grad_norms)),
            "gradient_norm_max": float(max(grad_norms)),
            "eigenvalue_min": float(eigs.min()),
            "eigenvalue_max": float(eigs.max()),
            "seam_mismatch_rms": float(np.sqrt(np.mean(np.square(seam_mismatch)))),
            "seam_mismatch_max": float(max(seam_mismatch))
        },
        "chart_covariance": {
            "transition_residual": float(max(cov_U)),
            "anisotropy_tensor_residual": float(max(cov_A))
        },
        "classification": "geometric construction audit; alpha illustrative, no material calibration"
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
