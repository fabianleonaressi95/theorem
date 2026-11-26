"""Regression tests for T155 geometric connection and covariant Hodge operator."""
import importlib.util
from pathlib import Path
import unittest
SCRIPT=Path(__file__).resolve().parents[1]/"scripts"/"audit_t155_dodecahedral_levi_civita_hodge.py"
spec=importlib.util.spec_from_file_location("audit_t155",SCRIPT)
audit=importlib.util.module_from_spec(spec); spec.loader.exec_module(audit)
class T155ConnectionHodge(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.report=audit.build_report()
    def test_combinatorics_and_gauss_bonnet(self):
        for c in self.report.values():
            if not isinstance(c,dict) or "counts" not in c: continue
            self.assertEqual(c["counts"],{"pentagonal_faces":12,"dual_edges":30,"gauss_map_triangles":20})
            self.assertLess(c["gauss_bonnet_4pi_residual"],2e-9)
    def test_transport_and_antipodes(self):
        for c in (self.report["supergolden"],self.report["regular_control"]):
            self.assertLess(c["transport_orthogonality_residual"],2e-9)
            self.assertLess(c["transport_determinant_residual"],2e-9)
            self.assertLess(c["antipodal_frame_covariance_residual"],2e-9)
    def test_covariant_hodge(self):
        for c in (self.report["supergolden"],self.report["regular_control"]):
            self.assertLess(c["covariant_hodge_hermiticity_residual"],2e-9)
            self.assertGreater(c["covariant_hodge_minimum_eigenvalue"],0)
            self.assertGreater(c["constant_section_energy"],1e-4)
            self.assertEqual(len(c["covariant_hodge_spectrum"]),12)
    def test_not_q6_triplet(self):
        for c in (self.report["supergolden"],self.report["regular_control"]):
            s=c["covariant_hodge_spectrum"]
            self.assertFalse(any(min(abs(v-q) for v in s)<1e-7 for q in (0.,4.,6.)))
if __name__=="__main__": unittest.main()
