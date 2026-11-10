"""Q6 cubical complex and higher-order topological Kuramoto models.

Equations (12)-(13) (NL) and (16)-(17) (NLT) of Ghorbanchian et al.,
Commun. Phys. 4, 120 (2021), with square 2-cells replacing triangles.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations, product
from typing import Literal
import numpy as np

ModelName = Literal["NL", "NLT"]

@dataclass(frozen=True)
class Q6Complex:
    vertices: tuple
    edges: tuple
    faces: tuple
    B1: np.ndarray
    B2: np.ndarray
    vertex_index: dict
    edge_index: dict

def build_q6_complex() -> Q6Complex:
    """Build the 6-cube 2-skeleton: 64 vertices, 192 edges, 240 squares."""
    vertices = tuple(product((0, 1), repeat=6))
    vertex_index = {v: i for i, v in enumerate(vertices)}
    edges_list = []
    for v in vertices:
        for axis in range(6):
            if v[axis] == 0:
                w = list(v); w[axis] = 1
                edges_list.append((vertex_index[v], vertex_index[tuple(w)]))
    edges = tuple(sorted(edges_list))
    edge_index = {e: i for i, e in enumerate(edges)}
    B1 = np.zeros((64, 192), dtype=np.int64)
    for j, (u, v) in enumerate(edges):
        B1[u, j], B1[v, j] = -1, 1
    faces_list = []
    for axes in combinations(range(6), 2):
        fixed_axes = [a for a in range(6) if a not in axes]
        for fixed in product((0, 1), repeat=4):
            base = [0] * 6
            for a, bit in zip(fixed_axes, fixed):
                base[a] = bit
            a, b = axes
            v00 = tuple(base)
            v10 = base.copy(); v10[a] = 1
            v11 = v10.copy(); v11[b] = 1
            v01 = base.copy(); v01[b] = 1
            faces_list.append(tuple(vertex_index[x] for x in
                                    (v00, tuple(v10), tuple(v11), tuple(v01))))
    faces = tuple(faces_list)
    B2 = np.zeros((192, 240), dtype=np.int64)
    for f, cycle in enumerate(faces):
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            e = edge_index[(min(u, v), max(u, v))]
            B2[e, f] += 1 if u < v else -1
    return Q6Complex(vertices, edges, faces, B1, B2, vertex_index, edge_index)

def anti_twin_chain_maps(K: Q6Complex):
    """Signed permutation maps induced by bitwise complement on oriented cells."""
    J0 = np.zeros((64, 64), dtype=np.int64)
    J1 = np.zeros((192, 192), dtype=np.int64)
    J2 = np.zeros((240, 240), dtype=np.int64)
    vmap = {v: tuple(1-x for x in v) for v in K.vertices}
    for i, v in enumerate(K.vertices):
        J0[K.vertex_index[vmap[v]], i] = 1
    for i, (u, v) in enumerate(K.edges):
        ju = K.vertex_index[vmap[K.vertices[u]]]
        jv = K.vertex_index[vmap[K.vertices[v]]]
        target = K.edge_index[(min(ju, jv), max(ju, jv))]
        J1[target, i] = 1 if ju < jv else -1
    face_lookup = {frozenset(cycle): i for i, cycle in enumerate(K.faces)}
    for f, cycle in enumerate(K.faces):
        mapped = tuple(K.vertex_index[vmap[K.vertices[v]]] for v in cycle)
        target = face_lookup[frozenset(mapped)]
        mapped_boundary = J1 @ K.B2[:, f]
        target_boundary = K.B2[:, target]
        sign = int(round(float(mapped_boundary @ target_boundary) / 4.0))
        if sign not in (-1, 1) or not np.array_equal(mapped_boundary, sign*target_boundary):
            raise AssertionError("Complement does not preserve an oriented square boundary")
        J2[target, f] = sign
    return J0, J1, J2

def audit_q6_complex(K: Q6Complex) -> dict:
    J0, J1, J2 = anti_twin_chain_maps(K)
    rank1 = int(np.linalg.matrix_rank(K.B1.astype(float)))
    rank2 = int(np.linalg.matrix_rank(K.B2.astype(float)))
    return {
        "counts": {"vertices": 64, "edges": 192, "square_faces": 240},
        "B1B2_exact_zero": bool(np.count_nonzero(K.B1 @ K.B2) == 0),
        "rank_B1_numeric": rank1, "rank_B2_numeric": rank2,
        "graph_cycle_rank": 192-rank1,
        "filled_betti_1": 192-rank1-rank2,
        "b2_of_truncated_2_skeleton": 240-rank2,
        "anti_twin_squared_identity": bool(
            np.array_equal(J0@J0, np.eye(64, dtype=np.int64)) and
            np.array_equal(J1@J1, np.eye(192, dtype=np.int64)) and
            np.array_equal(J2@J2, np.eye(240, dtype=np.int64))),
        "anti_twin_chain_map": bool(
            np.array_equal(J0@K.B1, K.B1@J1) and
            np.array_equal(J1@K.B2, K.B2@J2)),
    }

def order_parameters(K: Q6Complex, theta: np.ndarray, phi: np.ndarray) -> dict:
    return {
        "R0": float(abs(np.mean(np.exp(1j*theta)))),
        "R1_down": float(abs(np.mean(np.exp(1j*(K.B1@phi))))),
        "R1_up": float(abs(np.mean(np.exp(1j*(K.B2.T@phi))))),
    }

def rhs(K, theta, phi, omega, omega_link, sigma, model: ModelName):
    """Frozen NL/NLT vector fields; sine is applied componentwise.

NL:
  theta_dot = omega - sigma R1_down B1 sin(B1.T theta)
  phi_dot   = omega_link - sigma R0 B1.T sin(B1 phi)
                         - sigma B2 sin(B2.T phi)
NLT:
  theta_dot = omega - sigma R1_down B1 sin(B1.T theta)
  phi_dot   = omega_link - sigma R0 R1_up B1.T sin(B1 phi)
                         - sigma R1_down B2 sin(B2.T phi)

The definitions of R0, R1_down and R1_up are in order_parameters().
These equations are frozen for the T1/T2 verification protocol.
"""
    op = order_parameters(K, theta, phi)
    down, up = K.B1@phi, K.B2.T@phi
    theta_dot = omega - sigma*op["R1_down"]*(K.B1@np.sin(K.B1.T@theta))
    if model == "NL":
        phi_dot = (omega_link - sigma*op["R0"]*(K.B1.T@np.sin(down))
                   - sigma*(K.B2@np.sin(up)))
    elif model == "NLT":
        phi_dot = (omega_link - sigma*op["R0"]*op["R1_up"]*(K.B1.T@np.sin(down))
                   - sigma*op["R1_down"]*(K.B2@np.sin(up)))
    else:
        raise ValueError("model must be NL or NLT")
    return theta_dot, phi_dot

def rk4_step(K, theta, phi, omega, omega_link, sigma, model, dt):
    def f(t, p): return rhs(K, t, p, omega, omega_link, sigma, model)
    k1t,k1p=f(theta,phi)
    k2t,k2p=f(theta+.5*dt*k1t,phi+.5*dt*k1p)
    k3t,k3p=f(theta+.5*dt*k2t,phi+.5*dt*k2p)
    k4t,k4p=f(theta+dt*k3t,phi+dt*k3p)
    return (theta+dt*(k1t+2*k2t+2*k3t+k4t)/6,
            phi+dt*(k1p+2*k2p+2*k3p+k4p)/6)

def sample_intrinsic_frequencies(seed, n_nodes=64, n_links=192,
                                 omega0=2.0, omega1=2.0,
                                 tau0=1.0, tau1=1.0):
    """Sample source-paper Gaussian frequencies in a co-rotating node frame.

    The paper uses omega_i ~ N(Omega0, 1/tau0) and
    omega_tilde_l ~ N(Omega1, 1/tau1).  The common node drift Omega0 is
    removed by rotating the node phase frame; the link mean is retained.
    """
    if tau0 <= 0 or tau1 <= 0:
        raise ValueError("tau0 and tau1 must be positive")
    rng=np.random.default_rng(seed)
    omega=rng.normal(omega0,1.0/tau0,n_nodes)-omega0
    omega_link=rng.normal(omega1,1.0/tau1,n_links)
    return omega,omega_link


def simulate_branch(K, sigmas, model: ModelName, seed=0, steps_per_sigma=80,
                    dt=.025, initial=None, return_final=False,
                    omega0=2.0, omega1=2.0, tau0=1.0, tau1=1.0):
    """Quasi-static continuation with reproducible, configurable frequencies.

    The same seed produces the same intrinsic node/link frequencies regardless
    of branch initialization.  This lets the reverse sweep reuse the forward
    terminal state without silently drawing a different frequency realization.
    """
    omega, omega_link = sample_intrinsic_frequencies(
        seed, 64, 192, omega0, omega1, tau0, tau1
    )

    # Keep phase initialization on an independent stream so frequency sampling
    # is unchanged when a supplied terminal state is used for the reverse branch.
    phase_rng = np.random.default_rng(int(seed) + 1_000_003)
    if initial is None:
        theta = phase_rng.uniform(-np.pi, np.pi, 64)
        phi = phase_rng.uniform(-np.pi, np.pi, 192)
    else:
        theta = np.array(initial[0], dtype=float).copy()
        phi = np.array(initial[1], dtype=float).copy()

    rows = []
    for sigma in np.asarray(sigmas, dtype=float):
        for _ in range(int(steps_per_sigma)):
            theta, phi = rk4_step(
                K, theta, phi, omega, omega_link, float(sigma), model, dt
            )
        rows.append({"sigma": float(sigma), **order_parameters(K, theta, phi)})

    if return_final:
        return rows, (theta, phi)
    return rows
