"""T158 tests: continuous interior normal-map connection and Whitney masses."""
import importlib.util
from pathlib import Path
import unittest

SCRIPT = (Path(__file__).resolve().parents[1] / "scripts"
          / "audit_t158_interior_covariant_whitney.py")
spec = importlib.util.spec_from_file_location("audit_t158", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class T158InteriorCovariantWhitney(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = audit.build_report()

    def cases(self):
        return (self.report["supergolden"], self.report["regular_control"])

    def test_interior_normal_map_and_quadrature(self):
        for case in self.cases():
            self.assertEqual(case["counts"], [32, 90, 60])
            self.assertGreater(case["minimum_normal_interpolation_norm"], 0.8)
            self.assertGreater(case["minimum_base_to_interpolant_dot"], 0.5)
            self.assertLess(max(case["quadrature_order_8_vs_12_relative_residuals_M0_M1"]),
                            2e-9)

    def test_t155_restriction_and_curvature(self):
        for case in self.cases():
            self.assertLess(case["T155_face_link_residual"], 2e-9)
            self.assertLess(case["antipodal_link_covariance_residual"], 2e-9)
            self.assertLess(case["gauss_bonnet_4pi_residual"], 2e-9)
            self.assertLess(case["holonomy_spherical_area_residual"], 2e-9)
            self.assertGreater(case["D1D0_norm"], 1e-4)
            self.assertLess(case["curvature_identity_residual"], 2e-9)

    def test_interior_whitney_masses_and_hodge(self):
        for case in self.cases():
            self.assertTrue(all(v > 0 for v in case["mass_minimum_eigenvalues"]))
            self.assertLess(max(case["mass_hermiticity_residuals"]), 2e-9)
            self.assertLess(max(case["hodge_hermiticity_residuals"]), 2e-9)
            self.assertEqual([len(case["spectra"][str(k)]) for k in range(3)],
                             [32, 90, 60])

    def test_vertex_gauge_covariance(self):
        for case in self.cases():
            self.assertLess(case["gauge_covariance_residual"], 2e-9)


if __name__ == "__main__":
    unittest.main()
