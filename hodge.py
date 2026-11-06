"""Discrete inner products, adjoints, Hodge Laplacian and spectral analysis.

Conventions
-----------
C^k = R^{n_k} are the cubical k-cochains.  d_k : C^k -> C^{k+1} is the
incidence (coboundary) matrix from mesh.dmat.

The diagonal Hodge inner product is <a,b>_{M_k} = a^T M_k b with M_k
assembled by PullbackGeometry (dual-volume weights with pullback metric).

Adjoint (codifferential)  delta_k : C^k -> C^{k-1}:
    delta_k = M_{k-1}^{-1} d_{k-1}^T M_k

Hodge Laplacian on k-cochains:
    Delta_k = d_{k-1} delta_k + delta_{k+1} d_k
            = d_{k-1} M_{k-1}^{-1} d_{k-1}^T M_k + M_k^{-1} d_k^T M_{k+1} d_k

It is self-adjoint w.r.t. M_k, i.e. B_k := M_k Delta_k is symmetric.
Eigenvalues are computed from the generalized problem
    B_k x = lambda M_k x .

No boundary conditions are imposed: this is the algebraic Hodge
Laplacian of the full cubical complex (absolute-type).  On the
contractible domain [0,1]^d the expected Betti numbers are
(1, 0, ..., 0), hence dim ker Delta_k should equal beta_k.
"""
from __future__ import annotations

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import scipy.linalg as sla


# ---------------------------------------------------------------------- #
def hodge_matrices(mesh, M):
    """Return dict with dmat, M, Minv, delta, B (= M Delta), per level."""
    d = mesh.dim
    Minv = [1.0 / m for m in M]
    out = {"d": mesh.dmat, "M": M, "Minv": Minv,
           "delta": [None] * (d + 1), "B": [None] * (d + 1)}
    Dm = [sp.diags(m) for m in M]
    for k in range(d + 1):
        # delta_k : C^k -> C^{k-1}
        if k > 0:
            dkm1 = mesh.dmat[k - 1]                    # (n_k, n_{k-1})
            out["delta"][k] = (sp.diags(Minv[k - 1])
                               @ dkm1.T @ Dm[k]).tocsr()
        # B_k = M_k Delta_k
        terms = []
        if k > 0:
            dkm1 = mesh.dmat[k - 1]
            # M_k d_{k-1} Minv_{k-1} d_{k-1}^T M_k
            terms.append(Dm[k] @ dkm1 @ sp.diags(Minv[k - 1])
                         @ dkm1.T @ Dm[k])
        if k < d:
            dk = mesh.dmat[k]                          # (n_{k+1}, n_k)
            terms.append(dk.T @ Dm[k + 1] @ dk)
        B = terms[0]
        for t in terms[1:]:
            B = B + t
        out["B"][k] = B.tocsr()
    return out


def algebraic_residuals(mesh, M, H, rng=None):
    """Residuals for all algebraic identities (exact in exact arithmetic)."""
    d = mesh.dim
    res = {}
    rng = rng or np.random.default_rng(0)
    # 1) d_{k+1} d_k = 0  (k = 0..d-2)
    dd = []
    for k in range(d - 1):
        P = (mesh.dmat[k + 1] @ mesh.dmat[k]).toarray()
        dd.append(float(np.max(np.abs(P))))
    res["max_abs_dd_by_level"] = dd
    res["max_abs_dd"] = max(dd) if dd else 0.0

    # 2) B_k symmetry: B = M Delta should be symmetric
    bsym = []
    for k in range(d + 1):
        B = H["B"][k]
        D = (B - B.T).toarray()
        bsym.append(float(np.max(np.abs(D))))
    res["max_abs_B_minus_BT"] = max(bsym)

    # 3) adjointness <d_{k-1} a, b>_{M_k} = <a, delta_k b>_{M_{k-1}}
    adj = []
    for k in range(1, d + 1):
        nkm1, nk = mesh.nk[k - 1], mesh.nk[k]
        a = rng.standard_normal(nkm1)
        b = rng.standard_normal(nk)
        dkm1 = mesh.dmat[k - 1]
        lhs = float((dkm1 @ a) @ (M[k] * b))
        dk_b = H["delta"][k] @ b
        rhs = float(a @ (M[k - 1] * dk_b))
        adj.append(abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs)))
    res["max_rel_adjoint"] = max(adj) if adj else 0.0

    # 4) self-adjointness of Delta_k w.r.t. M_k on random vectors:
    #    <Delta a, b>_M = <a, Delta b>_M  <=>  (B a).b = a.(B b)
    sa = []
    for k in range(d + 1):
        nk = mesh.nk[k]
        a = rng.standard_normal(nk)
        b = rng.standard_normal(nk)
        Ba = H["B"][k] @ a
        lhs = float(Ba @ b)
        rhs = float(a @ (H["B"][k] @ b))
        sa.append(abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs)))
    res["max_rel_selfadjoint"] = max(sa)

    # 5) partition of unity: sum_v M0[v] = total volume = sum_K M_d[K]
    res["partition_of_unity_err"] = abs(float(np.sum(M[0]))
                                        - float(np.sum(M[d])))
    res["sum_M0"] = float(np.sum(M[0]))
    res["sum_Md"] = float(np.sum(M[d]))
    return res


def betti_numbers(mesh):
    """beta_k = n_k - rank(d_{k-1}) - rank(d_k) via dense SVD (moderate n).

    rk[j] = rank of d_{j-1} : C^{j-1} -> C^j  (rk[0] = rk[d] boundary = 0).
    """
    d = mesh.dim
    rk = [0] * (d + 2)
    for k in range(d):
        A = mesh.dmat[k].toarray().astype(float)
        rk[k + 1] = int(np.linalg.matrix_rank(A, tol=1e-10))
    beta = [mesh.nk[k] - rk[k] - rk[k + 1] for k in range(d + 1)]
    return beta, rk[: d + 1]


# ---------------------------------------------------------------------- #
def spectrum(mesh, H, M, k_eig=12, k_max=4, tol_rel=1e-7, dense_limit=2500):
    """Eigen-analysis of B_k x = lambda M_k x for every level k."""
    d = mesh.dim
    out = {}
    for k in range(d + 1):
        B = H["B"][k].tocsr()
        n = mesh.nk[k]
        Mk = sp.diags(M[k])
        keig = min(k_eig, max(2, n - 2))
        if n <= dense_limit:
            try:
                wv, V = sla.eigh(B.toarray(), np.diag(M[k]))
                order = np.argsort(wv)
                small = wv[order[:keig]]
                large = wv[order[-k_max:]][::-1] if n > k_max else wv[order][::-1]
                resid = []
                for idx in order[:min(keig, n)]:
                    x = V[:, idx]
                    r = B @ x - wv[idx] * (M[k] * x)
                    resid.append(float(np.linalg.norm(r)
                                        / max(1e-300, np.linalg.norm(x))))
                max_eig_resid = max(resid) if resid else 0.0
            except sla.LinAlgError:
                small = np.array([]); large = np.array([])
                max_eig_resid = np.nan
        else:
            try:
                w_small, _ = spla.eigsh(B, k=keig, M=Mk, which="SA",
                                        tol=1e-10, maxiter=5000)
                small = np.sort(w_small)
                kL = min(k_max, n - keig - 1)
                w_large, _ = (spla.eigsh(B, k=kL, M=Mk, which="LA",
                                         tol=1e-8, maxiter=5000)
                              if kL > 0 else (np.array([]), None))
                large = np.sort(w_large)[::-1] if len(w_large) else np.array([])
                max_eig_resid = np.nan
            except Exception:
                small = np.array([]); large = np.array([])
                max_eig_resid = np.nan
        # scale for kernel tolerance: largest |eigenvalue| seen
        scale = max(float(np.max(np.abs(large))) if len(large) else 0.0,
                    float(np.max(np.abs(small))) if len(small) else 0.0, 1e-300)
        tol = tol_rel * scale
        kernel_num = int(np.sum(small < tol)) if len(small) else -1
        pos = small[small > tol] if len(small) else np.array([])
        lam_min_pos = float(np.min(pos)) if len(pos) else np.nan
        lam_max = float(np.max(large)) if len(large) else np.nan
        cond_eff = (lam_max / lam_min_pos) if (lam_min_pos == lam_min_pos
                                             and lam_min_pos > 0) else np.inf
        out[k] = {
            "eigs_small": [float(x) for x in small],
            "eigs_large": [float(x) for x in large],
            "kernel_num": kernel_num,
            "lambda_min_pos": lam_min_pos,
            "lambda_max": lam_max,
            "cond_effective": float(cond_eff),
            "max_eig_resid": max_eig_resid,
            "n": int(n),
        }
    return out


def inner_product_stats(M):
    stats = []
    for k, m in enumerate(M):
        m = np.asarray(m, float)
        stats.append({
            "k": k,
            "n": int(m.size),
            "min": float(np.min(m)),
            "max": float(np.max(m)),
            "cond": float(np.max(m) / np.min(m)) if np.min(m) > 0 else np.inf,
        })
    return stats
