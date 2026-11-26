"""Reproducible chaos-game and anisotropic IFS checks for TSMR-02.

The implementation deliberately uses only the Python standard library.
It distinguishes exact contraction/pressure checks from finite random
sampling diagnostics; sampled point clouds are not proofs of fractality.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Sequence

Matrix2 = tuple[tuple[float, float], tuple[float, float]]


@dataclass(frozen=True)
class AffineMap2D:
    """Affine map (x,y) -> A(x,y) + b with a sampling probability."""

    a: float
    b: float
    c: float
    d: float
    e: float
    f: float
    probability: float
    name: str = ""

    @property
    def matrix(self) -> Matrix2:
        return ((self.a, self.b), (self.d, self.e))

    def apply(self, point: tuple[float, float]) -> tuple[float, float]:
        x, y = point
        return (self.a * x + self.b * y + self.c,
                self.d * x + self.e * y + self.f)


def singular_values_2x2(matrix: Matrix2) -> tuple[float, float]:
    """Return singular values (sigma_max, sigma_min), descending."""
    (a, b), (c, d) = matrix
    trace = a*a + b*b + c*c + d*d
    det_a = a*d - b*c
    disc = max(0.0, trace*trace - 4.0*det_a*det_a)
    root = math.sqrt(disc)
    lam_max = max(0.0, (trace + root) / 2.0)
    lam_min = max(0.0, (trace - root) / 2.0)
    return (math.sqrt(lam_max), math.sqrt(lam_min))


def validate_ifs(maps: Sequence[AffineMap2D], tolerance: float = 1e-12) -> dict:
    """Validate positive probabilities and strict Euclidean contractions."""
    if not maps:
        raise ValueError("IFS must contain at least one affine map")
    probabilities = [item.probability for item in maps]
    if any(not math.isfinite(p) or p <= 0.0 for p in probabilities):
        raise ValueError("sampling probabilities must be finite and positive")
    if not math.isclose(sum(probabilities), 1.0, rel_tol=0.0,
                        abs_tol=tolerance):
        raise ValueError("map probabilities must sum to one")
    contractions = []
    for item in maps:
        sigma_max, _ = singular_values_2x2(item.matrix)
        if not sigma_max < 1.0:
            raise ValueError(f"map {item.name!r} is not a strict Euclidean contraction")
        contractions.append(sigma_max)
    return {
        "map_count": len(maps),
        "probability_sum": sum(probabilities),
        "max_contraction": max(contractions),
        "all_strict_contractions": True,
    }


def chaos_game(
    maps: Sequence[AffineMap2D],
    iterations: int,
    seed: int = 0,
    start: tuple[float, float] = (0.0, 0.0),
    burn_in: int = 0,
) -> tuple[list[tuple[float, float]], list[int]]:
    """Sample an IFS attractor using weighted random affine maps."""
    validate_ifs(maps)
    if iterations < 0 or burn_in < 0:
        raise ValueError("iterations and burn_in must be nonnegative")
    rng = random.Random(seed)
    weights = [item.probability for item in maps]
    point = start
    points: list[tuple[float, float]] = []
    counts = [0] * len(maps)
    for step in range(iterations + burn_in):
        index = rng.choices(range(len(maps)), weights=weights, k=1)[0]
        counts[index] += 1
        point = maps[index].apply(point)
        if step >= burn_in:
            points.append(point)
    return points, counts


def matrix_product(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0]*right[0][0] + left[0][1]*right[1][0],
         left[0][0]*right[0][1] + left[0][1]*right[1][1]),
        (left[1][0]*right[0][0] + left[1][1]*right[1][0],
         left[1][0]*right[0][1] + left[1][1]*right[1][1]),
    )


def singular_value_function_2d(matrix: Matrix2, s: float) -> float:
    """Falconer singular-value function for 0 <= s <= 2."""
    if not 0.0 <= s <= 2.0:
        raise ValueError("s must lie in [0, 2]")
    sigma_max, sigma_min = singular_values_2x2(matrix)
    if s <= 1.0:
        return sigma_max ** s
    return sigma_max * sigma_min ** (s - 1.0)


def finite_depth_pressure(
    matrices: Sequence[Matrix2], s: float, depth: int
) -> float:
    """Finite-depth pressure estimate; diagnostic, not limiting pressure."""
    if not matrices or depth < 1:
        raise ValueError("provide matrices and a positive depth")
    products = [((1.0, 0.0), (0.0, 1.0))]
    for _ in range(depth):
        products = [matrix_product(previous, matrix)
                    for previous in products for matrix in matrices]
    total = sum(singular_value_function_2d(product, s)
                for product in products)
    if total <= 0.0:
        return float("-inf")
    return math.log(total) / depth


def common_diagonal_pressure(
    map_count: int, sigma_max: float, sigma_min: float, s: float
) -> float:
    """Exact pressure for m maps sharing a positive diagonal linear part."""
    if map_count < 1:
        raise ValueError("map_count must be positive")
    if not (0.0 < sigma_min <= sigma_max < 1.0):
        raise ValueError("singular values must satisfy 0 < min <= max < 1")
    if not 1.0 <= s <= 2.0:
        raise ValueError("s must lie in [1, 2]")
    return (math.log(map_count) + math.log(sigma_max)
            + (s - 1.0) * math.log(sigma_min))


def common_diagonal_affinity_dimension(
    map_count: int, sigma_max: float, sigma_min: float
) -> float:
    """Exact affinity-dimension root for maps with a common diagonal part.

    Assumes m maps share the same positive diagonal linear part, with
    singular values sigma_max >= sigma_min > 0. The value is capped at 2.
    """
    if map_count < 1:
        raise ValueError("map_count must be positive")
    if not (0.0 < sigma_min <= sigma_max < 1.0):
        raise ValueError("singular values must satisfy 0 < min <= max < 1")
    p_at_1 = math.log(map_count) + math.log(sigma_max)
    if p_at_1 <= 0.0:
        return min(1.0, max(0.0, -math.log(map_count) / math.log(sigma_max)))
    p_at_2 = p_at_1 + math.log(sigma_min)
    if p_at_2 >= 0.0:
        return 2.0
    return 1.0 - p_at_1 / math.log(sigma_min)


def sierpinski_ifs() -> tuple[AffineMap2D, ...]:
    """Equal-probability half-contractions toward triangle vertices."""
    return (
        AffineMap2D(.5, 0, 0, 0, .5, 0, 1/3, "A"),
        AffineMap2D(.5, 0, .5, 0, .5, 0, 1/3, "B"),
        AffineMap2D(.5, 0, .25, 0, .5, math.sqrt(3)/4, 1/3, "C"),
    )


def barnsley_fern_ifs() -> tuple[AffineMap2D, ...]:
    """Barnsley fern maps and 1%, 79%, 10%, 10% probabilities."""
    return (
        AffineMap2D(0, 0, 0, 0, .16, 0, .01, "stem"),
        AffineMap2D(.85, .04, 0, -.04, .85, 1.60, .79, "top"),
        AffineMap2D(.20, -.26, 0, .23, .22, .80, .10, "left"),
        AffineMap2D(-.15, .28, 0, .26, .24, .44, .10, "right"),
    )


def anisotropic_ifs() -> tuple[AffineMap2D, ...]:
    """Two maps with common anisotropic linear part diag(1/2,1/4)."""
    return (
        AffineMap2D(.5, 0, 0, 0, .25, 0, .5, "lower-left"),
        AffineMap2D(.5, 0, .5, 0, .25, .25, .5, "upper-right"),
    )
