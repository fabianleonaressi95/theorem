import unittest

from audits.tsmr_i_markov_blocks import audit


class GoldenMarkovBlockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = audit(samples=30000, terms=40, seed=20261124)
        cls.matrix = cls.result["operator_matrix"]

    def test_constant_mode_is_preserved(self):
        # M_g 1 = 1; in this convention the constant column is e_2.
        self.assertAlmostEqual(1.0, self.matrix[2][2], delta=2e-3)
        for i in (0, 1, 3, 4):
            self.assertAlmostEqual(0.0, self.matrix[i][2], delta=2e-2)

    def test_active_plane_is_not_invariant_numerically(self):
        # (I-Pi_1) M_g Pi_1 is nonzero at stable finite-sample scale.
        self.assertGreater(
            self.result["complement_from_active_frobenius"], 0.08
        )

    def test_complement_does_not_reduce_to_active_plane(self):
        # Pi_1 M_g (I-Pi_1) is also nonzero; M_g is not self-adjoint.
        self.assertGreater(
            self.result["active_from_complement_frobenius"], 0.8
        )

    def test_markov_operator_matrix_is_not_symmetric(self):
        asymmetry = max(
            abs(self.matrix[i][j] - self.matrix[j][i])
            for i in range(5) for j in range(5)
        )
        self.assertGreater(asymmetry, 0.2)


if __name__ == "__main__":
    unittest.main()
