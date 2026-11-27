import unittest

from scripts.audit_q6_golden_zonotope_t161 import run_audit


class TestQ6GoldenZonotopeT161(unittest.TestCase):
    def test_golden_frame_is_orthogonal(self):
        result = run_audit()
        residuals = result["frame_residuals"]
        self.assertLess(residuals["parallel_orthonormal"], 1e-12)
        self.assertLess(residuals["perp_orthonormal"], 1e-12)
        self.assertLess(residuals["cross_orthogonal"], 1e-12)

    def test_six_generators_are_in_general_position(self):
        result = run_audit()
        self.assertEqual(result["generator_triple_count"], 20)
        self.assertTrue(result["all_generator_triples_independent_numerically"])
        self.assertGreater(
            result["minimum_absolute_generator_triple_determinant"], 1e-12
        )

    def test_q6_projection_and_antipodal_pairing(self):
        result = run_audit()
        self.assertEqual(result["q6_state_count"], 64)
        self.assertEqual(result["distinct_internal_projected_points_rounded_1e-12"], 64)
        self.assertLess(result["antipodal_pairing_max_residual"], 1e-12)
        self.assertLess(result["minkowski_sum_reconstruction_max_residual"], 1e-12)


if __name__ == "__main__":
    unittest.main()
