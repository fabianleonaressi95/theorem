#!/usr/bin/env python3
"""T156: intrinsic Whitney/FEEC Hodge audit on the polar dodecahedral surface."""
from __future__ import annotations
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy.linalg import eigvalsh
from scripts.audit_t146_dodecahedron_q6_dual_barycentre import PSI_SG, dual_data, selected_q6_coisometry

TOL = 2e-9

def edge_id(a, b, edge_index, edges):
    key = tuple(sorted((int(a), int(b))))
    if key not in edge_index:
        edge_index[key] = len(edges)
        edges.append(key)
    return edge_index[key], (1 if a < b else -1)

def assemble_whitney(points, cycles):
    n0 = len(points)
    centres = np.asarray([points[c].mean(axis=0) for c in cycles])
    vertices = np.vstack((points, centres))
    triangles = []
    for k, cycle in enumerate(cycles):
        for j in range(5):
            triangles.append((n0+k, cycle[j], cycle[(j+1)%5]))
    edges, edge_index = [], {}
    for tri in triangles:
        for a,b in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])):
            edge_id(a,b,edge_index,edges)
    M0=np.zeros((len(vertices),len(vertices)))
    M1=np.zeros((len(edges),len(edges)))
    M2=np.zeros((len(triangles),len(triangles)))
    d0=np.zeros((len(edges),len(vertices)))
    d1=np.zeros((len(triangles),len(edges)))
    for k,(a,b) in enumerate(edges):
        d0[k,a],d0[k,b]=-1.,1.
    areas=[]
    for ti,tri in enumerate(triangles):
        ids=np.asarray(tri,dtype=int); p=vertices[ids]
        cross=np.cross(p[1]-p[0],p[2]-p[0])
        twice=float(np.linalg.norm(cross))
        if twice<=1e-13: raise AssertionError("degenerate fan triangle")
        area=twice/2.; normal=cross/twice
        grad=np.zeros((3,3))
        grad[1]=np.cross(normal,p[2]-p[0])/twice
        grad[2]=np.cross(p[1]-p[0],normal)/twice
        grad[0]=-grad[1]-grad[2]
        M0loc=area/12.*np.asarray([[2.,1.,1.],[1.,2.,1.],[1.,1.,2.]])
        M0[np.ix_(ids,ids)]+=M0loc
        loc_edges=((0,1),(1,2),(2,0))
        quad=(np.asarray([2/3,1/6,1/6]),np.asarray([1/6,2/3,1/6]),np.asarray([1/6,1/6,2/3]))
        w=[]
        for i,j in loc_edges:
            w.append([lam[i]*grad[j]-lam[j]*grad[i] for lam in quad])
        M1loc=np.zeros((3,3))
        for q in range(3):
            M1loc+=area/3.*np.asarray([[np.dot(w[i][q],w[j][q]) for j in range(3)] for i in range(3)])
        global_edges=[]
        for i,j in loc_edges:
            ei,sgn=edge_id(ids[i],ids[j],edge_index,edges)
            global_edges.append((ei,sgn)); d1[ti,ei]+=sgn
        for i,(ei,si) in enumerate(global_edges):
            for j,(ej,sj) in enumerate(global_edges):
                M1[ei,ej]+=si*sj*M1loc[i,j]
        M2[ti,ti]=1./area
        areas.append(area)
    K0=d0.T@M1@d0
    return {"vertices":vertices,"triangles":triangles,"edges":edges,"M0":M0,"M1":M1,"M2":M2,"d0":d0,"d1":d1,"K0":K0,"areas":np.asarray(areas)}

def antipodal_actions(data, anti_vertex, anti_face):
    vertices,triangles,edges=data["vertices"],data["triangles"],data["edges"]
    node_map=np.empty(len(vertices),dtype=int); node_map[:20]=anti_face; node_map[20:]=20+anti_vertex
    S0=np.zeros((len(vertices),len(vertices)))
    for i,j in enumerate(node_map): S0[j,i]=1.
    edge_lookup={tuple(e):i for i,e in enumerate(edges)}
    S1=np.zeros((len(edges),len(edges)))
    for i,(a,b) in enumerate(edges):
        aa,bb=int(node_map[a]),int(node_map[b]); j=edge_lookup[tuple(sorted((aa,bb)))]
        S1[j,i]=1. if aa<bb else -1.
    tri_lookup={tuple(sorted(t)):i for i,t in enumerate(triangles)}
    S2=np.zeros((len(triangles),len(triangles)))
    for i,tri in enumerate(triangles):
        mapped=tuple(int(node_map[v]) for v in tri); j=tri_lookup[tuple(sorted(mapped))]
        target=triangles[j]; perm=[target.index(v) for v in mapped]
        inv=sum(perm[a]>perm[b] for a in range(3) for b in range(a+1,3))
        S2[j,i]=-1. if inv%2 else 1.
    return S0,S1,S2

def audit():
    x,ico_faces,dual,dual_edges,anti_face,anti_vertex=dual_data(PSI_SG)
    cycles=[]
    for vertex in range(12):
        incident=[i for i,f in enumerate(ico_faces) if vertex in f]
        adj={i:[j for j in incident if j!=i and len(set(ico_faces[i])&set(ico_faces[j]))==2] for i in incident}
        start=min(incident); cycle=[start]; previous,current=None,start; nxt=min(adj[current])
        while nxt!=start:
            cycle.append(nxt); previous,current=current,nxt; nxt=next(q for q in adj[current] if q!=previous)
            if len(cycle)>5: raise AssertionError("pentagon boundary failed to close")
        if len(cycle)!=5: raise AssertionError("non-pentagonal dual face")
        cycles.append(cycle)
    data=assemble_whitney(dual,cycles)
    M0,M1,M2=data["M0"],data["M1"],data["M2"]; d0,d1,K0=data["d0"],data["d1"],data["K0"]
    S0,S1,S2=antipodal_actions(data,anti_vertex,anti_face)
    frame_orthogonality=[]; planarity=[]; face_areas=[]
    for cycle in cycles:
        p=dual[cycle]; centre=p.mean(axis=0); e1=p[1]-p[0]; e1/=np.linalg.norm(e1)
        normal=np.zeros(3)
        for j in range(5): normal+=np.cross(p[j]-centre,p[(j+1)%5]-centre)
        normal/=np.linalg.norm(normal); e2=np.cross(normal,e1); frame=np.vstack((e1,e2,normal))
        frame_orthogonality.append(float(np.linalg.norm(frame@frame.T-np.eye(3))))
        planarity.append(float(np.max(np.abs((p-centre)@normal))))
        local=(p-centre)@np.vstack((e1,e2)).T
        face_areas.append(abs(.5*sum(local[j,0]*local[(j+1)%5,1]-local[(j+1)%5,0]*local[j,1] for j in range(5))))
    eig0=eigvalsh(K0,M0)
    K1=M1@d0@np.linalg.inv(M0)@d0.T@M1+d1.T@M2@d1
    K1=(K1+K1.T)/2.; eig1=eigvalsh(K1,M1)
    codes=np.asarray((3,5,58,60,9,17,46,54,33,6,57,30))
    B20=np.zeros((20,64))
    for i,face in enumerate(ico_faces):
        for v in face: B20[i,codes[v]]+=1./3.
    B32=np.vstack((B20,np.asarray([B20[c].mean(axis=0) for c in cycles])))
    F=selected_q6_coisometry(); Lam=np.diag([0.,4.,6.]); Phi=F@B32.T
    intertwining=float(np.linalg.norm(Lam@Phi-Phi@np.linalg.solve(M0,K0)))
    residuals={
      "d1_d0_zero":float(np.linalg.norm(d1@d0)),
      "K0_whitney_identity":float(np.linalg.norm(K0-d0.T@M1@d0)),
      "M0_antipodal":float(np.linalg.norm(S0.T@M0@S0-M0)),
      "M1_antipodal":float(np.linalg.norm(S1.T@M1@S1-M1)),
      "M2_antipodal":float(np.linalg.norm(S2.T@M2@S2-M2)),
      "K0_antipodal":float(np.linalg.norm(S0.T@K0@S0-K0)),
      "M0_min_eigenvalue":float(np.linalg.eigvalsh(M0).min()),
      "M1_min_eigenvalue":float(np.linalg.eigvalsh(M1).min()),
      "M2_min_eigenvalue":float(np.linalg.eigvalsh(M2).min()),
      "frame_orthonormality_max":max(frame_orthogonality),
      "pentagon_planarity_max":max(planarity),
      "face_area_sum":float(sum(face_areas)),
      "Q6_selected_intertwining_residual":intertwining,
      "Q6_selected_map_rank":int(np.linalg.matrix_rank(Phi,tol=1e-9)),
      "triangulated_surface_vertices":len(data["vertices"]),
      "triangulated_surface_edges":len(data["edges"]),
      "triangulated_surface_triangles":len(data["triangles"]),
      "euler_characteristic":len(data["vertices"])-len(data["edges"])+len(data["triangles"]),
      "total_surface_area":float(data["areas"].sum()),
    }
    checks={
      "canonical_60_triangle_fan":len(data["triangles"])==60,
      "closed_surface_euler_characteristic_2":residuals["euler_characteristic"]==2,
      "d1_d0_zero":residuals["d1_d0_zero"]<TOL,
      "whitney_stiffness_identity":residuals["K0_whitney_identity"]<TOL,
      "M0_positive_definite":residuals["M0_min_eigenvalue"]>0,
      "M1_positive_definite":residuals["M1_min_eigenvalue"]>0,
      "M2_positive_definite":residuals["M2_min_eigenvalue"]>0,
      "antipodal_M0_equivariance":residuals["M0_antipodal"]<TOL,
      "antipodal_M1_equivariance":residuals["M1_antipodal"]<TOL,
      "antipodal_M2_equivariance":residuals["M2_antipodal"]<TOL,
      "antipodal_K0_equivariance":residuals["K0_antipodal"]<TOL,
      "face_frames_orthonormal":residuals["frame_orthonormality_max"]<TOL,
      "pentagons_planar":residuals["pentagon_planarity_max"]<TOL,
      "selected_Q6_map_rank_three":residuals["Q6_selected_map_rank"]==3,
      "Hodge_0_spectrum_nonnegative":eig0.min()>-TOL,
      "Hodge_1_spectrum_nonnegative":eig1.min()>-TOL,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {"parameter":PSI_SG,
      "counts":{"icosahedron_faces":len(ico_faces),"dodecahedron_vertices":len(dual),"dodecahedron_edges":len(dual_edges),"pentagonal_faces":len(cycles),"triangulation_vertices":len(data["vertices"]),"triangulation_edges":len(data["edges"]),"triangulation_triangles":len(data["triangles"])},
      "Hodge_0_generalized_eigenvalues":eig0.tolist(),"Hodge_1_generalized_eigenvalues":eig1.tolist(),
      "residuals":residuals,"checks":checks,"all_checks_pass":bool(all(checks.values())),
      "interpretation":"Canonical centroid-fan Whitney FEEC data are positive and antipodally equivariant. The Hodge-0 spectrum and selected-Q6 intertwiner are reported without rescaling; this construction does not establish (0,4,6) or derive f."}

if __name__=="__main__":
    report=audit()
    if not report["all_checks_pass"]: raise AssertionError(report["checks"])
    out=Path("results/json/t156_dodecahedral_feec_hodge_audit.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
