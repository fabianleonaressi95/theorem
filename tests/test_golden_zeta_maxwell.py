"""Regression checks for exact identities and the stated Fibonacci toy model.

Run from the repository root:
    python -m unittest discover -s tests -p 'test_golden_zeta_maxwell.py' -v

Only the Python standard library is required. Floating-point tests check identities
numerically; they do not replace symbolic proofs or establish physical claims.
"""
from __future__ import annotations

import math
import unittest
from fractions import Fraction


PHI = (1.0 + math.sqrt(5.0)) / 2.0
EPSILON = 1.0 / (2.0 * PHI**3)


def bernoulli_numbers(n: int) -> list[Fraction]:
    """Bernoulli numbers B_0,...,B_n with B_1=-1/2."""
    values: list[Fraction] = []
    for m in range(n + 1):
        total = Fraction(0)
        for k in range(m):
            total += math.comb(m + 1, k) * values[k]
        values.append(-total / (m + 1))
    return values


def zeta_even(n: int) -> float:
    """Return zeta(2n) from the exact Bernoulli-number formula."""
    if n < 1:
        raise ValueError("n must be positive")
    b = bernoulli_numbers(2 * n)[2 * n]
    return float(((-1) ** (n + 1)) * b) * (
        (2.0 * math.pi) ** (2 * n) / (2.0 * math.factorial(2 * n))
    )


def fibonacci_word(m: int) -> str:
    if m < 1:
        raise ValueError("m must be >= 1")
    words = ["", "A", "AB"]
    if m <= 2:
        return words[m]
    for _ in range(3, m + 1):
        words.append(words[-1] + words[-2])
    return words[m]


def segment_matrix(q: float, length: float, tension: float = 1.0):
    phase = q * length
    c, s = math.cos(phase), math.sin(phase)
    return (
        (c, s / (tension * q)),
        (-tension * q * s, c),
    )


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


class GoldenZetaIdentityTests(unittest.TestCase):
    def test_triangle_and_pentagon_closed_forms(self):
        delta3 = 3.0 * math.pi / math.tan(math.pi / 3.0)
        self.assertAlmostEqual(delta3, math.pi * math.sqrt(3.0), places=13)

        delta5 = 5.0 * math.pi / math.tan(math.pi / 5.0)
        closed = math.pi * math.sqrt(25.0 + 10.0 * math.sqrt(5.0))
        golden = math.pi * math.sqrt(15.0 + 20.0 * PHI)
        self.assertAlmostEqual(delta5, closed, places=13)
        self.assertAlmostEqual(delta5, golden, places=13)

    def test_zeta_series_for_delta5(self):
        # Delta_p = p^2 - 2 sum zeta(2n)/p^(2n-2).
        p = 5
        partial = p * p - 2.0 * sum(
            zeta_even(n) / (p ** (2 * n - 2)) for n in range(1, 31)
        )
        direct = p * math.pi / math.tan(math.pi / p)
        self.assertAlmostEqual(partial, direct, places=12)

    def test_golden_cotangent_zeta_series(self):
        partial = 1.0 / EPSILON - 2.0 * sum(
            zeta_even(n) * EPSILON ** (2 * n - 1) for n in range(1, 9)
        )
        direct = math.pi / math.tan(math.pi * EPSILON)
        self.assertAlmostEqual(partial, direct, places=12)

        # Periodicity: sqrt(5)/2 = 1 + epsilon.
        periodic = math.pi / math.tan(math.pi * math.sqrt(5.0) / 2.0)
        self.assertAlmostEqual(periodic, direct, places=12)


class FibonacciModelTests(unittest.TestCase):
    def test_word_counts_and_indexing(self):
        expected = {
            1: (1, 0),
            2: (1, 1),
            3: (2, 1),
            4: (3, 2),
            5: (5, 3),
            6: (8, 5),
        }
        for m, counts in expected.items():
            word = fibonacci_word(m)
            self.assertEqual((word.count("A"), word.count("B")), counts)

    def test_spatial_fractions_and_mean_density(self):
        theta_a = PHI**2 / (PHI**2 + 1.0)
        theta_b = 1.0 / (PHI**2 + 1.0)
        self.assertAlmostEqual(theta_a + theta_b, 1.0, places=14)
        rho_bar = theta_a * 1.0 + theta_b * PHI**2
        self.assertAlmostEqual(rho_bar, 1.0 + 1.0 / math.sqrt(5.0), places=14)

    def test_segment_matrix_has_unit_determinant(self):
        for q, length, tension in ((0.7, 0.13, 1.0), (2.1, 0.08, 1.7), (4.0, 0.2, 0.5)):
            matrix = segment_matrix(q, length, tension)
            determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            self.assertAlmostEqual(determinant, 1.0, places=14)

    def test_transfer_product_preserves_unit_determinant(self):
        word = fibonacci_word(6)
        matrices = [
            segment_matrix(1.3 if letter == "A" else 1.3 * PHI,
                           0.07 if letter == "A" else 0.07 / PHI)
            for letter in word
        ]
        product = ((1.0, 0.0), (0.0, 1.0))
        for matrix in matrices:  # left-to-right physical word: P_N ... P_1
            product = matmul(matrix, product)
        determinant = product[0][0] * product[1][1] - product[0][1] * product[1][0]
        self.assertAlmostEqual(determinant, 1.0, places=11)

    def test_homogeneous_boundary_derivative(self):
        q, length = 0.83, 1.4
        derivative_response = (q / length) / math.tan(q)
        normalized = length * derivative_response
        self.assertAlmostEqual(normalized, q / math.tan(q), places=14)


if __name__ == "__main__":
    unittest.main()
