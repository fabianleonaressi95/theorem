# T010 — Rumin spectral reduction on the Poincaré homology sphere

**Status:** theorem proved under the stated equivariance hypotheses; application to the standard contact structure on (S^3/2I) is valid. The complete list of Rumin eigenvalues and multiplicities on the quotient has **not** yet been computed.

**Scope:** finite-covering spectral reduction, character projection, and a scalar-Laplacian benchmark. This is not a claim that the full Rumin spectrum has already been evaluated.

## 1. Geometric setting

Let
[
S^3={zinmathbb C^2:lVert zVert=1}simeq SU(2)
]
carry its standard contact form
[
alpha=operatorname{Im}(ar z_1,dz_1+ar z_2,dz_2)
]
and the associated standard contact metric/Sasakian structure. Let (2Isubset SU(2)) be the binary icosahedral group, of order (120), acting on (S^3) by left multiplication. This action is free and preserves the standard contact metric structure. Set
[
M_{2I}=S^3/(2I).
]
The contact structure, contact metric, and Sasakian structure therefore descend to the compact quotient.

The descended Hopf/Reeb circle action makes (M_{2I}) a three-dimensional CR-Seifert manifold. Its orbifold base is (S^2/A_5), with cone orders ((2,3,5)). In particular, this is a Seifert fibration with orbifold base, not an ordinary smooth Hopf base.

## 2. Theorem: spectral projection under a finite contact quotient

Let (X) be a compact contact manifold with a contact metric, let a finite group (Gamma) act freely on (X) by contact isometries, and let
[
pi:Xlongrightarrow X/Gamma
]
be the quotient covering. Let (Delta_R^{(k)}) be a self-adjoint Rumin Laplacian in degree (k), defined naturally from the contact structure and metric. Assume its realization has compact resolvent and is (Gamma)-equivariant.

For every eigenvalue (lambda), let
[
E_{lambda}^{(k)}(X)=ker(Delta_R^{(k)}-lambda I).
]
Then pullback by (pi) identifies the eigenspace on the quotient with the invariant subspace:
[
pi^*E_{lambda}^{(k)}(X/Gamma)
cong E_{lambda}^{(k)}(X)^Gamma.
]
Consequently,
[
oxed{
operatorname{mult}_{X/Gamma}(lambda;Delta_R^{(k)})
=dim E_{lambda}^{(k)}(X)^Gamma
=rac{1}{|Gamma|}sum_{ginGamma}
operatorname{Tr}!left(gmid E_{lambda}^{(k)}(X)ight).
}
]

### Proof

Because the action is free, (X	o X/Gamma) is a regular finite covering. Differential forms and the bundles/forms in the Rumin complex on (X/Gamma) pull back to (Gamma)-invariant forms on (X); conversely, every invariant smooth form on (X) descends uniquely to the quotient.

The Rumin differential and its metric adjoint are natural under contact isometries. Hence the Rumin Laplacian commutes with the (Gamma)-action. Pullback therefore intertwines the quotient Laplacian with the restriction of the covering-space Laplacian to invariant sections. Restricting this intertwining identity to the (lambda)-eigenspaces gives the first isomorphism.

For a finite-dimensional unitary representation (E_lambda^{(k)}(X)), the operator
[
P_Gamma=rac{1}{|Gamma|}sum_{ginGamma}g
]
is the orthogonal projection onto its invariant subspace. Its rank equals its trace, which gives the character-average formula. (square)

### Application to the binary icosahedral quotient

Taking (X=S^3) and (Gamma=2I), for each Rumin degree (k):
[
oxed{
m_{lambda,k}(S^3/2I)
=rac1{120}sum_{gin 2I}
chi_{lambda,k}(g),
}
]
where (chi_{lambda,k}) is the character of the (2I)-representation on the (lambda)-eigenspace of the covering-space Rumin Laplacian.

This formula is exact. It reduces the quotient spectral multiplicity problem to the character decomposition of the eigenspaces already studied on the contact sphere.

## 3. Translation from (U(2)) types to (2I)-invariants

Suppose an eigenspace in Kitaoka's (U(2))-equivariant decomposition contains an irreducible (U(2))-module of highest weight ((a,b)), with (age b), and multiplicity (c_{lambda,k}(a,b)). On restriction to (SU(2)),
[
V_{(a,b)}ig|_{SU(2)}
cong operatorname{Sym}^{a-b}(mathbb C^2),
]
because the determinant character is trivial on (SU(2)).

Define
[
mu_n=dimleft(operatorname{Sym}^{n}(mathbb C^2)ight)^{2I}.
]
Then the contribution of this (U(2))-type to the quotient eigenspace is
[
c_{lambda,k}(a,b),mu_{a-b},
]
and hence
[
m_{lambda,k}(S^3/2I)
=sum_{age b}c_{lambda,k}(a,b),mu_{a-b},
]
provided the (U(2))-decomposition of the covering-space eigenspace is complete and its multiplicities (c_{lambda,k}(a,b)) have been correctly extracted.

This is a reduction formula, not yet the evaluated Rumin spectrum: the complete list of (c_{lambda,k}(a,b)) from the relevant Rumin degrees must still be transcribed and checked.

## 4. Character benchmark for the binary icosahedral group

For the irreducible (SU(2))-module (operatorname{Sym}^{n}(mathbb C^2)), the character at an element with eigenvalues (e^{pm i	heta}) is
[
chi_n(	heta)=rac{sin((n+1)	heta)}{sin	heta},
]
with limiting values (n+1) at (	heta=0) and ((-1)^n(n+1)) at (	heta=pi).

The nine conjugacy classes of (2I) can be grouped by class size and (SU(2)) half-angle as follows:

| Class size | Half-angle (	heta) |
|---:|---:|
| 1 | (0) |
| 1 | (pi) |
| 20 | (pi/3) |
| 20 | (2pi/3) |
| 30 | (pi/2) |
| 12 | (pi/5) |
| 12 | (2pi/5) |
| 12 | (3pi/5) |
| 12 | (4pi/5) |

Therefore
[
mu_n=rac1{120}sum_{[g]}|[g]|chi_n(	heta_g).
]
Direct character evaluation gives, for (0le nle30), nonzero invariant dimensions at
[
n=0,12,20,24,30,
qquad mu_n=1
]
for each of these five values; all other (n) in this range have (mu_n=0). This finite-range statement is a character calculation, not a claim about all higher degrees.

## 5. Independent scalar-Laplacian benchmark

The scalar spherical harmonics of degree (n) on the unit (S^3) have Laplace eigenvalue
[
lambda_n=n(n+2)
]
and, under (SU(2)_L	imes SU(2)_R), form the representation
[
operatorname{Sym}^{n}(mathbb C^2)otimes
operatorname{Sym}^{n}(mathbb C^2)^*.
]
The left (2I)-invariant subspace therefore has dimension
[
(n+1)mu_n.
]
It follows from the character calculation above that the first positive scalar eigenvalue on the unit round quotient is
[
oxed{lambda_1^{mathrm{scalar}}=12(12+2)=168,qquad
operatorname{mult}(lambda_1^{mathrm{scalar}})=13.}
]
This is an independent benchmark for the quotient geometry. It is **not** an eigenvalue or multiplicity claim for the Rumin Laplacian.

## 6. Contact torsion: a separate theorem and a necessary distinction

Rumin–Seshadri prove that on a compact three-dimensional CR-Seifert manifold, with a unitary representation of the fundamental group, the analytic torsion of their contact complex is related to Ray–Singer torsion (with the inverse convention stated in their Theorem 4.2). The descended Hopf/Reeb action and CR structure put (S^3/2I) in the CR-Seifert setting, so that theorem is relevant to the corresponding Rumin–Seshadri contact torsion.

Do **not** identify this automatically with every torsion normalization or modified Rumin Laplacian used by Kitaoka. The precise Laplacian, grading, zeta convention, and local correction term must be matched before transferring a torsion formula.

## 7. What is proved, and what remains open

**Proved here**
1. The free (2I)-quotient inherits the standard contact/Sasakian structure.
2. For any natural self-adjoint equivariant Rumin Laplacian with compact resolvent, quotient eigenspaces are exactly the (2I)-invariant covering-space eigenspaces.
3. Their multiplicities are given by the finite-group character projector.
4. The stated scalar-Laplacian benchmark follows from the binary icosahedral character average.

**Still to do**
1. Extract the complete (U(2))-type/eigenvalue table from Kitaoka's P1 for every Rumin degree.
2. Restrict each type to (SU(2)) and apply the invariant multiplicities (mu_n).
3. Check the resulting quotient spectrum independently, including zero modes and multiplicities.
4. Only then form the appropriate spectral zeta functions and compare torsion conventions.
5. Treat a discrete PRISM approximation and Mosco convergence as a separate open problem; neither follows from this finite-quotient theorem.

## 8. Relation to the Nielsen Hopf-fibration record

The repository already records Jennifer Lorraine Nielsen's *The Topological Unified Field Theory on the Complex Hopf Fibration* and its cited bibliography in
[`bibliography/source-bibliographies/nielsen-hopf-manuscript.md`](../bibliography/source-bibliographies/nielsen-hopf-manuscript.md).

That record is provenance for the sources cited by Nielsen; it is not an independent validation of the manuscript. T010 is a separate, standard-geometric result using the Hopf/Seifert structure of (S^3/2I). It is linked to the same Hopf-fibration research thread without attributing the Rumin theorem to Nielsen.

## References

1. A. Kitaoka, *Analytic torsions associated with the Rumin complex on contact spheres*, Int. J. Math. **31** (2020), 2050112. [arXiv:1911.03092](https://arxiv.org/abs/1911.03092).
2. A. Kitaoka, *Ray-Singer Torsion and the Rumin Laplacian on Lens Spaces*, SIGMA **18** (2022), 091. [arXiv:2009.03276](https://arxiv.org/abs/2009.03276), [DOI: 10.3842/SIGMA.2022.091](https://doi.org/10.3842/SIGMA.2022.091).
3. A. Kitaoka, *Harmonic forms and the Rumin complex on Sasakian manifolds*, [arXiv:2204.03446](https://arxiv.org/abs/2204.03446).
4. M. Rumin and N. Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier **62** (2012), no. 2, 727–782. [DOI: 10.5802/aif.2693](https://doi.org/10.5802/aif.2693).
5. Binary icosahedral group character table: [nLab, character table of (2I)](https://ncatlab.org/nlab/show/character+table+of+2I). The class-size/angle list above is used only for the explicit finite character average.

## Repository provenance

This theorem extends the repository's existing Hopf-fibration source trail. It does not rewrite or replace the Nielsen manuscript bibliography, and it does not treat citations in that manuscript as proof of T010.
