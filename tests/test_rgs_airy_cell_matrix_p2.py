"""Convergence tests for the P2 annular Hessian/Laplacian matrix audit."""
import unittest
from scripts.rgs_airy_cell_matrix_p2 import audit_p2_annulus, run


class AiryCellP2MatrixTests(unittest.TestCase):
    def test_matrix_difference_decreases_under_refinement(self):
        report=run()
        errors=report["relative_matrix_difference"]
        self.assertTrue(all(errors[i+1] < errors[i] for i in range(len(errors)-1)), errors)
        self.assertTrue(all(rate > 1.5 for rate in report["observed_halving_rates"]), report)

    def test_matrices_are_symmetric_and_positive(self):
        result=audit_p2_annulus(radial_cells=8,angular_cells=32)
        self.assertLess(result["symmetry_residual_hessian"],1e-10)
        self.assertLess(result["symmetry_residual_laplacian"],1e-10)
        self.assertGreater(result["min_eigenvalue_hessian"],0.0)
        self.assertGreater(result["min_eigenvalue_laplacian"],0.0)


if __name__=="__main__":
    unittest.main()
