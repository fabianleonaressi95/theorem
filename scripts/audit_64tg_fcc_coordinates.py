#!/usr/bin/env python3
"""Reconstruct the Galeffi 64-TG as a finite FCC (D3) lattice patch.

Exact coordinate convention:
    x(n) = a/(2*sqrt(2)) * n,  n in Z^3, -2 <= n_i <= 2,
    n_1+n_2+n_3 even.

All distances are exact integer squared distances before the common scale.
No floating-point geometry is needed for the incidence audit.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from math import sqrt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "64tg_fcc_coordinates.json"


def sqdist(p, q):
    return sum((p[i] - q[i]) ** 2 for i in range(3))


def build_model():
    points = sorted(
        p for p in product(range(-2, 3), repeat=3)
        if sum(p) % 2 == 0
    )
    point_set = set(points)

    edges = sorted(
        (p, q)
        for p, q in combinations(points, 2)
        if sqdist(p, q) == 2
    )
    adjacency = {p: set() for p in points}
    for p, q in edges:
        adjacency[p].add(q)
        adjacency[q].add(p)

    tetrahedra = []
    for p in points:
        for q in sorted(v for v in adjacency[p] if v > p):
            common_pq = adjacency[p] & adjacency[q]
            for r in sorted(v for v in common_pq if v > q):
                common_pqr = common_pq & adjacency[r]
                for s in sorted(v for v in common_pqr if v > r):
                    tetrahedra.append((p, q, r, s))
    tetrahedra = sorted(tetrahedra)

    # The 14 edge-a/2 octahedra: six axial centres and eight cube-corner centres.
    octahedra = []
    for c in product((-1, 0, 1), repeat=3):
        if sum(c) % 2:
            vertices = []
            for axis in range(3):
                for sign in (-1, 1):
                    v = list(c)
                    v[axis] += sign
                    vertices.append(tuple(v))
            octahedra.append({"center_n": c, "vertices_n": sorted(vertices)})
    octahedra.sort(key=lambda x: x["center_n"])

    # The 24 square pyramids: four bases on each of the six square
    # faces of the edge-a cuboctahedron; each has one inward apex.
    pyramids = []
    for axis in range(3):
        for sign in (-2, 2):
            face_points = [p for p in points if p[axis] == sign]
            for base in combinations(face_points, 4):
                ds = [sqdist(u, v) for u, v in combinations(base, 2)]
                if Counter(ds) != Counter({2: 4, 4: 2}):
                    continue
                apices = [
                    p for p in points if p not in base
                    and all(sqdist(p, q) == 2 for q in base)
                ]
                if len(apices) != 1:
                    continue
                pyramids.append({
                    "face_axis": axis,
                    "face_sign": sign,
                    "base_n": sorted(base),
                    "apex_n": apices[0],
                })
    pyramids.sort(key=lambda x: (x["face_axis"], x["face_sign"], x["base_n"]))

    # Every regular tetrahedron has its circumcentre at its vertex average
    # and circumradius a*sqrt(6)/8. Store centres in exact n/4 coordinates.
    circumspheres = []
    center_numerators = []
    for index, tet in enumerate(tetrahedra):
        numerator = tuple(sum(p[i] for p in tet) for i in range(3))
        center_numerators.append(numerator)
        circumspheres.append({
            "tetrahedron_index": index,
            "center_n_numerator": numerator,
            "center_n_denominator": 4,
            "radius_over_a": "sqrt(6)/8",
        })

    # Equal-radius circumsphere balls overlap iff squared centre distance
    # in n-coordinates is < 3. The denominator 16 comes from centres n/4.
    lens_pairs = []
    center_adjacency = {i: set() for i in range(len(tetrahedra))}
    for i, j in combinations(range(len(tetrahedra)), 2):
        d2_num = sum(
            (center_numerators[i][k] - center_numerators[j][k]) ** 2
            for k in range(3)
        )
        if d2_num < 48:
            d2_n = d2_num // 16
            lens_pairs.append({
                "tetrahedron_indices": [i, j],
                "center_distance_squared_n": d2_n,
            })
            center_adjacency[i].add(j)
            center_adjacency[j].add(i)

    # A triple of equal balls has a common point for each 3-clique here.
    # The only triangle types are right isosceles (R_min^2=1/2) and
    # equilateral (R_min^2=2/3), both below the ball-radius square 3/4
    # in n-units. These are the canonical triple-overlap/triveca candidates.
    triple_overlaps = []
    for i, j, k in combinations(range(len(tetrahedra)), 3):
        if j not in center_adjacency[i] or k not in center_adjacency[i] or k not in center_adjacency[j]:
            continue
        d2s = []
        for u, v in ((i, j), (i, k), (j, k)):
            d2_num = sum(
                (center_numerators[u][m] - center_numerators[v][m]) ** 2
                for m in range(3)
            )
            d2s.append(d2_num // 16)
        shape = tuple(sorted(d2s))
        if shape == (1, 1, 2):
            min_enclosing_radius_squared_n = "1/2"
        elif shape == (2, 2, 2):
            min_enclosing_radius_squared_n = "2/3"
        else:
            raise AssertionError(f"Unexpected triple-overlap shape: {shape}")
        triple_overlaps.append({
            "tetrahedron_indices": [i, j, k],
            "pairwise_center_distances_squared_n": list(shape),
            "common_intersection_certificate_radius_squared_n": min_enclosing_radius_squared_n,
        })

    cuboctahedron_vertices = [
        p for p in points if sorted(abs(x) for x in p) == [0, 2, 2]
    ]
    cube_vertices = [
        p for p in points if all(abs(x) == 2 for x in p)
    ]
    inside_tets = [
        t for t in tetrahedra
        if all(sum(abs(x) for x in p) <= 4 for p in t)
    ]
    outside_tets = [t for t in tetrahedra if t not in set(inside_tets)]

    # Exact uniform-volume barycentres and covariance tensors.
    # Covariances are expressed relative to a^2 in physical orthonormal axes.
    cell_moments = {
        "tetrahedra": [
            {
                "index": i,
                "centroid_n_numerator": tuple(sum(p[k] for p in tet) for k in range(3)),
                "centroid_n_denominator": 4,
                "covariance_over_a2_diagonal": ["1/160", "1/160", "1/160"],
            }
            for i, tet in enumerate(tetrahedra)
        ],
        "octahedra": [
            {
                "index": i,
                "centroid_n": octa["center_n"],
                "covariance_over_a2_diagonal": ["1/80", "1/80", "1/80"],
            }
            for i, octa in enumerate(octahedra)
        ],
        "square_pyramids": [
            {
                "index": i,
                "centroid_n_numerator": tuple(
                    3 * sum(p[k] for p in pyr["base_n"]) + 4 * pyr["apex_n"][k]
                    for k in range(3)
                ),
                "centroid_n_denominator": 16,
                "covariance_over_a2_diagonal": [
                    "3/640" if k == pyr["face_axis"] else "1/80"
                    for k in range(3)
                ],
            }
            for i, pyr in enumerate(pyramids)
        ],
    }

    return {
        "points": points,
        "edges": edges,
        "tetrahedra": tetrahedra,
        "inside_tetrahedra": inside_tets,
        "outside_tetrahedra": outside_tets,
        "octahedra": octahedra,
        "pyramids": pyramids,
        "circumspheres": circumspheres,
        "lens_pairs": lens_pairs,
        "triple_overlaps": triple_overlaps,
        "cell_moments": cell_moments,
        "cuboctahedron_vertices": sorted(cuboctahedron_vertices),
        "cube_vertices": sorted(cube_vertices),
    }


def face_incidence(model):
    faces = []
    for tet in model["inside_tetrahedra"]:
        faces.extend(tuple(sorted(f)) for f in combinations(tet, 3))

    for octa in model["octahedra"]:
        c = octa["center_n"]
        for signs in product((-1, 1), repeat=3):
            tri = []
            for axis, sign in enumerate(signs):
                v = list(c)
                v[axis] += sign
                tri.append(tuple(v))
            faces.append(tuple(sorted(tri)))

    for pyr in model["pyramids"]:
        base = pyr["base_n"]
        apex = pyr["apex_n"]
        faces.append(tuple(sorted(base)))
        for u, v in combinations(base, 2):
            if sqdist(u, v) == 2:
                faces.append(tuple(sorted((u, v, apex))))
    return Counter(faces)


def audit(model):
    assert len(model["points"]) == 63
    assert len(model["edges"]) == 240
    assert len(model["tetrahedra"]) == 64
    assert len(model["inside_tetrahedra"]) == 56
    assert len(model["outside_tetrahedra"]) == 8
    assert len(model["cuboctahedron_vertices"]) == 12
    assert len(model["cube_vertices"]) == 8
    assert len(model["octahedra"]) == 14
    assert len(model["pyramids"]) == 24
    assert len(model["circumspheres"]) == 64
    assert len({tuple(x["center_n_numerator"]) for x in model["circumspheres"]}) == 64
    assert len(model["lens_pairs"]) == 360
    assert len(model["triple_overlaps"]) == 648
    assert len(model["cell_moments"]["tetrahedra"]) == 64
    assert len(model["cell_moments"]["octahedra"]) == 14
    assert len(model["cell_moments"]["square_pyramids"]) == 24

    for edge in model["edges"]:
        assert sqdist(*edge) == 2
    for tet in model["tetrahedra"]:
        assert all(sqdist(u, v) == 2 for u, v in combinations(tet, 2))

    for octa in model["octahedra"]:
        c = octa["center_n"]
        vertices = octa["vertices_n"]
        assert len(vertices) == 6
        assert all(sqdist(u, v) in (2, 4) for u, v in combinations(vertices, 2))
        assert Counter(sqdist(u, v) for u, v in combinations(vertices, 2)) == Counter({2: 12, 4: 3})
        assert all(sum(abs(x) for x in p) <= 4 for p in vertices)

    for pyr in model["pyramids"]:
        base, apex = pyr["base_n"], pyr["apex_n"]
        assert Counter(sqdist(u, v) for u, v in combinations(base, 2)) == Counter({2: 4, 4: 2})
        assert all(sqdist(apex, u) == 2 for u in base)

    incidence = face_incidence(model)
    assert len(incidence) == 256
    assert Counter(incidence.values()) == Counter({1: 56, 2: 200})
    assert all(k in (1, 2) for k in incidence.values())

    # Each of the 14 octahedra has all eight triangular faces shared
    # with tetrahedron faces in the reconstructed tetrahedral complex.
    tet_faces = {
        tuple(sorted(f))
        for tet in model["tetrahedra"]
        for f in combinations(tet, 3)
    }
    for octa in model["octahedra"]:
        c = octa["center_n"]
        for signs in product((-1, 1), repeat=3):
            tri = []
            for axis, sign in enumerate(signs):
                v = list(c)
                v[axis] += sign
                tri.append(tuple(v))
            assert tuple(sorted(tri)) in tet_faces

    return {
        "vertices": len(model["points"]),
        "edges": len(model["edges"]),
        "tetrahedra": len(model["tetrahedra"]),
        "tetrahedra_inside_cuboctahedron": len(model["inside_tetrahedra"]),
        "tetrahedra_outside_cuboctahedron": len(model["outside_tetrahedra"]),
        "cuboctahedron_vertices": len(model["cuboctahedron_vertices"]),
        "cube_vertices": len(model["cube_vertices"]),
        "octahedral_cavities": len(model["octahedra"]),
        "square_pyramidal_cavities": len(model["pyramids"]),
        "tetrahedron_circumspheres": len(model["circumspheres"]),
        "pairwise_circumsphere_lenses": len(model["lens_pairs"]),
        "common_triple_ball_intersections": len(model["triple_overlaps"]),
        "cell_moment_records": sum(len(v) for v in model["cell_moments"].values()),
        "cell_face_incidences": dict(sorted(Counter(incidence.values()).items())),
        "boundary_facets_by_size": dict(sorted(Counter(
            len(face) for face, count in incidence.items() if count == 1
        ).items())),
    }


def serialise(model, audit_result):
    return {
        "title": "64-TG exact FCC/D3 coordinate reconstruction",
        "coordinate_convention": {
            "integer_lattice": "n in Z^3, -2 <= n_i <= 2, n1+n2+n3 even",
            "physical_coordinate": "x(n) = a/(2*sqrt(2)) * n",
            "reference_edge": "cuboctahedron edge a",
            "nearest_neighbour_squared_distance_n": 2,
            "nearest_neighbour_physical_distance": "a/2",
            "enclosing_cube_edge": "sqrt(2)*a",
        },
        "vertices_n": model["points"],
        "edges": model["edges"],
        "tetrahedra": model["tetrahedra"],
        "inside_tetrahedra": model["inside_tetrahedra"],
        "outside_tetrahedra": model["outside_tetrahedra"],
        "cuboctahedron_vertices_n": model["cuboctahedron_vertices"],
        "cube_vertices_n": model["cube_vertices"],
        "octahedra": model["octahedra"],
        "square_pyramids": model["pyramids"],
        "tetrahedron_circumspheres": model["circumspheres"],
        "pairwise_circumsphere_lenses": model["lens_pairs"],
        "common_triple_ball_intersections": model["triple_overlaps"],
        "uniform_cell_barycentres_and_covariances": model["cell_moments"],
        "audit": audit_result,
        "volume_identities": {
            "tetrahedron_edge_a_over_2": "sqrt(2)*a^3/96",
            "56_tetrahedra": "7*sqrt(2)*a^3/12",
            "one_octahedron_edge_a_over_2": "sqrt(2)*a^3/24",
            "14_octahedra": "7*sqrt(2)*a^3/12",
            "one_square_pyramid_base_a_over_2_height_sqrt2a_over_4": "sqrt(2)*a^3/48",
            "24_square_pyramids": "sqrt(2)*a^3/2",
            "cuboctahedron": "5*sqrt(2)*a^3/3",
        },
    }


def main():
    model = build_model()
    result = audit(model)
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(serialise(model, result), indent=2) + "\n")
    print(json.dumps(result, indent=2))
    print(f"Wrote {DATA}")


if __name__ == "__main__":
    main()
