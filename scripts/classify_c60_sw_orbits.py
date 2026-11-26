#!/usr/bin/env python3
"""Classify C60 SW_5|6 moves by postgraph isomorphism and Ih symmetry.

The symmetry action is applied to the dual edge being flipped, not to an
arbitrarily labelled direct-graph reconstruction. This avoids dependence on
the arbitrary ordering used when assigning carbon labels to the two new dual
triangles.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import networkx as nx

from audit_c60_stone_wales import (
    c60_ideal, graph_from_bonds, oriented_faces, incidence, enumerate_switches,
)


def graph_isomorphism_classes(graphs: list[nx.Graph]) -> list[list[int]]:
    classes: list[list[int]] = []
    for i, g in enumerate(graphs):
        for cls in classes:
            if nx.is_isomorphic(g, graphs[cls[0]]):
                cls.append(i)
                break
        else:
            classes.append([i])
    return classes


def dual_edge_orbits(dual: nx.Graph, moves: list[dict]) -> tuple[list[dict], list[list[int]]]:
    """Compute orbits of the actual flipped dual edges under Aut(dual)."""
    automorphisms = list(nx.algorithms.isomorphism.GraphMatcher(dual, dual).isomorphisms_iter())
    move_index = {tuple(sorted(move["dual_edge"])): i for i, move in enumerate(moves)}
    if len(move_index) != len(moves):
        raise ValueError("enumerated dual flip edges are not unique")
    images: list[set[int]] = [set() for _ in moves]
    for i, move in enumerate(moves):
        u, v = move["dual_edge"]
        for permutation in automorphisms:
            target = move_index.get(tuple(sorted((permutation[u], permutation[v]))))
            if target is None:
                raise ValueError("Aut(dual C60) does not preserve the enumerated SW dual-edge set")
            images[i].add(target)

    unseen = set(range(len(moves)))
    orbits: list[list[int]] = []
    while unseen:
        seed = min(unseen)
        orbit = set(images[seed])
        frontier = list(orbit)
        while frontier:
            current = frontier.pop()
            for target in images[current]:
                if target not in orbit:
                    orbit.add(target)
                    frontier.append(target)
        if not orbit <= unseen and not orbit.isdisjoint(set(range(len(moves))) - unseen):
            raise ValueError("overlapping automorphism orbits")
        unseen -= orbit
        orbits.append(sorted(orbit))
    return automorphisms, orbits


def classify() -> dict:
    xyz, bonds = c60_ideal()
    carbon_graph = graph_from_bonds(len(xyz), bonds)
    faces = oriented_faces(carbon_graph)
    moves = enumerate_switches(carbon_graph, faces)
    postgraphs = [move["graph"] for move in moves]

    dual = nx.Graph()
    dual.add_nodes_from(range(len(faces)))
    for incident_faces in incidence(faces).values():
        dual.add_edge(*incident_faces)

    isomorphism_classes = graph_isomorphism_classes(postgraphs)
    automorphisms, orbits = dual_edge_orbits(dual, moves)
    return {
        "status": "exact_finite_graph_classification",
        "starting_carbon_graph": {
            "vertices": carbon_graph.number_of_nodes(),
            "edges": carbon_graph.number_of_edges(),
        },
        "dual_graph": {"vertices": dual.number_of_nodes(), "edges": dual.number_of_edges()},
        "admissible_labelled_SW_5_6_moves": len(moves),
        "dual_graph_automorphism_group_order": len(automorphisms),
        "automorphism_group_interpretation": (
            "The automorphism group of the icosahedral fullerene dual graph; "
            "its order 120 agrees with the full Ih symmetry group."
        ),
        "unlabelled_postgraph_isomorphism_classes": len(isomorphism_classes),
        "isomorphism_class_sizes": sorted([len(group) for group in isomorphism_classes], reverse=True),
        "isomorphism_classes_move_indices_zero_based": isomorphism_classes,
        "Ih_dual_edge_orbit_count": len(orbits),
        "Ih_dual_edge_orbit_sizes": sorted([len(group) for group in orbits], reverse=True),
        "Ih_dual_edge_orbits_move_indices_zero_based": orbits,
        "limitations": [
            "Graph isomorphism and Ih orbits are combinatorial classifications, not atomistic transition-state calculations.",
            "One unlabelled postgraph class does not enumerate all C60 chemical isomers or multi-step SW pathways.",
            "No energy barrier, electronic-density response, or Kathara/Q6 intertwiner is computed."
        ]
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="c60_stone_wales_audit/orbit_classification.json")
    args = parser.parse_args()
    result = classify()
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
