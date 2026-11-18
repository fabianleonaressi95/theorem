import unittest

import numpy as np

from audits.t136_bias_noise_ratio import run_audit


class T136BiasNoiseRatioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_audit()

    def test_ratio_is_computed_for_every_scale(self):
        for key in ("six_probe", "twelve_probe_d_optimal"):
            design = self.result[key]
            self.assertEqual(len(design["scale_records"]), 10)
            for row in design["scale_records"]:
                self.assertAlmostEqual(
                    row["bias_noise_ratio"],
                    row["bias_frobenius"] / row["noise_rms_frobenius"],
                    places=12,
                )

    def test_effective_coefficients_reconstruct_the_ratio(self):
        sigma = self.result["relative_volume_noise_sigma"]
        for key in ("six_probe", "twelve_probe_d_optimal"):
            for row in self.result[key]["scale_records"]:
                reconstructed = (
                    row["effective_bias_coefficient"] * row["scale"]
                ) / (
                    row["effective_noise_coefficient"] * sigma
                    / row["scale"]**2
                )
                self.assertAlmostEqual(
                    row["bias_noise_ratio"], reconstructed, places=11
                )

    def test_grid_minimum_ratio_is_reported_without_forcing_sqrt_two(self):
        target = np.sqrt(2.0)
        for key in ("six_probe", "twelve_probe_d_optimal"):
            design = self.result[key]
            self.assertGreater(design["absolute_ratio_gap"], 0.0)
            self.assertAlmostEqual(
                design["absolute_ratio_gap"],
                abs(design["grid_optimum_bias_noise_ratio"] - target),
                places=12,
            )


if __name__ == "__main__":
    unittest.main()
