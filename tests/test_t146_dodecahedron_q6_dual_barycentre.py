import unittest
import numpy as np

from scripts.audit_t146_dodecahedron_q6_dual_barycentre import audit


class TestT146DodecahedronQ6DualBarycentre(unittest.TestCase):
    def test_dual_incidence_and_antipodes(self):
        r = audit()
        self.assertTrue(r["all_structural_checks_pass"])
        self.assertEqual(r["dodecahedron_vertices"], 20)
        self.assertEqual(r["dodecahedron_edges"], 30)
        self.assertEqual(r["dodecahedron_vertex_degree_set"], [3])
        self.assertTrue(r["antipodal_dual_graph_automorphism"])

    def test_edge_chain_map_commutes_with_boundary(self):
        r = audit()
        self.assertLess(r["dodecahedron_q6_edge_chain_boundary_residual"], 1e-9)
        self.assertEqual(r["dodecahedron_q6_edge_chain_path_lengths"], {"2": 18, "4": 12})
        self.assertEqual(r["chain_induced_energy_rank"], 19)
        self.assertTrue(r["checks"]["dodecahedron_edge_chain_boundary_commutes"])
        self.assertLess(r["dodecahedron_q6_edge_chain_antipodal_residual"], 1e-9)
        self.assertTrue(r["checks"]["dodecahedron_edge_chain_antipodal_equivariance"])

    def test_canonical_operator_does_not_claim_target_spectrum(self):
        r = audit()
        eig = np.asarray(r["induced_q6_energy_eigenvalues"])
        self.assertEqual(np.count_nonzero(eig > 1e-8), 12)
        self.assertGreater(r["selected_q6_intertwining_residual"], 1.0)
        self.assertGreater(r["nearest_induced_eigenvalue_to_4"], 0.1)
        self.assertGreater(r["nearest_induced_eigenvalue_to_6"], 0.1)


if __name__ == "__main__":
    unittest.main()
