import numpy as np
import pytest

from models.constitutive_hysteresis import (
    asymmetric_play_features,
    fit_asymmetric_prandtl_ishlinskii,
    predict_asymmetric_prandtl_ishlinskii,
)


def test_asymmetric_play_has_distinct_loading_unloading_memory():
    up = np.linspace(-1.0, 1.0, 101)
    down = np.linspace(1.0, -1.0, 101)[1:]
    u = np.r_[up, down]
    features = asymmetric_play_features(u, [0.1, 0.25], [0.4, 0.6])
    assert features.shape == (len(u), 2)
    assert np.all(np.isfinite(features))
    # Unequal projection widths produce a genuinely asymmetric branch response.
    assert not np.allclose(features[:101, 0], features[101:, 0][::-1])


def test_asymmetric_pi_fit_predicts_fixed_dictionary_training_history():
    up = np.linspace(-1.0, 1.0, 101)
    down = np.linspace(1.0, -1.0, 101)[1:]
    u = np.r_[up, down, up[1:]]
    lower = np.array([0.08, 0.2, 0.35])
    upper = np.array([0.15, 0.3, 0.5])
    Phi = asymmetric_play_features(u, lower, upper)
    y = 0.3 * u + Phi @ np.array([0.7, -0.2, 0.1])
    model = fit_asymmetric_prandtl_ishlinskii(u, y, lower, upper)
    prediction = predict_asymmetric_prandtl_ishlinskii(u, model)
    assert prediction.shape == y.shape
    assert np.all(np.isfinite(prediction))
    assert np.sqrt(np.mean((prediction - y) ** 2)) < 1e-10


def test_asymmetric_pi_rejects_incompatible_thresholds():
    with pytest.raises(ValueError):
        asymmetric_play_features(np.arange(5.0), [0.1, 0.2], [0.3])
