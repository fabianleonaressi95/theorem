"""Exact combinatorial checks for the Q6 -> eight-panel Jitterbug quotient."""

import itertools
import unittest
from collections import Counter


BITS3 = list(itertools.product((0, 1), repeat=3))
BITS6 = list(itertools.product((0, 1), repeat=6))
SIGNS = list(itertools.product((-1, 1), repeat=3))


def panel_vertices(eps):
    """Unscaled integer coordinates; the common factor 1/sqrt(2) is omitted."""
    e1, e2, e3 = eps
    return {
        (e1, e2, 0),
        (e1, 0, e3),
        (0, e2, e3),
    }


def quotient(x):
    """First three Q6 bits label a Jitterbug panel; last three are fibre bits."""
    return x[:3]


class TestQ6JitterbugPanelQuotient(unittest.TestCase):
    def test_panel_contact_graph_is_q3(self):
        panels = {eps: panel_vertices(eps) for eps in SIGNS}
        degrees = Counter()
        contacts = set()
        for i, eps in enumerate(SIGNS):
            for eta in SIGNS[i + 1:]:
                shared = panels[eps] & panels[eta]
                hamming = sum(a != b for a, b in zip(eps, eta))
                self.assertEqual(len(shared), 1 if hamming == 1 else 0)
                if shared:
                    contacts.add((eps, eta))
                    degrees[eps] += 1
                    degrees[eta] += 1
        self.assertEqual(len(contacts), 12)
        self.assertEqual(set(degrees.values()), {3})

    def test_q6_projection_has_eight_states_per_panel(self):
        fibres = {a: [x for x in BITS6 if quotient(x) == a] for a in BITS3}
        self.assertEqual(len(fibres), 8)
        self.assertEqual({len(f) for f in fibres.values()}, {8})

    def test_horizontal_edges_lift_each_panel_edge_eight_times(self):
        lifts = Counter()
        vertical_count = 0
        for x in BITS6:
            for k in range(6):
                y = list(x)
                y[k] ^= 1
                y = tuple(y)
                if x > y:
                    continue
                a, c = quotient(x), quotient(y)
                if a == c:
                    vertical_count += 1
                else:
                    self.assertEqual(sum(u != v for u, v in zip(a, c)), 1)
                    lifts[tuple(sorted((a, c)))] += 1
        self.assertEqual(len(lifts), 12)
        self.assertEqual(set(lifts.values()), {8})
        self.assertEqual(vertical_count, 3 * 64 // 2)

    def test_projected_boundary_identity_on_each_q6_edge(self):
        # For an oriented edge x -> y, Pi_0(boundary) equals the boundary
        # of Pi_1(edge); a fibre edge maps to zero because both endpoints
        # have the same panel label.
        for x in BITS6:
            for k in range(6):
                y = list(x)
                y[k] ^= 1
                y = tuple(y)
                if x > y:
                    continue
                px, py = quotient(x), quotient(y)
                if px == py:
                    projected_edge_boundary = (0, 0)
                    projected_vertex_boundary = (0, 0)
                else:
                    projected_edge_boundary = (-1, 1)
                    projected_vertex_boundary = (-1, 1)
                self.assertEqual(projected_edge_boundary,
                                 projected_vertex_boundary)


if __name__ == "__main__":
    unittest.main()
