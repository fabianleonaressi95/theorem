"""Algebra of differential k-forms on cubical cells.

Conventions
-----------
A k-form u on the physical domain [0,1]^d (or its image) is stored as a
vector of components ``u_I`` indexed by sorted tuples ``I`` of size k,
meaning ``u = sum_I u_I dx^{i1} ^ ... ^ dx^{ik}`` with ``i1 < ... < ik``.
Component ordering is ``itertools.combinations(range(d), k)``.

The FEEC degrees of freedom used by ``feec_mass.assemble_consistent_masses``
are integrals of u over oriented cubical k-faces; the local basis form
attached to a face with varying axes ``I`` is ``phi_face(xi) dxi^I``.
"""
from __future__ import annotations

from itertools import combinations

import numpy as np


def combos(d, k):
    return list(combinations(range(d), k))


def combo_index(d, k):
    return {I: j for j, I in enumerate(combos(d, k))}


def sign_insert(j, I):
    """Sign of dx^j ^ dx^I rewritten as dx^{sort(j u I)}.

    Equals (-1)^{#{i in I : i < j}}.
    """
    return -1 if sum(1 for i in I if i < j) % 2 else 1


def insert_sorted(j, I):
    """Return (U, sign) with U = sorted tuple of {j} u I."""
    if j in I:
        return None, 0
    U = tuple(sorted(I + (j,)))
    return U, sign_insert(j, I)


# ---------------------------------------------------------------------- #
# Minors and pullback of k-forms
# ---------------------------------------------------------------------- #
def subdet(A, rows, cols):
    """det of A[..., rows][:, :, cols] for batched A (..., d, d)."""
    return np.linalg.det(A[..., list(rows), :][..., :, list(cols)])


def pullback_components(u_comps, DF, d, k):
    """Pull a k-form back through F: u_comps (..., ncomp) -> (..., ncomp).

    If u = sum_J u_J dx^J on the physical side and DF = dF/dxi, then
    (F* u)_I = sum_J u_J det(DF[J, I])  where det(DF[J,I]) is the minor
    with row set J and column set I.
    """
    Is = combos(d, k)
    ncomp = len(Is)
    out = np.zeros(u_comps.shape[:-1] + (ncomp,), dtype=float)
    for a, I in enumerate(Is):
        acc = np.zeros(u_comps.shape[:-1], dtype=float)
        for b, J in enumerate(Is):
            minor = subdet(DF, J, I)          # (...,)
            acc = acc + u_comps[..., b] * minor
        out[..., a] = acc
    return out


def minor_matrix(inv_g, components):
    """(Lambda^k g^{-1})_{I,J} = det(g^{-1}[I,J]) at each point.

    inv_g: (..., d, d); components: list of k-tuples.
    Returns (..., ncomp, ncomp).
    """
    nq = inv_g.shape[0] if inv_g.ndim >= 3 else 1
    shp = inv_g.shape[:-2]
    ncomp = len(components)
    W = np.empty(shp + (ncomp, ncomp), dtype=float)
    if not components:
        W[..., 0, 0] = 1.0
        return W
    for a, I in enumerate(components):
        for b, J in enumerate(components):
            W[..., a, b] = np.linalg.det(
                inv_g[..., list(I), :][..., :, list(J)])
    return W


def pointwise_norm2_g(comps, g, d, k):
    """|omega|^2_g for k-form components comps (..., ncomp) under metric g.

    |omega|^2 = sum_{I,J} omega_I omega_J det(g^{-1}[I,J]).
    """
    inv_g = np.linalg.inv(g)
    W = minor_matrix(inv_g, combos(d, k))
    return np.einsum("...i,...ij,...j->...", comps, W, comps)


def reference_volume_density(g):
    """sqrt(det g) for batched SPD matrices g (..., d, d)."""
    return np.sqrt(np.linalg.det(g))
