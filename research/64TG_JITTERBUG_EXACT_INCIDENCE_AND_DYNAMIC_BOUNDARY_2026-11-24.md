# 64-TG ↔ Jitterbug: exact vertex-set congruence, incidence mismatch and dynamic obstruction

**Date:** 2026-11-24  
**Issues:** #398, #401 (with dependencies #399–#400)  
**Classification:** [A] exact geometric congruence of a distinguished 12-vertex set; [A] exact incidence mismatch between the 64-TG FCC edge graph and the Jitterbug rods; [N] dynamic Jitterbug path independently constraint-audited; [O] full 64-TG dynamic extension and Vesica-phase incidence.

## 1. The exact identification already present

The FCC/D3 reconstruction in `data/64tg_fcc_coordinates.json` uses
\[
x(n)=\frac{a}{2\sqrt2}n,\qquad
n\in\mathbb Z^3,\quad -2\le n_i\le2,\quad n_1+n_2+n_3\equiv0\pmod2.
\]
Its cuboctahedral 12-vertex subset is
\[
C_{64} = \{n:\{|n_1|,|n_2|,|n_3|\}=\{2,2,0\}\}.
\]
The standard Jitterbug audit uses the unit-edge cuboctahedron
\[
C_J=\left\{\frac1{\sqrt2}(s_1,s_2,0)
\text{ and coordinate permutations}:s_1,s_2\in\{\pm1\}\right\}.
\]
The map
\[
\boxed{\;\Phi_0(x(n))=\frac{n}{2\sqrt2}\;}
\]
is therefore an exact bijection from the 12 cuboctahedral FCC vertices to the 12 unit Jitterbug joints when the reference edge scale is set to \(a=1\). For general \(a\), the physical map is \(x(n)\mapsto n/2\) in dimensionless Jitterbug coordinates, i.e. divide physical coordinates by \(a\).

It preserves all pairwise Euclidean distances after this declared scale normalization. The Jitterbug rods have length \\(a\\), whereas the stored FCC graph edges have length \\(a/2\\); these are different incidence structures.

**Correction from the direct incidence audit (24 November 2026).** The stored 64-TG FCC edge list uses integer-coordinate squared distance 2 (physical edge length a/2). Each of the 24 Jitterbug rod pairs in the same 12-point set has integer-coordinate squared distance 8 (physical length a). Direct comparison against all 240 stored FCC edges gives **0 matches out of 24**. Thus the 12-point geometric congruence is exact, but the rods are not edges of the stored 64-TG graph. The previous draft's claim of an initial-pose subcomplex isomorphism is withdrawn.

## 2. Eight panels: explicit incidence map

Index the eight triangular faces by
\(\varepsilon=(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{\pm1\}^3\).
Their ordered vertices are
\[
v_{\varepsilon,0}=\frac1{\sqrt2}(\varepsilon_1,\varepsilon_2,0),\quad
v_{\varepsilon,1}=\frac1{\sqrt2}(\varepsilon_1,0,\varepsilon_3),\quad
v_{\varepsilon,2}=\frac1{\sqrt2}(0,\varepsilon_2,\varepsilon_3).
\]
In FCC integer coordinates these are simply
\[
n_{\varepsilon,0}=(2\varepsilon_1,2\varepsilon_2,0),\quad
n_{\varepsilon,1}=(2\varepsilon_1,0,2\varepsilon_3),\quad
n_{\varepsilon,2}=(0,2\varepsilon_2,2\varepsilon_3).
\]
Thus the eight ordered triples are explicit as Jitterbug panel data on the matched 12-point set. They are not 2-cells of the FCC/D3 tetrahedral cellulation merely by virtue of sharing those coordinates. The eight triangles split into two chiral tetrahedral families by
\(\varepsilon_1\varepsilon_2\varepsilon_3=+1\) and (-1\), matching the existing Jitterbug audit's \(T_+\) and \(T_-\) grouping, subject to the declared vertex-order convention.

Within the Jitterbug linkage, the 8 panels are the 8 triangular faces of the cuboctahedron, the 24 rods are its cuboctahedral edges, and the 12 points are its joints. This is the standard Jitterbug incidence structure, imported as a separate linkage on a geometrically congruent 12-point subset. It is not the incidence structure induced by the 64-TG FCC graph. The remaining 6 square faces are flexible quadrilateral openings, not additional rigid panels.

**Important incidence distinction:** two triangular panels whose sign labels differ in one coordinate share one joint (the panel-label contact graph is \(Q_3\)); they do not share a full rod. A rod belongs to one triangular panel and one square opening in the cuboctahedral surface. Do not use \(Q_3\) as the hinge/rod graph.

## 3. Frame construction is exact at the reference pose

For each ordered panel triple \((p_0,p_1,p_2)\), define
\[
c_\varepsilon=\frac{p_0+p_1+p_2}{3},\quad
e_{1,\varepsilon}=\frac{p_1-p_0}{a},\quad
n_\varepsilon=
\frac{(p_1-p_0)\times(p_2-p_0)}
{\|(p_1-p_0)\times(p_2-p_0)\|},\quad
e_{2,\varepsilon}=n_\varepsilon\times e_{1,\varepsilon}.
\]
Since every panel edge has length \(a\), \(e_1\) is unit. The frame matrix
\(R_\varepsilon=[e_1\ e_2\ n]\) is in \(SO(3)\) for the displayed ordering. Reversing two vertex labels reverses the normal and must also reverse the coil winding sign if the physical winding is unchanged.

For a later Jitterbug configuration, fit each panel's three ordered vertices by a proper Kabsch rotation (determinant +1) and translation. The existing one-panel coil implementation already uses this procedure for one face. The eight-panel frame extension is a direct repetition of that method, but must report each panel's residual and orientation continuity.

## 4. What the dynamic Jitterbug audit contributes

The existing `audits/jitterbug_gray_kinematics.py` independently constructs the 12 joints as the orbit of a tetrahedral group of order 12 and solves the two edge-orbit constraints
\[
w^TQ_1w=1,\qquad w^TQ_2w=1.
\]
The resulting one-dimensional branch is continued numerically. The verified report records:
- maximum edge-length residual \(2.2\times10^{-16}\);
- all 12 vertex paths planar to about \(10^{-17}\), with ellipse semiaxes \(1\) and \(1/\sqrt3\);
- opposite rotations of the two four-panel chiral families;
- \(V(\gamma)=\sqrt{2/3}L\cos\gamma\) to about \(3.9\times10^{-16}\);
- the icosahedral configuration at the predicted angle;
- collapse to the octahedral endpoint.

This is a strong dynamic certificate for the 12-joint/24-rod Jitterbug framework and its rigid triangular faces. It is not yet a dynamic map of the other 51 FCC vertices, the 64 tetrahedra, 14 octahedra and 24 pyramids.

## 5. The exact obstruction to calling it a full 64-TG immersion

The static 64-TG contains 63 vertices, 240 edges and 64 tetrahedral cells. The Jitterbug linkage has 12 joints and 24 rods, together with eight rigid triangular panels. The exact map above identifies only a distinguished 12-point subset geometrically congruent to the Jitterbug joints. The 24 Jitterbug rods and eight panel triples are additional linkage incidence data; they are not inherited from the 64-TG FCC edge/cell incidence.

There is no canonical injective map from all 63 64-TG vertices to the 12 Jitterbug joints. Nor does the static FCC coordinate set prescribe where its interior vertices should move while preserving all 64 tetrahedra and the 14/24 cavity geometry. Such an extension would require additional degrees of freedom, a cellwise deformation rule, and compatibility constraints; it cannot be inferred from the Jitterbug path alone.

Consequently:
- **proved exactly:** geometric bijection of the 12 distinguished FCC points with the 12 Jitterbug joints, with all pairwise distances preserved under scale normalization;
- **proved exactly:** incidence mismatch — the 24 Jitterbug rods are not FCC edges in the stored 64-TG graph (0/24 matches; squared-distance conventions 8 versus 2);
- **numerically verified in the existing independent model:** the standard Jitterbug path and rigid-bar constraints;
- **open:** a time-dependent map of the complete 64-TG, its cellwise rigidity/deformation law, and whether it is an immersion, quotient or projection;
- **open:** an incidence-compatible map from Vesica conformal boundary phase, T101 trigram phases or T097 polar-frame phase to the Jitterbug parameter. None is identified with \(\theta\) or \(\gamma\) by this construction.

## 6. Consequences for #398–#401

1. Close the purely static 64-TG/cuboctahedron/Jitterbug incidence subproblem in #398 using \(\Phi_0\) and the eight explicit panel triples. Do not claim that the Vesica phase map is thereby solved.
2. In #401, treat the existing Jitterbug branch as the target motion of the 12 boundary joints. The first meaningful extension test is whether a declared deformation of the remaining FCC vertices can be constructed with a continuous, rank-controlled cellwise map. Until then the full 64-TG immersion remains open.
3. Feed the eight Kabsch frames into #409 only after checking the panel vertex ordering and normal signs along the entire branch.
4. Derive #399's Ehresmann connection only after a genuine base/fibre map has been selected. Do not infer \(A_a{}^m\) from the static incidence map alone.
5. Derive #400 torsion from the full coframe; neither the Jitterbug flex nor the \(Q_3\) panel-contact graph alone establishes nonzero Cartan torsion.

## 7. Reproduction sources

- Static FCC/D3 coordinate model: `data/64tg_fcc_coordinates.json`; generator/audit: `scripts/audit_64tg_fcc_coordinates.py`.
- Dynamic Jitterbug: `audits/jitterbug_gray_kinematics.py`; report: `docs/JITTERBUG_GRAY_KINEMATICS_VERIFIED.md`.
- Existing Vesica/Q6/Jitterbug crosswalk: PR #394, merged.
- Existing one-panel Kabsch/coil implementation: PR #390, merged.

The incidence comparison is an exact integer-coordinate check against the stored JSON edge list: 24 Jitterbug rod pairs tested, 0 found in the 240 FCC edges. The dynamic numerical tolerances quoted above remain those recorded by the already merged Jitterbug audit.
