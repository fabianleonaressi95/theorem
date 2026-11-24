# Q6–Jitterbug incidence, variational microscopic stress, and the Green–Kubo–Stokes limit

**Date:** 2026-11-24  
**Status:** [P] exact combinatorial quotient and conditional finite-dimensional OU stress formula; [N] inherited Jitterbug frame/coil checks; [C] candidate geometric coupling; [O] physical Q6–Jitterbug immersion, material stress calibration, hydrodynamic limit and unconditional \(\eta_{\rm GK}=\eta_{\rm Stokes}\).

## 0. Result

There is an exact, explicit \(8{:}1\) quotient map from the Boolean six-cube \(Q_6=Q_3\square Q_3\) to the eight-panel Jitterbug hinge graph \(Q_3\). A strain-dependent quadratic energy gives a microscopic stress by differentiation and an exact OU Green–Kubo formula for its quadratic fluctuations. Equality with the viscosity in the Stokes traction map follows only after a common constitutive/hydrodynamic limit is established. The quotient is not yet a geometric immersion of all Q6 cells into the moving mechanism.

## 1. The eight Jitterbug panels form a cube graph

Index the eight triangular panels by
\[
\mathcal P=\{\varepsilon=(\varepsilon_1,\varepsilon_2,\varepsilon_3):
\varepsilon_k\in\{-1,+1\}\}.
\]
In the unit-edge cuboctahedral reference configuration, panel \(\varepsilon\) has vertices
\[
v_{12}=2^{-1/2}(\varepsilon_1,\varepsilon_2,0),\quad
v_{13}=2^{-1/2}(\varepsilon_1,0,\varepsilon_3),\quad
v_{23}=2^{-1/2}(0,\varepsilon_2,\varepsilon_3).
\]
Two panels share a vertex precisely when their labels differ in one sign: changing \(\varepsilon_3\) preserves \(v_{12}\), changing \(\varepsilon_2\) preserves \(v_{13}\), and changing \(\varepsilon_1\) preserves \(v_{23}\). Thus the panel-contact/hinge-incidence graph is exactly \(Q_3\): 8 panel vertices, 12 adjacency edges and degree 3. Each shared vertex corresponds to one edge of this panel graph. This is an exact combinatorial statement about the labelled reference panels, independent of the motion parameter.

## 2. Explicit Q6-to-panel quotient

Write a Q6 vertex as \(x=(a,b)\in\mathbb F_2^3\times\mathbb F_2^3\), and define
\[
\boxed{\pi:\mathbb F_2^6\to\mathcal P,\qquad
\pi(a,b)=((-1)^{a_1},(-1)^{a_2},(-1)^{a_3}).}
\]
The map is surjective and every panel has exactly eight preimages:
\[
|\pi^{-1}(\varepsilon)|=2^3=8.
\]
The Q6 graph factors as \(Q_3^{\rm panel}\square Q_3^{\rm fibre}\). Its edge types are:
- horizontal edges: flip one of \(a_1,a_2,a_3\); they project to an edge of the Jitterbug panel graph;
- fibre edges: flip one of \(b_1,b_2,b_3\); they remain inside one panel fibre and are collapsed by \(\pi\).

For each panel-graph edge there are eight horizontal Q6 edge lifts, one for each \(b\). Hence \(\pi\) is a graph quotient/product projection with fibres, not a graph covering and not an edge bijection. No six-to-eight bijection is asserted, and no Q6 edge is silently identified with a physical Jitterbug rod.

### 2.1 Chain-level statement

Let \(C_0(Q_6)\) and \(C_0(Q_3^{\rm panel})\) have standard vertex bases. Define
\[
\Pi_0 e_{(a,b)}=e_a.
\]
For a horizontal oriented edge, define
\[
\Pi_1 e_{(a,b),(\,a+e_k,b)}=e_{a,a+e_k};
\]
for a fibre edge set \(\Pi_1e=0\). With consistent orientations,
\[
\boxed{\partial_1^{\rm panel}\Pi_1=\Pi_0\partial_1^{Q6}.}
\]
This is the chain-map identity on the graph 1-skeleton. It does not define a map on Q6 squares, cubes, 64-TG/FCC-D3 cells, or the moving Jitterbug configuration space. The split into first and last three coordinates is a declared choice; the physical programme must select it by an independently derived symmetry/phase convention.

## 3. Moving panel frames: attach geometry without inventing it

Reuse the existing Gray/Jitterbug trajectory \(W(t)\), its eight labelled triangles, and proper Kabsch fits. For panel \(a\), with reference vertices \(r_{a,\ell}\) and moving vertices \(R_{a,\ell}(t)\), define
\[
(R_a(t),c_a(t))=
\arg\min_{R\in SO(3),\,c\in\mathbb R^3}
\sum_{\ell=1}^3\|Rr_{a,\ell}+c-R_{a,\ell}(t)\|^2.
\]
The oriented normal is \(n_a(t)=R_a(t)n_a(0)\). The fit residual is a numerical rigidity diagnostic. Existing code already reports all eight frames, panel-fit residuals, finite-surface fluxes and receiver-side circuit balance.

For \(x=(a,b)\), the quotient attaches label \(a\) to frame \((R_a(t),c_a(t),n_a(t))\); \(b\) remains a fibre label. This is a label-to-frame assignment, not a physical position for the eight states in a fibre. No within-panel map \(b\mapsto y_{a,b}(t)\), six-dimensional immersion, or Q6-to-64-TG-to-Jitterbug embedding is claimed.

A complete lift must construct \(y_{a,b}(t)\) and prove compatibility with panel rigidity, the 12 panel contacts, the three collapsed fibre directions, the full Gray branch (cuboctahedral, icosahedral and octahedral configurations), Vesica phase conventions and higher-cell incidence. These are concrete remaining acceptance conditions for issues #398 and #401. The merged coil calculation is an observable attached to panel frames, not a substitute for this lift.

## 4. Deriving microscopic stress from a strain-dependent energy

Let \(q\in\mathbb R^N\) be microscopic variables and \(\varepsilon\) a symmetric macroscopic strain tensor. For a differentiable energy \(H(q,\varepsilon)\), define the total extensive microscopic stress by
\[
\boxed{\Pi_{ij}(q)=-\left.\frac{\partial H(q,\varepsilon)}
{\partial\varepsilon_{ij}}\right|_{\varepsilon=0}.}
\]
For a gradient/nonlocal energy, vary before discarding integrations-by-parts terms. If
\(H=\int_\Omega h(q,\nabla q,\varepsilon,\nabla\varepsilon)\,dx\), then the variation contains a bulk stress and boundary/hyperstress terms. Those boundary terms must be retained when deriving traction; they cannot be silently absorbed into a bulk viscosity.

### 4.1 Explicit quadratic model

Take
\[
H(q,\varepsilon)=\frac12q^TK(\varepsilon)q,\qquad
K(\varepsilon)=K_0+\sum_{ij}\varepsilon_{ij}A^{ij}+O(|\varepsilon|^2),
\]
with symmetric \(K_0,A^{ij}\). Then
\[
\boxed{\Pi_{ij}(q)=-\frac12q^TA^{ij}q.}
\]
The centered stress is a quadratic observable:
\[
\delta\Pi_{ij}=-\frac12\left(q^TA^{ij}q-
\langle q^TA^{ij}q\rangle_{\rm eq}\right).
\]
It is not the earlier linear OU observable \(J_b=b^TX\). Those two Green–Kubo calculations must not be conflated.

A possible Q6 discrete strain energy is
\[
\mathcal E(a,\varepsilon)=\frac12
\sum_{e=(v,w)}\omega_e(\varepsilon)
\left[a_w-a_v-\ell_e(\varepsilon)\cdot\bar\nabla a_e\right]^2
+\mathcal E_{\rm cell}(a,\varepsilon),
\]
where edge weights, edge vectors and cell terms must be derived from the chosen embedding and material energy. Its stress is \(-\partial_{\varepsilon_{ij}}\mathcal E|_0\). T130 supplies a geometric/variational discretization framework, but does not determine physical weights, \(A^{ij}\), or a nonlocal Stokes kernel. The static identity \(\Delta\mu_4=-8w^4\mathcal F_{Q6}\) is not itself this strain derivative; first define how its variables and metric depend on strain.

## 5. Exact quadratic-stress Green–Kubo formula for the declared Q6 OU dynamics

This is an exact finite-dimensional result conditional on the stated OU model and quadratic stress; it is not a material calibration.

Let \(H_0=\mathbf1^\perp\subset\mathbb R^{64}\), and let \(L_0\) be the Q6 graph Laplacian restricted to \(H_0\), with positive eigenvalues \(\lambda_\alpha\). Consider
\[
dX_t=-\gamma L_0X_t\,dt+
\sqrt{2\gamma\sigma^2L_0}\,dW_t,\qquad X_t\in H_0.
\]
Its invariant covariance is \(\sigma^2I_{H_0}\), and
\[
\mathbb E[X_tX_0^T]=\sigma^2e^{-\gamma L_0t}.
\]
For symmetric \(A\) on \(H_0\), define
\[
\delta\Pi_A(t)=-\frac12
\left(X_t^TAX_t-\sigma^2\operatorname{Tr}A\right).
\]
The Gaussian fourth-moment/Wick identity gives
\[
C_A(t)=\mathbb E[\delta\Pi_A(t)\delta\Pi_A(0)]
=\frac{\sigma^4}{2}
\operatorname{Tr}\left(Ae^{-\gamma L_0t}Ae^{-\gamma L_0t}\right).
\]
In an orthonormal eigenbasis of \(L_0\),
\[
C_A(t)=\frac{\sigma^4}{2}
\sum_{\alpha,\beta}|A_{\alpha\beta}|^2
e^{-\gamma(\lambda_\alpha+\lambda_\beta)t}.
\]
Consequently
\[
\boxed{\int_0^\infty C_A(t)\,dt
=\frac{\sigma^4}{2\gamma}
\sum_{\alpha,\beta}
\frac{|A_{\alpha\beta}|^2}{\lambda_\alpha+\lambda_\beta}.}
\]
For shear component \(A^{xy}\), the classical coefficient associated with total extensive stress and physical volume \(V\) is
\[
\boxed{\eta_{GK}^{xy,xy}
=\frac{1}{k_BT\,V}\int_0^\infty C_A(t)\,dt
=\frac{\sigma^4}{2\gamma k_BT\,V}
\sum_{\alpha,\beta}
\frac{|A_{\alpha\beta}^{xy}|^2}
{\lambda_\alpha+\lambda_\beta}.}
\]
The integral is finite because \(\lambda_\alpha>0\) on \(H_0\). Additional linear/internal variables require their own centered correlations and cross-correlations. For nonquadratic energy or anharmonic dynamics the Wick reduction does not apply.

**Important distinction:** the exact linear-observable result
\(\sigma^2\langle b,L_0^\dagger b\rangle/\gamma\) remains correct for \(J_b=b^TX\), but it is not the microscopic shear-stress formula unless stress is independently derived to be that linear observable. The quadratic formula above is the appropriate result for the explicitly strain-derived stress of this Gaussian quadratic model.

## 6. What would prove \(\eta_{\rm GK}=\eta_{\rm Stokes}\)?

For a smooth bounded domain, the Stokes problem is
\[
-\nabla p+\eta_{\rm Stokes}\Delta u+f=0,\qquad
\nabla\cdot u=0,
\]
with traction
\[
t=(2\eta_{\rm Stokes}D(u)-pI)n,\qquad
D(u)=\tfrac12(\nabla u+\nabla u^T).
\]
The hydrodynamic traction map is
\[
\Lambda_{\eta_{\rm Stokes}}:g=u|_{\partial\Omega}
\longmapsto t|_{\partial\Omega}.
\]
It is distinct from both the Q6 graph Green operator and the magnetic scalar DN map in the coil note.

### 6.1 Conditional constitutive theorem

**Theorem (Green–Kubo/Stokes consistency, conditional form).**  
Assume a sequence of equilibrium microscopic models indexed by \(h\downarrow0\) satisfies:

1. **Common energy and stress:** each model has a specified Hamiltonian \(H_h(q,\varepsilon)\), and total microscopic stress \(\Pi_h=-\partial_\varepsilon H_h|_0\), including boundary/hyperstress terms.
2. **Equilibrium linear response:** dynamics is stationary, satisfies the relevant detailed-balance/linear-response hypotheses, and stress correlations are integrable after conserved-mode projection.
3. **Green–Kubo convergence:** for the selected shear component,
   \[
   \lim_{h\downarrow0}\frac{1}{k_BT V_h}
   \int_0^\infty
   \langle\delta\Pi_h^{xy}(t)\delta\Pi_h^{xy}(0)\rangle\,dt
   =\eta_*,
   \]
   with uniform tail control sufficient to exchange long-time and continuum limits.
4. **Hydrodynamic limit:** the same models, under the same scaling and boundary conditions, converge to an incompressible Newtonian constitutive law \(\tau=2\eta_*D(u)\), with no residual memory kernel, anisotropic viscosity tensor, or independent surface stress.
5. **Boundary-response convergence:** microscopic boundary traction/velocity response converges in the selected trace spaces to the Stokes traction map.

Then
\[
\boxed{\eta_{\rm Stokes}=\eta_*=\eta_{\rm GK}.}
\]

**Proof.** By assumptions 1–3 and equilibrium linear response, the limiting coefficient multiplying the shear-rate perturbation in the bulk constitutive response is \(\eta_*\). Assumption 4 states that the limiting constitutive response is Newtonian and local, so its deviatoric stress is \(2\eta_*D(u)\). Substitution into momentum balance and incompressibility yields the Stokes PDE with coefficient \(\eta_*\). Assumption 5 identifies the limiting boundary traction with \((2\eta_*D(u)-pI)n\), hence its traction map is \(\Lambda_{\eta_*}\). The coefficient in the Green–Kubo response and in the Stokes traction map is therefore the same. \(\square\)

This is a conditional theorem: its proof is rigorous once the five hypotheses are verified. It does not establish those hypotheses for the current finite Q6/Jitterbug data. Convergence of a graph Laplacian or coil inductance matrix alone is not a hydrodynamic limit.

### 6.2 When scalar equality is not the right target

If the limit is anisotropic, viscoelastic, nonlocal, or retains surface/hyperstress terms, the target must instead be a tensor- or frequency-dependent relation, such as
\[
\eta_{ij,kl}(\omega),\qquad
\tau_{ij}(\omega)=2\eta_{ij,kl}(\omega)D_{kl}(\omega),
\]
possibly with additional surface variables. The six Q6 directions must be retained until isotropy is proved; averaging them by assumption would prejudge the result.

## 7. Work packages and acceptance tests

### A. Exact quotient and frame coupling
- Verify \(\Pi_0\partial_1=\partial_1\Pi_1\) exactly over integer matrices.
- Enumerate all eight fibres and twelve panel-graph edges; verify eight horizontal lifts per panel edge and three collapsed fibre directions per Q6 vertex.
- Check panel contact incidence from the explicit sign-triple vertex formula.
- Reuse Gray path and Kabsch frames; report maximum rigid-fit residual and \(\det R_a=+1\).
- Do not call the quotient a geometric immersion until a within-fibre coordinate map and higher-cell chain maps exist.

### B. Microscopic stress
- Derive \(K_0\) and \(A^{ij}=\partial_{\varepsilon_{ij}}K|_0\) from one explicit Q6/material energy.
- Verify symmetry and units of \(A^{ij}\), and include all boundary terms in the variation.
- Compare quadratic-stress formula with direct OU Monte Carlo and Wick evaluation.
- Retain phonon/phason/mixed cross-correlations if those variables are included; T131 already requires this separation.

### C. Green–Kubo to Stokes
- Replace illustrative finite OU bath by physically justified equilibrium dynamics, or justify it as a controlled effective model.
- Establish correlation integrability, conserved-mode projection, finite-size scaling and uniform long-time tail bounds.
- Derive the nonlocal microscopic resistance/mobility operator; T130's local positive resistance assembly is not sufficient for Stokes convergence.
- Prove convergence of bulk stress response and boundary traction in compatible spaces.
- Test isotropy. If it fails, report \(\eta_{ij,kl}\), not a scalar.

### D. Jitterbug electromagnetic coupling remains separate
The existing eight-coil model supplies \(L(q)\), finite-surface flux and receiver-side energy balance. To couple it to mechanical stress, derive magnetic energy and generalized force from the same source/receiver field model, include primary supply and actuator work, and vary the full energy with respect to panel configuration and strain. The coil Neumann Green pairing is not itself a hydrodynamic viscosity.

## 8. Repository links and monograph placement

- Jitterbug/Vesica and panel frames: chapters 13–14; issues #398 and #401.
- Mixed frame connection and Cartan torsion: issues #399–#400; neither is identified with the stress derived here.
- Q6 gradient, barycentres and resistance: T130.
- Q6 phonon/phason and Green–Kubo stress: T131.
- Q6 Green–Kubo/OU scale bridge: theorems/Q6_GREEN_KUBO_KRYSTALLO_SCALE_BRIDGE_2026-11-23.md.
- Eight-panel finite-surface coil and receiver energy audit: research/JITTERBUG_NEUMANN_DIRICHLET_BRIDGE.md, merged PR #414.
- Q6/Jitterbug crosswalk and OU normalization: research/UNIFIED_PROGRAM_27_CHAPTER_CROSSWALK_2026-11-24.md, merged PR #419.
- Transport and boundary response: chapters 20–22.

## 9. Final classification

| Claim | Status |
|---|---|
| Eight Jitterbug panels have the \(Q_3\) contact graph under sign-triple labelling | [P] exact combinatorics |
| \(Q_6=Q_3\square Q_3\to Q_3^{\rm panel}\) is an explicit surjective \(8{:}1\) graph quotient | [P] exact combinatorics |
| Chain-map identity on the graph 1-skeleton | [P] exact, with stated orientations |
| Assignment of each Q6 fibre to a moving Kabsch panel frame | [C] explicit candidate |
| Full Q6/64-TG geometric immersion into moving Jitterbug | [O] |
| Stress as \(-\partial_\varepsilon H\) for specified differentiable energy | [P] variational identity |
| Quadratic-stress OU Green–Kubo formula in §5 | [P] exact under declared OU model |
| Identification of matrices \(A^{ij}\) with calibrated material stress | [O] |
| Conditional implication \(\eta_{\rm GK}=\eta_{\rm Stokes}\) under §6 hypotheses | [P] conditional theorem |
| Verification of those hypotheses for Q6/Jitterbug | [O] |
| Complete primary + actuator + receiver + Maxwell mechanical energy closure | [O] |

No theorem number is assigned: this is a research bridge note with a conditional theorem, not a new unconditional physical theorem.
