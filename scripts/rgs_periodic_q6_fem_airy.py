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




def periodic_triangle_complex(n: int, diagonal: str="sw_ne"):
    """Sparse integer incidence matrices for the periodic triangulated torus."""
    if n<3:
        raise ValueError("periodic triangulation requires n >= 3")
    def node(i,j): return (j % n)*n+(i % n)
    faces=[]
    for j in range(n):
        for i in range(n):
            a,b,c,d=node(i,j),node(i+1,j),node(i+1,j+1),node(i,j+1)
            if diagonal=="sw_ne":
                faces.extend(((a,b,c),(a,c,d)))
            elif diagonal=="se_nw":
                faces.extend(((a,b,d),(b,c,d)))
            else:
                raise ValueError(diagonal)
    edge_set=set()
    for tri in faces:
        for a,b in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])):
            edge_set.add((min(a,b),max(a,b)))
    edges=sorted(edge_set)
    edge_id={e:k for k,e in enumerate(edges)}
    d0r=[]; d0c=[]; d0v=[]
    for k,(a,b) in enumerate(edges):
        d0r.extend((k,k)); d0c.extend((a,b)); d0v.extend((-1,1))
    D0=coo_matrix((d0v,(d0r,d0c)),shape=(len(edges),n*n),dtype=np.int64).tocsr()
    d1r=[]; d1c=[]; d1v=[]
    for f,tri in enumerate(faces):
        for a,b in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])):
            d1r.append(f)
            d1c.append(edge_id[(min(a,b),max(a,b))])
            d1v.append(1 if a<b else -1)
    D1=coo_matrix((d1v,(d1r,d1c)),shape=(len(faces),len(edges)),dtype=np.int64).tocsr()
    if (D1@D0).nnz:
        raise AssertionError("periodic P1 incidence matrices violate D1 D0 = 0")
    return edges,faces,D0,D1

def periodic_tri_B(points: np.ndarray) -> np.ndarray:
    """Engineering-strain matrix for a linear triangle with unwrapped coordinates."""
    coeff=np.linalg.inv(np.column_stack((np.ones(3),points)))
    gx,gy=coeff[1,:],coeff[2,:]
    B=np.zeros((3,6),float)
    for a in range(3):
        B[0,2*a]=gx[a]
        B[1,2*a+1]=gy[a]
        B[2,2*a]=gy[a]
        B[2,2*a+1]=gx[a]
    return B


def periodic_p1_energy(u: np.ndarray, epsp: np.ndarray, diagonal: str="sw_ne",
                       lam: float=1.0, mu: float=1.0) -> float:
    """Energy of the periodic P1 triangulation using a nodal displacement."""
    n=epsp.shape[0]
    if u.shape!=(n*n,2):
        raise ValueError("u must have shape (n*n,2)")
    h=LENGTH/n
    C=elasticity_tensor(lam,mu)
    energy=0.0
    def node(i,j): return (j % n)*n+(i % n)
    for j in range(n):
        for i in range(n):
            ids=(node(i,j),node(i+1,j),node(i+1,j+1),node(i,j+1))
            pts=np.array(((i*h,j*h),((i+1)*h,j*h),
                          ((i+1)*h,(j+1)*h),(i*h,(j+1)*h)),float)
            if diagonal=="sw_ne":
                triangles=((0,1,2),(0,2,3))
            elif diagonal=="se_nw":
                triangles=((0,1,3),(1,2,3))
            else:
                raise ValueError(diagonal)
            for tri in triangles:
                local_ids=np.array([ids[k] for k in tri],int)
                B=periodic_tri_B(pts[list(tri)])
                dofs=np.array([d for a in local_ids for d in (2*a,2*a+1)],int)
                e=B@u.reshape(-1)[dofs]-epsp[j,i]
                energy += 0.5*(h*h/2)*float(e@C@e)
    return float(energy)


def periodic_p1_solve(n: int, kind: str, diagonal: str="sw_ne",
                       lam: float=1.0, mu: float=1.0,
                       amplitude: float=0.02, width: float=0.65,
                       return_fields: bool=True) -> dict:
    """Periodic P1 simplicial/cochain elasticity on the same torus as Q1/Airy.

    The triangle diagonal is a derived edge coboundary between existing
    quotient vertices; it introduces no additional displacement DOFs.
    """
    h=LENGTH/n
    epsp=periodic_source(n,kind,amplitude,width)
    edges,faces,D0,D1=periodic_triangle_complex(n,diagonal)
    C=elasticity_tensor(lam,mu)
    ndof=2*n*n
    rows=[]; cols=[]; vals=[]
    rhs=np.zeros(ndof,float)
    def node(i,j): return (j % n)*n+(i % n)
    for j in range(n):
        for i in range(n):
            ids=(node(i,j),node(i+1,j),node(i+1,j+1),node(i,j+1))
            pts=np.array(((i*h,j*h),((i+1)*h,j*h),
                          ((i+1)*h,(j+1)*h),(i*h,(j+1)*h)),float)
            triangles=((0,1,2),(0,2,3)) if diagonal=="sw_ne" else ((0,1,3),(1,2,3))
            for tri in triangles:
                local_ids=np.array([ids[k] for k in tri],int)
                B=periodic_tri_B(pts[list(tri)])
                area=h*h/2
                dofs=np.array([d for a in local_ids for d in (2*a,2*a+1)],int)
                Ke=area*(B.T@C@B)
                fe=area*(B.T@C@epsp[j,i])
                rr,cc=np.meshgrid(dofs,dofs,indexing="ij")
                rows.extend(rr.ravel()); cols.extend(cc.ravel()); vals.extend(Ke.ravel())
                rhs[dofs]+=fe
    K=coo_matrix((vals,(rows,cols)),shape=(ndof,ndof)).tocsr()
    # Periodic displacement has two translational zero modes; no rotational
    # gauge is admissible as a periodic affine rotation is not periodic.
    fixed=np.array([0,1],int)
    free=np.setdiff1d(np.arange(ndof),fixed)
    u=np.zeros(ndof,float)
    u[free]=spsolve(K[free][:,free],rhs[free])
    residual=K@u-rhs
    relres=float(np.linalg.norm(residual[free])/max(np.linalg.norm(rhs[free]),1e-30))
    energy=periodic_p1_energy(u.reshape(n*n,2),epsp,diagonal,lam,mu)
    stress=np.zeros((n,n,3),float)
    strain=np.zeros_like(stress)
    def node(i,j): return (j % n)*n+(i % n)
    for j in range(n):
        for i in range(n):
            ids=(node(i,j),node(i+1,j),node(i+1,j+1),node(i,j+1))
            pts=np.array(((i*h,j*h),((i+1)*h,j*h),
                          ((i+1)*h,(j+1)*h),(i*h,(j+1)*h)),float)
            triangles=((0,1,2),(0,2,3)) if diagonal=="sw_ne" else ((0,1,3),(1,2,3))
            for tri in triangles:
                local_ids=np.array([ids[k] for k in tri],int)
                B=periodic_tri_B(pts[list(tri)])
                dofs=np.array([d for a in local_ids for d in (2*a,2*a+1)],int)
                e=B@u[dofs]-epsp[j,i]
                strain[j,i]+=0.5*e
                stress[j,i]+=0.5*(C@e)
    out={"n":n,"h":h,"case":kind,"diagonal":diagonal,
         "p1_vertices":n*n,"p1_edges":len(edges),"p1_triangles":len(faces),
         "p1_chain_boundary_of_boundary_max_abs":int(np.max(np.abs((D1@D0).data))) if (D1@D0).nnz else 0,
         "p1_energy":energy,"p1_relative_free_residual":relres,
         "p1_mean_stress":[float(x) for x in stress.mean(axis=(0,1))]}
    if return_fields:
        out["displacement"]=u.reshape(n*n,2)
        out["stress_cells"]=stress
        out["strain_cells"]=strain
        out["eigenstrain_cells"]=epsp
    return out


def q6_lift_p1_audit(u4: np.ndarray, epsp4: np.ndarray,
                     diagonal: str="sw_ne", lam: float=1.0, mu: float=1.0):
    """Check P1 energy and edge coboundary after lifting quotient DOFs to Q6."""
    c=build_q6_complex()
    lifted=lift_displacement(np.asarray(u4).reshape(16,2),c)
    edge_q6=c["d0"]@lifted
    edge_base=c["d0_base"]@np.asarray(u4).reshape(16,2)
    pullback=edge_q6-c["p1"]@edge_base
    # Recover one representative from each fibre, then evaluate the same
    # quotient triangulation; the energy is invariant under the exact lift.
    representatives=np.array([np.flatnonzero(c["pi"]==k)[0] for k in range(16)])
    recovered=lifted[representatives]
    energy=periodic_p1_energy(recovered,np.asarray(epsp4).reshape(4,4,3),
                              diagonal,lam,mu)
    return energy,float(np.max(np.abs(pullback))),lifted


def compare(levels=(4,8,16,32), kinds=("shear_inclusion","shear_dipole")):
    rows=[]
    for kind in kinds:
        for n in levels:
            q=periodic_q1_solve(n,kind,return_fields=True)
            a=periodic_airy_spectral(q["eigenstrain_cells"])
            p1a=periodic_p1_solve(n,kind,diagonal="sw_ne",return_fields=True)
            p1b=periodic_p1_solve(n,kind,diagonal="se_nw",return_fields=True)
            ds=q["stress_cells"]-a["stress_cells"]
            de=q["strain_cells"]-a["strain_cells"]
            dps=p1a["stress_cells"]-a["stress_cells"]
            dpe=p1a["strain_cells"]-a["strain_cells"]
            row={"n":n,"case":kind,"q1_energy":q["q1_energy"],
                 "p1_energy":p1a["p1_energy"],"airy_energy":a["airy_energy"],
                 "q1_airy_relative_energy_difference":abs(q["q1_energy"]-a["airy_energy"])/max(abs(q["q1_energy"]),abs(a["airy_energy"]),1e-30),
                 "p1_airy_relative_energy_difference":abs(p1a["p1_energy"]-a["airy_energy"])/max(abs(p1a["p1_energy"]),abs(a["airy_energy"]),1e-30),
                 "q1_p1_relative_energy_difference":abs(q["q1_energy"]-p1a["p1_energy"])/max(abs(q["q1_energy"]),abs(p1a["p1_energy"]),1e-30),
                 "q1_stress_relative_l2":float(np.linalg.norm(ds)/max(np.linalg.norm(a["stress_cells"]),1e-30)),
                 "q1_strain_relative_l2":float(np.linalg.norm(de)/max(np.linalg.norm(a["strain_cells"]),1e-30)),
                 "p1_stress_relative_l2":float(np.linalg.norm(dps)/max(np.linalg.norm(a["stress_cells"]),1e-30)),
                 "p1_strain_relative_l2":float(np.linalg.norm(dpe)/max(np.linalg.norm(a["strain_cells"]),1e-30)),
                 "p1_diagonal_energy_relative_difference":abs(p1a["p1_energy"]-p1b["p1_energy"])/max(abs(p1a["p1_energy"]),abs(p1b["p1_energy"]),1e-30),
                 "q1_residual":q["q1_relative_free_residual"],
                 "p1_residual":p1a["p1_relative_free_residual"],
                 "p1_chain_residual":p1a["p1_chain_boundary_of_boundary_max_abs"],
                 "p1_vertices":p1a["p1_vertices"],"p1_edges":p1a["p1_edges"],
                 "p1_triangles":p1a["p1_triangles"],
                 "airy_residual":a["airy_spectral_compatibility_residual"]}
            if n==4:
                e6q,pbq,liftedq=q6_lift_energy(q["displacement"],q["eigenstrain_cells"])
                e6p,pbp,liftedp=q6_lift_p1_audit(p1a["displacement"],p1a["eigenstrain_cells"],"sw_ne")
                row["q6_lift_q1_energy"]=e6q
                row["q6_q1_energy_relative_difference"]=abs(e6q-q["q1_energy"])/max(abs(e6q),abs(q["q1_energy"]),1e-30)
                row["q6_lift_p1_energy"]=e6p
                row["q6_p1_energy_relative_difference"]=abs(e6p-p1a["p1_energy"])/max(abs(e6p),abs(p1a["p1_energy"]),1e-30)
                row["q6_q1_chain_pullback_max_abs"]=pbq
                row["q6_p1_chain_pullback_max_abs"]=pbp
                row["q6_lift_shape"]=list(liftedq.shape)
            rows.append(row)
    return {"title":"Periodic Q6 quotient / Q1 FEM / P1 cochain / spectral Airy comparison",
            "domain":[0.0,LENGTH,0.0,LENGTH],
            "material":{"lambda":1.0,"mu":1.0},
            "boundary":"periodic displacement; translation gauge fixed at one vertex; periodic Airy with mean stress mode restored",
            "source":"identical smooth periodic cell-centred shear eigenstrain for Q1, P1 and Airy; no singular core",
            "levels":list(levels),"results":rows,
            "limitations":["Q6 quotient is exactly the 4x4 periodic cell; higher n are Q1/P1 refinements, not larger Q6 graphs",
                           "P1 triangle diagonal is a derived coboundary between existing quotient vertices, not an additional Q6 graph edge",
                           "Q6-to-P1 energy equality checks the lift of the same quotient displacement and energy, not a new constitutive law",
                           "spectral Airy is an independent periodic continuum reference",
                           "smooth sources only; no periodic Volterra/disclination core or material calibration"]}


def self_test():
    report=compare(levels=(4,8,16))
    for kind in ("shear_inclusion","shear_dipole"):
        rows=[r for r in report["results"] if r["case"]==kind]
        assert rows[0]["q6_q1_energy_relative_difference"]<1e-12,rows[0]
        assert rows[0]["q6_p1_energy_relative_difference"]<1e-12,rows[0]
        assert rows[0]["q6_q1_chain_pullback_max_abs"]<1e-12,rows[0]
        assert rows[0]["q6_p1_chain_pullback_max_abs"]<1e-12,rows[0]
        assert rows[-1]["q1_airy_relative_energy_difference"]<rows[0]["q1_airy_relative_energy_difference"],rows
        assert rows[-1]["p1_airy_relative_energy_difference"]<rows[0]["p1_airy_relative_energy_difference"],rows
        assert rows[-1]["q1_stress_relative_l2"]<rows[0]["q1_stress_relative_l2"],rows
        assert rows[-1]["p1_stress_relative_l2"]<rows[0]["p1_stress_relative_l2"],rows
        assert max(r["q1_residual"] for r in rows)<1e-8,rows
        assert max(r["p1_residual"] for r in rows)<1e-8,rows
        assert max(r["p1_chain_residual"] for r in rows)==0,rows
        assert max(r["airy_residual"] for r in rows)<1e-10,rows
        assert max(r["p1_diagonal_energy_relative_difference"] for r in rows)<1e-12,rows
    return {"periodic_q6_q1_p1_energy_pullback":"PASS",
            "periodic_q1_and_p1_to_spectral_airy_refinement":"PASS",
            "both_triangle_diagonals":"PASS"}


def run(out: Path):
    out.mkdir(parents=True,exist_ok=True)
    report=compare()
    (out/"periodic_q6_fem_airy.json").write_text(json.dumps(report,indent=2)+"\n")
    with (out/"periodic_q6_fem_airy.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(report["results"][0]))
        w.writeheader(); w.writerows(report["results"])
    return report


# The single self_test above is the canonical periodic Q6/Q1/P1/Airy audit.
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
