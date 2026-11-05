# T020 — Strong-resolvent limit with a fixed smooth SU(3) connection

**Status:** PROVED under the explicit regularity and trivial-bundle assumptions below. This extends T019 from zero gauge field to a prescribed smooth continuum connection sampled by parallel-transport links. It does **not** integrate over gauge fields or establish an interacting Yang–Mills/QCD continuum limit.

## 1. Continuum data

Work on \(\mathbb T^6_2=(\mathbb R/2\mathbb Z)^6\), with spin space \(\mathbb C^8\) and color space \(\mathbb C^3\). Let
\[
\mathcal A_i\in C^\infty(\mathbb T^6_2;\mathfrak{su}(3)),\quad i=1,\ldots,6,
\qquad \nabla_i=\partial_i+\mathcal A_i.
\]
The connection is globally defined and periodic, hence is on the trivial bundle. Define
\[
A_{\mathcal A}=m_0I+\sum_{i=1}^6\Gamma_i\nabla_i,\qquad
\mathcal D(A_{\mathcal A})=H^1(\mathbb T^6_2;\mathbb C^8\otimes\mathbb C^3),
\]
where the Hermitian \(\Gamma_i\) satisfy the six-dimensional Euclidean Clifford relations and act trivially on color. Since \(\mathcal A_i^\dagger=-\mathcal A_i\), the covariant derivatives are skew-adjoint on periodic sections. The elliptic Dirac-type operator has its standard closed skew-adjoint realization after subtracting \(m_0I\), and
\[
\operatorname{Re}\langle\Psi,A_{\mathcal A}\Psi\rangle\geq m_0\|\Psi\|^2.
\]

## 2. Links and lattice operator

Let \(h_n=1/n\), \(\Lambda_n=(\mathbb Z/(2n)\mathbb Z)^6\), and \(x_j=h_nj\). Let \(U_{n,i}(x_j)\in SU(3)\) be the backward parallel transporter from \(x_j+h_ne_i\) to \(x_j\) for \(\nabla_i=\partial_i+\mathcal A_i\). Fix its path-ordering convention by
\[
U_{n,i}^{\,g}(x_j)=g(x_j)U_{n,i}(x_j)g(x_j+h_ne_i)^\dagger
\]
under
\[
\Psi^g=g\Psi,\qquad
\mathcal A_i^g=g\mathcal A_i g^\dagger-(\partial_i g)g^\dagger.
\]
With this convention,
\[
U_{n,i}(x_j)=I+h_n\mathcal A_i(x_j)+O(h_n^2),
\quad
U_{n,i}(x_j)\Psi(x_j+h_ne_i)
=\Psi(x_j)+h_n\nabla_i\Psi(x_j)+O(h_n^2).
\]

Define
\[
(S_{n,i}\psi)(x_j)=U_{n,i}(x_j)\psi(x_j+h_ne_i),\qquad
(S_{n,i}^\dagger\psi)(x_j)=U_{n,i}(x_j-h_ne_i)^\dagger\psi(x_j-h_ne_i).
\]
These are unitary on \(\mathcal H_n=\ell^2(\Lambda_n,h_n^6)\otimes\mathbb C^8\otimes\mathbb C^3\). For \(r>0\) and real \(m_0\), set
\[
A_{n,\mathcal A}=m_0I+
\frac1{2h_n}\sum_{i=1}^6\Gamma_i(S_{n,i}-S_{n,i}^\dagger)
+\frac r{2h_n}\sum_{i=1}^6(2I-S_{n,i}-S_{n,i}^\dagger).
\]
This is the link-covariant Wilson operator with the normalization fixed in the PR #15 construction.

## 3. Uniform resolvent estimate

Unitarity gives
\[
\left\langle\psi,
\frac r{2h_n}\sum_i(2I-S_{n,i}-S_{n,i}^\dagger)\psi
\right\rangle_n
=\frac r{2h_n}\sum_i\|(I-S_{n,i})\psi\|_n^2\geq0.
\]
The centered kinetic term is anti-Hermitian. Hence
\[
\operatorname{Re}\langle\psi,A_{n,\mathcal A}\psi\rangle_n
\geq m_0\|\psi\|_n^2,
\qquad
\|(A_{n,\mathcal A}-z)^{-1}\|
\leq\frac1{m_0-\operatorname{Re}z}
\]
for \(\operatorname{Re}z<m_0\). The continuum operator has the same bound. The estimate is independent of \(n\).

## 4. Consistency on smooth sections

Let \(I_n\Psi(x_j)=\Psi(x_j)\) be point sampling and let \(J_n\) be the isometric piecewise-constant embedding into
\(\mathcal H=L^2(\mathbb T^6_2;\mathbb C^8\otimes\mathbb C^3)\). Covariant Taylor expansion along a coordinate line gives, uniformly in lattice sites,
\[
S_{n,i}I_n\Psi
=I_n\Psi+h_nI_n(\nabla_i\Psi)
+\frac{h_n^2}{2}I_n(\nabla_i^2\Psi)+O_\Psi(h_n^3),
\]
\[
S_{n,i}^\dagger I_n\Psi
=I_n\Psi-h_nI_n(\nabla_i\Psi)
+\frac{h_n^2}{2}I_n(\nabla_i^2\Psi)+O_\Psi(h_n^3).
\]
It follows that
\[
\frac{S_{n,i}-S_{n,i}^\dagger}{2h_n}I_n\Psi
=I_n(\nabla_i\Psi)+O_\Psi(h_n^2),
\]
and
\[
\frac r{2h_n}(2I-S_{n,i}-S_{n,i}^\dagger)I_n\Psi
=-\frac{rh_n}{2}I_n(\nabla_i^2\Psi)+O_\Psi(rh_n^2).
\]
Thus the Wilson contribution is \(O_\Psi(rh_n)\), while the centered covariant difference has \(O_\Psi(h_n^2)\) consistency error. In particular,
\[
J_nI_n\Psi\to\Psi,\qquad
J_nA_{n,\mathcal A}I_n\Psi\to A_{\mathcal A}\Psi
\quad\text{in }L^2.
\]
Equivalently,
\[
\|A_{n,\mathcal A}I_n\Psi-I_n(A_{\mathcal A}\Psi)\|_n=O_\Psi(h_n).
\]

## 5. Theorem — generalized strong-resolvent convergence

For every \(z\) with \(\operatorname{Re}z<m_0\) and every \(f\in\mathcal H\),
\[
\boxed{
J_n(A_{n,\mathcal A}-z)^{-1}J_n^*f
\longrightarrow
(A_{\mathcal A}-z)^{-1}f
\quad\text{strongly in }\mathcal H.
}
\]

**Proof.** First take \(f=(A_{\mathcal A}-z)\Psi\) with \(\Psi\in C^\infty\). Consistency and \(J_nJ_n^*f\to f\) imply
\[
\|(A_{n,\mathcal A}-z)I_n\Psi-J_n^*f\|_n\to0.
\]
The uniform resolvent estimate yields
\[
\|J_n(A_{n,\mathcal A}-z)^{-1}J_n^*f-J_nI_n\Psi\|
\leq
\frac{\|J_n^*f-(A_{n,\mathcal A}-z)I_n\Psi\|_n}
{m_0-\operatorname{Re}z}
\to0.
\]
Since \(J_nI_n\Psi\to\Psi=(A_{\mathcal A}-z)^{-1}f\), convergence holds on this set of right-hand sides. Smooth sections form a graph core for the elliptic operator \(A_{\mathcal A}\), so \((A_{\mathcal A}-z)C^\infty\) is dense in \(\mathcal H\). The uniform resolvent bound and \(\|J_n^*\|\leq1\) extend convergence to every \(f\in\mathcal H\). \(\square\)

This is generalized strong-resolvent convergence between varying Hilbert spaces, with \(J_n,J_n^*\) explicitly specified. It is not norm-resolvent convergence.

## 6. Scope

**PROVED under the stated hypotheses**
- Uniform accretivity of the finite-lattice gauge-covariant Wilson operator.
- Generalized strong-resolvent convergence for links sampled from a fixed smooth periodic \(\mathfrak{su}(3)\) connection on the trivial bundle.
- Vanishing of the Wilson term on smooth fixed sections at rate \(O(h_n)\); centered covariant difference consistency at rate \(O(h_n^2)\).

**OPEN / NOT ESTABLISHED**
- Rough or distributional gauge fields; uniformity over families of connections with weaker regularity.
- Nontrivial principal bundles and topological sectors requiring multiple local trivializations.
- Norm-resolvent convergence, moving-window spectral-projector convergence, or uniform eigenvalue estimates.
- Gauge-field integration, Yang–Mills measure, fermion determinants, reflection positivity, renormalization, asymptotic freedom, confinement, or baryon masses.
- A physical \(3+1\)-dimensional reduction or any evasion of Nielsen–Ninomiya.

## 7. Relation to T019 and PR #15

T019 is the zero-connection case. PR #15 defines the exact finite-lattice link-covariant Wilson operator. T020 supplies the analytic bridge for a prescribed smooth classical connection: consistent parallel-transport links plus a uniform coercive bound imply strong-resolvent convergence. This is still not a quantized interacting gauge theory.
