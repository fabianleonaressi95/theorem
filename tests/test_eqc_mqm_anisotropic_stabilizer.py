import unittest

from audits.morphodynamics.q6_mqm_anisotropic_stabilizer import (
    anisotropic_gate_report, arbitrary_reference_stabilizer_order,
    directional_anisotropy, mqm_reference_stabilizer,
)
from audits.morphodynamics.q6_mqm_symmetry import q6_edges


class TestMQMAnisotropicRGSStabilizer(unittest.TestCase):
    def test_six_distinct_directional_values_leave_three_sign_flips(self):
        report = anisotropic_gate_report((0.1, 0.2, 0.3, 0.4, 0.5, 0.6))
        self.assertEqual(report["stabilizer_order"], 8)
        self.assertEqual(sum(report["surviving_generators"].values()), 3)
        self.assertFalse(report["survives_pair_swap"])

    def test_pair_equalities_restore_full_order_sixteen_subgroup(self):
        report = anisotropic_gate_report((0.1, 0.1, 0.3, 0.4, 0.4, 0.6))
        self.assertEqual(report["stabilizer_order"], 16)
        self.assertTrue(all(report["surviving_generators"].values()))

    def test_uniform_reference_preserves_all_sixteen_rgs_gates(self):
        self.assertEqual(len(mqm_reference_stabilizer((0.7,) * 192)), 16)

    def test_generic_edgewise_reference_has_trivial_rgs_stabilizer(self):
        self.assertEqual(arbitrary_reference_stabilizer_order(tuple(float(i) for i in range(192))), 1)

    def test_reference_expansion_matches_canonical_edge_direction(self):
        values = (10, 20, 30, 40, 50, 60)
        ref = directional_anisotropy(values)
        self.assertEqual(len(ref), 192)
        for value, (_, _, direction) in zip(ref, q6_edges()):
            self.assertEqual(value, values[direction])

    def test_stabilizer_is_a_subgroup_and_has_expected_order(self):
        for values, expected in [
            ((0.1,0.2,0.3,0.4,0.5,0.6), 8),
            ((0.1,0.1,0.3,0.4,0.4,0.6), 16),
            ((1,1,1,1,1,1), 16),
        ]:
            group = set(mqm_reference_stabilizer(directional_anisotropy(values)))
            self.assertEqual(len(group), expected)
            for a in group:
                for b in group:
                    self.assertIn(tuple(a[b[v]] for v in range(64)), group)


if __name__ == "__main__":
    unittest.main()
