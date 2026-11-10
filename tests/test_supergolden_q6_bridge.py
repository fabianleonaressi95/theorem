import unittest
import numpy as np

from scripts.audit_supergolden_q6_bridge import (
    A_PSI, M_TRIGRAM, P, audit, q6_antipodal_audit, supergolden_sequence
)


class TestSupergoldenQ6Bridge(unittest.TestCase):
    def test_supergolden_recurrence(self):
        s = supergolden_sequence(20)
        self.assertEqual(s[:8], [0, 0, 1, 1, 1, 2, 3, 4])
        for n in range(len(s) - 3):
            self.assertEqual(s[n + 3], s[n + 2] + s[n])

    def test_phase21_trigram_permutation_conjugacy(self):
        self.assertTrue(np.array_equal(P @ A_PSI @ P.T, M_TRIGRAM))
        self.assertTrue(np.array_equal(P.T @ P, np.eye(3, dtype=np.int64)))

    def test_antipode_is_not_bipartition_flip_for_q6(self):
        result = q6_antipodal_audit()
        self.assertEqual(result["antipodal_pairs"], 32)
        self.assertEqual(result["fixed_points"], 0)
        self.assertEqual(result["involution_failures"], 0)
        self.assertEqual(result["bipartition_even_odd"], [32, 32])
        self.assertEqual(result["antipode_changes_bipartition"], 0)

    def test_audit_keeps_missing_geometric_bridge_open(self):
        result = audit()
        self.assertTrue(result["supergolden"]["permutation_conjugacy_exact"])
        self.assertTrue(result["q6"]["axis_transfer_is_2I6_not_supergolden"])
        self.assertEqual(
            result["classification"]["q6_midpoint_to_supergolden_intertwiner"],
            "NOT_ESTABLISHED",
        )


if __name__ == "__main__":
    unittest.main()
