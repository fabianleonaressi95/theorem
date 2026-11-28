import unittest

from scripts.audit_q6_handle_words_t168 import (
    attaching_words, audit, boundary_matrix_rank, square_faces, spanning_tree
)


class TestQ6HandleWordsT168(unittest.TestCase):
    def test_cube_counts_and_tree(self):
        parent, tree = spanning_tree()
        self.assertEqual(len(parent), 64)
        self.assertEqual(len(tree), 63)
        self.assertEqual(len(square_faces()), 240)

    def test_square_words(self):
        chords, words = attaching_words()
        self.assertEqual(len(chords), 129)
        self.assertEqual(len(words), 240)
        self.assertTrue(all(words))
        self.assertTrue(all(all(sign in (-1, 1) for _, sign in w) for w in words))

    def test_exact_boundary_rank_and_homology(self):
        self.assertEqual(boundary_matrix_rank(), 129)
        result = audit()
        self.assertEqual(result["H2_rank"], 111)
        self.assertEqual(result["Euler_characteristic"], 112)


if __name__ == "__main__":
    unittest.main()
