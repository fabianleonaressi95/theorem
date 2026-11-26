# Consolidated Q6–C60 equivariance audit

**Date:** 2026-11-26  
**Classification:** consolidation of existing numerical/geometric audits; no new numerical result is claimed.

## Executive result

The proposed identification of the 64 Q6 states with the direct sum of the 32 actual C60 face-tangent planes is **not equivariant under the tested common group**. The obstruction is an exact character mismatch in the finite-group representation data:

\[
\chi_{Q6}(g)=4,\qquad \chi_{C60,\,\oplus_f E_f}(g)=-2
\]

for each of the eight order-three elements in the tested \(A_4\subset T_h\). Therefore the representations are inequivalent and no invertible intertwiner exists for this pair.

This is a representation-theoretic obstruction, not a spectral comparison. The archived spectral comparison remains unauthorized.

## 1. State order and coordinate symmetry

The archived Q6 state array is in canonical binary lexicographic row order, from 000000 to 111111. The point-cloud signed-coordinate action has order 48, identified with the coordinate cubic group \(O_h\). Only 16 of these 48 transformations preserve Q6 adjacency. Consequently, this coordinate action is **not** a 48-element graph-automorphism action on Q6.

The subgroup used for the 188D tangent reconstruction is the 16-element common geometry/Q6 subgroup. Its group closure was checked with zero failures.

## 2. Keep the two fibre constructions distinct

### 2.1 Antipodal-direction proxy

The earlier 32-pair construction uses one representative direction from each antipodal pair in the reconstructed Q6 point cloud and assigns the perpendicular plane to that direction. Its total dimension is 64, but these directions are **not independently recovered C60 face normals**. The proxy fails the \(T_h\) character test and must not be presented as the actual C60 face bundle.

### 2.2 Actual C60 face-tangent bundle

The separate C60 construction recovers the 32 polygonal faces of the truncated icosahedron: 12 pentagons and 20 hexagons. Each face carries
\[
E_f=n_f^\perp\subset\mathbb R^3,
\qquad
\dim\bigoplus_f E_f=32\cdot2=64.
\]
This is the geometrically relevant face-bundle candidate. Its character on the tested \(A_4\) subgroup is:
- identity: 64;
- eight order-three elements: -2;
- three order-two elements: 0.

For Q6 the corresponding values are 64, 4, and 0. Since all eight order-three elements have the same respective characters, the mismatch is invariant under any abstract isomorphism of the two \(A_4\) subgroups. The representations are not equivalent.

The inversion coset has zero character in both constructions; that agreement does not remove the order-three obstruction.

## 3. The 188D tangent action

The 192 rows of Q_tangent are ordered as 64 vertex displacement triples \((x_i,y_i,z_i)\), not as 192 graph-edge labels. For a compatible signed-coordinate symmetry with spatial matrix \(T\) and vertex permutation \(p\), the ambient action \(S\) induces
\[
U(T,p)=Q_{\rm tangent}^{T}S(T,p)Q_{\rm tangent}.
\]

The archived reconstruction reports:
- \(Q_{\rm tangent}\in\mathbb R^{192\times188}\), orthonormality residual \(1.31\times10^{-14}\);
- 16 compatible group elements, zero closure failures;
- maximum projector-invariance residual \(1.34\times10^{-14}\);
- maximum intertwining residual \(1.95\times10^{-14}\);
- maximum induced orthogonality residual \(3.86\times10^{-14}\).

Operator covariance on this 16-element group is selective:
- R_geo_tangent: preserved by all 16 elements;
- K0, P_G, T_transport: preserved only by the identity (at tolerance \(10^{-10}\)).

Thus the 188D action is reconstructed, but it does not make the archived K0, P_G, or T_transport equivariant under the whole common subgroup.

## 4. Scientific decision

1. Retain the 64 = 32×2 dimension count as a dimensional compatibility only.
2. Reject the antipodal-direction proxy as an identification with actual C60 face fibres.
3. Record the actual C60 face-fibre representation mismatch as a negative equivariance result.
4. Do not compare T2u eigenvalues or other spectra as though an equivariant Q6–C60 operator map had been established.
5. Keep the 188D reconstruction as a separate finite-group numerical verification, with its operator-specific covariance results.

## 5. Reproduction

The consolidation script checks the archived outputs without rerunning or overwriting the source audits:

    python scripts/consolidate_q6_c60_equivariance_audits.py

Source audits:
- audits/Q6_Oh_face_fibre_equivariance.md
- docs/Q6_C60_TH_CHARACTER_COMPARISON.md
- audits/Q6_tangent_188D_reconstruction.json

## 6. Open mathematical work

A new candidate map must specify, independently of the desired spectrum:
- the exact map from Q6 labels to the 32 geometric C60 faces (or face-fibre basis);
- the group homomorphism and its action on both sides;
- the subgroup under which equivariance is claimed;
- the resulting character equality and an explicit intertwiner.

If the full \(T_h\) character obstruction is retained, no invertible intertwiner exists for the tested representations. A smaller subgroup may be studied only as a separately declared mathematical question, not as a repair hidden in the comparison.
