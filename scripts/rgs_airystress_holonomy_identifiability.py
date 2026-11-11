#!/usr/bin/env python3
"""Audit what Airy stress does and does not identify about defect holonomy."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Callable
import numpy as np

J = np.array([[0.0, -1.0], [1.0, 0.0]])

def plane_strain_from_stress(stress: np.ndarray, young_modulus: float,
                             poisson_ratio: float) -> np.ndarray:
    """3D isotropic Hooke law restricted to plane strain (epsilon_zz=0)."""
    sigma = np.asarray(stress, dtype=float)
    E, nu = float(young_modulus), float(poisson_ratio)
    if sigma.shape[-2:] != (2, 2) or not np.isfinite(sigma).all():
        raise ValueError("stress must be finite with shape (..., 2, 2)")
    if not np.allclose(sigma, np.swapaxes(sigma, -1, -2), atol=1e-11):
        raise ValueError("stress must be symmetric")
    if not np.isfinite(E) or E <= 0.0:
        raise ValueError("young_modulus must be positive and finite")
    if not np.isfinite(nu) or not (-1.0 < nu < 0.5):
        raise ValueError("poisson_ratio must lie in (-1, 1/2)")
    trace = np.trace(sigma, axis1=-2, axis2=-1)
    return ((1.0 + nu) / E) * (sigma - nu * trace[..., None, None] * np.eye(2))

def elastic_distortion(strain: np.ndarray, local_rotation: np.ndarray) -> np.ndarray:
    """Return beta = epsilon + omega J; epsilon alone leaves omega unknown."""
    eps = np.asarray(strain, dtype=float)
    omega = np.asarray(local_rotation, dtype=float)
    if eps.shape[-2:] != (2, 2) or not np.isfinite(eps).all():
        raise ValueError("strain must be finite with shape (..., 2, 2)")
    if not np.isfinite(omega).all():
        raise ValueError("local_rotation must be finite")
    return eps + omega[..., None, None] * J

def polygon_area(vertices: np.ndarray) -> float:
    points = np.asarray(vertices, dtype=float)
    if points.ndim != 2 or points.shape[1] != 2 or len(points) < 3:
        raise ValueError("vertices must have shape (N, 2), N >= 3")
    if not np.isfinite(points).all():
        raise ValueError("vertices must be finite")
    return float(0.5 * np.sum(points[:, 0] * np.roll(points[:, 1], -1)
                              - points[:, 1] * np.roll(points[:, 0], -1)))

def loop_closure(vertices: np.ndarray, strain_at: Callable[[np.ndarray], np.ndarray],
                 rotation_at: Callable[[np.ndarray], float]) -> np.ndarray:
    """Midpoint line integral b = integral_beta dx around a closed polygon."""
    points = np.asarray(vertices, dtype=float)
    if points.ndim != 2 or points.shape[1] != 2 or len(points) < 3:
        raise ValueError("vertices must have shape (N, 2), N >= 3")
    result = np.zeros(2)
    for p, q in zip(points, np.roll(points, -1, axis=0)):
        delta = q - p
        midpoint = 0.5 * (p + q)
        eps = np.asarray(strain_at(midpoint), dtype=float)
        omega = float(rotation_at(midpoint))
        if eps.shape != (2, 2) or not np.isfinite(eps).all() or not np.isfinite(omega):
            raise ValueError("field callbacks must return finite strain (2,2) and rotation")
        result += elastic_distortion(eps, np.asarray(omega)) @ delta
    return result

def audit_rotation_ambiguity(radius: float = 0.2, vertices_count: int = 256,
                             rotation_gradient: float = 1.0) -> dict:
    """Same zero strain, two skew fields, different Burgers loop closures."""
    r, c = float(radius), float(rotation_gradient)
    if not np.isfinite(r) or r <= 0.0:
        raise ValueError("radius must be positive and finite")
    if not np.isfinite(c):
        raise ValueError("rotation_gradient must be finite")
    if int(vertices_count) < 8:
        raise ValueError("vertices_count must be at least 8")
    angles = 2.0 * np.pi * np.arange(int(vertices_count)) / int(vertices_count)
    vertices = r * np.column_stack((np.cos(angles), np.sin(angles)))
    zero_strain = lambda _x: np.zeros((2, 2))
    b0 = loop_closure(vertices, zero_strain, lambda _x: 0.0)
    b1 = loop_closure(vertices, zero_strain, lambda x: c * float(x[0]))
    area = polygon_area(vertices)
    predicted = np.array([-c * area, 0.0])
    return {
        "status": "numerical non-identifiability witness",
        "same_symmetric_strain": True,
        "strain": [[0.0, 0.0], [0.0, 0.0]],
        "loop_vertices": int(vertices_count),
        "polygon_area": area,
        "rotation_fields": ["omega_0(x)=0", f"omega_1(x)={c}*x_1"],
        "burgers_closure_zero_rotation": b0.tolist(),
        "burgers_closure_affine_rotation": b1.tolist(),
        "analytic_affine_rotation_closure": predicted.tolist(),
        "closure_difference_norm": float(np.linalg.norm(b1 - b0)),
        "quadrature_identity_residual": float(np.linalg.norm(b1 - predicted)),
        "conclusion": ("The same strain field is compatible with distinct elastic-distortion "
          "loop closures. Airy stress plus a constitutive law does not identify translational "
          "SE(2) holonomy without an independently specified rotation/distortion field.")
    }

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--radius", type=float, default=0.2)
    parser.add_argument("--vertices", type=int, default=256)
    parser.add_argument("--rotation-gradient", type=float, default=1.0)
    parser.add_argument("--out", default="artifacts/airystress_holonomy_identifiability/report.json")
    args = parser.parse_args()
    report = audit_rotation_ambiguity(args.radius, args.vertices, args.rotation_gradient)
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
