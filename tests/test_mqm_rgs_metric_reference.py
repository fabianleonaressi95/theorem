import unittest
import numpy as np
from audits.morphodynamics.q6_mqm_metric_reference import (
    metric_reference, metric_reference_report, rgs_edge_lengths,
    rgs_psu_raw_coframes, rgs_psu_unit_coframes, a13_action_derivation_audit,
)
from audits.morphodynamics.q6_mqm_symmetry import q6_edges, edge_permutation
from audits.morphodynamics.q6_mqm_anisotropic_stabilizer import rgs_gate_vertex_permutations

class TestMQMRGSPsuMetricReference(unittest.TestCase):
    def test_positive_finite_edgewise_reference(self):
        x=metric_reference()
        self.assertEqual(x.shape,(192,))
        self.assertTrue(np.all(np.isfinite(x)))
        self.assertTrue(np.all(np.exp(x)>0))

    def test_reconstructed_unit_coframe_hash_matches_a13_manifest(self):
        report=metric_reference_report()
        self.assertTrue(report["edge_order_matches_A13_manifest"])
        self.assertTrue(report["normalized_coframe_matches_A13_manifest"])
        self.assertLessEqual(report["normalized_coframe_norm_residual"],1e-14)

    def test_raw_and_unit_coframes_are_not_confused(self):
        raw=rgs_psu_raw_coframes()
        unit=rgs_psu_unit_coframes()
        self.assertEqual(raw.shape,(192,4))
        self.assertEqual(unit.shape,(192,4))
        np.testing.assert_allclose(np.linalg.norm(unit,axis=1),1.0,atol=1e-14)
        self.assertGreater(np.ptp(np.linalg.norm(raw,axis=1)),1e-3)
        self.assertEqual(len(np.unique(np.round(rgs_edge_lengths(),12))),13)

    def test_directional_rms_pairs_follow_rgs_symmetry(self):
        d=metric_reference_report()["directional_lengths"]
        for a,b in ((0,1),(1,2),(3,4)):
            self.assertAlmostEqual(d[str(a)]["rms_raw_coframe_length"],
                                   d[str(b)]["rms_raw_coframe_length"],places=12)
        self.assertNotAlmostEqual(d["2"]["rms_raw_coframe_length"],
                                  d["3"]["rms_raw_coframe_length"],places=6)

    def test_all_sixteen_gates_preserve_edgewise_reference(self):
        x=metric_reference()
        self.assertEqual(len(rgs_gate_vertex_permutations()),16)
        for p in rgs_gate_vertex_permutations():
            ep=np.asarray(edge_permutation(p),dtype=int)
            np.testing.assert_allclose(x,x[ep],atol=1e-12,rtol=0.0)

    def test_metric_graph_dirichlet_matrix_is_symmetric_psd(self):
        from audits.morphodynamics.q6_mqm_metric_reference import metric_graph_energy_matrix
        K=metric_graph_energy_matrix()
        np.testing.assert_allclose(K,K.T,atol=1e-12)
        self.assertGreaterEqual(float(np.linalg.eigvalsh(K)[0]),-1e-10)
        self.assertAlmostEqual(float(np.linalg.norm(K@np.ones(64))),0.0,places=10)

    def test_a13_action_does_not_yet_derive_inverse_length_weight(self):
        audit=a13_action_derivation_audit()
        self.assertFalse(audit["inverse_raw_coframe_length_derived_by_current_A13_action"])
        self.assertEqual(audit["coframe_in_fermion_operator"],"normalized unit coframe ehat_e")

    def test_report_confirms_full_gate_survival_and_provenance(self):
        report=metric_reference_report()
        self.assertEqual(report["edge_count"],192)
        self.assertEqual(report["rgs_q6_gate_group_order"],16)
        self.assertTrue(report["all_16_gates_preserve_reference"])
        self.assertTrue(report["normalized_coframe_matches_A13_manifest"])
        self.assertLessEqual(report["max_reference_invariance_residual"],1e-12)

if __name__=="__main__":
    unittest.main()
