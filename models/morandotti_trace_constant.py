"""Finite-dimensional generalized-eigenvalue estimate for T134 trace constants."""
from __future__ import annotations

import numpy as np
from scipy.linalg import eigh
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh


def largest_generalized_eigenvalue(numerator, denominator, *, tol=1e-10):
    """Return max x.T A x / x.T B x for symmetric A and SPD B.

    Inputs may be dense arrays or SciPy sparse matrices. This routine estimates
    the exact finite-dimensional supremum represented by the assembled FEM
    matrices; it does not prove a bound uniform over a mesh family.
    """
    A = csr_matrix(numerator, dtype=float)
    B = csr_matrix(denominator, dtype=float)
    if A.shape != B.shape or A.ndim != 2 or A.shape[0] == 0:
        raise ValueError("numerator and denominator must be nonempty square matrices of equal shape")
    if not np.isfinite(A.data).all() or not np.isfinite(B.data).all():
        raise ValueError("generalized eigenvalue matrices must be finite")
    scale_a = max(float(np.linalg.norm(A.data)), 1.0)
    scale_b = max(float(np.linalg.norm(B.data)), 1.0)
    if (A - A.T).data.size and np.max(np.abs((A - A.T).data)) > 1e-9 * scale_a:
        raise ValueError("numerator matrix is not symmetric")
    if (B - B.T).data.size and np.max(np.abs((B - B.T).data)) > 1e-9 * scale_b:
        raise ValueError("denominator matrix is not symmetric")
    n = A.shape[0]
    if n <= 3:
        values = eigh(A.toarray(), B.toarray(), eigvals_only=True, check_finite=True)
        result = float(values[-1])
    else:
        values = eigsh(A, k=1, M=B, which="LA", tol=tol, return_eigenvectors=False)
        result = float(values[0])
    if not np.isfinite(result):
        raise RuntimeError("largest generalized eigenvalue is not finite")
    return result
