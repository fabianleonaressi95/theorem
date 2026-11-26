import unittest
from math import comb

from models.eqc_ternary import (
    all_words, decode, encode, flip_sign, hamming_distance, neighbors,
    q6_binary_words, qutrit_clock, qutrit_shift, matrix_multiply,
    conjugate_transpose, is_identity, ternary_hamming_spectrum,
)


class TestEsagrammaticQuantumComputing(unittest.TestCase):
    def test_exact_state_count_and_bijection(self):
        words = list(all_words())
        self.assertEqual(len(words), 729)
        self.assertEqual(len({encode(w) for w in words}), 729)
        for index, word in enumerate(words):
            self.assertEqual(encode(word), index)
            self.assertEqual(decode(index), word)

    def test_ternary_hamming_graph_degree_and_edge_count(self):
        words = list(all_words())
        self.assertTrue(all(len(list(neighbors(w))) == 12 for w in words))
        self.assertEqual(len(words) * 12 // 2, 4374)
        for word in words[::37]:
            self.assertTrue(all(hamming_distance(word, n) == 1
                                for n in neighbors(word)))

    def test_q6_is_induced_binary_subgraph(self):
        words = list(q6_binary_words())
        self.assertEqual(len(words), 64)
        binary_set = set(words)
        induced_edges = sum(
            1 for w in words for n in neighbors(w) if n in binary_set
        )
        self.assertTrue(all(
            sum(1 for n in neighbors(w) if n in binary_set) == 6
            for w in words
        ))
        self.assertEqual(induced_edges, 384)  # oriented edge count
        self.assertEqual(induced_edges // 2, 192)

    def test_spectrum_multiplicities(self):
        spectrum = ternary_hamming_spectrum()
        self.assertEqual(spectrum, tuple(
            (12 - 3*k, comb(6, k) * 2**k) for k in range(7)))
        self.assertEqual(sum(m for _, m in spectrum), 729)

    def test_qutrit_weyl_relations_and_unitarity(self):
        x, z = qutrit_shift(), qutrit_clock()
        ident = tuple(tuple(1 if i == j else 0 for j in range(3))
                      for i in range(3))
        x3 = matrix_multiply(matrix_multiply(x, x), x)
        z3 = matrix_multiply(matrix_multiply(z, z), z)
        self.assertTrue(is_identity(x3))
        self.assertTrue(is_identity(z3))
        self.assertTrue(is_identity(matrix_multiply(x, conjugate_transpose(x))))
        self.assertTrue(is_identity(matrix_multiply(z, conjugate_transpose(z))))
        omega = z[1][1]
        zx = matrix_multiply(z, x)
        xz = matrix_multiply(x, z)
        self.assertTrue(all(abs(zx[i][j] - omega*xz[i][j]) < 1e-12
                            for i in range(3) for j in range(3)))

    def test_sign_flip_is_involution(self):
        word = (-1, 0, 1, -1, 1, 0)
        self.assertEqual(flip_sign(flip_sign(word, 2), 2), word)
        self.assertEqual(flip_sign(word, 0), (1, 0, 1, -1, 1, 0))


if __name__ == "__main__":
    unittest.main()
