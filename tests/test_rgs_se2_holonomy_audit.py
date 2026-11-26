import json
import tempfile
from pathlib import Path

import numpy as np

from scripts.rgs_se2_holonomy_audit import (
    adapt_core_holonomies, audit_sizes, connection, curvature_xy,
)


def test_manufactured_connection_has_noncommuting_rotation_translation_parts():
    ax, ay = connection(0.4, 0.5)
    commutator = ax @ ay - ay @ ax
    assert np.linalg.norm(commutator, ord="fro") > 1e-3
    assert np.linalg.norm(curvature_xy(0.4, 0.5), ord="fro") > 0.0


def test_face_holonomy_density_error_decreases_under_refinement():
    report = audit_sizes([0.24, 0.12, 0.06])
    errors = [row["density_error_frobenius"] for row in report["rows"]]
    assert np.isfinite(errors).all()
    assert all(error > 0.0 for error in errors)
    # This is a trend guard, not a proof of the asymptotic order.
    assert errors[1] < errors[0]
    assert errors[2] < errors[1]


def test_core_holonomy_adapter_uses_t093_sign_and_morandotti_order():
    payload = {
        "cores": [
            {"center": [-0.28, 0.0], "theta": 0.2, "q": [0.01, -0.02]},
            {"center": [0.28, 0.0], "theta": -0.1, "q": [-0.03, 0.04]},
        ]
    }
    with tempfile.TemporaryDirectory() as tmp:
        source = Path(tmp) / "cores.json"
        source.write_text(json.dumps(payload))
        result = adapt_core_holonomies(source)
    assert np.allclose(result["frank_angles"], [-0.2, 0.1])
    assert np.allclose(result["burgers_vectors"], [[-0.01, 0.02], [0.03, -0.04]])
    assert np.allclose(
        np.asarray(result["phi_total"]),
        np.asarray(result["phi_frank"]) + np.asarray(result["phi_burgers"]),
    )


def test_core_holonomy_adapter_rejects_empty_or_malformed_input():
    with tempfile.TemporaryDirectory() as tmp:
        source = Path(tmp) / "bad.json"
        source.write_text('{"cores":[]}')
        try:
            adapt_core_holonomies(source)
        except ValueError as exc:
            assert "non-empty" in str(exc)
        else:
            raise AssertionError("empty core list must be rejected")
