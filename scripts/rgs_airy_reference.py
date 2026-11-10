#!/usr/bin/env python3
"""Airy-stress reference for regularized planar defect incompatibilities.

Solves c * Delta^2(v) = -inc(eps_p) on the unit square with clamped Airy
boundary data. On straight sides these are equivalent, modulo an affine
gauge, to zero traction: Hessian(v) t = 0. The associated Airy stress is
automatically divergence-free. This is a finite-difference reference, not
the CIP-DG method of Cesana et al.
"""
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix, bmat, csr_matrix
from scipy.sparse.linalg import spsolve
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

def material_constants(lam=1.0,mu=1.0):
    nu=lam/(2.0*(lam+mu))
    young=mu*(3.0*lam+2.0*mu)/(lam+mu)
    return young,nu,(1.0-nu*nu)/young

def plastic_strain_nodes(n,kind,burgers=.02,core_width=.025,frank=.01,dipole_separation=.1):
    h=1.0/(n-1)
    x=np.linspace(0,1,n); X,Y=np.meshgrid(x,x)
    # Put the cut tip halfway between the two nodal columns bracketing x=1/2.
    x0=.5+.5*h  # cut lies at the first Q1/cochain cell centre to the right of x=1/2
    e=np.zeros((n,n,3),float)
    delta=np.exp(-.5*((Y-.5)/core_width)**2)/(np.sqrt(2*np.pi)*core_width)
    if kind=="volterra_edge":
        e[:,:,2]=burgers*delta*(X>=x0)
    elif kind=="wedge_disclination":
        e[:,:,1]=frank*(X-x0)*delta*(X>=x0)
    elif kind=="wedge_dipole":
        dp=np.exp(-.5*((Y-(.5+dipole_separation/2))/core_width)**2)/(np.sqrt(2*np.pi)*core_width)
        dm=np.exp(-.5*((Y-(.5-dipole_separation/2))/core_width)**2)/(np.sqrt(2*np.pi)*core_width)
        e[:,:,1]=(burgers/dipole_separation)*(X-x0)*(X>=x0)*(dp-dm)
    else:
        raise ValueError("Airy incompatibility reference supports Volterra edge and wedge disclination")
    return e

def incompatibility(e,h):
    """Discrete inc(e)=dyy exx + dxx eyy - dxy gamma_xy."""
    exx,eyy,gamma=e[:,:,0],e[:,:,1],e[:,:,2]
    out=np.zeros(exx.shape,float)
    out[1:-1,1:-1]=(
        (exx[2:,1:-1]-2*exx[1:-1,1:-1]+exx[:-2,1:-1])/h**2
        +(eyy[1:-1,2:]-2*eyy[1:-1,1:-1]+eyy[1:-1,:-2])/h**2
        -(gamma[2:,2:]-gamma[2:,:-2]-gamma[:-2,2:]+gamma[:-2,:-2])/(4*h**2)
    )
    return out

def laplacian_interior_matrix(n,h):
    rows=[]; cols=[]; vals=[]
    def idx(i,j): return j*n+i
    row=0
    for j in range(1,n-1):
        for i in range(1,n-1):
            for ii,jj,val in ((i,j,-4/h**2),(i-1,j,1/h**2),(i+1,j,1/h**2),(i,j-1,1/h**2),(i,j+1,1/h**2)):
                rows.append(row); cols.append(idx(ii,jj)); vals.append(val)
            row+=1
    return coo_matrix((vals,(rows,cols)),shape=((n-2)**2,n*n)).tocsr()

def clamped_constraints(n,h):
    rows=[]; cols=[]; vals=[]; r=0
    def add(items):
        nonlocal r
        for k,v in items: rows.append(r); cols.append(k); vals.append(v)
        r+=1
    def idx(i,j): return j*n+i
    # v=0 on the complete boundary.
    boundary=[]
    for i in range(n): boundary.extend((idx(i,0),idx(i,n-1)))
    for j in range(1,n-1): boundary.extend((idx(0,j),idx(n-1,j)))
    for k in boundary: add(((k,1.0),))
    # One-sided second-order normal derivative: -3v0+4v1-v2=0.
    for i in range(2,n-2):
        add(((idx(i,0),-3/(2*h)),(idx(i,1),4/(2*h)),(idx(i,2),-1/(2*h))))
        add(((idx(i,n-1),3/(2*h)),(idx(i,n-2),-4/(2*h)),(idx(i,n-3),1/(2*h))))
    for j in range(2,n-2):
        add(((idx(0,j),-3/(2*h)),(idx(1,j),4/(2*h)),(idx(2,j),-1/(2*h))))
        add(((idx(n-1,j),3/(2*h)),(idx(n-2,j),-4/(2*h)),(idx(n-3,j),1/(2*h))))
    return coo_matrix((vals,(rows,cols)),shape=(r,n*n)).tocsr()

def solve_airy(n,kind,lam=1.0,mu=1.0,burgers=.02,core_width=.025,frank=.01,dipole_separation=.1,return_fields=False):
    h=1/(n-1); young,nu,c=material_constants(lam,mu)
    ep=plastic_strain_nodes(n,kind,burgers,core_width,frank,dipole_separation)
    incp=incompatibility(ep,h)
    L=laplacian_interior_matrix(n,h)
    K=(c*h*h)*(L.T@L)
    rhs=np.zeros(n*n,float)
    rhs.reshape(n,n)[1:-1,1:-1]=(-incp[1:-1,1:-1])*h*h
    C=clamped_constraints(n,h)
    saddle=bmat([[K,C.T],[C,None]],format="csc")
    sol=spsolve(saddle,np.concatenate((rhs,np.zeros(C.shape[0]))))
    v=sol[:n*n].reshape(n,n)
    vxx=np.zeros_like(v); vyy=np.zeros_like(v); vxy=np.zeros_like(v)
    vxx[1:-1,1:-1]=(v[1:-1,2:]-2*v[1:-1,1:-1]+v[1:-1,:-2])/h**2
    vyy[1:-1,1:-1]=(v[2:,1:-1]-2*v[1:-1,1:-1]+v[:-2,1:-1])/h**2
    vxy[1:-1,1:-1]=(v[2:,2:]-v[2:,:-2]-v[:-2,2:]+v[:-2,:-2])/(4*h*h)
    stress=np.zeros((n,n,3),float)
    stress[:,:,0]=vyy; stress[:,:,1]=vxx; stress[:,:,2]=-vxy
    # Plane-strain compliance: engineering strain [exx, eyy, gamma_xy].
    strain=np.zeros_like(stress)
    strain[:,:,0]=(1+nu)/young*((1-nu)*stress[:,:,0]-nu*stress[:,:,1])
    strain[:,:,1]=(1+nu)/young*((1-nu)*stress[:,:,1]-nu*stress[:,:,0])
    strain[:,:,2]=2*(1+nu)/young*stress[:,:,2]
    # Discrete weak residual on unconstrained degrees of freedom.
    weak=K@v.ravel()-rhs
    constrained=np.unique(C.indices)
    free=np.setdiff1d(np.arange(n*n),constrained)
    weak_res=float(np.linalg.norm(weak[free])/max(np.linalg.norm(rhs[free]),1e-30))
    # Check the source moments: wedge charge and Burgers first moment.
    xx=np.linspace(0,1,n); X,Y=np.meshgrid(xx,xx)
    if kind=="wedge_disclination":
        charge=float(np.sum(incp)*h*h)
        topological_error=abs(charge-frank)
        target=frank
    else:
        charge=float(np.sum(Y*incp)*h*h)
        topological_error=abs(charge-burgers)
        target=burgers
    result={"n":n,"case":kind,"young":young,"poisson":nu,"airy_coefficient":c,
        "incompatibility_moment":charge,"topological_target":target,
        "topological_moment_error":topological_error,"weak_residual":weak_res,
        "boundary":"traction-free Airy: clamped v and normal derivative on straight square boundary"}
    if return_fields:
        # Stress/strain at cell centres by averaging the four surrounding nodes.
        result["stress_cells"]=.25*(stress[:-1,:-1]+stress[1:,:-1]+stress[:-1,1:]+stress[1:,1:])
        result["strain_cells"]=.25*(strain[:-1,:-1]+strain[1:,:-1]+strain[:-1,1:]+strain[1:,1:])
        result["airy_nodes"]=v
    return result

def compare_case(n,kind,lam=1.0,mu=1.0,diagonal="sw_ne",dipole_separation=.1):
    from scripts.rgs_defect_benchmark import solve_case
    from scripts.rgs_cochain_defect_benchmark import solve_cochain
    q=solve_case(n,kind,lam,mu,return_fields=True,dipole_separation=dipole_separation)
    p=solve_cochain(n,kind,lam,mu,diagonal=diagonal,return_fields=True,dipole_separation=dipole_separation)
    a=solve_airy(n,kind,lam,mu,dipole_separation=dipole_separation,return_fields=True)
    # Compare away from the outer boundary, where finite-difference closure is least accurate.
    sl=(slice(3,-3),slice(3,-3))
    airy_energy=float(0.5*np.sum(a["stress_cells"]*a["strain_cells"])*((1.0/(n-1))**2))
    out={"n":n,"case":kind,"diagonal":diagonal,
        "q1_energy":q["energy"],"cochain_energy":p["energy"],"airy_energy":airy_energy,
        "q1_cochain_relative_energy_difference":abs(q["energy"]-p["energy"])/max(abs(q["energy"]),abs(p["energy"]),1e-30),
        "q1_airy_relative_energy_difference":abs(q["energy"]-airy_energy)/max(abs(q["energy"]),abs(airy_energy),1e-30),
        "cochain_airy_relative_energy_difference":abs(p["energy"]-airy_energy)/max(abs(p["energy"]),abs(airy_energy),1e-30),
        "airy_topological_moment_error":a["topological_moment_error"],
        "airy_weak_residual":a["weak_residual"]}
    for label,res in (("q1",q),("cochain",p)):
        ds=res["stress_cells"][sl]-a["stress_cells"][sl]
        ref=a["stress_cells"][sl]
        out[label+"_airy_stress_rel_l2"]=float(np.linalg.norm(ds)/max(np.linalg.norm(ref),1e-30))
        de=res["strain_cells"][sl]-a["strain_cells"][sl]
        eref=a["strain_cells"][sl]
        out[label+"_airy_strain_rel_l2"]=float(np.linalg.norm(de)/max(np.linalg.norm(eref),1e-30))
        out[label+"_free_residual"]=res["relative_free_residual"]
    return out

def run(out:Path,levels=(17,33,65)):
    out.mkdir(parents=True,exist_ok=True); rows=[]
    for n in levels:
        for kind in ("volterra_edge","wedge_disclination","wedge_dipole"):
            for diagonal in ("sw_ne","se_nw"):
                rows.append(compare_case(n,kind,diagonal=diagonal))
    # The narrow dipole core needs a finer grid: add a dedicated n=129 comparison.
    for diagonal in ("sw_ne","se_nw"):
        rows.append(compare_case(129,"wedge_dipole",diagonal=diagonal))
    report={"title":"Airy-stress reference versus displacement/cochain elasticity",
        "status":"finite-difference clamped-biharmonic reference; not the published CIP-DG implementation",
        "model":"c Delta^2 v = -inc(eps_p), sigma11=v_yy, sigma12=-v_xy, sigma22=v_xx",
        "boundary":"traction-free Airy condition on straight sides, equivalent modulo affine gauge to clamped Airy data",
        "comparison":"Q1 and P1-cochain energies against Airy stress-derived elastic energy; stress and strain relative L2 errors on interior cells (three-cell boundary margin). All three use the same regularized source parameters and traction-free boundary convention.",
        "limitations":["finite-difference Airy reference, not a reproduction of the paper's semi-discrete/CIP-DG solver",
            "the Airy nodal source and Q1/cochain cell-centred source are samples of the same regularized profile; residual quadrature/interpolation differences remain",
            "regularized core width fixed at 0.025; singular-core asymptotics not tested",
            "no Q6/PRISM-to-physical-mesh chain map",
            "no disclination dynamics or material calibration"],
        "levels":list(levels),"results":rows,"dipole_edge_equivalence":dipole_edge_equivalence()}
    (out/"airy_comparison.json").write_text(json.dumps(report,indent=2)+"\n")
    with (out/"airy_comparison.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    return report

def dipole_edge_equivalence(n=129,burgers=.002,core_width=.025,separations=(.1,.075,.05,.0375,.025)):
    """Compare a +/- wedge-dipole with its limiting edge-dislocation source."""
    h=1/(n-1)
    edge_ep=plastic_strain_nodes(n,"volterra_edge",burgers=burgers,core_width=core_width)
    edge_inc=incompatibility(edge_ep,h)
    edge=solve_airy(n,"volterra_edge",burgers=burgers,core_width=core_width,return_fields=True)
    rows=[]
    mask=(slice(4,-4),slice(4,-4))
    for sep in separations:
        dip_ep=plastic_strain_nodes(n,"wedge_dipole",burgers=burgers,core_width=core_width,dipole_separation=sep)
        dip_inc=incompatibility(dip_ep,h)
        dip=solve_airy(n,"wedge_dipole",burgers=burgers,core_width=core_width,dipole_separation=sep,return_fields=True)
        src=float(np.linalg.norm((dip_inc-edge_inc)[mask])/max(np.linalg.norm(edge_inc[mask]),1e-30))
        ds=dip["stress_cells"][mask]-edge["stress_cells"][mask]
        ref=edge["stress_cells"][mask]
        stress=float(np.linalg.norm(ds)/max(np.linalg.norm(ref),1e-30))
        rows.append({"separation":sep,"separation_over_h":sep/h,"frank_charge_each":burgers/sep,
            "effective_burgers":(burgers/sep)*sep,
            "incompatibility_relative_l2":src,"airy_stress_relative_l2":stress,
            "airy_weak_residual":dip["weak_residual"]})
    return {"n":n,"burgers":burgers,"core_width":core_width,
        "interpretation":"fixed-grid regularized comparison of opposite Frank charges +/-(b/d); separations are deliberately not locked to a finite-difference stencil spacing, and the sweep is not a continuum-limit proof",
        "results":rows}

def self_test():
    for kind in ("volterra_edge","wedge_disclination"):
        r=solve_airy(17,kind)
        assert np.isfinite(r["weak_residual"]) and r["weak_residual"]<1e-7,r
        assert r["topological_moment_error"]<0.01,r
    return {"airy_clamped_solve":"PASS","topological_moments":"PASS"}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--out",default="artifacts/rgs_airy_comparison")
    p.add_argument("--self-test",action="store_true"); a=p.parse_args()
    if a.self_test: print(json.dumps(self_test(),indent=2))
    else:
        r=run(Path(a.out)); print(json.dumps({"rows":len(r["results"]),"levels":r["levels"],"output":a.out},indent=2))
if __name__=="__main__": main()
