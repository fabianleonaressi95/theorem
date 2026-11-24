# Q6 golden memory spectrum and the Green–Kubo–Stokes comparison

**Date:** 2026-11-24  
**Status:** [P] conditional spectral identities and convergence criterion; [N] inherited finite-Q6 spectral data; [C] golden hierarchy of relaxation rates and stress weights; [O] derivation of that hierarchy from Q6 dynamics, identification of the stress spectral measure, and hydrodynamic/Stokes matching.

**Relation to existing records:** this is a focused supplement, not a replacement for the microscopic stress derivation in `research/Q6_JITTERBUG_MICROSCOPIC_STRESS_GREEN_KUBO_STOKES_2026-11-24.md`, the central-force construction in `research/Q6_CENTRAL_FORCE_STRAIN_ENERGY_2026-11-24.md`, or T131/T132/T137. It does not repeat their finite-dimensional OU formulas.

## 1. The three objects that must not be conflated

The proposed connection involves three different spectral objects:

1. **Geometric overlap measure** from the TSMR-C-I/Q6 pair automaton. It describes scalar coincidences and close-pair statistics of the golden-coded Q6 walk.
2. **Relaxation spectrum** of a specified dynamical generator. Its positive rates determine how dynamical modes decay.
3. **Stress spectral measure** associated with the actual microscopic stress observable derived from a strain-dependent energy.

Only the third enters the Green–Kubo viscosity. A map
[
	ext{Q6 overlap automaton}longrightarrow
	ext{relaxation generator}longrightarrow
	ext{stress spectral measure}
]
must be constructed and justified before the geometric measure can be used in a transport formula. Equality of supports, dimensions, or algebraic constants would not suffice.

## 2. Spectral form of Green–Kubo and the infrared condition

Let (Pi_{xy}) be the total extensive microscopic shear stress and
[
C_{PiPi}(t)=
langledeltaPi_{xy}(t)deltaPi_{xy}(0)angle_{m eq}.
]
For a reversible equilibrium dynamics with a nonnegative self-adjoint relaxation generator, the spectral theorem gives a positive measure (mu_Pi) on positive relaxation rates such that
[
C_{PiPi}(t)=int_{(0,infty)}e^{-gamma t},dmu_Pi(gamma),
]
provided the stress has been projected off conserved/non-decaying modes. Tonelli's theorem then gives, with extended values allowed,
[
int_0^infty C_{PiPi}(t),dt
=int_{(0,infty)}rac{dmu_Pi(gamma)}{gamma}.
]
Thus the classical shear coefficient is
[
oxed{eta_{m GK}=
rac{1}{k_BT V}int_{(0,infty)}
rac{dmu_Pi(gamma)}{gamma}}
]
for total extensive stress. If the observable is stress density (P_{xy}=Pi_{xy}/V), the equivalent prefactor is (V/(k_BT)).

The exact infrared acceptance conditions are:
- no residual atom at (gamma=0) after conserved-mode projection;
- (intgamma^{-1},dmu_Pi(gamma)<infty);
- uniform control of the small-(gamma) tail in any continuum/refinement limit.

For a density (dmu_Pi(gamma)sim cgamma^{s-1}L(gamma)dgamma) near zero, the inverse-rate integral is finite only when the corresponding integral (int_0^epsilongamma^{s-2}L(gamma)dgamma) converges. In the simple slowly-varying case this requires (s>1); the borderline (s=1) depends on (L).

## 3. Why the finite Q6 graph does not already contain a golden slow hierarchy

For the standard six-cube,
[
operatorname{spec}(L_{Q6})=
0^{(1)},2^{(6)},4^{(15)},6^{(20)},8^{(15)},10^{(6)},12^{(1)}.
]
In the reversible vertex-OU model with drift (gamma_0L_{Q6}), after removing the constant mode, every relaxation rate is at least (2gamma_0). This finite model has a positive spectral gap and finitely many rates. It cannot by itself generate an infinite sequence (gamma_ndownarrow0), a continuous infrared tail, or a scale-free memory law.

The same warning applies to a finite face-cochain Hodge operator when its positive spectrum is bounded away from zero. T131's harmonic frequencies are not relaxation rates, and a harmonic spectrum alone does not produce dissipative decay. A slow hierarchy would require an explicitly defined family of refinements/volumes, a different dynamical generator, or a controlled thermodynamic limit in which rates accumulate at zero.

## 4. Conditional golden hierarchy: an exact summation, not a discovery

Let (arphi=(1+sqrt5)/2). Consider the *candidate* discrete spectral ansatz
[
gamma_n=gamma_0arphi^{-n},qquad
a_n=a_0arphi^{-alpha n},qquad nge0,
]
where (a_n) is the stress-correlation spectral weight at rate (gamma_n). If the stress spectral measure is
[
mu_Pi=sum_{nge0}a_n,delta_{gamma_n},
]
then
[
intrac{dmu_Pi(gamma)}{gamma}
=rac{a_0}{gamma_0}
sum_{nge0}arphi^{-(alpha-1)n}.
]
Consequently,
[
oxed{
eta_{m GK}=
rac{a_0}{gamma_0 k_BT V}
rac{1}{1-arphi^{1-alpha}}
quad	ext{if }alpha>1.
}
]
For the special exponent (alpha=2),
[
rac{1}{1-arphi^{-1}}=arphi^2,
qquad
eta_{m GK}=
rac{a_0arphi^2}{gamma_0 k_BT V}.
]

These are exact consequences of the ansatz. They do **not** show that Q6 has this hierarchy, that (alpha=2), or that the resulting coefficient is a material viscosity. In particular, (alpha) must be estimated from independently generated stress-correlation data or derived from a model; it must not be selected to manufacture a factor (arphi^2).

A falsifiable test is to estimate, over increasing refinement levels,
[
rac{gamma_{n+1}}{gamma_n}
quad	ext{and}quad
rac{a_{n+1}}{a_n}.
]
The proposed golden law predicts limits (arphi^{-1}) and (arphi^{-alpha}), respectively. The special (alpha=2) case predicts (arphi^{-2}) for the weight ratio. Report uncertainty, finite-size drift, and sensitivity to the stress definition.

## 5. Where (pi) enters—and where it does not

For a no-slip sphere of radius (a) translating at speed (U) in an incompressible Newtonian fluid,
[
F=6pieta_{m St}aU,qquad
eta_{m St}=rac{F}{6pi aU}.
]
The factor (pi) is part of the three-dimensional spherical Stokes boundary-value problem; it also occurs in (V_s=4pi a^3/3) and (S_s=4pi a^2). It is not generated by the golden hierarchy above. Conversely, (arphi) does not enter the classical Stokes drag law unless a constitutive/geometric model derives it.

The meaningful comparison is therefore not an asserted identity between (pi) and (arphi), but the dimensionally consistent matching test
[
R_eta(h)=
rac{eta_{m GK}(h)}{eta_{m St}(h)}
longrightarrow1
]
along one and the same controlled family of microscopic models and boundary-value problems. The microscopic stress, volume normalization, temperature, time scaling, boundary conditions, and hydrodynamic limit must be common to numerator and denominator. If the limit is anisotropic, nonlocal, viscoelastic, or has persistent memory, a scalar Stokes viscosity is the wrong target; compare the full constitutive/traction operator instead.

## 6. Acceptance programme

1. **Stress observable:** reuse the same-energy central-force stress in `Q6_CENTRAL_FORCE_STRAIN_ENERGY_2026-11-24.md`; do not substitute a generic linear observable unless derived from that energy.
2. **Dynamics:** specify the generator and equilibrium state. Establish reversibility or state the non-reversible response framework. Identify all conserved modes.
3. **Spectral measure:** compute the stress-weighted measure, not merely the unweighted graph spectrum. Verify positivity and the inverse-rate integrability condition.
4. **Golden test:** test rate and weight ratios on a predeclared refinement sequence; estimate (alpha) without fixing it to 2.
5. **Continuum limit:** prove finite-size and long-time tail bounds sufficient to exchange limits.
6. **Stokes comparison:** derive the same model's boundary traction and velocity response and test (R_eta	o1), or compare the full tensor/nonlocal operator if Newtonian isotropy fails.

## 7. Classification

| Statement | Classification |
|---|---|
| Spectral representation and inverse-rate Green–Kubo formula under reversible self-adjoint dynamics | [P] conditional spectral theorem |
| Positive gap of the finite standard Q6 vertex Laplacian | [P] exact finite-graph fact |
| Finite standard Q6 OU cannot itself yield rates accumulating at zero | [P] consequence of the gap |
| Geometric overlap measure equals the stress spectral measure | [O] no identification established |
| Golden rate/weight hierarchy | [C] falsifiable ansatz |
| (alpha=2) and the resulting (arphi^2) factor | [C] special case, not derived |
| (pi) from the spherical Stokes problem | [P] classical hydrodynamic formula |
| (eta_{m GK}/eta_{m St}	o1) for Q6/RGS/Jitterbug | [O] hydrodynamic and boundary-response limit |

**Conclusion.** The rigorous bridge is the stress spectral measure and its inverse-rate moment. The Q6 overlap automaton may motivate a candidate hierarchy, but it is not yet that measure. The golden factor and the spherical (pi) factor occupy different mathematical roles; their only defensible meeting point is a derived, dimensionally consistent Green–Kubo/Stokes matching limit.

## References within this repository

- `research/Q6_JITTERBUG_MICROSCOPIC_STRESS_GREEN_KUBO_STOKES_2026-11-24.md`: variational stress, quadratic-stress OU benchmark, and conditional Green–Kubo/Stokes theorem.
- `research/Q6_CENTRAL_FORCE_STRAIN_ENERGY_2026-11-24.md`: central-force energy and stress derived from one embedding and one potential.
- `theorems/T131-q6-phonon-phason-green-kubo-transport.md`: physical stress-correlation requirements and phonon/phason distinctions.
- `theorems/T132-coupled-phonon-phason-ou-green-kubo.md`: finite reversible coupled OU benchmark.
- `theorems/Q6_GREEN_KUBO_KRYSTALLO_SCALE_BRIDGE_2026-11-23.md`: exact Q6 inverse-spectral sum and its supergolden obstruction.
- `research/TSMR-FDT_comparative_note.md` and `audits/tsmr_c_iching_overlap_automaton.py`: golden-coded Q6 overlap construction and its separate measure-theoretic status.



## 8. Operator-level bridge to the stress observable

The exact finite pair-transfer operator, its substochastic interpretation, the stress-weighted two-replica statistic, and the missing physical intertwiner are formalized in [From the Q6 pair-overlap automaton to a stress operator](Q6_PAIR_AUTOMATON_TO_STRESS_OPERATOR_2026-11-24.md). The companion audit is `audits/tsmr_q6_stress_transfer_bridge.py`.

The central conclusion is that the pair automaton is not itself a Green–Kubo relaxation generator: it propagates two independent symbolic paths and discards paths leaving its finite enclosure. A physical spectral identification requires a conservative reversible generator, a stress observable derived from the same mechanical energy, and an isometric intertwining map.
