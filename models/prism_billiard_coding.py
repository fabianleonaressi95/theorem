"""Exact symbolic codings of circle rotations for the X6 PRISM study."""
from __future__ import annotations
from decimal import Decimal, localcontext
from fractions import Fraction
from typing import Sequence, TypeVar

Number = TypeVar("Number", Fraction, Decimal)

def _frac(x):
    return x % 1 if isinstance(x, Fraction) else x % Decimal(1)

def rotation_code(alpha, length: int, phase=None) -> tuple[int, ...]:
    """Code x -> x+alpha mod 1 using the half-open interval [1-alpha,1)."""
    if length < 0:
        raise ValueError("length must be non-negative")
    zero = Fraction(0) if isinstance(alpha, Fraction) else Decimal(0)
    one = Fraction(1) if isinstance(alpha, Fraction) else Decimal(1)
    if not zero < alpha < one:
        raise ValueError("alpha must lie strictly between 0 and 1")
    phase = zero if phase is None else phase
    if not zero <= phase < one:
        raise ValueError("phase must lie in [0,1)")
    threshold = one - alpha
    return tuple(int(_frac(phase + n * alpha) >= threshold) for n in range(length))

def continued_fraction_convergents(coefficients: Sequence[int]) -> tuple[Fraction, ...]:
    """Exact convergents [a0; a1,...,ak]."""
    if not coefficients or any(a < 0 for a in coefficients):
        raise ValueError("coefficients must be non-empty non-negative integers")
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    out = []
    for a in coefficients:
        p, q = a * pm1 + pm2, a * qm1 + qm2
        out.append(Fraction(p, q))
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
    return tuple(out)

def subword_complexity(word, width: int) -> int:
    if width <= 0:
        raise ValueError("width must be positive")
    if width > len(word):
        return 0
    return len({tuple(word[i:i+width]) for i in range(len(word)-width+1)})

def symbol_frequency(word, symbol=1) -> float:
    return sum(x == symbol for x in word) / len(word) if word else 0.0

def return_times(word, symbol=1) -> tuple[int, ...]:
    pos = [i for i, x in enumerate(word) if x == symbol]
    return tuple(b-a for a, b in zip(pos, pos[1:]))

def q6_six_bit_blocks(word) -> tuple[int, ...]:
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("word must be binary")
    return tuple(sum(int(bit) << (5-j) for j, bit in enumerate(word[i:i+6]))
                 for i in range(0, len(word)-5, 6))

def hamming_transition_counts(labels) -> tuple[int, ...]:
    return tuple((a ^ b).bit_count() for a, b in zip(labels, labels[1:]))

def cycle_lift(word, cycle_length: int) -> tuple[int, ...]:
    if cycle_length <= 0 or not word:
        raise ValueError("cycle_length and word length must be positive")
    return tuple(int(word[i % len(word)]) for i in range(cycle_length))

def approximation_report(irrational_alpha: Decimal, coefficients, length: int, precision: int=80) -> dict:
    if precision < 20:
        raise ValueError("precision must be at least 20")
    with localcontext() as ctx:
        ctx.prec = precision
        target = +irrational_alpha
        target_word = rotation_code(target, length)
        rows = []
        for approx in continued_fraction_convergents(coefficients):
            if not 0 < approx < 1:
                continue
            word = rotation_code(approx, length)
            q6 = q6_six_bit_blocks(word)
            rows.append({
                "p": approx.numerator, "q": approx.denominator,
                "value": str(Decimal(approx.numerator)/Decimal(approx.denominator)),
                "mismatch_count_vs_decimal_target": sum(a != b for a,b in zip(target_word,word)),
                "frequency_one": symbol_frequency(word),
                "subword_complexity": {str(k): subword_complexity(word,k) for k in range(1,min(8,length)+1)},
                "return_times_of_one": list(return_times(word)),
                "q6_block_count": len(q6), "q6_labels": list(q6),
                "q6_hamming_transitions": list(hamming_transition_counts(q6)),
            })
        return {
            "coding": "s_n=1 iff {phase+n*alpha} >= 1-alpha",
            "partition": "[1-alpha,1)", "target_alpha_decimal": str(target),
            "decimal_precision": precision, "target_word_length": length,
            "target_frequency_one": symbol_frequency(target_word),
            "target_subword_complexity": {str(k): subword_complexity(target_word,k) for k in range(1,min(8,length)+1)},
            "continued_fraction_coefficients": list(coefficients),
            "rational_approximants": rows,
            "interpretation": "Finite symbolic comparison only; no billiard trajectory or physical identification is established."
        }
