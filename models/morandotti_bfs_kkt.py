"""Rectangular Bogner--Fox--Schmit (BFS) prototype for the planar
Saint-Venant/KKT benchmark.

The scalar test space is globally C1 and therefore H2-conforming. All
boundary-vertex value and first-derivative DOFs are clamped to zero.
The strain space is the cellwise-constant symmetric tensor space.

This is a reproducible rectangular prototype, not yet a general
triangular/CIP-DG finite-element implementation.
"""
from __future__ import annotations

import numpy as np

from models.discrete_incompatibility_weak import (
    assemble_constitutive_energy,
    assemble_inc_weak,
    assemble_burgers_frank_load,
    solve_constrained_energy,
)


def _hermite_1d(t: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Cubic Hermite endpoint value/derivative basis and first two t-derivatives."""
    h = np.array([1 - 3*t*t + 2*t**3, t - 2*t*t + t**3,
                  3*t*t - 2*t**3, -t*t + t**3], dtype=float)
    dh = np.array([-6*t + 6*t*t, 1 - 4*t + 3*t*t,
                   6*t - 6*t*t, -2*t + 3*t*t], dtype=float)
    ddh = np.array([-6 + 12*t, -4 + 6*t,
                    6 - 12*t, -2 + 6*t], dtype=float)
    return h, dh, ddh


def plane_stress_stiffness(young_modulus: float, poisson_ratio: float) -> np.ndarray:
    """Fourth-order plane-stress stiffness on Sym(2), tensor-shear convention.

    As an operator on symmetric strains: C(eps)=2*mu*eps+lambda_2d*tr(eps)*I,
    where mu=E/(2*(1+nu)) and lambda_2d=E*nu/(1-nu**2).
    Its deviatoric/volumetric eigenvalues are E/(1+nu) and E/(1-nu).
    """
    E = float(young_modulus)
    nu = float(poisson_ratio)
    if not np.isfinite(E) or E <= 0:
        raise ValueError("young_modulus must be finite and positive")
    if not np.isfinite(nu) or not (-1.0 < nu < 1.0):
        raise ValueError("poisson_ratio must lie strictly between -1 and 1")
    I = np.eye(2)
    C = np.empty((2, 2, 2, 2), dtype=float)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    sym_identity = 0.5 * (I[i, k]*I[j, l] + I[i, l]*I[j, k])
                    mu = E / (2.0*(1.0 + nu))
                    lam = E*nu / (1.0 - nu**2)
                    C[i, j, k, l] = 2.0*mu*sym_identity + lam*I[i, j]*I[k, l]
    return C


def assemble_bfs_rectangular(
    nx: int = 2,
    ny: int = 2,
    *,
    quadrature_order: int = 3,
    young_modulus: float = 1.0,
    poisson_ratio: float = 0.3,
) -> dict[str, np.ndarray | int | float]:
    """Assemble A_h and M_h on [0,1]^2 using a uniform BFS mesh.

    Returns
    -------
    A: (n_test, 3*n_cell) weak incompatibility matrix.
    M: (3*n_cell, 3*n_cell) physical strain-energy matrix using plane-stress stiffness.
    test_hessians: (n_test, n_cell, nq, 2, 2).
    strain_basis: (n_cell, nq, 3*n_cell, 2, 2).
    weights: physical quadrature weights (n_cell, nq).
    free_dofs: global BFS DOF indices after clamping the boundary.
    """
    nx, ny, order = int(nx), int(ny), int(quadrature_order)
    if nx < 2 or ny < 2 or order < 3:
        raise ValueError("nx, ny must be >=2 and quadrature_order >=3")
    xs = np.linspace(0.0, 1.0, nx + 1)
    ys = np.linspace(0.0, 1.0, ny + 1)
    nnode = (nx + 1) * (ny + 1)
    ndof = 4 * nnode
    free = []
    for j in range(ny + 1):
        for i in range(nx + 1):
            if 0 < i < nx and 0 < j < ny:
                node = j * (nx + 1) + i
                free.extend(range(4*node, 4*node + 4))
    free = np.asarray(free, dtype=int)
    q, qw = np.polynomial.legendre.leggauss(order)
    q, qw = 0.5*(q + 1.0), 0.5*qw
    nq, ncell = order*order, nx*ny
    H_all = np.zeros((ndof, ncell, nq, 2, 2), dtype=float)
    V_all = np.zeros((ndof, ncell, nq), dtype=float)
    G_all = np.zeros((ndof, ncell, nq, 2), dtype=float)
    weights = np.zeros((ncell, nq), dtype=float)

    cell = 0
    for j in range(ny):
        hy = ys[j+1] - ys[j]
        for i in range(nx):
            hx = xs[i+1] - xs[i]
            vertices = ((i, j), (i+1, j), (i+1, j+1), (i, j+1))
            iq = 0
            for a, tx in enumerate(q):
                hxv, hxd, hxdd = _hermite_1d(float(tx))
                for b, ty in enumerate(q):
                    hyv, hyd, hydd = _hermite_1d(float(ty))
                    weights[cell, iq] = qw[a]*qw[b]*hx*hy
                    for ix, iy in vertices:
                        node = iy*(nx+1) + ix
                        ex = 0 if ix == i else 1
                        ey = 0 if iy == j else 1
                        vx, dx = 2*ex, 2*ex + 1
                        vy, dy = 2*ey, 2*ey + 1
                        for dof in range(4):
                            if dof == 0:
                                ax, ay, scale = vx, vy, 1.0
                            elif dof == 1:
                                ax, ay, scale = dx, vy, hx
                            elif dof == 2:
                                ax, ay, scale = vx, dy, hy
                            else:
                                ax, ay, scale = dx, dy, hx*hy
                            g = 4*node + dof
                            V_all[g, cell, iq] = scale*hxv[ax]*hyv[ay]
                            G_all[g, cell, iq, 0] = scale*hxd[ax]/hx*hyv[ay]
                            G_all[g, cell, iq, 1] = scale*hxv[ax]*hyd[ay]/hy
                            H_all[g, cell, iq, 0, 0] = scale*hxdd[ax]/hx**2*hyv[ay]
                            H_all[g, cell, iq, 1, 1] = scale*hxv[ax]*hydd[ay]/hy**2
                            cross = scale*hxd[ax]/hx*hyd[ay]/hy
                            H_all[g, cell, iq, 0, 1] = cross
                            H_all[g, cell, iq, 1, 0] = cross
                    iq += 1
            cell += 1

    test_hessians = H_all[free]
    test_values = V_all[free]
    test_gradients = G_all[free]
    strain_basis = np.zeros((ncell, nq, 3*ncell, 2, 2), dtype=float)
    for k in range(ncell):
        strain_basis[k, :, 3*k, 0, 0] = 1.0
        strain_basis[k, :, 3*k+1, 1, 1] = 1.0
        strain_basis[k, :, 3*k+2, 0, 1] = 1.0/np.sqrt(2.0)
        strain_basis[k, :, 3*k+2, 1, 0] = 1.0/np.sqrt(2.0)

    stiffness = plane_stress_stiffness(young_modulus, poisson_ratio)
    A = assemble_inc_weak(strain_basis, test_hessians, weights)
    M = assemble_constitutive_energy(strain_basis, weights, stiffness)
    return {
        "A": A, "M": M, "test_hessians": test_hessians,
        "test_values": test_values, "test_gradients": test_gradients,
        "strain_basis": strain_basis, "weights": weights,
        "free_dofs": free, "ncell": ncell, "n_test": len(free),
        "quadrature_order": order, "young_modulus": float(young_modulus),
        "poisson_ratio": float(poisson_ratio),
    }


def solve_bfs_kkt(
    source: np.ndarray,
    nx: int = 2,
    ny: int = 2,
    *,
    quadrature_order: int = 3,
    young_modulus: float = 1.0,
    poisson_ratio: float = 0.3,
) -> dict[str, np.ndarray | float | int]:
    """Assemble and solve the clamped BFS/cellwise-strain KKT prototype."""
    assembled = assemble_bfs_rectangular(
        nx, ny, quadrature_order=quadrature_order,
        young_modulus=young_modulus, poisson_ratio=poisson_ratio,
    )
    out = solve_constrained_energy(assembled["M"], assembled["A"], source)
    out.update({k: assembled[k] for k in ("A", "M", "free_dofs", "ncell", "n_test")})
    return out



def evaluate_bfs_test_basis(
    points: np.ndarray, nx: int = 2, ny: int = 2
) -> tuple[np.ndarray, np.ndarray]:
    """Evaluate all free clamped BFS test functions and gradients at points.

    Points must lie in the closed unit square. Values have shape
    (n_test,n_points), gradients have shape (n_test,n_points,2).
    """
    P = np.asarray(points, dtype=float)
    if P.ndim != 2 or P.shape[1] != 2 or not np.isfinite(P).all():
        raise ValueError("points must be a finite array of shape (npoint,2)")
    if np.any(P < 0.0) or np.any(P > 1.0):
        raise ValueError("all evaluation points must lie in [0,1]^2")
    nx, ny = int(nx), int(ny)
    if nx < 2 or ny < 2:
        raise ValueError("nx and ny must be >=2")
    xs, ys = np.linspace(0.0, 1.0, nx+1), np.linspace(0.0, 1.0, ny+1)
    free = []
    for j in range(1, ny):
        for i in range(1, nx):
            node = j*(nx+1) + i
            free.extend(range(4*node, 4*node+4))
    free_map = {g: k for k, g in enumerate(free)}
    V = np.zeros((len(free), len(P)), dtype=float)
    G = np.zeros((len(free), len(P), 2), dtype=float)
    for p, (x, y) in enumerate(P):
        i = min(int(x*nx), nx-1)
        j = min(int(y*ny), ny-1)
        hx, hy = xs[i+1]-xs[i], ys[j+1]-ys[j]
        tx, ty = (x-xs[i])/hx, (y-ys[j])/hy
        hxv, hxd, _ = _hermite_1d(float(tx))
        hyv, hyd, _ = _hermite_1d(float(ty))
        vertices = ((i, j), (i+1, j), (i+1, j+1), (i, j+1))
        for ix, iy in vertices:
            node = iy*(nx+1) + ix
            ex, ey = int(ix != i), int(iy != j)
            vx, dx, vy, dy = 2*ex, 2*ex+1, 2*ey, 2*ey+1
            for dof in range(4):
                if dof == 0:
                    ax, ay, scale = vx, vy, 1.0
                elif dof == 1:
                    ax, ay, scale = dx, vy, hx
                elif dof == 2:
                    ax, ay, scale = vx, dy, hy
                else:
                    ax, ay, scale = dx, dy, hx*hy
                row = free_map.get(4*node+dof)
                if row is None:
                    continue
                V[row, p] += scale*hxv[ax]*hyv[ay]
                G[row, p, 0] += scale*hxd[ax]/hx*hyv[ay]
                G[row, p, 1] += scale*hxv[ax]*hyd[ay]/hy
    return V, G


def assemble_bfs_defect_source(
    dislocation_positions: np.ndarray,
    burgers_vectors: np.ndarray,
    disclination_positions: np.ndarray,
    frank_angles: np.ndarray,
    *,
    nx: int = 2,
    ny: int = 2,
    core_radius: float | None = None,
    quadrature_order: int = 3,
) -> np.ndarray:
    """Assemble point or normalized Gaussian-core Burgers/Frank loads.

    For core_radius=None or zero, the distributions are evaluated pointwise.
    For core_radius>0, a Gaussian is integrated over the mesh quadrature and
    normalized on the unit square (including boundary truncation). The
    normalization is part of this prototype's explicit core convention.
    """
    Xd = np.asarray(dislocation_positions, dtype=float).reshape(-1, 2)
    B = np.asarray(burgers_vectors, dtype=float).reshape(-1, 2)
    Xf = np.asarray(disclination_positions, dtype=float).reshape(-1, 2)
    F = np.asarray(frank_angles, dtype=float).reshape(-1)
    if len(Xd) != len(B) or len(Xf) != len(F):
        raise ValueError("each defect position must have one Burgers/Frank datum")
    if core_radius is not None and (not np.isfinite(core_radius) or core_radius < 0):
        raise ValueError("core_radius must be finite and nonnegative")
    assembled = assemble_bfs_rectangular(
        nx, ny, quadrature_order=quadrature_order
    )
    if core_radius is None or core_radius == 0.0:
        Vd, Gd = evaluate_bfs_test_basis(Xd, nx, ny)
        Vf, _ = evaluate_bfs_test_basis(Xf, nx, ny)
    else:
        eps = float(core_radius)
        Vq = assembled["test_values"]
        Gq = assembled["test_gradients"]
        w = assembled["weights"]
        def gaussian_moments(center: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
            # Reconstruct the same tensor-product Gauss points used by assembly.
            q, _ = np.polynomial.legendre.leggauss(quadrature_order)
            q = 0.5*(q+1.0)
            pts = []
            for j in range(ny):
                for i in range(nx):
                    hx, hy = 1.0/nx, 1.0/ny
                    for tx in q:
                        for ty in q:
                            pts.append(((i+tx)*hx, (j+ty)*hy))
            pts = np.asarray(pts).reshape(nx*ny, quadrature_order**2, 2)
            rho = np.exp(-np.sum((pts-center[None, None, :])**2, axis=2)/(2*eps**2))
            norm = float(np.sum(rho*w))
            if norm <= np.finfo(float).tiny:
                raise ValueError("Gaussian core is numerically unresolved by the mesh quadrature")
            values = np.einsum("tkq,kq,kq->t", Vq, rho, w)/norm
            gradients = np.einsum("tkqd,kq,kq->td", Gq, rho, w)/norm
            return values, gradients
        Vd = np.zeros((len(assembled["free_dofs"]), len(Xd)))
        Gd = np.zeros((len(assembled["free_dofs"]), len(Xd), 2))
        for j, center in enumerate(Xd):
            Vd[:, j], Gd[:, j] = gaussian_moments(center)
        Vf = np.zeros((len(assembled["free_dofs"]), len(Xf)))
        for j, center in enumerate(Xf):
            Vf[:, j], _ = gaussian_moments(center)
    return assemble_burgers_frank_load(Vd, Gd, B, Vf, F)
