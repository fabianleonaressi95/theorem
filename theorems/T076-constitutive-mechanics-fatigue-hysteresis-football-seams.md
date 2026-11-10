# T076 — Constitutive mechanics, damage and cyclic response of the 90 physical football seams

**Status: INTERFACE FRAMEWORK FORMULATED; PANEL-DISCONTINUOUS SEAM TRACE AND ELASTIC PENALTY ASSEMBLER IMPLEMENTED; solver coupling, damage/contact and football-specific identification OPEN.**  
**Depends on:** T073 (football-shell continuum programme), T074 (icosahedral shell combinatorics), T075 (ellipsoid/ovaloid reduction and physical seam network), `models/football_shell.py`.

## 1. Object and scope

Let \\(\\Gamma=\\bigcup_{e=1}^{90}\\Gamma_e\\) be the physical panel-boundary seam network of the repository's truncated-icosahedral football model. The 90 curves join 12 pentagonal and 20 hexagonal panels. They are not interchangeable with the 270 triangle hinges of the fan triangulation. A seam is a material joint whose response depends on its construction: stitching, welding, adhesive bonding, clamping or another joining process.

The present theorem record defines a family of admissible interface models. It does **not** assign measured properties to an unspecified football, nor assume that its seams are welded, glued or sewn with a particular thread.

## 2. Kinematics on a shell

For a seam \\(\\Gamma_e\\) shared by panels \\(P_e^-\\) and \\(P_e^+\\), let \\(y^\\pm\\) denote the traces of the deformed panel maps. Choose a unit tangent \\(s_e\\) to the seam and a local in-surface normal \\(m_e^\\pm\\) on each side. Define the displacement jump
\\[
\\delta_e=y^+-y^-,
\\qquad
\\delta_{s,e}=\\delta_e\\cdot s_e,
\\qquad
\\delta_{n,e}=\\delta_e\\cdot m_e .
\\]
For a shell embedded in \\(\\mathbb R^3\\), the relative displacement also has an out-of-surface component; retain it when the construction permits peel/opening. The local frame and sign convention must be fixed once and transported consistently along each seam.

The panel bulk energy and interface energy are separate:
\\[
\\mathcal E[y,z]=
\\sum_{p=1}^{32}\\int_{P_p}W_p(x,\\nabla_Sy)\\,dA_g+
\\sum_{e=1}^{90}\\int_{\\Gamma_e}\\psi_e(\\delta_e,\\eta_e,z_e; x)\\,ds_g
+\\mathcal E_{\\rm bend}[y].
\\]
Here \\(\\eta_e\\) denotes any relative rotation or director jump required by a shell theory, and \\(z_e\\) collects interface internal variables. The line energy density \\(\\psi_e\\) has units J/m; its derivative with respect to a displacement jump has units N/m. A seam represented by discrete stitches instead requires a sum of stitch energies, or a justified homogenisation to a line density.

## 3. Reversible traction response

Before damage, a simple local elastic interface potential is
\\[
\\psi_e^{(0)}=
\\tfrac12 k_{n,e}\\langle\\delta_{n,e}\\rangle_+^2+
\\tfrac12 k_{s,e}\\delta_{s,e}^2+
\\tfrac12 k_{o,e}\\delta_{o,e}^2+
\\tfrac12 k_{\\theta,e}\\eta_e^2,
\\qquad
t_e=\\partial_{\\delta_e}\\psi_e^{(0)}.
\\]
The positive-part convention \\(\\langle r\\rangle_+=\\max(r,0)\\) is appropriate only for a tension-carrying interface that does not transmit tensile normal traction after opening; compressive contact must be supplied separately. The coefficients are effective line stiffnesses and must be dimensioned and calibrated for the selected seam construction. This quadratic law is a small-displacement baseline, not a universal seam law.

For a perfectly bonded interface, impose the appropriate displacement/rotation continuity as a constraint. A finite-stiffness spring is not mathematically identical to perfect bonding except in a specified limiting regime.

## 4. Cohesive opening, peel and mixed-mode damage

For a bonded or welded seam for which cohesive separation is physically appropriate, introduce a scalar damage variable \\(d_e\\in[0,1]\\), non-decreasing in time, and for example
\\[
\\psi_e=(1-d_e)\\psi_e^{(0)},\\qquad
\\dot d_e\\geq0.
\\]
A mixed-mode initiation condition can be written in normalized form
\\[
\\left(\\frac{\\langle t_n\\rangle}{t_n^0}\\right)^2+
\\left(\\frac{t_s}{t_s^0}\\right)^2+
\\left(\\frac{t_o}{t_o^0}\\right)^2=1,
\\]
with subsequent evolution governed by a calibrated fracture-energy criterion. The critical energies \\(G_{Ic},G_{IIc},G_{IIIc}\\), peak tractions and mixed-mode interaction parameter are material/process parameters, not values derivable from football geometry. A bilinear or exponential traction–separation curve is a model choice; its area must match the measured fracture energy.

Do not use a cohesive law to represent a purely mechanical sewn seam without evidence that it captures the stitch/thread load path. Thread rupture, needle-hole tear-out, stitch pull-out and fabric tearing may require discrete stitch elements or a calibrated effective seam law.

## 5. Contact, clamping and frictional slip

For a seam whose load transfer is due to contact or clamping, use unilateral contact variables rather than an adhesive cohesive potential. With gap (g_n), compressive contact pressure \\(\\lambda_n\\), and tangential traction \\(\\tau_e\\), the ideal Signorini/Coulomb conditions are
\\[
g_n\\geq0,\\quad \\lambda_n\\geq0,\\quad g_n\\lambda_n=0,
\\qquad
\\|\\tau_e\\|\\leq\\mu_e\\lambda_n.
\\]
During sliding, the frictional dissipation is non-negative. A clamped seam may additionally need bolt/clamp compliance, pre-load loss and local bearing/tear-out. These effects cannot be inferred from a welded-seam test.

## 6. Fatigue and hysteresis under cyclic loading

Cyclic loading is not represented by a static strength number. The state may include accumulated damage \\(d_e(N)\\), residual slip \\(r_e(N)\\), and a hysteretic internal variable \\(q_e\\). A general thermodynamically admissible formulation requires
\\[
\\mathcal D_e=t_e\\cdot\\dot\\delta_e-
\\dot\\psi_e\\geq0
\\]
(after including all internal-variable power terms consistently). For cycle-based degradation one may write only the abstract evolution
\\[
d_e^{N+1}=d_e^N+
\\mathcal F_e(\\Delta G_e,R_e,N,T,\\mathrm{RH},\\ldots),
\\qquad d_e^{N+1}\\geq d_e^N,
\\]
where \\(\\Delta G_e\\) is a cycle energy-release measure and \\(R_e\\) a load ratio. The function \\(\\mathcal F_e\\) must be identified from cyclic tests; a Paris-type law is not to be imported automatically from bulk fracture into textile seams.

Hysteresis can be represented by a rate-independent internal variable or a viscoelastic/viscoplastic law, depending on observed rate, frequency and temperature effects. The loop area
\\[
W_{\\rm diss}^{(N)}=\\oint_{\\text{cycle }N} t_e\\cdot d\\delta_e
\\]
is an observable energy-loss measure. Its nonzero value must be measured; it must not be inserted merely because the model is intended to have memory.

## 7. Junctions and seam network coupling

At each multi-panel junction \\(v\\), enforce force and moment balance using the incident seam resultants and panel boundary tractions:
\\[
\\sum_{e\\ni v} f_{e,v}+\\sum_{p\\ni v} f_{p,v}=0,
\\qquad
\\sum_{e\\ni v} m_{e,v}+\\sum_{p\\ni v} m_{p,v}=0,
\\]
with signs and admissible moments determined by the shell discretisation. A junction may need its own local compliance or reinforcement variable; do not distribute a junction defect uniformly over adjacent seams without a model.

## 8. What the literature actually supports

1. **Membrane engineering guidance.** Stranghöner et al., JRC 132615 (2023), DOI 10.2760/24763, treats seams as structural joints, distinguishes seam resistance from parent-fabric tensile/tear/adhesion properties, and requires experimental seam resistance characterisation. It also distinguishes sewn joints in uncoated fabrics from welded/clamped joints in coated fabrics.
2. **Welded PVDF seams.** Liu et al. (2026), *Thin-Walled Structures* 222, 114501, DOI 10.1016/j.tws.2026.114501, report 140 parent-membrane and 430 weld-seam specimens; tensile rupture and peeling are distinct failure modes, and seam strength depends on membrane density, seam width and direction.
3. **Off-axis welded seams.** Yu et al. (2025), *Journal of Industrial Textiles*, DOI 10.1177/15589250251342853, test the effects of off-axis angle and weld length.
4. **Cyclic welded seams.** Zhao et al., “Study on tensile performance of welded seams of PVC coated fabric membrane under uniaxial cyclic load”, DOI 10.1177/15280837241300935, report cyclic changes in modulus, ratcheting/residual strain and dissipated strain energy. This supports testing hysteresis and degradation in welded seams, not assuming the same parameters for sewn seams.
5. **Cohesive-zone methods.** The traction–separation and mixed-mode damage framework is established in interface/fracture mechanics; its parameters and even its suitability remain construction-specific. Cohesive models are not a substitute for identifying the actual failure mechanism.

These sources establish the relevance of seam-specific strength, peel, off-axis response and cyclic degradation. They do not supply parameters for the user's football.

## 9. Minimum experimental programme to identify the football seam law

Before numerical calibration, identify the actual panel material and joining process, seam geometry, stitch/weld/adhesive details, manufacturing direction and conditioning. Then sample representative seam families and junctions.

| Test | Primary identification | Required observations |
|---|---|---|
| Monotonic seam tension, warp/weft and off-axis | line stiffness, peak load, ultimate extension | force–displacement, failure location/mode |
| Peel/opening (where applicable) | opening stiffness and Mode-I resistance | peel force, separation path |
| Lap shear (where applicable) | shear stiffness and Mode-II resistance | slip, debonding, rupture |
| Cyclic tension/shear | hysteresis, ratcheting, residual slip, stiffness loss | full loops over cycle count |
| Fatigue to failure | life distribution and damage law | load ratio, amplitude, cycles, failure mode |
| Temperature/humidity conditioning | environmental dependence | conditioned vs reference response |
| Junction coupon test | local concentration and junction compliance | crack initiation and load redistribution |

Use replicate specimens and report scatter/quantiles; do not fit a deterministic design strength to a single coupon. Preserve separate datasets for seam construction, orientation and panel type. A real scan and material coupons are needed before claims about the actual football's ovaloid mechanics or industrial durability.

## 10. Discrete implementation plan

The current `models/football_shell.py` line reinforcement and seam bending multiplier are not a general cohesive/contact/fatigue model. The next implementation should proceed in gates:

- **Gate A — topology audit:** verify the 90 physical seam edges and junction incidence independently of the 270 fan-triangulation hinges.
- **Gate B1 — axial seam reinforcement:** implemented separately on the 90 physical seam edges; tests cover symmetry, semidefiniteness, rigid-translation invariance and edgewise energy equivalence.\n- **Gate B2 — discontinuous interface kinematics:** implemented by `build_seam_discontinuous_mesh`, which duplicates panel-local traces and returns 90 pairs of side-specific seam segments. `assemble_seam_jump_stiffness` assembles the consistent P1 line penalty for the full vector jump, with energy \\(\\frac12\\kappa\\int_{\\Gamma_e}|u^+-u^-|^2ds\\). Tests cover coincident reference traces, topology, symmetry, positive semidefiniteness and the rigid-translation kernel. An independent local reconstruction of the repository's truncated-icosahedral mesh reproduced 212 panel-local nodes, 180 triangles, 90 seam pairs; the assembled 636×636 penalty matrix was symmetric, had minimum eigenvalue about \\(-1.54\\times10^{-14}\\) (roundoff), and annihilated rigid translations to about \\(7.5\\times10^{-15}\\). This is an independent numerical cross-check of the assembly formula, not a run of the repository's pytest suite.\n- **Important boundary:** these are assembly primitives and regression tests, not yet a complete coupled shell solve. The existing conforming CST/hinge solver has not yet been rewritten to assemble panel bulk and bending terms on the duplicated degrees of freedom. Therefore the interface penalty has not yet been exercised in a pressure-loaded global equilibrium problem.
- **Gate C — construction-specific branch:** implement either (i) cohesive opening/damage, (ii) discrete stitch/thread law, or (iii) contact/friction/clamp law only after construction is identified.
- **Gate D — cyclic state:** add internal variables and cycle update only after cyclic coupon data exist; test non-negative dissipation and mesh/time-step objectivity.
- **Gate E — calibration/validation:** fit on one subset of coupons and validate on held-out seam orientations, widths and junction tests; report uncertainty and failure-mode confusion matrix.

No arbitrary seam stiffness, damage threshold, fatigue exponent or hysteresis coefficient should be selected to improve agreement with the global ellipsoid fit.

## 11. Status ledger

| Claim | Status |
|---|---|
| The model has 90 physical panel-boundary seams, distinct from 270 triangulation hinges | Implemented combinatorics; verify against source/test before changing topology |
| Seams require construction-specific mechanical characterisation | Supported by engineering literature |
| Cohesive traction–separation is an established model class for bonded/welded interfaces | Established method; applicability is conditional |
| Contact/Coulomb laws are appropriate for contact/clamped interfaces | Established method; parameters/application conditional |
| Fatigue/hysteresis can matter for cyclically loaded welded seams | Experimentally supported in coated membrane literature |
| Actual football seam technology and parameters | Unknown/open |
| Sewn seam thread pull-out law for this football | Open; requires construction details and tests |
| Energy-consistent axial spring on 90 physical seam edges | Implemented in Gate B1; regression tests added, execution not yet confirmed |\n| Panel-discontinuous traces and consistent vector-jump penalty assembler | Implemented as assembly primitives; solver coupling and execution remain unverified |\n| Full pressure-loaded shell solve with duplicated seam traces | Open; requires remapping bulk CST and hinge terms and junction constraints |\n| Football-specific damage/fatigue/hysteresis law | Open; requires cyclic tests |
| Seam-aware ellipsoid/ovaloid numerical calibration | Open |
| Industrial durability or certification | Not established |

## References

- Stranghöner et al. (2023), *Prospect for European Guidance for the Structural Design of Tensile Membrane Structures*, JRC 132615, DOI: 10.2760/24763.
- Liu et al. (2026), *Tensile strength evaluation for the weld seams of PVDF-coated fabrics membrane*, *Thin-Walled Structures* 222, 114501, DOI: 10.1016/j.tws.2026.114501.
- Yu et al. (2025), *Experimental study on mechanical properties and failure mechanisms of coated fabrics with different welding lengths*, DOI: 10.1177/15589250251342853.
- Zhao et al., *Study on tensile performance of welded seams of PVC coated fabric membrane under uniaxial cyclic load*, DOI: 10.1177/15280837241300935.
- See also `audits/2026-11-10_physical_seams_interfaces_literature_audit.md` for the broader interface/defect literature audit.
