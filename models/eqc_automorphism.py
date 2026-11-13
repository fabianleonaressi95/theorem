"""Exact combinatorial automorphism audit for the six-line ternary Hamming graph."""
from itertools import product
from math import factorial

ALPHABET = (-1, 0, 1)
N = 6


def hamming_distance(left, right):
    if len(left) != N or len(right) != N:
        raise ValueError("words must have six symbols")
    return sum(a != b for a, b in zip(left, right))


def symbol_shift(word, positions=None):
    """Apply the cyclic symbol permutation -1 -> 0 -> +1 -> -1."""
    out = list(word)
    selected = range(N) if positions is None else positions
    shift = {-1: 0, 0: 1, 1: -1}
    for i in selected:
        if not 0 <= i < N:
            raise ValueError("position must be in [0,5]")
        if out[i] not in shift:
            raise ValueError("invalid ternary symbol")
        out[i] = shift[out[i]]
    return tuple(out)


def symbol_inversion(word, positions=None):
    """Apply the semantic polarity inversion -1 <-> +1, 0 fixed."""
    out = list(word)
    selected = range(N) if positions is None else positions
    for i in selected:
        if not 0 <= i < N:
            raise ValueError("position must be in [0,5]")
        if out[i] not in ALPHABET:
            raise ValueError("invalid ternary symbol")
        out[i] = -out[i]
    return tuple(out)


def permute_lines(word, order):
    """Output coordinate i receives input coordinate order[i]."""
    if len(word) != N or sorted(order) != list(range(N)):
        raise ValueError("order must be a permutation of six positions")
    return tuple(word[order[i]] for i in range(N))


def all_ternary_words():
    return product(ALPHABET, repeat=N)


def ternary_hamming_graph_order():
    """|Aut(H(6,3))| = (3!)^6 * 6!."""
    return factorial(3) ** N * factorial(N)


def binary_q6_automorphism_order():
    """|Aut(Q6)| = (2!)^6 * 6!."""
    return factorial(2) ** N * factorial(N)


def generators_preserve_hamming_distance():
    """Exhaustively verify the named generator families on H(6,3)."""
    words = list(all_ternary_words())
    maps = [
        lambda w: symbol_shift(w, (0,)),
        lambda w: symbol_inversion(w, (2,)),
        lambda w: permute_lines(w, (5, 1, 2, 3, 4, 0)),
        lambda w: permute_lines(w, (5, 4, 3, 2, 1, 0)),
    ]
    for transform in maps:
        for word in words:
            image = transform(word)
            for neighbor in words:
                if hamming_distance(word, neighbor) == 1:
                    if hamming_distance(image, transform(neighbor)) != 1:
                        return False
    return True
