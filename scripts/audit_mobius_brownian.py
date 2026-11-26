#!/usr/bin/env python3
"""Finite arithmetic and descriptive block diagnostics for Möbius coefficients.

This is not a test of RH/GRH and does not establish Brownian convergence.
Only the Python standard library is required.
"""
from __future__ import annotations

import argparse
import json
import math
from statistics import fmean, pvariance
from typing import Iterable


def mobius_sieve(n_max: int) -> list[int]:
    """Return mu[0..n_max] using a linear sieve and exact integer arithmetic."""
    if n_max < 0:
        raise ValueError("n_max must be non-negative")
    mu = [0] * (n_max + 1)
    if n_max == 0:
        return mu
    mu[1] = 1
    primes: list[int] = []
    composite = bytearray(n_max + 1)
    for n in range(2, n_max + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            m = p * n
            if m > n_max:
                break
            composite[m] = 1
            if n % p == 0:
                mu[m] = 0
                break
            mu[m] = -mu[n]
    return mu


def mertens_prefix(mu: list[int]) -> list[int]:
    """Return M[0..N], where M[k] = sum_{n<=k} mu(n)."""
    out = [0] * len(mu)
    running = 0
    for n in range(1, len(mu)):
        running += mu[n]
        out[n] = running
    return out


def squarefree_signs(mu: list[int]) -> list[int]:
    """Return mu(f_j) in increasing order of square-free integers f_j."""
    return [value for value in mu[1:] if value != 0]


def block_sums(values: Iterable[int], block_size: int) -> list[int]:
    """Non-overlapping sums of complete blocks; discard the incomplete tail."""
    if block_size <= 0:
        raise ValueError("block_size must be positive")
    data = list(values)
    count = len(data) // block_size
    return [sum(data[i * block_size : (i + 1) * block_size]) for i in range(count)]


def block_statistics(values: Iterable[int], block_size: int) -> dict[str, float | int | None]:
    """Descriptive statistics of complete non-overlapping block sums."""
    sums = block_sums(values, block_size)
    count = len(sums)
    if count == 0:
        return {"block_size": block_size, "block_count": 0, "mean": None,
                "variance": None, "standardized_fourth_moment": None,
                "lag1_correlation": None}
    mean = fmean(sums)
    variance = pvariance(sums)
    fourth = None if variance == 0.0 else fmean(
        ((x - mean) / math.sqrt(variance)) ** 4 for x in sums
    )
    if count < 2:
        lag1 = None
    else:
        left, right = sums[:-1], sums[1:]
        lm, rm = fmean(left), fmean(right)
        numerator = sum((x - lm) * (y - rm) for x, y in zip(left, right))
        left_ss = sum((x - lm) ** 2 for x in left)
        right_ss = sum((y - rm) ** 2 for y in right)
        denominator = math.sqrt(left_ss * right_ss)
        lag1 = numerator / denominator if denominator else None
    return {"block_size": block_size, "block_count": count, "mean": mean,
            "variance": variance, "standardized_fourth_moment": fourth,
            "lag1_correlation": lag1}


def estimate_descriptive_hurst(values: list[int], block_sizes: Iterable[int]) -> dict[str, object]:
    """Fit log variance = intercept + 2H log(block size), descriptively only."""
    points: list[tuple[float, float]] = []
    used: list[int] = []
    for size in block_sizes:
        stats = block_statistics(values, size)
        variance, count = stats["variance"], stats["block_count"]
        if count >= 8 and variance is not None and variance > 0:
            points.append((math.log(size), math.log(variance)))
            used.append(size)
    if len(points) < 2:
        return {"hurst_exponent": None, "scales_used": used, "loglog_r_squared": None}
    xs, ys = [p[0] for p in points], [p[1] for p in points]
    xbar, ybar = fmean(xs), fmean(ys)
    sxx = sum((x - xbar) ** 2 for x in xs)
    if sxx == 0:
        return {"hurst_exponent": None, "scales_used": used, "loglog_r_squared": None}
    slope = sum((x - xbar) * (y - ybar) for x, y in points) / sxx
    intercept = ybar - slope * xbar
    residual = sum((y - (intercept + slope * x)) ** 2 for x, y in points)
    total = sum((y - ybar) ** 2 for y in ys)
    return {"hurst_exponent": slope / 2.0, "scales_used": used,
            "loglog_r_squared": 1.0 - residual / total if total else 1.0}


def audit(n_max: int, block_sizes: Iterable[int]) -> dict[str, object]:
    if n_max < 1:
        raise ValueError("n_max must be at least 1")
    sizes = list(block_sizes)
    if not sizes or any(size <= 0 for size in sizes):
        raise ValueError("provide one or more positive block sizes")
    mu = mobius_sieve(n_max)
    mertens = mertens_prefix(mu)
    signs = squarefree_signs(mu)
    return {
        "n_max": n_max,
        "mertens_M_n": mertens[n_max],
        "squarefree_count": len(signs),
        "squarefree_density": len(signs) / n_max,
        "block_statistics": [block_statistics(signs, size) for size in sizes],
        "descriptive_hurst_fit": estimate_descriptive_hurst(signs, sizes),
        "scope": ("Finite exact arithmetic plus descriptive sample statistics; "
                  "not a proof of RH/GRH, independence, or Brownian convergence."),
    }


def parse_sizes(raw: str) -> list[int]:
    try:
        sizes = [int(part.strip()) for part in raw.split(",") if part.strip()]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("block sizes must be comma-separated integers") from exc
    if not sizes or any(size <= 0 for size in sizes):
        raise argparse.ArgumentTypeError("block sizes must be positive")
    return sizes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-max", type=int, default=100_000)
    parser.add_argument("--block-sizes", type=parse_sizes, default=[8, 16, 32, 64, 128])
    parser.add_argument("--json", action="store_true", help="emit JSON (default output is also JSON)")
    args = parser.parse_args()
    print(json.dumps(audit(args.n_max, args.block_sizes), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
