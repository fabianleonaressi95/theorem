# T067 — Stokes commutation of cubical face-integral interpolation

**Status:** proved for exact face integrals on a compatible oriented cubical complex.

## 1. Setting

Let (K) be an oriented cubical cell complex with compatible traces on common faces. Let (omega) be a sufficiently smooth differential (k)-form. Define the degree-(k) face-integral interpolator (pi_h^k) by
[
(pi_h^komega)(sigma)=int_sigmaomega
]
for every oriented (k)-cell (sigma); in degree zero this is point evaluation. Let (D_h^k) be the cellular cochain differential induced by the oriented incidence numbers.

## 2. Theorem

For every smooth differential form in the stated degree,
[
oxed{D_h^kpi_h^komega=pi_h^{k+1}(domega).}
]
In other words, the face-integral interpolator commutes exactly with the exterior derivative.

## 3. Proof

Evaluate both sides on an oriented ((k+1))-cell (	au). By the definition of the incidence differential,
[
(D_h^kpi_h^komega)(	au)
=sum_{sigmasubsetpartial	au}[	au:sigma]int_sigmaomega.
]
The oriented incidence signs are precisely the induced boundary orientations, so the sum is
[
int_{partial	au}omega.
]
Stokes' theorem gives
[
int_{partial	au}omega=int_	au domega
=(pi_h^{k+1}domega)(	au).
]
The equality holds on every ((k+1))-cell and therefore on the whole cochain complex. (square)

## 4. Numerical implementation boundary

The theorem concerns exact mathematical face integrals. The benchmark computes face degrees of freedom by finite-order Gauss quadrature. Its commutator residuals therefore verify the quadrature implementation on the tested forms, maps, and meshes; they do not prove exact integration for arbitrary non-polynomial data.

The source-level orientation audit confirms that the incidence coefficient
[
(-1)^p(2s-1)
]
matches the increasing active-axis orientation used by the cubical face degrees of freedom. Here (p) is the zero-based position of the removed axis and (s=0,1) selects the lower or upper facet.

## 5. Scope and non-conclusions

This is a finite-complex Stokes identity. It does not establish uniform boundedness of the interpolator in (HLambda^k), FEEC stability, discrete compactness, Mosco convergence, norm-resolvent convergence, or spectral convergence. Those require additional analytic estimates.
