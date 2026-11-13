# MQM — Multidimensional geometric and statistical structure

## Status

**Methodological specification + tested finite-data transformations.**
This document does not state a new physical law or theorem. PCA, correlations,
and clustering are exploratory tools; they do not establish causality.

## 1. Observation units and data blocks

The finite Q6 seed has 64 vertices and 192 undirected edges. The analysis
therefore keeps three observational levels separate:

1. **Vertex block** (64 rows): local scalar field, torsion profile, graph
   neighbourhood summaries and explicitly defined local densities.
2. **Edge block** (192 rows): endpoint means/differences, direction labels,
   and metric conductances only when supplied from the archived metric data.
3. **Operator/global block**: spectra, singular values, determinant values,
   Hessian eigenvalues, solver residuals and global parameters. These are
   not replicated over vertex rows.

The implementation is in `models/mqm_multidimensional.py`.

## 2. Initial vertex variables

For vertex (g), the default exploratory row is

[
X_g=(phi_g,	au_g,d_g,overlinephi_{N(g)},
sigma_{phi,N(g)},(L_{Q6}phi)_g,V(phi_g)).
]

Here (d_g=6) on Q6, (overlinephi_{N(g)}) and
(sigma_{phi,N(g)}) are neighbourhood summaries, and (L_{Q6}) is the
unweighted combinatorial graph Laplacian. The quartic density is
(V(phi_g)=	frac14(phi_g^2-1)^2), matching the dimensionless potential
parameters of the current finite model.

Because Q6 is regular, degree is a structural check, not a variable with
cross-vertex variation. It must not be presented as an explanatory PCA factor.

## 3. Metric and edge blocks

The exact metric-edge Dirichlet density is included only when the caller
provides the 192 positive conductances (w_e):

[
E_e=rac12w_e(phi_v-phi_u)^2.
]

Half of each edge energy is assigned to each endpoint, so summing the vertex
densities recovers the total graph kinetic energy. The code does not infer
metric weights from the unweighted Q6 graph.

The edge table records ((arphi_e,Deltaphi_e,ar	au_e,
Delta	au_e,	ext{direction}_e)), with conductance appended only when
available. Categorical labels are preserved as labels and are not encoded as
ordinal numerical measurements.

## 4. Exploratory methods

The first implemented methods are:
- standardized SVD-PCA for numerical feature blocks;
- Pearson correlation matrices for descriptive screening.

Constant columns are retained but contribute no variance. In particular,
the constant Q6 degree column must not be interpreted as a discovered factor.
For categorical/mixed analysis, use an explicitly declared encoding or a
mixed-data distance; never silently ordinal-encode group labels.

## 5. Initial A13/Q6 application

The current archived A13 report supplies the converged 64-component field
(phi_g), the 64-component torsion profile (	au_g), and the Q6 graph
convention. It reports a stationary field with mean 1.8700401, standard
deviation 0.0161992, and Pearson correlation with torsion 0.9269817.

That correlation is a property of this finite model, its archived operators,
and the specified dimensionless parameters. Since the determinant coupling
uses the torsion profile, the association is not independent evidence of a
new physical law. It must be re-evaluated under parameter changes, alternative
initializations, symmetry-respecting perturbations and independent graph
refinements.

## 6. Required next audits

1. Rebuild vertex/edge features from the original A13 bundle and preserve
   source hashes and edge ordering.
2. Add the metric conductances from the audited raw coframe, not unit weights.
3. Separate parameter-sweep rows (simulation/configuration units) from
   vertex rows; do not pool them as independent samples.
4. Compare ordinary PCA with Q6-Laplacian/spectral methods and symmetry-orbit
   summaries.
5. Test stability under parameter variation, multistart, and refinement.
6. Only after robustness checks, formulate mathematical propositions.

## 7. Epistemic classification

- Q6 vertex/edge counts and regular degree: exact combinatorial facts.
- Feature construction and PCA implementation: definitions and numerical
  transformations, covered by unit tests.
- The (phi)-(	au) correlation: finite-model numerical observation.
- Causal interpretation, continuum behaviour, physical calibration and
  predictive power: open.
