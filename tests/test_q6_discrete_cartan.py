import unittest

import numpy as np

from scripts.audit_q6_discrete_cartan import (
    build_discrete_cartan,
    gauge_covariance_audit,
    q6_squares,
    reconstruct_seed,
    spatial_coframes,
)


class Q6DiscreteCartanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.X, cls.edges = reconstruct_seed()
        cls.E = spatial_coframes(cls.X)
        cls.data = build_discrete_cartan(cls.X, cls.edges, cls.E)

    def test_hexagram_q6_counts(self):
        self.assertEqual(self.X.shape, (64, 3))
        self.assertEqual(self.edges.shape, (192, 3))
        self.assertEqual(len(q6_squares()), 240)

    def test_so3_edge_connection(self):
        self.assertLess(self.data["link_orthogonality_max"], 1e-12)
        self.assertLess(self.data["link_determinant_residual_max"], 1e-12)

    def test_face_curvature_and_developed_torsion(self):
        self.assertEqual(len(self.data["torsions"]), 240)
        self.assertEqual(len(self.data["holonomies"]), 240)
        self.assertGreater(
            np.count_nonzero(np.linalg.norm(self.data["torsions"], axis=1) > 1e-10), 0
        )
        self.assertGreater(np.count_nonzero(self.data["curvature_angles"] > 1e-10), 0)

    def test_local_so3_gauge_covariance(self):
        result = gauge_covariance_audit(self.X, self.edges, self.E, self.data)
        self.assertLess(result["torsion_covariance_max"], 1e-10)
        self.assertLess(result["curvature_conjugation_max"], 1e-10)


if __name__ == "__main__":
    unittest.main()
