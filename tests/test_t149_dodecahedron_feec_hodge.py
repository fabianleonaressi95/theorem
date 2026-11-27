"""T149 regression tests: supergolden FEEC run and regular control."""
import importlib.util
from pathlib import Path
import unittest

SCRIPT=Path(__file__).resolve().parents[1]/"scripts"/"audit_t149_dodecahedron_feec_hodge.py"
spec=importlib.util.spec_from_file_location("audit_t149",SCRIPT)
audit=importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

class T149FEEC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=audit.build_report()

    def test_incidence_and_antipodal_mass(self):
        for case in self.report.values():
            self.assertEqual(case["counts"],[32,90,60])
            self.assertEqual(case["euler_characteristic"],2)
            self.assertEqual(case["incidence_ranks"],[31,59])
            self.assertLess(max(case["incidence_residuals"]),2e-9)
            self.assertLess(max(case["antipodal_mass_residuals"]),2e-9)
            self.assertLess(max(case["antipodal_involution_residuals"]),2e-9)

    def test_mass_positive_and_spectra(self):
        for case in self.report.values():
            for bounds in case["mass_eigenvalue_bounds"]:
                self.assertGreater(bounds[0],0)
            self.assertEqual(len(case["spectra"]["0"]),32)
            self.assertEqual(len(case["spectra"]["1"]),90)
            self.assertEqual(len(case["spectra"]["2"]),60)

    def test_supergolden_q6_obstruction(self):
        q=self.report["supergolden"]["q6_comparison"]
        self.assertLess(q["original_q6_sector_residual"],2e-9)
        self.assertGreater(q["pull_intertwiner_residual"],1e-2)
        self.assertGreater(q["chain_intertwiner_residual"],1e-2)
        self.assertNotIn("q6_comparison",self.report["regular_control"])

if __name__=="__main__":
    unittest.main()
