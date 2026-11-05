"""T045: exhaustive exact certificate for the finite 2I representation layer.

This audit strengthens T034's exact identities by making the finite coverage
explicit: all 120 group elements, all 81 character inner products, all
projector pairs on Sym^m for m<=13, and every matrix-unit multiplication
quadruple on the tested finite representations.  It does not claim an
all-degree analytic or continuum theorem.
"""
from __future__ import annotations

from src import t034_binary_icosahedral_representations as T
from src.t032_2i_molien import IRREP_DIMENSIONS, molien_coefficients


def exhaustive_matrix_units(G, reps, U, multiplicities):
    """Check E_ij E_kl = delta_jk E_il for every index quadruple."""
    dim = len(U[0])
    checked = 0
    per_irrep = {}
    for label, mult in multiplicities.items():
        rep = reps[label]
        d = rep.dim
        E = {(i, j): T.matrix_unit(G, rep, i, j, U)
             for i in range(d) for j in range(d)}
        for i in range(d):
            if not T.mat_eq(T.mat_mul(E[i, i], E[i, i]), E[i, i]):
                raise AssertionError(("diagonal idempotent", label, i))
            if T.mat_trace(E[i, i]) != mult:
                raise AssertionError(("multiplicity trace", label, i, mult))
        for i in range(d):
            for j in range(d):
                for k in range(d):
                    for ell in range(d):
                        lhs = T.mat_mul(E[i, j], E[k, ell])
                        rhs = E[i, ell] if j == k else T.mat_zero(dim)
                        if not T.mat_eq(lhs, rhs):
                            raise AssertionError(("matrix-unit law", label,
                                                  i, j, k, ell))
                        checked += 1
        # The full matrix-unit family must recover the central isotypic block.
        block = T.mat_zero(dim)
        for i in range(d):
            block = T.mat_add(block, E[i, i])
        chi = T.characters_from_matrices(G, reps)[0][label]
        P = T.central_projector(G, chi, T.ordered_classes(G), d, U)
        if not T.mat_eq(block, P):
            raise AssertionError(("matrix units do not sum to central projector", label))
        per_irrep[label] = {"dimension": d, "multiplicity": mult,
                            "quadruples": d ** 4}
    return {"quadruples_checked": checked, "irreps": per_irrep}


def run_certificate(max_projector_degree: int = 13):
    G = T.build_group()
    group_report = T.verify_group(G)
    reps = T.build_representations(G)

    hom = {}
    weighted = {}
    for label in T.LABELS:
        hom[label] = T.verify_homomorphism(G, reps[label].matrices)
        if reps[label].weights:
            weighted[label] = T.verify_weighted_unitarity(G, reps[label])
            if not weighted[label]:
                raise AssertionError(("weighted unitarity", label))

    table, classes = T.characters_from_matrices(G, reps)
    character_report = T.verify_character_table(table)
    schur_entries = T.verify_schur_orthogonality(G, reps)
    if schur_entries != 120 * 120:
        raise AssertionError("incomplete Schur coefficient audit")

    projector_reports = []
    for m in range(max_projector_degree + 1):
        projector_reports.append(T.verify_projectors_on_sym(
            G, table, classes, m, full_orthogonality=True))

    # Exhaustive matrix-unit multiplication, not seeded sampling.
    matrix_unit_reports = []
    for m in range(8):
        U = T.symmetric_power_rep(G, m)
        mult = {label: molien_coefficients(label, m)[m]
                for label in T.LABELS
                if molien_coefficients(label, m)[m] > 0}
        matrix_unit_reports.append({
            "representation": f"Sym^{m}",
            **exhaustive_matrix_units(G, reps, U, mult),
        })

    U2 = T.block_diagonal([T.symmetric_power_rep(G, 2),
                           T.symmetric_power_rep(G, 10)])
    matrix_unit_reports.append({
        "representation": "Sym^2 direct-sum Sym^10",
        **exhaustive_matrix_units(G, reps, U2, {"3": 2}),
    })

    # Molien is explicitly the multiplicity of rho in Sym^m(V), where
    # V is the defining two-dimensional SU(2) representation.
    molien = T.verify_molien_exact(table)
    return {
        "status": "PASS",
        "group_order": group_report["cardinality"],
        "irreducibles": {k: IRREP_DIMENSIONS[k] for k in T.LABELS},
        "homomorphism_cayley_edges_per_irrep": {
            k: hom[k]["edges_checked"] for k in T.LABELS},
        "weighted_unitarity_all_120_elements": weighted,
        "character_orthogonality": character_report,
        "matrix_coefficient_schur_entries": schur_entries,
        "projectors_all_pairs_degrees_0_to_max": projector_reports,
        "matrix_units_exhaustive": matrix_unit_reports,
        "molien_representation": "V = defining 2-dimensional representation; Sym^m(V)",
        "molien_exact_numerator_identity": molien,
        "sum_squared_dimensions": sum(d*d for d in IRREP_DIMENSIONS.values()),
    }


if __name__ == "__main__":
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-projector-degree", type=int, default=13)
    args = parser.parse_args()
    print(json.dumps(run_certificate(args.max_projector_degree), indent=2))
