"""Exact tests for the Q6 -> periodic 2D kinematic quotient."""
import unittest
import numpy as np
from scripts.q6_prism_kinematic_map import (
    build_q6_complex, lift_displacement, cell_gradients, elastic_energy, audit
)


class Q6PrismKinematicMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = build_q6_complex()

    def test_q6_counts_and_gray_coordinates(self):
        c = self.c
        self.assertEqual(c["coords"].shape, (64, 3))
        self.assertEqual(len({tuple(x) for x in c["coords"].tolist()}), 64)
        self.assertEqual(len(c["edges"]), 192)
        self.assertEqual(c["d1_full"].shape, (240, 192))
        self.assertEqual(c["d1_product"].shape, (192, 192))

    def test_exact_boundary_of_boundary(self):
        c = self.c
        self.assertTrue(np.array_equal(c["d1_full"] @ c["d0"],
                                       np.zeros((240, 64), dtype=np.int64)))
        self.assertTrue(np.array_equal(c["d1_product"] @ c["d0"],
                                       np.zeros((192, 64), dtype=np.int64)))
        self.assertTrue(np.array_equal(c["d1_base"] @ c["d0_base"],
                                       np.zeros((16, 16), dtype=np.int64)))

    def test_vertex_and_face_chain_maps(self):
        c = self.c
        self.assertTrue(np.array_equal(c["d0"] @ c["p0"],
                                       c["p1"] @ c["d0_base"]))
        self.assertTrue(np.array_equal(c["d1_product"] @ c["p1"],
                                       c["p2"] @ c["d1_base"]))

    def test_lifted_displacement_is_exact_coboundary_pullback(self):
        rng = np.random.default_rng(20261109)
        u = rng.normal(size=(16, 2))
        lifted = lift_displacement(u, self.c)
        lhs = self.c["d0"] @ lifted
        rhs = self.c["p1"] @ (self.c["d0_base"] @ u)
        self.assertTrue(np.allclose(lhs, rhs, rtol=0, atol=0))
        fibre_edges = [k for k,(_,_,bit) in enumerate(self.c["edges"]) if bit//2 == 2]
        self.assertTrue(np.array_equal(lhs[fibre_edges],
                                       np.zeros((len(fibre_edges),2))))

    def test_gradient_and_energy_are_finite_and_nonnegative(self):
        u = np.array([[np.sin(2*np.pi*x/4), np.cos(2*np.pi*y/4)]
                      for y in range(4) for x in range(4)], dtype=float)
        g = cell_gradients(u, self.c)
        self.assertEqual(g.shape, (16,2,2))
        self.assertTrue(np.all(np.isfinite(g)))
        self.assertGreaterEqual(elastic_energy(u), 0.0)
        self.assertEqual(elastic_energy(np.zeros((16,2))), 0.0)

    def test_machine_readable_audit(self):
        r = audit()
        self.assertEqual(r["exact_checks"]["vertex_chain_map_max_abs"], 0)
        self.assertEqual(r["exact_checks"]["face_chain_map_max_abs"], 0)
        self.assertEqual(r["exact_checks"]["displacement_pullback_max_abs"], 0.0)


if __name__ == "__main__":
    unittest.main()
