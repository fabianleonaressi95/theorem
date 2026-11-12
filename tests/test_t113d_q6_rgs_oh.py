import unittest
import numpy as np

from scripts.audit_t113d_q6_rgs_oh import audit


class TestT113DQ6RGSOH(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = audit()

    def test_all_exact_structure_and_numerical_checks(self):
        self.assertTrue(self.report["all_checks_pass"], self.report["checks"])

    def test_icosahedral_orbit_action_is_not_assumed(self):
        induced = self.report["induced_Oh_action"]
        self.assertEqual(induced["permutations"], 48)
        self.assertEqual(induced["Q6_graph_automorphisms"], 16)
        self.assertEqual(induced["non_automorphisms"], 32)

    def test_reynolds_operator_is_distinct_from_q6(self):
        op = self.report["Oh_Reynolds_Q6_laplacian"]
        self.assertFalse(op["is_original_Q6_laplacian"])
        self.assertEqual(op["weighted_edges"], 288)
        self.assertTrue(op["max_Oh_invariance_residual"] < 1e-10)

    def test_two_involutions_are_not_conflated(self):
        inv = self.report["involutions"]
        self.assertEqual(inv["RGS_coordinate_inversion_mask"], 7)
        self.assertEqual(inv["Q6_graph_antipode_mask"], 63)
        self.assertGreater(inv["Q6_antipode_coordinate_residual"], 1e-6)


if __name__ == "__main__":
    unittest.main()
