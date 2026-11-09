"""Manufactured annulus tests for the Airy cell interaction matrix identity."""
import unittest
import numpy as np
from scripts.rgs_airy_cell_matrix_identity import audit_annulus, run


class AiryCellMatrixIdentityTests(unittest.TestCase):
    def test_hessian_and_laplacian_matrices_agree(self):
        for radius in (0.1, 0.2, 0.35):
            result = audit_annulus(a=radius, R=1.0, order=320)
            self.assertLess(result["relative_frobenius_difference"], 1e-9, result)
            self.assertLess(result["symmetry_residual_hessian"], 1e-10, result)
            self.assertLess(result["symmetry_residual_laplacian"], 1e-10, result)

    def test_cell_matrices_are_positive(self):
        result = run()
        for case in result["cases"]:
            self.assertGreater(case["min_eigenvalue_hessian"], 0.0, case)
            self.assertGreater(case["min_eigenvalue_laplacian"], 0.0, case)


if __name__ == "__main__":
    unittest.main()
