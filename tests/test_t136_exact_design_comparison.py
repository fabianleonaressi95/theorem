import unittest
from unittest.mock import patch

import numpy as np

from audits import t136_exact_design_comparison as audit
from audits.t136_moment_design_optimization import candidate_pool


class T136ExactDesignComparisonTests(unittest.TestCase):
    def test_observation_covariance_matches_declared_relative_noise_model(self):
        vertices = np.array([
            [[0., 0., 0.], [1., 0., 0.], [0., 1., 0.], [0., 0., 1.]],
            [[0., 0., 0.], [1., 0., 0.], [0., 1., 0.], [0., 0., 2.]],
        ])
        scale = 0.01
        q_expected = np.array([1.0002, 0.9998])
        def fake_volume(tetra, r, order=7, steps=80):
            index = 0 if np.allclose(tetra, vertices[0]) else 1
            volume0 = abs(np.linalg.det(tetra[1:] - tetra[0])) / 6.0
            return r**3 * volume0 * q_expected[index]

        with patch.object(audit, "geodesic_tetrahedron_volume", side_effect=fake_volume):
            y, covariance_y, q = audit.observation_and_covariance(
                vertices, scale, 2.0e-5, order=3, steps=20
            )
        np.testing.assert_allclose(q, q_expected)
        np.testing.assert_allclose(y, -6.0 * (q_expected - 1.0) / scale**2)
        expected_diag = (6.0 * 2.0e-5 * q_expected / scale**2)**2
        np.testing.assert_allclose(covariance_y, np.diag(expected_diag))

    def test_reconstruction_covariance_is_pushed_forward_by_L(self):
        items = candidate_pool(seed=1362026, size=16, include_vertices=True)[1]
        A = np.asarray([audit.moment_row(v) for v in items[:8]])
        self.assertEqual(np.linalg.matrix_rank(A), 6)
        L = audit.reconstruction_map(A)
        covariance_y = np.diag(np.linspace(1e-8, 8e-8, len(A)))
        covariance_R = L @ covariance_y @ L.T
        self.assertEqual(covariance_R.shape, (6, 6))
        np.testing.assert_allclose(covariance_R, covariance_R.T, atol=1e-18)
        self.assertGreaterEqual(
            float(np.linalg.eigvalsh(covariance_R).min()), -1e-16
        )

    def test_exact_augmentation_returns_distinct_twelve_probe_subset(self):
        _, vertices = candidate_pool(
            seed=1362026, size=40, include_vertices=True
        )
        A = np.asarray([audit.moment_row(v) for v in vertices])
        from audits.t136_moment_design_optimization import greedy_d_optimal_design
        seed = greedy_d_optimal_design(A, count=6)
        selected = audit.greedy_exact_augmentation(
            vertices, seed, 12,
            lambda ids: float(np.linalg.cond(A[np.asarray(ids)])),
        )
        self.assertEqual(len(selected), 12)
        self.assertEqual(len(set(selected)), 12)
        self.assertEqual(np.linalg.matrix_rank(A[selected]), 6)

    def test_multiscale_objective_distinguishes_a_and_risk(self):
        _, vertices = candidate_pool(
            seed=1362026, size=20, include_vertices=True
        )
        A = np.asarray([audit.moment_row(v) for v in vertices])
        seed = __import__(
            "audits.t136_moment_design_optimization",
            fromlist=["greedy_d_optimal_design"]
        ).greedy_d_optimal_design(A, count=6)
        q_table = np.ones((len(vertices), len(audit.SELECTION_SCALES)))
        a_value = audit.cached_subset_objective(seed, "A", A, q_table)
        risk_value = audit.cached_subset_objective(seed, "risk", A, q_table)
        self.assertGreater(a_value, 0.0)
        self.assertGreater(risk_value, 0.0)
        self.assertGreaterEqual(risk_value, a_value)


if __name__ == "__main__":
    unittest.main()
