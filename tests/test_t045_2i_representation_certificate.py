import unittest

from src.t045_2i_representation_certificate import run_certificate


class TestT045Exact2IRepresentationCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = run_certificate(max_projector_degree=13)

    def test_finite_group_and_character_layer(self):
        self.assertEqual(self.report["status"], "PASS")
        self.assertEqual(self.report["group_order"], 120)
        self.assertEqual(self.report["sum_squared_dimensions"], 120)
        self.assertEqual(self.report["matrix_coefficient_schur_entries"], 14400)

    def test_all_projector_degrees_are_pairwise_audited(self):
        reports = self.report["projectors_all_pairs_degrees_0_to_max"]
        self.assertEqual(len(reports), 14)
        self.assertTrue(all(r["orthogonal_pairs"] == 36 for r in reports))

    def test_matrix_units_are_exhaustive(self):
        reports = self.report["matrix_units_exhaustive"]
        self.assertEqual(len(reports), 9)
        self.assertTrue(all(r["quadruples_checked"] > 0 for r in reports))


if __name__ == "__main__":
    unittest.main()
