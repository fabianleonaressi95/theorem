#!/usr/bin/env python3
"""Finite algebraic checks for S.9 rotating-field/coframe identities."""
from __future__ import annotations
import json
import math
import numpy as np


def rotation(theta: float) -> np.ndarray:
    return np.array([[math.cos(theta), -math.sin(theta)],
                     [math.sin(theta), math.cos(theta)]])


def run() -> dict:
    t = np.linspace(0.0, 2.0 * math.pi, 257, endpoint=False)
    # Ferraris: two orthogonal axes, temporal quadrature.
    h2 = np.column_stack((np.cos(t), np.sin(t)))
    norm2 = np.linalg.norm(h2, axis=1)

    # Three phase axes and balanced currents, same positive sequence.
    alpha = 2.0 * math.pi * np.arange(3) / 3.0
    axes = np.column_stack((np.cos(alpha), np.sin(alpha)))
    h3 = np.stack([
        np.sum(np.cos(tt - alpha)[:, None] * axes, axis=0)
        for tt in t
    ])
    target = 1.5 * h2
    three_phase_residual = float(np.max(np.linalg.norm(h3 - target, axis=1)))

    # Orthonormal coframe rotation: components rotate inversely to frame.
    theta = 0.731
    R = rotation(theta)
    v = np.array([0.6, -0.8])
    v_prime = R @ v
    frame_prime = R.T
    coordinate_before = np.eye(2) @ v
    coordinate_after = frame_prime @ v_prime

    return {
        "two_coil_amplitude_spread": float(np.ptp(norm2)),
        "three_phase_amplitude_spread": float(np.ptp(np.linalg.norm(h3, axis=1))),
        "three_phase_identity_residual": three_phase_residual,
        "coframe_frame_covariance_residual": float(np.linalg.norm(coordinate_before - coordinate_after)),
        "checks": {
            "two_coil_constant_amplitude": bool(np.ptp(norm2) < 1e-12),
            "three_phase_constant_amplitude": bool(np.ptp(np.linalg.norm(h3, axis=1)) < 1e-12),
            "three_phase_identity": bool(three_phase_residual < 1e-12),
            "coframe_covariance": bool(np.linalg.norm(coordinate_before - coordinate_after) < 1e-12),
        },
        "scope": "ideal balanced winding identities and 2D frame covariance only; no motor, Maxwell PDE, or RGS embedding solved",
    }


if __name__ == "__main__":
    report = run()
    report["pass"] = all(report["checks"].values())
    print(json.dumps(report, indent=2))
