# S.9 — Three-phase rotating fields, Ferraris' two-coil construction, and the coframe/tetrad

**Classification:** exact field-composition identities; exact coframe/tetrad transformation laws; physical motor interpretation conditional on the stated winding idealizations. This is a geometric bridge, not a claim that an electrical neutral point is a spacetime origin or that a rotating magnetic field is itself a tetrad.

## 1. Three distinct meanings of “star”

The word *star* is used for different structures and they must not be conflated:

1. **Star connection (Y):** three winding terminals meet at an electrical neutral node. The neutral is a circuit node/potential reference; it is not a geometric centre of space.
2. **Phasor star:** three balanced phase phasors have equal magnitudes and phases separated by \(2\pi/3\). Their vector sum is zero.
3. **Spatial winding star:** three stator magnetic axes lie in a physical plane at angles \(0,2\pi/3,4\pi/3\).

The rotating-field construction requires a relation between the spatial axes and the time-dependent phase currents. A phasor diagram alone does not establish that relation.

## 2. Ferraris' two orthogonal windings

Let \((\mathbf e_1,\mathbf e_2)\) be an orthonormal basis of the stator plane. In the idealized two-coil model, equal-amplitude currents in orthogonal windings are in temporal quadrature:
\[
i_1(t)=I\cos\omega t,\qquad i_2(t)=I\sin\omega t.
\]
If the winding geometry gives the same field-per-current coefficient \(c\), linear superposition gives
\[
\mathbf H(t)=cI\big(\cos\omega t\,\mathbf e_1+
                         \sin\omega t\,\mathbf e_2\big).
\]
Consequently
\[
|\mathbf H(t)|=cI,\qquad
\dot\vartheta(t)=\omega,
\]
where \(\vartheta\) is the angle of the field in the stator plane. This is a uniformly rotating field.

If the amplitudes differ, the phase difference is not \(\pi/2\), or the winding coefficients differ, the tip generally traces an ellipse rather than a circle. Thus circular rotation is a consequence of the balanced orthogonal/quadrature conditions, not merely of having two coils.

## 3. Three-phase construction

Let three equal stator winding axes be
\[
\mathbf n_k=(\cos\alpha_k,\sin\alpha_k),\qquad
\alpha_k=\frac{2\pi k}{3},\quad k=0,1,2,
\]
and let their balanced currents be
\[
i_k(t)=I\cos(\omega t-\alpha_k).
\]
For equal winding coefficients \(c\), the resultant field is
\[
\begin{aligned}
\mathbf H(t)
&=c\sum_{k=0}^2 i_k(t)\mathbf n_k\\
&=\frac{3cI}{2}
  (\cos\omega t\,\mathbf e_x+\sin\omega t\,\mathbf e_y).
\end{aligned}
\]
The identity follows by expanding the sine/cosine components and summing the three roots-of-unity directions. The magnitude is constant and the field rotates at angular frequency \(\omega\). Reversing the phase sequence reverses the direction of rotation.

For the balanced system, \(i_0+i_1+i_2=0\), so the neutral current is zero in the ideal symmetric case. This electrical balance is separate from the spatial vector identity producing the rotating field.

## 4. The coframe is the bridge from frame components to geometry

Let \(M\) be a spatial three-manifold and let \(e^a=e^a{}_i dx^i\), \(a=1,2,3\), be an orthonormal coframe for a spatial metric
\[
h_{ij}=\delta_{ab}e^a{}_i e^b{}_j.
\]
The dual frame is \(E_a=E_a{}^i\partial_i\), with
\[
e^a{}_iE_b{}^i=\delta^a{}_b.
\]
A physical magnetic-field vector has frame components \(H^a(t)\) and coordinate components
\[
H^i(t)=E_a{}^i H^a(t).
\]
For the two-coil construction, choose the first two coframe axes along the stator winding axes. Then
\[
H^a(t)=H_0(\cos\omega t,\sin\omega t,0),
\qquad
H^i(t)=E_1{}^iH_0\cos\omega t+
        E_2{}^iH_0\sin\omega t.
\]
For the three-phase construction the same formula holds with \(H_0=3cI/2\). This is the direct coframe bridge: the rotating field is a vector field, and the coframe converts its local components into coordinate components.

Under a local frame rotation \(e'^a=R^a{}_b e^b\), the components transform inversely, \(H'^a=R^a{}_bH^b\) or with the corresponding dual-index convention, so the geometric vector \(H=H^aE_a\) is unchanged. The apparent components depend on the frame; the physical field does not.

## 5. Spacetime tetrad and electromagnetic field strength

On spacetime, use a tetrad \(e^A{}_{\mu}\), with internal Lorentz metric \(\eta_{AB}=\mathrm{diag}(-1,1,1,1)\), so
\[
g_{\mu\nu}=\eta_{AB}e^A{}_{\mu}e^B{}_{\nu}.
\]
For the electromagnetic two-form \(F_{\mu\nu}\), tetrad components are
\[
F_{AB}=e_A{}^{\mu}e_B{}^{\nu}F_{\mu\nu}.
\]
Relative to the observer's timelike tetrad leg, define (up to the chosen sign convention)
\[
E_a=F_{a0},\qquad
B_a=\frac12\epsilon_{abc}F_{bc}.
\]
Thus the electric and magnetic fields are precisely the spatial components of the spacetime field strength in an observer-adapted tetrad. A rotating stator field is represented by time-dependent spatial tetrad components \(B_a(t)\) or \(H_a(t)\), while the spacetime two-form and observer choice determine their geometric meaning.

A time-dependent rotation of the spatial tetrad is a change of observer frame, not automatically a physical rotation of the electromagnetic field. If the tetrad itself rotates, its spin connection acquires the corresponding inertial/angular-velocity term. One must distinguish:
- physical time evolution of \(F_{\mu\nu}\);
- change of tetrad components under a local Lorentz/spatial-frame rotation;
- inertial effects of a rotating observer tetrad.

## 6. Connection and curvature: where the geometry becomes dynamical

For a Lorentz connection \(\omega^A{}_B\), the tetrad postulate/covariant derivative and curvature are expressed as
\[
T^A=de^A+\omega^A{}_B\wedge e^B,
\qquad
\mathcal R^A{}_B=d\omega^A{}_B+
                 \omega^A{}_C\wedge\omega^C{}_B.
\]
The rotating-field phase \(\omega t\) is not the spin connection \(\omega^A{}_B\); the same letter is traditionally used for two different quantities. Use \(\Omega_{\rm el}\) for electrical angular frequency and \(\omega^A{}_B\) for the geometric connection in future formulas.

The phase evolution can be encoded by a circle-valued order parameter \(z(t)=e^{i\Omega_{\rm el}t}\). The stator plane carries the real two-dimensional representation
\[
\begin{pmatrix}\cos\Omega_{\rm el}t\\
\sin\Omega_{\rm el}t\end{pmatrix}
=
\begin{pmatrix}\Re z(t)\\\Im z(t)\end{pmatrix}.
\]
This is an internal phase-plane representation embedded into the spatial coframe plane. A gauge connection for phase transport may be introduced only after specifying how phase is compared between points; it is not automatically the gravitational spin connection.

## 7. Consequences for RGS/PSU and the existing Maxwell/coframe records

This bridge gives a disciplined interpretation of the existing repository structures:

- **S.8 (coframe variation):** supplies the variational language for a spatial coframe and its metric. The rotating-field vector can be expressed in this frame; the motor field does not by itself supply a coframe action.
- **S.7 (fourth-moment/Maxwell bridge):** the electromagnetic field is an antisymmetric two-form. Its electric/magnetic constitutive response may be written in tetrad components. The existing no-go against contracting a fully symmetric fourth-moment tensor directly with two antisymmetric field strengths remains in force; an independent STF order parameter is still required.
- **T.088 (panel tangent frames and holonomy):** supplies the discrete analogue of local frames and transition maps. A winding field on a network can be transported between local tangent frames, and cycle holonomy can be measured. This is not yet an electric-machine model.
- **RGS vierbein/tetrad:** a candidate local frame for expressing the physical and internal sectors, but a mapping from the electrical phase plane to a specific RGS subspace must be defined by an explicit intertwiner or coframe embedding. It cannot be inferred from the word “star”.

A useful next model is a complex two-component field
\[
\Psi_{\rm stator}(t)=H_0e^{i\Omega_{\rm el}t}
\]
together with a declared embedding \(J:\mathbb R^2\to T_xM\) (or into a chosen RGS tangent subspace):
\[
H(t)=J\begin{pmatrix}\Re\Psi_{\rm stator}(t)\\
                         \Im\Psi_{\rm stator}(t)\end{pmatrix}.
\]
The embedding must be isometric if the circular field amplitude is to be preserved. For a varying frame, its covariant derivative includes the induced connection. This gives a precise place to test phase holonomy, frame holonomy, and their possible coupling without identifying them prematurely.

## 8. Classification and limits

| Claim | Status |
|---|---|
| Two orthogonal equal windings with equal quadrature currents produce a constant-amplitude rotating field | Exact ideal-model identity |
| Three equally spaced axes with balanced phase-sequence currents produce the same rotating-field form | Exact ideal-model identity |
| Coframe maps frame components to coordinate vector components | Exact differential-geometric identity |
| Electromagnetic \(E\) and \(B\) are tetrad components of \(F_{AB}\) | Exact, convention-dependent decomposition |
| Electrical neutral/star point is a tetrad origin | False identification |
| Electrical phase angular frequency equals spin-connection coefficient | Not generally true |
| RGS phase-plane embedding and connection | Candidate; requires explicit map and covariance audit |
| Motor torque, losses, saturation, winding harmonics and industrial efficiency | Outside the ideal field identity; require electromagnetic/material model and validation |

## 9. Historical note

The standard historical account credits Galileo Ferraris with the rotating magnetic field principle from two orthogonal coils carrying currents in temporal quadrature, with his 1888 publication. The exact priority, chronology, and comparison with Tesla's independent work should be documented from historical primary sources before being used as a priority claim in a publication. The mathematical identities above do not depend on the historical attribution.


## 10. The already-established 120-degree quaternionic structure

The 120-degree angle is not only the phase spacing of a balanced three-phase circuit. In the geometric programme it also occurs as a proper tetrahedral rotation and is represented by a unit quaternion. In the even Clifford algebra,
\[
Cl^+(3)=\operatorname{span}\{1,e_{23},e_{31},e_{12}\}\cong\mathbb H,
\]
and a rotation through angle \(\theta\) about unit axis \(\mathbf n\) is represented by
\[
q=\cos(\theta/2)+\mathbf n\sin(\theta/2).
\]
For \(\theta=2\pi/3\),
\[
q=\frac12+\frac{\sqrt3}{2}\mathbf n,
\qquad q^3=-1,\quad q^6=1.
\]
The corresponding element of \(SO(3)\) has order three; its lift in \(SU(2)\) has order six. This is the correct double-cover distinction. It connects the threefold phase/spatial cycle to the already-used tetrahedral, \(H_3\), and binary-icosahedral quaternionic structures, but does not identify the electrical phase sequence with a particular group element until the axis, orientation and representation map are fixed.

## 11. Maxwell's quaternionic formulation already fixed in the programme

The quaternionic Maxwell notation used in the prior derivation is retained:
\[
\mathcal A=\frac{\phi}{c}+\mathbf i A_x+\mathbf j A_y+\mathbf k A_z,
\qquad
\mathcal F=\mathbf E+i c\mathbf B,
\qquad
\nabla_q=\mathbf i\partial_x+\mathbf j\partial_y+\mathbf k\partial_z.
\]
Here the quaternion units \(\mathbf i,\mathbf j,\mathbf k\) must not be silently confused with the commuting scalar complex unit \(i\) in the displayed field combination. The component conventions and signs must be checked against
\[
\partial_\mu F^{\mu\nu}=\mu_0J^\nu
\]
and the homogeneous Maxwell equations, component by component. The covariant Maxwell action, stress-energy tensor and four-momentum remain the reference formulation.

This quaternionic packaging is a representation of the Abelian electromagnetic field. It does **not** by itself introduce a non-Abelian \(SU(2)\) gauge connection. Any additional \(SU(2)\) structure must be independently defined and varied; it is not a relabelling of Maxwell's \(U(1)\) potential.

## 12. Rotating field and Cartan torsion: the precise bridge

A rotating field can define a preferred local direction in the stator plane. If this direction is promoted to a spatially varying local coframe, write
\[
e^1=\cos\vartheta(x)\,dx+\sin\vartheta(x)\,dy,
\qquad
e^2=-\sin\vartheta(x)\,dx+\cos\vartheta(x)\,dy.
\]
Then the coframe derivatives are
\[
de^1=d\vartheta\wedge e^2,
\qquad
de^2=-d\vartheta\wedge e^1.
\]
The Cartan torsion is not \(de^a\) alone but
\[
T^a=de^a+\omega^a{}_b\wedge e^b.
\]
For the compensating inertial/Levi-Civita connection
\[
\omega^1{}_2=-d\vartheta,\qquad
\omega^2{}_1=d\vartheta,
\]
one obtains \(T^1=T^2=0\). Thus a mere rotation of an orthonormal frame in flat space does not create physical torsion. If instead the coframe is coupled to an independent connection, or the material frame is genuinely non-integrable, the Cartan torsion can be nonzero and must be computed from the pair \((e,\omega)\).

This is the rigorous sense in which a rotating magnetic texture can be connected to torsion: its orientation field can be used to construct a coframe, and gradients/holonomy of that coframe enter the Cartan structure equations. A nonzero torsion response requires a specified connection dynamics or constitutive coupling; it cannot be inferred from the temporal rotation of a uniform Ferraris field alone.

In the earlier density/helical-field construction, keep the objects separate:
\[
T^a=de^a+\omega^a{}_b\wedge e^b,
\qquad
\Omega=d\varpi,
\qquad
\mathbf B.
\]
The proposed constitutive map \(\mathbf B=\mathcal K(T)\), or more generally \(B=\mathcal K\,T\) after choosing compatible tensor types, remains to be derived from an action with correct units, symmetries and observables. Mechanical vorticity, magnetic moment and magnetic induction may be related by projections in a specified medium, but they are not identical to Cartan torsion.

The repository's S.6 connection-current variation is the appropriate existing variational starting point:
\[
D_iQ=\partial_iQ+[\omega_i,Q],
\qquad
J_i=\kappa[H(D_iQ),Q]\in\mathfrak{so}(3).
\]
It derives a local \(\mathfrak{so}(3)\)-connection current for the displayed gradient action. It does not yet solve a torsion field equation. S.8 explicitly contains no coframe derivatives and therefore cannot generate torsion on its own. A complete bridge must combine the coframe, the independent/inertial connection, the matter or spin current, and the electromagnetic constitutive sector in one covariant action.

## 13. Updated claim ledger

| Statement | Status |
|---|---|
| 120-degree rotation has an order-three image in \(SO(3)\) and order-six quaternionic lift in \(SU(2)\) | Exact |
| Balanced three-phase currents generate a rotating stator field in the ideal model | Exact |
| Maxwell field can be packaged in the previously fixed quaternionic notation | Exact representation, subject to component/sign audit |
| A field-orientation texture can define a coframe whose derivatives enter Cartan's torsion equation | Exact construction |
| A uniform rotating field necessarily produces nonzero Cartan torsion | False |
| Nonzero torsion sourced by the electromagnetic/helical field | Candidate; requires a covariant action and constitutive derivation |
| Identification of magnetic induction, vorticity and Cartan torsion | Not permitted without a derived map |
| S.6 connection current as a source in a complete torsion equation | Open; requires full coframe/connection/matter variation |


## 14. Supersession of the external-anisotropy ansatz

**Correction status:** the effective model in the previous version of this section is retained only as a generic material-medium example. It is **not** the RGS/Kathara derivation and must not be used as its source law.

The previous ansatz introduced an independent biaxial tensor
\[
Q=\operatorname{diag}(q,-q,0)
\]
and inferred a $2\Omega_{\rm el}$ torsion-trace response. That calculation is conditionally correct for the displayed external-director model, but it inserts a material anisotropy not derived from the RGS operators. It is therefore superseded for the present programme. In particular, it does not establish that the RGS triplet produces a torsion trace or that a rotating Ferraris field alone generates torsion.

### 14.1 Intrinsic RGS operator data

The relevant numerical record is maintained in the companion repository:

- [RGS–QLG quaternion bridge](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge)
- [188D T2u geometry audit]$https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/reports/rgs_188d/188D_T2U_GEOMETRY_AUDIT.json$
- [Kathara/Krystal square-similarity reconstruction]$https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/KATHARA_KRYSTAL_SPIRAL_SQUARE_GEOMETRY.md$

For the selected orthonormal triplet basis $J_0\in\mathbb R^{188\times3}$, the archived audit reports
\[
\|J_0^TJ_0-I_3\|\simeq5.60\times10^{-16}.
\]
It distinguishes two observables which must not be conflated:
\[
M_{\rm geom}=J_0^T K_{\rm tangent}^{+}J_0
\simeq-0.95403126139055\,I_3,
\]
with relative anisotropy $3.96\times10^{-15}$, and
\[
M_{\rm field}=J_0^T K_{\rm field}^{+}J_0,
\]
whose reported eigenvalues are
\[
$0.8272550028,\;0.8272550028,\;0.9512140709$,
\]
with relative anisotropy (0.1427155). The direct compression $J_0^TK_{\rm field}J_0$ is instead approximately $4.96933853 I_3$, but $J_0$ is not invariant under $K_{\rm field}$: the reported relative invariance residual is (0.7219434), and the leakage outside the triplet is (0.3321124).

These are **numerical properties of the archived operators**, not a proof of a physical constitutive law. They show why an external $Q$ is unnecessary as an explanatory input: the anisotropic response is already visible in the full operator/inverse response and its coupling to modes outside the selected triplet. The geometry-compressed tangent observable remains isotropic. Do not state that every RGS triplet is anisotropic, or identify the selected $T_{2u}$ triplet with the 94 dynamical two-planes.

### 14.2 Kathara square map and quaternionic lift

Use the source-derived Kathara/Krystal planar stage map, not an independently postulated anisotropy tensor:
\[
T=\sqrt2R_{-\pi/4}
=\begin{pmatrix}1&1\\-1&1\end{pmatrix},
\qquad T^TT=2I,\quad\det T=2.
\]
Its square is
\[
T^2=\begin{pmatrix}0&2\\-2&0\end{pmatrix}
=2R_{-\pi/2}.
\]
Thus two Kathara stages produce a clockwise quarter-turn and a length doubling. In complex notation $T:z\mapsto(1-i)z$, so $T^2:z\mapsto-2iz$. The scale-normalized quarter-turn is $R_{-\pi/2}$, represented in the spin double cover by
\[
q_{-90}=\frac{1-\mathbf k}{\sqrt2},
\qquad q_{-90}^2=-\mathbf k,\quad
q_{-90}^4=-1,\quad q_{-90}^8=1.
\]
The image in (SO(3)) has order four; this chosen lift in (SU(2)\) has order eight. The planar complex unit $i$, the quaternion unit \$\mathbf k$, and Cartesian sign sectors are related only through the declared representation map; they must not be silently identified.

For comparison, a proper $120^\circ$ rotation around \(\mathbf n=(1,1,1)/\sqrt3\) has lift
\[
q_{120}=\frac{1+\mathbf i+\mathbf j+\mathbf k}{2},
\qquad q_{120}^3=-1,\quad q_{120}^6=1.
\]
Its (SO(3)\) image has order three and its (SU(2)\) lift order six. The axis and orientation must be specified when identifying this with a tetrahedral or three-phase action.

### 14.3 Correct RGS-to-torsion derivation target

The source chain to be tested is
\[
\text{Kathara planar similarity}
\longrightarrow \text{quaternionic lift}
\longrightarrow \text{induced action on }J_0
\longrightarrow \text{operator commutators and leakage}
\longrightarrow \text{coframe/connection variation}.
\]
For the actual 188D representation, construct the lifted action $\rho(q)$ from the archived representation matrices and calculate
\[
[ K_{\rm field},\rho(q)],\qquad
$I-J_0J_0^T$K_{\rm field}J_0,
\qquad
J_0^T K_{\rm field}^{+}J_0.
\]
The first tests equivariance, the second measures mode leakage, and the third is the response observable. No numerical value for the commutator with $\rho(q)$ is asserted until the actual representation matrix is recovered and the calculation is run.

Only after this step may a coframe $e^a$, a connection choice $\omega^a{}_b$, and the Cartan expression
\[
T^a=de^a+\omega^a{}_b\wedge e^b
\]
be evaluated. The existing minimal Einstein--Cartan module supplies a separate action-derived matter-spin result,
\[
T_{abc}=-\frac{\kappa}{2}\epsilon_{abcd}J_5^d,
\]
in its documented conventions. This is an axial, algebraic torsion sourced by the Dirac axial current; it is not automatically the torsion induced by the Kathara/RGS coframe. The Levi-Civita spin-connection kernel is torsion-free by construction. A teleparallel inertial connection is a third, distinct choice.

### 14.4 Epistemic and validation ledger

- **Exact algebra:** Kathara planar similarity $T^TT=2I$, $T^2=2R_{-\pi/2}$, and the stated quaternionic lift identities.
- **Numerically reported:** the two compressed RGS observables, triplet leakage and invariance residuals quoted above; reproducibility still requires matching input hashes, commit, command and dependency versions.
- **Candidate:** the induced Kathara/quaternionic action on the selected RGS triplet and its coupling to the coframe.
- **Open:** representation matrix $\rho(q)$, commutator audit, coframe embedding, full connection variation, and any electromagnetic-to-torsion constitutive law.
- **Retracted as an RGS claim:** the previous external $Q=\operatorname{diag}(q,-q,0)$ source model and its $2\Omega_{\rm el}$ prediction. It remains only a conditional toy model for an independently anisotropic material medium.

