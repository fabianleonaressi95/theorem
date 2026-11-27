import numpy as np
import pytest

from audits.morphodynamics.eqc_rgs_q6_gates import generated_rgs_q6_group
from audits.morphodynamics.q6_mqm_symmetry import (
    edge_permutation,
    q6_edges,
)
from audits.morphodynamics.mqm_dynamical_rgs_q6_symmetry import (
    equivariance_residuals,
    integrate_rk4,
    rgs_mqm_stabilizer,
    transform_edge_field,
    transform_vertex_state,
)


def samples():
    rng = np.random.default_rng(20261127)
    x = rng.normal(scale=0.025, size=192)
    z = rng.normal(size=64) + 1j * rng.normal(size=64)
    psi = z / np.linalg.norm(z)
    uniform = np.zeros(192)
    directional = np.asarray([float(direction) for _, _, direction in q6_edges()])
    generic = np.arange(192, dtype=float)
    return x, psi, uniform, directional, generic


def assert_small_residuals(residuals, tolerance=2e-10):
    for name, value in residuals.items():
        if name == "reference_invariance":
            continue
        assert value < tolerance, (name, value)


def test_reference_stabilizer_orders_are_16_8_and_1():
    _, _, uniform, directional, generic = samples()
    assert len(rgs_mqm_stabilizer(uniform)) == 16
    assert len(rgs_mqm_stabilizer(directional)) == 8
    assert len(rgs_mqm_stabilizer(generic)) == 1


def test_full_rgs_q6_group_is_equivariant_for_uniform_reference():
    x, psi, uniform, _, _ = samples()
    group = generated_rgs_q6_group()
    assert len(group) == 16
    for vertex_map in group:
        residuals = equivariance_residuals(
            x, psi, uniform, vertex_map,
            stiffness=1.2, coupling=0.8, mobility=0.3, hbar=1.1
        )
        assert residuals["reference_invariance"] == 0.0
        assert_small_residuals(residuals)


def test_directional_reference_retains_exactly_its_eight_element_subgroup():
    x, psi, _, directional, _ = samples()
    subgroup = rgs_mqm_stabilizer(directional)
    assert len(subgroup) == 8
    for vertex_map in subgroup:
        residuals = equivariance_residuals(
            x, psi, directional, vertex_map,
            stiffness=0.9, coupling=1.1, mobility=0.2, hbar=0.7
        )
        assert residuals["reference_invariance"] == 0.0
        assert_small_residuals(residuals)


def test_generic_reference_has_only_identity_symmetry():
    x, psi, _, _, generic = samples()
    subgroup = rgs_mqm_stabilizer(generic)
    assert len(subgroup) == 1
    identity = tuple(range(64))
    residuals = equivariance_residuals(x, psi, generic, identity)
    assert_small_residuals(residuals)


def test_nonstabilizing_group_element_breaks_reference_and_energy_covariance():
    x, psi, _, directional, _ = samples()
    subgroup = rgs_mqm_stabilizer(directional)
    broken = next(g for g in generated_rgs_q6_group() if g not in subgroup)
    residuals = equivariance_residuals(x, psi, directional, broken)
    assert residuals["reference_invariance"] > 0.0
    assert residuals["energy_invariance"] > 1e-8


def test_coupled_rk4_trajectories_commute_with_uniform_reference_symmetry():
    x, psi, uniform, _, _ = samples()
    group = generated_rgs_q6_group()
    vertex_map = next(g for g in group if g != tuple(range(64)))
    edge_map = edge_permutation(vertex_map)
    xp0 = transform_edge_field(x, edge_map)
    psip0 = transform_vertex_state(psi, vertex_map)
    kwargs = dict(steps=4, dt=1e-4, stiffness=1.1, coupling=0.7,
                  mobility=0.25, hbar=0.9)
    x_final, psi_final = integrate_rk4(x, psi, uniform, **kwargs)
    xp_final, psip_final = integrate_rk4(xp0, psip0, uniform, **kwargs)
    assert np.max(np.abs(xp_final - transform_edge_field(x_final, edge_map))) < 2e-11
    assert np.max(np.abs(psip_final - transform_vertex_state(psi_final, vertex_map))) < 2e-11


def test_directional_rk4_flow_commutes_with_surviving_subgroup():
    x, psi, _, directional, _ = samples()
    subgroup = rgs_mqm_stabilizer(directional)
    vertex_map = next(g for g in subgroup if g != tuple(range(64)))
    edge_map = edge_permutation(vertex_map)
    x_final, psi_final = integrate_rk4(
        x, psi, directional, steps=3, dt=5e-5,
        stiffness=1.0, coupling=0.6, mobility=0.2, hbar=1.0
    )
    xp_final, psip_final = integrate_rk4(
        transform_edge_field(x, edge_map),
        transform_vertex_state(psi, vertex_map),
        directional, steps=3, dt=5e-5,
        stiffness=1.0, coupling=0.6, mobility=0.2, hbar=1.0
    )
    assert np.max(np.abs(xp_final - transform_edge_field(x_final, edge_map))) < 2e-11
    assert np.max(np.abs(psip_final - transform_vertex_state(psi_final, vertex_map))) < 2e-11


def test_edge_transform_is_a_permutation_and_preserves_edge_multiset():
    _, _, uniform, _, _ = samples()
    vertex_map = next(iter(generated_rgs_q6_group()))
    edge_map = edge_permutation(vertex_map)
    transformed = transform_edge_field(np.arange(192.0), edge_map)
    assert sorted(transformed.tolist()) == list(np.arange(192.0))


if __name__ == "__main__":
    pytest.main([__file__, "-q"])
