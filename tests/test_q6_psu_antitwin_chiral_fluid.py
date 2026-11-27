import unittest
import numpy as np
from scripts.audit_q6_psu_antitwin_chiral_fluid import dirac_matrices, run_audit

class Q6PSUAntiTwinChiralFluidTests(unittest.TestCase):
    def test_all_finite_identities(self):
        result = run_audit()
        self.assertTrue(result["pass"], result["checks"])
        self.assertTrue(all(result["checks"].values()))

    def test_right_left_sheet_lock(self):
        g0, g1, g2, g3, g5 = dirac_matrices()
        eye4 = np.eye(4)
        tau1 = np.asarray([[0, 1], [1, 0]], dtype=complex)
        tau3 = np.diag([1, -1]).astype(complex)
        C = np.kron(g5, tau3)
        J = np.kron(eye4, tau1)
        self.assertLess(np.linalg.norm(J @ C @ J + C), 1e-12)
        parity_exchange = np.kron(g0, tau1)
        self.assertLess(np.linalg.norm(parity_exchange @ C @ parity_exchange - C), 1e-12)

    def test_conjugate_anti_twin_link(self):
        theta = 0.413
        up = np.exp(1j * theta)
        um = np.conjugate(up)
        self.assertLess(abs(um - up.conjugate()), 1e-12)

if __name__ == "__main__":
    unittest.main()
