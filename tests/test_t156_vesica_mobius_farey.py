import math
import unittest
from fractions import Fraction

from scripts.audit_t156_vesica_mobius_farey import (
    conjugated_farey,
    developability_residual,
    farey,
    h,
    h_inverse,
    mobius_transverse_after_laps,
    question_mark_rational,
    run_audit,
    sadowsky_density,
    tent,
    vesica_metrics,
)


class T156VesicaMobiusFareyTests(unittest.TestCase):
    def test_projective_threshold_is_exact(self):
        self.assertEqual(h(Fraction(2, 3)), Fraction(1, 2))
        self.assertEqual(h_inverse(Fraction(1, 2)), Fraction(2, 3))
        self.assertEqual(conjugated_farey(Fraction(2, 3)), Fraction(1))

    def test_conjugacy_on_reduced_rationals(self):
        for q in range(2, 25):
            for p in range(1, q):
                alpha = Fraction(p, q)
                self.assertEqual(
                    conjugated_farey(alpha),
                    h_inverse(farey(h(alpha))),
                )

    def test_question_mark_farey_tent_identity_on_rationals(self):
        for q in range(2, 25):
            for p in range(1, q):
                x = Fraction(p, q)
                self.assertEqual(
                    question_mark_rational(farey(x)),
                    tent(question_mark_rational(x)),
                )

    def test_vesica_half_separation_exact_benchmark(self):
        b_over_r, area_over_r2 = vesica_metrics(0.5)
        self.assertTrue(math.isclose(b_over_r, math.sqrt(3) / 2, abs_tol=1e-14))
        expected = 2 * math.pi / 3 - math.sqrt(3) / 2
        self.assertTrue(math.isclose(area_over_r2, expected, abs_tol=1e-14))

    def test_mobius_transverse_monodromy(self):
        q = 0.371
        self.assertEqual(mobius_transverse_after_laps(q, 1), -q)
        self.assertEqual(mobius_transverse_after_laps(q, 2), q)

    def test_developability_identity_is_separate_from_equilibrium(self):
        eta = [0.0, 0.2, -0.4]
        kappa = [0.5, 1.5, 2.0]
        tau = [e * k for e, k in zip(eta, kappa)]
        self.assertEqual(developability_residual(eta, kappa, tau), 0.0)

    def test_sadowsky_density_positive_for_nonzero_curvature(self):
        for kappa, tau in [(0.5, 0.0), (1.0, 0.25), (2.0, -0.5)]:
            self.assertGreater(sadowsky_density(kappa, tau), 0.0)

    def test_audit_summary(self):
        report = run_audit()
        self.assertEqual(report["record"], "T156")
        self.assertGreater(report["farey_conjugacy_rational_checks"], 0)
        self.assertGreater(report["question_mark_tent_rational_checks"], 0)


if __name__ == "__main__":
    unittest.main()
