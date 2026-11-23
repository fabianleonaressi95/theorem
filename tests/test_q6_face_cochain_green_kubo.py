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


if __name__ == "__main__":
    unittest.main()
