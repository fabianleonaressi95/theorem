"""Minimal six-qutrit EQC instruction compiler and state-vector simulator.

Basis digits 0,1,2 correspond respectively to symbols -1,0,+1.
This is a simulator/reference semantics, not a hardware backend.
"""
from math import sqrt, pi
import cmath

N_QUTRITS = 6
DIM = 3 ** N_QUTRITS
OMEGA = cmath.exp(2j * pi / 3)


def _qindex(token):
    if not token.startswith("q") or not token[1:].isdigit():
        raise ValueError("registers must be written q0,...,q5")
    value = int(token[1:])
    if not 0 <= value < N_QUTRITS:
        raise ValueError("qutrit index must be in [0, 5]")
    return value


def compile_source(source):
    """Compile line-oriented EQC source into validated instruction tuples.

    Grammar:
      X qN | Z qN | F qN | FDG qN
      SUM qCONTROL qTARGET
      P qN p0 p1 p2     (permutation of basis digits 0,1,2)
    Blank lines and text after # are ignored.
    """
    program = []
    for line_number, raw in enumerate(source.splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        fields = line.split()
        op = fields[0].upper()
        try:
            if op in {"X", "Z", "F", "FDG"} and len(fields) == 2:
                program.append((op, _qindex(fields[1])))
            elif op == "SUM" and len(fields) == 3:
                control, target = _qindex(fields[1]), _qindex(fields[2])
                if control == target:
                    raise ValueError("SUM control and target must differ")
                program.append((op, control, target))
            elif op == "P" and len(fields) == 5:
                q = _qindex(fields[1])
                permutation = tuple(int(x) for x in fields[2:])
                if sorted(permutation) != [0, 1, 2]:
                    raise ValueError("P requires a permutation of 0,1,2")
                program.append((op, q, permutation))
            elif op == "INV" and len(fields) == 2:
                program.append((op, _qindex(fields[1])))
            elif op == "SWAP" and len(fields) == 3:
                a, b = _qindex(fields[1]), _qindex(fields[2])
                if a == b:
                    raise ValueError("SWAP registers must differ")
                program.append((op, a, b))
            elif op in {"REV", "ROT"} and len(fields) == 1:
                program.append((op,))
            else:
                raise ValueError("unknown instruction or wrong number of operands")
        except ValueError as exc:
            raise ValueError(f"line {line_number}: {exc}") from exc
    return tuple(program)


def _single_matrix(op):
    if op == "X":
        return tuple(tuple(1 if r == (c + 1) % 3 else 0
                           for c in range(3)) for r in range(3))
    if op == "Z":
        return tuple(tuple(OMEGA ** c if r == c else 0j
                           for c in range(3)) for r in range(3))
    if op in {"F", "FDG"}:
        sign = 1 if op == "F" else -1
        return tuple(tuple(OMEGA ** (sign * r * c) / sqrt(3)
                           for c in range(3)) for r in range(3))
    raise ValueError(f"not a one-qutrit gate: {op}")


def _replace_digit(index, position, digit):
    stride = 3 ** (N_QUTRITS - 1 - position)
    old = (index // stride) % 3
    return index + (digit - old) * stride


def _apply_single(state, position, matrix):
    out = [0j] * DIM
    for base in range(DIM):
        if (base // (3 ** (N_QUTRITS - 1 - position))) % 3 != 0:
            continue
        indices = [_replace_digit(base, position, d) for d in range(3)]
        for row in range(3):
            out[indices[row]] = sum(
                matrix[row][col] * state[indices[col]] for col in range(3)
            )
    return out


def _apply_permutation(state, position, permutation):
    out = [0j] * DIM
    for old_index, amplitude in enumerate(state):
        stride = 3 ** (N_QUTRITS - 1 - position)
        old_digit = (old_index // stride) % 3
        new_index = _replace_digit(old_index, position, permutation[old_digit])
        out[new_index] = amplitude
    return out


def _apply_position_permutation(state, order):
    """Permute the six hexagram line/register positions."""
    out = [0j] * DIM
    for old_index, amplitude in enumerate(state):
        old_digits = [0] * N_QUTRITS
        value = old_index
        for pos in range(N_QUTRITS - 1, -1, -1):
            value, old_digits[pos] = divmod(value, 3)
        new_digits = [old_digits[order[pos]] for pos in range(N_QUTRITS)]
        new_index = 0
        for digit in new_digits:
            new_index = 3 * new_index + digit
        out[new_index] = amplitude
    return out


def _apply_sum(state, control, target):
    out = [0j] * DIM
    cstride = 3 ** (N_QUTRITS - 1 - control)
    tstride = 3 ** (N_QUTRITS - 1 - target)
    for old_index, amplitude in enumerate(state):
        c = (old_index // cstride) % 3
        t = (old_index // tstride) % 3
        new_index = old_index + ((t + c) % 3 - t) * tstride
        out[new_index] = amplitude
    return out


def run(program, initial_state=None):
    """Execute compiled instructions on a 729-amplitude state vector.

    Default initial state is |000000>. Returns a new complex list.
    """
    if initial_state is None:
        state = [0j] * DIM
        state[0] = 1 + 0j
    else:
        if len(initial_state) != DIM:
            raise ValueError("state vector must have 729 amplitudes")
        state = [complex(x) for x in initial_state]
        norm2 = sum(abs(x) ** 2 for x in state)
        if abs(norm2 - 1.0) > 1e-10:
            raise ValueError("initial state must be normalized")
    for instruction in program:
        op = instruction[0]
        if op in {"X", "Z", "F", "FDG"}:
            state = _apply_single(state, instruction[1], _single_matrix(op))
        elif op == "P":
            state = _apply_permutation(state, instruction[1], instruction[2])
        elif op == "SUM":
            state = _apply_sum(state, instruction[1], instruction[2])
        elif op == "INV":
            # Digit map 0<->2, 1 fixed: symbol map -1<->+1, 0 fixed.
            state = _apply_permutation(state, instruction[1], (2, 1, 0))
        elif op == "SWAP":
            order = list(range(N_QUTRITS))
            order[instruction[1]], order[instruction[2]] = (
                order[instruction[2]], order[instruction[1]]
            )
            state = _apply_position_permutation(state, order)
        elif op == "REV":
            state = _apply_position_permutation(
                state, tuple(reversed(range(N_QUTRITS)))
            )
        elif op == "ROT":
            state = _apply_position_permutation(
                state, (1, 2, 3, 4, 5, 0)
            )
        else:
            raise ValueError(f"unsupported instruction: {op}")
    return state


def norm_squared(state):
    return sum(abs(x) ** 2 for x in state)


def nonzero_amplitudes(state, tolerance=1e-12):
    """Return (basis_index, amplitude) pairs above a numerical threshold."""
    return tuple((i, value) for i, value in enumerate(state)
                 if abs(value) > tolerance)
