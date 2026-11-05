# M1 — Hölder gauge fields and the Q6 Wilson strong-resolvent limit

**Status:** PROVED under the hypotheses stated below, subject to the explicit sampling/parallel-transport convention. The result extends the smooth-background theorem T020 to periodic Hölder-continuous SU(3) connections. In fact, the qualitative strong-resolvent argument only needs continuity of the connection; Hölder regularity supplies the quantitative consistency rate. No gauge-field integration or interacting Yang–Mills/QCD limit is claimed.

## 1. Geometry and Hilbert spaces

Let
\[
\mathbb T^6_2=(\mathbb R/2\mathbb Z)^6,\qquad
h_n=n^{-1},\qquad
\Lambda_n=(\mathbb Z/(2n)\mathbb Z)^6.
\]
The lattice sites are \(x_j=h_nj\), with periodic coordinates. Let
\[
\mathcal H=L^2(\mathbb T^6_2;\mathbb C^8\otimes\mathbb C^3),\qquad
\mathcal H_n=\ell^2(\Lambda_n,h_n^6)\otimes\mathbb C^8\otimes\mathbb C^3.
\]
The map \(J_n:\mathcal H_n\to\mathcal H\) is the isometric piecewise-constant embedding on the half-open cells
\[
C_{n,j}=h_n(j+[0,1)^6),
\]
and \(J_n^*\) is its cell-average adjoint. For a continuous section \(\Psi\), write \(I_n\Psi(j)=\Psi(x_j)\). Then
\[
J_nI_n\Psi\longrightarrow\Psi\quad\text{in }L^2.
\]
For every continuous \(g\), also
\[
\|I_ng-J_n^*g\|_n\longrightarrow0.
\]
Both statements follow from uniform continuity on the compact torus.

Choose constant Hermitian matrices \(\Gamma_1,\ldots,\Gamma_6\in M_8(\mathbb C)\) satisfying
\[
\Gamma_i\Gamma_j+\Gamma_j\Gamma_i=2\delta_{ij}I_8.
\]

## 2. Continuum connection and operator

Fix \(0<\alpha\leq1\) and a periodic connection
\[
\mathcal A_i\in C^{0,\alpha}(\mathbb T^6_2;\mathfrak{su}(3)),
\qquad i=1,\ldots,6.
\]
The convention is
\[
\nabla_i=\partial_i+\mathcal A_i,\qquad
A_{\mathcal A}=m_0I+\sum_{i=1}^6\Gamma_i\otimes\nabla_i,
\qquad
\mathcal D(A_{\mathcal A})=H^1(\mathbb T^6_2;\mathbb C^8\otimes\mathbb C^3),
\]
where \(m_0\in\mathbb R\). Since \(\mathcal A_i\) is bounded and anti-Hermitian, \(A_{\mathcal A}-m_0\) is a bounded skew-adjoint perturbation of the free Euclidean Dirac operator \(\sum_i\Gamma_i\partial_i\). It is therefore skew-adjoint on \(H^1\), and
\[
\operatorname{Re}\langle\Psi,A_{\mathcal A}\Psi\rangle
=m_0\|\Psi\|^2.
\]
In particular, for \(\operatorname{Re}z<m_0\),
\[
\|(A_{\mathcal A}-z)^{-1}\|
\leq (m_0-\operatorname{Re}z)^{-1}.
\]
The smooth periodic sections are a graph core: the free Dirac operator has core \(C^\infty\), and a bounded perturbation preserves this core.

## 3. Exact links from the continuous connection

For each positively oriented edge from \(x\) to \(x+h_ne_i\), define \(U_{n,i}(x)\in SU(3)\) as the parallel transporter solving
\[
\frac{d}{dt}U(t)=U(t)\mathcal A_i(x+te_i),\qquad U(0)=I_3,
\qquad U_{n,i}(x)=U(h_n).
\]
This right-ordered convention is chosen so that
\[
U_{n,i}^{\,g}(x)=g(x)U_{n,i}(x)g(x+h_ne_i)^\dagger
\]
when
\[
\Psi^g=g\Psi,\qquad
\mathcal A_i^g=g\mathcal A_i g^\dagger-(\partial_i g)g^\dagger
\]
for smooth gauge transformations \(g\). Since \(\mathcal A_i\) is anti-Hermitian, every link is unitary and has determinant one.

Define the unitary covariant shift
\[
(S_{n,i}\psi)(x)=U_{n,i}(x)\psi(x+h_ne_i),\qquad
(S_{n,i}^\dagger\psi)(x)=U_{n,i}(x-h_ne_i)^\dagger\psi(x-h_ne_i).
\]
For fixed \(r>0\), set
\[
A_{n,\mathcal A}=m_0I+
\frac1{2h_n}\sum_{i=1}^6\Gamma_i(S_{n,i}-S_{n,i}^\dagger)
+\frac r{2h_n}\sum_{i=1}^6(2I-S_{n,i}-S_{n,i}^\dagger).
\]
The spin matrices commute with the shifts, which act only on lattice and color indices.

## 4. Hölder transport estimate and consistency

Let \([\,\mathcal A_i\,]_{C^{0,\alpha}}\) denote the Hölder seminorm. The integral equation for the parallel transporter and boundedness of \(\mathcal A_i\) imply, uniformly in lattice sites,
\[
U_{n,i}(x)=I+h_n\mathcal A_i(x)+R_{n,i}(x),
\qquad
\|R_{n,i}(x)\|\leq C_{\mathcal A}h_n^{1+\alpha}.
\]
Here and below constants may depend on \(\|\mathcal A\|_{C^{0,\alpha}}\), the dimension, and fixed test sections, but not on \(n\). To see the order, write
\[
U(h)-I-\!h\mathcal A_i(x)
=\int_0^h\big(U(t)\mathcal A_i(x+te_i)-\mathcal A_i(x)\big)\,dt.
\]
The integrand is bounded by \(C(t^\alpha+t)\); integration gives \(O(h^{1+\alpha})\) for \(0<\alpha\leq1\). The same estimate holds for the reversed link.

For every fixed \(\Psi\in C^\infty\), Taylor expansion of \(\Psi\), together with the link estimate, gives
\[
S_{n,i}I_n\Psi
=I_n\Psi+h_nI_n(\nabla_i\Psi)+O_\Psi(h_n^{1+\alpha}),
\]
\[
S_{n,i}^\dagger I_n\Psi
=I_n\Psi-h_nI_n(\nabla_i\Psi)+O_\Psi(h_n^{1+\alpha}),
\]
in the lattice norm, uniformly in sites. Consequently,
\[
\left\|
\frac{S_{n,i}-S_{n,i}^\dagger}{2h_n}I_n\Psi
-I_n(\nabla_i\Psi)
\right\|_n
\leq C_\Psi h_n^\alpha,
\]
and
\[
\left\|
\frac{2I-S_{n,i}-S_{n,i}^\dagger}{2h_n}I_n\Psi
\right\|_n
\leq C_\Psi h_n^\alpha.
\]
Thus the Wilson contribution vanishes on fixed smooth sections at rate \(O(h_n^\alpha)\), and
\[
\boxed{\;
\|A_{n,\mathcal A}I_n\Psi-I_n(A_{\mathcal A}\Psi)\|_n
\leq C_\Psi h_n^\alpha.
\;}
\tag{M1.1}
\]
The estimate includes the Wilson term for fixed \(r\); its constant is allowed to depend linearly on \(r\).

**Important regularity point.** The proof does not require differentiating \(\mathcal A_i\). The parallel transporter is defined by an ODE with continuous coefficients, and the only regularity input in (M1.1) is the modulus of continuity of \(\mathcal A_i\). In particular, the same argument works for \(\mathcal A_i\in C^0\), with \(h_n^\alpha\) replaced by a quantity bounded by
\[
C_\Psi\big(\omega_{\mathcal A}(h_n)+h_n\big)\longrightarrow0,
\]
where \(\omega_{\mathcal A}\) is a common modulus of continuity. Hölder regularity gives the explicit algebraic rate.

## 5. Uniform accretivity

The centered kinetic term is anti-Hermitian. Since every \(S_{n,i}\) is unitary,
\[
\left\langle\psi,
\frac r{2h_n}(2I-S_{n,i}-S_{n,i}^\dagger)\psi
\right\rangle_n
=\frac r{2h_n}\|(I-S_{n,i})\psi\|_n^2\geq0.
\]
Therefore
\[
\operatorname{Re}\langle\psi,A_{n,\mathcal A}\psi\rangle_n
\geq m_0\|\psi\|_n^2,
\]
and for every \(\operatorname{Re}z<m_0\),
\[
\|(A_{n,\mathcal A}-z)^{-1}\|
\leq(m_0-\operatorname{Re}z)^{-1}.
\tag{M1.2}
\]
The bound is independent of \(n\). This is the key stability estimate; no derivative of the gauge field enters it.

## 6. Lemma M1 — generalized strong-resolvent convergence

**Theorem.** Under Sections 1–3, for every \(z\in\mathbb C\) with \(\operatorname{Re}z<m_0\) and every \(f\in\mathcal H\),
\[
\boxed{
J_n(A_{n,\mathcal A}-z)^{-1}J_n^*f
\longrightarrow
(A_{\mathcal A}-z)^{-1}f
\quad\text{strongly in }\mathcal H.
}
\tag{M1.3}
\]
This is generalized strong-resolvent convergence for varying Hilbert spaces, with comparison maps \(J_n,J_n^*\) explicitly specified. It is not norm-resolvent convergence.

**Proof.** Let \(\Psi\in C^\infty\) and set \(f=(A_{\mathcal A}-z)\Psi\). Since \(\mathcal A_i\) and \(\Psi\) are continuous, \(f\) is continuous. By (M1.1),
\[
\|(A_{n,\mathcal A}-z)I_n\Psi-I_nf\|_n\longrightarrow0.
\]
Uniform continuity gives
\[
\|I_nf-J_n^*f\|_n\longrightarrow0,
\qquad
J_nI_n\Psi\longrightarrow\Psi.
\]
Using (M1.2),
\[
\begin{aligned}
&\|J_n(A_{n,\mathcal A}-z)^{-1}J_n^*f-J_nI_n\Psi\|\\
&\quad\leq
\frac{\|J_n^*f-(A_{n,\mathcal A}-z)I_n\Psi\|_n}
{m_0-\operatorname{Re}z}
\longrightarrow0.
\end{aligned}
\]
Hence (M1.3) holds for every \(f\) in the set
\[
\{(A_{\mathcal A}-z)\Psi:\Psi\in C^\infty\}.
\]
This set is dense in \(\mathcal H\), because \(C^\infty\) is a graph core and \(A_{\mathcal A}-z\) is onto. Finally, both the lattice and continuum resolvents satisfy the same uniform bound, while \(\|J_n^*\|\leq1\). Approximation by this dense set extends convergence to every \(f\in\mathcal H\). \(\square\)

## 7. Gauge covariance

For a smooth periodic gauge transformation \(g:\mathbb T^6_2\to SU(3)\), let \(G_n\) be multiplication by \(g(x_j)\) on lattice fields and \(G\) multiplication by \(g(x)\) in the continuum. The link transformation law in Section 3 gives the exact finite-lattice identity
\[
A_{n,\mathcal A^g}G_n=G_nA_{n,\mathcal A}.
\]
The continuum operators satisfy
\[
A_{\mathcal A^g}G=GA_{\mathcal A}.
\]
This is exact covariance for smooth gauge transformations. The theorem does not assert covariance under arbitrary nonsmooth gauge transformations unless the transformed connection and multiplication operators are defined in a compatible regularity class.

## 8. What is and is not established

**PROVED under the stated assumptions**
1. Exact unitarity of parallel-transport links for continuous \(\mathfrak{su}(3)\)-valued connections.
2. Uniform accretivity and a uniform resolvent bound for the finite-lattice Wilson operator.
3. Hölder consistency estimate (M1.1) on smooth sections, with rate \(O(h_n^\alpha)\).
4. Generalized strong-resolvent convergence (M1.3) for a fixed periodic \(C^{0,\alpha}\) connection on the trivial bundle.
5. The qualitative proof extends to continuous connections, with the Hölder rate replaced by the modulus-of-continuity rate.

**NOT CLAIMED / OPEN**
- Norm-resolvent convergence or uniform convergence over all lattice momenta.
- Uniformity over bounded subsets of \(C^{0,\alpha}\) without tracking the Hölder norms.
- Nontrivial principal bundles, nontrivial topological sectors, or patchwise link constructions.
- Distributional connections, rough gauge potentials below continuity, or stochastic gauge fields.
- Integration over gauge fields, Yang–Mills measure, fermion determinants, reflection positivity, renormalization, asymptotic freedom, confinement, or baryon masses.
- A physical \(3+1\)-dimensional reduction or an evasion of Nielsen–Ninomiya.

## 9. Relation to T016–T020

- T016 remains the no-go audit: the finite Q6 graph does not evade Nielsen–Ninomiya.
- T017 defines the six-dimensional periodic refinement and the free Wilson symbol.
- T019 proves the free generalized strong-resolvent limit.
- T020 treats a fixed smooth periodic \(\mathfrak{su}(3)\) connection.
- M1 lowers the regularity of that prescribed classical connection to \(C^{0,\alpha}\), preserving a quantitative consistency rate.

The refinement is six-dimensional throughout. Nothing here derives a \(3+1\)-dimensional physical theory or an interacting continuum QCD model.

## 10. Verification checklist for review

- [ ] Independently check the left/right convention in the parallel-transport ODE against the stated gauge transformation law.
- [ ] Check the \(O(h^{1+\alpha})\) transport remainder for both forward and reverse links.
- [ ] Check the Wilson cancellation and its \(O(h^\alpha)\) rate without differentiating the connection.
- [ ] Check the graph-core and dense-range step for the non-self-adjoint accretive operator.
- [ ] Check that the comparison maps \(J_n,J_n^*\) are used consistently.
- [ ] Attempt counterexamples for merely continuous coefficients and identify the exact point where continuity is needed.
- [ ] Keep norm-resolvent convergence and uniformity over connection families explicitly outside the theorem.
