from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.morandotti_resolution_decomposition import analyze_report
from pathlib import Path\nimport sys\n\nROOT = Path(__file__).resolve().parents[1]\nif str(ROOT) not in sys.path:\n    sys.path.insert(0, str(ROOT))\n\nfrom scripts.morandotti_resolution_decomposition import analyze_report


def _report():
    rows = []
    for distance in (0.48, 0.56):
        for h, center in ((0.08, 10.0), (0.04, 5.0)):
            for seed, delta in enumerate((-1.0, 0.0, 1.0), start=1):
                rows.append({
                    "distance": distance,
                    "h_target": h,
                    "mesh_seed": seed,
                    "signed_anisotropy_A_d": center + delta,
                    "normalized_coupling_C_d": center / 10 + delta / 10,
                })
    return {"runs": rows}


def test_decomposes_resolution_and_within_resolution_spread():
    result = analyze_report(_report())
    d = result["by_distance"]["0.4800"]
    component = d["decomposition"]["signed_anisotropy_A_d"]
    assert component["between_resolution_sum_squares_fraction"] > 0.9
    assert component["within_resolution_sum_squares_fraction"] < 0.1
    assert d["mesh_sizes"]["0.080000"]["signed_anisotropy_A_d"]["sample_std"] == 1.0


def test_rejects_insufficient_remesh_replicates():
    report = _report()
    report["runs"] = report["runs"][:5]
    try:
        analyze_report(report)
    except ValueError:
        pass
    else:
        raise AssertionError("expected insufficient-replicate validation")


def test_rejects_unbalanced_resolution_groups():
    report = _report()
    report["runs"].pop()
    try:
        analyze_report(report)
    except ValueError:
        pass
    else:
        raise AssertionError("expected unbalanced-group validation")
