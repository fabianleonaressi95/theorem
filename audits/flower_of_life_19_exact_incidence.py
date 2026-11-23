#!/usr/bin/env python3
"""Exact incidence audit for the 19-circle Flower of Life. Requires SymPy."""
from collections import Counter
import sympy as sp

s3 = sp.sqrt(3)
Q = sp.Rational


def canon(point):
    return tuple(sp.simplify(x) for x in point)


def build_centres():
    return [
        (Q(2*m+n, 2), s3*Q(n, 2), m, n)
        for m in range(-2, 3)
        for n in range(-2, 3)
        if max(abs(m), abs(n), abs(m+n)) <= 2
    ]


def pair_intersections(centres):
    points = set()
    distance_counts = Counter()
    intersecting_pairs = 0
    for i, (x1, y1, *_rest1) in enumerate(centres):
        for x2, y2, *_rest2 in centres[i+1:]:
            dx, dy = sp.simplify(x2-x1), sp.simplify(y2-y1)
            d2 = sp.simplify(dx**2 + dy**2)
            if d2 == 0 or d2 > 4:
                continue
            intersecting_pairs += 1
            distance_counts[d2] += 1
            mx, my = (x1+x2)/2, (y1+y2)/2
            if d2 == 4:
                points.add(canon((mx, my)))
            else:
                d = sp.sqrt(d2)
                h = sp.sqrt(1-d2/4)
                points.add(canon((mx-h*dy/d, my+h*dx/d)))
                points.add(canon((mx+h*dy/d, my-h*dx/d)))
    return points, intersecting_pairs, distance_counts


def incidence_matrix(centres, points):
    ordered_points = sorted(
        points,
        key=lambda p: (sp.default_sort_key(p[0]), sp.default_sort_key(p[1]))
    )
    B = sp.zeros(len(ordered_points), len(centres))
    for r, (px, py) in enumerate(ordered_points):
        for c, (cx, cy, *_rest) in enumerate(centres):
            if sp.simplify((px-cx)**2 + (py-cy)**2 - 1) == 0:
                B[r, c] = 1
    return B


def rotate60(point):
    x, y = point
    return canon((x/2-s3*y/2, s3*x/2+y/2))


def reflect_x(point):
    x, y = point
    return canon((x, -y))


def d6_orbits(points):
    remaining = set(points)
    sizes = []
    while remaining:
        p = next(iter(remaining))
        orbit = set()
        q = p
        for _ in range(6):
            orbit.add(q)
            orbit.add(reflect_x(q))
            q = rotate60(q)
        assert orbit <= points
        sizes.append(len(orbit))
        remaining -= orbit
    return sorted(sizes)


def main():
    centres = build_centres()
    assert len(centres) == 19
    points, pair_count, distance_counts = pair_intersections(centres)
    B = incidence_matrix(centres, points)
    point_degrees = Counter(
        int(sum(B[r, c] for c in range(B.cols))) for r in range(B.rows)
    )
    circle_degrees = Counter(
        int(sum(B[r, c] for r in range(B.rows))) for c in range(B.cols)
    )
    gram = B.T * B
    lam = sp.Symbol("lambda")
    charpoly = sp.factor(gram.charpoly(lam).as_expr())
    expected = (
        (lam-6)**2 * (lam-3)**2 * (lam-2)**3
        * (lam**2-8*lam+11)
        * (lam**3-19*lam**2+78*lam-76)**2
        * (lam**4-38*lam**3+375*lam**2-1350*lam+1584)
    )
    assert pair_count == 99
    assert distance_counts == Counter({Q(1): 42, Q(3): 30, Q(4): 27})
    assert len(points) == 31
    assert point_degrees == Counter({2: 12, 3: 6, 4: 6, 6: 7})
    assert circle_degrees == Counter({6: 13, 5: 6})
    assert d6_orbits(points) == [1, 6, 6, 6, 12]
    assert B.rank() == gram.rank() == 19
    assert sp.expand(charpoly-expected) == 0
    assert sp.trace(gram) == 108
    assert gram.det() == 260861534208
    print("centres:", len(centres))
    print("intersecting circle pairs:", pair_count)
    print("pair distances squared:", dict(sorted(distance_counts.items())))
    print("distinct intersection points:", len(points))
    print("point incidence multiplicities:", dict(sorted(point_degrees.items())))
    print("intersection points per circle:", dict(sorted(circle_degrees.items())))
    print("D6 point-orbit sizes:", d6_orbits(points))
    print("incidence matrix shape/rank:", B.shape, B.rank())
    print("trace/determinant of B^T B:", sp.trace(gram), gram.det())
    print("Gram characteristic polynomial:")
    print(charpoly)


if __name__ == "__main__":
    main()
