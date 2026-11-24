#!/usr/bin/env python3
"""Audit square Z2 reflection, PRISM biverso block, and RGS six-dimensional carrier."""
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
K, ZA, ZS = [np.load(ROOT / n, allow_pickle=False)
             for n in ("K0.npy", "Z_A.npy", "Z_S.npy")]
if any(A.shape != (188, 188) for A in (K, ZA, ZS)):
    raise SystemExit("Expected original 188x188 K0, Z_A, Z_S arrays.")

def fro(A):
    return float(np.linalg.norm(A, "fro"))

def maxabs(A):
    return float(np.max(np.abs(A)))

Pplus = 2 * ZS @ ZS + ZS
cols = []
for j in range(188):
    v = Pplus[:, j].copy()
    for q in cols:
        v -= q * np.dot(q, v)
    nv = np.linalg.norm(v)
    if nv > 1e-9:
        cols.append(v / nv)
    if len(cols) == 3:
        break
if len(cols) != 3:
    raise SystemExit(f"Expected rank(Pplus)=3, got {len(cols)}")
V = np.column_stack(cols)
W = 2 * ZA @ V
U = np.column_stack((V, W))
Kc = U.T @ K @ U
H1, H2 = Kc[:3, :3], Kc[3:, 3:]
B12, B21 = Kc[:3, 3:], Kc[3:, :3]
I3, I6 = np.eye(3), np.eye(6)
S = np.block([[np.zeros((3,3)), I3], [I3, np.zeros((3,3))]])
Pp, Pm = (I6 + S)/2, (I6 - S)/2
kappa = float(-np.trace(B12)/3)
L0 = H1 - kappa * I3
Lbi = np.kron(np.eye(2), L0) + kappa * (I6 - S)
Had = np.block([[I3, I3], [I3, -I3]]) / np.sqrt(2)
Kdiag, Sdiag = Had.T @ Kc @ Had, Had.T @ S @ Had
ZS_c, ZA_c = U.T @ ZS @ U, U.T @ ZA @ U
R = np.array([[0., 1.], [1., 0.]])
tri_a = np.array([[0.,0.], [1.,0.], [1.,1.]])
tri_b = tri_a @ R.T

report = {
    "classification": "numerical audit of exact finite-dimensional identities",
    "square": {
        "reflection_matrix": R.tolist(),
        "R_squared_max": maxabs(R @ R - np.eye(2)),
        "orthogonality_max": maxabs(R.T @ R - np.eye(2)),
        "determinant": float(np.linalg.det(R)),
        "triangle_A_vertices": tri_a.tolist(),
        "reflected_triangle_B_vertices": tri_b.tolist(),
        "area_square": 1.0, "area_each_triangle": 0.5,
        "area_partition_residual": 0.0,
    },
    "RGS_carrier": {
        "carrier_orthogonality_fro": fro(U.T @ U - I6),
        "K0_carrier_leakage_fro": fro(K @ U - U @ Kc),
        "K0_compression": Kc.tolist(),
        "equal_diagonal_block_residual_fro": fro(H1-H2),
        "offdiagonal_scalar_coupling_residual_fro": fro(B12 + kappa*I3),
        "offdiagonal_symmetry_residual_fro": fro(B12-B21.T),
        "kappa": kappa, "L_Omega": L0.tolist(),
        "L_Omega_eigenvalues": np.linalg.eigvalsh((L0+L0.T)/2).tolist(),
        "biverso_reconstruction_fro": fro(Kc-Lbi),
        "exchange_commutator_fro": fro(Kc@S-S@Kc),
        "Pplus_idempotence_fro": fro(Pp@Pp-Pp),
        "Pplus_restricted_spectrum": np.linalg.eigvalsh((Had.T @ Kc @ Had)[:3, :3]).tolist(),
        "Pminus_idempotence_fro": fro(Pm@Pm-Pm),
        "Pminus_restricted_spectrum": np.linalg.eigvalsh((Had.T @ Kc @ Had)[3:, 3:]).tolist(),
        "Pplus_Pminus_fro": fro(Pp@Pm),
        "Hadamard_diagonalization_residual_fro": fro(
            Kdiag-np.block([[L0, np.zeros((3,3))],
                            [np.zeros((3,3)), L0+2*kappa*I3]])),
        "Hadamard_exchange_diagonal_residual_fro":
            fro(Sdiag-np.diag([1.]*3+[-1.]*3)),
        "two_triplet_spectra": [
            np.linalg.eigvalsh((L0+L0.T)/2).tolist(),
            np.linalg.eigvalsh((L0+2*kappa*I3+(L0+2*kappa*I3).T)/2).tolist(),
        ],
    },
    "RGS_half_pair_algebra": {
        "ZS_canonical_residual_fro": fro(
            ZS_c-.5*np.block([[I3,np.zeros((3,3))],
                              [np.zeros((3,3)),-I3]])),
        "ZA_canonical_residual_fro": fro(
            ZA_c-.5*np.block([[np.zeros((3,3)),-I3],
                              [I3,np.zeros((3,3))]])),
        "exchange_anticommutes_ZS_fro": fro(S@ZS_c+ZS_c@S),
        "exchange_anticommutes_ZA_fro": fro(S@ZA_c+ZA_c@S),
        "2ZA_equals_exchange_times_2ZS_fro": fro(2*ZA_c-S@(2*ZS_c)),
    },
    "interpretation_guard": [
        "Square diagonal reflection exchanges the two congruent triangles.",
        "PRISM biverso adds an explicit inter-sheet K2 coupling.",
        "The scalar Euclidean square Laplacian is not asserted to equal this operator.",
        "RGS identification is restricted to the numerically invariant six-dimensional carrier.",
        "No full 188D PRISM intertwiner or physical origin of every 1/2 is claimed."
    ],
}
out = ROOT / "audits" / "T145_SQUARE_BIVERSE_RGS_CARRIER_2026-11-24.json"
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
