import unittest

from audits.t136_nonquadratic_conformal import run_audit


class T136NonQuadraticConformalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_audit()

    def test_full_rank_moment_design_and_nonzero_cubic_jet(self):
        self.assertEqual(self.result["moment_matrix_rank"], 6)
        self.assertTrue(self.result["cubic_jet_nonzero"])
        self.assertLess(self.result["moment_matrix_condition_number"], 25.0)

    def test_first_order_truncation_convergence(self):
        errors = [row["truncation_l2_error"]
                  for row in self.result["scale_records"]]
        self.assertTrue(all(b < a for a, b in zip(errors, errors[1:])))
        ratios = self.result["successive_truncation_error_ratios"]
        self.assertTrue(all(0.65 < ratio < 0.85 for ratio in ratios))

    def test_relative_volume_noise_is_amplified_at_smaller_scales(self):
        changes = [row["reconstruction_change_from_relative_volume_noise"]
                   for row in self.result["scale_records"]]
        self.assertTrue(all(b > a for a, b in zip(changes, changes[1:])))


if __name__ == "__main__":
    unittest.main()
