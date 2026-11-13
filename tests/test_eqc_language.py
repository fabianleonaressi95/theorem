import unittest
from math import sqrt

from models.eqc_language import (
    DIM, compile_source, nonzero_amplitudes, norm_squared, run,
)


class TestEQCLanguage(unittest.TestCase):
    def test_compile_and_execute_x_cubed(self):
        program = compile_source("X q0\nX q0\nX q0")
        state = run(program)
        self.assertAlmostEqual(abs(state[0] - 1), 0.0, places=12)
        self.assertAlmostEqual(norm_squared(state), 1.0, places=12)

    def test_sum_cubed_is_identity(self):
        program = compile_source("X q0\nSUM q0 q1\nSUM q0 q1\nSUM q0 q1")
        state = run(program)
        # X q0 leaves the control at digit 1; three SUMs restore target.
        expected = 3 ** 5  # index with q0=1, remaining digits zero
        self.assertAlmostEqual(abs(state[expected] - 1), 0.0, places=12)
        self.assertAlmostEqual(norm_squared(state), 1.0, places=12)

    def test_fourier_and_adjoint_restore_basis_state(self):
        state = run(compile_source("F q3\nFDG q3"))
        self.assertAlmostEqual(abs(state[0] - 1), 0.0, places=12)
        self.assertAlmostEqual(norm_squared(state), 1.0, places=12)

    def test_fourier_sum_creates_entangled_three_term_state(self):
        state = run(compile_source("F q0\nSUM q0 q1"))
        support = nonzero_amplitudes(state)
        self.assertEqual(len(support), 3)
        self.assertTrue(all(abs(abs(a) - 1 / sqrt(3)) < 1e-12
                            for _, a in support))
        self.assertAlmostEqual(norm_squared(state), 1.0, places=12)

    def test_local_permutation_is_reversible_and_norm_preserving(self):
        p = compile_source("P q5 1 0 2")
        state = run(p)
        self.assertEqual(len(state), DIM)
        # q5 is the least significant trit: |000002> is index 2.
        self.assertAlmostEqual(abs(state[1] - 1), 0.0, places=12)
        self.assertAlmostEqual(norm_squared(state), 1.0, places=12)

    def test_compiler_rejects_invalid_instructions(self):
        invalid = [
            "X q6",
            "SUM q1 q1",
            "P q0 0 0 2",
            "H q0",
            "Z",
        ]
        for source in invalid:
            with self.subTest(source=source):
                with self.assertRaises(ValueError):
                    compile_source(source)

    def test_hexagram_line_reversal_is_involution(self):
        state = run(compile_source("X q0\nX q1\nREV\nREV"))
        expected_index = 3 + 1
        self.assertAlmostEqual(abs(state[expected_index] - 1), 0.0, places=12)
        self.assertAlmostEqual(norm_squared(state), 1.0, places=12)

    def test_hexagram_line_rotation_has_order_six(self):
        source = "X q0\n" + "\n".join(["ROT"] * 6)
        state = run(compile_source(source))
        self.assertAlmostEqual(abs(state[3**5] - 1), 0.0, places=12)

    def test_polarity_inversion_is_involution(self):
        state = run(compile_source("X q0\nX q0\nINV q0\nINV q0"))
        self.assertAlmostEqual(abs(state[2 * 3**5] - 1), 0.0, places=12)

    def test_register_swap_is_involution(self):
        state = run(compile_source("X q0\nSWAP q0 q5\nSWAP q0 q5"))
        self.assertAlmostEqual(abs(state[3**5] - 1), 0.0, places=12)

    def test_initial_state_must_be_normalized(self):
        with self.assertRaises(ValueError):
            run((), [0j] * DIM)


if __name__ == "__main__":
    unittest.main()
