import math
import unittest

from audits.tsmr_f_multifractal import (
    cantor_bernoulli_dimension,
    cantor_bernoulli_tau,
    finite_level_self_affine_pressure,
    singular_value_function,
    singular_values_2x2,
)


class TestTSMRFMultifractal(unittest.TestCase):
    def test_uniform_cantor_measure_is_monofractal(self):
        expected = math.log(2.0) / math.log(3.0)
        for q in (0.5, 0.8, 1.0, 2.0, 4.0):
            self.assertAlmostEqual(
                cantor_bernoulli_dimension(q, 0.5, 1.0/3.0),
                expected, places=12)

    def test_nonuniform_bernoulli_measure_has_q_dependent_dimensions(self):
        dims = [cantor_bernoulli_dimension(q, 0.25, 1.0/3.0)
                for q in (0.5, 1.0, 2.0, 4.0)]
        self.assertGreater(max(dims)-min(dims), 0.05)

    def test_information_dimension_is_shannon_entropy_over_log_scale(self):
        p, ratio = 0.2, 1.0/3.0
        expected = -(p*math.log(p)+(1-p)*math.log(1-p))/math.log(1/ratio)
        self.assertAlmostEqual(
            cantor_bernoulli_dimension(1.0, p, ratio), expected, places=12)
        self.assertAlmostEqual(
            cantor_bernoulli_tau(1.0, p, ratio), 0.0, places=12)

    def test_tau_and_dimension_are_consistent_away_from_q_one(self):
        q, p, ratio = 2.0, 0.3, 1.0/3.0
        self.assertAlmostEqual(
            cantor_bernoulli_dimension(q, p, ratio),
            cantor_bernoulli_tau(q, p, ratio)/(q-1.0), places=12)

    def test_singular_values_and_anisotropic_phi(self):
        matrix = ((0.5, 0.0), (0.0, 0.25))
        self.assertEqual(singular_values_2x2(matrix), (0.5, 0.25))
        self.assertAlmostEqual(singular_value_function(matrix, 0.5),
                               math.sqrt(0.5), places=12)
        self.assertAlmostEqual(singular_value_function(matrix, 1.5),
                               0.5*math.sqrt(0.25), places=12)

    def test_finite_pressure_matches_common_scalar_maps(self):
        ratio = 0.4
        matrix = ((ratio, 0.0), (0.0, ratio))
        p = (0.3, 0.7)
        q, s, depth = 2.0, 1.0, 4
        measured = finite_level_self_affine_pressure(
            [matrix, matrix], p, q, s, depth)
        expected = math.log((p[0]**q+p[1]**q) * ratio**(s*(1-q)))
        self.assertAlmostEqual(measured, expected, places=12)

    def test_invalid_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            cantor_bernoulli_dimension(2.0, 1.0, 1.0/3.0)
        with self.assertRaises(ValueError):
            finite_level_self_affine_pressure(
                [((0.5, 0.0), (0.0, 0.25))], [0.8], 2.0, 1.0, 2)


if __name__ == "__main__":
    unittest.main()
