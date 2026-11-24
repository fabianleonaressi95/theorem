import math
import unittest

from audits.tsmr03_discrete_refinement import (
    cycle_betti_numbers, cycle_boundary_matrix, cycle_laplacian_spectrum,
    rank_over_rational, refine_cycle_values, refinement_report,
)


class TestTSMR03DiscreteRefinement(unittest.TestCase):
    def test_cycle_chain_complex_boundary_has_rank_n_minus_one(self):
        for n in (3, 5, 8):
            boundary = cycle_boundary_matrix(n)
            self.assertEqual(rank_over_rational(boundary), n-1)
            # The sum of oriented edge boundaries vanishes: B1 * (1,...,1)=0.
            self.assertTrue(all(sum(row) == 0 for row in boundary))

    def test_cycle_betti_numbers_are_invariant_under_subdivision(self):
        for n in (3, 5, 8, 12):
            self.assertEqual(cycle_betti_numbers(n), (1, 1))
            self.assertEqual(cycle_betti_numbers(2*n), (1, 1))

    def test_cycle_laplacian_has_one_zero_mode_and_positive_gap(self):
        spectrum = cycle_laplacian_spectrum(16)
        self.assertEqual(len(spectrum), 16)
        self.assertAlmostEqual(spectrum[0], 0.0, places=12)
        self.assertGreater(spectrum[1], 0.0)
        self.assertAlmostEqual(spectrum[1], 2-2*math.cos(2*math.pi/16))

    def test_piecewise_linear_transport_preserves_coarse_vertices(self):
        coarse = [0.0, 1.0, 0.0, -1.0]
        fine = refine_cycle_values(coarse, factor=2)
        self.assertEqual(len(fine), 8)
        self.assertEqual([fine[2*i] for i in range(4)], coarse)
        self.assertEqual([fine[2*i+1] for i in range(4)], [0.5, 0.5, -0.5, -0.5])

    def test_refinement_report_preserves_topology_and_resolves_spectrum(self):
        report = refinement_report(12, factor=2)
        self.assertEqual(report["coarse_betti"], (1, 1))
        self.assertEqual(report["fine_betti"], (1, 1))
        self.assertEqual(report["fine_vertices"], 24)
        self.assertGreater(report["fine_spectral_gap"], 0.0)
        # Discrete spectral gaps shrink under refinement; h^-2 scaling tends
        # toward the same continuum value (4 pi^2), with a bounded discrepancy.
        ratio = report["fine_scaled_gap"] / report["coarse_scaled_gap"]
        self.assertGreater(ratio, 0.95)
        self.assertLess(ratio, 1.05)



    def test_torus_cellular_chain_complex_and_betti_numbers(self):
        from audits.tsmr03_discrete_refinement import (
            matrix_product_integer, torus_betti_numbers,
            torus_cellular_boundaries,
        )
        for n in (3, 4):
            b1, b2 = torus_cellular_boundaries(n)
            product = matrix_product_integer(b1, b2)
            self.assertTrue(all(value == 0 for row in product for value in row))
            self.assertEqual(torus_betti_numbers(n), (1, 2, 1))

    def test_torus_spectrum_and_bilinear_transport_under_refinement(self):
        from audits.tsmr03_discrete_refinement import (
            prolong_torus_field, torus_graph_spectrum,
        )
        coarse = torus_graph_spectrum(8)
        fine = torus_graph_spectrum(16)
        coarse_gap = next(value for value in coarse if value > 1e-12)
        fine_gap = next(value for value in fine if value > 1e-12)
        scaled_ratio = (fine_gap * 16**2) / (coarse_gap * 8**2)
        self.assertGreater(scaled_ratio, 0.99)
        self.assertLess(scaled_ratio, 1.02)
        field = [[float(i+j) for j in range(4)] for i in range(4)]
        refined = prolong_torus_field(field, factor=2)
        self.assertEqual(len(refined), 8)
        self.assertEqual([refined[2*i][2*j] for i in range(4) for j in range(4)],
                         [field[i][j] for i in range(4) for j in range(4)])


if __name__ == "__main__":
    unittest.main()
