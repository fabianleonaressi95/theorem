import unittest
from itertools import permutations

from models.eqc_automorphism import (
    all_ternary_words, binary_q6_automorphism_order,
    generators_preserve_hamming_distance, hamming_distance,
    permute_lines, symbol_inversion, symbol_shift,
    ternary_hamming_graph_order,
)


class TestEQCAutomorphismStructure(unittest.TestCase):
    def test_local_symbol_generators_generate_s3(self):
        # The cyclic 3-cycle and semantic polarity transposition generate S3.
        shift = {-1: 0, 0: 1, 1: -1}
        inv = {-1: 1, 0: 0, 1: -1}
        identity = {-1: -1, 0: 0, 1: 1}
        generators = [shift, inv]
        seen = {tuple(identity[x] for x in (-1, 0, 1))}
        frontier = [identity]
        while frontier:
            current = frontier.pop()
            for generator in generators:
                composed = {x: generator[current[x]] for x in (-1, 0, 1)}
                key = tuple(composed[x] for x in (-1, 0, 1))
                if key not in seen:
                    seen.add(key)
                    frontier.append(composed)
        self.assertEqual(len(seen), 6)

    def test_line_permutations_form_six_position_symmetries(self):
        self.assertEqual(len(list(permutations(range(6)))), 720)
        word = (-1, 0, 1, -1, 0, 1)
        self.assertEqual(
            permute_lines(permute_lines(word, (5, 4, 3, 2, 1, 0)),
                          (5, 4, 3, 2, 1, 0)),
            word,
        )

    def test_generators_preserve_ternary_hamming_adjacency(self):
        self.assertTrue(generators_preserve_hamming_distance())

    def test_local_symbol_maps_are_bijections_and_isometries(self):
        words = list(all_ternary_words())
        for transform in (
            lambda w: symbol_shift(w, (0, 3)),
            lambda w: symbol_inversion(w, (1, 4)),
        ):
            images = [transform(w) for w in words]
            self.assertEqual(len(set(images)), 729)
            for w in words[::53]:
                for v in words[::71]:
                    self.assertEqual(hamming_distance(w, v),
                                     hamming_distance(transform(w), transform(v)))

    def test_exact_automorphism_group_orders(self):
        self.assertEqual(ternary_hamming_graph_order(), 33592320)
        self.assertEqual(binary_q6_automorphism_order(), 46080)
        self.assertEqual(ternary_hamming_graph_order()
                         // binary_q6_automorphism_order(), 729)


if __name__ == "__main__":
    unittest.main()
