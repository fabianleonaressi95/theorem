import unittest
from audits.morphodynamics.q6_mqm_symmetry import (
    induced_rgs_permutations, preserves_q6_adjacency, signed_permutation_matrices,
)
from models.eqc_rgs_gates import (
    DIM, apply_gate, lifted_group_on_q6, q6_subspace_indices,
    rgs_generators, rgs_q6_group_on_labels,
)


def generated_group_from_declared_gates():
    """Compute closure from the four declared gates, not from a formula."""
    sub = q6_subspace_indices()
    lookup = {state: i for i, state in enumerate(sub)}
    generators = []
    for gate in rgs_generators():
        generators.append(tuple(
            lookup[apply_gate(state, gate)] for state in sub
        ))
    identity = tuple(range(64))
    group = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            composed = tuple(generator[current[i]] for i in range(64))
            if composed not in group:
                group.add(composed)
                frontier.append(composed)
    return group


class TestEQCRGSGates(unittest.TestCase):
    def test_four_generators(self):
        self.assertEqual(len(rgs_generators()), 4)
        self.assertEqual({g[1] for g in rgs_generators() if g[0] == "P"}, {3, 4, 5})
        self.assertEqual(rgs_generators()[-1], ("PAIRSWAP", 1, 2, 4, 5))

    def test_each_gate_is_unitary_basis_permutation(self):
        for gate in rgs_generators():
            image = [apply_gate(i, gate) for i in range(DIM)]
            self.assertEqual(sorted(image), list(range(DIM)))

    def test_q6_subspace_is_invariant(self):
        sub = set(q6_subspace_indices())
        for gate in rgs_generators():
            self.assertEqual({apply_gate(i, gate) for i in sub}, sub)

    def test_generated_group_order_is_exactly_16(self):
        generated = generated_group_from_declared_gates()
        self.assertEqual(len(generated), 16)
        self.assertEqual(generated, lifted_group_on_q6())

    def test_generated_group_is_closed(self):
        group = generated_group_from_declared_gates()
        for a in group:
            for b in group:
                self.assertIn(tuple(a[b[i]] for i in range(64)), group)

    def test_exact_match_with_adjacency_preserving_rgs_actions(self):
        matrices = signed_permutation_matrices()
        actions = induced_rgs_permutations()
        actual = {
            action for action in actions if preserves_q6_adjacency(action)
        }
        self.assertEqual(len(actual), 16)
        self.assertEqual(actual, generated_group_from_declared_gates())


if __name__ == "__main__":
    unittest.main()
