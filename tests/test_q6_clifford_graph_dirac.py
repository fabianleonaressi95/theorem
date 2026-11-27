import unittest
import numpy as np
from scripts.audit_q6_clifford_graph_dirac import graph_dirac, run_audit

class Q6CliffordGraphDiracTests(unittest.TestCase):
    def test_exact_finite_graph_operator(self):
        result=run_audit()
        self.assertTrue(result["pass"],result["checks"])
        self.assertTrue(all(result["checks"].values()))
    def test_flat_gapped_identity_link_spectrum(self):
        D=graph_dirac()
        self.assertLess(np.linalg.norm(D@D+1.5*np.eye(512)),1e-10)
        ev=np.linalg.eigvalsh(1j*D)
        self.assertEqual(int(np.count_nonzero(ev>0)),256)
        self.assertEqual(int(np.count_nonzero(ev<0)),256)

if __name__=="__main__": unittest.main()
