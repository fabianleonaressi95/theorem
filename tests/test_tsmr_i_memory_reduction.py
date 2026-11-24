import unittest

from audits.tsmr_i_memory_reduction import audit


class GoldenMemoryReductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = audit()

    def test_second_harmonic_complement_is_contracting_in_compression(self):
        self.assertLess(self.result["D_spectral_radius"], 0.22)

    def test_memory_kernel_decays_in_first_iterations(self):
        norms = self.result["memory_kernel_norms"]
        self.assertGreater(norms["0"], norms["1"])
        self.assertGreater(norms["1"], norms["2"])
        self.assertGreater(norms["2"], norms["3"])

    def test_nonzero_frequency_dependent_self_energy(self):
        self.assertGreater(
            self.result["self_energy_frobenius_at_z_1"], 0.09
        )

    def test_effective_operator_is_active_block_plus_self_energy(self):
        a = self.result["retained_active_block_A11"]
        s = self.result["self_energy_at_z_1"]
        effective = self.result["effective_active_operator_at_z_1"]
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(effective[i][j], a[i][j] + s[i][j], places=12)


if __name__ == "__main__":
    unittest.main()
