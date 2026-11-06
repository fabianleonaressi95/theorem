# Uniform FEEC stability on curvilinear cubical refinements

**Purpose.** This note isolates the analytic step between exact Stokes commutation and convergence. It proves the local metric/mass equivalence supplied by uniform geometry, states the precise additional hypothesis needed for a uniformly bounded commuting projection, and explains why the current face-integral routine does not by itself satisfy that hypothesis.

## 1. Uniform geometric hypothesis

Let \(\widehat K=(0,1)^d\), \(d\in\{2,3\}\), and let
\(F_{K,h}:\widehat K\to K_h\) be orientation-preserving cell diffeomorphisms in a conforming refinement family. Assume there are constants \(0<c_J\le C_J<\infty\), independent of \(h,K\), such that
\[
 c_J h |\xi|\le |DF_{K,h}(\widehat x)\xi|
 \le C_J h |\xi|,\qquad
 \widehat x\in\widehat K.
\tag{G1}
\]
Assume the ambient metric satisfies
\[
 0<g_- I\le G(x)\le g_+ I<\infty
\tag{G2}
\]
on the domain. For higher-order approximation estimates one additionally needs scaled derivative bounds, for example
\[
 \|D^mF_{K,h}\|_{L^\infty}\le C_m h^m
 \quad(m=2,\ldots,r+1),
\tag{G3}
\]
and corresponding uniform bounds for the scaled inverse maps. (G3) is not needed for the mass-equivalence result below.

## 2. Theorem: uniform local metric and mass equivalence

**Theorem 2.1.** Under (G1)–(G2), the pullback metric
\(g_{K,h}=DF_{K,h}^{T}G(F_{K,h})DF_{K,h}\) satisfies
\[
 g_-c_J^2h^2 I\le g_{K,h}(\widehat x)
 \le g_+C_J^2h^2 I
\]
pointwise. For every degree \(k\), the exact local FEEC Gram form on the fixed reference tensor-product space obeys
\[
 c_k h^{d-2k}\|\widehat v\|_{L^2(\widehat K)}^2
 \le
 \| (F_{K,h}^{-1})^*\widehat v\|_{L^2(K_h,G)}^2
 \le
 C_k h^{d-2k}\|\widehat v\|_{L^2(\widehat K)}^2,
\tag{2.1}
\]
where \(c_k,C_k>0\) depend only on \(d,k,c_J,C_J,g_-,g_+\), not on \(h\) or the cell.

**Proof.** The first inequality follows by applying (G2) to \(DF\xi\) and then (G1). The induced metric on covariant k-forms is the k-th exterior-power metric. Its eigenvalues lie between constants times \(h^{-2k}\), while the volume density \(\sqrt{\det g}\) lies between constants times \(h^d\). Their product therefore lies between constants times \(h^{d-2k}\). Integrating the pointwise bounds gives (2.1). \(\square\)

**Consequence.** On a shape-regular conforming cubical mesh with uniformly bounded cell incidence, summing (2.1) yields uniform spectral equivalence of the exact assembled mass matrices to the corresponding reference-element mass scaling. This is a coercivity/continuity statement for the *mass forms*. It is not a bound for a cochain interpolation operator.

For quadrature-assembled masses, the same conclusion requires a quadrature consistency estimate uniform in \(h,K\), or a uniformly coercive quadrature rule on the finite-dimensional reference space. Pointwise positivity at finitely many sampled nodes alone is not such a uniform estimate.

## 3. Theorem: what is sufficient for stable commuting projections

Let \(V^k=H\Lambda^k(\Omega)\), with graph norm
\[
 \|u\|_{H\Lambda^k}^2=\|u\|_{L^2\Lambda^k}^2+
 \|du\|_{L^2\Lambda^{k+1}}^2,
\]
and let \(V_h^\bullet\subset V^\bullet\) be conforming finite-dimensional subcomplexes.

**Theorem 3.1 (uniform projection criterion).** Suppose that for every \(h,k\) there is a linear map
\(\Pi_h^k:V^k\to V_h^k\) such that:

1. \((\Pi_h^k)^2=\Pi_h^k\) and \(\operatorname{ran}\Pi_h^k=V_h^k\);
2. \(d\Pi_h^k u=\Pi_h^{k+1}du\) for every \(u\) in the domain of \(d\);
3. there is a constant \(C_\Pi\), independent of \(h,k\), with
   \[
   \|\Pi_h^k u\|_{H\Lambda^k}\le C_\Pi\|u\|_{H\Lambda^k};
   \tag{3.1}
   \]
4. the spaces are dense in the graph norm in the refinement limit: for every \(u\in H\Lambda^k\), there are \(v_h\in V_h^k\) with \(v_h\to u\) in \(H\Lambda^k\).

Then \(\Pi_h^k u\to u\) strongly in \(H\Lambda^k\) for every \(u\in H\Lambda^k\), and the family is uniformly bounded as a cochain map.

**Proof.** Since \(\Pi_h^k\) is a projection, \(\Pi_h^k v_h=v_h\). Hence
\[
\|\Pi_h^ku-u\|_{H\Lambda^k}
\le \|\Pi_h^k(u-v_h)\|_{H\Lambda^k}
      +\|v_h-u\|_{H\Lambda^k}
\le (C_\Pi+1)\|u-v_h\|_{H\Lambda^k}\to0.
\]
Commutation is assumption 2, and the operator bound is (3.1). \(\square\)

This theorem is a sufficient criterion, not a proof that the benchmark's canonical interpolation has the stated properties. In standard FEEC constructions, one obtains such uniformly bounded commuting projections by combining local smoothing with a bounded cochain projection; the smoothing scale, patch overlap, geometry pullbacks, and boundary conditions all need uniform control.

## 4. Obstruction: canonical face interpolation is not automatically an HΛ projection

The routine `face_dofs` computes oriented face integrals (and vertex values in degree zero) for sufficiently regular input forms. It is an exact cochain interpolator on that regularity class, by Stokes' theorem. It is **not automatically a bounded map on** \(H\Lambda^k\).

Already for \(k=0\), \(H\Lambda^0=H^1(\Omega)\). In dimensions \(d\ge2\), point evaluation at a vertex is not a bounded functional on \(H^1(\Omega)\) in general: point values are not controlled by the H^1 norm. Thus the degree-zero nodal interpolation operator cannot be extended as a uniformly bounded operator \(H^1\to V_h^0\) merely from (G1)–(G3). For higher-degree face integrals, trace regularity presents the analogous issue.

Therefore:
- Stokes commutation on smooth forms is established;
- local mass coercivity follows from (G1)–(G2);
- uniform boundedness on the full \(H\Lambda\) graph space requires a *smoothed commuting projection* or another independently constructed regularized operator;
- geometry bounds alone do not supply that operator.

## 5. What the current repository establishes

The current benchmark provides:
- `face_dofs`: canonical face-integral cochains for analytic test forms;
- `commutation_residual`: finite-quadrature checks of Stokes commutation;
- `projection_l2_error`: approximation measurements on selected forms and meshes;
- `map_quality`: sampled Jacobian and inverse-Jacobian diagnostics;
- exact FEEC mass assembly formulas, with finite quadrature in computation.

It does **not yet** provide:
- a regularized FEEC projection defined on all of \(H\Lambda^k\);
- a proof of the uniform bound (3.1);
- a uniform quadrature-error/coercivity theorem for the whole refinement family;
- graph-norm density estimates for the actual curvilinear Herasymov family.

Consequently Theorem 3.1 is presently a conditional theorem whose hypotheses remain to be constructed and verified for this mesh family. It must not be reported as an established Mosco or spectral-convergence result.

## 6. Exact next proof obligations

1. Define a smoothing operator \(R_h^k\) on the physical domain (or a uniformly controlled reference-patch construction) and prove \(\|R_h^k\|_{H\Lambda\to H\Lambda}\le C\).
2. Construct a cochain projection \(P_h^k\) on the smoothed range and prove \(dP_h=P_hd\).
3. Set \(\Pi_h^k=P_h^kR_h^k\), verify idempotence and exact range, and prove the uniform graph bound.
4. Prove approximation/density uniformly for the non-affine curvilinear maps, including trace compatibility on shared faces.
5. Establish uniform quadrature consistency before transferring exact mass coercivity to the matrices used in the code.

Only after these steps should one use the resulting projections to build recovery sequences for the primal differential form. Discrete compactness and the lower-bound argument for the adjoint/Hodge energy remain separate obligations.
