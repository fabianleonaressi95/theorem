"""Tests for the Airy-stress incompatibility reference."""
import unittest
import numpy as np
from scripts.rgs_airy_reference import solve_airy, incompatibility, plastic_strain_nodes, compare_case, dipole_edge_equivalence

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

    def test_disclination_dipole_has_edge_burgers_moment(self):
        n=129; h=1/(n-1); x=np.linspace(0,1,n); X,Y=np.meshgrid(x,x)
        e=plastic_strain_nodes(n,"wedge_dipole",burgers=.02,dipole_separation=.05)
        inc=incompatibility(e,h)
        self.assertAlmostEqual(float(np.sum(Y*inc)*h*h),.02,delta=3e-4)

    def test_disclination_dipole_converges_to_edge_source(self):
        r=dipole_edge_equivalence(n=129,separations=(.125,.0625,.03125,.015625))
        a=r["results"]
        self.assertLess(a[-1]["incompatibility_relative_l2"],a[0]["incompatibility_relative_l2"])
        self.assertLess(a[-1]["airy_stress_relative_l2"],a[0]["airy_stress_relative_l2"])

    def test_dipole_sweep_avoids_stencil_locked_separations(self):
        r=dipole_edge_equivalence(n=129)
        a=r["results"]
        ratios=[row["separation_over_h"] for row in a]
        self.assertTrue(all(not np.isclose(q,2.0,rtol=0,atol=1e-12) for q in ratios),ratios)
        self.assertLess(a[-1]["incompatibility_relative_l2"],a[0]["incompatibility_relative_l2"])
        self.assertLess(a[-1]["airy_stress_relative_l2"],a[0]["airy_stress_relative_l2"])

    def test_airy_source_cut_matches_cell_centred_convention(self):
        n=33
        e=plastic_strain_nodes(n,"volterra_edge",burgers=.02)
        # The cut is halfway between x=1/2 and the first active cell centre.
        self.assertEqual(float(np.max(np.abs(e[:,n//2,2]))),0.0)
        self.assertGreater(float(np.max(np.abs(e[:,n//2+1,2]))),0.0)

    def test_energy_comparison_is_finite_and_positive(self):
        r=compare_case(17,"volterra_edge")
        for key in ("q1_energy","cochain_energy","airy_energy",
                    "q1_airy_relative_energy_difference",
                    "cochain_airy_relative_energy_difference"):
            self.assertTrue(np.isfinite(r[key]),(key,r[key]))
        self.assertGreater(r["q1_energy"],0.0)
        self.assertGreater(r["cochain_energy"],0.0)
        self.assertGreater(r["airy_energy"],0.0)

    def test_clamped_airy_solutions(self):
        for kind in ("volterra_edge","wedge_disclination"):
            r=solve_airy(17,kind)
            self.assertTrue(np.isfinite(r["weak_residual"]),r)
            self.assertLess(r["weak_residual"],1e-7,r)
            self.assertLess(r["topological_moment_error"],.01,r)

if __name__=="__main__": unittest.main()
