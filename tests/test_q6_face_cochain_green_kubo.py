import unittest

from audits.q6_face_cochain_green_kubo import build_report


class Q6FaceCochainAuditTests(unittest.TestCase):
    def test_cell_counts(self):
        report = build_report()
        self.assertEqual(report["cell_counts_C1_C2_C3"], {1: 192, 2: 240, 3: 160})

    def test_boundary_identities(self):
        report = build_report()
        self.assertEqual(
            report["boundary_identities"],
            {"B1_B2_zero": True, "B2_B3_zero": True},
        )

    def test_exact_ranks_and_cohomology(self):
        report = build_report()
        self.assertEqual(report["boundary_ranks_B1_B2_B3"], {1: 63, 2: 129, 3: 111})
        self.assertEqual(report["closed_2_cochain_dimension"], 129)
        self.assertEqual(report["harmonic_2_cochain_dimension"], 0)

    def test_closed_face_hodge_spectrum_and_green_kubo_trace(self):
        report = build_report()
        self.assertEqual(
            report["closed_2_hodge_spectrum"],
            {4: 15, 6: 40, 8: 45, 10: 24, 12: 5},
        )
        self.assertEqual(report["green_kubo_trace_sum_m_over_lambda"], "2263/120")
        self.assertEqual(report["isotropic_green_kubo_coefficient"], "2263/15480")


if __name__ == "__main__":
    unittest.main()
