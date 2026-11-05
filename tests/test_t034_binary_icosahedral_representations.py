"""Exact tests for T034 (explicit 2I representations, characters, projectors).

All identities are checked in exact arithmetic over Q(sqrt5)[i]; no floating
point tolerance appears anywhere.  Run from the repository root:

    python -m unittest tests.test_t034_binary_icosahedral_representations -v
"""
import json
import tempfile
import unittest
from pathlib import Path

from src import t034_binary_icosahedral_representations as T
from src.t032_2i_molien import IRREP_DIMENSIONS, molien_coefficients


class TestT034(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.G = T.build_group()
        cls.reps = T.build_representations(cls.G)
        cls.table, cls.classes = T.characters_from_matrices(cls.G, cls.reps)

    # ---- Task 1 -------------------------------------------------------
    def test_group_axioms_exact(self):
        r = T.verify_group(self.G)
        self.assertEqual(r["cardinality"], 120)
        self.assertEqual(r["centre"], sorted([self.G.identity, self.G.minus_one]))
        self.assertEqual(r["class_sizes"], list(T.CLASS_SIZES))
        self.assertEqual(r["class_orders"], list(T.CLASS_ORDERS))

    def test_minus_one_is_central_and_square_of_order_two_elements(self):
        G = self.G
        m1 = G.minus_one
        self.assertEqual(G.mul[m1][m1], G.identity)
        self.assertEqual(T.element_order(G, m1), 2)

    # ---- Task 2 -------------------------------------------------------
    def test_all_nine_are_homomorphisms(self):
        for l in T.LABELS:
            T.verify_homomorphism(self.G, self.reps[l].matrices)
            self.assertEqual(len(self.reps[l].matrices[0]), IRREP_DIMENSIONS[l])

    def test_weighted_unitarity(self):
        for l in T.LABELS:
            if self.reps[l].weights:
                self.assertTrue(T.verify_weighted_unitarity(self.G, self.reps[l]), l)

    def test_galois_conjugate_is_representation_but_sigma_does_not_preserve_set(self):
        r = T.galois_compatibility(self.G, self.reps)
        self.assertFalse(r["sigma_preserves_set_2I"])
        self.assertEqual(r["sigma_of_2I_inside_2I"], 24)   # only the binary tetrahedral part
        self.assertTrue(all(r["relations"].values()))

    def test_2_and_2prime_are_inequivalent(self):
        self.assertNotEqual(self.table["2"], self.table["2'"])
        self.assertNotEqual(self.table["3"], self.table["3'"])

    # ---- Task 3 -------------------------------------------------------
    def test_character_table_orthogonality(self):
        r = T.verify_character_table(self.table)
        self.assertEqual(r["row_pairs"], 81)
        self.assertEqual(sum(T.CLASS_SIZES), 120)
        self.assertEqual(sum(d * d for d in IRREP_DIMENSIONS.values()), 120)

    def test_fundamental_character(self):
        self.assertEqual(tuple(self.table["2"]), T.FUNDAMENTAL_CHARACTER)

    def test_json_export_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            payload = T.export_json(self.G, self.reps, self.table, self.classes, {"note": "test"})
            path = Path(tmp) / "t.json"
            path.write_text(json.dumps(payload))
            data = json.loads(path.read_text())
        self.assertEqual(data["class_sizes"], list(T.CLASS_SIZES))
        self.assertEqual(data["class_element_orders"], list(T.CLASS_ORDERS))
        self.assertEqual(set(data["irreps"]), set(T.LABELS))
        self.assertEqual(data["character_field"], "Q(sqrt5)")

    def test_committed_json_matches_recomputed_table(self):
        path = Path(__file__).resolve().parents[1] / "data" / "t034_2i_character_table.json"
        if not path.exists():
            self.skipTest("data file not generated yet")
        data = json.loads(path.read_text())
        for l in T.LABELS:
            self.assertEqual(data["irreps"][l]["values"], [x.encode() for x in self.table[l]])

    # ---- Task 4 -------------------------------------------------------
    def test_schur_orthogonality_all_coefficients(self):
        n = T.verify_schur_orthogonality(self.G, self.reps)
        self.assertEqual(n, 120 * 120)     # sum_{rho,sigma} d_rho^2 d_sigma^2

    def test_central_projectors_on_symmetric_powers(self):
        for m in range(0, 14):
            r = T.verify_projectors_on_sym(self.G, self.table, self.classes, m,
                                           full_orthogonality=(m <= 7))
            for l in T.LABELS:
                self.assertEqual(r["ranks"][l], IRREP_DIMENSIONS[l] * molien_coefficients(l, m)[m])

    def test_matrix_units_single_copies(self):
        for m in range(8):
            T.verify_matrix_units_on_sym(self.G, self.reps, m)

    def test_matrix_units_multiplicity_two(self):
        r = T.verify_matrix_units_multiplicity_two(self.G, self.reps)
        self.assertEqual(r["multiplicities"], {"3": 2})

    # ---- Task 5 -------------------------------------------------------
    def test_molien_series_from_characters_all_degrees(self):
        r = T.verify_molien_exact(self.table)
        self.assertEqual(r["numerators_checked"], 9)

    def test_character_averages_equal_molien_through_240(self):
        self.assertEqual(T.verify_character_average_series(self.table, 240), 9 * 241)

    def test_sum_d_M_is_one_over_one_minus_t_squared(self):
        # finite readout of the all-degree identity proved in verify_molien_exact
        for m in range(0, 241):
            self.assertEqual(
                sum(IRREP_DIMENSIONS[l] * molien_coefficients(l, m)[m] for l in T.LABELS), m + 1)

    def test_peter_weyl_level_dimension(self):
        self.assertTrue(T.cover_level_multiplicities(120))

    def test_characters_are_real_so_dual_twist_is_isomorphic(self):
        for l in T.LABELS:
            self.assertTrue(all(x.is_real() for x in self.table[l]))


if __name__ == "__main__":
    unittest.main()
