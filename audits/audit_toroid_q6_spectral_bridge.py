"""Metric torus-grid versus Q6: a controlled D4 spectral comparison."""
from __future__ import annotations

import json
from itertools import product

import numpy as np
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


def _d4_actions(vertices, index):
    R = tuple(index[_r(v)] for v in vertices)
    S = tuple(index[_s(v)] for v in vertices)
    identity = tuple(range(64))
    found, todo = {identity}, [identity]
    while todo:
        g = todo.pop()
        for generator in (R, S):
            for candidate in (_compose(generator, g), _compose(g, generator)):
                if candidate not in found:
                    found.add(candidate)
                    todo.append(candidate)
    if len(found) != 8:
        raise ArithmeticError(f"expected D4 of order 8, found {len(found)}")
    elements = []
    for k in range(4):
        Rk = identity
        for _ in range(k):
            Rk = _compose(R, Rk)
        for reflection in (0, 1):
            perm = Rk if reflection == 0 else _compose(Rk, S)
            elements.append((perm, k, reflection))
    if len({p for p, _, _ in elements}) != 8 or {p for p, _, _ in elements} != found:
        raise ArithmeticError("D4 normal forms are not distinct or complete")
    return elements


def _permutation_matrix(perm):
    P = np.zeros((64, 64), dtype=float)
    for source, target in enumerate(perm):
        P[target, source] = 1.0
    return P


def _generalized_eigenvalues(K, M):
    L = np.linalg.cholesky(M)
    left = np.linalg.solve(L, K)
    C = np.linalg.solve(L, left.T).T
    C = 0.5 * (C + C.T)
    return np.linalg.eigvalsh(C)


def _build_torus_grid(R, r, n=8):
    if not (R > r > 0):
        raise ValueError("the regular ring torus requires R > r > 0")
    if n != 8:
        raise ValueError("the six-bit/Q6 comparison fixes n=8")
    vertices = tuple(product((0, 1), repeat=6))
    index = {v: i for i, v in enumerate(vertices)}

    def ij(v):
        return (4 * v[0] + 2 * v[1] + v[2],
                4 * v[3] + 2 * v[4] + v[5])

    def encode(i, j):
        return ((i >> 2) & 1, (i >> 1) & 1, i & 1,
                (j >> 2) & 1, (j >> 1) & 1, j & 1)

    ntheta = nphi = 2.0 * np.pi / n
    edges, edge_kind = [], []
    for v in vertices:
        i, j = ij(v)
        edges.append((index[v], index[encode((i + 1) % n, j)]))
        edge_kind.append(("theta", i, j))
        edges.append((index[v], index[encode(i, (j + 1) % n)]))
        edge_kind.append(("phi", i, j))

    faces = []
    for v in vertices:
        i, j = ij(v)
        faces.append((
            index[encode(i, j)],
            index[encode((i + 1) % n, j)],
            index[encode((i + 1) % n, (j + 1) % n)],
            index[encode(i, (j + 1) % n)],
        ))

    B1 = np.zeros((64, len(edges)), dtype=np.int64)
    for e, (u, v) in enumerate(edges):
        B1[u, e], B1[v, e] = -1, 1
    edge_index = {tuple(sorted(e)): k for k, e in enumerate(edges)}
    B2 = np.zeros((len(edges), len(faces)), dtype=np.int64)
    for f, cycle in enumerate(faces):
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            e = edge_index[tuple(sorted((u, v)))]
            B2[e, f] += 1 if edges[e] == (u, v) else -1
    if not np.array_equal(B1 @ B2, np.zeros((64, len(faces)), dtype=np.int64)):
        raise ArithmeticError("torus grid does not satisfy B1 B2 = 0")

    W0 = np.zeros((64, 64), dtype=float)
    lengths = []
    for kind, i, j in edge_kind:
        if kind == "theta":
            length = 2.0 * r * np.sin(ntheta / 2.0)
        else:
            length = 2.0 * (R + r * np.cos(ntheta * i)) * np.sin(nphi / 2.0)
        if length <= 0:
            raise ArithmeticError("nonpositive torus edge length")
        lengths.append(length)

    for (u, v), length in zip(edges, lengths):
        W0[u, u] += length / 3.0
        W0[v, v] += length / 3.0
        W0[u, v] += length / 6.0
        W0[v, u] += length / 6.0

    W1 = np.diag(1.0 / np.asarray(lengths))
    areas = []
    for cycle in faces:
        i, _ = ij(vertices[cycle[0]])
        area = r * nphi * (R * ntheta + r * (
            np.sin(ntheta * (i + 1)) - np.sin(ntheta * i)
        ))
        if area <= 0:
            raise ArithmeticError("nonpositive torus face area")
        areas.append(area)
    W2 = np.diag(1.0 / np.asarray(areas))

    K0 = B1 @ W1 @ B1.T
    rank_B1 = int(sp.Matrix(B1).rank())
    rank_B2 = int(sp.Matrix(B2).rank())
    betti1 = len(edges) - rank_B1 - rank_B2
    betti2 = len(faces) - rank_B2
    return {
        "B1": B1, "B2": B2, "W0": W0, "W1": W1, "W2": W2,
        "K0": K0, "rank_B1": rank_B1, "rank_B2": rank_B2,
        "betti1": betti1, "betti2": betti2, "vertices": vertices,
    }


def _sector_projectors(actions):
    chars = {
        "A1": lambda k, s: 1.0,
        "A2": lambda k, s: -1.0 if s else 1.0,
        "B1": lambda k, s: -1.0 if k % 2 else 1.0,
        "B2": lambda k, s: -1.0 if (k + s) % 2 else 1.0,
    }
    matrices = [(k, s, _permutation_matrix(perm))
                for perm, k, s in actions]
    projectors = {
        name: sum(character(k, s) * matrix
                  for k, s, matrix in matrices) / 8.0
        for name, character in chars.items()
    }
    projectors["E"] = np.eye(64) - sum(projectors.values())
    return projectors


def _reynolds(A, matrices):
    return sum(P.T @ A @ P for P in matrices) / len(matrices)


def run_audit(R=2.0, r=1.0):
    torus = _build_torus_grid(float(R), float(r), 8)
    actions = _d4_actions(
        torus["vertices"], {v: i for i, v in enumerate(torus["vertices"])}
    )
    Pmats = [_permutation_matrix(perm) for perm, _, _ in actions]

    q6 = build_q6_complex()
    Lq = q6.B1 @ q6.B1.T
    Lt = torus["K0"]
    torus_comm = max(float(np.linalg.norm(P.T @ Lt @ P - Lt, ord="fro"))
                     for P in Pmats)
    q6_comm = max(float(np.linalg.norm(P.T @ Lq @ P - Lq, ord="fro"))
                  for P in Pmats)

    Lq_bar = _reynolds(Lq, Pmats)
    Lt_bar = _reynolds(Lt, Pmats)
    Mt_bar = _reynolds(torus["W0"], Pmats)
    projectors = _sector_projectors(actions)
    sector_dimensions = {
        name: int(round(float(np.trace(projector))))
        for name, projector in projectors.items()
    }
    projector_residuals = {
        name: float(np.linalg.norm(projector @ projector - projector, ord="fro"))
        for name, projector in projectors.items()
    }

    return {
        "audit": "TORUS_Q6_D4_SPECTRAL_BRIDGE_V1",
        "parameters": {"R": float(R), "r": float(r), "lambda": float(R / r)},
        "torus_cellulation": {
            "vertices": 64, "edges": 128, "faces": 64,
            "B1_shape": list(torus["B1"].shape),
            "B2_shape": list(torus["B2"].shape),
            "B1B2_exact_zero": True,
            "rank_B1_exact": torus["rank_B1"],
            "rank_B2_exact": torus["rank_B2"],
            "betti1_exact": torus["betti1"],
            "betti2_exact": torus["betti2"],
        },
        "q6_graph": {"vertices": 64, "edges": 192, "degree": 6},
        "D4": {
            "order": len(actions),
            "vertex_representation_sector_dimensions": sector_dimensions,
            "projector_idempotence_residuals": projector_residuals,
            "torus_raw_operator_commutator_frobenius_max": torus_comm,
            "q6_raw_operator_commutator_frobenius_max": q6_comm,
        },
        "spectra": {
            "torus_raw_generalized_eigenvalues":
                _generalized_eigenvalues(Lt, torus["W0"]).tolist(),
            "q6_raw_graph_eigenvalues": np.linalg.eigvalsh(Lq).tolist(),
            "torus_reynolds_generalized_eigenvalues":
                _generalized_eigenvalues(Lt_bar, Mt_bar).tolist(),
            "q6_reynolds_graph_eigenvalues":
                np.linalg.eigvalsh(0.5 * (Lq_bar + Lq_bar.T)).tolist(),
        },
        "interpretation": {
            "raw_spectral_match_claimed": False,
            "intertwiner_claimed": False,
            "chain_map_between_torus_and_q6_claimed": False,
            "reynolds_spectra_are_geometric_invariants": False,
            "caveat": (
                "The torus and Q6 have different edge/face sets. They share a "
                "64-vertex labeling, not a cellular chain complex. D4 commutators "
                "are measured on raw operators; Reynolds averages are only "
                "symmetry-restored comparison operators."
            ),
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
