"""Exact Molien-covariant multiplicities for the nine irreps of 2I.

Numerators are transcribed from T021. This module does not claim explicit
unitary matrices or a full character table. All coefficient arithmetic is exact.
"""
IRREP_NUMERATORS = {
    "1": (0, 30), "2": (1, 11, 19, 29), "2'": (7, 13, 17, 23),
    "3": (2, 10, 12, 18, 20, 28), "3'": (6, 10, 14, 16, 20, 24),
    "4": (6, 8, 12, 14, 16, 18, 22, 24),
    "4'": (3, 9, 11, 13, 17, 19, 21, 27),
    "5": (4, 8, 10, 12, 14, 16, 18, 20, 22, 26),
    "6": (5, 7, 9, 11, 13, 15, 15, 17, 19, 21, 23, 25),
}
IRREP_DIMENSIONS = {"1": 1, "2": 2, "2'": 2, "3": 3, "3'": 3,
                    "4": 4, "4'": 4, "5": 5, "6": 6}


def molien_coefficients(label: str, max_degree: int) -> tuple[int, ...]:
    """Coefficients of N(t)/((1-t^12)(1-t^20)) through max_degree."""
    if label not in IRREP_NUMERATORS:
        raise KeyError(label)
    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    support = IRREP_NUMERATORS[label]
    return tuple(sum(1 for a in range(m // 12 + 1)
                     for b in range(m // 20 + 1)
                     if m - 12*a - 20*b in support)
                 for m in range(max_degree + 1))


def all_multiplicities(max_degree: int) -> dict[str, tuple[int, ...]]:
    return {name: molien_coefficients(name, max_degree)
            for name in IRREP_NUMERATORS}


def verify_dimension_decomposition(max_degree: int) -> bool:
    """Check sum_r dim(r)b_(m,r)=m+1 for every degree in the range."""
    coeffs = all_multiplicities(max_degree)
    return all(sum(IRREP_DIMENSIONS[r] * coeffs[r][m]
                   for r in IRREP_NUMERATORS) == m + 1
               for m in range(max_degree + 1))


def verify_sum_of_squares() -> bool:
    return sum(d*d for d in IRREP_DIMENSIONS.values()) == 120


def isotypic_projector_normalization(label: str) -> tuple[int, int]:
    """Return (d_rho, |2I|); character and U(g) matrices are separate inputs."""
    if label not in IRREP_DIMENSIONS:
        raise KeyError(label)
    return IRREP_DIMENSIONS[label], 120
