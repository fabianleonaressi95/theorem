import numpy as np
from models.constitutive_hysteresis import (
    play_features,fit_prandtl_ishlinskii,predict_prandtl_ishlinskii,
    threshold_grid,preisach_features,fit_preisach,predict_preisach,
    simulate_bouc_wen, simulate_jiles_atherton,
)
from models.hysteresis_metrics import loop_area,rmse


def cycle():
    up=np.linspace(-1,1,61)
    down=np.linspace(1,-1,61)[1:]
    return np.r_[up,down,up[1:]]


def test_play_operator_retains_reversal_memory():
    u=cycle(); P=play_features(u,[0.1,0.3,0.6])
    assert P.shape==(len(u),3)
    assert np.all(np.isfinite(P))
    assert not np.allclose(P[:61],P[61:122][::-1])


def test_preisach_and_pi_dictionary_fit_and_predict():
    u=cycle(); dt=0.01
    y=simulate_bouc_wen(u,dt,A=1.0,beta=.4,gamma=.2,n=2,
                        linear_gain=.2,hysteretic_gain=.8)
    radii=np.linspace(.05,.9,10)
    pi=fit_prandtl_ishlinskii(u,y,radii)
    yp=predict_prandtl_ishlinskii(u,pi)
    alpha,beta=threshold_grid(u,levels=9)
    pr=fit_preisach(u,y,alpha,beta)
    yr=predict_preisach(u,pr)
    assert yp.shape==y.shape and yr.shape==y.shape
    assert np.all(np.isfinite(yp)) and np.all(np.isfinite(yr))
    assert np.isfinite(rmse(y,yp)) and np.isfinite(rmse(y,yr))


def test_bouc_wen_generates_nonzero_loop_area():
    u=cycle(); y=simulate_bouc_wen(u,.01)
    assert loop_area(u,y)>0


def test_jiles_atherton_is_finite_and_has_hysteresis():
    up=np.linspace(-2.0,2.0,801)
    H=np.r_[up,up[-2::-1]]
    M=simulate_jiles_atherton(H,Ms=1.0,a=0.35,k=0.25,alpha=0.02,c=0.15)
    assert M.shape==H.shape
    assert np.all(np.isfinite(M))
    assert np.max(np.abs(M))<=1.2
    assert loop_area(H,M)>0.0


def test_jiles_atherton_handles_zero_field_and_rejects_bad_parameters():
    H=np.zeros(10)
    M=simulate_jiles_atherton(H,Ms=1.0,a=0.3,k=0.2,alpha=0.0,c=0.1)
    assert np.allclose(M,0.0)
    import pytest
    with pytest.raises(ValueError):
        simulate_jiles_atherton(H,Ms=1.0,a=0.0,k=0.2,alpha=0.0,c=0.1)
