#!/usr/bin/env python3
"""T155: geometric Levi-Civita connection and magnetic Hodge star on dodecahedral faces."""
from __future__ import annotations
from itertools import combinations
from pathlib import Path
import json
import numpy as np
from scipy.spatial import ConvexHull

PSI_SG=1.465571231876768
PHI=(1.0+np.sqrt(5.0))/2.0
TOL=2e-9
VESICA_AXIS=np.array([1.0,0.0,0.0])

def geometry(t, regular_control):
    x=np.asarray([(0.,a,b*t) for a in (-1.,1.) for b in (-1.,1.)]
      +[(a,b*t,0.) for a in (-1.,1.) for b in (-1.,1.)]
      +[(a*t,0.,b) for a in (-1.,1.) for b in (-1.,1.)])
    hull=ConvexHull(x)
    equations={tuple(sorted(map(int,s))):e for s,e in zip(hull.simplices,hull.equations)}
    facets=sorted(equations)
    polar=np.asarray([equations[f][:3]/(-equations[f][3]) for f in facets])
    antipode=np.asarray([int(np.argmin(np.linalg.norm(x+p,axis=1))) for p in x])
    cycles=[]
    for vertex in range(12):
        inc=[i for i,f in enumerate(facets) if vertex in f]
        adj={i:[j for j in inc if j!=i and len(set(facets[i])&set(facets[j]))==2] for i in inc}
        start=min(inc); cycle=[start]; previous=None; current=start; nxt=min(adj[current])
        while nxt!=start:
            cycle.append(nxt); previous,current=current,nxt
            nxt=next(q for q in adj[current] if q!=previous)
        assert len(cycle)==5
        cycles.append(cycle)
    scale=1.
    if regular_control:
        dual_edges=[(i,j) for i,j in combinations(range(20),2) if len(set(facets[i])&set(facets[j]))==2]
        scale=2*np.sin(np.pi/5)/np.linalg.norm(polar[dual_edges[0][0]]-polar[dual_edges[0][1]])
    polar*=scale
    centres=np.asarray([polar[c].mean(axis=0) for c in cycles])
    areas=[]
    for cycle,centre in zip(cycles,centres):
        pts=polar[cycle]
        areas.append(sum(np.linalg.norm(np.cross(pts[k]-centre,pts[(k+1)%5]-centre))/2 for k in range(5)))
    normals=x/np.linalg.norm(x,axis=1)[:,None]
    return x,facets,polar,cycles,centres,np.asarray(areas),normals,antipode

def run_case(t, regular_control):
    x,facets,polar,cycles,centres,areas,normals,antipode=geometry(t,regular_control)
    axis=VESICA_AXIS/np.linalg.norm(VESICA_AXIS)
    frames=[]; projection_norms=[]
    for n in normals:
        e1=axis-(axis@n)*n
        projection_norms.append(np.linalg.norm(e1))
        e1=e1/np.linalg.norm(e1)
        e2=np.cross(n,e1); e2=e2/np.linalg.norm(e2)
        frames.append(np.column_stack((e1,e2)))
    edges=[(i,j) for i,j in combinations(range(12),2) if len(set(cycles[i])&set(cycles[j]))==2]
    edge_index={edge:k for k,edge in enumerate(edges)}
    transports=[]; phases=[]; conductances=[]; shared_lengths=[]; centre_distances=[]
    for i,j in edges:
        ni,nj=normals[i],normals[j]
        cross=np.cross(ni,nj); sine=np.linalg.norm(cross); cosine=float(np.clip(ni@nj,-1,1))
        K=np.asarray([[0.,-cross[2],cross[1]],[cross[2],0.,-cross[0]],[-cross[1],cross[0],0.]])
        R=np.eye(3)+K+K@K*((1-cosine)/(sine*sine))
        T=frames[j].T@R@frames[i]
        transports.append(T); phases.append(float(np.arctan2(T[1,0],T[0,0])))
        common=sorted(set(cycles[i])&set(cycles[j]))
        length=float(np.linalg.norm(polar[common[0]]-polar[common[1]]))
        distance=float(np.linalg.norm(centres[i]-centres[j]))
        shared_lengths.append(length); centre_distances.append(distance); conductances.append(length/distance)
    face_antipode=antipode[:12].copy()
    A=[frames[face_antipode[i]].T@(-np.eye(3))@frames[i] for i in range(12)]
    anti_residuals=[]
    for k,(i,j) in enumerate(edges):
        bi,bj=int(face_antipode[i]),int(face_antipode[j])
        kk=edge_index[tuple(sorted((bi,bj)))]
        Tbar=transports[kk] if bi<bj else transports[kk].T
        anti_residuals.append(float(np.linalg.norm(Tbar@A[i]-A[j]@transports[k])))
    holonomy_angles=[]; spherical_areas=[]
    for facet in facets:
        tri=list(facet)
        if np.dot(np.cross(x[tri[1]]-x[tri[0]],x[tri[2]]-x[tri[0]]),x[tri].mean(axis=0))<0:
            tri=[tri[0],tri[2],tri[1]]
        # Independent spherical-triangle area on the Gauss map.
        na,nb,nc=normals[tri]
        area_num=float(np.dot(na,np.cross(nb,nc)))
        area_den=float(1+na@nb+nb@nc+nc@na)
        spherical_areas.append(float(2*np.arctan2(abs(area_num),area_den)))
        P=np.eye(2)
        for a,b in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])):
            kk=edge_index[tuple(sorted((a,b)))]
            T=transports[kk] if a<b else transports[kk].T
            P=T@P
        holonomy_angles.append(float(np.arctan2(P[1,0],P[0,0])))
    U=np.exp(1j*np.asarray(phases))
    DA=np.zeros((len(edges),12),dtype=complex)
    for k,((i,j),u) in enumerate(zip(edges,U)):
        DA[k,i]=-u; DA[k,j]=1.
    W=np.diag(conductances); M=np.diag(areas)
    Kcov=DA.conj().T@W@DA
    Mhalf=np.diag(1/np.sqrt(areas))
    spectrum=np.linalg.eigvalsh(Mhalf@Kcov@Mhalf)
    report={
      "label":"regular_control" if regular_control else "supergolden","parameter":float(t),
      "counts":{"pentagonal_faces":12,"dual_edges":len(edges),"gauss_map_triangles":len(facets)},
      "frame_gauge":"projection of vesica-square axis (1,0,0) onto each Gauss-map tangent plane",
      "minimum_frame_projection_norm":float(min(projection_norms)),
      "face_areas":areas.tolist(),"shared_edge_lengths":shared_lengths,
      "face_centre_distances":centre_distances,"finite_volume_conductances":conductances,
      "transport_orthogonality_residual":max(float(np.linalg.norm(T.T@T-np.eye(2))) for T in transports),
      "transport_determinant_residual":max(abs(float(np.linalg.det(T))-1) for T in transports),
      "antipodal_frame_covariance_residual":max(anti_residuals),
      "holonomy_angles_radians":holonomy_angles,"spherical_triangle_areas_radians":spherical_areas,
      "holonomy_spherical_area_max_residual":float(max(abs(a-b) for a,b in zip(holonomy_angles,spherical_areas))),
      "holonomy_sum":float(sum(holonomy_angles)),
      "gauss_bonnet_4pi_residual":float(abs(sum(holonomy_angles)-4*np.pi)),
      "covariant_hodge_hermiticity_residual":float(np.linalg.norm(Kcov-Kcov.conj().T)),
      "covariant_hodge_spectrum":spectrum.tolist(),
      "covariant_hodge_minimum_eigenvalue":float(spectrum[0]),
      "constant_section_energy":float(np.linalg.norm(Kcov@np.ones(12,dtype=complex))),
      "connection_phases_radians":phases
    }
    return report

def build_report():
    return {"supergolden":run_case(PSI_SG,False),"regular_control":run_case(PHI,True),
      "interpretation":{
        "connection":"Levi-Civita parallel transport on the unit-sphere Gauss map of the 12 pentagonal face normals",
        "hodge_star_0":"diagonal pentagon-area mass M0",
        "hodge_star_1":"diagonal finite-volume conductance W_ij = shared-edge-length / face-centre-distance",
        "covariant_derivative":"(d_A u)_ij = u_j - U_ij u_i",
        "laplacian":"Delta_A = M0^{-1} d_A^* W d_A",
        "gauge_status":"vesica-axis projection fixes local SO(2) gauges; spectrum and Wilson holonomies are gauge invariant",
        "scope":"face-centred covariant finite-volume Hodge operator, distinct from T149 Whitney FEEC"}}

def main():
    report=build_report()
    for case in (report["supergolden"],report["regular_control"]):
        assert case["counts"]=={"pentagonal_faces":12,"dual_edges":30,"gauss_map_triangles":20}
        assert case["minimum_frame_projection_norm"]>0.1
        assert case["transport_orthogonality_residual"]<TOL
        assert case["transport_determinant_residual"]<TOL
        assert case["antipodal_frame_covariance_residual"]<TOL
        assert case["gauss_bonnet_4pi_residual"]<TOL
        assert case["holonomy_spherical_area_max_residual"]<TOL
        assert case["covariant_hodge_hermiticity_residual"]<TOL
        assert case["covariant_hodge_minimum_eigenvalue"]>0
        assert case["constant_section_energy"]>1e-4
    path=Path("results/json/t155_dodecahedral_levi_civita_hodge.json")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
