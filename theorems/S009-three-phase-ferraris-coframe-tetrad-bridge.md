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


## 14. Minimal covariant electromagnetic source for the torsion trace

This section supplies an explicit **effective Riemann--Cartan constitutive model**. It is a candidate dynamical bridge, not a derived law of vacuum electrodynamics and not yet a constrained teleparallel theory.

Let the spacetime signature be \((-+++ )\), let \(u^\mu u_\mu=-1\) be the material observer field, and let \(Q_{\mu\nu}\) be a symmetric trace-free spatial material anisotropy:
\[
Q_{\mu\nu}=Q_{\nu\mu},\quad
Q^\mu{}_{\mu}=0,\quad Q_{\mu\nu}u^\nu=0.
\]
Define the magnetic four-vector and the anisotropic magnetic invariant by
\[
B^\mu={}^\star F^{\mu\nu}u_\nu,\qquad
\mathcal X_Q=Q_{\mu\nu}B^\mu B^\nu.
\]
The invariant is gauge invariant and has mass dimension four in natural units when \(Q\) is dimensionless.

Use the torsion trace convention \(T_\mu=T^\nu{}_{\mu\nu}\). Treat this irreducible trace component as an independent variable in the local Riemann--Cartan variation, with the other irreducible torsion pieces held fixed. Consider
\[
S=\int d^4x\,e\left[
-\frac14F_{\mu\nu}F^{\mu\nu}
-\frac{M_T^2}{2}T_\mu T^\mu
+g_T T^\mu\nabla_\mu\mathcal X_Q
+\mathcal L_Q+\mathcal L_{\rm rest}
\right].
\]
Here \(M_T^2>0\), \([g_T]=-2\) in mass units, and \(\mathcal L_Q\) supplies the material director's own dynamics and stabilizes its amplitude. The displayed torsion sector is algebraic in \(T_\mu\); no torsion kinetic term is assumed in this minimal effective model.

### 14.1 Torsion-trace field equation

Varying the independent trace gives
\[
\delta_T S=\int d^4x\,e
\left(-M_T^2T_\mu+g_T\nabla_\mu\mathcal X_Q\right)
\delta T^\mu.
\]
Therefore
\[
\boxed{T_\mu=\frac{g_T}{M_T^2}\nabla_\mu\mathcal X_Q.}
\]
This is the explicit constitutive source equation. The electromagnetic anisotropy gradient sources the torsion trace. It predicts no source when \(\mathcal X_Q\) is spacetime-constant. Substitution back into the action gives the local effective term
\[
\mathcal L_{T,\rm eff}
=\frac{g_T^2}{2M_T^2}
\nabla_\mu\mathcal X_Q\nabla^\mu\mathcal X_Q.
\]
The sign follows from the displayed \((-+++ )\) action and positive algebraic coefficient \(M_T^2\); stability of the complete material/field theory must be assessed together with \(\mathcal L_Q\), higher-derivative terms and boundary conditions.

### 14.2 Maxwell equation and constitutive excitation

Define
\[
P^{\mu\nu}:=\frac{\partial\mathcal X_Q}{\partial F_{\mu\nu}},
\qquad P^{\mu\nu}=-P^{\nu\mu},
\qquad D_T:=\nabla_\mu T^\mu.
\]
Up to a boundary term,
\[
g_T T^\mu\nabla_\mu\mathcal X_Q
\doteq -g_TD_T\mathcal X_Q.
\]
The electromagnetic excitation associated with the displayed action is consequently
\[
\boxed{\mathcal H^{\mu\nu}
=-2\frac{\partial\mathcal L}{\partial F_{\mu\nu}}
=F^{\mu\nu}+2g_TD_TP^{\mu\nu}.}
\]
With the convention \(\nabla_\mu\mathcal H^{\mu\nu}=J^\nu\), the sourced Maxwell equation is
\[
\boxed{\nabla_\mu\left(F^{\mu\nu}+2g_TD_TP^{\mu\nu}\right)=J^\nu,}
\qquad
\nabla_{[\lambda}F_{\mu\nu]}=0.
\]
Thus the same coupling that sources torsion also changes the electromagnetic constitutive excitation. This reciprocal structure is essential: one must not add a torsion source to the Maxwell sector while leaving the variation of the same action inconsistent.

### 14.3 Explicit rotating-field test

In a local material rest frame, take a rotating magnetic field
\[
\mathbf B(t)=B_0(\cos\Omega_{\rm el}t,\sin\Omega_{\rm el}t,0)
\]
and a fixed biaxial material tensor
\[
Q=\operatorname{diag}(q,-q,0).
\]
Then
\[
\mathcal X_Q(t)=qB_0^2\cos(2\Omega_{\rm el}t),
\qquad
T_0(t)=\frac{g_T}{M_T^2}\partial_t\mathcal X_Q(t)
=-\frac{2g_TqB_0^2\Omega_{\rm el}}{M_T^2}
\sin(2\Omega_{\rm el}t),
\]
where the last expression uses the local coordinate component convention for the time derivative. The torsion-trace source oscillates at twice the electrical rotation frequency. It vanishes if \(q=0\), if \(B_0=0\), or if the invariant is constant. If the material tensor co-rotates exactly with the magnetic field, \(\mathcal X_Q\) is constant and this particular coupling produces no torsion. The effect is therefore controlled by **relative rotation between field and material anisotropy**, not by rotation alone.

### 14.4 Scope and constraints

1. This is a gauge-invariant nonminimal electromagnetic--torsion coupling because it depends on \(F\), not directly on the gauge potential \(A\).
2. The equation above sources only the torsion trace irreducible component. It does not establish an axial or tensor torsion source.
3. The model is a local Riemann--Cartan effective action. In a teleparallel formulation, the flatness/inertial-spin-connection constraint must be imposed and varied consistently; one cannot vary the torsion trace as an unconstrained independent field and then claim a teleparallel solution.
4. The coframe and material director equations, stress-energy, boundary terms, and the remaining irreducible torsion sectors must be varied to obtain a complete coupled system.
5. The S.6 current \(J_i=\kappa[H(D_iQ),Q]\) is a distinct connection current. Its contribution must be included through the complete connection variation, with compatible index and normalization conventions; it is not silently equal to the electromagnetic torsion-trace source above.
6. A uniform isotropic Ferraris field in an isotropic medium has no \(Q\)-anisotropy invariant gradient and hence no source in this model. The nonzero prediction requires a fixed or spatially varying anisotropic material director and relative field/director motion.

### 14.5 Evidence classification

- **PROVED conditional variational identity:** the torsion-trace equation and Maxwell excitation follow from the displayed action and independent-trace variation.
- **EXACT idealized test:** the biaxial fixed-director rotating-field invariant oscillates at \(2\Omega_{\rm el}\), and the displayed constitutive equation gives the stated trace response.
- **CANDIDATE:** the effective coupling constant \(g_T/M_T^2\), the material director dynamics, and its identification with the user's RGS/PSU helical sector.
- **OPEN:** constrained teleparallel reduction; complete tetrad/connection/material variation; positivity and hyperbolicity of the full coupled equations; numerical calibration and experimental/industrial validation.
