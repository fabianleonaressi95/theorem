import unittest
import numpy as np

from scripts.audit_t143b_original_archive_q6_plaquettes import (
    P, canonical_links, q6_coordinate_squares, build_edge_lookup,
    ordered_holonomy,
)


class T143BQ6PlaquetteTests(unittest.TestCase):
    def fixture(self):
        rng = np.random.default_rng(14307)
        normals = np.zeros((64, 3), dtype=float)
        for g in range(64):
            h = g ^ 7
            if g < h:
                v = rng.normal(size=3)
                v /= np.linalg.norm(v)
                normals[g] = v
                normals[h] = -v
        edges = []
        for g in range(64):
            for d in range(6):
                h = g ^ (1 << d)
                if g < h:
                    edges.append((g, h, d))
        return normals, np.asarray(edges, dtype=int)

    def test_all_240_coordinate_squares_and_antipodal_holonomy(self):
        normals, edges = self.fixture()
        squares, lookup = q6_coordinate_squares(edges)
        self.assertEqual(squares.shape, (240, 4))
        self.assertEqual(len({tuple(sorted(s)) for s in squares}), 240)

        r_links, u_links, _ = canonical_links(normals, edges)
        for cycle in squares:
            image = cycle ^ 7
            r0 = ordered_holonomy(cycle, r_links, lookup, spin=False)
            rp = ordered_holonomy(image, r_links, lookup, spin=False)
            u0 = ordered_holonomy(cycle, u_links, lookup, spin=True)
            up = ordered_holonomy(image, u_links, lookup, spin=True)
            self.assertLess(np.linalg.norm(rp-r0), 1e-12)
            self.assertLess(np.linalg.norm(up-u0), 1e-12)

    def test_anti_twin_is_a_fixed_point_free_involution(self):
        self.assertTrue(np.array_equal(P[P], np.arange(64)))
        self.assertTrue(np.all(P != np.arange(64)))
        normals, edges = self.fixture()
        self.assertEqual(len(build_edge_lookup(edges)), 192)
        self.assertTrue(np.allclose(normals[P], -normals))


if __name__ == "__main__":
    unittest.main()
