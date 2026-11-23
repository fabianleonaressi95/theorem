import unittest

import numpy as np

from audits.jitterbug_coil_coupling import (
    coil_radius_limit, emf_from_rotations, exp_so3,
    fit_panel_rotation, panel_normal,
)


class TestJitterbugCoilCoupling(unittest.TestCase):
    def test_panel_pose_recovers_known_rotation(self):
        reference = np.array([
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.5, np.sqrt(3.0) / 2.0, 0.0],
        ])
        expected = exp_so3(np.array([0.23, -0.17, 0.31]))
        translation = np.array([2.0, -1.0, 0.7])
        current = (expected @ reference.T).T + translation
        actual, residual = fit_panel_rotation(reference, current)
        self.assertLess(np.max(np.abs(actual - expected)), 1e-12)
        self.assertLess(residual, 1e-12)

    def test_static_panel_has_zero_emf(self):
        rotations = np.repeat(np.eye(3)[None, :, :], 3, axis=0)
        emf, _, flux = emf_from_rotations(
            rotations, np.array([0.0, 0.1, 0.2]),
            np.array([0.0, 0.0, 0.2]), 50, 0.01,
            np.array([0.0, 0.0, 1.0])
        )
        self.assertTrue(np.allclose(emf, 0.0, atol=1e-14))
        self.assertTrue(np.allclose(flux, 0.1))

    def test_rotating_panel_matches_faraday_derivative(self):
        omega = 0.7
        times = np.array([0.0, 0.001, 0.002])
        rotations = np.array([
            exp_so3(np.array([0.0, omega * t, 0.0])) for t in times
        ])
        B = np.array([0.0, 0.0, 0.2])
        turns, area = 80, 0.003
        n0 = np.array([0.0, 0.0, 1.0])
        emf, tm, _ = emf_from_rotations(rotations, times, B, turns, area, n0)
        expected = turns * area * B[2] * omega * np.sin(omega * tm)
        self.assertTrue(np.allclose(emf, expected, rtol=1e-9, atol=1e-12))

    def test_coil_radius_must_fit_inside_equilateral_panel(self):
        limit = coil_radius_limit(1.0)
        self.assertAlmostEqual(limit, np.sqrt(3.0) / 6.0)
        self.assertLess(0.8 * limit, limit)

    def test_panel_normal_is_unit(self):
        triangle = np.array([
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.5, np.sqrt(3.0) / 2.0, 0.0],
        ])
        self.assertAlmostEqual(np.linalg.norm(panel_normal(triangle)), 1.0)


if __name__ == "__main__":
    unittest.main()
