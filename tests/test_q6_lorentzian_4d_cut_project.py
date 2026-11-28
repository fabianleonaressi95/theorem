import numpy as np

from audits.q6_lorentzian_4d_cut_project import (
    audit_q6_lorentzian_4d_cut_project,
    q6_four_faces,
    q6_four_simplex_triangulation,
    q6_lorentzian_cut_project_frame,
    q6_three_face_incidence,
)


def test_cut_project_frame_is_orthonormal_and_all_4_faces_nondegenerate():
    frame, min_minor = q6_lorentzian_cut_project_frame()
    assert frame.shape == (4, 6)
    assert np.allclose(frame @ frame.T, np.eye(4), atol=1e-12)
    assert min_minor > 1e-10


def test_q6_4_skeleton_counts_and_freudenthal_split():
    cells = q6_four_faces()
    simplices = q6_four_simplex_triangulation()
    incidence = q6_three_face_incidence()
    assert len(cells) == 60
    assert simplices.shape == (1440, 5)
    assert len(incidence) == 160
    assert set(incidence.values()) == {3}


def test_q6_4d_gradient_and_barycentric_p1_affine_patch():
    report = audit_q6_lorentzian_4d_cut_project()
    assert report["vertices"] == 64
    assert report["edges"] == 192
    assert report["coordinate_4_cells"] == 60
    assert report["coordinate_3_faces"] == 160
    assert report["freudenthal_4_simplices"] == 1440
    assert report["affine_patch_pass"]
    assert report["affine_patch_max_operator_residual"] < 1e-9
    assert report["maximum_q6_4d_star_condition_number"] < 10


def test_4_skeleton_is_explicitly_branched_not_mislabelled_manifold():
    report = audit_q6_lorentzian_4d_cut_project()
    assert report["facet_incidence_values"] == [3]
    assert not report["is_4_manifold_by_facet_incidence"]
    assert report["all_lorentzian_simplex_grams_nondegenerate"]
    assert report["nonaffine_parity_field_operator_residual"] > 1e-6
