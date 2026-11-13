import unittest

from audits.morphodynamics.q6_mqm_symmetry import (
    count_reference_stabilizer, directional_reference_weights,
    edge_permutation, induced_rgs_permutations, preserves_q6_adjacency,
    q6_automorphism_order, q6_edges, q6_vertex_permutation,
    rgs_q6_stabilizer_report,
)


class TestQ6MQMSymmetry(unittest.TestCase):
    def test_canonical_q6_counts_and_full_automorphism_order(self):
        self.assertEqual(len(q6_edges()), 192)
        self.assertEqual(q6_automorphism_order(), 46080)

    def test_generators_act_as_graph_and_edge_permutations(self):
        p = q6_vertex_permutation(mask=37, coordinate_order=(2, 5, 1, 4, 0, 3))
        self.assertTrue(preserves_q6_adjacency(p))
        self.assertEqual(sorted(edge_permutation(p)), list(range(192)))

    def test_uniform_reference_has_full_q6_stabilizer(self):
        self.assertEqual(count_reference_stabilizer((0.0,) * 192), 46080)

    def test_distinct_directional_reference_has_translation_stabilizer(self):
        xstar = directional_reference_weights((0., 1., 2., 3., 4., 5.))
        self.assertEqual(count_reference_stabilizer(xstar), 64)

    def test_generic_edgewise_reference_has_trivial_stabilizer(self):
        self.assertEqual(count_reference_stabilizer(tuple(range(192))), 1)

    def test_rgs_induced_oh_stabilizer_is_order_16(self):
        report = rgs_q6_stabilizer_report()
        self.assertEqual(report["induced_Oh_order"], 48)
        self.assertEqual(report["Q6_adjacency_preserving_order"], 16)
        self.assertEqual(report["not_Q6_adjacency_preserving"], 32)
        self.assertTrue(report["survivors_fix_first_coordinate_axis"])
        self.assertEqual(report["survivor_group_order_formula"], 16)

    def test_rgs_induced_maps_are_permutations(self):
        actions = induced_rgs_permutations()
        self.assertEqual(len(actions), 48)
        self.assertTrue(all(sorted(p) == list(range(64)) for p in actions))


if __name__ == "__main__":
    unittest.main()
