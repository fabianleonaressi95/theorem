#!/usr/bin/env python3
"""T159: mesh-refinement audit for the interior curved Whitney connection."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigvalsh
from numpy.polynomial.legendre import leggauss

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "t159_t157", ROOT / "scripts/audit_t157_full_covariant_whitney_curvature.py"
)
T157 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T157)
PAIRS = ((0, 1), (1, 2), (2, 0))
TOL = 2e-9


def refine_surface(vertices, normals, triangles, factor):
    """Conforming barycentric lattice subdivision, retaining the parent normal map."""
    node_index, keys, points, nodal_normals = {}, [], [], []
    for v in range(len(vertices)):
        key = ((v, factor),)
        node_index[key] = v
        keys.append(key)
        points.append(vertices[v])
        nodal_normals.append(normals[v])
    fine_triangles, parents, parent_maps = [], [], []

    for parent_id, tri in enumerate(triangles):
        lattice = {}
        def get_node(i, j):
            k = factor - i - j
            bary = np.asarray([k, i, j], dtype=float) / factor
            key = tuple(sorted(
                (int(tri[q]), int(round(bary[q] * factor)))
                for q in range(3) if bary[q] > 1e-12
            ))
            raw = bary @ normals[list(tri)]
            candidate = raw / np.linalg.norm(raw)
            if key not in node_index:
                node_index[key] = len(points)
                keys.append(key)
                points.append(bary @ vertices[list(tri)])
                nodal_normals.append(candidate)
            elif np.linalg.norm(nodal_normals[node_index[key]] - candidate) > TOL:
                raise AssertionError("parent normal map is discontinuous on a shared edge")
            return node_index[key], bary

        for i in range(factor + 1):
            for j in range(factor + 1 - i):
                lattice[(i, j)] = get_node(i, j)

        for i in range(factor):
            for j in range(factor - i):
                local = [lattice[(i, j)], lattice[(i + 1, j)], lattice[(i, j + 1)]]
                fine_triangles.append(tuple(item[0] for item in local))
                parents.append(parent_id)
                parent_maps.append(np.asarray([item[1] for item in local]))
                if i + j <= factor - 2:
                    local = [lattice[(i + 1, j)], lattice[(i + 1, j + 1)], lattice[(i, j + 1)]]
                    fine_triangles.append(tuple(item[0] for item in local))
                    parents.append(parent_id)
                    parent_maps.append(np.asarray([item[1] for item in local]))

    edges = sorted({
        tuple(sorted(edge))
        for tri in fine_triangles
        for edge in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0]))
    })
    return (np.asarray(points), np.asarray(nodal_normals), fine_triangles, edges,
            np.asarray(parents), parent_maps, keys, node_index)


def make_atlas_frames(normals):
    """Use the vesica x-axis gauge, switching to a coordinate chart near its singularity."""
    axes = np.eye(3)
    frames, fallback_count, min_projection = [], 0, 1.0
    for normal in normals:
        axis = T157.AXIS
        projection = axis - (axis @ normal) * normal
        if np.linalg.norm(projection) < 0.5:
            fallback_count += 1
            axis = axes[int(np.argmin(np.abs(axes @ normal)))]
            projection = axis - (axis @ normal) * normal
        norm = np.linalg.norm(projection)
        min_projection = min(min_projection, float(norm))
        e1 = projection / norm
        e2 = np.cross(normal, e1)
        e2 /= np.linalg.norm(e2)
        frames.append(np.column_stack((e1, e2)))
    return np.asarray(frames), fallback_count, min_projection


def assemble_refined(factor, order=8):
    base = T157.geometry(T157.PSI_SG, False)
    (x, facets, polar, cycles, vertices, triangles, edges, normals,
     triangle_normals, triangle_areas, antipode, scale) = base
    V, N, tris, fine_edges, parents, parent_maps, keys, node_index = refine_surface(
        vertices, normals, triangles, factor
    )
    frames, fallback_count, min_projection = make_atlas_frames(N)
    edge_index = {edge: i for i, edge in enumerate(fine_edges)}
    transports, links = [], []
    for i, j in fine_edges:
        R = T157.minimal_rotation(N[i], N[j])
        T = frames[j].T @ R @ frames[i]
        transports.append(T)
        links.append(T[0, 0] + 1j * T[1, 0])
    transports, links = np.asarray(transports), np.asarray(links)

    def U(a, b):
        value = links[edge_index[tuple(sorted((a, b)))]]
        return value if a < b else np.conj(value)

    def edge_factor(a, b):
        return 1.0 if a < b else -U(a, b)

    n0, n1, n2 = len(V), len(fine_edges), len(tris)
    D0 = np.zeros((n1, n0), dtype=complex)
    D1 = np.zeros((n2, n1), dtype=complex)
    for e, (i, j) in enumerate(fine_edges):
        D0[e, i], D0[e, j] = -links[e], 1.0

    z, w = leggauss(order)
    z, w = (z + 1.0) / 2.0, w / 2.0
    quadrature = []
    for u, wu in zip(z, w):
        for v, wv in zip(z, w):
            lam = np.asarray([1.0 - u, u * (1.0 - v), u * v])
            quadrature.append((lam, 2.0 * u * wu * wv))

    M0 = np.zeros((n0, n0), dtype=complex)
    M1 = np.zeros((n1, n1), dtype=complex)
    M2 = np.zeros((n2, n2), dtype=complex)
    min_normal_norm, min_base_dot = 1.0, 1.0
    for face, tri in enumerate(tris):
        i, j, k = tri
        ids = np.asarray(tri, dtype=int)
        p = V[ids]
        E = np.column_stack((p[1] - p[0], p[2] - p[0]))
        Ginv = np.linalg.inv(E.T @ E)
        grad1, grad2 = E @ Ginv[:, 0], E @ Ginv[:, 1]
        gradients = np.asarray([-grad1 - grad2, grad1, grad2])
        area = np.sqrt(np.linalg.det(E.T @ E)) / 2.0
        edge_ids = [edge_index[tuple(sorted((tri[a], tri[b])))] for a, b in PAIRS]
        edge_factors = np.asarray([edge_factor(tri[a], tri[b]) for a, b in PAIRS])
        parent_tri = triangles[parents[face]]
        parent_map = parent_maps[face]

        for lam, weight in quadrature:
            parent_lam = lam @ parent_map
            raw_normal = parent_lam @ normals[list(parent_tri)]
            raw_norm = np.linalg.norm(raw_normal)
            min_normal_norm = min(min_normal_norm, float(raw_norm))
            nx = raw_normal / raw_norm
            min_base_dot = min(min_base_dot, float(N[i] @ nx))
            R_xi = T157.minimal_rotation(nx, N[i])
            q_vertex = []
            for vertex in tri:
                R_vx = T157.minimal_rotation(N[vertex], nx)
                Q = frames[i].T @ R_xi @ R_vx @ frames[vertex]
                q_vertex.append(Q[0, 0] + 1j * Q[1, 0])
            q_vertex = np.asarray(q_vertex)

            phi0 = lam * q_vertex
            M0[np.ix_(ids, ids)] += np.outer(np.conj(phi0), phi0) * (area * weight)
            whitney = np.asarray([
                lam[a] * gradients[b] - lam[b] * gradients[a]
                for a, b in PAIRS
            ])
            q_edge = np.asarray([q_vertex[b] for a, b in PAIRS])
            increment = (
                np.conj(q_edge[:, None]) * q_edge[None, :]
                * (whitney @ whitney.T) * (area * weight)
            )
            M1[np.ix_(edge_ids, edge_ids)] += (
                np.conj(edge_factors)[:, None] * increment * edge_factors[None, :]
            )

        for a, b, transport in ((i, j, U(j, i)), (j, k, U(k, i)), (k, i, 1.0)):
            e = edge_index[tuple(sorted((a, b)))]
            D1[face, e] += transport * edge_factor(a, b)
        M2[face, face] = 1.0 / area

    K0 = D0.conj().T @ M1 @ D0
    eigenvalues = eigvalsh(K0, M0, subset_by_index=[0, min(11, n0 - 1)])
    predicted = np.zeros_like(D1 @ D0)
    for face, (i, j, k) in enumerate(tris):
        predicted[face, j] = U(j, i) - U(k, i) * U(j, k)
    curvature_residual = float(np.linalg.norm(D1 @ D0 - predicted))

    facet_index = {face: i for i, face in enumerate(facets)}
    anti_faces = np.asarray([
        facet_index[tuple(sorted(antipode[list(face)]))] for face in facets
    ])
    anti_base = np.r_[anti_faces, 20 + antipode]
    anti_nodes = np.empty(n0, dtype=int)
    for i, key in enumerate(keys):
        target = tuple(sorted((int(anti_base[v]), weight) for v, weight in key))
        anti_nodes[i] = node_index[target]
    anti_normal_residual = float(np.max(np.linalg.norm(N[anti_nodes] + N, axis=1)))
    A = np.asarray([
        frames[anti_nodes[i]].T @ (-np.eye(3)) @ frames[i] for i in range(n0)
    ])
    anti_link_residuals = []
    for e, (i, j) in enumerate(fine_edges):
        ib, jb = int(anti_nodes[i]), int(anti_nodes[j])
        eb = edge_index[tuple(sorted((ib, jb)))]
        Tbar = transports[eb] if ib < jb else transports[eb].T
        anti_link_residuals.append(np.linalg.norm(Tbar @ A[i] - A[j] @ transports[e]))

    holonomies, spherical_areas = [], []
    for i, j, k in tris:
        holonomies.append(float(np.angle(U(i, j) * U(j, k) * U(k, i))))
        a, b, c = N[[i, j, k]]
        spherical_areas.append(float(2 * np.arctan2(
            np.linalg.det(np.asarray([a, b, c])),
            1.0 + a @ b + b @ c + c @ a
        )))

    np.linalg.cholesky(M0)
    np.linalg.cholesky(M1)
    report = {
        "factor": factor, "counts": [n0, n1, n2],
        "first_12_hodge0_eigenvalues": eigenvalues.tolist(),
        "minimum_M0_eigenvalue": float(np.linalg.eigvalsh(M0)[0]),
        "minimum_M1_cholesky_diagonal": float(np.min(np.real(np.diag(np.linalg.cholesky(M1))))),
        "minimum_M2_diagonal": float(np.min(np.real(np.diag(M2)))),
        "minimum_normal_interpolation_norm": min_normal_norm,
        "minimum_base_to_interpolant_dot": min_base_dot,
        "vesica_axis_fallback_chart_nodes": fallback_count,
        "minimum_frame_projection_norm": min_projection,
        "curvature_defect_norm": float(np.linalg.norm(D1 @ D0)),
        "curvature_identity_residual": curvature_residual,
        "antipodal_node_involution": bool(np.all(anti_nodes[anti_nodes] == np.arange(n0))),
        "antipodal_normal_residual": anti_normal_residual,
        "antipodal_link_covariance_residual": float(max(anti_link_residuals)),
        "holonomy_sum": float(sum(holonomies)),
        "gauss_bonnet_4pi_residual": float(abs(sum(holonomies) - 4 * np.pi)),
        "holonomy_spherical_area_residual": float(max(
            abs(a - b) for a, b in zip(holonomies, spherical_areas)
        )),
    }
    return report, M0, M1


def build_report():
    reports, M0_8, M1_8 = [], None, None
    for factor in (1, 2, 3, 4):
        report, M0, M1 = assemble_refined(factor, 8)
        reports.append(report)
        if factor == 2:
            M0_8, M1_8 = M0, M1
    _, M0_12, M1_12 = assemble_refined(2, 12)
    qres = [
        float(np.linalg.norm(M0_12 - M0_8) / np.linalg.norm(M0_12)),
        float(np.linalg.norm(M1_12 - M1_8) / np.linalg.norm(M1_12)),
    ]
    first = [r["first_12_hodge0_eigenvalues"][0] for r in reports]
    deltas = [abs(first[i + 1] - first[i]) for i in range(len(first) - 1)]
    return {
        "geometry": "T157 supergolden polar dodecahedron",
        "normal_map": "fixed coarse T157 nodal-normal interpolation, restricted to each refined triangle through parent barycentric coordinates",
        "connection": "T158 interior pullback of the unit-sphere Levi-Civita connection",
        "refinements": reports,
        "first_eigenvalue_absolute_increments": deltas,
        "factor_2_quadrature_order_8_vs_12_relative_mass_residuals": qres,
        "interpretation": "The finite refinement sequence shows stabilization of the lowest covariant Hodge-0 eigenvalue for this fixed piecewise normal map. This is numerical evidence only, not a proof of spectral convergence or a curved-FEEC error estimate."
    }


def main():
    report = build_report()
    assert [r["counts"] for r in report["refinements"]] == [
        [32, 90, 60], [122, 360, 240], [272, 810, 540], [482, 1440, 960]
    ]
    for r in report["refinements"]:
        assert r["minimum_M0_eigenvalue"] > 0
        assert r["minimum_M1_cholesky_diagonal"] > 0
        assert r["minimum_M2_diagonal"] > 0
        assert r["minimum_normal_interpolation_norm"] > 0.8
        assert r["minimum_base_to_interpolant_dot"] > 0.5
        assert r["minimum_frame_projection_norm"] > 0.5
        assert r["curvature_defect_norm"] > 1e-4
        assert r["curvature_identity_residual"] < TOL
        assert r["antipodal_node_involution"]
        assert r["antipodal_normal_residual"] < TOL
        assert r["antipodal_link_covariance_residual"] < TOL
        assert r["gauss_bonnet_4pi_residual"] < 2e-7
        assert r["holonomy_spherical_area_residual"] < 2e-7
    assert max(report["factor_2_quadrature_order_8_vs_12_relative_mass_residuals"]) < TOL
    d = report["first_eigenvalue_absolute_increments"]
    assert d[2] < d[1] < d[0]
    out = Path("results/json/t159_curved_feec_refinement.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
