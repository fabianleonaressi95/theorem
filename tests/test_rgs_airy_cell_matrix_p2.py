"""Convergence tests for the P2 annular Hessian/Laplacian matrix audit."""
import unittest
import json
import sys
import tempfile
import io
from pathlib import Path
from contextlib import redirect_stdout
from unittest.mock import patch
from scripts.rgs_airy_cell_matrix_p2 import audit_p2_annulus, run, main


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

    def test_written_report_is_valid_json(self):
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)/"p2_report.json"
            with patch.object(sys,"argv",["airy-p2-audit","--out",str(target)]):
                with redirect_stdout(io.StringIO()):
                    main()
            payload=json.loads(target.read_text())
            self.assertIn("relative_matrix_difference",payload)


if __name__=="__main__":
    unittest.main()
