from audits.audit_t069_q6_antipodal_covariance import run_audit


def test_t069_q6_antipodal_walsh_covariance():
    report = run_audit()
    assert all(report["checks"].values())
    assert report["point_cloud"]["covariance_rank"] == 3
    assert report["involution_checks"]["q6_global_antipode_coordinate_residual"] > 1e-3
    assert report["involution_checks"]["rgs_coordinate_inversion_residual"] < 1e-12
    assert report["walsh_energy"]["geometric_inversion_even"] < 1e-24
