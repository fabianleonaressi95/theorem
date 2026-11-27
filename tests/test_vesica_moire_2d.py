import unittest

import numpy as np

from audits.vesica_moire_2d import (
    phase_field,
    weighted_graph_laplacian,
)


class VesicaMoireGeometryTests(unittest.TestCase):
    def test_intersection_ratio_sqrt_three(self):
        radius = 2.4
        a = radius / 2
        y_intersection = np.sqrt(radius**2 - a**2)
        ratio = (2 * y_intersection) / (2 * a)
        self.assertAlmostEqual(ratio, np.sqrt(3), places=13)

    def test_phase_gradient_axis_formula(self):
        a, k, y = 0.8, 1.7, 1.1
        # Analytic derivative in x at x=0:
        # d/dx [k(rho_1-rho_2)] = 2ak/sqrt(a²+y²).
        analytic = 2 * a * k / np.sqrt(a*a + y*y)
        delta = 1e-6
        rho1_plus = np.hypot(delta + a, y)
        rho2_plus = np.hypot(delta - a, y)
        rho1_minus = np.hypot(-delta + a, y)
        rho2_minus = np.hypot(-delta - a, y)
        f_plus = k * (rho1_plus - rho2_plus)
        f_minus = k * (rho1_minus - rho2_minus)
        numerical = (f_plus - f_minus) / (2 * delta)
        self.assertAlmostEqual(numerical, analytic, places=8)

    def test_axis_spacing_at_vesica_intersection_is_lambda(self):
        # y=sqrt(3)a and lambda=2pi/k => d_M=lambda.
        a, k = 1.3, 2.2
        y = np.sqrt(3) * a
        d_moire = (np.pi / (a * k)) * np.sqrt(a*a + y*y)
        wavelength = 2 * np.pi / k
        self.assertAlmostEqual(d_moire, wavelength, places=13)


class VesicaMoireGraphTests(unittest.TestCase):
    def setUp(self):
        _, _, self.delta = phase_field(n=6, length=8.0, a=1.0, k=1.2)

    def test_weighted_operator_is_symmetric(self):
        matrix, _ = weighted_graph_laplacian(self.delta, 8.0, 0.1, True)
        difference = matrix - matrix.T
        self.assertLess(np.max(np.abs(difference.data), initial=0.0), 1e-12)

    def test_weights_are_strictly_positive(self):
        _, weights = weighted_graph_laplacian(self.delta, 8.0, 0.2, True)
        self.assertTrue(np.all(weights >= 0.8 - 1e-14))

    def test_constant_is_null_mode(self):
        matrix, _ = weighted_graph_laplacian(self.delta, 8.0, 0.1, True)
        residual = matrix @ np.ones(matrix.shape[0])
        self.assertLess(np.linalg.norm(residual), 1e-10)

    def test_operator_is_positive_semidefinite(self):
        matrix, _ = weighted_graph_laplacian(self.delta, 8.0, 0.1, True)
        eigenvalues = np.linalg.eigvalsh(matrix.toarray())
        self.assertGreaterEqual(float(eigenvalues.min()), -1e-10)

    def test_epsilon_zero_recovers_uniform_operator(self):
        weighted, _ = weighted_graph_laplacian(self.delta, 8.0, 0.0, True)
        uniform, _ = weighted_graph_laplacian(self.delta, 8.0, 0.0, False)
        difference = weighted - uniform
        self.assertLess(np.max(np.abs(difference.data), initial=0.0), 1e-12)


if __name__ == "__main__":
    unittest.main()
