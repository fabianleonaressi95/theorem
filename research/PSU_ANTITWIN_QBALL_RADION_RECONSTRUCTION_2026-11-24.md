# PSU–Anti-Twin Q-ball and radion: reconstruction of prior derivations

**Date:** 24 November 2026  
**Status:** prior two-field variational model reconstructed; conditional field equations and symmetry identities; numerical benchmarks are model-specific; physical identification and radion stabilization remain open.  
**Editorial rule:** this continues the earlier PSU–Anti-Twin/Q-ball work. It is not a restart from the generic Coleman definition.

## 1. Two different uses of “Q-ball” in the repository

The repository uses “Q-ball” in two mathematically distinct senses:

1. **Field-theoretic Q-ball:** a non-topological soliton of one or more complex scalar fields with a conserved global \(U(1)\) charge. This is the PSU–Anti-Twin branch reconstructed below.
2. **Q-ball/football shell:** the finite 32-panel, 60-vertex shell geometry used in T080 and T088. These records establish a finite oriented shell complex, discrete Stokes identities, panel frames, seam transport and geometric anisotropy. They do not by themselves establish a Coleman-type scalar soliton or its \(U(1)\) charge.

The shell may eventually provide a spatial discretization/domain for field profiles or interface terms, but that coupling requires an explicit field discretization and action.

## 2. Prior PSU–Anti-Twin spectral construction

The earlier derive_rgs_psu_sea.py work was recorded with:

- \(J_{\rm AT}^2=I\): the Anti-Twin exchange is an involution.
- An exact \(128\to4\times32\) PSU/Anti-Twin spectral split.
- The bosonic operator family
  \[
  K_{\sigma,\varepsilon}
  =L_\varepsilon+m_B^2I+
  (\lambda_Bq+\sigma\varepsilon\mu)T_\varepsilon.
  \]
- The exchange \(Z_2\) check was passed. At that stage, however, the common \(U(1)\), a charged Q-ball solution and a radion equation had **not** yet been derived.

Recorded numerical values from that audit (provenance benchmarks, not universal constants):

| Quantity | Recorded value |
|---|---:|
| \(\tau_g\), min / mean / RMS / max | 0.07834387 / 0.17614073 / 0.20941879 / 0.45027537 |
| \(m_B,\mu,\lambda_B\) | 0.6, 0.2, 0.4 |
| Bosonic spectrum | 0.32458948–12.39541052 |
| \(\Gamma_B(0),\Gamma'_B(0),\Gamma''_B(0)\) | 111.60456335, 1.01407224, −0.06084670 |
| Fermionic \(\sigma_{\min},\sigma_{\max}\) | 0.89336113, 4.31489910 |
| \(\Gamma_F(0),\Gamma'_F(0),\Gamma''_F(0)\) | −393.54945721, −4.77022757, −0.50188469 |
| Loop derivatives | −3.75615533, −0.56273139 |

The historical script name is retained for provenance. It was not found in the current default-branch file tree during this reconstruction; these values are prior-session results pending a reproducible source/artifact link. They are not presented as a fresh rerun.

## 3. Prior two-field PSU–Anti-Twin Q-ball action

The subsequent construction introduced two complex fields \(\Phi_P,\Phi_A\), one on each PSU/Anti-Twin sector, with:

- a **common global \(U(1)\)**: \((\Phi_P,\Phi_A)\mapsto e^{i\alpha}(\Phi_P,\Phi_A)\);
- an **exchange \(Z_2\)**: \(\Phi_P\leftrightarrow\Phi_A\);
- a shared vierbein/metric in the kinetic terms.

The model action was
\[
S=\int d^4x\,\sqrt{-g}\left[
\sum_{s=P,A}g^{\mu\nu}\partial_\mu\Phi_s^*
\partial_\nu\Phi_s
-U(|\Phi_P|^2)-U(|\Phi_A|^2)
-V_{\rm int}(\Phi_P,\Phi_A)
\right].
\]
Here \(V_{\rm int}\) must be invariant under the common \(U(1)\) and exchange \(Z_2\). Its explicit functional form was deliberately left undetermined; no coupling should be invented merely to close the equations.

For a common-frequency stationary ansatz
\[
\Phi_s(r,t)=f_s(r)e^{i\omega t},\qquad f_s(r)\in\mathbb R,
\]
the radial equations are
\[
f_s''+\frac2r f_s'
=(m^2-\omega^2)f_s-2\lambda f_s^3+3g f_s^5
+\frac12\frac{\partial V_{\rm int}}{\partial f_s},
\qquad s=P,A,
\]
for the previously used sextic self-potential
\[
U(s)=m^2s-\lambda s^2+g s^3,\qquad s=|\Phi|^2.
\]
Boundary conditions:
\[
f_s'(0)=0,\qquad f_s(r)\to0\quad(r\to\infty).
\]

The common \(U(1)\) gives one conserved Noether current (up to the overall sign convention for \(j^\mu\)); with the convention used in the prior derivation,
\[
Q=2\omega I,\qquad
I=\int_{\mathbb R^3}(f_P^2+f_A^2)\,d^3x.
\]
The stationary energy was organized as
\[
E_Q=E_{\rm grad}+E_{\rm pot}+E_{\rm int}+\frac{Q^2}{4I}.
\]
All terms must use the same field normalization and action convention.

For the single-field sextic potential,
\[
\frac{U(s)}s=m^2-\lambda s+gs^2.
\]
For \(g>0,\lambda>0\), its minimum occurs at \(s=\lambda/(2g)\), with value \(m^2-\lambda^2/(4g)\). Thus the single-field frequency window is conditional on \(0<m^2-\lambda^2/(4g)<m^2\):
\[
m^2-\frac{\lambda^2}{4g}<\omega^2<m^2.
\]
For the coupled model, the actual existence interval must be recomputed from the full \(V_{\rm int}\); the single-field bound is not automatically the coupled bound.

A previous two-field reduction recorded the disjoint-limit interval
\[
0.6614378<\omega<1.
\]
This is a model-specific prior result. Its parameter normalization and derivation must be recovered from the original calculation before identifying it with the analytic sextic bound above.

## 4. Exchange symmetry and symmetric/antisymmetric fluctuations

At an exchange-symmetric background \(f_P=f_A=f_*\), the radial Hessian has equal diagonal entries. Write its local potential Hessian as
\[
H_f=
\begin{pmatrix}
V_{PP}&V_{PA}\\
V_{PA}&V_{PP}
\end{pmatrix}.
\]
The normalized exchange eigenvectors are
\[
e_+=\frac1{\sqrt2}(1,1)^T,\qquad
e_-=\frac1{\sqrt2}(1,-1)^T,
\]
with eigenvalues
\[
\boxed{\kappa_+=V_{PP}+V_{PA},\qquad
\kappa_-=V_{PP}-V_{PA}.}
\]
This is an exact consequence of exchange symmetry. It separates common-mode and Anti-Twin relative-mode local stability tests. Positivity of both local eigenvalues is necessary locally, not a complete proof of global soliton stability; the full radial fluctuation operator and charge-preserving perturbations remain to be analyzed.

## 5. Previously recorded numerical benchmark — do not mislabel

A prior **single-profile** numerical benchmark used
\[
m=1,\qquad\lambda=1,\qquad g=0.5,
\]
and recorded
\[
\omega=0.905607329,\qquad E/Q=0.988291616.
\]
This is a single-profile result with no coupled PSU–Anti-Twin interaction. It is not numerical confirmation of the two-field model, its exchange-mode stability, or a radion solution.

The earlier two-field work also recorded \(0.6614378<\omega<1\), but no claim is made here that the single-profile benchmark and this interval came from the same parameterization.

## 6. Radion: what was proposed and what is still missing

The radion was identified as a collective geometric modulus associated with relative PSU/Anti-Twin separation or a throat/radius degree of freedom. A prior wormhole/torus programme used sectors \(l<0\) (PSU) and \(l>0\) (Anti-Twin), and a throat coordinate \(R_{\rm th}\). A schematic interaction
\[
V_{\rm int}^{\rm throat}
=g\,W(R_{\rm th})\,\mathcal C(q_+,q_-),\qquad
\mathcal C=\frac12(q_+-q_-)^T\Lambda(q_+-q_-),
\quad\Lambda\succeq0,
\]
was explicitly an ansatz, not a derived radion potential.

A genuine radion sector requires:
1. a specified higher-dimensional or four-dimensional metric ansatz with modulus \(R_{\rm th}(x)\);
2. dimensional reduction of the gravitational/PSU–Anti-Twin action, including the radion kinetic term and normalization;
3. derivation of the effective radion potential from the action, boundary conditions and stabilizing flux/brane/source terms;
4. derivation of its coupling to \(\Phi_P,\Phi_A\), rather than inserting \(W(R_{\rm th})\) by hand;
5. the coupled Euler–Lagrange equations and full constrained Hessian.

Until then, “Q-ball–radion bound state” is a research target, not an established solution.

## 7. Relation to the existing Q-ball shell theorems

The field-theoretic soliton branch must be cross-linked to, but not identified with, the existing shell geometry:

- **T080** proves \(B_1B_2=0\), the exact discrete Stokes identity and finite-shell structured-gradient incompatibility for the generated closed triangulated shell. Counts: 92 triangulation vertices, 270 edges, 180 triangles, 90 physical seams; \(\chi=2\), \(b_1=0\). It does not prove a scalar Q-ball solution.
- **T088** defines panel tangent frames, seam transport \(U_{pq}\), gauge-covariant cycle holonomy and an \(H_4\)-derived tangent anisotropy tensor. The algebraic covariance and SPD statements are exact under the stated construction; material calibration, continuum curvature convergence and a seam constitutive law remain open.
- **T073** organizes the shell/RGS–PRISM–Q6 limit programme. It explicitly treats Q6 and the 92-node shell as different complexes and requires actual chain/field maps rather than matching node counts.

A possible future discretization is to place the two complex profiles on the shell or on a Q6-derived complex and use T080's incidence structure for discrete gradients and T088's panel connection for fibre transport. That requires a discrete \(U(1)\)-invariant action, a discrete Noether identity, a convergent radial/elliptic operator and a demonstrated continuum limit. None follows from shell topology alone.

## 8. Interfaces to QAT, photons, PSU and Anti-Twin

The common \(U(1)\) is a global phase symmetry of the two scalar fields in this model. It is **not automatically electromagnetic gauge \(U(1)\)** and does not by itself identify Q-ball charge with photon number, electric charge or a PSU Planck-scale unit.

A photon/QAT coupling would require a gauge field \(A_\mu\), covariant derivative \(D_\mu=\nabla_\mu-ieA_\mu\), a gauge-invariant action, Maxwell equations with the derived current, and a controlled weak-field/linearized limit. Quaternionic or spinorial transport identities can provide geometric data, but do not replace this field-theoretic derivation.

The PSU and Anti-Twin labels specify the two sectors and their exchange structure in this effective model. Their physical interpretation requires the metric, vierbein, stress tensor, conserved charges and coupling constants to be derived from the underlying PSU construction. The finite Anti-Twin involution \(J_{\rm AT}^2=I\) supplies exchange algebra, not the scalar-field action by itself.

## 9. Classification and next proof obligations

| Component | Classification |
|---|---|
| Finite PSU/Anti-Twin exchange \(J_{\rm AT}^2=I\) and reported \(128\to4\times32\) split | Exact finite-dimensional result as recorded; reproducible source/artifact link to be restored |
| Common \(U(1)\) and exchange \(Z_2\) of the two-field action | Exact symmetry of the declared model |
| Noether current and charge \(Q=2\omega I\) | Conditional theorem for the declared action/ansatz and normalization |
| Coupled radial equations | Euler–Lagrange equations conditional on the self-potential and still-undetermined \(V_{\rm int}\) |
| \(\kappa_\pm=V_{PP}\pm V_{PA}\) | Exact Hessian diagonalization at an exchange-symmetric background |
| \(0.6614378<\omega<1\) | Prior model-specific result; source normalization/replay required |
| \((\omega,E/Q)=(0.905607329,0.988291616)\) | Prior single-profile numerical benchmark, not coupled PSU–Anti-Twin |
| Radion \(W(R_{\rm th})\) interaction | Phenomenological ansatz; not derived |
| Radion kinetic term, stabilization and coupled Q-ball solution | Open |
| Photon/QAT gauging and physical charge identification | Open |
| Embedding of the field soliton on the T080/T088 shell or Q6 complex | Open |

**Immediate continuation order:** (i) restore/replay the historical derive_rgs_psu_sea.py source and exact \(128\to4\times32\) split; (ii) specify the smallest exchange-symmetric \(V_{\rm int}\) consistent with the PSU–Anti-Twin reduction, without fitting it to a desired solution; (iii) solve the coupled radial boundary-value problem and compute \(Q(\omega),E(\omega),dQ/d\omega\); (iv) analyze the full radial Hessian in the \(+\) and \(-\) sectors; (v) derive the radion action by reduction; (vi) only then gauge the common \(U(1)\) and connect to QAT/photons. T080/T088 can enter as a spatial discretization after the field action and chain maps are fixed.
