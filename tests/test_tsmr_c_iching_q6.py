import unittest
from fractions import Fraction

from audits.tsmr_c_iching_q6 import (
    golden_value,
    non_lumpable_classes,
    q6_edge_count,
    q6_neighbors,
    scalar_classes,
    trigram_name,
    q6_walk_spectrum,
    graph_directed_hull,
    first_level_hull_overlap_count,
    fourier_transfer_matrix,
    minimum_translation_gap_pair,
    translation_multiplicity_profile,
)


class TSMRIChingGoldenQ6Tests(unittest.TestCase):
    def test_trigram_identification_bottom_to_top(self):
        self.assertEqual(trigram_name(0b100), "Zhen")
        self.assertEqual(trigram_name(0b011), "Xun")

    def test_exact_zhen_xun_golden_collision(self):
        # Printed order is bottom-to-top: the leftmost digit has weight 1.
        self.assertEqual(golden_value(0b100, 3), (1, 0))
        self.assertEqual(golden_value(0b011, 3), (1, 0))
        self.assertEqual(golden_value(0b001, 3), (1, -1))

    def test_eight_trigrams_have_seven_golden_values(self):
        self.assertEqual(len(scalar_classes(3)), 7)

    def test_hexagram_space_is_q6(self):
        self.assertEqual(len(q6_neighbors(0)), 6)
        self.assertEqual(q6_edge_count(), 192)
        self.assertEqual(len(scalar_classes(6)), 33)

    def test_scalar_partition_is_not_q6_lumpable(self):
        # Exact pair arithmetic finds 21 of the 33 scalar classes fail
        # the equitable-partition criterion for the Q6 line-flip walk.
        self.assertEqual(len(non_lumpable_classes(6)), 21)

    def test_exact_translation_collision_multiplicities(self):
        self.assertEqual(
            translation_multiplicity_profile(),
            ((1, 12), (2, 12), (3, 8), (4, 1)),
        )

    def test_minimum_distinct_translation_gap_is_lambda_six(self):
        # lambda**6 = 5 - 8*lambda in Z[lambda].
        self.assertEqual(minimum_translation_gap_pair(), (5, -8))

    def test_exact_q6_walk_spectrum(self):
        # Eigenvalues are 1-k/3 with binomial multiplicities C(6,k).
        self.assertEqual(
            q6_walk_spectrum(),
            ((Fraction(3, 3), 1), (Fraction(2, 3), 6), (Fraction(1, 3), 15),
             (Fraction(0, 3), 20), (Fraction(-1, 3), 15),
             (Fraction(-2, 3), 6), (Fraction(-3, 3), 1)),
        )

    def test_graph_directed_hulls_are_bounded_and_ordered(self):
        lower, upper = graph_directed_hull(16)
        self.assertEqual(len(lower), 64)
        self.assertEqual(len(upper), 64)
        self.assertTrue(all(a <= b for a, b in zip(lower, upper)))
        self.assertGreater(min(upper), 0.0)
        self.assertLess(max(lower), 2.7)

    def test_first_level_hull_overlaps_are_detected(self):
        # Convex hull overlap only; it is not a proof of support intersection.
        self.assertEqual(first_level_hull_overlap_count(16), 48)

    def test_fourier_transfer_matrix_at_zero_is_q6_transition_matrix(self):
        matrix = fourier_transfer_matrix(0.0)
        self.assertEqual(len(matrix), 64)
        self.assertTrue(all(abs(sum(row) - 1.0) < 1e-12 for row in matrix))
        self.assertTrue(all(abs(matrix[i][j] - matrix[j][i]) < 1e-12
                            for i in range(64) for j in range(64)))

    def test_neighbor_operation_is_single_line_change(self):
        for state in (0, 1, 0b100011, 63):
            neighbors = q6_neighbors(state)
            self.assertEqual(len(neighbors), 6)
            self.assertTrue(all((state ^ n).bit_count() == 1 for n in neighbors))


if __name__ == "__main__":
    unittest.main()
