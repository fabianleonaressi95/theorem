# Kathara spherical completion and non-degenerate Q6 H2 lift

**Status:** exact integer chain-map construction implemented; CI pending. This is a new, explicitly declared spherical completion of the Kathara planar graph, not the original ten-bounded-face disk complex.

## 1. Why the distinction matters

The canonical Kathara transcription has 12 vertices and 21 edges. Its planar rotation system has 11 face walks:
- ten bounded faces, which define the existing Kathara disk complex;
- one outer face, the 8-cycle
  \[
  (1,3,6,9,12,10,7,4).
  \]

The original convention fills only the ten bounded faces:
\[
(C_0,C_1,C_2)=(12,21,10),\quad \chi=1,\quad
(\beta_0,\beta_1,\beta_2)=(1,0,0).
\]
It is a disk. Every chain map from C60's sphere complex through this disk necessarily kills the C60 fundamental class in H2.

Now attach the outer 8-gon as an eleventh 2-cell, with the orientation induced by the planar rotation system. The oriented boundaries of all eleven faces cancel edge-by-edge. The completed complex has
\[
(C_0,C_1,C_2)=(12,21,11),\quad \chi=2,\quad
(\beta_0,\beta_1,\beta_2)=(1,0,1).
\]
It is a closed spherical cellulation. This is a mathematically natural compactification of the planar drawing, but it is a distinct source complex and must be named separately.

## 2. Explicit non-degenerate map to Q6

Use the existing explicit Kathara vertex chart:
\[
g(x,y)=16c(x)+y,\qquad c(-2)=0,\ c(0)=1,\ c(2)=2.
\]
Use the declared Q6 path-axis order
\[
(1,2,0,3,4,5).
\]
For each canonically oriented Kathara edge, map it to the corresponding shortest axis-ordered Q6 path. For each of the eleven oriented face boundaries, concatenate its edge-path words and fill the resulting closed word by exact adjacent axis swaps across Q6 square faces.

The resulting integer matrices have shapes
\[
R_0\in\mathbb Z^{64\times12},\quad
R_1\in\mathbb Z^{192\times21},\quad
R_2\in\mathbb Z^{240\times11}.
\]
The implementation checks exactly
\[
B_1^{Q6}R_1=R_0B_1^{K^+},\qquad
B_2^{Q6}R_2=R_1B_2^{K^+}.
\]
It certifies \(\operatorname{rank}R_2=11\) modulo 1,000,003, which implies full column rank over \(\mathbb Q\).

## 3. Image of the spherical fundamental class

Let \(\mathbf 1\in\mathbb Z^{11}\) denote the coherently oriented sum of the eleven Kathara faces. Since their boundaries cancel,
\[
B_2^{K^+}\mathbf 1=0.
\]
The image
\[
z=R_2\mathbf 1
\]
satisfies
\[
B_2^{Q6}z=0.
\]
The executed construction gives:
- \(z\neq0\);
- support on **30** Q6 square faces;
- \(\|z\|_1=30\).

The target is the Q6 **2-skeleton**, which has no 3-cells. Therefore its second homology is \(H_2=\ker B_2^{Q6}\), with no quotient by 3-boundaries. The nonzero cycle z represents a nonzero H2 class. Thus the spherical completion's fundamental class is not collapsed by this particular Kathara→Q6 chain map.

This does not make the map RGS-metric canonical. The axis-order convention is a declared combinatorial choice. Nor does it yet provide a C60→Kathara map.

## 4. Relation to the C60 bridge

The original ten-face disk and the eleven-face spherical completion must not be conflated:

| Source complex | H2 | Consequence for C60→source→Q6 |
|---|---:|---|
| Kathara disk (10 bounded faces) | 0 | C60 sphere class necessarily maps to zero |
| Kathara spherical completion (add outer 8-gon) | 1 | A nonzero H2 map is possible; the constructed map to Q6 preserves the completed source class |

The next unresolved task is a geometrically justified cellular map
\[
P:C_*(C60)\longrightarrow C_*(K^+)
\]
with typed integer matrices and exact boundary identities. Since both complexes have H2=Q, it is now topologically possible for P to have nonzero degree. But no such P has been constructed or selected by the C60/Q6 geometry yet.

After P exists, the composite R∘P can be tested for degree on H2. The Stone–Wales intertwining condition still requires a separately defined target action and a commuting square.

## 5. Reproduction and evidence

Run:
```bash
python scripts/audit_kathara_spherical_q6_lift.py --out kathara_spherical_q6_lift.json
pytest -q tests/test_kathara_spherical_q6_lift.py
```

| Claim | Status |
|---|---|
| Outer Kathara face is the stated 8-cycle | Exact from the declared planar rotation system |
| Eleven oriented face boundaries cancel | Exact integer check |
| Completed Kathara homology is (1,0,1) | Exact rational calculation |
| Gate D-style chain identities for K+→Q6 | Exact integer matrix checks in the new script |
| rank(R2)=11 | Certified modulo 1,000,003 |
| Fundamental class image is a nonzero Q6 H2 class | Exact cycle check plus absence of Q6 3-cells |
| RGS-metric canonicality | Open |
| C60→K+ map and its degree | Open |
| Stone–Wales/Q6 intertwiner | Open |

The new implementation is in scripts/audit_kathara_spherical_q6_lift.py and its focused test is tests/test_kathara_spherical_q6_lift.py.
