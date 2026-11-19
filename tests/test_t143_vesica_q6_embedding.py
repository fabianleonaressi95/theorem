"""Regression tests for the geometrically antipodal T143 embedding."""
import unittest
from scripts.audit_t143_vesica_q6_embedding import (
    EXPECTED_REPRESENTATIVES, FREE_REPRESENTATIVES, REPRESENTATIVES, run_audit,
)

class T143VesicaQ6EmbeddingTests(unittest.TestCase):
    def test_canonical_pair_partition_and_free_count(self):
        self.assertEqual(REPRESENTATIVES, EXPECTED_REPRESENTATIVES)
        self.assertEqual(len(REPRESENTATIVES), 32)
        self.assertEqual(FREE_REPRESENTATIVES, (
            0, 1, 8, 10, 11, 16, 17, 18, 19, 24, 25, 26, 27,
            32, 33, 34, 35, 40, 41, 42, 43, 48, 49, 50, 51,
            56, 57, 58, 59,
        ))
        self.assertEqual(len(FREE_REPRESENTATIVES), 29)

    def test_isometry_intertwining_and_zero_extension(self):
        result = run_audit()
        self.assertEqual(result["status"], "PASS")
        self.assertLess(max(result["errors"].values()), 1e-10)
        self.assertTrue(result["pair_partition"])
        self.assertTrue(result["fixed_values"])

    def test_embedded_and_full_space_ranks(self):
        result = run_audit()
        self.assertEqual(result["ranks"], {
            "embedded_X_even_to_odd": 3, "embedded_Y_even_to_odd": 2,
            "zero_extension_X": 6, "zero_extension_Y": 4,
            "orthogonal_complement_dimension": 58,
        })

    def test_29_canonical_free_angles(self):
        result = run_audit()
        self.assertEqual(result["free_angle_count"], 29)
        self.assertEqual(result["free_representatives"], FREE_REPRESENTATIVES)

if __name__ == "__main__":
    unittest.main()
