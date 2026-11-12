# T104 — Q6 cycle–cocycle–holonomy law

**Classification:** proved finite-complex theorem over \(\mathbb F_2\). Its integer ranks and canonical basis construction are independently checked by the accompanying audit. It is a discrete topological/gauge-theoretic law, not yet a physical charge law.

## 1. Setting and notation

Let \(X=I^6\) be the standard six-dimensional cubical complex and let \(G=X^{(1)}=Q_6\) be its 1-skeleton. Then
\[
|V|=64,\qquad |E|=192,\qquad |F_2|=240,\qquad |F_3|=160.
\]
All chains and cochains in this theorem have coefficients in \(\mathbb F_2\). Write
\[
C_2(X)\xrightarrow{\partial_2}C_1(X)
 \xrightarrow{\partial_1}C_0(X),\qquad
C^0(X)\xrightarrow{\delta_0}C^1(X)
 \xrightarrow{\delta_1}C^2(X),
\]
with \(\delta_k=\partial_{k+1}^{\,T}\).

Three spaces must not be conflated:
- the **graph cycle space** \(Z_1(G)=\ker\partial_1\);
- the **graph cut/cocycle space** \(B^1(G)=\operatorname{im}\delta_0\);
- the **cubical 1-cocycle space** \(Z^1(X)=\ker\delta_1\).

For this contractible cube, \(Z^1(X)=B^1(G)\), but this equality is a consequence of \(H^1(X;\mathbb F_2)=0\), not a definition.

## 2. Theorem: cycle–cocycle–holonomy correspondence

**Cohomological hypotheses (explicit).** The isomorphism induced by the coboundary map,
\\[
\\overline{\\delta}_1:C^1(X;\\mathbb F_2)/\\operatorname{im}\\delta_0
\\longrightarrow \\ker\\delta_2,
\\qquad [a]\\longmapsto\\delta_1a,
\\]
uses both
\\[
H^1(X;\\mathbb F_2)=0
\\qquad\\text{and}\\qquad
H^2(X;\\mathbb F_2)=0.
\\]
The first gives \\(\\ker\\delta_1=\\operatorname{im}\\delta_0\\), hence injectivity on gauge classes; the second gives \\(\\ker\\delta_2=\\operatorname{im}\\delta_1\\), hence surjectivity. Both hold because \\(X=I^6\\) is contractible.

**Theorem.** The following statements hold.

1. The graph cycle space has dimension
   \[
   \dim Z_1(G)=192-63=129.
   \]
   A spanning tree has 63 edges; its 129 chords determine a fundamental-cycle basis.

2. The graph cut/cocycle space has dimension
   \[
   \dim B^1(G)=\operatorname{rank}\delta_0=63.
   \]
   It is the orthogonal complement of the cycle space under the mod-2 edge pairing:
   \[
   B^1(G)=Z_1(G)^\perp.
   \]

3. The 240 square-face boundaries generate the entire graph cycle space:
   \[
   \operatorname{im}\partial_2=\ker\partial_1=Z_1(G),
   \qquad \operatorname{rank}\partial_2=129.
   \]
   Thus the 240 generators have exactly 111 independent relations.

4. The cubical cocycles are precisely the graph cuts:
   \[
   Z^1(X)=\ker\delta_1=\operatorname{im}\delta_0,
   \qquad \dim Z^1(X)=63.
   \]
   Equivalently,
   \[
   H_1(X;\mathbb F_2)=H^1(X;\mathbb F_2)=0.
   \]

5. Let \(a\in C^1(X;\mathbb F_2)\) be a \(\mathbb Z_2\) link connection. Its gauge class is uniquely determined by either:
   - its 129 holonomies on any fundamental-cycle basis, or
   - its plaquette-flux cochain \(b=\delta_1a\).

   The admissible plaquette fluxes are exactly
   \[
   \ker\delta_2=\operatorname{im}\delta_1,
   \]
   a 129-dimensional subspace of \(C^2(X)\). They satisfy 111 independent cube constraints.

### Proof

The graph \(Q_6\) is connected, so \(\operatorname{rank}\partial_1=|V|-1=63\). Hence
\[
\dim\ker\partial_1=|E|-\operatorname{rank}\partial_1=129.
\]
For any connected graph, the cut space is the orthogonal complement of its cycle space; its dimension is 63. A spanning tree gives one fundamental cycle for each non-tree edge, hence 192−63=129 independent cycles.

The cubical complex \(I^6\) is contractible. Therefore its first homology and cohomology vanish. In the cellular chain complex this gives
\[
\ker\partial_1=\operatorname{im}\partial_2,
\]
and in the cochain complex
\[
\ker\delta_1=\operatorname{im}\delta_0.
\]
Consequently \(\operatorname{rank}\partial_2=129\), and the 240 square boundaries have a 111-dimensional relation space. Also \(\operatorname{rank}\delta_1=129\), so \(\dim\ker\delta_1=192-129=63\).

A gauge transformation is \(a\mapsto a+\delta_0g\). For every cycle \(z\),
\[
\langle\delta_0g,z\rangle=\langle g,\partial_1z\rangle=0.
\]
Thus cycle holonomies \((-1)^{\langle a,z\rangle}\) are gauge-invariant. If two connections have equal holonomies on a cycle basis, their difference is orthogonal to all cycles and hence belongs to \(B^1(G)=\operatorname{im}\delta_0\); they are gauge-equivalent. This proves that the 129 basis holonomies classify gauge classes.

The flux is \(b=\delta_1a\), so \(\delta_2b=0\) by \(\delta_2\delta_1=0\). Conversely, if \(\delta_2b=0\), then \(b\in\ker\delta_2\). Since \(H^2(X;\mathbb F_2)=0\) for the contractible cube, \(\ker\delta_2=\operatorname{im}\delta_1\), so \(b\) is the flux of a connection. If two connections have the same flux, their difference lies in \(\ker\delta_1=\operatorname{im}\delta_0\), so they are gauge-equivalent. Finally, \(\dim\ker\delta_2=\operatorname{rank}\delta_1=129\), hence the 240 face fluxes obey 240−129=111 independent constraints. \(\square\)

## 3. The law in operational form

For an edge field \(a\), define
\[
\operatorname{Hol}_a(z)=(-1)^{\langle a,z\rangle},\qquad
W_a(p)=(-1)^{(\delta_1a)(p)}.
\]
Then, on \(I^6\),
\[
[a]_{\mathrm{gauge}}
\longleftrightarrow
\bigl(\operatorname{Hol}_a(\gamma_1),\ldots,
\operatorname{Hol}_a(\gamma_{129})\bigr)
\longleftrightarrow
b=\delta_1a\in\ker\delta_2.
\]
This is a bijection. The first representation uses 129 independent cycle measurements; the second uses 240 plaquette measurements subject to 111 independent cube constraints. Flatness \(b=0\) implies trivial holonomy on every cycle and therefore a pure-gauge connection.

## 4. Exact finite results versus physical interpretation

**Proved:** the dimensions, orthogonality, square-boundary generation, vanishing of \(H_1,H^1,H^2\), and the bijections above, under the stated cubical-complex hypotheses.

**Computationally audited:** the explicit Q6 cell enumeration, boundary ranks, fundamental-cycle and cut bases, orthogonality, and constraints. The audit is reproducible; CI is the execution record.

**Not proved by this theorem:** that a hexagram carries a particular electric, magnetic, Burgers, or Frank charge; that an experimentally measured correlation equals a cycle holonomy; or that this finite complex has a continuum physical limit. Those claims require a calibrated map from each of the 64 individual hexagrams to measured vertex/edge variables and an independently specified observable. The 64 hexagrams must not be collapsed to eight trigram labels when testing such a map.

## 5. Reproducibility

Run:
\`\`\`bash
python -m pytest -q tests/test_t103_cycle_cocycle.py tests/test_t103_q6_z2_magnetic_holonomy.py
python scripts/audit_t103_cycle_cocycle.py
python scripts/audit_t103_q6_z2_magnetic_holonomy.py
\`\`\`

The audit checks exact ranks over \(\mathbb F_2\), not floating-point approximations to homology. The magnetic spectra are separate finite numerical checks.

## 6. Relation to T103

T103 defines the \(\mathbb Z_2\) magnetic connection, plaquette curvature, and magnetic graph Laplacian. T104 supplies the structural theorem explaining why 129 cycle holonomies and 240 constrained plaquette fluxes encode the same 129-dimensional gauge information on the contractible six-cube.

## 7. Canonical duality clarification

The graph cycle space \\(Z_1(G)=\\ker\\partial_1\\subset C_1(G)\\) must be distinguished from the cubical cocycle space \\(Z^1(X)=\\ker\\delta_1\\subset C^1(X)\\). The mod-2 edge pairing identifies \\(C^1(X)\\) with \\(C_1(G)^*\\). Restriction to graph cycles gives
\\[
r:C^1(X)\\longrightarrow Z_1(G)^*,
\\qquad r(a)(z)=\\langle a,z\\rangle.
\\]
Its kernel is the annihilator of \\(Z_1(G)\\), which is \\(Z_1(G)^\\perp=\\operatorname{im}\\delta_0\\). Therefore
\\[
C^1(X)/\\operatorname{im}\\delta_0
\\;\\cong\\;Z_1(G)^*
=\\operatorname{Hom}(Z_1(G),\\mathbb F_2).
\\]
This is the canonical cycle-dual identification. Separately, the cohomological hypotheses above give the isomorphism induced by \\(\\delta_1\\):
\\[
C^1(X)/\\operatorname{im}\\delta_0
\\xrightarrow{\\;\\overline{\\delta}_1\\;}
\\ker\\delta_2.
\\]
Consequently \\(\\ker\\delta_2\\) is identified with \\(Z_1(G)^*\\) by composition of these two canonical isomorphisms. This avoids conflating graph cycles, graph cocycles/cuts, and cubical cocycles.

