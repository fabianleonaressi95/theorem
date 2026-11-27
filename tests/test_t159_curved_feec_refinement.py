import unittest
from scripts.audit_t159_curved_feec_refinement import build_report

class T159CurvedFEECRefinement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_conforming_refinement_and_geometry(self):
        expected = [[32,90,60],[122,360,240],[272,810,540],[482,1440,960]]
        self.assertEqual([r["counts"] for r in self.report["refinements"]], expected)
        for r in self.report["refinements"]:
            self.assertTrue(r["antipodal_node_involution"])
            self.assertLess(r["antipodal_normal_residual"],2e-9)
            self.assertLess(r["antipodal_link_covariance_residual"],2e-9)
            self.assertLess(r["curvature_identity_residual"],2e-9)
            self.assertLess(r["gauss_bonnet_4pi_residual"],2e-7)
            self.assertGreater(r["minimum_M0_eigenvalue"],0)
            self.assertGreater(r["minimum_M1_cholesky_diagonal"],0)

    def test_quadrature_and_spectral_stabilization(self):
        self.assertLess(max(self.report["factor_2_quadrature_order_8_vs_12_relative_mass_residuals"]),2e-9)
        d=self.report["first_eigenvalue_absolute_increments"]
        self.assertLess(d[2],d[1])
        self.assertLess(d[1],d[0])
        last=self.report["refinements"][-1]["first_12_hodge0_eigenvalues"][0]
        self.assertAlmostEqual(last,2.3715586988468,places=7)
        self.assertGreater(abs(last-4.0),1.0)
        self.assertGreater(abs(last-6.0),1.0)

if __name__=="__main__":
    unittest.main()
