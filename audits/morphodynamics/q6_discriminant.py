"""Discriminant analysis for finite MQM-1 / Q6 configurations."""
from __future__ import annotations
import numpy as np


def q6_incidence():
    """Oriented incidence matrix of the six-cube: 64 vertices, 192 edges."""
    b = np.zeros((64, 192), dtype=float)
    j = 0
    for v in range(64):
        for bit in range(6):
            if ((v >> bit) & 1) == 0:
                b[v, j] = -1.0
                b[v ^ (1 << bit), j] = 1.0
                j += 1
    return b


def mqm1_feature_vector(x, psi, x_reference, *, incidence=None,
                        include_spectrum=True, ternary_state=None):
    """Real global-phase-invariant MQM descriptor.

    Blocks: x-x_reference (192), |psi|^2 (64),
    exp(x)|B.T psi|^2 (192), eigvalsh(H(x)) (64, optional),
    and an optional explicitly supplied six-entry ternary descriptor.
    """
    x = np.asarray(x, float)
    x0 = np.asarray(x_reference, float)
    psi = np.asarray(psi, complex)
    if x.shape != (192,) or x0.shape != (192,):
        raise ValueError("x and x_reference must have shape (192,)")
    if psi.shape != (64,) or not np.all(np.isfinite(psi)):
        raise ValueError("psi must be a finite complex vector of length 64")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(x0)):
        raise ValueError("geometry vectors must be finite")
    if not np.isclose(np.vdot(psi, psi).real, 1.0, atol=1e-10, rtol=1e-10):
        raise ValueError("psi must have unit norm")
    b = q6_incidence() if incidence is None else np.asarray(incidence, float)
    if b.shape != (64, 192):
        raise ValueError("incidence must have shape (64, 192)")
    blocks = [x - x0, np.abs(psi)**2, np.exp(x) * np.abs(b.T @ psi)**2]
    if include_spectrum:
        h = (b * np.exp(x)) @ b.T
        blocks.append(np.linalg.eigvalsh(h))
    if ternary_state is not None:
        s = np.asarray(ternary_state)
        if s.shape != (6,) or not np.all(np.isin(s, (-1, 0, 1))):
            raise ValueError("ternary_state must contain six entries in {-1,0,+1}")
        blocks.append(s.astype(float))
    return np.concatenate(blocks)


def _regularized_covariance(residuals, shrinkage):
    n, p = residuals.shape
    cov = residuals.T @ residuals / max(n - 1, 1)
    scale = float(np.trace(cov) / p)
    if not np.isfinite(scale) or scale <= np.finfo(float).eps:
        scale = 1.0
    return (1.0 - shrinkage) * cov + shrinkage * scale * np.eye(p)


def fit_discriminant(X, y, *, shrinkage=0.1):
    """Fit regularized Fisher LDA; returns at most k-1 discriminant axes."""
    X, y = np.asarray(X, float), np.asarray(y)
    if X.ndim != 2 or y.ndim != 1 or X.shape[0] != y.size:
        raise ValueError("X must be 2-D and y must have one label per row")
    if X.shape[0] < 3 or X.shape[1] < 1 or not np.all(np.isfinite(X)):
        raise ValueError("X must contain at least three finite observations")
    if not 0.0 < shrinkage <= 1.0:
        raise ValueError("shrinkage must lie in (0, 1]")
    classes = np.unique(y)
    if classes.size < 2:
        raise ValueError("at least two independently defined classes are required")
    n, p = X.shape
    mean = X.mean(axis=0)
    within = np.zeros((p, p))
    between = np.zeros((p, p))
    means, covs, priors = [], [], []
    for label in classes:
        Xi = X[y == label]
        mi = Xi.mean(axis=0)
        residual = Xi - mi
        within += residual.T @ residual
        delta = mi - mean
        between += Xi.shape[0] * np.outer(delta, delta)
        means.append(mi)
        covs.append(_regularized_covariance(residual, shrinkage))
        priors.append(Xi.shape[0] / n)
    within /= max(n - classes.size, 1)
    scale = float(np.trace(within) / p)
    if not np.isfinite(scale) or scale <= np.finfo(float).eps:
        scale = 1.0
    within_reg = (1.0 - shrinkage) * within + shrinkage * scale * np.eye(p)
    ew, qw = np.linalg.eigh(within_reg)
    ew = np.maximum(ew, np.finfo(float).eps * max(1.0, ew.max()))
    invsqrt = (qw / np.sqrt(ew)) @ qw.T
    whitened = invsqrt @ between @ invsqrt
    vals, vecs = np.linalg.eigh((whitened + whitened.T) / 2)
    order = np.argsort(vals)[::-1][:classes.size - 1]
    return {
        "classes": classes, "mean": mean, "class_means": np.asarray(means),
        "class_covariances": np.asarray(covs), "class_priors": np.asarray(priors),
        "within_covariance": within_reg, "between_scatter": between,
        "eigenvalues": np.maximum(vals[order], 0.0),
        "directions": invsqrt @ vecs[:, order],
        "shrinkage": float(shrinkage), "n_features": p,
    }


def discriminant_scores(model, X):
    X = np.asarray(X, float)
    if X.ndim != 2 or X.shape[1] != model["n_features"]:
        raise ValueError("X has the wrong feature dimension")
    return (X - model["mean"]) @ model["directions"]


def predict_discriminant(model, X, *, rule="pooled"):
    """Pooled Mahalanobis or class-specific Sebestyen-type distance."""
    X = np.asarray(X, float)
    if X.ndim != 2 or X.shape[1] != model["n_features"]:
        raise ValueError("X has the wrong feature dimension")
    if rule not in ("pooled", "sebestyen"):
        raise ValueError("rule must be 'pooled' or 'sebestyen'")
    distances = np.empty((len(X), len(model["classes"])))
    for j, center in enumerate(model["class_means"]):
        delta = X - center
        cov = model["within_covariance"] if rule == "pooled" else model["class_covariances"][j]
        solved = np.linalg.solve(cov, delta.T).T
        distances[:, j] = np.einsum("ij,ij->i", delta, solved)
    return model["classes"][np.argmin(distances, axis=1)], distances


def confusion_matrix(y_true, y_pred, classes=None):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    if y_true.shape != y_pred.shape or y_true.ndim != 1:
        raise ValueError("y_true and y_pred must be equal-length vectors")
    classes = np.unique(np.concatenate((y_true, y_pred))) if classes is None else np.asarray(classes)
    lookup = {label: i for i, label in enumerate(classes.tolist())}
    out = np.zeros((len(classes), len(classes)), dtype=int)
    for a, b in zip(y_true, y_pred):
        if a not in lookup or b not in lookup:
            raise ValueError("labels are not contained in classes")
        out[lookup[a], lookup[b]] += 1
    return classes, out


def leave_one_group_out(X, y, groups, *, shrinkage=0.1, rule="sebestyen"):
    """Hold out complete trajectories/groups to prevent time-sample leakage."""
    X, y, groups = np.asarray(X, float), np.asarray(y), np.asarray(groups)
    if X.ndim != 2 or y.ndim != 1 or groups.ndim != 1:
        raise ValueError("X, y, groups must be 2-D, 1-D, 1-D")
    if len(X) != len(y) or len(y) != len(groups):
        raise ValueError("X, y and groups must have equal row counts")
    unique = np.unique(groups)
    if len(unique) < 2:
        raise ValueError("at least two independent trajectories/groups are required")
    pred = np.empty(y.shape, dtype=y.dtype)
    dist = [None] * len(y)
    for group in unique:
        test, train = groups == group, groups != group
        if np.unique(y[train]).size < 2:
            raise ValueError("a training fold contains fewer than two classes")
        model = fit_discriminant(X[train], y[train], shrinkage=shrinkage)
        p, d = predict_discriminant(model, X[test], rule=rule)
        pred[test] = p
        for idx, row in zip(np.flatnonzero(test), d):
            dist[idx] = row
    classes, matrix = confusion_matrix(y, pred)
    return {"predictions": pred, "distances": np.asarray(dist), "classes": classes,
            "confusion_matrix": matrix, "accuracy": float(np.mean(pred == y))}
