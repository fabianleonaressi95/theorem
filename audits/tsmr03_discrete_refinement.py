"""Chain-complex, homology, spectrum and transport checks on cycle refinements.

The cycle C_n is a 1-dimensional simplicial complex. Refinement C_n -> C_(kn)
subdivides every edge into k edges. Betti numbers are computed from boundary
ranks over R (for this graph, integer incidence matrices have exact rank
n-1); the cycle Laplacian spectrum is evaluated from its closed formula.
"""
from __future__ import annotations

import math


def cycle_boundary_matrix(n_vertices: int) -> list[list[int]]:
    """Return B1 (vertices x oriented edges) for the oriented cycle C_n."""
    if n_vertices < 3:
        raise ValueError("a simple cycle requires at least three vertices")
    matrix = [[0] * n_vertices for _ in range(n_vertices)]
    for edge in range(n_vertices):
        matrix[edge][edge] = -1
        matrix[(edge + 1) % n_vertices][edge] = 1
    return matrix


def rank_over_rational(matrix: list[list[int]]) -> int:
    """Exact Gaussian elimination using Fraction arithmetic."""
    from fractions import Fraction
    if not matrix:
        return 0
    work = [[Fraction(value) for value in row] for row in matrix]
    rows, cols = len(work), len(work[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][col]
        work[rank] = [value / pivot_value for value in work[rank]]
        for r in range(rows):
            if r != rank and work[r][col]:
                factor = work[r][col]
                work[r] = [a - factor*b for a, b in zip(work[r], work[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def cycle_betti_numbers(n_vertices: int) -> tuple[int, int]:
    """Return (beta_0, beta_1) for C_n from ranks of its chain boundary."""
    boundary = cycle_boundary_matrix(n_vertices)
    rank_b1 = rank_over_rational(boundary)
    beta0 = n_vertices - rank_b1
    beta1 = n_vertices - rank_b1
    return beta0, beta1


def cycle_laplacian_spectrum(n_vertices: int) -> list[float]:
    """Eigenvalues 2 - 2 cos(2 pi j/n), j=0,...,n-1."""
    if n_vertices < 3:
        raise ValueError("a simple cycle requires at least three vertices")
    return sorted(2.0 - 2.0*math.cos(2.0*math.pi*j/n_vertices)
                  for j in range(n_vertices))


def refine_cycle_values(values: list[float], factor: int = 2) -> list[float]:
    """Piecewise-linear prolongation of vertex values to a refined cycle."""
    n = len(values)
    if n < 3 or factor < 2:
        raise ValueError("need at least 3 coarse vertices and refinement factor >= 2")
    refined = [0.0] * (n * factor)
    for edge in range(n):
        left, right = values[edge], values[(edge + 1) % n]
        for step in range(factor):
            t = step / factor
            refined[edge*factor + step] = (1.0-t)*left + t*right
    return refined


def refinement_report(n_vertices: int, factor: int = 2) -> dict:
    """Compare topology, spectrum and prolongation over one refinement."""
    coarse_beta = cycle_betti_numbers(n_vertices)
    fine_n = n_vertices * factor
    fine_beta = cycle_betti_numbers(fine_n)
    coarse_spectrum = cycle_laplacian_spectrum(n_vertices)
    fine_spectrum = cycle_laplacian_spectrum(fine_n)
    # First positive eigenvalue; multiply by h^-2 to compare continuum scale.
    coarse_gap = next(value for value in coarse_spectrum if value > 1e-12)
    fine_gap = next(value for value in fine_spectrum if value > 1e-12)
    coarse_h = 1.0 / n_vertices
    fine_h = 1.0 / fine_n
    coarse_scaled_gap = coarse_gap / (coarse_h**2)
    fine_scaled_gap = fine_gap / (fine_h**2)
    sample = [math.sin(2.0*math.pi*j/n_vertices) for j in range(n_vertices)]
    prolonged = refine_cycle_values(sample, factor)
    return {
        "coarse_vertices": n_vertices,
        "fine_vertices": fine_n,
        "coarse_betti": coarse_beta,
        "fine_betti": fine_beta,
        "coarse_boundary_rank": n_vertices - coarse_beta[0],
        "fine_boundary_rank": fine_n - fine_beta[0],
        "coarse_spectral_gap": coarse_gap,
        "fine_spectral_gap": fine_gap,
        "coarse_scaled_gap": coarse_scaled_gap,
        "fine_scaled_gap": fine_scaled_gap,
        "prolonged_values": prolonged,
        "coarse_values": sample,
    }


def torus_cellular_boundaries(n: int) -> tuple[list[list[int]], list[list[int]]]:
    """Return (B1, B2) for the periodic n-by-n square cellulation of T^2.

    Vertices are indexed by (i,j), horizontal then vertical oriented edges,
    and positively oriented square faces. This is a cellular (cubical) chain
    complex, not a simplicial triangulation.
    """
    if n < 3:
        raise ValueError("periodic square torus requires n >= 3")
    vertices = n*n
    edges = 2*vertices
    faces = vertices
    def v(i: int, j: int) -> int:
        return (i % n)*n + (j % n)
    def h(i: int, j: int) -> int:
        return (i % n)*n + (j % n)
    def e_v(i: int, j: int) -> int:
        return vertices + (i % n)*n + (j % n)
    b1 = [[0]*edges for _ in range(vertices)]
    for i in range(n):
        for j in range(n):
            b1[v(i,j)][h(i,j)] -= 1
            b1[v(i+1,j)][h(i,j)] += 1
            b1[v(i,j)][e_v(i,j)] -= 1
            b1[v(i,j+1)][e_v(i,j)] += 1
    b2 = [[0]*faces for _ in range(edges)]
    for i in range(n):
        for j in range(n):
            face = i*n+j
            b2[h(i,j)][face] += 1
            b2[e_v(i+1,j)][face] += 1
            b2[h(i,j+1)][face] -= 1
            b2[e_v(i,j)][face] -= 1
    return b1, b2


def matrix_product_integer(left: list[list[int]],
                           right: list[list[int]]) -> list[list[int]]:
    """Multiply compatible integer matrices."""
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    return [[sum(left[i][k]*right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def torus_betti_numbers(n: int) -> tuple[int, int, int]:
    """Compute cellular Betti numbers (beta0,beta1,beta2) over Q."""
    b1, b2 = torus_cellular_boundaries(n)
    r1 = rank_over_rational(b1)
    r2 = rank_over_rational(b2)
    vertices, edges, faces = n*n, 2*n*n, n*n
    return (vertices-r1, edges-r1-r2, faces-r2)


def torus_graph_spectrum(n: int) -> list[float]:
    """Spectrum of the 1-skeleton Laplacian on the periodic square torus."""
    if n < 3:
        raise ValueError("periodic square torus requires n >= 3")
    return sorted(4.0 - 2.0*math.cos(2*math.pi*p/n)
                  - 2.0*math.cos(2*math.pi*q/n)
                  for p in range(n) for q in range(n))


def prolong_torus_field(values: list[list[float]], factor: int = 2) -> list[list[float]]:
    """Periodic bilinear interpolation of a vertex field to a refined torus."""
    n = len(values)
    if n < 3 or any(len(row) != n for row in values) or factor < 2:
        raise ValueError("values must be a square n>=3 grid and factor >= 2")
    fine_n = n*factor
    fine = [[0.0]*fine_n for _ in range(fine_n)]
    for i in range(fine_n):
        x0, tx = divmod(i, factor)
        tx = tx/factor
        for j in range(fine_n):
            y0, ty = divmod(j, factor)
            ty = ty/factor
            a = values[x0 % n][y0 % n]
            b = values[(x0+1) % n][y0 % n]
            c = values[x0 % n][(y0+1) % n]
            d = values[(x0+1) % n][(y0+1) % n]
            fine[i][j] = ((1-tx)*(1-ty)*a + tx*(1-ty)*b
                          + (1-tx)*ty*c + tx*ty*d)
    return fine
