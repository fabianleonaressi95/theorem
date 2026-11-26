"""Regression tests for T149 regular-dodecahedron FEEC Hodge audit."""
import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_t149_dodecahedron_feec_hodge.py"
spec = importlib.util.spec_from_file_location("audit_t149", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class T149FEEC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = audit.build()

    def test_closed_spherical_triangulation(self):
        r = self.r
        self.assertEqual((r["vertices"], r["edges"], r["triangles"]), (32, 90, 60))
        self.assertEqual(r["euler_characteristic"], 2)
        self.assertEqual((r["rank_D0"], r["rank_D1"]), (31, 59))
        self.assertLess(r["boundary_squared_residual"], 2e-9)

    def test_regular_pentagon_frames_and_positive_masses(self):
        r = self.r
        self.assertLess(max(r["frame_max_residuals"]), 2e-9)
        for key in ("M0_eigenvalue_bounds", "M1_eigenvalue_bounds", "M2_eigenvalue_bounds"):
            self.assertGreater(r[key][0], 0.0)

    def test_q6_sector_is_valid_but_transfer_fails(self):
        r = self.r
        self.assertEqual(r["q6_map_rank"], 12)
        self.assertLess(r["q6_original_intertwiner_residual"], 2e-9)
        self.assertGreater(r["q6_sector_intertwiner_residual"], 1e-2)


if __name__ == "__main__":
    unittest.main()
