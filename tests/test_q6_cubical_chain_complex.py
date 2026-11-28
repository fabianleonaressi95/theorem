import unittest
from scripts.audit_q6_cubical_chain_complex import build_report

class Q6CubicalChainComplexTests(unittest.TestCase):
    def test_exact_cell_counts(self):
        r=build_report()
        self.assertEqual(r["cell_counts_by_dimension"],[64,192,240,160,60,12,1])

    def test_boundary_squared_zero(self):
        r=build_report()
        self.assertEqual(r["boundary_squared_max_abs"],{"d1_d2":0,"d2_d3":0})

    def test_euler_characteristic(self):
        self.assertEqual(build_report()["euler_characteristic"],1)

if __name__=="__main__":
    unittest.main()
