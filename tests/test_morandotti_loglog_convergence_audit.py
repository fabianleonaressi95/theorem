import numpy as np
import pytest

from scripts.morandotti_loglog_convergence_audit import analyze_report


def _level(h, scale):
    def matrix(v):
        return [[v, 0.0], [0.0, v]]
    case = {
        "interior_facet_traction_jump_L2": 2.0 * h**2,
        "interior_facet_traction_jump_frank_L2": 1.0 * h**2,
        "interior_facet_traction_jump_burgers_L2": 0.5 * h**2,
        "interior_facet_traction_jump_second_moment_total_xy": matrix(scale),
        "interior_facet_traction_jump_second_moment_frank_xy": matrix(scale / 2),
        "interior_facet_traction_jump_second_moment_burgers_xy": matrix(scale / 4),
        "interior_facet_traction_jump_second_moment_cross_xy": matrix(scale / 4),
        "source_quadratic_decomposition": {
            "frank_quadratic": 1.0, "burgers_quadratic": 0.5,
            "mixed_cross_term": 0.5, "total_quadratic": 2.0,
            "additivity_residual": 0.0,
        },
        "interior_facet_traction_jump_squared_decomposition": {
            "frank_squared": 1.0, "burgers_squared": 0.25,
            "mixed_cross_term": 0.75, "total_squared": 2.0,
            "additivity_residual": 1e-16,
        },
    }
    return {"h_target": h, "cells": int(100 / h), "reconstruction_cases": {"mixed": case}}


def test_exact_power_law_and_additivity_are_reported():
    report = {"title": "synthetic", "levels": [
        _level(0.08, 4.0), _level(0.04, 2.0), _level(0.02, 1.0),
    ]}
    result = analyze_report(report)
    metric = result["by_case"]["mixed"]["traction_jump_norms"]["total"]
    assert metric["fit_all_levels"]["exponent"] == pytest.approx(2.0)
    assert metric["local_loglog_exponents_coarse_to_fine"] == pytest.approx([2.0, 2.0])
    residuals = result["by_case"]["mixed"]["additivity"][
        "interior_facet_traction_jump_squared_decomposition"
    ]["absolute_residuals"]
    assert residuals == [1e-16, 1e-16, 1e-16]


def test_rejects_duplicate_or_nonpositive_mesh_sizes():
    with pytest.raises(ValueError, match="positive and unique"):
        analyze_report({"levels": [_level(0.1, 1.0), _level(0.1, 0.5)]})


def test_rejects_missing_case_at_one_level():
    a, b = _level(0.1, 1.0), _level(0.05, 0.5)
    b["reconstruction_cases"] = {}
    with pytest.raises(ValueError, match="same reconstruction cases"):
        analyze_report({"levels": [a, b]})
