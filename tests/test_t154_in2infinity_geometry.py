import unittest

from scripts.audit_t154_in2infinity_geometry import (
    cuboctahedron_vertices,
    dist2,
    polar_rhombic_dodecahedron_vertices,
)
from itertools import combinations


class T154CoordinateTests(unittest.TestCase):
    def test_cuboctahedron_vertices_and_edges(self):
        vertices = cuboctahedron_vertices()
        self.assertEqual(len(vertices), 12)
        edges = [(p, q) for p, q in combinations(vertices, 2) if dist2(p, q) == 2]
        self.assertEqual(len(edges), 24)

    def test_polar_vertex_count(self):
        self.assertEqual(len(polar_rhombic_dodecahedron_vertices()), 14)


if __name__ == "__main__":
    unittest.main()
