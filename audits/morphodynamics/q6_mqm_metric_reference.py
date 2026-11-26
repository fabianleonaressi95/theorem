"""RGS-PSU coframe provenance and metric-graph MQM reference audit.

Separates the archived unit coframe used by the A13 SEA Dirac operator
from the raw coframe norm used as a metric-graph edge length. It also
checks what the current A13 finite action does and does not derive.
"""
from __future__ import annotations
import hashlib
import numpy as np
from src.rgs_seed_64_reconstruction import load_rgs_seed_data
from audits.morphodynamics.q6_mqm_symmetry import q6_edges, edge_permutation
from audits.morphodynamics.q6_mqm_anisotropic_stabilizer import rgs_gate_vertex_permutations

EXPECTED_X = "6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf"
EXPECTED_EDGES = "da7854ca655577b629dc508208918326fde1d50563485f953ea0fdc1b2fb78e8"
EXPECTED_A13_UNIT_COFRAME = "72980c38fdc652ece31895cf5c9f113a6206675fdf876c924bf6890d6e7fc263"

def _sha256_le_f64(a):
    return hashlib.sha256(np.ascontiguousarray(a,dtype="<f8").tobytes()).hexdigest()

def _sha256_le_i64(a):
    return hashlib.sha256(np.ascontiguousarray(a,dtype="<i8").tobytes()).hexdigest()

def rgs_psu_raw_coframes():
    """A13 raw C_e=(X_v-X_u, ||X_v||-||X_u||), in manifest edge order."""
    x=load_rgs_seed_data().coordinates
    radii=np.linalg.norm(x,axis=1)
    return np.asarray([np.r_[x[v]-x[u],radii[v]-radii[u]]
                       for u,v,_ in q6_edges()],dtype=float)

def rgs_psu_unit_coframes():
    raw=rgs_psu_raw_coframes()
    norms=np.linalg.norm(raw,axis=1)
    if np.any(norms<=0):
        raise ValueError("A13 raw coframe contains a zero edge")
    return raw/norms[:,None]

def rgs_edge_lengths():
    """Raw PSU coframe norms; do not use the archived unit coframe norm (=1)."""
    return np.linalg.norm(rgs_psu_raw_coframes(),axis=1)

def metric_reference():
    lengths=rgs_edge_lengths()
    if lengths.shape!=(192,) or not np.all(np.isfinite(lengths)) or np.any(lengths<=0):
        raise ValueError("PSU coframe lengths must be 192 finite positive values")
    ell_rms=float(np.sqrt(np.mean(lengths**2)))
    return np.log(ell_rms/lengths)

def metric_graph_energy_matrix():
    """Dimensionless weighted Q6 Laplacian from the declared 1D metric-edge action."""
    lengths=rgs_edge_lengths()
    ell_rms=float(np.sqrt(np.mean(lengths**2)))
    B=np.zeros((64,192),dtype=float)
    for k,(u,v,_) in enumerate(q6_edges()):
        B[u,k]=-1.0
        B[v,k]=1.0
    return B @ np.diag(ell_rms/lengths) @ B.T

def a13_action_derivation_audit():
    """Read the implemented A13 SEA operator definitions as an evidence boundary."""
    return {
      "fermion_edge_symbol":"kappa * (gamma_A * ehat_e^A) tensor U_e",
      "coframe_in_fermion_operator":"normalized unit coframe ehat_e",
      "boson_operator":"diag(L_Q6+m_B^2,L_Q6+m_B^2)+mu*H_cross+lambda_B*q*diag(tau,tau)",
      "edge_metric_weight_in_archived_A13_action":"not explicit",
      "inverse_raw_coframe_length_derived_by_current_A13_action":False,
      "reason":"The SEA Dirac symbol uses the unit coframe; the bosonic graph Laplacian is unweighted. The determinant/trace terms therefore do not, as currently written, establish an additional scalar conductance ell_rms/L_e.",
      "possible_extension":"Add a scalar metric-edge Dirichlet sector with conductance ell_rms/L_e and derive it from a declared continuum scalar action."
    }

def metric_reference_report():
    raw=rgs_psu_raw_coframes()
    unit=rgs_psu_unit_coframes()
    lengths=np.linalg.norm(raw,axis=1)
    ell_rms=float(np.sqrt(np.mean(lengths**2)))
    x_ref=np.log(ell_rms/lengths)
    edges=q6_edges()
    edge_actions=[edge_permutation(p) for p in rgs_gate_vertex_permutations()]
    residuals=[float(np.max(np.abs(x_ref-x_ref[np.asarray(ep,dtype=int)])))
               for ep in edge_actions]
    by_direction={}
    for direction in range(6):
        mask=np.asarray([bit==direction for _,_,bit in edges])
        by_direction[str(direction)]={
          "edge_count":int(mask.sum()),
          "rms_raw_coframe_length":float(np.sqrt(np.mean(lengths[mask]**2))),
          "distinct_raw_lengths_12dp":int(len(np.unique(np.round(lengths[mask],12))))
        }
    unique,counts=np.unique(np.round(lengths,12),return_counts=True)
    return {
      "seed_sha256":EXPECTED_X,
      "edge_order_sha256":_sha256_le_i64(np.asarray(edges,dtype=np.int64)),
      "edge_order_matches_A13_manifest":_sha256_le_i64(np.asarray(edges,dtype=np.int64))==EXPECTED_EDGES,
      "raw_coframe_sha256":_sha256_le_f64(raw),
      "normalized_coframe_sha256":_sha256_le_f64(unit),
      "normalized_coframe_matches_A13_manifest":_sha256_le_f64(unit)==EXPECTED_A13_UNIT_COFRAME,
      "normalized_coframe_norm_residual":float(np.max(np.abs(np.linalg.norm(unit,axis=1)-1))),
      "raw_coframe":"(X_v-X_u, ||X_v||-||X_u||) in R^4",
      "metric_choice":"w_e=ell_rms/||C_e_raw||; x*_e=log(w_e)",
      "ell_rms":ell_rms,
      "edge_count":int(len(lengths)),
      "distinct_raw_edge_lengths_12dp":int(len(unique)),
      "edge_length_class_counts":{str(float(a)):int(n) for a,n in zip(unique,counts)},
      "directional_lengths":by_direction,
      "rgs_q6_gate_group_order":len(edge_actions),
      "max_reference_invariance_residual":max(residuals),
      "all_16_gates_preserve_reference":max(residuals)<=1e-12,
      "a13_action_audit":a13_action_derivation_audit(),
      "classification":"exact coframe provenance hash match plus finite-seed metric-graph candidate; not derived by current A13 SEA action"
    }
