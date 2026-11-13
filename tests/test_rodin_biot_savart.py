import numpy as np
import pytest
from scripts.audit_rodin_biot_savart import Winding, biot_savart, centreline

def test_centreline_is_finite_and_has_expected_shape():
    r, dl = centreline(Winding(), 2048)
    assert r.shape == (2048, 3)
    assert dl.shape == (2048, 3)
    assert np.isfinite(r).all()
    assert np.isfinite(dl).all()

def test_phase_shift_changes_geometric_path():
    r0, _ = centreline(Winding(phase_rad=0.0), 2048)
    r1, _ = centreline(Winding(phase_rad=np.pi / 12.0), 2048)
    assert np.max(np.linalg.norm(r0 - r1, axis=1)) > 1e-4

def test_current_reversal_reverses_field():
    point = np.array([[0.0, 0.0, 0.0]])
    bp = biot_savart(point, [Winding(current_a=1.0)], n_segments=4096)
    bm = biot_savart(point, [Winding(current_a=-1.0)], n_segments=4096)
    assert np.allclose(bm, -bp, rtol=1e-12, atol=1e-14)

def test_field_scales_linearly_with_current():
    point = np.array([[0.0, 0.0, 0.0]])
    b1 = biot_savart(point, [Winding(current_a=1.0)], n_segments=4096)
    b2 = biot_savart(point, [Winding(current_a=2.5)], n_segments=4096)
    assert np.allclose(b2, 2.5 * b1, rtol=1e-12, atol=1e-14)

def test_opposite_identical_path_cancels():
    point = np.array([[0.0, 0.0, 0.0]])
    w = Winding(current_a=1.0)
    bc = biot_savart(point, [w, Winding(current_a=-1.0)], n_segments=4096)
    assert np.allclose(bc, 0.0, atol=1e-14)

def test_singular_filament_observation_is_rejected():
    r, _ = centreline(Winding(), 4096)
    with pytest.raises(ValueError, match="filament"):
        biot_savart(r[:1], [Winding()], n_segments=4096)
