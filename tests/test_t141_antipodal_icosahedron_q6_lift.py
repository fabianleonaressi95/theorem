import unittest
from scripts.audit_t141_antipodal_icosahedron_q6_lift import (
    ANTIPODES, Q6_CODES, Q6_MASK, audit, hull_edges, q6_path,
)


class TestT141AntipodalLift(unittest.TestCase):
    def test_injective_even_code_assignment(self):
        self.assertEqual(len(set(Q6_CODES)), 12)
        self.assertTrue(all(c.bit_count() % 2 == 0 for c in Q6_CODES))

    def test_vertex_antipodal_equivariance(self):
        for v in range(12):
            self.assertEqual(Q6_CODES[ANTIPODES[v]], Q6_CODES[v] ^ Q6_MASK)

    def test_all_icosahedron_edges_have_even_paths(self):
        _, edges = hull_edges()
        self.assertEqual(len(edges), 30)
        for u, v in edges:
            self.assertIn(len(q6_path(u, v)) - 1, (2, 4))

    def test_path_antipodal_equivariance(self):
        _, edges = hull_edges()
        for u, v in edges:
            p = q6_path(u, v)
            jp = q6_path(ANTIPODES[u], ANTIPODES[v])
            self.assertEqual(jp, tuple(x ^ Q6_MASK for x in p))

    def test_boundary_and_audit(self):
        result = audit()
        self.assertEqual((result["vertices"], result["edges"]), (12, 30))
        self.assertTrue(result["antipodal_equivariance"])


if __name__ == "__main__":
    unittest.main()
