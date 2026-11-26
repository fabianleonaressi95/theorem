#!/usr/bin/env python3
"""Finite Q6 audit for Walsh charge laws and the homogeneous thermal RC model."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from typing import Sequence

N, BITS = 64, 6

def walsh_character(vertex: int, subset: int) -> int:
    if not 0 <= vertex < N or not 0 <= subset < N:
        raise ValueError("vertex and subset must lie in {0,...,63}")
    return -1 if (vertex & subset).bit_count() % 2 else 1

def walsh_transform(charges: Sequence[float]) -> list[float]:
    if len(charges) != N:
        raise ValueError("exactly 64 charge values are required")
    return [sum(float(charges[h]) * walsh_character(h, s)
                for h in range(N)) / N for s in range(N)]

def walsh_inverse(coefficients: Sequence[float]) -> list[float]:
    if len(coefficients) != N:
        raise ValueError("exactly 64 Walsh coefficients are required")
    return [sum(float(coefficients[s]) * walsh_character(h, s)
                for s in range(N)) for h in range(N)]

def hypercube_distance(h: int, hp: int) -> int:
    if not (0 <= h < N and 0 <= hp < N):
        raise ValueError("hexagram labels must lie in {0,...,63}")
    return (h ^ hp).bit_count()

def rc_charge_correlation(h: int, hp: int, tau: float, conductance: float,
                          capacitance: float, temperature: float,
                          boltzmann: float = 1.0) -> float:
    """Projected homogeneous thermal RC covariance at lag tau."""
    if tau < 0 or conductance <= 0 or capacitance <= 0 or temperature < 0:
        raise ValueError("require tau>=0, g>0, c>0 and T>=0")
    d = hypercube_distance(h, hp)
    r = math.exp(-2.0 * conductance * tau / capacitance)
    kernel = ((1.0 + r) ** (BITS - d) * (1.0 - r) ** d) / N
    return boltzmann * temperature * capacitance * (kernel - 1.0 / N)

def audit() -> dict[str, object]:
    mult = {str(2*k): math.comb(BITS, k) for k in range(BITS + 1)}
    assert sum(mult.values()) == N
    diag = rc_charge_correlation(0, 0, 0.0, 1.0, 1.0, 1.0)
    off = rc_charge_correlation(0, 1, 0.0, 1.0, 1.0, 1.0)
    assert math.isclose(diag, 63/64) and math.isclose(off, -1/64)
    for tau in (0.0, 0.1, 1.0, 10.0):
        assert abs(sum(rc_charge_correlation(0, hp, tau, 1, 1, 1)
                       for hp in range(N))) < 1e-10
    return {"vertices": N, "walsh_modes": N,
            "laplacian_eigenvalue_multiplicities": mult,
            "charge_law": "not assigned; requires measured or derived 64-vector",
            "symmetry_result": "full Q6 automorphism invariance forces a constant scalar",
            "thermal_RC_model": {"assumptions": "uniform g, C_node=cI, zero mode projected, FDT noise",
                                 "equal_time_diagonal_for_kBTc_1": diag,
                                 "equal_time_off_diagonal_for_kBTc_1": off,
                                 "row_sum_zero": True},
            "status": "PASS"}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--charges", type=Path,
                        help="JSON file containing 64 measured/derived q(h) values")
    args = parser.parse_args()
    result = audit()
    if args.charges is not None:
        charges = json.loads(args.charges.read_text(encoding="utf-8"))
        coeff = walsh_transform(charges)
        rec = walsh_inverse(coeff)
        result["walsh_coefficients"] = coeff
        result["walsh_reconstruction_max_error"] = max(
            abs(float(a)-b) for a, b in zip(charges, rec))
        result["charge_vector_source"] = str(args.charges)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
