"""T157 regression tests: 32-90-60 link-covariant Whitney model."""
import importlib.util
from pathlib import Path
import unittest

SCRIPT = (Path(__file__).resolve().parents[1] / "scripts"
          / "audit_t157_full_covariant_whitney_curvature.py")
spec = importlib.util.spec_from_file_location("audit_t157", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class T157FullCovariantWhitney(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = audit.build_report()

    def cases(self):
        return (self.report["supergolden"], self.report["regular_control"])

    def test_full_complex_counts_and_t155_restriction(self):
        for case in self.cases():
            self.assertEqual(case["counts"], [32, 90, 60])
            self.assertLess(case["centroid_normal_T155_residual"], 2e-9)
            self.assertLess(case["T155_face_link_residual"], 2e-9)

    def test_link_geometry_and_antipodal_covariance(self):
        for case in self.cases():
            self.assertGreater(case["minimum_frame_projection_norm"], 0.1)
            self.assertLess(case["link_orthogonality_residual"], 2e-9)
            self.assertLess(case["link_determinant_residual"], 2e-9)
            self.assertLess(case["antipodal_normal_residual"], 2e-9)
            self.assertLess(case["antipodal_link_covariance_residual"], 2e-9)

    def test_holonomy_and_curvature_identity(self):
        for case in self.cases():
            self.assertLess(case["gauss_bonnet_4pi_residual"], 2e-9)
            self.assertLess(case["holonomy_spherical_area_residual"], 2e-9)
            self.assertGreater(case["D1D0_norm"], 1e-4)
            self.assertLess(case["curvature_identity_residual"], 2e-9)

    def test_covariant_whitney_masses_and_spectra(self):
        for case in self.cases():
            self.assertTrue(all(v > 0 for v in case["mass_minimum_eigenvalues"]))
            self.assertLess(max(case["mass_hermiticity_residuals"]), 2e-9)
            self.assertEqual([len(case["spectra"][str(k)]) for k in range(3)],
                             [32, 90, 60])

    def test_gauge_covariance(self):
        for case in self.cases():
            self.assertLess(case["gauge_covariance_residual"], 2e-9)


if __name__ == "__main__":
    unittest.main()
