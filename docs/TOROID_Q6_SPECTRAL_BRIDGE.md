# Toroid–Q6 spectral bridge: metric discretization and D4 audit

**Status:** implementation and tests added; execution not yet performed. No numerical spectrum or intertwiner is claimed.

## 1. Discrete torus

Use an 8-by-8 periodic quadrilateral grid, with 64 vertices, 128 oriented edges and 64 faces. The first three binary coordinates encode the meridian index and the last three encode the azimuthal index. The cellulation is a torus, with exact incidence closure

\[
B_1B_2=0,\qquad
\beta_0=1,\quad\beta_1=2,\quad\beta_2=1.
\]

The parametrization is

\[
X(\theta,\varphi)=
((R+r\cos\theta)\cos\varphi,
 (R+r\cos\theta)\sin\varphi,
 r\sin\theta).
\]

The exact area of a parameter cell is integrated from
\(dA=r(R+r\cos\theta)d\theta d\varphi\). Edge lengths are exact Euclidean chord lengths for the corresponding coordinate edges.

## 2. Geometric masses

For each edge of length \(L_e\), assemble the one-dimensional P1 vertex mass

\[
M_e^{(0)}=\frac{L_e}{6}
\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]

For the constant edge 1-form coefficient and constant integrated face flux conventions, use

\[
(W_1)_{ee}=L_e^{-1},\qquad (W_2)_{FF}=A_F^{-1}.
\]

The vertex stiffness and generalized scalar Laplacian are

\[
K_0=B_1W_1B_1^T,\qquad K_0u=\lambda W_0u.
\]

All weights come from the torus metric, not from fitted Q6 values.

## 3. Q6 comparison

The Q6 comparator is the ordinary six-cube graph Laplacian on the same 64 binary labels. It has 192 edges and degree six. The torus graph has 128 edges. Thus the two objects share a vertex set but **not** an edge set or a cellular chain complex.

No chain map, cochain intertwiner, or equality of raw spectra is assumed.

## 4. D4 test

Use the D4 generators already recorded in the Q6 audit, and construct the vertex permutation representation. For each raw operator \(L\), compute

\[
\varepsilon_{D_4}(L)=
\max_{g\in D_4}\|P_g^TLP_g-L\|_F.
\]

This measures whether the actual geometric operator commutes with the specified Boolean D4 action. It must be reported rather than assumed.

The irreducible isotypic projectors are formed from the D4 characters. Their dimensions and idempotence residuals are audited.

## 5. Reynolds comparison is separate

For diagnostic purposes only, define

\[
\overline L=\frac18\sum_{g\in D_4}P_g^TLP_g,
\qquad
\overline W_0=\frac18\sum_{g\in D_4}P_g^TW_0P_g.
\]

These operators are D4-invariant by construction and remain positive when the original mass is positive. Their spectra are **not** the raw geometric torus spectrum and must never be presented as such.

## 6. What this audit can establish

- exact closure of the toroidal cell complex;
- exact Betti numbers of its periodic 8-by-8 cellulation;
- metric-derived mass matrices and generalized scalar spectrum;
- raw D4 commutator residuals for torus and Q6 graph operators;
- D4 representation-sector dimensions on the common 64-vertex label space;
- separately labeled Reynolds-averaged comparison spectra.

## 7. What remains open

A genuine torus–Q6 spectral theorem requires more than matching 64 vertex labels. It requires a cellular map or a chain-level correspondence compatible with incidence, a geometrically justified transfer operator, and an intertwining identity. None is asserted here. The next step is to determine whether a nontrivial chain map exists for a specified Q6 subcomplex, or whether the incidence ranks obstruct it.
