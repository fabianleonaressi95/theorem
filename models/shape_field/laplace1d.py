"""Generic 1-D P1 finite-element solver for -d/dx(k du/dx) + c u = 0 style BVPs.

Backend: NumPy + SciPy sparse direct solve. Elements are linear (P1);
element matrices are integrated with 2-point Gauss quadrature so the same
assembly path serves both the plate (k=1, c=0) and the sphere l=1 radial
problem (k=r^2, c=2).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

# 2-point Gauss-Legendre on [-1, 1]
_GP_XI = np.array([-1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)])
_GP_W = np.array([1.0, 1.0])


@dataclass
class Fem1DResult:
    nodes: np.ndarray          # (n_nodes,)
    values: np.ndarray         # nodal solution u(x_i)
    element_values: np.ndarray  # (n_elem, 2) nodal values per element
    element_gradients: np.ndarray  # (n_elem,) du/dx per element (P1: constant)


def assemble_and_solve(
    nodes: np.ndarray,
    k_of_x,
    c_of_x,
    dirichlet: dict[int, float],
) -> Fem1DResult:
    """Solve  int (k u' v' + c u v) dx = 0  with Dirichlet nodal values.

    k_of_x, c_of_x: callables evaluated at Gauss points (arrays accepted).
    dirichlet: {node_index: value}; all remaining nodes are free.
    """
    nodes = np.asarray(nodes, dtype=float)
    n_elem = len(nodes) - 1
    rows, cols, data = [], [], []

    for e in range(n_elem):
        xa, xb = nodes[e], nodes[e + 1]
        h = xb - xa
        ke = np.zeros((2, 2))
        for xi, w in zip(_GP_XI, _GP_W):
            xg = 0.5 * (xa + xb) + 0.5 * h * xi
            jac = 0.5 * h
            # P1 shape functions on reference element [0,1]
            N = np.array([0.5 * (1.0 - xi), 0.5 * (1.0 + xi)])
            dN = np.array([-1.0 / h, 1.0 / h])
            kg = float(np.mean(k_of_x(np.array([xg])))) if callable(k_of_x) else k_of_x
            cg = float(np.mean(c_of_x(np.array([xg])))) if callable(c_of_x) else c_of_x
            ke += w * jac * (kg * np.outer(dN, dN) + cg * np.outer(N, N))
        for a in range(2):
            for b in range(2):
                rows.append(e + a)
                cols.append(e + b)
                data.append(ke[a, b])

    K = sp.coo_matrix((data, (rows, cols)), shape=(len(nodes), len(nodes))).tocsr()
    n = len(nodes)
    fixed = sorted(dirichlet)
    free = np.array([i for i in range(n) if i not in dirichlet], dtype=int)

    u = np.zeros(n)
    for i, v in dirichlet.items():
        u[i] = v
    if len(free):
        rhs = -K[free][:, fixed] @ u[fixed]
        u[free] = spla.spsolve(K[free][:, free].tocsc(), rhs)

    grads = np.array([(u[e + 1] - u[e]) / (nodes[e + 1] - nodes[e]) for e in range(n_elem)])
    return Fem1DResult(
        nodes=nodes,
        values=u,
        element_values=np.stack([u[:-1], u[1:]], axis=1),
        element_gradients=grads,
    )


def graded_mesh(a: float, b: float, n_elem: int, beta: float = 2.0) -> np.ndarray:
    """Geometrically graded mesh on [a, b], clustering toward a.

    beta > 1 gives ratio r = beta**(1/n_elem)-ish spacing growth; beta = 1
    recovers a uniform mesh.
    """
    if beta == 1.0:
        return np.linspace(a, b, n_elem + 1)
    t = np.linspace(0.0, 1.0, n_elem + 1)
    s = (np.exp(np.log(beta) * t) - 1.0) / (beta - 1.0)
    return a + (b - a) * s
