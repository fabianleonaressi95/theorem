#!/usr/bin/env python3
"""Test 2 of audits/K0_SU2_LADDER_GEOMETRIC_COMPATIBILITY_PROTOCOL_2026-11-24.md.

Builds the canonical su(2) ladder on the 124D complement of K0 with a frozen
phase convention, then measures commutators against Z_S, Z_A, T_transport
(including kernel/complement block decomposition) and compares against null
controls (random phase gauge, random unitary conjugation, random subspace).

Verdicts are reported per protocol section 5; no outcome is assumed.
"""
import hashlib
import json
import numpy as np

rng = np.random.default_rng(20261124)

def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

# ---------- load + certify inputs ----------
paths = {
    "K0": "artifacts/K0.npy", "Z_S": "artifacts/Z_S.npy",
    "Z_A": "artifacts/Z_A.npy", "P_G": "artifacts/P_G.npy",
}
npz = np.load("data/RGS_PSU_all_matrices.npz")
K0 = np.load(paths["K0"]); ZS = np.load(paths["Z_S"]); ZA = np.load(paths["Z_A"])
PG = np.load(paths["P_G"]); T = npz["T_transport"]; R = npz["R_geo_tangent"]
hashes = {k: sha256(v) for k, v in paths.items()}
hashes["npz"] = sha256("data/RGS_PSU_all_matrices.npz")

I188 = np.eye(188)
Pperp = I188 - PG

# ---------- spectral ladder ----------
w, V = np.linalg.eigh((K0 + K0.T) / 2)
# complement = eigenvectors with eigenvalue > 1e-8, ascending
idx = np.where(w > 1e-8)[0]
assert len(idx) == 124 and np.allclose(w[idx], (np.arange(124) + 5) / 10, atol=1e-8)
U = V[:, idx].copy()          # 188 x 124, columns ordered by rung n=0..123
# frozen phase convention: largest-|component| entry of each column -> positive real
for c in range(U.shape[1]):
    k = np.argmax(np.abs(U[:, c]))
    if U[k, c].real < 0 or (abs(U[k, c].imag) > 1e-12 and U[k, c].imag < 0):
        U[:, c] *= -1
# re-orthogonalize cheaply (sign flips preserve orthonormality)
assert np.allclose(U.conj().T @ U, np.eye(124), atol=1e-10)

n = 124; j = 61.5
m = -j + np.arange(n)          # -61.5 .. 61.5
# J_z, J_+, J_- in the ordered eigenbasis
Jz_b = np.diag(m).astype(complex)
Jp_b = np.zeros((n, n), complex)
for a in range(n - 1):
    mm = m[a]
    Jp_b[a + 1, a] = np.sqrt(j * (j + 1) - mm * (mm + 1))
Jm_b = Jp_b.conj().T
Jx_b = (Jp_b + Jm_b) / 2
Jy_b = (Jp_b - Jm_b) / (2j)

# lift to 188D by zero extension on kernel
Zero = np.zeros((188, 188), complex)
def lift(B):
    O = np.zeros((188, 188), complex)
    O[np.ix_(idx, idx)] = U.conj().T @ B @ U if B.shape == (124, 124) else B
    return O
# simpler: operators already in eigenbasis coords -> embed via U
Jz = U @ Jz_b @ U.conj().T
Jp = U @ Jp_b @ U.conj().T
Jm = U @ Jm_b @ U.conj().T
Jx = U @ Jx_b @ U.conj().T
Jy = U @ Jy_b @ U.conj().T

# ---------- su(2) self-check ----------
su2 = {
    "[Jz,Jp]-Jp": float(np.linalg.norm(Jz @ Jp - Jp @ Jz - Jp)),
    "[Jz,Jm]+Jm": float(np.linalg.norm(Jz @ Jm - Jm @ Jz + Jm)),
    "[Jp,Jm]-2Jz": float(np.linalg.norm(Jp @ Jm - Jm @ Jp - 2 * Jz)),
    "casimir-j(j+1)": float(np.linalg.norm(Jx @ Jx + Jy @ Jy + Jz @ Jz - j * (j + 1) * (U @ U.conj().T))),
}
# restrict Casimir check to complement projector
Cas = Jx @ Jx + Jy @ Jy + Jz @ Jz
su2["casimir-j(j+1)"] = float(np.linalg.norm(Cas - j * (j + 1) * (U @ U.conj().T)))

# ---------- commutator suite ----------
def blocks(B):
    return {
        "pp": Pperp @ B @ Pperp,
        "pg": PG @ B @ Pperp,
        "gp": Pperp @ B @ PG,
        "gg": PG @ B @ PG,
    }

def comm_norms(J, B):
    C = J @ B - B @ J
    out = {"full": float(np.linalg.norm(C))}
    bl = blocks(B)
    # commutator of J (zero on kernel) with each block of B
    out["[J,B_pp]"] = float(np.linalg.norm(J @ bl["pp"] - bl["pp"] @ J))
    out["[J,B_pg]"] = float(np.linalg.norm(J @ bl["pg"] - bl["pg"] @ J))
    out["[J,B_gp]"] = float(np.linalg.norm(J @ bl["gp"] - bl["gp"] @ J))
    out["[J,B_gg]"] = float(np.linalg.norm(J @ bl["gg"] - bl["gg"] @ J))
    denom = np.linalg.norm(J) * np.linalg.norm(B)
    out["normalized_full"] = out["full"] / denom if denom else None
    return out

Js = {"Jz": Jz, "Jp": Jp, "Jm": Jm, "Jx": Jx, "Jy": Jy}
Bs = {"Z_S": ZS, "Z_A": ZA, "T_transport": T, "R_geo_tangent": R}
results = {"su2_selfcheck": su2, "commutators": {}, "null_controls": {}}
for bn, B in Bs.items():
    results["commutators"][bn] = {jn: comm_norms(J, B) for jn, J in Js.items()}

# ---------- null controls ----------
# (a) random diagonal phase gauge on U
Uph = U * np.exp(1j * rng.uniform(0, 2 * np.pi, size=U.shape[1]))
Jz_p = Uph @ Jz_b @ Uph.conj().T
results["null_controls"]["phase_gauge_max_comm"] = max(
    comm_norms(Jz_p, ZS)["full"], comm_norms(Jz_p, ZA)["full"], comm_norms(Jz_p, T)["full"]
)
# (b) random unitary conjugation of whole ladder
Qr, _ = np.linalg.qr(rng.standard_normal((188, 188)) + 1j * rng.standard_normal((188, 188)))
# keep it unitary; conjugate Jz only (representative)
Jz_r = Qr @ Jz @ Qr.conj().T
results["null_controls"]["random_conj_max_comm"] = max(
    comm_norms(Jz_r, ZS)["full"], comm_norms(Jz_r, ZA)["full"], comm_norms(Jz_r, T)["full"]
)
# (c) random 124D subspace: project ladder onto random subspace is ill-defined;
# instead random Hermitian with same spectrum commutes trivially -> use random
# orthogonal mixing of eigenbasis within degenerate-free spectrum is impossible;
# use random unitary V124 and rebuild Jz_b spectrum -> same as (b) restricted.
V124, _ = np.linalg.qr(rng.standard_normal((124, 124)) + 1j * rng.standard_normal((124, 124)))
Jz_s = U @ (V124 @ Jz_b @ V124.conj().T) @ U.conj().T
results["null_controls"]["random_basis_max_comm"] = max(
    comm_norms(Jz_s, ZS)["full"], comm_norms(Jz_s, ZA)["full"], comm_norms(Jz_s, T)["full"]
)

# observed for comparison
results["observed_Jz_max_comm"] = max(
    results["commutators"][bn]["Jz"]["full"] for bn in Bs
)
results["observed_all_max_comm"] = max(
    results["commutators"][bn][jn]["full"] for bn in Bs for jn in Js
)

with open("audits/K0_SU2_LADDER_GEOMETRIC_COMPATIBILITY_2026-11-24.json", "w") as fh:
    json.dump({"hashes": hashes, "results": results}, fh, indent=2)
print(json.dumps(results, indent=2)[:6000])
print("wrote audits/K0_SU2_LADDER_GEOMETRIC_COMPATIBILITY_2026-11-24.json")
