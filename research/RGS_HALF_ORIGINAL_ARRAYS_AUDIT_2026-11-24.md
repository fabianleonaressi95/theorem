# Audit of the original RGS half-step arrays

**Date:** 2026-11-24  
**Source:** root-level binary arrays on `main`, uploaded in commit `22bcb3985856302c23ddd2b2dd4b8be4aa896eca`.  
**Scope:** numerical audit of the original `K0.npy`, `P_G.npy`, `Z_A.npy`, `Z_S.npy`; no reconstructed or synthetic substitutes.

## 1. Input integrity

All four arrays load as real `float64`, shape (188\times188). The upload commit lists the four files as newly added. The checks below are computed directly from their binary payloads.

## 2. (P_G) and (K_0)

- (P_G=P_G^T) to machine precision; (|P_G^2-P_G|_{\max}=5.56\times10^{-16}).
- (operatorname{tr}P_G=64), with spectrum (1^{(64)},0^{(124)}). Thus (P_G) is an orthogonal projector of rank 64, not rank 33.
- (K_0=K_0^T) in the stored array; its spectrum is nonnegative to numerical precision, with 64 eigenvalues at approximately (10^{-12}) and 124 positive eigenvalues. Extremes: (9.99\times10^{-13}) and (12.8).
- (operatorname{tr}K_0=824.600000000064).
- (K_0P_G\simeq0): maximum entry residual (4.80\times10^{-13}), Frobenius residual (8.00\times10^{-12}). Since (dim\ker K_0=\operatorname{rank}P_G=64), the numerical evidence identifies
  [
  \operatorname{ran}P_G=\ker K_0.
  ]
  This is stronger than mere commutation: the projector selects the nullspace of (K_0).

## 3. The two original operators

The stored (Z_A) is skew-symmetric:
[
Z_A^T=-Z_A,qquad \|Z_A\|_F=\sqrt{3/2}.
]
Its symmetric part vanishes at the stored precision. Its singular spectrum has six values (1/2) and 182 zero values.

The stored (Z_S) is symmetric:
[
Z_S^T=Z_S,qquad \|Z_S\|_F=\sqrt{3/2}.
]
Its spectrum is
[
(+1/2)^{(3)},\quad (-1/2)^{(3)},\quad 0^{(182)}.
]
Thus the coefficient (1/2) is an actual spectral value with multiplicity three in each sign sector, not merely a coefficient inferred from an earlier note.

## 4. Exact-looking algebraic relations (numerical residuals)

Direct matrix products give:
[
Z_A^2+Z_S^2\simeq0,
\qquad
Z_AZ_S+Z_SZ_A\simeq0,
\qquad
Z_S^3-\tfrac14 Z_S\simeq0,
\qquad
Z_A^3+\tfrac14 Z_A\simeq0.
]
The maximum-entry residuals are respectively:
- (\|Z_A^2+Z_S^2\|_{\max}=2.43\times10^{-17});
- (\|Z_AZ_S+Z_SZ_A\|_{\max}=1.74\times10^{-17});
- (\|Z_S^3-\tfrac14Z_S\|_{\max}=9.54\times10^{-18});
- (\|Z_A^3+\tfrac14Z_A\|_{\max}=6.94\times10^{-18}).

Consequently (Q:=4Z_S^2=-4Z_A^2) is, to numerical precision, a rank-six orthogonal projector. On its six-dimensional range, (2Z_S) is a symmetric involution with (+1) and (-1) eigenspaces of dimension three each; (2Z_A) is a skew complex structure and anticommutes with (2Z_S). This gives a concrete six-dimensional algebraic structure with a (3+3) splitting.

## 5. Position relative to (P_G) and (K_0)

[
P_GZ_A\simeq Z_AP_G\simeq0,\qquad
P_GZ_S\simeq Z_SP_G\simeq0.
]
The Frobenius norms of (P_GZ_A) and (P_GZ_S) are both about (6.3\times10^{-16}). Therefore the active six-dimensional space of (Z_A,Z_S) lies in the orthogonal complement of (operatorname{ran}P_G=\ker K_0), i.e. in the positive spectral sector of (K_0).

Important qualification: (Z_A) and (Z_S) do **not** commute with (K_0) (maximum-entry commutator residuals approximately (9.85\times10^{-3}) and (1.16\times10^{-2})). They are not established as conserved symmetries of (K_0).

## 6. What this says about the earlier (1/2) bridge

The previous shorthand (Z_A^{BA}=\tfrac12\operatorname{diag}(1,1,-1)), (Z_S^{BA}=-Z_A^{BA}) must not be imposed on these 188-dimensional arrays. In the original data, (Z_A) is skew and (Z_S) is symmetric; they are not negatives of one another.

What is now established numerically is more structured:
- a rank-six carrier space;
- a canonical (3+3) eigenspace splitting from (Z_S);
- a skew operator (Z_A) exchanging those two sectors because it anticommutes with (Z_S);
- exact-looking half-scale relations (Z_S^2=-Z_A^2=Q/4).

This is a finite-dimensional Clifford-type pair on the six-dimensional carrier space. It is a candidate algebraic realization of the “half” bridge, not yet an identified intertwiner with the spherical (z=\pm1/2) rings or the earlier (J_A\leftrightarrow J_B) basis. That identification still requires recovering/constructing the explicit orthonormal basis and verifying the change-of-basis map. The old three-dimensional diagonal formula and the present six-dimensional pair are not to be conflated.

## 7. Status

**Numerically verified from original arrays:** projector ranks/spectra, (K_0P_G\simeq0), symmetry types, spectra of (Z_A,Z_S), anticommutation, quadratic/cubic relations, and support orthogonality to (P_G).

**Still open:** explicit basis vectors for the rank-six carrier space; the (3+3) basis identification with the prior (J_A,J_B) triplets; any intertwiner to the spherical construction; a physical interpretation or a claim that these operators commute with (K_0).

Reproducible local audit: `audits/audit_rgs_half_original_arrays.py`.
