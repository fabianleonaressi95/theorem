#!/usr/bin/env python3
"""Build the first reproducible vertex/edge MQM multivariate audit from A13."""
from __future__ import annotations
import argparse
from io import BytesIO
import json
from pathlib import Path
import zipfile
import numpy as np

from models.mqm_multidimensional import build_mqm_dataset, standardized_pca, correlation_matrix


def load_npz(zf, suffix):
    matches = [name for name in zf.namelist() if name.endswith(suffix)]
    if len(matches) != 1:
        raise ValueError(f"expected one {suffix}, found {len(matches)}")
    return np.load(BytesIO(zf.read(matches[0])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", required=True, type=Path)
    parser.add_argument("--field-report", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    report = json.loads(args.field_report.read_text())
    phi = np.asarray(report["stationary_local_field"]["phi_by_q6_vertex"], dtype=float)
    with zipfile.ZipFile(args.bundle) as zf:
        fibre = load_npz(zf, "psu_fibre_connection_matrices.npz")
        X = np.asarray(fibre["X"], dtype=float)
        edges = np.asarray(fibre["edges"], dtype=int)
        radii = np.linalg.norm(X, axis=1)
        raw = np.column_stack([
            X[edges[:, 1]] - X[edges[:, 0]],
            radii[edges[:, 1]] - radii[edges[:, 0]],
        ])
        lengths = np.linalg.norm(raw, axis=1)
        weights = float(np.sqrt(np.mean(lengths**2))) / lengths
        sea = load_npz(zf, "sea_operators.npz")
        tau = np.asarray(sea["tau"], dtype=float)

    data = build_mqm_dataset(phi, tau, edges=edges, metric_weights=weights)
    # The regular degree column is structural metadata and has zero variance.
    varying = np.std(data.vertex_features, axis=0) > 1e-14
    reduced = data.vertex_features[:, varying]
    reduced_names = [name for name, keep in zip(data.vertex_feature_names, varying) if keep]
    pca = standardized_pca(reduced, n_components=min(5, reduced.shape[1]))
    corr = correlation_matrix(reduced)

    def finite_or_none(array):
        return [[float(x) if np.isfinite(x) else None for x in row]
                for row in np.atleast_2d(array)]

    result = {
        "status": "EXPLORATORY_FINITE_Q6_MULTIVARIATE_AUDIT",
        "input_field_report": args.field_report.name,
        "observational_units": {"vertices": 64, "edges": 192, "operator_global": "kept separate"},
        "vertex_feature_names": list(data.vertex_feature_names),
        "vertex_feature_matrix": data.vertex_features.tolist(),
        "edge_feature_names": list(data.edge_feature_names),
        "edge_feature_matrix": data.edge_features.tolist(),
        "edge_labels": list(data.edge_labels),
        "pca_feature_names": reduced_names,
        "pca": {
            "scores": pca["scores"].tolist(),
            "loadings": pca["loadings"].tolist(),
            "explained_variance_ratio": pca["explained_variance_ratio"].tolist(),
        },
        "pearson_correlation": {
            "feature_names": reduced_names,
            "matrix": finite_or_none(corr),
        },
        "checks": {
            "q6_degree_constant_six": bool(np.allclose(data.vertex_features[:, 2], 6.0)),
            "metric_weights_positive": bool(np.all(weights > 0)),
            "phi_tau_correlation": float(np.corrcoef(phi, tau)[0, 1]),
            "metric_dirichlet_total": float(data.vertex_features[:, -1].sum()),
            "edge_order_preserved": bool(len(data.edge_features) == 192),
        },
        "interpretation": [
            "PCA and correlations are descriptive summaries of this single finite Q6 solution.",
            "The phi-tau association is model-conditioned because tau enters the determinant coupling.",
            "The 64 vertex rows are spatially coupled observations, not independent samples.",
            "Operator spectra and solver-level quantities are intentionally not replicated across vertices.",
        ],
        "limitations": [
            "No inferential p-values, causal claims, or population sampling interpretation.",
            "No continuum refinement or physical-unit calibration is established.",
            "Categorical symmetry/orbit labels remain labels and require a declared mixed-data method.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result["checks"], indent=2))


if __name__ == "__main__":
    main()
