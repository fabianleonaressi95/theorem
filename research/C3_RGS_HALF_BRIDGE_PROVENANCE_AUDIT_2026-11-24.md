# C3–RGS one-half bridge: provenance audit (2026-11-24)

## Executive result

**Status: NUMERICAL BRIDGE OPEN; provenance partially recovered.**

The geometric half in the new spherical model is exact:
\[
z=\pm\tfrac12,\qquad \rho=\sqrt{1-z^2}=\tfrac{\sqrt3}{2}.
\]
The earlier RGS notes report a separate three-dimensional block with coefficient pattern
\[
Z_A^{BA}=\tfrac12\operatorname{diag}(1,1,-1),\qquad
Z_S^{BA}=-Z_A^{BA}.
\]
These are not yet identified as the same operator or representation. The value (1/2) alone does not provide an intertwiner.

## What was recovered

A repository search in `fabianleonaressi95/rgs-qlg-quaternion-bridge` found:

- `reports/imported/formule_extracted.txt`, which reproduces an inventory of the 188D checkpoint bundle.
- The inventory explicitly lists `Z_A.npy`, `Z_S.npy`, `Zmat.npy`, `K0.npy`, `P_G.npy`, `J_A.npy), and `J_B.npy` as 188×188 or associated 188D objects. In particular, `Z_A.npy` and `Z_S.npy` are listed as 188×188 float64 arrays; the inventory is not the array payload.
- The extracted notebook context calls `audit_188d(Zmat, "Zmat")` and assigns its outputs to `Z_S, Z_A`. This establishes that the stored (Z_S,Z_A) names are associated with the symmetric/antisymmetric audit of (Zmat), not by itself the provenance of the particular 3×3 (BA) block quoted above.
- The archived inventory reports the array location as `/kaggle/working/188D_CHECKPOINT/AUTO_DUMP/`; those Kaggle-local files are not present as downloadable matrix payloads in the Git repository.

A separate first-principles reconstruction record in the project archive reports:
- original (J_A,J_B) provenance: `NOT_RECOVERABLE`;
- a proposed (J_A,J_B) reconstruction used a QR-orthogonalized soft (T_{2u}) triplet with a (0.01\) noise perturbation;
- the original (O_h) projector and RNG seed were not recovered;
- the proposed (J_A,J_B) therefore remain `HYPOTHESIS_ONLY`, not verified original couplings;
- (K^{-1}) was reconstructed separately by a documented spectral pseudoinverse, while the derived (M_A,M_B,\Delta M) remained `HYPOTHESIS_ONLY`.

This matters: the reconstructed (J_A,J_B) cannot be used as a canonical basis map for proving the C3–RGS bridge. Doing so would build the desired correspondence into an unverified proxy.

## What is not yet verified

The current repository evidence does **not** provide the binary contents of the original 188×188 arrays, the ordered three-dimensional basis defining the quoted (BA) block, or a source-level derivation of that block. Consequently, we cannot yet calculate:

1. the actual block restriction (Z_A^{BA}) from the archived matrix;
2. its basis-invariant spectrum and the embedding of its three-dimensional support;
3. the overlap of that support with (P_G), the tangent/Möbius subspace, or a (C_3\times C_3) character sector;
4. an explicit intertwiner (U) to the spherical (z=\pm1/2) coordinate action or to an invariant eigenspace of \(\overline L_6\).

The prior RGS value (Delta K_0=0.3) and (Delta N=3) remain reported historical values, not independently recomputed in this audit.

## Correct mathematical comparison

There are three distinct appearances of one-half:

1. **Spherical geometry:** (z=\pm1/2) is the axial coordinate of two latitude triangles on (S^2), with radius (\sqrt3/2).
2. **Planar Vesica geometry:** (x=1/2) is the midpoint coordinate for unit-separated circle centres.
3. **RGS block datum:** (1/2\,\mathrm{diag}(1,1,-1)) is a reported coefficient matrix in a three-dimensional block.

Only the first two are established directly by the current geometric constructions. The third still needs raw-matrix and basis provenance. Also, the spherical triangle side is (3/2), whereas the planar unit-circle chord is (\sqrt3); these lengths must not be conflated.

The target is not simply equality of coefficients. It is a basis-aware relation, for example
\[
U Z_A^{BA} U^{-1}=A_{\mathrm{target}},
\]
where both the source subspace and target operator are independently defined and (U) is explicitly constructed. If the intended comparison is with a (C_3\times C_3) sector of \(\overline L_6\), dimensions and representation characters must match before attempting the intertwiner.

## Next required input / test

Recover the original checkpoint payloads (at minimum `Zmat.npy`, `Z_A.npy`, `Z_S.npy`, `P_G.npy`, `K0.npy`, and the basis/projector data defining the (BA) block) from the original Kaggle checkpoint or an archived NPZ. Then:

1. hash and shape-audit every payload;
2. reconstruct (Z_S=(Zmat+Zmat^T)/2) and (Z_A=(Zmat-Zmat^T)/2), if that is indeed the original audit convention, and compare to stored arrays;
3. identify the (BA) block indices/basis from source provenance, not by fitting;
4. test the block's invariant subspace, rank, singular values, and action under the relevant RGS projectors;
5. only then compute character-sector overlaps and solve for an intertwiner to the new C3 operator.

**No numerical intertwiner is claimed in this commit.** The correct result is a documented provenance gap, not an invented matrix match.

## Classification

| Object / claim | Status |
|---|---|
| Spherical latitude (z=\pm1/2), radius (\sqrt3/2) | **PROVED BY COORDINATES** |
| Planar Vesica midpoint (x=1/2) | **PROVED BY GEOMETRIC CONSTRUCTION** |
| Historical 188D array inventory | **RECOVERED AS MANIFEST ONLY** |
| Binary contents of original (Z_A,Z_S,Zmat,P_G,K0) | **NOT RECOVERED IN REPOSITORY** |
| Original (J_A,J_B) provenance | **NOT_RECOVERABLE** (per archived reconstruction record) |
| Reported (Z_A^{BA}=\frac12\operatorname{diag}(1,1,-1)) | **HISTORICAL CLAIM; RAW BLOCK NOT REAUDITED** |
| C3–RGS invariant-subspace identification | **OPEN** |
| Explicit intertwiner (U) | **NOT COMPUTED / OPEN** |


## 2026-11-24 correction: original arrays recovered

The previous “not recovered” conclusion is superseded. The four binary arrays were uploaded to the repository root on 2026-11-24 in commit `22bcb3985856302c23ddd2b2dd4b8be4aa896eca`. Their numerical contents have now been read and audited directly. See [RGS_HALF_ORIGINAL_ARRAYS_AUDIT_2026-11-24.md](RGS_HALF_ORIGINAL_ARRAYS_AUDIT_2026-11-24.md) and reproducible script [audit_rgs_half_original_arrays.py](../audits/audit_rgs_half_original_arrays.py).

The original arrays establish a rank-six carrier with a symmetric/antisymmetric half-scale pair: (Z_S) has eigenvalues (+1/2) and (-1/2), each of multiplicity three; (Z_A) is skew-symmetric; (Z_A^2+Z_S^2\simeq0) and (Z_AZ_S+Z_SZ_A\simeq0). Both operators annihilate (operatorname{ran}P_G) and act in its orthogonal complement. This corrects the earlier “manifest only” and “payload not recovered” statements.

The historical (3\times3) (BA) block/basis provenance is still not established by these four files alone. Accordingly, the six-dimensional half-scale algebra is **NUMERICALLY VERIFIED**, while the explicit identification with the previously quoted (J_A\leftrightarrow J_B) basis and the intertwiner to the spherical construction remain **OPEN**.
