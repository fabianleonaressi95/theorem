# Edge-cochain comparator

This implementation makes the discrete kinematics explicit:

- each displacement component is a 0-cochain on mesh vertices;
- `d0` is the integer oriented vertex-to-edge incidence matrix;
- `d1` is the oriented edge-to-face incidence matrix;
- the exact chain identity `d1 @ d0 == 0` is tested;
- on each oriented triangle, edge differences reconstruct the constant P1 displacement gradient;
- the symmetric gradient enters the isotropic elastic energy.

The square can be split along either the SW–NE or SE–NW diagonal. Both orientations are now assembled as separate chain complexes and are included in the Q1-versus-cochain comparison. Each triangle inherits the smooth cellwise eigenstrain of its parent square. This allows a first sensitivity audit for mesh-orientation bias, but does not eliminate all mesh anisotropy or replace a rotated-mesh study. This is a cochain-based simplicial P1 comparator, not a physical realization of Q6 or the full PRISM graph. It also does not yet model singular Volterra dislocations, disclinations, or the Airy-stress formulation.

Run:

```bash
python scripts/rgs_cochain_defect_benchmark.py --self-test
python scripts/rgs_cochain_defect_benchmark.py --out artifacts/rgs_cochain_defect
```

Outputs are `report.json` and `results.csv`. The tests check the chain identity, affine patch test, zero-source case, and finite single/dipole solutions. Passing these tests validates only the implementation-level comparator, not a continuum limit or a material model.


## Regularized Volterra edge-dislocation source

A first Volterra-type source is now available as `volterra_edge`. It is a finite-width regularization of a slip cut starting at `(x0,y0)=(0.5,0.5)) and extending to the right boundary. For Burgers vector `b = b e_x` and cut normal `n = e_y`, the plastic distortion is represented distributionally by

`beta_p = b (e_x tensor e_y) delta(y-y0) H(x-x0)`.

The elastic energy uses the symmetric plastic strain, whose engineering shear component is

`gamma_p_xy = b delta(y-y0) H(x-x0)`.

The delta is regularized by a normalized Gaussian of width `core_width=0.025`. The code integrates this engineering shear across a vertical section to audit the Burgers magnitude (`b=0.02`). Both Q1 and cochain solvers include this source, and the comparison script runs it for both triangulation diagonals.

This is a controlled regularized Volterra slip-cut benchmark, not an exact singular Volterra solution: the core is smeared, the cut is represented by an eigenstrain field, and no atomistic core physics is included. The Burgers integral validates the imposed slip jump; it does not by itself validate the far-field Volterra stress/displacement asymptotics.


## Regularized wedge-disclination source

The `wedge_disclination` case adds a rotational Volterra cut. Along the same horizontal cut, the prescribed displacement jump is

`[u](x) = Omega (x-x0) e_y H(x-x0)`.

The corresponding cut-normal plastic distortion has a regularized `yy` component

`beta^p_yy = Omega (x-x0) delta_sigma(y-y0) H(x-x0)`.

The Frank-angle audit integrates this component across the cut-normal direction and differentiates the resulting slip with respect to x. The recovered slope is compared with the input `Omega=0.01` rad. This is a finite-width representation of a wedge-disclination slip cut. It is not a singular disclination-core solution, and its far-field stress asymptotics still require comparison with the analytical/semidiscrete reference model.


## Airy-stress reference and boundary-condition alignment

The comparison now includes an independent finite-difference Airy reference for the two defect incompatibilities. It solves

`c Delta^2 v = -inc(eps_p),  c=(1-nu^2)/E`

with
`sigma_xx=v_yy, sigma_xy=-v_xy, sigma_yy=v_xx`.
The discrete incompatibility operator is
`inc(eps_p)=d_yy eps^p_xx + d_xx eps^p_yy - d_xy gamma^p_xy`.
For the edge cut this gives the regularized derivative-of-Dirac source associated with a Burgers vector; for the wedge cut it gives the regularized Dirac source associated with a Frank angle. The Airy stress is divergence-free by construction.

For the square domain, the Airy boundary condition is clamped `v=0, partial_n v=0`. On straight sides this is equivalent, modulo the affine gauge of the Airy potential, to the zero-traction condition `Hess(v) t=0`. Therefore the displacement-based Q1 and cochain defect solves now use natural traction-free boundaries; only three degrees of freedom are pinned to remove the two translations and one rotation. The manufactured affine patch test retains its Dirichlet boundary data.

The new `scripts/rgs_airy_reference.py` compares stress and strain fields from Q1 and cochain P1 with the Airy reference on interior cells, excluding a three-cell boundary strip. It records topological source moments and weak residuals. This is an independent finite-difference reference, not a reproduction of the published semi-discrete/CIP-DG method. The core remains regularized and no singular-core asymptotic theorem is claimed.


## Eshelby wedge-disclination dipole to edge-dislocation limit

A second incompatibility source, `wedge_dipole`, represents two opposite Frank charges `+s` and `-s` at `y_0+d/2` and `y_0-d/2`, with `s=b/d`. The total Burgers vector of the dipole is therefore `B=s d e_x=b e_x`, in agreement with the kinematic relation discussed by Cesana–De Luca–Morandotti. At the source level,
`s[delta(y-y0-d/2)-delta(y-y0+d/2)] -> -b partial_y delta(y-y0)`
as `d -> 0`, which is the edge-dislocation incompatibility source for this orientation convention.

The Airy script evaluates the regularized source and stress-field differences at fixed core width 0.025 and successively smaller separations. The asymptotic check is numerical and regularized; it does not reproduce the paper's renormalized-energy expansion or prove the singular limit. The Frank charges are kept small in the dedicated limiting audit (`b=0.002`) so that the linearized-kinematics approximation remains more credible.


## First Airy-field comparison results (CI run #46)

The generated artifact from the full workflow reports the following relative (L^2) errors on interior cells, excluding a three-cell boundary strip:

| Defect, mesh | Q1 stress | Q1 strain | Cochain stress | Cochain strain |
|---|---:|---:|---:|---:|
| Volterra edge, 65x65 | 14.44% | 16.96% | 14.68% | 19.20% |
| Wedge disclination, 65x65 | 6.28% | 5.90% | 6.62% | 6.23% |
| Wedge dipole, 129x129 | 5.67% | 5.70% | 5.97% | 5.97% |

The errors decrease with refinement in the tested sequences. The wedge-dipole Q1/cochain relative energy difference also decreases from 31.23% at 65x65 to 12.12% at 129x129; this is still too large to claim energetic agreement at the present resolution.

For the dedicated dipole-to-edge limit audit, with (b=0.002) and core width 0.025, reducing dipole separation from 0.1 to 0.025 gives:
The fixed-grid sweep uses (n=129), hence (h=1/128); its separations are deliberately (0.1, 0.075, 0.05, 0.0375, 0.025), corresponding to (d/h=12.8, 9.6, 6.4, 4.8, 3.2). This avoids the stencil-locked value (d=2h), for which the centered finite-difference source can coincide algebraically with the discrete edge source and produce a misleading near-zero residual. The sweep is still a fixed-grid regularized check, not a proof of a continuum limit.
- relative incompatibility-source difference: 70.12% → 4.74%;
- relative Airy-stress difference: 23.76% → 1.26%.

The discrete Airy weak residuals are below (1.5\times10^{-11}), and the Q1/cochain free-equilibrium residuals are below (2\times10^{-14}) in the reported runs. These are numerical consistency checks, not a proof of the singular asymptotic result.
