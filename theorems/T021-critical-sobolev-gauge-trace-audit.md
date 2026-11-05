# T021 — Critical Sobolev gauge fields: continuum operator, edge traces, and the missing lattice limit

**Status:** PARTIAL ANALYTIC AUDIT. The continuum operator is well-defined under the stated assumptions, and edgewise parallel transport has a canonical trace-based meaning at the critical exponent. The generalized strong-resolvent limit at \(W^{1,6}\) regularity is **OPEN** in this note. No \(p=6\) lattice convergence theorem is claimed.

## 1. Scope and geometry

The ambient continuum space is the six-torus
\[
\mathbb T^6_2=(\mathbb R/2\mathbb Z)^6.
\]
The approximating spaces are periodic six-dimensional lattices
\[
\Lambda_n=(\mathbb Z/(2n)\mathbb Z)^6,\qquad h_n=n^{-1}.
\]
This is the periodic refinement used in T017–T020 and M1. It is not the single 64-vertex graph \(Q_6\).

Let \(\mathcal A_i\in W^{1,6}(\mathbb T^6_2;\mathfrak{su}(3))\), \(i=1,\ldots,6\).

The purpose is to distinguish four questions which must not be conflated:

1. whether the continuum Dirac operator is defined and closed;
2. whether a connection has a well-defined trace on each lattice edge;
3. whether endpoint-sampled lattice gauge transformations are defined;
4. whether the discrete Wilson operators converge in generalized strong-resolvent sense.

## 2. Continuum operator at \(W^{1,6}\)

Since the torus has finite measure, \(W^{1,6}\subset L^6\). Define
\[
D_0=\sum_{i=1}^6\Gamma_i\partial_i,
\qquad
V_{\mathcal A}=\sum_{i=1}^6\Gamma_i\mathcal A_i,
\qquad
D_{\mathcal A}=D_0+V_{\mathcal A},
\]
where the \(\Gamma_i\) are constant Hermitian Clifford matrices and \(\mathcal A_i\) act on colour.

For \(\psi\in H^1(\mathbb T^6_2;\mathbb C^8\otimes\mathbb C^3)\), Sobolev embedding gives \(H^1\hookrightarrow L^3\), hence
\[
\|V_{\mathcal A}\psi\|_2
\leq C\|\mathcal A\|_6\|\psi\|_3
\leq C\|\mathcal A\|_6\|\psi\|_{H^1}.
\]
The Clifford identity yields the elliptic graph estimate
\[
\|\psi\|_{H^1}\leq C(\|D_0\psi\|_2+\|\psi\|_2).
\]

More is true: the perturbation has relative bound zero. For a truncation \(\mathcal A^{(M)}\) with bounded coefficients, write
\(\mathcal A=\mathcal A^{(M)}+\mathcal R^{(M)}\), where
\(\|\mathcal R^{(M)}\|_6\to0\). Then
\[
\|V_{\mathcal R^{(M)}}\psi\|_2
\leq C\|\mathcal R^{(M)}\|_6
(\|D_0\psi\|_2+\|\psi\|_2),
\]
while
\[
\|V_{\mathcal A^{(M)}}\psi\|_2
\leq C_M\|\psi\|_2.
\]
Thus for every \(\varepsilon>0\) there is \(C_\varepsilon\) such that
\[
\|V_{\mathcal A}\psi\|_2
\leq\varepsilon\|D_0\psi\|_2+C_\varepsilon\|\psi\|_2.
\]

Because \(\mathcal A_i\) is anti-Hermitian and commutes with the spin matrices, \(V_{\mathcal A}\) is skew-symmetric on \(H^1\). The relative-bound-zero theorem applied to \(iD_0\) and \(iV_{\mathcal A}\) therefore gives a skew-adjoint realization of \(D_{\mathcal A}\) on \(H^1\).

**Conclusion:** the continuum differential operator is not the obstruction at \(p=6\). Under these hypotheses it has a natural closed skew-adjoint realization on \(H^1\). This does not by itself prove convergence of lattice operators.

## 3. Edge traces at the critical exponent

A lattice link uses a one-dimensional edge \(e\subset\mathbb T^6_2\). The edge has codimension five. The Sobolev trace theorem for a smooth one-dimensional submanifold applies when \(p>5\):
\[
W^{1,p}(\mathbb T^6_2)
\longrightarrow
B^{1-5/p}_{p,p}(e).
\]
At \(p=6\), this gives
\[
\operatorname{Tr}_e\mathcal A_i
\in B^{1/6}_{6,6}(e)\subset L^6(e)\subset L^1(e).
\]

Consequently, for each fixed edge, the coefficient has a canonical trace class along that edge. The Carathéodory integral equation
\[
\frac{dU}{dt}=U(t)\operatorname{Tr}_e\mathcal A_i(t),
\qquad U(0)=I,
\]
has a unique absolutely continuous solution. Anti-Hermiticity implies \(U(t)\in SU(3)\).

This is the correct critical-exponent replacement for the invalid operation of evaluating a generic \(W^{1,6}\) representative at a lattice vertex.

**Important distinction:** the trace is defined almost everywhere along the edge; it does not supply a canonical value at either endpoint. The link ODE only needs the almost-everywhere edge coefficient, but a vertex-sampled gauge transformation does need endpoint values.

## 4. Gauge covariance at the critical exponent

For smooth periodic \(g:\mathbb T^6_2\to SU(3)\), the usual endpoint values exist and the exact link law
\[
U_i^g(x)=g(x)U_i(x)g(x+he_i)^\dagger
\]
is meaningful. The parallel-transport ODE gives this identity with the convention
\[
\mathcal A_i^g=g\mathcal A_i g^\dagger-(\partial_i g)g^\dagger.
\]

For a merely \(W^{1,6}\) gauge transformation, point values \(g(x_j)\) are not generally defined. The trace on a one-dimensional edge is not a substitute for a value at its endpoint. Therefore the standard vertex-multiplication lattice gauge map \(G_n\psi(x_j)=g(x_j)\psi(x_j)\) is not defined for a general \(W^{1,6}\) gauge transformation.

A theorem at critical regularity must either:
- restrict lattice covariance statements to smooth (or continuous) gauge transformations; or
- define a different discrete gauge action using additional data and prove its compatibility.

## 5. Why M1 does not already prove the critical case

M1 uses a continuous connection, exact edge transport, and the consistency estimate on smooth sections
\[
\|A_{n,\mathcal A}I_n\Psi-I_n(A_{\mathcal A}\Psi)\|_n
\leq C_\Psi h_n^\alpha.
\]
For \(W^{1,6}\) coefficients:
- point sampling \(I_n(\mathcal A\Psi)\) is not defined in general;
- the Hölder expansion \(U_i(x)=I+h\mathcal A_i(x)+O(h^{1+\alpha})\) is unavailable;
- edge traces exist, but the required uniform estimates over all shrinking lattice edges have not been established here;
- the correct comparison of continuum and discrete outputs must use cell averages or another \(L^2\)-stable identification, not nodal interpolation of \(\mathcal A\Psi\).

Thus the dense-core argument in M1 cannot simply be copied with \(C^{0,\alpha}\) replaced by \(W^{1,6}\).

## 6. Required estimates for a genuine \(p=6\) theorem

A valid extension must supply all of the following.

1. **Skeleton trace estimate.** A scale-explicit estimate for the traces of \(W^{1,6}\) fields on the complete family of lattice edges, uniform in \(n\) in the aggregate norm needed by the operator.
2. **Transport stability.** A bound comparing path-ordered exponentials for edge traces, including the effect of local mollification if used.
3. **Cellwise consistency.** A consistency statement formulated with \(L^2\) cell averages or another bounded comparison map; no pointwise sampling of \(\mathcal A\).
4. **Uniform operator stability.** The Wilson accretivity estimate must remain uniform and must be combined with the correct discrete-to-continuum comparison.
5. **Dense-range argument.** Prove convergence on a genuine dense subset of the continuum Hilbert space and extend it using uniform resolvent bounds.
6. **Gauge scope.** State separately the class of gauge transformations for which the finite-lattice covariance identity is meaningful.

Possible approaches include smooth approximation \(\mathcal A^{(\epsilon)}\to\mathcal A\) in \(L^6\), trace-compatible link construction, and a two-parameter limit \(h\to0\), \(\epsilon\to0\). The order of limits and uniformity in both parameters must be proved, not assumed.

## 7. Regularity map

| Connection regularity in dimension 6 | Continuum Dirac on \(H^1\) | Edge transport | Vertex sampling | Strong-resolvent limit |
|---|---|---|---|---|
| \(C^{0,\alpha}\), \(0<\alpha\leq1\) | Defined | Classical ODE | Defined | M1 proved under its stated hypotheses |
| \(C^0\) | Defined | Classical ODE | Defined | M1 records qualitative extension via modulus of continuity |
| \(W^{1,p}\), \(p>6\) | Defined | Classical representative / trace | Defined by Morrey continuity | Follows from M1 after Morrey embedding, with exponent \(\alpha=1-6/p\) |
| \(W^{1,6}\) | Defined by relative-bound-zero perturbation | Canonical edge trace in \(L^6(e)\) | Not generally defined | OPEN: new skeleton and consistency estimates required |
| \(W^{1,p}\), \(p\leq5\) | Requires separate analysis | General codimension-five edge trace is not supplied by the above trace theorem | Not generally defined | OPEN |

## 8. Verdict

- **PROVED (standard Sobolev/perturbation framework):** \(W^{1,6}\) coefficients define a relatively bounded, relative-bound-zero perturbation of the free six-dimensional Dirac operator on \(H^1\).
- **PROVED (trace theorem):** for \(p=6>5\), each fixed one-dimensional lattice edge has a canonical trace of a \(W^{1,6}\) coefficient in \(L^6(e)\), sufficient to define its path-ordered transport ODE.
- **NOT DEFINED in general:** vertex samples of a \(W^{1,6}\) connection or a \(W^{1,6}\) gauge transformation.
- **OPEN:** generalized strong-resolvent convergence of the trace-link Wilson discretization at \(W^{1,6}\) regularity.
- **NOT CLAIMED:** norm-resolvent convergence, nonsmooth vertex gauge covariance, nontrivial bundles, gauge-field integration, or an interacting Yang–Mills/QCD continuum limit.

The critical case \(p=6\) is therefore neither automatically covered by M1 nor automatically impossible. The continuum operator and individual edge transports have meaningful definitions; the missing theorem is the uniform lattice-skeleton consistency and resolvent argument.
