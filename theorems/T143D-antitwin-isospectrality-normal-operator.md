# T143-D — Anti-Twin isospectrality from the covariantly constant normal operator

**Classification:** exact conditional operator theorem; the archived \(K_{\rm fibre}\) realization is numerically certified in T143-B.  
**Purpose:** explain the equality of the \(P=+1\) and \(P=-1\) spectra, rather than merely record it.

## 1. Geometric setup

Let \(G=(V,E)\) be a finite graph, \(p:V\to V\) a fixed-point-free involutive graph automorphism, and
\[
n:V\to S^2\subset\mathbb R^3,\qquad n_{p(g)}=-n_g.
\tag{1}
\]
On
\[
\mathcal H=\bigoplus_{g\in V}\mathbb C^2
\]
define the deck involution and the vertexwise normal operator by
\[
(P\psi)_g=\psi_{p(g)},\qquad
(\mathcal N\psi)_g=(n_g\cdot\sigma)\psi_g.
\tag{2}
\]
Then
\[
P^\dagger=P,\quad P^2=I,\qquad
\mathcal N^\dagger=\mathcal N,\quad \mathcal N^2=I.
\tag{3}
\]
The antipodal condition gives
\[
P\mathcal N P=-\mathcal N,
\qquad\text{equivalently}\qquad
P\mathcal N=-\mathcal N P.
\tag{4}
\]

## 2. Geometric transport lemma

For an oriented edge \(g\to h\), let \(U_{gh}\in SU(2)\) be the canonical lift of the shortest rotation carrying \(n_g\) to \(n_h\), with convention
\[
U_{gh}(x\cdot\sigma)U_{gh}^\dagger
=(R_{gh}x)\cdot\sigma.
\tag{5}
\]
Since \(R_{gh}n_g=n_h\),
\[
U_{gh}(n_g\cdot\sigma)U_{gh}^\dagger
=n_h\cdot\sigma.
\tag{6}
\]
Thus the normal operator is parallel with respect to this connection.

Equation (6) is a link-level statement. To infer commutation with a global operator, its assembly must respect this intertwining relation.

## 3. Operator compatibility hypothesis

Let \(K=K^\dagger\) be a block operator on \(\mathcal H\), with \(2\times2\) blocks \(K_{gh}\). Assume
\[
K_{gh}(n_h\cdot\sigma)
=(n_g\cdot\sigma)K_{gh}
\qquad(g,h\in V).
\tag{7}
\]
This includes the diagonal blocks \(g=h\). Equation (7) is equivalent to
\[
[K,\mathcal N]=0.
\tag{8}
\]
Separately assume Anti-Twin invariance
\[
[K,P]=0.
\tag{9}
\]

A sufficient construction rule for (7) is that every off-diagonal block is assembled from the connection transports in a way that intertwines the endpoint normal operators, and every diagonal block commutes with its local normal operator. The connection alone, without an operator assembly rule, does not imply (8).

## 4. Theorem: isospectrality of the two Anti-Twin sectors

Under (1)–(3), (8), and (9), the restrictions
\[
K_+=K|_{\mathcal H_+},\qquad
K_-=K|_{\mathcal H_-},
\qquad
\mathcal H_\pm=\ker(P\mp I)
\tag{10}
\]
are unitarily equivalent. In particular,
\[
\operatorname{Spec}(K_+)=\operatorname{Spec}(K_-)
\tag{11}
\]
including algebraic multiplicities.

**Proof.** By (9), both parity sectors are invariant under \(K\). By (4), \(\mathcal N\) maps \(\mathcal H_+\) into \(\mathcal H_-\) and vice versa. Since \(\mathcal N^2=I\), this map is a unitary bijection between the two sectors. By (8), it intertwines the restrictions:
\[
K_-\mathcal N|_{\mathcal H_+}
=\mathcal N|_{\mathcal H_+}K_+.
\]
Thus \(K_-\) and \(K_+\) are unitarily equivalent, proving (11). \(\square\)

The theorem is stronger than equality of characteristic polynomials: it gives an explicit unitary intertwiner, namely the restriction of \(\mathcal N\).

## 5. Application to Q6 / RGS Anti-Twin

For \(V=\mathbb F_2^6\) and \(p(g)=g\oplus7\), the space has 32 antipodal vertex pairs. The two parity sectors each have dimension 64 after including the two-component spin fibre.

For the original archive, T143-B tests:
\[
\|[K_{\rm fibre},P]\|_F,\qquad
\|[K_{\rm fibre},\mathcal N]\|_F,\qquad
\|\mathcal N^2-I\|_F,
\]
as well as the blockwise residuals in (7). The observed values are at floating-point roundoff:
\[
\frac{\|[K_{\rm fibre},\mathcal N]\|_F}
{\|K_{\rm fibre}\|_F}
=1.1914\times10^{-16},
\]
\[
\|\mathcal N^2-I\|_F=2.3626\times10^{-15},
\qquad
\|\mathcal NP+P\mathcal N\|_F=0.
\]
The two 64-dimensional parity blocks have matching sorted spectra to \(1.2435\times10^{-14}\), in agreement with the theorem's prediction.

## 6. Relation to the three-generator Clifford symmetry

T143-C gives three commuting-with-\(K_{\rm fibre}\) involutions \(G_1,G_2,G_3\) with
\[
P=iG_1G_2G_3.
\]
That algebra explains parity reduction and even multiplicity within each sector. T143-D supplies a different operator, \(\mathcal N\), which anticommutes with \(P\) and commutes with \(K_{\rm fibre}\); it explains equality of the spectra **between** the two sectors.

These are complementary symmetries. Neither should be inferred from the other without additional hypotheses.

## 7. Evidence boundary

The theorem is exact under its operator hypotheses. The original archive currently verifies those hypotheses numerically to machine precision. A source-level specification of the construction of \(K_{\rm fibre}\) remains necessary to promote the numerical commutator checks to exact provenance claims.

No conclusion is asserted for \(K_{\rm fibre,biverso}\), \(K_0\), or the tangent-space operators until their own deck actions and normal intertwiners are identified and tested.
