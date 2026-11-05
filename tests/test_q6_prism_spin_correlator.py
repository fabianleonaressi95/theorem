import numpy as np
import pytest
from scripts.q6_prism_spin_correlator import Q6_DIMS,PRISM_DIMS,audit_snapshots,invariant_decomposition,shell_correlations,fit_q

def test_q6_hamming_shell_counts():
    c=shell_correlations(np.zeros((64,3)),Q6_DIMS,6)
    assert [r["directed_pair_count"]//64 for r in c["shells"]]==[1,6,15,20,15,6,1]

def test_exact_self_pair_identity_and_negative_pair():
    d=invariant_decomposition([[1,0,0],[-1,0,0]],1)
    assert d["s2_self"]==pytest.approx(2)
    assert d["s2_distinct_pair"]==pytest.approx(-2)
    assert d["s2_total"]==pytest.approx(0)

def test_prism_degree_ten_shell():
    n=int(np.prod(PRISM_DIMS))
    r=audit_snapshots([1],np.zeros((1,n,3)),[1],PRISM_DIMS,max_distance=1)
    assert r["snapshots"][0]["correlation"]["shells"][1]["directed_pair_count"]==10*n

def test_fixed_cell_dilution_gives_self_q3_and_coherent_q6():
    a=np.array([1.,2**(1/3),4**(1/3),8**(1/3)])
    occ=[64,32,16,8]; x=np.zeros((4,64,3))
    for t,n in enumerate(occ): x[t,:n,0]=1
    r=audit_snapshots(a,x,np.full(4,64.),Q6_DIMS,np.array(occ),2)
    assert r["scaling_fits"]["q_density"]["q"]==pytest.approx(3)
    assert r["scaling_fits"]["q_self"]["q"]==pytest.approx(3)
    assert r["scaling_fits"]["q_total"]["q"]==pytest.approx(6)
    assert r["snapshots"][0]["pair_g_effective"]==pytest.approx(63/64)

def test_ensemble_axis_averages_quadratic_before_mean_current():
    x=np.array([[[[1.,0,0],[-1.,0,0]],[[1.,0,0],[-1.,0,0]]]])
    r=audit_snapshots([1],x,[1],(2,),[2],1)
    assert r["snapshots"][0]["ensemble_size"]==2
    assert r["snapshots"][0]["s2_total"]==pytest.approx(0)
    assert r["snapshots"][0]["s2_self"]==pytest.approx(2)

def test_nonpositive_values_not_log_fitted():
    assert fit_q([1,2,3],[1,0,-1])["q"] is None

def test_invalid_volume_rejected():
    with pytest.raises(ValueError): invariant_decomposition(np.ones((2,3)),0)
