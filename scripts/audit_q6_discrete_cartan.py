#!/usr/bin/env python3
"""Gauge-covariant discrete Cartan audit on the I Ching/Kirchhoff Q6 carrier.

The 64 vertices are six-bit hexagrams; edges flip one bit; 240 square
plaquettes are the 2-cells. RGS site coframes define edge coframe increments
and the existing shortest-radial-rotation links define an SO(3) connection.
Face torsion is the developed boundary closure defect; face curvature is the
ordered link holonomy.

This is a finite spatial discrete Cartan construction, not yet a Lorentzian
4D Cartan field, a teleparallel solution, or a continuum theorem. NumPy only.
"""
from __future__ import annotations

import hashlib
import json
from itertools import combinations

import numpy as np

ELL2 = 7.035514834154695
C0 = 43.96495130838031
EXPECTED_X_SHA256 = "6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf"
EXPECTED_EDGE_SHA256 = "da7854ca655577b629dc508208918326fde1d50563485f953ea0fdc1b2fb78e8"
I3 = np.eye(3)


def sha256_array(a: np.ndarray, dtype: str) -> str:
    return hashlib.sha256(np.ascontiguousarray(a, dtype=dtype).tobytes()).hexdigest()


def reconstruct_seed() -> tuple[np.ndarray, np.ndarray]:
    """Rebuild the archived 64-site seed and oriented Hamming-1 Q6 edges."""
    v = {
        "cube_inner": 0.47863916086470326,
        "small_1": 0.48042984818593559,
        "small_2": 0.48230704367200045,
        "cube_outer": 0.95183963342906408,
        "large_1": 1.5073116806169751,
        "large_2": 1.9039106736116611,
    }
    reps = [
        (v["cube_inner"],) * 3,
        (v["large_1"], v["large_1"], v["small_1"]),
        (v["large_1"], v["small_1"], v["large_1"]),
        (v["small_1"], v["large_1"], v["large_1"]),
        (v["large_2"], v["small_2"], v["small_2"]),
        (v["small_2"], v["large_2"], v["small_2"]),
        (v["small_2"], v["small_2"], v["large_2"]),
        (v["cube_outer"],) * 3,
    ]
    signs = [(sx, sy, sz) for sx in (-1.0, 1.0)
             for sy in (-1.0, 1.0) for sz in (-1.0, 1.0)]
    X = np.asarray([[s[0]*p[0], s[1]*p[1], s[2]*p[2]]
                    for p in reps for s in signs], dtype=np.float64)
    edges = np.asarray([
        (g, g | (1 << axis), axis)
        for g in range(64) for axis in range(6)
        if not ((g >> axis) & 1)
    ], dtype=np.int64)
    if X.shape != (64, 3) or edges.shape != (192, 3):
        raise AssertionError("unexpected Q6 seed dimensions")
    if sha256_array(X, "<f8") != EXPECTED_X_SHA256:
        raise AssertionError("RGS seed SHA-256 mismatch")
    if sha256_array(edges, "<i8") != EXPECTED_EDGE_SHA256:
        raise AssertionError("Q6 edge SHA-256 mismatch")
    return X, edges


def spatial_coframes(X: np.ndarray) -> np.ndarray:
    """Archived local covariance prescription and principal SPD square root."""
    E = np.empty((len(X), 3, 3), dtype=np.float64)
    for i, x in enumerate(X):
        delta = X - x
        weights = np.exp(-np.einsum("ij,ij->i", delta, delta) / ELL2)
        weights[i] = 0.0
        C = np.einsum("i,ia,ib->ab", weights, delta, delta) / C0
        lam, U = np.linalg.eigh(C)
        if lam[0] <= 0.0:
            raise ValueError(f"non-positive covariance at vertex {i}")
        E[i] = (U * np.sqrt(lam)) @ U.T
    return E


def skew(v: np.ndarray) -> np.ndarray:
    x, y, z = v
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def minimal_rotation(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    a, b = a / np.linalg.norm(a), b / np.linalg.norm(b)
    c = float(np.clip(a @ b, -1.0, 1.0))
    v = np.cross(a, b)
    s = float(np.linalg.norm(v))
    if s < 1e-14:
        if c > 0.0:
            return I3.copy()
        ref = np.array([1.0, 0.0, 0.0]) if abs(a[0]) < 0.8 else np.array([0.0, 1.0, 0.0])
        axis = np.cross(a, ref)
        axis /= np.linalg.norm(axis)
        return 2.0 * np.outer(axis, axis) - I3
    V = skew(v / s)
    return I3 + V * s + (V @ V) * (1.0 - c)


def q6_squares() -> list[tuple[int, int, int, int]]:
    """All 240 positively oriented coordinate squares, one per lower corner/axis pair."""
    squares = []
    for a, b in combinations(range(6), 2):
        for g in range(64):
            if ((g >> a) & 1) or ((g >> b) & 1):
                continue
            j, l = g | (1 << a), g | (1 << b)
            k = j | (1 << b)
            squares.append((g, j, k, l))
    if len(squares) != 240:
        raise AssertionError("Q6 must have 240 coordinate squares")
    return squares


def random_so3(rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1
    return q


def build_discrete_cartan(X=None, edges=None, E=None, gauge=None) -> dict:
    if X is None or edges is None:
        X0, edges0 = reconstruct_seed()
        X = X0 if X is None else X
        edges = edges0 if edges is None else edges
    if E is None:
        E = spatial_coframes(X)
    edge_index = {(int(g), int(h)): i for i, (g, h, _) in enumerate(edges)}
    links = np.asarray([minimal_rotation(X[g], X[h]) for g, h, _ in edges])
    coframe_edges = np.asarray([E[g] @ (X[h] - X[g]) for g, h, _ in edges])
    if gauge is not None:
        links = np.asarray([gauge[h] @ U @ gauge[g].T
                            for U, (g, h, _) in zip(links, edges)])
        coframe_edges = np.asarray([gauge[g] @ theta
                                    for theta, (g, h, _) in zip(coframe_edges, edges)])

    def oriented_edge(a: int, b: int):
        if a < b:
            idx = edge_index[(a, b)]
            return links[idx], coframe_edges[idx]
        idx = edge_index[(b, a)]
        return links[idx].T, -links[idx] @ coframe_edges[idx]

    torsions, holonomies, curvature_angles = [], [], []
    squares = q6_squares()
    for square in squares:
        P = I3.copy()  # maps base-frame components to the current vertex frame
        torsion = np.zeros(3)
        for a, b in zip(square, square[1:] + square[:1]):
            U, theta = oriented_edge(a, b)
            torsion += P.T @ theta
            P = U @ P
        H = P
        torsions.append(torsion)
        holonomies.append(H)
        cosine = np.clip((np.trace(H) - 1.0) / 2.0, -1.0, 1.0)
        curvature_angles.append(float(np.arccos(cosine)))

    torsions = np.asarray(torsions)
    holonomies = np.asarray(holonomies)
    curvature_angles = np.asarray(curvature_angles)
    return {
        "links": links,
        "coframe_edges": coframe_edges,
        "torsions": torsions,
        "holonomies": holonomies,
        "curvature_angles": curvature_angles,
        "link_orthogonality_max": max(float(np.linalg.norm(U.T @ U - I3)) for U in links),
        "link_determinant_residual_max": max(abs(float(np.linalg.det(U)) - 1.0) for U in links),
        "edge_index": edge_index,
        "edges": edges,
        "squares": squares,
    }


def gauge_covariance_audit(X, edges, E, base):
    rng = np.random.default_rng(20261127)
    gauge = np.asarray([random_so3(rng) for _ in range(64)])
    transformed = build_discrete_cartan(X, edges, E, gauge=gauge)
    t_res, h_res = [], []
    for i, square in enumerate(base["squares"]):
        G = gauge[square[0]]
        t_res.append(float(np.linalg.norm(transformed["torsions"][i] - G @ base["torsions"][i])))
        h_res.append(float(np.linalg.norm(
            transformed["holonomies"][i] - G @ base["holonomies"][i] @ G.T
        )))
    return {
        "deterministic_seed": 20261127,
        "torsion_covariance_max": max(t_res),
        "curvature_conjugation_max": max(h_res),
    }


def summarize(x: np.ndarray) -> dict:
    return {"mean": float(np.mean(x)), "rms": float(np.sqrt(np.mean(x*x))),
            "max": float(np.max(x)), "p95": float(np.quantile(x, 0.95))}


def build_report() -> dict:
    X, edges = reconstruct_seed()
    E = spatial_coframes(X)
    data = build_discrete_cartan(X, edges, E)
    gauge = gauge_covariance_audit(X, edges, E, data)
    torsion_norms = np.linalg.norm(data["torsions"], axis=1)
    return {
        "status": "FINITE_SPATIAL_DISCRETE_CARTAN_CANDIDATE_GAUGE_COVARIANCE_AUDITED",
        "origin": {
            "carrier": "64 six-bit I Ching hexagrams",
            "adjacency": "single-line flip / Hamming distance one",
            "graph": "Q6; 64 vertices, 192 oriented-positive edges, degree 6",
            "faces": "240 coordinate square plaquettes",
            "edge_sha256": EXPECTED_EDGE_SHA256,
            "seed_sha256": EXPECTED_X_SHA256,
        },
        "discrete_geometry": {
            "coframe": "theta_(g->h) = E_g (X_h-X_g), in the source orthonormal frame",
            "connection": "U_(g->h) = minimal SO(3) radial rotation X_g/|X_g| -> X_h/|X_h|",
            "reverse_edge": "U_(h->g)=U_(g->h)^T; theta_(h->g)=-U_(g->h) theta_(g->h)",
            "face_torsion": "T_p = sum_edges P_(base->source)^(-1) theta_edge; developed boundary closure defect",
            "face_curvature": "H_p = ordered product of oriented SO(3) edge links; rotation angle from trace",
            "face_count": 240,
            "link_orthogonality_max": data["link_orthogonality_max"],
            "link_determinant_residual_max": data["link_determinant_residual_max"],
            "torsion_norm": summarize(torsion_norms),
            "curvature_angle_radians": summarize(data["curvature_angles"]),
            "torsion_curvature_nonzero_faces": int(np.count_nonzero(
                (torsion_norms > 1e-10) & (data["curvature_angles"] > 1e-10)
            )),
        },
        "gauge_covariance": gauge,
        "epistemic_limits": [
            "The site coframe is reconstructed from the archived local covariance prescription; it is not a uniquely determined continuum field.",
            "The SO(3) link is the existing shortest-radial-rotation Q6 connection, not yet derived from a common variational action.",
            "Face torsion is a discrete developed-loop closure defect; its continuum Cartan limit is not established.",
            "This audit is spatial SO(3), not a Lorentzian Spin(1,3) or 4D Cartan construction.",
            "No teleparallel flat-connection condition is imposed; nonzero face holonomy is allowed.",
            "No discrete non-Abelian cube Bianchi identity or Mosco/refinement theorem is claimed here.",
        ],
    }


def main() -> None:
    report = build_report()
    print(json.dumps(report, indent=2))
    g = report["gauge_covariance"]
    if g["torsion_covariance_max"] > 1e-10 or g["curvature_conjugation_max"] > 1e-10:
        raise SystemExit("discrete Cartan gauge covariance failed")
    if report["discrete_geometry"]["face_count"] != 240:
        raise SystemExit("unexpected Q6 face count")


if __name__ == "__main__":
    main()
