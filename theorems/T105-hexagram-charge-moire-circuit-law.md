# T105 — Hexagram-resolved charge, two-field moiré coupling, and circuit response

**Classification:** exact finite-graph and finite-circuit identities under the stated orientation and positivity assumptions; exact phase-lift definitions; conditional linear-response formula; experimentally testable constitutive hypothesis. This record does not claim that a charge law, moiré embedding, or material defect has already been measured.

**Dependency:** T099 (Q6 Kirchhoff network), T100 (64-node charge correlations and thermal-RC benchmark), T101 (two-circle trigram phases lifted to 64 hexagrams), and T104 (cycle–cocycle–holonomy law).

## 1. The 64 hexagrams are the measurement sites

Write each six-bit hexagram as
\[
h=(\ell,u)\in\{0,1\}^3\times\{0,1\}^3,\qquad
\ell=h\bmod 8,\quad u=\lfloor h/8\rfloor.
\]
The 64 values of \(h\) remain distinct physical/model measurement sites. The two trigram factors label the two line families; they do not replace the 64-site state space.

The graph is
\[
Q_6=Q_3^-\square Q_3^+,
\]
with 64 vertices and 192 edges: 96 lower-line edges and 96 upper-line edges. Let \(B\in\mathbb R^{64\times192}\) be the oriented incidence matrix, with \(+1\) at the tail and \(-1\) at the head of each oriented edge. Let \(G=\operatorname{diag}(g_e)\), \(g_e>0\), and \(C=\operatorname{diag}(c_h)\), \(c_h>0\). Then
\[
L_G=BGB^\top,\qquad L_G\succeq0,\qquad \ker L_G=\operatorname{span}\{\mathbf1\}.
\]

The measured node charge and voltage are related by
\[
Q(t)=CV(t),\qquad V(t)=C^{-1}Q(t).
\]
For an oriented edge \(e=(h,h')\), define
\[
j_e(t)=g_e\big(V_h(t)-V_{h'}(t)\big).
\]
With source/sink vector \(s(t)\), Kirchhoff continuity is
\[
\dot Q(t)+Bj(t)=s(t),\qquad
j=GB^\top V,
\]
or equivalently
\[
\boxed{\dot Q+L_GC^{-1}Q=s.}
\]
Summing over all 64 sites gives
\[
\frac{d}{dt}\sum_{h=0}^{63}Q_h(t)=\sum_hs_h(t).
\]
Thus total charge is conserved for a source-free circuit. These identities follow from \(\mathbf1^\top B=0\), not from a continuum approximation.

**Measurement rule:** record \(Q_h(t)\) separately for every one of the 64 hexagrams. Do not infer the 64 charges from eight trigram averages. If an intrinsic label charge \(q(h)\) and a time-dependent occupation \(n_h(t)\) are used instead, state the constitutive convention \(Q_h(t)=q(h)n_h(t)\) and measure/derive all 64 values of \(q(h)\); no numerical \(q(h)\) is assigned by this theorem.

## 2. Two measured circle fields lifted to each hexagram

Let \(\alpha^+_t\) and \(\alpha^-_t\), \(t=0,\ldots,7\), be the eight measured angular phases on the two registered circles. Let \(\chi\) be the calibrated frame offset and \(\sigma\in\{-1,+1\}\) the calibrated relative orientation. Define the eight complement residuals
\[
\epsilon_t=\operatorname{wrap}\!\left(
\alpha^-_{t\oplus7}-\sigma\alpha^+_t-\chi
\right)\in(-\pi,\pi].
\]
For every individual hexagram \(h=(\ell,u)\), lift the two fields as the ordered pair
\[
E_h=(\epsilon_\ell,\epsilon_u)\in(S^1)^2.
\]
This gives 64 two-component observations. It preserves the two field components and the identity of all 64 hexagrams. The construction is the T101 phase-lift definition; it does not by itself assign electric charge.

A charge–phase constitutive relation is therefore stated as a testable map, not silently assumed:
\[
Q_h(t)=\mathcal F_h\!\left(E_h,\mathcal X_h(t),\lambda\right)+\xi_h(t),
\]
where \(\mathcal X_h\) denotes any additionally measured local circuit variables, \(\lambda\) is a declared parameter vector, and \(\xi_h\) is a residual/noise term. The null model is that \(Q_h\) is independent of \(E_h\) after conditioning on declared circuit controls. A nonzero phase–charge relation must survive out-of-sample tests, calibration uncertainty, and comparison with the 64-site unconstrained baseline. No universal function \(\mathcal F\) is asserted in the absence of data.

## 3. Charge and phase correlations on the 64 sites

For an equilibrium or stationary ensemble, define
\[
\delta Q_h(t)=Q_h(t)-\langle Q_h\rangle,\qquad
C_{hh'}(\tau)=
\left\langle\delta Q_h(t+\tau)\delta Q_{h'}(t)\right\rangle.
\]
The complete observable is the \(64\times64\) matrix \(C(\tau)\), not an eight-by-eight trigram correlation. Also define the two-component phase–charge cross-correlation
\[
K_{h,a}(\tau)=
\left\langle\delta Q_h(t+\tau)\,
\delta E_{h,a}(t)\right\rangle,\qquad a=1,2,
\]
where angular residuals must be unwrapped or represented by circular statistics before ordinary covariance is used. For circular data, a safe elementary diagnostic is the complex moment
\[
K^{\rm circ}_{h,a}(\tau)=
\left\langle\delta Q_h(t+\tau)e^{iE_{h,a}(t)}\right\rangle.
\]
The chosen estimator, centering convention, sampling interval, stationarity window, and uncertainty method must be reported.

When no physical embedding is available, analyze \(C(\tau)\) in graph modes of \(L_G\). Only after a calibrated map \(X:V(Q_6)\to\mathbb R^d\) is supplied may one define
\[
S(k,\omega)=\sum_{h,h'}e^{-ik\cdot(X_h-X_{h'})}
\int_{\mathbb R}e^{i\omega\tau}C_{hh'}(\tau)\,d\tau.
\]
This prevents an abstract Q6 adjacency relation from being mistaken for a physical distance or reciprocal lattice.

## 4. Moiré is the interference of the two reconstructed fields

Given two phase-resolved spatial reconstructions
\[
\psi_\pm(x)=A_\pm(x)e^{i(G_\pm\cdot x+\phi_\pm(x))},
\]
their coherent superposition has intensity
\[
I(x)=|\psi_+(x)+\psi_-(x)|^2
=|A_+|^2+|A_-|^2+
2\operatorname{Re}\!\left[
A_+\overline{A_-}e^{i(q_m\cdot x+\Delta\phi(x))}
\right],
\]
where
\[
q_m=G_+-G_-,\qquad \Delta\phi=\phi_+-\phi_-.
\]
For constant amplitudes and phases, the fringe spacing is
\[
\Lambda_m=\frac{2\pi}{|q_m|}.
\]
For two equal-length reciprocal vectors separated by angle \(\vartheta\),
\[
|q_m|=2|G|\left|\sin\frac{\vartheta}{2}\right|,
\qquad
\Lambda_m=\frac{\pi}{|G|\,|\sin(\vartheta/2)|}.
\]

The Q6 data can determine the amplitudes and phases only through a declared reconstruction operator, for example
\[
\psi_\pm(x)=\sum_{h=0}^{63}w^\pm_h(x)\,a^\pm_h,
\]
where \(a^\pm_h\) are measured complex amplitudes and \(w^\pm_h(x)\) are specified interpolation/basis functions. The 64-site charge and phase measurements are retained as inputs. Neither \(G_\pm\), the embedding \(X_h\), nor the interpolation weights are universal consequences of the graph. The moiré wavevector is thus a derived quantity of a calibrated reconstruction, not a geometric constant inserted by hand.

## 5. Green–Kubo transport and the independent response check

For a declared spatial embedding \(X_h\), orient each edge \(e=(h,h')\) and set \(d_e=X_h-X_{h'}\). The extensive current flux is
\[
\mathcal J_a(t)=\sum_{e=1}^{192}d_{e,a}j_e(t).
\]
For a classical equilibrium model with the appropriate extensive-flux convention, the transport tensor is
\[
\kappa_{ab}=
\frac{1}{k_BT\,\mathcal V}
\int_0^\infty
\langle\mathcal J_a(t)\mathcal J_b(0)\rangle_{\rm eq}\,dt.
\]
For electrical conductivity, \(\mathcal J\), its units, and the prefactor must be chosen for the actual electrical realization. A quantum system requires the Kubo commutator and any diamagnetic/contact terms; the classical expression above is not a quantum formula.

For the specific overdamped thermal-RC model with energy \(H(Q)=\tfrac12Q^\top C^{-1}Q\), the Langevin forcing covariance on the dissipative subspace is
\[
\langle\eta(t)\eta(t')^\top\rangle
=2k_BT L_G\,\delta(t-t'),
\]
with the constant mode projected out or separately constrained. This is a model-specific fluctuation–dissipation choice. A valid Green–Kubo audit must compare the integrated equilibrium current correlation with an independently computed small-field linear response using the same geometry, normalization, and boundary conditions. The graph pseudoinverse \(L_G^\dagger\) is not itself a Green–Kubo integral.

## 6. Defects: keep phase winding, Burgers, Frank, and T104 holonomy distinct

For an oriented plaquette \(p\) of Q6 and a lifted phase component, define the principal-increment winding
\[
n_p=\frac{1}{2\pi}\sum_{e\in\partial p}^{\rm oriented}
\operatorname{wrap}(\Delta_e E)\in\mathbb Z,
\]
provided the branch convention is fixed and the quantization residual is checked. This is a discrete phase-vortex index. It is not automatically a material defect.

- **Dislocation:** requires a calibrated translational density-wave phase with reciprocal vector \(G\), or a reconstructed displacement \(u\). Then \(G\cdot b\in2\pi\mathbb Z\) and \(b=\oint_\Gamma du\).
- **Disclination:** requires a calibrated local-frame orientation and rotational symmetry. Its Frank angle is the rotational holonomy \(\Omega=\oint_\Gamma\omega\).
- **T104 magnetic holonomy:** requires a separately declared \(\mathbb F_2\) edge connection \(a\), with plaquette flux \(\delta_1a\). Do not identify \(a\) with a thresholded phase increment or a current sign unless that quantization map is explicitly calibrated and tested.

The phase winding, translational closure, rotational holonomy, and \(\mathbb Z_2\) flux are different observables. Their correspondence is a further theorem only after the measurement maps are supplied.

## 7. Falsifiable protocol and acceptance criteria

A complete data package must contain:

1. 64 synchronized node-charge traces \(Q_h(t)\), with units, calibration, sampling interval, uncertainty, and missing-data policy;
2. two arrays of eight measured phases \(\alpha^\pm_t\), plus calibrated \(\chi\), \(\sigma\), phase convention, and uncertainty;
3. 192 edge conductances \(g_e\), 64 capacitances \(c_h\), source vector \(s(t)\), and the declared incidence orientation;
4. a spatial embedding \(X_h\), or an explicit statement that only graph-mode analysis is performed;
5. for Green–Kubo, a stationary equilibrium window, temperature, current convention, volume/area normalization, and an independent small-field response measurement;
6. for material defects, phase unwrapping, local-frame or displacement reconstruction, and loop/refinement stability data.

The audit must report: (i) Kirchhoff continuity residuals; (ii) all 64 node means and the full \(64\times64\) correlation matrix; (iii) all 64 two-component phase lifts and phase–charge cross-correlations; (iv) the two reconstructed fields and measured moiré wavevector; (v) current autocorrelation and Green–Kubo/linear-response discrepancy; and (vi) separate phase-vortex, Burgers, Frank, and \(\mathbb F_2\)-flux diagnostics.

**Acceptance gate:** no charge law is accepted from symmetry counting alone; no moiré scale is accepted without calibrated reciprocal vectors; no Green–Kubo coefficient is accepted without an independent response check; no Frank/Burgers label is accepted without frame/spatial calibration. Synthetic fixtures test software only.

## 8. Exact content and open physical claims

**Exact:** Q6 has 64 distinct vertices, 192 edges split 96+96, and the oriented-incidence Kirchhoff identity \(L_G=BGB^\top\); the two-circle phase residual and 64-site lift are well-defined once registration is calibrated; the two-wave interference and moiré formulas follow from the stated fields.

**Conditional/model-dependent:** thermal-RC equilibrium covariance, fluctuation–dissipation noise, Green–Kubo transport, and spatial reconstruction depend on the specified circuit, ensemble, and embedding.

**Open physical hypotheses:** the intrinsic constitutive charge \(q(h)\); a predictive phase-to-charge map \(\mathcal F_h\); the emergence of the two reciprocal fields from the circuit; and the identification of measured winding with material dislocations/disclinations. T105 makes these hypotheses measurable and falsifiable; it does not label them as proved.
