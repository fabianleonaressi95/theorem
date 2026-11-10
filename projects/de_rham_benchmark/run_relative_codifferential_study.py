"""Relative codifferential convergence study on a curved square.

The test 1-form is u=f(x,y) dx with
    f(x,y)=sin(pi*y) cos(pi*x).
Its tangential trace vanishes on the whole square boundary. In the
Euclidean metric, delta u = -partial_x f = pi sin(pi*x) sin(pi*y),
which also has zero boundary trace. We compare the relative discrete
adjoint with face-integral interpolation of the analytic codifferential.

Run from this directory:
    python run_relative_codifferential_study.py --output reports/relative_codifferential.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import scipy.sparse.linalg as spla

from ddr.mesh import CubicalMesh
from ddr.geometry import PullbackGeometry
from ddr.feec_mass import assemble_consistent_masses
from ddr.boundary_complex import build_relative_complex, relative_betti_numbers
from ddr.feec_study import face_dofs, discrete_norm2
from ddr.test_forms import ScalarField, Form


def boundary_compatible_form():
    # sin(y)cos(x) = 1/2[sin(x+y) + sin(y-x)].
    f = ScalarField(2, [
        {"kind": "sin", "amp": 0.5, "freq": np.array([np.pi, np.pi]),
         "phase": 0.0},
        {"kind": "sin", "amp": 0.5, "freq": np.array([-np.pi, np.pi]),
         "phase": 0.0},
    ])
    return Form.single(2, 1, f, (0,))


def relative_adjoint_identity(rel, rng_seed=7):
    """Return the relative discrete Hilbert-adjoint identity residual."""
    rng = np.random.default_rng(rng_seed)
    D = rel.dmat[0]
    M0, M1 = rel.masses[0], rel.masses[1]
    x = rng.standard_normal(D.shape[1])
    y = rng.standard_normal(D.shape[0])
    delta_y = spla.spsolve(M0.tocsc(), D.T @ (M1 @ y))
    lhs = float((D @ x) @ (M1 @ y))
    rhs = float(x @ (M0 @ delta_y))
    return abs(lhs - rhs) / max(abs(lhs), abs(rhs), 1.0)


def run_level(N: int, amplitude: float = 0.08, nq: int = 5,
              nqf: int = 8) -> dict:
    mesh = CubicalMesh(N, 2)
    geometry = PullbackGeometry(
        mesh,
        {"type": "sinusoid", "amplitude": amplitude, "freq": 1},
        {"type": "identity"},
        nq=nq, nqf=nqf,
    )
    masses, _ = assemble_consistent_masses(mesh, geometry)
    rel = build_relative_complex(mesh, masses)
    form = boundary_compatible_form()

    full_u = face_dofs(mesh, geometry, form.eval, 1, nqf=nqf)
    full_du = face_dofs(
        mesh, geometry, lambda x: form.delta(x, geometry.metric),
        0, nqf=nqf,
    )
    u = full_u[rel.keep[1]]
    rhs = full_du[rel.keep[0]]

    D = rel.dmat[0]
    M0, M1 = rel.masses[0], rel.masses[1]
    delta_h = spla.spsolve(M0.tocsc(), D.T @ (M1 @ u))
    error = delta_h - rhs
    err_norm = float(np.sqrt(max(discrete_norm2(error, M0), 0.0)))
    rhs_norm = float(np.sqrt(max(discrete_norm2(rhs, M0), 0.0)))

    boundary_u = float(np.max(np.abs(full_u[rel.boundary[1]]))) \
        if np.any(rel.boundary[1]) else 0.0
    boundary_rhs = float(np.max(np.abs(full_du[rel.boundary[0]]))) \
        if np.any(rel.boundary[0]) else 0.0

    return {
        "N": N,
        "h": 1.0 / N,
        "dimensions": rel.dimensions,
        "relative_betti": relative_betti_numbers(rel)[0],
        "relative_adjoint_identity_rel": relative_adjoint_identity(rel),
        "codifferential_error_M0": err_norm,
        "codifferential_relative_error": err_norm / max(rhs_norm, 1e-300),
        "rhs_norm_M0": rhs_norm,
        "max_boundary_tangential_dof": boundary_u,
        "max_boundary_delta_dof": boundary_rhs,
        "mass_min_eigenvalue_estimate": float(min(
            np.linalg.eigvalsh(M0.toarray())[0],
            np.linalg.eigvalsh(M1.toarray())[0],
        )),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--levels", type=int, nargs="+", default=[4, 8, 16])
    parser.add_argument("--amplitude", type=float, default=0.08)
    parser.add_argument("--output", type=Path,
                        default=Path("reports/relative_codifferential.json"))
    args = parser.parse_args()

    rows = [run_level(N, amplitude=args.amplitude) for N in args.levels]
    for i in range(1, len(rows)):
        rows[i]["observed_rate"] = float(
            np.log(rows[i - 1]["codifferential_error_M0"]
                   / rows[i]["codifferential_error_M0"])
            / np.log(rows[i - 1]["h"] / rows[i]["h"])
        )
    payload = {
        "study": "relative_codifferential_curved_square",
        "map": {"type": "sinusoid", "amplitude": args.amplitude, "freq": 1},
        "metric": "identity",
        "form": "u=sin(pi*y)*cos(pi*x) dx",
        "continuous_codifferential":
            "delta u=pi*sin(pi*x)*sin(pi*y)",
        "levels": rows,
        "status": "finite-level numerical study; not a Mosco or operator-norm proof",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
