"""Constitutive law for a discrete elastic shell seam.

This is a mechanical shell law, not the relativistic Israel surface tensor.
Angles are in radians; energies and moments use a consistent unit system.
"""
from __future__ import annotations
import numpy as np


def seam_bending_law(theta, theta0, Db, length, width, multiplier=1.0):
    """Return edge energy, conjugate hinge moment and linear tangent stiffness.

    E = 1/2 * Db * multiplier * (length/width) * (theta-theta0)^2.
    """
    if Db <= 0 or length <= 0 or width <= 0 or multiplier < 0:
        raise ValueError("Db, length and width must be positive; multiplier nonnegative")
    delta = float(theta) - float(theta0)
    k = float(Db) * float(multiplier) * float(length) / float(width)
    return {
        "rotation_jump": delta,
        "energy": 0.5 * k * delta**2,
        "edge_moment": k * delta,
        "tangent_stiffness": k,
        "units_note": "energy and edge_moment have units Db; angle is dimensionless",
    }


def seam_cohesive_law(jump, Kline, length):
    """Quadratic translational interface law: E=1/2 length jump^T Kline jump."""
    d = np.asarray(jump, dtype=float).reshape(-1)
    K = np.asarray(Kline, dtype=float)
    if K.shape != (d.size, d.size) or length <= 0:
        raise ValueError("Kline must be square with jump dimension and length positive")
    if not np.allclose(K, K.T, atol=1e-10):
        raise ValueError("Kline must be symmetric")
    eig = np.linalg.eigvalsh(K)
    if eig[0] < -1e-10:
        raise ValueError("Kline must be positive semidefinite")
    resultant_per_length = K @ d
    return {
        "energy": float(0.5 * length * d @ K @ d),
        "resultant_per_length": resultant_per_length,
        "resultant": length * resultant_per_length,
    }


def quaternion_relative_rotation(q_minus, q_plus, edge_tangent):
    """Signed relative rotation about the oriented edge tangent.

    q are scalar-first unit quaternions mapping local frames to ambient frames.
    The returned angle is the SO(3) logarithm projected on the oriented edge.
    """
    qm = np.asarray(q_minus, dtype=float).reshape(4)
    qp = np.asarray(q_plus, dtype=float).reshape(4)
    t = np.asarray(edge_tangent, dtype=float).reshape(3)
    if np.linalg.norm(qm) < 1e-14 or np.linalg.norm(qp) < 1e-14 or np.linalg.norm(t) < 1e-14:
        raise ValueError("quaternions and edge tangent must be nonzero")
    qm = qm / np.linalg.norm(qm)
    qp = qp / np.linalg.norm(qp)
    t = t / np.linalg.norm(t)
    # q_rel = conjugate(q_minus) * q_plus
    w1, x1, y1, z1 = qm
    w2, x2, y2, z2 = qp
    qrel = np.array([
        w1*w2 + x1*x2 + y1*y2 + z1*z2,
        w1*x2 - x1*w2 - y1*z2 + z1*y2,
        w1*y2 + x1*z2 - y1*w2 - z1*x2,
        w1*z2 - x1*y2 + y1*x2 - z1*w2,
    ])
    qrel /= np.linalg.norm(qrel)
    # Choose the principal representative; q and -q encode the same SO(3) rotation.
    if qrel[0] < 0:
        qrel = -qrel
    vn = np.linalg.norm(qrel[1:])
    if vn < 1e-14:
        rotvec = np.zeros(3)
    else:
        angle = 2.0 * np.arctan2(vn, np.clip(qrel[0], -1.0, 1.0))
        rotvec = angle * qrel[1:] / vn
    return float(rotvec @ t)


def seam_internal_force(moment, dihedral_gradient):
    """Small-rotation internal force vector f_int = moment * grad(theta)."""
    g = np.asarray(dihedral_gradient, dtype=float).reshape(-1)
    return float(moment) * g


def seam_tangent_matrix(tangent_stiffness, dihedral_gradient):
    """Material part of the consistent tangent: k * grad(theta) grad(theta)^T."""
    g = np.asarray(dihedral_gradient, dtype=float).reshape(-1)
    return float(tangent_stiffness) * np.outer(g, g)
