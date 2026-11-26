from fractions import Fraction
import unittest


def influence_from_walsh(coefficients, coordinate):
    """Squared-difference influence from a sparse Walsh coefficient map."""
    return 4 * sum(
        value * value
        for subset, value in coefficients.items()
        if coordinate in subset
    )


def variance_from_walsh(coefficients):
    return sum(
        value * value
        for subset, value in coefficients.items()
        if subset
    )


class TestT109GeneralQnInfluence(unittest.TestCase):
    def test_total_influence_identity_and_degree_bounds(self):
        # Sparse exact Walsh data on Q_9, with degree at most three.
        coefficients = {
            frozenset(): Fraction(2, 7),
            frozenset({0}): Fraction(1, 3),
            frozenset({1, 4}): Fraction(2, 5),
            frozenset({2, 5, 8}): Fraction(1, 6),
        }
        influences = [
            influence_from_walsh(coefficients, i) for i in range(9)
        ]
        variance = variance_from_walsh(coefficients)
        weighted_sum = 4 * sum(
            len(subset) * value * value
            for subset, value in coefficients.items()
            if subset
        )
        self.assertEqual(sum(influences), weighted_sum)
        self.assertGreaterEqual(sum(influences), 4 * variance)
        self.assertLessEqual(sum(influences), 12 * variance)

    def test_q6_specialization(self):
        coefficients = {
            frozenset({0}): Fraction(1, 2),
            frozenset({1, 2}): Fraction(1, 3),
            frozenset({3, 4, 5}): Fraction(1, 4),
        }
        variance = variance_from_walsh(coefficients)
        influences = [
            influence_from_walsh(coefficients, i) for i in range(6)
        ]
        self.assertGreaterEqual(max(influences), Fraction(2, 3) * variance)

    def test_degree_one_family_rules_out_linear_dimension_free_constant(self):
        # f_n(x) = n^{-1} sum_i x_i: Var=1/n and I_i=4/n^2.
        for n in (4, 8, 16, 32):
            variance = Fraction(1, n)
            coordinate_influence = Fraction(4, n * n)
            self.assertEqual(
                coordinate_influence / variance, Fraction(4, n)
            )
        self.assertLess(Fraction(4, 32), Fraction(1, 4))


if __name__ == "__main__":
    unittest.main()
