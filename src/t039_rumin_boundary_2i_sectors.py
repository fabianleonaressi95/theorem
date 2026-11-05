"""T039: exact Rumin boundary spectrum and binary-icosahedral multiplicities.

Kitaoka's n=1 boundary weights are (q,-p)=(-1,-p) and (q,1).
Their SU(2) highest-weight degree is m=q+p, hence p-1 or q-1.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path


def boundary_data(kind: str, index: int):
    import sympy as sp
    if kind not in ("q=-1", "p=-1"):
        raise ValueError("kind must be 'q=-1' or 'p=-1'")
    if not isinstance(index, int) or isinstance(index, bool) or index < 1:
        raise ValueError("boundary index must be an integer >= 1")
    m = index - 1
    return {
        "kind": kind,
        "boundary_index": index,
        "highest_weight_U2": "(-1,-p)" if kind == "q=-1" else "(q,1)",
        "SU2_symmetric_power_degree": m,
        "SU2_module_dimension": m + 1,
        "D_adjoint_D_eigenvalue": str(sp.Rational((index + 1) ** 2, 4)),
    }


def audit_boundary_sector(kind: str, index: int):
    """Return exact 2I isotypic multiplicities using T032 Molien coefficients."""
    result = boundary_data(kind, index)
    from src.t032_2i_molien import IRREP_DIMENSIONS, molien_coefficients
    m = result["SU2_symmetric_power_degree"]
    multiplicities = {label: int(molien_coefficients(label, m)[m])
                      for label in IRREP_DIMENSIONS}
    dimensions = {label: IRREP_DIMENSIONS[label] * multiplicities[label]
                  for label in IRREP_DIMENSIONS}
    total = sum(dimensions.values())
    if total != m + 1:
        raise AssertionError(f"2I decomposition dimension {total} != {m + 1}")
    result.update({
        "2I_irrep_multiplicities": multiplicities,
        "2I_isotypic_dimensions": dimensions,
        "2I_dimension_sum": total,
        "trivial_2I_multiplicity": multiplicities["1"],
        "quotient_invariant_boundary_multiplicity": multiplicities["1"],
        "method": "exact T032 Molien coefficients; sum(dim(rho)*b_m,rho)=m+1",
        "geometric_identification": "Kitaoka n=1 Proposition 1.1 cases VI/VII: m=q+p=index-1",
    })
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("q=-1", "p=-1"), required=True)
    parser.add_argument("--index", type=int, required=True)
    parser.add_argument("--output", default="data/t039_rumin_boundary_2i_audit.json")
    args = parser.parse_args()
    report = audit_boundary_sector(args.kind, args.index)
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
