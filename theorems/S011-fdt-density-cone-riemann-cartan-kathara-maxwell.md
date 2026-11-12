# S011 — FDT density-cone extension of the Riemann–Cartan/Kathara–Maxwell model

**Classification:** `interpretive` FDT-to-field-theory identification; `proved` variational identities conditional on the action below; `open` physical coupling, stability, parameter bounds and RGS/Q6 continuum correspondence.

**FDT here means Fundamental Density Theory (Manuel Alfaro).** To avoid acronym collision, fluctuation–dissipation relations are called FDR in this record.

**Dependencies:** S009 (rotating fields/coframe/Cartan bridge); S010 (Kathara quaternionic lift and RGS triplet response; related PR #209); T091–T107 (Frank–Burgers, Q6, Born measure and FDR/defect tests); `research/FDT_RATTI_BIBLIOGRAPHY_AND_CRITICAL_INTEGRATION.md`.

---

## 1. Scope and epistemic separation

This is a **candidate effective action**, not a theorem that FDT, ECSK, RGS and Maxwell have already been unified by nature. It is designed so that each sector can be switched off and independently tested.

1. **Reference physics:** Einstein–Cartan/Riemann–Cartan gravity, Maxwell electrodynamics, ordinary matter and (where chosen) Einstein–aether dynamics.
2. **FDT variables:** a bounded density-cone coordinate, a complex amplitude/phase, the (S^3	o S^2) Hopf structure, and a medium-velocity/vorticity sector. The field realization below is an explicit model map, not an assertion that the FDT source corpus uniquely fixes this action.
3. **RGS–PRISM/Kathara variables:** discrete Q6 geometry, Kathara plane map, quaternionic lifts, frame/connection holonomy, and the measured RGS operator response.

The force scale
[
F_{max}=rac{c^4}{4G}
]
has dimensions of force. It is **not** a bulk Lagrangian density or an energy density. The FDT relation
[
F=F_{max}alpha_1alpha_2,qquad 0<alpha_i<1,
]
is retained as a proposed constitutive/boundary law for a specified pair of source regions. A radial dependence, source profile and work integral are needed before it defines a conservative potential. Likewise (alpha_{m ext}=R_s/r_f) is a dimensionless external-density parameter; identifying it with a local field (alpha(x)) is a model choice to be calibrated.

## 2. Fields and conventions

Use natural units (c=hbar=1) and signature ((-+++)). Let (e^A{}_mu) be a coframe, (g_{mu
u}=eta_{AB}e^A{}_mu e^B{}_
u), and (e=det(e^A{}_mu)). Let (omega^{AB}{}_mu=-omega^{BA}{}_mu) be an independent Lorentz connection, with
[
T^A=de^A+omega^A{}_Bwedge e^B,qquad
R^{AB}=domega^{AB}+omega^A{}_Cwedgeomega^{CB}.
]
Let (U^mu U_mu=-1) be a unit timelike observer/aether field, (A_mu) the electromagnetic potential, and (F=dA).

The FDT density-cone coordinate is (0<alpha(x)<1). Its proposed complex amplitude realization is
[
Psi(x)=sqrt{ho_*},alpha(x)e^{iphi(x)},
]
where (ho_*) is a reference scale chosen so that (Psi) has mass dimension one. This makes the Born density proportional to (|Psi|^2=ho_*alpha^2). The identification is a model ansatz to compare with the FDT papers, not a theorem.

For the Hopf sector let (zetainmathbb C^2), (zeta^daggerzeta=1), and
[
n^a=zeta^daggersigma^azeta,quad n^an^a=1,qquad
a_H=-izeta^dagger dzeta,quad f_H=da_H.
]
Thus (zetain S^3), (nin S^2), and (a_H) is the composite Hopf-fibre connection. It is not automatically the electromagnetic potential or an independent (SU(2)) gauge field.

Let (v^mu) be a medium velocity orthogonal to (U^mu), (U_mu v^mu=0), and define its kinematic vorticity
[
Omega_{mu
u}=2
abla_{[mu}v_{
u]}.
]
The FDT kinematic relation (v^2+w^2=c^2) may be imposed relative to (U^mu), with (w) the complementary scalar component. It is an additional constraint, not a consequence of (U^2=-1), and requires its own multiplier if made dynamical.

The independent two-forms are
[
F=dA,qquad Omega=d(v^lat),qquad T^A=De^A,qquad f_H=da_H.
]
They are not interchangeable.

## 3. Candidate covariant action

Let (D_muPsi=(
abla_mu-iqA_mu)Psi), (T_mu=T^
u{}_{mu
u}) be the torsion trace, and (H^T_{mu
u}=2
abla_{[mu}T_{
u]}). Consider
[
S_{m ext}=int d^4x,e,
(mathcal L_{m RC}+mathcal L_U+mathcal L_{m EM}
+mathcal L_{m FDT}+mathcal L_{m med}
+mathcal L_T+mathcal L_{m spin}+mathcal L_{m matter}).
]

### 3.1 Riemann–Cartan and aether reference

[
mathcal L_{m RC}=rac{M_{m P}^2}{2}R(e,omega),qquad
M_{m P}^2=(8pi G)^{-1},
]
and
[
mathcal L_U=-K^{mu
u}{}_{hosigma}
(
abla^omega_mu U^ho)(
abla^omega_
u U^sigma)
+lambda_U(U^mu U_mu+1).
]
The four standard Einstein–aether coefficients are contained in (K^{mu
u}{}_{hosigma}). Because (
abla^omega U) uses the independent connection, this sector contributes to the connection/torsion equation. A spin-only torsion source cannot be asserted for this action without doing the full variation.

### 3.2 Maxwell and FDT amplitude/Hopf sectors

[
mathcal L_{m EM}=-rac{1}{4mu_0}F_{mu
u}F^{mu
u}
]
in SI normalization. Minimal Maxwell theory uses (F=dA); it does not acquire affine torsion by replacing partial derivatives with a connection.

A minimal FDT realization is
[
mathcal L_{m FDT}
=-rac{Z_Psi}{2}(D_muPsi)^*D^muPsi
-V(alpha)
-rac{f_H^2}{2}partial_mu n^apartial^mu n^a
-rac{Z_H}{4}f_{H,mu
u}f_H^{mu
u}.
]
The potential/domain prescription must keep (0<alpha<1). The Hopf term realizes the (S^3	o S^2) geometry as a sigma-model sector; it does not establish a physical Hopfion or identify the Hopf fibre with electromagnetic (U(1)).

### 3.3 Medium vorticity and a nonminimal electromagnetic ansatz

[
mathcal L_{m med}
=-rac{Z_v}{4}Omega_{mu
u}Omega^{mu
u}
+lambda_{BF}F_{mu
u}Omega^{mu
u}.
]
The mixed term is a gauge-invariant effective ansatz once the transformation properties of (v^mu) are fixed. It is not standard Maxwell theory and is not implied merely by saying that magnetism is medium vorticity. Its units, parity, constitutive meaning and coefficient require independent derivation and measurement.

### 3.4 Optional propagating torsion-trace mode

[
mathcal L_T=
-rac{1}{4g_T^2}H^T_{mu
u}H_T^{mu
u}
-rac{m_T^2}{2}T_mu T^mu
+g_{Talpha}T^mu
abla_mualpha.
]
This is an explicit extension beyond minimal ECSK. The coefficient (m_T^2) is the **net coefficient after decomposing the Einstein–Cartan curvature term and adding any allowed quadratic-torsion invariants**; it must not be double-counted. A healthy Proca-like trace mode requires a positive kinetic normalization and a stable mass sign in the chosen signature. The density-gradient coupling is a gauge- and diffeomorphism-invariant ansatz, not a consequence of FDT alone.

The axial torsion component sourced by a minimally coupled Dirac axial current is distinct from the trace component (T_mu). For a Dirac field use the standard tetrad/spin-connection covariant kinetic term; its variation with respect to (omega^{AB}{}_mu) defines the spin current. Do not identify axial torsion and torsion trace.

## 4. Variational equations

The following are conditional Euler–Lagrange results of the displayed action.

### 4.1 Torsion trace

Varying (T_mu) gives
[
oxed{rac{1}{g_T^2}
abla_
u H_T^{
umu}
-m_T^2T^mu+g_{Talpha}
abla^mualpha=0.}
]
If the kinetic term is removed, the trace is algebraically constrained:
[
T^mu=rac{g_{Talpha}}{m_T^2}
abla^mualpha.
]
With the kinetic term present it obeys a sourced Proca-type equation and may carry a propagating mode, subject to constraint and stability analysis. Thus “ECSK torsion is algebraic” is correct for minimal ECSK, but is not a no-go theorem for every Riemann–Cartan extension.

### 4.2 Maxwell

Define the excitation
[
mathcal H^{mu
u}=F^{mu
u}-2mu_0lambda_{BF}Omega^{mu
u}
]
in SI normalization. Variation with respect to (A_
u) gives
[
oxed{
abla_mumathcal H^{mu
u}=mu_0j^
u_{m matter+Psi},}
]
where the current is defined by the variation of charged matter and amplitude sectors. Gauge invariance gives current conservation on shell. The homogeneous equation remains (dF=0). The mixed term changes the constitutive excitation; it does not make (Omega) identical to (F).

### 4.3 Amplitude/phase and Hopf equations

Variation of (Psi^*) gives
[
Z_Psi D_mu D^muPsi-rac{partial V}{partialPsi^*}=0,
]
where the derivative of (V(alpha)) is understood through (alpha=|Psi|/sqrt{ho_*}). Separating amplitude and phase gives a density equation and a conserved (U(1)) current. The constrained variation of (zeta), or equivalently (n^an^a=1), gives the (S^2) sigma-model equation with its unit-vector constraint. The composite (f_H) is the pullback of the Hopf-bundle curvature. Identifying its fibre phase with electromagnetic (U(1)) requires an explicit bundle and charge map.

### 4.4 Independent connection, coframe and aether

The connection equation is
[
oxed{rac{delta S_{m ext}}{deltaomega^{AB}{}_mu}=0.}
]
It contains the Einstein–Cartan Cartan term, the aether connection current, the Dirac spin current, and the torsion-trace kinetic/interaction contribution. Schematically,
[
mathcal C_{AB}{}^mu(e,T)+
mathcal J^{(U)}_{AB}{}^mu+
mathcal J^{(m spin)}_{AB}{}^mu+
mathcal J^{(T,alpha)}_{AB}{}^mu=0.
]
This is the required correction to a spin-only source statement: the aether sector also sources the connection equation because its covariant derivative uses (omega). The component equation must be expanded after fixing the irreducible torsion decomposition.

The coframe equation is (delta S_{m ext}/delta e^A{}_mu=0), giving the gravitational equation with the total stress-energy of all sectors. The connection and coframe equations must be varied together; imposing the Levi-Civita connection before variation would remove the independent torsion equation. The aether and medium equations are respectively (delta S/delta U^mu=0) and (delta S/delta v^mu=0), with their normalization/orthogonality constraints.

## 5. Kathara/quaternionic and Q6/RGS embedding

Retain the audited Kathara map
[
T_K=egin{pmatrix}1&1\-1&1end{pmatrix},qquad
T_K^TT_K=2I,qquad T_K^2=2R_{-90^circ},
]
and the oriented quaternionic lift
[
q_K=rac{1-mathbf k}{sqrt2},qquad q_K^2=-mathbf k.
]
These are exact algebraic identities. They do not specify how the operation acts on (Psi,zeta,U^mu,F), or the 188D RGS operator. That requires an explicit representation/intertwiner (J_K), including the transformation of the connection, followed by an action-covariance test.

For the 64 Q6 amplitudes retain T107's finite graph interaction
[
H_J(z)=-Jsum_{{h,k}in E(Q_6)}
operatorname{Re}(z_hoverline{z_k}),qquad
sum_h|z_h|^2=1.
]
This defines a finite-dimensional statistical model and, with T107's reversible generator, an FDR model. It is not real-time unitary quantum evolution without a separately specified Hamiltonian. A continuum-to-graph map (I_h:Psi(x)mapsto z_h) must preserve normalization and have a declared length/time scale before the two descriptions can be identified.

The existing 188D triplet observation remains numerical: the geometric inverse compression is isotropic to numerical precision, while the field inverse compression has relative anisotropy about (0.1427). This is not yet a calibrated physical force or a coupling constant in the action. The representation (ho(q_K)), commutator ([K_{m field},ho(q_K)]), and leakage calculation remain open.

## 6. FDT force scale: constitutive relation, not guessed bulk term

Keep
[
F_{12}=F_{max}alpha_1alpha_2,qquad F_{max}=rac{c^4}{4G}
]
outside the local bulk action until the source functionals (alpha_i[Psi,U,zeta]), separation vector, force direction and work/potential relation are specified. The dimensionless ratio (alpha_{m ext}=R_s/r_f) can be compared with (alpha(x)) only after the source geometry and meaning of (r_f) are fixed. No term proportional to (F_{max}) is added to (mathcal L) by dimensional guesswork.

Keep distinct: electromagnetic (F_{mu
u}), medium vorticity (Omega_{mu
u}), Cartan torsion (T^A), Hopf curvature (f_H), and Lorentz curvature (R^{AB}). Any constitutive identification needs a derived tensor map with dimensions, symmetries and measurable coefficient.

## 7. Falsifiable work programme

1. Decompose torsion into trace, axial and tensor pieces; derive coefficients from the Palatini term and added invariants. Include the aether contribution.
2. Perform a constraint/Hamiltonian analysis of the torsion-trace kinetic term: poles, residues, characteristic cones, ghosts, tachyons and the massless limit.
3. Fix (ho_*), the normalization/domain of (alpha), and the map from (alpha_{m ext}) to (alpha(x)). Test the FDT force law on a specified two-source configuration.
4. Derive the Hopf bundle/charge map and finite-energy conditions; keep (a_H) distinct from (A) until then.
5. Vary (v^mu); derive the modified constitutive response and test gauge invariance, parity, causality, passivity and energy conservation. Bound (lambda_{BF}).
6. Construct (J_K) on the RGS subspace and calculate ([K_{m field},ho(q_K)]), invariant-subspace leakage and response tensor.
7. Construct and test (I_h); preserve Q6 chain-map identities and Born normalization; compare graph and continuum correlators under refinement.
8. For the photoelectric sector, separate photon threshold, electron transport and detector collection. A static magnetic field does no work on a charge; a time-dependent field can induce (E) through Faraday's law. Measure spectra, current, field phase and total energy independently.
9. Retain the calibrated coframe/connection pair for Frank–Burgers defects. Do not infer torsion or curvature holonomy from an uncalibrated phase or magnetic texture.
10. Use T107's equilibrium/response protocol for FDR. A finite graph alone supplies neither a material temperature nor a physical transport coefficient.

## 8. Claim ledger — audit FDT

| Claim | Status | Promotion criterion |
|---|---|---|
| (T_K^TT_K=2I), (T_K^2=2R_{-90^circ}), and the stated quaternionic lift | `proved` | Exact algebraic identities |
| Cartan definitions (T^A=De^A), (R^{AB}=domega^{AB}+omega^A{}_Cwedgeomega^{CB}) | `proved` | Differential-geometric identities |
| Torsion-trace equation follows from the displayed effective action | `proved` | Conditional Euler–Lagrange calculation |
| Minimal ECSK torsion is algebraic | `proved` | Standard result under minimal assumptions |
| A kinetic trace-torsion extension can carry a propagating mode | `interpretive` | Constraint and stability analysis |
| (alpha) is the local FDT density-cone field and (Psi=sqrt{ho_*}alpha e^{iphi}) its realization | `interpretive` | Compare with the FDT source corpus |
| FDT (F_{max}alpha_1alpha_2) is generated by this bulk action | `open` | Source functional and conservative potential absent |
| Hopf fibre is identical to electromagnetic (U(1)) | `open` | Bundle/charge map absent |
| Medium vorticity is electromagnetic induction | `open` | Only a mixed effective term is proposed |
| FDT vorticity is Cartan torsion | `open` | No constitutive map derived |
| Kathara is a symmetry of the full extended action | `open` | Field representation and connection transformation absent |
| Q6 continuum field is physically equivalent to the FDT amplitude | `open` | Interpolation/measurement map absent |
| RGS triplet anisotropy is a new physical force | `open` | Operator observation is not a calibrated force measurement |

## 9. Conclusion

This is not “ECSK plus a new name for torsion”. It is a layered candidate theory with an independent coframe/connection, FDT density/amplitude/Hopf sector, medium-vorticity sector, Maxwell electrodynamics, an optional propagating torsion-trace mode, and a discrete Q6/RGS/Kathara correspondence that still requires an intertwiner.

Turning off (g_{Talpha}), removing the torsion kinetic term, setting (lambda_{BF}=0), and decoupling the FDT fields recovers the corresponding reference sectors. New physics exists only if the extra coefficients yield stable, gauge-consistent, causal and independently measurable deviations.

**No laboratory effect, vacuum-energy extraction, superluminal signal or propagating torsion detection is claimed by this record.**


## 10. Experimental and mathematical validation dependencies

S011 does not absorb the following work as established evidence. These four open repository issues are the validation work packages; their outputs may constrain or falsify sectors of this action.

| Work package | Role in S011 | Required evidence before use as a physical input |
|---|---|---|
| [#109 — 188D/Krist-All source-data recovery](https://github.com/fabianleonaressi95/theorem/issues/109) | Establish provenance and reproducibility of the RGS operator data and Krist-All claims used in §5 | Commit original binary artifacts with hashes and provenance; regenerate the 188D report from committed arrays; recover the original 64×3 coordinates from their generator; independently reproduce the Krist-All enumerator, equivalence relation, operator definitions and tests, or withdraw unsupported counts/residuals |
| [#84 — Q6–D5 Wilson integer fibre](https://github.com/fabianleonaressi95/theorem/issues/84) | Certify the discrete Q6 measure/fibre construction before proposing a continuum density interpretation | Exact rational/integer incidence and saturated-kernel certificates; unimodular splitting; explicit positive fibre sum; rigorous tail interval; Poisson/Gaussian comparison with stated regime. No continuum FDT identification follows from the finite quotient alone |
| [#114 — Jiles–Atherton measured magnetic loops](https://github.com/fabianleonaressi95/theorem/issues/114) | Independent magnetic-material benchmark for the Maxwell/material-response side; not a test of torsion by itself | Verify exact dataset version, files, checksum, licence, units, frequency, temperature and geometry; fit training loops and report held-out loops/specimens, loop area, coercivity, remanence, saturation and error; keep quasi-static and dynamic losses separate |
| [#113 — experimental actuator hysteresis/GPI](https://github.com/fabianleonaressi95/theorem/issues/113) | Independent test of memory-bearing constitutive dynamics and possible industrial relevance; distinct from magnetic hysteresis | Verify Zenodo version/checksum/schema and trial/cycle boundaries; compare Preisach, PI, asymmetric GPI and Bouc–Wen on identical complete-cycle splits; report held-out-cycle errors, loop-area/branch/reversal errors, uncertainty and runtime. No industrial qualification follows from fit quality alone |

### 10.1 Execution order and dependency logic

**Stage A — provenance first:** close the source-data gaps in #109. Until then, 188D/Krist-All quantities remain reported audit values with explicit provenance limitations, not newly regenerated independent evidence.

**Stage B — exact discrete measure:** complete #84. Only after the full integer-fibre sum and remainder are certified may it be used as a controlled discrete measure in a continuum-limit study. The Q6 quotient alone is not a derivation of the local FDT field \(\alpha(x)\).

**Stage C — material validation in two separate tracks:** complete #114 for measured ferromagnetic loops and #113 for pneumatic actuator loops. Do not train Jiles–Atherton on actuator outputs, and do not treat pneumatic GPI/Preisach parameters as magnetic material constants. Both tracks must use held-out complete loops/cycles and preserve raw-data provenance.

### 10.2 How the results can constrain S011

- #109 can validate or force revision of the RGS operator inputs and the triplet anisotropy statement in §5.
- #84 can validate the exact Q6 lattice measure, but an interpolation \(I_h\), normalization map and continuum convergence proof are still required to connect it to \(\Psi\) or \(\alpha\).
- #114 can constrain ordinary magnetic constitutive response and the Maxwell/material sector. A successful Jiles–Atherton fit is not evidence for propagating torsion, aether flow or a new electromagnetic coupling.
- #113 can quantify hysteretic memory in a real actuator and its predictive limits. It does not by itself identify the memory variable with Cartan torsion or FDT density.

No fitted parameter from these issues is to be inserted into \(\lambda_{BF}\), \(g_{T\alpha}\), \(m_T\), or an RGS–FDT coupling without a separately derived parameter map and an independent measurement. The four issues are therefore **validation dependencies**, not confirmation of S011.

