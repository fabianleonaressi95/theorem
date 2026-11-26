#!/usr/bin/env python3
"""Consolidate the existing Q6/C60 equivariance audits without recomputing them.

This script validates the archived JSON outputs from the three source audits.
It deliberately does not infer a new group action, construct an intertwiner,
or compare spectra. Run from the repository root.
"""
import argparse
import json
from pathlib import Path

SOURCES = {
    "proxy": Path("audits/Q6_Oh_face_fibre_equivariance.json"),
    "c60": Path("audits/Q6_C60_T_h_character_comparison.json"),
    "tangent": Path("audits/Q6_tangent_188D_reconstruction.json"),
}

def load(path):
    if not path.exists():
        raise FileNotFoundError(f"Required audit output missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))

def build():
    proxy, c60, tangent = (load(p) for p in SOURCES.values())

    checks = {
        "proxy_Oh_order_48": proxy["coordinate_signed_permutation_group_order"] == 48,
        "proxy_only_16_graph_automorphisms": proxy["Q6_adjacency_automorphisms_in_coordinate_group"] == 16,
        "proxy_32_antipodal_pairs": proxy["antipodal_pairs_count"] == 32,
        "proxy_character_mismatch": proxy["T_h_characters_equal"] is False,
        "actual_C60_32_faces": c60["C60_face_count"] == 32,
        "actual_C60_12_pentagons_20_hexagons": c60["C60_face_size_counts"] == {"5": 12, "6": 20},
        "actual_C60_fibre_dimension_64": c60["C60_fibre_dimension"] == 64,
        "actual_C60_character_mismatch": c60["equivalent_T_h_representations"] is False,
        "spectral_comparison_not_authorized": c60["spectral_comparison_authorized"] is False,
        "tangent_188D_reconstructed": tangent["dimensions"]["tangent_dimension"] == 188,
        "tangent_group_order_16": tangent["geometry_and_Q6_compatible_subgroup_order"] == 16,
        "tangent_group_closure": tangent["group_closure_failures"] == 0,
    }
    if not all(checks.values()):
        failed = [k for k, v in checks.items() if not v]
        raise AssertionError("Consolidation checks failed: " + ", ".join(failed))

    return {
        "classification": "consolidation of existing numerical/geometric audits; no new numerical result",
        "source_reports": {k: str(v) for k, v in SOURCES.items()},
        "state_order": proxy["canonical_state_order"],
        "coordinate_Oh": {
            "order": proxy["coordinate_signed_permutation_group_order"],
            "Q6_adjacency_automorphisms": proxy["Q6_adjacency_automorphisms_in_coordinate_group"],
            "not_a_full_Q6_graph_action": True,
        },
        "antipodal_proxy": {
            "pairs": proxy["antipodal_pairs_count"],
            "character_equivalence_under_Th": proxy["T_h_characters_equal"],
            "status": "rejected proxy; its normals are antipodal point directions, not actual C60 face normals",
        },
        "actual_C60_face_bundle": {
            "faces": c60["C60_face_count"],
            "face_sizes": c60["C60_face_size_counts"],
            "dimension": c60["C60_fibre_dimension"],
            "Q6_character_multiset_on_A4": c60["Q6_A4_character_multiset"],
            "C60_character_multiset_on_A4": c60["C60_A4_fibre_character_multiset"],
            "equivalent_under_Th": c60["equivalent_T_h_representations"],
            "obstruction": "Eight order-three elements have characters 4 (Q6) and -2 (C60); no invertible intertwiner exists for these representations.",
            "spectral_comparison_authorized": c60["spectral_comparison_authorized"],
        },
        "tangent_188D": {
            "ambient_dimension": tangent["dimensions"]["ambient_dimension"],
            "tangent_dimension": tangent["dimensions"]["tangent_dimension"],
            "row_semantics": tangent["coordinate_semantics"],
            "compatible_group_order": tangent["geometry_and_Q6_compatible_subgroup_order"],
            "closure_failures": tangent["group_closure_failures"],
            "operator_covariance": tangent["operator_covariance"],
        },
        "checks": checks,
        "overall_conclusion": "The proposed Q6-to-actual-C60 face-tangent representation equivalence fails the Th character test. The 188D action is reconstructed for the 16-element common geometry/Q6 subgroup, but archived K0, P_G and T_transport are not covariant under that full subgroup. Do not compare their spectra with a C60 operator as if an equivariant identification had been established.",
        "open_items": [
            "Recover and document the independent geometric provenance of the 32 C60 face normals and the precise face-to-state candidate map, if a different map is proposed.",
            "If a smaller common subgroup is scientifically motivated, state it explicitly and recompute its character decomposition; do not silently weaken Th.",
            "Any spectral comparison requires a separately justified operator intertwiner or a clearly labelled non-equivariant comparison.",
        ],
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="audits/Q6_C60_EQUIVARIANCE_CONSOLIDATED_2026-11-26.json")
    args = ap.parse_args()
    report = build()
    target = Path(args.out)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
