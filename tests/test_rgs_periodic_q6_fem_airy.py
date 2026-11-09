import unittest
import numpy as np
from scripts.rgs_periodic_q6_fem_airy import (
    compare, periodic_q1_solve, periodic_p1_solve, periodic_airy_spectral,
    q6_lift_energy, q6_lift_p1_audit, periodic_triangle_complex
)

class PeriodicQ6FEMAiryTests(unittest.TestCase):
    def test_q6_lift_preserves_periodic_q1_energy(self):
        for kind in ("shear_inclusion","shear_dipole"):
            q=periodic_q1_solve(4,kind)
            e,pb,lifted=q6_lift_energy(q["displacement"],q["eigenstrain_cells"])
            self.assertLess(abs(e-q["q1_energy"])/max(abs(e),abs(q["q1_energy"]),1e-30),1e-12)
            self.assertLess(pb,1e-12)
            self.assertEqual(lifted.shape,(64,2))

    def test_periodic_q1_converges_to_spectral_airy(self):
        r=compare(levels=(4,8,16))
        for kind in ("shear_inclusion","shear_dipole"):
            rows=[x for x in r["results"] if x["case"]==kind]
            self.assertLess(rows[-1]["q1_airy_relative_energy_difference"],rows[0]["q1_airy_relative_energy_difference"])
            self.assertLess(rows[-1]["q1_stress_relative_l2"],rows[0]["q1_stress_relative_l2"])
            self.assertLess(rows[-1]["q1_strain_relative_l2"],rows[0]["q1_strain_relative_l2"])

    def test_periodic_solver_residuals_and_mean_stress(self):
        q=periodic_q1_solve(8,"shear_inclusion")
        a=periodic_airy_spectral(q["eigenstrain_cells"])
        self.assertLess(q["q1_relative_free_residual"],1e-8)
        self.assertLess(a["airy_spectral_compatibility_residual"],1e-10)
        self.assertTrue(np.all(np.isfinite(a["stress_cells"])))
        self.assertTrue(np.all(np.isfinite(a["strain_cells"])))

    def test_periodic_p1_converges_to_spectral_airy(self):
        r=compare(levels=(4,8,16,32))
        for kind in ("shear_inclusion","shear_dipole"):
            rows=[x for x in r["results"] if x["case"]==kind]
            self.assertLess(rows[-1]["p1_airy_relative_energy_difference"],
                            rows[0]["p1_airy_relative_energy_difference"])
            self.assertLess(rows[-1]["p1_stress_relative_l2"],
                            rows[0]["p1_stress_relative_l2"])
            self.assertLess(rows[-1]["p1_strain_relative_l2"],
                            rows[0]["p1_strain_relative_l2"])
            self.assertLess(max(x["p1_residual"] for x in rows),1e-8)
            self.assertLess(max(x["p1_diagonal_energy_relative_difference"] for x in rows),1e-12)

    def test_q6_lift_preserves_periodic_p1_cochain_energy(self):
        for kind in ("shear_inclusion","shear_dipole"):
            for diagonal in ("sw_ne","se_nw"):
                p=periodic_p1_solve(4,kind,diagonal=diagonal)
                e,pb,lifted=q6_lift_p1_audit(
                    p["displacement"],p["eigenstrain_cells"],diagonal=diagonal)
                self.assertLess(abs(e-p["p1_energy"])/max(abs(e),abs(p["p1_energy"]),1e-30),1e-12)
                self.assertLess(pb,1e-12)
                self.assertEqual(lifted.shape,(64,2))

    def test_periodic_p1_incidence_is_an_exact_chain_complex(self):
        for diagonal in ("sw_ne","se_nw"):
            edges,faces,d0,d1=periodic_triangle_complex(4,diagonal)
            self.assertEqual(len(edges),48)
            self.assertEqual(len(faces),32)
            self.assertEqual((d1@d0).nnz,0)

if __name__=="__main__": unittest.main()
