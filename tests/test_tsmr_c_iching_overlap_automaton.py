import unittest
from fractions import Fraction

from audits.tsmr_c_iching_overlap_automaton import (
    exact_hull_endpoints,
    exact_global_diameter,
    build_overlap_automaton,
    max_row_sum_power,
    overlap_dimension_audit,
)


class TSMRIChingExactOverlapAutomatonTests(unittest.TestCase):
    def test_exact_bellman_extrema(self):
        lower = exact_hull_endpoints("min")
        upper = exact_hull_endpoints("max")
        self.assertEqual(min(lower, key=lambda x: float(x[0] + x[1] * Fraction(6180339887498948, 10**16))),
                         (Fraction(7, 40), Fraction(-11, 40)))
        self.assertEqual(max(upper, key=lambda x: float(x[0] + x[1] * Fraction(6180339887498948, 10**16))),
                         (Fraction(73, 40), Fraction(51, 40)))
        self.assertEqual(exact_global_diameter(), (Fraction(33, 20), Fraction(31, 20)))

    def test_finite_pair_automaton_cardinality(self):
        states, outgoing, _ = build_overlap_automaton()
        self.assertEqual(len(states), 5566)
        self.assertEqual(sum(map(len, outgoing.values())), 34762)
        self.assertEqual(len({(s[2], s[3]) for s in states}), 13)
        self.assertEqual(sum(1 for s in states if s[2] == 0 and s[3] == 0), 4096)

    def test_exact_path_count_certificate_and_dimension_bound(self):
        states, outgoing, _ = build_overlap_automaton()
        maximum = max_row_sum_power(outgoing, 20)
        self.assertEqual(maximum, 9412274067081088)
        audit = overlap_dimension_audit(20)
        self.assertGreater(audit["correlation_dimension_lower_bound"], 0.60)
        self.assertLess(audit["correlation_dimension_lower_bound"], 0.61)


if __name__ == "__main__":
    unittest.main()
