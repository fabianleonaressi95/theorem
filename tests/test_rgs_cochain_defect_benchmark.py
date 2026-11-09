"""Tests for the edge-cochain elasticity comparator."""
import unittest
import numpy as np
from scripts.rgs_cochain_defect_benchmark import square_complex, solve_cochain

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

    def test_single_and_dipole(self):
        for kind in ("single","dipole"):
            for diagonal in ("sw_ne","se_nw"):
                r=solve_cochain(9,kind,diagonal=diagonal)
                self.assertTrue(np.isfinite(r["energy"]))
                self.assertGreaterEqual(r["energy"],0)
                self.assertLess(r["relative_free_residual"],1e-8)

if __name__=="__main__": unittest.main()
