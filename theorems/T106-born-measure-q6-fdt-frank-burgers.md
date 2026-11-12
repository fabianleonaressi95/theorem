# T106 — Born measure, Q6 phase torus, fluctuation–dissipation, and Frank–Burgers defects

**Classification:** (A) exact Haar/Born push-forward theorem (known result, restated and specialized to 64 labelled outcomes); (B) exact Q6 indexing and Dirichlet moment identities; (C) conditional classical fluctuation–dissipation/Kubo relations; (D) exact continuum defect definitions under calibrated elasticity/frame data; (E) open RGS–Q6 physical correspondence.

**Dependencies:** T100 (hypercube–moiré response, Green–Kubo and defects), T101 (two-circle phases and plaquette winding), T104 (cycle–cocycle–holonomy), T105 (hexagram-resolved charge and two-field interference).

**Source motivation:** Greg Kuperberg, “Archimedes’ other principle and quantum supremacy” (Scott Aaronson’s Shtetl-Optimized, 26 Nov 2019). The Born-measure result is not claimed as new. T106 records its exact 64-outcome form and specifies what additional structures are required before coupling it to FDT or material defects.

## 1. Complex Born map and its exact push-forward measure

Let \(d\geq2\), and let
\[
z=(z_0,\ldots,z_{d-1})\in\mathbb C^d,\qquad
\sum_{j=0}^{d-1}|z_j|^2=1.
\]
Equip \(S^{2d-1}\subset\mathbb C^d\) with normalized unitary-invariant (Haar) surface measure \(\sigma_d\). Define
\[
\mathcal B:S^{2d-1}\longrightarrow\Delta^{d-1},\qquad
\mathcal B(z)_j=|z_j|^2,
\]
where
\[
\Delta^{d-1}=\{p_j\geq0:\ \sum_jp_j=1\}.
\]

**Born–simplex theorem (Kuperberg/Sýkora).**
\[
\boxed{\quad (\mathcal B)_*\sigma_d
=\operatorname{Dirichlet}(1,\ldots,1)
=\operatorname{Unif}(\Delta^{d-1}).\quad}
\]
The uniformity is with respect to the ordinary \((d-1)\)-dimensional Lebesgue measure on the simplex. This statement concerns Haar-random pure states; it is not a statement about arbitrary state-preparation ensembles, mixed states, or thermal equilibrium.

A direct measure calculation writes \(z_j=r_je^{i\theta_j}\). For each complex coordinate,
\[
dx_j\,dy_j=r_j\,dr_j\,d\theta_j,\qquad p_j=r_j^2,\qquad dp_j=2r_j\,dr_j.
\]
After integrating each angular variable, the radial measure becomes a constant multiple of \(dp_j\). Restricting to \(\sum_jp_j=1\) therefore gives constant density on the simplex. The factor-of-two-dimensionality is essential: for real amplitudes, the push-forward is instead
\[
(p_0,\ldots,p_{d-1})\sim
\operatorname{Dirichlet}\left(\tfrac12,\ldots,\tfrac12\right),
\]
not the uniform simplex law.

Equivalently, take independent standard complex Gaussian variables \(g_j\) with density proportional to \(e^{-|g_j|^2}\), and set \(z=g/\|g\|\). Then \(p_j=|g_j|^2/\sum_k|g_k|^2\), with independent exponential numerators. This gives the same Dirichlet law.

## 2. Exact specialization to the 64 individual hexagrams

Set \(d=64\), and label coordinates by the six-bit hexagrams
\[
h=(b_0,\ldots,b_5)\in\{0,1\}^6=V(Q_6).
\]
For a normalized complex state
\[
|\psi\rangle=\sum_{h=0}^{63}z_h|h\rangle,
\]
the Born probabilities are
\[
p_h=|z_h|^2,\qquad \sum_{h=0}^{63}p_h=1.
\]
Thus
\[
\boxed{\quad S^{127}\subset\mathbb C^{64}
\xrightarrow{\ \mathcal B\ }\Delta^{63},\qquad
(\mathcal B)_*\sigma_{127}=\operatorname{Dirichlet}(1^{64}).\quad}
\]

The exact first and second moments are
\[
\mathbb E[p_h]=\frac1{64},
\]
\[
\operatorname{Var}(p_h)=\frac{63}{64^2\cdot65},\qquad
\operatorname{Cov}(p_h,p_k)=-\frac{1}{64^2\cdot65}\quad(h\ne k).
\]
The marginal law is \(p_h\sim\operatorname{Beta}(1,63)\), with density
\[
f(p)=63(1-p)^{62},\qquad 0\leq p\leq1.
\]
For \(x=64p_h\), the finite-\(64\) density is
\[
f_{64}(x)=\frac{63}{64}\left(1-\frac{x}{64}\right)^{62},
\quad 0\leq x\leq64,
\]
which approaches \(e^{-x}\) in the large-dimension limit. The exponential/Porter–Thomas profile is therefore an asymptotic marginal statement, not an exact finite-\(64\) identity.

The established bijection
\[
(b_0,\ldots,b_5)\longleftrightarrow
(k_1,k_2,k_3)\in\mathbb Z_4^3,\qquad
k_1=2b_0+b_1,\quad k_2=2b_2+b_3,\quad k_3=2b_4+b_5
\]
is an exact indexing of the 64 outcomes by a \(4\times4\times4\) discrete torus. It does **not** identify the 64 independent complex phases with only three phases. The state has 64 amplitudes and 64 coordinate phases before quotienting the common global phase.

For \(p_h>0\), write
\[
z_h=\sqrt{p_h}\,e^{i\theta_h}.
\]
The Haar measure disintegrates into uniform simplex measure for \(p\) and independent uniform coordinate phases \(\theta_h\in S^1\). Modding out the physically irrelevant common phase leaves \(T^{63}\) of relative phases over the interior of \(\Delta^{63}\). On simplex boundary strata, one or more amplitudes vanish and their phases cease to be defined. The finite set \(\mathbb Z_4^3\) is the label geometry; the phase fibre is generically \(T^{63}\), not \(\mathbb Z_4^3\).

## 3. What the Born map does — and does not — say about Q6 correlations

The Born theorem determines the one-state probability-vector distribution under Haar sampling. It does not determine the dynamics, spatial embedding, or time correlations of a Q6 model.

For each state, define the rank-one density matrix
\[
\rho_{hk}=z_h\overline{z_k}
=\sqrt{p_hp_k}\,e^{i(\theta_h-\theta_k)}.
\]
The diagonal entries are \(p_h\); off-diagonal entries retain relative-phase information. The graph \(Q_6\) selects 192 distinguished pairs \((h,k)\) on which nearest-neighbour phase and coherence observables may be measured. The 240 square faces select elementary loop tests. Neither adjacency nor face incidence changes the Born push-forward theorem.

For Haar-random pure states, unitary invariance gives
\[
\mathbb E[\rho]=\frac{I_{64}}{64},
\qquad
\mathbb E[\rho_{hh}\rho_{kk}]
=\frac{1+\delta_{hk}}{64\cdot65}.
\]
For \(h\ne k\), \(\mathbb E[\rho_{hk}]=0\). These are ensemble moments, not dynamical FDT correlations.

A crucial distinction for defects: if a single-valued vertex phase \(\theta:V(Q_6)\to S^1\) defines edge transports
\[
U_{hh'}=e^{i(\theta_{h'}-\theta_h)},
\]
then the product of \(U\) around every graph cycle is exactly one: this is a pure-gauge coboundary. A nonzero integer obtained by summing principal-value edge increments can record branch winding of a chosen lift, but it is not by itself nontrivial \(U(1)\) holonomy or a material defect. A physical vortex/dislocation requires a spatial interpolation, a singular core/puncture, or an independently measured connection/order parameter with a calibrated loop interpretation. This distinction must be preserved alongside T104's separate \(\mathbb F_2\) holonomy.

## 4. The conditional bridge to fluctuation–dissipation theory

Let a classical equilibrium model have Hamiltonian \(H_0\), inverse temperature \(\beta=(k_BT)^{-1}\), and observables \(A_a\). Perturb it by fields \(f_b(t)\) conjugate to observables \(X_b\):
\[
H(t)=H_0-\sum_b f_b(t)X_b.
\]
In the classical linear-response regime, under the equilibrium and regularity assumptions of Kubo theory,
\[
\delta\langle A_a(t)\rangle
=\sum_b\int_{-\infty}^{t}R_{ab}(t-s)f_b(s)\,ds,
\]
\[
\boxed{\quad R_{ab}(t)=
\beta\,\Theta(t)\,
\left\langle A_a(t)\,\dot X_b(0)\right\rangle_{\rm eq}\quad}
\]
for the stated perturbation convention. Equivalent forms may move derivatives between correlation functions under stationarity, time-reversal, and boundary assumptions; signs must be checked against the chosen \(H'= -fX\) convention. Static equilibrium response is
\[
\frac{\partial\langle A_a\rangle}{\partial f_b}\bigg|_{f=0}
=\beta\,\operatorname{Cov}_{\rm eq}(A_a,X_b)
\]
when the ensemble is canonical and the observables have no explicit field dependence.

For transport, the Green–Kubo formula is the corresponding current-correlation relation, with the physical current, units, volume normalization, and any quantum contact/diamagnetic terms specified. T100 and T105 already impose an independent small-field-response check; T106 does not replace that check.

### 4.1 The precise relation to the Born/Haar measure

The Haar measure on \(S^{127}\) is a mathematically defined invariant measure, not automatically a Gibbs measure at temperature \(T\). Unitary evolution preserves Haar measure but is not, by itself, a dissipative thermalization mechanism. Therefore:
- Born/Haar push-forward is exact geometry/probability;
- FDT is a relation between equilibrium fluctuations and response of a specified dynamical system;
- one cannot infer FDT from the Born theorem alone, nor infer a Haar ensemble from a measured FDT.

A consistent **model construction** is possible: consider reversible overdamped diffusion on \(S^{127}\) with generator proportional to the Laplace–Beltrami operator. Its stationary measure is Haar surface measure. Add a weak potential \(-\sum_b f_b X_b(z)\) and choose the corresponding gradient drift/noise so that the perturbed stationary measure is proportional to
\[
\exp\!\left(\beta\sum_b f_bX_b(z)\right)d\sigma_{127}(z).
\]
This model satisfies detailed balance and admits the classical FDT. Its zero-field Born probabilities have the uniform-simplex law. It is a stochastic model on the pure-state sphere, **not** ordinary closed-system Schrödinger evolution and not a claim about a quantum circuit's physical noise. Any physical use requires a separately justified dynamics and noise model.

## 5. Frank and Burgers data: distinct order parameters and loop observables

A material dislocation and a material disclination are different defects.

### 5.1 Dislocation: translational order and Burgers vector

Given a calibrated reciprocal vector \(G\) and a complex translational density-wave order parameter
\[
\Psi_G(x)=|\Psi_G(x)|e^{i\theta_G(x)},
\]
a loop \(\Gamma\) around a defect core has phase winding
\[
\oint_\Gamma d\theta_G=2\pi m.
\]
For the displaced-wave convention
\[
\theta_G(x)=G\cdot(x-u(x)),
\]
the coordinate part closes and
\[
\boxed{\quad G\cdot b=-2\pi m,\qquad
b=\oint_\Gamma du.\quad}
\]
The sign changes if the Fourier/displacement convention is reversed. One reciprocal vector constrains only the projection \(G\cdot b\); recovering the full Burgers vector in two or three dimensions requires enough independent reciprocal vectors and a calibrated spatial frame.

### 5.2 Disclination: orientational order and Frank angle

Let \(\alpha(x)\) be a calibrated local lattice orientation. For an \(n\)-fold orientational order parameter
\[
\Psi_n(x)=|\Psi_n(x)|e^{in\alpha(x)},
\]
a loop winding \(m\in\mathbb Z\) gives
\[
\oint_\Gamma d(n\alpha)=2\pi m,\qquad
\boxed{\quad \Omega_F=\oint_\Gamma d\alpha=\frac{2\pi m}{n}.\quad}
\]
This is a rotational defect (Frank angle), not a translational closure failure.

### 5.3 Cartan geometry and the torsion/curvature split

For a calibrated coframe \(e^a\) and connection \(\omega^a{}_b\),
\[
T^a=de^a+\omega^a{}_b\wedge e^b,\qquad
R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\]
The translational closure failure is represented by integrated torsion; rotational holonomy is represented by curvature/connection holonomy. In a small-loop or distributional defect description, these encode Burgers and Frank data respectively, with convention-dependent signs and frame factors. They must not be collapsed into one scalar phase winding.

A further subtlety from classical defect theory is that disclination and dislocation content can mix in some continuous/discrete defect representations. In particular, the general Burgers characteristic vector of a combined defect need not equal the Burgers vector of an isolated dislocation line. T106 therefore requires the chosen defect representation (continuous density, discrete line, or loop density) to be declared before comparing vectors.

## 6. FDT applied to defect observables: a falsifiable response matrix

Once a material reconstruction exists, define defect observables, for example:
- \(\rho_d\): a translational/dislocation density or Burgers-density component;
- \(\rho_c\): an orientational/disclination density or Frank-density component.

Let their conjugate perturbations be specified physically (stress-like fields for translational distortion; torque/couple-stress-like fields for orientation). Denote the corresponding generalized observables by \(X_d,X_c\). The equilibrium correlation matrix is
\[
C_{ab}(t)=\langle\delta A_a(t)\delta A_b(0)\rangle_{\rm eq},
\qquad A=(\rho_d,\rho_c),
\]
and the response matrix is
\[
\chi_{ab}(t)=\frac{\delta\langle A_a(t)\rangle}{\delta f_b(0)}.
\]
Under the Kubo assumptions in §4,
\[
\chi_{ab}(t)=\beta\Theta(t)
\langle A_a(t)\dot X_b(0)\rangle_{\rm eq}.
\]
The off-diagonal entries test whether translational and rotational defect sectors are dynamically coupled. They do not prove that one defect is the other. A cross-response can also arise from elastic anisotropy, boundary conditions, coupled order parameters, or the chosen coarse-graining.

For the Q6 circuit realization, the corresponding sequence is:
1. record the 64 node-charge traces and the 192 oriented branch currents;
2. estimate equilibrium correlations only after stationarity and ensemble checks;
3. identify candidate translational and orientational order parameters from phase-resolved, spatially calibrated fields;
4. measure Burgers and Frank loop observables separately;
5. perturb with calibrated weak stress/drive and weak torque/orientational drive;
6. compare measured response kernels with the equilibrium Kubo correlations, using the same normalization and boundary conditions.

The existing thermal-RC noise covariance in T100/T105 is one model-specific FDT realization. It must not be silently reused for a mechanical defect field or for quantum dynamics.

### 6.1 Two-dimensional melting: the KTHNY bridge

If the eventual spatial realization is a two-dimensional crystal with the appropriate elastic and symmetry conditions, the Frank/Burgers split also connects to defect-mediated melting. In the KTHNY scenario:
- dislocation-pair unbinding first destroys quasi-long-range translational order while sixfold orientational order can remain quasi-long-range, producing a hexatic regime;
- subsequent disclination unbinding destroys the orientational order and produces the isotropic liquid.

This is a conditional phase-transition scenario, not a universal law for every 2D material: interaction potentials, anisotropy, defect-core energies and grain-boundary proliferation can alter or pre-empt the two-step sequence.

The measurable bridge to FDT is through translational and orientational susceptibilities. Define translational and bond-orientational order parameters, their equilibrium correlation functions, and the corresponding responses to weak stress and torque. Under equilibrium linear response, the susceptibilities are related to the appropriate time-dependent correlations by Kubo/FDT. In a KTHNY-like regime, changes in the defect populations and correlation lengths should be accompanied by changes in these susceptibilities. The topology labels the defects (Burgers/Frank); FDT quantifies how their order-parameter sectors fluctuate and respond. Neither relation says that FDT creates the defects or that a susceptibility peak alone proves a KTHNY transition.

For a sixfold orientational field, use \(\Psi_6=|\Psi_6|e^{i6\alpha}\). Its elementary orientational winding is \(2\pi/6\) in \(\alpha\). Translational order requires independent reciprocal vectors \(G\) and fields \(\Psi_G\); do not infer Burgers vectors from \(\Psi_6\) alone.


## 7. Relation to moiré and the two registered phase fields

For two coherent reconstructed modes
\[
\psi_\pm(x)=A_\pm(x)e^{i(G_\pm\cdot x+\phi_\pm(x))},
\]
the cross term in the intensity depends on
\[
q_m=G_+-G_-,\qquad \Delta\phi=\phi_+-\phi_-.
\]
The moiré phase is therefore a relative phase field. If one mode is a translational density-wave order parameter, its singularities can encode dislocations through its Burgers projection. If a separately reconstructed local frame supplies an orientational order parameter, its winding can encode disclinations/Frank angle. A scalar moiré intensity alone is insufficient to reconstruct both: phase-sensitive complex fields and local-frame information are required.

The two-circle phase lift of T101/T105 is a discrete input to this programme, not yet a calibrated translational density wave or local-frame orientation. Its 64 ordered pairs can be correlated with charge and circuit current, but a material Frank/Burgers assignment remains open until the physical map is measured.

## 8. Exact, conditional, and open statements

**Exact / known theorem**
- Haar-random complex pure states map under Born probabilities to the uniform measure on the probability simplex (Kuperberg/Sýkora).
- For 64 outcomes, the law is \(\operatorname{Dirichlet}(1^{64})\), with the moments in §2.
- The six-bit-to-\(\mathbb Z_4^3\) map is a bijective relabelling; it does not reduce the 64-dimensional amplitude vector to three amplitudes.
- A vertex-phase coboundary has trivial \(U(1)\) Wilson holonomy on every cycle.

**Conditional standard theory**
- Classical Kubo/FDT and Green–Kubo require equilibrium, specified dynamics, conjugate perturbations, and linear response.
- Burgers and Frank observables require calibrated translational and orientational order, respectively.
- Cartan torsion/curvature encode translational/rotational defect content only after a coframe, connection, and defect convention are fixed.

**Open RGS–Q6 hypotheses**
- whether measured two-circle fields define translational and/or orientational order parameters;
- whether their phase-charge correlations predict the 64 measured charges out of sample;
- whether moiré singularities correspond to material dislocations/disclinations;
- whether Q6 defect observables obey a measurable FDT with the proposed circuit or material dynamics;
- whether cross-response between Frank and Burgers sectors is nonzero after controls for elastic coupling and anisotropy.

No physical defect, transport coefficient, or constitutive charge law is declared proved by T106.

## 9. Related Shtetl-Optimized context and scope of the blog connection

The linked 2019 guest post is the direct source for the geometric Haar/Born push-forward argument. Other relevant posts on the same blog sharpen the interpretation but do not supply the FDT or crystal-defect theory:

- In “The quantum state cannot be interpreted as something other than a quantum state” (2011), Aaronson discusses the Pusey–Barrett–Rudolph result and the distinction between pure and mixed states. This is about ontological/statistical interpretations under preparation-independence assumptions, not a derivation of the Dirichlet push-forward law.
- In “Interpretive cards (MWI, Bohm, Copenhagen: collect ’em all)” (2018), Aaronson notes that once the unitary structure and 2-norm are fixed, there are multiple mathematical arguments for the Born probabilities; the discussion also treats quantum equilibrium in Bohmian mechanics. This reinforces that Kuperberg's theorem is a measure theorem **given** the Born map, not a derivation of the Born rule from Q6, FDT, or mechanics.
- In “Quantum Information Supremacy” (2025), Aaronson and collaborators discuss a resource separation between qubits and classical memory. The post and comments concern information/communication complexity and entangled-state resources; they do not imply that a Q6 circuit samples Haar measure or that a finite circuit is Haar-random.

Targeted searches of the related blog material did not identify a treatment of the fluctuation–dissipation theorem, Frank angles, or Burgers vectors. Those connections in T106 therefore come from the independent linear-response and continuum-defect literature cited above, not from attributing those theories to Aaronson or Kuperberg.

The correct chain is consequently:
\[
\text{Haar pure-state ensemble}
\xrightarrow{\text{Born map}}
\text{uniform simplex law}
\]
and, separately, for a specified equilibrium dynamics,
\[
\text{equilibrium correlations}
\xrightarrow{\text{Kubo/FDT}}
\text{linear response}.
\]
Only after spatial and frame reconstruction can the measured phase fields be assigned translational Burgers or rotational Frank data. These are linked research interfaces, not one theorem that derives all four structures from the Born map.

## References

1. G. Kuperberg, “Archimedes’ other principle and quantum supremacy,” Shtetl-Optimized, 26 Nov 2019, https://scottaaronson.blog/?p=4432.
2. S. Sýkora (1974), generalized Archimedes/Born-map result cited by Kuperberg; full primary-publication metadata remains to be verified before formal citation in a paper.
3. R. Kubo, “The fluctuation-dissipation theorem,” *Reports on Progress in Physics* 29 (1966), 255–284, DOI: 10.1088/0034-4885/29/1/306.
4. R. deWit, “Theory of Disclinations: II. Continuous and Discrete Disclinations in Anisotropic Elasticity,” *Journal of Research of the National Bureau of Standards A* 77A (1973), 49–100, DOI: 10.6028/jres.077A.003.
5. R. deWit, “Theory of Disclinations: III. Continuous and Discrete Disclinations in Isotropic Elasticity,” *Journal of Research of the National Bureau of Standards A* 77A (1973), 359–368, DOI: 10.6028/jres.077A.024.
6. J. M. Kosterlitz, “Kosterlitz–Thouless physics: a review of key issues,” *Reports on Progress in Physics* 79 (2016), 026001, DOI: 10.1088/0034-4885/79/2/026001.

Bibliographic note: the exact Sýkora reference is deliberately flagged for verification rather than supplied from uncertain metadata. The mathematical statement is independently derivable by the complex-Gaussian/exponential construction in §1.
