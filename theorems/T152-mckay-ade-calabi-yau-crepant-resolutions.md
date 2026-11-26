# T152 — Binary McKay–ADE correspondence, Calabi–Yau orbifolds and crepant resolutions

**Date:** 26 November 2026  
**Classification:** established algebraic geometry and representation theory, specialized to the binary icosahedral group; dimension-dependent existence statements are separated explicitly.  
**Source prompt:** Mee Seong Im, UIUC presentation, 21 July 2008 (lecture outline supplied for this repository integration).  
**Dependencies:** T119 (binary icosahedral group and selected representations), T121 (icosahedral \(A_5\) action), T144 (invariant-count coefficients), T146 (dodecahedral dual and Q6 lift), A1 (scalar spectrum on \(S^3/2I\)).  
**Status boundary:** this record formalizes classical theorems and their application to \(2I\). It does not claim a new proof of McKay, BKR, or existence of a crepant resolution in dimensions where no general theorem applies.

## 1. Calabi–Yau conventions

Let \(X\) be a smooth complex \(n\)-fold. Its canonical bundle is
\[
K_X=\bigwedge\nolimits^n T_X^*.
\]
For this record, a **Calabi–Yau manifold** means a compact Kähler manifold with holomorphically trivial canonical bundle, unless a weaker convention is explicitly stated. Triviality of \(K_X\) implies \(c_1(X)=0\); the converse at the level of the real cohomology class \(c_1(X)=0\) does not by itself assert holomorphic triviality without additional hypotheses. Some literature uses “Calabi–Yau” for noncompact or singular spaces, or imposes extra conditions such as simple connectivity; those conventions must be stated when used.

For a compact Kähler manifold with \(c_1(X)=0\), Yau's theorem supplies a Ricci-flat Kähler metric in every Kähler class. This metric statement is not a claim that every orbifold quotient is flat away from its singular locus.

A nonzero holomorphic \(n\)-form trivializing \(K_X\) gives a holomorphic volume form. Integration requires a specified measure/form and suitable compactness or integrability hypotheses; it is not justified merely by saying that a space has a volume form.

## 2. Quotient orbifolds and the determinant-one condition

Let \(G\subset GL(n,\mathbb C)\) be finite and act linearly on \(\mathbb C^n\). The quotient
\[
X=\mathbb C^n/G
\]
is generally singular at images of points with nontrivial stabilizer. Locally it is an orbifold quotient; it need not be singular only at isolated points, and it need not be flat on the regular locus for an arbitrary metric.

The determinant-one condition has a precise canonical-bundle meaning. If \(G\subset SL(n,\mathbb C)\), the standard form
\[
\Omega=dz_1\wedge\cdots\wedge dz_n
\]
is \(G\)-invariant. Thus the quotient is Gorenstein (in the standard finite-quotient setting) and its canonical divisor is Cartier and trivial in the affine quotient setting. This is the natural hypothesis for a crepant-resolution problem. The converse should not be asserted without specifying the quotient action and canonical linearization.

The elementary real quotient \(\mathbb R/\{\pm1\}\cong[0,\infty)\) illustrates a fixed-point quotient, but it is not a model for the complex canonical-bundle condition or for a crepant resolution.

## 3. Crepant resolutions

A resolution of a normal variety \(X\) is a proper birational morphism
\[
p:Y\longrightarrow X
\]
with \(Y\) smooth. When \(X\) is Gorenstein, the resolution is **crepant** if
\[
K_Y=p^*K_X,
\]
equivalently the discrepancy divisor is zero. In line-bundle notation this is \(K_Y\simeq p^*K_X\), with the canonical identification understood; the expression \(p^*(K_X)\cong K_Y\) is shorthand for this condition.

Crepant does not mean unique, and smooth does not automatically mean compact. A crepant resolution of a quotient with trivial canonical class has trivial canonical bundle under the stated hypotheses, so it is a noncompact Calabi–Yau in the corresponding algebraic-geometric sense; it is not automatically a compact Calabi–Yau manifold.

The illustrative reducible curve \(xy=0\) can be separated by a blow-up/strict-transform construction, but this elementary operation is not a general crepant-resolution algorithm and does not establish the McKay correspondence. The informal “lift one branch to height \(z=1\)” picture is not used as a proof here.

## 4. Dimension two: Kleinian singularities and the classical McKay correspondence

Let \(G\subset SL(2,\mathbb C)\) be finite. Then \(\mathbb C^2/G\) is a Kleinian (Du Val, rational double-point) surface singularity. It has a unique minimal resolution, and that resolution is crepant. The exceptional curves are smooth rational curves whose intersection graph is the finite Dynkin diagram of type \(A\), \(D\), or \(E\).

The McKay quiver is defined from the defining two-dimensional representation \(V\) of \(G\): its vertices are the irreducible representations \(\rho_i\), and the multiplicity of \(\rho_j\) in \(V\otimes\rho_i\) gives the directed adjacency multiplicity. For the finite subgroups of \(SL(2,\mathbb C)\), the underlying graph is the corresponding **affine** ADE Dynkin diagram. The trivial representation corresponds to the affine vertex; the nontrivial irreducibles correspond to the finite Dynkin vertices and hence to the exceptional curves. This qualification avoids the imprecise claim that every irreducible representation corresponds one-to-one to an exceptional curve.

The ADE assignment is:
| Surface type | Finite subgroup of \(SL(2,\mathbb C)\) | Order |
|---|---|---:|
| \(A_{k-1}\), \(k\ge2\) | cyclic group \(C_k\) | \(k\) |
| \(D_{k+2}\), \(k\ge2\) | binary dihedral group of order \(4k\) | \(4k\) |
| \(E_6\) | binary tetrahedral group | \(24\) |
| \(E_7\) | binary octahedral group | \(48\) |
| \(E_8\) | binary icosahedral group \(2I\) | \(120\) |

The binary polyhedral groups are the finite subgroups of \(SU(2)\), hence of \(SL(2,\mathbb C)\), up to conjugacy. Triangle-group notation is convention-dependent; this record uses group names and orders rather than an ambiguous presentation shorthand.

### 4.1 The \(2I\) / \(E_8\) case

The binary icosahedral group \(2I\) has order \(120\), lies in \(SU(2)\), and fits into
\[
1\longrightarrow\{\pm1\}\longrightarrow 2I
\longrightarrow A_5\longrightarrow1.
\]
These facts and the explicit quaternionic model are recorded in T119. Its quotient singularity
\[
\mathbb C^2/2I
\]
is the Kleinian singularity of type \(E_8\). Equivalently, its analytic hypersurface model is
\[
x^2+y^3+z^5=0
\]
(up to the usual analytic/algebraic coordinate conventions). The minimal resolution has eight exceptional rational curves with intersection matrix equal to the negative \(E_8\) Cartan matrix. The dual graph is \(E_8\); the affine McKay graph is \(\widetilde E_8\).

This is the rigorous bridge between the icosahedral rotational group \(A_5\), its binary lift \(2I\), and the exceptional Lie type \(E_8\). The dodecahedron and icosahedron share rotational symmetry group \(A_5\); the binary lift is a spin cover, not another ordinary spatial symmetry group. T146 supplies a separate, explicit finite dodecahedron-to-Q6 chain construction and records its spectral obstruction. No claim is made that the T146 Q6 Laplacians are the \(E_8\) intersection form or the McKay Cartan matrix.

## 5. Dimension three: \(G\)-Hilbert schemes, flops and derived McKay

Let \(G\subset SL(3,\mathbb C)\) be finite. The \(G\)-Hilbert scheme \(G\text{-Hilb}(\mathbb C^3)\) parametrizes \(G\)-clusters: zero-dimensional \(G\)-invariant subschemes \(Z\) whose coordinate ring is the regular representation of \(G\). Under the hypotheses of Bridgeland–King–Reid, the distinguished \(G\)-Hilb component gives a crepant resolution of \(\mathbb C^3/G\), and the Fourier–Mukai transform yields an equivalence
\[
D^b\!\operatorname{Coh}(G\text{-Hilb}(\mathbb C^3))
\simeq
D^b_G\!\operatorname{Coh}(\mathbb C^3).
\]
This is a derived-category statement, not an assertion that the resolved variety and the quotient are isomorphic or that the resolution is unique.

Different crepant resolutions of a threefold can be related by flops. For abelian \(G\), variation of GIT and moduli of \(G\)-constellations provide a systematic description of crepant resolutions; the precise statement depends on the stability chamber and the class of resolutions under consideration. Do not attribute to Craw–Ishii a stronger universal statement than their hypotheses establish.

The three-dimensional McKay correspondence is not the same simple finite ADE graph classification as in dimension two. In particular, the irreducible-representation/exceptional-curve bijection for Kleinian surfaces must not be copied unchanged to threefolds.

## 6. Dimension greater than three

For \(n>3\), a crepant resolution of \(\mathbb C^n/G\) need not exist. Terminal quotient singularities provide important obstructions: if a singularity is terminal, every exceptional divisor has positive discrepancy, so a crepant resolution by a smooth variety cannot exist. Existence is special and depends on the group action and singularity.

Higher-dimensional versions of derived McKay equivalence exist under additional geometric hypotheses, but there is no blanket theorem that every finite \(G\subset SL(n,\mathbb C)\) admits a crepant resolution. The existence question, the classification of all crepant resolutions, and the structure of their cohomology or K-theory are separate problems.

## 7. Integration with the repository's existing results

This record is intentionally connected to, rather than a replacement for, existing work:

- **T119:** exact quaternionic construction of \(2I\), order \(120\), selected representations and central characters. T119 does not contain the full irreducible character table or the McKay adjacency calculation.
- **T121:** the ordinary \(A_5\) action on Q6 and its exterior Clifford module. This is an \(A_5\)-action and must be distinguished from a \(2I\)-module on which the central element \(-1\) acts nontrivially.
- **T144:** invariant-count coefficients. Molien/invariant-series calculations are related representation-theoretic data, but do not by themselves prove the geometric McKay correspondence or construct a resolution.
- **A1:** scalar spectral multiplicities on \(S^3/2I\). This is spectral geometry of the spherical quotient, distinct from the exceptional-curve intersection lattice of the \(E_8\) resolution.
- **T146:** dodecahedral polar dual, antipodal action and finite Q6 chain map. Its failed selected-sector intertwining is retained; no fitted weights or inferred \(E_8\) operator are introduced.
- **T027:** Rumin differential/intertwiner work remains a separate analytic/spectral branch. A derived equivalence of coherent-sheaf categories does not automatically identify Rumin complexes or their spectra.

The justified dependency path is
\[
T119\longrightarrow (2I\subset SL(2,\mathbb C))
\longrightarrow \mathbb C^2/2I
\longrightarrow \widetilde{\mathbb C^2/2I}\text{ of type }E_8.
\]
The icosahedral/dodecahedral geometry supplies the \(A_5\) quotient and its binary lift. The arrows from the resolution to Q6, RGS, T027, or physical models are **comparison/open-obligation** edges unless an explicit functor, chain map, or operator intertwiner is constructed.

## 8. Proof-status register

| Claim | Status in this record | Evidence / closure |
|---|---|---|
| \(2I\subset SU(2)\), \(|2I|=120\), \(2I/\{\pm1\}\cong A_5\) | PROVED; exact finite audit in T119 | T119 and exact quaternionic closure audit |
| Binary polyhedral groups correspond to affine ADE types | PROVED classical theorem | McKay construction from tensoring by the defining two-dimensional representation |
| \(\mathbb C^2/2I\) is type \(E_8\) | PROVED classical classification | Kleinian quotient classification |
| Minimal resolution of \(\mathbb C^2/2I\) is unique and crepant | PROVED classical surface theorem | Du Val/Kleinian surface theory |
| \(G\)-Hilb gives a crepant resolution for finite \(G\subset SL(3,\mathbb C)\), with BKR derived equivalence | PROVED under BKR hypotheses | Bridgeland–King–Reid |
| All threefold crepant resolutions are classified by one ADE graph | NOT CLAIMED | False as a general extension of the surface statement |
| Every \(G\subset SL(n,\mathbb C)\), \(n>3\), admits a crepant resolution | NOT CLAIMED; generally false | Terminal quotient obstructions and special-case existence |
| A canonical \(E_8\) operator is already realized by T146/Q6 | OPEN | Requires a specified chain/cohomology map preserving the intersection pairing and operator |
| McKay/derived equivalence identifies T027 Rumin spectra | OPEN | Requires a functorial construction on the relevant complexes and an operator-intertwining theorem |

## 9. References

1. J. McKay, “Graphs, singularities, and finite groups,” *Proc. Sympos. Pure Math.* 37 (1980), 183–186.
2. M. Artin, “On isolated rational singularities of surfaces,” *Amer. J. Math.* 88 (1966), 129–136.
3. T. Bridgeland, A. King, M. Reid, “The McKay correspondence as an equivalence of derived categories,” *J. Amer. Math. Soc.* 14 (2001), 535–554, DOI: [10.1090/S0894-0347-01-00368-X](https://doi.org/10.1090/S0894-0347-01-00368-X); preprint [arXiv:math/9908027](https://arxiv.org/abs/math/9908027).
4. Y. Ito, M. Reid, “The McKay correspondence for finite subgroups of SL(3,C),” in *Higher-dimensional complex varieties* (Trento, 1994), de Gruyter, 1996, 221–240; preprint [alg-geom/9411010](https://arxiv.org/abs/alg-geom/9411010).
5. A. Craw, A. Ishii, “Flops of \(G\)-Hilb and equivalences of derived categories by variation of GIT quotient,” *Duke Math. J.* 124 (2004), 259–307; preprint [math/0211360](https://arxiv.org/abs/math/0211360).
6. S. S. Roan, “On the generalization of Kummer surfaces,” *J. Differential Geom.* 30 (1989), 523–537. (Historical threefold constructions should be cited with their exact hypotheses; this reference is not used here as a universal existence theorem.)
7. S.-T. Yau, “On the Ricci curvature of a compact Kähler manifold and the complex Monge–Ampère equation, I,” *Comm. Pure Appl. Math.* 31 (1978), 339–411.

**Reproducibility:** no new numerical result is claimed by T152. T119, T121, T144, T146 and A1 retain their existing scripts, outputs and tests. A future computational McKay adjacency audit should construct the complete irreducible character data and tensor-product multiplicities exactly, then compare the resulting affine graph with \(\widetilde E_8\); it must not be represented as already executed by the existing T119 selected-representation audit.
