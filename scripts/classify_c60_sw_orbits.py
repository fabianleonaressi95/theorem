#!/usr/bin/env python3
"""Classify the 30 admissible C60 SW_5|6 postgraphs under graph isomorphism and Ih.

This is an exact finite-graph audit. It does not infer a transition-state path or
chemical energy ordering. The Ih action is represented by Aut(G_C60), whose
order is checked rather than assumed.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import networkx as nx

from audit_c60_stone_wales import c60_ideal, graph_from_bonds, oriented_faces, enumerate_switches


def edge_key(g: nx.Graph) -> frozenset[tuple[int, int]]:
    return frozenset(tuple(sorted((int(u), int(v)))) for u, v in g.edges())


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


def automorphism_orbits(base: nx.Graph, graphs: list[nx.Graph]) -> tuple[list[dict[int, int]], list[list[int]]]:
    autos = list(nx.algorithms.isomorphism.GraphMatcher(base, base).isomorphisms_iter())
    by_key = {edge_key(g): i for i, g in enumerate(graphs)}
    if len(by_key) != len(graphs):
        raise ValueError("candidate postgraphs are not uniquely labelled")
    images: list[set[int]] = [set() for _ in graphs]
    for i, g in enumerate(graphs):
        for p in autos:
            transformed = frozenset(tuple(sorted((p[u], p[v]))) for u, v in g.edges())
            j = by_key.get(transformed)
            if j is None:
                raise ValueError("Aut(C60) action does not preserve the enumerated candidate set")
            images[i].add(j)
    unseen = set(range(len(graphs)))
    orbits: list[list[int]] = []
    while unseen:
        seed = min(unseen)
        orbit = set(images[seed])
        frontier = list(orbit)
        while frontier:
            k = frontier.pop()
            for j in images[k]:
                if j not in orbit:
                    orbit.add(j)
                    frontier.append(j)
        if not orbit <= unseen:
            # Existing orbits must be disjoint; overlap means the action data is inconsistent.
            if not orbit.isdisjoint(set(range(len(graphs))) - unseen):
                raise ValueError("overlapping automorphism orbits")
        unseen -= orbit
        orbits.append(sorted(orbit))
    return autos, orbits


def classify() -> dict:
    xyz, bonds = c60_ideal()
    base = graph_from_bonds(len(xyz), bonds)
    faces = oriented_faces(base)
    moves = enumerate_switches(base, faces)
    graphs = [m["graph"] for m in moves]
    classes = graph_isomorphism_classes(graphs)
    autos, orbits = automorphism_orbits(base, graphs)
    return {
        "status": "exact_finite_graph_classification",
        "starting_graph": {"vertices": base.number_of_nodes(), "edges": base.number_of_edges()},
        "admissible_labelled_moves": len(moves),
        "automorphism_group_order": len(autos),
        "automorphism_group_interpretation": "Full graph automorphism group of the ideal truncated-icosahedral C60 cage; identified with Ih only after the group order and fullerene symmetry model are stated.",
        "unlabelled_postgraph_isomorphism_classes": len(classes),
        "isomorphism_class_sizes": sorted([len(c) for c in classes], reverse=True),
        "isomorphism_classes_move_indices_zero_based": classes,
        "Ih_orbit_count": len(orbits),
        "Ih_orbit_sizes": sorted([len(o) for o in orbits], reverse=True),
        "Ih_orbits_move_indices_zero_based": orbits,
        "limitations": [
            "Graph automorphism equivalence is a combinatorial symmetry statement, not an atomistic transition-state calculation.",
            "Unlabelled graph isomorphism classes are not a complete chemical isomer enumeration.",
            "The automorphism action is on the labelled post-switch carbon graph; it does not classify multi-step SW pathways."
        ]
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="c60_stone_wales_audit/orbit_classification.json")
    args = ap.parse_args()
    result = classify()
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
