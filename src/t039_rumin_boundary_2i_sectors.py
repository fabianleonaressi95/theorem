"""T039: exact boundary eigenvalues and conditional 2I harmonic restriction."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any


def boundary_eigenvalue(kind: str, index: int):
    """Exact D*D boundary eigenvalue as a SymPy Rational."""
    import sympy as sp
    if kind not in ("q=-1", "p=-1"):
        raise ValueError("kind must be 'q=-1' or 'p=-1'")
    if not isinstance(index, int) or isinstance(index, bool) or index < 1:
        raise ValueError("boundary index must be an integer >= 1")
    return sp.Rational((index + 1) ** 2, 4)


def audit_boundary_sector(kind: str, index: int,
                          representation_degree: int | None = None) -> dict[str, Any]:
    """A supplied m is conditional; it is never inferred from the boundary index."""
    eigenvalue = boundary_eigenvalue(kind, index)
    result = {
        "kind": kind, "boundary_index": index,
        "D_adjoint_D_eigenvalue": str(eigenvalue),
        "representation_identification":
            "not supplied; geometric boundary-to-Sym^m identification remains open",
    }
    if representation_degree is None:
        return result
    if (not isinstance(representation_degree, int)
            or isinstance(representation_degree, bool) or representation_degree < 0):
        raise ValueError("representation_degree must be an integer >= 0")
    from src.t037_rumin_harmonic_multiplicities import decompose_degree
    from src.t036_2i_irreducible_models import build_all_models
    group, chars, _, models = build_all_models()
    decomposition = decompose_degree(representation_degree, group, chars, models)
    irreps = {
        label: {"dimension": int(entry["dimension"]),
                "multiplicity": int(entry["Molien_multiplicity"]),
                "isotypic_dimension": int(entry["isotypic_dimension"])}
        for label, entry in decomposition.items()
    }
    total = sum(item["isotypic_dimension"] for item in irreps.values())
    ambient = representation_degree + 1
    if total != ambient:
        raise AssertionError(f"2I decomposition dimension {total} != {ambient}")
    result.update({
        "representation_degree": representation_degree,
        "representation_dimension": ambient,
        "2I_irreducible_multiplicities": irreps,
        "2I_dimension_sum": total,
        "representation_identification":
            "conditional audit of supplied Sym^m(C^2)|_2I; not proof this is the geometric boundary module",
    })
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("q=-1", "p=-1"), required=True)
    parser.add_argument("--index", type=int, required=True)
    parser.add_argument("--representation-degree", type=int, default=None)
    parser.add_argument("--output", default="data/t039_rumin_boundary_2i_audit.json")
    args = parser.parse_args()
    report = audit_boundary_sector(args.kind, args.index, args.representation_degree)
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
