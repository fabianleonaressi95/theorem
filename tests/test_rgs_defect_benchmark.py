"""Tests for scripts/rgs_defect_benchmark.py."""
import unittest
import numpy as np
from scripts.rgs_defect_benchmark import incidence_square, solve_case

class DefectBenchmarkTests(unittest.TestCase):
    def test_boundary_of_boundary_is_zero(self):
        d0,d1=incidence_square(8)
        self.assertTrue(np.array_equal(d1@d0,np.zeros((49,64),dtype=np.int64)))

    def test_affine_manufactured_solution(self):
        result=solve_case(9,"affine")
        self.assertLess(result["affine_relative_error"],1e-9)
        self.assertLess(result["relative_free_residual"],1e-8)

    def test_zero_source_has_zero_energy(self):
        result=solve_case(9,"none")
        self.assertLess(result["energy"],1e-20)

    def test_single_and_dipole_are_finite(self):
        for case in ("single","dipole"):
            result=solve_case(9,case)
            self.assertTrue(np.isfinite(result["energy"]))
            self.assertGreaterEqual(result["energy"],0.0)
            self.assertLess(result["relative_free_residual"],1e-8)

if __name__=="__main__":
    unittest.main()
