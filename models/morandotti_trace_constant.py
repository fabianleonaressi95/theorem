"""Finite-dimensional generalized-eigenvalue estimate for T134 trace constants."""
from __future__ import annotations

import numpy as np
from scipy.linalg import eigh
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh


def largest_generalized_eigenvalue(numerator, denominator, *, tol=1e-9,
                                   return_diagnostics=False):
    """Compute max x.T A x / x.T B x and verify the computed eigenpair.

    B must be numerically positive definite. The reported residual is the
    normwise residual of A x = lambda B x. This validates the algebraic solve,
    not the FEM formulation or quadrature accuracy.
    """
    A = csr_matrix(numerator, dtype=float)
    B = csr_matrix(denominator, dtype=float)
    if A.shape != B.shape or A.ndim != 2 or A.shape[0] == 0:
        raise ValueError("numerator and denominator must be nonempty square matrices of equal shape")
    if not np.isfinite(A.data).all() or not np.isfinite(B.data).all():
        raise ValueError("generalized eigenvalue matrices must be finite")
    scale_a = max(float(np.linalg.norm(A.data)), 1.0)
    scale_b = max(float(np.linalg.norm(B.data)), 1.0)
    asym_a = float(np.max(np.abs((A - A.T).data))) if (A - A.T).nnz else 0.0
    asym_b = float(np.max(np.abs((B - B.T).data))) if (B - B.T).nnz else 0.0
    if asym_a > 1e-9 * scale_a:
        raise ValueError("numerator matrix is not symmetric")
    if asym_b > 1e-9 * scale_b:
        raise ValueError("denominator matrix is not symmetric")

    n = A.shape[0]
    if n <= 3:
        Ad, Bd = A.toarray(), B.toarray()
        bvals, bvecs = np.linalg.eigh(Bd)
        bmin, bmax = float(bvals[0]), float(bvals[-1])
        if bmin <= 1e-12 * max(bmax, 1.0):
            raise ValueError(f"denominator is not numerically positive definite: lambda_min={bmin:g}")
        values, vectors = eigh(Ad, Bd, check_finite=True)
        result = float(values[-1])
        x = vectors[:, -1]
    else:
        bmin_arr = eigsh(B, k=1, which="SA", tol=max(tol, 1e-8),
                         return_eigenvectors=False, maxiter=max(5000, 5*n))
        bmax_arr = eigsh(B, k=1, which="LA", tol=max(tol, 1e-8),
                         return_eigenvectors=False, maxiter=max(5000, 5*n))
        bmin, bmax = float(bmin_arr[0]), float(bmax_arr[0])
        if not np.isfinite(bmin) or bmin <= 1e-12 * max(bmax, 1.0):
            raise ValueError(
                "denominator is not numerically positive definite: "
                f"lambda_min={bmin:g}, lambda_max={bmax:g}"
            )
        values, vectors = eigsh(A, k=1, M=B, which="LA", tol=tol,
                                return_eigenvectors=True, maxiter=max(5000, 5*n))
        result = float(values[0])
        x = vectors[:, 0]

    Ax = A @ x
    Bx = B @ x
    rayleigh = float(np.dot(x, Ax) / np.dot(x, Bx))
    residual = float(np.linalg.norm(Ax - result * Bx) /
                     max(np.linalg.norm(Ax) + abs(result)*np.linalg.norm(Bx), 1e-300))
    diagnostics = {
        "denominator_lambda_min_estimate": bmin,
        "denominator_lambda_max_estimate": bmax,
        "denominator_condition_estimate": float(bmax / bmin),
        "generalized_eigenvalue": result,
        "rayleigh_quotient_check": rayleigh,
        "relative_generalized_eigenpair_residual": residual,
        "numerator_relative_symmetry_defect": float(asym_a / scale_a),
        "denominator_relative_symmetry_defect": float(asym_b / scale_b),
    }
    if not np.isfinite(result) or not np.isfinite(residual):
        raise RuntimeError("largest generalized eigenpair is not finite")
    if abs(rayleigh - result) > 1e-7 * max(abs(result), 1.0):
        raise RuntimeError("generalized eigenvalue disagrees with its Rayleigh quotient")
    if residual > 1e-7:
        raise RuntimeError(f"generalized eigenpair residual too large: {residual:g}")
    return (result, diagnostics) if return_diagnostics else result
