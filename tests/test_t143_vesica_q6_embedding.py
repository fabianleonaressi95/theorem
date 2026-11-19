"""Regression tests for T143's six-state antipodal Q6 embedding."""

import unittest

from scripts.audit_t143_vesica_q6_embedding import run_audit


class T143VesicaQ6EmbeddingTests(unittest.TestCase):
    def test_isometry_intertwining_and_zero_extension(self):
        result = run_audit()
        self.assertEqual(result["status"], "PASS")
        self.assertLess(max(result["errors"].values()), 1e-10)
        self.assertTrue(result["parity_counts"]["complement_pairs"])
        self.assertEqual(result["parity_counts"]["even_codes"], 6)

    def test_embedded_and_full_space_ranks(self):
        result = run_audit()
        self.assertEqual(result["ranks"]["embedded_X_even_to_odd"], 3)
        self.assertEqual(result["ranks"]["embedded_Y_even_to_odd"], 2)
        self.assertEqual(result["ranks"]["full_zero_extension_X"], 6)
        self.assertEqual(result["ranks"]["full_zero_extension_Y"], 4)
        self.assertEqual(result["ranks"]["orthogonal_complement_dimension"], 58)


if __name__ == "__main__":
    unittest.main()
