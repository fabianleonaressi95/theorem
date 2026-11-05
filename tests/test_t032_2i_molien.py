import unittest
from src.t032_2i_molien import (
    IRREP_DIMENSIONS, IRREP_NUMERATORS, molien_coefficients,
    verify_dimension_decomposition, verify_sum_of_squares,
    isotypic_projector_normalization,
)

class TestT032Molien(unittest.TestCase):
    def test_nine_irreps_and_sum_squares(self):
        self.assertEqual(len(IRREP_NUMERATORS), 9)
        self.assertEqual(sum(d*d for d in IRREP_DIMENSIONS.values()), 120)
        self.assertTrue(verify_sum_of_squares())

    def test_dimension_decomposition_through_degree_240(self):
        self.assertTrue(verify_dimension_decomposition(240))

    def test_initial_coefficients(self):
        self.assertEqual(molien_coefficients("1", 30)[0], 1)
        self.assertEqual(molien_coefficients("2", 1), (0, 1))
        self.assertEqual(molien_coefficients("6", 15)[15], 2)

    def test_projector_normalization(self):
        self.assertEqual(isotypic_projector_normalization("4'"), (4, 120))

if __name__ == "__main__":
    unittest.main()
