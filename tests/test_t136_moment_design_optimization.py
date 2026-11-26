import unittest

from audits.t136_moment_design_optimization import run_audit


class T136MomentDesignOptimizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_audit()

    def test_d_optimal_design_is_full_rank(self):
        self.assertEqual(self.result["selected_probe_count"], 12)
        self.assertEqual(self.result["rank"], 6)

    def test_design_improves_conditioning_over_baseline(self):
        self.assertLess(self.result["condition_number"], 3.0)
        self.assertGreater(self.result["condition_number_reduction_factor"], 5.0)


if __name__ == "__main__":
    unittest.main()
