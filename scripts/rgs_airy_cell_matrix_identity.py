#!/usr/bin/env python3
"""Analytic annulus audit of Hessian/Laplacian cell interaction matrices.

Builds the three biharmonic cell functions (constant, x, y boundary data)
on an annulus and compares integral D2(u):D2(v) with integral Delta(u)Delta(v).
This is a continuum manufactured-solution audit, not a C0-IPDG reproduction.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss


def _basis(r, mode):
    r = np.asarray(r, dtype=float)
    if mode == 0:
        f = np.stack((np.ones_like(r), np.log(r), r*r, r*r*np.log(r)), axis=-1)
        fp = np.stack((np.zeros_like(r), 1/r, 2*r, 2*r*np.log(r)+r), axis=-1)
        fpp = np.stack((np.zeros_like(r), -1/(r*r), 2*np.ones_like(r), 2*np.log(r)+3), axis=-1)
    elif mode == 1:
        f = np.stack((r, 1/r, r**3, r*np.log(r)), axis=-1)
        fp = np.stack((np.ones_like(r), -1/(r*r), 3*r*r, np.log(r)+1), axis=-1)
        fpp = np.stack((np.zeros_like(r), 2/(r**3), 6*r, 1/r), axis=-1)
    else:
        raise ValueError("mode must be 0 or 1")
    return f, fp, fpp


def _cell_coefficients(a, R, mode):
    # Inner and outer boundary traces: kappa_0=(1,0), kappa_1/2=(x_1/2,n_1/2).
    f, fp, _ = _basis(np.array([a, R]), mode)
    if mode == 0:
        rhs = np.array([1.0, 0.0, 0.0, 0.0])
    else:
        rhs = np.array([a, 1.0, 0.0, 0.0])
    A = np.vstack((f[0], fp[0], f[1], fp[1]))
    return np.linalg.solve(A, rhs)


def _radial_integrals(a, R, mode, ci, cj, order):
    x, w = leggauss(order)
    r = (R-a)*0.5*x + (R+a)*0.5
    wr = (R-a)*0.5*w*r  # polar area measure r dr
    fi, fpi, fppi = _basis(r, mode)
    fj, fpj, fppj = fi, fpi, fppi
    Fi, Fpi, Fppi = fi @ ci, fpi @ ci, fppi @ ci
    Fj, Fpj, Fppj = fj @ cj, fpj @ cj, fppj @ cj
    if mode == 0:
        angular = 2*np.pi
        hrr_i, htt_i = Fppi, Fpi/r
        hrr_j, htt_j = Fppj, Fpj/r
        hess = angular*np.sum(wr*(hrr_i*hrr_j + htt_i*htt_j))
        lap_i, lap_j = hrr_i+htt_i, hrr_j+htt_j
    else:
        angular = np.pi  # integral cos^2 or sin^2 over [0,2pi]
        hrr_i, htt_i = Fppi, Fpi/r - Fi/(r*r)
        hrr_j, htt_j = Fppj, Fpj/r - Fj/(r*r)
        hrt_i, hrt_j = Fpi/r-Fi/(r*r), Fpj/r-Fj/(r*r)
        hess = angular*np.sum(wr*(hrr_i*hrr_j + 2*hrt_i*hrt_j + htt_i*htt_j))
        lap_i, lap_j = hrr_i+htt_i, hrr_j+htt_j
    lap = angular*np.sum(wr*lap_i*lap_j)
    return float(hess), float(lap)


def audit_annulus(a=0.2, R=1.0, order=256):
    if not (0 < a < R):
        raise ValueError("require 0 < inner radius < outer radius")
    coeff = [_cell_coefficients(a, R, 0),
             _cell_coefficients(a, R, 1),
             _cell_coefficients(a, R, 1)]
    # kappa_0 is radial; kappa_1 and kappa_2 are cos(theta)/sin(theta) modes.
    H = np.zeros((3,3)); L = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            if i == j == 0:
                H[i,j], L[i,j] = _radial_integrals(a,R,0,coeff[i],coeff[j],order)
            elif i > 0 and j > 0:
                if i != j:  # orthogonal angular modes cos(theta), sin(theta)
                    H[i,j] = L[i,j] = 0.0
                else:
                    H[i,j], L[i,j] = _radial_integrals(a,R,1,coeff[i],coeff[j],order)
            else:
                H[i,j] = L[i,j] = 0.0
    delta = H-L
    rel = float(np.linalg.norm(delta,ord="fro")/max(np.linalg.norm(H,ord="fro"),1e-300))
    return {"inner_radius":a,"outer_radius":R,"quadrature_order":order,
            "hessian_matrix":H.tolist(),"laplacian_matrix":L.tolist(),
            "relative_frobenius_difference":rel,
            "symmetry_residual_hessian":float(np.linalg.norm(H-H.T)),
            "symmetry_residual_laplacian":float(np.linalg.norm(L-L.T)),
            "min_eigenvalue_hessian":float(np.linalg.eigvalsh(H).min()),
            "min_eigenvalue_laplacian":float(np.linalg.eigvalsh(L).min())}


def run():
    cases=[audit_annulus(a=a,R=1.0,order=384) for a in (0.1,0.2,0.35)]
    return {"title":"Annular Airy cell matrix identity audit",
            "status":"continuum analytic cell fields; independent of C0-IPDG discretization",
            "identity":"integral D2(kappa_i):D2(kappa_j) = integral Delta(kappa_i)Delta(kappa_j)",
            "boundary_data":"inner active core affine traces with matching normal derivatives; outer clamped zero traces",
            "cases":cases,
            "max_relative_frobenius_difference":max(c["relative_frobenius_difference"] for c in cases)}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",default=None)
    args=p.parse_args()
    result=run()
    payload=json.dumps(result,indent=2)
    if args.out:
        path=Path(args.out); path.parent.mkdir(parents=True,exist_ok=True); path.write_text(payload+"\n")
    print(payload)


if __name__=="__main__":
    main()
