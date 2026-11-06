"""Structured cubical mesh and its oriented cubical cochain complex.

The mesh is a Cartesian product of 1D interval complexes on [0, L]^d.
A k-face is described by
  * ``vary``  : sorted tuple of axes along which the face extends,
  * ``fixed`` : tuple of (axis, grid_line) for the remaining axes,
  * ``lo``    : tuple of lower cell indices along the ``vary`` axes.

The boundary/coboundary incidence uses the standard cubical boundary
sign  (-1)^(pos+1) * (2s-1)  where ``pos`` is the position of the removed
direction inside ``vary`` and ``s in {0,1}`` selects the lower/upper facet.
This is the cellular boundary of the cubical complex, so d_{k+1} d_k = 0
holds exactly; the residual is verified numerically in hodge.py.
"""
from __future__ import annotations

from itertools import combinations, product

import numpy as np
import scipy.sparse as sp


class Face:
    __slots__ = ("id", "k", "vary", "fixed", "lo", "verts")

    def __init__(self, fid, k, vary, fixed, lo, verts):
        self.id = fid
        self.k = k
        self.vary = vary
        self.fixed = fixed
        self.lo = lo
        self.verts = verts


class CubicalMesh:
    """Structured cubical mesh on [0, L]^d with N_i intervals per axis."""

    def __init__(self, N, dim, L=1.0):
        self.dim = int(dim)
        if np.isscalar(N):
            self.Ns = (int(N),) * self.dim
        else:
            self.Ns = tuple(int(n) for n in N)
        assert len(self.Ns) == self.dim
        self.L = float(L)
        self.hs = tuple(self.L / n for n in self.Ns)
        self.h_eff = min(self.hs)

        # vertex linear index strides (axis 0 fastest)
        strides = []
        s = 1
        for n in self.Ns:
            strides.append(s)
            s *= n + 1
        self.vstride = tuple(strides)
        self.nv = s

        self._build_faces()
        self._build_coboundary()
        self._build_cofaces()

    # ------------------------------------------------------------------ #
    def _vertex_index(self, coord):
        idx = 0
        for a in range(self.dim):
            idx += int(coord[a]) * self.vstride[a]
        return idx

    def _build_faces(self):
        d = self.dim
        self.faces = [[] for _ in range(d + 1)]
        self.key2id = {}
        for k in range(d + 1):
            for vary in combinations(range(d), k):
                nonvary = tuple(a for a in range(d) if a not in vary)
                line_ranges = [range(self.Ns[a] + 1) for a in nonvary]
                lo_ranges = [range(self.Ns[a]) for a in vary]
                for fl in product(*line_ranges):
                    fixed = tuple(sorted(zip(nonvary, fl)))
                    for lo in product(*lo_ranges):
                        verts = []
                        for bits in product((0, 1), repeat=k):
                            coord = [0] * d
                            for ax, ln in fixed:
                                coord[ax] = ln
                            for i, ax in enumerate(vary):
                                coord[ax] = lo[i] + bits[i]
                            verts.append(self._vertex_index(coord))
                        fid = len(self.faces[k])
                        f = Face(fid, k, vary, fixed, lo,
                                 tuple(sorted(verts)))
                        self.faces[k].append(f)
                        self.key2id[(k, vary, fixed, lo)] = fid
        self.nk = [len(self.faces[k]) for k in range(d + 1)]
        # cell lower corners (multi-index) for each d-face (= cell)
        self.cell_lo = [f.lo for f in self.faces[d]]

    def _facet_key(self, tau, pos, s):
        """Key of the facet of (k+1)-face tau obtained by fixing direction
        tau.vary[pos] at side s (0=lower, 1=upper)."""
        level = tau.k - 1
        c = tau.vary[pos]
        vary2 = tau.vary[:pos] + tau.vary[pos + 1:]
        fixed2 = tuple(sorted(tau.fixed + ((c, tau.lo[pos] + s),)))
        lo2 = tau.lo[:pos] + tau.lo[pos + 1:]
        return (level, vary2, fixed2, lo2)

    def _build_coboundary(self):
        """d[k] : C^k -> C^{k+1}, shape (n_{k+1}, n_k), entry [tau, sigma]
        = coefficient of sigma in the cubical boundary of tau."""
        d = self.dim
        self.dmat = []
        for k in range(d):
            rows, cols, vals = [], [], []
            for tau in self.faces[k + 1]:
                for pos, c in enumerate(tau.vary):
                    for s in (0, 1):
                        key = self._facet_key(tau, pos, s)
                        sid = self.key2id[key]
                        coeff = ((-1) ** (pos + 1)) * (1 if s == 1 else -1)
                        rows.append(tau.id)
                        cols.append(sid)
                        vals.append(coeff)
            self.dmat.append(
                sp.csr_matrix(
                    (vals, (rows, cols)),
                    shape=(self.nk[k + 1], self.nk[k]),
                )
            )

    def _build_cofaces(self):
        """For every k-face (k < d) list the d-cells containing it.

        A k-face spans the full cell width along its ``vary`` axes, so its
        cell index there is ``lo``; along each fixed axis the cell index is
        either ``line-1`` or ``line``.
        """
        d = self.dim
        self.cells_of_face = [
            [[] for _ in range(self.nk[k])] for k in range(d)
        ]
        cell_key = lambda ci: (d, tuple(range(d)), (), tuple(ci))
        for k in range(d):
            for f in self.faces[k]:
                per_axis = []
                fixed_map = dict(f.fixed)
                for a in range(d):
                    if a in f.vary:
                        i = f.vary.index(a)
                        per_axis.append([f.lo[i]])
                    else:
                        line = fixed_map[a]
                        per_axis.append(
                            [c for c in (line - 1, line)
                             if 0 <= c < self.Ns[a]]
                        )
                cells = []
                for ci in product(*per_axis):
                    cells.append(self.key2id[cell_key(ci)])
                self.cells_of_face[k][f.id] = cells

        # inverse: cell id -> per-level list of face ids
        self.cell_to_faces = [
            [[] for _ in range(d)] for _ in range(self.nk[d])
        ]
        for k in range(d):
            for fid, cells in enumerate(self.cells_of_face[k]):
                for cid in cells:
                    self.cell_to_faces[cid][k].append(fid)

    # ------------------------------------------------------------------ #
    @property
    def euler_characteristic(self):
        return sum((-1) ** k * self.nk[k] for k in range(self.dim + 1))
