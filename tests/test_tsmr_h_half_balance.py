import math
import unittest

from audits.tsmr_h_half_balance import (
    balanced_unit_vector,
    binary_entropy,
    golden_contraction,
    matvec,
    pentagonal_projector,
    projected_norm_squared,
    signed_first_level_gap,
)


class HalfBalanceTests(unittest.TestCase):
    def test_exact_geometric_transition(self):
        self.assertGreater(signed_first_level_gap(0.4), 0.0)
        self.assertAlmostEqual(0.0, signed_first_level_gap(0.5), places=14)
        self.assertLess(signed_first_level_gap(0.6), 0.0)

    def test_equal_bernoulli_weight_maximizes_entropy(self):
        h_half = binary_entropy(0.5)
        self.assertAlmostEqual(math.log(2.0), h_half, places=14)
        for p in (0.1, 0.25, 0.4, 0.6, 0.75, 0.9):
            self.assertLess(binary_entropy(p), h_half)

    def test_pentagonal_matrix_is_numerically_projector(self):
        p = pentagonal_projector()
        p2 = tuple(matvec(p, tuple(p[i][j] for i in range(5))) for j in range(5))
        # Compare P^2 with P column by column.
        for j in range(5):
            for i in range(5):
                self.assertAlmostEqual(p[i][j], p2[j][i], places=12)

    def test_balanced_vector_has_half_projection_and_five_quarters(self):
        q = balanced_unit_vector()
        self.assertAlmostEqual(1.0, sum(x * x for x in q), places=13)
        self.assertAlmostEqual(0.5, projected_norm_squared(q), places=12)
        p = pentagonal_projector()
        pq = matvec(p, q)
        # q^T G q = (5/2) ||Pq||^2
        self.assertAlmostEqual(1.25, 2.5 * sum(x * x for x in pq), places=12)

    def test_golden_parameter_is_in_overlap_regime(self):
        lam = golden_contraction()
        self.assertGreater(lam, 0.5)
        self.assertAlmostEqual(1.0, lam * lam + lam, places=14)
        self.assertLess(signed_first_level_gap(lam), 0.0)


if __name__ == "__main__":
    unittest.main()
