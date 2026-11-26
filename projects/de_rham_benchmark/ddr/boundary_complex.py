"""Relative cubical de Rham complex (essential tangential trace).

A relative k-cochain has zero degrees of freedom on every k-face
contained in the boundary.  For the tensor-product cubical mesh this is
exactly the tangential trace condition: a k-face lies in the boundary
iff at least one of its fixed coordinates is an outer grid line.

The construction is deliberately separate from the full/absolute
complex.  It returns index maps, restricted incidence matrices and
principal submatrices of the already assembled consistent FEEC masses.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp


@dataclass
class RelativeComplex:
    """Restricted relative complex and maps back to full cochain indices."""

    keep: list[np.ndarray]
    boundary: list[np.ndarray]
    dmat: list[sp.csr_matrix]
    masses: list[sp.csr_matrix] | None

    @property
    def dimensions(self) -> list[int]:
        return [int(len(idx)) for idx in self.keep]


def relative_boundary_mask(mesh, k: int) -> np.ndarray:
    """Mark k-faces contained in the boundary (relative DOFs are zero)."""
    if not 0 <= k <= mesh.dim:
        raise ValueError("form degree outside mesh dimension")
    mask = np.zeros(mesh.nk[k], dtype=bool)
    if k == mesh.dim:
        return mask
    for fid, face in enumerate(mesh.faces[k]):
        for axis, line in face.fixed:
            if line == 0 or line == mesh.Ns[axis]:
                mask[fid] = True
                break
    return mask


def build_relative_complex(mesh, masses=None) -> RelativeComplex:
    """Build C^k( mesh, boundary ) with consistent restricted FEEC masses.

    The relative differential is the restriction of the full incidence
    matrix to retained rows and columns.  The omitted boundary rows must
    vanish on retained columns; this is checked rather than assumed.
    """
    boundary = [relative_boundary_mask(mesh, k)
                for k in range(mesh.dim + 1)]
    keep = [np.flatnonzero(~mask) for mask in boundary]
    drel = []
    for k, D in enumerate(mesh.dmat):
        # Relative cochains must map to cochains whose boundary trace is
        # still zero.  Boundary rows therefore vanish on retained columns.
        omitted_rows = np.flatnonzero(boundary[k + 1])
        if len(omitted_rows):
            leak = D[omitted_rows, :][:, keep[k]]
            if leak.nnz and np.max(np.abs(leak.data)) != 0:
                raise ValueError(
                    f"relative subspace is not a subcomplex at degree {k}")
        drel.append(D[keep[k + 1], :][:, keep[k]].tocsr())

    if masses is None:
        mrel = None
    else:
        if len(masses) != mesh.dim + 1:
            raise ValueError("one mass matrix is required per form degree")
        mrel = []
        for k, M in enumerate(masses):
            if M.shape != (mesh.nk[k], mesh.nk[k]):
                raise ValueError(f"mass matrix shape mismatch at degree {k}")
            mrel.append(M.tocsr()[keep[k], :][:, keep[k]].tocsr())

    return RelativeComplex(keep=keep, boundary=boundary,
                           dmat=drel, masses=mrel)


def relative_betti_numbers(complex_: RelativeComplex) -> tuple[list[int], list[int]]:
    """Compute relative Betti numbers and differential ranks (audit sizes)."""
    dim = len(complex_.keep) - 1
    ranks = [0] * (dim + 2)
    for k, D in enumerate(complex_.dmat):
        ranks[k + 1] = int(np.linalg.matrix_rank(D.toarray(), tol=1e-10))
    beta = [complex_.dimensions[k] - ranks[k] - ranks[k + 1]
            for k in range(dim + 1)]
    return beta, ranks[:dim + 1]
