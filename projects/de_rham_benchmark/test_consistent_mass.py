import numpy as np
from compare_mass_matrices import run


def check(dim, N):
    result = run(dim, N, amplitude=0.0, nq=4, nqf=3)
    assert result["betti"][0] == 1
    assert all(b == 0 for b in result["betti"][1:])
    assert len(result["consistent_mass_diagnostics"]) == dim + 1
    for k in range(dim + 1):
        md = result["DEC_diagonal"][k]
        mf = result["FEEC_consistent"][k]
        assert md["mass_min_eigenvalue"] > 0
        assert mf["mass_min_eigenvalue"] > 0
        assert mf["mass_asymmetry_inf"] < 1e-11
        assert mf["energy_matrix_asymmetry_inf"] < 1e-9
        assert mf["relative_generalized_eigen_residual"] < 1e-8
        assert np.isfinite(result["comparison"][k]["FEEC_over_DEC"])
        assert result["comparison"][k]["FEEC_over_DEC"] > 0


def test_2d_consistent_mass():
    check(2, 2)


def test_3d_consistent_mass():
    check(3, 2)
