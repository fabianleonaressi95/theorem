#!/usr/bin/env python3
"""RGS–PRISM defect benchmark (candidate discrete elasticity prototype).

This is a reproducible Q1 finite-element reference/prototype on a square mesh.
It is NOT yet the RGS/Q6 discretization and does NOT model a crystallographic
dislocation core. Localized plastic eigenstrain fields are used as controlled
defect-inspired test sources. The script is intended to establish B0–B4
invariants and a baseline before the RGS cochain map is introduced.

Dependencies: numpy, scipy. Optional: matplotlib.
Run:
  python scripts/rgs_defect_benchmark.py --out artifacts/rgs_defect_benchmark
  python scripts/rgs_defect_benchmark.py --self-test
"""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import spsolve

def incidence_square(n: int):
    """Integer incidence matrices d0: vertices->edges, d1: edges->faces.
    Grid has n x n vertices, (n-1)^2 oriented CCW faces.
    Edge orientation: horizontal +x, then vertical +y.
    """
    nv=n*n
    h_edges=n*(n-1); v_edges=(n-1)*n
    ne=h_edges+v_edges
    D0=np.zeros((ne,nv),dtype=np.int64)
    def vid(i,j): return j*n+i
    def hid(i,j): return j*(n-1)+i
    def vidx(i,j): return h_edges+j*n+i
    for j in range(n):
        for i in range(n-1):
            e=hid(i,j); D0[e,vid(i,j)]=-1; D0[e,vid(i+1,j)]=1
    for j in range(n-1):
        for i in range(n):
            e=vidx(i,j); D0[e,vid(i,j)]=-1; D0[e,vid(i,j+1)]=1
    D1=np.zeros(((n-1)*(n-1),ne),dtype=np.int64)
    for j in range(n-1):
        for i in range(n-1):
            f=j*(n-1)+i
            bottom=hid(i,j); right=vidx(i+1,j)
            top=hid(i,j+1); left=vidx(i,j)
            D1[f,bottom]=1; D1[f,right]=1
            D1[f,top]=-1; D1[f,left]=-1
    return D0,D1

def q1_B(h: float, xi: float=0.0, eta: float=0.0):
    """Engineering-strain matrix for a square Q1 element at (xi, eta)."""
    dxi=np.array([-(1-eta),1-eta,1+eta,-(1+eta)],float)/4
    deta=np.array([-(1-xi),-(1+xi),1+xi,1-xi],float)/4
    dNdx=dxi*(2/h); dNdy=deta*(2/h)
    B=np.zeros((3,8),float)
    for a in range(4):
        B[0,2*a]=dNdx[a]
        B[1,2*a+1]=dNdy[a]
        B[2,2*a]=dNdy[a]
        B[2,2*a+1]=dNdx[a]
    return B

def elasticity_tensor(lam: float, mu: float):
    return np.array([[lam+2*mu,lam,0.0],
                     [lam,lam+2*mu,0.0],
                     [0.0,0.0,mu]],float)

def source_field(n: int, kind: str, amplitude=0.02, width=0.12, burgers=0.02, core_width=0.025):
    """Cell-centred engineering eigenstrain [exx*, eyy*, gamma_xy*].
    single/dipole are smooth shear eigenstrain inclusions, not atomistic cores.
    """
    h=1.0/(n-1)
    c=(np.arange(n-1)+0.5)*h
    X,Y=np.meshgrid(c,c)
    eps=np.zeros((n-1,n-1,3),float)
    def bump(x0,y0):
        return np.exp(-((X-x0)**2+(Y-y0)**2)/(2*width**2))
    if kind=="none":
        return eps
    if kind=="affine":
        return eps
    if kind=="single":
        eps[:,:,2]=amplitude*bump(0.5,0.5)
    elif kind=="dipole":
        eps[:,:,2]=amplitude*(bump(0.35,0.5)-bump(0.65,0.5))
    elif kind=="volterra_edge":
        delta=np.exp(-0.5*((Y-.5)/core_width)**2)/(np.sqrt(2*np.pi)*core_width)
        eps[:,:,2]=burgers*delta*(X>=.5)
    else:
        raise ValueError(kind)
    return eps

def solve_case(n: int, kind: str, lam=1.0, mu=1.0, amplitude=0.02,
               width=0.12):
    h=1.0/(n-1); nn=n*n; ndof=2*nn
    B=q1_B(h); C=elasticity_tensor(lam,mu)
    epsp=source_field(n,kind,amplitude,width)
    rows=[]; cols=[]; vals=[]
    rhs=np.zeros(ndof,float)
    area=h*h
    def node(i,j): return j*n+i
    for j in range(n-1):
        for i in range(n-1):
            ids=[node(i,j),node(i+1,j),node(i+1,j+1),node(i,j+1)]
            dofs=np.array([d for a in ids for d in (2*a,2*a+1)],int)
            Ke=np.zeros((8,8),float); fe=np.zeros(8,float)
            gp=(-1/np.sqrt(3),1/np.sqrt(3))
            for xi in gp:
                for eta in gp:
                    Bq=q1_B(h,xi,eta); wdet=area/4
                    Ke+=wdet*(Bq.T@C@Bq)
                    fe+=wdet*(Bq.T@C@epsp[j,i])
            rr,cc=np.meshgrid(dofs,dofs,indexing="ij")
            rows.extend(rr.ravel()); cols.extend(cc.ravel()); vals.extend(Ke.ravel())
            rhs[dofs]+=fe
    K=coo_matrix((vals,(rows,cols)),shape=(ndof,ndof)).tocsr()
    coords=np.array([((i*h),(j*h)) for j in range(n) for i in range(n)])
    fixed_nodes=[]
    for j in range(n):
        for i in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                fixed_nodes.append(node(i,j))
    fixed=np.array([d for a in fixed_nodes for d in (2*a,2*a+1)],int)
    free=np.setdiff1d(np.arange(ndof),fixed)
    u=np.zeros(ndof,float)
    if kind=="affine":
        # Manufactured affine displacement u=(a*x+b*y,c*x+d*y).
        a,b,c,d=0.01,-0.004,0.003,0.008
        for k,(x,y) in enumerate(coords):
            u[2*k]=a*x+b*y; u[2*k+1]=c*x+d*y
        # All boundary values prescribed; solve interior correction.
        u[free]=spsolve(K[free][:,free],rhs[free]-(K[free][:,fixed]@u[fixed]))
    else:
        u[free]=spsolve(K[free][:,free],rhs[free])
    energy=0.0
    for j in range(n-1):
        for i in range(n-1):
            ids=[node(i,j),node(i+1,j),node(i+1,j+1),node(i,j+1)]
            dofs=np.array([d for a in ids for d in (2*a,2*a+1)],int)
            gp=(-1/np.sqrt(3),1/np.sqrt(3))
            for xi in gp:
                for eta in gp:
                    Bq=q1_B(h,xi,eta)
                    e=Bq@u[dofs]-epsp[j,i]
                    energy += 0.5*(area/4)*float(e@C@e)
    residual=K@u-rhs
    reaction_scale=float(np.linalg.norm(K[free][:,fixed]@u[fixed]))
    relres=float(np.linalg.norm(residual[free])/max(np.linalg.norm(rhs[free]),reaction_scale,1e-30))
    if kind=="affine":
        a,b,c,d=0.01,-0.004,0.003,0.008
        exact=np.array([v for x,y in coords for v in (a*x+b*y,c*x+d*y)])
        field_error=float(np.linalg.norm(u-exact)/max(np.linalg.norm(exact),1e-30))
    else:
        field_error=None
    return {"n":n,"h":h,"case":kind,"energy":float(energy),
            "relative_free_residual":relres,"affine_relative_error":field_error,
            "displacement_l2":float(np.linalg.norm(u)),
            "dof_total":int(ndof),"dof_free":int(len(free))}

def run(out: Path, levels=(9,17,33,65)):
    out.mkdir(parents=True,exist_ok=True)
    D0,D1=incidence_square(9)
    b0=int(np.max(np.abs(D1@D0)))
    rows=[]
    for n in levels:
        for case in ("affine","none","single","dipole","volterra_edge"):
            rows.append(solve_case(n,case))
    # B4 refinement trend for the regularized single-source problem.
    singles=[r for r in rows if r["case"]=="single"]
    for k,r in enumerate(singles):
        r["energy_delta_to_finest"]=abs(r["energy"]-singles[-1]["energy"])
        r["refinement_level"]=k
    report={
      "title":"RGS–PRISM defect benchmark prototype",
      "status":"candidate baseline; not yet an RGS/Q6 discretization",
      "physical_scope":"2D isotropic elasticity with smooth inclusions and a regularized Volterra slip cut",
      "limitations":[
        "single/dipole sources are smooth eigenstrain inclusions",
        "Volterra edge source is a regularized slip cut with finite core width, not a singular continuum or atomistic core",
        "no disclination connection or Airy-stress-function reproduction yet",
        "Q1 FEM baseline is not the RGS cochain method",
        "convergence trend is empirical and does not prove Mosco/Γ convergence"
      ],
      "B0":{"max_abs_d1d0":b0,"passed":bool(b0==0)},
      "burgers_audit":{"definition":"integral of engineering plastic shear gamma^p across a vertical section through the slip cut","target":0.02,"note":"section sampled at a cell-centre x > 0.5"},
      "parameters":{"lambda":1.0,"mu":1.0,"amplitude":0.02,"width":0.12,"burgers_magnitude":0.02,"core_width":0.025,
                    "domain":[0.0,1.0,0.0,1.0],"boundary":"Dirichlet"},
      "levels":list(levels),"results":rows
    }
    (out/"report.json").write_text(json.dumps(report,indent=2)+"\n")
    with (out/"results.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=sorted({key for row in rows for key in row}))
        w.writeheader(); w.writerows(rows)
    try:
        import matplotlib.pyplot as plt
        fig,ax=plt.subplots()
        ax.loglog([r["h"] for r in singles],
                  [max(r["energy_delta_to_finest"],1e-16) for r in singles],"o-")
        ax.set_xlabel("mesh size h"); ax.set_ylabel("|E_h - E_finest|")
        ax.set_title("Single eigenstrain source: empirical refinement trend")
        ax.grid(True,which="both")
        fig.tight_layout(); fig.savefig(out/"single_source_refinement.png",dpi=160)
        plt.close(fig)
    except ImportError:
        pass
    return report

def self_test():
    D0,D1=incidence_square(7)
    assert np.array_equal(D1@D0,np.zeros((36,49),dtype=np.int64))
    a=solve_case(9,"affine")
    z=solve_case(9,"none")
    assert a["affine_relative_error"] < 1e-9, a
    assert z["energy"] < 1e-20, z
    assert a["relative_free_residual"] < 1e-8, a
    v=source_field(129,"volterra_edge",burgers=0.02,core_width=0.025)
    h=1/128; ix=80
    measured=float(np.sum(v[:,ix,2])*h)
    assert abs(measured-0.02)<2e-4, measured
    return {"B0":"PASS","B1_affine_manufactured":"PASS",
            "B1_zero_source":"PASS","residual":"PASS",
            "affine_relative_error":a["affine_relative_error"]}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="artifacts/rgs_defect_benchmark")
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args()
    if args.self_test:
        print(json.dumps(self_test(),indent=2))
    else:
        report=run(Path(args.out))
        print(json.dumps({"B0":report["B0"],"output":args.out,
                          "cases":len(report["results"])},indent=2))
if __name__=="__main__":
    main()
