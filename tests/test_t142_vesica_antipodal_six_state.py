"""Regression tests for the exact finite model recorded in T142."""

import math
import unittest

from scripts.audit_t142_vesica_antipodal_six_state import run_audit


class T142AntipodalSixStateTests(unittest.TestCase):
    def test_finite_operator_identities_and_block_ranks(self):
        result = run_audit()
        self.assertEqual(result["point_count"], 6)
        self.assertEqual(result["status"], "PASS")
        self.assertLess(result["max_identity_error"], 1e-10)
        self.assertLess(result["coefficient_error"], 1e-10)
        self.assertEqual(result["block_ranks"]["rank(P-X-P+)"], 3)
        self.assertEqual(result["block_ranks"]["rank(P-Y-P+)"], 2)

    def test_exact_block_coefficients(self):
        result = run_audit()
        self.assertAlmostEqual(result["block_coefficients_X"][0], 1.0)
        self.assertAlmostEqual(result["block_coefficients_X"][1], -0.5)
        self.assertAlmostEqual(result["block_coefficients_X"][2], -0.5)
        self.assertAlmostEqual(result["block_coefficients_Y"][0], 0.0)
        self.assertAlmostEqual(result["block_coefficients_Y"][1],
                               math.sqrt(3.0) / 2.0)
        self.assertAlmostEqual(result["block_coefficients_Y"][2],
                               -math.sqrt(3.0) / 2.0)


if __name__ == "__main__":
    unittest.main()
