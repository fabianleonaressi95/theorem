#!/usr/bin/env python3
"""Audit the RGS carrier tetrahedron's geometric face fluxes.

The four carrier vertices are inherited from the earlier, explicitly finite
RGS coframe fixture. This script does not identify the tetrahedron with a Q6
subcomplex and does not assign SU(2) spins.
"""
from __future__ import annotations

import json
import sys
from itertools import combinations
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.rgs_seed_64_reconstruction import load_rgs_seed_data  # noqa: E402

VERTEX_IDS = (0, 8, 32, 56)
FACES = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))
TOL = 1.0e-12
EXPECTED_COORD_SHA256 = (
    "6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf"
)


def q6_hamming(a: int, b: int) -> int:
    return int((a ^ b).bit_count())


def build_audit() -> dict:
    seed = load_rgs_seed_data()
    points_all = np.asarray(seed.coordinates, dtype=float)
    points = points_all[list(VERTEX_IDS)].copy()

    if points.shape != (4, 3):
        raise RuntimeError("expected four RGS carrier points in R^3")

    determinant = float(np.linalg.det(np.column_stack((
        points[1] - points[0],
        points[2] - points[0],
        points[3] - points[0],
    ))))
    volume = determinant / 6.0
    if abs(volume) <= TOL:
        raise RuntimeError("selected carrier tetrahedron is degenerate")

    face_records = []
    area_vectors = []
    for face in FACES:
        a, b, c = points[list(face)]
        vector = 0.5 * np.cross(b - a, c - a)
        opposite = next(k for k in range(4) if k not in face)
        if float(np.dot(vector, points[opposite] - a)) > 0.0:
            vector = -vector
        area = float(np.linalg.norm(vector))
        if area <= TOL:
            raise RuntimeError(f"degenerate face {face}")
        normal = vector / area
        area_vectors.append(vector)
        face_records.append({
            "local_face": list(face),
            "carrier_vertex_ids": [VERTEX_IDS[k] for k in face],
            "area": area,
            "outward_unit_normal": normal.tolist(),
            "area_vector": vector.tolist(),
        })

    flux_sum = np.sum(np.asarray(area_vectors), axis=0)
    closure_residual = float(np.linalg.norm(flux_sum))

    edge_records = []
    for i, j in combinations(range(4), 2):
        distance = q6_hamming(VERTEX_IDS[i], VERTEX_IDS[j])
        edge_records.append({
            "local_pair": [i, j],
            "carrier_vertex_pair": [VERTEX_IDS[i], VERTEX_IDS[j]],
            "q6_hamming_distance": distance,
            "is_q6_edge": distance == 1,
            "euclidean_length": float(np.linalg.norm(points[j] - points[i])),
        })

    areas = np.asarray([item["area"] for item in face_records])
    q6_edge_count = sum(item["is_q6_edge"] for item in edge_records)
    q6_edges_bipartite = all(
        (u.bit_count() & 1) != ((u ^ (1 << bit)).bit_count() & 1)
        for u in range(64) for bit in range(6) if (u & (1 << bit)) == 0
    )

    result = {
        "title": "MQ-005 RGS carrier tetrahedron classical face-flux audit",
        "source": "src.rgs_seed_64_reconstruction.load_rgs_seed_data",
        "expected_coordinate_sha256": EXPECTED_COORD_SHA256,
        "selected_carrier_vertex_ids": list(VERTEX_IDS),
        "points": points.tolist(),
        "oriented_volume": volume,
        "faces": face_records,
        "face_area_ratios_to_face_012": (areas / areas[0]).tolist(),
        "outward_area_vector_sum": flux_sum.tolist(),
        "closure_residual_l2": closure_residual,
        "edges": edge_records,
        "q6_induced_edge_count": q6_edge_count,
        "q6_complete_graph_k4": q6_edge_count == 6,
        "q6_graph_bipartite": q6_edges_bipartite,
        "q6_global_k4_obstruction": q6_edges_bipartite,
        "tolerance": TOL,
        "classification": {
            "tetrahedral_area_vector_closure": "exact_general_identity",
            "rgs_seed_instance": "finite_numerical_audit",
            "selected_vertices_form_q6_k4": False,
            "q6_global_k4_obstruction": "exact_bipartite_parity_argument",
            "q6_cellular_identification": "not_established_and_direct_k4_test_fails",
            "su2_spin_assignment": "open_not_assigned",
            "physical_area_scale": "open_not_assigned",
            "coherent_intertwiner": "conditional_future_construction",
            "continuum_or_spinfoam_dynamics": "not_claimed",
        },
    }

    if closure_residual > TOL:
        raise AssertionError(f"flux closure residual {closure_residual} exceeds {TOL}")
    if not q6_edges_bipartite:
        raise AssertionError("Q6 parity bipartition check failed")
    if q6_edge_count != 2:
        raise AssertionError(f"expected exactly two Q6 edges, found {q6_edge_count}")
    if result["q6_complete_graph_k4"]:
        raise AssertionError("selected vertices unexpectedly form a Q6 K4")
    return result


def main() -> None:
    result = build_audit()
    output = ROOT / "results" / "mq005_rgs_tetrahedron_flux.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
