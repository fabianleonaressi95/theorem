import unittest
import numpy as np

from models.mqm_multidimensional import (
    build_mqm_dataset, canonical_q6_edges, standardized_pca,
    correlation_matrix,
)


class TestMQMMultidimensional(unittest.TestCase):
    def setUp(self):
        self.edges = canonical_q6_edges()
        self.phi = 1.8 + 0.02 * np.sin(np.arange(64) * 0.3)
        self.tau = 0.1 + 0.01 * np.cos(np.arange(64) * 0.2)

    def test_q6_edge_structure(self):
        self.assertEqual(len(self.edges), 192)
        degree = np.zeros(64)
        for u, v, _ in self.edges:
            degree[u] += 1
            degree[v] += 1
        np.testing.assert_array_equal(degree, np.full(64, 6))

    def test_vertex_and_edge_blocks_are_separate(self):
        data = build_mqm_dataset(self.phi, self.tau)
        self.assertEqual(data.vertex_features.shape, (64, 7))
        self.assertEqual(data.edge_features.shape, (192, 5))
        self.assertNotIn("metric_dirichlet_energy_density", data.vertex_feature_names)

    def test_metric_features_require_explicit_weights(self):
        weights = np.linspace(0.8, 1.2, 192)
        data = build_mqm_dataset(self.phi, self.tau, metric_weights=weights)
        self.assertEqual(data.vertex_features.shape, (64, 8))
        self.assertEqual(data.edge_features.shape, (192, 6))
        self.assertIn("metric_conductance", data.edge_feature_names)
        self.assertTrue(np.all(data.vertex_features[:, -1] >= 0))

    def test_pca_returns_orthonormal_loadings(self):
        data = build_mqm_dataset(self.phi, self.tau)
        result = standardized_pca(data.vertex_features, n_components=3)
        self.assertEqual(result["scores"].shape, (64, 3))
        np.testing.assert_allclose(
            result["loadings"].T @ result["loadings"], np.eye(3), atol=1e-12
        )
        self.assertAlmostEqual(float(result["explained_variance_ratio"].sum()),
                               float(np.sum(result["explained_variance_ratio"])))

    def test_correlations_and_categorical_labels(self):
        categories = ["A" if i < 32 else "B" for i in range(64)]
        data = build_mqm_dataset(self.phi, self.tau, vertex_categories=categories)
        self.assertEqual(len(data.edge_labels), 192)
        corr = correlation_matrix(data.vertex_features)
        self.assertEqual(corr.shape, (7, 7))

    def test_invalid_shapes_and_weights_rejected(self):
        with self.assertRaises(ValueError):
            build_mqm_dataset(self.phi[:-1], self.tau)
        with self.assertRaises(ValueError):
            build_mqm_dataset(self.phi, self.tau, metric_weights=np.ones(191))


if __name__ == "__main__":
    unittest.main()
