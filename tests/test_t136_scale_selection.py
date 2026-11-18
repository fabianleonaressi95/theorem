import unittest

from audits.t136_scale_selection import run_audit


class T136ScaleSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_audit()

    def test_both_probe_designs_are_identifiable(self):
        self.assertEqual(self.result["six_probe"]["moment_rank"], 6)
        self.assertEqual(self.result["twelve_probe_d_optimal"]["moment_rank"], 6)

    def test_scale_optimum_is_inside_the_tested_grid(self):
        for key in ("six_probe", "twelve_probe_d_optimal"):
            design = self.result[key]
            self.assertIn(design["grid_optimal_scale"], self.result["scales"])
            self.assertGreater(design["grid_optimal_scale"], min(self.result["scales"]))
            self.assertLess(design["grid_optimal_scale"], max(self.result["scales"]))

    def test_expected_error_separates_bias_and_noise(self):
        for key in ("six_probe", "twelve_probe_d_optimal"):
            for row in self.result[key]["scale_records"]:
                expected = (row["bias_l2"]**2 + row["covariance_trace"])**0.5
                self.assertAlmostEqual(
                    row["expected_total_rmse_l2"], expected, places=12
                )
                self.assertGreaterEqual(row["noise_rms_l2"], 0.0)


if __name__ == "__main__":
    unittest.main()
