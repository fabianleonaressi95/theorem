"""Tests for the Euclidean Cl(6) and Spin(6) audit."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_q6_spin6_clifford import (  # noqa: E402
    clifford6,
    chirality_matrix,
    golden_cut_project_frame,
    plane_spin_lift,
    run_audit,
)


class Q6Spin6CliffordTests(unittest.TestCase):
    def test_clifford_relations(self):
        import numpy as np
        gamma = clifford6()
        eye = np.eye(8, dtype=complex)
        for i in range(6):
            for j in range(6):
                target = 2 * eye if i == j else np.zeros((8, 8), dtype=complex)
                self.assertLess(np.linalg.norm(gamma[i] @ gamma[j]
                                                + gamma[j] @ gamma[i] - target), 1e-12)
        chir = chirality_matrix(gamma)
        self.assertLess(np.linalg.norm(chir @ chir - eye), 1e-12)

    def test_golden_frame_is_so6(self):
        import numpy as np
        frame = golden_cut_project_frame()
        self.assertLess(np.linalg.norm(frame @ frame.T - np.eye(6)), 1e-12)
        self.assertAlmostEqual(float(np.linalg.det(frame)), 1.0, places=12)

    def test_spin6_plane_lift(self):
        import numpy as np
        gamma = clifford6()
        S = plane_spin_lift(1, 4, 0.63, gamma)
        self.assertLess(np.linalg.norm(S.conj().T @ S - np.eye(8)), 1e-12)
        self.assertLess(np.linalg.norm(plane_spin_lift(1, 4, 2*np.pi, gamma)
                                       + np.eye(8)), 1e-12)
        self.assertLess(np.linalg.norm(plane_spin_lift(1, 4, 4*np.pi, gamma)
                                       - np.eye(8)), 1e-12)

    def test_complete_audit(self):
        result = run_audit()
        self.assertTrue(result["pass"], result["checks"])
        self.assertEqual(result["clifford_module"]["Weyl_spinor_dimensions_complex"],
                         [4, 4])


if __name__ == "__main__":
    unittest.main()
