#!/usr/bin/env python3
"""Manufactured SE(2) face-holonomy audit and Morandotti source adapter.

The smooth-connection experiment checks the local Cartan estimate from T093.
An optional core-holonomy JSON converts already measured loop data into the
Frank/Burgers ordering used by models.morandotti_cell_reconstruction.
It does not infer singular core data from a smooth manufactured field.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import logm

from models.morandotti_cell_reconstruction import build_defect_components


def se2(omega: float, velocity: np.ndarray) -> np.ndarray:
    out = np.zeros((3, 3), dtype=float)
    out[:2, :2] = omega * np.array([[0.0, -1.0], [1.0, 0.0]])
    out[:2, 2] = np.asarray(velocity, dtype=float)
    return out


def connection(x: float, y: float) -> tuple[np.ndarray, np.ndarray]:
    """Return A_x,A_y for a smooth, noncommuting manufactured connection."""
    ax = se2(0.17 * y, np.array([1.0 + 0.13 * y, 0.07 * x]))
    ay = se2(0.23 * x, np.array([0.09 * y, 1.0 + 0.11 * x]))
    return ax, ay


def curvature_xy(x: float, y: float) -> np.ndarray:
    """F_xy = d_x A_y - d_y A_x + [A_x,A_y]."""
    ax, ay = connection(x, y)
    dAy_dx = se2(0.23, np.array([0.0, 0.11]))
    dAx_dy = se2(0.17, np.array([0.13, 0.0]))
    return dAy_dx - dAx_dy + ax @ ay - ay @ ax


def edge_transport(p: np.ndarray, q: np.ndarray,
                   rtol: float = 2e-12, atol: float = 2e-14) -> np.ndarray:
    """Solve dU/dt = -A(gamma_dot) U along the straight edge p -> q."""
    delta = np.asarray(q, dtype=float) - np.asarray(p, dtype=float)

    def rhs(t: float, flat: np.ndarray) -> np.ndarray:
        point = p + t * delta
        ax, ay = connection(float(point[0]), float(point[1]))
        a_t = delta[0] * ax + delta[1] * ay
        u = flat.reshape(3, 3)
        return (-a_t @ u).reshape(-1)

    sol = solve_ivp(rhs, (0.0, 1.0), np.eye(3).reshape(-1),
                    method="DOP853", rtol=rtol, atol=atol)
    if not sol.success:
        raise RuntimeError(f"edge transport integration failed: {sol.message}")
    return sol.y[:, -1].reshape(3, 3)


def equilateral_vertices(center: tuple[float, float], side: float) -> np.ndarray:
    cx, cy = center
    h = float(side)
    vertices = np.array([
        [cx + h / np.sqrt(3.0), cy],
        [cx - h / (2.0 * np.sqrt(3.0)), cy + h / 2.0],
        [cx - h / (2.0 * np.sqrt(3.0)), cy - h / 2.0],
    ])
    return vertices


def face_holonomy(vertices: np.ndarray) -> np.ndarray:
    """Positive (CCW) loop, based at vertex 0: U_ki U_jk U_ij."""
    p0, p1, p2 = np.asarray(vertices, dtype=float)
    u01 = edge_transport(p0, p1)
    u12 = edge_transport(p1, p2)
    u20 = edge_transport(p2, p0)
    return u20 @ u12 @ u01


def audit_sizes(sizes: list[float], center=(0.4, 0.5)) -> dict:
    rows = []
    for h in sizes:
        if h <= 0:
            raise ValueError("all triangle side lengths must be positive")
        vertices = equilateral_vertices(center, h)
        area = np.sqrt(3.0) * h * h / 4.0
        holonomy = face_holonomy(vertices)
        logarithm = np.real_if_close(logm(holonomy), tol=1000).real
        estimate = -logarithm / area
        exact = curvature_xy(*center)
        error = float(np.linalg.norm(estimate - exact, ord="fro"))
        rows.append({
            "side_length": float(h),
            "area": float(area),
            "density_error_frobenius": error,
            "estimated_curvature_matrix": estimate.tolist(),
            "exact_curvature_matrix_at_centroid": exact.tolist(),
            "holonomy": holonomy.tolist(),
            "log_holonomy": logarithm.tolist(),
        })
    rows.sort(key=lambda row: row["side_length"], reverse=True)
    rates = []
    for coarse, fine in zip(rows, rows[1:]):
        rates.append({
            "coarse_h": coarse["side_length"],
            "fine_h": fine["side_length"],
            "error_ratio_coarse_over_fine": (
                coarse["density_error_frobenius"] /
                max(fine["density_error_frobenius"], 1e-30)
            ),
        })
    ax, ay = connection(*center)
    commutator_norm = float(np.linalg.norm(ax @ ay - ay @ ax, ord="fro"))
    return {
        "title": "Manufactured noncommuting SE(2) face-holonomy audit",
        "status": "generated numerical audit; execution required before verification claim",
        "connection": "A_x=se2(0.17*y,[1+0.13*y,0.07*x]); A_y=se2(0.23*x,[0.09*y,1+0.11*x])",
        "convention": "dU/dt=-A(gamma_dot)U; H=U_ki U_jk U_ij; estimator=-log(H)/area",
        "center": list(center),
        "commutator_frobenius_norm_at_center": commutator_norm,
        "rows": rows,
        "successive_refinement": rates,
        "interpretation": (
            "The target is first-order density consistency O(h) from T093. "
            "The report contains measurements only; no rate is asserted until executed."
        ),
    }


def adapt_core_holonomies(path: Path) -> dict:
    """Map measured log-loop blocks to the existing Morandotti source convention.

    Input schema:
      {"cores":[{"center":[x,y],"theta":Theta,"q":[qx,qy]}, ...]}
    With log(H)=[[Theta*J,q],[0,0]], the T093 convention is
    Frank=-Theta and Burgers=-q. These integrated core data are not
    interchangeable with pointwise smooth curvature/torsion densities.
    """
    payload = json.loads(path.read_text())
    cores = payload.get("cores")
    if not isinstance(cores, list) or not cores:
        raise ValueError("core holonomy input must contain a non-empty 'cores' list")
    centers, frank, burgers = [], [], []
    for index, core in enumerate(cores):
        c = np.asarray(core.get("center"), dtype=float)
        q = np.asarray(core.get("q"), dtype=float)
        theta = float(core.get("theta"))
        if c.shape != (2,) or q.shape != (2,):
            raise ValueError(f"core {index}: center and q must each have length 2")
        if not np.isfinite(c).all() or not np.isfinite(q).all() or not np.isfinite(theta):
            raise ValueError(f"core {index}: all data must be finite")
        centers.append(c)
        frank.append(-theta)
        burgers.append(-q)
    phi_f, phi_b, phi = build_defect_components(
        np.asarray(centers), np.asarray(frank), np.asarray(burgers)
    )
    return {
        "mapping": "frank=-theta; burgers=-q; Phi uses build_defect_components convention",
        "centers": np.asarray(centers).tolist(),
        "frank_angles": frank,
        "burgers_vectors": burgers,
        "phi_frank": phi_f.tolist(),
        "phi_burgers": phi_b.tolist(),
        "phi_total": phi.tolist(),
        "status": "source-vector adapter only; interaction solve requires a separately audited Morandotti matrix",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="+", type=float,
                        default=[0.32, 0.16, 0.08, 0.04])
    parser.add_argument("--center", nargs=2, type=float, default=[0.4, 0.5])
    parser.add_argument("--out", default="artifacts/se2_holonomy_audit/report.json")
    parser.add_argument("--core-holonomies", type=Path, default=None)
    args = parser.parse_args()
    report = audit_sizes(args.sizes, tuple(args.center))
    if args.core_holonomies is not None:
        report["morandotti_core_source_adapter"] = adapt_core_holonomies(args.core_holonomies)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "output": str(out),
        "commutator_norm": report["commutator_frobenius_norm_at_center"],
        "density_errors": [r["density_error_frobenius"] for r in report["rows"]],
        "morandotti_adapter": args.core_holonomies is not None,
    }, indent=2))


if __name__ == "__main__":
    main()
