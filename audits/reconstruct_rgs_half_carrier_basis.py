#!/usr/bin/env python3
"""Deterministic reconstruction of the six-dimensional RGS half-scale carrier."""
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "npz"
OUT.mkdir(parents=True, exist_ok=True)
K, P, ZA, ZS = [np.load(ROOT / "artifacts" / n, allow_pickle=False)
                 for n in ("K0.npy", "P_G.npy", "Z_A.npy", "Z_S.npy")]
n = K.shape[0]
assert all(x.shape == (n, n) for x in (P, ZA, ZS))
assert n == 188

# Spectral projector onto the +1/2 eigenspace of ZS:
# Q = 4 ZS^2 is the rank-six carrier projector and P+ = (Q + 2 ZS)/2.
Q = 4 * ZS @ ZS
Pplus = 2 * ZS @ ZS + ZS

# Deterministic pivoted-by-coordinate Gram-Schmidt on projected standard basis.
V = []
for j in range(n):
    v = Pplus[:, j].copy()
    for q in V:
        v -= q * np.dot(q, v)
    nv = np.linalg.norm(v)
    if nv > 1e-9:
        V.append(v / nv)
    if len(V) == 3:
        break
if len(V) != 3:
    raise RuntimeError(f"Expected rank 3 for Pplus, got {len(V)}")
V = np.column_stack(V)

# ZA maps the +1/2 sector isometrically to the -1/2 sector.
W = 2 * ZA @ V
U = np.column_stack((V, W))
Kc = U.T @ K @ U
H = Kc[:3, :3]
off = Kc[:3, 3:]
leak = K @ U - U @ Kc
evals, R = np.linalg.eigh(H)

JA = (V + W) @ R / np.sqrt(2)
JB = (V - W) @ R / np.sqrt(2)
D = np.diag([1., 1., -1.])
# Historical BA-block convention: an explicit sign gauge on the upper triplet.
JB_gauge = -JB @ D
ZA_BA = JB_gauge.T @ ZA @ JA
ZS_BA = JB_gauge.T @ ZS @ JA
low = evals - 0.15
high = evals + 0.15
# Reorder by increasing K0 eigenvalue; eigh(H) already sorts evals.
basis = np.column_stack((JA, JB))
basis_eigenvalues = np.r_[low, high]

# The natural C3 action on each ordered triplet is the cyclic permutation.
R3 = np.array([[0., 0., 1.], [1., 0., 0.], [0., 1., 0.]])
rho_diag = np.block([[R3, np.zeros((3,3))], [np.zeros((3,3)), R3]])
rho_A_only = np.block([[R3, np.zeros((3,3))], [np.zeros((3,3)), np.eye(3)]])
ZA_c = U.T @ ZA @ U
ZS_c = U.T @ ZS @ U
K_eig = basis.T @ K @ basis
ZA_eig = basis.T @ ZA @ basis
ZS_eig = basis.T @ ZS @ basis
maxabs = lambda x: float(np.max(np.abs(x)))
norm = lambda x: float(np.linalg.norm(x))
report = {
    "carrier_rank": int(round(np.trace(Q))),
    "Pplus_rank": int(round(np.trace(Pplus))),
    "basis_orthogonality_max": maxabs(U.T @ U - np.eye(6)),
    "ZS_canonical_max": maxabs(U.T @ ZS @ U -
        np.diag([.5]*3 + [-.5]*3)),
    "ZA_canonical_max": maxabs(U.T @ ZA @ U -
        np.block([[np.zeros((3,3)), -.5*np.eye(3)],
                  [.5*np.eye(3), np.zeros((3,3))]])),
    "K_compression": Kc.tolist(),
    "K_block_H": H.tolist(),
    "K_offdiagonal_block": off.tolist(),
    "H_eigenvalues": evals.tolist(),
    "K_carrier_eigenvalues": basis_eigenvalues.tolist(),
    "K_carrier_leakage_fro": norm(leak),
    "K_carrier_image_fro": norm(K @ U),
    "K_carrier_relative_leakage": norm(leak) / norm(K @ U),
    "ZA_low_to_high_max": maxabs(ZA @ JA + .5 * JB),
    "ZA_high_to_low_max": maxabs(ZA @ JB - .5 * JA),
    "historical_gauge_D": D.tolist(),
    "ZA_BA_block_gauged": ZA_BA.tolist(),
    "ZS_BA_block_gauged": ZS_BA.tolist(),
    "ZA_BA_half_sign_residual": maxabs(ZA_BA - .5 * D),
    "ZS_BA_opposite_half_sign_residual": maxabs(ZS_BA + .5 * D),
    "K_eigenvector_residual_max": maxabs(K @ basis -
        basis * basis_eigenvalues[None, :]),
    "spectral_involution_low_branch": [1, 1, -1],
}
np.savez_compressed(OUT / "RGS_HALF_CARRIER_BASIS.npz",
                    U=U, V_plus=V, W_minus=W, H=H, H_eigenvectors=R,
                    J_A=JA, J_B=JB, J_B_historical_gauge=JB_gauge,
                    gauge_D=D, ZA_BA=ZA_BA, ZS_BA=ZS_BA,
                    basis=basis, basis_eigenvalues=basis_eigenvalues)
(OUT / "RGS_HALF_CARRIER_BASIS_AUDIT.json").write_text(
    json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
