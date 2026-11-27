"""FEM-01 benchmark problems: parallel plate and conducting sphere (l=1).

Non-dimensional units throughout (epsilon0 = 1, E0 = V/d = 1 unless set).
All quantities needed by the verification protocol are returned in a plain
dict so results can be logged without a solver dependency.
"""
from __future__ import annotations

import numpy as np

from .laplace1d import assemble_and_solve, graded_mesh


def solve_plate(
    gap: float = 1.0,
    voltage: float = 1.0,
    n_elem: int = 8,
) -> dict:
    """Parallel-plate capacitor: phi'' = 0 on [0, gap], phi(0)=0, phi(gap)=V.

    P1 elements reproduce the linear solution exactly, so E = V/d and
    beta = 1 up to roundoff.
    """
    nodes = np.linspace(0.0, gap, n_elem + 1)
    res = assemble_and_solve(
        nodes,
        k_of_x=lambda x: np.ones_like(x),
        c_of_x=lambda x: np.zeros_like(x),
        dirichlet={0: 0.0, n_elem: voltage},
    )
    e_field = -res.element_gradients  # E = -dphi/dx, constant per element
    u_energy = 0.5 * float(np.sum(e_field**2 * np.diff(nodes)))  # eps=1, 1-D "per unit area"
    e_exact = -voltage / gap  # E = -dphi/dx; phi rises from 0 to V
    return {
        "problem": "parallel_plate",
        "n_elem": n_elem,
        "gap": gap,
        "voltage": voltage,
        "E_num": float(e_field[0]),
        "E_exact": e_exact,
        "E_rel_err": abs(e_field[0] - e_exact) / abs(e_exact),
        "beta": float(abs(e_field[0]) / abs(e_exact)),
        "energy_num": u_energy,
        "energy_exact_per_area": 0.5 * voltage**2 / gap,
        "max_abs_phi_err": float(np.max(np.abs(res.values - voltage * nodes / gap))),
    }


def _sphere_u_exact(r: np.ndarray, a: float, e0: float) -> np.ndarray:
    """Radial l=1 amplitude of phi = -E0 (r - a^3/r^2) cos(theta)."""
    return -e0 * (r - a**3 / r**2)


def solve_sphere_l1(
    a: float = 1.0,
    r_far: float = 20.0,
    e0: float = 1.0,
    n_elem: int = 200,
    grading: float = 6.0,
    outer_bc: str = "far_field",
    recovery_deg: int = 3,
    recovery_nodes: int = 8,
) -> dict:
    """Conducting sphere radius a in uniform field E0 (l=1 sector).

    phi(r,theta) = u(r) cos(theta); u solves
        u'' + (2/r) u' - (2/r^2) u = 0   on [a, r_far]
    Weak form used: int (r^2 u' v' + 2 u v) dr = 0 (P1, Gauss integration).

    outer_bc:
      'far_field' -> u(r_far) = -E0 * r_far      (truncated-domain physical BC)
      'exact'      -> u(r_far) = analytic value   (isolates discretisation error)
    Inner BC: u(a) = 0 (grounded sphere, phi = 0).

    beta is evaluated at the pole (theta=0) as |E_r(a)| / E0 with
    E_r = -du/dr on the first element.
    """
    if outer_bc not in {"far_field", "exact"}:
        raise ValueError("outer_bc must be 'far_field' or 'exact'")

    nodes = graded_mesh(a, r_far, n_elem, beta=grading)
    k_of_x = lambda x: x**2
    c_of_x = lambda x: np.full_like(x, 2.0)

    if outer_bc == "far_field":
        u_far = -e0 * r_far
    else:
        u_far = float(_sphere_u_exact(np.array([r_far]), a, e0)[0])

    res = assemble_and_solve(
        nodes, k_of_x=k_of_x, c_of_x=c_of_x,
        dirichlet={0: 0.0, n_elem: u_far},
    )

    # Field at the pole: E_r(a) = -u'(a).
    # (a) raw P1 element gradient on the first element;
    # (b) recovered derivative: cubic least-squares fit through the first
    #     `recovery_nodes` nodal values, differentiated at r = a. The fit is
    #     a standard post-processing step; it does not assume the analytic
    #     solution form.
    e_r_a_raw = -float(res.element_gradients[0])
    m = min(recovery_nodes, len(nodes))
    x_fit = nodes[:m] - a
    coef = np.polyfit(x_fit, res.values[:m], deg=recovery_deg)
    e_r_a_rec = -float(np.polyval(np.polyder(coef), 0.0))

    u_exact_nodes = _sphere_u_exact(nodes, a, e0)
    phi_err = float(np.max(np.abs(res.values - u_exact_nodes)))

    beta_exact = 3.0  # |u'(a)| = 3 E0 for the isolated sphere
    beta_raw = abs(e_r_a_raw) / e0
    beta_rec = abs(e_r_a_rec) / e0

    # Energy in the shell (per unit solid-angle factor): U ~ 2pi int u'^2 r^2 ...
    # Keep it simple and consistent: report field/energy diagnostics, not U.
    return {
        "problem": "sphere_l1",
        "outer_bc": outer_bc,
        "a": a,
        "r_far": r_far,
        "e0": e0,
        "n_elem": n_elem,
        "grading": grading,
        "beta_raw": float(beta_raw),
        "beta_recovered": float(beta_rec),
        "beta_exact": beta_exact,
        "beta_err": abs(beta_rec - beta_exact),
        "beta_rel_err": abs(beta_rec - beta_exact) / beta_exact,
        "beta_raw_err": abs(beta_raw - beta_exact),
        "max_abs_u_err": phi_err,
        "E_r_at_a_raw": float(e_r_a_raw),
        "E_r_at_a_recovered": float(e_r_a_rec),
        "E_r_at_a_exact": -3.0 * e0,
        "u_far_applied": u_far,
        "u_far_exact": float(_sphere_u_exact(np.array([r_far]), a, e0)[0]),
        "truncation_bc_gap": abs(u_far - float(_sphere_u_exact(np.array([r_far]), a, e0)[0])),
    }


def sphere_convergence(
    a: float = 1.0,
    r_far: float = 20.0,
    e0: float = 1.0,
    n_elems: tuple = (50, 100, 200, 400, 800),
    outer_bc: str = "exact",
    grading: float = 6.0,
) -> list[dict]:
    """Mesh-refinement sweep; returns one result dict per n_elem."""
    return [
        solve_sphere_l1(a=a, r_far=r_far, e0=e0, n_elem=n,
                        outer_bc=outer_bc, grading=grading)
        for n in n_elems
    ]
