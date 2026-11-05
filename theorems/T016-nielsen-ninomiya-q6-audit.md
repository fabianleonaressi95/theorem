# T016 — Nielsen–Ninomiya no-go theorem and the Q6 finite-graph audit

**Status:** literature theorem reconstructed at the level of its hypotheses and topological mechanism; Q6 conclusions below are exact finite-graph statements. No evasion of the no-go theorem is claimed.

## 1. Scope and conventions

The Nielsen–Ninomiya result is not the assertion that every finite graph has an even number of zero eigenvalues. It concerns a regularization of chiral fermions whose low-energy singularities can be interpreted as Weyl species. In the Hamiltonian formulation of Nielsen and Ninomiya, the relevant assumptions include locality, translation invariance, Hermiticity, a periodic Brillouin zone, and an exactly conserved, locally defined, quantized charge. The conclusion is a vanishing net chirality: for each fixed set of conserved quantum numbers covered by the theorem, left- and right-handed Weyl species occur in equal numbers.

The exact hypotheses differ between the Hamiltonian/homotopy formulation in *Absence I* and the intuitive topological formulation in *Absence II*. This note records the common structural content and does not silently replace those hypotheses by a stronger or weaker modern formulation.

## 2. Hamiltonian formulation: hypotheses

Consider a translation-invariant lattice Hamiltonian with a finite number of fermionic components per unit cell. In momentum space it is a periodic matrix-valued function on the Brillouin torus
\[
\mathbb T^d=\mathbb R^d/(2\pi\mathbb Z)^d.
\]
The standard assumptions used in the original argument have the following roles.

1. **Locality:** sufficiently rapid decay of position-space couplings gives the regularity in momentum required to define the map and its local topological degree.
2. **Translation invariance:** momentum is a good quantum number and the momentum domain is a torus, not \(\mathbb R^d\) with an arbitrary boundary.
3. **Hermiticity:** the Hamiltonian has real energy eigenvalues and isolated band crossings can be assigned the appropriate local structure.
4. **Exact conserved charge:** the charge is exactly conserved, quantized, and has a locally defined density. The theorem is applied separately in the relevant charge sectors.
5. **Weyl/continuum interpretation:** the zeroes under discussion are isolated low-energy singularities with a well-defined Weyl chirality. A generic zero of an arbitrary graph matrix is not automatically such a species.

The hypotheses are substantive. If one is relaxed, the theorem's conclusion need not apply in the same form; this is not a contradiction.

## 3. Topological mechanism in three spatial dimensions

For an isolated Weyl point \(p_a\) in the Brillouin torus, choose a small sphere \(S_a^2\) enclosing it and no other degeneracy. The eigenspaces of the relevant band(s) define a map to a complex projective space,
\[
f_a:S_a^2\longrightarrow \mathbb{CP}^{N-1}.
\]
The homotopy group
\[
\pi_2(\mathbb{CP}^{N-1})\cong\mathbb Z
\]
provides an integer topological charge. In the two-band case this is equivalently the degree/Chern number of the map to \(\mathbb{CP}^{1}\cong S^2\). For a simple Weyl point the charge is its chirality, up to the chosen orientation convention.

Remove disjoint small open balls around all isolated Weyl points from the Brillouin torus. The remaining compact manifold has boundary equal to the disjoint union of the enclosing spheres with the induced boundary orientations. The Berry curvature (or the corresponding closed topological two-form) is smooth on this punctured region. Since it is closed, Stokes' theorem gives
\[
0=\int_{\partial(\mathbb T^3\setminus\cup_a B_a^3)}F
  =-\sum_a\int_{S_a^2}F.
\]
Thus the sum of the integer charges vanishes:
\[
\boxed{\sum_a \chi_a=0.}
\]
For simple Weyl points, \(\chi_a=+1\) or \(-1\), so the number of positive- and negative-chirality points is equal. The homotopy-theoretic paper expresses the same balance through the classes of the maps into projective space. This is the topological core; it is not a count of all lattice eigenvectors.

**Qualification.** This boundary-flux presentation is the geometric explanation of the three-dimensional Weyl-node balance. It does not replace every technical step in the more general Hamiltonian theorem, particularly its charge-sector and degeneracy assumptions.

## 4. Why periodicity matters

The Brillouin zone of a translation-invariant lattice is compact and has no boundary. A single Weyl point cannot export its topological charge through an external momentum-space boundary. The total charge on the torus must cancel. A continuum model on a noncompact momentum space, a nonlocal lattice operator, or a model without the required exact charge can fall outside this argument; each case requires its own analysis.

## 5. What the theorem does not say

- It does not forbid lattice gauge theory in general.
- It does not forbid Wilson fermions: the Wilson term removes unwanted low-energy modes by breaking the naive chiral symmetry at nonzero lattice spacing.
- It does not say that every discretization has the same number of zero eigenvalues at finite size.
- It does not identify graph-theoretic zero modes with physical Weyl fermions.
- It does not rule out formulations that alter a hypothesis, such as overlap/Ginsparg–Wilson constructions, domain-wall constructions with an extra dimension, or nonlocal discretizations. Their locality, symmetry, and continuum properties must be checked on their own terms.

## 6. Exact Q6 statements

Let \(Q_6\) be the Cayley graph of \(\mathbb Z_2^6\), with translations \(T_i f(x)=f(x+e_i)\). Then
\[
T_i^2=I,\qquad T_i^{-1}=T_i.
\]
Consequently the centered difference is identically zero:
\[
\nabla_i^{\rm cent}=\frac{T_i-T_i^{-1}}2=0.
\]
This is an exact obstruction to interpreting the literal six-cube graph as a conventional centered-difference lattice.

For the already registered Clifford operator
\[
D_+=\sum_{i=1}^6\Gamma_i(T_i-I),
\]
the character \(\chi_k(x)=(-1)^{k\cdot x}\) gives
\[
D_+(k)=-2\sum_{i:k_i=1}\Gamma_i,\qquad
D_+(k)^2=4|k|I_8.
\]
Therefore only the trivial character \(k=0\) is a zero sector. This is a finite-dimensional algebraic spectrum, not a Weyl-node count: \(\mathbb Z_2^6\) has no continuous Brillouin torus, no momentum neighbourhood around \(k=0\), and no established continuum scaling parameter.

**Conclusion for Q6:** T015's single zero character does not evade Nielsen–Ninomiya. The standard hypotheses and the continuum Weyl interpretation have not been established for this graph. In particular, the centered derivative vanishes. A proposed refinement must supply a sequence of graphs/operators, a limiting momentum or phase space, locality bounds, a continuum symbol with isolated Weyl points, a chirality grading, and a controlled spectral/low-energy limit before a no-go comparison is meaningful.

## 7. Acceptance checklist for any claimed Q6 construction

A future Q6-derived chiral regulator must document all of the following, with proofs or reproducible bounds:

- [ ] a refinement sequence and a specified limiting space;
- [ ] a translation or replacement symmetry sufficient to define the relevant momentum/phase-space structure;
- [ ] locality (or an explicit statement that locality is abandoned);
- [ ] self-adjoint Hamiltonian / correct adjoint convention;
- [ ] exact charge and local charge density, or an explicit statement that this hypothesis is relaxed;
- [ ] a continuum Weyl symbol and isolated singularities;
- [ ] a chirality invariant for each singularity;
- [ ] total chirality and species count;
- [ ] controlled convergence of low-energy spectra and eigenvectors.

Until these items are met, the status is **finite graph result verified; chiral continuum regulator open**.

## 8. Primary references

1. H. B. Nielsen and M. Ninomiya, “Absence of neutrinos on a lattice (I). Proof by homotopy theory,” *Nuclear Physics B* **185** (1981), 20–40. DOI: [10.1016/0550-3213(81)90361-8](https://doi.org/10.1016/0550-3213(81)90361-8).
2. H. B. Nielsen and M. Ninomiya, “Absence of neutrinos on a lattice (II). Intuitive topological proof,” *Nuclear Physics B* **193** (1981), 173–194. DOI: [10.1016/0550-3213(81)90524-1](https://doi.org/10.1016/0550-3213(81)90524-1).
3. H. B. Nielsen and M. Ninomiya, “A no-go theorem for regularizing chiral fermions,” *Physics Letters B* **105** (1981), 219–223. DOI: [10.1016/0370-2693(81)91026-1](https://doi.org/10.1016/0370-2693(81)91026-1).

The 1982 DOI 10.1016/0550-3213(82)90011-6 is the erratum to *Absence I*, not a separate proof or a substitute for the 1981 article.
