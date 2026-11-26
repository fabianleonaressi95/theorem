import math
import unittest

from audits.tsmr02_chaos_game import (
    AffineMap2D,
    anisotropic_ifs,
    barnsley_fern_ifs,
    chaos_game,
    common_diagonal_affinity_dimension,
    common_diagonal_pressure,
    finite_depth_pressure,
    sierpinski_ifs,
    singular_values_2x2,
    validate_ifs,
)


class TestTSMR02ChaosGame(unittest.TestCase):
    def test_sierpinski_ifs_is_contracting_and_probability_normalized(self):
        report = validate_ifs(sierpinski_ifs())
        self.assertEqual(report["map_count"], 3)
        self.assertAlmostEqual(report["probability_sum"], 1.0)
        self.assertLess(report["max_contraction"], 1.0)

    def test_sierpinski_chaos_game_stays_inside_triangle(self):
        points, counts = chaos_game(
            sierpinski_ifs(), iterations=30000, seed=20261124,
            start=(0.13, 0.21), burn_in=100,
        )
        self.assertEqual(len(points), 30000)
        self.assertEqual(sum(counts), 30100)
        height = math.sqrt(3.0) / 2.0
        for x, y in points:
            self.assertGreaterEqual(x, -1e-12)
            self.assertLessEqual(x, 1.0 + 1e-12)
            self.assertGreaterEqual(y, -1e-12)
            self.assertLessEqual(y, height + 1e-12)
            self.assertLessEqual(y, math.sqrt(3.0) * min(x, 1.0-x) + 1e-12)

    def test_chaos_game_is_reproducible_for_fixed_seed(self):
        first, first_counts = chaos_game(sierpinski_ifs(), 1000, seed=17)
        second, second_counts = chaos_game(sierpinski_ifs(), 1000, seed=17)
        self.assertEqual(first, second)
        self.assertEqual(first_counts, second_counts)

    def test_barnsley_fern_weighted_sampling(self):
        maps = barnsley_fern_ifs()
        report = validate_ifs(maps)
        self.assertEqual(report["map_count"], 4)
        points, counts = chaos_game(maps, 50000, seed=314159, start=(0, 0), burn_in=100)
        self.assertEqual(len(points), 50000)
        self.assertEqual(sum(counts), 50100)
        observed = [count / sum(counts) for count in counts]
        expected = [0.01, 0.79, 0.10, 0.10]
        for actual, target in zip(observed, expected):
            self.assertLess(abs(actual-target), 0.012)
        for x, y in points:
            self.assertTrue(math.isfinite(x) and math.isfinite(y))
            self.assertGreaterEqual(y, -1e-9)
            self.assertLess(y, 12.0)

    def test_anisotropic_linear_part_and_chaos_game(self):
        maps = anisotropic_ifs()
        report = validate_ifs(maps)
        self.assertAlmostEqual(report["max_contraction"], 0.5)
        sigma_max, sigma_min = singular_values_2x2(maps[0].matrix)
        self.assertAlmostEqual(sigma_max, 0.5)
        self.assertAlmostEqual(sigma_min, 0.25)
        points, _ = chaos_game(maps, 5000, seed=23)
        self.assertEqual(len(points), 5000)
        self.assertTrue(all(math.isfinite(x) and math.isfinite(y) for x, y in points))

    def test_exact_pressure_for_common_diagonal_anisotropic_ifs(self):
        self.assertAlmostEqual(common_diagonal_pressure(2, .5, .25, 1.0), 0.0)
        self.assertLess(common_diagonal_pressure(2, .5, .25, 1.1), 0.0)
        self.assertAlmostEqual(common_diagonal_affinity_dimension(2, .5, .25), 1.0)

    def test_finite_depth_pressure_matches_exact_diagonal_case(self):
        matrices = [item.matrix for item in anisotropic_ifs()]
        estimate = finite_depth_pressure(matrices, 1.5, depth=8)
        exact = common_diagonal_pressure(2, .5, .25, 1.5)
        self.assertAlmostEqual(estimate, exact, places=10)

    def test_invalid_probability_and_noncontractive_map_are_rejected(self):
        with self.assertRaises(ValueError):
            validate_ifs((sierpinski_ifs()[0],))
        expanding = (AffineMap2D(1.0, 0, 0, 0, .5, 0, 1.0, "not-contracting"),)
        with self.assertRaises(ValueError):
            validate_ifs(expanding)


if __name__ == "__main__":
    unittest.main()
