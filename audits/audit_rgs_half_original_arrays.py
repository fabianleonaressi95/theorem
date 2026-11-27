#!/usr/bin/env python3
"""Numerical audit of original K0, P_G, Z_A, Z_S arrays (188x188)."""
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
names = ("K0.npy", "P_G.npy", "Z_A.npy", "Z_S.npy")
A = {n: np.load(ROOT / "artifacts" / n, allow_pickle=False) for n in names}
for n, x in A.items():
    if x.shape != (188, 188) or x.dtype != np.float64:
        raise ValueError(f"{n}: expected float64 (188,188), got {x.dtype} {x.shape}")
K, P, ZA, ZS = (A[n] for n in names)
maxabs = lambda x: float(np.max(np.abs(x)))
norm = lambda x: float(np.linalg.norm(x, "fro"))
eigK = np.linalg.eigvalsh(K)
eigP = np.linalg.eigvalsh(P)
eigS = np.linalg.eigvalsh(ZS)
singA = np.linalg.svd(ZA, compute_uv=False)
Q = 4 * ZS @ ZS
out = {
    "shapes": {n: list(x.shape) for n, x in A.items()},
    "K0": {"trace": float(np.trace(K)), "symmetry_max": maxabs(K-K.T),
           "eig_min": float(eigK[0]), "eig_max": float(eigK[-1]),
           "nullity_1e-8": int(np.sum(np.abs(eigK) < 1e-8))},
    "P_G": {"trace": float(np.trace(P)), "symmetry_max": maxabs(P-P.T),
            "idempotence_max": maxabs(P@P-P),
            "eig_0_1_counts": [int(np.sum(np.abs(eigP)<1e-8)),
                               int(np.sum(np.abs(eigP-1)<1e-8))]},
    "K0_PG": {"max": maxabs(K@P), "fro": norm(K@P)},
    "Z_A": {"skew_max": maxabs(ZA+ZA.T), "fro": norm(ZA),
            "singular_values_half_count": int(np.sum(np.abs(singA-.5)<1e-8))},
    "Z_S": {"symmetry_max": maxabs(ZS-ZS.T), "fro": norm(ZS),
            "eig_min": float(eigS[0]), "eig_max": float(eigS[-1]),
            "eig_minus_half_count": int(np.sum(np.abs(eigS+.5)<1e-8)),
            "eig_plus_half_count": int(np.sum(np.abs(eigS-.5)<1e-8))},
    "relations": {
        "ZA2_plus_ZS2_max": maxabs(ZA@ZA+ZS@ZS),
        "anticommutator_max": maxabs(ZA@ZS+ZS@ZA),
        "ZS_cubic_max": maxabs(ZS@ZS@ZS-.25*ZS),
        "ZA_cubic_max": maxabs(ZA@ZA@ZA+.25*ZA),
        "Q_idempotence_max": maxabs(Q@Q-Q),
        "PG_ZA_fro": norm(P@ZA), "PG_ZS_fro": norm(P@ZS),
        "K_ZA_commutator_max": maxabs(K@ZA-ZA@K),
        "K_ZS_commutator_max": maxabs(K@ZS-ZS@K),
    },
}
print(json.dumps(out, indent=2, sort_keys=True))
