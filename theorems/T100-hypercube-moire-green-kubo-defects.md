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

The 64 vertices are not merely labels for two collective trigram fields. Each individual hexagram \(h\in V(Q_6)\) is a distinct measurement/model site. A candidate intrinsic assignment is
\[
q:V(Q_6)\to\mathbb R,\qquad h\mapsto q(h),
\]
but its physical meaning (electric charge, effective charge-like observable, or dimensionless variable), units and numerical values must be derived or measured. No value is assigned by the combinatorial label alone.

For a circuit or statistical realization, let \(Q_h(t)\) be the measured node charge. If an intrinsic label value and an occupation variable are useful, state the constitutive convention explicitly:
\[
Q_h(t)=q(h)n_h(t).
\]
Collect the 64 measured charges into \(Q(t)=(Q_0(t),\ldots,Q_{63}(t))^T\). A continuously varying circuit may instead take \(Q_h(t)\) as the primary measured variable without introducing a separate occupation model.

The primary equal-time and time-dependent correlation matrix is
\[
C_{hh'}(\tau)=
\left\langle\delta Q_h(t+\tau)\,\delta Q_{h'}(t)\right\rangle_{\rm eq},
\qquad
\delta Q_h=Q_h-\langle Q_h\rangle_{\rm eq}.
\]
The full \(64\times64\) matrix is retained: its diagonal records each site's variance and its off-diagonal entries record correlations between distinct hexagrams. Dependence on graph distance, Hamming distance and the lower/upper-line transition classes can be compared without replacing the 64 sites by eight trigram averages.

Let \(B\in\mathbb R^{64\times192}\) be an oriented incidence matrix, with \(+1\) at each edge tail and \(-1\) at its head. Let \(G=\operatorname{diag}(g_e)\), \(g_e\geq0\), and let \(C_{\rm node}\) be a positive node-capacitance matrix. With
\[
V(t)=C_{\rm node}^{-1}Q(t),\qquad
j(t)=G B^\top V(t),
\]
the charge-continuity equation is
\[
\dot Q(t)=-B j(t)+s(t)
=-BGB^\top C_{\rm node}^{-1}Q(t)+s(t),
\]
where \(s(t)\) is the declared source/sink vector. Since \(L_g=BGB^\top\),
\[
\boxed{\dot Q+L_g C_{\rm node}^{-1}Q=s.}
\]
Summing over all 64 sites gives
\[
\frac{d}{dt}\mathbf1^\top Q(t)=\mathbf1^\top s(t).
\]
Thus total charge is conserved when the net source vanishes; this follows from \(\mathbf1^\top B=0\), independently of any moiré interpretation.

Given a declared spatial embedding \(X:V(Q_6)\to\mathbb R^d\), orient each edge \(e=(h_{\rm tail},h_{\rm head})\) and set \(d_e=X(h_{\rm head})-X(h_{\rm tail})\). The extensive current flux is
\[
\mathcal J_a(t)=\sum_{e=1}^{192}d_{e,a}j_e(t).
\]
The node-charge correlations \(C_{hh'}(\tau)\) and edge-current correlations \(\langle j_e(t+\tau)j_{e'}(t)\rangle\) are different observables and should both be recorded.

Once coordinates \(X_h\) are specified, a spatial/dynamical structure factor is
\[
S(k,\omega)=
\sum_{h,h'}e^{-ik\cdot(X_h-X_{h'})}
\int_{-\infty}^{\infty}e^{i\omega\tau}
C_{hh'}(\tau)\,d\tau.
\]
Without a spatial embedding, the well-defined alternative is the graph-mode correlation matrix obtained by projecting \(C(\tau)\) onto eigenvectors of \(L_g\). Peaks may suggest modulation or a candidate moiré scale, but do not establish a physical reciprocal-space pattern without the embedding and its calibration.

## 3. Spatial reconstruction: the additional data moiré requires

The node-charge field \(Q_h(t)\) remains primary. A moiré pattern is a possible spatial signature of correlations between two reconstructed fields, not a replacement for the 64 node variables. It is not determined by the abstract graph alone. Specify either two embeddings \(X_\pm:V(Q_6)\to\mathbb R^2\), or one common embedding with two distinct reciprocal-mode families, together with measured complex amplitudes \(a_h^\pm\) and reciprocal vectors \(G^\pm\).

For the single-mode benchmark, define
\[
\psi_\pm(x)=A_\pm(x)e^{i(G^\pm\cdot x+\phi_\pm(x))}.
\]
Their coherent intensity is exactly
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
This is the standard two-wave interference/moiré identity. It becomes a Q6-derived prediction only after \(G^\pm\), amplitudes and embeddings have been obtained from a specified eigenmode or reconstruction procedure. No canonical graph-to-space map is assumed.

For nonconstant amplitudes or several modes, the intensity contains the corresponding pairwise cross terms. A scalar intensity map alone generally loses phase information; defect reconstruction therefore requires access to the complex fields or an equivalent phase-sensitive observable.

## 4. Dynamics and Green–Kubo response

The static Kirchhoff equation \(L_gV=J\) from T099 does not by itself define an equilibrium time-correlation function. A dynamical model must be specified. One admissible linear circuit model is
\[
C_{\rm node}\dot V(t)+L_gV(t)=\eta(t)+J_{\rm ext}(t),
\]
where the constant-potential mode is treated consistently with total-charge conservation and \(\eta\) is a stationary current-noise source. For the linear thermal RC model with energy
\[
H(Q)=\tfrac12Q^TC_{\rm node}^{-1}Q,
\]
the equilibrium Langevin choice is
\[
\langle\eta(t)\eta(t')^T\rangle
=2k_BT L_g\,\delta(t-t')
\]
on the dissipative subspace, with the zero mode projected out or separately constrained. This is a fluctuation–dissipation relation for this particular overdamped model; other circuit realizations require their own noise covariance.

For a classical system in equilibrium, the Green–Kubo transport tensor has the form
\[
\boxed{
\kappa_{ab}=
\frac{1}{k_BT\,\mathcal V}
\int_0^\infty
\left\langle\mathcal J_a(t)\mathcal J_b(0)\right\rangle_{\rm eq}\,dt
}
\]
when \(\mathcal J\) is the extensive flux convention appropriate to this prefactor. If an intensive current density is used, the volume factor must be changed accordingly. For electrical conductivity, the flux must be the properly normalized electric current and the prefactor must match the chosen microscopic convention. Quantum response requires the corresponding Kubo commutator and, where applicable, diamagnetic/contact terms; the classical formula above must not be relabelled as a quantum conductivity formula.

The graph Green operator \(L_g^\dagger\) and the Green–Kubo integral are different objects. In the deterministic RC model, the zero-mean voltage propagator is
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


## 6.1 Walsh charge-law decomposition and an exactly solvable RC benchmark

A scalar charge assignment on the 64 hexagrams is a function
\[
q:\{0,1\}^6\to\mathbb R.
\]
It has the unique Walsh expansion
\[
q(h)=\sum_{S\subseteq\{1,\ldots,6\}}\widehat q(S)\chi_S(h),
\qquad
\chi_S(h)=(-1)^{|S\cap h|},
\]
with
\[
\widehat q(S)=\frac1{64}\sum_{h\in Q_6}q(h)\chi_S(h).
\]
The 64 Walsh characters form an orthogonal basis and satisfy
\[
L_6\chi_S=2|S|\chi_S.
\]
Consequently, this basis resolves every possible node-charge assignment into graph-frequency sectors \(k=|S|=0,\ldots,6\), with multiplicities \(\binom6k\). It does **not** determine the coefficients \(\widehat q(S)\): those require a constitutive derivation or a measured 64-component data vector.

The full automorphism group of the six-cube acts transitively on its vertices. Therefore, if a scalar assignment obeys \(q(\gamma h)=q(h)\) for every cube automorphism \(\gamma\), then \(q\) is constant. A nonconstant charge law must either break some graph automorphisms or depend on additional structure (for example, a physically justified orientation, embedding, boundary condition, or external field). Such structure must be specified rather than silently built into the labels.

For a separate dynamical benchmark, take \(C_{\rm node}=cI\), \(L_g=gL_6\), \(g,c>0\), and projected zero-total-charge fluctuations \(x=Q-\overline Q\) satisfying
\[
\dot x=-\frac gcL_6x+\eta,\qquad
\langle\eta(t)\eta(t')^T\rangle=2k_BTgL_6\,\delta(t-t').
\]
On the subspace orthogonal to constants, the stationary covariance is \(k_BT c I\). In the full 64-dimensional notation this gives
\[
C(\tau)=k_BT c\,e^{-(g/c)L_6|\tau|}P_0,
\qquad
P_0=I-\frac1{64}\mathbf1\mathbf1^T.
\]
By the product heat kernel, if \(d=d_H(h,h')\) and \(r=e^{-2g|\tau|/c}\),
\[
\boxed{
C_{hh'}(\tau)=k_BT c\left[
\frac{(1+r)^{6-d}(1-r)^d}{64}-\frac1{64}
\right].
}
\]
This exact benchmark is a prediction of the declared homogeneous thermal RC model, not a derivation of the intrinsic constitutive law \(q(h)\). It is isotropic in Hamming distance and has zero row sums because the uniform total-charge mode is constrained. Nonzero mode-dependent structure beyond this kernel would require nonuniform conductances/capacitances, a symmetry-breaking charge law, external forcing, or additional degrees of freedom.

The companion script scripts/audit_t100_q6_charge_correlations.py checks the Walsh transform/inverse, the Walsh Laplacian eigenvalues, the exact RC covariance, and its conservation constraint. A measured or independently derived 64-value charge vector can be supplied as JSON to compute its Walsh coefficients; no synthetic vector is treated as physical data. Tests are in tests/test_t100_q6_charge_correlations.py.


## 6.2 Ordered-line symmetry classes: an exact model-selection audit

Fix bit 0 as the bottom line and bit 5 as the top line. The number of independent values in a scalar law q:{0,1}^6 -> R depends on which transformations are physically required to leave the law invariant. These are distinct hypotheses:

| Assumed invariance of q | Number of vertex orbits / independent values |
|---|---:|
| No extra symmetry | 64 |
| Reversal of the six-line order h -> rev(h) | 36 |
| Arbitrary permutation of six line positions (S6) | 7 |
| Reversal together with global yin-yang exchange h -> h XOR 63 | 20 |
| Full automorphism group of Q6 | 1 |

For reversal alone, the orbit count is (64+8)/2=36: reversal fixes the eight palindromic six-bit strings. For the group generated by reversal and complement, Burnside's lemma gives (64+8+0+8)/4=20. Under arbitrary line permutations, the orbits are exactly the seven Hamming-weight classes of sizes 1,6,15,20,15,6,1. Under the full cube automorphism group, transitivity leaves only one orbit.

These counts provide a falsifiable model-selection ladder. If a measured 64-vector is available, project it onto each invariant subspace by averaging within the corresponding orbits and compare residuals against measurement uncertainty. The smallest residual is not by itself proof of a symmetry: the symmetry must also be justified by the physical setup and survive independent measurements. In particular, line reversal, global yin-yang exchange, and arbitrary line permutation are separate assumptions. The vertical order of the six lines is retained unless evidence supports discarding it.

The companion audit scripts/audit_t100_q6_symmetry_classes.py computes the orbit partitions and invariant projections. It accepts a JSON array of 64 measured or independently derived values with --charges and reports residuals for each hypothesis. Tests are in tests/test_t100_q6_symmetry_classes.py. This is an exact combinatorial classification, not yet a selection of the physical charge law.

## 6.3 A concrete but non-conserved candidate: net line polarity

An earlier exploratory ansatz can be tested without promoting it to the physical law. Encode each line by \(\varepsilon_a(h)=2h_a-1\in\{-1,+1\}\), with bit 1 denoting Yang and bit 0 Yin, and define
\[
\boxed{q_{\rm net}(h)=q_0\sum_{a=1}^6\varepsilon_a(h)
=q_0(2|h|-6).}
\]
This candidate depends only on Hamming weight and is therefore invariant under arbitrary permutations of the six line positions, including top-bottom reversal. It takes seven values \(-6q_0,-4q_0,-2q_0,0,2q_0,4q_0,6q_0\), with exact multiplicities \(1,6,15,20,15,6,1\). It is odd under global Yin-Yang exchange:
\[
q_{\rm net}(h\oplus63)=-q_{\rm net}(h).
\]
Thus it does **not** obey complement invariance except in the trivial case \(q_0=0\); the appropriate candidate symmetry is sign reversal, not invariance, under Yin-Yang exchange.

For a single hexagram performing a continuous-time random walk on Q6, with each of the six lines independently flipped at rate \(\gamma\), the generator is \(W=-\gamma L_6\). Each one-line Walsh character has Laplacian eigenvalue 2, so under the uniform stationary distribution the candidate's mean is zero and its autocorrelation is exactly
\[
\boxed{\langle q_{\rm net}(X_t)q_{\rm net}(X_0)\rangle
=6q_0^2e^{-2\gamma|t|}.}
\]
For unequal flip rates \(\gamma_a\), this becomes \(q_0^2\sum_{a=1}^6e^{-2\gamma_a|t|}\). This is a *single-walker state-observable correlation*, distinct from the 64-node circuit covariance \(C_{hh'}(t)\) in Sections 2 and 6.1.

The candidate is not conserved by Q6 hopping. Let \(D_q=\operatorname{diag}(q_{\rm net}(h))\). Directly summing the squared commutator entries over the 192 undirected edges gives
\[
\boxed{\|[D_q,L_6]\|_F=16\sqrt6\,|q_0|.}
\]
It vanishes only for \(q_0=0\). Therefore this ansatz can be tested as a state-dependent observable, but it cannot be called a conserved charge under the proposed one-line-flip dynamics. This does not rule out a different 64-node circuit interpretation with externally constrained node charges.

The companion symmetry audit implements this candidate, its seven-level degeneracies, the random-walk autocorrelation, and the commutator norm. It is explicitly classified as a candidate ansatz, not as an established electric-charge law.

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
| Net line-polarity ansatz q0 sum(epsilon_a) | Explicit candidate; 7 levels; not conserved under Q6 hopping |
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
