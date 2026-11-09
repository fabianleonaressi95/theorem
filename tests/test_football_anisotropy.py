from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from models.football_anisotropy import (
    build_truncated_icosahedron,
    run_audit,
    solve_panel_model,
)


def test_truncated_icosahedron_combinatorics():
    mesh = build_truncated_icosahedron()
    types = mesh["panel_types"]
    assert len(mesh["vertices"]) == 60
    assert len(mesh["panels"]) == 32
    assert np.sum(types == "pentagon") == 12
    assert np.sum(types == "hexagon") == 20
    assert len(mesh["panel_edges"]) == 90
    assert sum(types[i] != types[j] for i, j, _ in mesh["panel_edges"]) == 60
    assert sum(
        types[i] == types[j] == "hexagon"
        for i, j, _ in mesh["panel_edges"]
    ) == 30
    assert sum(
        types[i] == types[j] == "pentagon"
        for i, j, _ in mesh["panel_edges"]
    ) == 0


def test_isotropic_control_is_uniform():
    mesh = build_truncated_icosahedron()
    q, stiffness, report = solve_panel_model(
        mesh, pressure=0.02, C5=1.0, C6=1.0, coupling=0.2
    )
    assert np.max(np.abs(q - 0.02)) < 1e-12
    assert report["solution"]["linear_system_relative_residual"] < 1e-12
    assert report["solution"]["panel_center_radial_rms_anisotropy"] < 1e-12
    assert np.linalg.eigvalsh(stiffness)[0] > 0


def test_pentagon_stiffness_contrast_produces_panel_anisotropy():
    mesh = build_truncated_icosahedron()
    q, stiffness, report = solve_panel_model(
        mesh, pressure=0.01, C5=1.25, C6=1.0, coupling=0.15
    )
    solution = report["solution"]
    assert solution["pentagon_mean_displacement"] < solution["hexagon_mean_displacement"]
    assert solution["panel_center_radial_rms_anisotropy"] > 0
    assert solution["linear_system_relative_residual"] < 1e-12
    assert np.linalg.eigvalsh(stiffness)[0] > 0


def test_pressure_scaling_is_linear():
    mesh = build_truncated_icosahedron()
    q1, _, _ = solve_panel_model(
        mesh, pressure=0.01, C5=1.25, C6=1.0, coupling=0.15
    )
    q2, _, _ = solve_panel_model(
        mesh, pressure=0.02, C5=1.25, C6=1.0, coupling=0.15
    )
    assert np.max(np.abs(q2 - 2 * q1)) < 1e-12


def test_report_records_scope_and_residual():
    _, _, _, report = run_audit()
    assert report["status"] == "numerically_verified_phenomenological_model"
    assert "experimental_material_validation" in report["not_claimed"]
    assert report["geometry"]["pentagon_hexagon_adjacencies"] == 60
    assert report["solution"]["linear_system_relative_residual"] < 1e-12
