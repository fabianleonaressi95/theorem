import numpy as np
from compare_mass_matrices import run
from ddr.mesh import CubicalMesh
from ddr.geometry import PullbackGeometry
from ddr.feec_mass import assemble_consistent_masses


def check(dim, N):
    result = run(dim, N, amplitude=0.0, nq=4, nqf=3)
    assert result["betti"][0] == 1
    assert all(b == 0 for b in result["betti"][1:])
    assert len(result["consistent_mass_diagnostics"]) == dim + 1
    for k in range(dim + 1):
        md = result["DEC_integral_cochain_top_corrected"][k]
        legacy = result["DEC_legacy_diagonal"][k]
        mf = result["FEEC_consistent"][k]
        assert md["mass_min_eigenvalue"] > 0
        assert legacy["mass_min_eigenvalue"] > 0
        assert mf["mass_min_eigenvalue"] > 0
        assert mf["mass_asymmetry_inf"] < 1e-11
        assert mf["energy_matrix_asymmetry_inf"] < 1e-9
        assert mf["relative_generalized_eigen_residual"] < 1e-8
        assert np.isfinite(result["comparison"][k]["FEEC_over_corrected_DEC"])
        assert result["comparison"][k]["FEEC_over_corrected_DEC"] > 0


def test_2d_consistent_mass():
    check(2, 2)


def test_3d_consistent_mass():
    check(3, 2)


def test_flat_DEC_is_row_sum_lumping_of_FEEC():
    for dim, N in ((2, 3), (3, 2)):
        mesh = CubicalMesh(N, dim)
        geo = PullbackGeometry(mesh, {"type": "identity"},
                               {"type": "identity"}, nq=4, nqf=3)
        Mfeec, _ = assemble_consistent_masses(mesh, geo)
        Mdec = [np.asarray(m, float).copy() for m in geo.M]
        Mdec[dim] = 1.0 / geo.vol_g
        for k in range(dim + 1):
            row_sum = np.asarray(Mfeec[k].sum(axis=1)).ravel()
            scale = max(1.0, float(np.max(np.abs(Mdec[k]))))
            assert np.max(np.abs(row_sum - Mdec[k])) / scale < 1e-10


def test_curved_2d_consistent_mass():
    result = run(2, 2, amplitude=0.03, freq=1, nq=5, nqf=4)
    assert result["geometry"]["min_det_jac"] > 0
    for k in range(3):
        assert result["FEEC_consistent"][k]["mass_min_eigenvalue"] > 0
        assert result["FEEC_consistent"][k]["relative_generalized_eigen_residual"] < 1e-8


if __name__ == '__main__':
    test_2d_consistent_mass()
    test_3d_consistent_mass()
    test_flat_DEC_is_row_sum_lumping_of_FEEC()
    test_curved_2d_consistent_mass()
    print('consistent FEEC mass checks passed')
