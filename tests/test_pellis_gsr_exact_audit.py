import unittest
import sympy as sp
from audits.pellis_gsr_exact_audit import audit


class TestPellisGSRExactAudit(unittest.TestCase):
    def test_exact_algebraic_value(self):
        phi = (1 + sp.sqrt(5)) / 2
        value = 360 / phi**2 - 2 / phi**3 + 1 / (3 * phi)**5
        expected = (sp.Integer(264373) - sp.Integer(88447)*sp.sqrt(5)) / 486
        self.assertEqual(sp.simplify(value - expected), 0)
        self.assertTrue(audit()["passed"])

    def test_comparisons_and_source_arithmetic(self):
        report = audit()
        self.assertTrue(report["comparison"]["within_2022_uncertainty"])
        self.assertTrue(report["comparison"]["within_2023_uncertainty"])
        checks = report["source_text_checks"]
        self.assertNotEqual(
            checks["claimed_absolute_error_2022"],
            checks["computed_absolute_error_2022"],
        )
        self.assertNotEqual(
            checks["claimed_(3phi)^5"],
            checks["computed_(3phi)^5"],
        )


if __name__ == "__main__":
    unittest.main()
