#!/usr/bin/env python3
"""Edge-cochain P1 elasticity comparator for the RGS–PRISM defect study.

The displacement is a pair of 0-cochains on the vertices. Its discrete
gradient is the oriented edge coboundary d0. On each oriented triangle, the
three edge differences reconstruct a constant displacement gradient; its
symmetric part is the strain. The resulting energy is a P1 simplicial
elasticity energy assembled from cochain data.

This is an independent comparator to scripts/rgs_defect_benchmark.py.
It is NOT the 64-state Q6 model and does not yet derive a map from PRISM
coordinates to a physical mesh. Smooth eigenstrain sources are used; they
are not singular Volterra dislocations.

Dependencies: numpy, scipy.
Run:
  python scripts/rgs_cochain_defect_benchmark.py --self-test
  python scripts/rgs_cochain_defect_benchmark.py --out artifacts/rgs_cochain_defect
"""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

def square_complex(n: int, diagonal: str='sw_ne'):
    """Return vertices, unique oriented edges, faces and integer incidences."""
    h=1.0/(n-1)
    xy=np.array([(i*h,j*h) for j in range(n) for i in range(n)],float)
    def v(i,j): return j*n+i
    edges=[]
    for j in range(n):
        for i in range(n-1): edges.append((v(i,j),v(i+1,j)))
    for j in range(n-1):
        for i in range(n): edges.append((v(i,j),v(i,j+1)))
    if diagonal not in ("sw_ne","se_nw"): raise ValueError("diagonal must be sw_ne or se_nw")
    # Add the selected diagonal edges used by the triangulation.
    for j in range(n-1):
        for i in range(n-1):
            if diagonal=="sw_ne": edges.append((v(i,j),v(i+1,j+1)))
            else: edges.append((v(i+1,j),v(i,j+1)))
    edge_id={e:k for k,e in enumerate(edges)}
    faces=[]
    for j in range(n-1):
        for i in range(n-1):
            a,b,c,d=v(i,j),v(i+1,j),v(i+1,j+1),v(i,j+1)
            # Consistent CCW triangles, fixed SW-NE diagonal.
            if diagonal=="sw_ne": faces.extend([(a,b,c),(a,c,d)])
            else: faces.extend([(a,b,d),(b,c,d)])
    d0r=[]; d0c=[]; d0v=[]
    for k,(a,b) in enumerate(edges):
        d0r.extend((k,k)); d0c.extend((a,b)); d0v.extend((-1,1))
    D0=coo_matrix((d0v,(d0r,d0c)),shape=(len(edges),n*n),dtype=np.int64).tocsr()
    d1r=[]; d1c=[]; d1v=[]
    for f,tri in enumerate(faces):
        for a,b in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])):
            sign=1
            if a>b: a,b=b,a; sign=-1
            d1r.append(f); d1c.append(edge_id[(a,b)]); d1v.append(sign)
    D1=coo_matrix((d1v,(d1r,d1c)),shape=(len(faces),len(edges)),dtype=np.int64).tocsr()
    return xy,edges,faces,D0,D1

def material(lam,mu):
    return np.array([[lam+2*mu,lam,0.0],
                     [lam,lam+2*mu,0.0],
                     [0.0,0.0,mu]],float)

def eigenstrain_cell_centres(n,kind,amplitude=0.02,width=0.12,burgers=.02,core_width=.025,frank=.01):
    h=1.0/(n-1)
    c=(np.arange(n-1)+0.5)*h
    X,Y=np.meshgrid(c,c)
    out=np.zeros((n-1,n-1,3),float)
    bump=lambda x,y: np.exp(-((X-x)**2+(Y-y)**2)/(2*width**2))
    if kind=="single": out[:,:,2]=amplitude*bump(.5,.5)
    elif kind=="dipole": out[:,:,2]=amplitude*(bump(.35,.5)-bump(.65,.5))
    elif kind=="volterra_edge":
        # Regularized Volterra slip cut: beta^p = b (ex tensor ey) delta(y-y0) H(x-x0).
        # Symmetric part has engineering shear gamma^p = b delta(y-y0) H(x-x0).
        delta=np.exp(-.5*((Y-.5)/core_width)**2)/(np.sqrt(2*np.pi)*core_width)
        out[:,:,2]=burgers*delta*(X>=.5)
    elif kind=="wedge_disclination":
        # Rotational jump [u]=Omega J(x-x0)ex = Omega(x-x0)ey along the cut.
        delta=np.exp(-.5*((Y-.5)/core_width)**2)/(np.sqrt(2*np.pi)*core_width)
        out[:,:,1]=frank*(X-.5)*delta*(X>=.5)
    elif kind not in ("none","affine"): raise ValueError(kind)
    return out

def measure_volterra_burgers(n=129,burgers=.02,core_width=.025,x_probe=.75):
    """Integrate regularized plastic engineering shear across the slip cut."""
    eps=eigenstrain_cell_centres(n,"volterra_edge",burgers=burgers,core_width=core_width)
    h=1.0/(n-1); centres=(np.arange(n-1)+.5)*h
    ix=int(np.argmin(np.abs(centres-x_probe)))
    return float(np.sum(eps[:,ix,2])*h)

def measure_wedge_frank(n=129,frank=.01,core_width=.025,x_left=.65,x_right=.85):
    """Recover Frank angle from the x-derivative of integrated cut-normal slip."""
    eps=eigenstrain_cell_centres(n,"wedge_disclination",frank=frank,core_width=core_width)
    h=1.0/(n-1); centres=(np.arange(n-1)+.5)*h
    il=int(np.argmin(np.abs(centres-x_left))); ir=int(np.argmin(np.abs(centres-x_right)))
    jump_l=float(np.sum(eps[:,il,1])*h); jump_r=float(np.sum(eps[:,ir,1])*h)
    return (jump_r-jump_l)/(centres[ir]-centres[il])

def tri_strain_matrix(x):
    """Engineering strain [exx, eyy, gamma_xy] from triangle nodal DOFs."""
    M=np.column_stack((np.ones(3),x))
    coeff=np.linalg.inv(M) # rows: constant, d/dx, d/dy for nodal shape funcs
    gx=coeff[1,:]; gy=coeff[2,:]
    B=np.zeros((3,6),float)
    for a in range(3):
        B[0,2*a]=gx[a]
        B[1,2*a+1]=gy[a]
        B[2,2*a]=gy[a]
        B[2,2*a+1]=gx[a]
    return B

def solve_cochain(n,kind,lam=1.0,mu=1.0,amplitude=.02,width=.12,diagonal='sw_ne',burgers=.02,core_width=.025,return_fields=False):
    xy,edges,faces,D0,D1=square_complex(n,diagonal)
    C=material(lam,mu)
    epscell=eigenstrain_cell_centres(n,kind,amplitude,width,burgers,core_width)
    ndof=2*len(xy); rows=[]; cols=[]; vals=[]
    rhs=np.zeros(ndof,float); area_total=0.0
    for f,tri in enumerate(faces):
        pts=xy[list(tri)]
        twice=(pts[1,0]-pts[0,0])*(pts[2,1]-pts[0,1])-(pts[1,1]-pts[0,1])*(pts[2,0]-pts[0,0])
        area=abs(float(twice))/2
        B=tri_strain_matrix(pts)
        # Each pair of triangles inherits its parent square's cell source.
        cell=f//2; j=cell//(n-1); i=cell%(n-1)
        epsp=epscell[j,i]
        dofs=np.array([d for a in tri for d in (2*a,2*a+1)],int)
        Ke=area*(B.T@C@B)
        fe=area*(B.T@C@epsp)
        rr,cc=np.meshgrid(dofs,dofs,indexing="ij")
        rows.extend(rr.ravel()); cols.extend(cc.ravel()); vals.extend(Ke.ravel())
        rhs[dofs]+=fe
        area_total+=area
    K=coo_matrix((vals,(rows,cols)),shape=(ndof,ndof)).tocsr()
    if kind=="affine":
        boundary=[]
        for k,(x,y) in enumerate(xy):
            if min(x,y,1-x,1-y)<1e-12: boundary.extend((2*k,2*k+1))
        fixed=np.array(boundary,dtype=int)
        boundary_type="manufactured_dirichlet"
    else:
        # Natural zero-traction boundary; remove translations and rotation.
        fixed=np.array([0,1,3],dtype=int)
        boundary_type="traction_free_rigid_gauge"
    free=np.setdiff1d(np.arange(ndof),fixed)
    u=np.zeros(ndof,float)
    if kind=="affine":
        a,b,c,d=.01,-.004,.003,.008
        u=np.array([v for x,y in xy for v in (a*x+b*y,c*x+d*y)],float)
        u[free]=spsolve(K[free][:,free],rhs[free]-K[free][:,fixed]@u[fixed])
    else:
        u[free]=spsolve(K[free][:,free],rhs[free])
    energy=0.0
    for f,tri in enumerate(faces):
        pts=xy[list(tri)]; area=abs(float((pts[1,0]-pts[0,0])*(pts[2,1]-pts[0,1])-(pts[1,1]-pts[0,1])*(pts[2,0]-pts[0,0])))/2
        B=tri_strain_matrix(pts)
        cell=f//2; j=cell//(n-1); i=cell%(n-1)
        epsp=epscell[j,i]
        dofs=np.array([d for a in tri for d in (2*a,2*a+1)],int)
        e=B@u[dofs]-epsp
        energy+=.5*area*float(e@C@e)
    residual=K@u-rhs
    reaction_scale=float(np.linalg.norm(K[free][:,fixed]@u[fixed]))
    relres=float(np.linalg.norm(residual[free])/max(np.linalg.norm(rhs[free]),reaction_scale,1e-30))
    affine_error=None
    if kind=="affine":
        a,b,c,d=.01,-.004,.003,.008
        exact=np.array([v for x,y in xy for v in (a*x+b*y,c*x+d*y)])
        affine_error=float(np.linalg.norm(u-exact)/max(np.linalg.norm(exact),1e-30))
    result={"n":n,"h":1/(n-1),"case":kind,"energy":float(energy),
            "relative_free_residual":relres,"affine_relative_error":affine_error,
            "dof_total":ndof,"dof_free":int(len(free)),
            "vertices":int(len(xy)),"edges":int(len(edges)),"triangles":int(len(faces)),
            "domain_area":area_total,"diagonal":diagonal,"boundary_type":boundary_type}
    if return_fields:
        strain_cells=np.zeros((n-1,n-1,3),float); stress_cells=np.zeros_like(strain_cells)
        for f,tri in enumerate(faces):
            pts=xy[list(tri)]; B=tri_strain_matrix(pts)
            cell=f//2; j=cell//(n-1); i=cell%(n-1)
            dofs=np.array([d for a in tri for d in (2*a,2*a+1)],int)
            e=B@u[dofs]-epscell[j,i]
            strain_cells[j,i]+=0.5*e
            stress_cells[j,i]+=0.5*(C@e)
        result["strain_cells"]=strain_cells
        result["stress_cells"]=stress_cells
        result["displacement_nodes"]=u.reshape(n,n,2)
    return result

def run(out:Path,levels=(9,17,33,65)):
    out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for n in levels:
        for case in ("affine","none","single","dipole","volterra_edge","wedge_disclination"):
            rows.append(solve_cochain(n,case))
    D0,D1=None,None
    _,_,_,D0,D1=square_complex(9)
    chain=(D1@D0).tocsr(); b0=int(np.max(np.abs(chain.data))) if chain.nnz else 0
    singles=[r for r in rows if r["case"]=="single"]
    for k,r in enumerate(singles):
        r["energy_delta_to_finest"]=abs(r["energy"]-singles[-1]["energy"])
        r["refinement_level"]=k
    report={"title":"RGS edge-cochain elasticity comparator",
      "status":"cochain-based P1 simplicial comparator; not yet Q6/PRISM physical realization",
      "discrete_definition":"two displacement 0-cochains; oriented edge coboundary d0; trianglewise reconstruction of constant gradient; symmetric strain and isotropic elastic energy",
      "source_scope":"smooth inclusions, finite-width regularized Volterra edge cut, and finite-width wedge-disclination rotational cut; neither defect has a singular core",
      "limitations":["triangulation orientation may introduce directional bias",
        "regularized Volterra cut is not an atomistic core or singular Volterra solution",
        "wedge disclination is a finite-width rotational slip cut, not a singular core solution",
        "no continuum rotational connection or Airy-stress formulation; wedge cut is imposed as a prescribed eigenstrain",
        "no derived map from Q6/PRISM states to physical mesh",
        "empirical refinement is not a Mosco/Gamma convergence proof"],
      "B0":{"max_abs_d1d0":b0,"passed":b0==0},
      "frank_audit":{"definition":"x derivative of integrated cut-normal plastic slip","target":0.01,"measured":measure_wedge_frank(),"absolute_error":abs(measure_wedge_frank()-.01),"x_interval":[.65,.85]},
      "burgers_audit":{"definition":"integral of regularized engineering plastic shear across the slip cut","target":0.02,"measured":measure_volterra_burgers(),"absolute_error":abs(measure_volterra_burgers()-.02),"probe_x":0.75},
      "parameters":{"lambda":1.0,"mu":1.0,"amplitude":0.02,"width":0.12,
        "domain":[0,1,0,1],"boundary":"homogeneous Dirichlet for source cases; manufactured affine trace for affine case","burgers_magnitude":0.02,"frank_angle":0.01,"core_width":0.025},
      "levels":list(levels),"results":rows}
    (out/"report.json").write_text(json.dumps(report,indent=2)+"\n")
    with (out/"results.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=sorted({key for row in rows for key in row})); w.writeheader(); w.writerows(rows)
    return report

def self_test():
    xy,e,f,D0,D1=square_complex(8)
    assert (D1@D0).nnz==0
    aff=solve_cochain(9,"affine"); zero=solve_cochain(9,"none")
    assert aff["affine_relative_error"]<1e-9,aff
    assert aff["relative_free_residual"]<1e-8,aff
    assert zero["energy"]<1e-20,zero
    for kind in ("single","dipole","volterra_edge"):
        r=solve_cochain(9,kind)
        assert np.isfinite(r["energy"]) and r["energy"]>=0
        assert r["relative_free_residual"]<1e-8
    return {"B0":"PASS","affine_patch":"PASS","zero_source":"PASS",
            "single_dipole":"PASS","affine_relative_error":aff["affine_relative_error"]}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="artifacts/rgs_cochain_defect")
    p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    if a.self_test: print(json.dumps(self_test(),indent=2))
    else:
        r=run(Path(a.out))
        print(json.dumps({"B0":r["B0"],"levels":r["levels"],"cases":len(r["results"]),"output":a.out},indent=2))
if __name__=="__main__": main()
