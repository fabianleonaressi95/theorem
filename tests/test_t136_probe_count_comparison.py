import unittest

from audits.t136_probe_count_comparison import run_audit


class T136ProbeCountComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_audit()

    def test_twelve_probe_design_is_better_conditioned(self):
        self.assertLess(self.result["twelve_probe_condition_number"],
                        self.result["six_probe_condition_number"])

    def test_twelve_probes_reduce_bias_and_noise_sensitivity(self):
        for row in self.result["scale_records"]:
            self.assertLess(row["twelve_probe_truncation_error"],
                            row["six_probe_truncation_error"])
            self.assertLess(row["twelve_probe_noise_change"],
                            row["six_probe_noise_change"])


if __name__ == "__main__":
    unittest.main()
