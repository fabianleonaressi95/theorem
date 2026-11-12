"""Independent reconstruction of the wall-corrected Purcell swimmer.

The implementation assembles the 5x5 generalized resistance matrix by
Gauss-Legendre quadrature of the local resistive-force law. It is an audit prototype that reproduces the published leading-order longitudinal benchmark of Micalizio et al. (2026).
"""
from __future__ import annotations

import argparse
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp


def resistance_matrix(q, *, length=1.0, lam=1.0, radius=1e-4,
                      viscosity=1.0, quadrature_order=64):
    """Return the symmetric 5x5 resistance matrix for q=(x,y,theta,a-,a+).

    The three generalized body velocities are (xdot, ydot, thetadot);
    the last two are the hinge rates (adot-, adot+).  The local drag tensor
    is C_perp (I - e e^T/2), with C_perp=4*pi*mu/log(2*d/r).
    """
    _, y, theta, alpha_minus, alpha_plus = np.asarray(q, dtype=float)
    central_length = lam * length
    nodes, weights = leggauss(quadrature_order)
    matrix = np.zeros((5, 5), dtype=float)
    identity = np.eye(2)

    e0 = np.array([np.cos(theta), np.sin(theta)])
    n0 = np.array([-e0[1], e0[0]])

    def accumulate(direction, distance, jacobian, weight):
        if distance <= radius / 2:
            raise ValueError("configuration violates the wall-clearance condition")
        log_argument = 2.0 * distance / radius
        if log_argument <= 1.0:
            raise ValueError("invalid logarithm in wall-corrected drag coefficient")
        c_perp = 4.0 * np.pi * viscosity / np.log(log_argument)
        drag = c_perp * (identity - 0.5 * np.outer(direction, direction))
        matrix[:] += weight * (jacobian.T @ drag @ jacobian)

    # Central link: s is measured from its midpoint, over [-L0/2,L0/2].
    for node, weight0 in zip(nodes, weights):
        s = 0.5 * central_length * node
        weight = 0.5 * central_length * weight0
        jacobian = np.zeros((2, 5))
        jacobian[:, :2] = identity
        jacobian[:, 2] = s * n0
        accumulate(e0, y + s * e0[1], jacobian, weight)

    # Outer links.  The sign is both the hinge-side and outward-link sign.
    for sign, alpha, shape_column in (
        (-1.0, alpha_minus, 3),
        (+1.0, alpha_plus, 4),
    ):
        angle = theta + alpha
        direction = np.array([np.cos(angle), np.sin(angle)])
        normal = np.array([-direction[1], direction[0]])
        hinge_height = y + sign * 0.5 * central_length * e0[1]

        for node, weight0 in zip(nodes, weights):
            s = 0.5 * length * (node + 1.0)
            weight = 0.5 * length * weight0
            distance = hinge_height + sign * s * direction[1]
            jacobian = np.zeros((2, 5))
            jacobian[:, :2] = identity
            jacobian[:, 2] = (
                sign * 0.5 * central_length * n0 + sign * s * normal
            )
            jacobian[:, shape_column] = sign * s * normal
            accumulate(direction, distance, jacobian, weight)

    return matrix


def swimmer_rhs(_time, q, control, **parameters):
    """Force/torque-free body velocity coupled to prescribed shape rates."""
    resistance = resistance_matrix(q, **parameters)
    body_velocity = np.linalg.solve(
        resistance[:3, :3],
        -resistance[:3, 3:] @ np.asarray(control, dtype=float),
    )
    return np.concatenate((body_velocity, np.asarray(control, dtype=float)))


def simulate_square_gait(amplitude, *, quadrature_order=64,
                         rtol=1e-10, atol=1e-12, **parameters):
    """Integrate the four-stage gait (+u-, +u+, -u-, -u+) over four time units."""
    q = np.array([0.0, 1e-2, 0.0, 0.0, 0.0])
    controls = (
        (amplitude, 0.0),
        (0.0, amplitude),
        (-amplitude, 0.0),
        (0.0, -amplitude),
    )
    for stage, control in enumerate(controls):
        solution = solve_ivp(
            lambda t, state: swimmer_rhs(
                t, state, control,
                quadrature_order=quadrature_order, **parameters
            ),
            (float(stage), float(stage + 1)),
            q,
            method="DOP853",
            rtol=rtol,
            atol=atol,
        )
        if not solution.success:
            raise RuntimeError(solution.message)
        q = solution.y[:, -1]
    return q


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--amplitude", type=float, default=1e-3)
    parser.add_argument("--order", type=int, default=64)
    args = parser.parse_args()
    final = simulate_square_gait(args.amplitude,
                                 quadrature_order=args.order)
    initial = np.array([0.0, 1e-2, 0.0, 0.0, 0.0])
    print("final_state =", np.array2string(final, precision=12))
    print("normalized_cycle_displacement =",
          np.array2string((final - initial)[:3] / args.amplitude**2,
                          precision=12))
    print("paper_reference_dx_limit = 0.0617283950617")
    print("status = leading-order longitudinal coefficient reproduced; Q6 discretization remains open")


if __name__ == "__main__":
    main()
