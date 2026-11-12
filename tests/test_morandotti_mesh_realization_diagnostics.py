from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.morandotti_mesh_realization_diagnostics import diagnose_run


def test_reports_core_exchange_mismatch_and_mesh_quality(tmp_path):
    coordinates = np.array([
        [0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0],
        [2.0, 0.0, 0.0], [3.0, 0.0, 0.0], [2.0, 1.0, 0.0],
    ])
    dofmap = np.array([[0, 1, 2], [3, 4, 5]])
    M = np.zeros((6, 6))
    M[1:3, 1:3] = np.eye(2)
    M[4:6, 4:6] = 2.0 * np.eye(2)
    M[1:3, 4:6] = np.array([[0.2, 0.1], [0.1, 0.3]])
    M[4:6, 1:3] = M[1:3, 4:6].T
    path = tmp_path / "fields.npz"
    np.savez(
        path,
        geometry_coordinates=coordinates,
        geometry_dofmap=dofmap,
        M_laplacian=M,
        M_boundary_flux=np.zeros((6, 6)),
        M_interior_facet_flux=np.zeros((6, 6)),
    )
    row = {
        "distance": 0.48,
        "h_target": 0.08,
        "mesh_seed": 11,
        "field_export": str(path),
        "interior_facet_traction_jump_L2": {"case": 0.01},
    }
    result = diagnose_run(row)
    assert result["corner_quality_min"] > 0.8
    assert result["self_block_relative_mismatch"] > 0.3
    assert result["cross_block_reciprocity_relative"] == 0.0
    cross_norm = np.linalg.norm(M[1:3, 4:6])
    assert np.isclose(result["C_d_original_core0_normalized"], cross_norm / np.linalg.norm(M[1:3, 1:3]))
    assert np.isclose(
        result["C_d_symmetric_geometric_mean_normalized"],
        cross_norm / np.sqrt(np.linalg.norm(M[1:3, 1:3]) * np.linalg.norm(M[4:6, 4:6])),
    )
    assert result["C_d_symmetric_geometric_mean_normalized"] > result["C_d_original_core0_normalized"]
