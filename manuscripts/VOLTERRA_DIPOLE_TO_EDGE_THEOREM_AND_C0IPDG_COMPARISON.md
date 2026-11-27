# Volterra dipole-to-edge limit: theorem statement and C0-IPDG comparison

**Record:** VDE-01  
**Status:** source-limit theorem proved under smooth-core hypotheses; periodic Airy response estimate conditional on an operator bound; Fourier-spectral evidence numerically verified; independent C0-IPDG comparison open.  
**Scope:** plane-strain linear elasticity with smooth regularized cores. No singular-core or atomistic limit is claimed.

## 1. Setting and sign convention

Let f_sigma belong to W^{5,2} on the line or periodic cell, and let delta_rho belong to L^2 be a fixed regularized core. For d>0 set
\[
q_d(y)=\frac{f_\sigma(y-d/2)-f_\sigma(y+d/2)}{d}.
\]
The matched opposite-wedge pair and edge source are
\[
\zeta_d(x,y)=b\,\delta_\rho(x-x_0)q_d(y),\qquad
\zeta_e(x,y)=-b\,\delta_\rho(x-x_0)f_\sigma'(y),
\]
where b=Omega d. This convention fixes the sign: the limit is -f_sigma', not +f_sigma'.

All comparisons require the same b,d,rho,sigma, material, domain, boundary conditions and zero-mode convention. If Omega is fixed as d tends to zero, b=Omega d also tends to zero. The normalized source-shape limit is obtained after factoring out b.

## 2. Theorem VDE-01 — smooth-core dipole quotient

**Theorem.** If f_sigma belongs to W^{3,2}, then
\[
q_d\longrightarrow -f_\sigma'\quad\hbox{strongly in }L^2
\quad(d\downarrow0).
\]
If f_sigma belongs to W^{3,2} (in particular W^{5,2} is sufficient), then
\[
\|q_d+f_\sigma'\|_{L^2}
\leq \frac{d^2}{24}\|f_\sigma'''\|_{L^2}.
\]
Consequently,
\[
\|\zeta_d-\zeta_e\|_{L^2(\mathbb R^2)}
\leq \frac{|b|d^2}{24}
\|\delta_\rho\|_{L^2}\|f_\sigma'''\|_{L^2}.
\]
Thus zeta_d/b converges strongly to -delta_rho f_sigma', with second-order error in d.

**Proof.** The symmetric translation identity is
\[
q_d(y)=-\frac1d\int_{-d/2}^{d/2}f_\sigma'(y+t)\,dt.
\]
Strong continuity of translations in L^2 gives convergence. The symmetric second-order averaging estimate gives
\[
\left\|\frac1d\int_{-d/2}^{d/2}f_\sigma'(\cdot+t)\,dt-f_\sigma'\right\|_2
\leq \frac{d^2}{24}\|f_\sigma'''\|_2.
\]
Fubini gives the tensor-product estimate. QED.

This is a source-level theorem for smooth cores. It does not cover a singular delta core or a renormalized defect energy.

## 3. Airy response estimate (conditional corollary)

Let S map incompatibility to the recovered periodic Airy stress, with the zero Fourier mode fixed. Assume that on the admissible mean-zero source space
\[
\|\mathcal Sg\|_{L^2}\leq C_{\mathcal S}\|g\|_{L^2}.
\]
Then
\[
\|\sigma_d-\sigma_e\|_2
\leq C_{\mathcal S}\frac{|b|d^2}{24}
\|\delta_\rho\|_2\|f_\sigma'''\|_2.
\]
For positive-definite compliance C^{-1} and
\[
E(\sigma)=\frac12\int_\Omega \sigma:C^{-1}:\sigma\,dx,
\]
one has
\[
|E(\sigma_d)-E(\sigma_e)|
\leq \frac12\|C^{-1}\|
\|\sigma_d-\sigma_e\|_2(\|\sigma_d\|_2+\|\sigma_e\|_2).
\]
Hence energy differences are second order in d if stress norms are uniformly bounded. Relative-error convergence additionally requires a positive lower bound on the reference stress/energy. These operator hypotheses are not established here for perforated domains or singular cores.

## 4. Existing periodic Fourier evidence

The merged audit in [PR #450](https://github.com/fabianleonaressi95/theorem/pull/450) implements the two matched sources with periodized Gaussian cores and the same periodic Fourier Airy solver. Its CI report records:

- 140 parameter-sweep rows and 6 fixed-grid small-separation rows;
- maximum Airy compatibility residual 1.96e-16;
- maximum absolute source mean 1.08e-18;
- at d/sigma=1/32, relative stress, strain and energy differences about 1.93e-5, 1.96e-5 and 1.96e-5;
- halving d/sigma in the fixed-grid sequence gives ratios tending to four.

These are numerical verifications for the smooth-core periodic Fourier model, consistent with the source theorem. They are not a proof of discretization convergence, a singular-core limit, or a result on non-periodic domains.

## 5. Comparison with the Cesana–Fabbrini–León Baldelli–Morandotti C0-IPDG framework

Relevant references:

1. P. Cesana, E. Fabbrini, A. A. León Baldelli, M. Morandotti, *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation*, arXiv:2609.29614 (2026), https://arxiv.org/abs/2609.29614.
2. P. Cesana, E. Fabbrini, M. Morandotti, *Variational Formulation of Planar Linearized Elasticity with Incompatible Kinematics*, Journal of Elasticity 157 (2025), Article 71, DOI https://doi.org/10.1007/s10659-025-10161-5.

The finite-element framework addresses a fourth-order Airy boundary-value problem for incompatible plane-strain elasticity and uses a C0 interior-penalty discontinuous Galerkin discretization with local cell problems. It provides the relevant variational/FEM baseline for finite defect systems. The current Fourier experiment is not an implementation of that method.

| Aspect | Current RGS / Fourier audit | Cesana et al. C0-IPDG framework |
|---|---|---|
| Unknown | Periodic Airy potential in Fourier space | Discrete Airy potential in a C0-IPDG variational formulation |
| Geometry | Periodic square torus | Body/domain and defect-cell geometry of the variational model |
| Defects | Smooth periodized Gaussian incompatibility sources | Volterra translational/rotational incompatibilities and local cell problems |
| Discretization | Fourier-spectral grid | Finite elements with continuous interior penalty |
| Boundary conditions | Periodic; zero Fourier mode fixed | Boundary/internal-boundary conditions of the variational problem |
| Current evidence | Reproducible stress/strain/energy sweep; CI green | Published/preprint formulation and its own benchmarks |
| Missing comparison | No independent FEM result | Not yet run on identical dipole/edge data |

**Conclusion.** The approaches address related Airy elasticity problems but are not yet a head-to-head benchmark. Fourier analysis isolates the smooth-core dipole-to-edge asymptotics. C0-IPDG supplies the variational finite-element baseline for finite defects, cell formulas and non-periodic/perforated geometries. It would be incorrect to claim that the Fourier code reproduces, improves on, or validates C0-IPDG.

## 6. Common benchmark protocol

Before comparing results, freeze:

1. **Geometry:** same periodic square if periodic identification is supported by the C0-IPDG formulation; otherwise use a common bounded domain and explicitly matched boundary conditions.
2. **Sources:** identical zeta_d and zeta_e, same b=Omega d, core profiles and source quadrature.
3. **Constitutive law:** identical plane-strain Lamé parameters and Airy sign/normalization.
4. **Gauge:** identical Airy nullspace and mean-stress treatment; report source means explicitly.
5. **Meshes:** refine independently of d; include aligned and non-aligned defect positions; hold physical rho,sigma,d fixed during mesh refinement.
6. **Observables:** relative L2 stress/strain errors, energy difference, Airy residual, equilibrium residual and convergence rates. Compare each method with a refined reference as well as with the other method.
7. **Core effects:** vary core radius and cell size separately; do not conflate d-to-zero, mesh refinement and core removal.
8. **Reproducibility:** publish input data, meshes, quadrature, solver tolerances, output tables and CI logs for both solvers.

Acceptance requires source sign/Burgers matching before solving, each method passing its own residual checks, convergence under mesh refinement at fixed physical parameters, and a decreasing dipole-to-edge difference as d/sigma tends to zero on a sufficiently fine grid. No superiority claim is justified without accuracy at matched degrees of freedom or computational cost.

## 7. Classification and open problems

| Claim | Classification |
|---|---|
| Smooth-core symmetric quotient converges to -f_sigma' in L2 | **Proved** under Theorem VDE-01 |
| Second-order source error bound | **Proved** under W^{3,2} regularity |
| Periodic Fourier stress/energy trend | **Numerically verified** in PR #450 |
| Periodic Airy stress estimate | **Conditional** on the stated operator bound |
| Independent C0-IPDG reproduction | **Open** |
| Displacement Q1/P1 cross-check | **Open** |
| Traction-free/non-periodic boundary extension | **Open** |
| Singular-core limit and renormalized energy | **Open** |
| Mosco or Gamma convergence of defect energies | **Open** |

## 8. Reproducibility

Existing implementation and CI:
- scripts/rgs_volterra_elastic_limit.py
- tests/test_rgs_volterra_elastic_limit.py
- .github/workflows/volterra-elastic-limit.yml
- [PR #450 and CI/artifact links](https://github.com/fabianleonaressi95/theorem/pull/450)

This manuscript formalizes the continuum source limit and records the scope of the comparison. It does not claim that a C0-IPDG solver has been implemented in this repository.
