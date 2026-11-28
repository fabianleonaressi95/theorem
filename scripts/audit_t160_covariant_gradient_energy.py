#!/usr/bin/env python3
"""T160: covariant-gradient Galerkin energy for transported nodal sections.

Unlike T159, the stiffness is assembled from the covariant derivatives of the
same transported nodal basis used in the mass matrix. Derivatives include the
variation of vertex-to-point parallel transport.
"""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigvalsh
from numpy.polynomial.legendre import leggauss

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "t160_t159", ROOT / "scripts/audit_t159_curved_feec_refinement.py"
)
T159 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T159)
T157 = T159.T157
TOL = 2e-8


def quadrature_rule(order):
    z, w = leggauss(order)
    z, w = (z + 1.0) / 2.0, w / 2.0
    for u, wu in zip(z, w):
        for v, wv in zip(z, w):
            yield np.asarray([1.0-u, u*(1.0-v), u*v]), 2.0*u*wu*wv


def local_basis(lam, tri, parent_tri, parent_map, normals, frames):
    """Ambient C^3 representation of Q_{v->x}(e1+i e2), weighted by lambda_v."""
    parent_lam = lam @ parent_map
    raw = parent_lam @ normals[list(parent_tri)]
    nr = np.linalg.norm(raw)
    if nr < 1e-10:
        raise ValueError("normal interpolation vanished")
    nx = raw / nr
    out = []
    for vertex, weight in zip(tri, lam):
        R = T157.minimal_rotation(normals[vertex], nx)
        wv = frames[vertex][:, 0] + 1j * frames[vertex][:, 1]
        out.append(weight * (R @ wv))
    return np.asarray(out), nx


def assemble(factor, order=4, derivative_step=2e-6):
    base = T157.geometry(T157.PSI_SG, False)
    (_, _, _, _, vertices, triangles, _, normals, _, _, _, _) = base
    V, N, tris, edges, parents, parent_maps, keys, node_index = T159.refine_surface(
        vertices, normals, triangles, factor
    )
    frames, _, _ = T159.make_atlas_frames(N)
    n0 = len(V)
    M = np.zeros((n0, n0), dtype=complex)
    K = np.zeros((n0, n0), dtype=complex)
    min_normal = 1.0
    max_projected_radial = 0.0

    for face, tri in enumerate(tris):
        ids = np.asarray(tri, dtype=int)
        p = V[ids]
        E = np.column_stack((p[1]-p[0], p[2]-p[0]))
        gram = E.T @ E
        Ginv = np.linalg.inv(gram)
        area = np.sqrt(np.linalg.det(gram))/2.0
        parent_tri = triangles[parents[face]]
        parent_map = parent_maps[face]
        h = derivative_step
        for lam, weight in quadrature_rule(order):
            basis, nx = local_basis(lam, tri, parent_tri, parent_map, N, frames)
            min_normal = min(min_normal, float(np.linalg.norm(
                (lam @ parent_map) @ normals[list(parent_tri)]
            )))
            # Differentiate the complete transported basis in the two affine
            # reference directions; this includes d(Q_{v->x})/dx.
            du = np.asarray([1.0, -1.0, 0.0])
            dv = np.asarray([1.0, 0.0, -1.0])
            bp, _ = local_basis(lam+h*du, tri, parent_tri, parent_map, N, frames)
            bm, _ = local_basis(lam-h*du, tri, parent_tri, parent_map, N, frames)
            cp, _ = local_basis(lam+h*dv, tri, parent_tri, parent_map, N, frames)
            cm, _ = local_basis(lam-h*dv, tri, parent_tri, parent_map, N, frames)
            d_u = (bp-bm)/(2*h)
            d_v = (cp-cm)/(2*h)
            # Levi-Civita derivative on S^2 is ambient differentiation
            # followed by orthogonal projection to T_{n(x)}S^2.
            d_u -= np.outer(d_u @ nx, nx)
            d_v -= np.outer(d_v @ nx, nx)
            max_projected_radial = max(
                max_projected_radial,
                float(np.max(np.abs(d_u @ nx))),
                float(np.max(np.abs(d_v @ nx))),
            )
            local_M = np.conjugate(basis) @ basis.T
            # local_M[a,b] = <basis_a,basis_b>_Hermitian
            local_K = (
                Ginv[0,0] * (np.conjugate(d_u) @ d_u.T)
                + Ginv[0,1] * (np.conjugate(d_u) @ d_v.T)
                + Ginv[1,0] * (np.conjugate(d_v) @ d_u.T)
                + Ginv[1,1] * (np.conjugate(d_v) @ d_v.T)
            )
            fac = area * weight
            M[np.ix_(ids, ids)] += local_M * fac
            K[np.ix_(ids, ids)] += local_K * fac

    M = (M + M.conj().T)/2
    K = (K + K.conj().T)/2
    evals = eigvalsh(K, M, subset_by_index=[0, min(11, n0-1)])
    return {
        "factor": factor, "counts": [n0, len(edges), len(tris)],
        "lowest_12_eigenvalues": evals.tolist(),
        "minimum_mass_eigenvalue": float(np.linalg.eigvalsh(M)[0]),
        "minimum_stiffness_eigenvalue": float(np.linalg.eigvalsh(K)[0]),
        "mass_hermiticity_residual": float(np.linalg.norm(M-M.conj().T)),
        "stiffness_hermiticity_residual": float(np.linalg.norm(K-K.conj().T)),
        "minimum_normal_interpolation_norm": min_normal,
        "projected_derivative_radial_residual": max_projected_radial,
        "derivative_step": derivative_step,
    }, M, K


def build_report():
    rows = []
    for factor in (1, 2, 3, 4):
        row, _, _ = assemble(factor)
        rows.append(row)
    first = [r["lowest_12_eigenvalues"][0] for r in rows]
    return {
        "geometry": "T157 supergolden polar dodecahedron with fixed parent normal map",
        "basis": "phi_i(x)=lambda_i(x) P_{v_i->x}(e1_i+i e2_i), represented in ambient C^3",
        "connection_derivative": "P_{n(x)} d(phi_i), with the derivative acting on both lambda_i and the full minimal-rotation transport",
        "forms": "M_ij=integral <phi_i,phi_j>; K_ij=integral <nabla^A phi_i,nabla^A phi_j>",
        "derivative": "central differences in affine reference coordinates; h=2e-6; derivative-step sensitivity is tested separately",
        "refinements": rows,
        "first_eigenvalue_absolute_increments": [
            abs(first[i+1]-first[i]) for i in range(len(first)-1)
        ],
        "status": "A covariant-gradient Galerkin discretization of the specified piecewise-smooth pullback connection. Numerical evidence only; no asymptotic error bound or spectral convergence theorem is claimed.",
    }


def main():
    report = build_report()
    expected = [[32,90,60],[122,360,240],[272,810,540],[482,1440,960]]
    assert [r["counts"] for r in report["refinements"]] == expected
    for r in report["refinements"]:
        assert r["minimum_mass_eigenvalue"] > 0
        assert r["minimum_stiffness_eigenvalue"] > -1e-8
        assert r["mass_hermiticity_residual"] < TOL
        assert r["stiffness_hermiticity_residual"] < TOL
        assert r["minimum_normal_interpolation_norm"] > 0.8
        assert r["projected_derivative_radial_residual"] < 1e-7
    out = Path("results/json/t160_covariant_gradient_energy.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
