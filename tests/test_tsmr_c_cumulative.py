import math
import unittest

from audits.tsmr_c_cumulative import (
    empirical_cdf,
    finite_bernoulli_atoms,
    golden_identity_residual,
    golden_parameter,
    golden_support_radius,
    uniform_half_cdf,
)


class TSMRCumulativeTests(unittest.TestCase):
    def test_golden_algebraic_identity(self):
        self.assertLess(abs(golden_identity_residual()), 2e-16)

    def test_golden_support_radius(self):
        phi = (1.0 + math.sqrt(5.0)) / 2.0
        self.assertAlmostEqual(golden_support_radius(), phi * phi, places=14)

    def test_uniform_half_control_cdf(self):
        self.assertEqual(uniform_half_cdf(-2.0), 0.0)
        self.assertAlmostEqual(uniform_half_cdf(0.0), 0.5)
        self.assertEqual(uniform_half_cdf(2.0), 1.0)

    def test_finite_golden_approximants_are_atomic(self):
        atoms = sorted(finite_bernoulli_atoms(golden_parameter(), 5))
        self.assertEqual(len(atoms), 32)
        # A finite truncation is atomic; this says nothing about the limit.
        self.assertEqual(empirical_cdf(atoms, -10.0), 0.0)
        self.assertEqual(empirical_cdf(atoms, 10.0), 1.0)

    def test_empirical_cdf_counts_multiplicities(self):
        atoms = sorted([-1.0, 0.0, 0.0, 1.0])
        self.assertEqual(empirical_cdf(atoms, 0.0), 0.75)


if __name__ == "__main__":
    unittest.main()
