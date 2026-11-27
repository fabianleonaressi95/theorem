import unittest
from scripts.audit_q6_connection_difference import build_connection_difference

class Q6ConnectionDifferenceTests(unittest.TestCase):
    def test_exact_link_and_face_factorization(self):
        r=build_connection_difference()
        self.assertLess(r["max_link_reconstruction_residual"],1e-10)
        self.assertLess(r["max_face_factorization_residual"],1e-12)
        self.assertEqual(r["carrier"]["faces"],240)

if __name__=="__main__":
    unittest.main()
