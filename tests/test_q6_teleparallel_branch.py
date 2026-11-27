import unittest
import numpy as np
from scripts.audit_q6_discrete_cartan import reconstruct_seed, spatial_coframes
from scripts.audit_q6_teleparallel_branch import build_teleparallel_branch, gauge_audit

class Q6TeleparallelBranchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.X, cls.edges = reconstruct_seed()
        cls.E = spatial_coframes(cls.X)
        cls.data = build_teleparallel_branch(cls.X, cls.edges, cls.E)

    def test_all_plaquette_holonomies_are_identity(self):
        self.assertEqual(len(self.data["holonomies"]), 240)
        self.assertLess(self.data["flat_holonomy_residual_max"], 1e-14)
        for H in self.data["holonomies"]:
            self.assertTrue(np.allclose(H, np.eye(3), atol=1e-14))

    def test_nonzero_face_closure_defect(self):
        norms = np.linalg.norm(self.data["torsions"], axis=1)
        self.assertEqual(len(norms), 240)
        self.assertGreater(np.count_nonzero(norms > 1e-10), 0)

    def test_local_gauge_covariance(self):
        result = gauge_audit(self.X, self.edges, self.E, self.data)
        self.assertLess(result["torsion_covariance_max"], 1e-10)
        self.assertLess(result["holonomy_conjugation_max"], 1e-10)

if __name__ == "__main__":
    unittest.main()
