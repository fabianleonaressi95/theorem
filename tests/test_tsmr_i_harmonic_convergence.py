import unittest
from audits.tsmr_i_harmonic_convergence import fourier_basis, reduce_matrix, power_norms, frobenius

class IncreasingHarmonicTests(unittest.TestCase):
    def test_basis_dimension_and_constant(self):
        v=fourier_basis(0.125,4)
        self.assertEqual(len(v),9)
        self.assertEqual(v[2],1.0)
    def test_constant_excluded_from_complement(self):
        m=[[float(i==j) for j in range(7)] for i in range(7)]
        r=reduce_matrix(m,3)
        self.assertEqual(r["complement_dimension"],4)
        self.assertEqual(r["constant_mode"],"removed_exactly")
        self.assertEqual(r["D"],[[float(i==j) for j in range(4)] for i in range(4)])
    def test_zero_memory_for_block_diagonal_matrix(self):
        m=[[0.0]*7 for _ in range(7)]
        for i in range(7): m[i][i]=0.5
        self.assertAlmostEqual(reduce_matrix(m,3)["K0_frobenius"],0.0)
    def test_B_D_power_C_kernel(self):
        b=[[1.0,0.0]]; d=[[0.5,0.0],[0.0,0.25]]; c=[[1.0],[2.0]]
        k=power_norms(b,d,c,3)
        self.assertAlmostEqual(k["0"],1.0); self.assertAlmostEqual(k["1"],0.5); self.assertAlmostEqual(k["2"],0.25)
    def test_frobenius(self): self.assertAlmostEqual(frobenius([[3.0,4.0]]),5.0)

if __name__=="__main__": unittest.main()
