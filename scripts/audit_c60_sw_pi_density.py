#!/usr/bin/env python3
"""C60 pyracylene SW: orthogonal pi tight-binding population and Q6 parity audit.

This is an explicitly limited one-orbital Hückel model on the carbon graph.
It computes site populations from the occupied pi density matrix; it is not
DFT and does not construct a continuous real-space electron density.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import networkx as nx
import numpy as np

from audit_c60_stone_wales import c60_ideal, graph_from_bonds, oriented_faces, enumerate_switches


def pi_density(graph: nx.Graph, electrons: int = 60, degeneracy_tol: float = 1e-8):
    """Return H=-A spectrum and a spin-summed, shell-balanced pi density matrix."""
    A = nx.to_numpy_array(graph, nodelist=range(graph.number_of_nodes()), dtype=float)
    eigenvalues, vectors = np.linalg.eigh(-A)  # hopping t=1; energy unit is t
    remaining = electrons / 2.0
    occupations = np.zeros(len(eigenvalues), dtype=float)
    i = 0
    while i < len(eigenvalues) and remaining > 1e-12:
        j = i + 1
        while j < len(eigenvalues) and abs(eigenvalues[j] - eigenvalues[i]) <= degeneracy_tol:
            j += 1
        fill = min(1.0, remaining / (j - i))
        occupations[i:j] = fill
        remaining -= fill * (j - i)
        i = j
    if remaining > 1e-9:
        raise ValueError("Not enough pi orbitals for requested electron count")
    P = 2.0 * (vectors * occupations) @ vectors.T
    return eigenvalues, occupations, P, np.diag(P)


def population_covariance(coords: np.ndarray, populations: np.ndarray):
    weights = np.array(populations, dtype=float, copy=True)
    total = float(weights.sum())
    if not np.isclose(total, 60.0, atol=1e-8):
        raise ValueError(f"pi population must sum to 60, got {total}")
    weights /= total
    center = (weights[:, None] * coords).sum(axis=0)
    centered = coords - center
    Q = (centered * weights[:, None]).T @ centered
    eigenvalues = np.linalg.eigvalsh(Q)
    anisotropy = float((eigenvalues[-1] - eigenvalues[0]) /
                       (eigenvalues[-1] + eigenvalues[0]))
    return {
        "center": center.tolist(),
        "tensor": Q.tolist(),
        "eigenvalues": eigenvalues.tolist(),
        "anisotropy": anisotropy,
        "population_min": float(populations.min()),
        "population_max": float(populations.max()),
        "population_std": float(populations.std()),
        "population_sum": total,
    }


def model_metrics(graph: nx.Graph, coords: np.ndarray):
    eig, occ, P, populations = pi_density(graph)
    occupied = np.flatnonzero(occ > 1e-10)
    unoccupied = np.flatnonzero(occ < 1.0 - 1e-10)
    gap = (float(eig[unoccupied[0]] - eig[occupied[-1]])
           if len(occupied) and len(unoccupied) else None)
    return {
        "electron_count_trace_P": float(np.trace(P)),
        "H_minus_adjacency_hopping_t_1": {
            "HOMO_eigenvalue_over_t": float(eig[occupied[-1]]) if len(occupied) else None,
            "LUMO_eigenvalue_over_t": float(eig[unoccupied[0]]) if len(unoccupied) else None,
            "HOMO_LUMO_gap_over_t": gap,
            "partially_occupied_orbitals": int(np.sum((occ > 1e-10) & (occ < 1.0 - 1e-10))),
        },
        "site_population_covariance": population_covariance(coords, populations),
    }


def automorphism_group_report(graph: nx.Graph):
    automorphisms = list(nx.algorithms.isomorphism.GraphMatcher(graph, graph).isomorphisms_iter())
    identity = {v: v for v in graph.nodes}
    orders = []
    for p in automorphisms:
        q = dict(identity)
        order = 0
        while True:
            q = {v: p[q[v]] for v in graph.nodes}
            order += 1
            if q == identity:
                break
            if order > 24:
                raise RuntimeError("Unexpected automorphism order")
        orders.append(order)
    nonidentity_orders = sorted(o for o in orders if o != 1)
    return {
        "order": len(automorphisms),
        "element_orders": sorted(orders),
        "is_klein_four_V4": len(automorphisms) == 4 and nonidentity_orders == [2, 2, 2],
    }


def q6_one_skeleton():
    graph = nx.Graph()
    graph.add_nodes_from(range(64))
    for v in range(64):
        for axis in range(6):
            w = v ^ (1 << axis)
            if v < w:
                graph.add_edge(v, w)
    return graph


def audit():
    coords, bonds = c60_ideal()
    c60 = graph_from_bonds(len(coords), bonds)
    c60_faces = oriented_faces(c60)
    moves = enumerate_switches(c60, c60_faces)
    if len(moves) != 30:
        raise RuntimeError(f"Expected 30 labelled pyracylene moves, got {len(moves)}")

    before = model_metrics(c60, coords)
    post_metrics = []
    postgraphs = []
    for move in moves:
        post = move["graph"]
        postgraphs.append(post)
        post_metrics.append(model_metrics(post, coords))

    # All 30 are one Ih orbit; compare the numerical model invariant across labels.
    gaps = [m["H_minus_adjacency_hopping_t_1"]["HOMO_LUMO_gap_over_t"] for m in post_metrics]
    anisotropies = [m["site_population_covariance"]["anisotropy"] for m in post_metrics]
    spread_gap = float(max(gaps) - min(gaps))
    spread_anisotropy = float(max(anisotropies) - min(anisotropies))

    same_postgraph_class = all(nx.is_isomorphic(moves[0]["graph"], move["graph"]) for move in moves[1:])
    if not same_postgraph_class:
        raise RuntimeError("The 30 labelled SW moves do not form one unlabelled postgraph class")
    post_group = automorphism_group_report(moves[0]["graph"])
    q6 = q6_one_skeleton()
    c60_has_odd_face = any(len(face) % 2 for face in c60_faces)
    q6_bipartite = nx.is_bipartite(q6)
    direct_graph_homomorphism_impossible = bool(c60_has_odd_face and q6_bipartite)

    return {
        "classification": "finite_graph_exact_checks_plus_one_orbital_Huckel_numerics",
        "model": {
            "hamiltonian": "H = -A(C60), uniform nearest-neighbour pi hopping t=1",
            "electrons": 60,
            "spin": "two spin states per spatial orbital",
            "occupation": "fill 30 orbitals; equal fractional occupation within a degenerate shell if needed",
            "density_matrix": "P = 2 U diag(occupation) U^T",
            "observable": "covariance of carbon-site positions weighted by diagonal pi populations P_ii",
            "geometry": "unrelaxed ideal truncated-icosahedron coordinates; same coordinates before and after to isolate graph-connectivity effect",
            "not_included": ["sigma electrons", "overlap matrix", "distance-dependent hopping", "electron-electron interaction", "self-consistent field", "continuous real-space density"],
        },
        "starting_C60": {
            "vertices": c60.number_of_nodes(),
            "edges": c60.number_of_edges(),
            "faces": len(c60_faces),
            "ring_inventory": {"pentagons": sum(len(f) == 5 for f in c60_faces),
                               "hexagons": sum(len(f) == 6 for f in c60_faces)},
            "pi_model": before,
        },
        "SW_5_6": {
            "labelled_moves": len(moves),
            "postgraph_isomorphism_classes": 1 if same_postgraph_class else None,
            "all_30_postgraphs_isomorphic_to_selected": same_postgraph_class,
            "postgraph_automorphism_group": post_group,
            "selected_move": {
                "dual_edge": list(moves[0]["dual_edge"]),
                "opposite_pentagon_faces": list(moves[0]["opposite_pentagon_faces"]),
                "removed_bonds": moves[0]["removed_edges"],
                "added_bonds": moves[0]["added_edges"],
            },
            "selected_postgraph_pi_model": post_metrics[0],
            "all_30_labelled_moves": {
                "HOMO_LUMO_gap_over_t_min": float(min(gaps)),
                "HOMO_LUMO_gap_over_t_max": float(max(gaps)),
                "HOMO_LUMO_gap_over_t_spread": spread_gap,
                "site_population_anisotropy_min": float(min(anisotropies)),
                "site_population_anisotropy_max": float(max(anisotropies)),
                "site_population_anisotropy_spread": spread_anisotropy,
            },
        },
        "Q6_graph_map_obstruction": {
            "Q6_vertices": q6.number_of_nodes(),
            "Q6_edges": q6.number_of_edges(),
            "Q6_is_bipartite": q6_bipartite,
            "C60_contains_pentagonal_odd_cycle": c60_has_odd_face,
            "direct_C60_carbon_graph_to_Q6_1_skeleton_graph_homomorphism_exists": not direct_graph_homomorphism_impossible,
            "proof": (
                "A graph homomorphism sends every source cycle to a closed walk of the same length. "
                "A bipartite graph has no closed odd walk. C60 has pentagonal 5-cycles, whereas Q6 is bipartite; "
                "therefore no edge-preserving vertex map C60 -> Q6 exists."
            ),
            "scope": "This rules out only a direct 1-skeleton graph homomorphism. It does not rule out a cellular chain map that sends edges to multi-edge paths, a subdivision, a face-fibre representation map, or a common-refinement construction.",
        },
        "Q6_C60_prior_results": {
            "pristine_C60_A4_face_tangent_representation": "A4 character mismatch is already recorded; no invertible A4 intertwiner.",
            "pristine_C60_V4_face_tangent_representation": "A V4 representation intertwiner exists, but it is abstract and not a canonical geometric face map.",
            "post_SW_status": "The post-SW graph has a V4 combinatorial automorphism group; identifying its action with the archived Q6 V4 action on a geometrically realized post-SW face-tangent bundle remains open.",
        },
        "limitations": [
            "The Hückel site-population covariance is not a continuous electron-density tensor and is not DFT.",
            "Uniform hopping on the graph isolates connectivity but omits bond-length and orbital-orientation effects.",
            "The post-SW geometry is not relaxed in this calculation.",
            "No transition-state path or activation barrier is computed.",
            "No Stone-Wales/Q6 commuting chain-map square is constructed.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="c60_stone_wales_audit/pi_density_q6_parity.json")
    args = parser.parse_args()
    result = audit()
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
