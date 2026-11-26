# T089 — Gauge–fluid variational coupling on the anisotropic Q-ball bundle

**Date:** 11 November 2026  
**Status:** continuum variational derivation under stated smoothness and positivity assumptions; exact discrete gauge-invariance identities; finite-element convergence open.

**Dependencies:** T080, T086, T087, T088.

## 1. Fields and bundle meaning

Let \(\Sigma\) be the closed oriented Q-ball shell, regarded as a piecewise-smooth surface with panel charts. Let \(L\to\Sigma\) be a Hermitian complex line bundle with unitary connection \(a\), locally represented by a real one-form. Its curvature is \(F_a=da\) in a local trivialization. The local phase \(\theta\) is not itself globally defined when \(L\) is nontrivial; the gauge-covariant combination below is.

Let \(\rho:\Sigma\to(0,\infty)\) be the density and \(q\in\mathbb R\) the coupling. In each chart define
\[
v=d\theta-q\,a.
\]
For a gauge parameter \(\chi\),
\[
\theta'=\theta+q\chi,\qquad a'=a+d\chi,
\]
so
\[
\boxed{v'=v.}
\]
On overlaps these formulas are interpreted through the transition functions of \(L\); phase differences are circle-valued, not globally real-valued. If \(q\) is fixed by a chosen normalization of the \(U(1)\) representation, it is not an independently adjustable chart parameter.

The panel tensor \(A_p(\alpha)\) is the SPD, chart-covariant anisotropy from T088. It defines a measurable positive quadratic form on tangent covectors (using the induced metric to identify tangent vectors and covectors). For clarity, write the corresponding global tensor as \(A\).

## 2. A common energy for both sectors

Let \(V\) be an external scalar potential, \(W:(0,\infty)\to\mathbb R\) a differentiable internal-energy density, \(\kappa\ge0\) a density-gradient coefficient, \(g>0\) a gauge stiffness, and \(F_{\rm ext}\) a prescribed two-form. Put
\[
b=*_\Sigma(F_a-F_{\rm ext}).
\]
Consider the static energy
\[
\boxed{\begin{aligned}
\mathcal E[\rho,\theta,a]
=\int_\Sigma \bigg[
&\frac{\kappa}{2}
 \langle d\sqrt\rho,A\,d\sqrt\rho\rangle
+\frac{\rho}{2}\langle v,A\,v\rangle
+W(\rho)+V\rho\\
&+\frac{1}{2g^2}|F_a-F_{\rm ext}|^2
\bigg]\,dA.
\end{aligned}}
\tag{89.1}
\]
All terms are gauge invariant. The first term is a density-gradient/quantum-pressure regularizer; set \(\kappa=0\) for the classical barotropic potential-flow model. The second term is the fluid kinetic energy in the T088 anisotropic tangent metric. The last term is the gauge-curvature energy.

This is a proposed constitutive model, not a consequence of the combinatorics of Q6 or of the shell topology. The material functions \(W\), \(V\), and constants \(\kappa,g,q,\alpha\) require physical interpretation and calibration.

## 3. Euler–Lagrange equations

Assume for this derivation that \(\rho>0\), fields are sufficiently regular on each chart, and either \(\Sigma\) is closed with compatible bundle gluing or boundary/interface terms are included explicitly.

### 3.1 Phase variation: fluid continuity

For \(\theta\mapsto\theta+\varepsilon\zeta\), one has \(\delta v=d\zeta\). Thus
\[
\delta_\theta\mathcal E
=\int_\Sigma \rho\langle A v,d\zeta\rangle\,dA
=-\int_\Sigma \zeta\,\operatorname{div}_\Sigma(\rho A v)\,dA.
\]
Stationarity for all \(\zeta\) gives
\[
\boxed{\operatorname{div}_\Sigma(\rho A v)=0.}
\tag{89.2}
\]
This is the steady mass-conservation equation for the gauge-coupled anisotropic potential flow. The physical flux is \(\rho A v\), not \(\rho v\) unless \(A=I\).

### 3.2 Density variation: Bernoulli relation

Write \(s=\sqrt\rho\). For \(\delta\rho\), \(\delta s=\delta\rho/(2s)\). Integration by parts in the density-gradient term gives
\[
\delta_\rho\mathcal E
=\int_\Sigma \left[
-\frac{\kappa}{2\sqrt\rho}
 \operatorname{div}_\Sigma(A\,d\sqrt\rho)
+\frac12\langle v,A v\rangle
+W'(\rho)+V
\right]\delta\rho\,dA.
\]
If total mass \(\int_\Sigma\rho\,dA\) is fixed, the multiplier is a constant \(\mu\), and
\[
\boxed{
\frac12\langle v,A v\rangle+W'(\rho)+V
-\frac{\kappa}{2\sqrt\rho}\operatorname{div}_\Sigma(A\,d\sqrt\rho)
=\mu.
}
\tag{89.3}
\]
For \(\kappa=0\), this is the steady Bernoulli/chemical-potential relation. For a barotropic fluid with specific enthalpy \(h(\rho)=W'(\rho)\), it reads
\[
\frac12|v|_A^2+h(\rho)+V=\mu.
\]
The \(\kappa\)-term is the explicitly displayed density-gradient correction; it must not be silently discarded when \(\kappa>0\).

### 3.3 Connection variation: gauge field equation

Let \(\eta\) be an arbitrary real one-form variation of \(a\). Then \(\delta v=-q\eta\), \(\delta F_a=d\eta\), and
\[
\boxed{
\int_\Sigma \left[
\frac1{g^2}\langle F_a-F_{\rm ext},d\eta\rangle
-q\rho\langle A v,\eta\rangle
\right]dA=0
\quad\text{for every }\eta.
}
\tag{89.4}
\]
This weak equation is the gauge-field Euler–Lagrange equation and fixes the sign convention unambiguously. In differential-form notation, on a closed surface it is equivalently
\[
\frac1{g^2}d_\Sigma^*(F_a-F_{\rm ext})
=q\,(\rho A v)^\flat,
\]
where the codifferential convention is \(d^*=\delta\) and the musical map uses the surface metric. The weak form (89.4) is primary if conventions differ.

The current sourcing the gauge field is
\[
j=q\rho A v.
\]
Thus the gauge equation and the Bernoulli/continuity equations are not independent decorations: they are the three stationarity conditions of one energy.

## 4. Curvature–vorticity identity

Locally, where \(\theta\) is a smooth real phase,
\[
dv=d^2\theta-q\,da=-qF_a.
\]
Therefore
\[
\boxed{dv=-qF_a.}
\tag{89.5}
\]
The gauge curvature is the source of vorticity in this model. This statement is local and exact away from phase singularities. If \(\theta\) has vortices/zeros of the underlying complex field, their quantized distributional contribution must be added; it is not covered by the smooth positive-density hypothesis \(\rho>0\).

## 5. Discrete gauge invariance on the Q-ball complex

Use the oriented incidence matrices \(B_1\) and \(B_2\) from T080. Let \(\vartheta\in\mathbb R^{|\mathcal V|}\) be a nodal phase cochain and \(a\in\mathbb R^{|\mathcal E|}\) an edge connection cochain. In the chosen edge orientation define
\[
v_h=B_1^T\vartheta-q\,a,\qquad
f_h=B_2^Ta.
\]
For any nodal gauge parameter \(\chi\), set
\[
\vartheta'=\vartheta+q\chi,\qquad
a'=a+B_1^T\chi.
\]
Then, using \(B_1B_2=0\),
\[
\boxed{v_h'=v_h,\qquad f_h'=f_h.}
\tag{89.6}
\]
The first identity is exact edgewise. The second is exact facewise. Thus any discrete energy assembled solely from gauge-invariant reconstructions of \(v_h\), \(f_h\), density, and the chart-covariant \(A_p\) is invariant under these discrete gauge transformations.

A consistent implementation must reconstruct \(v_h\) as a tangent one-form (for example with Whitney 1-forms or a compatible covariant finite-element space) before applying the \(2\times2\) panel tensor \(A_p\). It is mathematically incorrect to multiply a scalar edge cochain directly by \(A_p\).

## 6. Interfaces and physical seams

A panel boundary is a chart interface unless an actual independent trace/disarrangement is introduced. On a pure chart interface, the line-bundle transition identifies the two local phases and connection forms; no physical seam energy is added.

If independent traces are physically intended, define the covariant phase mismatch using the \(U(1)\) transition \(h_{pq}\):
\[
J_{pq}=\theta_q-\theta_p-\arg h_{pq}
\quad\pmod{2\pi}.
\]
A possible interface energy is
\[
\mathcal E_{\rm seam}
=\frac12\sum_{\Gamma_{pq}}\lambda_{pq}
 \int_{\Gamma_{pq}}|e^{iJ_{pq}}-1|^2\,ds.
\]
It is gauge invariant when the transition is transformed with the local trivializations. This is only a candidate interface law. It is not implied by T086–T088 and does not yet represent fatigue, friction, cohesive damage, or hysteresis. Those require internal variables and a dissipative evolution law.

## 7. What has and has not been derived

**Derived from (89.1):**
- anisotropic steady continuity (89.2);
- Bernoulli/chemical-potential equation including the density-gradient correction (89.3);
- gauge-field equation in weak form (89.4);
- curvature–vorticity identity (89.5);
- exact discrete gauge invariance (89.6), conditional only on the T080 incidence identity.

**Not derived or validated:**
- the physical choice of \(W,\kappa,g,q,\alpha\);
- compressible time-dependent Euler/Navier–Stokes dynamics or viscosity;
- a calibrated relation between panel holonomy and Gaussian curvature;
- seam damage, fatigue, hysteresis, or manufacturing constitutive laws;
- \(\Gamma\)-/Mosco-convergence of the discrete energies to (89.1);
- a derivation of this model from the microscopic PSU/Anti-Twin degrees of freedom.

## 8. Next mathematical obligations

1. Implement a Whitney/covariant finite-element reconstruction of \(v_h\) on the actual 180 triangles, with the T088 panel tensor pulled back to each triangle.
2. Verify (89.6) numerically under random nodal gauge transformations, including nonzero face curvature.
3. Derive the discrete first variations and compare them with (89.2)–(89.4).
4. Only then introduce a seam internal variable and a rate-independent or viscoelastic dissipation potential for hysteresis.
5. Establish coercivity, compactness, liminf and recovery estimates for a shape-regular refinement family before claiming a surface SBV relaxation or a Gamma/Mosco limit.

**Classification:** continuum Euler–Lagrange derivation — proved under the stated smoothness and positivity assumptions; discrete gauge identities — exact; constitutive interpretation and numerical convergence — open.
