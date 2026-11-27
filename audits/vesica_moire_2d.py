#!/usr/bin/env python3
"""Reproducible scalar 2-D Vesica/radial-Moire graph audit.

This is a scalar graph-wave prototype, not a Maxwell solver.
Dependencies: numpy, scipy; matplotlib is optional for --plot.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh


def phase_field(n: int = 32, length: float = 12.0, a: float = 1.0,
                k: float = np.pi / 2) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return coordinates and Δφ=k(ρ1-ρ2) on an n-by-n interior grid."""
    if n < 2 or length <= 0 or a <= 0 or k <= 0:
        raise ValueError("Require n>=2 and positive length, a, k.")
    h = length / (n + 1)
    x = np.linspace(-length / 2 + h, length / 2 - h, n)
    X, Y = np.meshgrid(x, x, indexing="ij")
    rho1 = np.hypot(X + a, Y)
    rho2 = np.hypot(X - a, Y)
    return X, Y, k * (rho1 - rho2)


def weighted_graph_laplacian(delta: np.ndarray, length: float,
                             epsilon: float, weighted: bool = True):
    """Build B.T W B / h² on an n-by-n grid, with free graph boundaries."""
    if delta.ndim != 2 or delta.shape[0] != delta.shape[1]:
        raise ValueError("delta must be a square 2-D array.")
    if not (abs(epsilon) < 1):
        raise ValueError("Require |epsilon| < 1 for strictly positive weights.")
    n = delta.shape[0]
    h = length / (n + 1)
    rows: list[int] = []
    cols: list[int] = []
    vals: list[float] = []
    edge_weights: list[float] = []

    for i in range(n):
        for j in range(n):
            p = i * n + j
            for di, dj in ((1, 0), (0, 1)):
                ii, jj = i + di, j + dj
                if ii >= n or jj >= n:
                    continue
                q = ii * n + jj
                phase_mid = 0.5 * (delta[i, j] + delta[ii, jj])
                w = 1.0 + epsilon * np.cos(phase_mid) if weighted else 1.0
                w_scaled = float(w) / h**2
                edge_weights.append(float(w))
                rows.extend((p, p, q, q))
                cols.extend((p, q, p, q))
                vals.extend((w_scaled, -w_scaled, -w_scaled, w_scaled))

    size = n * n
    matrix = coo_matrix((vals, (rows, cols)), shape=(size, size)).tocsr()
    return matrix, np.asarray(edge_weights)


def low_spectrum(matrix, count: int = 9) -> np.ndarray:
    """Smallest eigenvalues, including the graph's constant zero mode."""
    n = matrix.shape[0]
    if count < 2 or count >= n:
        raise ValueError("count must satisfy 2 <= count < matrix dimension.")
    vals = eigsh(matrix, k=count, which="SM", return_eigenvectors=False,
                 tol=1e-10, maxiter=max(1000, 20 * n))
    vals = np.sort(np.real(vals))
    vals[np.abs(vals) < 1e-9] = 0.0
    return vals


def run(n: int = 32, length: float = 12.0, a: float = 1.0,
        k: float = np.pi / 2, epsilon: float = 0.10,
        modes: int = 9) -> dict:
    X, Y, delta = phase_field(n, length, a, k)
    L0, w0 = weighted_graph_laplacian(delta, length, epsilon, weighted=False)
    LM, wm = weighted_graph_laplacian(delta, length, epsilon, weighted=True)
    eig0 = low_spectrum(L0, modes)
    eigM = low_spectrum(LM, modes)
    rows = []
    for index, (u, m) in enumerate(zip(eig0[1:], eigM[1:]), start=1):
        rows.append({
            "mode": index,
            "lambda_uniform": float(u),
            "lambda_moire": float(m),
            "frequency_proxy_uniform": float(np.sqrt(max(u, 0.0))),
            "frequency_proxy_moire": float(np.sqrt(max(m, 0.0))),
            "frequency_shift_percent": float(100 * (np.sqrt(max(m, 0.0) / u) - 1))
            if u > 0 else None,
        })
    return {
        "model": "scalar weighted graph Laplacian; not Maxwell",
        "parameters": {
            "n": n, "length": length, "a": a, "k": k,
            "epsilon": epsilon, "modes_including_zero": modes,
            "grid_spacing": length / (n + 1),
            "boundary_convention": "free graph boundary; internal nearest-neighbour edges only",
        },
        "phase_range": [float(delta.min()), float(delta.max())],
        "uniform_edge_weight_range": [float(w0.min()), float(w0.max())],
        "moire_edge_weight_range": [float(wm.min()), float(wm.max())],
        "uniform_eigenvalues": eig0.tolist(),
        "moire_eigenvalues": eigM.tolist(),
        "nonzero_mode_comparison": rows,
        "interpretation": (
            "Normalized scalar-operator spectrum only. No optical-frequency calibration, "
            "vector Maxwell equations, topological defects, or physical spectrum prediction."
        ),
    }, X, Y, delta


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=32)
    parser.add_argument("--length", type=float, default=12.0)
    parser.add_argument("--a", type=float, default=1.0)
    parser.add_argument("--k", type=float, default=float(np.pi / 2))
    parser.add_argument("--epsilon", type=float, default=0.10)
    parser.add_argument("--modes", type=int, default=9)
    parser.add_argument("--output-dir", type=Path, default=Path("results/vesica_moire"))
    parser.add_argument("--plot", action="store_true", help="Write an optional PNG (needs matplotlib).")
    args = parser.parse_args()

    report, X, Y, delta = run(args.n, args.length, args.a, args.k,
                              args.epsilon, args.modes)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "scalar_graph_spectrum.json"
    csv_path = args.output_dir / "scalar_graph_spectrum.csv"
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(report["nonzero_mode_comparison"][0]))
        writer.writeheader()
        writer.writerows(report["nonzero_mode_comparison"])

    if args.plot:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(6, 5))
        image = ax.contourf(X, Y, np.cos(delta), levels=32)
        ax.contour(X, Y, delta, levels=np.linspace(-np.pi, np.pi, 13),
                   colors="black", linewidths=0.45)
        ax.set_aspect("equal")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Two-circle radial phase difference")
        fig.colorbar(image, ax=ax, label="cos(Δφ)")
        fig.tight_layout()
        fig.savefig(args.output_dir / "vesica_moire_phase.png", dpi=180)
        plt.close(fig)

    print(json.dumps({
        "json": str(json_path),
        "csv": str(csv_path),
        "moire_weight_range": report["moire_edge_weight_range"],
        "lowest_nonzero_frequency_shifts_percent": [
            row["frequency_shift_percent"] for row in report["nonzero_mode_comparison"]
        ],
        "status": "scalar graph audit only; not a Maxwell result",
    }, indent=2))


if __name__ == "__main__":
    main()
