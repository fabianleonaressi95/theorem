# T057 — Exact square-similarity map and Kathara center-overlay relation

**Status:** exact Euclidean geometry theorem, conditional on the stated Kathara diagram constraints.  
**Scope:** the planar \(45^\circ\) clockwise rotation with scale \(\sqrt2\), the \(2:1\) central-column proportion, and the two reported center-overlay conditions. It does not assert a physical interpretation of the source diagram.

## 1. Geometric hypotheses and coordinates

Let \(A\) be the AzurA point and let \(w>0\) be the distance between centers 6 and 7. Choose coordinates with \(A=(0,0)\), the 6–7 line horizontal, and the 1–12 central column vertical. The midpoint condition gives
\[
p_6=(-w/2,0),\qquad p_7=(w/2,0).
\]
The stated \(2:1\) proportion, with \(A\) the midpoint of the 1–12 column, gives
\[
p_1=(0,-w),\qquad p_{12}=(0,w).
\]

A clockwise \(45^\circ\) rotation followed by a scale factor \(\sqrt2\) is represented by
\[
T=\sqrt2R_{-\pi/4}
=\begin{pmatrix}1&1\\-1&1\end{pmatrix}.
\]
The source overlay statements are encoded as
\[
Tp_9=p_{12},\qquad T^2p_6=p_{12}.
\]

## 2. Theorem

Under these hypotheses:
\[
T^TT=2I,\qquad \det T=2,\qquad
T^2=\begin{pmatrix}0&2\\-2&0\end{pmatrix}
=2R_{-\pi/2}.
\]
The overlay conditions uniquely determine
\[
\boxed{p_9=Tp_6=(-w/2,w/2).}
\]
Consequently
\[
\|p_6\|=w/2,\qquad
\|p_9\|=w/\sqrt2,\qquad
\|p_{12}\|=w,
\]
and the two successive center radii increase by exactly \(\sqrt2\).

The induced integer-lattice map satisfies
\[
T(\mathbb Z^2)=\{(u,v)\in\mathbb Z^2:u\equiv v\pmod2\},
\]
an index-two sublattice, and \(T^2(\mathbb Z^2)=2\mathbb Z^2\), of index four.

## 3. Proof

The rotation matrix is
\[
R_{-\pi/4}=\frac1{\sqrt2}
\begin{pmatrix}1&1\\-1&1\end{pmatrix},
\]
so multiplying by \(\sqrt2\) gives the displayed integer matrix \(T\). Direct multiplication yields \(T^TT=2I\), \(\det T=2\), and the displayed formula for \(T^2\).

From the two overlay equations,
\[
Tp_9=T^2p_6.
\]
Since \(T\) is invertible, \(p_9=Tp_6=(-w/2,w/2)\). Substitution gives \(Tp_9=(0,w)=p_{12}\) and \(T^2p_6=(0,w)=p_{12}\). The radius statements follow by taking Euclidean norms.

Finally, for integers \(x,y\),
\[
T(x,y)=(x+y,-x+y).
\]
The two coordinates have equal parity. Conversely, if \(u\equiv v\pmod2\), then \(x=(u-v)/2\) and \(y=(u+v)/2\) are integers and map to \((u,v)\). This proves the image-lattice identity; the index equals \(|\det T|=2\). Applying the map twice gives \(T^2\mathbb Z^2=2\mathbb Z^2\). \(\square\)

## 4. Non-conclusions

The theorem determines the similarity and the constrained positions of centers 1, 6, 7, 9 and 12. It does not determine the exact positions and all line incidences of the remaining centers 2, 3, 4, 5, 8, 10 and 11. Those require the complete source-controlled center/line diagram and a declared incidence convention.

The \(2\times2\) matrix \(T\) has characteristic polynomial
\[
\lambda^2-2\lambda+2.
\]
It is not the \(3\times3\) trigram transfer matrix with polynomial \(\lambda^3-\lambda^2-1\). A further, explicitly defined action on oriented cells and a proved map from those cells to the trigram channels are required before any supergolden derivation can be claimed.

The source-based reconstruction and its exact numerical audit are maintained in the companion repository:
https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/KATHARA_KRYSTAL_SPIRAL_SQUARE_GEOMETRY.md.
