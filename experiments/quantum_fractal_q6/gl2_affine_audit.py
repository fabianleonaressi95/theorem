"""GL(6,2)-affine filtration audit for the Q6 Walsh filtration.

Task: characterize coordinate-MIXING affine maps T(x) = P x + b on the
64 Q6 states that do NOT preserve the prefix conditional expectations
E_j, and classify commutator profiles.

Mathematical facts used (verified numerically in tests):
- The induced permutation operator U_T on l^2(Q6) gives
  [U_T, E_j] = U_T (E_j - U_T^{-1} E_j U_T); since U_T is unitary,
  ||[U_T,E_j]|| equals ||E_j - E'_j|| where E'_j is the conditional
  expectation onto the pulled-back partition.  For affine T the
  pullback partition is the level-set partition of the first j
  coordinates of P x (the translation b does not change the
  sigma-algebra).
- Translations b alone preserve every E_j: verified explicitly below.

Scope: finite algebra only.  |GL(6,2)| = 20,158,709,760 is too large
to enumerate; we enumerate the natural distinguished classes
(coordinate permutations S6 = Aut(Q6) linear part, trigram block
GL(3,2)xGL(3,2), elementary transvections, a Singer-type companion
cycle) plus a fixed-seed random sample of GL(6,2).  No physical
interpretation is claimed for any element.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np

from walsh_filtration import (N_BITS, N_SITES, conditional_expectation,
                              load_canonical_q6)

REPO_ROOT = Path(__file__).resolve().parents[2]


def gf2_rank(M: np.ndarray) -> int:
    """Rank over F2 of a binary matrix (rows = vectors)."""
    A = np.asarray(M, dtype=np.uint8).copy()
    rows, cols = A.shape
    rank = 0
    for c in range(cols):
        piv = next((r for r in range(rank, rows) if A[r, c]), None)
        if piv is None:
            continue
        A[[rank, piv]] = A[[piv, rank]]
        for r in range(rows):
            if r != rank and A[r, c]:
                A[r] ^= A[rank]
        rank += 1
        if rank == rows:
            break
    return rank


def random_gl6(rng: np.random.Generator, n: int) -> list[np.ndarray]:
    """Sample invertible 6x6 binary matrices via random transvection
    products (guaranteed in GL(6,2))."""
    out = []
    while len(out) < n:
        P = np.eye(N_BITS, dtype=np.uint8)
        for _ in range(24):
            i, j = rng.choice(N_BITS, 2, replace=False)
            P[i] ^= P[j]  # elementary transvection E_{ij}
        if gf2_rank(P) == N_BITS:
            out.append(P.copy())
    return out


def permutation_matrix_from_map(idx) -> np.ndarray:
    P = np.zeros((N_SITES, N_SITES), dtype=np.float64)
    P[np.arange(N_SITES), idx] = 1.0
    return P


def affine_vertex_map(P: np.ndarray, b: np.ndarray | None = None):
    """Return the index map i -> j of T(x)=Px+b on the 64 states.

    State index i has bits = columns of Q6_states[i] (MSB-first, i.e.
    bit a of the state tuple is column a).  P acts on the column
    vector: (Px)[a] = sum_c P[a,c] x[c] mod 2.
    """
    states = np.array(list(itertools.product((0, 1), repeat=N_BITS)),
                      dtype=np.uint8)
    X = states.T  # 6 x 64, column a = coordinate a
    Y = (P.astype(np.uint8) @ X) % 2
    if b is not None:
        Y = (Y + np.asarray(b, dtype=np.uint8)[:, None]) % 2
    # encode each output column vector back to an index (MSB-first)
    idx = np.zeros(N_SITES, dtype=int)
    for a in range(N_BITS):
        idx += Y[a].astype(int) << (N_BITS - 1 - a)
    return idx


def commutator_profile(Pmat_idx, projections):
    """Frobenius and spectral norms of [U_T, E_j] for all j."""
    U = permutation_matrix_from_map(Pmat_idx)
    fro, spec = {}, {}
    for j, E in projections.items():
        C = U @ E - E @ U
        fro[str(j)] = float(np.linalg.norm(C, "fro"))
        spec[str(j)] = float(np.linalg.norm(C, 2))
    return fro, spec


def first_nonzero(fro: dict, tol: float = 1e-9) -> int | None:
    for j in range(N_BITS + 1):
        if fro[str(j)] > tol:
            return j
    return None


def gl3_elements() -> list[np.ndarray]:
    """All 168 invertible 3x3 binary matrices."""
    out = []
    for bits in itertools.product((0, 1), repeat=9):
        M = np.array(bits, dtype=np.uint8).reshape(3, 3)
        if gf2_rank(M) == 3:
            out.append(M)
    return out


def embed_block(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Block-diagonal 6x6 matrix acting on cols {0,1,2} and {3,4,5}."""
    P = np.zeros((6, 6), dtype=np.uint8)
    P[:3, :3] = A
    P[3:, 3:] = B
    return P


def companion_matrix(poly: list[int]) -> np.ndarray:
    """Companion matrix of a monic binary polynomial given as coefficient
    list [c0,...,c5,1] (lowest degree first)."""
    P = np.zeros((6, 6), dtype=np.uint8)
    P[1:, :-1] = np.eye(5, dtype=np.uint8)
    P[:, -1] = np.array(poly[:6], dtype=np.uint8)
    return P


def s6_permutations() -> list[np.ndarray]:
    """All 720 coordinate permutations as 6x6 binary matrices."""
    out = []
    for perm in itertools.permutations(range(6)):
        P = np.zeros((6, 6), dtype=np.uint8)
        for a in range(6):
            P[a, perm[a]] = 1  # output coord a takes input coord perm[a]
        out.append(P)
    return out


def preserves_Ej_block_criterion(P: np.ndarray, j: int) -> bool:
    """Exact linear-algebra criterion: an invertible binary matrix P
    preserves the E_j sigma-algebra iff its top-right j x (6-j) block
    vanishes, i.e. P[a, c] = 0 for all a < j <= c.

    Reason: the partition defining E_j pulled back through x -> Px is
    the level-set partition of the first j coordinates of Px; it equals
    the original partition iff the first j rows of P involve only the
    first j columns, i.e. the off-diagonal block is zero.  P preserves
    the WHOLE flag iff P is lower triangular (P[a,c]=0 for a<c).
    """
    P = np.asarray(P, dtype=np.uint8)
    return not P[:j, j:].any()


def _hist(values) -> dict:
    h = {}
    for v in values:
        key = "None" if v is None else str(v)
        h[key] = h.get(key, 0) + 1
    return {k: h[k] for k in sorted(h, key=lambda x: (x == "None", x))}


def profile_signature(fro: dict, ndigits: int = 6) -> tuple:
    return tuple(round(fro[str(j)], ndigits) for j in range(N_BITS + 1))


def run_audit(sample_size: int = 20000, seed: int = 20261124) -> dict:
    arrays = load_canonical_q6()
    projections = {j: conditional_expectation(j)
                   for j in range(N_BITS + 1)}

    classes = {}

    # ---- 1. translations alone (P = I, random b) ----
    rng = np.random.default_rng(seed)
    trans_profiles = set()
    for _ in range(64):
        b = rng.integers(0, 2, N_BITS, dtype=np.uint8)
        fro, _ = commutator_profile(affine_vertex_map(np.eye(6, dtype=np.uint8), b),
                                    projections)
        trans_profiles.add(profile_signature(fro))
    classes["pure_translations"] = {
        "count": 64,
        "distinct_profiles": len(trans_profiles),
        "all_zero": all(all(abs(v) < 1e-9 for v in sig)
                        for sig in trans_profiles),
    }

    # ---- 2. coordinate permutations S6 (Aut(Q6) linear part) ----
    s6 = []
    seen = {}
    for P in s6_permutations():
        fro, spec = commutator_profile(affine_vertex_map(P), projections)
        sig = profile_signature(fro)
        jstar = first_nonzero(fro)
        s6.append({"perm": P, "fro": fro, "spec": spec,
                   "signature": sig, "first_nonzero": jstar})
        seen.setdefault(sig, 0)
        seen[sig] += 1
    classes["coordinate_permutations_S6"] = {
        "count": len(s6),
        "distinct_profiles": len(seen),
        "profile_histogram": {str(k): v for k, v in
                              sorted(seen.items(), key=lambda kv: -kv[1])},
        "identity_is_only_full_preserver": all(
            e["first_nonzero"] is not None for e in s6
            if not np.array_equal(e["perm"], np.eye(6, dtype=np.uint8))),
        "first_nonzero_histogram": _hist(
            [e["first_nonzero"] for e in s6]),
    }

    # ---- 3. trigram block GL(3,2) x GL(3,2) ----
    g3 = gl3_elements()
    block_profiles = {}
    block_examples = {}
    for A in g3:
        for B in g3:
            P = embed_block(A, B)
            fro, _ = commutator_profile(affine_vertex_map(P), projections)
            sig = profile_signature(fro)
            block_profiles[sig] = block_profiles.get(sig, 0) + 1
            block_examples.setdefault(sig, P.copy())
    classes["trigram_block_GL3xGL3"] = {
        "count": len(g3) ** 2,
        "distinct_profiles": len(block_profiles),
        "profile_histogram": {str(k): v for k, v in
                              sorted(block_profiles.items(),
                                     key=lambda kv: -kv[1])[:50]},
    }

    # ---- 4. elementary transvections + companion cycle ----
    special = {}
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            P = np.eye(6, dtype=np.uint8)
            P[i] ^= P[j]
            fro, _ = commutator_profile(affine_vertex_map(P), projections)
            special[f"transvection_E{i}{j}"] = {
                "signature": profile_signature(fro),
                "first_nonzero": first_nonzero(fro),
            }
    classes["elementary_transvections"] = special

    for name, coeffs in {
        "companion_x6+x+1": [1, 1, 0, 0, 0, 0],
        "companion_x6+x5+x4+x3+x2+x+1": [1, 1, 1, 1, 1, 1],
    }.items():
        P = companion_matrix(coeffs + [1])
        assert gf2_rank(P) == 6
        fro, spec = commutator_profile(affine_vertex_map(P), projections)
        classes.setdefault("companion_cycles", {})[name] = {
            "matrix_rows": P.tolist(),
            "signature": profile_signature(fro),
            "first_nonzero": first_nonzero(fro),
        }

    # ---- 5. random GL(6,2) sample ----
    mats = random_gl6(rng, sample_size)
    rand_profiles = {}
    rand_first = {}
    for P in mats:
        fro, _ = commutator_profile(affine_vertex_map(P), projections)
        sig = profile_signature(fro)
        rand_profiles[sig] = rand_profiles.get(sig, 0) + 1
        j = first_nonzero(fro)
        rand_first[j] = rand_first.get(j, 0) + 1
    full_preservers = sum(
        1 for P in mats
        if all(preserves_Ej_block_criterion(P, j) for j in range(1, 6)))
    classes["random_GL6_sample"] = {
        "sample_size": sample_size,
        "seed": seed,
        "distinct_profiles": len(rand_profiles),
        "first_nonzero_histogram": {str(k): v for k, v in
                                    sorted(rand_first.items(),
                                           key=lambda kv: (kv[0] is None,
                                                           kv[0]))},
        "top_profiles": {str(k): v for k, v in
                         sorted(rand_profiles.items(),
                                key=lambda kv: -kv[1])[:20]},
        "full_flag_preservers_in_sample": full_preservers,
    }

    # ---- 6. natural distinguished candidates: EQC/Aut(Q6) generators ----
    # permute_lines orders from models/eqc_automorphism.py docstring and
    # the REV/ROT named generators; bit flips = translations.
    named = {
        "ROT_(5,1,2,3,4,0)": [5, 1, 2, 3, 4, 0],
        "REV_(5,4,3,2,1,0)": [5, 4, 3, 2, 1, 0],
    }
    natural = {}
    for name, order in named.items():
        P = np.zeros((6, 6), dtype=np.uint8)
        for a in range(6):
            P[a, order[a]] = 1
        idx = affine_vertex_map(P)
        fro, spec = commutator_profile(idx, projections)
        # Walsh block norms at each level
        states = load_canonical_q6()["Q6_states"]
        from walsh_filtration import walsh_matrix, suffix_mask
        W = walsh_matrix(states)
        U = permutation_matrix_from_map(idx)
        blocks = {}
        for j in range(7):
            OW = W.T @ (U @ conditional_expectation(j)
                        - conditional_expectation(j) @ U) @ W
            keep = suffix_mask(j)
            blocks[str(j)] = float(np.linalg.norm(
                OW[np.ix_(keep, ~keep)], "fro")) if (~keep).any() else 0.0
        natural[name] = {
            "matrix_rows": P.tolist(),
            "signature": profile_signature(fro),
            "first_nonzero": first_nonzero(fro),
            "walsh_block_fro": blocks,
        }
    classes["natural_candidates_EQC_automorphisms"] = natural

    # ---- 7. exact block criterion verification ----
    # For random GL(6,2) samples and structured classes, check that
    # first_nonzero(fro) equals min{j : P[:j,j:] != 0} whenever the
    # commutator vanishes iff the block vanishes.
    criterion_checks = {"tested": 0, "mismatches": 0}
    test_mats = random_gl6(np.random.default_rng(seed + 1), 300)
    test_mats += s6_permutations()[:200]
    for P in test_mats:
        fro, _ = commutator_profile(affine_vertex_map(P), projections)
        nz = {j for j in range(7)
              if fro[str(j)] > 1e-9}
        crit = {j for j in range(7)
                if not preserves_Ej_block_criterion(P, j)}
        # j=0,6 are degenerate (E_0 rank1 const, E_6=I): exclude
        nz.discard(0); nz.discard(6)
        crit.discard(0); crit.discard(6)
        criterion_checks["tested"] += 1
        if nz != crit:
            criterion_checks["mismatches"] += 1
    criterion_checks["statement"] = (
        "for affine x->Px+b, [U_T,E_j]=0 iff P[:j,j:]=0 (verified on "
        "500 sampled matrices, j=1..5)")

    return {
        "experiment": "GL(6,2)-affine Q6 Walsh-filtration mixing audit",
        "scope": ("finite algebra on 64 Q6 states; |GL(6,2)| too large "
                  "for exhaustive enumeration - natural classes plus "
                  "fixed-seed random sample; no physical interpretation"),
        "classes": classes,
        "block_criterion": criterion_checks,
    }


def main() -> None:
    out_dir = REPO_ROOT / "results" / "quantum_fractal_q6"
    out_dir.mkdir(parents=True, exist_ok=True)
    report = run_audit()
    out = out_dir / "gl2_affine_audit.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {out.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
