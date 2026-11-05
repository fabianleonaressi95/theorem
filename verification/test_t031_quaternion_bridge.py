"""Standalone finite audit for the T031 quaternionic bridge.

No external repository, package, or CI result is required.  This verifies the
standard 120-element coordinate model and the implemented left/right action
convention.  It is not a proof of the analytic Rumin descent theorem.
"""
import itertools
import math
import unittest

PHI = (1.0 + math.sqrt(5.0)) / 2.0
TOL = 3.0e-12


def qmul(a, b):
    """Hamilton product, scalar-first (w, x, y, z)."""
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return (
        aw*bw - ax*bx - ay*by - az*bz,
        aw*bx + ax*bw + ay*bz - az*by,
        aw*by - ax*bz + ay*bw + az*bx,
        aw*bz + ax*by - ay*bx + az*bw,
    )


def qnorm(q):
    return math.sqrt(sum(x*x for x in q))


def even_permutations(values):
    for p in itertools.permutations(values):
        inversions = sum(
            p[i] > p[j] for i in range(4) for j in range(i + 1, 4)
        )
        if inversions % 2 == 0:
            yield p


def binary_icosahedral_elements():
    """Return the 120 standard unit-quaternion coordinates of 2I."""
    elements = set()

    # 8 coordinate units.
    for axis in range(4):
        for sign in (-1.0, 1.0):
            q = [0.0] * 4
            q[axis] = sign
            elements.add(tuple(q))

    # 16 vertices of the half-coordinate family.
    for signs in itertools.product((-1.0, 1.0), repeat=4):
        elements.add(tuple(s / 2.0 for s in signs))

    # 96 even-permutation/sign variants of (0, 1, phi, phi^{-1}) / 2.
    base = (0.0, 1.0, PHI, 1.0 / PHI)
    for p in even_permutations(base):
        nonzero = [i for i, value in enumerate(p) if value != 0.0]
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            q = list(p)
            for i, sign in zip(nonzero, signs):
                q[i] *= sign / 2.0
            elements.add(tuple(q))

    return tuple(sorted(elements))


def unit_quaternion(axis, angle):
    norm = math.sqrt(sum(x*x for x in axis))
    v = tuple(math.sin(angle / 2.0) * x / norm for x in axis)
    return (math.cos(angle / 2.0),) + v


class TestT031QuaternionBridge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.group = binary_icosahedral_elements()
        cls.group_set = set(cls.group)

    def test_binary_icosahedral_cardinality_and_unit_norm(self):
        self.assertEqual(len(self.group), 120)
        self.assertEqual(len(self.group_set), 120)
        for g in self.group:
            self.assertAlmostEqual(qnorm(g), 1.0, delta=TOL)

    def test_closure_under_hamilton_product(self):
        # Check all 120 x 120 products against the generated coordinate set.
        for g in self.group:
            for h in self.group:
                product = qmul(g, h)
                key = tuple(round(x, 12) for x in product)
                self.assertIn(key, {
                    tuple(round(x, 12) for x in element)
                    for element in self.group_set
                })

    def test_left_2i_action_commutes_with_right_hopf_circle(self):
        samples = (
            (1.0, 0.0, 0.0, 0.0),
            unit_quaternion((1.0, 2.0, -1.0), 0.731),
            unit_quaternion((-2.0, 1.0, 3.0), 1.217),
        )
        angles = (0.0, 0.17, 0.5 * math.pi, math.pi, 1.73)
        hopf_axis = (1.0, 0.0, 0.0)  # fixed imaginary unit i
        max_commutator = 0.0
        max_norm_error = 0.0

        for g in self.group:
            for q in samples:
                for angle in angles:
                    h = unit_quaternion(hopf_axis, angle)
                    lhs = qmul(g, qmul(q, h))
                    rhs = qmul(qmul(g, q), h)
                    max_commutator = max(
                        max_commutator,
                        math.sqrt(sum((x-y)**2 for x, y in zip(lhs, rhs))),
                    )
                    max_norm_error = max(
                        max_norm_error, abs(qnorm(lhs)-1.0), abs(qnorm(rhs)-1.0)
                    )

        self.assertLess(max_commutator, TOL)
        self.assertLess(max_norm_error, TOL)


if __name__ == "__main__":
    unittest.main()
