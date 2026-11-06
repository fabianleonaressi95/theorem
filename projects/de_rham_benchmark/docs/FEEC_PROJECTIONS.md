# FEEC projections and discrete adjoints on curvilinear cubical meshes

Benchmark for Phases A–D of the projection/adjoint study, built on top of
the consistent tensor-product cubical FEEC masses introduced in PR #87
(`ddr/feec_mass.py`).  Standard FEEC only: no penalty weights, no PRISM
terms.

## What is implemented

| Phase | Content | Code |
|-------|---------|------|
| A | Map family `F_{K,h}(xi) = Phi(p_K + h xi)`, uniform bounds on `det J`, `sigma(J)`, `||J^{-1}||`, `||D^2 Phi||` estimate, face conformity, injectivity proxy | `ddr/feec_study.py::map_quality`, `ddr/geometry.py` |
| B | de Rham (face-integral) projections `pi_h`, commutator `d_h pi_h = pi_h d`, `L^2` projection errors, operator-norm proxy `||pi_h u||_M / ||u||_{L^2}` | `face_dofs`, `commutation_residual`, `projection_l2_error`, `_reconstruct_cell` |
| C | `delta_h^k = M_{k-1}^{-1} D_{k-1}^T M_k`, consistency vs the continuous codifferential on analytic test forms, mass stability | `DiscreteAdjoints`, `adjoint_consistency`, `mass_stability` |
| D | `lambda_min^+`, spectral gap, kernel dimension vs Betti numbers, Hodge energy split | `feec_spectrum`, `hodge_energy_parts` |

## Degrees of freedom and the projection

For every degree `k` the DOFs are the oriented integrals of the physical
k-form over the global cubical k-faces (point values for `k = 0`):

```
(pi_h u)_sigma = int_sigma u ,   sigma a k-face.
```

On each cell the local FEEC space is the lowest-order tensor-product
space: a basis function attached to a k-face `sigma` with varying axes
`I` and fixed axes `F` is `phi_sigma(xi) dxi^I`, where `phi_sigma` is the
product of the 1D endpoint factors `(1-xi_a)` / `xi_a` over `a in F`.
This is exactly the basis used by `assemble_consistent_masses`, so the
coefficients `cu` produced by `face_dofs` are the coordinates of `pi_h u`
in the consistent mass basis, and `_reconstruct_cell` evaluates `pi_h u`
pointwise for `L^2` error measurement.

The complex orientation was fixed so that the cubical boundary sign
`(-1)^pos (2s-1)` matches the vary-order face orientation used by the
DOFs; before this change `d_h pi_h = pi_h d` failed by a global sign.

## Quadrature

* Cell integrals (mass matrices, `L^2` norms, projection errors):
  tensor Gauss rule with `nq` points per direction.
* Face DOFs: tensor Gauss rule with `nqf` points per *varying* direction
  on each face.  `nqf = 6` integrates the polynomial test fields exactly;
  trig fields (frequencies <= 2.5) are integrated to ~1e-14.
* The continuous codifferential `delta u` is semi-analytic: first
derivatives of the test-form coefficients are analytic, while
derivatives of the metric factor `rho g^{ab}` use central differences
(`_FD_EPS = 1e-6`).  This limits the attainable adjoint residuals to
roughly 1e-6 relative; observed commutator residuals are ~1e-14 because
`d` needs only first derivatives.

## Phase A checks (`map_quality`)

* `min/max det J`, `sigma_min/max(J)`, `max ||J^{-1}||_2`, an estimate of
  `||D^2 Phi||_inf` by central differences of `J Phi`.
* `min sqrt(det g_K)`, `max cond(g_K)` from the pullback metric.
* Face conformity: every interior k-face must have `2^{d-k}` incident
  cells; physical images of face vertices computed through each incident
  cell must agree (exact by construction of the global map `Phi`, checked
  numerically).
* Injectivity *proxy*: `min det J > 0` plus exact preservation of the
  boundary (`Phi_a = x_a` on each face `x_a in {0,1}`, normal component
  only — tangential sliding is allowed, e.g. for `axis_bump`).  A map
  homotopic to the identity with positive Jacobian and boundary
  preservation is injective; this is reported as a proxy, not a proof.

Map families in `DomainMap`: `identity`, `affine`, `sinusoid`
(`Phi = x + a P(x) c`, `P = prod sin(m pi x_i)`), and `axis_bump`
(`Phi_i = x_i + a_i sin(pi x_i) sin(pi x_{i+1})`, genuinely
multi-directional curvature, boundary-preserving).

## Phase B: commutator and approximation

`commutation_residual` computes `||d_h pi_h u - pi_h d u||_inf`,
normalized by the largest DOF magnitude (so exactly closed forms with
`du = 0` still yield meaningful residuals).  On all tested affine and
curved maps the residual is at the quadrature/roundoff level (~1e-14).

`projection_l2_error` measures `||u - pi_h u||_{L^2}` and
`||pi_h u||_{L^2}` by pulling everything back to the reference cell and
using the pullback metric `g = DF^T G DF` — the same inner product as
the consistent mass matrices.

## Phase C: the discrete codifferential and its boundary layer

`delta_h^k = M_{k-1}^{-1} D_{k-1}^T M_k` is the algebraic adjoint of `d_h`
with respect to the FEEC mass inner products, i.e. it satisfies
`<d_h a, b>_{M_k} = <a, delta_h b>_{M_{k-1}}` for *all* cochains.

Comparison target: `pi_h(delta u)`, where `delta` is the strong
(pointwise) codifferential

```
(delta u)_K = -(1/rho) sum_{a,b} d_a( rho g^{ab} u_{bK} ).
```

**Key numerical observation.**  On the *unconstrained* complex (no
essential boundary conditions, as in this benchmark) `delta_h pi_h u`
does **not** converge to `pi_h delta u` up to the boundary: a boundary
layer of amplitude `O(1/h)` develops at `dOmega` whenever the form has a
nonzero relevant boundary flux (e.g. `u = dx` gives `delta_h pi_h u`
values `+-6` at `N=2`, concentrated exactly on boundary vertices, while
`delta(dx) = 0`).  In a fixed interior region `[0.2, 0.8]^d` the residual
converges at roughly `O(h^2)` for smooth forms, and for compactly
supported forms (`ScalarField.bump`) the *global* residual converges.
`adjoint_consistency` therefore reports the residual split into
boundary / interior / core (`[0.2,1-0.2]^d`) parts.

This is a numerical observation about the lowest-order unconstrained
FEEC complex; whether it reflects the analytically expected boundary
term in the codifferential consistency identity is left to the
analytical side.  No claim of discrete compactness or Mosco convergence
is made anywhere in this benchmark.

## Phase D: spectral indicators

`feec_spectrum` computes, per degree, `lambda_min^+` (smallest positive
generalized eigenvalue of `B_k = M_k Delta_k`), the spectral gap, the
numerical kernel dimension vs `beta_k`, and the first eigenpair residual.
Dense `eigh` is used, so it is only enabled when `max(n_k) <=
spectral_max_n` (default 500 in the shipped config).

## Observed results (`results/feec/feec_results.json`, `configs/feec_default.json`)

Finite-range observations on the shipped levels; not asymptotic claims.

* **Geometry (Phase A).**  All cases report `face_conformity_ok`,
  `injectivity_proxy`, and refinement-independent Jacobian ranges
  (e.g. sinusoid 2D `det J in [0.372, 1.628]`, `sigma_min = 0.372` at
  every level; axis_bump 2D `det J in [0.529, 1.471]`).  Mass condition
  numbers stay bounded under refinement (2D affine `cond M_0 ~ 15`,
  `cond M_1 ~ 4`; sinusoid `cond M_0` grows mildly 23 -> 40).
* **Commutator (Phase B).**  `d_h pi_h = pi_h d` holds to the quadrature
  floor on every case: worst relative residual `2.6e-8` (3D sinusoid,
  `nqf = 5`), typically `1e-13` or better in 2D.
* **Projection errors (Phase B).**  `||u - pi_h u||_{L^2} / ||u||_{L^2}`
  roughly halves per refinement (e.g. affine 2D `generic_1form`
  0.110 -> 0.055 -> 0.028 for N = 4, 8, 16).
* **Adjoints (Phase C).**  Global `delta_h pi_h u - pi_h delta u`
  residuals do *not* vanish for forms with boundary flux (the boundary
  layer described above; `rel_m_residual` stays O(1) or grows slowly).
  On the fixed core `[0.2, 0.8]^d` and for compactly supported forms the
  residuals converge: compact 1-form `rel_m_residual_core`
  0.18 -> 0.029 -> 0.006 (affine 2D), 0.40 -> 0.052 -> 0.010
  (sinusoid 2D); 3D compact forms show the same trend.
* **Spectra (Phase D).**  `lambda_min^+` converges toward the flat
  values (`~pi^2` at k=0,1 and `~2 pi^2` at k=2 in 2D; analogous in 3D)
  on affine meshes and to geometry-dependent limits on curved maps;
  numerical kernel dimensions equal the Betti numbers `(1,0,...)` at
  every tested level.  No small-eigenvalue pollution was observed for
  the consistent FEEC masses in these tests — consistent with, but not
  proving, the absence of the diagonal-mass collapse seen with the
  historical DEC weights.

## Running

```
python run_feec_study.py configs/feec_default.json --out results/feec
python test_feec_study.py
```

`configs/feec_default.json` covers affine / sinusoid / axis_bump /
aniso-metric cases in 2D and affine / sinusoid in 3D.

## Limitations

* Lowest-order elements only; `pi_h` is the de Rham interpolant, not an
  `H^1`-elliptic projection.
* `delta u` uses finite differences for metric-factor derivatives
  (semi-analytic, ~1e-6 floor).
* Spectral indicators are dense-eigensolver limited to moderate meshes.
* Injectivity is a proxy (positive Jacobian + boundary preservation),
  not a certified check.
* All convergence statements are finite-range empirical observations on
  the tested families; they are not asymptotic proofs.
