import unittest

from audits.tsmr_c_iching_q6 import (
    golden_value,
    non_lumpable_classes,
    q6_edge_count,
    q6_neighbors,
    scalar_classes,
    trigram_name,
)


class TSMRIChingGoldenQ6Tests(unittest.TestCase):
    def test_trigram_identification_bottom_to_top(self):
        self.assertEqual(trigram_name(0b100), "Zhen")
        self.assertEqual(trigram_name(0b011), "Xun")

    def test_exact_zhen_xun_golden_collision(self):
        self.assertEqual(golden_value(0b100, 3), (1, 0))
        self.assertEqual(golden_value(0b011, 3), (1, 0))

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

    def test_neighbor_operation_is_single_line_change(self):
        for state in (0, 1, 0b100011, 63):
            neighbors = q6_neighbors(state)
            self.assertEqual(len(neighbors), 6)
            self.assertTrue(all((state ^ n).bit_count() == 1 for n in neighbors))


if __name__ == "__main__":
    unittest.main()
