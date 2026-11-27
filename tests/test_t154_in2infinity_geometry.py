import unittest
from scripts.audit_t154_in2infinity_geometry import all_audits, tribonacci_constant

class T154ExtendedJitterbugTests(unittest.TestCase):
    def test_combinatorics_and_euler(self):
        expected={"octahedron":(6,12,8),"icosahedron":(12,30,20),
                  "cuboctahedron":(12,24,14),"snub_cube":(24,60,38),
                  "rhombic_cuboctahedron":(24,48,26)}
        for item in all_audits():
            self.assertEqual((item["V"],item["E"],item["F"]),expected[item["name"]])
            self.assertEqual(item["V"]-item["E"]+item["F"],2)

    def test_tribonacci_parameter(self):
        t=tribonacci_constant()
        self.assertAlmostEqual(t**3-t**2-t-1,0.0,places=12)
        self.assertGreater(t,1.8); self.assertLess(t,1.9)

    def test_face_orbit_radii_not_collapsed(self):
        by_name={x["name"]:x for x in all_audits()}
        for name in ("cuboctahedron","snub_cube","rhombic_cuboctahedron"):
            self.assertEqual(len(by_name[name]["face_plane_radii"]),2)

if __name__=="__main__": unittest.main()
