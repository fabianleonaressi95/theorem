import unittest
import sympy as sp

from src.t034_exact_2i_character_table import (
    CLASS_SIZES, FUNDAMENTAL, independent_degree_rows,
    reconstruct_character_table, verify_character_table,
)


class TestExact2ICharacterTable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table, cls.degrees = reconstruct_character_table()

    def test_nine_rows_and_dimensions(self):
        self.assertEqual(len(self.table), 9)
        self.assertEqual(len(self.degrees), 9)
        for row in self.table.values():
            self.assertEqual(len(row), 9)

    def test_fundamental_row(self):
        self.assertEqual(tuple(self.table["2"]), tuple(FUNDAMENTAL))

    def test_exact_character_orthogonality_and_molien(self):
        report = verify_character_table(self.table, max_degree=240)
        self.assertTrue(report["passed"])
        self.assertEqual(report["character_orthogonality_pairs"], 81)
        self.assertEqual(report["molien_character_averages_checked"], 9 * 241)

    def test_class_order(self):
        self.assertEqual(sum(CLASS_SIZES), 120)

    def test_interpolation_rows_are_independent(self):
        self.assertEqual(len(set(self.degrees)), 9)


if __name__ == "__main__":
    unittest.main()
