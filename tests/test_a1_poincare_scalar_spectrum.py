import unittest
from audits.a1_poincare_scalar_spectrum import audit, binary_molien_coefficient


class TestA1PoincareScalarSpectrum(unittest.TestCase):
    def test_binary_molien_initial_values(self):
        self.assertEqual([binary_molien_coefficient(k) for k in range(13)],
                         [1] + [0] * 11 + [1])

    def test_exact_character_average_through_degree_120(self):
        report = audit(120)
        self.assertTrue(report["passed"])
        self.assertEqual(report["degrees_checked"], 121)
        self.assertTrue(report["odd_degree_vanishing"])
        self.assertEqual(report["first_positive_eigenpair"], {
            "degree": 12,
            "invariant_dimension": 1,
            "laplace_eigenvalue": 168,
            "spectral_multiplicity": 13,
        })
        self.assertEqual(report["degree_120"], {
            "degree": 120,
            "invariant_dimension": 3,
            "laplace_eigenvalue": 14640,
            "spectral_multiplicity": 363,
        })

    def test_selected_coefficients(self):
        expected = {20: 1, 30: 1, 60: 2, 72: 2, 120: 3}
        for degree, value in expected.items():
            self.assertEqual(binary_molien_coefficient(degree), value)


if __name__ == "__main__":
    unittest.main()
