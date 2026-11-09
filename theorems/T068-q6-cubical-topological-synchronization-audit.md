# T068 — Q6 cubical chain complex, Anti-Twin lift, and synchronization benchmark

**Status:** exact finite combinatorial identities plus an implemented exploratory dynamical model. No theorem about hysteresis or industrial material response is claimed.

## 1. Cubical 2-skeleton

Take the 64 binary words in {0,1}^6 as vertices; join words differing in
one coordinate. This gives 192 edges. For each pair of coordinate directions
and each assignment of the remaining four bits, include a square. There are
C(6,2) 2^4 = 240 squares.

Orient edges lexicographically and each square cyclically as (00,10,11,01).
The integer boundary matrices have shapes B1: C1 -> C0 (64 x 192) and
B2: C2 -> C1 (192 x 240). The exact identity B1 B2 = 0 follows because
each square boundary is a closed cycle and is checked entrywise.

The graph cycle rank is 192-63=129. The 240 square boundaries span the
cycle space, rank(B2)=129, so b1 of the 2-skeleton is zero. Since the
truncated complex has no C3, its second Betti number is b2=240-129=111.
These 2-cycles are killed by the omitted 3-cells in the full 6-cube.

## 2. Anti-Twin chain involution

Define c(v)=1-v coordinatewise. It induces signed permutation maps J0,J1,J2
on oriented cells. The finite audit verifies

J0 B1 = B1 J1,
J1 B2 = B2 J2,
J0^2 = J1^2 = J2^2 = I.

Thus bitwise complement is a cellular chain involution on the Q6 cubical
2-skeleton. This is an exact finite combinatorial statement.

## 3. NL and NLT dynamics

For node phases theta in R^64 and edge phases phi in R^192, set

R0 = |64^-1 sum_v exp(i theta_v)|,
R1_down = |64^-1 sum_v exp(i (B1 phi)_v)|,
R1_up = |240^-1 sum_f exp(i (B2^T phi)_f)|.

NL:
theta_dot = omega - sigma R1_down B1 sin(B1^T theta),
phi_dot = omega_link - sigma R0 B1^T sin(B1 phi)
          - sigma B2 sin(B2^T phi).

NLT:
theta_dot = omega - sigma R1_down B1 sin(B1^T theta),
phi_dot = omega_link - sigma R0 R1_up B1^T sin(B1 phi)
          - sigma R1_down B2 sin(B2^T phi).

Sine is componentwise. The original article uses simplicial complexes; the
Q6 implementation substitutes square cells and is therefore a cubical
generalization, not a result already established by the paper.

The source-paper frequency convention is
`omega_i ~ Normal(Omega0, 1/tau0)` and
`omega_tilde_l ~ Normal(Omega1, 1/tau1)`. The numerical implementation
uses the co-rotating node frame, subtracting the common Omega0 drift from
node frequencies; it retains the link-frequency mean Omega1. Independent
random streams are used for frequencies and initial phases, so forward and
backward sweeps with the same seed have exactly the same intrinsic
frequencies. This is necessary for a meaningful branch comparison.

## 4. Industrial hysteresis distinction

Synchronization hysteresis is a bifurcation/continuation phenomenon.
Constitutive hysteresis is path dependence in measured input/output cycles,
for example magnetization, strain or actuator displacement. These are
different observables and require different validation.

Loop-area, RMSE and loading/unloading branch-separation metrics are supplied.
Reference implementations are included for discrete Preisach relays,
Prandtl-Ishlinskii play operators and Bouc-Wen dynamics. Linear weights for
fixed Preisach/PI dictionaries can be fitted by least squares. This is
synthetic/model-level plumbing, not industrial identification or validation.
Jiles-Atherton is deferred to a ferromagnetic B-H data study with a specified
parameter convention. No industrial performance claim is included.

## 5. Verification boundary

Exact: finite cell counts, B1 B2 = 0, Anti-Twin chain-map identities.
Implemented: NL/NLT vector fields on Q6; finite continuation runner; Preisach,
PI and Bouc-Wen reference simulators/fit plumbing; loop metrics.
Implemented: finite multi-seed/multi-dwell sweep study with branch-gap and loop-area summaries plus mean/dispersion plots.
Open: robust Q6 hysteresis under independent initialization/fixed-frequency controls and larger finite-size comparisons,
Open: robust Q6 hysteresis under sweep-rate/seed/initialization controls,
Jiles-Atherton magnetic comparison, experimental data identification,
continuum limits, industrial utility and PSU interpretation.
