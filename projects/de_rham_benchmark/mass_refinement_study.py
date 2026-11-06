#!/usr/bin/env python3
"""Refinement study for legacy DEC, top-corrected DEC and consistent FEEC."""
import argparse
import json
import numpy as np
from compare_mass_matrices import run


def study(dim, levels, amplitude=0.0, nq=5, nqf=4):
    rows = []
    for N in levels:
        result = run(dim, N, amplitude=amplitude, nq=nq, nqf=nqf)
        row = {"N": N, "h": result["h"],
               "min_det_jac": result["geometry"]["min_det_jac"],
               "max_det_jac": result["geometry"]["max_det_jac"],
               "degrees": {}}
        for k in (dim - 1, dim):
            row["degrees"][str(k)] = {
                "legacy_DEC": result["DEC_legacy_diagonal"][k]["lambda_min_positive"],
                "top_corrected_DEC": result["DEC_integral_cochain_top_corrected"][k]["lambda_min_positive"],
                "consistent_FEEC": result["FEEC_consistent"][k]["lambda_min_positive"],
            }
        rows.append(row)
    exponents = {}
    for k in (dim - 1, dim):
        exponents[str(k)] = {}
        for method in ("legacy_DEC", "top_corrected_DEC", "consistent_FEEC"):
            x = np.log([r["h"] for r in rows])
            y = np.log([r["degrees"][str(k)][method] for r in rows])
            exponents[str(k)][method] = float(np.polyfit(x, y, 1)[0])
    return {
        "dimension": dim, "levels": levels, "amplitude": amplitude,
        "rows": rows, "empirical_loglog_exponents": exponents,
        "warning": "Finite-range slopes are descriptive, not asymptotic proofs.",
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--dim", type=int, choices=(2, 3), required=True)
    p.add_argument("--levels", default="")
    p.add_argument("--amplitude", type=float, default=0.0)
    p.add_argument("--nq", type=int, default=5)
    p.add_argument("--nqf", type=int, default=4)
    p.add_argument("--out", default="")
    a = p.parse_args()
    if a.levels:
        levels = [int(x) for x in a.levels.split(",")]
    else:
        levels = [4, 8, 16] if a.dim == 2 else [2, 3, 4, 5]
    result = study(a.dim, levels, a.amplitude, a.nq, a.nqf)
    payload = json.dumps(result, indent=2)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(payload + "\n")
    print(payload)
