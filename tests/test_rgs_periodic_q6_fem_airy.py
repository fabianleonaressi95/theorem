import unittest
import numpy as np
from scripts.rgs_periodic_q6_fem_airy import (
    compare, periodic_q1_solve, periodic_airy_spectral, q6_lift_energy
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
            self.assertLess(rows[-1]["relative_energy_difference"],rows[0]["relative_energy_difference"])
            self.assertLess(rows[-1]["stress_relative_l2"],rows[0]["stress_relative_l2"])
            self.assertLess(rows[-1]["strain_relative_l2"],rows[0]["strain_relative_l2"])

    def test_periodic_solver_residuals_and_mean_stress(self):
        q=periodic_q1_solve(8,"shear_inclusion")
        a=periodic_airy_spectral(q["eigenstrain_cells"])
        self.assertLess(q["q1_relative_free_residual"],1e-8)
        self.assertLess(a["airy_spectral_compatibility_residual"],1e-10)
        self.assertTrue(np.all(np.isfinite(a["stress_cells"])))
        self.assertTrue(np.all(np.isfinite(a["strain_cells"])))

if __name__=="__main__": unittest.main()
