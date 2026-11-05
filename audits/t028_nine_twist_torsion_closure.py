#!/usr/bin/env python3
"""T028 end-to-end exact/numerical closure audit for the nine 2I Rumin twists.

Run from the repository root:
  python audits/t028_nine_twist_torsion_closure.py --precision 60 --max-degree 240 --json

Requires SymPy. Imports the existing T022, T023 and T027 audit modules.
It cross-checks their outputs rather than duplicating their derivations.
"""
import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
T022_PATH = ROOT / "bibliography/spin-geometry-quaternionic/RUMIN_2I_T022_EVENTUAL_HURWITZ_AUDIT.py"
T023_PATH = ROOT / "bibliography/spin-geometry-quaternionic/RUMIN_2I_T023_GAMMA_SINE_IDENTITIES.py"
T027_PATH = ROOT / "audits/t027_mckay_molien_bridge.py"
LABELS = ("1", "2", "2'", "3", "3'", "4", "4'", "5", "6")
DIMENSIONS = {"1": 1, "2": 2, "2'": 2, "3": 3, "3'": 3, "4": 4, "4'": 4, "5": 5, "6": 6}
T026_TO_T021 = {"1": "1", "2_s": "2", "3": "3", "4_s": "4'", "5": "5", "6_s": "6", "4": "4", "2'_s": "2'", "3'": "3'"}


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load audit module: " + str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def audit(max_degree=240, precision=60):
    import sympy as sp
    if max_degree < 60:
        raise ValueError("max_degree must be at least 60")
    if precision < 40:
        raise ValueError("precision must be at least 40 digits")
    t022 = load_module("t022_audit", T022_PATH)
    t023 = load_module("t023_audit", T023_PATH)
    t027 = load_module("t027_audit", T027_PATH)

    # Stage 1: affine-E8 recurrence equals all nine Molien coefficient series.
    mckay = t027.audit(max_degree)
    assert mckay["all_assertions_passed"]
    assert mckay["coefficient_equalities_checked"] == 9 * (max_degree + 1)

    # Stage 2: T022 and T023 must agree on exact polynomial/preperiod/tails.
    period_data = {}
    for label in LABELS:
        p22, finite22, tails22, _ = t022.eventual_data(label)
        p23, finite23, tails23 = t023.residue_tail_data(label)
        assert sp.expand(p22.as_expr() - p23.as_expr()) == 0, label
        assert finite22 == finite23, (label, finite22, finite23)
        expected_tails22 = [(N, d, N % 60) for N, d in tails23]
        assert tails22 == expected_tails22, (label, tails22, expected_tails22)
        period_data[label] = {
            "period_polynomial_degree": int(p22.degree()),
            "finite_preperiod_terms": len(finite22),
            "eventual_residue_tails": len(tails22),
            "exact_data_match": True,
        }

    # Stage 3: exact Gamma/sine reductions versus independent Hurwitz/Gamma.
    exact = t023.audit()
    numerical = t022.audit(precision=precision)
    torsion_data = {}
    for label in LABELS:
        exact_value = sp.sympify(exact[label]["torsion"])
        computed = sp.N(sp.exp(t022.log_torsion(label)), precision)
        benchmark = sp.N(exact_value, precision)
        residual = sp.N(abs(computed - benchmark), precision)
        assert residual < sp.Float(10) ** (-(precision // 2)), (label, residual)
        reported = sp.Float(numerical[label]["torsion"], precision)
        assert abs(reported - computed) < sp.Float(10) ** (-(precision // 2))
        torsion_data[label] = {
            "dimension": DIMENSIONS[label],
            "exact_gamma_sine_value": str(exact_value),
            "hurwitz_gamma_value": str(computed),
            "absolute_residual": str(residual),
            "passed": True,
        }

    assert sum(d*d for d in DIMENSIONS.values()) == 120
    return {
        "audit": "T028 end-to-end nine-twist Rumin torsion closure",
        "max_mckay_degree": max_degree,
        "mckay_molien_equalities": mckay["coefficient_equalities_checked"],
        "gamma_precision_digits": precision,
        "irreducible_twists_checked": len(LABELS),
        "sum_squared_irrep_dimensions": sum(d*d for d in DIMENSIONS.values()),
        "T026_to_T021_label_map": T026_TO_T021,
        "stage_1_mckay_equals_molien": True,
        "stage_2_T022_equals_T023_period_decompositions": period_data,
        "stage_3_gamma_sine_vs_hurwitz_gamma": torsion_data,
        "all_assertions_passed": True,
        "scope": [
            "T024 already proves the 3D Kitaoka/Rumin-Seshadri operator and torsion convention match under its stated hypotheses.",
            "T028 cross-audits the nine character twists and their exact/analytic-continuation pipeline.",
            "No new spectral theorem or higher-dimensional extension is claimed.",
            "The trivial-twist determinant-line cohomology normalization remains the separate T021 calculation."
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=240)
    parser.add_argument("--precision", type=int, default=60)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = audit(args.max_degree, args.precision)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(report["audit"])
        print("McKay/Molien coefficient equalities:", report["mckay_molien_equalities"])
        print("T022/T023 exact period decompositions: PASS")
        print("all nine Gamma/sine vs Hurwitz/Gamma values: PASS")
        print("precision:", report["gamma_precision_digits"], "digits")
        print("all assertions passed")


if __name__ == "__main__":
    main()
