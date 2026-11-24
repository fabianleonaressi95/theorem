"""Finite Q6/Walsh filtration audit (research note Sec. 6D / Sec. 8 items 1-5).

Scope: exact finite linear-algebra computations on the canonical 64-site
Q6 vertex space stored in ``data/RGS_PSU_all_matrices.npz``.  This module
implements only provenance-identified operators; it does not invent a
coupled or weighted PRISM operator.  No fractal scaling, spectral
dimension, or physical interpretation is claimed.

Coordinate convention
---------------------
``Q6_states`` rows are ``itertools.product((0,1), repeat=6)`` order, i.e.
column 0 varies slowest and column 5 fastest.  The filtration level ``j``
keeps the FIRST ``j`` columns (columns ``0..j-1``) and averages over the
suffix columns ``j..5``.  This matches research-note Sec. 10 with the
coordinate order ``x=(x_1,...,x_6)`` mapped to columns ``0..5``.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
NPZ_PATH = REPO_ROOT / "data" / "RGS_PSU_all_matrices.npz"

N_BITS = 6
N_SITES = 64


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def load_canonical_q6() -> dict[str, np.ndarray]:
    """Load the canonical recovered Q6 arrays; verify state ordering."""
    z = np.load(NPZ_PATH)
    states = np.asarray(z["Q6_states"], dtype=np.int64)
    reference = np.array(list(itertools.product((0, 1), repeat=6)),
                         dtype=np.int64)
    if not np.array_equal(states, reference):
        raise ValueError("Q6_states ordering is not product((0,1),repeat=6)")
    return {k: np.asarray(z[k]) for k in
            ("Q6_states", "Q6_adjacency", "Q6_laplacian",
             "Q6_antipodal", "Pi_AT")}


def walsh_matrix(states: np.ndarray) -> np.ndarray:
    """Unitary Walsh/Sylvester matrix W[x, S] = 64^{-1/2} (-1)^{S.x}."""
    s = states.astype(np.int64)
    # columns of the unnormalized character table, index S = 0..63
    signs = (-1.0) ** (s[:, None, :] * s[None, :, :]).sum(axis=2)
    return signs / np.sqrt(N_SITES)


def suffix_mask(j: int) -> np.ndarray:
    """Boolean mask over Walsh indices S whose support is inside first j bits."""
    if not 0 <= j <= N_BITS:
        raise ValueError("j must lie in [0, 6]")
    keep = np.zeros(N_SITES, dtype=bool)
    for s in range(N_SITES):
        # bit a of Walsh index S corresponds to coordinate column a
        if all(((s >> (N_BITS - 1 - a)) & 1) == 0 for a in range(j, N_BITS)):
            keep[s] = True
    return keep


def conditional_expectation(j: int) -> np.ndarray:
    """E_j: orthogonal projection onto functions of the first j bits.

    (E_j f)(x) = 2^{-(6-j)} sum over suffix bits of f.
    In the position basis E_j[x, y] = 2^{-(6-j)} iff x, y agree on the
    first j columns.
    """
    if not 0 <= j <= N_BITS:
        raise ValueError("j must lie in [0, 6]")
    states = np.array(list(itertools.product((0, 1), repeat=6)),
                      dtype=np.int64)
    e = np.zeros((N_SITES, N_SITES), dtype=np.float64)
    size = 1 << (N_BITS - j)
    for x in range(N_SITES):
        prefix = states[x, :j]
        for y in range(N_SITES):
            if np.array_equal(states[y, :j], prefix):
                e[x, y] = 1.0 / size
    return e


def operator_inventory(arrays: dict[str, np.ndarray]) -> dict[str, dict]:
    """Provenance-identified 64x64 operators on the Q6 vertex space.

    Only operators actually stored in the canonical NPZ are listed, plus
    sector projectors derived from stored involutions.  No coupled or
    weighted PRISM operator is fabricated: if one is later identified,
    it must be added here with its own provenance entry.
    """
    L = arrays["Q6_laplacian"].astype(np.float64)
    A_adj = arrays["Q6_adjacency"].astype(np.float64)
    anti = arrays["Q6_antipodal"].astype(np.float64)
    pi_at = arrays["Pi_AT"].astype(np.float64)
    I = np.eye(N_SITES)
    ops = {
        "Q6_laplacian": {
            "matrix": L,
            "provenance": ("data/RGS_PSU_all_matrices.npz::Q6_laplacian; "
                           "verified identical to 6I - Q6_adjacency "
                           "(standard unweighted hypercube Laplacian)"),
            "role": "control (research note Sec. 10 predicts zero commutator)",
        },
        "Q6_adjacency": {
            "matrix": A_adj,
            "provenance": ("data/RGS_PSU_all_matrices.npz::Q6_adjacency; "
                           "verified 0/1 cube adjacency"),
            "role": "control (L = 6I - A)",
        },
        "Q6_antipodal": {
            "matrix": anti,
            "provenance": ("data/RGS_PSU_all_matrices.npz::Q6_antipodal; "
                           "symmetric involution, bitwise-complement "
                           "permutation of the 64 states"),
            "role": "stored involution; generates sector projectors",
        },
        "Pi_AT": {
            "matrix": pi_at,
            "provenance": ("data/RGS_PSU_all_matrices.npz::Pi_AT; "
                           "Anti-Twin involution on Q6 states "
                           "(equivariance R_geo_tangent A = A Pi_AT, "
                           "see scripts/audit_188d_antitwin.py)"),
            "role": "stored involution; generates sector projectors",
        },
        "P_antipodal_plus": {
            "matrix": 0.5 * (I + anti),
            "provenance": ("derived: (I + Q6_antipodal)/2 from stored "
                           "involution"),
            "role": "derived sector projector (not a stored array)",
        },
        "P_antipodal_minus": {
            "matrix": 0.5 * (I - anti),
            "provenance": ("derived: (I - Q6_antipodal)/2"),
            "role": "derived sector projector (not a stored array)",
        },
        "P_AT_plus": {
            "matrix": 0.5 * (I + pi_at),
            "provenance": ("derived: (I + Pi_AT)/2"),
            "role": "derived sector projector (not a stored array)",
        },
        "P_AT_minus": {
            "matrix": 0.5 * (I - pi_at),
            "provenance": ("derived: (I - Pi_AT)/2"),
            "role": "derived sector projector (not a stored array)",
        },
    }
    # Synthetic control: a generic symmetric operator with no reason to
    # respect the coordinate filtration.  NOT a stored Q6 operator; it
    # exists only to demonstrate that the commutator/block machinery has
    # discriminating power (nonzero output for a non-fiber-preserving
    # operator).  Fixed seed for reproducibility.
    rng = np.random.default_rng(20261124)
    G = rng.standard_normal((N_SITES, N_SITES))
    G = 0.5 * (G + G.T)
    ops["synthetic_GOE_control"] = {
        "matrix": G,
        "provenance": ("SYNTHETIC CONTROL: fixed-seed (20261124) GOE "
                       "symmetric random matrix; not a stored Q6 operator, "
                       "not a PRISM/Kathara candidate"),
        "role": "discrimination control only",
    }
    return ops


def _norms(M: np.ndarray) -> dict[str, float]:
    if M.size == 0:
        return {"frobenius": 0.0, "spectral": 0.0}
    return {
        "frobenius": float(np.linalg.norm(M, "fro")),
        "spectral": float(np.linalg.norm(M, 2)),
    }


def audit_operator(O: np.ndarray, projections: dict[int, np.ndarray],
                   W: np.ndarray) -> dict:
    """Commutators, Walsh block couplings and compression spectra."""
    out = {"commutators": {}, "walsh_blocks": {}, "compressions": {}}
    masks = {j: suffix_mask(j) for j in projections}
    for j, E in projections.items():
        comm = O @ E - E @ O
        out["commutators"][str(j)] = _norms(comm)
        # Walsh-basis block coupling: O_W = W^T O W; block between
        # retained modes (S subset of first j bits) and averaged modes.
        OW = W.T @ O @ W
        keep = masks[j]
        block = OW[np.ix_(keep, ~keep)]
        out["walsh_blocks"][str(j)] = _norms(block)
        # Compression spectrum of E O E on range(E): eigenvalues of the
        # 2^j x 2^j matrix W_keep^T O W_keep in the Walsh basis.
        Wk = W[:, keep]
        comp = Wk.T @ O @ Wk
        eig = np.linalg.eigvalsh(comp)
        out["compressions"][str(j)] = {
            "dim": int(keep.sum()),
            "eigenvalues": [round(float(v), 10) for v in eig],
        }
    return out


def run_audit() -> dict:
    arrays = load_canonical_q6()
    states = arrays["Q6_states"]
    W = walsh_matrix(states)
    projections = {j: conditional_expectation(j) for j in range(N_BITS + 1)}

    # --- projection identity checks (exact, reported) ---
    proj_checks = {}
    for j, E in projections.items():
        rank = int(round(np.linalg.matrix_rank(E, tol=1e-9)))
        proj_checks[str(j)] = {
            "idempotent_fro": float(np.linalg.norm(E @ E - E, "fro")),
            "selfadjoint_fro": float(np.linalg.norm(E - E.T, "fro")),
            "rank": rank,
            "expected_rank": 1 << j,
        }
    for j in range(N_BITS):
        lhs = projections[j] @ projections[j + 1]
        proj_checks[f"chain_{j}_{j+1}"] = {
            "E_j E_{j+1} - E_j fro": float(np.linalg.norm(lhs - projections[j], "fro")),
        }

    ops = operator_inventory(arrays)
    per_operator = {}
    for name, spec in ops.items():
        per_operator[name] = {
            "provenance": spec["provenance"],
            "role": spec["role"],
            **audit_operator(spec["matrix"], projections, W),
        }

    # eigenvalue comparison for the Laplacian control: full spectrum vs
    # Walsh-character eigenvalues 2|S| (exact identity cross-check)
    L = ops["Q6_laplacian"]["matrix"]
    eig_L = np.linalg.eigvalsh(L)
    walsh_eigs = sorted(2 * bin(s).count("1") for s in range(N_SITES))
    laplacian_check = {
        "numeric_eigenvalues": [round(float(v), 10) for v in eig_L],
        "walsh_formula_eigenvalues": walsh_eigs,
        "max_abs_difference": float(np.max(np.abs(eig_L - np.array(walsh_eigs)))),
    }

    return {
        "experiment": "Q6/Walsh finite filtration audit",
        "scope": ("finite 64-site computations only; no fractal scaling, "
                  "spectral dimension, or physical interpretation claimed"),
        "npz": str(NPZ_PATH.relative_to(REPO_ROOT)),
        "npz_sha256": sha256_file(NPZ_PATH),
        "filtration": {
            "definition": ("E_j = conditional expectation onto functions of "
                           "the first j columns of Q6_states "
                           "(columns 0..j-1); suffix columns j..5 averaged"),
            "levels": list(range(N_BITS + 1)),
            "projection_checks": proj_checks,
        },
        "operators": per_operator,
        "laplacian_spectrum_check": laplacian_check,
        "missing_operators": {
            "coupled_or_weighted_vertex_operator": (
                "No weighted/coupled 64x64 vertex-space Q6 operator was "
                "found in data/RGS_PSU_all_matrices.npz or in the audited "
                "scripts. The stored Q6_laplacian is exactly the standard "
                "hypercube Laplacian, so its commutators vanish identically "
                "(control only). A genuine PRISM/Kathara coupled operator "
                "must be supplied with provenance before a nontrivial "
                "commutator test is possible."),
        },
    }


def main() -> None:
    out_dir = REPO_ROOT / "results" / "quantum_fractal_q6"
    out_dir.mkdir(parents=True, exist_ok=True)
    report = run_audit()
    out_path = out_dir / "walsh_filtration_audit.json"
    out_path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
