"""Tests for the Airy-stress incompatibility reference."""
import unittest
import numpy as np
from scripts.rgs_airy_reference import solve_airy, incompatibility, plastic_strain_nodes, compare_case

class AiryReferenceTests(unittest.TestCase):
    def test_wedge_incompatibility_charge(self):
        n=65; h=1/(n-1)
        e=plastic_strain_nodes(n,"wedge_disclination",frank=.01)
        inc=incompatibility(e,h)
        self.assertAlmostEqual(float(np.sum(inc)*h*h),.01,delta=.003)

    def test_edge_burgers_first_moment(self):
        n=65; h=1/(n-1); x=np.linspace(0,1,n); X,Y=np.meshgrid(x,x)
        e=plastic_strain_nodes(n,"volterra_edge",burgers=.02)
        inc=incompatibility(e,h)
        self.assertAlmostEqual(float(np.sum(Y*inc)*h*h),.02,delta=.004)

    def test_stress_and_strain_errors_decrease_with_refinement(self):
        for kind in ("volterra_edge","wedge_disclination"):
            coarse=compare_case(17,kind)
            fine=compare_case(33,kind)
            for key in ("q1_airy_stress_rel_l2","q1_airy_strain_rel_l2",
                        "cochain_airy_stress_rel_l2","cochain_airy_strain_rel_l2"):
                self.assertLess(fine[key],coarse[key],(kind,key,coarse[key],fine[key]))

    def test_clamped_airy_solutions(self):
        for kind in ("volterra_edge","wedge_disclination"):
            r=solve_airy(17,kind)
            self.assertTrue(np.isfinite(r["weak_residual"]),r)
            self.assertLess(r["weak_residual"],1e-7,r)
            self.assertLess(r["topological_moment_error"],.01,r)

if __name__=="__main__": unittest.main()
