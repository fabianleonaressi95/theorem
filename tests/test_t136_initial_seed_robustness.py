import unittest

import numpy as np

from audits.t136_initial_seed_robustness import (\n    a_optimal_six_seed, random_full_rank_seeds,\n)\nfrom audits import t136_exact_design_comparison as base
from audits import t136_exact_design_comparison as base
from audits.t136_initial_seed_robustness import (
    a_optimal_six_seed,
    random_full_rank_seeds,
)


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


    def test_a_seed_is_full_rank_and_no_worse_than_its_starts(self):
        rng = np.random.default_rng(41)
        pool = rng.normal(size=(24, 6))
        q_table = np.ones((24, len(base.SELECTION_SCALES)))
        d_seed = list(range(6))
        random_seeds = random_full_rank_seeds(pool, pool_seed=4321, count=3)
        selected, report = a_optimal_six_seed(
            pool, q_table, 4321, d_seed, random_seeds
        )
        self.assertEqual(len(selected), 6)
        self.assertEqual(np.linalg.matrix_rank(pool[selected]), 6)
        self.assertEqual(report["number_of_starts"], 4)
        objective = lambda ids: base.cached_subset_objective(
            ids, "A", pool, q_table
        )
        self.assertLessEqual(
            objective(selected),
            min(objective(ids) for ids in [d_seed] + random_seeds) + 1e-25,
        selected_objective = objective(selected)
        tolerance = 1.0e-12 * max(abs(selected_objective), 1.0e-30)
        self.assertLessEqual(
            selected_objective,
            min(objective(ids) for ids in [d_seed] + random_seeds) + tolerance,
        )
        selected_set = set(selected)
        for slot in range(6):
            for candidate in range(len(pool)):
                if candidate in selected_set:
                    continue
                trial = selected.copy()
                trial[slot] = candidate
                if np.linalg.matrix_rank(pool[trial]) == 6:
                    self.assertGreaterEqual(
                        objective(trial), objective(selected) - 1e-25
                        objective(trial), selected_objective - tolerance
                    )

    def test_seed_generation_is_reproducible(self):
        pool = np.random.default_rng(29).normal(size=(64, 6))
        self.assertEqual(
            random_full_rank_seeds(pool, 9876, count=3),
            random_full_rank_seeds(pool, 9876, count=3),
        )


if __name__ == "__main__":
    unittest.main()
