import math

import numpy as np
import pytest

from scripts.rgs_prism_mosco_calibration import (
    PeriodicCycle,
    audit_cycle,
    continuum_mode_energy,
)


def test_vertex_mass_is_normalized():
    for n in (8, 16, 64, 128):
        graph = PeriodicCycle(n)
        assert n * graph.mass == pytest.approx(1.0)


def test_constant_mode_has_zero_energy():
    graph = PeriodicCycle(32)
    assert graph.energy(np.ones(32)) == pytest.approx(0.0, abs=1e-14)


def test_sampled_fourier_mode_energy_converges():
    errors = []
    for n in (32, 64, 128, 256):
        graph = PeriodicCycle(n)
        errors.append(abs(graph.energy(graph.sample_mode(2)) -
                          continuum_mode_energy(2)))
    assert errors[-1] < errors[0]
    assert errors[-1] < 2e-2


def test_discrete_eigenvalue_converges_to_continuum():
    k = 3
    errors = []
    target = (2.0 * math.pi * k) ** 2
    for n in (32, 64, 128, 256):
        errors.append(abs(PeriodicCycle(n).eigenvalue(k) - target))
    assert errors[-1] < errors[0]
    assert errors[-1] < 6e-2


def test_audit_explicitly_labels_scope():
    result = audit_cycle([16, 32, 64], mode=1)
    assert result["status"] == "calibration_only_not_a_general_Mosco_proof"
    assert len(result["rows"]) == 3


@pytest.mark.parametrize("n", [0, 1, 2, -5])
def test_invalid_cycle_size_rejected(n):
    with pytest.raises(ValueError):
        PeriodicCycle(n)


def test_invalid_mode_rejected():
    with pytest.raises(ValueError):
        PeriodicCycle(16).sample_mode(16)
