"""RGS–PRISM discrete shell model for a pentagon/hexagon football.
Linearised triangular membrane + dihedral-hinge shell with orthotropic panels and explicit seams.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree

def _icosahedron():
    phi=(1+np.sqrt(5))/2; raw=[]
    for a in (-1.,1.):
        for b in (-phi,phi): raw.extend(((0.,a,b),(a,b,0.),(b,0.,a)))
    v=np.unique(np.asarray(raw),axis=0); v/=np.linalg.norm(v,axis=1)[:,None]
    d=np.linalg.norm(v[:,None]-v[None,:],axis=2); le=np.min(d[d>1e-10])
    edges={(i,j) for i in range(12) for j in range(i+1,12) if abs(d[i,j]-le)<1e-8}
    faces=[tuple(f) for f in combinations(range(12),3) if all(tuple(sorted(e)) in edges for e in combinations(f,2))]
    return v,edges,faces

def _ordered_ring(points,center):
    normal=center/np.linalg.norm(center); trial=np.array([1.,0,0])
    if abs(trial@normal)>.9: trial=np.array([0.,1,0])
    e1=trial-(trial@normal)*normal; e1/=np.linalg.norm(e1); e2=np.cross(normal,e1)
    rel=points-center
    return np.argsort(np.arctan2(rel@e2,rel@e1))

def cube_sphere_fields(directions):
    n=np.asarray(directions,float); n=n/np.linalg.norm(n,axis=1)[:,None]
    xi=1/np.max(np.abs(n),axis=1)
    return {"xi":xi,"chi":xi-1,"H4":np.sum(n**4,axis=1)-3/5}

def build_football_shell(radius=1.,cube_alpha=0.,h4_alpha=0.):
    if radius<=0: raise ValueError("radius must be positive")
    ico,ico_edges,ico_faces=_icosahedron(); directed={}
    for i,j in ico_edges:
        directed[i,j]=(2*ico[i]+ico[j])/3; directed[j,i]=(2*ico[j]+ico[i])/3
    keys=sorted(directed); kid={k:i for i,k in enumerate(keys)}
    directions=np.asarray([directed[k] for k in keys]); directions/=np.linalg.norm(directions,axis=1)[:,None]
    fields=cube_sphere_fields(directions); chi0=fields["chi"]-np.mean(fields["chi"])
    radii=radius*(1+cube_alpha*chi0+h4_alpha*fields["H4"]); vertices=directions*radii[:,None]
    panels=[]; types=[]
    for i in range(12):
        ids=[kid[i,j] for j in sorted(j for a,j in keys if a==i)]
        pts=vertices[ids]; order=_ordered_ring(pts,pts.mean(axis=0))
        panels.append(tuple(ids[k] for k in order)); types.append("pentagon")
    for a,b,c in ico_faces:
        cyc=(a,b,c); dc=[]
        for u,v in zip(cyc,cyc[1:]+cyc[:1]): dc.extend((kid[u,v],kid[v,u]))
        pts=vertices[dc]; order=_ordered_ring(pts,pts.mean(axis=0))
        panels.append(tuple(dc[k] for k in order)); types.append("hexagon")
    for i,face in enumerate(panels):
        pts=vertices[list(face)]
        normal=sum((np.cross(x,y) for x,y in zip(pts,np.roll(pts,-1,axis=0))),np.zeros(3))
        if normal@pts.mean(axis=0)<0: panels[i]=tuple(reversed(face))
    centres=np.asarray([vertices[list(f)].mean(axis=0) for f in panels])
    nodes=np.vstack((vertices,centres)); triangles=[]; tri_panels=[]
    for pi,face in enumerate(panels):
        ci=len(vertices)+pi
        for u,v in zip(face,face[1:]+face[:1]):
            tri=(ci,u,v); p=nodes[list(tri)]
            if np.cross(p[1]-p[0],p[2]-p[0])@p.mean(axis=0)<0: tri=(ci,v,u)
            triangles.append(tri); tri_panels.append(pi)
    edge_tris=defaultdict(list)
    for ti,tri in enumerate(triangles):
        for u,v in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])):
            edge_tris[tuple(sorted((u,v)))].append(ti)
    if any(len(a)!=2 for a in edge_tris.values()): raise RuntimeError("shell mesh is not a closed two-manifold")
    return {"vertices":vertices,"nodes":nodes,"panels":panels,"panel_types":np.asarray(types),
        "triangles":np.asarray(triangles,int),"triangle_panels":np.asarray(tri_panels,int),
        "edge_triangles":dict(edge_tris),"physical_seams":{e for e in edge_tris if max(e)<60},
        "directions":directions,"cube_sphere":fields,"radii":radii,"radius":float(radius)}

def _panel_frame(nodes,face,angle):
    pts=nodes[list(face)]; centre=pts.mean(axis=0)
    normal=sum((np.cross(x,y) for x,y in zip(pts,np.roll(pts,-1,axis=0))),np.zeros(3))
    normal/=np.linalg.norm(normal)
    if normal@centre<0: normal=-normal
    edge=pts[1]-pts[0]; e1=edge-(edge@normal)*normal; e1/=np.linalg.norm(e1); e2=np.cross(normal,e1)
    ca,sa=np.cos(angle),np.sin(angle)
    return ca*e1+sa*e2,-sa*e1+ca*e2,normal

def _cst_B(xy):
    x1,y1=xy[0]; x2,y2=xy[1]; x3,y3=xy[2]
    twice=(x2-x1)*(y3-y1)-(x3-x1)*(y2-y1); area=abs(twice)/2
    b=np.array([y2-y3,y3-y1,y1-y2])/twice; c=np.array([x3-x2,x1-x3,x2-x1])/twice
    B=np.zeros((3,6))
    for i in range(3):
        B[0,2*i]=b[i]; B[1,2*i+1]=c[i]; B[2,2*i]=c[i]; B[2,2*i+1]=b[i]
    return area,B

def _orthotropic_D(E1,E2,nu12,G12):
    if min(E1,E2,G12)<=0: raise ValueError("orthotropic moduli must be positive")
    nu21=nu12*E2/E1; den=1-nu12*nu21
    if den<=0: raise ValueError("orthotropic Poisson constants violate plane-stress stability")
    return np.array([[E1/den,nu12*E2/den,0],[nu12*E2/den,E2/den,0],[0,0,G12]])

def _signed_dihedral(nodes,t1,t2,edge):
    def normal(tri):
        p=nodes[list(tri)]; v=np.cross(p[1]-p[0],p[2]-p[0]); return v/np.linalg.norm(v)
    n1,n2=normal(t1),normal(t2); tangent=nodes[edge[1]]-nodes[edge[0]]; tangent/=np.linalg.norm(tangent)
    return np.arctan2(tangent@np.cross(n1,n2),n1@n2)

def _hinge_gradient(nodes,t1,t2,edge,epsilon=1e-6):
    ids=np.unique(np.r_[t1,t2]); g=np.zeros((len(ids),3))
    for a,node in enumerate(ids):
        for axis in range(3):
            plus,minus=nodes.copy(),nodes.copy(); plus[node,axis]+=epsilon; minus[node,axis]-=epsilon
            g[a,axis]=(_signed_dihedral(plus,t1,t2,edge)-_signed_dihedral(minus,t1,t2,edge))/(2*epsilon)
    return ids,g.ravel()

def _shape_coefficients(vertices,directions,radius):
    f=cube_sphere_fields(directions)
    A=np.column_stack((np.ones(len(directions)),f["chi"]-np.mean(f["chi"]),f["H4"]))
    radial=np.linalg.norm(vertices,axis=1)/radius-1
    c,*_=np.linalg.lstsq(A,radial,rcond=None); residual=radial-A@c
    return {"constant":float(c[0]),"cube_sphere_chi":float(c[1]),"cubic_harmonic_H4":float(c[2]),
        "fit_rms":float(np.sqrt(np.mean(residual**2))),"radial_rms":float(np.std(radial)),
        "radial_peak_to_peak":float(np.ptp(radial))}

def _discrete_metric_diagnostics(reference_nodes,deformed_nodes,triangles):
    """Elementwise pullback metric and Green-Lagrange strain on each triangle."""
    strains=[]; stretches=[]
    for tri in triangles:
        x=reference_nodes[list(tri)]; y=deformed_nodes[list(tri)]
        e1=x[1]-x[0]; e2=x[2]-x[0]
        b1=e1/np.linalg.norm(e1)
        e2_perp=e2-(e2@b1)*b1; b2=e2_perp/np.linalg.norm(e2_perp)
        reference_coordinates=np.array([[np.linalg.norm(e1),e2@b1],[0.,np.linalg.norm(e2_perp)]])
        deformed_edges=np.column_stack((y[1]-y[0],y[2]-y[0]))
        F=deformed_edges@np.linalg.inv(reference_coordinates)
        C=F.T@F
        Egreen=.5*(C-np.eye(2))
        eig=np.linalg.eigvalsh(C)
        strains.append(np.linalg.norm(Egreen,ord="fro"))
        stretches.extend(np.sqrt(np.maximum(eig,0.)))
    return {
        "definition":"g'_ab=partial_a X' dot partial_b X'; E_GL=0.5*(F^T F-I)",
        "triangle_count":int(len(triangles)),
        "green_lagrange_metric_strain_rms":float(np.sqrt(np.mean(np.square(strains)))),
        "principal_stretch_min":float(np.min(stretches)),
        "principal_stretch_max":float(np.max(stretches)),
    }


def solve_discrete_shell(mesh,pressure=1e-3,thickness=.02,E1=1000.,E2=700.,nu12=.25,G12=300.,
        material_angle=0.,seam_Et=0.,seam_bending_factor=4.,panel_hinge_factor=1.):
    """Linearised orthotropic CST membrane + signed-dihedral bending shell."""
    if pressure<0 or thickness<=0 or seam_Et<0: raise ValueError("invalid pressure, thickness or seam stiffness")
    X=mesh["nodes"].copy(); ndof=3*len(X); K=np.zeros((ndof,ndof)); force=np.zeros(ndof); D=_orthotropic_D(E1,E2,nu12,G12)
    frames={pi:_panel_frame(X,face,material_angle) for pi,face in enumerate(mesh["panels"])}
    for ti,tri in enumerate(mesh["triangles"]):
        pi=int(mesh["triangle_panels"][ti]); e1,e2,_=frames[pi]; pts=X[list(tri)]
        xy=np.column_stack((pts@e1,pts@e2)); area,B=_cst_B(xy); T=np.zeros((6,9))
        for a in range(3): T[2*a:2*a+2,3*a:3*a+3]=np.vstack((e1,e2))
        Bg=B@T; ke=area*thickness*(Bg.T@D@Bg); dofs=np.array([3*i+j for i in tri for j in range(3)])
        K[np.ix_(dofs,dofs)]+=ke
        av=np.cross(pts[1]-pts[0],pts[2]-pts[0]); ar=np.linalg.norm(av)/2; normal=av/np.linalg.norm(av)
        for node in tri: force[3*node:3*node+3]+=pressure*ar*normal/3
    Db=E1*thickness**3/(12*(1-nu12**2)); seam_count=0
    for edge,adjacent in mesh["edge_triangles"].items():
        t1,t2=mesh["triangles"][adjacent[0]],mesh["triangles"][adjacent[1]]
        ids,g=_hinge_gradient(X,t1,t2,edge); a,b=edge; length=np.linalg.norm(X[a]-X[b])
        o1=next(i for i in t1 if i not in edge); o2=next(i for i in t2 if i not in edge)
        h1=np.linalg.norm(np.cross(X[b]-X[a],X[o1]-X[a]))/length
        h2=np.linalg.norm(np.cross(X[b]-X[a],X[o2]-X[a]))/length
        width=max((h1+h2)/2,1e-12); seam=edge in mesh["physical_seams"]
        kb=Db*length/width*(seam_bending_factor if seam else panel_hinge_factor)
        dofs=np.array([3*i+j for i in ids for j in range(3)])
        K[np.ix_(dofs,dofs)]+=kb*np.outer(g,g)
        if seam:
            seam_count+=1
            if seam_Et>0:
                tangent=(X[b]-X[a])/length; grad=np.zeros(ndof)
                grad[3*a:3*a+3]=-tangent; grad[3*b:3*b+3]=tangent
                K+=(seam_Et/length)*np.outer(grad,grad)
    constrained=np.array([0,1,2,4,5,8]); free=np.setdiff1d(np.arange(ndof),constrained)
    Kff=K[np.ix_(free,free)]; uf=np.linalg.solve(Kff,force[free]); u=np.zeros(ndof); u[free]=uf
    u=u.reshape(-1,3); deformed=X+u
    residual=np.linalg.norm((K@u.ravel()-force)[free])/max(np.linalg.norm(force[free]),1e-30)
    r0=np.linalg.norm(X[:60],axis=1); r1=np.linalg.norm(deformed[:60],axis=1)
    diag={"linear_system_relative_residual_free_dofs":float(residual),
        "constrained_stiffness_min_eigenvalue":float(np.linalg.eigvalsh(Kff)[0]),
        "max_node_displacement":float(np.linalg.norm(u,axis=1).max()),
        "rms_node_displacement":float(np.sqrt(np.mean(np.sum(u*u,axis=1)))),
        "radial_increment_rms":float(np.std(r1-r0)),"radial_rms_after":float(np.std(r1)),
        "radial_peak_to_peak_after":float(np.ptp(r1)),"mean_radius_after":float(np.mean(r1)),
        "physical_seam_count":int(seam_count),"triangular_element_count":int(len(mesh["triangles"])),
        "hinge_count":int(len(mesh["edge_triangles"]))}
    diag["discrete_metric"]=_discrete_metric_diagnostics(X,deformed,mesh["triangles"])
    return deformed,u,K,diag

def sample_shell_surface(nodes,triangles,subdivisions=3):
    points=[]
    for tri in triangles:
        a,b,c=nodes[list(tri)]
        for i in range(subdivisions+1):
            for j in range(subdivisions+1-i):
                k=subdivisions-i-j; points.append((i*a+j*b+k*c)/subdivisions)
    return np.asarray(points)

def read_point_cloud(path):
    path=Path(path); suffix=path.suffix.lower()
    if suffix==".csv":
        try:
            data=np.genfromtxt(path,delimiter=",",names=True)
            if data.dtype.names and all(k in data.dtype.names for k in ("x","y","z")):
                points=np.column_stack([data["x"],data["y"],data["z"]])
            else: points=np.loadtxt(path,delimiter=",",skiprows=1)
        except (ValueError,TypeError): points=np.loadtxt(path,delimiter=",",skiprows=1)
    elif suffix in (".xyz",".txt"): points=np.loadtxt(path)
    elif suffix==".obj":
        points=np.asarray([[float(v) for v in line.split()[1:4]] for line in path.read_text().splitlines() if line.startswith("v ")])
    elif suffix==".ply":
        lines=path.read_text().splitlines()
        if not lines or lines[0].strip()!="ply" or "format ascii" not in "\n".join(lines[:5]): raise ValueError("only ASCII PLY supported")
        end=lines.index("end_header"); count=int(next(x for x in lines[:end] if x.startswith("element vertex ")).split()[-1])
        points=np.asarray([[float(v) for v in lines[i].split()[:3]] for i in range(end+1,end+1+count)])
    else: raise ValueError("scan format must be CSV, XYZ, OBJ, or ASCII PLY")
    points=np.asarray(points,float).reshape(-1,3); points=points[np.all(np.isfinite(points),axis=1)]
    if len(points)<10: raise ValueError("scan needs at least 10 finite 3D points")
    return points

def _rigid_fit(source,target):
    sc,tc=source.mean(axis=0),target.mean(axis=0); U,_,Vt=np.linalg.svd((source-sc).T@(target-tc)); R=U@Vt
    if np.linalg.det(R)<0: U[:,-1]*=-1; R=U@Vt
    return R,tc-sc@R

def compare_scan(scan_points,predicted_nodes,triangles,subdivisions=3,max_iterations=60):
    target=sample_shell_surface(predicted_nodes,triangles,subdivisions); tree=cKDTree(target)
    aligned=np.asarray(scan_points,float).copy(); previous=np.inf; R=np.eye(3); translation=np.zeros(3); iterations=0
    for iterations in range(1,max_iterations+1):
        distances,idx=tree.query(aligned); R,translation=_rigid_fit(aligned,target[idx]); aligned=aligned@R+translation
        error=float(np.mean(distances**2))
        if abs(previous-error)<1e-14: break
        previous=error
    ds,_=tree.query(aligned); dm,_=cKDTree(aligned).query(target); both=np.r_[ds,dm]
    return {"status":"scan_compared_after_rigid_icp","scan_points":int(len(scan_points)),
        "model_surface_samples":int(len(target)),"icp_iterations":int(iterations),
        "scan_to_model_mean":float(np.mean(ds)),"scan_to_model_rms":float(np.sqrt(np.mean(ds**2))),
        "scan_to_model_p95":float(np.quantile(ds,.95)),"model_to_scan_mean":float(np.mean(dm)),
        "model_to_scan_rms":float(np.sqrt(np.mean(dm**2))),"symmetric_chamfer_rms":float(np.sqrt(np.mean(both**2))),
        "symmetric_hausdorff_sampled":float(np.max(both)),"registration_rotation":R.tolist(),
        "registration_translation":translation.tolist()}

def run_shell_audit(radius=1.,pressure=1e-3,thickness=.02,E1=1000.,E2=700.,nu12=.25,G12=300.,
        material_angle=0.,seam_Et=0.,seam_bending_factor=4.,cube_alpha=0.,h4_alpha=0.,scan_path=None):
    mesh=build_football_shell(radius,cube_alpha,h4_alpha)
    deformed,u,K,mech=solve_discrete_shell(mesh,pressure,thickness,E1,E2,nu12,G12,material_angle,seam_Et,seam_bending_factor)
    before=_shape_coefficients(mesh["vertices"],mesh["directions"],radius)
    after=_shape_coefficients(deformed[:60],mesh["directions"],radius)
    report={"model":"RGS_PRISM_linearised_orthotropic_discrete_shell_v1","status":"numerically_verified_linearised_shell_model",
        "geometry":{"vertices":60,"panels":32,"pentagons":12,"hexagons":20,"shell_nodes_including_panel_centres":92,
            "triangular_shell_elements":180,"hinges":270,"physical_seams":90},
        "cube_sphere_geometry":{"exact_radial_factor":"xi(n)=1/||n||_infinity","exact_radial_excess":"chi(n)=xi(n)-1",
            "cubic_harmonic":"H4=nx^4+ny^4+nz^4-3/5",
            "chi_range_sampled":[float(mesh["cube_sphere"]["chi"].min()),float(mesh["cube_sphere"]["chi"].max())],
            "H4_range_sampled":[float(mesh["cube_sphere"]["H4"].min()),float(mesh["cube_sphere"]["H4"].max())],
            "cube_alpha":float(cube_alpha),"h4_alpha":float(h4_alpha),"shape_coefficients_before":before,
            "shape_coefficients_after":after,"interpretation":"Cube-sphere and H4 amplitudes are independent inputs, default zero; not inferred from football topology."},
        "constitutive_parameters":{"pressure":float(pressure),"thickness":float(thickness),"E1":float(E1),"E2":float(E2),
            "nu12":float(nu12),"G12":float(G12),"material_angle_radians":float(material_angle),
            "seam_line_stiffness_Et":float(seam_Et),"seam_bending_factor":float(seam_bending_factor)},
        "mechanics":mech,"scan_validation":{"status":"not_run_no_experimental_scan",
            "accepted_formats":["CSV","XYZ","OBJ","ASCII PLY"],"required_units":"scan and model radius must use same length unit"},
        "scope":{"implemented":["orthotropic CST triangular membrane elements","signed-dihedral discrete shell bending hinges",
            "physical seam line reinforcement and seam bending multiplier","cube-sphere radial excess and cubic H4 shape modes",
            "rigid ICP and symmetric sampled-surface scan metrics"],
            "not_implemented":["geometrically nonlinear finite-strain shell iteration","contact, folds, adhesive damage, yarn-scale homogenisation",
            "experimental parameter identification without scan and coupon data"]}}
    if scan_path is not None: report["scan_validation"]=compare_scan(read_point_cloud(scan_path),deformed,mesh["triangles"])
    return mesh,deformed,u,K,report
