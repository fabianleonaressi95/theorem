import unittest
from scripts.audit_t160_covariant_gradient_energy import assemble, build_report

class T160CovariantGradientEnergy(unittest.TestCase):
    def test_refinement_forms_are_hermitian_and_positive(self):
        report = build_report()
        self.assertEqual(
            [r["counts"] for r in report["refinements"]],
            [[32,90,60],[122,360,240],[272,810,540],[482,1440,960]],
        )
        for r in report["refinements"]:
            self.assertGreater(r["minimum_mass_eigenvalue"], 0)
            self.assertGreater(r["minimum_stiffness_eigenvalue"], -1e-8)
            self.assertLess(r["mass_hermiticity_residual"], 2e-8)
            self.assertLess(r["stiffness_hermiticity_residual"], 2e-8)
            self.assertLess(r["projected_derivative_radial_residual"], 1e-7)

    def test_derivative_step_sensitivity_on_coarse_mesh(self):
        a, _, _ = assemble(1, order=4, derivative_step=2e-6)
        b, _, _ = assemble(1, order=4, derivative_step=1e-6)
        x, y = a["lowest_12_eigenvalues"], b["lowest_12_eigenvalues"]
        rel = max(abs(p-q) for p,q in zip(x,y)) / max(1.0, max(abs(q) for q in y))
        self.assertLess(rel, 2e-5)

if __name__ == "__main__":
    unittest.main()
