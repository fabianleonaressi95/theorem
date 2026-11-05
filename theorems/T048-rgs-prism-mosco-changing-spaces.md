# T048 — Mosco convergence and spectral compactness for RGS–PRISM refinements

**Status: convergence framework and falsifiable proof obligations. Not yet a Mosco-convergence theorem for the RGS–PRISM sequence.**

## 1. Scope and logical separation

The target is a sequence of weighted discrete spaces
\[
(H_h,\mathcal E_h),\qquad h\downarrow0,
\]
approximating a continuum space \((H,\mathcal E)\), where the discrete vertex/edge sets, measures, and possibly the underlying geometric realizations vary with \(h\).

Four conclusions must not be conflated:

1. Mosco convergence of closed nonnegative forms on varying Hilbert spaces;
2. strong resolvent (equivalently, semigroup) convergence under a consistent varying-space identification;
3. collective compactness of energy-bounded sequences / compactness of resolvents;
4. convergence of isolated eigenvalues, multiplicities, and spectral subspaces.

Items 1–2 do not by themselves imply 3–4. Intrinsic metric estimates, volume doubling, and Sobolev inequalities are useful inputs, but are not by themselves a substitute for a compactness/tightness argument. In noncompact settings, mass escape must be ruled out separately.

This note therefore specifies the missing structures and a testable proof programme. It does **not** claim that the current finite PRISM graph or the 188-dimensional tangent data already form a refining sequence.

## 2. Varying Hilbert spaces: data that must be fixed

For every resolution \(h\), specify:

- a countable or finite vertex set \(V_h\);
- a vertex measure \(m_h(x)>0\);
- symmetric edge conductances \(b_h(x,y)=b_h(y,x)\ge0\), with \(b_h(x,x)=0\);
- the Hilbert space \(H_h=\ell^2(V_h,m_h)\);
- the form domain \(D(\mathcal E_h)\) and the closed form
  \[
  \mathcal E_h(u)=\frac12\sum_{x,y\in V_h}
  b_h(x,y)|u(x)-u(y)|^2;
  \]
- the associated nonnegative self-adjoint operator \(L_h\), with the convention
  \(\mathcal E_h(u,v)=\langle L_hu,v\rangle_{H_h}\) on the operator domain.

The factor \(1/2\) is part of the convention and must not silently change between resolutions. For finite graphs the form domain is all of \(H_h\). For infinite graphs, closedness and the choice of minimal/Neumann or maximal/Dirichlet realization must be stated.

A weighted graph Laplacian is not determined by its adjacency matrix alone: both \(m_h\) and \(b_h\), and their scaling with \(h\), are part of the approximation.

## 3. Identification maps and generalized Mosco convergence

Choose a dense core \(\mathcal C\subset H\) and linear maps
\[
J_h:\mathcal C\to H_h
\]
(or equivalent comparison maps \(I_h:H_h\to H\)). State and prove norm consistency:
\[
\|J_h f\|_{H_h}\longrightarrow\|f\|_H,
\qquad f\in\mathcal C.
\]

The maps induce the strong and weak convergence notions for \(u_h\in H_h\). These notions must be written explicitly in the paper/code specification; “embed all spaces in a common Hilbert space” is not enough unless the embeddings are compatible with the norms and the adjoint/comparison maps.

A useful concrete choice for a mesh partition is:
- \(J_h f\): cell averages of \(f\);
- \(I_h u_h\): piecewise-constant reconstruction;
- \(I_h\) is isometric when \(m_h(x)\) equals the measure of the cell represented by \(x\).

For a curved RGS–PRISM refinement, the cells, measure, and reconstruction must be defined geometrically, not inferred from graph labels alone.

Generalized Mosco convergence consists of two independent conditions:

**(M1) weak liminf.** If \(u_h\) weakly converges to \(u\), then
\[
\mathcal E(u)\le\liminf_{h\to0}\mathcal E_h(u_h).
\]

**(M2) strong recovery.** For every \(u\in D(\mathcal E)\), there is a strongly convergent \(u_h\to u\) such that
\[
\limsup_{h\to0}\mathcal E_h(u_h)\le\mathcal E(u).
\]

The target form \(\mathcal E\) must itself be densely defined, closed, and nonnegative. For the scalar case, Markovianity may be required if the target is a Dirichlet form and a sub-Markov semigroup is intended. Do not impose that property on higher-degree Hodge forms.

Under the appropriate Kuwae–Shioya varying-Hilbert-space hypotheses, generalized Mosco convergence is equivalent to strong convergence of the associated resolvents/semigroups. This equivalence concerns strong operator convergence, not norm-resolvent convergence and not convergence of isolated eigenvalues with multiplicity.

## 4. Intrinsic metrics: geometric control, not compactness by themselves

For a weighted graph, an intrinsic pseudometric \(d_h\) must satisfy, with the present form convention,
\[
\sum_y b_h(x,y)d_h(x,y)^2\le m_h(x).
\]
The precise factor changes if the form convention changes. Require finite jump size and, where relevant, finite balls.

Intrinsic metrics provide the correct geometry for graph heat-kernel estimates and volume-growth hypotheses. Doubling and Sobolev estimates can yield heat-kernel bounds in suitable settings. They do not alone establish precompactness of arbitrary energy-bounded sequences across a changing family.

For compact target spaces, a proof still needs a uniform discrete Rellich theorem / translation estimate / approximation-number estimate. For noncompact targets it additionally needs tightness, for example a uniform tail condition
\[
\lim_{R\to\infty}\sup_h
\sum_{x:\ d_h(x,K_h)>R}m_h(x)|u_h(x)|^2=0
\]
for the relevant energy-bounded family, with base sets \(K_h\) and comparison maps specified. This is a schematic condition: the actual exhaustion and distance must be compatible with the limit space.

A usable compactness lemma for the RGS programme should have the form:
\[
\sup_h\big(\|u_h\|_{H_h}^2+\mathcal E_h(u_h)\big)<\infty
\quad\Longrightarrow\quad
\{u_h\}\text{ is relatively strongly compact}.
\]
It must be proved from uniform geometric/analytic estimates, not asserted from doubling alone.

## 5. From strong resolvent to eigenvalues: the extra step

Let \(R_h=(L_h+1)^{-1}\). Strong resolvent convergence controls \(R_h f_h\) for convergent data under the chosen identifications. It does not prevent spectral pollution/escape and does not by itself force convergence of isolated eigenvalues or eigenspaces.

For spectral convergence on a compact limit, establish compactness of the limit form embedding
\[
D(\mathcal E)\hookrightarrow H
\]
and collective compactness of the identified resolvents (or a suitable generalized norm-resolvent estimate). Then use the min–max principle and spectral projection estimates to prove convergence of each isolated finite-multiplicity eigenvalue cluster and its spectral subspace.

The proof ledger must report separately:
- convergence of eigenvalues;
- preservation of multiplicity;
- convergence of spectral projections/eigenspaces;
- absence of spectral pollution in the window under study.

On a noncompact limit, the essential spectrum may persist. In that case the theorem must target isolated eigenvalues below/away from the essential spectrum and state the relevant compactness or localization assumptions.

## 6. Higher-degree Hodge forms: a separate convergence problem

For a weighted simplicial complex, let \(C_h^k\) be the \(k\)-cochains with a specified inner product, and let
\[
d_h^k:C_h^k\to C_h^{k+1},\qquad d_h^{k+1}d_h^k=0.
\]
The Hodge form is
\[
\mathcal Q_h^k(\omega)
=\|d_h^k\omega\|_{H_h^{k+1}}^2
+\| (d_h^{k-1})^*\omega\|_{H_h^{k-1}}^2,
\]
with its closed form domain specified. The associated operator is
\[
\Delta_h^k=(d_h^k)^*d_h^k+d_h^{k-1}(d_h^{k-1})^*.
\]

For every degree, specify:
- simplex weights and the induced cochain Hilbert norms;
- boundary/coboundary sign conventions;
- closedness/self-adjoint realization;
- cochain identification maps to the continuum \(k\)-form space;
- convergence of both \(d_h^k\) and their adjoints (or an equivalent form argument);
- treatment of harmonic subspaces and cohomology.

The scalar Markov property is not available in general for \(k\ge1\). Thus scalar Dirichlet-form contraction arguments cannot simply be copied to Hodge Laplacians. The complex identity \(d_h^{k+1}d_h^k=0\), uniform control of the cochain norms, and convergence of the full quadratic form are separate obligations.

## 7. Concrete proof programme for RGS–PRISM

The programme is ordered to prevent an unjustified jump from a finite graph spectrum to a continuum claim.

### Stage A — Freeze the approximation sequence

Publish a sequence \(X_h\) of actual RGS–PRISM refinements, not only one graph. For every \(h\), archive:
- vertices, edges, faces, higher cells and incidence matrices;
- vertex/simplex measures and edge/simplex weights;
- mesh size and intrinsic metric;
- geometric realization and cell-to-continuum reconstruction;
- symmetry action and boundary conditions.

The current PRISM graph \(C_{64}\square C_6^3\square C_5\) is one finite object. Its Betti numbers and gap are finite-level invariants; they do not establish a refinement limit.

### Stage B — Scalar energy consistency

Choose a target compact manifold/orbifold (or explicitly defined metric-measure space) and a dense smooth core. Prove:
1. norm consistency of \(J_h\);
2. convergence of \(\mathcal E_h(J_hf)\) to the target energy for smooth \(f\);
3. a recovery construction for all \(f\in D(\mathcal E)\);
4. the weak liminf inequality for every weakly convergent energy-bounded sequence.

Only after all four may scalar Mosco convergence be claimed.

### Stage C — Uniform compactness

Prove a uniform discrete Rellich estimate. On compact targets this can be a translation/oscillation estimate tied to the mesh and energy. On noncompact targets include a uniform tail/tightness estimate preventing mass escape. Track constants uniformly in \(h\).

### Stage D — Spectral conclusion

Use generalized resolvent convergence for strong operator convergence. Use the compactness result (or generalized norm-resolvent control) separately for eigenvalue clusters, multiplicities, and eigenspaces.

### Stage E — Hodge degrees

Repeat the construction in each degree using cochain Hilbert spaces and the Hodge forms. Do not infer higher-degree convergence from the scalar result or from Betti-number stability alone.

## 8. Finite verification model: periodic cycle

The companion script implements a transparent one-dimensional calibration, not the RGS sequence. On the periodic cycle with \(n\) vertices, set
\[
m_n(i)=1/n,\qquad b_n(i,i+1)=n.
\]
Then
\[
\mathcal E_n(u)=n\sum_{i=0}^{n-1}|u_{i+1}-u_i|^2
\]
is the standard finite-difference approximation to \(\int_{S^1}|f'(x)|^2dx\). For a fixed Fourier mode \(k\), the exact discrete eigenvalue is
\[
\lambda_{n,k}=4n^2\sin^2(\pi k/n)
\longrightarrow4\pi^2k^2.
\]
The tests check this limit, mass normalization, and energy convergence for sampled smooth Fourier modes. They are regression/calibration checks; they are not a proof of Mosco convergence for arbitrary sequences and are not evidence that the RGS–PRISM weights already satisfy the required estimates.

## 9. References and how they are used

1. M. Keller, D. Lenz, R. K. Wojciechowski, *Graphs and Discrete Dirichlet Spaces*, Springer, 2021. Foundational weighted graph forms, Laplacians, intrinsic metrics, and operator realizations.
2. M. Keller, F. Münch, R. K. Wojciechowski, “Neumann semigroup, subgraph convergence, form uniqueness, stochastic completeness and the Feller property,” *J. Geom. Anal.* 35 (2025), DOI 10.1007/s12220-024-01838-9, arXiv:2310.14927. A specific induced-subgraph/Neumann semigroup approximation, not a general theorem for arbitrary curved refinements.
3. M. Keller, “Intrinsic Metrics on Graphs: A Survey” (2015), arXiv:1407.7453. Intrinsic metric framework and graph geometry.
4. M. Keller, C. Rose, “Gaussian upper bounds, volume doubling and Sobolev inequalities on graphs,” *J. Éc. polytech. Math.* 13 (2026), 965–1005, DOI 10.5802/jep.340. Heat-kernel, doubling, and Sobolev relations under the paper's hypotheses; not a stand-alone compactness theorem for changing spaces.
5. P. Bartmann, M. Keller, “On Hodge Laplacians on General Simplicial Complexes,” arXiv:2508.07761 (2025). Operator/form foundations on weighted simplicial complexes, not a convergence theorem for curved cubical refinements.
6. O. Post, *Spectral Analysis on Graph-like Spaces*, Lecture Notes in Mathematics 2039, Springer, 2012. Abstract varying-space operator comparison and norm-resolvent/spectral convergence in graph-like settings.
7. M. Keller, L. Pettinari, C. J. F. van de Ven, “Coupling of the continuum and semiclassical limit. Part I: convergence of eigenvalues,” arXiv:2602.23156 (2026). A specific mesh-discretized semiclassical setting; useful as a model of a theorem with explicit hypotheses, not directly transferable to RGS.

## 10. Evidence ledger

| Claim | Status |
|---|---|
| Weighted graph form and associated operator convention in §2 | Defined |
| Varying-space M1/M2 obligations | Defined |
| Strong resolvent does not alone imply eigenvalue/multiplicity convergence | Established operator-theoretic distinction |
| Intrinsic metric/doubling/Sobolev as geometric analytic controls | Literature-backed, hypotheses required |
| Need uniform compactness/tightness for the desired spectral conclusion | Proof obligation identified |
| Periodic-cycle Fourier calibration | Numerically testable exact finite model |
| Mosco convergence of the actual RGS–PRISM refinement | Open |
| Uniform discrete Rellich/tightness for RGS–PRISM | Open |
| Hodge-form convergence for degrees k≥1 | Open |
| Continuum spectral convergence with multiplicities/eigenspaces | Open |

## 11. Reproducibility

Run:
\`\`\`bash
python -m pytest tests/test_t048_rgs_prism_mosco_calibration.py -q
python -m scripts.rgs_prism_mosco_calibration --n 32 64 128 256 --mode 1
\`\`\`

The tests are deterministic. Passing them validates only the periodic-cycle calibration and its implementation, not the open RGS–PRISM convergence theorem.
