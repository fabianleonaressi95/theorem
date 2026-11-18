"""Exact audit of the core Pellis/GSR fine-structure expression."""
from __future__ import annotations
import json
import sympy as sp


def audit() -> dict:
    phi = (1 + sp.sqrt(5)) / 2
    t_surface = 360 / phi**2
    t_volume = -2 / phi**3
    t_wave = 1 / (3 * phi)**5
    value = sp.simplify(t_surface + t_volume + t_wave)
    exact = sp.Rational(264373, 486) - sp.Rational(88447, 486) * sp.sqrt(5)
    if sp.simplify(value - exact) != 0:
        raise AssertionError("exact Q(sqrt(5)) expression mismatch")

    codata = sp.Rational("137.035999177")
    codata_u = sp.Rational("0.000000021")
    ge_2023 = sp.Rational("137.035999166")
    ge_2023_u = sp.Rational("0.000000015")
    return {
        "passed": True,
        "formula": "360*phi^(-2) - 2*phi^(-3) + (3*phi)^(-5)",
        "exact_value": "(264373 - 88447*sqrt(5))/486",
        "decimal_value": str(sp.N(value, 40)),
        "terms": {
            "360_phi_minus_2": str(sp.N(t_surface, 30)),
            "-2_phi_minus_3": str(sp.N(t_volume, 30)),
            "(3_phi)_minus_5": str(sp.N(t_wave, 30)),
        },
        "comparison": {
            "codata_2022_inverse": str(codata),
            "codata_2022_uncertainty": str(codata_u),
            "difference_2022": str(sp.N(value-codata, 30)),
            "relative_difference_2022": str(sp.N(abs(value-codata)/codata, 20)),
            "within_2022_uncertainty": bool(abs(value-codata) <= codata_u),
            "electron_g_2023_inverse": str(ge_2023),
            "electron_g_2023_uncertainty": str(ge_2023_u),
            "difference_2023": str(sp.N(value-ge_2023, 30)),
            "relative_difference_2023": str(sp.N(abs(value-ge_2023)/ge_2023, 20)),
            "within_2023_uncertainty": bool(abs(value-ge_2023) <= ge_2023_u),
        },
        "source_text_checks": {
            "claimed_absolute_error_2022": "1.12344e-8",
            "computed_absolute_error_2022": str(sp.N(abs(value-codata), 30)),
            "claimed_relative_error_2022": "8.2e-11",
            "computed_relative_error_2022": str(sp.N(abs(value-codata)/codata, 20)),
            "claimed_(3phi)^5": "approximately 6158.64",
            "computed_(3phi)^5": str(sp.N((3*phi)**5, 30)),
            "computed_(3phi)^(-5)": str(sp.N(1/(3*phi)**5, 30)),
        },
        "scope": "Exact algebra and arithmetic comparisons only; no physical derivation.",
    }


def main() -> None:
    print(json.dumps(audit(), indent=2))


if __name__ == "__main__":
    main()
