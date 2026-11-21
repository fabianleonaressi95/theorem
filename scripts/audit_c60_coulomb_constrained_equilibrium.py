#!/usr/bin/env python3
"""Constrained Coulomb equilibrium audit for a relaxed C60 cage.

Minimizes the all-pairs unit-charge Coulomb energy at fixed center of mass
and fixed RMS radius, starting from the MMFF94s-relaxed coordinates.
The constrained Hessian is formed only after the KKT residual is checked.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from itertools import combinations, product, permutations
import numpy as np
from scipy.optimize import minimize, linear_sum_assignment
from scipy.spatial import ConvexHull
from scipy.spatial.distance import cdist
from scipy.linalg import null_space

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from audit_c60_mmff94s_relaxed_coulomb import (
    ico_vertices, c60_ideal, mmff_relax, coulomb_energy_gradient,
    coulomb_hessian, tangent_basis
)

def symmetry_matrices_icosahedron(tol=1e-8):
    """Recover all orthogonal symmetries of the ideal icosahedron from triples."""
    v = ico_vertices()
    src = v[[0, 1, 2]]
    gram = src @ src.T
    mats = []
    for idx in permutations(range(len(v)), 3):
        dst = v[list(idx)]
        if np.max(np.abs(dst @ dst.T - gram)) > tol:
            continue
        u, _, vt = np.linalg.svd(src.T @ dst)
        O = u @ vt
        if np.max(np.min(cdist(v @ O, v), axis=1)) > 1e-7:
            continue
        if not any(np.linalg.norm(O-M, ord="fro") < 1e-7 for M in mats):
            mats.append(O)
    return mats

def symmetry_audit(x, matrices):
    rows=[]
    for O in matrices:
        transformed = x @ O
        d = cdist(transformed, x)
        ri, ci = linear_sum_assignment(d)
        matched = d[ri, ci]
        rows.append((float(np.sqrt(np.mean(matched**2))),
                     float(np.max(matched))))
    rms = np.array([a for a, _ in rows])
    mx = np.array([b for _, b in rows])
    return {
        "candidate_icosahedral_orthogonal_operations": len(matrices),
        "operations_preserved_rms_le_1e-6": int(np.sum(rms <= 1e-6)),
        "operations_preserved_max_le_1e-6": int(np.sum(mx <= 1e-6)),
        "operations_preserved_max_le_1e-4": int(np.sum(mx <= 1e-4)),
        "best_nonidentity_or_any_operation_rms": float(np.min(rms)),
        "worst_operation_rms": float(np.max(rms)),
        "max_assignment_residual_over_group": float(np.max(mx)),
        "interpretation": "Each ideal I_h operation is tested by an optimal point assignment; counts are coordinate-preservation diagnostics, not an assumed symmetry decomposition."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-npz", default=None,
                    help="Optional prior audit NPZ; otherwise regenerate MMFF94s relaxation.")
    ap.add_argument("--max-iterations", type=int, default=20000)
    ap.add_argument("--out-dir", default="c60_coulomb_equilibrium_audit")
    args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    if args.input_npz:
        data=np.load(args.input_npz)
        x0=np.asarray(data["X_ideal"],float)
        x_start=np.asarray(data["X_relaxed"],float)
        bonds=np.asarray(data["bonds"],int)
        model={"source":"prior MMFF94s audit NPZ"}
    else:
        x0,bonds0=c60_ideal()
        x_start,model=mmff_relax(x0,bonds0,10000)
        bonds=np.asarray(bonds0,int)
    if x_start.shape != (60,3) or len(bonds)!=90:
        raise RuntimeError("Expected C60 coordinates (60,3) and 90 bonds.")
    # Remove center-of-mass translation without changing the radius.
    x_start=x_start-x_start.mean(axis=0)
    radius2=float(np.sum(x_start*x_start))
    radius=float(np.sqrt(radius2/60.0))
    n=x_start.size
    def objective(z):
        e,g=coulomb_energy_gradient(z.reshape(60,3))
        return e,g.reshape(-1)
    def constraints(z):
        x=z.reshape(60,3)
        return np.r_[x.sum(axis=0), 0.5*(np.sum(x*x)-radius2)]
    def constraints_jac(z):
        x=z.reshape(60,3)
        J=np.zeros((4,n))
        J[0,0::3]=1; J[1,1::3]=1; J[2,2::3]=1
        J[3]=x.reshape(-1)
        return J
    opt=minimize(objective,x_start.reshape(-1),jac=True,method="SLSQP",
                 constraints={"type":"eq","fun":constraints,"jac":constraints_jac},
                 options={"maxiter":args.max_iterations,"ftol":1e-12,"disp":False})
    x=opt.x.reshape(60,3)
    E,g=coulomb_energy_gradient(x)
    Q=tangent_basis(x)
    # KKT multipliers for the three COM constraints and fixed-radius constraint.
    J=constraints_jac(opt.x)
    multipliers=np.linalg.lstsq(J.T,-g.reshape(-1),rcond=None)[0]
    kkt_res=float(np.linalg.norm(g.reshape(-1)+J.T@multipliers))
    tangent_res=float(np.linalg.norm(Q.T@g.reshape(-1)))
    lam=float(multipliers[3])
    H=coulomb_hessian(x)
    HL=H+lam*np.eye(n)
    K=Q.T@HL@Q
    eig=np.linalg.eigvalsh((K+K.T)/2)
    sym=symmetry_audit(x,symmetry_matrices_icosahedron())
    report={
      "status":"computed_by_script_when_run",
      "optimization":{
        "method":"SLSQP with analytic gradient",
        "success":bool(opt.success),"status":int(opt.status),"message":str(opt.message),
        "iterations":int(opt.nit),"objective_evaluations":int(opt.nfev),
        "coulomb_energy":float(E),"fixed_rms_radius":radius,
        "center_of_mass_norm":float(np.linalg.norm(x.mean(axis=0))),
        "radius_constraint_abs_residual":float(abs(np.sum(x*x)-radius2)),
        "tangent_gradient_norm":tangent_res,
        "full_kkt_residual":kkt_res,
        "constraint_multipliers_translation":multipliers[:3].tolist(),
        "constraint_multiplier_radius":lam,
        "tangent_dimension":int(Q.shape[1])
      },
      "lagrangian_hessian":{
        "definition":"Q.T @ (H_Coulomb + lambda_radius * I) @ Q; translation constraints are linear",
        "min_eigenvalue":float(eig[0]),"max_eigenvalue":float(eig[-1]),
        "negative_modes":int(np.sum(eig < -1e-7)),
        "near_zero_modes":int(np.sum(np.abs(eig)<=1e-7)),
        "positive_modes":int(np.sum(eig > 1e-7)),
        "expected_rotational_zero_modes":3
      },
      "symmetry":sym,
      "model":model,
      "limitations":[
        "This is a classical equal-charge Thomson-type optimization on a sphere at the MMFF-relaxed RMS radius, not an electronic-structure calculation.",
        "SLSQP success alone is insufficient: interpret the constrained Hessian only if both tangent_gradient_norm and full_kkt_residual meet the stated numerical tolerance.",
        "The Hessian spectrum is local to the obtained stationary configuration; a local minimum claim additionally requires no negative modes after accounting for rotational zero modes.",
        "The symmetry test uses optimal point assignments for the 120 ideal icosahedral orthogonal operations; it does not infer irreducible-representation labels."
      ],
      "classification":"numerically_verified_equilibrium" if opt.success and tangent_res<1e-7 and kkt_res<1e-7 else "stationarity_not_established"
    }
    np.savez_compressed(out/"C60_Coulomb_constrained_equilibrium.npz",
      X_start=x_start,X_equilibrium=x,bonds=bonds,Q_tangent=Q,
      H_coulomb=H,H_lagrangian=HL,K_lagrangian=K,eigenvalues=eig,
      gradient=g,multipliers=multipliers)
    (out/"report.json").write_text(json.dumps(report,indent=2)+"\\n")
    print(json.dumps(report,indent=2))
    if not opt.success: sys.exit(2)

if __name__=="__main__": main()
