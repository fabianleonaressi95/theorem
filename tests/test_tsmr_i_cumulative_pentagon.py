import math
import unittest

from audits.tsmr_i_cumulative_pentagon import (
    balanced_vector,
    coefficients,
    fourier_basis,
    inner_product_on_uniform_coordinate,
    pentagonal_fourier_frame,
    pentagonal_projector,
    projected_energy,
)


class CumulativePentagonTests(unittest.TestCase):
    def test_real_dft_frame_is_orthogonal(self):
        u = pentagonal_fourier_frame()
        for i in range(5):
            for j in range(5):
                dot = sum(u[k][i] * u[k][j] for k in range(5))
                self.assertAlmostEqual(1.0 if i == j else 0.0, dot, places=12)

    def test_projector_is_rank_two_and_idempotent(self):
        p = pentagonal_projector()
        for i in range(5):
            for j in range(5):
                p2 = sum(p[i][k] * p[k][j] for k in range(5))
                self.assertAlmostEqual(p[i][j], p2, places=12)
        self.assertAlmostEqual(2.0, sum(p[i][i] for i in range(5)), places=12)

    def test_parseval_for_cumulative_coordinate_lift(self):
        q = (0.2, -0.4, 0.7, 0.1, -0.3)
        r = (0.5, 0.1, -0.2, 0.6, -0.1)
        lhs = inner_product_on_uniform_coordinate(q, r, samples=10000)
        rhs = sum(q[i] * r[i] for i in range(5))
        self.assertAlmostEqual(rhs, lhs, places=7)

    def test_exact_active_complement_balance(self):
        q = balanced_vector()
        self.assertAlmostEqual(1.0, sum(x * x for x in q), places=12)
        self.assertAlmostEqual(0.5, projected_energy(q), places=12)
        self.assertAlmostEqual(1.25, 2.5 * projected_energy(q), places=12)
        c = coefficients(q)
        self.assertAlmostEqual(0.5, c[0] ** 2 + c[1] ** 2, places=12)
        self.assertAlmostEqual(0.5, c[2] ** 2 + c[3] ** 2 + c[4] ** 2, places=12)

    def test_lifted_functions_are_real_and_finite(self):
        q = (1.0, 0.0, 0.0, 0.0, 0.0)
        for t in (0.0, 0.1, 0.25, 0.5, 0.75, 0.99, 1.0):
            value = sum(a * b for a, b in zip(coefficients(q), fourier_basis(t)))
            self.assertTrue(math.isfinite(value))


if __name__ == "__main__":
    unittest.main()
