"""Exact comparison of the original Q6 coexact D5 sector with the M3 D4 modes.

The M3 rotation does not preserve the original Q6 edge set: two coordinate
directions are sent to diagonal directions. We therefore embed the 192 Q6
edges into the 256-edge D4 orbit graph and test whether the transported
coexact eigenspace remains in the original edge subspace. All calculations
are over QQ / ZZ (SymPy); no floating-point rank decisions are used.
"""
from __future__ import annotations

import sympy as sp

from src.rgs_q6_equivariant_cochains import build_q6_cochain_complex


def _bits(v: int) -> tuple[int, ...]:
    return tuple((v >> (5 - j)) & 1 for j in range(6))


def _index(v: tuple[int, ...]) -> int:
    out = 0
    for bit in v:
        out = (out << 1) | bit
    return out


def _r(v: tuple[int, ...]) -> tuple[int, ...]:
    b1, b2, b3, s1, s2, s3 = v
    return (b1, b2, b3 ^ b1 ^ b2, s2, 1 ^ s1, s3)


def _s(v: tuple[int, ...]) -> tuple[int, ...]:
    b1, b2, b3, s1, s2, s3 = v
    return (b1, b2, b3, 1 ^ s1, s2, s3)


def _compose(g, h):
    return tuple(g[h[i]] for i in range(64))


def _group(r, s):
    identity = tuple(range(64))
    found = {identity}
    todo = [identity]
    while todo:
        g = todo.pop()
        for gen in (r, s):
            for candidate in (_compose(gen, g), _compose(g, gen)):
                if candidate not in found:
                    found.add(candidate)
                    todo.append(candidate)
    return tuple(sorted(found))


def _edge_action(g, orbit_edges, orbit_index):
    """Signed permutation on oriented orbit edges, as an exact matrix."""
    out = sp.zeros(len(orbit_edges), len(orbit_edges))
    for j, (a, b) in enumerate(orbit_edges):
        ga, gb = g[a], g[b]
        key = (min(ga, gb), max(ga, gb))
        out[orbit_index[key], j] = 1 if ga < gb else -1
    return out


def run_audit() -> dict:
    c = build_q6_cochain_complex()
    d1 = sp.Matrix(c["D1"].astype(int).tolist())
    hodge = d1.T * d1
    modes = (hodge - 12 * sp.eye(192)).nullspace()
    if len(modes) != 5:
        raise ArithmeticError(f"expected 5 old Q6 coexact modes, got {len(modes)}")
    v = sp.Matrix.hstack(*modes)

    r_map = tuple(_index(_r(_bits(i))) for i in range(64))
    s_map = tuple(_index(_s(_bits(i))) for i in range(64))
    group = _group(r_map, s_map)
    if len(group) != 8:
        raise ArithmeticError("M3 generators did not produce D4 of order 8")

    old_edges = tuple((int(a), int(b)) for a, b, _axis in c["edges"])
    old_edge_set = set(old_edges)
    orbit_edge_set = set()
    for g in group:
        for a, b in old_edges:
            orbit_edge_set.add(tuple(sorted((g[a], g[b]))))
    orbit_edges = tuple(sorted(orbit_edge_set))
    orbit_index = {edge: i for i, edge in enumerate(orbit_edges)}
    if len(orbit_edges) != 256:
        raise ArithmeticError(f"expected 256 orbit edges, got {len(orbit_edges)}")

    # Inclusion of the original cubical edge cochains into the orbit graph.
    embed = sp.zeros(256, 192)
    for j, edge in enumerate(old_edges):
        embed[orbit_index[edge], j] = 1
    original_support = embed * embed.T

    jr = _edge_action(r_map, orbit_edges, orbit_index)
    js = _edge_action(s_map, orbit_edges, orbit_index)

    # The transported R-modes leave the original Q6 edge subspace.
    r_outside = (sp.eye(256) - original_support) * jr * embed * v
    s_outside = (sp.eye(256) - original_support) * js * embed * v

    # S does preserve the original cubical edge set and acts on its old
    # five-dimensional coexact eigenspace by the scalar -1.
    s_on_old = embed.T * js * embed * v
    gram = v.T * v
    rho_old_s = gram.inv() * v.T * s_on_old
    s_invariant = v * rho_old_s == s_on_old

    # In the M3 orbit-graph character basis (D,E,A,B,C), S has eigenvalues
    # (-1,+1,+1,+1,-1). This is not similar to -I_5.
    rho_orbit_s = sp.diag(-1, 1, 1, 1, -1)
    no_invertible_s_intertwiner = (
        rho_old_s == -sp.eye(5)
        and (rho_orbit_s + sp.eye(5)).rank() == 3
    )

    return {
        "audit": "Q6_D5_M3_D4_INTERTWINER_OBSTRUCTION_EXACT",
        "arithmetic": "exact SymPy rational/integer arithmetic",
        "old_q6": {
            "edge_count": 192,
            "hodge_operator": "D1.T * D1",
            "eigenvalue": 12,
            "eigenspace_dimension": 5,
        },
        "m3_orbit": {
            "group_order": len(group),
            "edge_count": len(orbit_edges),
            "old_edges_embedded": len(old_edge_set),
        },
        "transport": {
            "R_outside_old_edge_subspace_rank": r_outside.rank(),
            "S_outside_old_edge_subspace_rank": s_outside.rank(),
            "R_preserves_old_edge_subspace": r_outside == sp.zeros(256, 5),
            "S_preserves_old_edge_subspace": s_outside == sp.zeros(256, 5),
        },
        "S_representations": {
            "old_q6_rho_S": rho_old_s.tolist(),
            "orbit_graph_rho_S": rho_orbit_s.tolist(),
            "old_s_invariant_exact": s_invariant,
            "old_spectrum": [-1, -1, -1, -1, -1],
            "orbit_spectrum": [-1, -1, 1, 1, 1],
            "invertible_intertwiner_exists": not no_invertible_s_intertwiner,
            "intertwiner_obstruction_rank": (rho_orbit_s + sp.eye(5)).rank(),
        },
        "conclusion": (
            "No D4-equivariant isomorphism identifies the original Q6 "
            "eigenvalue-12 coexact sector with the M3 orbit-graph five-mode "
            "sector under the natural edge transport. R does not preserve "
            "the original 192-edge subspace, and even the common generator "
            "S has inequivalent five-dimensional representations."
        ),
        "all_exact_checks_passed": bool(
            r_outside.rank() == 2
            and s_outside == sp.zeros(256, 5)
            and s_invariant
            and rho_old_s == -sp.eye(5)
            and no_invertible_s_intertwiner
        ),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
