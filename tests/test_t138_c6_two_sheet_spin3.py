import unittest
from scripts.audit_t138_c6_two_sheet_spin3 import C, U, S, tr, mm, eye, scale

class TestT138(unittest.TestCase):
    def test_all_36_entries(self):
        self.assertEqual(mm(C, C), scale(5, eye(6)))

    def test_block_identities(self):
        st = tr(S)
        target = tuple(tuple(4*int(i == j)-1 for j in range(3)) for i in range(3))
        self.assertEqual(mm(S, st), target)
        self.assertEqual(mm(st, S), target)
        self.assertEqual(mm(U, S), mm(S, U))
        self.assertEqual(
            tuple(tuple(x+y for x, y in zip(a, b)) for a, b in zip(mm(U,U), mm(S,st))),
            scale(5, eye(3)),
        )

    def test_symmetry_and_zero_trace(self):
        self.assertEqual(tr(C), C)
        self.assertEqual(sum(C[i][i] for i in range(6)), 0)

if __name__ == "__main__":
    unittest.main()
