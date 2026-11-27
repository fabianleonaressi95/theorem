import unittest
from scripts.audit_t156_dodecahedral_feec_hodge import audit

class T156DodecahedralFEEC(unittest.TestCase):
    def test_structural_checks(self):
        r=audit()
        self.assertTrue(r["all_checks_pass"],r["checks"])
        self.assertEqual(r["counts"]["triangulation_vertices"],32)
        self.assertEqual(r["counts"]["triangulation_edges"],90)
        self.assertEqual(r["counts"]["triangulation_triangles"],60)
    def test_spectral_obstruction_is_not_rescaled(self):
        r=audit(); eig=r["Hodge_0_generalized_eigenvalues"]
        self.assertAlmostEqual(eig[0],0.0,places=8)
        self.assertTrue(all(abs(v-4.0)>1e-3 and abs(v-6.0)>1e-3 for v in eig))
        self.assertAlmostEqual(r["residuals"]["Q6_selected_intertwining_residual"],13.021786695995926,places=7)

if __name__=="__main__": unittest.main()
