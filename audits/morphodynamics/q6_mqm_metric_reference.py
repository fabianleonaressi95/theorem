"""RGS-PSU coframe metric pullback for the MQM-1 Q6 reference."""
from __future__ import annotations
import numpy as np
from src.rgs_seed_64_reconstruction import load_rgs_seed_data
from audits.morphodynamics.q6_mqm_symmetry import q6_edges, edge_permutation
from audits.morphodynamics.q6_mqm_anisotropic_stabilizer import rgs_gate_vertex_permutations

def rgs_psu_edge_coframes():
    """Reconstruct the documented raw PSU coframe (Delta X, Delta ||X||)."""
    x = load_rgs_seed_data().coordinates
    radii = np.linalg.norm(x, axis=1)
    return np.asarray([
        np.r_[x[v]-x[u], radii[v]-radii[u]]
        for u,v,_ in q6_edges()
    ], dtype=float)

def rgs_edge_lengths():
    """Metric-graph edge lengths induced by the four-component PSU coframe."""
    return np.linalg.norm(rgs_psu_edge_coframes(), axis=1)

def metric_reference():
    lengths = rgs_edge_lengths()
    if lengths.shape != (192,) or not np.all(np.isfinite(lengths)) or np.any(lengths <= 0):
        raise ValueError("PSU coframe lengths must be 192 finite positive values")
    ell_rms = float(np.sqrt(np.mean(lengths**2)))
    return np.log(ell_rms/lengths)

def metric_reference_report():
    lengths = rgs_edge_lengths()
    ell_rms = float(np.sqrt(np.mean(lengths**2)))
    x_ref = np.log(ell_rms/lengths)
    edge_actions = [edge_permutation(p) for p in rgs_gate_vertex_permutations()]
    residuals = [float(np.max(np.abs(x_ref-x_ref[np.asarray(ep,dtype=int)])))
                 for ep in edge_actions]
    edges = q6_edges()
    by_direction = {}
    for direction in range(6):
        selected = np.asarray([bit == direction for _,_,bit in edges])
        by_direction[str(direction)] = {
            "edge_count": int(selected.sum()),
            "rms_length": float(np.sqrt(np.mean(lengths[selected]**2))),
            "mean_squared_length": float(np.mean(lengths[selected]**2)),
        }
    unique, counts = np.unique(np.round(lengths,12),return_counts=True)
    return {
        "seed_sha256": "6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf",
        "psu_coframe": "(X_v-X_u, ||X_v||-||X_u||) in R^4",
        "metric_choice": "w_e=ell_rms/||C_e_PSU||; x*_e=log(w_e)",
        "ell_rms": ell_rms,
        "edge_count": int(len(lengths)),
        "distinct_rounded_edge_lengths": int(len(unique)),
        "edge_length_class_counts": {str(float(a)):int(n) for a,n in zip(unique,counts)},
        "directional_rms_lengths": by_direction,
        "rgs_q6_gate_group_order": len(edge_actions),
        "max_reference_invariance_residual": max(residuals),
        "all_16_gates_preserve_reference": max(residuals) <= 1e-12,
        "classification": "finite-seed numerical RGS-PSU metric pullback; physical constitutive calibration open",
    }
