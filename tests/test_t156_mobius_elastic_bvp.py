"""Focused tests for the T156 finite-width Mobius BVP formulation."""
import math
import unittest

import numpy as np

from scripts.solve_t156_mobius_elastic_bvp import (
    boundary_conditions,
    initial_guess,
    rhs,
    vesica_width_from_perimeter_map,
    wunderlich_coefficients,
)


class T156MobiusElasticBVPTests(unittest.TestCase):
    def test_vesica_half_threshold_width_map(self):
        data = vesica_width_from_perimeter_map(0.5)
        self.assertAlmostEqual(data["b_over_R"], math.sqrt(3.0)/2.0, places=14)
        self.assertAlmostEqual(data["perimeter_over_R"], 4.0*math.pi/3.0, places=14)
        self.assertAlmostEqual(data["w_over_L"], 3.0*math.sqrt(3.0)/(8.0*math.pi), places=14)
        self.assertAlmostEqual(data["L_over_2w"], 4.0*math.pi/(3.0*math.sqrt(3.0)), places=14)
        self.assertAlmostEqual(data["w_when_L_2pi"], 3.0*math.sqrt(3.0)/4.0, places=14)

    def test_wunderlich_coefficients_regular_at_zero_slope(self):
        arrays = wunderlich_coefficients(np.array([0.0]), 0.7)
        self.assertTrue(all(np.all(np.isfinite(a)) for a in arrays))
        V = arrays[-1][0]
        self.assertAlmostEqual(float(V), 1.0, places=14)

    def test_initial_guess_respects_developability_domain(self):
        mesh = np.linspace(0.0, math.pi, 40)
        width = 3.0*math.sqrt(3.0)/4.0
        y = initial_guess(width, 5e-2, mesh)
        z = np.tanh(y[8])
        self.assertLess(float(np.max(np.abs(z))), 1.0)
        self.assertAlmostEqual(float(y[8, 0]), 0.0, places=14)

    def test_full_equilibrium_rhs_is_finite_on_seed(self):
        mesh = np.linspace(0.0, math.pi, 40)
        width = 3.0*math.sqrt(3.0)/4.0
        y = initial_guess(width, 5e-2, mesh)
        dy = rhs(mesh, y, width)
        self.assertEqual(dy.shape, y.shape)
        self.assertTrue(np.all(np.isfinite(dy)))

    def test_constitutive_endpoint_sign_matches_eq21(self):
        mesh = np.linspace(0.0, math.pi, 40)
        width = 3.0*math.sqrt(3.0)/4.0
        y = initial_guess(width, 5e-2, mesh)
        y[5, 0] = 2.0*y[6, 0]*(1.0+y[7, 0]**2)**2 - y[7, 0]*y[3, 0]
        residual = boundary_conditions(y[:, 0], y[:, -1], 5e-2)
        self.assertAlmostEqual(float(residual[-1]), 0.0, places=12)

    def test_boundary_condition_count_and_seed_residual_shape(self):
        mesh = np.linspace(0.0, math.pi, 40)
        width = 3.0*math.sqrt(3.0)/4.0
        y = initial_guess(width, 5e-2, mesh)
        residual = boundary_conditions(y[:, 0], y[:, -1], 5e-2)
        self.assertEqual(residual.shape, (15,))
        self.assertTrue(np.all(np.isfinite(residual)))


if __name__ == "__main__":
    unittest.main()
