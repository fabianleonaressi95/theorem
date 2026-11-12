import importlib.util
from pathlib import Path
import pytest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "audit_t110_gp_zero_vortex.py"
spec = importlib.util.spec_from_file_location("audit_t110_gp_zero_vortex", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

@pytest.mark.parametrize("n", [8, 16, 32, 64, 128])
def test_single_simple_zero_has_unit_plaquette_index(n):
    result = module.audit_one(n)
    assert result.plaquette_charge == 1
    assert result.detected_cells == 1
    assert result.max_abs_charge == 1

def test_zero_localization_error_is_cell_scale():
    for n in [8, 16, 32, 64, 128]:
        result = module.audit_one(n)
        assert result.localization_error <= (2**0.5)*result.grid_spacing/2 + 1e-12

def test_full_refinement_report_passes_acceptance():
    report = module.run([8, 16, 32, 64, 128])
    assert report["acceptance"]["one_unit_positive_plaquette_per_grid"]
    assert report["acceptance"]["localization_error_bounded_by_sqrt2_h_over_2"]
