import unittest
from audits.morphodynamics.q6_mqm_symmetry import induced_rgs_permutations, signed_permutation_matrices
from models.eqc_rgs_gates import DIM, apply_gate, lifted_group_on_q6, q6_subspace_indices, rgs_generators, rgs_q6_group_on_labels

class TestEQCRGSGates(unittest.TestCase):
    def test_four_generators(self):
        self.assertEqual(len(rgs_generators()),4)
        self.assertEqual({g[1] for g in rgs_generators() if g[0]=="P"},{3,4,5})
    def test_each_gate_is_unitary_basis_permutation(self):
        for gate in rgs_generators():
            image=[apply_gate(i,gate) for i in range(DIM)]
            self.assertEqual(sorted(image),list(range(DIM)))
    def test_q6_subspace_is_invariant(self):
        sub=set(q6_subspace_indices())
        for gate in rgs_generators():
            self.assertEqual({apply_gate(i,gate) for i in sub},sub)
    def test_group_order_and_closure(self):
        group=rgs_q6_group_on_labels()
        self.assertEqual(len(group),16)
        self.assertEqual(len(lifted_group_on_q6()),16)
        for a in group:
            for b in group:
                self.assertIn(tuple(a[b[i]] for i in range(64)),group)
    def test_exact_match_with_rgs_seed_induced_subgroup(self):
        matrices=signed_permutation_matrices()
        actions=induced_rgs_permutations()
        actual={action for m,action in zip(matrices,actions)
                if m[0][1]==m[0][2]==m[1][0]==m[2][0]==0}
        self.assertEqual(actual,lifted_group_on_q6())

if __name__=="__main__": unittest.main()
