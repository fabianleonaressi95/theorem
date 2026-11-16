import numpy as np
import pytest
from audits.morphodynamics.q6_discriminant import (
    confusion_matrix, discriminant_scores, fit_discriminant,
    leave_one_group_out, mqm1_feature_vector, predict_discriminant, q6_incidence,
)


def test_descriptor_shape_and_global_phase_invariance():
    rng = np.random.default_rng(20261113)
    x = rng.normal(scale=0.05, size=192)
    x0 = np.linspace(-0.1, 0.1, 192)
    z = rng.normal(size=64) + 1j * rng.normal(size=64)
    psi = z / np.linalg.norm(z)
    s = [-1, 0, 1, -1, 0, 1]
    a = mqm1_feature_vector(x, psi, x0, ternary_state=s)
    b = mqm1_feature_vector(x, psi * np.exp(0.73j), x0, ternary_state=s)
    assert a.shape == (518,)
    assert np.allclose(a, b, atol=1e-12)
    assert q6_incidence().shape == (64, 192)


def test_ternary_descriptor_validation():
    psi = np.ones(64, complex) / 8
    with pytest.raises(ValueError, match="ternary_state"):
        mqm1_feature_vector(np.zeros(192), psi, np.zeros(192),
                            ternary_state=[-1, 0, 2, 0, 0, 1])


def test_lda_axes_scores_and_both_decision_rules():
    rng = np.random.default_rng(31)
    centers = np.array([[-3., 0., 0.], [0., 3., 0.], [3., 0., 0.]])
    X = np.vstack([c + .15 * rng.normal(size=(30, 3)) for c in centers])
    y = np.repeat(np.array(["A", "B", "C"]), 30)
    model = fit_discriminant(X, y, shrinkage=.05)
    assert model["directions"].shape == (3, 2)
    assert discriminant_scores(model, X).shape == (90, 2)
    for rule in ("pooled", "sebestyen"):
        pred, dist = predict_discriminant(model, X, rule=rule)
        assert np.mean(pred == y) > .98
        assert dist.shape == (90, 3)


def test_leave_one_trajectory_out():
    rng = np.random.default_rng(42)
    rows, labels, groups = [], [], []
    for trajectory in range(12):
        label = trajectory % 3
        for _ in range(5):
            rows.append(rng.normal(loc=label * 4., scale=.2, size=4))
            labels.append(label)
            groups.append(trajectory)
    result = leave_one_group_out(np.asarray(rows), np.asarray(labels),
                                 np.asarray(groups), shrinkage=.1)
    assert result["accuracy"] > .95
    assert result["confusion_matrix"].shape == (3, 3)
    assert result["predictions"].shape == (60,)


def test_confusion_matrix_orientation():
    classes, matrix = confusion_matrix([0, 0, 1, 1], [0, 1, 1, 1])
    assert classes.tolist() == [0, 1]
    assert matrix.tolist() == [[1, 1], [0, 2]]
