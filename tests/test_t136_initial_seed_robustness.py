import unittest

import numpy as np

from audits.t136_initial_seed_robustness import random_full_rank_seeds


class T136InitialSeedRobustnessTests(unittest.TestCase):
    def test_random_initial_seeds_are_distinct_and_full_rank(self):
        pool = np.random.default_rng(17).normal(size=(64, 6))
        seeds = random_full_rank_seeds(pool, pool_seed=1234, count=4)
        self.assertEqual(len(seeds), 4)
        self.assertEqual(len({tuple(seed) for seed in seeds}), 4)
        for seed in seeds:
            self.assertEqual(len(seed), 6)
            self.assertEqual(len(set(seed)), 6)
            self.assertEqual(np.linalg.matrix_rank(pool[seed]), 6)

    def test_seed_generation_is_reproducible(self):
        pool = np.random.default_rng(29).normal(size=(64, 6))
        self.assertEqual(
            random_full_rank_seeds(pool, 9876, count=3),
            random_full_rank_seeds(pool, 9876, count=3),
        )


if __name__ == "__main__":
    unittest.main()
