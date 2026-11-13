import unittest
import numpy as np
from audits.morphodynamics.q6_mqm_metric_reference import metric_reference, metric_reference_report, rgs_edge_lengths
from audits.morphodynamics.q6_mqm_symmetry import q6_edges, edge_permutation
from audits.morphodynamics.q6_mqm_anisotropic_stabilizer import rgs_gate_vertex_permutations

class TestMQMRGSMetricReference(unittest.TestCase):
    def test_positive_finite_reference(self):
        x=metric_reference()
        self.assertEqual(x.shape,(192,))
        self.assertTrue(np.all(np.isfinite(x)))
        self.assertTrue(np.all(np.exp(x)>0))

    def test_seed_metric_has_13_edge_length_classes(self):
        lengths=rgs_edge_lengths()
        self.assertEqual(lengths.shape,(192,))
        self.assertEqual(len(np.unique(np.round(lengths,12))),13)

    def test_directional_rms_pairs_follow_rgs_symmetry(self):
        d=metric_reference_report()["directional_rms_lengths"]
        self.assertAlmostEqual(d["0"]["rms_length"],d["1"]["rms_length"],places=12)
        self.assertAlmostEqual(d["1"]["rms_length"],d["2"]["rms_length"],places=12)
        self.assertAlmostEqual(d["3"]["rms_length"],d["4"]["rms_length"],places=12)
        self.assertNotAlmostEqual(d["2"]["rms_length"],d["3"]["rms_length"],places=6)
        self.assertNotAlmostEqual(d["4"]["rms_length"],d["5"]["rms_length"],places=6)

    def test_all_sixteen_gates_preserve_edgewise_reference(self):
        x=metric_reference()
        self.assertEqual(len(rgs_gate_vertex_permutations()),16)
        for p in rgs_gate_vertex_permutations():
            ep=np.asarray(edge_permutation(p),dtype=int)
            np.testing.assert_allclose(x,x[ep],atol=1e-12,rtol=0.0)

    def test_report_confirms_full_gate_survival(self):
        report=metric_reference_report()
        self.assertEqual(report["edge_count"],192)
        self.assertEqual(report["rgs_q6_gate_group_order"],16)
        self.assertTrue(report["all_16_gates_preserve_reference"])
        self.assertLessEqual(report["max_reference_invariance_residual"],1e-12)

    def test_reference_is_edgewise_not_direction_averaged(self):
        x=metric_reference()
        direction_zero=[x[i] for i,(_,_,bit) in enumerate(q6_edges()) if bit==0]
        self.assertGreater(len(np.unique(np.round(direction_zero,12))),1)

if __name__=="__main__":
    unittest.main()
