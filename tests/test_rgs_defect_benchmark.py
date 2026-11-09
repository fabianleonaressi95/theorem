"""Tests for scripts/rgs_defect_benchmark.py."""
import unittest
import numpy as np
from scripts.rgs_defect_benchmark import incidence_square, solve_case, measure_volterra_burgers, measure_wedge_frank

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

    def test_regularized_volterra_burgers_integral(self):
        measured=measure_volterra_burgers(n=129,burgers=0.02,core_width=0.025)
        self.assertAlmostEqual(measured,0.02,delta=2e-4)

    def test_volterra_solution_is_finite(self):
        result=solve_case(33,"volterra_edge")
        self.assertTrue(np.isfinite(result["energy"]))
        self.assertGreaterEqual(result["energy"],0.0)
        self.assertLess(result["relative_free_residual"],1e-8)

    def test_regularized_wedge_frank_angle(self):
        measured=measure_wedge_frank(n=129,frank=0.01,core_width=0.025)
        self.assertAlmostEqual(measured,0.01,delta=2e-4)

    def test_wedge_disclination_solution_is_finite(self):
        result=solve_case(33,"wedge_disclination")
        self.assertTrue(np.isfinite(result["energy"]))
        self.assertGreaterEqual(result["energy"],0.0)
        self.assertLess(result["relative_free_residual"],1e-8)

    def test_single_and_dipole_are_finite(self):
        for case in ("single","dipole"):
            result=solve_case(9,case)
            self.assertTrue(np.isfinite(result["energy"]))
            self.assertGreaterEqual(result["energy"],0.0)
            self.assertLess(result["relative_free_residual"],1e-8)

if __name__=="__main__":
    unittest.main()
