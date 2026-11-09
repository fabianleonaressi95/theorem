import numpy as np
from models.q6_topological_synchronization import (
    build_q6_complex,audit_q6_complex,anti_twin_chain_maps,
    order_parameters,rhs,rk4_step,
)

def test_q6_counts_and_boundary_identity():
    K=build_q6_complex()
    assert K.B1.shape==(64,192) and K.B2.shape==(192,240)
    assert np.array_equal(K.B1@K.B2,np.zeros((64,240),dtype=np.int64))

def test_q6_homology_of_two_skeleton():
    report=audit_q6_complex(build_q6_complex())
    assert report["rank_B1_numeric"]==63
    assert report["rank_B2_numeric"]==129
    assert report["graph_cycle_rank"]==129
    assert report["filled_betti_1"]==0

def test_antitwin_signed_chain_involution():
    K=build_q6_complex(); J0,J1,J2=anti_twin_chain_maps(K)
    assert np.array_equal(J0@J0,np.eye(64,dtype=np.int64))
    assert np.array_equal(J1@J1,np.eye(192,dtype=np.int64))
    assert np.array_equal(J2@J2,np.eye(240,dtype=np.int64))
    assert np.array_equal(J0@K.B1,K.B1@J1)
    assert np.array_equal(J1@K.B2,K.B2@J2)

def test_constant_phases_have_unit_order_parameters():
    K=build_q6_complex()
    assert order_parameters(K,np.zeros(64),np.zeros(192))=={
        "R0":1.0,"R1_down":1.0,"R1_up":1.0}

def test_nl_nlt_rhs_and_rk4():
    K=build_q6_complex(); rng=np.random.default_rng(3)
    th=rng.normal(size=64); ph=rng.normal(size=192)
    om=rng.normal(size=64); ol=rng.normal(size=192)
    nl=rhs(K,th,ph,om,ol,.7,"NL"); nlt=rhs(K,th,ph,om,ol,.7,"NLT")
    assert np.all(np.isfinite(nl[0])) and np.all(np.isfinite(nl[1]))
    assert np.all(np.isfinite(nlt[0])) and np.all(np.isfinite(nlt[1]))
    assert np.allclose(nl[0],nlt[0]) and not np.allclose(nl[1],nlt[1])
    out=rk4_step(K,th,ph,om,ol,.5,"NLT",.01)
    assert out[0].shape==(64,) and out[1].shape==(192,)
