"""Consistent tensor-product cubical FEEC mass matrices.

Lowest-order tensor-product de Rham spaces: Q1 vertices, edge/face
tensor-product forms, and cellwise top forms. Degrees of freedom are
oriented integrals over cubical k-faces.
"""
from __future__ import annotations
from itertools import combinations
import numpy as np
import scipy.sparse as sp


def _minor_matrix(inv_g, components):
    """Exterior-power metric (Lambda^k g^{-1})_{I,J}."""
    nq = inv_g.shape[0]
    ncomp = len(components)
    W = np.empty((nq, ncomp, ncomp), dtype=float)
    if not components:
        W[:, 0, 0] = 1.0
        return W
    for a, I in enumerate(components):
        for b, J in enumerate(components):
            W[:, a, b] = np.linalg.det(inv_g[:, I, :][:, :, J])
    return W


def assemble_consistent_masses(mesh, geometry):
    """Assemble sparse consistent Gram matrices for all form degrees."""
    d = mesh.dim
    pts, qw = geometry.xiq, geometry.wq
    masses, diagnostics = [], []
    for k in range(d + 1):
        components = list(combinations(range(d), k))
        comp_id = {I: j for j, I in enumerate(components)}
        rows, cols, data = [], [], []
        for cid in range(mesh.nk[d]):
            ci = np.asarray(mesh.cell_lo[cid], dtype=int)
            _, g, _, _ = geometry._cell_frame(cid, pts)
            detg = np.linalg.det(g)
            if np.any(detg <= 0):
                raise ValueError(f"non-positive pullback metric determinant in cell {cid}")
            rho = np.sqrt(detg)
            invg = np.linalg.inv(g)
            W = _minor_matrix(invg, components)
            local_faces = mesh.cell_to_faces[cid][k]
            ndof = len(local_faces)
            phi = np.ones((ndof, len(pts)), dtype=float)
            cids = np.empty(ndof, dtype=int)
            for a, fid in enumerate(local_faces):
                f = mesh.faces[k][fid]
                cids[a] = comp_id[tuple(f.vary)]
                for axis, line in dict(f.fixed).items():
                    side = int(line - ci[axis])
                    if side not in (0, 1):
                        raise ValueError("face is not a facet of its listed cell")
                    x = pts[:, axis]
                    phi[a] *= x if side else (1.0 - x)
            local = np.empty((ndof, ndof), dtype=float)
            weighted_volume = qw * rho
            for a in range(ndof):
                Wa = W[:, cids[a], :]
                for b in range(a, ndof):
                    value = float(np.sum(weighted_volume * phi[a] * phi[b]
                                         * Wa[:, cids[b]]))
                    local[a, b] = local[b, a] = value
            rr, cc = np.meshgrid(local_faces, local_faces, indexing="ij")
            rows.extend(rr.ravel().tolist())
            cols.extend(cc.ravel().tolist())
            data.extend(local.ravel().tolist())
        M = sp.coo_matrix((data, (rows, cols)),
                          shape=(mesh.nk[k], mesh.nk[k])).tocsr()
        M.sum_duplicates()
        M.eliminate_zeros()
        asym = M - M.T
        asym_norm = float(np.max(np.abs(asym.data))) if asym.nnz else 0.0
        masses.append(M)
        diagnostics.append({"k": k, "n": int(mesh.nk[k]), "nnz": int(M.nnz),
                            "max_abs_asymmetry": asym_norm})
    return masses, diagnostics


def consistent_hodge_matrices(mesh, masses):
    """Build symmetric energy matrices B_k=M_k Delta_k using dense solves.

    B_k = D_{k-1} M_{k-1}^{-1} D_{k-1}^T M_k
          + D_k^T M_{k+1} D_k.
    Intended for moderate-size audit problems, not large production runs.
    """
    import scipy.linalg as la
    d = mesh.dim
    result = []
    for k in range(d + 1):
        Mk = masses[k].toarray()
        energy = np.zeros_like(Mk)
        if k > 0:
            Dm = mesh.dmat[k - 1].toarray()
            rhs = Dm.T @ Mk
            y = la.solve(masses[k - 1].toarray(), rhs, assume_a="pos")
            energy += Mk @ Dm @ y
        if k < d:
            Dp = mesh.dmat[k].toarray()
            energy += Dp.T @ masses[k + 1].toarray() @ Dp
        result.append(0.5 * (energy + energy.T))
    return result
