import unittest

from audits.t136_pool_seed_robustness import TRIALS, summarize_trials


class T136PoolSeedRobustnessTests(unittest.TestCase):
    def test_trial_matrix_varies_pool_seed_and_pool_size(self):
        self.assertEqual(len(TRIALS), 5)
        sizes = {item["pool_size"] for item in TRIALS}
        self.assertEqual(sizes, {128, 256})
        seeds_128 = {
            item["pool_seed"] for item in TRIALS if item["pool_size"] == 128
        }
        self.assertEqual(len(seeds_128), 3)
        seeds_256 = {
            item["pool_seed"] for item in TRIALS if item["pool_size"] == 256
        }
        self.assertEqual(len(seeds_256), 2)
        for seed in seeds_256:
            self.assertIn(seed, seeds_128)

    def test_summary_counts_wins_and_reports_trial_dispersion(self):
        trials = [
            {
                "risk_design_beats_D": True,
                "risk_design_beats_A": True,
                "risk_design_beats_both": True,
                "risk_design_relative_reduction_vs_D": 0.20,
                "risk_design_relative_reduction_vs_A": 0.10,
            },
            {
                "risk_design_beats_D": True,
                "risk_design_beats_A": False,
                "risk_design_beats_both": False,
                "risk_design_relative_reduction_vs_D": 0.10,
                "risk_design_relative_reduction_vs_A": -0.02,
            },
        ]
        result = summarize_trials(trials)
        self.assertEqual(result["risk_design_beats_D_count"], 2)
        self.assertEqual(result["risk_design_beats_A_count"], 1)
        self.assertEqual(result["risk_design_beats_both_count"], 1)
        self.assertAlmostEqual(
            result["relative_risk_reduction_vs_D"]["mean"], 0.15
        )
        self.assertAlmostEqual(
            result["relative_risk_reduction_vs_D"]["standard_deviation_across_trials"],
            0.0707106781,
            places=8,
        )


if __name__ == "__main__":
    unittest.main()
