import unittest

from audits.t136_bias_noise_convergence import (
    FINE_SCALES, RESOLUTIONS, run_audit,
)


class T136BiasNoiseConvergenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_audit()

    def test_finer_grid_extends_below_previous_minimum(self):
        self.assertLess(min(FINE_SCALES), 0.0009)
        self.assertEqual(len(FINE_SCALES), 7)

    def test_both_designs_remain_identifiable(self):
        for design in self.result["designs"].values():
            self.assertEqual(design["moment_rank"], 6)

    def test_two_resolution_levels_are_reported(self):
        expected = {f"q{order}_rk{steps}" for order, steps in RESOLUTIONS}
        for design in self.result["designs"].values():
            self.assertEqual(
                set(design["resolution_records"].keys()), expected
            )
            for record in design["resolution_sensitivity"]:
                self.assertGreaterEqual(record["bias_change"], 0.0)
                self.assertGreaterEqual(record["noise_change"], 0.0)
                self.assertGreaterEqual(record["rho_change"], 0.0)


if __name__ == "__main__":
    unittest.main()
