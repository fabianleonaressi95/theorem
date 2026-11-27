import unittest

from audits.morphodynamics.eqc_rgs_q6_gates import (
    RGS_Q6_GATE_SOURCE, apply_q6_gate_generator,
    direction_reference_stabilizer_order, generated_rgs_q6_group,
    induced_rgs_q6_group, q6_vertex_to_qutrit_digits,
    qutrit_digits_to_q6_vertex, rgs_q6_edge_stabilizer,
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
    def test_three_generators_generate_exact_order_16_subgroup(self):
        generated = generated_rgs_q6_group()
        self.assertEqual(len(generated), 16)
        self.assertEqual(generated, induced_rgs_q6_group())

    def test_three_native_gate_programs_realize_exact_rgs_actions(self):
        self.assertEqual(len(RGS_Q6_GATE_SOURCE), 3)
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

    def test_full_qutrit_basis_permutations_are_bijective(self):
        for source in RGS_Q6_GATE_SOURCE.values():
            program = compile_source(source)
            images = []
            for basis in range(3 ** 6):
                state = [0j] * (3 ** 6)
                state[basis] = 1 + 0j
                output = run(program, state)
                images.append(next(i for i, a in enumerate(output)
                                   if abs(a) > 1e-12))
            self.assertEqual(len(set(images)), 3 ** 6)

    def test_binary_flip_fixes_excluded_ternary_level(self):
        for register in (1, 2):
            program = compile_source(f"P q{register} 0 2 1")
            digits = [1] * 6
            digits[register] = 0
            state = [0j] * (3 ** 6)
            state[encode_qutrit_digits(digits)] = 1 + 0j
            output = run(program, state)
            nonzero = next(i for i, a in enumerate(output) if abs(a) > 1e-12)
            self.assertEqual(decode_qutrit_digits(nonzero)[register], 0)

    def test_isotropic_and_anisotropic_reference_stabilizers(self):
        self.assertEqual(len(rgs_q6_edge_stabilizer((0.0,) * 192)), 16)
        self.assertEqual(direction_reference_stabilizer_order(
            (0., 1., 2., 3., 4., 5.)), 8)
        self.assertEqual(direction_reference_stabilizer_order(
            (0., 0., 2., 3., 3., 5.)), 16)

    def test_generic_edgewise_reference_has_trivial_stabilizer(self):
        self.assertEqual(len(rgs_q6_edge_stabilizer(tuple(range(192)))), 1)


if __name__ == "__main__":
    unittest.main()
