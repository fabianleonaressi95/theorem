from research.sangaku_geometry.flower_of_life import (
    centre_distance_square_classes,
    centres_axial,
    reflect_x,
    rotate60,
    squared_lattice_distance,
)


def test_radius_two_hexagonal_patch_has_nineteen_centres():
    assert len(centres_axial(2)) == 19


def test_dihedral_generators_preserve_the_circle_centres():
    points = centres_axial(2)
    assert {rotate60(p) for p in points} == set(points)
    assert {reflect_x(p) for p in points} == set(points)


def test_centre_squared_distances_are_exact():
    points = sorted(centres_axial(2))
    values = {
        squared_lattice_distance(a, b)
        for i, a in enumerate(points)
        for b in points[i + 1 :]
    }
    assert values == {1, 3, 4, 7, 9, 12, 13, 16}
    assert centre_distance_square_classes(2) == {1, 3, 7, 13}
