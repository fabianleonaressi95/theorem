import unittest
import sympy as sp
from src.t038_rumin_reduced_differential import (
    A, B, rumin_polarization_block, restrict_degree
)
from src.t036_2i_irreducible_models import build_all_models
from audits.t035_exact_binary_icosahedral_model import elements_2i

class TestT038ReducedRuminDifferential(unittest.TestCase):
    def test_geometric_gram_factorization(self):
        D, gram, meta = rumin_polarization_block(2, 3)
        expected = sp.Rational(meta["L"], 2) * sp.Matrix(
            [[B**2, -A*B], [-A*B, A**2]])
        self.assertEqual(sp.simplify(D.conjugate().T*D-expected), sp.zeros(2))

    def test_rejects_boundary_sector(self):
        with self.assertRaises(ValueError):
            rumin_polarization_block(0, 2)

    def test_reduced_operator_is_identity_on_multiplicity(self):
        group, chars, _, models = build_all_models()
        report = restrict_degree(1, group, chars, models)
        self.assertEqual(report["equivariance_checks"], 120)
        self.assertTrue(report["restriction_checks"] >= 1)
        for label, item in report["reduced"].items():
            if item["multiplicity"]:
                self.assertEqual(item["source_dimension"],
                                 2*item["irrep_dimension"]*item["multiplicity"])

if __name__ == "__main__":
    unittest.main()
