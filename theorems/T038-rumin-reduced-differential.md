# T038 — Exact reduced Rumin differential on 2I harmonic sectors

## Objective

Restrict the geometric middle-degree Rumin differential to the exact 2I-isotypic decomposition constructed in T035–T037. This is a finite-dimensional equivariant reduction, not a new continuum spectral theorem.

## Geometric polarization block

For generic integers p,q >= 1, T025/T032 give

\[
A^2=\frac{p(q+1)}2,\qquad
B^2=\frac{q(p+1)}2,\qquad
L=2pq+p+q,\qquad S=\frac L2,
\]

and the geometric row differential

\[
D_{p,q}=\frac{L}{2\sqrt S}(-B,A).
\]

Its Gram operator is

\[
D_{p,q}^{*}D_{p,q}
=\frac L2
\begin{pmatrix}B^2&-AB\\-AB&A^2\end{pmatrix}.
\]

The scalar normalization is carried by the polarization row; it does not act on the group representation factor.

## Equivariance and reduction

Let U_m(g) be the symmetric-power representation on W_m=Sym^m(C^2). The group acts trivially on the two-dimensional polarization factor, so

\[
\mathcal D_m=D_{p,q}\otimes I_{W_m},\qquad
\mathcal U_m(g)=I_2\otimes U_m(g).
\]

Consequently, exactly,

\[
\mathcal D_m\mathcal U_m(g)
=\mathcal U_m(g)\mathcal D_m
\]

with the target action U_m(g). For an irreducible rho with multiplicity b_{m,rho}, T037 supplies an embedding

\[
M_{m,\rho}:V_\rho\otimes\mathbb C^{b_{m,\rho}}
\longrightarrow W_m.
\]

The induced reduced differential is therefore

\[
D^{\mathrm{red}}_{m,\rho}
=D_{p,q}\otimes I_{d_\rho b_{m,\rho}}.
\]

The implementation verifies the embedding identity

\[
(D_{p,q}\otimes I_{W_m})(I_2\otimes M_{m,\rho})
=M_{m,\rho}(D_{p,q}\otimes I_{d_\rho b_{m,\rho}})
\]

exactly for each nonzero sector and degree in the selected finite audit range. It also checks equivariance against all 120 group elements.

## Scope and limitations

- The reduction is exact because the Rumin polarization row and the finite-group action act on separate tensor factors.
- This does not produce new nontrivial matrices on the multiplicity factor: the reduced action there is the identity. Any future coupling between distinct harmonic degrees or additional geometric components would require its own operator matrix and proof of equivariance.
- The code currently treats generic p,q >= 1 middle-degree blocks and finite degrees. Boundary sectors are excluded.
- No all-degree compactness, analytic torsion, Mosco convergence, or Laplace–Beltrami–Yang–Mills limit is claimed.

## Reproducibility

\`\`\`bash
python -m unittest tests.test_t038_rumin_reduced_differential -v
python -m src.t038_rumin_reduced_differential --max-degree 3
\`\`\`

The included tests are regression tests; they must be executed in CI before a passing status is claimed.
