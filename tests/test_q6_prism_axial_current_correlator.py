import numpy as np
import pytest
from scripts.q6_prism_axial_current_correlator import Q6,PRISM,audit,local_moments,shell_correlator

def test_unpolarized_current_has_zero_mean_nonzero_lorentz_contact():
    j=np.array([.2,.1,-.3,.4]); m=local_moments([j,-j])
    assert m['mean_axial_current']==pytest.approx([0,0,0,0])
    assert m['mean_of_lorentz_norm_squared']==pytest.approx(-j[0]**2+j[1]**2+j[2]**2+j[3]**2)
    assert m['moment_decomposition_residual']==pytest.approx(0,abs=1e-14)

def test_q6_shell_counts():
    r=shell_correlator(np.zeros((64,4)),Q6,6)
    assert [z['directed_pair_count']//64 for z in r]==[1,6,15,20,15,6,1]

def test_prism_first_shell_degree_ten():
    n=int(np.prod(PRISM)); r=shell_correlator(np.zeros((n,4)),PRISM,1)
    assert r[1]['directed_pair_count']==10*n

def test_contact_and_coarse_cell_decomposition():
    x=np.array([[[1.,0,0,0],[-1.,0,0,0]],[[1.,0,0,0],[-1.,0,0,0]]])
    r=audit([1.],x[None,:,:,:],(2,),volumes=[1.],kappa=2.,max_distance=1)['rows'][0]
    assert r['mean_of_lorentz_norm_squared']==pytest.approx(-1)
    assert r['four_fermion_contact_density']==pytest.approx(-3/8)
    assert r['coarse_decomposition_residual']==pytest.approx(0)

def test_lorentz_scalar_is_not_euclidean_norm():
    assert local_moments([[2.,0,0,0]])['mean_of_lorentz_norm_squared']==pytest.approx(-4)

def test_bad_shape_rejected():
    with pytest.raises(ValueError): local_moments(np.ones((3,3)))


def test_dirac_spinor_bilinear_is_real_and_phase_invariant():
    from scripts.q6_prism_axial_current_correlator import spinors_to_axial_currents
    psi=np.array([.2+.1j,.5-.3j,-.4+.2j,.7+.6j])
    j=spinors_to_axial_currents(psi)
    jp=spinors_to_axial_currents(np.exp(.731j)*psi)
    assert j.shape==(4,)
    assert np.isrealobj(j)
    assert jp==pytest.approx(j,abs=1e-12)


def test_spinor_bilinear_quadratic_under_amplitude_scaling():
    from scripts.q6_prism_axial_current_correlator import spinors_to_axial_currents
    psi=np.array([.2+.1j,.5-.3j,-.4+.2j,.7+.6j])
    j=spinors_to_axial_currents(psi)
    j2=spinors_to_axial_currents(2*psi)
    assert j2==pytest.approx(4*j,abs=1e-12)
