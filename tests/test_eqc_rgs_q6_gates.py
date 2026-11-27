import unittest

from audits.morphodynamics.eqc_rgs_q6_gates import (
    RGS_Q6_GATE_SOURCE,
    apply_q6_gate_generator,
    generated_rgs_q6_group,
    induced_rgs_q6_group,
    q6_vertex_to_qutrit_digits,
    qutrit_digits_to_q6_vertex,
    rgs_q6_edge_stabilizer,
)
from models.eqc_language import compile_source, run


def encode_qutrit_digits(digits):
    value = 0
    for digit in digits:
        value = 3 * value + digit
    return value


def decode_qutrit_digits(value):
    digits = [0] * 6
    for i in range(5, -1, -1):
        value, digits[i] = divmod(value, 3)
    return tuple(digits)


class TestEQCRGSQ6GateRealization(unittest.TestCase):
    def test_generated_group_has_order_16_and_matches_rgs_seed(self):
        generated = generated_rgs_q6_group()
        induced = induced_rgs_q6_group()
        self.assertEqual(len(generated), 16)
        self.assertEqual(generated, induced)

    def test_named_generators_preserve_q6_adjacency(self):
        group = generated_rgs_q6_group()
        self.assertTrue(all(sorted(p) == list(range(64)) for p in group))
        for p in group:
            for v in range(64):
                for bit in range(6):
                    self.assertEqual(
                        (p[v] ^ p[v ^ (1 << bit)]).bit_count(), 1
                    )

    def test_qutrit_gate_programs_realize_exact_q6_actions(self):
        for name, source in RGS_Q6_GATE_SOURCE.items():
            program = compile_source(source)
            for vertex in range(64):
                digits = q6_vertex_to_qutrit_digits(vertex)
                state = [0j] * (3 ** 6)
                state[encode_qutrit_digits(digits)] = 1 + 0j
                output = run(program, state)
                nonzero = [i for i, amplitude in enumerate(output)
                           if abs(amplitude) > 1e-12]
                self.assertEqual(len(nonzero), 1)
                result_digits = decode_qutrit_digits(nonzero[0])
                result_vertex = qutrit_digits_to_q6_vertex(result_digits)
                self.assertEqual(
                    result_vertex, apply_q6_gate_generator(vertex, name)
                )

    def test_binary_sector_is_preserved_and_excluded_level_is_fixed(self):
        # Stored digit 0 represents symbol -1 and must remain outside Q6.
        for name, source in RGS_Q6_GATE_SOURCE.items():
            program = compile_source(source)
            self.assertTrue(program)
            for vertex in range(64):
                digits = q6_vertex_to_qutrit_digits(vertex)
                self.assertTrue(all(d in (1, 2) for d in digits))
        # The local Q6 flip fixes the excluded digit 0 pointwise.
        for q in range(3):
            source = f"P q{q} 0 2 1"
            digits = [1, 1, 1, 1, 1, 1]
            digits[q] = 0
            state = [0j] * (3 ** 6)
            state[encode_qutrit_digits(digits)] = 1 + 0j
            output = run(compile_source(source), state)
            nonzero = next(i for i, a in enumerate(output) if abs(a) > 1e-12)
            self.assertEqual(decode_qutrit_digits(nonzero)[q], 0)
        # Existing INV swaps stored digits 0 and 2, so it does not preserve Q6.
        inv = compile_source("INV q0")
        digits = (2, 1, 1, 1, 1, 1)
        state = [0j] * (3 ** 6)
        state[encode_qutrit_digits(digits)] = 1 + 0j
        output = run(inv, state)
        nonzero = next(i for i, a in enumerate(output) if abs(a) > 1e-12)
        self.assertEqual(decode_qutrit_digits(nonzero)[0], 0)

    def test_rgs_restricted_mqm_stabilizers(self):
        uniform = (0.0,) * 192
        directional = tuple(float(direction) for _, _, direction in
                             __import__(
                                 "audits.morphodynamics.q6_mqm_symmetry",
                                 fromlist=["q6_edges"]
                             ).q6_edges())
        generic = tuple(float(i) for i in range(192))
        self.assertEqual(len(rgs_q6_edge_stabilizer(uniform)), 16)
        self.assertEqual(len(rgs_q6_edge_stabilizer(directional)), 8)
        self.assertEqual(len(rgs_q6_edge_stabilizer(generic)), 1)


if __name__ == "__main__":
    unittest.main()
