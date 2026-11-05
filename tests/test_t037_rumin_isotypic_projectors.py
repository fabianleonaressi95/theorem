import unittest

from src.t037_rumin_isotypic_projectors import (
    audit_isotypic_degree,
    rumin_block_dimension,
)


class TestT037RuminIsotypicProjectors(unittest.TestCase):
    def test_exact_projectors_on_all_first_occurrence_degrees(self):
        # Includes the first multiplicity-one occurrence of each of the
        # nine irreps: 1, 2, 3, 4', 5, 3', 4, 6, 2'.
        for degree in (0, 1, 2, 3, 4, 5, 6, 7):
            report = audit_isotypic_degree(degree, check_centrality=True)
            self.assertTrue(report["passed"])
            self.assertEqual(report["ambient_dimension"], degree + 1)
            self.assertEqual(report["irreducibles_checked"], 9)

    def test_first_nontrivial_invariant_level(self):
        report = audit_isotypic_degree(12, check_centrality=True)
        self.assertTrue(report["passed"])
        self.assertEqual(report["ambient_dimension"], 13)

    def test_t021_rumin_block_counts(self):
        self.assertEqual(rumin_block_dimension(12, "1", "E0"), 13)
        self.assertEqual(rumin_block_dimension(12, "1", "E1"), 26)
        self.assertEqual(rumin_block_dimension(11, "1", "E0"), 0)

    def test_invalid_sector(self):
        with self.assertRaises(ValueError):
            rumin_block_dimension(12, "1", "middle")


if __name__ == "__main__":
    unittest.main()
