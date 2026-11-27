# Shape–Field: electrostatic FEM research protocol (CADFEM reference)

**Status:** OPEN — research protocol, no simulation results yet.
**Date:** 2026-11-26.
**Canonical location:** `theorem/docs/` (provisional — see §10 ownership note).

## 1. Reference

- René Fuger, *Understanding electrical discharges using field simulations*, CADFEM Blog, 10 April 2026.
  URL: https://blog.cadfem.net/en/understanding-electrical-discharges-using-field-simulations
- Role: motivation and methodology reference for electrostatic FEM treatment of electrode geometries relevant to electrical discharge inception. It is a practitioner article, **not** a peer-reviewed source; quantitative claims taken from it must be re-derived, not cited as established results.

## 2. Scientific objectives

1. Establish an electrostatic FEM baseline for convergent electrode geometries.
2. Compare wedge, opposed-tip, triangular and circular configurations.
3. Sweep convergence angles and electrode curvature radii.
4. Calculate electric potential, field strength and electrostatic energy density.
5. Identify local field maxima and compare them with geometric predictions.
6. Implement an inception-voltage estimation stage using appropriate gas-discharge physics.
7. Keep plasma breakdown and transient arc dynamics as a separate advanced model (out of scope here).
8. Investigate Maxwell–Fluent coupling, Joule heating, gas buoyancy and Lorentz forces (future stage).
9. Define separate metrics for electromagnetic energy transport and fluid vorticity.

## 3. Mathematical model

Quasi-static electrostatics in the gas gap (valid while displacement current ≪ conduction, i.e. before breakdown):

- Potential: `∇·(ε ∇φ) = 0` with `ε = ε0 εr` (air: εr = 1).
- Field: `E = −∇φ`; energy density `u = ½ ε |E|²`; total energy `U = ∫ u dV`.
- Field enhancement factor `β = |E|_max / |E|_avg` over the gap, where `|E|_avg = V/d` for planar reference.
- Boundary conditions: Dirichlet `φ = V` on live electrodes, `φ = 0` on ground/return electrode, homogeneous Neumann `∂φ/∂n = 0` on symmetry planes and outer boundaries placed far enough that the field there is verified negligible (domain-independence test required).
- Conductors are modeled as equipotential boundaries (perfect-conductor approximation). **Mathematical boundary surfaces are not physical conductors**: edge singularities at sharp corners/edges are mesh-dependent and must be reported as such, never interpreted as physical field divergence.

## 4. Geometries under study

| ID | Geometry | Control parameters |
|---|---|---|
| G1 | Wedge / conical convergent electrode vs. plane | half-angle θ, tip radius r, gap d |
| G2 | Opposed tips (sphere–sphere or sphere–plane) | radii R1, R2, separation d |
| G3 | Triangular electrode vs. plane | apex angle, edge radius, orientation |
| G4 | Circular disk / annulus vs. plane | radius R, thickness t, gap d |

All geometries are axisymmetric where possible (2D axisymmetric FEM); triangular and asymmetric cases fall back to 3D with documented mesh-size justification.

## 5. FEM simulation specification

- Solver: open-source preferred (FEniCSx / Firedrake) or equivalent; choice and version recorded.
- Mesh: graded refinement toward tips/edges with documented minimum element size `h_min`; at least 3 refinement levels for every reported quantity.
- Quantities exported per run: `φ`, `|E|`, `u`, `β`, `E_max` location, total `U`.
- Every run records: geometry parameters, mesh statistics, solver tolerance, wall time, domain size, and a domain-independence check (outer boundary moved ×2 → reported drift in `E_max`).

## 6. Parameter sweeps

- Convergence angle θ (wedge): e.g. 10°–170°.
- Tip curvature radius r: logarithmic sweep down to the smallest resolvable value; sharp-edge limit flagged separately.
- Gap d and applied voltage V (V affects only linear scaling in the electrostatic stage — inception stage is where V enters nonlinearly).
- Electrode spacing/orientation for opposed-tip cases.

## 7. Inception-voltage estimation stage

Separate module, clearly labeled **estimate**, using standard gas-discharge criteria:

- Effective ionization coefficient `α_eff = α(E/N) − η(E/N)` for the chosen gas (start with dry air, T = 293 K, p = 1013 hPa; parameters from published swarm data — source and fit recorded).
-Streamer/inception criterion of the form `∫ α_eff dl ≈ K` along field lines from the high-field region, with K documented (typical literature values ~10–40 depending on convention).
- Cross-check against the Paschen curve for uniform fields; report deviation as a function of β.
- Output: `V_inception(geometry)` per configuration, with uncertainty from mesh and α_eff fit propagated.

**Explicitly out of scope:** self-consistent plasma fluid models, streamer propagation, arc dynamics, thermal ionization transients. Those require a separate model specification before any claim.

## 8. Verification tests (pre-registered)

1. Parallel-plate capacitor: `|E| = V/d` uniform, `U = ½ ε V² A/d` — tolerance ≤ 1e-6 relative on fine mesh.
2. Isolated sphere in uniform field: `β = 3` at surface — tolerance ≤ 1e-3.
3. Sphere-plane / sphere-sphere literature enhancement factors where available.
4. Mesh convergence: `|E|_max` vs `h_min` must show asymptotic behavior; divergence at sharp edges documented, not hidden.
5. Domain independence: outer-boundary doubling changes `E_max` < 1%.
6. Energy consistency: `U` from volume integral vs. `½ ∫ φ σ dS` boundary form agree.

## 9. Falsifiable predictions

- P1: For fixed gap and voltage, `β` increases monotonically as tip radius `r → 0` for G1/G2/G3, saturating only at mesh resolution.
- P2: `V_inception` decreases with increasing `β` at fixed gap; the product `β · V_inception` is approximately constant across geometries at fixed gas conditions (to be tested, not assumed).
- P3: Circular disk (G4) shows lower `β` than triangular apex (G3) at equal minimum radius of curvature.
- P4: For very obtuse wedge angles (θ → 180°), `β → 1` (plane limit).

Each prediction states the observable, the expected direction/magnitude, and the measurement that would falsify it.

## 10. Experimental validation requirements

- Field mapping: electrostatic field-mill or Kelvin-probe scans near tips; compare measured `E_max` position and magnitude with FEM (allowing for probe resolution).
- Inception voltage: controlled-air measurements with documented pressure/temperature/humidity; compare with §7 estimates within stated uncertainty.
- **No unsafe high-voltage experiments**: all work at reduced scale or with appropriate lab protection; no mains-voltage or stored-energy hazards.
- Simulation images are visualization aids only — they are **not** experimental validation.

## 11. Future coupling stage (specification only)

- Maxwell–Fluent (or equivalent FEM–CFD) coupling for Joule heating in the pre-breakdown and post-inception regimes.
- Buoyancy of hot gas and Lorentz forces `f = J × B` as separate source terms.
- **Distinct metrics required:** electromagnetic energy transport (`S = E × H`, Poynting flux, Joule dissipation `J·E`) vs. fluid vorticity (`ω = ∇ × u`, enstrophy). These must never be conflated: field concentration is not energy generation; plasma motion is not electromagnetic energy circulation.

## 12. Scientific safeguards (binding)

- Geometry concentrates field; it does not create energy. No claim of energy generation from shape alone.
- Field concentration ≠ energy generation; plasma motion ≠ EM energy circulation.
- Mathematical boundary surfaces ≠ physical conductors (edge singularities are numerical artifacts until regularized by a physical radius).
- Simulation outputs are numerical predictions, not experimental validation.
- All material parameters, boundary conditions, mesh and uncertainty documented per run (§5).
- No unsafe high-voltage experiments (§10).

## 13. Connection to RGS–PRISM — EXPLORATORY ONLY

The RGS geometric carrier and discrete coframe work (theorem #321 merged; #476 open) provides a possible geometric language for field-line/coframe structures. Any link between the discrete RGS carrier and electrode field geometry is **exploratory**: no claim is made that RGS–PRISM predicts discharge behavior, and no RGS parameter may be tuned to reproduce FEM results. Cross-references, if any, will be documented separately and labeled HYPOTHESIS.

## 14. Ownership and status

- Canonical repo for this protocol: **`theorem`** (`docs/`), provisionally — it is a research protocol, not yet simulation software or data. If/when FEM code and datasets exist, they belong in a dedicated application repo (per MASTER_PROJECT_REGISTRY.md ownership rules); this document would then be cited, not duplicated.
- Registry updates: `docs/project/OPEN_WORKSTREAMS.md` and `SCIENTIFIC_STATUS_MATRIX.md` updated in the same PR to map Shape–Field from UNMAPPED to this document.
- Status label: **OPEN** (protocol only). Nothing here is SOFTWARE-VERIFIED until §8 tests pass on committed code.
