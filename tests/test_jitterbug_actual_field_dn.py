import unittest

import numpy as np

from audits.jitterbug_actual_field_dn import (
    circular_source_segments, biot_savart_polygon, finite_surface_flux,
    build_actual_mechanism_run,
)


class TestActualJitterbugField(unittest.TestCase):
    def test_biot_savart_on_axis_matches_circular_loop_formula(self):
        radius, current, z = 0.2, 1.3, 0.07
        pts, dl = circular_source_segments(radius, np.zeros(3),
                                            np.array([0., 0., 1.]), 2048)
        B = biot_savart_polygon(np.array([[0., 0., z]]), pts, dl, current)[0]
        exact = 4e-7*np.pi*current*radius**2 / (
            2*(radius**2+z**2)**1.5)
        self.assertAlmostEqual(B[2]/exact, 1.0, delta=2e-5)
        self.assertLess(abs(B[0])+abs(B[1]), 1e-12)

    def test_finite_surface_flux_is_nonzero_for_source_field(self):
        pts, dl = circular_source_segments(0.2, np.zeros(3),
                                            np.array([0., 0., 1.]), 256)
        flux = finite_surface_flux(np.array([0.04, 0., 0.02]), np.eye(3),
                                   np.array([0., 0., 1.]), 0.01, 100,
                                   pts, dl, 1.0, nr=4, ntheta=16)
        self.assertGreater(flux, 0.0)

    def test_actual_jitterbug_receiver_energy_balance(self):
        result = build_actual_mechanism_run(
            ds=0.16, segments=24, source_segments=96,
            disk_nr=3, disk_ntheta=12)
        self.assertGreater(result["frames"], 2)
        self.assertGreater(result["max_abs_external_emf_V"], 0.0)
        self.assertGreater(result["max_abs_current_A"], 0.0)
        self.assertGreater(result["min_inductance_eigenvalue_H"], 0.0)
        self.assertLess(result["energy_audit_receiver_side_J"][
            "relative_balance_residual"], 1e-10)


if __name__ == "__main__":
    unittest.main()
