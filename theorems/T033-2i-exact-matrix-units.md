# T033 — Exact matrix units and multiplicity-space extraction for the binary icosahedral action

**Status:** exact finite-group construction, conditional on an exact unitary model of each irreducible representation and an exact enumeration of the 120 group elements. This theorem supplies the algebraic extraction mechanism; it does **not** claim that the repository already contains all nine exact irreducible matrices.

## 1. Scope and convention

Let \(G=2I\), \(|G|=120\). Let \(U:G\to U(\mathcal H)\) be a finite-dimensional unitary representation, and let
\(\rho:G\to U(V_\rho)\) be an irreducible unitary representation of dimension \(d_\rho\).
Fix orthonormal bases in \(V_\rho\) and \(\mathcal H\). The inner product is conjugate-linear in the first variable.

The construction below is independent of the choice of coordinates on the ambient representation space, but the individual matrix units depend covariantly on the chosen basis of \(V_\rho\).

## 2. Matrix-unit formula

For \(1\leq i,j\leq d_\rho\), define
\[
\boxed{
E_{ij}^{(\rho)}
=\frac{d_\rho}{120}\sum_{g\in G}
\overline{\rho(g)_{ij}}\,U(g).
}
\]
This convention is fixed throughout this document. Equivalently, one may transpose the coefficient indices and obtain the transposed matrix-unit convention; mixing the two conventions is not allowed.

By Schur orthogonality, the operators satisfy
\[
E_{ij}^{(\rho)}E_{k\ell}^{(\sigma)}
=\delta_{\rho\sigma}\delta_{jk}E_{i\ell}^{(\rho)},
\qquad
(E_{ij}^{(\rho)})^*=E_{ji}^{(\rho)}.
\]
The central isotypic projector is
\[
P_\rho=\sum_{i=1}^{d_\rho}E_{ii}^{(\rho)}
=\frac{d_\rho}{120}\sum_{g\in G}
\overline{\chi_\rho(g)}\,U(g).
\]
In particular \(P_\rho^2=P_\rho=P_\rho^*\), and \(P_\rho P_\sigma=0\) for inequivalent irreducibles.

*Convention note:* the formula is for a left representation \(U(gh)=U(g)U(h)\). If the lifted deck action is represented by pullback \(g\mapsto L_{g^{-1}}^*\), use that as \(U\); do not silently replace \(g\) by \(g^{-1}\) in only one factor.

## 3. Multiplicity-space extraction

Choose a unit vector \(v_1\in V_\rho\) and let \(W_1=\operatorname{ran}E_{11}^{(\rho)}\). Then
\[
\mathcal H_\rho=P_\rho\mathcal H
\simeq V_\rho\otimes W_1,
\]
where the identification sends
\[
e_i\otimes w\longmapsto E_{i1}^{(\rho)}w.
\]
The matrix-unit identities imply
\[
\langle E_{i1}w,E_{j1}z\rangle
=\delta_{ij}\langle w,z\rangle,
\qquad
U(g)E_{i1}w=\sum_j\rho(g)_{ji}E_{j1}w.
\]
Thus an orthonormal basis of \(W_1\), transported by \(E_{i1}\), yields an orthonormal basis of the entire \(\rho\)-isotypic component. Its multiplicity is
\[
m_\rho=\dim W_1=\frac{1}{d_\rho}\operatorname{rank}P_\rho.
\]
For a Rumin differential \(D_R\) intertwining the group actions in adjacent degrees, the same construction in source and target identifies its restriction with
\[
D_R|_{\mathcal H_\rho}
=I_{V_\rho}\otimes D_{R,\rho}
\]
after compatible multiplicity bases are fixed. The reduced matrix \(D_{R,\rho}\) is the object to compare with the \((p,q)\)-blocks of T025/T032.

## 4. Exact arithmetic requirements

For \(2I\), numerical floating-point projectors are useful diagnostics but are not an exact certificate. A complete implementation must use a number field containing the matrix entries and character values (typically a specified cyclotomic extension, or an explicitly embedded algebraic extension), with a fixed complex conjugation.

The audit must verify, exactly:
1. \(U(g)U(h)=U(gh)\) and \(U(g)^*=U(g^{-1})\);
2. the irreducible model dimensions and unitarity;
3. the matrix-unit multiplication and adjoint identities;
4. \(P_\rho=\sum_iE_{ii}^{(\rho)}\), \(P_\rho^2=P_\rho\), and pairwise orthogonality;
5. \(\sum_\rho d_\rho^2=120\);
6. \(\sum_\rho P_\rho=I\) on a representation containing all irreducible types;
7. the multiplicity identity \(\dim P_\rho\mathcal H=d_\rho m_\rho\);
8. the intertwining identity \(D_RP_\rho^{\rm src}=P_\rho^{\rm tgt}D_R\).

The last identity is the bridge from the abstract equivariance in T031 to actual reduced harmonic matrices. It must be checked degree by degree.

## 5. What this establishes and what it does not

**Established algebraically:** once exact unitary irreducible models and the exact group table are supplied, the displayed sums construct matrix units, projectors, and multiplicity-space bases. The decomposition and intertwining conclusions follow from finite-group representation theory.

**Not established by this file alone:** the nine explicit \(2I\) representation matrices, a machine-readable exact character table, the values of the multiplicities in every \(\operatorname{Sym}^m(\mathbb C^2)\), or the actual geometric Rumin matrices in those bases. Those require the exact input data and a successful execution of the accompanying audit. T033 therefore closes the construction formula, not the data-export task.

## 6. Relation to prior results

- T024 closes the three-dimensional Kitaoka/Rumin–Seshadri operator and torsion convention comparison under its stated hypotheses.
- T030 supplies the local normalized-representative formula for the central Rumin differential.
- T031 proves naturality and \(2I\)-equivariance/descent, while explicitly leaving the full nine-irrep models open.
- T032 fixes the harmonic-block Gram matrix and distinguishes the geometric row differential from a square-root factorization.

T033 supplies the exact finite-group matrix-unit mechanism needed to turn equivariance into explicit multiplicity-space matrices. It does not alter the conclusions or hypotheses of those results.

## References

1. Standard finite-group representation theory: Schur orthogonality and the Wedderburn decomposition of \(\mathbb C[G]\).
2. Repository T024, T030, T031, and T032.
