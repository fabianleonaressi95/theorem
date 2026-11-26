#!/usr/bin/env python3
"""Finite verification of T113-G rank-two symmetry statements.

This script checks the algebraic invariance criterion on explicit planar
rotations and a finite icosahedral rotation group generated independently
in exact symbolic form is deliberately NOT claimed here. The planar checks
use floating-point matrices and report residuals; the theorem itself is
proved in the accompanying record.
"""
from __future__ import annotations

import json
import math
import numpy as np


def rotation(theta: float) -> np.ndarray:
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=float)


def invariance_residual(D: np.ndarray, R: np.ndarray) -> float:
    return float(np.linalg.norm(R @ D @ R.T - D, ord="fro"))


def run() -> dict:
    # Anisotropic symmetric tensor is not invariant under a 120-degree turn.
    D_aniso = np.diag([2.0, 1.0])
    R3 = rotation(2.0 * math.pi / 3.0)
    # Isotropic symmetric tensor is invariant under every planar rotation.
    D_iso = 1.7 * np.eye(2)
    # General nonsymmetric invariant tensors may contain the antisymmetric J.
    J = np.array([[0.0, -1.0], [1.0, 0.0]])
    D_general = 1.7 * np.eye(2) + 0.4 * J
    residuals = {
        "anisotropic_symmetric_under_C3": invariance_residual(D_aniso, R3),
        "isotropic_symmetric_under_C3": invariance_residual(D_iso, R3),
        "general_aI_plus_bJ_under_C3": invariance_residual(D_general, R3),
    }
    assert residuals["anisotropic_symmetric_under_C3"] > 1e-2
    assert residuals["isotropic_symmetric_under_C3"] < 1e-12
    assert residuals["general_aI_plus_bJ_under_C3"] < 1e-12
    return {
        "checks": residuals,
        "status": "PASS",
        "scope": "planar algebraic examples only; no Q6 projection or material tensor computed",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
