from math import isclose, sin, cos

from scripts.audit_q6_mobius_phase import (
    audit, edges, mobius_apply, mobius_matrix, plaquettes,
)


def test_q6_cell_counts():
    assert len(list(range(64))) == 64
    assert len(edges()) == 192
    assert len(plaquettes()) == 240


def test_canonical_connection_is_flat_on_every_square():
    result = audit()
    assert result["all_square_holonomies_one"]
    assert result["square_holonomy_values"] == [1]


def test_exact_laplacian_spectrum_and_antipodal_split():
    result = audit()
    assert result["laplacian_spectrum_multiplicities"] == {
        "0": 1, "2": 6, "4": 15, "6": 20, "8": 15, "10": 6, "12": 1
    }
    assert result["antipodal_plus_dimension"] == 32
    assert result["antipodal_minus_dimension"] == 32
    assert result["antipodal_plus_spectrum"] == {
        "0": 1, "4": 15, "8": 15, "12": 1
    }
    assert result["antipodal_minus_spectrum"] == {
        "2": 6, "6": 20, "10": 6
    }


def test_mobius_matrix_is_rotation_and_composes():
    d1, d2 = 0.37, -0.81
    m1, m2 = mobius_matrix(d1), mobius_matrix(d2)
    product = (
        (m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0],
         m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]),
        (m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0],
         m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]),
    )
    expected = mobius_matrix(d1 + d2)
    for i in range(2):
        for j in range(2):
            assert isclose(product[i][j], expected[i][j], abs_tol=1e-14)
    assert isclose(m1[0][0]*m1[1][1] - m1[0][1]*m1[1][0], 1.0)


def test_mobius_affine_formula_matches_phase_addition():
    u, delta = 0.42, 0.73
    c, s = cos(delta / 2), sin(delta / 2)
    expected = (c*u + s) / (-s*u + c)
    assert isclose(mobius_apply(u, delta), expected, abs_tol=1e-14)
