# Vesica–Minkowski: reflection-equivariant moment compression of all 64 hexagrams

**Date:** 24 November 2026  
**Status:** exact finite-dimensional construction; floating-point audit supplied.

## 1. Eight samples and reflection

On the lower arc use theta_k = -pi/3 + 2k*pi/21; on the upper arc use phi_k = 2pi/3 + 2k*pi/21, for k=0,...,7. The ambient reflection (t,x,y) -> (t,x,-y) induces k -> 7-k on both sample lists. Let P8 denote this permutation. Its eigenspaces have dimensions 4 and 4.

Set s_k = 2k-7 = (-7,-5,-3,-1,1,3,5,7), proportional to the centered angular coordinate. Reflection sends s to -s.

## 2. The moment map C: R^8 -> R^3

Use the first three polynomial moments compatible with parity: constant (even), centered quadratic (even), and linear (odd). After Gram–Schmidt and Euclidean normalization, the rows are

C = [
  (1,1,1,1,1,1,1,1)/sqrt(8);
  (7,1,-3,-5,-5,-3,1,7)/sqrt(462);
  (-7,-5,-3,-1,1,3,5,7)/sqrt(168)
].

They are orthonormal, so CC^T=I3 and rank(C)=3. In the target basis (constant-even, quadratic-even, linear-odd),

**C P8 = D C,   D = diag(1,1,-1).**

This is an exact intertwining identity. The output coordinates are moments of all eight samples, not three selected physical points.

The prescription is canonical relative to the ordered polynomial basis 1,s,s^2, the uniform eight-point measure, parity, removal of the constant part of s^2, and normalization. Reflection symmetry alone does not uniquely select this triple; other even/even/odd triples exist. No universal uniqueness claim is made.

## 3. All 64 hexagrams and the paired map

Fix the computational convention H_ij=(L_i,U_j), i,j=0,...,7, with binary labels 000,...,111, lower trigram first. The correspondence between these bits and traditional bottom-to-top line order must be fixed before assigning historical hexagram names or numbers.

The paired compression is

**C tensor C : R^8 tensor R^8 -> R^3 tensor R^3 = R^9.**

For each of the 64 basis states its nine-component feature vector is (C e_i) tensor (C e_j). The complete 64-row lookup, with both three-bit labels and all nine coordinates, is stored in results/json/vesica_hexagram_moment_compression_2026-11-24.json.

All 64 labelled basis states have pairwise distinct nine-component feature vectors at tolerance 1e-14. However, the linear map on arbitrary fields has rank 9 and kernel dimension 55. Thus the 64 labels remain distinguishable as this finite list of feature vectors, but a general scalar field on 64 hexagrams cannot be reconstructed from nine moments.

## 4. Reflection equivariance on both sheets

For each factor independently:
(C tensor C)(P8 tensor I8) = (D tensor I3)(C tensor C),
(C tensor C)(I8 tensor P8) = (I3 tensor D)(C tensor C).

Their product, the single ambient Minkowski reflection acting diagonally on the two cone sheets, gives:
(C tensor C)(P8 tensor P8) = (D tensor D)(C tensor C).

The compression is therefore equivariant for the abstract Z2 x Z2 action on the two factors. Only the diagonal generator is identified with the one ambient spacetime reflection. The independent factor flips are algebraic symmetries of the product label space, not two separate Lorentz transformations of the same spacetime.

The nine-dimensional target decomposes under D tensor D into a five-dimensional even sector and a four-dimensional odd sector.

## 5. Relation to the three-channel RGS carrier

The single-trigram target has the same reflection parity signature (2,1) as the previously recovered RGS carrier D=diag(1,1,-1). This supplies a specified equivariant 8-to-3 map, rather than arbitrarily identifying three of the eight samples with the marked channels (-,0,+).

It does not yet prove that the moment basis is the unique or physically preferred RGS basis; that C tensor C intertwines K0, ZA, ZS on the full 188D space; that the nine-dimensional paired sector reduces canonically to one three-dimensional carrier; that the moments reproduce the Q6 graph Laplacian; or that the model has Lorentzian dynamics or a continuum limit.

The next test must derive a nine-to-three reduction from an independently specified operator (for example a symmetry projector or coupling operator) and compare it with the stored RGS arrays. It must not be imposed by hand.

## 6. Reproducibility and classification

Run from the repository root:

python audits/audit_vesica_hexagram_moment_compression.py

The standard-library audit checks row orthonormality, CP8=DC, tensor-map orthonormality, equivariance under each factor reflection, all 64 labels, and pairwise distinctness of their feature vectors.

**Classification:** exact finite-dimensional algebraic construction; numerical verification of its floating-point implementation; canonical relative to the declared polynomial-moment prescription; full RGS dynamical compatibility remains open.
