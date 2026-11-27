#!/usr/bin/env python3
"""Audit the K0 spectral ladder and the Z_S coupling scale (188D RGS arrays).

Verifies, on the stored float64 arrays at repository root:
  1. spec(K0) = {0^(64)} cup {(k+5)/10 : k = 0..123}  (ladder 0.5..12.8, step 0.1)
  2. Z_S has eigenvalues {-1/2 (x3), 0 (x182), +1/2 (x3)} and Z_S^2 = (1/4) P_W
     on its 6-dimensional range.
  3. f(0) = 1/2 coincides with min positive eigenvalue of K0 and with |spec(Z_S)|.

This documents a spectral coincidence; it does NOT derive f from K0 or Z_S.
"""
import json
import numpy as np

K0 = np.load("artifacts/K0.npy")
ZS = np.load("artifacts/Z_S.npy")
ZA = np.load("artifacts/Z_A.npy")

report = {}

# --- K0 spectrum ---
assert K0.shape == (188, 188) and np.allclose(K0, K0.T)
w = np.linalg.eigvalsh(K0)
nz = w[w > 1e-8]
expected = (np.arange(124) + 5) / 10.0
report["k0_shape"] = list(K0.shape)
report["k0_symmetric"] = bool(np.allclose(K0, K0.T))
report["kernel_dim"] = int(np.sum(w <= 1e-8))
report["positive_eigenvalue_count"] = int(len(nz))
report["ladder_min"] = float(nz.min())
report["ladder_max"] = float(nz.max())
report["ladder_step_max_dev"] = float(np.max(np.abs(np.diff(nz) - 0.1)))
report["ladder_matches_(k+5)/10"] = bool(
    len(nz) == 124 and np.allclose(nz, expected, atol=1e-8)
)

# --- Z_S spectrum and Z_S^2 ---
assert ZS.shape == (188, 188)
ws = np.linalg.eigvalsh((ZS + ZS.T) / 2)
u, c = np.unique(np.round(ws, 8), return_counts=True)
report["zs_eigenvalues"] = {str(k): int(v) for k, v in zip(u, c)}
QS = (ZS @ ZS + (ZS @ ZS).T) / 2
wq = np.linalg.eigvalsh(QS)
uq, cq = np.unique(np.round(wq, 8), return_counts=True)
report["zs_squared_eigenvalues"] = {str(k): int(v) for k, v in zip(uq, cq)}
report["zs_squared_is_quarter_projector"] = bool(
    np.allclose(wq, np.where(wq > 1e-8, 0.25, 0.0), atol=1e-8)
    and int(np.sum(wq > 1e-8)) == 6
)
report["za_antisymmetric"] = bool(np.allclose(ZA, -ZA.T))
report["za_zs_anticommute_on_W_fro"] = float(
    np.linalg.norm(ZA @ ZS + ZS @ ZA)
)

# --- coincidence statement ---
report["f_at_0"] = 0.5
report["f0_equals_k0_min_positive"] = bool(abs(nz.min() - 0.5) < 1e-8)
report["f0_equals_abs_zs_eigenvalue"] = bool(
    np.any(np.isclose(np.abs(ws), 0.5))
)
report["classification"] = (
    "spectral coincidence on stored arrays; not a derivation of f from K0/Z_S"
)

out = "audits/K0_SPECTRAL_LADDER_AND_ZS_SCALE.json"
with open(out, "w") as fh:
    json.dump(report, fh, indent=2)
print(json.dumps(report, indent=2))
print("wrote", out)
