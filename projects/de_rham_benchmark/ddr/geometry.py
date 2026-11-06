"""Cell maps, pullback metrics and quadrature on the reference cube.

Domain map
----------
The physical mesh is the image of the structured reference mesh
``[0,1]^d`` (per-axis ``[0,L_a]`` with ``L_a = 1`` here) under a global
smooth map ``Phi``.  Each cell map is the restriction

    F_K(xi) = Phi(p_K + h * xi),   xi in [0,1]^d,

which has the required form ``F_K(xi) = x_K + A_K xi + r_K(xi)`` with
``A_K = h * D Phi(center_K)`` (secant part) and ``r_K`` the smooth
remainder.  Because ``Phi`` is global, adjacent cells share identical
face parametrisations: the mesh is conforming by construction.

The curvature amplitude is a parameter of ``Phi`` and is therefore
independent of the refinement parameter ``h`` unless the
``amplitude_h`` schedule is used explicitly.

Pullback metric
---------------
On cell K we use ``g_K = DF_K^T G(F_K) DF_K`` where ``G`` is an
optional ambient (physical) metric, default identity.  The Riemannian
volume element on the reference cube is ``sqrt(det g_K) dxi``, which
equals the physical volume element; no extra ``det DF`` factor is
needed.

Quadrature is tensor Gauss-Legendre on [0,1]^d.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial.legendre import leggauss

from .mesh import CubicalMesh


# ---------------------------------------------------------------------- #
# Domain maps
# ---------------------------------------------------------------------- #
class DomainMap:
    """Global diffeomorphism Phi: reference domain -> physical domain.

    spec keys
    ---------
    type       : 'identity' | 'affine' | 'sinusoid'
    matrix     : (d,d) array, affine case (default I)
    offset     : (d,) array, affine case (default 0)
    amplitude  : scalar a, sinusoid case
    amplitude_h: [a0, gamma] -> a = a0 * h_eff**gamma (resolved per mesh)
    freq       : integer m, sinusoid case (default 1)
    direction  : (d,) vector c, sinusoid case (default e1)

    sinusoid:  Phi(x) = x + a * P(x) * c,  P(x) = prod_i sin(m pi x_i).
    P vanishes on the boundary of [0,1]^d, so the domain boundary is fixed.
    """

    def __init__(self, spec, dim):
        self.dim = dim
        self.type = spec.get("type", "identity")
        self.spec = dict(spec)
        if self.type == "affine":
            self.S = np.array(spec.get("matrix", np.eye(dim)), float)
            self.t = np.array(spec.get("offset", np.zeros(dim)), float)
        elif self.type == "sinusoid":
            self.a = float(spec.get("amplitude", 0.0))
            self.m = float(spec.get("freq", 1))
            c = np.array(spec.get("direction",
                                  [1.0] + [0.0] * (dim - 1)), float)
            n = np.linalg.norm(c)
            self.c = c / n if n > 0 else c
        elif self.type == "axis_bump":
            # Phi_i(x) = x_i + a_i sin(pi x_i) sin(pi x_{i+1 mod d})
            # boundary-preserving, genuinely multi-directional curvature
            a = spec.get("amplitudes", spec.get("amplitude", 0.1))
            if np.isscalar(a):
                a = [float(a)] * dim
            self.amp = np.asarray(a, float)
        elif self.type == "identity":
            pass
        else:
            raise ValueError(f"unknown map type {self.type!r}")

    def set_amplitude(self, a):
        self.a = float(a)

    # -- scalar bump P and its gradient ------------------------------- #
    def _P_and_grad(self, X):
        m = self.m
        S = np.sin(m * np.pi * X)          # (..., d)
        C = np.cos(m * np.pi * X)
        P = np.prod(S, axis=-1)            # (...,)
        dP = np.empty_like(X)
        for i in range(self.dim):
            # prod over j != i of sin(m pi x_j)
            others = [j for j in range(self.dim) if j != i]
            Pi = np.prod(S[..., others], axis=-1) if others else np.ones_like(P)
            dP[..., i] = m * np.pi * C[..., i] * Pi
        return P, dP

    def phi(self, X):
        """X: (..., d) reference coords -> (..., d) physical coords."""
        X = np.asarray(X, float)
        if self.type == "identity":
            return X.copy()
        if self.type == "affine":
            return X @ self.S.T + self.t
        if self.type == "sinusoid":
            P, _ = self._P_and_grad(X)
            return X + self.a * P[..., None] * self.c[None, :]
        if self.type == "axis_bump":
            d = self.dim
            S = np.sin(np.pi * X)              # (..., d)
            C = np.cos(np.pi * X)
            nxt = np.roll(S, -1, axis=-1)      # sin(pi x_{i+1})
            phi = X.copy()
            for i in range(d):
                phi[..., i] += self.amp[i] * S[..., i] * nxt[..., i]
            return phi
        raise ValueError(self.type)

    def jac(self, X):
        """D Phi at X: (..., d, d)."""
        X = np.asarray(X, float)
        shp = X.shape[:-1]
        if self.type == "identity":
            return np.broadcast_to(np.eye(self.dim), shp + (self.dim, self.dim)).copy()
        if self.type == "affine":
            return np.broadcast_to(self.S, shp + (self.dim, self.dim)).copy()
        if self.type == "sinusoid":
            _, dP = self._P_and_grad(X)
            J = np.broadcast_to(np.eye(self.dim), shp + (self.dim, self.dim)).copy()
            J += self.a * np.einsum("i,...j->...ij", self.c, dP)
            return J
        if self.type == "axis_bump":
            d = self.dim
            S = np.sin(np.pi * X)
            C = np.cos(np.pi * X)
            nxtS = np.roll(S, -1, axis=-1)     # sin(pi x_{i+1})
            nxtC = np.roll(C, -1, axis=-1)     # cos(pi x_{i+1})
            J = np.broadcast_to(np.eye(self.dim), shp + (self.dim, self.dim)).copy()
            for i in range(d):
                j = (i + 1) % d
                # d Phi_i / d x_i
                J[..., i, i] += self.amp[i] * (np.pi * C[..., i] * nxtS[..., i])
                # d Phi_i / d x_j  (only j = i+1)
                J[..., i, j] += self.amp[i] * (np.pi * S[..., i] * nxtC[..., i])
            return J
        raise ValueError(self.type)


# ---------------------------------------------------------------------- #
# Ambient metric G(x)
# ---------------------------------------------------------------------- #
class AmbientMetric:
    """Ambient metric tensor G(x), SPD d x d.

    spec keys
    ---------
    type        : 'identity' | 'aniso' | 'oscillatory' | 'nonuniform'
    alpha       : scalar or (d,) diagonal entries for 'aniso'
    beta        : oscillation amplitude (<1 keeps SPD), default 0.4
    freq        : scalar f or (d,d) matrix of spatial frequencies
    phase       : (d,) phases, default 0
    """

    def __init__(self, spec, dim):
        self.dim = dim
        self.type = spec.get("type", "identity")
        self.spec = dict(spec)
        if self.type == "aniso":
            a = np.array(spec.get("alpha", 1.0), float)
            self.alpha = np.broadcast_to(a, (dim,)).astype(float).copy()
        elif self.type in ("oscillatory", "nonuniform"):
            self.beta = float(spec.get("beta", 0.4))
            f = np.array(spec.get("freq", 2.0), float)
            self.freq = np.broadcast_to(f, (dim, dim)).astype(float).copy()
            self.phase = np.array(spec.get("phase", np.zeros(dim)), float)
        elif self.type == "identity":
            pass
        else:
            raise ValueError(f"unknown metric type {self.type!r}")

    def G(self, X):
        """X: (..., d) -> (..., d, d) SPD matrices."""
        X = np.asarray(X, float)
        shp = X.shape[:-1]
        if self.type == "identity":
            return np.broadcast_to(np.eye(self.dim),
                                   shp + (self.dim, self.dim)).copy()
        if self.type == "aniso":
            G = np.zeros(shp + (self.dim, self.dim))
            for i in range(self.dim):
                G[..., i, i] = self.alpha[i]
            return G
        # diagonal oscillatory metrics: g_i(x) = 1 + beta_i sin(2 pi f_i . x + phi_i)
        diag = np.ones(shp + (self.dim,))
        for i in range(self.dim):
            arg = 2 * np.pi * (X @ self.freq[i]) + self.phase[i]
            diag[..., i] = 1.0 + self.beta * np.sin(arg)
        np.clip(diag, 1e-3, None, out=diag)
        G = np.zeros(shp + (self.dim, self.dim))
        for i in range(self.dim):
            G[..., i, i] = diag[..., i]
        return G


# ---------------------------------------------------------------------- #
# Pullback geometry on the mesh
# ---------------------------------------------------------------------- #
def _tensor_gauss(n, d):
    t, w = leggauss(n)
    xi = (t + 1.0) / 2.0
    wi = w / 2.0
    grids = np.meshgrid(*([xi] * d), indexing="ij")
    wgrids = np.meshgrid(*([wi] * d), indexing="ij")
    pts = np.stack([g.ravel() for g in grids], axis=-1)      # (n^d, d)
    wts = np.prod(np.stack([g.ravel() for g in wgrids], axis=-1), axis=-1)
    return pts, wts


class PullbackGeometry:
    """Computes vol_g(K), face measures |sigma|_{g,K}, M_k and diagnostics.

    Inner product weights (documented approximation):
        M_k[sigma, sigma] = sum_{K > sigma}
            vol_g(K) / (2^{d-k} |sigma|^2_{g,K})     (k < d)
        M_d[K, K]       = vol_g(K)
    For a flat affine mesh with G = I this reduces exactly to the standard
    discrete-exterior-calculus weights  |sigma*|/|sigma|.
    """

    def __init__(self, mesh: CubicalMesh, map_spec, metric_spec,
                 nq=5, nqf=4):
        self.mesh = mesh
        self.dim = mesh.dim
        self.nq = nq
        self.nqf = nqf
        self.xiq, self.wq = _tensor_gauss(nq, mesh.dim)
        self.hs = np.array(mesh.hs)
        self.cell_lo = [np.array(lo, float) for lo in mesh.cell_lo]
        # lower reference corner of each cell
        self.cell_p = [lo * self.hs for lo in self.cell_lo]

        amp_h = map_spec.get("amplitude_h")
        if amp_h is not None:
            a0, gamma = amp_h
            map_spec = dict(map_spec)
            map_spec["amplitude"] = float(a0) * mesh.h_eff ** float(gamma)
        self.dmap = DomainMap(map_spec, mesh.dim)
        self.dmap_type = map_spec.get("type", "identity")
        self.metric = AmbientMetric(metric_spec, mesh.dim)

        self.vol_g = np.zeros(mesh.nk[mesh.dim])
        self.M = [np.zeros(mesh.nk[k]) for k in range(mesh.dim + 1)]
        self.geo = self._compute()

    # -- helpers -------------------------------------------------------- #
    def _cell_frame(self, cid, xi):
        """Return (DF, g, Y) at local points xi (..., d) of cell cid."""
        p = self.cell_p[cid]
        ref = p + xi * self.hs          # broadcast (..., d)
        Y = self.dmap.phi(ref)
        J = self.dmap.jac(ref)          # (..., d, d), dPhi_a/dx_b
        # DF_{ij} = dF_i/dxi_j = h_j * J_{ij}: scale the last (column) axis
        DF = J * self.hs
        G = self.metric.G(Y)
        # g = DF^T G DF :  g_ab = sum_ij DF_{ia} G_{ij} DF_{jb}
        g = np.einsum("...ia,...ij,...jb->...ab", DF, G, DF)
        return DF, g, Y, J

    def _compute(self):
        m = self.mesh
        d = self.dim
        stats = {
            "min_det_jac": np.inf, "max_det_jac": -np.inf,
            "min_sv_jac": np.inf, "max_sv_jac": 0.0,
            "min_sqrt_det_g": np.inf, "max_cond_g": 0.0,
            "bad_jac_cells": 0,
        }
        all_detJ, all_sv = [], []

        for cid in range(m.nk[d]):
            DF, g, Y, J = self._cell_frame(cid, self.xiq)
            # --- cell volume ---
            detg = np.linalg.det(g)
            rho = np.sqrt(np.maximum(detg, 0.0))
            vol = float(np.sum(self.wq * rho))
            self.vol_g[cid] = vol
            self.M[d][cid] = vol
            stats["min_sqrt_det_g"] = min(stats["min_sqrt_det_g"],
                                          float(np.min(rho)))
            # metric condition number
            try:
                cg = np.linalg.cond(g)
                stats["max_cond_g"] = max(stats["max_cond_g"], float(np.max(cg)))
            except np.linalg.LinAlgError:
                stats["max_cond_g"] = np.inf
            # --- Jacobian diagnostics (dimensionless J = D Phi) ---
            detJ = np.linalg.det(J)
            sv = np.linalg.svd(J, compute_uv=False)
            stats["min_det_jac"] = min(stats["min_det_jac"], float(np.min(detJ)))
            stats["max_det_jac"] = max(stats["max_det_jac"], float(np.max(detJ)))
            stats["min_sv_jac"] = min(stats["min_sv_jac"], float(np.min(sv)))
            stats["max_sv_jac"] = max(stats["max_sv_jac"], float(np.max(sv)))
            all_detJ.append(detJ)
            all_sv.append(sv)
            if np.any(detJ <= 0):
                stats["bad_jac_cells"] += 1

            # --- lower-order face measures and M_k contributions ---
            for k in range(d):
                denom = 2.0 ** (d - k)
                for fid in m.cell_to_faces[cid][k]:
                    f = m.faces[k][fid]
                    if k == 0:
                        meas = 1.0
                    else:
                        meas = self._face_measure(cid, f)
                    if meas <= 1e-14:
                        stats["bad_jac_cells"] += 1
                        meas = 1e-14
                    self.M[k][fid] += vol / (denom * meas * meas)

        stats["min_det_jac"] = float(stats["min_det_jac"])
        stats["max_det_jac"] = float(stats["max_det_jac"])
        stats["min_sv_jac"] = float(stats["min_sv_jac"])
        stats["max_sv_jac"] = float(stats["max_sv_jac"])
        stats["min_sqrt_det_g"] = float(stats["min_sqrt_det_g"])
        stats["max_cond_g"] = float(stats["max_cond_g"])
        stats["total_volume"] = float(np.sum(self.vol_g))
        stats["n_cells"] = int(m.nk[d])
        return stats

    def _face_measure(self, cid, f):
        """k-volume |sigma|_{g,K} of face f measured in cell cid's metric."""
        k = f.k
        m = self.mesh
        # local fixed coordinates along non-varying axes
        ci = self.cell_lo[cid]
        fixed_map = dict(f.fixed)
        xi_fixed = {}
        for ax, line in fixed_map.items():
            xi_fixed[ax] = float(line) - float(ci[ax])  # 0 or 1
        # quadrature points on the k-face
        xiqf, wqf = _tensor_gauss(self.nqf, k)
        npts = xiqf.shape[0]
        xi = np.empty((npts, self.dim))
        vary = list(f.vary)
        for j, ax in enumerate(vary):
            xi[:, ax] = xiqf[:, j]
        for ax, val in xi_fixed.items():
            xi[:, ax] = val
        _, g, _, _ = self._cell_frame(cid, xi)
        # g_K = DF^T G DF is the pullback metric in reference coordinates;
        # the k-volume element on the coordinate face is sqrt(det g_K|_S).
        Gram = g[:, vary, :][:, :, vary]          # (npts, k, k)
        detG = np.linalg.det(Gram)
        el = np.sqrt(np.maximum(detG, 0.0))
        return float(np.sum(wqf * el))
