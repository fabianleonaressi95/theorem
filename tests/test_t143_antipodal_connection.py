import unittest
import numpy as np
from scripts.audit_t143_antipodal_connection import build_audit

class AntipodalConnectionAuditTests(unittest.TestCase):
    def fixture(self):
        rng=np.random.default_rng(143)
        X=np.zeros((64,3))
        for g in range(64):
            h=g^7
            if g<h:
                X[g]=rng.normal(size=3); X[h]=-X[g]
        A=np.zeros((64,64))
        for g in range(64):
            for bit in range(6): A[g,g^(1<<bit)]=1
        return X,A

    def test_antipodal_link_and_face_equivariance(self):
        report=build_audit(*self.fixture())
        self.assertTrue(report["checks_pass"])
        self.assertEqual(report["antipodal"]["max_X_antipodal_residual"],0.0)
        self.assertEqual(report["link_transport"]["SO3_antipodal_max_residual"],0.0)
        self.assertEqual(report["plaquette_holonomy"]["faces"],240)

    def test_nonabelian_holonomies(self):
        report=build_audit(*self.fixture())
        self.assertGreater(report["nonabelianity"]["noncommuting_pairs_mod_centre"],0)

if __name__=="__main__": unittest.main()
