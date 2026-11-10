import numpy as np

from models.football_shell import build_football_shell
from models.football_bundle_connection import (
    build_physical_seam_bundle_transitions,
    fibre_seam_jump,
    transform_seam_chart,
    transform_channel_gauge,
)


def _orthogonal(rng,n):
    q,_=np.linalg.qr(rng.normal(size=(n,n)))
    return q


def test_all_90_physical_seams_have_orthogonal_discrete_lc_transitions():
    mesh=build_football_shell()
    data=build_physical_seam_bundle_transitions(mesh)
    assert data["seam_count"]==90
    assert data["vertex_holonomy_count"]==60
    assert data["maximum_vertex_holonomy_orthogonality_residual"]<1e-10
    assert data["maximum_transition_orthogonality_residual"]<1e-10
    assert data["maximum_full_transition_orthogonality_residual"]<1e-10
    assert data["maximum_normal_transport_residual"]<1e-10
    for seam in data["seams"]:
        g=seam["transition_plus_from_minus"]
        assert g.shape==(2,2)
        G=seam["full_transition_plus_from_minus"]
        assert G.shape==(3,3)
        assert np.allclose(G.T@G,np.eye(3),atol=1e-10)
        assert np.allclose(g.T@g,np.eye(2),atol=1e-10)
        assert seam["edge_length"]>0


def test_seam_jump_is_covariant_under_independent_panel_chart_changes():
    rng=np.random.default_rng(712)
    gm=_orthogonal(rng,2); gp=_orthogonal(rng,2)
    g=_orthogonal(rng,2)
    um=rng.normal(size=2); up=rng.normal(size=2)
    jump=fibre_seam_jump(um,up,g)
    ump,upp,gp2=transform_seam_chart(um,up,g,gm,gp)
    jump2=fibre_seam_jump(ump,upp,gp2)
    assert np.allclose(jump2,gp.T@jump,atol=1e-12)


def test_t2u_prism_channel_gauge_is_a_simultaneous_basis_change():
    rng=np.random.default_rng(2026)
    V=np.zeros((188,3)); V[:3]=np.eye(3)
    R=rng.normal(size=(2,3))
    O=_orthogonal(rng,3)
    Vp,Rp=transform_channel_gauge(V,R,O)
    assert np.allclose(Vp.T@Vp,np.eye(3),atol=1e-12)
    G=R.T@np.array([[2.,-3.],[-3.,6.]])@R
    Gp=Rp.T@np.array([[2.,-3.],[-3.,6.]])@Rp
    assert np.allclose(Gp,O.T@G@O,atol=1e-12)
    # The identity is the algebraic gauge law; it does not choose a physical
    # O(3) alignment between PRISM channel labels and the T2u eigenbasis.
