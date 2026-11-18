import unittest

import numpy as np

from audits.t136_scale_selection import (
    TENSOR_METRIC, run_audit,
)


class T136ScaleSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_audit()

    def test_both_probe_designs_are_identifiable(self):
        self.assertEqual(self.result["six_probe"]["moment_rank"], 6)
        self.assertEqual(self.result["twelve_probe_d_optimal"]["moment_rank"], 6)

    def test_deterministic_grid_minima_are_reproduced(self):
        self.assertEqual(self.result["six_probe"]["grid_optimal_scale"], 0.00375)
        self.assertEqual(
            self.result["twelve_probe_d_optimal"]["grid_optimal_scale"], 0.0021
        )

    def test_scale_optimum_is_inside_the_tested_grid(self):
        for key in ("six_probe", "twelve_probe_d_optimal"):
            design = self.result[key]
            self.assertIn(design["grid_optimal_scale"], self.result["scales"])
            self.assertGreater(design["grid_optimal_scale"], min(self.result["scales"]))
            self.assertLess(design["grid_optimal_scale"], max(self.result["scales"]))

    def test_frobenius_metric_weights_off_diagonal_components(self):
        np.testing.assert_array_equal(
            np.diag(TENSOR_METRIC), np.array([1., 1., 1., 2., 2., 2.])
        )

    def test_expected_error_separates_tensor_bias_and_covariance(self):
        for key in ("six_probe", "twelve_probe_d_optimal"):
            for row in self.result[key]["scale_records"]:
                expected = (
                    row["bias_frobenius"]**2
                    + row["weighted_covariance_trace"]
                )**0.5
                self.assertAlmostEqual(
                    row["expected_total_rmse_frobenius"], expected, places=12
                )
                self.assertGreaterEqual(row["noise_rms_frobenius"], 0.0)


if __name__ == "__main__":
    unittest.main()
