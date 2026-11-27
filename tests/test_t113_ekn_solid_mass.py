import pytest
from scripts.audit_t113_ekn_solid_mass import (
    ekn_solid_packet_mass,
    ekn_solid_packet_mass_from_compression,
    fluid_limit_mass,
)


def test_longitudinal_and_transverse_use_common_longitudinal_green_scale():
    assert ekn_solid_packet_mass(
        c_longitudinal=4.0, dlog_c_dlog_rho=0.25, energy=8.0
    ) == pytest.approx(-0.125)
    assert ekn_solid_packet_mass(
        c_longitudinal=4.0, dlog_c_dlog_rho=-0.5, energy=6.0
    ) == pytest.approx(0.1875)


def test_hydrostatic_compression_chain_rule():
    b0, cL, dc_db0, energy = 3.0, 5.0, 0.4, 7.0
    result = ekn_solid_packet_mass_from_compression(
        b0=b0, c_longitudinal=cL, dc_branch_db0=dc_db0, energy=energy
    )
    assert result == pytest.approx(-(b0 * dc_db0 / cL) * energy / cL**2)


def test_fluid_limit_reduces_to_standard_eos_formula():
    assert fluid_limit_mass(c_sound=3.0, slope=0.2, energy=9.0) == pytest.approx(-0.2)


@pytest.mark.parametrize("kwargs", [
    dict(c_longitudinal=0, dlog_c_dlog_rho=1, energy=1),
    dict(c_longitudinal=1, dlog_c_dlog_rho=1, energy=-1),
])
def test_invalid_inputs_rejected(kwargs):
    with pytest.raises(ValueError):
        ekn_solid_packet_mass(**kwargs)
