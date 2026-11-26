"""Regression tests for the deterministic C01-C04 spectral controls."""
import unittest

import numpy as np

from scripts.cymatics_wave_benchmarks import (
    discrete_laplacian_eigenvalue,
    plate_spectrum,
    q6_laplacian_spectrum,
    run_benchmarks,
)


class CymaticsBenchmarkTests(unittest.TestCase):
    def test_c01_plate_matches_discrete_separation_formula(self):
        result = run_benchmarks(10)
        self.assertLess(result["C01"]["max_abs_error_first_12"], 1e-7)
        self.assertAlmostEqual(result["C01"]["first_mode_vector_norm"], 1.0, places=10)

    def test_c02_square_mode_degeneracy(self):
        n = 12
        self.assertAlmostEqual(
            discrete_laplacian_eigenvalue(n, 1, 2),
            discrete_laplacian_eigenvalue(n, 2, 1),
            places=12,
        )

    def test_c03_asymmetric_perturbation_splits_degenerate_pair(self):
        result = run_benchmarks(10)
        self.assertLess(result["C03"]["unperturbed_pair_gap"], 1e-7)
        self.assertGreater(result["C03"]["perturbed_pair_gap"], 1e-5)

    def test_c04_q6_exact_spectrum_and_multiplicities(self):
        values, counts = q6_laplacian_spectrum()
        np.testing.assert_array_equal(values, np.arange(0, 13, 2))
        np.testing.assert_array_equal(counts, [1, 6, 15, 20, 15, 6, 1])

    def test_invalid_grid_rejected(self):
        with self.assertRaises(ValueError):
            plate_spectrum(1)


if __name__ == "__main__":
    unittest.main()
