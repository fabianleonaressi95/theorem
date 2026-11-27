import numpy as np
from scipy.sparse import diags
from audits.vesica_moire_tmz_maxwell import analytic_uniform_eigenvalues, generalized_spectrum, run, tmz_matrices

def test_relative_permittivity_is_positive_and_bounded():
    d=tmz_matrices(n=12,length=8.0,a=1.0,modulation=0.2)
    assert np.min(d["eps_r"]) >= 0.8-1e-12
    assert np.max(d["eps_r"]) <= 1.2+1e-12
    assert np.all(d["eps_r"]>0)

def test_uniform_generalized_spectrum_matches_exact_discrete_formula():
    n=10; d=tmz_matrices(n=n,length=8.0,a=1.0,modulation=0.0)
    M=diags(np.ones(n*n),format="csr")
    numerical=generalized_spectrum(d["K"],M,count=6)
    exact=analytic_uniform_eigenvalues(n,d["h"],count=6)
    assert np.max(np.abs(numerical-exact))<1e-8

def test_zero_moire_modulation_recovers_uniform_spectrum():
    r=run(n=12,length=8.0,a=1.0,modulation=0.0,modes=6)
    assert np.max(np.abs(np.asarray(r["uniform_discrete_eigenvalues"])-np.asarray(r["moire_generalized_eigenvalues"])))<1e-8

def test_dirichlet_tmz_stiffness_is_symmetric_positive():
    K=tmz_matrices(n=8,length=8.0,a=1.0,modulation=0.1)["K"]
    assert (K-K.T).nnz==0
    assert np.linalg.eigvalsh(K.toarray()).min()>0

def test_generalized_spectrum_is_positive_and_finite():
    r=run(n=14,length=8.0,a=1.0,modulation=0.1,modes=8)
    v=np.asarray(r["moire_generalized_eigenvalues"])
    assert np.all(np.isfinite(v)) and np.all(v>0)
    assert r["relative_permittivity_range"][0]>0

def test_uniform_analytic_control_is_reported():
    r=run(n=12,length=8.0,a=1.0,modulation=0.1,modes=6)
    assert r["uniform_analytic_max_abs_error"]<1e-8
