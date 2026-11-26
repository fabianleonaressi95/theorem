"""Increasing-harmonic Galerkin audit for the golden cumulative Markov operator.

The exact Markov operator is an L2 contraction. Finite empirical-CDF
compressions need not preserve that inequality exactly; the excess over one
in the reported matrix 2-norm is therefore a discretization diagnostic.
"""
from bisect import bisect_right
from math import cos, pi, sin, sqrt
import argparse
import json
import random

import numpy as np

PHI = (1.0 + sqrt(5.0)) / 2.0
LAMBDA = 1.0 / PHI


def fourier_basis(t, h):
    out = [sqrt(2) * cos(2*pi*t), sqrt(2) * sin(2*pi*t), 1.0]
    for k in range(2, h+1):
        out.extend((sqrt(2)*cos(2*pi*k*t), sqrt(2)*sin(2*pi*k*t)))
    return out


def estimate_compression(samples=300000, terms=48, max_harmonic=16, seed=20261124):
    if samples < 1000 or terms < 1 or max_harmonic < 2:
        raise ValueError("invalid audit parameters")
    rng = random.Random(seed)
    powers = [LAMBDA**k for k in range(terms)]
    xs = np.sort(np.asarray([
        sum(w if rng.getrandbits(1) else -w for w in powers)
        for _ in range(samples)
    ], dtype=float))
    inv = 1.0 / samples
    t = (np.arange(samples, dtype=float) + 0.5) * inv
    tm = np.searchsorted(xs, LAMBDA*xs - 1.0, side="right") * inv
    tp = np.searchsorted(xs, LAMBDA*xs + 1.0, side="right") * inv

    def basis(values):
        out = np.empty((samples, 2*max_harmonic+1), dtype=float)
        out[:, 0] = sqrt(2)*np.cos(2*pi*values)
        out[:, 1] = sqrt(2)*np.sin(2*pi*values)
        out[:, 2] = 1.0
        for k in range(2, max_harmonic+1):
            out[:, 2*k-1] = sqrt(2)*np.cos(2*pi*k*values)
            out[:, 2*k] = sqrt(2)*np.sin(2*pi*k*values)
        return out

    source = basis(t)
    target = 0.5 * (basis(tm) + basis(tp))
    return (source.T @ target * inv).tolist()


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def frobenius(a):
    return sqrt(sum(x*x for row in a for x in row))


def power_norms(b, d, c, count=8):
    cur = [r[:] for r in c]
    out = {}
    for n in range(count):
        out[str(n)] = frobenius(matmul(b, cur))
        cur = matmul(d, cur)
    return out


def reduce_matrix(matrix, h):
    dim = 2*h+1
    arr = np.asarray(matrix, dtype=float)[:dim, :dim]
    if arr.shape != (dim, dim):
        raise ValueError("matrix too small")
    active = [0, 1]
    comp = list(range(3, dim))
    a = arr[np.ix_(active, active)]
    b = arr[np.ix_(active, comp)]
    c = arr[np.ix_(comp, active)]
    d = arr[np.ix_(comp, comp)]
    eig = np.linalg.eigvals(d)
    singular = np.linalg.svd(d, compute_uv=False)
    kernels = {}
    power = np.eye(len(comp))
    for n in range(8):
        kernels[str(n)] = float(np.linalg.norm(b @ power @ c, ord="fro"))
        power = power @ d
    return {
        "harmonic_cutoff": h,
        "active_dimension": 2,
        "constant_mode": "removed_exactly",
        "complement_dimension": len(comp),
        "A11": a.tolist(),
        "B": b.tolist(),
        "C": c.tolist(),
        "D": d.tolist(),
        "K0": (b @ c).tolist(),
        "K0_frobenius": float(np.linalg.norm(b @ c, ord="fro")),
        "memory_kernel_frobenius": kernels,
        "D_eigenvalues": [[float(z.real), float(z.imag)] for z in eig],
        "D_spectral_radius": float(np.max(np.abs(eig))) if len(eig) else 0.0,
        "D_operator_norm_2": float(singular[0]) if len(singular) else 0.0,
        "empirical_contraction_excess": max(0.0, float(singular[0])-1.0) if len(singular) else 0.0,
        "scope": "finite empirical-CDF Galerkin estimate; not exact L2",
    }


def audit(samples=300000, terms=48, cutoffs=(2,3,4,6,8,10,12,16), seed=20261124):
    matrix = estimate_compression(samples, terms, max(cutoffs), seed)
    return {
        "model": "increasing-harmonic finite Galerkin audit",
        "samples": samples,
        "bernoulli_terms": terms,
        "seed": seed,
        "cutoffs": list(cutoffs),
        "cdf_series_tail_bound": LAMBDA**terms/(1.0-LAMBDA),
        "full_compression_dimension": len(matrix),
        "records": [reduce_matrix(matrix, h) for h in cutoffs],
        "exact_operator_fact": "The invariant golden Markov operator is an L2 contraction by Jensen's inequality and invariance of Lebesgue measure.",
        "warning": "Finite empirical-CDF compression can violate the exact contraction bound slightly; excess above one is a numerical discretization diagnostic. Finite sections do not prove H-to-infinity convergence.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=300000)
    parser.add_argument("--terms", type=int, default=48)
    parser.add_argument("--cutoffs", type=int, nargs="+", default=[2,3,4,6,8,10,12,16])
    parser.add_argument("--seed", type=int, default=20261124)
    parser.add_argument("--output", default="results/tsmr_i_harmonic_convergence.json")
    args = parser.parse_args()
    result = audit(args.samples, args.terms, tuple(args.cutoffs), args.seed)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps(result, indent=2))
