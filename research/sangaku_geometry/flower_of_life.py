"""Exact combinatorial model of a 19-circle Flower-of-Life-type patch."""
from itertools import combinations


def centres_axial(radius=2):
    """Hexagonal patch in axial coordinates; radius=2 gives 19 centres."""
    return frozenset(
        (m, n)
        for m in range(-radius, radius + 1)
        for n in range(-radius, radius + 1)
        if max(abs(m), abs(n), abs(m + n)) <= radius
    )


def rotate60(point):
    m, n = point
    return (-n, m + n)


def reflect_x(point):
    m, n = point
    return (m + n, -n)


def squared_lattice_distance(a, b):
    dm, dn = a[0] - b[0], a[1] - b[1]
    return dm * dm + dm * dn + dn * dn


def centre_distance_square_classes(radius=2):
    """Square-free parts of all nonzero squared centre distances."""
    points = centres_axial(radius)
    values = {
        squared_lattice_distance(a, b)
        for a, b in combinations(sorted(points), 2)
    }
    classes = set()
    for value in values:
        square_free, factor = value, 2
        while factor * factor <= square_free:
            if square_free % (factor * factor) == 0:
                square_free //= factor * factor
            else:
                factor += 1
        classes.add(square_free)
    return frozenset(classes)


def summary():
    points = centres_axial(2)
    distances = frozenset(
        squared_lattice_distance(a, b)
        for a, b in combinations(sorted(points), 2)
    )
    return {
        "circle_count": len(points),
        "squared_centre_distances": sorted(distances),
        "distance_square_classes": sorted(centre_distance_square_classes(2)),
        "rotation_invariant": {rotate60(p) for p in points} == set(points),
        "reflection_invariant": {reflect_x(p) for p in points} == set(points),
    }


if __name__ == "__main__":
    print(summary())
