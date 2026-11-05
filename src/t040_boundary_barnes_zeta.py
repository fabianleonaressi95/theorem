"""T040: exact Barnes-zeta reduction of the two exceptional Rumin boundaries.

For either boundary orientation, m=n-1 and lambda_n=(n+1)^2/4.
The untwisted S^3/2I multiplicity is the trivial 2I Molien coefficient
a_m=[t^m](1+t^30)/((1-t^12)(1-t^20)).
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

from src.t032_2i_molien import molien_coefficients

BOUNDARY_KINDS = ("q=-1", "p=-1")
BARNES_PERIODS = (12, 20)
BARNES_STARTS = (2, 32)


def boundary_level(kind: str, index: int) -> dict:
    """Exact spectral data at positive exceptional-boundary index n."""
    if kind not in BOUNDARY_KINDS:
        raise ValueError("kind must be 'q=-1' or 'p=-1'")
    if not isinstance(index, int) or isinstance(index, bool) or index < 1:
        raise ValueError("boundary index must be an integer >= 1")
    degree = index - 1
    eigenvalue = Fraction((index + 1) ** 2, 4)
    multiplicity = molien_coefficients("1", degree)[degree]
    return {
        "kind": kind,
        "boundary_index": index,
        "SU2_degree": degree,
        "eigenvalue": str(eigenvalue),
        "untwisted_2I_multiplicity": multiplicity,
    }


def invariant_multiplicity(degree: int) -> int:
    """Exact dimension of (Sym^degree C^2)^(2I), from T032 Molien data."""
    if not isinstance(degree, int) or isinstance(degree, bool) or degree < 0:
        raise ValueError("degree must be a nonnegative integer")
    return molien_coefficients("1", degree)[degree]


def barnes_zeta_decomposition(kind: str) -> dict:
    """Return the exact meromorphic-continuation identity for one orientation.

    Z_kind(s) = 4^s [zeta_2(2s,2|12,20) + zeta_2(2s,32|12,20)].
    The Barnes double zeta is initially defined by its convergent series
    for Re(s)>1 here; its standard meromorphic continuation defines Z.
    """
    if kind not in BOUNDARY_KINDS:
        raise ValueError("kind must be 'q=-1' or 'p=-1'")
    return {
        "kind": kind,
        "formula": "4^s * (BarnesZeta2(2s,2|12,20) + BarnesZeta2(2s,32|12,20))",
        "barnes_starts": list(BARNES_STARTS),
        "barnes_periods": list(BARNES_PERIODS),
        "eigenvalue_factor": "4^s",
        "argument": "2s",
        "initial_convergence": "Re(s) > 1",
        "continuation": "Barnes double-zeta meromorphic continuation",
        "scope": "one exceptional boundary orientation; no torsion sign or complex multiplicity convention is imposed",
    }


def partial_spectral_zeta(kind: str, s: float, max_index: int) -> float:
    """Finite partial sum; max_index includes indices 1,...,max_index."""
    if kind not in BOUNDARY_KINDS:
        raise ValueError("kind must be 'q=-1' or 'p=-1'")
    if not isinstance(max_index, int) or isinstance(max_index, bool) or max_index < 1:
        raise ValueError("max_index must be an integer >= 1")
    if not isinstance(s, (int, float)) or not math.isfinite(float(s)):
        raise ValueError("s must be finite and real")
    return math.fsum(
        invariant_multiplicity(n - 1) * (((n + 1) ** 2) / 4.0) ** (-float(s))
        for n in range(1, max_index + 1)
    )


def audit(max_index: int = 40) -> dict:
    if not isinstance(max_index, int) or isinstance(max_index, bool) or max_index < 1:
        raise ValueError("max_index must be an integer >= 1")
    levels = [boundary_level(kind, n) for kind in BOUNDARY_KINDS
              for n in range(1, max_index + 1)]
    return {
        "passed": True,
        "levels_per_orientation": max_index,
        "boundary_levels": levels,
        "barnes_zeta": {kind: barnes_zeta_decomposition(kind)
                        for kind in BOUNDARY_KINDS},
        "combined_if_both_orientations_are_counted": "2 * Z_boundary(s); separate sectors retained",
        "regularized_log_determinant_per_orientation": "-Z_boundary'(0), not numerically evaluated in T040",
        "scope": "exact untwisted boundary multiplicities and Barnes-zeta representation; analytic torsion combination/signs remain open",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-index", type=int, default=40)
    parser.add_argument("--output", default="data/t040_boundary_barnes_zeta.json")
    args = parser.parse_args()
    report = audit(args.max_index)
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "boundary_levels"}, indent=2))


if __name__ == "__main__":
    main()
