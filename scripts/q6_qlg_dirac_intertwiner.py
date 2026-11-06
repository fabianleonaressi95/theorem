"""Representation-theoretic QLG(2) -> Dirac(4) embedding audit.

The source QLG fibre is a complex SU(2) doublet.  Restricting the
Dirac representation to spatial Spin(3) gives U \oplus U.  Consequently
Hom_{SU(2)}(C^2,C^4) is two-dimensional: every intertwiner is
K_{alpha,beta} = (alpha I_2, beta I_2)^T.

This establishes a family of spatially equivariant isometric embeddings,
not a preferred physical embedding and not a Lorentz/boost intertwiner.
"""
from __future__ import annotations
import numpy as np


def su2_from_unit_quaternion(q):
    q = np.asarray(q, dtype=float)
    if q.shape != (4,) or not np.all(np.isfinite(q)):
        raise ValueError("q must be a finite scalar-first quaternion")
    norm = np.linalg.norm(q)
    if norm <= 1e-14:
        raise ValueError("q must be nonzero")
    w, x, y, z = q / norm
    return np.array([[w-1j*z, -y-1j*x],
                     [y-1j*x, w+1j*z]], dtype=complex)


def dirac_spatial_restriction(u):
    u = np.asarray(u, dtype=complex)
    if u.shape != (2, 2):
        raise ValueError("u must be 2x2")
    return np.block([[u, np.zeros((2, 2), complex)],
                     [np.zeros((2, 2), complex), u]])


def intertwiner(alpha=1.0, beta=0.0):
    """K: C^2 -> C^4; normalize alpha,beta for an isometric embedding."""
    a, b = complex(alpha), complex(beta)
    norm = np.sqrt(abs(a)**2 + abs(b)**2)
    if norm <= 1e-14:
        raise ValueError("alpha and beta cannot both vanish")
    a, b = a/norm, b/norm
    return np.vstack((a*np.eye(2), b*np.eye(2)))


def intertwiner_residual(q, alpha=1.0, beta=0.0):
    u = su2_from_unit_quaternion(q)
    k = intertwiner(alpha, beta)
    return float(np.linalg.norm(dirac_spatial_restriction(u) @ k - k @ u))


def numerical_intertwiner_dimension(quaternions, tol=1e-10):
    """Nullity of stacked equations (U⊕U)K-KU=0, K in C^(4x2)."""
    blocks = []
    for q in quaternions:
        u = su2_from_unit_quaternion(q)
        r = dirac_spatial_restriction(u)
        # vec(AK-KB) = (I kron A - B^T kron I) vec(K)
        blocks.append(np.kron(np.eye(2), r) - np.kron(u.T, np.eye(4)))
    matrix = np.vstack(blocks)
    singular = np.linalg.svd(matrix, compute_uv=False)
    rank = int(np.count_nonzero(singular > tol * max(singular[0], 1.0)))
    return 8-rank, singular.tolist()


def audit(seed=49049, samples=24, tol=2e-10):
    rng = np.random.default_rng(seed)
    qs = rng.normal(size=(samples, 4))
    dim, singular = numerical_intertwiner_dimension(qs, tol=tol)
    maps = [(1, 0), (0, 1), (1/np.sqrt(2), 1j/np.sqrt(2)), (0.6, 0.8)]
    residuals = [intertwiner_residual(q, *ab) for q in qs for ab in maps]
    isometry = max(float(np.linalg.norm(intertwiner(*ab).conj().T @
                                         intertwiner(*ab)-np.eye(2)))
                   for ab in maps)
    return {
        "schema": "T049C_QLG_DIRAC_INTERTWINER_AUDIT_V1",
        "input_representation": "SU(2) fundamental, complex dimension 2",
        "output_representation": "spatial Dirac restriction U direct_sum U, dimension 4",
        "sampled_group_elements": samples,
        "computed_intertwiner_dimension": dim,
        "theoretical_intertwiner_dimension": 2,
        "max_equivariance_residual": max(residuals),
        "max_isometry_residual": isometry,
        "singular_values_constraint_matrix": singular,
        "conclusion": "TWO_COMPLEX-DIMENSIONAL_FAMILY; NO_CANONICAL_EMBEDDING",
        "scope": "spatial SU(2)/2I subgroup only; no boost, parity, or Pin lift",
        "passed": dim == 2 and max(residuals) <= tol and isometry <= tol,
    }


def embed_fibre_field(field, alpha=1.0, beta=0.0):
    """Apply one explicitly chosen intertwiner to (...,2) fibre data."""
    x = np.asarray(field, dtype=complex)
    if x.ndim < 1 or x.shape[-1] != 2:
        raise ValueError("field must have final dimension 2")
    return x @ intertwiner(alpha, beta).T


if __name__ == "__main__":
    import json
    print(json.dumps(audit(), indent=2))
