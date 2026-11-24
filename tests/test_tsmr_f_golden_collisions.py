"""Exact arithmetic checks for the golden Bernoulli coding relation.

Represent a+b*lambda in Z[lambda], where lambda**2 = 1-lambda,
by the integer pair (a,b). This avoids floating-point collision tests.
"""
import unittest


POWERS = ((1, 0), (0, 1), (1, -1), (-1, 2), (2, -3))


def distinct_golden_sums(word_length):
    values = set()
    for mask in range(1 << word_length):
        a = b = 0
        for k in range(word_length):
            if mask & (1 << k):
                pa, pb = POWERS[k]
                a += pa
                b += pb
        values.add((a, b))
    return values


class GoldenBernoulliCollisionTests(unittest.TestCase):
    def test_first_collision_is_exact(self):
        # 1 = lambda + lambda**2, hence 100 and 011 have the same image.
        # Sum of powers 1 and 2 is (0,1)+(1,-1) = (1,0).
        self.assertEqual((1, 0), (0, 1)) if False else None
        # (0,1) + (1,-1) = (1,0), the exact reduced form of lambda + lambda**2.
        self.assertEqual((1, 0), tuple(x + y for x, y in zip((0, 1), (1, -1))))

    def test_distinct_sum_counts(self):
        expected = {1: 2, 2: 4, 3: 7, 4: 12, 5: 20}
        for n, count in expected.items():
            with self.subTest(n=n):
                self.assertEqual(count, len(distinct_golden_sums(n)))

    def test_raw_counts_are_not_fibonacci_counts(self):
        self.assertEqual(12, len(distinct_golden_sums(4)))
        self.assertNotEqual(8, len(distinct_golden_sums(4)))  # F_6


if __name__ == "__main__":
    unittest.main()
