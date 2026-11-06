"""Library of smooth test differential forms on the physical domain.

A k-form is represented as a sum of terms ``f(x) dx^I`` where ``f`` is a
scalar field with analytic value and gradient.  Component vectors follow
``kforms.combos`` ordering.

Scalar fields are sums of
  * monomials   c * prod_i x_i^{p_i}
  * trig terms  a * sin(w . x + phi)   or   a * cos(w . x + phi)

Exterior derivative ``d`` is exact (first derivatives only).
Codifferential ``delta`` uses the analytic formula

    (delta u)_K = -(1/rho) sum_{a,b} d_a( rho g^{ab} u_{bK} ),

where g is the ambient metric G(x), rho = sqrt(det G), and u_{bK} is the
component of u on the ordered multi-index (b, K) with the insertion sign.
Derivatives of u are analytic where available; second derivatives needed
by ``DirectionalScalar``/``ScaledField`` gradients and derivatives of
``rho*g^{ab}`` use central differences (documented semi-analytic steps).
"""
from __future__ import annotations

import numpy as np

from .kforms import combos, combo_index, insert_sorted

_FD_EPS = 1e-6


def _fd_grad(func, x, dim):
    """Central-difference gradient of scalar func (...,)->(...,) at x (...,d)."""
    x = np.asarray(x, float)
    shp = x.shape[:-1]
    g = np.empty(shp + (dim,))
    for a in range(dim):
        xa = x.copy(); xa[..., a] += _FD_EPS
        xb = x.copy(); xb[..., a] -= _FD_EPS
        g[..., a] = (func(xa) - func(xb)) / (2 * _FD_EPS)
    return g


# ---------------------------------------------------------------------- #
# Scalar fields
# ---------------------------------------------------------------------- #
class ScalarField:
    """f(x) = sum of monomial / sin / cos terms (analytic value+grad)."""

    def __init__(self, dim, terms):
        self.dim = dim
        self.terms = terms

    @staticmethod
    def monomial(dim, powers, coeff=1.0):
        return ScalarField(dim, [{"kind": "monomial",
                                  "powers": tuple(int(p) for p in powers),
                                  "coeff": float(coeff)}])

    @staticmethod
    def trig(dim, amp=1.0, freq=None, phase=0.0, kind="sin"):
        if freq is None:
            freq = [1.0] * dim
        return ScalarField(dim, [{"kind": kind, "amp": float(amp),
                                  "freq": np.asarray(freq, float),
                                  "phase": float(phase)}])

    @staticmethod
    def bump(dim):
        """p(x_1)...p(x_d) with p(t) = t^2 (1-t)^2.

        Vanishes to second order on dOmega together with its first
        derivatives' boundary traces relevant for codifferential tests.
        """
        # p(t) = t^2 - 2 t^3 + t^4  ->  coeffs {2:1, 3:-2, 4:1}
        pc = {2: 1.0, 3: -2.0, 4: 1.0}
        terms = []
        # iterate over all choices of power per axis
        def rec(axis, powers, coeff):
            if axis == dim:
                terms.append({"kind": "monomial",
                              "powers": tuple(powers), "coeff": coeff})
                return
            for p, c in pc.items():
                rec(axis + 1, powers + [p], coeff * c)
        rec(0, [], 1.0)
        return ScalarField(dim, terms)

    @staticmethod
    def mixed(dim, seed=0):
        """Deterministic mixed test field (monomial + two trig modes)."""
        rng = np.random.default_rng(seed)
        terms = [{"kind": "monomial",
                  "powers": tuple(int(rng.integers(0, 3)) for _ in range(dim)),
                  "coeff": float(rng.uniform(0.5, 1.5))}]
        for i, kind in enumerate(("sin", "cos")):
            terms.append({"kind": kind,
                          "amp": float(rng.uniform(0.4, 1.0)),
                          "freq": rng.uniform(0.5, 2.5, size=dim),
                          "phase": float(rng.uniform(0, np.pi))})
        return ScalarField(dim, terms)

    def __call__(self, x):
        x = np.asarray(x, float)
        shp = x.shape[:-1]
        f = np.zeros(shp)
        for t in self.terms:
            if t["kind"] == "monomial":
                val = np.full(shp, t["coeff"])
                for l in range(self.dim):
                    val = val * np.power(x[..., l], t["powers"][l])
                f = f + val
            else:
                arg = x @ t["freq"] + t["phase"]
                f = f + t["amp"] * (np.sin(arg) if t["kind"] == "sin"
                                    else np.cos(arg))
        return f

    def grad(self, x):
        x = np.asarray(x, float)
        shp = x.shape[:-1]
        g = np.zeros(shp + (self.dim,))
        for t in self.terms:
            if t["kind"] == "monomial":
                pw = t["powers"]
                for j in range(self.dim):
                    if pw[j] == 0:
                        continue
                    term = np.full(shp, t["coeff"] * pw[j])
                    for l in range(self.dim):
                        p = pw[l] - (1 if l == j else 0)
                        term = term * np.power(x[..., l], p)
                    g[..., j] += term
            else:
                arg = x @ t["freq"] + t["phase"]
                if t["kind"] == "sin":
                    g += (t["amp"] * np.cos(arg))[..., None] * t["freq"]
                else:
                    g -= (t["amp"] * np.sin(arg))[..., None] * t["freq"]
        return g


class _PartialScalar:
    """Scalar field equal to d_j f (used for exact gradients)."""

    def __init__(self, f, j):
        self.f = f
        self.j = j
        self.dim = f.dim

    def __call__(self, x):
        return self.f.grad(x)[..., self.j]

    def grad(self, x):
        return _fd_grad(self, x, self.dim)


class _DerivativeScalar:
    """Scalar field equal to sign * d_j f (for du terms)."""

    def __init__(self, f, j, sign):
        self.f = f
        self.j = j
        self.sign = sign
        self.dim = f.dim

    def __call__(self, x):
        return self.sign * self.f.grad(x)[..., self.j]

    def grad(self, x):
        return _fd_grad(self, x, self.dim)


# ---------------------------------------------------------------------- #
# Differential forms
# ---------------------------------------------------------------------- #
class Form:
    """u = sum_a f_a(x) dx^{I_a}; I_a sorted tuples of size k."""

    def __init__(self, dim, k, terms):
        self.dim = dim
        self.k = k
        self.terms = terms  # list of (scalar-field-like, I tuple)
        self._idx = combo_index(dim, k)

    @staticmethod
    def exact_gradient(dim, f):
        """df for scalar field f -> 1-form."""
        return Form(dim, 1, [(_PartialScalar(f, j), (j,))
                             for j in range(dim)])

    @staticmethod
    def from_scalar_top(dim, f):
        """f dx^0 ^ ... ^ dx^{d-1} (top-degree form)."""
        return Form(dim, dim, [(f, tuple(range(dim)))])

    @staticmethod
    def single(dim, k, f, I):
        return Form(dim, k, [(f, tuple(I))])

    def eval(self, x):
        """x (..., d) -> components (..., ncomp_k)."""
        x = np.asarray(x, float)
        shp = x.shape[:-1]
        out = np.zeros(shp + (len(combos(self.dim, self.k)),))
        for f, I in self.terms:
            out[..., self._idx[I]] += f(x)
        return out

    def component_grads(self, x):
        """d_a u_I for all components -> (..., ncomp_k, d)."""
        x = np.asarray(x, float)
        shp = x.shape[:-1]
        ncomp = len(combos(self.dim, self.k))
        out = np.zeros(shp + (ncomp, self.dim))
        for f, I in self.terms:
            out[..., self._idx[I], :] += f.grad(x)
        return out

    def d(self):
        """Return the (k+1)-form du (exact, analytic first derivatives)."""
        new_terms = []
        for f, I in self.terms:
            for j in range(self.dim):
                U, s = insert_sorted(j, I)
                if U is None:
                    continue
                new_terms.append((_DerivativeScalar(f, j, s), U))
        return Form(self.dim, self.k + 1, new_terms)

    def delta(self, x, metric):
        """Codifferential at x (..., d) under ambient `metric`.

        (delta u)_K = -(1/rho) sum_{a,b} d_a( rho g^{ab} u_{bK} )
        with u_{bK} = sign_insert(b,K) * u_{insert(b,K)}.
        Metric-factor derivatives use central differences.
        """
        if self.k == 0:
            shp = np.asarray(x).shape[:-1]
            return np.zeros(shp + (0,))
        d, k = self.dim, self.k
        x = np.asarray(x, float)
        shp = x.shape[:-1]
        G = metric.G(x)
        rho = np.sqrt(np.linalg.det(G))
        ginv = np.linalg.inv(G)
        # dH[..., a, b, c] = d_c (rho g^{ab})
        dH = np.empty(shp + (d, d, d))
        for c in range(d):
            xp = x.copy(); xp[..., c] += _FD_EPS
            xm = x.copy(); xm[..., c] -= _FD_EPS
            Gp, Gm = metric.G(xp), metric.G(xm)
            Hp = np.sqrt(np.linalg.det(Gp))[..., None, None] \
                * np.linalg.inv(Gp)
            Hm = np.sqrt(np.linalg.det(Gm))[..., None, None] \
                * np.linalg.inv(Gm)
            dH[..., :, :, c] = (Hp - Hm) / (2 * _FD_EPS)
        u = self.eval(x)
        du = self.component_grads(x)
        Ks = combos(d, k - 1)
        idx_k = combo_index(d, k)
        out = np.zeros(shp + (len(Ks),))
        Hab = rho[..., None, None] * ginv                    # (..., a, b)
        for ic, K in enumerate(Ks):
            acc = np.zeros(shp)
            for a in range(d):
                for b in range(d):
                    U, s = insert_sorted(b, K)
                    if U is None:
                        continue
                    jU = idx_k[U]
                    u_bK = s * u[..., jU]
                    du_bK = s * du[..., jU, a]
                    acc = acc - (dH[..., a, b, a] * u_bK
                                 + Hab[..., a, b] * du_bK)
            out[..., ic] = acc / rho
        return out
