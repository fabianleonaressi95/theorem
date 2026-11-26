#!/usr/bin/env python3
"""T146: dodecahedron--Q6 dual-face barycentre lift and operator audit.

No fitted edge weights are used:
- the geometric dodecahedron is the polar dual of the T139 icosahedral hull;
- its metric edge weights are inverse squared Euclidean edge lengths;
- each dual vertex (icosahedral triangular face) maps to the equal barycentre
  of its three T141 Q6 vertex codes in R^64;
- the induced Q6 energy is B L_Q6 B^T.

The script deliberately reports spectral mismatches rather than tuning scales.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
import json
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull

PSI_SG = 1.465571231876768
PHI = (1.0 + np.sqrt(5.0)) / 2.0
Q6_CODES = np.asarray((3, 5, 58, 60, 9, 17, 46, 54, 33, 6, 57, 30), dtype=int)
Q6_MASK = 63
TOL = 2e-9


def icosa_vertices(t: float) -> np.ndarray:
    return np.asarray(
        [(0.0, a, b * t) for a in (-1.0, 1.0) for b in (-1.0, 1.0)]
        + [(a, b * t, 0.0) for a in (-1.0, 1.0) for b in (-1.0, 1.0)]
        + [(a * t, 0.0, b) for a in (-1.0, 1.0) for b in (-1.0, 1.0)],
        dtype=float,
    )


def dual_data(t: float):
    x = icosa_vertices(t)
    hull = ConvexHull(x)
    face_equations = {}
    for simplex, equation in zip(hull.simplices, hull.equations):
        face_equations[tuple(sorted(map(int, simplex)))] = equation
    faces = sorted(face_equations)
    face_index = {face: i for i, face in enumerate(faces)}

    dual_vertices = np.asarray([
        equation[:3] / (-equation[3])
        for equation in (face_equations[f] for f in faces)
    ])
    dual_edges = []
    for i, j in combinations(range(len(faces)), 2):
        if len(set(faces[i]).intersection(faces[j])) == 2:
            dual_edges.append((i, j))

    antipodal_vertex = []
    for point in x:
        hit = np.flatnonzero(np.linalg.norm(x + point, axis=1) < 1e-9)
        if len(hit) != 1:
            raise AssertionError("icosahedral antipode is not unique")
        antipodal_vertex.append(int(hit[0]))
    antipodal_face = []
    for face in faces:
        opposite = tuple(sorted(antipodal_vertex[v] for v in face))
        antipodal_face.append(face_index[opposite])

    return x, faces, dual_vertices, dual_edges, np.asarray(antipodal_face), np.asarray(antipodal_vertex)


def q6_laplacian() -> np.ndarray:
    L = np.zeros((64, 64), dtype=float)
    for state in range(64):
        for bit in range(6):
            neighbour = state ^ (1 << bit)
            L[state, state] += 1.0
            L[state, neighbour] -= 1.0
    return L


def barycentre_lift(faces) -> np.ndarray:
    """B[f,g]=1/3 when Q6 code g labels a vertex of icosahedral face f."""
    B = np.zeros((len(faces), 64), dtype=float)
    for i, face in enumerate(faces):
        for vertex in face:
            B[i, Q6_CODES[vertex]] += 1.0 / 3.0
    return B


def selected_q6_coisometry() -> np.ndarray:
    C = np.asarray([
        np.ones(8) / np.sqrt(8.0),
        np.asarray([7, 1, -3, -5, -5, -3, 1, 7]) / np.sqrt(168.0),
        np.asarray([1, -1, -1, 1, -1, 1, 1, -1]) / np.sqrt(8.0),
    ])
    E = np.zeros((9, 3), dtype=float)
    E[0, 0] = 1.0
    E[1, 1] = E[3, 1] = 1.0 / np.sqrt(2.0)
    E[2, 2] = E[6, 2] = 1.0 / np.sqrt(2.0)
    K = np.kron(C, C)
    F = np.zeros((3, 64), dtype=float)
    # Six-bit code convention: low three bits are L, high three bits are U.
    for code in range(64):
        left, upper = code & 7, (code >> 3) & 7
        F[:, code] = E.T @ K[:, left * 8 + upper]
    return F


def dodecahedron_face_boundaries(faces, dual_edges, anti_face, anti_vertex, S_dual):
    """Return the oriented 20x30 edge boundary and 30x12 face boundary."""
    edge_index = {tuple(edge): k for k, edge in enumerate(dual_edges)}
    D2 = np.zeros((len(dual_edges), 12), dtype=float)
    cycles = []
    for vertex in range(12):
        incident = [i for i, face in enumerate(faces) if vertex in face]
        adjacency = {
            i: [j for j in incident
                if j != i and len(set(faces[i]).intersection(faces[j])) == 2]
            for i in incident
        }
        if len(incident) != 5 or any(len(adjacency[i]) != 2 for i in incident):
            raise AssertionError("dual face around an icosahedral vertex is not a pentagon")
        start = min(incident)
        cycle = [start]
        previous, current = None, start
        nxt = min(adjacency[current])
        while nxt != start:
            cycle.append(nxt)
            previous, current = current, nxt
            nxt = next(q for q in adjacency[current] if q != previous)
            if len(cycle) > 5:
                raise AssertionError("pentagonal dual face did not close")
        if len(cycle) != 5:
            raise AssertionError("dual face boundary does not have five edges")
        cycles.append(cycle)
        for k in range(5):
            i, j = cycle[k], cycle[(k + 1) % 5]
            e = edge_index[tuple(sorted((i, j)))]
            D2[e, vertex] = 1.0 if i < j else -1.0

    if np.linalg.norm(S_dual @ D2) < 1e-12:
        raise AssertionError("unexpected zero antipodal action on face boundaries")
    S_dual2 = np.zeros((12, 12), dtype=float)
    for vertex in range(12):
        opposite = int(anti_vertex[vertex])
        image = S_dual @ D2[:, vertex]
        sign = float(np.dot(image, D2[:, opposite]) / 5.0)
        if abs(abs(sign) - 1.0) > 1e-10:
            raise AssertionError("antipodal map does not preserve/reverse a pentagonal boundary")
        S_dual2[opposite, vertex] = 1.0 if sign > 0 else -1.0
    return D2, S_dual2, cycles


def q6_square_complex(qedges, qindex):
    """All 240 oriented cubical 2-cells and their boundary matrix."""
    squares, square_index = [], {}
    for i in range(6):
        for j in range(i + 1, 6):
            for state in range(64):
                if ((state >> i) & 1) == 0 and ((state >> j) & 1) == 0:
                    square_index[(state, i, j)] = len(squares)
                    squares.append((state, i, j))
    boundary = np.zeros((len(qedges), len(squares)), dtype=float)
    for col, (state, i, j) in enumerate(squares):
        ei0 = qindex[(state, state ^ (1 << i))]
        ej_i = qindex[(state ^ (1 << i),
                       (state ^ (1 << i)) ^ (1 << j))]
        ei_j = qindex[(state ^ (1 << j),
                       (state ^ (1 << j)) ^ (1 << i))]
        ej0 = qindex[(state, state ^ (1 << j))]
        boundary[ei0, col] += 1.0
        boundary[ej_i, col] += 1.0
        boundary[ei_j, col] -= 1.0
        boundary[ej0, col] -= 1.0

    S_q1 = np.zeros((len(qedges), len(qedges)), dtype=float)
    for k, (u, v) in enumerate(qedges):
        S_q1[qindex[(v ^ Q6_MASK, u ^ Q6_MASK)], k] = -1.0

    S_q2 = np.zeros((len(squares), len(squares)), dtype=float)
    for k, (state, i, j) in enumerate(squares):
        opposite = state ^ Q6_MASK
        opposite &= ~(1 << i)
        opposite &= ~(1 << j)
        S_q2[square_index[(opposite, i, j)], k] = 1.0
    return squares, boundary, S_q1, S_q2


def q6_edge_complex():
    """Canonical oriented 1-cells g -> g xor 2^k, with bit k initially zero."""
    edges = []
    index = {}
    for state in range(64):
        for bit in range(6):
            if ((state >> bit) & 1) == 0:
                neighbour = state ^ (1 << bit)
                index[(state, neighbour)] = len(edges)
                edges.append((state, neighbour))
    boundary = np.zeros((64, len(edges)), dtype=float)
    for k, (u, v) in enumerate(edges):
        boundary[u, k] = -1.0
        boundary[v, k] = 1.0
    return edges, index, boundary


def dodecahedron_edge_chain_lift(faces, dual_edges, B, antipodal_face):
    """Antipodal-equivariant averaged-shortest-path lift of dual edges.

    For adjacent dual vertices f_i,f_j, the barycentre difference is
    (e_code(b)-e_code(a))/3 for the opposite primal vertices a,b.
    Average all shortest Q6 paths from code(a) to code(b), with coefficient
    1/3. Averaging over every bit-flip order makes the chain independent of
    an arbitrary path ordering and restores reversal/antipodal equivariance.
    """
    qedges, qindex, qboundary = q6_edge_complex()
    D = np.zeros((len(faces), len(dual_edges)), dtype=float)
    C = np.zeros((len(qedges), len(dual_edges)), dtype=float)
    path_lengths = Counter()

    for k, (i, j) in enumerate(dual_edges):
        D[i, k], D[j, k] = -1.0, 1.0
        fi, fj = set(faces[i]), set(faces[j])
        a = next(iter(fi - fj))
        b = next(iter(fj - fi))
        start, target = int(Q6_CODES[a]), int(Q6_CODES[b])
        bits = [bit for bit in range(6) if ((start ^ target) >> bit) & 1]
        orders = tuple(permutations(bits))
        path_lengths[len(bits)] += 1
        for order in orders:
            current = start
            coefficient = 1.0 / (3.0 * len(orders))
            for bit in order:
                nxt = current ^ (1 << bit)
                if (current, nxt) in qindex:
                    edge_index, sign = qindex[(current, nxt)], 1.0
                else:
                    edge_index, sign = qindex[(nxt, current)], -1.0
                C[edge_index, k] += sign * coefficient
                current = nxt
            if current != target:
                raise AssertionError("Q6 path did not reach its endpoint")

    boundary_residual = float(np.linalg.norm(qboundary @ C - B.T @ D))

    # Induced action on oriented dual edges, including orientation reversal.
    dual_edge_index = {tuple(edge): k for k, edge in enumerate(dual_edges)}
    S_dual = np.zeros((len(dual_edges), len(dual_edges)), dtype=float)
    for k, (i, j) in enumerate(dual_edges):
        ai, aj = int(antipodal_face[i]), int(antipodal_face[j])
        target_edge = tuple(sorted((ai, aj)))
        target_index = dual_edge_index[target_edge]
        S_dual[target_index, k] = 1.0 if ai < aj else -1.0

    # Complement reverses the canonical orientation of every Q6 edge.
    S_q6 = np.zeros((len(qedges), len(qedges)), dtype=float)
    for k, (u, v) in enumerate(qedges):
        target_edge = (v ^ Q6_MASK, u ^ Q6_MASK)
        S_q6[qindex[target_edge], k] = -1.0
    antipodal_residual = float(np.linalg.norm(S_q6 @ C - C @ S_dual))

    L_chain = D @ C.T @ C @ D.T
    L_chain = (L_chain + L_chain.T) / 2.0
    return (D, C, L_chain, boundary_residual, antipodal_residual,
            dict(sorted(path_lengths.items())), S_dual)


def weighted_laplacian(points: np.ndarray, edges):
    W = np.zeros((len(points), len(points)), dtype=float)
    lengths = []
    for i, j in edges:
        length = float(np.linalg.norm(points[i] - points[j]))
        if length <= 1e-12:
            raise AssertionError("collapsed dual edge")
        lengths.append(length)
        W[i, j] = W[j, i] = length ** -2
    return np.diag(W.sum(axis=1)) - W, np.asarray(lengths)


def audit(t: float = PSI_SG) -> dict:
    x, faces, dual, edges, anti_face, anti_vertex = dual_data(t)
    B = barycentre_lift(faces)
    Lq = q6_laplacian()
    L_induced = B @ Lq @ B.T
    L_induced = (L_induced + L_induced.T) / 2.0

    # Antipodal permutation on Q6 states.
    J = np.zeros((64, 64), dtype=float)
    for g in range(64):
        J[g, g ^ Q6_MASK] = 1.0

    # Polar-dual metric Laplacian, with no fitted weights.
    L_geom, edge_lengths = weighted_laplacian(dual, edges)

    # Chain-level lift: each dual edge is a scaled Q6 path with matching boundary.
    Ddual, Cedge, L_chain, chain_boundary_residual, chain_antipodal_residual, chain_path_lengths, S_dual = (
        dodecahedron_edge_chain_lift(faces, edges, B, anti_face)
    )

    # Complete the dodecahedral 2-skeleton into the cubical 2-skeleton of Q6.
    D2, S_dual2, dual_face_cycles = dodecahedron_face_boundaries(
        faces, edges, anti_face, anti_vertex, S_dual
    )
    qedges, qindex, qboundary = q6_edge_complex()
    squares, q2boundary, S_q1, S_q2 = q6_square_complex(qedges, qindex)
    q2_chain = np.linalg.pinv(q2boundary, rcond=1e-12) @ (Cedge @ D2)
    face_fill_residual = float(np.linalg.norm(q2boundary @ q2_chain - Cedge @ D2))
    face_fill_antipodal_residual = float(np.linalg.norm(S_q2 @ q2_chain - q2_chain @ S_dual2))
    dodecahedron_chain_complex_residual = float(np.linalg.norm(Ddual @ D2))
    q6_cubical_chain_complex_residual = float(np.linalg.norm(qboundary @ q2boundary))
    q6_square_antipodal_residual = float(np.linalg.norm(q2boundary @ S_q2 - S_q1 @ q2boundary))

    # Selected three-dimensional Q6 sector from the archived spectral map.
    F = selected_q6_coisometry()
    Lambda = np.diag([0.0, 4.0, 6.0])
    Phi = F @ B.T
    selected_residual = float(np.linalg.norm(Lambda @ Phi - Phi @ L_induced))
    selected_chain_residual = float(np.linalg.norm(Lambda @ Phi - Phi @ L_chain))

    eig_induced = np.linalg.eigvalsh(L_induced)
    eig_geom = np.linalg.eigvalsh(L_geom)
    eig_unweighted = np.linalg.eigvalsh(
        np.diag(np.asarray([sum(1 for e in edges if i in e) for i in range(20)]))
        - np.asarray([[1.0 if (i, j) in edges or (j, i) in edges else 0.0
                       for j in range(20)] for i in range(20)])
    )

    # The antipodal face map must be a graph automorphism and intertwine B with J.
    dual_edge_set = {tuple(sorted(e)) for e in edges}
    anti_edges_ok = all(
        tuple(sorted((int(anti_face[i]), int(anti_face[j])))) in dual_edge_set
        for i, j in edges
    )
    B_anti_residual = float(np.linalg.norm(B[anti_face] - B @ J))
    q6_eigen_residual = float(np.linalg.norm(F @ Lq - Lambda @ F))

    result = {
        "parameter": float(t),
        "icosahedron_vertices": len(x),
        "icosahedron_triangular_faces": len(faces),
        "dodecahedron_vertices": len(dual),
        "dodecahedron_edges": len(edges),
        "dodecahedron_vertex_degree_set": sorted({
            sum(i in edge for edge in edges) for i in range(len(dual))
        }),
        "antipodal_face_involution": bool(np.all(anti_face[anti_face] == np.arange(20))),
        "antipodal_dual_graph_automorphism": bool(anti_edges_ok),
        "face_barycentre_row_sum_residual": float(np.linalg.norm(B.sum(axis=1) - 1.0)),
        "face_barycentre_antipodal_residual": B_anti_residual,
        "barycentre_map_rank": int(np.linalg.matrix_rank(B, tol=1e-9)),
        "induced_q6_energy_rank": int(np.linalg.matrix_rank(L_induced, tol=1e-8)),
        "induced_q6_energy_eigenvalues": eig_induced.tolist(),
        "dodecahedron_q6_edge_chain_path_lengths": {
            str(k): int(v) for k, v in chain_path_lengths.items()
        },
        "dodecahedron_q6_edge_chain_boundary_residual": chain_boundary_residual,
        "dodecahedron_q6_edge_chain_antipodal_residual": chain_antipodal_residual,
        "dodecahedron_face_boundary_squared_zero_residual": dodecahedron_chain_complex_residual,
        "q6_cubical_boundary_squared_zero_residual": q6_cubical_chain_complex_residual,
        "dodecahedron_to_q6_face_fill_residual": face_fill_residual,
        "dodecahedron_to_q6_face_fill_antipodal_residual": face_fill_antipodal_residual,
        "dodecahedron_face_count": len(dual_face_cycles),
        "q6_cubical_square_count": len(squares),
        "q6_face_fill_rank": int(np.linalg.matrix_rank(q2_chain, tol=1e-9)),
        "q6_square_antipodal_boundary_residual": q6_square_antipodal_residual,
        "chain_induced_energy_rank": int(np.linalg.matrix_rank(L_chain, tol=1e-8)),
        "chain_induced_energy_eigenvalues": np.linalg.eigvalsh(L_chain).tolist(),
        "selected_q6_chain_energy_intertwining_residual": selected_chain_residual,
        "polar_dual_edge_length_classes": {
            str(k): int(v) for k, v in Counter(np.round(edge_lengths, 10)).items()
        },
        "polar_dual_metric_laplacian_eigenvalues": eig_geom.tolist(),
        "unweighted_dodecahedron_laplacian_eigenvalues": eig_unweighted.tolist(),
        "selected_q6_coisometry_rank": int(np.linalg.matrix_rank(F, tol=1e-9)),
        "dodecahedron_to_selected_q6_map_rank": int(np.linalg.matrix_rank(Phi, tol=1e-9)),
        "selected_q6_intertwining_residual": selected_residual,
        "selected_q6_operator_identity_residual": q6_eigen_residual,
        "nearest_induced_eigenvalue_to_4": float(np.min(np.abs(eig_induced - 4.0))),
        "nearest_induced_eigenvalue_to_6": float(np.min(np.abs(eig_induced - 6.0))),
        "nearest_geometric_eigenvalue_to_4": float(np.min(np.abs(eig_geom - 4.0))),
        "nearest_geometric_eigenvalue_to_6": float(np.min(np.abs(eig_geom - 6.0))),
    }

    checks = {
        "icosahedron_20_faces": len(faces) == 20,
        "dodecahedron_30_edges": len(edges) == 30,
        "cubic_dual_graph": result["dodecahedron_vertex_degree_set"] == [3],
        "antipodal_face_involution": result["antipodal_face_involution"],
        "antipodal_dual_graph_automorphism": result["antipodal_dual_graph_automorphism"],
        "barycentre_rows_normalized": result["face_barycentre_row_sum_residual"] < TOL,
        "barycentre_antipodal_equivariance": B_anti_residual < TOL,
        "selected_q6_sector_is_correct": q6_eigen_residual < TOL,
        "selected_q6_map_has_rank_3": result["dodecahedron_to_selected_q6_map_rank"] == 3,
        "induced_energy_is_psd": float(eig_induced.min()) > -TOL,
        "chain_induced_energy_is_psd": float(np.linalg.eigvalsh(L_chain).min()) > -TOL,
        "dodecahedron_edge_chain_boundary_commutes": chain_boundary_residual < TOL,
        "dodecahedron_edge_chain_antipodal_equivariance": chain_antipodal_residual < TOL,
        "dodecahedron_2_boundary_squared_zero": dodecahedron_chain_complex_residual < TOL,
        "q6_2_boundary_squared_zero": q6_cubical_chain_complex_residual < TOL,
        "dodecahedron_pentagons_fill_in_q6": face_fill_residual < TOL,
        "pentagon_fill_antipodal_equivariance": face_fill_antipodal_residual < TOL,
        "q6_square_boundary_antipodal_equivariance": q6_square_antipodal_residual < TOL,
        "polar_metric_energy_is_psd": float(eig_geom.min()) > -TOL,
    }
    result["checks"] = checks
    result["all_structural_checks_pass"] = bool(all(checks.values()))
    result["interpretation"] = (
        "The dual incidence, antipodal barycentre lift, and antipodal-equivariant Q6 chain map through dodecahedral 2-cells are valid. "
        "However, the canonical barycentre pullback, the Q6 path-chain energy, "
        "and the polar-dual inverse-square metric Laplacian do not produce the "
        "selected spectrum (0,4,6); the selected-sector intertwining tests fail. "
        "Thus these canonical constructions do not derive f."
    )
    if not result["all_structural_checks_pass"]:
        raise AssertionError(checks)
    return result


if __name__ == "__main__":
    report = audit()
    out = Path("results/json/dodecahedron_q6_dual_barycentre_audit_2026-11-24.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    for key, value in report.items():
        print(f"{key}: {value}")
    print(f"wrote {out}")
