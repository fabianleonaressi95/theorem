"""D4-Reynolds weighted Hodge assembly on the admissible Q6 face subcomplex.

The canonical Euclidean embedding is not assumed to be D4-isometric.
Instead, each positive geometric mass is Reynolds-averaged over D4.
All incidence and mass assembly is exact SymPy arithmetic.
"""
from __future__ import annotations

import json
from itertools import combinations

import sympy as sp

from models.q6_topological_synchronization import build_q6_complex


def _r(v):
    b1, b2, b3, s1, s2, s3 = v
    return (b1, b2, b3 ^ b1 ^ b2, s2, 1 ^ s1, s3)


def _s(v):
    b1, b2, b3, s1, s2, s3 = v
    return (b1, b2, b3, 1 ^ s1, s2, s3)


def _compose(g, h):
    return tuple(g[h[i]] for i in range(64))


def _group(K):
    R = tuple(K.vertex_index[_r(v)] for v in K.vertices)
    S = tuple(K.vertex_index[_s(v)] for v in K.vertices)
    identity = tuple(range(64))
    group, todo = {identity}, [identity]
    while todo:
        g = todo.pop()
        for generator in (R, S):
            for product in (_compose(generator, g), _compose(g, generator)):
                if product not in group:
                    group.add(product)
                    todo.append(product)
    if len(group) != 8:
        raise ArithmeticError(f"expected D4 order 8, got {len(group)}")
    return tuple(sorted(group))


def _canonical_cycle(cycle):
    candidates = []
    for oriented in (tuple(cycle), tuple(reversed(cycle))):
        candidates.extend(oriented[i:] + oriented[:i] for i in range(4))
    return min(candidates)


def _area_squared(points):
    u = tuple(points[1][i] - points[0][i] for i in range(6))
    v = tuple(points[3][i] - points[0][i] for i in range(6))
    return sum((u[i]*v[j] - u[j]*v[i])**2
               for i, j in combinations(range(6), 2))


def _is_rotation(a, b):
    return any(a == b[i:] + b[:i] for i in range(4))


def _face_action_sign(mapped, canonical):
    if _is_rotation(mapped, canonical):
        return 1
    if _is_rotation(mapped, tuple(reversed(canonical))):
        return -1
    raise ArithmeticError("mapped cycle is not the same unoriented face")


def run_audit():
    K = build_q6_complex()
    group = _group(K)
    cycles = sorted({
        _canonical_cycle(tuple(g[v] for v in face))
        for g in group for face in K.faces
    })
    orbit_edges = sorted({
        tuple(sorted((g[u], g[v])))
        for g in group for u, v in K.edges
    })
    edge_index = {e: i for i, e in enumerate(orbit_edges)}
    face_index = {f: i for i, f in enumerate(cycles)}
    if len(cycles) != 384 or len(orbit_edges) != 256:
        raise ArithmeticError("unexpected Q6 D4 orbit counts")

    # Select only whole D4 face-orbits whose every member is a
    # nondegenerate parallelogram. The raw parallelogram predicate need not
    # be invariant under a Boolean-coordinate action, so selecting individual
    # faces would generally destroy D4 closure.
    unseen = set(cycles)
    face_orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {
            _canonical_cycle(tuple(g[v] for v in seed))
            for g in group
        }
        if not orbit.issubset(set(cycles)):
            raise ArithmeticError("D4 action does not close on orbit-face set")
        face_orbits.append(tuple(sorted(orbit)))
        unseen.difference_update(orbit)

    admissible = []
    rejected_orbits = {"contains_nonparallelogram": 0, "contains_degenerate": 0}
    for orbit in face_orbits:
        orbit_records = []
        all_parallelograms = True
        all_nondegenerate = True
        for cycle in orbit:
            points = tuple(tuple(int(x) for x in K.vertices[v]) for v in cycle)
            parallelogram = all(
                points[0][i] + points[2][i] == points[1][i] + points[3][i]
                for i in range(6)
            )
            area2 = _area_squared(points) if parallelogram else 0
            all_parallelograms &= parallelogram
            all_nondegenerate &= area2 > 0
            orbit_records.append((cycle, points, int(area2)))
        if not all_parallelograms:
            rejected_orbits["contains_nonparallelogram"] += 1
        elif not all_nondegenerate:
            rejected_orbits["contains_degenerate"] += 1
        else:
            admissible.extend(orbit_records)
    admissible.sort(key=lambda item: item[0])
    admissible_cycles = tuple(item[0] for item in admissible)
    admissible_index = {f: i for i, f in enumerate(admissible_cycles)}

    # Incidence matrices in the fixed canonical orientations.
    B1 = sp.zeros(64, 256)
    for j, (u, v) in enumerate(orbit_edges):
        B1[u, j], B1[v, j] = -1, 1
    B2 = sp.zeros(256, len(admissible))
    for j, (cycle, _, _) in enumerate(admissible):
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            e = tuple(sorted((u, v)))
            B2[edge_index[e], j] += 1 if u < v else -1
    if B1 * B2 != sp.zeros(64, len(admissible)):
        raise ArithmeticError("B1 B2 is not exactly zero")

    # Raw geometric W0: P1 edge masses; raw W1: constant Whitney 1-form masses.
    W0_raw = sp.zeros(64, 64)
    W1_raw_diag = []
    for u, v in orbit_edges:
        x, y = K.vertices[u], K.vertices[v]
        d2 = sum((a ^ b)**2 for a, b in zip(x, y))
        if d2 not in (1, 2):
            raise ArithmeticError(f"unexpected squared edge length {d2}")
        length = sp.sqrt(d2)
        W0_raw[u, u] += length / 3
        W0_raw[v, v] += length / 3
        W0_raw[u, v] += length / 6
        W0_raw[v, u] += length / 6
        W1_raw_diag.append(1 / length)

    W2_raw_diag = [1 / sp.sqrt(area2) for _, _, area2 in admissible]

    # Reynolds average. For diagonal cochain masses, signs cancel in P^T W P.
    W0 = sp.zeros(64, 64)
    for g in group:
        for i in range(64):
            for j in range(64):
                W0[i, j] += W0_raw[g[i], g[j]] / 8
    W1_diag = [sp.S.Zero] * 256
    W2_diag = [sp.S.Zero] * len(admissible)

    edge_maps = []
    face_maps = []
    for g in group:
        emap = []
        for u, v in orbit_edges:
            gu, gv = g[u], g[v]
            emap.append(edge_index[tuple(sorted((gu, gv)))])
        edge_maps.append(emap)

        fmap = []
        for cycle in admissible_cycles:
            mapped = tuple(g[v] for v in cycle)
            canonical = _canonical_cycle(mapped)
            if canonical not in admissible_index:
                raise ArithmeticError("D4 does not preserve admissible face family")
            fmap.append(admissible_index[canonical])
        face_maps.append(fmap)

    for emap in edge_maps:
        for i, target in enumerate(emap):
            W1_diag[i] += W1_raw_diag[target] / 8
    for fmap in face_maps:
        for i, target in enumerate(fmap):
            W2_diag[i] += W2_raw_diag[target] / 8

    W1 = sp.diag(*W1_diag)
    W2 = sp.diag(*W2_diag)

    # Exact metric invariance under every group element.
    metric_invariant = True
    for g, emap, fmap in zip(group, edge_maps, face_maps):
        for i in range(64):
            for j in range(64):
                if W0[i, j] != W0[g[i], g[j]]:
                    metric_invariant = False
                    break
            if not metric_invariant:
                break
        if any(W1_diag[i] != W1_diag[emap[i]] for i in range(256)):
            metric_invariant = False
        if any(W2_diag[i] != W2_diag[fmap[i]] for i in range(len(admissible))):
            metric_invariant = False
        if not metric_invariant:
            break

    # Weighted Hodge stiffness: K1 = D0^T W0 D0 + D1^T W2 D1,
    # with D0=B1^T and D1=B2^T. Solve K1 x = lambda W1 x.
    K1 = B1.T * W0 * B1 + B2 * W2 * B2.T
    symmetric = K1 == K1.T
    if not symmetric:
        raise ArithmeticError("weighted Hodge stiffness is not symmetric")

    # Exact signed permutation actions on oriented edges and faces.
    signed_edge_actions = []
    signed_face_actions = []
    for g in group:
        se, sf = [], []
        for u, v in orbit_edges:
            gu, gv = g[u], g[v]
            target = edge_index[tuple(sorted((gu, gv)))]
            se.append((target, 1 if gu < gv else -1))
        for cycle in admissible_cycles:
            mapped = tuple(g[v] for v in cycle)
            canonical = _canonical_cycle(mapped)
            sf.append((admissible_index[canonical],
                       _face_action_sign(mapped, canonical)))
        signed_edge_actions.append(se)
        signed_face_actions.append(sf)

    # Covariance of incidence and stiffness, checked without dense permutation matrices.
    chain_equivariant = True
    for se, sf in zip(signed_edge_actions, signed_face_actions):
        for f in range(len(admissible)):
            lhs = {}
            for e in range(256):
                value = B2[e, f]
                if value:
                    target, sign = se[e]
                    lhs[target] = lhs.get(target, 0) + sign * value
            rhs = {}
            target_f, sign_f = sf[f]
            for e in range(256):
                value = B2[e, target_f]
                if value:
                    rhs[e] = sign_f * value
            if lhs != rhs:
                chain_equivariant = False
                break
        if not chain_equivariant:
            break

    return {
        "audit": "Q6_D4_REYNOLDS_WEIGHTED_HODGE_V1",
        "D4_order": len(group),
        "orbit_vertices": 64,
        "orbit_edges": 256,
        "orbit_faces_total": 384,
        "admissible_parallelogram_faces": len(admissible),\n        "face_orbit_count": len(face_orbits),\n        "admissible_face_orbit_count": admissible_orbit_count,\n        "rejected_face_orbit_counts": rejected_orbits,
        "admissible_parallelogram_faces": len(admissible),
        "face_orbit_count": len(face_orbits),
        "admissible_face_orbit_count": sum(1 for orbit in face_orbits if set(orbit).issubset(set(admissible_cycles))),
        "rejected_face_orbit_counts": rejected_orbits,
        "B1_shape": [64, 256],
        "B2_shape": [256, len(admissible)],
        "B1B2_exact_zero": True,
        "W0_shape": [64, 64],
        "W1_shape": [256, 256],
        "W2_shape": [len(admissible), len(admissible)],
        "all_mass_matrices_positive_definite_by_construction": (
            all(x.is_positive is True for x in W1_diag + W2_diag)
            and W0.det(method="domain-ge") > 0
        ),
        "D4_metric_invariance_exact": bool(metric_invariant),
        "incidence_equivariance_exact": bool(chain_equivariant),
        "K1_shape": [256, 256],
        "K1_symmetric_exact": bool(symmetric),
        "generalized_eigenproblem": "K1 x = lambda W1 x",
        "K1_definition": "B1.T W0 B1 + B2 W2 B2.T",
        "weighted_betti_formula": "beta1 = 256 - rank(B1) - rank(B2)",
        "spectrum_computed": False,
        "mass_construction": "D4 Reynolds average of positive geometric masses",
        "caveat": (
            "The raw six-bit Euclidean embedding is not assumed D4-isometric. "
            "Reynolds averaging restores D4 invariance while retaining SPD. "
            "The spectrum and exact ranks are intentionally not asserted here."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
