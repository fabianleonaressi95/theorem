"""Unit tests for the Q6 golden-vector PSU and spin-lift audit."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_q6_ivm_psu_spinor import (  # noqa: E402
    q6_edges,
    q6_squares,
    q6_vectors,
    run_audit,
    shortest_spin_lift,
    qmul,
    qconj,
)


class Q6IVMPSUSpinorTests(unittest.TestCase):
    def test_hexagram_carrier_and_shells(self):
        bits, points = q6_vectors()
        self.assertEqual(bits.shape, (64, 6))
        self.assertEqual(points.shape, (64, 3))
        self.assertEqual(len({tuple(row.round(10)) for row in points}), 64)
        self.assertEqual(len(q6_edges()), 192)
        self.assertEqual(len(q6_squares()), 240)
        radii = sorted(set(points.__class__([]))) if False else None
        import numpy as np
        values, counts = np.unique(np.round(np.linalg.norm(points, axis=1), 10),
                                   return_counts=True)
        self.assertEqual(len(values), 4)
        self.assertEqual(counts.tolist(), [12, 20, 20, 12])

    def test_edge_spin_lift_and_reverse_link(self):
        import numpy as np
        _, points = q6_vectors()
        g, h, _ = q6_edges()[0]
        q = shortest_spin_lift(points[g], points[h])
        q_reverse = shortest_spin_lift(points[h], points[g])
        self.assertLess(np.linalg.norm(q_reverse - qconj(q)), 1e-12)
        product = qmul(q_reverse, q)
        self.assertLess(np.linalg.norm(product - np.asarray([1., 0., 0., 0.])), 1e-12)

    def test_complete_audit(self):
        result = run_audit()
        self.assertTrue(result["pass"], result["checks"])
        self.assertEqual(result["construction"]["vertices"], 64)
        self.assertEqual(result["construction"]["edges"], 192)
        self.assertEqual(result["spinorial_lift"]["face_count"], 240)
        self.assertEqual(result["fuller_haramein_comparison"]["equivariant_Q6_to_tetra_grid_match"],
                         "NOT_TESTED")


if __name__ == "__main__":
    unittest.main()
