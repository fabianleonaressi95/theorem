"""Finite-dimensional generalized-eigenvalue estimate for T134 trace constants."""
from __future__ import annotations

import numpy as np
from scipy.linalg import eigh
from scipy.sparse import csr_matrix, diags
from scipy.sparse.linalg import eigsh


def largest_generalized_eigenvalue(numerator, denominator, *, tol=1e-10,
                                   return_diagnostics=False):
    """Compute max x.T A x / x.T B x with diagonal equilibration.

    B must be positive definite. Congruence scaling by diag(B)^(-1/2)
    preserves the generalized spectrum while reducing the severe coefficient
    scaling caused by curved, graded finite-element Hessian Gram matrices.
    The returned eigenpair is checked in the equilibrated coordinates.
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

    # Remove harmless assembly asymmetry before factorization.
    A = ((A + A.T) * 0.5).tocsr()
    B = ((B + B.T) * 0.5).tocsr()
    n = A.shape[0]

    if n <= 3:
        Ad, Bd = A.toarray(), B.toarray()
        bvals = np.linalg.eigvalsh(Bd)
        bmin, bmax = float(bvals[0]), float(bvals[-1])
        if bmin <= 1e-12 * max(bmax, 1.0):
            raise ValueError(f"denominator is not numerically positive definite: lambda_min={bmin:g}")
        values, vectors = eigh(Ad, Bd, check_finite=True)
        result = float(values[-1])
        x = vectors[:, -1]
        residual_matrix_a, residual_matrix_b = A, B
        scaling_min = scaling_max = 1.0
    else:
        diagonal = np.asarray(B.diagonal(), dtype=float)
        if not np.isfinite(diagonal).all() or np.any(diagonal <= 0.0):
            raise ValueError(
                "denominator has a non-positive or non-finite diagonal; "
                "the Hessian energy may contain unconstrained null modes"
            )

        # Congruence transform: x = S y, S_ii = B_ii^(-1/2).
        # The equilibrated denominator has unit diagonal.
        inv_sqrt_diagonal = 1.0 / np.sqrt(diagonal)
        S = diags(inv_sqrt_diagonal, format="csr")
        As = (S @ A @ S).tocsr()
        Bs = (S @ B @ S).tocsr()
        residual_matrix_a, residual_matrix_b = As, Bs
        scaling_min = float(np.min(inv_sqrt_diagonal))
        scaling_max = float(np.max(inv_sqrt_diagonal))

        ncv_values = sorted(set(min(n, value) for value in
                                (40, 80, 160, 320) if min(n, value) > 2))
        best = None
        last_error = None
        for ncv in ncv_values:
            try:
                values, vectors = eigsh(
                    As, k=1, M=Bs, which="LA", tol=tol,
                    return_eigenvectors=True, maxiter=max(30000, 30*n),
                    ncv=ncv,
                )
                y = vectors[:, 0]
                candidate_value = float(values[0])
                Ay, By = As @ y, Bs @ y
                rq = float(np.dot(y, Ay) / np.dot(y, By))
                res = float(np.linalg.norm(Ay - rq * By) /
                            max(np.linalg.norm(Ay) + abs(rq)*np.linalg.norm(By), 1e-300))
                if best is None or res < best[0]:
                    best = (res, candidate_value, rq, y.copy())
                if np.isfinite(res) and res <= 1e-7:
                    break
            except Exception as exc:
                from scipy.sparse.linalg import ArpackNoConvergence
                if isinstance(exc, RuntimeError) and "Factor is exactly singular" in str(exc):
                    raise ValueError(
                        "equilibrated denominator is singular; generalized "
                        "eigenproblem requires a positive definite denominator"
                    ) from exc
                if not isinstance(exc, ArpackNoConvergence):
                    raise
                last_error = exc
        if best is None:
            raise RuntimeError(
                f"largest generalized eigenpair did not converge (n={n}, ncv={ncv_values}); "
                f"partial eigenvalues={getattr(last_error, 'eigenvalues', None)}"
            ) from last_error

        residual, solver_eigenvalue, rayleigh_scaled, y = best
        # Map the equilibrated eigenvector back to the original coordinates.
        x = inv_sqrt_diagonal * y
        result = solver_eigenvalue
        bmin, bmax = None, None

    Ax = residual_matrix_a @ (x if n <= 3 else y)
    Bx = residual_matrix_b @ (x if n <= 3 else y)
    rayleigh = float(np.dot(x if n <= 3 else y, Ax) /
                     np.dot(x if n <= 3 else y, Bx))
    residual = float(np.linalg.norm(Ax - rayleigh * Bx) /
                     max(np.linalg.norm(Ax) + abs(rayleigh)*np.linalg.norm(Bx), 1e-300))
    eigenvalue_disagreement = float(abs(float(result) - rayleigh) /
                                    max(abs(float(result)), abs(rayleigh), 1.0))
    diagnostics = {
        "denominator_lambda_min_estimate": bmin,
        "denominator_lambda_max_estimate": bmax,
        "denominator_condition_estimate": (float(bmax / bmin) if bmin is not None else None),
        "denominator_extreme_eigenvalues_estimated": bmin is not None,
        "denominator_diagonal_min": float(np.min(B.diagonal())),
        "denominator_diagonal_max": float(np.max(B.diagonal())),
        "congruence_scaling_min": scaling_min,
        "congruence_scaling_max": scaling_max,
        "generalized_eigenvalue": rayleigh,
        "solver_reported_eigenvalue": float(result),
        "solver_rayleigh_relative_disagreement": eigenvalue_disagreement,
        "rayleigh_quotient_check": rayleigh,
        "relative_generalized_eigenpair_residual": residual,
        "numerator_relative_symmetry_defect": float(asym_a / scale_a),
        "denominator_relative_symmetry_defect": float(asym_b / scale_b),
    }
    if not np.isfinite(rayleigh) or not np.isfinite(residual):
        raise RuntimeError("largest generalized eigenpair is not finite")
    if residual > 1e-7:
        raise RuntimeError(
            "largest generalized eigenvector failed the equilibrated Rayleigh residual check: "
            f"relative residual={residual:g}, "
            f"solver eigenvalue={float(result):g}, Rayleigh quotient={rayleigh:g}; "
            f"diagonal scaling range=[{scaling_min:g}, {scaling_max:g}]"
        )
    return (rayleigh, diagnostics) if return_diagnostics else rayleigh
