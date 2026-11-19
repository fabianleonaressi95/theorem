import unittest
import numpy as np

from scripts.audit_t139_supergolden_icosahedron import PSI_SG, PHI, audit


class TestT139SupergoldenIcosahedron(unittest.TestCase):
    def test_supergolden_hull_counts_and_euler(self):
        result = audit(PSI_SG, verbose=False)
        self.assertEqual((result["vertices"], result["edges"], result["faces"]), (12, 30, 20))
        self.assertEqual(result["euler"], 2)

    def test_supergolden_edge_and_face_classes(self):
        result = audit(PSI_SG, verbose=False)
        self.assertEqual(sorted(result["edge_classes"].values()), [6, 24])
        self.assertEqual(sorted(result["face_classes"].values()), [8, 12])
        expected_short = np.sqrt(2 * (PSI_SG**2 - PSI_SG + 1))
        lengths = sorted(result["edge_classes"].keys())
        self.assertAlmostEqual(lengths[0], expected_short, places=7)
        self.assertAlmostEqual(lengths[1], 2.0, places=7)

    def test_supergolden_laplacian_spectrum(self):
        spectrum = audit(PSI_SG, verbose=False)["spectrum"]
        expected = np.array([
            0.0,
            0.793981242, 0.793981242, 0.793981242,
            1.68882895, 1.68882895, 1.68882895,
            1.78324343, 1.78324343,
            2.08367666, 2.08367666, 2.08367666,
        ])
        np.testing.assert_allclose(spectrum, expected, atol=2e-7, rtol=0.0)

    def test_antipodal_commutation(self):
        result = audit(PSI_SG, verbose=False)
        self.assertLess(result["antipodal_commutator_norm"], 1e-10)

    def test_regular_icosahedron_control(self):
        result = audit(PHI, verbose=False)
        self.assertEqual((result["vertices"], result["edges"], result["faces"]), (12, 30, 20))
        self.assertEqual(result["euler"], 2)
        self.assertEqual(len(result["edge_classes"]), 1)
        self.assertEqual(next(iter(result["edge_classes"].keys())), 2.0)
        self.assertEqual(next(iter(result["edge_classes"].values())), 30)


if __name__ == "__main__":
    unittest.main()
