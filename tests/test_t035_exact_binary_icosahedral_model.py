import unittest

from audits.t035_exact_binary_icosahedral_model import audit


class TestT035ExactBinaryIcosahedralModel(unittest.TestCase):
    def test_exact_group_and_fundamental_representation(self):
        report = audit()

        self.assertTrue(report["passed"])
        self.assertEqual(report["group"], "2I")
        self.assertEqual(report["order"], 120)
        self.assertEqual(report["field"], "Q(sqrt(5))")
        self.assertEqual(report["construction"], "600-cell unit quaternions")
        self.assertEqual(report["closure_products_checked"], 120**2)
        self.assertEqual(report["unit_norms_checked"], 120)
        self.assertEqual(report["identity_inverse_checks"], 240)
        self.assertEqual(report["fundamental_su2_determinants_checked"], 120)
        self.assertEqual(report["fundamental_su2_unitarity_checked"], 120)
        self.assertEqual(
            report["class_sizes"], (1, 1, 20, 30, 12, 12, 20, 12, 12)
        )
        self.assertEqual(report["class_orders"], (1, 2, 3, 4, 5, 5, 6, 10, 10))
        self.assertIn("remaining eight irreducible matrix models", report["scope"])


if __name__ == "__main__":
    unittest.main()
