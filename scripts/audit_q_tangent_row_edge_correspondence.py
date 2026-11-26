#!/usr/bin/env python3
"""Deprecated: Q_tangent rows are vertex-coordinate DOFs, not graph edges.

Use scripts/reconstruct_q6_tangent_188d_action.py. This file is retained only
as a pointer so older commands fail safely instead of reviving the false
row-to-edge identification.
"""
raise SystemExit(
    "SUPERSEDED: Q_tangent is ordered as 64 vertex triples (x_i,y_i,z_i), "
    "not as 192 Q6 edges. Run scripts/reconstruct_q6_tangent_188d_action.py."
)
