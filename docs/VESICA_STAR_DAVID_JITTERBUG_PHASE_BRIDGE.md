# Vesica–Star-of-David–Jitterbug phase and transport crosswalk

**Record type:** dependency/crosswalk document; no new geometric theorem is claimed.  
**Status:** component constructions and identities are recorded in the linked theorem files; the global incidence-compatible map from the planar phase data to the three-dimensional Jitterbug frame remains open.

## 1. Purpose: integrate existing results, do not restart the construction

This document connects existing repository records that had been treated too separately:

1. the two-circle Vesica and its positive/negative equilateral triangles;
2. the antipodal six-state configuration, geometrically represented by two opposite equilateral triangles (the planar Star-of-David/hexagram motif);
3. the fivefold construction of the regular pentagon;
4. the Q6/RGS antipodal embedding and trigram phase data;
5. the standard three-dimensional Jitterbug flex of the cuboctahedron (Vector Equilibrium) through the icosahedral configuration to the octahedron;
6. the barycentric, gradient, Frank–Burgers and holonomy machinery.

The point is not to identify all these objects by name. Each arrow below has a specified mathematical meaning and an explicit evidence boundary.

## 2. The Vesica generator: two triangles, two branches

For circle centres \(C_1,C_2\), common radius \(r\), and \(|C_2-C_1|=r\), put
\[
u=(C_2-C_1)/r,\qquad u^\perp=Ju,\qquad M=(C_1+C_2)/2,
\]
\[
P_\pm=M\pm\frac{\sqrt3r}{2}u^\perp.
\]
Then
\[
\Delta_\pm=\operatorname{conv}(C_1,C_2,P_\pm)
\]
are equilateral triangles of side \(r\), with opposite orientations. Their barycentres are
\[
B_\pm=M\pm\frac{r}{2\sqrt3}u^\perp,
\qquad \frac{B_++B_-}{2}=M.
\]
The reflection across the line of centres exchanges the two triangles. The positive branch carries the exact mean-gradient/boundary-flux identity; the negative branch carries the reflected barycentre and covariance.

These are the statements of **T098**, not a new conjecture in this document. T097 then uses the kinematic gradient and structured-gradient mismatch to reconstruct Frank and Burgers closure. T092 supplies the \(SE(2)\) composition and the conditional Cartan interpretation.

References:
- [T098 — Two-circle positive-gradient / negative-barycentre duality](../theorems/T098-two-circle-positive-gradient-negative-barycentre-duality.md)
- [T097 — Barycentric–kinematic Frank–Burgers reconstruction](../theorems/T097-barycentric-kinematic-frank-burgers-law.md)
- [T092 — Two-circle / Frank–Burgers holonomy bridge](../theorems/T092-local-two-circle-frank-burgers-holonomy-bridge.md)
- [T091 — Frank–Burgers tensor composition and sensitivity](../theorems/T091-frank-burgers-tensorial-anisotropy-composition-law.md)

## 3. Star of David: the antipodal six-state Vesica/hexagon sector

Let
\[
\omega=e^{2\pi i/3},\qquad
T=\{1,\omega,\omega^2\},\qquad
-T=\{-1,-\omega,-\omega^2\}.
\]
The two equilateral triples \(T\) and \(-T\) are antipodal. Their union
\[
\mathcal H=T\cup(-T)=\{\pm1,\pm\omega,\pm\omega^2\}
\]
is the regular unit hexagon; joining alternate vertices gives the two opposite triangles, i.e. the planar Star-of-David/hexagram motif. The ratio of a triangle side to a hexagon side is \(\sqrt3\).

T142 proves the six-state antipodal operator identities, including
\[
X^2+Y^2=I_6,\qquad \{J,X\}=\{J,Y\}=0,
\]
and the even/odd block ranks \(3\) and \(2\). T143 gives a concrete isometric embedding of these six states into the archived RGS/Q6 antipodal convention \(p(g)=g\oplus7\), using the pairs
\[
(2,5),\quad(3,4),\quad(9,14).
\]
The 29 remaining antipodal pairs admit a 29-angle diagonal extension, but those angles are not selected by the embedding itself.

This is the precise algebraic content behind the planar antipodal-triangle motif and its Q6/RGS realization. It is not a claim that the six planar points are the full three-dimensional Jitterbug, or that the 29 remaining phases have already been determined.

References:
- [T142 — Antipodal six-state Vesica/hexagon model](../theorems/T142-vesica-antipodal-six-state-mixing.md)
- [T143 — Vesica embedding with the geometric RGS AntiTwin](../theorems/T143-vesica-q6-isometric-antipodal-embedding.md)

## 4. The fivefold branch is separate but geometrically compatible

The exact Vesica-to-pentagon construction of Sparavigna–Baldi is documented in [VESICA_PENTAGON_FRAME_BRIDGE.md](VESICA_PENTAGON_FRAME_BRIDGE.md). Its auxiliary construction gives
\[
OH=\frac r\varphi,\qquad CH=2r\sin36^\circ,
\]
so \(CH\) is a chord subtending \(72^\circ\) in the radius-\(r\) circle. The five pentagonal positions are
\[
\alpha_k=\alpha_0+\frac{2\pi k}{5},\qquad k=0,\ldots,4.
\]

These five discrete phases are not the same object as:
- the two-circle trigram phases \(\theta_t^\pm\) in T101;
- the polar angle \(\theta_G\) reconstructed from a deformation gradient in T097;
- the Jitterbug face-rotation parameter \(\gamma\) or ellipse parameter \(\theta\).

A correspondence between these phase systems requires an incidence map and a declared orientation/branch convention. Equality of angular increments or a shared geometric carrier is not sufficient.

Reference:
- [Exact Vesica–pentagon construction and selected-direction map](VESICA_PENTAGON_FRAME_BRIDGE.md)
- Sparavigna and Baldi (2016), §6, Figs. 3–5, Eqs. (25)–(27), [institutional PDF](https://iris.polito.it/retrieve/e384c431-930e-d4b2-e053-9f05fe0a1d67/properties-pentagon.pdf).

## 5. The phase variables already present in the repository

There are three relevant phase constructions, with different roles.

### 5.1 Two-circle trigram phases (T101)

For two registered circles, T101 records
\[
\theta_t^+,\theta_t^-\in\mathbb R/(2\pi\mathbb Z),
\qquad t=0,\ldots,7,
\]
with measured relative registration
\[
\rho(\theta)=\sigma\theta+\chi\pmod{2\pi},
\qquad \sigma\in\{+1,-1\}.
\]
The complementary-trigram mismatch is
\[
\epsilon_t=\operatorname{wrap}
\bigl(\theta_{\bar t}^--\sigma\theta_t^+-\chi\bigr),
\qquad \bar t=t\mathbin{\mathrm{xor}}7.
\]
It lifts to 64 hexagram mismatch pairs and to integer winding diagnostics on the 240 Q6 plaquettes. A nonzero winding is a candidate phase defect; its interpretation as Frank or Burgers charge requires the calibration specified in T101.

### 5.2 Gradient-derived frame phase (T097)

For an orientation-preserving nonsingular kinematic gradient \(G\), T097 fixes the polar rotation
\[
G=R_GU_G,\qquad
\theta_G=\operatorname{atan2}(G_{21}-G_{12},G_{11}+G_{22}).
\]
The angle is tracked continuously chart by chart. Its winding supplies the rotational part of the defect closure. The translational part is separately supplied by the circulation of the structured mismatch \(\mathsf D=\nabla g-G\), with the appropriate interface terms and common-frame transport.

This is a principled source of a continuous frame angle when the kinematic gradient \(G\) is actually available. It is not an arbitrary \(R(\theta(x))\) inserted by hand.

### 5.4 Boundary phase candidate from the conformal-coordinate calculation

The earlier *gradienti e baricentri* calculation also records a scalar phase candidate on the two boundary arcs. Keep it separate from the discrete pentagonal phases, the eight trigram phases and the gradient polar angle.

With
\[
P_\pm=\frac12\pm i\frac{\sqrt3}{2},\qquad
q(z)=-\frac{z-P_-}{z-P_+},\qquad
\rho=|q|,
\]
the first arc \(z=e^{i\theta}\), \(-\pi/3<\theta<\pi/3\), gives
\[
\rho=
\frac{\sin((\theta+\pi/3)/2)}
{\sin((\pi/3-\theta)/2)}.
\]
The second arc \(z=1+e^{i\phi}\), \(2\pi/3<\phi<4\pi/3\), gives the recorded radial relation
\[
\rho=
\frac{\sin((4\pi/3-\phi)/2)}
{\sin((\phi-2\pi/3)/2)}.
\]
The corresponding inverse expressions are
\[
\theta(\rho)=2\arctan\frac{\sqrt3\rho}{2+\rho}-\frac{\pi}{3},
\qquad
\phi(\rho)=\frac{2\pi}{3}
+2\arctan\frac{\sqrt3}{1+2\rho}.
\]
They have the correct endpoint ranges:
\[
\theta(0)=-\frac{\pi}{3},\quad
\theta(+\infty)=\frac{\pi}{3};
\qquad
\phi(0)=\frac{4\pi}{3},\quad
\phi(+\infty)=\frac{2\pi}{3}.
\]
With
\[
f_1(\theta)=\frac{3\theta}{\pi},\qquad
f_2(\phi)=3-\frac{3\phi}{\pi},
\]
both branches reduce, for \(\rho>0\), to
\[
g(\rho)=\frac6\pi
\arctan\frac{\sqrt3\rho}{2+\rho}-1,
\]
because
\[
\arctan\frac{\sqrt3\rho}{2+\rho}
+\arctan\frac{\sqrt3}{1+2\rho}
=\frac{\pi}{3}.
\]
Under the recorded parameter convention \(\rho=|t|^{2/3}\), this becomes
\[
g(t)=\frac6\pi
\arctan\left(
\frac{\sqrt3|t|^{2/3}}{2+|t|^{2/3}}
\right)-1,
\]
which is even, with \(g(0)=-1\) and limits \(g(t)\to1\) as \(|t|\to\infty\).

**Evidence boundary.** The identity unifying the two scalar expressions is an exact algebraic identity. The arc inversions have the endpoint ranges shown above. The complete conformal claim still requires a direct, independent verification of the definition of \(q\) on both arcs, the image of the two-dimensional Vesica interior, and a continuous branch of \(q^{3/2}\). In particular, on the first arc the ratio of sines in
\[
\frac{z-P_-}{z-P_+}
=e^{-i\pi/3}
\frac{\sin((\theta+\pi/3)/2)}
{\sin((\theta-\pi/3)/2)}
\]
is negative, so the leading minus in \(q\) makes \(\arg q=-\pi/3\) on the stated principal branch. This boundary fact alone does not establish the interior sector map.

The parameter \(t\) and the identification \(\rho=|t|^{2/3}\) must remain explicit conventions until the original parameterization is independently replayed. Do not identify \(g(t)\) with \(\alpha_k\), \(\theta_t^\pm\), \(\theta_G\), or the Jitterbug angles without a proved transition map.

### 5.3 Non-affine Vesica continuation (T099)

T099 defines a differentiable family of two-ellipse lenses and exact shape derivatives of area, first moment and covariance under transversality and fixed-topology assumptions. Its Koopman generator is with respect to a continuation parameter \(p\), not physical time. It can supply a parameter-dependent geometric state once the ellipse centres and shape matrices are specified.

It does not by itself identify \(p\) with the Jitterbug time or determine the Jitterbug's mechanical phase.

References:
- [T101 — Trigram angular phases and Q6 plaquette holonomy](../theorems/T101-trigram-angular-phases-q6-plaquette-holonomy.md)
- [T097 — Gradient-derived polar frame and Burgers closure](../theorems/T097-barycentric-kinematic-frank-burgers-law.md)
- [T099 — Non-affine Vesica observables and parameter-Koopman bridge](../theorems/T099-nonaffine-vesica-parameter-koopman-bridge.md)

## 6. The Jitterbug link: what is already established

The standard Jitterbug is a three-dimensional rigid-bar flex of the cuboctahedron (Vector Equilibrium) through the icosahedral configuration to the octahedron. The verified repository model has:
- 12 spherical joints (the cuboctahedron vertices);
- 24 rigid struts;
- 8 rigid equilateral triangular panels, grouped into two chiral tetrahedral families \(T_+\) and \(T_-\);
- a one-parameter constraint curve obtained from the two independent edge-orbit quadratic constraints.

The independent constraint audit verifies the standard path, the vertex ellipses, opposite rotations of \(T_+\) and \(T_-\), the face-centroid law
\[
V(\gamma)=\sqrt{\frac23}\,L\cos\gamma,
\]
and the icosahedral configuration. The ellipse parameter \(\theta\) and face-rotation parameter \(\gamma\) obey
\[
\tan\gamma=\sqrt3\tan\theta.
\]
They must not be conflated.

The planar Star-of-David motif and the Jitterbug share the paired/oppositely oriented equilateral-triangle structure. In the Jitterbug this structure occurs as two *families of four rigid faces* in three dimensions. T142's six-state model is therefore a finite planar antipodal sector model compatible with the same triangular motif, not a one-to-one identification of six points with the eight Jitterbug panels. An explicit incidence/embedding map is still required to make that identification dynamical.

References:
- [Verified standard Jitterbug kinematics](JITTERBUG_GRAY_KINEMATICS_VERIFIED.md)
- [64-TG, Vesica geometry, barycentric moments and Morandotti interface](64TG_VESICA_MORANDOTTI_BRIDGE.md)
- R. W. Gray, *The Jitterbug Motion* (2002), [paper PDF](https://www.rwgrayprojects.com/rbfnotes/polyhed/jitterbug/paper01/jbCurve.pdf).

## 7. From geometry to the mixed frame and torsion

The full frame/coframe convention remains
\[
E_a=e_a{}^\mu\partial_\mu+A_a{}^m\partial_m,\qquad
E_i=\phi_i{}^m\partial_m,
\]
\[
E^a=e^a{}_\mu dx^\mu,\qquad
E^i=\phi^i{}_m(dy^m-A_a{}^m e^a).
\]

The geometric programme now has distinct inputs for the mixed block:
- a local two-circle correspondence and its reflected branch (T098);
- phase mismatch and winding data on the Q6 incidence complex (T101);
- a continuous polar-frame angle when a kinematic gradient is supplied (T097);
- parameter-dependent lens geometry and moments (T099);
- the pentagonal fivefold construction and its discrete phases;
- a candidate three-dimensional mechanical path from the verified Jitterbug.

The mixed block \(A_a{}^m\) must be obtained by an incidence-compatible map between these already defined structures. It is not equal by definition to the pentagon map \(F\), the DtN matrix, the phase mismatch, or the Frank–Burgers holonomy. Once \(A\), \(\phi\), \(e\), and the spin connection are specified, compute the full torsion
\[
T^A=dE^A+\omega^A{}_B\wedge E^B.
\]
A constant mixed block in the simplified coframe is integrable and gives zero torsion. A nonzero Burgers closure from T092/T097 is meaningful only after the coframe development and path transport are matched to that same geometry.

The desired \(T\,B_\perp\) term remains open until the internal bivector \(B_\perp\), its representation, the coupling density, and the variational reduction are all explicitly defined. No torsion term is inferred solely from the existence of the Vesica, the Star of David, or the Jitterbug flex.

## 8. Dependency map and proof-status register

\[
\begin{array}{c}
\text{Two-circle Vesica}\\
\downarrow\ \text{T098: opposite triangles, gradient and barycentre}\\
\text{Frank--Burgers / }SE(2)\text{ closure (T092, T097)}\\
\downarrow\\
\text{phase data: trigram mismatch (T101), polar frame (T097)}\\
\downarrow\\
\text{six-state antipodal sector / Star-of-David motif (T142)}\\
\downarrow\ \text{isometric embedding}\\
\text{RGS/Q6 AntiTwin (T143)}
\end{array}
\qquad
\begin{array}{c}
\text{Vesica}\\
\downarrow\ \text{Sparavigna--Baldi}\\
\text{fivefold pentagon phases}\\
\downarrow\ \text{incidence map still required}\\
\text{candidate compatibility with Jitterbug phases}\\
\downarrow\\
\text{standard 3D Jitterbug path}
\end{array}
\]

| Component | Repository record | Status |
|---|---|---|
| Two-circle Vesica and \(\sqrt3\) chord | T137 | Proved |
| Opposite equilateral triangles, positive gradient and negative barycentre | T098 | Proved under stated Euclidean hypotheses |
| \(SE(2)\) Frank/Burgers closure and Cartan bridge | T092, T097 | Exact discrete identities; continuum interpretation conditional |
| Non-affine lens moments and parameter derivatives | T099 | Proved under transversality/fixed-topology hypotheses |
| Trigram phases and Q6 plaquette winding | T101 | Exact definitions/combinatorics; measured phases and physical interpretation data-dependent |
| Antipodal six-state Star-of-David/hexagon sector | T142 | Exact finite-dimensional identities |
| Six-state embedding into RGS AntiTwin | T143 | Exact algebra conditional on archived antipodal convention; transport phase selection open |
| Exact Vesica-to-pentagon construction | VESICA_PENTAGON_FRAME_BRIDGE | Euclidean construction proved |
| Standard Jitterbug kinematics | JITTERBUG_GRAY_KINEMATICS_VERIFIED | Independently constraint-audited standard mechanism |
| Map from planar phases/six-state sector to eight Jitterbug panels | — | Open |
| 64-TG moving embedding into the Jitterbug | 64TG_VESICA_MORANDOTTI_BRIDGE | Open |
| Full mixed frame \(A_a{}^m\), nonzero torsion and \(T B_\perp\) coupling | — | Open |

## 9. Reproduction and editorial rules

Existing audits (run separately from the repository root):
\`\`\`bash
python scripts/audit_t099_nonaffine_vesica_koopman.py
python scripts/audit_t101_trigram_phase_holonomy.py
python scripts/audit_t142_vesica_antipodal_six_state.py
python scripts/audit_t143_vesica_q6_embedding.py
python3 audits/jitterbug_gray_kinematics.py
python3 -m unittest discover -s tests -p 'test_jitterbug_coil_coupling.py' -v
\`\`\`

These commands are listed as reproduction entry points; this document does not claim that they were executed in this change.

Editorial constraints:
- do not conflate the pentagonal \(\alpha_k\), trigram \(\theta_t^\pm\), gradient polar angle \(\theta_G\), Jitterbug \(\theta\), and Jitterbug \(\gamma\);
- do not call a continuation parameter physical time;
- do not identify the planar six-state sector with all eight Jitterbug panels;
- do not infer nonzero torsion from a constant \(A\) or from a phase label;
- retain the existing theorem classifications and do not promote conditional/parameter-dependent results to universal physical laws.
