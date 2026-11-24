import unittest

import numpy as np

from audits.jitterbug_eight_coil_validation import (
    coaxial_mutual_exact, convergence_audit, driven_eight_coil_probe,
)


class TestEightCoilValidation(unittest.TestCase):
    def test_exact_coaxial_reference_is_positive(self):
        value = coaxial_mutual_exact(0.03, 0.025, 0.04, 100, 80)
        self.assertGreater(value, 0.0)
        self.assertAlmostEqual(value, 5.734392e-5, delta=2e-7)

    def test_polygon_quadrature_converges_to_exact_reference(self):
        result = convergence_audit(segment_counts=(48, 96, 192, 384))
        errors = [row["relative_error"]
                  for row in result["segment_convergence"]]
        self.assertTrue(all(b < a for a, b in zip(errors, errors[1:])))
        self.assertLess(errors[-1], 3e-5)

    def test_static_field_and_prescribed_rotation_generate_emf(self):
        result = driven_eight_coil_probe(frames=31, segments=32)
        self.assertGreater(result["max_abs_emf_V"], 1e-5)
        self.assertGreater(result["max_abs_current_A"], 0.0)
        self.assertGreater(result["min_inductance_eigenvalue_H"], 0.0)
        self.assertEqual(result["max_reciprocity_residual_H"], 0.0)
        self.assertTrue(np.isfinite(result["max_abs_current_A"]))


if __name__ == "__main__":
    unittest.main()
