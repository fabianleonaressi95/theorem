# T036 — Explicit exact irreducible matrix models of 2I

Status: constructive exact-algebraic extraction from symmetric powers of the defining SU(2) representation. The implementation and tests are included; execution is not yet certified.

## Construction

For each irreducible label rho, select the least degree m for which the exact T021 Molien multiplicity b(m,rho) is one. The code determines these degrees from the numerator series, without hard-coding them.

On homogeneous polynomials of degree m, use the action f(v) -> f(rho_2(g)^(-1) v). The character projector is

P(rho,m) = d(rho)/120 sum over g in 2I of conjugate(chi_rho(g)) Sym^m(rho_2)(g).

At a multiplicity-one occurrence its image has dimension d(rho). An exact column basis B_rho of this image therefore gives an explicit irreducible model.

For every group element, solve

Sym^m(rho_2)(g) B_rho = B_rho R_rho(g)

using an exact nonsingular pivot-row minor. This produces matrices for all 120 elements.

## Invariant Hermitian metric

In the monomial basis X^(m-k)Y^k, the symmetric-power representation has invariant Gram matrix

W_m = diag(1/binomial(m,0), ..., 1/binomial(m,m)).

The induced metric is G_rho = B_rho^* W_m B_rho. The audit checks R_rho(g)^* G_rho R_rho(g) = G_rho for all 120 elements. The matrices need not be unitary in the arbitrary extracted basis; they are unitary with respect to this explicit positive invariant metric.

## Exact acceptance checks

For all nine irreducibles, the code checks central-projector idempotence and rank, invariance of the extracted subspace, exact recovery of all nine character values by traces, preservation of the induced Hermitian metric, and sum of squared dimensions equal to 120.

The JSON export stores exact bases, Gram matrices, all group matrices, group-element coordinates, and selected Molien degrees. Algebraic entries are serialized as exact SymPy expression strings.

## Reproducibility

Run from repository root:

```bash
python -m unittest tests.test_t036_2i_irreducible_models -v
python -m src.t036_2i_irreducible_models --output data/t036_2i_irreducible_models_exact.json
```

## Scope

T036 constructs explicit exact matrix models and invariant metrics. Together with T033, this makes the finite-group matrix-unit construction executable. The next step is to apply those matrix units to the Rumin harmonic eigenspaces and compute the Rumin-specific multiplicity bases and reduced geometric differential matrices.

No new spectral theorem, analytic torsion value, or continuum-limit claim is made.


## Eight models beyond the defining representation — explicit target

The eight non-fundamental irreducibles are
\[
\mathbf1,\quad \mathbf2',\quad \mathbf3,\quad \mathbf3',
\quad \mathbf4,\quad \mathbf4',\quad \mathbf5,\quad \mathbf6.
\]
Their dimensions are respectively \(1,2,3,3,4,4,5,6\), and
\[
1^2+2^2+3^2+3^2+4^2+4^2+5^2+6^2=116;
\qquad 116+2^2=120.
\]
The first multiplicity-one symmetric-power degrees, as specified by the exact Molien series, are:

| Irrep | Dimension | First multiplicity-one degree in \(\operatorname{Sym}^m(\mathbf2)\) |
|---|---:|---:|
| \(\mathbf1\) | 1 | 12 |
| \(\mathbf2\) (fundamental, reference) | 2 | 1 |
| \(\mathbf2'\) | 2 | 7 |
| \(\mathbf3\) | 3 | 2 |
| \(\mathbf3'\) | 3 | 6 |
| \(\mathbf4\) | 4 | 6 |
| \(\mathbf4'\) | 4 | 3 |
| \(\mathbf5\) | 5 | 4 |
| \(\mathbf6\) | 6 | 5 |

T034 independently constructs all nine representation families over \(\mathbb Q(\sqrt5,i)\), including the Galois-conjugate \(\mathbf2'\) and \(\mathbf3'\). T036 supplies a second, projector-based extraction and is responsible for the full matrix export indexed by all 120 group elements. These are independent constructions and should be compared by characters and intertwining equivalence, not by demanding entrywise equality between different bases.

## Reproducible build

The dedicated workflow `.github/workflows/t036-explicit-2i-models.yml` compiles the builder, runs its full exact `build_all_models()` and `verify_models()` acceptance path once, exports `data/t036_2i_irreducible_models_exact.json`, and uploads the exact model file as `t036-exact-2i-irreducible-models`. This avoids computing the same expensive exact models twice in a single CI job; the standalone unittest remains available for local/deeper regression.

**Acceptance criteria:** nine models; 120 matrices per model; exact projector rank equal to the irrep dimension; all nine character rows recovered from traces on all nine conjugacy classes; invariant positive Hermitian Gram matrix preserved by every group matrix; and total squared dimension 120.

**Execution status:** pending the dedicated T036 workflow run. The existence of the T034 construction and character table is not substituted for this independent T036 execution certificate. No T036 pass is claimed until its CI run and exported artifact are confirmed.
