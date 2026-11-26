#!/usr/bin/env python3
"""Exact-coordinate/numerical audit of the Vesica–Minkowski D-reflection model.

This checks the three paired channels, their null-cone equations, common
Vesica midpoint, ambient Lorentz reflection, and its conjugacy to diag(1,1,-1).
It does not load or modify the original RGS arrays.
"""
import json
import math
import numpy as np

s3 = math.sqrt(3.0)
# Spatial points at t=1, ordered (-, 0, +).
A = np.array([[0.5, -s3 / 2], [1.0, 0.0], [0.5, s3 / 2]])
B = np.array([[0.5, s3 / 2], [0.0, 0.0], [0.5, -s3 / 2]])

# Null-cone residuals: t^2 - x^2-y^2 and t^2 -(x-1)^2-y^2.
null_A = np.array([1.0 - x*x - y*y for x, y in A])
null_B = np.array([1.0 - (x-1.0)**2 - y*y for x, y in B])
midpoints = (A + B) / 2.0
distances = np.linalg.norm(A - B, axis=1)

P = np.array([[0., 0., 1.],
              [0., 1., 0.],
              [1., 0., 0.]])
Q = np.array([[0., 1/math.sqrt(2), 1/math.sqrt(2)],
              [1., 0., 0.],
              [0., 1/math.sqrt(2), -1/math.sqrt(2)]])
D = np.diag([1., 1., -1.])
conjugated = Q.T @ P @ Q

# Spatial reflection y -> -y, tested on each sheet's three points.
reflection_A = A * np.array([1., -1.])
reflection_B = B * np.array([1., -1.])

expected_midpoint = np.array([0.5, 0.0])
expected_distances = np.array([s3, 1.0, s3])
checks = {
    "null_cone_A": bool(np.max(np.abs(null_A)) < 1e-14),
    "null_cone_B": bool(np.max(np.abs(null_B)) < 1e-14),
    "common_midpoint": bool(np.max(np.abs(midpoints - expected_midpoint)) < 1e-14),
    "channel_distances": bool(np.max(np.abs(distances - expected_distances)) < 1e-14),
    "reflection_swaps_endpoints_fixes_center_A": bool(np.max(np.abs(reflection_A - A[[2, 1, 0]])) < 1e-14),
    "reflection_swaps_endpoints_fixes_center_B": bool(np.max(np.abs(reflection_B - B[[2, 1, 0]])) < 1e-14),
    "orthogonal_channel_basis": bool(np.max(np.abs(Q.T @ Q - np.eye(3))) < 1e-14),
    "reflection_conjugates_to_D": bool(np.max(np.abs(conjugated - D)) < 1e-14),
}
report = {
    "checks": checks,
    "all_pass": all(checks.values()),
    "A_spatial_points": A.tolist(),
    "B_spatial_points": B.tolist(),
    "paired_midpoints": midpoints.tolist(),
    "paired_distances": distances.tolist(),
    "channel_reflection_matrix": P.tolist(),
    "reflection_adapted_basis_columns": Q.tolist(),
    "D": D.tolist(),
    "conjugated_reflection": conjugated.tolist(),
    "scope": "coordinate audit only; no full-188D K0 intertwiner or 64-state embedding claimed",
}
print(json.dumps(report, indent=2))
if not report["all_pass"]:
    raise SystemExit("Vesica–Minkowski D-reflection audit failed")
