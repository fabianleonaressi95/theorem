# T100 — Hypercube–moiré response, Green–Kubo transport, and geometric defects

**Status:** exact graph identities inherited from T099; continuum moiré identities are conditional on an explicit spatial embedding; Green–Kubo is a standard linear-response formula under equilibrium hypotheses; the Q6-to-defect correspondence is a research programme, not yet proved.

**Scope:** construct a mathematically explicit bridge from the two edge families of the six-dimensional hypercube to two spatially reconstructed fields, their moiré interference, equilibrium transport, and translational/rotational defect holonomy.

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

## 2. Spatial reconstruction: the additional data moiré requires

A moiré pattern is not determined by an abstract finite graph alone. Introduce, as explicit model data:

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
A_+\overline{A_-}
e^{i(q_m\cdot x+\Delta\phi(x))}
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

## 3. Dynamics and Green–Kubo response

The static Kirchhoff equation \(L_gV=J\) from T099 does not by itself define an equilibrium time-correlation function. A dynamical model must be specified. One admissible linear circuit model is
\[
C\dot V(t)+L_gV(t)=\eta(t)+J_{\rm ext}(t),
\]
where \(C\) is a positive capacitance matrix, the constant-potential mode is grounded or projected out, and \(\eta\) is a stationary noise source. For a thermal equilibrium interpretation, the noise covariance and dissipative operator must satisfy the appropriate fluctuation–dissipation relation for the chosen circuit variables and units. This condition must be stated, not assumed from the graph.

For an oriented edge \(e=(i,j)\), let
\[
j_e(t)=g_e\big(V_i(t)-V_j(t)\big)
\]
be the branch current, with the orientation fixed once. Given a spatial embedding \(X\), let \(d_e=X(j)-X(i)\). A macroscopic current observable can then be defined, for example, by
\[
\mathcal J_a(t)=\frac{1}{\mathcal V}\sum_{e}d_{e,a}\,j_e(t),
\]
where \(\mathcal V\) is the chosen normalization volume/area. Its physical meaning and units depend on the circuit realization and embedding.

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
e^{-C^{-1}L_gt}.
\]
Its time integral on the decaying subspace is related to the inverse of \(C^{-1}L_g\), and hence to a graph Green operator. Green–Kubo instead integrates equilibrium correlations of a specified flux. A relation between the two requires the noise law, observable, equilibrium covariance and normalization to be derived.

## 4. Dislocations and disclinations in the reconstructed moiré field

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

## 5. Proposed computational audit

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

## 6. Evidence and status register

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

## 7. Falsifiability gates

The proposed bridge fails in its present form if any of the following occurs:
1. no reproducible spatial embedding/mode map yields stable \(G^\pm\);
2. the measured fringe wavevector does not agree with \(G^+-G^-\) within stated uncertainty;
3. the stochastic circuit violates the declared fluctuation–dissipation relation;
4. the Green–Kubo estimate fails to agree with independent linear response in the controlled regime;
5. reconstructed Burgers/Frank values depend strongly on the loop or refinement away from defect cores.

Passing these tests would validate the specified model, not establish that all I Ching arrangements encode physical fields.

## 8. Relation to T099

T099 supplies the finite graph and conditional Kirchhoff network. T100 adds the missing spatial embedding, two-field interference, equilibrium dynamics, transport observables and defect reconstruction. T100 does not alter T099 and does not promote any of its open physical interpretations to theorem status.
