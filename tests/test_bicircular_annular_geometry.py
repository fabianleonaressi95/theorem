import numpy as np
import pytest

from models.bicircular_annular_geometry import (
    annular_points,
    fit_affine_deformation,
    green_strain,
    lens_area_centroid,
    lens_area_exact,
    lens_geometry,
    sample_loop_closure,
    strain_anisotropy,
)


def test_classical_vesica_chord_area_and_centroid():
    g = lens_geometry(1.0, 1.0, 1.0)
    area, cx, cy = lens_area_centroid(1.0, 1.0, 1.0)
    expected = (4.0 * np.pi - 3.0 * np.sqrt(3.0)) / 6.0
    assert g["chord"] == pytest.approx(np.sqrt(3.0), abs=1e-12)
    assert area == pytest.approx(expected, abs=1e-12)
    assert cx == pytest.approx(0.5, abs=1e-12)
    assert cy == pytest.approx(0.0, abs=1e-12)


def test_asymmetric_lens_quadrature_matches_exact_area():
    for r1, r2, d in ((1.35, 0.92, 1.10), (1.0, 1.4, 1.2), (0.8, 1.1, 1.3)):
        aq, _, _ = lens_area_centroid(r1, r2, d)
        assert aq == pytest.approx(lens_area_exact(r1, r2, d), rel=1e-11, abs=1e-12)


def test_affine_gradient_recovered_from_two_annular_families():
    F = np.array([[1.2, 0.15], [0.05, 0.82]])
    points = np.vstack([
        annular_points((-0.5, 0.0), 0.1, 0.5, 4, 40),
        annular_points((0.5, 0.0), 0.1, 0.5, 4, 40),
    ])
    u = ((F - np.eye(2)) @ points.T).T
    fitted, _ = fit_affine_deformation(points, u)
    assert np.allclose(fitted, F, atol=1e-12)
    assert strain_anisotropy(green_strain(fitted)) > 0


def test_annular_gradient_converges_for_cubic_manufactured_field():
    A = np.array([[0.12, -0.07], [0.04, -0.09]])
    errors = []
    for h in (0.4, 0.2, 0.1, 0.05):
        xi = annular_points((0.0, 0.0), h, 2.0 * h, 4, 96)
        u = xi @ A.T + 0.7 * xi ** 3
        fitted, _ = fit_affine_deformation(xi, u)
        errors.append(np.linalg.norm((fitted - np.eye(2)) - A))
    assert all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))


def test_manufactured_frank_burgers_loop_closure_converges():
    b = (0.7, -0.25)
    target_frank = 0.4
    levels = [
        sample_loop_closure(0.8, n, b, target_frank)
        for n in (32, 64, 128, 256, 512)
    ]
    errors_b = [np.linalg.norm(value[0] - np.asarray(b)) for value in levels]
    errors_f = [abs(value[1] - target_frank) for value in levels]
    assert errors_b[-1] < errors_b[0]
    assert errors_f[-1] < errors_f[0]
    assert errors_b[-1] < 1e-4
    assert errors_f[-1] < 1e-4


def test_nonintersecting_or_nested_disks_are_rejected():
    with pytest.raises(ValueError):
        lens_geometry(1.0, 1.0, 2.0)
    with pytest.raises(ValueError):
        lens_geometry(1.0, 0.2, 0.5)
