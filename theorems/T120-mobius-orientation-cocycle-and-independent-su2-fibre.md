# T120 — Möbius orientation cocycle and independent SU(2) fibre

**Classification:** exact finite \(\mathbb Z_2\) transition-system result for the six-face complex of T117.

The six face-adjacency dual graph is the cycle \(0\to1\to2\to5\to4\to3\to0\). For adjacent faces sharing an edge, let \(s_i,s_j\in\{\pm1\}\) be the induced edge directions relative to the canonical increasing-vertex orientation. Define \(t_{ij}=-s_is_j\). In cycle order, the six transition signs are
\[
(+1,+1,+1,+1,+1,-1),\qquad \prod_{\rm cycle}t_{ij}=-1.
\]
Under local frame changes \(h_i\in\mathbb Z_2\), \(t'_{ij}=h_jt_{ij}h_i^{-1}\). Every \(h_i\) occurs twice in the cycle product, so the holonomy \(-1\) is invariant.

The source realizes three representations of this transition group:
\[
\rho_{\rm scalar}(-1)=1,\quad
\rho_{\rm sign}(-1)=-1,\quad
\rho_{\rm regular}(-1)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Each obeys the \(\mathbb Z_2\) representation law; the regular representation swaps its two channels around the cycle and swaps them back after a second application.

The base orientation transitions \(t_{ij}\) and the edge variables \(U_{uv}\in SU(2)\) of T118 are different data with different transformation laws. Although \(\mathbb Z_2\to SU(2)\), \(-1\mapsto-I_2\), is a group homomorphism, choosing it to identify the orientation cocycle with the internal gauge field would be an additional bundle prescription, not a consequence of the present construction.

The source also represents a negative sign by \(R=\mathrm{diag}(-1,1,\ldots,1)\in O(d)\), verifying \(R^TR=I\), \(\det R=-1\), and \(R^2=I\). This is only an orthogonal frame transition. A Pin lift requires a Clifford convention, lifts of all transitions and compatible overlap cocycles. The source explicitly reports `pin_lift_defined=False`.

**Source:** `src/mobius_representations.py`. **Tests:** `tests/test_mobius_representations.py`. Tests cover the six transitions, cycle product, representation laws, local-frame covariance and O(d) reflection identities.

**Boundary:** no Pin structure, spin structure, torsion tensor or coupling to the fundamental \(2I\) representation is established. Non-orientability alone implies none of these.