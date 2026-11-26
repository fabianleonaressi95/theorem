# Physical seams and interfaces — literature audit (10 November 2026)

## Scope and terminology

A sewn seam in a textile shell is a **physical line joint** between separate panel pieces. In mechanics it is represented as an interface with its own traction–separation, slip, peel, rotational and failure response. In condensed-matter physics, related mathematical objects include grain boundaries, phase/domain walls, dislocations, disconnections and line defects. These are not all literally textile seams and must not be conflated: the transferable content is the mathematics of interfaces, defects, energy concentration and transmission/jump laws.

## Direct evidence: membrane engineering

**Stranghöner et al. (2023), JRC 132615, EUR 31430 EN**, *Prospect for European Guidance for the Structural Design of Tensile Membrane Structures*, DOI 10.2760/24763.

The JRC report explicitly defines membrane joints and says the joint between two membranes is carried out by seams (pp. 140–141). For uncoated fabrics the joints are sewn; for coated fabrics common seam types include welding and clamping. It states that seam resistance must be determined experimentally by tensile tests and treated statistically (5% fractile in the proposed design outlook). It also distinguishes seam strength from base-material tensile strength, tear strength and adhesion. This is direct engineering evidence that a seam is a mechanically designed and tested component, not a geometric marking.

The report also discusses seam width and strength, temperature dependence, seam crossings and fabrication controls (around pp. 159 onward). The correct material law depends on the joining technology: stitching, welding, clamping, lacing and adhesive bonding are distinct joint classes.

## Experimental seam response

**Liu et al. (2026), Thin-Walled Structures 222, 114501**, *Tensile strength evaluation for the weld seams of PVDF-coated fabrics membrane*, DOI 10.1016/j.tws.2026.114501.

The study reports tensile testing of 140 membrane specimens and 430 welded-seam specimens. It classifies direct tensile fracture and peeling failure and reports that seam failure can govern even when the parent membrane is stronger. This supports including seam-specific failure modes and not representing the joint solely by the bulk panel modulus.

**Yu et al. (2025), Journal of Industrial Textiles**, *Experimental study on mechanical properties and failure mechanisms of coated fabrics with different welding lengths*, DOI 10.1177/15589250251342853.

Off-axis tensile behaviour is examined as a function of weld length and loading angle. This is relevant because the football shell loads seams in multidirectional states, not just uniaxial tension.

## Interface mechanics and cohesive laws

**A review on failure theories and simulation models for adhesive joints** (2021/2022), *Journal of Adhesion*, DOI 10.1080/00218464.2021.1941903.

The review compares linear elastic fracture mechanics, virtual crack closure, finite fracture mechanics, cohesive-zone models, progressive damage and probabilistic approaches. These are candidate frameworks for adhesive/bonded interfaces, but the appropriate one for a sewn football seam must be selected from its actual construction and tests.

**A. F. Bower, Applied Mechanics of Solids, §3.13, “Constitutive models for contacting surfaces and interfaces in solids.”**

This source distinguishes cohesive-zone laws (interface separation/adhesion) from contact/friction laws (normal and tangential interaction during sliding). It is a useful mechanics reference for formulating interface tractions as functions of relative displacement.

## Condensed-matter physics: interfaces and line defects

**Han, Thomas & Srolovitz (2018), Progress in Materials Science 98, 386–476**, *Grain-boundary kinetics: A unified approach*, DOI 10.1016/j.pmatsci.2018.05.004.

Grain boundaries are internal interfaces in polycrystals. Their motion can be described using disconnections, line defects constrained to interfaces with both step and dislocation character. This demonstrates that physical interfaces can carry their own defect degrees of freedom and kinetics.

**Clayton (2018), “Mesoscale models of interface mechanics in crystalline solids: a review.”**

The review distinguishes sharp-interface, continuum-defect and diffuse-interface models for grain boundaries and twin boundaries, and discusses cohesive-zone and continuum-damage descriptions of failure interfaces.

**Kleman & Friedel (2008), Reviews of Modern Physics 80, 61**, *Disclinations, dislocations, and continuous defects: A reappraisal*, DOI 10.1103/RevModPhys.80.61.

A foundational review of line and continuous defects in ordered media. These are not textile seams; they are physically distinct defects with elastic and topological content.

**Nataf et al. (2020), Nature Reviews Physics 2, 634–648**, *Domain-wall engineering and topological defects in ferroelectric and ferroelastic materials*, DOI 10.1038/s42254-020-0235-z.

Ferroelectric/ferroelastic domain walls are two-dimensional defects separating ordered domains; they can host distinct polarization, conductivity and lower-dimensional defects. This is an example where an interface is itself an active physical object rather than a passive boundary.

## Mathematical translation to the football shell

Let each panel be a two-dimensional material region (P_p) on a reference ovaloid ((S,g)), and let (Gamma_e) denote the physical seam curve joining adjacent panels. The shell energy should have the structure
[
mathcal E[y]=
sum_pint_{P_p}W_p(x,
abla_S y),dA_g
+sum_eint_{Gamma_e}psi_e(x,[y],[
abla_Sy],z_e),ds_g
+mathcal E_{m bend}[y].
]
Here (z_e) may encode internal seam variables (stitch/thread state, damage, slip, opening, hysteresis). This is a general interface-energy template, not a constitutive law identified for the user's ball.

For a cohesive seam, a traction–separation law may be written
[
t_e=partial_deltapsi_e(delta,z_e),qquad
delta=[y]_{Gamma_e},
]
with irreversible damage/history variables where supported by tests. For a stitched textile, a homogenised seam law may instead require thread pull-out, stitch geometry, fabric anisotropy, seam allowance and cyclic loading. For welded seams, peel and tensile modes and weld width/temperature/process parameters are relevant. For a clamped joint, contact, friction and bolt/clamp preload may dominate.

The present repository model only includes an optional axial line spring on the 90 physical seam edges and a separate seam bending multiplier. It does **not** yet contain a measured traction–separation law, peel law, cohesive damage, stitch/thread pull-out, frictional slip or hysteretic internal variable. Those must not be claimed as implemented.

## Consequences for T075

1. Retain the 90 physical seams as first-class interfaces throughout ellipsoid/ovaloid reduction.
2. Do not merge physical seams with the 270 triangular hinges used for numerical bending.
3. Give each seam its own geometry, material/process class, tangent direction, local frame and constitutive parameters.
4. Calibrate seam laws with seam-specific tests; use parent-material tests separately.
5. Distinguish tensile, shear, peel, opening, bending/rotation, cyclic fatigue and failure.
6. Only homogenise seam behaviour after defining the scaling regime and proving/validating the effective interface law.
7. Treat the seam network as a metric-measure graph embedded in the ovaloid, coupled to panel PDEs. Its vertices (junctions/crossings) may require separate junction conditions.
8. Keep condensed-matter analogies at the level of interface mathematics; do not identify a textile seam with a grain boundary or a ferroelectric domain wall.

## Status

| Claim | Status |
|---|---|
| Seams are structural membrane joints with independently tested resistance | Directly supported by JRC report |
| Seam response depends on joining method, direction, width and temperature | Supported by engineering literature |
| Interfaces and line defects carry independent physical degrees of freedom in condensed matter | Established in cited reviews |
| Cohesive/contact/interface laws are candidate mathematical frameworks | Established framework; choice is system-dependent |
| Actual football seam constitutive law and parameters | Open; requires construction details and tests |
| Seam-aware ellipsoid/ovaloid continuum limit | Open |
