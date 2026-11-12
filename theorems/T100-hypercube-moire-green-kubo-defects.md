# T100 — Hypercube–moiré response, Green–Kubo transport, and geometric defects

**Status:** exact graph identities inherited from T099; continuum moiré identities are conditional on an explicit spatial embedding; Green–Kubo is a standard linear-response formula under equilibrium hypotheses; the Q6-to-defect correspondence is a research programme, not yet proved.

**Scope:** treat the 64 individual hexagrams as the primary charge-bearing degrees of freedom. Their charge correlations are the primary observables; edge currents describe charge transfer between hexagrams. Moiré structure, Green–Kubo transport, and geometric defects are derived or tested from these node-level data, subject to an explicit spatial reconstruction.

## 1. Discrete substrate: the two edge families of Q6

Let
\[
V(Q_6)=\{0,1\}^6=\{0,1\}^3\times\{0,1\}^3,
\qquad v=(\ell,u),
\]
where \(\ell\) and \(u\) encode the lower and upper trigrams. As established in T099,
\[
Q_6=Q_3^-\square Q_3^+,\qquad
L_6=L_-+L_+,
\]
with
\[
L_-=L_3\otimes I_8,\qquad L_+=I_8\otimes L_3
\]
in the tensor ordering where the upper factor is fastest. Under the lower-fastest indexing used in T099, the two Kronecker factors are exchanged. In either convention, there are 96 lower-line edges and 96 upper-line edges.

For nonnegative conductances \(g_-,g_+\), define
\[
L_g=g_-L_-+g_+L_+.
\]
This is a weighted graph Laplacian. It is positive semidefinite, and for \(g_-,g_+>0\) its kernel consists exactly of constants. These are finite graph facts; they do not yet define a spatial lattice or a moiré pattern.


## 2. Primary variables: charge on each individual hexagram

The 64 vertices are not merely labels for two collective trigram fields. The proposed constitutive law assigns an intrinsic charge (or charge-like observable) to each individual six-bit hexagram:
\[
q:V(Q_6)\to\mathbb R,\qquad h\mapsto q(h).
\]
Whether \(q(h)\) is electric charge, effective/coarse-grained charge, or a dimensionless observable—and its units—must be specified by the physical model. The 64 labels provide the domain of this map; its numerical rule is the central law to derive or measure, not a value to invent.

For a dynamical circuit or statistical model, introduce an occupation variable \(n_h(t)\) and define the measured node charge
\[
Q_h(t)=q(h)n_h(t),\qquad Q(t)=(Q_1(t),\ldots,Q_{64}(t))^T.
\]
This separates the intrinsic charge assigned to a hexagram from its time-dependent occupation. In a circuit with continuously varying stored charge, \(Q_h(t)\) is simply the dynamical node-charge variable; the constitutive interpretation of \(q(h)\) must then be supplied separately.

The primary equal-time and time-dependent correlation functions are
\[
C_{hh'}(\tau)=
\left\langle\delta Q_h(t+\tau)\,\delta Q_{h'}(t)\right\rangle_{\rm eq},
\qquad
\delta Q_h=Q_h-\langle Q_h\rangle_{\rm eq}.
\]
Thus correlations are measured **between individual hexagrams**, not inferred by first postulating two macroscopic fields. The diagonal \(C_{hh}(0)\) measures the variance of the measured charge on hexagram \(h\); off-diagonal entries measure correlations between distinct hexagrams. Dependence on graph distance, Hamming distance, and the lower/upper-line transition classes can be compared without conflating trigram decomposition with a 32/32 partition.

Let \(B\in\mathbb R^{64\times192}\) be an oriented incidence matrix of \(Q_6\), and let \(G=\operatorname{diag}(g_e)\) contain nonnegative edge conductances. With node potentials \(V=C_{\rm node}^{-1}Q\), where \(C_{\rm node}\) is a positive node-capacitance matrix, define oriented edge currents
\[
j(t)=G B^\top V(t).
\]
The charge-continuity equation is
\[
\dot Q(t)=-B j(t)+s(t)
=-BGB^\top C_{\rm node}^{-1}Q(t)+s(t),
\]
where \(s_h(t)\) is an explicitly specified source/sink term. Since \(BGB^\top=L_g\), this is the charge-variable form of the graph RC dynamics:
\[
\dot Q+L_g C_{\rm node}^{-1}Q=s.
\]
The total charge obeys
\[
\frac{d}{dt}\mathbf1^\top Q(t)=\mathbf1^\top s(t),
\]
so it is conserved when the net source vanishes. This conservation statement follows from \(\mathbf1^\top B=0\), independently of any moiré interpretation.

The Green–Kubo observable is then built from the currents that transfer charge along edges. Given a declared spatial embedding \(X:V(Q_6)\to\mathbb R^d\), let \(d_e=X(h_{\rm head})-X(h_{\rm tail})\). Define the extensive charge-current flux
\[
\mathcal J_a(t)=\sum_{e=1}^{192}d_{e,a}\,j_e(t).
\]
Its equilibrium autocorrelation, with normalization fixed by the chosen physical realization, is the transport observable. The node-charge correlations \(C_{hh'}(\tau)\) and edge-current correlations \(\langle j_e(t+\tau)j_{e'}(t)\rangle\) must both be recorded: they answer different questions and are linked by the continuity equation.

A useful spectral summary of the node correlations, once coordinates \(X_h\) are specified, is
\[
S(k,\omega)=
\sum_{h,h'}e^{-ik\cdot(X_h-X_{h'})}
\int_{-\infty}^{\infty}e^{i\omega\tau}
C_{hh'}(\tau)\,d\tau.
\]
Without a spatial embedding, the corresponding well-defined object is the graph-mode correlation matrix obtained by projecting \(C(\tau)\) onto eigenvectors of \(L_g\). Peaks in \(S(k,\omega)\), or structured cross-correlations between graph-mode sectors, may reveal a modulation or candidate moiré scale. They do not establish one until the embedding and reciprocal-space interpretation are independently specified.

## 3. Spatial reconstruction: the additional data moiré requires

The node-charge field (Q_h(t)) is primary. A moiré pattern is a possible spatial signature of its correlations, not a replacement for the 64 node variables. It is not determined by an abstract finite graph alone. Introduce, as explicit model data:

1. two spatial embeddings \(X_\pm:V(Q_6)\to\mathbb R^2\), or a declared common embedding together with two distinct reciprocal-mode families;
2. complex mode amplitudes \(a^\pm_v\);
3. reciprocal vectors \(G^\pm\in\mathbb R^2\), or more generally finite reciprocal sets \(\mathcal G_\pm\).

For the single-mode benchmark, define reconstructed fields
\[
\psi_\pm(x)=A_\pm(x)e^{i(G^\pm\cdot x+\phi_\pm(x))}.
\]
Their coherent intensity is
\[
I(x)=|\psi_+(x)+\psi_-(x)|^2
=|A_+|^2+|A_-|^2+
2\operatorname{Re}\!\left[
A_+\overline{A_-}\,e^{i(q_m\cdot x+\Delta\phi(x))}
\right],
\]
where
\[
q_m=G^+-G^-,
\qquad \Delta\phi=\phi_+-\phi_-.
\]
For constant amplitudes and phases, the fringe spacing normal to the fringes is
\[
\Lambda_m=\frac{2\pi}{|q_m|}\quad(q_m\ne0).
\]
For two rotated copies of a reciprocal vector of length \(G\), with relative angle \(\vartheta\),
\[
|q_m|=2G\left|\sin\frac{\vartheta}{2}\right|,
\qquad
\Lambda_m=\frac{\pi}{G|\sin(\vartheta/2)|}.
\]
This is the standard two-wave interference/moiré relation. It becomes a Q6-derived prediction only after \(G^\pm\), amplitudes and embeddings have been obtained from a specified eigenmode or reconstruction procedure on the graph. No such canonical map is asserted here.

For nonconstant amplitudes or several modes, the intensity contains the corresponding pairwise cross terms. A scalar intensity map alone generally loses phase information; defect reconstruction therefore requires access to the complex fields or an equivalent phase-sensitive observable.

## 4. Dynamics and Green–Kubo response

The static Kirchhoff equation \(L_gV=J\) from T099 does not by itself define an equilibrium time-correlation function. A dynamical model must be specified. One admissible linear circuit model is
\[
C_{\rm node}\dot V(t)+L_gV(t)=\eta(t)+J_{\rm ext}(t),
\]
where \(C_{\rm node}\) is a positive node-capacitance matrix, the constant-potential mode is treated consistently with total-charge conservation, and \(\eta\) is a stationary current-noise source. For the linear thermal RC model with energy \(H(Q)=\tfrac12Q^TC_{\rm node}^{-1}Q\), the equilibrium Langevin choice is \(\langle\eta(t)\eta(t')^T\rangle=2k_BT L_g\,\delta(t-t')\) on the dissipative subspace (with the zero mode projected out or separately constrained). This gives the fluctuation–dissipation relation for this particular overdamped model; other circuit realizations require their own noise covariance.

For an oriented edge \(e=(i,j)\), let
\[
j_e(t)=g_e\big(V_i(t)-V_j(t)\big)
\]
be the branch current, with the orientation fixed once. Given a spatial embedding \(X\), let \(d_e=X(j)-X(i)\). A macroscopic current observable can then be defined, for example, by
\[
\mathcal J_a(t)=\sum_{e}d_{e,a}\,j_e(t),
\]
where \(\mathcal J_a\) is the extensive flux; its physical meaning and units depend on the circuit realization and embedding. The Green–Kubo prefactor below then includes \(1/\mathcal V\).

For a classical system in equilibrium, the Green–Kubo transport tensor has the form
\[
\boxed{\;
\kappa_{ab}=
\frac{1}{k_BT\,\mathcal V}
\int_0^\infty
\left\langle \mathcal J_a(t)\mathcal J_b(0)\right\rangle_{\rm eq}\,dt
\;}
\]
when \(\mathcal J\) is the extensive flux convention appropriate to this prefactor. If an intensive current density is used instead, the volume factor must be changed accordingly. For electrical conductivity, the flux must be the properly normalized electric current and the prefactor must match the chosen microscopic convention. Quantum response requires the corresponding Kubo commutator and, where applicable, diamagnetic/contact terms; the classical formula above must not be relabelled as a quantum conductivity formula.

The graph Green operator \(L_g^\dagger\) and the Green–Kubo integral are different objects. In the linear deterministic RC model, the zero-mean propagator is
\[
e^{-C_{\rm node}^{-1}L_gt}.
\]
Its time integral on the decaying subspace is related to the inverse of \(C_{\rm node}^{-1}L_g\), and hence to a graph Green operator. Green–Kubo instead integrates equilibrium correlations of a specified flux. A relation between the two requires the noise law, observable, equilibrium covariance and normalization to be derived.

## 5. Dislocations and disclinations in the reconstructed moiré field

Assume a reconstructed continuum displacement field \(u(x)\) and a local lattice/frame description have been obtained. For a closed loop \(\Gamma\) around an isolated core, the translational closure failure is the Burgers vector
\[
b=\oint_\Gamma du.
\]
For a reciprocal vector \(G\), the phase of a displaced mode can be written
\[
\theta_G(x)=G\cdot(x-u(x)).
\]
Its loop increment is
\[
\Delta_\Gamma\theta_G=-G\cdot b
\]
when the explicit coordinate contribution closes. Single-valued complex phase requires
\[
G\cdot b\in2\pi\mathbb Z.
\]
This is the phase-winding signature of a dislocation. It is measurable from a phase-resolved reconstructed field, not from intensity alone in general.

A disclination is instead detected by rotational holonomy. If \(\omega\) is the local connection/rotation one-form, its Frank angle is
\[
\Omega=\oint_\Gamma\omega,
\]
with quantization determined by the rotational symmetry group of the reconstructed lattice (for an \(n\)-fold lattice, allowed elementary rotations are multiples of \(2\pi/n\), subject to the chosen convention and defects allowed by the material).

In a Cartan description, choose a coframe \(e^a\) and connection \(\omega^a{}_b\). Then
\[
T^a=de^a+\omega^a{}_b\wedge e^b,
\qquad
R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\]
The integrated torsion encodes translational closure failure (dislocation content); curvature/rotational holonomy encodes disclination content. The normalization and signs depend on the coframe and connection conventions and must be fixed in an implementation.

**Limitation.** A two-wave scalar moiré intensity does not automatically supply a material displacement, coframe, or connection. To infer Burgers and Frank data, one must specify a phase-unwrapping/registration procedure, reconstruct a local frame, and demonstrate loop closure stability under mesh refinement and noise. The Cartan interpretation is a geometric encoding after that reconstruction, not a consequence of the cosine formula alone.

## 6. Proposed computational audit

The following staged audit is the minimal route from the finite graph to a falsifiable model.

### A. Exact graph checks (inherited from T099)
- verify the 64 vertices, 192 edges, 96+96 edge split and weighted Laplacian spectrum;
- verify positivity and the one-dimensional kernel for \(g_\pm>0\);
- verify the zero-mean solution of \(L_gV=J\) for balanced \(J\).

### B. Mode-to-space reconstruction
- declare \(X_\pm\) and the rule mapping graph eigenvectors to complex amplitudes;
- calculate the resulting reciprocal vectors \(G^\pm\);
- verify the measured fringe wavevector against \(G^+-G^-\);
- test stability under graph relabelling and coordinate refinement.

### C. Linear-response audit
- declare \(C\), the stochastic forcing covariance, temperature and grounding/projection convention;
- verify the fluctuation–dissipation relation for the chosen RC/RLC model;
- estimate equilibrium current autocorrelations and compare their Green–Kubo integral with an independently computed small-field response;
- report finite-time, finite-size and statistical errors.

### D. Defect audit
- impose or identify a phase winding and reconstruct \(b\);
- impose or identify a frame rotation and reconstruct \(\Omega\);
- compare phase-derived Burgers data with translational holonomy and frame-derived Frank data with rotational holonomy;
- test loop independence away from cores and convergence under refinement.

## 7. Evidence and status register

| Statement | Status |
|---|---|
| \(Q_6=Q_3^-\square Q_3^+\), edge counts and finite spectrum | Proved finite combinatorial result (T099) |
| Positivity/kernel of \(L_g\) for \(g_\pm>0\) | Proved finite-dimensional Laplacian result |
| Two-wave moiré wavevector and fringe spacing | Standard exact interference identity, conditional on two specified fields |
| Deriving \(G^\pm\) from Q6 modes and a spatial embedding | Open construction |
| Green–Kubo formula under equilibrium linear-response hypotheses | Standard framework; model-specific observable/noise/normalization must be supplied |
| Identifying graph Green operator with Green–Kubo response | Not established; requires a model-specific derivation |
| Burgers phase winding and Frank rotational holonomy | Standard defect-theory identities under the stated continuum reconstruction |
| Extracting dislocations/disclinations from the Q6/moiré circuit | Open and experimentally testable |
| A universal physical charge or transport law generated by hexagram labels | Not claimed; open hypothesis |

## 8. Falsifiability gates

The proposed bridge fails in its present form if any of the following occurs:
1. no reproducible spatial embedding/mode map yields stable \(G^\pm\);
2. the measured fringe wavevector does not agree with \(G^+-G^-\) within stated uncertainty;
3. the stochastic circuit violates the declared fluctuation–dissipation relation;
4. the Green–Kubo estimate fails to agree with independent linear response in the controlled regime;
5. reconstructed Burgers/Frank values depend strongly on the loop or refinement away from defect cores.

Passing these tests would validate the specified model, not establish that all I Ching arrangements encode physical fields.

## 9. Relation to T099

T099 supplies the finite graph and conditional Kirchhoff network. T100 adds the node-charge correlation model, conditional spatial reconstruction, equilibrium dynamics, transport observables and defect reconstruction. T100 does not alter T099 and does not promote any of its open physical interpretations to theorem status.
