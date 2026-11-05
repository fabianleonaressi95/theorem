# T019 — Strong-resolvent limit of the free Q6 Wilson refinement

**Status:** PROVED for the free, translation-invariant six-dimensional periodic refinement, in the generalized strong-resolvent sense defined below. Fixed-momentum eigenvalue convergence follows. Norm-resolvent convergence, convergence with nontrivial gauge links, and an interacting continuum limit are **not** claimed.

## 1. Geometry and Hilbert spaces

For \(n\geq 2\), set \(h_n=n^{-1}\), \(L_n=2n\), and
\[
\Lambda_n=(\mathbb Z/L_n\mathbb Z)^6.
\]
The physical torus is
\[
\mathbb T^6_2=(\mathbb R/2\mathbb Z)^6,
\]
of side length \(2\). Its Fourier momenta are \(k\in\pi\mathbb Z^6\). The lattice cells are
\[
C_{n,j}=h_n(j+[0,1)^6),\qquad j\in\Lambda_n.
\]
Use the weighted lattice Hilbert space
\[
\mathcal H_n=\ell^2(\Lambda_n,h_n^6)\otimes\mathbb C^8,
\quad
\|\psi\|_n^2=h_n^6\sum_{j\in\Lambda_n}\|\psi(j)\|^2,
\]
and the continuum space
\[
\mathcal H=L^2(\mathbb T^6_2;\mathbb C^8).
\]

Let \(J_n:\mathcal H_n\to\mathcal H\) be the isometric piecewise-constant embedding:
\[
(J_n\psi)(x)=\psi(j)\quad(x\in C_{n,j}).
\]
Its adjoint \(J_n^*\) takes cell averages. Thus \(J_nJ_n^*\) is the orthogonal projection onto cellwise-constant functions. This fixes the comparison between Hilbert spaces; no informal identification of vectors of different dimensions is used.

## 2. Operators

Choose Hermitian Clifford matrices \(\Gamma_1,\ldots,\Gamma_6\) with
\[
\Gamma_i\Gamma_j+\Gamma_j\Gamma_i=2\delta_{ij}I_8.
\]
Let \(T_i\) be the positive coordinate shift on \(\Lambda_n\). For fixed \(r>0\) and real \(m_0\), define
\[
A_n=m_0I+
\frac1{2h_n}\sum_{i=1}^6\Gamma_i(T_i-T_i^{-1})
+\frac r{2h_n}\sum_{i=1}^6(2I-T_i-T_i^{-1}).
\]
The last term is the free Wilson Laplacian. The continuum operator is
\[
A=m_0I+\sum_{i=1}^6\Gamma_i\partial_i,
\qquad \mathcal D(A)=H^1(\mathbb T^6_2;\mathbb C^8).
\]
With the stated Fourier convention, \(A\) has symbol \(m_0I+i\Gamma\cdot k\).

For \(k\in\pi\mathbb Z^6\) in the lattice Brillouin zone, the lattice Fourier symbol is
\[
A_n(k)=m_0I+
\frac i{h_n}\sum_i\Gamma_i\sin(h_nk_i)
+\frac r{h_n}\sum_i(1-\cos(h_nk_i))I.
\]
The allowed representatives can be chosen with \(-n\leq k_i/\pi<n\).

## 3. Coercive resolvent bound

The centered kinetic term is anti-Hermitian. The Wilson term is self-adjoint and nonnegative, since
\[
\left\langle\psi,
\frac r{2h_n}\sum_i(2I-T_i-T_i^{-1})\psi
\right\rangle_n
=\frac r{2h_n}\sum_i\|(I-T_i)\psi\|_n^2\geq0.
\]
Consequently
\[
\operatorname{Re}\langle\psi,A_n\psi\rangle_n
\geq m_0\|\psi\|_n^2.
\]
The same inequality holds for \(A\), because each \(\partial_i\) is skew-adjoint on the periodic torus and each \(\Gamma_i\) is Hermitian. Therefore, for every \(z\in\mathbb C\) with \(\operatorname{Re}z<m_0\),
\[
\|(A_n-z)^{-1}\|\leq\frac1{m_0-\operatorname{Re}z},
\qquad
\|(A-z)^{-1}\|\leq\frac1{m_0-\operatorname{Re}z}.
\]
In particular, all resolvents in the statement below exist on this common left half-plane.

## 4. Fixed Fourier-mode consistency

Fix \(k\in\pi\mathbb Z^6\). For all sufficiently large \(n\), this is an allowed lattice momentum. Its lattice symbol satisfies
\[
A_n(k)\longrightarrow A(k)=m_0I+i\Gamma\cdot k.
\]
Indeed,
\[
\left\|\frac i{h_n}\sum_i\Gamma_i\sin(h_nk_i)
-i\Gamma\cdot k\right\|
\leq\frac{h_n^2}{6}\sum_i|k_i|^3,
\]
and
\[
0\leq\frac r{h_n}\sum_i(1-\cos(h_nk_i))
\leq\frac{rh_n}{2}|k|^2.
\]
The first error is \(O(h_n^2|k|^3)\); the Wilson contribution is \(O(rh_n|k|^2)\). Hence the full matrix symbol converges in operator norm for each fixed \(k\).

For the normalized Fourier character \(e_k(x)=2^{-3}e^{ik\cdot x}\), \(J_n^*e_k\) is a scalar multiple of the corresponding lattice character; its scalar cell-average factor tends to \(1\). The piecewise-constant reconstruction of that character converges to \(e_k\) in \(L^2\). Thus, for every spin vector \(v\in\mathbb C^8\),
\[
J_n(A_n-z)^{-1}J_n^*(e_kv)
\longrightarrow
(A-z)^{-1}(e_kv)
\quad\text{in }\mathcal H.
\]

## 5. Theorem — generalized strong-resolvent convergence

For every \(z\) with \(\operatorname{Re}z<m_0\) and every \(f\in\mathcal H\),
\[
\boxed{
J_n(A_n-z)^{-1}J_n^*f
\longrightarrow
(A-z)^{-1}f
\quad\text{strongly in }\mathcal H.
}
\]

**Proof.** First take \(f\) to be a finite Fourier sum. The result follows term by term from the fixed-mode consistency in Section 4; for sufficiently large \(n\), its finitely many momenta are all represented without aliasing. Finite Fourier sums are dense in \(\mathcal H\).

For general \(f\), choose a finite Fourier sum \(g\) with \(\|f-g\|<\varepsilon\). Since \(J_n\) is an isometry, \(\|J_n^*\|\leq1\). The coercive estimates in Section 3 give
\[
\begin{aligned}
&\|J_n(A_n-z)^{-1}J_n^*(f-g)\|\\
&\qquad+\|(A-z)^{-1}(f-g)\|
\leq \frac{2\varepsilon}{m_0-\operatorname{Re}z}.
\end{aligned}
\]
For this fixed \(g\), the difference of the two resolvent expressions tends to zero. Taking the upper limit in \(n\), then letting \(\varepsilon\downarrow0\), proves the claim. \(\square\)

This is a generalized strong-resolvent statement because the finite-dimensional spaces vary with \(n\); the maps \(J_n,J_n^*\) are part of the theorem. It is not a norm-resolvent assertion.

## 6. Fixed-mode spectral consequence

For each fixed \(k\in\pi\mathbb Z^6\), the eigenvalues of the spin block are
\[
m_0+W_n(k)\ \pm\
i\left(\sum_i\frac{\sin^2(h_nk_i)}{h_n^2}\right)^{1/2},
\]
with multiplicity four for each sign when the square-root term is nonzero, where
\[
W_n(k)=\frac r{h_n}\sum_i(1-\cos(h_nk_i)).
\]
They converge, with multiplicity, to
\[
m_0\pm i|k|,
\]
the corresponding eigenvalues of the continuum Fourier block. At \(k=0\), all eight eigenvalues equal \(m_0\) for every \(n\). This is a fixed-mode statement; it is not by itself a theorem about the entire spectrum in moving energy windows.

## 7. What this theorem does not establish

**PROVED**
- Generalized strong-resolvent convergence of the free six-dimensional Wilson refinement to the flat-torus Euclidean Dirac operator, on the common half-plane \(\operatorname{Re}z<m_0\).
- Fixed-Fourier-mode matrix and eigenvalue convergence.
- A uniform resolvent bound on that half-plane.

**NOT PROVED / OPEN**
- Norm-resolvent convergence or a uniform estimate over all lattice momenta.
- Convergence of spectral projectors for arbitrary moving windows, or a complete eigenvector convergence theorem.
- Strong-resolvent convergence for nontrivial \(SU(3)\) link fields. This needs a specified sequence of link fields approximating a continuum connection and uniform estimates.
- Gauge-field integration, reflection positivity, fermion determinant control, interacting continuum QCD, confinement, or baryon masses.
- Any derivation of a physical \(3+1\)-dimensional theory from the six-dimensional refinement or from the finite graph \(Q_6\).
- Any evasion of Nielsen–Ninomiya. The Wilson term lifts the unwanted corners by breaking the naive chiral anticommutation.

## 8. Relation to T017 and the gauge-covariant Wilson construction

T017 establishes the lattice family, the 64 naive corners, the Wilson corner lift, and fixed-mode symbol convergence. The gauge-covariant construction merged in PR #15 establishes exact finite-lattice gauge covariance and positivity identities for unitary links. T019 adds a continuum theorem only for the **free** translation-invariant family. It does not automatically extend to the link-coupled operator: pointwise gauge covariance is not a substitute for convergence of the link fields.

The physical torus has side length \(2\), not \(2\pi\), because \(h_n=1/n\) and there are \(2n\) sites in each direction. Its momentum lattice is therefore \(\pi\mathbb Z^6\).
