import math
import pytest
from scripts.audit_rodin_paper_geometry import PublishedGeometry, audit

def test_published_dimensions_expose_aperture_mismatch():
    result = audit()
    assert result["outer_radius_mm"] == pytest.approx(49.75)
    assert result["theta_from_reported_winding_deg"] == pytest.approx(15.0)
    assert result["aperture_radius_from_eq8_mm"] == pytest.approx(12.876, abs=0.002)
    assert result["reported_aperture_radius_mm"] == pytest.approx(14.5)
    assert result["geometry_consistent_within_1_percent"] is False

def test_angle_implied_by_reported_aperture():
    result = audit()
    assert result["winding_angle_implied_by_reported_aperture_deg"] == pytest.approx(146.1, abs=0.1)

def test_equation_9_segment_length():
    result = audit()
    assert result["eq9_segment_length_mm"] == pytest.approx(96.12, abs=0.02)

def test_invalid_diameters_are_rejected():
    with pytest.raises(ValueError, match="positive"):
        audit(PublishedGeometry(external_diameter_m=0.0))

def test_invalid_winding_angle_is_rejected():
    with pytest.raises(ValueError, match="between"):
        audit(PublishedGeometry(winding_angle_deg=180.0))
