#!/usr/bin/env python3
"""T158: interior pullback Levi-Civita connection and path-transported Whitney masses."""
from __future__ import annotations
from itertools import combinations
from pathlib import Path
import importlib.util
import json
import numpy as np
from scipy.linalg import eigvalsh
from numpy.polynomial.legendre import leggauss

T157_PATH = Path(__file__).resolve().with_name("audit_t157_full_covariant_whitney_curvature.py")
_spec = importlib.util.spec_from_file_location("audit_t157_for_t158", T157_PATH)
_t157 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_t157)

PSI_SG = _t157.PSI_SG
PHI = _t157.PHI
AXIS = _t157.AXIS
TOL = 2e-9
PAIRS = ((0, 1), (1, 2), (2, 0))


def links_from_frames(normals, edges, frames):
    transports, links = [], []
    for i, j in edges:
        R = _t157.minimal_rotation(normals[i], normals[j])
        T = frames[j].T @ R @ frames[i]
        transports.append(T)
        links.append(T[0, 0] + 1j * T[1, 0])
    return np.asarray(transports), np.asarray(links)


def interior_whitney_masses(vertices, triangles, edges, edge_index, normals,
                            frames, links, order):
    """Integrate Whitney bases parallel-transported through each triangle interior.

    On T=(i,j,k), n_T(lambda)=normalize(sum lambda_a n_a). The pullback of
    the S^2 Levi-Civita connection is trivialized at vertex i by geodesic
    transport x->i. Each nodal/edge basis is transported along v->x->i.
    """
    z, w = leggauss(order)
    z, w = (z + 1.0) / 2.0, w / 2.0
    # Duffy map lambda=(1-u,u(1-v),uv); physical dA=2*area*u du dv.
    quadrature = []
    for u, wu in zip(z, w):
        for v, wv in zip(z, w):
            lam = np.asarray([1.0 - u, u * (1.0 - v), u * v])
            quadrature.append((lam, 2.0 * u * wu * wv))

    def U(a, b):
        value = links[edge_index[tuple(sorted((a, b)))]]
        return value if a < b else np.conj(value)

    def oriented_edge_factor(a, b):
        return 1.0 if a < b else -U(a, b)

    M0 = np.zeros((len(vertices), len(vertices)), dtype=complex)
    M1 = np.zeros((len(edges), len(edges)), dtype=complex)
    M2 = np.zeros((len(triangles), len(triangles)), dtype=complex)
    min_interp_norm, min_base_dot = 1.0, 1.0

    for face, tri in enumerate(triangles):
        i, j, k = tri
        p = vertices[list(tri)]
        E = np.column_stack((p[1] - p[0], p[2] - p[0]))
        Ginv = np.linalg.inv(E.T @ E)
        grad1, grad2 = E @ Ginv[:, 0], E @ Ginv[:, 1]
        gradients = np.asarray([-grad1 - grad2, grad1, grad2])
        area = np.sqrt(np.linalg.det(E.T @ E)) / 2.0
        edge_ids = [edge_index[tuple(sorted((tri[a], tri[b])))] for a, b in PAIRS]
        edge_factors = np.asarray([
            oriented_edge_factor(tri[a], tri[b]) for a, b in PAIRS
        ])

        for lam, weight in quadrature:
            raw_normal = lam @ normals[list(tri)]
            raw_norm = np.linalg.norm(raw_normal)
            min_interp_norm = min(min_interp_norm, float(raw_norm))
            nx = raw_normal / raw_norm
            min_base_dot = min(min_base_dot, float(normals[i] @ nx))

            R_xi = _t157.minimal_rotation(nx, normals[i])
            q_vertex = []
            for vertex in tri:
                R_vx = _t157.minimal_rotation(normals[vertex], nx)
                Q = frames[i].T @ R_xi @ R_vx @ frames[vertex]
                q_vertex.append(Q[0, 0] + 1j * Q[1, 0])
            q_vertex = np.asarray(q_vertex)

            phi0 = lam * q_vertex
            M0_local_increment = np.outer(np.conj(phi0), phi0) * (area * weight)
            M0[np.ix_(tri, tri)] += M0_local_increment

            whitney_vectors = np.asarray([
                lam[a] * gradients[b] - lam[b] * gradients[a]
                for a, b in PAIRS
            ])
            q_edge = np.asarray([q_vertex[b] for a, b in PAIRS])
            M1_local_increment = (
                np.conj(q_edge[:, None]) * q_edge[None, :]
                * (whitney_vectors @ whitney_vectors.T)
                * (area * weight)
            )
            M1[np.ix_(edge_ids, edge_ids)] += (
                np.conj(edge_factors)[:, None]
                * M1_local_increment
                * edge_factors[None, :]
            )

        # The normalized Whitney 2-form has constant squared norm 1/area;
        # transport is unitary, so its mass is unchanged.
        M2[face, face] = 1.0 / area

    return M0, M1, M2, min_interp_norm, min_base_dot


def hodge_spectra(D0, D1, M0, M1, M2):
    K0 = D0.conj().T @ M1 @ D0
    K1 = (M1 @ D0 @ np.linalg.solve(M0, D0.conj().T @ M1)
          + D1.conj().T @ M2 @ D1)
    K2 = M2 @ D1 @ np.linalg.solve(M1, D1.conj().T @ M2)
    return {
        "0": eigvalsh(K0, M0).tolist(),
        "1": eigvalsh(K1, M1).tolist(),
        "2": eigvalsh(K2, M2).tolist(),
    }, [np.linalg.norm(K - K.conj().T) for K in (K0, K1, K2)]


def run_case(t, regular_control):
    (x, facets, polar, cycles, vertices, triangles, edges, normals,
     triangle_normals, triangle_areas, antipode, scale) = _t157.geometry(t, regular_control)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    frames, projection_norms = _t157.make_frames(normals)
    transports, links = links_from_frames(normals, edges, frames)

    # D0 and D1 are the same edge-link operators as T157; only the masses
    # are upgraded from endpoint transports to interior path transports.
    D0, D1, M0_endpoint, M1_endpoint, M2_endpoint = (
        _t157.build_covariant_operators(
            vertices, triangles, edges, edge_index, frames, links
        )
    )
    M0, M1, M2, min_interp_norm, min_base_dot = interior_whitney_masses(
        vertices, triangles, edges, edge_index, normals, frames, links, 12
    )
    M0_8, M1_8, _, _, _ = interior_whitney_masses(
        vertices, triangles, edges, edge_index, normals, frames, links, 8
    )
    quadrature_residuals = [
        float(np.linalg.norm(M0 - M0_8) / np.linalg.norm(M0)),
        float(np.linalg.norm(M1 - M1_8) / np.linalg.norm(M1)),
    ]

    # Gauge-covariance check: rotate each nodal tangent frame independently.
    theta = np.asarray([0.13 * i + 0.07 * np.sin(i) for i in range(len(vertices))])
    gauge = np.exp(-1j * theta)
    frames_g = np.empty_like(frames)
    for i, angle in enumerate(theta):
        R2 = np.asarray([[np.cos(angle), -np.sin(angle)],
                         [np.sin(angle), np.cos(angle)]])
        frames_g[i] = frames[i] @ R2
    _, links_g = links_from_frames(normals, edges, frames_g)
    D0g, D1g, _, _, _ = _t157.build_covariant_operators(
        vertices, triangles, edges, edge_index, frames_g, links_g
    )
    M0g, M1g, M2g, _, _ = interior_whitney_masses(
        vertices, triangles, edges, edge_index, normals, frames_g, links_g, 12
    )
    G0 = np.diag(gauge)
    G1 = np.diag([gauge[j] for i, j in edges])
    G2 = np.diag([gauge[tri[0]] for tri in triangles])
    gauge_residual = max(
        np.linalg.norm(D0g - G1 @ D0 @ G0.conj().T),
        np.linalg.norm(D1g - G2 @ D1 @ G1.conj().T),
        np.linalg.norm(M0g - G0 @ M0 @ G0.conj().T),
        np.linalg.norm(M1g - G1 @ M1 @ G1.conj().T),
        np.linalg.norm(M2g - G2 @ M2 @ G2.conj().T),
    )

    def U(a, b):
        value = links[edge_index[tuple(sorted((a, b)))]]
        return value if a < b else np.conj(value)

    holonomies, spherical_areas = [], []
    for i, j, k in triangles:
        holonomies.append(float(np.angle(U(i, j) * U(j, k) * U(k, i))))
        a, b, c = normals[[i, j, k]]
        spherical_areas.append(float(2 * np.arctan2(
            np.linalg.det(np.asarray([a, b, c])),
            1.0 + a @ b + b @ c + c @ a
        )))

    curvature_defect = D1 @ D0
    predicted_defect = np.zeros_like(curvature_defect)
    for face, (i, j, k) in enumerate(triangles):
        predicted_defect[face, j] = U(j, i) - U(k, i) * U(j, k)

    # T155 compatibility on the 30 face-graph links, checked independently.
    t155_residuals = []
    for i, j in [(i, j) for i, j in combinations(range(12), 2)
                 if len(set(cycles[i]) & set(cycles[j])) == 2]:
        ni, nj = x[i] / np.linalg.norm(x[i]), x[j] / np.linalg.norm(x[j])
        def t155_frame(n):
            e1 = AXIS - (AXIS @ n) * n
            e1 /= np.linalg.norm(e1)
            e2 = np.cross(n, e1)
            e2 /= np.linalg.norm(e2)
            return np.column_stack((e1, e2))
        old = frames[20 + j].T @ _t157.minimal_rotation(ni, nj) @ frames[20 + i]
        ref = t155_frame(nj).T @ _t157.minimal_rotation(ni, nj) @ t155_frame(ni)
        t155_residuals.append(np.linalg.norm(old - ref))

    # Antipodal covariance of all 90 real SO(2) link matrices.
    facet_index = {face: i for i, face in enumerate(facets)}
    anti_faces = np.asarray([
        facet_index[tuple(sorted(antipode[list(face)]))] for face in facets
    ])
    anti_nodes = np.r_[anti_faces, 20 + antipode]
    A = np.asarray([
        frames[anti_nodes[i]].T @ (-np.eye(3)) @ frames[i]
        for i in range(len(vertices))
    ])
    anti_residuals = []
    for e, (i, j) in enumerate(edges):
        ib, jb = int(anti_nodes[i]), int(anti_nodes[j])
        eb = edge_index[tuple(sorted((ib, jb)))]
        Tbar = transports[eb] if ib < jb else transports[eb].T
        anti_residuals.append(np.linalg.norm(Tbar @ A[i] - A[j] @ transports[e]))

    spectra, hodge_hermiticity = hodge_spectra(D0, D1, M0, M1, M2)
    return {
        "label": "regular_control" if regular_control else "supergolden",
        "parameter": float(t),
        "scale": float(scale),
        "counts": [len(vertices), len(edges), len(triangles)],
        "minimum_frame_projection_norm": float(np.min(projection_norms)),
        "minimum_normal_interpolation_norm": min_interp_norm,
        "minimum_base_to_interpolant_dot": min_base_dot,
        "quadrature_order_8_vs_12_relative_residuals_M0_M1": quadrature_residuals,
        "endpoint_to_interior_mass_relative_difference_M0_M1": [
            float(np.linalg.norm(M0 - M0_endpoint) / np.linalg.norm(M0)),
            float(np.linalg.norm(M1 - M1_endpoint) / np.linalg.norm(M1)),
        ],
        "T155_face_link_residual": float(max(t155_residuals)),
        "antipodal_link_covariance_residual": float(max(anti_residuals)),
        "holonomy_sum": float(sum(holonomies)),
        "gauss_bonnet_4pi_residual": float(abs(sum(holonomies) - 4 * np.pi)),
        "holonomy_spherical_area_residual": float(max(
            abs(a - b) for a, b in zip(holonomies, spherical_areas)
        )),
        "D1D0_norm": float(np.linalg.norm(curvature_defect)),
        "curvature_identity_residual": float(np.linalg.norm(curvature_defect - predicted_defect)),
        "mass_minimum_eigenvalues": [
            float(np.linalg.eigvalsh(M)[0]) for M in (M0, M1, M2)
        ],
        "mass_hermiticity_residuals": [
            float(np.linalg.norm(M - M.conj().T)) for M in (M0, M1, M2)
        ],
        "hodge_hermiticity_residuals": [float(v) for v in hodge_hermiticity],
        "gauge_covariance_residual": float(gauge_residual),
        "spectra": spectra,
    }


def build_report():
    return {
        "supergolden": run_case(PSI_SG, False),
        "regular_control": run_case(PHI, True),
        "interior_connection": {
            "normal_map": "n_T(lambda)=normalize(sum_a lambda_a n_a)",
            "connection": "pullback of the unit-sphere Levi-Civita connection by the piecewise smooth normal map",
            "path": "parallel transport from each vertex to x, then x to the triangle base vertex, along minor great-circle arcs",
            "edge_restriction": "on a triangle edge the normal map follows the minor great-circle arc, so its endpoint link equals T157",
            "quadrature": "Duffy-transformed tensor Gauss-Legendre; order 8 versus 12 is checked",
            "scope": "interior path-transported Whitney masses for the specified discrete normal map; no mesh-refinement convergence theorem is claimed",
        },
    }


def main():
    report = build_report()
    for case in (report["supergolden"], report["regular_control"]):
        assert case["counts"] == [32, 90, 60]
        assert case["minimum_frame_projection_norm"] > 0.1
        assert case["minimum_normal_interpolation_norm"] > 0.8
        assert case["minimum_base_to_interpolant_dot"] > 0.5
        assert max(case["quadrature_order_8_vs_12_relative_residuals_M0_M1"]) < TOL
        assert case["T155_face_link_residual"] < TOL
        assert case["antipodal_link_covariance_residual"] < TOL
        assert case["gauss_bonnet_4pi_residual"] < TOL
        assert case["holonomy_spherical_area_residual"] < TOL
        assert case["D1D0_norm"] > 1e-4
        assert case["curvature_identity_residual"] < TOL
        assert min(case["mass_minimum_eigenvalues"]) > 0
        assert max(case["mass_hermiticity_residuals"]) < TOL
        assert max(case["hodge_hermiticity_residuals"]) < TOL
        assert case["gauge_covariance_residual"] < TOL
        assert [len(case["spectra"][str(k)]) for k in range(3)] == [32, 90, 60]
    path = Path("results/json/t158_interior_covariant_whitney.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
