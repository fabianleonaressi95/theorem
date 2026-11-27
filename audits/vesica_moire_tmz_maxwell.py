#!/usr/bin/env python3
"""2-D TM_z Maxwell eigenproblem with an explicitly assumed Vesica-Moire dielectric.

This is a polarization-reduced Maxwell model, not a full 3-D solver.
Dependencies: numpy, scipy; matplotlib is optional for --plot.
"""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
import numpy as np
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import eigsh

def phase_field(n, length, a, grating_k):
    if n < 2 or length <= 0 or a <= 0 or grating_k <= 0:
        raise ValueError("Require n>=2 and positive length, a, grating_k.")
    h = length / (n + 1)
    x = np.linspace(-length / 2 + h, length / 2 - h, n)
    X, Y = np.meshgrid(x, x, indexing="ij")
    dphi = grating_k * (np.hypot(X + a, Y) - np.hypot(X - a, Y))
    return X, Y, dphi, h

def tmz_matrices(n=24, length=8.0, a=1.0, grating_k=np.pi/2, modulation=0.10):
    """Build K e=(omega/c)^2 M_eps e for TM_z, PEC E_z=0, mu_r=1."""
    if not abs(modulation) < 1:
        raise ValueError("Require |modulation| < 1 so eps_r stays positive.")
    X, Y, dphi, h = phase_field(n, length, a, grating_k)
    eps_r = 1.0 + modulation * np.cos(dphi)
    if np.min(eps_r) <= 0:
        raise ValueError("Relative permittivity must be strictly positive.")
    T = diags([-np.ones(n-1), 2*np.ones(n), -np.ones(n-1)], [-1,0,1], format="csr")
    I = eye(n, format="csr")
    K = (kron(T,I) + kron(I,T)) / h**2
    M = diags(eps_r.ravel(), format="csr")
    return {"X":X,"Y":Y,"delta_phi":dphi,"eps_r":eps_r,"h":h,"K":K.tocsr(),"M":M.tocsr()}

def analytic_uniform_eigenvalues(n, h, count):
    vals = [4/h**2*(np.sin(p*np.pi/(2*(n+1)))**2 + np.sin(q*np.pi/(2*(n+1)))**2)
            for p in range(1,n+1) for q in range(1,n+1)]
    return np.sort(np.asarray(vals))[:count]

def generalized_spectrum(K, M, count=9):
    size=K.shape[0]
    if count < 1 or count >= size:
        raise ValueError("count must satisfy 1 <= count < number of grid unknowns.")
    vals=eigsh(K,k=count,M=M,sigma=0.0,which="LM",tol=1e-10,
               maxiter=max(2000,30*size),return_eigenvectors=False)
    vals=np.sort(np.real(vals))
    if vals[0] <= 0: raise RuntimeError("PEC Dirichlet spectrum should be strictly positive.")
    return vals

def run(n=24,length=8.0,a=1.0,grating_k=np.pi/2,modulation=0.10,modes=9):
    d=tmz_matrices(n,length,a,grating_k,modulation)
    K,M=d["K"],d["M"]
    M0=diags(np.ones(n*n),format="csr")
    u=generalized_spectrum(K,M0,modes)
    m=generalized_spectrum(K,M,modes)
    rows=[{"mode":i,"lambda_uniform":float(x),"lambda_moire":float(y),
           "omega_over_c_uniform":float(np.sqrt(x)),"omega_over_c_moire":float(np.sqrt(y)),
           "frequency_shift_percent":float(100*(np.sqrt(y/x)-1))}
          for i,(x,y) in enumerate(zip(u,m),1)]
    exact=analytic_uniform_eigenvalues(n,d["h"],modes)
    return {"model":"2-D TM_z polarization-reduced Maxwell eigenproblem",
      "equation":"K e = (omega/c)^2 M_eps e; PEC E_z=0; mu_r=1",
      "constitutive_ansatz":"eps_r(x,y)=1+modulation*cos(k_g*(rho1-rho2))",
      "parameters":{"n_interior":n,"length":length,"a":a,"grating_k":grating_k,
        "modulation":modulation,"grid_spacing":d["h"],"modes":modes,
        "boundary":"perfect electric conductor; Dirichlet E_z=0","mu_relative":1.0},
      "relative_permittivity_range":[float(d["eps_r"].min()),float(d["eps_r"].max())],
      "uniform_discrete_eigenvalues":u.tolist(),"uniform_analytic_eigenvalues":exact.tolist(),
      "moire_generalized_eigenvalues":m.tolist(),
      "uniform_analytic_max_abs_error":float(np.max(np.abs(u-exact))),
      "mode_comparison":rows,
      "interpretation":"Dimensionless TM_z Maxwell polarization model with an assumed positive dielectric modulation. It does not derive eps_r from the Vesica, model full 3-D vector Maxwell, or predict optical frequencies."}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--n",type=int,default=24); p.add_argument("--length",type=float,default=8.0)
    p.add_argument("--a",type=float,default=1.0); p.add_argument("--grating-k",type=float,default=float(np.pi/2))
    p.add_argument("--modulation",type=float,default=0.10); p.add_argument("--modes",type=int,default=9)
    p.add_argument("--output-dir",type=Path,default=Path("results/vesica_moire_tmz"))
    p.add_argument("--plot",action="store_true"); args=p.parse_args()
    report=run(args.n,args.length,args.a,args.grating_k,args.modulation,args.modes)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/"tmz_spectrum.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    with (args.output_dir/"tmz_spectrum.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(report["mode_comparison"][0])); w.writeheader(); w.writerows(report["mode_comparison"])
    if args.plot:
        import matplotlib.pyplot as plt
        d=tmz_matrices(args.n,args.length,args.a,args.grating_k,args.modulation)
        fig,ax=plt.subplots(figsize=(6,5))
        im=ax.contourf(d["X"],d["Y"],d["eps_r"],levels=32)
        ax.contour(d["X"],d["Y"],d["delta_phi"],levels=np.linspace(-np.pi,np.pi,13),colors="black",linewidths=.45)
        ax.set_aspect("equal"); ax.set_xlabel("x"); ax.set_ylabel("y")
        ax.set_title("TM_z dielectric coefficient: Vesica-Moire ansatz")
        fig.colorbar(im,ax=ax,label="relative permittivity eps_r"); fig.tight_layout()
        fig.savefig(args.output_dir/"tmz_dielectric_moire.png",dpi=180); plt.close(fig)
    print(json.dumps({"json":str(args.output_dir/"tmz_spectrum.json"),
      "csv":str(args.output_dir/"tmz_spectrum.csv"),
      "eps_r_range":report["relative_permittivity_range"],
      "uniform_analytic_max_abs_error":report["uniform_analytic_max_abs_error"],
      "frequency_shifts_percent":[r["frequency_shift_percent"] for r in report["mode_comparison"]],
      "status":"TM_z polarization-reduced Maxwell; assumed dielectric, not full 3-D"},indent=2))

if __name__=="__main__": main()
