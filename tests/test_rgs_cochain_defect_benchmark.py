"""Tests for the edge-cochain elasticity comparator."""
import unittest
import numpy as np
from scripts.rgs_cochain_defect_benchmark import square_complex, solve_cochain, measure_volterra_burgers, measure_wedge_frank

class CochainDefectTests(unittest.TestCase):
    def test_boundary_of_boundary(self):
        xy,edges,faces,d0,d1=square_complex(8)
        self.assertEqual((d1@d0).nnz,0)

    def test_both_diagonal_chain_complexes(self):
        for diagonal in ("sw_ne","se_nw"):
            xy,edges,faces,d0,d1=square_complex(7,diagonal)
            self.assertEqual((d1@d0).nnz,0)

    def test_diagonal_affine_patch(self):
        for diagonal in ("sw_ne","se_nw"):
            r=solve_cochain(9,"affine",diagonal=diagonal)
            self.assertLess(r["affine_relative_error"],1e-9)
            self.assertLess(r["relative_free_residual"],1e-8)

    def test_affine_patch(self):
        r=solve_cochain(9,"affine")
        self.assertLess(r["affine_relative_error"],1e-9)
        self.assertLess(r["relative_free_residual"],1e-8)

    def test_zero_source(self):
        self.assertLess(solve_cochain(9,"none")["energy"],1e-20)

    def test_regularized_volterra_burgers_integral(self):
        measured=measure_volterra_burgers(n=129,burgers=.02,core_width=.025)
        self.assertAlmostEqual(measured,.02,delta=2e-4)

    def test_volterra_solution_on_both_diagonals(self):
        for diagonal in ("sw_ne","se_nw"):
            result=solve_cochain(17,"volterra_edge",diagonal=diagonal)
            self.assertTrue(np.isfinite(result["energy"]))
            self.assertGreaterEqual(result["energy"],0.0)
            self.assertLess(result["relative_free_residual"],1e-8)

    def test_regularized_wedge_frank_angle(self):
        measured=measure_wedge_frank(n=129,frank=.01,core_width=.025)
        self.assertAlmostEqual(measured,.01,delta=2e-4)

    def test_wedge_disclination_solution_on_both_diagonals(self):
        for diagonal in ("sw_ne","se_nw"):
            result=solve_cochain(17,"wedge_disclination",diagonal=diagonal)
            self.assertTrue(np.isfinite(result["energy"]))
            self.assertGreaterEqual(result["energy"],0.0)
            self.assertLess(result["relative_free_residual"],1e-8)

    def test_defect_energy_is_diagonal_invariant_on_square_mesh(self):
        for kind in ("single","volterra_edge","wedge_disclination"):
            a=solve_cochain(17,kind,diagonal="sw_ne")["energy"]
            b=solve_cochain(17,kind,diagonal="se_nw")["energy"]
            self.assertAlmostEqual(a,b,delta=1e-14*max(1.0,abs(a),abs(b)))

    def test_single_and_dipole(self):
        for kind in ("single","dipole"):
            for diagonal in ("sw_ne","se_nw"):
                r=solve_cochain(9,kind,diagonal=diagonal)
                self.assertTrue(np.isfinite(r["energy"]))
                self.assertGreaterEqual(r["energy"],0)
                self.assertLess(r["relative_free_residual"],1e-8)

if __name__=="__main__": unittest.main()
