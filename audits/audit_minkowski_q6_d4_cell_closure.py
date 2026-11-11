"""Exact audit of the D4 orbit closure of the RGS/Q6 cubical 2-skeleton.

The script constructs the D4 action on the six-bit labels, takes the orbit
of Q6 edges and square cycles, checks regular face intersections, and builds
integer boundary matrices and signed chain maps. It reports (rather than
assumes) whether the generated square family is a regular square complex.
"""
from __future__ import annotations

import json
from collections import defaultdict
from itertools import combinations

import numpy as np

from models.q6_topological_synchronization import build_q6_complex


def _r_vertex(v):
    b1, b2, b3, s1, s2, s3 = v
    return (b1, b2, b3 ^ b1 ^ b2, s2, 1 ^ s1, s3)


def _s_vertex(v):
    b1, b2, b3, s1, s2, s3 = v
    return (b1, b2, b3, 1 ^ s1, s2, s3)


def _permutation_from_vertex_map(K, fn):
    return tuple(K.vertex_index[fn(v)] for v in K.vertices)


def _compose(g, h):
    """Return g after h, with permutations stored as image tuples."""
    return tuple(g[h[i]] for i in range(len(g)))


def _generated_group(R, S):
    identity = tuple(range(len(R)))
    group = {identity}
    frontier = [identity]
    while frontier:
        g = frontier.pop()
        for generator in (R, S):
            for candidate in (_compose(generator, g), _compose(g, generator)):
                if candidate not in group:
                    group.add(candidate)
                    frontier.append(candidate)
    return tuple(sorted(group))


def _canonical_cycle(cycle):
    """Canonical unoriented cyclic order, modulo rotation and reversal."""
    cycle = tuple(cycle)
    forms = []
    for seq in (cycle, tuple(reversed(cycle))):
        forms.extend(seq[i:] + seq[:i] for i in range(len(seq)))
    return min(forms)


def _orientation_sign(cycle, canonical):
    cycle = tuple(cycle)
    canonical = tuple(canonical)
    n = len(cycle)
    for i in range(n):
        if cycle[i:] + cycle[:i] == canonical:
            return 1
    reverse = tuple(reversed(canonical))
    for i in range(n):
        if cycle[i:] + cycle[:i] == reverse:
            return -1
    raise AssertionError("cycles do not have the same cyclic boundary")


def _build_orbit_cells(K, group):
    edge_cells = set()
    face_by_vertices = {}
    incompatible_cycles = []

    for g in group:
        for u, v in K.edges:
            edge_cells.add(tuple(sorted((g[u], g[v]))))
        for face in K.faces:
            mapped = tuple(g[v] for v in face)
            vertex_key = frozenset(mapped)
            cycle_key = _canonical_cycle(mapped)
            previous = face_by_vertices.get(vertex_key)
            if previous is None:
                face_by_vertices[vertex_key] = cycle_key
            elif previous != cycle_key:
                incompatible_cycles.append({
                    "vertices": sorted(vertex_key),
                    "first_cycle": list(previous),
                    "second_cycle": list(cycle_key),
                })

    edges = tuple(sorted(edge_cells))
    faces = tuple(sorted(face_by_vertices.values()))
    return edges, faces, incompatible_cycles


def _intersection_audit(edges, faces):
    edge_set = {frozenset(e) for e in edges}
    face_edges = []
    vertex_to_faces = defaultdict(list)

    for i, face in enumerate(faces):
        f_edges = {
            frozenset((face[j], face[(j + 1) % 4]))
            for j in range(4)
        }
        face_edges.append(f_edges)
        for vertex in face:
            vertex_to_faces[vertex].append(i)

    candidate_pairs = set()
    for incident in vertex_to_faces.values():
        candidate_pairs.update(combinations(sorted(set(incident)), 2))

    bad = []
    for i, j in sorted(candidate_pairs):
        shared = set(faces[i]).intersection(faces[j])
        if not shared:
            continue
        if len(shared) == 1:
            continue
        if len(shared) == 2:
            edge = frozenset(shared)
            if edge in face_edges[i] and edge in face_edges[j] and edge in edge_set:
                continue
            bad.append({
                "faces": [i, j],
                "shared_vertices": sorted(shared),
                "reason": "two shared vertices are not a common boundary edge",
            })
            continue
        bad.append({
            "faces": [i, j],
            "shared_vertices": sorted(shared),
            "reason": "distinct square cells share three or more vertices",
        })
    return bad


def _boundary_matrices(edges, faces, n_vertices):
    edge_index = {e: i for i, e in enumerate(edges)}
    B1 = np.zeros((n_vertices, len(edges)), dtype=np.int64)
    for j, (u, v) in enumerate(edges):
        B1[u, j], B1[v, j] = -1, 1

    B2 = np.zeros((len(edges), len(faces)), dtype=np.int64)
    for j, face in enumerate(faces):
        for u, v in zip(face, face[1:] + face[:1]):
            e = tuple(sorted((u, v)))
            if e not in edge_index:
                raise AssertionError("a square boundary edge is absent from the edge orbit")
            B2[edge_index[e], j] += 1 if u < v else -1
    return B1, B2, edge_index


def _chain_maps(group, edges, faces, edge_index, n_vertices):
    face_index = {frozenset(f): i for i, f in enumerate(faces)}
    results = []
    for g in group:
        J0 = np.zeros((n_vertices, n_vertices), dtype=np.int64)
        J1 = np.zeros((len(edges), len(edges)), dtype=np.int64)
        J2 = np.zeros((len(faces), len(faces)), dtype=np.int64)

        for i in range(n_vertices):
            J0[g[i], i] = 1

        for i, (u, v) in enumerate(edges):
            gu, gv = g[u], g[v]
            target = edge_index[tuple(sorted((gu, gv)))]
            J1[target, i] = 1 if gu < gv else -1

        for i, face in enumerate(faces):
            mapped = tuple(g[v] for v in face)
            target = face_index[frozenset(mapped)]
            sign = _orientation_sign(mapped, faces[target])
            J2[target, i] = sign

        results.append((J0, J1, J2))
    return results


def run_audit():
    K = build_q6_complex()
    R = _permutation_from_vertex_map(K, _r_vertex)
    S = _permutation_from_vertex_map(K, _s_vertex)
    identity = tuple(range(64))
    R2 = _compose(R, R)
    R4 = _compose(R2, R2)
    S2 = _compose(S, S)
    SRS = _compose(S, _compose(R, S))
    R_inverse = tuple(R.index(i) for i in range(64))
    group = _generated_group(R, S)

    group_relations = (
        R4 == identity and S2 == identity and SRS == R_inverse
    )
    if not group_relations or len(group) != 8:
        raise AssertionError("the six-bit maps do not generate the expected D4 action")

    edges, faces, incompatible_cycles = _build_orbit_cells(K, group)
    B1, B2, edge_index = _boundary_matrices(edges, faces, len(K.vertices))
    boundary_zero = bool(np.count_nonzero(B1 @ B2) == 0)
    bad_intersections = _intersection_audit(edges, faces)
    chain_maps = _chain_maps(group, edges, faces, edge_index, len(K.vertices))

    chain_map_checks = []
    for J0, J1, J2 in chain_maps:
        chain_map_checks.append(
            bool(np.array_equal(J0 @ B1, B1 @ J1)
                 and np.array_equal(J1 @ B2, B2 @ J2))
        )

    # The standard basis directions and their D4 images are computed exactly
    # over F_2, then counted as undirected translation edges.
    directions = set()
    zero = (0, 0, 0, 0, 0, 0)
    for g in group:
        image_zero = g[K.vertex_index[zero]]
        for axis in range(6):
            e = [0] * 6
            e[axis] = 1
            image_e = g[K.vertex_index[tuple(e)]]
            directions.add(tuple(a ^ b for a, b in zip(
                K.vertices[image_zero], K.vertices[image_e]
            )))

    return {
        "audit": "M3_D4_Q6_CELL_ORBIT_CLOSURE_V1",
        "group": {
            "order": len(group),
            "R4_identity": R4 == identity,
            "S2_identity": S2 == identity,
            "SRS_R_inverse": SRS == R_inverse,
        },
        "graph_orbit": {
            "vertices": len(K.vertices),
            "directions": [list(d) for d in sorted(directions)],
            "direction_count": len(directions),
            "edges": len(edges),
            "degree_regular": len(edges) * 2 // len(K.vertices),
            "expected_directions": 8,
            "expected_edges": 256,
        },
        "square_orbit": {
            "distinct_faces": len(faces),
            "incompatible_cycles_on_same_vertex_set": len(incompatible_cycles),
            "non_regular_intersections": len(bad_intersections),
            "regular_square_complex": (
                len(incompatible_cycles) == 0 and len(bad_intersections) == 0
            ),
            "sample_incompatible_cycles": incompatible_cycles[:10],
            "sample_bad_intersections": bad_intersections[:10],
        },
        "chain_complex": {
            "B1_shape": list(B1.shape),
            "B2_shape": list(B2.shape),
            "B1B2_zero": boundary_zero,
            "all_eight_D4_chain_maps_exact": all(chain_map_checks),
            "chain_map_count": len(chain_map_checks),
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
