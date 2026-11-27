#!/usr/bin/env python3
"""T157: full 32-90-60 link-covariant Whitney construction with curvature defect.

This is a discrete connection model, not a flat cochain complex: D1_A D0_A
is the Wilson-curvature defect and is required to be nonzero.
"""
from __future__ import annotations
from itertools import combinations
from pathlib import Path
import json
import numpy as np
from scipy.linalg import eigvalsh
from scipy.spatial import ConvexHull

PSI_SG = 1.465571231876768
PHI = (1.0 + np.sqrt(5.0)) / 2.0
AXIS = np.asarray([1.0, 0.0, 0.0])
TOL = 2e-9
QPTS = np.asarray([[2/3, 1/6, 1/6], [1/6, 2/3, 1/6], [1/6, 1/6, 2/3]])
PAIRS = ((0, 1), (1, 2), (2, 0))


def geometry(t: float, regular_control: bool):
    x = np.asarray(
        [(0., a, b*t) for a in (-1., 1.) for b in (-1., 1.)]
        + [(a, b*t, 0.) for a in (-1., 1.) for b in (-1., 1.)]
        + [(a*t, 0., b) for a in (-1., 1.) for b in (-1., 1.)]
    )
    hull = ConvexHull(x)
    equations = {tuple(sorted(map(int, s))): e
                 for s, e in zip(hull.simplices, hull.equations)}
    facets = sorted(equations)
    polar = np.asarray([equations[f][:3] / (-equations[f][3]) for f in facets])
    antipode = np.asarray([int(np.argmin(np.linalg.norm(x + p, axis=1))) for p in x])

    cycles = []
    for vertex in range(12):
        incident = [i for i, f in enumerate(facets) if vertex in f]
        adjacency = {
            i: [j for j in incident if j != i and len(set(facets[i]) & set(facets[j])) == 2]
            for i in incident
        }
        start = min(incident)
        cycle = [start]
        previous, current = None, start
        nxt = min(adjacency[current])
        while nxt != start:
            cycle.append(nxt)
            previous, current = current, nxt
            nxt = next(q for q in adjacency[current] if q != previous)
        assert len(cycle) == 5
        cycles.append(cycle)

    scale = 1.0
    if regular_control:
        dual_edges = [(i, j) for i, j in combinations(range(20), 2)
                      if len(set(facets[i]) & set(facets[j])) == 2]
        raw_edge = np.linalg.norm(polar[dual_edges[0][0]] - polar[dual_edges[0][1]])
        scale = 2 * np.sin(np.pi / 5) / raw_edge
    polar *= scale
    vertices = np.vstack([polar, np.asarray([polar[c].mean(axis=0) for c in cycles])])

    triangles = []
    for face, cycle in enumerate(cycles):
        centre = 20 + face
        for k in range(5):
            tri = (centre, cycle[k], cycle[(k + 1) % 5])
            p = vertices[list(tri)]
            if np.dot(np.cross(p[1] - p[0], p[2] - p[0]), p.mean(axis=0)) < 0:
                tri = (centre, cycle[(k + 1) % 5], cycle[k])
            triangles.append(tri)
    edges = sorted({
        tuple(sorted(e))
        for tri in triangles
        for e in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0]))
    })

    triangle_normals, triangle_areas = [], []
    for tri in triangles:
        p = vertices[list(tri)]
        cross = np.cross(p[1] - p[0], p[2] - p[0])
        triangle_normals.append(cross / np.linalg.norm(cross))
        triangle_areas.append(np.linalg.norm(cross) / 2)
    triangle_normals = np.asarray(triangle_normals)
    triangle_areas = np.asarray(triangle_areas)

    # Natural discrete normal extension: area-weighted incident triangle normals.
    # At each of the 12 face-centroid nodes this equals the polar-face normal.
    nodal_normals = np.zeros((32, 3))
    for tri, normal, area in zip(triangles, triangle_normals, triangle_areas):
        for vertex in tri:
            nodal_normals[vertex] += area * normal
    normal_lengths = np.linalg.norm(nodal_normals, axis=1)
    assert np.min(normal_lengths) > 1e-12
    nodal_normals /= normal_lengths[:, None]
    return (x, facets, polar, cycles, vertices, triangles, edges, nodal_normals,
            triangle_normals, triangle_areas, antipode, scale)


def skew(v):
    return np.asarray([[0., -v[2], v[1]], [v[2], 0., -v[0]], [-v[1], v[0], 0.]])


def minimal_rotation(ni, nj):
    cross = np.cross(ni, nj)
    sine = np.linalg.norm(cross)
    cosine = float(np.clip(ni @ nj, -1.0, 1.0))
    if sine < 1e-13:
        if cosine > 0:
            return np.eye(3)
        raise ValueError("antipodal adjacent normals have no unique minimal rotation")
    K = skew(cross)
    return np.eye(3) + K + K @ K * ((1.0 - cosine) / (sine * sine))


def make_frames(normals):
    frames, projection_norms = [], []
    for normal in normals:
        e1 = AXIS - (AXIS @ normal) * normal
        projection_norms.append(np.linalg.norm(e1))
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(normal, e1)
        e2 /= np.linalg.norm(e2)
        frames.append(np.column_stack((e1, e2)))
    return np.asarray(frames), np.asarray(projection_norms)


def build_covariant_operators(vertices, triangles, edges, edge_index, frames, links):
    def U(a, b):
        value = links[edge_index[tuple(sorted((a, b)))]]
        return value if a < b else np.conj(value)

    # An oriented edge cochain c_ab takes values in the fibre at b.
    # Reversing orientation gives c_ba = -U_ba c_ab.
    def oriented_edge_coefficient(a, b):
        return 1.0 if a < b else -U(a, b)

    D0 = np.zeros((len(edges), len(vertices)), dtype=complex)
    for e, (i, j) in enumerate(edges):
        D0[e, i] = -links[e]
        D0[e, j] = 1.0

    D1 = np.zeros((len(triangles), len(edges)), dtype=complex)
    M0 = np.zeros((len(vertices), len(vertices)), dtype=complex)
    M1 = np.zeros((len(edges), len(edges)), dtype=complex)
    M2 = np.zeros((len(triangles), len(triangles)), dtype=complex)

    for face_index, tri in enumerate(triangles):
        i, j, k = tri
        # Boundary sum transported to the base fibre at vertex i.
        for a, b, transport in ((i, j, U(j, i)), (j, k, U(k, i)), (k, i, 1.0)):
            e = edge_index[tuple(sorted((a, b)))]
            D1[face_index, e] += transport * oriented_edge_coefficient(a, b)

        p = vertices[list(tri)]
        E = np.column_stack((p[1] - p[0], p[2] - p[0]))
        Ginv = np.linalg.inv(E.T @ E)
        grad1, grad2 = E @ Ginv[:, 0], E @ Ginv[:, 1]
        gradients = np.asarray([-grad1 - grad2, grad1, grad2])
        area = np.sqrt(np.linalg.det(E.T @ E)) / 2.0

        M0_local = area / 12.0 * (np.ones((3, 3)) + np.eye(3))
        whitney = np.asarray([
            [lam[a] * gradients[b] - lam[b] * gradients[a] for a, b in PAIRS]
            for lam in QPTS
        ])
        M1_local = np.einsum("qia,qja->ij", whitney, whitney) * area / 3.0

        # B0 transports vertex values to the common base fibre at i.
        B0 = np.zeros((3, len(vertices)), dtype=complex)
        for row, vertex in enumerate(tri):
            B0[row, vertex] = 1.0 if vertex == i else U(vertex, i)

        # B1 transports oriented edge values to the same base fibre.
        B1 = np.zeros((3, len(edges)), dtype=complex)
        for row, (local_a, local_b) in enumerate(PAIRS):
            a, b = tri[local_a], tri[local_b]
            transport = 1.0 if b == i else U(b, i)
            edge = edge_index[tuple(sorted((a, b)))]
            B1[row, edge] = transport * oriented_edge_coefficient(a, b)

        M0 += B0.conj().T @ M0_local @ B0
        M1 += B1.conj().T @ M1_local @ B1
        M2[face_index, face_index] = 1.0 / area

    return D0, D1, M0, M1, M2


def run_case(t, regular_control):
    (x, facets, polar, cycles, vertices, triangles, edges, normals,
     triangle_normals, triangle_areas, antipode, scale) = geometry(t, regular_control)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    frames, projection_norms = make_frames(normals)
    transports, links = [], []
    for i, j in edges:
        R = minimal_rotation(normals[i], normals[j])
        T = frames[j].T @ R @ frames[i]
        transports.append(T)
        links.append(T[0, 0] + 1j * T[1, 0])
    transports, links = np.asarray(transports), np.asarray(links)

    def U(a, b):
        value = links[edge_index[tuple(sorted((a, b)))]]
        return value if a < b else np.conj(value)

    # The 12 centroid fibres reproduce T155's 30 Gauss-map links exactly.
    face_edges = [(i, j) for i, j in combinations(range(12), 2)
                  if len(set(cycles[i]) & set(cycles[j])) == 2]
    t155_residuals = []
    for i, j in face_edges:
        ni, nj = x[i] / np.linalg.norm(x[i]), x[j] / np.linalg.norm(x[j])
        def t155_frame(normal):
            e1 = AXIS - (AXIS @ normal) * normal
            e1 /= np.linalg.norm(e1)
            e2 = np.cross(normal, e1)
            e2 /= np.linalg.norm(e2)
            return np.column_stack((e1, e2))
        F_i, F_j = t155_frame(ni), t155_frame(nj)
        T_centroid = frames[20 + j].T @ minimal_rotation(ni, nj) @ frames[20 + i]
        T_t155 = F_j.T @ minimal_rotation(ni, nj) @ F_i
        t155_residuals.append(np.linalg.norm(T_centroid - T_t155))

    # Antipodal covariance in real tangent-frame coordinates.
    facet_index = {face: i for i, face in enumerate(facets)}
    anti_faces = np.asarray([facet_index[tuple(sorted(antipode[list(face)]))]
                             for face in facets])
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

    holonomies, spherical_areas = [], []
    for i, j, k in triangles:
        H = U(i, j) * U(j, k) * U(k, i)
        holonomies.append(float(np.angle(H)))
        a, b, c = normals[[i, j, k]]
        spherical_areas.append(float(2 * np.arctan2(
            np.linalg.det(np.asarray([a, b, c])),
            1.0 + a @ b + b @ c + c @ a
        )))

    D0, D1, M0, M1, M2 = build_covariant_operators(
        vertices, triangles, edges, edge_index, frames, links
    )
    curvature_defect = D1 @ D0
    predicted_defect = np.zeros_like(curvature_defect)
    for face, (i, j, k) in enumerate(triangles):
        predicted_defect[face, j] = U(j, i) - U(k, i) * U(j, k)

    # Gauge covariance under a deterministic, nonconstant U(1) vertex gauge.
    theta = np.asarray([0.13 * i + 0.07 * np.sin(i) for i in range(len(vertices))])
    gauge = np.exp(1j * theta)
    gauged_links = np.asarray([
        gauge[j] * links[e] * np.conj(gauge[i]) for e, (i, j) in enumerate(edges)
    ])
    D0g, D1g, M0g, M1g, M2g = build_covariant_operators(
        vertices, triangles, edges, edge_index, frames, gauged_links
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

    K0 = D0.conj().T @ M1 @ D0
    K1 = M1 @ D0 @ np.linalg.solve(M0, D0.conj().T @ M1) + D1.conj().T @ M2 @ D1
    K2 = M2 @ D1 @ np.linalg.solve(M1, D1.conj().T @ M2)
    spectra = {
        "0": eigvalsh(K0, M0).tolist(),
        "1": eigvalsh(K1, M1).tolist(),
        "2": eigvalsh(K2, M2).tolist(),
    }

    return {
        "label": "regular_control" if regular_control else "supergolden",
        "parameter": float(t),
        "scale": float(scale),
        "counts": [len(vertices), len(edges), len(triangles)],
        "minimum_frame_projection_norm": float(np.min(projection_norms)),
        "centroid_normal_T155_residual": float(max(
            np.linalg.norm(normals[20 + i] - x[i] / np.linalg.norm(x[i]))
            for i in range(12)
        )),
        "T155_face_link_residual": float(max(t155_residuals, default=0.0)),
        "link_orthogonality_residual": float(max(
            np.linalg.norm(T.T @ T - np.eye(2)) for T in transports
        )),
        "link_determinant_residual": float(max(abs(np.linalg.det(T) - 1.0) for T in transports)),
        "antipodal_normal_residual": float(max(
            np.linalg.norm(normals[anti_nodes[i]] + normals[i]) for i in range(len(vertices))
        )),
        "antipodal_link_covariance_residual": float(max(anti_residuals)),
        "holonomy_sum": float(sum(holonomies)),
        "gauss_bonnet_4pi_residual": float(abs(sum(holonomies) - 4 * np.pi)),
        "holonomy_spherical_area_residual": float(max(
            abs(a - b) for a, b in zip(holonomies, spherical_areas)
        )),
        "D1D0_norm": float(np.linalg.norm(curvature_defect)),
        "curvature_identity_residual": float(np.linalg.norm(curvature_defect - predicted_defect)),
        "mass_minimum_eigenvalues": [float(np.linalg.eigvalsh(M)[0]) for M in (M0, M1, M2)],
        "mass_hermiticity_residuals": [float(np.linalg.norm(M - M.conj().T)) for M in (M0, M1, M2)],
        "gauge_covariance_residual": float(gauge_residual),
        "spectra": spectra,
    }


def build_report():
    return {
        "supergolden": run_case(PSI_SG, False),
        "regular_control": run_case(PHI, True),
        "construction": {
            "nodal_normal": "area-weighted sum of incident oriented triangle normals, normalized",
            "face_centres": "the 12 centroid normals coincide with the polar-face Gauss-map normals used in T155",
            "link": "minimal SO(3) rotation between nodal normals, projected to the local SO(2) frames",
            "D0": "(D0_A u)_ij = u_j - U_ij u_i, with the edge value in the fibre at j",
            "D1": "(D1_A c)_ijk = U_ji c_ij + U_ki c_jk + c_ki, based at vertex i",
            "curvature": "D1_A D0_A u = (1-H_ijk) U_ji u_j, H_ijk=U_ij U_jk U_ki",
            "masses": "link-transported local Whitney M0/M1 blocks; M2_T=1/area(T)",
            "scope": "finite link-covariant Whitney model; non-flat curved cochain sequence, not a cochain complex",
        },
    }


def main():
    report = build_report()
    for case in (report["supergolden"], report["regular_control"]):
        assert case["counts"] == [32, 90, 60]
        assert case["minimum_frame_projection_norm"] > 0.1
        assert case["centroid_normal_T155_residual"] < TOL
        assert case["T155_face_link_residual"] < TOL
        assert case["link_orthogonality_residual"] < TOL
        assert case["link_determinant_residual"] < TOL
        assert case["antipodal_normal_residual"] < TOL
        assert case["antipodal_link_covariance_residual"] < TOL
        assert case["gauss_bonnet_4pi_residual"] < TOL
        assert case["holonomy_spherical_area_residual"] < TOL
        assert case["D1D0_norm"] > 1e-4
        assert case["curvature_identity_residual"] < TOL
        assert min(case["mass_minimum_eigenvalues"]) > 0
        assert max(case["mass_hermiticity_residuals"]) < TOL
        assert case["gauge_covariance_residual"] < TOL
        assert [len(case["spectra"][str(k)]) for k in range(3)] == [32, 90, 60]
    path = Path("results/json/t157_full_covariant_whitney_curvature.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
