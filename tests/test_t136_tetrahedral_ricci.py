import unittest
import numpy as np

from audits.t136_tetrahedral_ricci import (
    measurement_matrix, run_audit, tetrahedra,
)


class T136TetrahedralRicciAuditTests(unittest.TestCase):
    def test_six_moment_tensors_have_full_rank(self):
        matrix = measurement_matrix(tetrahedra())
        self.assertEqual(np.linalg.matrix_rank(matrix), 6)
        self.assertLess(np.linalg.cond(matrix), 25.0)

    def test_manufactured_space_form_reconstruction_converges(self):
        result = run_audit()
        errors = [row["l2_error"] for row in result["scale_records"]]
        self.assertTrue(all(b < a for a, b in zip(errors, errors[1:])))
        self.assertEqual(result["moment_matrix_rank"], 6)

    def test_noise_sensitivity_is_finite_and_small(self):
        result = run_audit()
        self.assertTrue(np.isfinite(result["noise_reconstruction_l2_error"]))
        self.assertLess(result["noise_reconstruction_l2_error"], 1e-5)


if __name__ == "__main__":
    unittest.main()
