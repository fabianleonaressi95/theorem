#!/usr/bin/env python3
"""Exact finite checks for the coordinate model in T154 (no external packages)."""
from itertools import product, combinations
from math import sqrt


def cuboctahedron_vertices():
    out = set()
    for a, b in product((-1, 1), repeat=2):
        out.add((a, b, 0))
        out.add((a, 0, b))
        out.add((0, a, b))
    return sorted(out)


def dist2(p, q):
    return sum((x-y)**2 for x, y in zip(p, q))


def polar_rhombic_dodecahedron_vertices():
    out = set()
    for axis in range(3):
        for sign in (-1, 1):
            v = [0, 0, 0]
            v[axis] = sign
            out.add(tuple(v))
    for signs in product((-1, 1), repeat=3):
        out.add(tuple(s/2 for s in signs))
    return sorted(out)


def main():
    vertices = cuboctahedron_vertices()
    edges = [(p, q) for p, q in combinations(vertices, 2) if dist2(p, q) == 2]
    assert len(vertices) == 12
    assert len(edges) == 24
    assert all(dist2(p, q) == 2 for p, q in edges)

    # Face-pyramid volume contributions: 8 regular tetrahedra and 6 square pyramids.
    tetra_volume = 1.0 / 3.0  # regular tetrahedron, edge sqrt(2)
    square_pyramid_volume = 2.0 / 3.0  # base area 2, height 1
    total = 8*tetra_volume + 6*square_pyramid_volume
    assert abs(total - 20.0/3.0) < 1e-14

    polar_vertices = polar_rhombic_dodecahedron_vertices()
    assert len(polar_vertices) == 14
    # The polar inequalities are |x_i|+|x_j| <= 1 for each coordinate pair.
    for p in polar_vertices:
        assert all(abs(p[i]) + abs(p[j]) <= 1 + 1e-14
                   for i, j in ((0, 1), (0, 2), (1, 2)))

    print("T154 coordinate checks: PASS")
    print(f"cuboctahedron: V={len(vertices)}, E={len(edges)}, edge=sqrt(2)")
    print("face-pyramid volume: 8*(1/3) + 6*(2/3) = 20/3")
    print(f"polar rhombic dodecahedron: V={len(polar_vertices)}")


if __name__ == "__main__":
    main()
