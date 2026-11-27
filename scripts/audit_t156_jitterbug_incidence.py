#!/usr/bin/env python3
"""Exhaustive incidence audit for the rhombicuboctahedron -> snub-cube split.

Uses T154's coordinate/hull reconstruction and NetworkX only for finite
vertex-face incidence graph isomorphism. No geometric motion is simulated.
"""
from itertools import product
from math import atan2
import networkx as nx

try:
    from scripts.audit_t154_in2infinity_geometry import (
        vertices_rhombic_cuboctahedron, vertices_snub_cube, audit,
        hull_faces, norm, sub,
    )
except ModuleNotFoundError:
    from audit_t154_in2infinity_geometry import (
        vertices_rhombic_cuboctahedron, vertices_snub_cube, audit,
        hull_faces, norm, sub,
    )


def incidence_graph(n_vertices, faces):
    graph = nx.Graph()
    for i in range(n_vertices):
        graph.add_node(("v", i), kind="vertex")
    for j, face in enumerate(faces):
        graph.add_node(("f", j), kind="face", size=len(face))
        for vertex in face:
            graph.add_edge(("v", vertex), ("f", j))
    return graph


def face_edges(face, vertices, tol=1e-6):
    return {
        tuple(sorted((i, j)))
        for p, i in enumerate(face)
        for j in face[p + 1 :]
        if abs(norm(sub(vertices[i], vertices[j])) - 1.0) < tol
    }


def cyclic_square(face, vertices):
    centre = tuple(sum(vertices[i][k] for i in face) / 4.0 for k in range(3))
    a, b, c = (vertices[i] for i in face[:3])
    u0 = sub(a, centre)
    u = tuple(x / norm(u0) for x in u0)
    ab, ac = sub(b, a), sub(c, a)
    n0 = (ab[1]*ac[2]-ab[2]*ac[1],
          ab[2]*ac[0]-ab[0]*ac[2],
          ab[0]*ac[1]-ab[1]*ac[0])
    n = tuple(x / norm(n0) for x in n0)
    v = (n[1]*u[2]-n[2]*u[1],
         n[2]*u[0]-n[0]*u[2],
         n[0]*u[1]-n[1]*u[0])
    angles = []
    for i in face:
        d = sub(vertices[i], centre)
        angles.append((atan2(sum(d[k]*v[k] for k in range(3)),
                             sum(d[k]*u[k] for k in range(3))), i))
    return [i for _, i in sorted(angles)]


def split_faces(rc_vertices, rc_faces, bits):
    triangles = [f for f in rc_faces if len(f) == 3]
    squares = [f for f in rc_faces if len(f) == 4]
    tri_edges = set().union(*(face_edges(f, rc_vertices) for f in triangles))
    lateral = [f for f in squares if face_edges(f, rc_vertices) & tri_edges]
    caps = [f for f in squares if not (face_edges(f, rc_vertices) & tri_edges)]
    assert len(triangles) == 8 and len(lateral) == 12 and len(caps) == 6
    ordered = [cyclic_square(f, rc_vertices) for f in lateral]
    out = list(triangles) + list(caps)
    for f, bit in zip(ordered, bits):
        if bit == 0:
            out.extend(((f[0], f[1], f[2]), (f[0], f[2], f[3])))
        else:
            out.extend(((f[1], f[2], f[3]), (f[1], f[3], f[0])))
    return out


def run_audit():
    rc_raw = vertices_rhombic_cuboctahedron()
    snub_raw = vertices_snub_cube()
    rc_edge = min(norm(sub(a, b)) for i, a in enumerate(rc_raw) for b in rc_raw[i+1:])
    snub_edge = min(norm(sub(a, b)) for i, a in enumerate(snub_raw) for b in snub_raw[i+1:])
    rc = [tuple(x / rc_edge for x in p) for p in rc_raw]
    snub = [tuple(x / snub_edge for x in p) for p in snub_raw]
    rc_faces = list(hull_faces(rc).keys())
    snub_faces = list(hull_faces(snub).keys())
    target = incidence_graph(24, snub_faces)
    node_match = nx.algorithms.isomorphism.categorical_node_match(
        ("kind", "size"), (None, None)
    )
    solutions = []
    for bits in product((0, 1), repeat=12):
        graph = incidence_graph(24, split_faces(rc, rc_faces, bits))
        if nx.is_isomorphic(graph, target, node_match=node_match):
            solutions.append("".join(map(str, bits)))
    assert solutions == ["010101010101", "101010101010"], solutions
    return {
        "assignments_tested": 4096,
        "incidence_isomorphism_count": len(solutions),
        "patterns": solutions,
        "split_square_count": 12,
        "retained_square_count": 6,
    }


if __name__ == "__main__":
    print(run_audit())
    print("T156 exhaustive incidence audit: PASS")
