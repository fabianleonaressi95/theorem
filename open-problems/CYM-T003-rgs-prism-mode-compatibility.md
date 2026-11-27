# CYM-T003 — RGS/PRISM mode compatibility and predictive value

**Status:** open problem / physical-mathematical hypothesis.

## Question

Can a geometry-derived operator built from an existing RGS or PRISM structure predict spectral and morphological observables of a specified elastic-wave experiment more accurately, or with a genuinely new invariant prediction, than a matched classical discretization?

## Preconditions

A proposed bridge must provide:
- an explicit map from physical degrees of freedom to the discrete state space;
- a mass/inner-product matrix with physical units or a declared nondimensionalization;
- a stiffness/field operator derived from an action, constitutive law, or consistent discretization;
- boundary conditions and a symmetry representation;
- convergence and stability evidence;
- a held-out benchmark not used to tune the operator.

## Existing structures eligible for audit

Q6 (64 vertices, six-dimensional hypercube adjacency), RGS 188D archived operators, (O_h) symmetry data, and PRISM/Krist-All structures may be considered. Their spectra and dimensions must not be equated merely because they share numerical values or visual symmetries.

## Baseline and acceptance test

Compare against a classical finite-element or finite-difference model on the same domain and with the same observations. Report frequency errors, eigenspace angles, nodal-set distances, topology, parameter sensitivity, and computational cost. A claimed advantage must persist on held-out geometries or perturbations.

## Falsification

The hypothesis is not supported if the RGS/PRISM model requires arbitrary weights, post-hoc mode matching, or more fitted parameters than the classical baseline without delivering a reproducible predictive gain.
