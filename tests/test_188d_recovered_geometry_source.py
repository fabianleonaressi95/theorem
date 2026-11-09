import csv
from pathlib import Path

import numpy as np


def load_original_coordinates():
    path = Path(__file__).resolve().parents[1] / "data/rgs_188d/X_Oh_reconstructed.csv"
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 64
    return np.asarray([[float(row[k]) for k in ("x", "y", "z")] for row in rows])


def test_recovered_original_geometry_shape_finite_and_rank():
    x = load_original_coordinates()
    assert x.shape == (64, 3)
    assert np.isfinite(x).all()
    assert np.linalg.matrix_rank(x - x.mean(axis=0)) == 3
    assert np.linalg.norm(x.mean(axis=0)) < 1e-14


def test_recovered_original_geometry_exact_antipodal_pairing():
    x = load_original_coordinates()
    distances = np.linalg.norm(x[:, None, :] + x[None, :, :], axis=2)
    partner = distances.argmin(axis=1)
    assert distances[np.arange(64), partner].max() < 1e-14
    assert np.array_equal(np.sort(partner), np.arange(64))
    assert np.array_equal(partner[partner], np.arange(64))


def test_recovered_original_geometry_isotropic_second_moment():
    x = load_original_coordinates()
    covariance = (x - x.mean(axis=0)).T @ (x - x.mean(axis=0)) / 64
    assert np.linalg.norm(covariance - 1.25 * np.eye(3), ord="fro") < 1e-12
