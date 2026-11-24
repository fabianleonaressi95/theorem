import unittest

import numpy as np

from audits.jitterbug_eight_coil_coupling import (
    MU0, coil_polygon, inductance_matrix, midpoint_coupled_rl,
    neumann_mutual, self_inductance_circular,
)


class TestEightCoilPrimitives(unittest.TestCase):
    def test_polygon_loop_closes_and_has_expected_segment_count(self):
        loop = coil_polygon(np.zeros(3), np.eye(3), np.array([0, 0, 1]),
                            0.02, segments=32)
        vertices, segments = loop
        self.assertEqual(vertices.shape, (32, 3))
        self.assertEqual(segments.shape, (32, 3))
        self.assertTrue(np.allclose(segments.sum(axis=0), 0.0, atol=1e-14))

    def test_mutual_inductance_is_reciprocal(self):
        a = coil_polygon(np.array([0., 0., 0.]), np.eye(3), np.array([0, 0, 1]),
                         0.03, 64)
        R = np.array([[1., 0, 0], [0, 0, -1], [0, 1, 0]])
        b = coil_polygon(np.array([0.01, 0., 0.02]), R, np.array([0, 0, 1]),
                         0.025, 64)
        m1 = neumann_mutual(a, b, 100, 80, 1e-4)
        m2 = neumann_mutual(b, a, 80, 100, 1e-4)
        self.assertAlmostEqual(m1, m2, delta=1e-14)

    def test_self_inductance_positive_and_turns_quadratic(self):
        l1 = self_inductance_circular(10, 0.03, 1e-4)
        l2 = self_inductance_circular(20, 0.03, 1e-4)
        self.assertGreater(l1, 0)
        self.assertAlmostEqual(l2 / l1, 4.0, places=12)

    def test_inductance_matrix_symmetric(self):
        loop1 = coil_polygon(np.array([0., 0., 0.]), np.eye(3), np.array([0, 0, 1]),
                             0.03, 48)
        R = np.array([[1., 0, 0], [0, 0, -1], [0, 1, 0]])
        loop2 = coil_polygon(np.array([0.01, 0., 0.02]), R, np.array([0, 0, 1]),
                             0.025, 48)
        L = inductance_matrix([loop1, loop2], [100, 80], [0.03, 0.025],
                              [1e-4, 1e-4], 1e-4)
        self.assertTrue(np.allclose(L, L.T, atol=1e-14))
        self.assertTrue(np.all(np.diag(L) > 0))

    def test_zero_emf_keeps_zero_current(self):
        times = np.array([0., 0.1, 0.2])
        L = np.repeat((np.eye(2) * 1e-3)[None, :, :], 3, axis=0)
        emf = np.zeros((2, 2))
        R = np.eye(2) * 5
        current = midpoint_coupled_rl(L, emf, times, R)
        self.assertTrue(np.allclose(current, 0.0))

    def test_one_coil_constant_l_rl_midpoint_solution_is_finite(self):
        times = np.linspace(0, 0.1, 11)
        L = np.repeat(np.array([[[0.01]]]), len(times), axis=0)
        emf = np.ones((len(times)-1, 1))
        current = midpoint_coupled_rl(L, emf, times, np.array([[10.0]]))
        self.assertTrue(np.all(np.isfinite(current)))
        self.assertGreater(current[-1, 0], 0)


if __name__ == "__main__":
    unittest.main()
