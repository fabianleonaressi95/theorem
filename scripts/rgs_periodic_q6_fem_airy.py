#!/usr/bin/env python3
"""Periodic Q6 quotient / Q1 FEM / spectral Airy comparison on a 2-torus.

The 4x4 Q6 quotient is compared with a periodic Q1 finite-element cell on the
same physical torus [0,4]^2. A Fourier Airy solver provides an independent
periodic continuum reference. Smooth periodic eigenstrain sources are used;
this is not a singular dislocation-core calculation.
"""
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=ROOT/"scripts"
for _p in (str(ROOT),str(SCRIPTS)):
    if _p not in sys.path: sys.path.insert(0,_p)
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

from rgs_defect_benchmark import q1_B, elasticity_tensor
from q6_prism_kinematic_map import (
    build_q6_complex, lift_displacement, cell_gradient_samples
)

LENGTH = 4.0


def periodic_source(n: int, kind: str, amplitude: float = 0.02,
                    width: float = 0.65) -> np.ndarray:
    """Cell-centred engineering eigenstrain [exx, eyy, gamma_xy]."""
    h = LENGTH / n
    c = (np.arange(n) + 0.5) * h
    X, Y = np.meshgrid(c, c)
    def bump(x0, y0):
        dx = (X - x0 + LENGTH/2) % LENGTH - LENGTH/2
        dy = (Y - y0 + LENGTH/2) % LENGTH - LENGTH/2
        return np.exp(-0.5*((dx/width)**2 + (dy/width)**2))
    eps = np.zeros((n,n,3), float)
    if kind == "shear_inclusion":
        eps[:,:,2] = amplitude*bump(2.0,2.0)
    elif kind == "shear_dipole":
        eps[:,:,2] = amplitude*(bump(1.4,2.0)-bump(2.6,2.0))
    else:
        raise ValueError(kind)
    return eps


def periodic_q1_solve(n: int, kind: str, lam: float=1.0, mu: float=1.0,
                      amplitude: float=0.02, width: float=0.65,
                      return_fields: bool=True) -> dict:
    """Periodic Q1 FEM on [0,LENGTH]^2; translations fixed at one vertex."""
    h = LENGTH/n
    epsp = periodic_source(n, kind, amplitude, width)
    C = elasticity_tensor(lam,mu)
    ndof = 2*n*n
    rows=[]; cols=[]; vals=[]
    rhs=np.zeros(ndof,float)
    def node(i,j): return (j % n)*n+(i % n)
    gp=(-1/np.sqrt(3),1/np.sqrt(3))
    for j in range(n):
        for i in range(n):
            ids=[node(i,j),node(i+1,j),node(i+1,j+1),node(i,j+1)]
            dofs=np.array([d for a in ids for d in (2*a,2*a+1)],int)
            Ke=np.zeros((8,8)); fe=np.zeros(8)
            for xi in gp:
                for eta in gp:
                    B=q1_B(h,xi,eta)
                    wdet=h*h/4
                    Ke += wdet*(B.T@C@B)
                    fe += wdet*(B.T@C@epsp[j,i])
            rr,cc=np.meshgrid(dofs,dofs,indexing="ij")
            rows.extend(rr.ravel()); cols.extend(cc.ravel()); vals.extend(Ke.ravel())
            rhs[dofs]+=fe
    K=coo_matrix((vals,(rows,cols)),shape=(ndof,ndof)).tocsr()
    fixed=np.array([0,1],int)
    free=np.setdiff1d(np.arange(ndof),fixed)
    u=np.zeros(ndof,float)
    u[free]=spsolve(K[free][:,free],rhs[free])
    energy=0.0
    stress=np.zeros((n,n,3)); strain=np.zeros_like(stress)
    for j in range(n):
        for i in range(n):
            ids=[node(i,j),node(i+1,j),node(i+1,j+1),node(i,j+1)]
            dofs=np.array([d for a in ids for d in (2*a,2*a+1)],int)
            e=q1_B(h,0.0,0.0)@u[dofs]-epsp[j,i]
            stress[j,i]=C@e
            strain[j,i]=e
            for xi in gp:
                for eta in gp:
                    ee=q1_B(h,xi,eta)@u[dofs]-epsp[j,i]
                    energy += 0.5*(h*h/4)*float(ee@C@ee)
    residual=K@u-rhs
    relres=float(np.linalg.norm(residual[free])/max(np.linalg.norm(rhs[free]),1e-30))
    out={"n":n,"h":h,"case":kind,"q1_energy":float(energy),
         "q1_relative_free_residual":relres,
         "mean_stress":[float(x) for x in stress.mean(axis=(0,1))]}
    if return_fields:
        out["displacement"]=u.reshape(n,n,2)
        out["stress_cells"]=stress
        out["strain_cells"]=strain
        out["eigenstrain_cells"]=epsp
    return out


def periodic_airy_spectral(epsp: np.ndarray, lam: float=1.0,
                           mu: float=1.0) -> dict:
    """Fourier Airy solution on the torus, including the mean stress mode."""
    n=epsp.shape[0]
    if epsp.shape != (n,n,3):
        raise ValueError("epsp must have shape (n,n,3)")
    E,nu=(mu*(3*lam+2*mu)/(lam+mu),
          lam/(2*(lam+mu)))
    c=(1-nu*nu)/E
    C=elasticity_tensor(lam,mu)
    exx=np.fft.fft2(epsp[:,:,0])
    eyy=np.fft.fft2(epsp[:,:,1])
    gam=np.fft.fft2(epsp[:,:,2])
    k=(2*np.pi)*np.fft.fftfreq(n,d=LENGTH/n)
    kx=k[None,:]; ky=k[:,None]
    k2=kx*kx+ky*ky
    inc_hat=-(ky*ky)*exx-(kx*kx)*eyy+(kx*ky)*gam
    phi_hat=np.zeros((n,n),complex)
    mask=k2>0
    phi_hat[mask]=-inc_hat[mask]/(c*k2[mask]**2)
    sxx=np.fft.ifft2(-(ky*ky)*phi_hat).real
    syy=np.fft.ifft2(-(kx*kx)*phi_hat).real
    sxy=np.fft.ifft2((kx*ky)*phi_hat).real
    stress=np.stack((sxx,syy,sxy),axis=-1)
    mean_stress=-(C@epsp.mean(axis=(0,1)))
    stress += mean_stress[None,None,:]
    invC=np.linalg.inv(C)
    strain=np.einsum("ab,ijb->ija",invC,stress)
    h=LENGTH/n
    energy=float(0.5*np.sum(stress*strain)*h*h)
    residual=c*k2*k2*phi_hat+inc_hat
    residual[~mask]=0
    relres=float(np.linalg.norm(residual)/max(np.linalg.norm(inc_hat[mask]),1e-30))
    return {"airy_energy":energy,"stress_cells":stress,"strain_cells":strain,
            "mean_stress":[float(x) for x in mean_stress],
            "airy_spectral_compatibility_residual":relres}


def q6_lift_energy(u4: np.ndarray, epsp4: np.ndarray, lam=1.0, mu=1.0):
    """Evaluate the periodic Q1 energy after lifting the 4x4 field to Q6."""
    u4=np.asarray(u4,dtype=float).reshape(16,2)
    epsp4=np.asarray(epsp4,dtype=float).reshape(4,4,3)
    c=build_q6_complex()
    lifted=lift_displacement(u4,c)
    edge_q6=c["d0"]@lifted
    edge_base=c["d0_base"]@u4
    pullback=edge_q6-c["p1"]@edge_base
    grad=cell_gradient_samples(u4,c)
    eng=np.stack((grad[:,:,0,0],grad[:,:,1,1],
                  grad[:,:,0,1]+grad[:,:,1,0]),axis=-1)
    elastic=eng-epsp4.reshape(16,1,3)
    C=elasticity_tensor(lam,mu)
    density=0.5*np.einsum("...i,ij,...j->...",elastic,C,elastic)
    # Quotient cells have side length one; 2x2 Gauss weights sum to four.
    energy=float(0.25*np.sum(density))
    return energy,float(np.max(np.abs(pullback))),lifted


def compare(levels=(4,8,16,32), kinds=("shear_inclusion","shear_dipole")):
    rows=[]
    for kind in kinds:
        for n in levels:
            q=periodic_q1_solve(n,kind,return_fields=True)
            a=periodic_airy_spectral(q["eigenstrain_cells"])
            ds=q["stress_cells"]-a["stress_cells"]
            de=q["strain_cells"]-a["strain_cells"]
            row={"n":n,"case":kind,"q1_energy":q["q1_energy"],
                 "airy_energy":a["airy_energy"],
                 "relative_energy_difference":abs(q["q1_energy"]-a["airy_energy"])/max(abs(q["q1_energy"]),abs(a["airy_energy"]),1e-30),
                 "stress_relative_l2":float(np.linalg.norm(ds)/max(np.linalg.norm(a["stress_cells"]),1e-30)),
                 "strain_relative_l2":float(np.linalg.norm(de)/max(np.linalg.norm(a["strain_cells"]),1e-30)),
                 "q1_residual":q["q1_relative_free_residual"],
                 "airy_residual":a["airy_spectral_compatibility_residual"]}
            if n==4:
                e6,pb,lifted=q6_lift_energy(q["displacement"],q["eigenstrain_cells"])
                row["q6_lift_energy"]=e6
                row["q6_q1_energy_relative_difference"]=abs(e6-q["q1_energy"])/max(abs(e6),abs(q["q1_energy"]),1e-30)
                row["q6_chain_pullback_max_abs"]=pb
                row["q6_lift_shape"]=list(lifted.shape)
            rows.append(row)
    return {"title":"Periodic Q6 quotient / Q1 FEM / spectral Airy comparison",
            "domain":[0.0,LENGTH,0.0,LENGTH],
            "material":{"lambda":1.0,"mu":1.0},
            "boundary":"periodic displacement; translation gauge fixed at one vertex; periodic Airy with mean stress mode restored",
            "source":"smooth periodic cell-centred shear eigenstrain; no singular core",
            "levels":list(levels),"results":rows,
            "limitations":["Q6 quotient is exactly the 4x4 periodic cell; higher n are Q1 refinements, not larger Q6 graphs",
                           "Q6-to-Q1 energy equality checks the pullback of the chosen periodic Q1 energy, not a new constitutive law",
                           "spectral Airy is an independent periodic continuum reference",
                           "smooth sources only; no periodic Volterra/disclination core or material calibration"]}


def run(out: Path):
    out.mkdir(parents=True,exist_ok=True)
    report=compare()
    (out/"periodic_q6_fem_airy.json").write_text(json.dumps(report,indent=2)+"\n")
    with (out/"periodic_q6_fem_airy.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(report["results"][0]))
        w.writeheader(); w.writerows(report["results"])
    return report


def self_test():
    report=compare(levels=(4,8,16))
    for kind in ("shear_inclusion","shear_dipole"):
        rows=[r for r in report["results"] if r["case"]==kind]
        assert rows[0]["q6_q1_energy_relative_difference"]<1e-12,rows[0]
        assert rows[0]["q6_chain_pullback_max_abs"]<1e-12,rows[0]
        assert rows[-1]["relative_energy_difference"]<rows[0]["relative_energy_difference"],rows
        assert rows[-1]["stress_relative_l2"]<rows[0]["stress_relative_l2"],rows
        assert max(r["q1_residual"] for r in rows)<1e-8,rows
        assert max(r["airy_residual"] for r in rows)<1e-10,rows
    return {"periodic_q6_energy_pullback":"PASS",
            "periodic_q1_to_spectral_airy_refinement":"PASS"}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="artifacts/periodic_q6_fem_airy")
    p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    if a.self_test:
        print(json.dumps(self_test(),indent=2))
    else:
        r=run(Path(a.out))
        print(json.dumps({"rows":len(r["results"]),"levels":r["levels"],"output":a.out},indent=2))


if __name__=="__main__":
    main()
