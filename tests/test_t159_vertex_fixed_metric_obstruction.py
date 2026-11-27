from math import sqrt


def test_vertex_fixed_square_split_has_non_unit_diagonal():
    edge = 1.0
    diagonal = sqrt(edge * edge + edge * edge)
    assert abs(diagonal - sqrt(2.0)) < 1e-14
    assert diagonal != edge


def test_split_triangles_are_right_isosceles_not_equilateral():
    side_lengths = (1.0, 1.0, sqrt(2.0))
    assert side_lengths[0] == side_lengths[1]
    assert side_lengths[2] != side_lengths[0]
    assert abs(side_lengths[0] ** 2 + side_lengths[1] ** 2 - side_lengths[2] ** 2) < 1e-14
