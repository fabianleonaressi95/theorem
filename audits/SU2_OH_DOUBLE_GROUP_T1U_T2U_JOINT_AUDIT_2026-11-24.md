# Joint SU(2)–cubic-symmetry audit: T1u/T2u and the 124D K0 ladder

**Date:** 24 November 2026  
**Classification:** audit protocol and representation-theoretic correction; no new numerical verdict claimed  
**Status:** inputs are in `main`; implementation and execution remain open

## 1. Why the existing triplets change the test

The repository already contains a separate 188D geometric representation analysis:

- `T_{1u}) isotypic rank 39 (13 copies of a 3D irrep).
- `T_{2u}) isotypic rank 30 (10 copies of a 3D irrep).
- `T_{2u}) first isolated triplet reconstruction is implemented by `scripts/reconstruct_rgs_t2u_triplet.py` and `models/tangent_triplet_anisotropy.py`.
- T113-E records its first triplet eigenvalue as `-0.06994933008401777`, with rank-three basis and a gap above 0.3 in that particular constrained Coulomb Hessian.

These are existing results and must be reused. They are not, however, automatically projectors in the coordinate basis of `K0.npy`, `Z_S.npy`, and `Z_A.npy`.

## 2. Essential representation-theoretic correction: use the cubic double group

The reported K0 ladder has spin
\[
j=\frac{123}{2}=61.5,
\]
which is half-integral. The ordinary point group (O_h) is not itself a subgroup of (SU(2)). Its proper rotational subgroup (Osubset SO(3)) lifts to the binary octahedral group (2Osubset SU(2)). Since a half-integral spin representation sends the central element (-1in SU(2)) to (-I), it is a representation of the double group, not an ordinary single-valued representation of (O_h).

Therefore the correct comparison is:

1. construct the actual 48-element (O_h) action on the 188D geometric tangent space;
2. separate inversion parity and lift the proper 24-element rotational subgroup to its binary octahedral double cover;
3. restrict the spin-(61/2) representation to that lifted finite subgroup;
4. decompose it with the binary-octahedral double-group character projectors;
5. compare those double-valued irreps with the single-valued (T_{1u}), (T_{2u}) sectors only where the representation/parity types actually match.

A numerical resemblance between 3D blocks is not an intertwiner. In particular, do not label (T_{1u}) or (T_{2u}) as spin-1 without this restriction and character calculation.

## 3. Coordinate-basis gate — do not silently identify the two 188D spaces

The (T_{1u}/T_{2u}) projectors are reconstructed from the geometric action on the tangent basis (Q_{tangent}) / (R_{geo,tangent}). The K0-family arrays are stored in the archived 188D coordinates. The repository's `docs/RGS_188D_OPERATOR_PROVENANCE.md` explicitly says that an independent basis-identification certificate is still missing.

Thus any assertion that (P_{T_{1u}}), (P_{T_{2u}}), or the 16-element adjacency-preserving subgroup commutes with K0, (P_G), (Z_S), or (Z_A) is **conditional on a verified common-basis map**. Small residuals in unaligned coordinates do not resolve this provenance gap.

Before computing cross-commutators, require an orthogonal basis map (C) and record:
- source and target basis definitions;
- shape, orthogonality residual (|C^TC-I|_F);
- reconstruction residual against the shared geometric vectors;
- SHA-256 of both source bases and of (C).

If no such certificate is available, report the geometric irrep analysis and K0 spectral analysis separately. Do not manufacture a basis match by optimizing the desired commutators.

## 4. Exact block audit once the basis certificate exists

Let (P_G) be the 64D kernel projector and (P_\perp=I-P_G) the 124D positive-spectrum sector. Let (P_{1u}), (P_{2u}) be the geometric isotypic projectors transported into the same certified coordinate basis.

First report, rather than assume, the dimensions of intersections:
\[
d_{r,G}=\dim(\operatorname{Ran}P_r\cap\operatorname{Ran}P_G),\qquad
d_{r,\perp}=\dim(\operatorname{Ran}P_r\cap\operatorname{Ran}P_\perp).
\]
Compute them by principal-angle/SVD tests on orthonormal bases; the product (P_rP_G) is not itself a projector unless the two projectors commute.

Then report all four blocks for each (P_r):
\[
P_G P_rP_G,\quad P_G P_rP_\perp,\quad
P_\perp P_rP_G,\quad P_\perp P_rP_\perp.
\]
This decides whether the cubic sectors split cleanly across the 64D kernel and 124D ladder or mix them.

For (B\in\{Z_S,Z_A,T_{transport}\}), report the same four kernel/complement blocks and their ranks, singular values, Frobenius norms, and normalized norms. Do not infer selection rules from a global commutator alone.

## 5. Ladder selection rules and anisotropic operators

In the ordered K0 eigenbasis, define (m_n=-61.5+n) and construct (J_z,J_+,J_-) using the standard spin-(61/2) coefficients. Freeze the eigenvector phase convention and retain gauge-invariant checks.

For each operator (B=Z_S,Z_A), calculate matrix elements
\[
B_{mn}=\langle j,m|B|j,n\rangle
\]
and tabulate their norm by displacement (Delta m=m-n), not just the largest observed entries. Explicitly test:
- support at (Delta m=0,\pm1,\pm2,\pm3,\ldots);
- leakage outside any proposed (Delta m=\pm3) band;
- Hermiticity/anti-Hermiticity as appropriate;
- stability under the frozen phase convention and gauge-invariant singular-value summaries.

A pure (Delta m=\pm3) pattern is a **selection-rule observation** in this basis. It becomes a weight-three tensor claim only after verifying the commutators
\[
[J_z,B_q]=qB_q,\qquad
[J_\pm,B_q]=\sqrt{(k\mp q)(k\pm q+1)}B_{q\pm1}
\]
for a complete tensor multiplet ({B_q}_{q=-k}^k), with the appropriate normalization. Two operators (Z_S,Z_A) alone cannot establish a rank-three irreducible tensor multiplet.

Next, resolve each (B) into cubic isotypic blocks. The relevant question is whether it intertwines equivalent double-group irreps or couples distinct multiplicity copies, not whether two 3x3 matrices happen to look alike.

## 6. Reuse existing T2u work; do not regenerate it

Run the existing reconstruction only as a source-data reproduction:
```bash
python scripts/reconstruct_rgs_t2u_triplet.py
pytest -q tests/test_reconstruct_rgs_t2u_triplet.py
```

Use the exported `reports/rgs_q6_t2u_first_triplet.npz` basis/projector as the existing first T2u spectral triplet. The ten-copy T2u isotypic sector has dimension 30; the first isolated triplet is one selected 3D subspace, not the whole isotypic component.

The list of ten T2u triplet eigenvalues quoted in earlier working notes must be tied to its exact operator, normalization, source file, and basis before being merged with T113-E's Coulomb-Hessian eigenvalue. Do not assume these are the same spectrum: T113-E explicitly concerns a particular constrained Coulomb Hessian.

No T1u reconstruction should be repeated unless the existing T1u projector/basis is absent; first locate and reuse the archived object.

## 7. Required null controls and verdicts

Controls:
1. random phase gauges of the same ordered ladder;
2. random orthogonal embeddings of the 124D ladder subspace;
3. random conjugates preserving the ladder spectrum;
4. random cubic-equivariant operators with the same block ranks;
5. comparison against the exact binary-octahedral character decomposition.

Keep independent verdicts:
- **REPRODUCED:** existing T1u/T2u geometric projectors and T2u first triplet.
- **PASS/FAIL:** certified common-basis map.
- **PASS/FAIL:** 124D spin ladder Lie brackets and Casimir.
- **PASS/FAIL:** restriction to binary-octahedral double group and character multiplicities.
- **PASS/FAIL:** (Z_S,Z_A) tensor/selection-rule structure and cubic intertwining.
- **OPEN:** geometric origin of K0 and physical interpretation of the anisotropic operators.

## 8. Executable audit implementation

The conditional numerical implementation is now available at `scripts/audit_su2_oh_t1u_t2u_joint.py`. It:

- reconstructs the ordinary (O_h) character projectors for (T_{1u}) and (T_{2u}) from the existing 64-site geometry and 188D tangent basis;
- checks the expected isotypic ranks 39 and 30;
- transports the projectors only through a supplied orthogonal basis map (C), with convention operator-coordinates (=C\) geometric-coordinates;
- computes principal-angle intersections with (operatorname{Ran}P_G) and its complement;
- reconstructs the canonical spin-(61/2) ladder from the positive spectrum of (K_0);
- reports the (Z_S,Z_A,T_{transport}) kernel/complement and cubic blocks, plus the complete (Delta m) norm profiles for (Z_S,Z_A).

Invocation (after the independent basis-map certificate has been placed in the repository):

```bash
python scripts/audit_su2_oh_t1u_t2u_joint.py --basis-map data/RGS_188D_TO_K0_BASIS_MAP.npy
```

The example filename is a required-input placeholder, not a claim that this map already exists. The script intentionally exits before cross-basis comparisons if the file is absent or non-orthogonal. It does not optimize a basis map against the desired commutators. The ordinary (O_h) audit is implemented; the binary-octahedral double-group character decomposition and null-model ensemble remain follow-up work.

No numerical verdict for the joint SU(2)-cubic test is claimed until the independent basis-map certificate is supplied and the script is executed.
