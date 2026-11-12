# T134 — Conditional coercivity of the symmetric C0 interior-penalty Hessian form

**Classification:** [P] abstract coercivity theorem under an explicit mesh-uniform trace-inverse hypothesis and a penalty threshold. **Not yet certified:** the numerical value \(\alpha=10\) in the current curved P3 implementation has not been shown to exceed the required threshold.

**Dependencies:** T133 for the finite-dimensional constrained minimization result. Implementation under audit: `scripts/rgs_morandotti_c0_ipdg.py`; reproduction specification: `docs/rgs_defect_benchmark/MORANDOTTI_C0_IPDG_REPRODUCTION_PLAN.md`.

## 1. Setting and assumptions

Let \(\mathcal T_h\) be a connected, shape-regular triangulation of a bounded polygonal domain (or a uniformly shape-regular family of curved element maps). Let \(V_h\subset H^1(\Omega)\) be a continuous, elementwise-polynomial space of fixed degree at least two. Let \(\Gamma_D\) be the clamped boundary, and impose homogeneous Dirichlet trace on \(\Gamma_D\). The normal derivative is weakly imposed by the boundary penalty.

Write \(D_h(v)^2=\sum_{K\in\mathcal T_h}\|D^2v\|_{L^2(K)}^2\). Let \(\mathcal F_h^i\) denote interior facets and \(\mathcal F_h^D\) clamped boundary facets. On an interior facet, \([\partial_n v]\) denotes the sum of the two outward normal derivatives, and \(\{\partial_{nn}v\}\) the average of the two normal-normal Hessian traces. On a boundary facet these are replaced by \(\partial_n v\) and \(\partial_{nn}v\).

Define
\[
J_h(v)^2=
\sum_{F\in\mathcal F_h^i}h_F^{-1}\|[\partial_n v]\|_{L^2(F)}^2+
\sum_{F\in\mathcal F_h^D}h_F^{-1}\|\partial_n v\|_{L^2(F)}^2,
\]
and
\[
H_h(v)^2=
\sum_{F\in\mathcal F_h^i}h_F\|\{\partial_{nn}v\}\|_{L^2(F)}^2+
\sum_{F\in\mathcal F_h^D}h_F\|\partial_{nn}v\|_{L^2(F)}^2.
\]

Assume the following uniform trace-inverse estimate, with a constant \(C_{\rm tr}\) independent of \(h\):
\[
H_h(v)^2\le C_{\rm tr}D_h(v)^2
\qquad\forall v\in V_h^0.
\]
Here \(V_h^0\) is the homogeneous test space. For curved P3 elements this assumption includes uniform bounds on the element-map Jacobians and their scaled derivatives; ordinary straight-element shape regularity alone is not a substitute for those geometric bounds.

Consider the symmetric bilinear form
\[
\begin{aligned}
a_h(u,v)={}&\sum_K(D^2u,D^2v)_K\\
&-\sum_{F\in\mathcal F_h^i}
\big(\langle\{\partial_{nn}u\},[\partial_n v]\rangle_F+
\langle\{\partial_{nn}v\},[\partial_n u]\rangle_F\big)\\
&-\sum_{F\in\mathcal F_h^D}
\big(\langle\partial_{nn}u,\partial_n v\rangle_F+
\langle\partial_{nn}v,\partial_n u\rangle_F\big)\\
&+\alpha J_h(u,v),
\end{aligned}
\]
where \(J_h(u,v)\) is the bilinear form associated with \(J_h(\cdot)^2\), and \(\alpha>0\) is the penalty parameter.

## 2. Theorem

If the trace-inverse estimate holds and
\[
\boxed{\alpha>2C_{\rm tr},}
\]
then
\[
\boxed{
a_h(v,v)\ge
\frac12D_h(v)^2+
\left(\alpha-2C_{\rm tr}\right)J_h(v)^2
\qquad\forall v\in V_h^0.
}
\]
In particular, \(a_h\) is coercive in the mesh-dependent norm
\[
\|v\|_{2,h}^2:=D_h(v)^2+J_h(v)^2.
\]
If the homogeneous boundary conditions eliminate the affine kernel, this norm controls the corresponding discrete \(H^2\) norm through the discrete Poincare/Friedrichs inequality.

## 3. Proof

By Cauchy–Schwarz on the union of interior and clamped boundary facets,
\[
\left|\sum_F\langle\text{normal-normal Hessian trace},
\text{normal derivative jump/trace}\rangle_F\right|
\le H_h(v)J_h(v).
\]
The two symmetric consistency contributions therefore have absolute value at most \(2H_h(v)J_h(v)\). Using the assumed trace-inverse estimate and Young's inequality,
\[
2H_h(v)J_h(v)
\le2\sqrt{C_{\rm tr}}D_h(v)J_h(v)
\le\frac12D_h(v)^2+2C_{\rm tr}J_h(v)^2.
\]
Consequently,
\[
\begin{aligned}
a_h(v,v)
&\ge D_h(v)^2-\frac12D_h(v)^2
+\alpha J_h(v)^2-2C_{\rm tr}J_h(v)^2\\
&=\frac12D_h(v)^2+
(\alpha-2C_{\rm tr})J_h(v)^2.
\end{aligned}
\]
The stated penalty condition makes both coefficients strictly positive. This proves coercivity. \(\square\)

## 4. What this theorem does and does not certify

The proof is conditional on the stated trace-inverse estimate. It supplies a transparent sufficient penalty threshold, not an estimate of the sharp threshold.

In the current implementation, the facet consistency terms and \(\alpha/h\) penalties have this symmetric C0-IPDG structure. However, the proof above does **not** establish that the code's curved P3 mesh family has one uniform constant \(C_{\rm tr}\), nor that \(10>2C_{\rm tr}\). Thus the implementation's \(\alpha=10\) remains an empirically tested parameter, not a mathematically certified coercive choice.

Before claiming uniform coercivity for the actual solver, the audit must:
1. prove or bound \(C_{\rm tr}\) for the actual curved-element maps and facet scaling;
2. verify that the assembled facet orientations and boundary terms match the displayed symmetric form;
3. show the imposed homogeneous test space removes the affine kernel;
4. document a penalty satisfying the proved bound, uniformly over the mesh family.

Even after coercivity, convergence requires consistency, approximation, and mesh-uniform continuity estimates (and regularity of the exact cell fields). T134 alone does not prove an \(H^2\) error estimate, convergence of cell solutions, convergence of the interaction matrix, or a continuum distance law.
