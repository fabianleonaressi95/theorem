"""Manufactured annulus tests for the Airy cell interaction matrix identity."""
import unittest
import json
import sys
import tempfile
import io
from pathlib import Path
from contextlib import redirect_stdout
from unittest.mock import patch
from scripts.rgs_airy_cell_matrix_identity import audit_annulus, run, main


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

    def test_written_report_is_valid_json(self):
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)/"report.json"
            with patch.object(sys,"argv",["airy-cell-audit","--out",str(target)]):
                with redirect_stdout(io.StringIO()):
                    main()
            payload=json.loads(target.read_text())
            self.assertIn("max_relative_frobenius_difference",payload)


if __name__ == "__main__":
    unittest.main()
