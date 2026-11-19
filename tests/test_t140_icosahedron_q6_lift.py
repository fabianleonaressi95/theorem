import unittest
from scripts.audit_t140_icosahedron_q6_lift import Q6_CODES, lift


class TestT140Lift(unittest.TestCase):
    def test_vertex_injection_and_parity(self):
        self.assertEqual(len(set(Q6_CODES)), 12)
        self.assertTrue(all(x.bit_count() % 2 == 0 for x in Q6_CODES))

    def test_all_edges_have_two_step_lifts(self):
        result = lift()
        self.assertEqual(result["vertices"], 12)
        self.assertEqual(result["edges"], 30)
        self.assertEqual(len(result["paths"]), 30)
        for (u, v), (a, z, b) in result["paths"].items():
            self.assertEqual((a ^ z).bit_count(), 1)
            self.assertEqual((z ^ b).bit_count(), 1)
            self.assertEqual(a, Q6_CODES[u])
            self.assertEqual(b, Q6_CODES[v])

    def test_chain_boundary(self):
        for (u, v), (a, z, b) in lift()["paths"].items():
            self.assertEqual((a, z, b)[-1], Q6_CODES[v])
            self.assertEqual((a, z, b)[0], Q6_CODES[u])

    def test_antipodal_equivariance_is_not_claimed(self):
        self.assertFalse(lift()["antipodal_equivariance"])


if __name__ == "__main__":
    unittest.main()
