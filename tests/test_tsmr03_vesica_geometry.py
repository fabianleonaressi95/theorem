import math
import unittest

from audits.tsmr03_vesica_geometry import (
    affine_transform, box_count, circular_vesica_boundary,
    effective_box_dimension, ellipse_deform, vesica_family,
)


class TestTSMR03VesicaGeometry(unittest.TestCase):
    def test_circular_vesica_has_two_arcs_and_expected_symmetry(self):
        points = circular_vesica_boundary(radius=1.0, center_distance=1.0,
                                           samples_per_arc=501)
        self.assertEqual(len(points), 1002)
        self.assertAlmostEqual(max(y for _, y in points), math.sqrt(3)/2, places=10)
        self.assertAlmostEqual(min(y for _, y in points), -math.sqrt(3)/2, places=10)
        self.assertAlmostEqual(min(x for x, _ in points), -0.5, places=10)
        self.assertAlmostEqual(max(x for x, _ in points), 0.5, places=10)

    def test_elliptic_vesica_is_an_invertible_anisotropic_deformation(self):
        circle = circular_vesica_boundary(samples_per_arc=300)
        ellipse = ellipse_deform(circle, axis_x=1.7, axis_y=0.6, angle=0.31)
        self.assertEqual(len(circle), len(ellipse))
        self.assertGreater(max(x for x, _ in ellipse)-min(x for x, _ in ellipse), 1.0)
        self.assertGreater(max(y for _, y in ellipse)-min(y for _, y in ellipse), 0.5)
        with self.assertRaises(ValueError):
            ellipse_deform(circle, 1.0, 0.0)

    def test_affine_map_preserves_sample_count_and_rejects_singular_map(self):
        points = circular_vesica_boundary(samples_per_arc=50)
        transformed = affine_transform(points, ((2.0, 0.0), (0.0, 0.5)))
        self.assertEqual(len(points), len(transformed))
        with self.assertRaises(ValueError):
            affine_transform(points, ((1.0, 0.0), (0.0, 0.0)))

    def test_bivesica_and_trivesica_are_explicit_unions(self):
        family = vesica_family(samples_per_arc=100)
        self.assertEqual(len(family["bivesica"]), 2*len(family["vesica"]))
        self.assertEqual(len(family["trivesica"]), 3*len(family["vesica"]))
        self.assertIn("elliptic_vesica", family)

    def test_box_count_and_effective_dimension_are_finite_scale_diagnostics(self):
        circle = circular_vesica_boundary(samples_per_arc=1000)
        scales = [0.20, 0.14, 0.10, 0.07]
        counts = [box_count(circle, eps) for eps in scales]
        self.assertTrue(all(n > 0 for n in counts))
        estimate = effective_box_dimension(circle, scales)
        # A smooth one-dimensional curve has asymptotic box dimension 1;
        # finite sampling and finite scales justify a broad diagnostic band.
        self.assertGreater(estimate, 0.65)
        self.assertLess(estimate, 1.45)
        with self.assertRaises(ValueError):
            box_count(circle, 0.0)


if __name__ == "__main__":
    unittest.main()
