"""Monte Carlo audit of the golden cumulative-coordinate Markov operator.

Convention:
    A[i,j] = <e_i, M_g e_j>_{L2(0,1)}
where e_0,e_1 are the first real Fourier pair and e_2,e_3,e_4
are the constant and second-harmonic complement.

The CDF is approximated by the empirical CDF of a truncated golden
Bernoulli convolution. Results are numerical evidence, not exact
operator identities.
"""
from bisect import bisect_right
from math import cos, pi, sin, sqrt
import random


PHI = (1.0 + sqrt(5.0)) / 2.0
LAMBDA = 1.0 / PHI


def _basis(t):
    return (
        sqrt(2.0) * cos(2.0 * pi * t),
        sqrt(2.0) * sin(2.0 * pi * t),
        1.0,
        sqrt(2.0) * cos(4.0 * pi * t),
        sqrt(2.0) * sin(4.0 * pi * t),
    )


def estimate_markov_matrix(samples=300_000, terms=48, seed=20261124):
    """Estimate A[i,j]=integral e_i(t) (M_g e_j)(t) dt.

    Uses inverse-transform sampling through the empirical CDF. The omitted
    Bernoulli-series tail is bounded by LAMBDA**terms/(1-LAMBDA).
    """
    if samples < 1000:
        raise ValueError("use at least 1000 samples")
    if terms < 1:
        raise ValueError("terms must be positive")

    rng = random.Random(seed)
    powers = [LAMBDA ** k for k in range(terms)]
    values = []
    for _ in range(samples):
        x = 0.0
        for weight in powers:
            x += weight if rng.getrandbits(1) else -weight
        values.append(x)
    values.sort()

    matrix = [[0.0] * 5 for _ in range(5)]
    inv_n = 1.0 / samples
    for index, x in enumerate(values):
        t = (index + 0.5) * inv_n
        t_minus = bisect_right(values, LAMBDA * x - 1.0) * inv_n
        t_plus = bisect_right(values, LAMBDA * x + 1.0) * inv_n
        source = _basis(t)
        minus = _basis(t_minus)
        plus = _basis(t_plus)
        for i in range(5):
            for j in range(5):
                matrix[i][j] += (
                    source[i] * 0.5 * (minus[j] + plus[j]) * inv_n
                )
    return matrix


def block_norm(matrix, row_start, row_stop, col_start, col_stop):
    return sqrt(sum(
        matrix[i][j] ** 2
        for i in range(row_start, row_stop)
        for j in range(col_start, col_stop)
    ))


def audit(samples=300_000, terms=48, seed=20261124):
    matrix = estimate_markov_matrix(samples, terms, seed)
    return {
        "operator_matrix": matrix,
        "active_from_complement_frobenius": block_norm(matrix, 0, 2, 2, 5),
        "complement_from_active_frobenius": block_norm(matrix, 2, 5, 0, 2),
        "cdf_tail_bound": LAMBDA ** terms / (1.0 - LAMBDA),
        "samples": samples,
        "terms": terms,
        "seed": seed,
        "convention": "A[i,j] = <e_i, M_g e_j>",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(audit(), indent=2))
