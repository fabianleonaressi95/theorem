"""Exploratory multidimensional analysis for finite Q6/MQM fields.

Vertex, edge and operator-level observations are kept in separate blocks.
The default graph features are combinatorial/unweighted proxies; callers must
supply metric edge weights before interpreting them as metric-action features.
No inferential or causal claims are made by PCA/correlation.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class MQMDataset:
    vertex_features: np.ndarray
    vertex_feature_names: tuple[str, ...]
    edge_features: np.ndarray
    edge_feature_names: tuple[str, ...]
    edge_labels: tuple[str, ...]


def canonical_q6_edges() -> tuple[tuple[int, int, int], ...]:
    """Frozen Q6 edge ordering: vertex-major, then bit/direction-major."""
    return tuple(
        (v, v ^ (1 << bit), bit)
        for v in range(64)
        for bit in range(6)
        if not (v & (1 << bit))
    )


def build_mqm_dataset(phi, tau, *, edges=None, metric_weights=None,
                      vertex_categories=None) -> MQMDataset:
    """Build separate vertex/edge tables from aligned Q6 scalar and torsion data.

    Vertex features: phi, tau, degree, neighbour-mean(phi), neighbour-std(phi),
    unweighted graph Laplacian(phi), and local quartic-potential density.
    If metric_weights are supplied, also add the exact weighted Dirichlet
    density assigned half to each endpoint. Otherwise no metric-energy
    feature is fabricated.

    Edge features: endpoint mean/difference of phi and tau, direction index,
    and (when supplied) metric conductance. Categorical vertex labels are
    validated and returned as edge labels only; they are never silently
    converted into ordinal numbers.
    """
    phi = np.asarray(phi, dtype=float)
    tau = np.asarray(tau, dtype=float)
    edges = canonical_q6_edges() if edges is None else tuple(tuple(e) for e in edges)
    if phi.shape != (64,) or tau.shape != (64,):
        raise ValueError("phi and tau must each contain 64 vertex values")
    if not np.all(np.isfinite(phi)) or not np.all(np.isfinite(tau)):
        raise ValueError("phi and tau must be finite")
    if len(edges) != 192:
        raise ValueError("Q6 must contain exactly 192 edges")
    edge_array = np.asarray(edges, dtype=int)
    if edge_array.shape != (192, 3) or np.any(edge_array[:, :2] < 0) or np.any(edge_array[:, :2] >= 64):
        raise ValueError("edges must have shape (192,3) with valid endpoints")
    if np.any(edge_array[:, 0] == edge_array[:, 1]) or np.any(edge_array[:, 2] < 0) or np.any(edge_array[:, 2] >= 6):
        raise ValueError("invalid Q6 edge or direction")
    if len({(min(int(u), int(v)), max(int(u), int(v))) for u, v, _ in edge_array}) != 192:
        raise ValueError("duplicate undirected edges")

    u, v, direction = edge_array.T
    degree = np.bincount(np.concatenate([u, v]), minlength=64).astype(float)
    neighbour_sum = np.bincount(np.concatenate([u, v]),
                                weights=np.concatenate([phi[v], phi[u]]), minlength=64)
    neighbour_sq = np.bincount(np.concatenate([u, v]),
                               weights=np.concatenate([phi[v]**2, phi[u]**2]), minlength=64)
    neighbour_mean = neighbour_sum / degree
    neighbour_var = np.maximum(0.0, neighbour_sq / degree - neighbour_mean**2)
    lap_phi = degree * phi - neighbour_sum
    potential_density = 0.25 * (phi**2 - 1.0)**2

    vertex_columns = [phi, tau, degree, neighbour_mean,
                      np.sqrt(neighbour_var), lap_phi, potential_density]
    vertex_names = ["phi", "tau", "degree", "neighbour_phi_mean",
                    "neighbour_phi_std", "q6_laplacian_phi",
                    "quartic_potential_density"]

    if metric_weights is not None:
        weights = np.asarray(metric_weights, dtype=float)
        if weights.shape != (192,) or np.any(~np.isfinite(weights)) or np.any(weights <= 0):
            raise ValueError("metric_weights must be 192 finite positive conductances")
        edge_dirichlet = 0.5 * weights * (phi[v] - phi[u])**2
        local_metric_energy = np.bincount(
            np.concatenate([u, v]),
            weights=np.concatenate([0.5 * edge_dirichlet, 0.5 * edge_dirichlet]),
            minlength=64,
        )
        vertex_columns.append(local_metric_energy)
        vertex_names.append("metric_dirichlet_energy_density")

    vertex_features = np.column_stack(vertex_columns)
    edge_columns = [
        0.5 * (phi[u] + phi[v]), phi[v] - phi[u],
        0.5 * (tau[u] + tau[v]), tau[v] - tau[u],
        direction.astype(float),
    ]
    edge_names = ["phi_endpoint_mean", "delta_phi",
                  "tau_endpoint_mean", "delta_tau", "q6_direction"]
    if metric_weights is not None:
        edge_columns.append(weights)
        edge_names.append("metric_conductance")
    edge_features = np.column_stack(edge_columns)

    if vertex_categories is None:
        labels = tuple("unclassified" for _ in range(192))
    else:
        categories = tuple(str(x) for x in vertex_categories)
        if len(categories) != 64:
            raise ValueError("vertex_categories must contain 64 labels")
        labels = tuple(f"{categories[int(a)]}|{categories[int(b)]}" for a, b in zip(u, v))

    return MQMDataset(vertex_features, tuple(vertex_names), edge_features,
                      tuple(edge_names), labels)


def standardized_pca(matrix, *, n_components=None):
    """SVD-based descriptive PCA; returns scores, loadings, singular values.

    Constant columns are retained with unit scale and therefore contribute
    zero variance. The result is descriptive, not a significance test.
    """
    x = np.asarray(matrix, dtype=float)
    if x.ndim != 2 or x.shape[0] < 2 or x.shape[1] < 1 or not np.all(np.isfinite(x)):
        raise ValueError("matrix must be finite 2D data with >=2 rows and >=1 column")
    mean = x.mean(axis=0)
    scale = x.std(axis=0)
    scale[scale == 0] = 1.0
    z = (x - mean) / scale
    _, singular, vt = np.linalg.svd(z, full_matrices=False)
    k = min(len(singular), n_components if n_components is not None else len(singular))
    if k < 1:
        raise ValueError("n_components must be positive")
    scores = z @ vt[:k].T
    variance = singular**2
    ratio = variance / variance.sum() if variance.sum() else np.zeros_like(variance)
    return {
        "scores": scores[:, :k],
        "loadings": vt[:k].T,
        "singular_values": singular[:k],
        "explained_variance_ratio": ratio[:k],
        "feature_mean": mean,
        "feature_scale": scale,
    }


def correlation_matrix(matrix):
    """Pearson correlations across columns; constant columns yield NaN."""
    x = np.asarray(matrix, dtype=float)
    if x.ndim != 2 or x.shape[0] < 2 or not np.all(np.isfinite(x)):
        raise ValueError("matrix must be finite 2D data with at least two rows")
    return np.corrcoef(x, rowvar=False)
