# T143-A — Antipodal equivariance of the minimal SO(3)/SU(2) connection

**Classification:** theorem under explicit hypotheses.  
**Scope:** finite graph, exact real/complex arithmetic. This theorem is not, by itself, a provenance statement about any particular floating-point archive.

## 1. Data and conventions

Let \(G=(V,E)\) be a finite undirected graph and let \(p:V\to V\) be a fixed-point-free involutive graph automorphism. Let
\[
n:V\longrightarrow S^2\subset\mathbb R^3
\]
satisfy the antipodal condition
satisfy
\[
n_{p(g)}=-n_g\qquad(g\in V).
\]

For every oriented edge \(g\to h\), assume \(n_h\ne -n_g\). Put
\[
c_{gh}=n_g\cdot n_h,\qquad v_{gh}=n_g\times n_h.
\]
Thus \(c_{gh}>-1\). Write \([v]_\times x=v\times x\), and let \(\sigma=(\sigma_1,\sigma_2,\sigma_3)\) be the Pauli matrices.

The SO(3) link is the shortest rotation
For every oriented edge \(g\to h\), assume \(n_h\ne -n_g\). Set
\[
c_{gh}=n_g\cdot n_h,\qquad v_{gh}=n_g\times n_h,
\]
so \(c_{gh}>-1\). Write \([v]_\times x=v\times x\), and let
\(\sigma=(\sigma_1,\sigma_2,\sigma_3)\) be the Pauli matrices.

Define the shortest SO(3) link by
\[
R_{gh}=I+[v_{gh}]_\times+
\frac{[v_{gh}]_\times^2}{1+c_{gh}}.
\tag{1}
\]
The canonical SU(2) lift is fixed—not chosen independently edge by edge—by
Fix the canonical SU(2) lift—not independent edgewise signs—by
\[
U_{gh}=
\sqrt{\frac{1+c_{gh}}2}\,I_2
-\frac{i}{\sqrt{2(1+c_{gh})}}\,
(v_{gh}\cdot\sigma).
\tag{2}
\]
The action convention is
\[
U_{gh}(x\cdot\sigma)U_{gh}^{\dagger}
=(R_{gh}x)\cdot\sigma
\qquad(x\in\mathbb R^3).
\tag{3}
\]
In particular, (2) is the lift
\(\exp[-i(\theta_{gh}/2)\widehat v_{gh}\cdot\sigma]\), where
\(\cos\theta_{gh}=c_{gh}\) and
\(\sin\theta_{gh}\widehat v_{gh}=v_{gh}\).
For the reversed edge, the convention gives
If \(c_{gh}=1\), then \(v_{gh}=0\) and (1)–(2) give \(R_{gh}=I\), \(U_{gh}=I_2\). If \(-1<c_{gh}<1\), (2) is equivalently
\(\exp[-i(\theta_{gh}/2)\widehat v_{gh}\cdot\sigma]\), with
\(\cos\theta_{gh}=c_{gh}\) and
\(\sin\theta_{gh}\widehat v_{gh}=v_{gh}\).
For reversed orientation,
\[
R_{hg}=R_{gh}^{T},\qquad U_{hg}=U_{gh}^{\dagger}.
\tag{4}
\]

## 2. Lemma: antipodal invariance of the edge data
## 2. Lemma: antipodal invariance of edge data

For every oriented edge \(g\to h\),
\[
c_{p(g)p(h)}=c_{gh},\qquad
v_{p(g)p(h)}=v_{gh}.
\tag{5}
\]

**Proof.** By the antipodal hypothesis,
**Proof.** Since \(n_{p(g)}=-n_g\) and \(n_{p(h)}=-n_h\),
\[
(-n_g)\cdot(-n_h)=n_g\cdot n_h,\qquad
(-n_g)\times(-n_h)=n_g\times n_h.
\]
This proves (5). \(\square\)
\(\square\)

## 3. Theorem: equivariance of the canonical connection

Under the hypotheses of §1,
\[
R_{p(g)p(h)}=R_{gh},\qquad
U_{p(g)p(h)}=U_{gh}
\tag{6}
\]
for every oriented edge \(g\to h\).

**Proof.** Equations (1) and (2) are functions only of the pair
\((c_{gh},v_{gh})\). Substitution of (5) therefore gives both equalities
in (6), including the direct—not merely projective—SU(2) equality.
The graph-automorphism hypothesis ensures that \(p(g)\to p(h)\) is again
an edge. \(\square\)

The direct equality in (6) depends on using the same canonical formula
(2) on every oriented edge. If arbitrary signs are independently attached
to SU(2) lifts, only the corresponding projective SO(3) statement is
automatic; a direct equality of the chosen lifts then requires a
compatible sign convention.

## 4. Corollary: every path and cycle has the same transported product

For an oriented path
\(\gamma=(g_0,g_1,\ldots,g_k)\), define the column-spinor transport by
\[
U_\gamma=
U_{g_{k-1}g_k}\cdots U_{g_1g_2}U_{g_0g_1},
\qquad
R_\gamma=
R_{g_{k-1}g_k}\cdots R_{g_0g_1}.
\tag{7}
\]
Let \(p\gamma=(p(g_0),\ldots,p(g_k))\). Then
**Proof.** Equations (1) and (2) depend only on
\((c_{gh},v_{gh})\). Equation (5) therefore gives both equalities in
(6). The graph-automorphism hypothesis ensures that the image is again
an edge. \(\square\)

The direct SU(2) equality uses the fixed canonical formula (2).
If arbitrary signs are independently attached to edge lifts, only
projective equivariance is automatic; direct equality then requires a
compatible sign convention.

## 4. Corollary: path and cycle transport

For an oriented path
\(\gamma=(g_0,\ldots,g_k)\), use column-spinor transport and define
\[
U_\gamma=U_{g_{k-1}g_k}\cdots U_{g_1g_2}U_{g_0g_1},
\qquad
R_\gamma=R_{g_{k-1}g_k}\cdots R_{g_1g_2}R_{g_0g_1}.
\tag{7}
\]
For \(p\gamma=(p(g_0),\ldots,p(g_k))\),
\[
U_{p\gamma}=U_\gamma,\qquad R_{p\gamma}=R_\gamma.
\tag{8}
\]
In particular, (8) holds for every closed path, hence for every cycle
holonomy and every plaquette holonomy for which the boundary is an
oriented graph cycle.

**Proof.** Apply (6) to each factor in (7). The ordered products agree
factor by factor; no commutativity assumption is used. \(\square\)

## 5. Corollary: descent to the Anti-Twin quotient

Let \(\bar G=G/\langle p\rangle\) be the quotient graph whose vertices
and edges are \(p\)-orbits. The link transport on a quotient edge is
defined by choosing either of its two lifted oriented edges and taking
its \(R\)- or \(U\)-matrix. Equation (6) shows that the result is
independent of which antipodal lift is chosen. Thus the canonical
SO(3) and SU(2) link transports descend to well-defined transports on
\(\bar G\). Path and cycle transports on the quotient are represented
by the corresponding lifted products and inherit (8).

This statement concerns the quotient graph and its descended discrete
connection. It does not assert that the quotient is a manifold, that
the connection is flat, or that all quotient cycles are boundaries of
plaquettes.

## 6. Specialization to Q6 and the RGS Anti-Twin

For \(V=\{0,1\}^6\), with Q6 edges joining bit strings that differ in
one coordinate, the map
\[
p(g)=g\oplus7
\]
is a fixed-point-free involutive graph automorphism. Hence, if the
archived normals obey \(n_{g\oplus7}=-n_g\) and the edge matrices are
defined by (1)–(2), all conclusions above apply. The quotient has
\(64/2=32\) vertex orbits.

The count of 32 quotient vertices is combinatorial. The descent of the
connection additionally uses the antipodal-normal identity and the
canonical link definitions.

## 7. Evidence boundary for floating-point archives

The theorem is exact under its hypotheses. A numerical archive can only
test those hypotheses and formulae to a stated tolerance. In particular:

1. Check \(n_{p(g)}+n_g=0\) for every vertex.
2. Reconstruct (1)–(2) from the archived normals and compare them with
   the stored \(R_{\rm SO(3)}\) and \(U_{\rm SU(2)}\), recording direct
   and projective residuals separately.
3. Check matrix integrity (orthogonality, determinant, unitarity).
4. For any archived plaquette list, verify that it consists of ordered
   boundary cycles before multiplying links; do not infer face ordering
   from an unordered incidence array.
5. Record the generator/source specification that establishes that the
   archived matrices were originally constructed by (1)–(2).

Agreement to machine precision supports the identification of the
archive with this construction; it does not prove exact equality of
floating-point entries or establish provenance on its own.

## 8. What is not implied

The theorem does not imply that an arbitrary operator assembled from the
connection commutes with the Anti-Twin permutation. That requires the
operator's full assembly rule, inner product, weights, and boundary
conditions to be equivariant. If a specific operator \(K\) is shown to
satisfy \(KP=PK\), then its space decomposes into the \(P=\pm1\)
eigenspaces; this is a separate operator-level verification.

Nor does the theorem imply flatness, path independence, a common
invariant complex line for a non-Abelian holonomy family, a continuum
limit, or a physical PSU–AntiTwin dynamics.
In particular, this holds for every closed path and every cycle
holonomy, not only for square plaquettes.

**Proof.** Apply (6) to each factor in (7), preserving the stated
multiplication order. The products agree factor by factor; no
commutativity assumption is used. \(\square\)

## 5. Corollary: descent to the Anti-Twin quotient

Let \(\bar G=G/\langle p\rangle\) be the quotient graph with vertices
and edges given by \(p\)-orbits. Define the transport on a quotient
oriented edge by choosing either of its two lifted oriented edges.
Equation (6) makes the result independent of the chosen antipodal
lift. Thus the canonical SO(3) and SU(2) link transports descend to
well-defined transports on \(\bar G\).

This is a statement about a discrete quotient graph and its connection.
It does not assert that the quotient is a manifold, that the connection
is flat, or that every quotient cycle bounds a plaquette.

## 6. Specialization to Q6

For \(V=\{0,1\}^6\), with edges joining bit strings differing in one
coordinate, \(p(g)=g\oplus7\) is a fixed-point-free involutive graph
automorphism. Therefore, if
\[
n_{g\oplus7}=-n_g
\]
and the links are defined by (1)–(2), all conclusions above apply.
The quotient has \(64/2=32\) vertex orbits.

The count 32 is combinatorial; descent of the connection additionally
uses the antipodal-normal identity and the canonical link definitions.

## 7. Evidence boundary for numerical archives

The theorem is exact under its hypotheses. A floating-point archive
can test those hypotheses and formulae only to a stated tolerance.

1. Check \(n_{p(g)}+n_g=0\) for all vertices.
2. Reconstruct (1)–(2) from the archived normals and compare with the
   stored \(R_{\rm SO(3)}\) and \(U_{\rm SU(2)}\), reporting direct and
   projective SU(2) residuals separately.
3. Check orthogonality, determinants, and unitarity.
4. Verify that any claimed 240-face input is an ordered boundary-cycle
   array before multiplying link matrices.
5. Record the source/generator specification establishing that the
   archived matrices were originally constructed by (1)–(2).

Agreement to machine precision supports identification of the archive
with this construction; it does not prove exact equality of floating
point entries or establish provenance by itself.

## 8. Non-consequences

The theorem does not imply that an arbitrary operator assembled from
the connection commutes with the Anti-Twin permutation. That requires
the full operator assembly rule, weights, inner product, and boundary
conditions to be equivariant. If a particular operator \(K\) is shown
separately to satisfy \(KP=PK\), its space decomposes into the
\(P=\pm1\) eigenspaces.

The theorem also does not imply flatness, path independence, a common
invariant complex line for a non-Abelian holonomy family, a continuum
limit, or physical PSU–AntiTwin dynamics.
