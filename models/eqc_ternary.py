"""Finite combinatorics and qutrit primitives for Esagrammatic Quantum Computing.

The symbols -1, 0, +1 are labels, not quantum amplitudes.
No external dependencies are required.
"""
from itertools import product
from math import comb
import cmath

ALPHABET = (-1, 0, 1)
_DIGIT = {-1: 0, 0: 1, 1: 2}
_SYMBOL = (-1, 0, 1)
N_POSITIONS = 6


def encode(word):
    """Return the base-three rank of a six-symbol ternary word."""
    word = tuple(word)
    if len(word) != N_POSITIONS or any(x not in _DIGIT for x in word):
        raise ValueError("word must contain exactly six symbols from {-1, 0, +1}")
    rank = 0
    for symbol in word:
        rank = 3 * rank + _DIGIT[symbol]
    return rank


def decode(index):
    """Inverse of encode, for indices 0,...,728."""
    if not isinstance(index, int) or not 0 <= index < 3**N_POSITIONS:
        raise ValueError("index must be an integer in [0, 728]")
    digits = [0] * N_POSITIONS
    value = index
    for pos in range(N_POSITIONS - 1, -1, -1):
        value, digits[pos] = divmod(value, 3)
    return tuple(_SYMBOL[d] for d in digits)


def all_words():
    """Yield all 729 words in lexicographic order."""
    return product(ALPHABET, repeat=N_POSITIONS)


def hamming_distance(left, right):
    left, right = tuple(left), tuple(right)
    if len(left) != N_POSITIONS or len(right) != N_POSITIONS:
        raise ValueError("both words must have length six")
    return sum(a != b for a, b in zip(left, right))


def neighbors(word):
    """Yield the 12 words differing in exactly one coordinate."""
    word = tuple(word)
    encode(word)  # validate
    for pos in range(N_POSITIONS):
        for symbol in ALPHABET:
            if symbol != word[pos]:
                candidate = list(word)
                candidate[pos] = symbol
                yield tuple(candidate)


def q6_binary_words():
    """The {0,+1}^6 induced subgraph, canonically identified with Q6."""
    return product((0, 1), repeat=N_POSITIONS)


def ternary_hamming_spectrum():
    """Return (eigenvalue, multiplicity) pairs for K3^(square 6)."""
    return tuple((12 - 3 * k, comb(6, k) * (2**k)) for k in range(7))


def qutrit_shift():
    """Matrix X with X|j> = |j+1 mod 3>, represented by row tuples."""
    return tuple(tuple(1 if row == (col + 1) % 3 else 0
                       for col in range(3)) for row in range(3))


def qutrit_clock():
    """Matrix Z with Z|j> = omega^j |j>, represented by row tuples."""
    omega = cmath.exp(2j * cmath.pi / 3)
    return tuple(tuple(omega**col if row == col else 0j
                       for col in range(3)) for row in range(3))


def matrix_multiply(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def conjugate_transpose(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(len(a)))
                 for i in range(len(a[0])))


def is_identity(a, tol=1e-12):
    return all(abs(a[i][j] - (1 if i == j else 0)) <= tol
               for i in range(len(a)) for j in range(len(a[0])))


def flip_sign(word, position):
    """Classical reversible sign flip at one coordinate."""
    word = list(word)
    encode(word)
    if not isinstance(position, int) or not 0 <= position < N_POSITIONS:
        raise ValueError("position must be in [0, 5]")
    word[position] = -word[position]
    return tuple(word)
