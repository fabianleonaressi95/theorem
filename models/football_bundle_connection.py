"""Discrete Levi-Civita transport and frame-covariant seam transitions.

The connection is the hinge-wise minimal rotation carrying one panel normal
to the adjacent panel normal. This is a finite polyhedral connection; it is
not a smooth continuum connection or an experimentally calibrated seam law.
"""
from __future__ import annotations
import numpy as np


def _unit(x, tol=1e-12):
    x=np.asarray(x,float)
    n=np.linalg.norm(x)
    if n<=tol: raise ValueError("cannot normalize a zero vector")
    return x/n


def _minimal_normal_rotation(n_from,n_to,tol=1e-10):
    """Proper rotation of least angle carrying n_from to n_to."""
    a,b=_unit(n_from),_unit(n_to)
    v=np.cross(a,b); s=float(np.linalg.norm(v)); c=float(np.clip(a@b,-1.,1.))
    if s<=tol:
        if c>0: return np.eye(3)
        raise ValueError("antipodal panel normals: transport axis is not unique")
    K=np.array([[0.,-v[2],v[1]],[v[2],0.,-v[0]],[-v[1],v[0],0.]])
    return np.eye(3)+K+K@K*((1.-c)/(s*s))


def build_physical_seam_bundle_transitions(mesh):
    """Build all 90 oriented seam transitions and discrete LC transports.

    Panel tangent frames are fixed per panel. For a seam oriented from panel
    p_minus to p_plus, R maps the minus normal to the plus normal by the
    minimal hinge rotation; g=F_plus.T R F_minus is the 2x2 component map.
    """
    from .football_shell import _panel_frame
    nodes=np.asarray(mesh["nodes"],float)
    panels=mesh["panels"]
    frames={}; full_frames={}; normals={}
    for p,face in enumerate(panels):
        e1,e2,n=_panel_frame(nodes,face,0.0)
        frames[p]=np.column_stack((e1,e2))
        normals[p]=n
    rows=[]
    for edge in sorted(mesh["physical_seams"]):
        adjacent=mesh["edge_triangles"][edge]
        if len(adjacent)!=2: raise ArithmeticError("seam is not shared by two triangles")
        p0,p1=(int(mesh["triangle_panels"][ti]) for ti in adjacent)
        if p0==p1: raise ArithmeticError("physical seam lies inside one panel")
        # Deterministic orientation: lower panel id is minus, higher is plus.
        pm,pp=sorted((p0,p1))
        R=_minimal_normal_rotation(normals[pm],normals[pp])
        Fm,Fp=frames[pm],frames[pp]
        g=Fp.T@R@Fm
        edge_vec=nodes[edge[1]]-nodes[edge[0]]
        edge_length=float(np.linalg.norm(edge_vec))
        dihedral=float(np.arctan2(
            np.linalg.norm(np.cross(normals[pm],normals[pp])),
            np.clip(normals[pm]@normals[pp],-1.,1.)
        ))
        rows.append({
            "edge":tuple(map(int,edge)), "panel_minus":pm, "panel_plus":pp,
            "rotation_minus_to_plus":R, "transition_plus_from_minus":g,
            "edge_length":edge_length, "dihedral_angle":dihedral,
            "orthogonality_residual":float(np.linalg.norm(g.T@g-np.eye(2))),
            "determinant":float(np.linalg.det(g)),
            "normal_transport_residual":float(np.linalg.norm(R@normals[pm]-normals[pp])),
        })
    if len(rows)!=90: raise ArithmeticError(f"expected 90 physical seams, got {len(rows)}")
    return {
        "panel_frames":frames, "panel_full_frames":full_frames, "panel_normals":normals, "seams":rows,
        "seam_count":len(rows),
        "maximum_transition_orthogonality_residual":max(x["orthogonality_residual"] for x in rows),\n        "maximum_full_transition_orthogonality_residual":max(float(np.linalg.norm(x["full_transition_plus_from_minus"].T@x["full_transition_plus_from_minus"]-np.eye(3))) for x in rows),
        "maximum_normal_transport_residual":max(x["normal_transport_residual"] for x in rows),
        "connection":"hinge-wise discrete Levi-Civita transport by minimal normal rotation",
        "status":"FINITE_POLYHEDRAL_CONNECTION; CONTINUUM_EXTENSION_OPEN",
    }


def transform_channel_gauge(t2u_basis,triplett,orthogonal_gauge):
    """Apply one O(3) channel-basis change consistently to V and R.

    V' = V O and R' = O.T R, hence Gamma'=O.T Gamma O and
    (L V') Gamma' (L V')* = (L V) Gamma (L V)* exactly.
    """
    V=np.asarray(t2u_basis,float); R=np.asarray(triplett,float); O=np.asarray(orthogonal_gauge,float)
    if V.shape!=(188,3) or R.shape!=(2,3) or O.shape!=(3,3):
        raise ValueError("expected V(188x3), R(2x3), O(3x3)")
    if not np.allclose(O.T@O,np.eye(3),atol=1e-10):
        raise ValueError("channel gauge must be orthogonal")
    return V@O, O.T@R


def gauge_covariance_residual(fibre_maps,t2u_basis,triplett,orthogonal_gauge,q_g2):
    """Numerically compare pushed tensors before/after a common O(3) gauge."""
    from .tangent_triplet_anisotropy import push_triplett_to_shell_nodes
    V=np.asarray(t2u_basis,float); R=np.asarray(triplett,float)
    Vp,Rp=transform_channel_gauge(V,R,orthogonal_gauge)
    A=push_triplett_to_shell_nodes(R,fibre_maps,V,q_g2)["tangent_tensors"]
    Ap=push_triplett_to_shell_nodes(Rp,fibre_maps,Vp,q_g2)["tangent_tensors"]
    return float(np.linalg.norm(A-Ap)/max(1.,np.linalg.norm(A)))


def fibre_seam_jump(u_minus,u_plus,transition_plus_from_minus):
    """Compute [u]=u_plus-g_{+-}u_minus in the plus-side fibre coordinates."""
    um=np.asarray(u_minus,float).reshape(-1)
    up=np.asarray(u_plus,float).reshape(-1)
    g=np.asarray(transition_plus_from_minus,float)
    if g.shape!=(up.size,um.size):
        raise ValueError("transition dimensions do not match the two fibre traces")
    return up-g@um


def transform_seam_chart(u_minus,u_plus,g_plus_from_minus,O_minus,O_plus):
    """Change both panel frames and return transformed traces/transition.

    Frame changes F_s -> F_s O_s induce components u_s -> O_s.T u_s and
    g_{+-} -> O_plus.T g_{+-} O_minus.
    """
    um,up=np.asarray(u_minus,float),np.asarray(u_plus,float)
    g=np.asarray(g_plus_from_minus,float)
    Om,Op=np.asarray(O_minus,float),np.asarray(O_plus,float)
    if Om.shape!=(um.size,um.size) or Op.shape!=(up.size,up.size):
        raise ValueError("chart gauge dimensions do not match fibre traces")
    if not np.allclose(Om.T@Om,np.eye(um.size),atol=1e-10):
        raise ValueError("minus chart change must be orthogonal")
    if not np.allclose(Op.T@Op,np.eye(up.size),atol=1e-10):
        raise ValueError("plus chart change must be orthogonal")
    return Om.T@um, Op.T@up, Op.T@g@Om
