# T134 exact-integration and trace-constant certification gap

**Status: implementation foundation only; no new (C_{\\rm tr}) certificate.**

The current curved-P3 audit assembles (D_h) and (H_{h,\\ell}) with UFL
quadrature (degrees 24, 32, 40) and computes a floating-point generalized
eigenvalue. Agreement between the last two quadrature degrees is a numerical
stability diagnostic. It is not exact integration, a rigorous interval
enclosure, or a proof that (C_{\mathrm{tr},h}\) lies below a specified
rational number.

## Exact polynomial integration primitives

`models/morandotti_exact_integration.py` now provides:

- exact integration of rational-coefficient polynomials on the reference
  triangle, using
  [
  \int_{\widehat K}x^iy^j\,dx\,dy=\frac{i!j!}{(i+j+2)!};
  ]
- exact integration of rational-coefficient polynomials on a reference edge;
- exact positive-semidefinite testing of rational symmetric matrices;
- an exact check of (H\preceq C D), provided the caller supplies the
  already assembled exact rational matrices on a correctly reduced quotient
  space.

These are reusable building blocks, not an implementation of curved-P3
form assembly.

## Why this does not yet certify curved P3 cells

For a general curved isoparametric map, the physical Hessian contains
(J^{-1}), derivatives of (J^{-1}), and powers of ((\det J)^{-1}).
Consequently the pulled-back volume integrand is generally rational rather
than polynomial. On a curved edge, the physical unit normal and arclength
Jacobian introduce additional metric factors; a square root can occur.
The polynomial simplex moment formula therefore cannot be applied directly
to these integrands.

A valid exact/certified curved-cell route must do one of the following:

1. derive rational polynomial identities after a suitable algebraic
   reformulation and certify all positive denominators; or
2. use outward-rounded interval integration with a proved remainder bound,
   then propagate the resulting matrix-entry intervals into a rigorous
   lower bound for (C D-H).

For a finite mesh, the final certificate must include the exact quotient
construction and prove
[
C_\star D_h-H_{h,\ell}\succeq0
]
on that quotient, with a rational (C_\star<20) if the goal is to justify
(α=40) for that mesh. This is a per-mesh result only.

For a mesh-uniform theorem, one additionally needs a single analytic
(C_\star<20) valid for the complete certified geometric class and every
refinement level. A finite collection of per-mesh certificates cannot
establish that uniform statement.

## Explicit T134 status

- Exact per-cell positivity of the represented P3 Jacobians: certified for
  the archived finite meshes.
- Exact polynomial integration utility: implemented and unit-tested.
- Exact assembly of the curved-P3 (D_h,H_{h,\ell}) forms: **not implemented**.
- Certified finite-mesh bound (C_{\mathrm{tr},h}<20): **not established**.
- Uniform bound (C_{\mathrm{tr}}<20) for the Gmsh family: **open**.
- Uniform coercivity with (α=40): **not certified**.

Do not label quadrature-degree convergence as exact integration. Do not
promote (α=40) from provisional numerical tuning to a proved
coercivity threshold until the matrix inequality above has a rigorous
certificate and the geometric family hypotheses have been established.


## Certified rational-integral enclosure primitive (follow-up implementation)

`models/morandotti_certified_rational_integration.py` adds an exact-rational
Bernstein enclosure for integrals of (p/q) on the reference triangle. On
each rational subtriangle it composes (p,q) with the affine map, bounds
each polynomial by its simplex Bernstein coefficients, certifies a strictly
positive denominator (subdividing when needed), and encloses the integral
by area times the quotient range. The accumulated enclosure width is bounded
by the requested global tolerance. It rejects floating-point coefficients,
uncertified denominator positivity, and unmet tolerances.

This is a rigorous scalar integration primitive, not yet the T134 assembly:
the curved-cell Hessian tensor contractions and curved-facet normal/metric
terms have not been translated into its rational-polynomial input, and no
matrix interval/PSD propagation is yet wired to the finite-element quotient.
In particular, it does not resolve square-root metric factors on general
curved edges. The T134 status above therefore remains unchanged.


## Completed 24-mesh diagnostic (2026-11-13)

The extended finite-mesh run completed successfully on the merged implementation. It covers 24 meshes (four target sizes \(h=0.080,0.045,0.030,0.025\), two core separations \(d=0.48,0.56\), and seeds 11, 29, 47). The generalized-eigenvalue estimates range from 9.1545269506 to 15.8151565222; the largest observed sufficient threshold is 31.6303130444, so \(\alpha=40\) has an observed margin of 8.3696869556 on this finite sample.

The archived 145,256 exact-rational per-cell certificates prove positive Jacobians for every represented cell map. The quadrature-degree 32/40 estimates agree to relative error at most \(1.71\times10^{-13}\), but this remains a numerical stability check.

**The certification gap remains open:** the scalar rational integration primitive is not yet wired into the actual curved-P3 Hessian and facet forms; curved-edge square-root metric terms and interval matrix/PSD propagation remain unimplemented. Neither a certified finite-mesh \(C_{\rm tr,h}<20\) bound nor a mesh-uniform \(C_{\rm tr}<20\) bound has been established. The exact archive is finite and cannot prove the all-level compact-class and facet-comparability hypotheses.
