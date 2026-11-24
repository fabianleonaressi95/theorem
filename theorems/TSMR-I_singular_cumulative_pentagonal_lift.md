# TSMR-I — Singular cumulative coordinates and the pentagonal Fourier projector

**Record type:** exact measure-theoretic construction and finite-dimensional intertwining  
**Status:** proved under the stated hypotheses on the cumulative distribution. This is an isometric embedding of the pentagonal frame into \(L^2(\nu)\), not a conjugacy of the Bernoulli shift or a derivation of a physical interaction.

## 1. The measure and its cumulative coordinate

Let \(\nu\) be an atomless Borel probability measure whose support is a compact interval \(I=[a,b]\). Its distribution function
\[
F_\nu(x)=\nu([a,x])
\]
is continuous and strictly increasing on \(I\). If \(\nu\) is singular with respect to Lebesgue measure, then
\[
F_\nu'(x)=0\quad\text{for Lebesgue-a.e. }x,
\]
while the probability-integral transform gives
\[
(F_\nu)_*\nu=\mathcal L^1|_{[0,1]}.
\]
Thus \(t=F_\nu(x)\) is a uniform coordinate when \(x\) is sampled from \(\nu\), even though \(F_\nu\) is a singular function in the ambient Lebesgue coordinate.

For the equal-weight golden Bernoulli convolution
\[
\nu_g=\operatorname{Law}\!\left(\sum_{n=0}^{\infty}\varepsilon_n\varphi^{-n}\right),
\qquad \mathbb P(\varepsilon_n=\pm1)=\frac12,
\]
the support is the interval \([-1/(1-\varphi^{-1}),1/(1-\varphi^{-1})]\); the measure is atomless and singular. Hence its cumulative function \(F_g\) has the properties above. The singularity statement concerns \(\nu_g\), not a gap in its support.

## 2. The regular pentagon as a real Fourier decomposition

For \(j=0,\ldots,4\), define the five vectors in \(\mathbb R^5\)
\[
\begin{aligned}
u_c(j)&=\sqrt{\frac25}\cos\frac{2\pi j}{5},&
u_s(j)&=\sqrt{\frac25}\sin\frac{2\pi j}{5},\\
u_0(j)&=\frac1{\sqrt5},&
v_c(j)&=\sqrt{\frac25}\cos\frac{4\pi j}{5},&
v_s(j)&=\sqrt{\frac25}\sin\frac{4\pi j}{5}.
\end{aligned}
\]
They form an orthonormal basis. The regular-pentagon frame matrix \(E\in\mathbb R^{2\times5}\), with columns \((\cos(2\pi j/5),\sin(2\pi j/5))^T\), has projector
\[
P=\frac25E^TE=u_cu_c^T+u_su_s^T.
\]
Thus the rank-two active pentagonal plane is exactly the real discrete Fourier mode \(k=\pm1\); its orthogonal rank-three complement consists of modes \(k=0,\pm2\).

On \([0,1]\), introduce the orthonormal real Fourier functions
\[
\begin{aligned}
\phi_c(t)&=\sqrt2\cos(2\pi t),&
\phi_s(t)&=\sqrt2\sin(2\pi t),\\
\phi_0(t)&=1,&
\psi_c(t)&=\sqrt2\cos(4\pi t),&
\psi_s(t)&=\sqrt2\sin(4\pi t).
\end{aligned}
\]

## 3. Cumulative-coordinate lift

Write the orthogonal matrix
\[
U=(u_c\;u_s\;u_0\;v_c\;v_s)\in O(5).
\]
For \(q\in\mathbb R^5\), let
\[
(a_c,a_s,a_0,b_c,b_s)^T=U^Tq.
\]
Define
\[
(J_\nu q)(x)=
a_c\phi_c(F_\nu(x))+a_s\phi_s(F_\nu(x))
+a_0\phi_0(F_\nu(x))
+b_c\psi_c(F_\nu(x))+b_s\psi_s(F_\nu(x)).
\]

**Theorem I1 (cumulative-coordinate pentagonal lift).**  
For every atomless probability \(\nu\) with interval support, \(J_\nu:\mathbb R^5\to L^2(\nu)\) is an isometry:
\[
\langle J_\nu q,J_\nu r\rangle_{L^2(\nu)}
=\langle q,r\rangle_{\mathbb R^5}.
\]
Let \(\Pi_{\nu,1}\) be the orthogonal projection in \(L^2(\nu)\) onto
\[
\operatorname{span}\{\phi_c\circ F_\nu,\phi_s\circ F_\nu\}.
\]
Then the exact intertwining identity holds:
\[
\boxed{J_\nu P=\Pi_{\nu,1}J_\nu.}
\]
In particular,
\[
\|\Pi_{\nu,1}J_\nu q\|_{L^2(\nu)}^2=\|Pq\|_{\mathbb R^5}^2.
\]
For every unit \(q\) balanced by \(\|Pq\|^2=1/2\), the lifted function has equal active and complementary energies \(1/2\), and
\[
q^TE^TEq=\frac54.
\]

**Proof.** Since \((F_\nu)_*\nu\) is Lebesgue measure, the five functions obtained by composing the real Fourier orthonormal system with \(F_\nu\) remain orthonormal in \(L^2(\nu)\). Since \(U\) is orthogonal, \(J_\nu\) preserves inner products. The matrix \(P\) is diagonal in the \(U\)-basis with diagonal \((1,1,0,0,0)\); \(\Pi_{\nu,1}\) keeps exactly the first two Fourier functions. Therefore \(J_\nu P=\Pi_{\nu,1}J_\nu\). Finally \(E^TE=(5/2)P\), giving the \(5/4\) identity at balance. \(\square\)

## 4. What this proves — and what it does not

The construction answers the coordinate question affirmatively: **the singular cumulative function supplies a canonical probability coordinate** \(t=F_g(x)\), and the first real Fourier pair in that coordinate carries exactly the rank-two pentagonal projector. This is stronger than a numerical coincidence: it is an exact isometric intertwining of two orthogonal projections.

The construction is canonical relative to the ordered regular pentagon and the cumulative coordinate \(F_\nu\). It is not a unique map independent of choices of Fourier phase/orientation; rotating the first harmonic pair gives an equivalent projector.

It does **not** prove that:
1. the Bernoulli shift or its IFS Markov operator preserves the first-harmonic subspace;
2. the golden Bernoulli convolution is dynamically conjugate to the pentagonal rotation or to Minkowski's question-mark dynamics;
3. the map derives a De Aquino momentum, a physical scale, or a common action.

To test the genuinely dynamical bridge, define the cumulative-coordinate Markov operator
\[
(\mathscr M_g f)(t)=\frac12 f(\tau_-(t))+\frac12 f(\tau_+(t)),
\qquad
\tau_\pm(t)=F_g\!\left(\lambda_g F_g^{-1}(t)\pm1\right),
\]
where \(\lambda_g=\varphi^{-1}\). The invariant-measure identity makes \(\mathscr M_g\) a Markov operator preserving Lebesgue measure. The remaining, falsifiable question is whether its first-harmonic/complement off-diagonal blocks vanish:
\[
(I-\Pi_1)\mathscr M_g\Pi_1\stackrel{?}=0,\qquad
\Pi_1\mathscr M_g(I-\Pi_1)\stackrel{?}=0.
\]
No vanishing is assumed. These blocks, rather than the scalar \(1/2\) alone, are the next dynamical audit target.

## 5. Relation to Minkowski's question-mark function

Both \(F_g\) and Minkowski's \(?(x)\) are strictly increasing singular distribution coordinates, but they arise from different measures and different symbolic/arithmetic systems. The lift above applies to any atomless interval-supported measure; replacing \(F_g\) by \(?\) gives a corresponding \(L^2\)-isometric pentagonal lift for the probability measure whose distribution function is \(?\). It does not establish that the two lifts intertwine the same dynamics.

## 6. Evidence ledger

- **Proved:** probability-integral transform; orthonormality of the real Fourier pentagon basis; isometry of \(J_\nu\); exact projection intertwining \(J_\nu P=\Pi_{\nu,1}J_\nu\); preservation of the \(1/2\) active-energy balance and \(5/4\) quadratic value.
- **Established input for the golden case:** atomlessness, interval support and singularity of the equal-weight golden Bernoulli convolution.
- **Open:** invariance of the first-harmonic subspace under \(\mathscr M_g\); values of its off-diagonal blocks; any dynamical conjugacy with Minkowski's question-mark system; physical De Aquino coupling/action.

## References

- P. Erdős, “On a family of symmetric Bernoulli convolutions,” *Amer. J. Math.* 61 (1939), 974–976.
- Y. Peres, W. Schlag, and B. Solomyak, “Sixty Years of Bernoulli Convolutions,” survey.
- A. D. B. (Minkowski), classical construction of the question-mark function; see also modern treatments of its singular distribution and Farey dynamics.


## 7. Numerical audit of the dynamical off-diagonal blocks

The Markov operator is not assumed self-adjoint. In the real Fourier basis ordered as
\((\phi_c,\phi_s,\phi_0,\psi_c,\psi_s)\), define its compression matrix by
\[
A_{ij}=\langle e_i,\mathscr M_g e_j\rangle_{L^2([0,1])}.
\]
The two relevant blocks are therefore
\[
C_{\mathrm{out}}=(I-\Pi_1)\mathscr M_g\Pi_1=A_{2:5,\,0:2},
\qquad
C_{\mathrm{in}}=\Pi_1\mathscr M_g(I-\Pi_1)=A_{0:2,\,2:5}.
\]
A deterministic-seed Monte Carlo audit, using 300,000 Bernoulli samples and 48 terms of the golden series to approximate the CDF, gives
\[
\|C_{\mathrm{in}}\|_F\approx1.26450,\qquad
\|C_{\mathrm{out}}\|_F\approx0.13370.
\]
The omitted series tail is bounded by \(2.44\cdot10^{-10}\); the dominant uncertainty is empirical-CDF / sampling error, not series truncation. The two blocks are visibly different, as expected for a non-self-adjoint Markov operator.

**Numerical conclusion:** the first-harmonic plane is not invariant under the tested golden cumulative-coordinate Markov operator: \(C_{\mathrm{out}}\ne0\) at a scale far above the finite-sample fluctuations. The reverse coupling \(C_{\mathrm{in}}\) is also nonzero. Thus the exact isometry \(J_gP=\Pi_1J_g\) from Theorem I1 does not extend to an intertwining of the Markov dynamics.

This is a numerical falsification of the proposed invariant-plane property, not yet an exact analytic non-vanishing theorem. The stored matrix and reproducible audit are in \`results/tsmr_i_golden_markov_blocks.json\`; implementation and regression tests are in \`audits/tsmr_i_markov_blocks.py\` and \`tests/test_tsmr_i_markov_blocks.py\`.


## 8. Feshbach/Mori reduction: finite harmonic memory model

The constant function is an exact fixed vector of the Markov operator:
\(\mathscr M_g1=1\). It must therefore be separated from the dynamical
complement. On the stored five-mode compression, retain the active pair
\((\phi_c,\phi_s)\), isolate the constant, and retain the second-harmonic
pair \((\psi_c,\psi_s)\) as a resolved memory sector. The resulting
\(2+2\) matrix has block form
\[
A^{(4)}=\begin{pmatrix}A_{11}&B\\C&D\end{pmatrix}.
\]
The finite-dimensional eigenvalue-dependent effective operator is the
Schur/Feshbach complement
\[
\boxed{A_{\rm eff}(z)=A_{11}+B(zI-D)^{-1}C.}
\]
The second term is the frequency-dependent self-energy. Equivalently, in
the discrete-time projected evolution the finite-compression memory
kernels are
\[
\boxed{K_n=BD^nC,\qquad n\geq0.}
\]

For the stored numerical matrix:
\[
D\simeq\begin{pmatrix}
-0.153066&0.000278\\
0.000542&-0.214570
\end{pmatrix},
\quad \rho(D)\simeq0.214572.
\]
The first memory kernels have Frobenius norms
\[
\|K_0\|_F\simeq0.115237,\quad
\|K_1\|_F\simeq0.023780,\quad
\|K_2\|_F\simeq0.004996,\quad
\|K_3\|_F\simeq0.001060.
\]
At \(z=1\), the self-energy is approximately
\[
\Sigma(1)=B(I-D)^{-1}C\simeq
\begin{pmatrix}
0.039070&-0.000228\\
0.000154&0.087327
\end{pmatrix},
\]
so
\[
A_{\rm eff}(1)\simeq
\begin{pmatrix}
0.056844&-0.000242\\
-0.000266&0.183717
\end{pmatrix}.
\]

**Interpretation.** In this four-mode Galerkin compression the second-harmonic
sector is strongly contracting and produces a nonzero, rapidly decaying
memory correction to the retained pentagonal pair. Thus a memory-bearing
effective dynamics is more appropriate than a closed two-mode Markov law.

**Scope limitation.** These numbers are computed from the \(5\times5\)
compressed matrix already estimated by the empirical-CDF procedure. The
full orthogonal complement of the first-harmonic plane in \(L^2([0,1])\)
contains every higher Fourier mode, not only the constant and second
harmonics. Consequently \(A_{\rm eff}(z)\) and \(K_n\) above are a
reproducible finite Galerkin/Feshbach model, not the exact
infinite-dimensional Mori–Zwanzig kernel. Establishing convergence as
additional harmonics are included is the next open task.

## 9. Increasing-harmonic Galerkin convergence audit (protocol)

For cutoff H>=2 use the ordered basis
\[
\mathcal B_H=(\phi_c,\phi_s,1,\psi_{2,c},\psi_{2,s},\ldots,\psi_{H,c},\psi_{H,s}),
\]
where \(\psi_{k,c}(t)=\sqrt2\cos(2\pi kt)\) and
\(\psi_{k,s}(t)=\sqrt2\sin(2\pi kt)\). The constant index 2 is
excluded exactly from the memory complement. Partition the compression as
\[
A_H=\begin{pmatrix}A_{11}&B_H\\C_H&D_H\end{pmatrix},
\qquad K_{H,n}=B_HD_H^nC_H.
\]
The audit records memory-kernel norms and a power-iteration estimate for
the complement, using H=2,3,4,6,8 by default and one common empirical-CDF
sample for paired cross-cutoff comparisons.

**Reproducibility and status.** Source:
audits/tsmr_i_harmonic_convergence.py. Tests:
tests/test_tsmr_i_harmonic_convergence.py. Run
python -m audits.tsmr_i_harmonic_convergence --samples 30000 --terms 48
to generate results/tsmr_i_harmonic_convergence.json. The power iteration
is an estimate, not a certified spectral-radius bound. Sampling and
empirical-CDF errors remain. No infinite-dimensional convergence,
monotonicity, or stability is asserted until results are generated and
compared across larger sample counts, series lengths, and independent seeds.

## 10. First increasing-harmonic numerical record

A paired finite Galerkin experiment was recorded in results/tsmr_i_harmonic_convergence.json. It uses 30,000 samples, 48 Bernoulli terms, seed 20261124, and cutoffs H=2,3,4,6,8. The constant mode is excluded from each memory complement.

| H | dim(complement) | ||K_{H,0}||_F | numerical rho(D_H) |
|---:|---:|---:|---:|
| 2 | 2 | 0.114829 | 0.213264 |
| 3 | 4 | 0.128908 | 0.142265 |
| 4 | 6 | 0.122870 | 0.360509 |
| 6 | 10 | 0.125164 | 0.321210 |
| 8 | 14 | 0.124016 | 0.378839 |

The first memory-kernel norms decay rapidly for each fixed cutoff, but the cutoff dependence is not monotone. In particular, the complement spectral radius estimates rise for H>=4. This is evidence against claiming a cutoff-uniform contraction from the present experiment. It does not prove instability of the infinite-dimensional operator.

The result is finite-dimensional and empirical: one seed, a truncated Bernoulli series, and an empirical CDF. Independent seeds, larger sample counts, longer series, and certified spectral/norm bounds are still needed. No convergence as H tends to infinity is claimed.


## 11. Exact contraction and empirical high-frequency defect

The cumulative-coordinate Markov operator preserves Lebesgue measure:
\[
\int_0^1 \mathscr M_g h(t)\,dt=\int_0^1h(t)\,dt.
\]
Jensen's inequality gives
\[
|\mathscr M_g f(t)|^2\leq \mathscr M_g(|f|^2)(t),
\qquad
\boxed{\|\mathscr M_g f\|_{L^2}\leq\|f\|_{L^2}.}
\]
For every orthogonal finite-dimensional Galerkin projection, the exact
compression is therefore contractive. A computed singular norm above one
is a discretization/empirical-CDF defect, not a dynamical instability.

The previous H=8 value near 0.996 was already present in the earlier
audit. It is not a new discovery. The higher-cutoff values are numerical
diagnostics only; the result JSON records their separate vectorized
calculation provenance and does not claim a confirmed execution of the
repository script or CI.

## 12. Full Markov mixing versus compressed-complement dynamics

Let \(P_0\) project onto constants, \(\Pi_1\) onto the first real Fourier
pair, and
\[
Q=I-P_0-\Pi_1,\qquad
D=Q\mathscr M_g\!\restriction_{\operatorname{ran}Q}.
\]
The exact Markov contraction proves \(\|D\|_{2\to2}\leq1\), but does not
by itself prove a strict gap.

### Strong convergence of the full Markov operator

Transfer to the original Bernoulli coordinate by the unitary map
\(f(t)\mapsto h(x)=f(F_g(x))\). The operator becomes
\[
(Ph)(x)=\tfrac12h(\lambda x-1)+\tfrac12h(\lambda x+1),
\qquad \lambda=\varphi^{-1}.
\]
Let \(I=[-R,R]\), \(R=(1-\lambda)^{-1}\), and
\[
Y=\sum_{j=0}^{\infty}\varepsilon_j\lambda^j\sim\nu_g.
\]
For \(S_n=\sum_{j=0}^{n-1}\varepsilon_j\lambda^j\), couple the same first
\(n\) signs in \(P^nh(x)\) and in a stationary copy
\(Y=S_n+\lambda^nY'\), where \(Y'\sim\nu_g\) is independent. For every
continuous \(h\) on \(I\),
\[
\sup_{x\in I}|P^nh(x)-\nu_g(h)|
\leq \omega_h(2R\lambda^n),
\]
where \(\omega_h\) is the modulus of continuity. The right-hand side
tends to zero. Since continuous functions are dense in \(L^2(\nu_g)\)
and \(P\) is an \(L^2\)-contraction,
\[
\boxed{P^nh\longrightarrow \nu_g(h)\,1
\quad\text{strongly in }L^2(\nu_g).}
\]
Equivalently, \(\mathscr M_g^nf\to(\int_0^1f)\,1\) strongly in
\(L^2([0,1])\).

This is an exact strong-convergence theorem for the **full** Markov
operator. It is not an operator-norm estimate.

### Why this does not settle the compression

The compressed iterates are
\[
D^n=(Q\mathscr M_gQ)^n\!\restriction_{\operatorname{ran}Q},
\]
which insert \(Q\) after every step. In general
\(D^n\ne Q\mathscr M_g^nQ\). Thus strong convergence of the full
operator does not automatically imply strong stability or a spectral
gap for \(D\).

## 13. Exact norm of the infinite complementary compression

A stronger exact statement is available:
\[
\boxed{\|D\|_{2\to2}=1.}
\]
Thus the infinite complementary compression has **no strict one-step
operator-norm contraction**.

**Proof.** Work in the unitarily equivalent Bernoulli coordinate
\(L^2(\nu_g)\), and let
\[
\mathcal L=\operatorname{span}\{1,\phi_c\circ F_g,\phi_s\circ F_g\},
\qquad Q=I-P_{\mathcal L}.
\]
Let \(\mathcal P_2\) be the subspace of restrictions to \(I\) of
2-periodic functions on the circle \(\mathbb R/2\mathbb Z\). The
pushforward of \(\nu_g\) to this circle is atomless: each point has
finitely many preimages in the compact interval \(I\), and \(\nu_g\)
has no atoms. Hence \(\mathcal P_2\) is infinite-dimensional.

For \(h\in\mathcal P_2\), periodicity gives
\[
Ph(x)=\tfrac12h(\lambda x-1)+\tfrac12h(\lambda x+1)
     =h(\lambda x+1)=h(\lambda x-1).
\]
By invariance of \(\nu_g\),
\[
\begin{aligned}
\|Ph\|_{L^2(\nu_g)}^2
&=\int |h(\lambda x+1)|^2\,d\nu_g(x)\\
&=\frac12\int\bigl(|h(\lambda x-1)|^2+
                         |h(\lambda x+1)|^2\bigr)\,d\nu_g(x)\\
&=\int P(|h|^2)(x)\,d\nu_g(x)
 =\|h\|_{L^2(\nu_g)}^2.
\end{aligned}
\]
So \(P\) acts isometrically on the infinite-dimensional subspace
\(\mathcal P_2\).

The conditions \(h\perp\mathcal L\) and \(Ph\perp\mathcal L\) impose
only six linear constraints on \(\mathcal P_2\), because
\(\dim\mathcal L=3\). Their common kernel therefore contains a nonzero
\(h\). For this \(h\), \(Qh=h\), \(QPh=Ph\), and
\[
Dh=QPQh=QPh=Ph,\qquad \|Dh\|_2=\|h\|_2.
\]
Hence \(\|D\|\geq1\). The reverse inequality follows from the Markov
contraction and orthogonal projection, proving \(\|D\|=1\). \(\square\)

### Consequence for exact Galerkin sections

Let \(Q_H\) project onto complement harmonics \(2\leq k\leq H\), and
let \(D_H=Q_HD Q_H\). Since \(Q_H\to Q\) strongly,
\[
\boxed{\lim_{H\to\infty}\|D_H\|_{2\to2}
      =\|D\|_{2\to2}=1.}
\]
The upper bound is \(\|D_H\|\leq\|D\|\). For every fixed unit vector
\(h\), \(Q_Hh\to h\) and \(Q_HD Q_Hh\to Dh\), giving the matching
lower limit after taking the supremum over \(h\).

This gives the correct interpretation of the earlier H=8 value near
0.996: exact-measure Galerkin singular norms approach one. The
empirical values slightly above one at larger H remain numerical errors,
because every exact section is contractive.

**Important distinction.** The identity \(\|D\|=1\) rules out a strict
one-step norm gap. It does not determine the spectral radius
\(\rho(D)\), nor whether \(D^nh\to0\) strongly for every \(h\in QL^2\).
Those long-time questions remain open. Finite-section eigenvalue radii
alone do not settle them.


## 14. Orbit-energy criterion for strong stability of the complement

The full Markov operator restricted to the mean-zero space
\[
H_0=\{f:\int f\,d\nu_g=0\}
\]
is a strongly stable contraction, by Section 12. The first-harmonic complement
\[
QH_0=\operatorname{ran}Q,\qquad
D=QP|_{QH_0}
\]
is a finite-codimension compression of that stable contraction.

A relevant sufficient criterion is Kérchy–Müller, *Compressions of stable contractions*,
Integral Equations and Operator Theory **58** (2007), 477–486,
DOI: 10.1007/s00020-007-1500-6. Their Corollary 5 states that if \(T\)
is a stable contraction and \(T_P\) is an orthogonal compression, then
for a given vector \(f\),
\[
\sum_{n=0}^{\infty}
\left(\|T_P^n f\|^2-\|T_P^{n+1}f\|^2\right)^{1/2}<\infty
\quad\Longrightarrow\quad
\|T_P^n f\|\longrightarrow0.
\]
This is a sufficient orbit-by-orbit condition, not an automatic conclusion.

For \(f_n=D^nf\in QH_0\), orthogonality of \(Q\) and invariance of
the mean-zero space give the exact identity
\[
\boxed{
\begin{aligned}
\|f_n\|^2-\|f_{n+1}\|^2
={}&\frac14\int
|f_n(\lambda x-1)-f_n(\lambda x+1)|^2\,d\nu_g(x)\\
&+\|\Pi_1 P f_n\|^2 .
\end{aligned}}
\]
Indeed, the first term is \(\|f_n\|^2-\|Pf_n\|^2\), by the two-branch
variance identity and invariance of \(\nu_g\); the second is the norm
lost when \(P f_n\) is projected away from the first-harmonic plane.
The constant component is zero because \(P\) preserves the mean.

Consequently, a rigorous route to strong stability is to prove, for
each \(f\in QH_0\), summability of the square roots of these two
nonnegative losses along its compressed orbit. It is not enough that
the losses themselves have finite sum: that follows by telescoping
for every contraction and is automatic.

### Defect-index route and its present limitation

There is a second, more restrictive route in the literature. Benhida–Timotin,
*Finite rank perturbations of contractions*, Integral Equations and
Operator Theory **36** (2000), 253–268, DOI: 10.1007/BF01213924,
Lemma 3.3, concerns contractions of Sz.-Nagy–Foiaș class \(C_0\)
(their convention is \(T^{*n}x\to0\)) and a finite defect space
\(\overline{\operatorname{ran}(I-T^*T)^{1/2}}\). It therefore cannot
be applied merely from the strong stability of \(P^n\); the required
adjoint-side stability must also be established.

For the present Bernoulli operator, the defect form on the other side is
\[
\|f\|^2-\|Pf\|^2
=\frac14\int|f(\lambda x-1)-f(\lambda x+1)|^2\,d\nu_g(x).
\]
The difference map has infinite-dimensional range: testing exponential
functions \(f_\xi(y)=e^{i\xi y}\) with distinct \(\xi\) for which
\(\sin\xi\ne0\) produces distinct exponential functions proportional
to \(e^{i\xi\lambda x}\). These functions are linearly independent on
the interval support. Thus this finite-\(d_P\) hypothesis is unavailable.
The complementary finite-codimension criterion quoted by Kérchy–Müller
instead asks for finite \(d_{P^*}\), namely finite-dimensional
\(\overline{\operatorname{ran}(I-PP^*)^{1/2}}\); that defect index has
not been computed here. Neither criterion is claimed to apply yet.

**Status.** The orbit-energy identity is exact. Kérchy–Müller supplies
a valid sufficient criterion. Whether its square-root summability holds
for every vector in this particular golden-Bernoulli compression
remains open; so do strong stability and the spectral radius of \(D\).


## 15. The compressed complement has no unitary part

The strong convergence of the full Markov operator on \(H_0\) yields
another exact conclusion for its compression \(D=QP|_{QH_0}\).

Suppose \(f\in QH_0\) satisfies
\[
\|D^n f\|=\|f\|\qquad\text{for every }n\geq0.
\]
Since \(D=QP\), with \(P\) and \(Q\) contractions,
\[
\|f\|=\|D f\|=\|QP f\|\leq\|P f\|\leq\|f\|.
\]
Equality throughout implies \(Pf=QPf=Df\). Applying the same
argument to \(Df\), and then inductively, gives
\[
D^n f=P^n f\qquad(n\geq0).
\]
But \(f\in H_0\) and Section 12 proves \(P^n f\to0\) strongly.
Consequently \(\|f\|=0\).

Thus the maximal unitary part of the contraction \(D\) is trivial:
\[
\boxed{D\text{ is completely non-unitary}.}
\]
In particular, \(D\) has no eigenvalue on the unit circle.

This does **not** imply \(\rho(D)<1\). The unilateral backward shift is
the standard warning: it is strongly stable and has norm and spectral
radius equal to one, while having no unitary part. Therefore the
remaining possibilities for our \(D\) include strong stability with
\(\rho(D)=1\), as well as failure of strong stability through a
non-unitary component. The orbit-energy criterion in Section 14 is
designed to distinguish these behaviours.

## 16. Golden Fourier memory, Green–Kubo correlations, and the Stokes limit

This section records a cross-disciplinary bridge as a **research programme with
separated mathematical and physical status**. The Fourier identities below
are exact. The Green–Kubo and Stokes formulae are standard physical relations.
Identifying the present golden-Bernoulli compression with a physical stress or
friction memory kernel remains open.

### 16.1 The exact \(\pi\)–\(\varphi\) Fourier cascade

Let \(\lambda=\varphi^{-1}\), and let
\[
(P h)(x)=\frac12h(\lambda x-1)+\frac12h(\lambda x+1)
\]
be the equal-weight golden Bernoulli Markov operator. For every real
frequency \(\xi\),
\[
\boxed{P(e^{i\xi x})=\cos(\xi)e^{i\lambda\xi x}.}
\]
Iteration gives the exact identity
\[
\boxed{
P^n(e^{i\xi x})
=\left(\prod_{j=0}^{n-1}\cos(\lambda^j\xi)\right)
 e^{i\lambda^n\xi x}.}
\]
Consequently, for the characteristic function of the invariant golden
Bernoulli measure,
\[
\widehat{\nu_g}(\xi)
=\prod_{j=0}^{\infty}\cos(\lambda^j\xi).
\]

The roles of the constants are distinct:
- \(\varphi\) fixes the geometric contraction of frequencies,
  \(\xi\mapsto\lambda\xi\);
- \(2\pi\) fixes the Fourier phase convention and the locations of
  integer-period resonances;
- the cosine product is the exact amplitude accumulated along the
  scale cascade.

Since \(\varphi\) is a Pisot number, the classical Erdős theorem implies
that the Fourier transform of the equal-weight golden Bernoulli
convolution does not tend to zero at infinity; in particular there are
high-frequency sequences associated with \(2\pi\varphi^n\) along which
Fourier persistence occurs. This is a rigorous arithmetic property of
\(\nu_g\), not yet a statement about a physical relaxation spectrum.

### 16.2 The operator memory already available

For the orthogonal complement compression \(D=QP|_{\operatorname{ran}Q}\),
the scalar orbit correlations
\[
C_n(f)=\langle f,D^n f\rangle_{L^2(\nu_g)}
\]
are well-defined for every \(f\in\operatorname{ran}Q\). In a finite
Feshbach/Mori decomposition
\[
A=\begin{pmatrix}A_{11}&B\\C&D\end{pmatrix},
\]
the corresponding matrix-valued memory sequence is
\[
K_n=BD^nC,\qquad n\geq0,
\]
and the effective resolvent correction is
\[
\Sigma(z)=B(zI-D)^{-1}C.
\]
These are exact identities for a given block operator; in the present
project the stored harmonic matrices are finite empirical-CDF
approximations, while the infinite-dimensional compression results
are those proved in Sections 12–15.

Neither \(C_n(f)\) nor \(K_n\) is automatically a physical stress
autocorrelation. A physical identification requires specifying the
observable, the equilibrium state, the projection defining the resolved
variables, and the physical time represented by one Markov step.

### 16.3 Green–Kubo viscosity and Mori–Zwanzig memory

For an equilibrium, homogeneous Newtonian fluid, the Green–Kubo
expression for shear viscosity is
\[
\boxed{
\eta_{\rm GK}
=\frac{1}{Vk_BT}\int_0^\infty
\left\langle\delta\Pi_{xy}(t)\,
\delta\Pi_{xy}(0)\right\rangle_{\rm eq}\,dt,}
\]
where \(V\) is the volume, \(T\) the temperature, and
\(\delta\Pi_{xy}\) the fluctuation of the appropriate microscopic
off-diagonal stress component. The thermodynamic and long-time limits,
ensemble, and stress convention must be specified in an application.

In Mori–Zwanzig theory, a generalized Langevin equation contains a
memory kernel determined by a **projected random-force correlation**.
The exact prefactors depend on the normalization and inner product used
for the resolved variable. Thus a generic stress autocorrelation and a
Mori random-force memory kernel must not be identified without deriving
the relevant projection and fluctuation–dissipation relation.

If a discrete-time observable \(\Pi_n\) has been shown to represent the
equilibrium shear stress sampled at intervals \(\Delta t\), a consistent
trapezoidal Green–Kubo approximation is
\[
\eta_{\rm GK}^{(\Delta t)}
=\frac{\Delta t}{Vk_BT}
\left[\frac12 C_\Pi(0)+
\sum_{n=1}^{\infty}C_\Pi(n)\right],
\qquad
C_\Pi(n)=\langle\delta\Pi_n\delta\Pi_0\rangle_{\rm eq}.
\]
This formula is a discretization of Green–Kubo, not a licence to
substitute \(C_n(f)=\langle f,D^nf\rangle\): that substitution is
permitted only after the physical observable and dynamics have been
identified and the correlation series shown to converge.

### 16.4 Stokes friction and the continuum matching condition

For a rigid sphere of hydrodynamic radius \(a\), translating slowly
through an unbounded incompressible Newtonian fluid with no-slip
boundary condition and negligible Reynolds number, Stokes' law gives
\[
\zeta_{\rm Stokes}=6\pi\eta a.
\]
Therefore
\[
\boxed{\eta_{\rm Stokes}=\frac{\zeta}{6\pi a}.}
\]
The Einstein relation in thermal equilibrium,
\(D_{\rm diff}=k_BT/\zeta\), connects the same friction coefficient
to the long-time translational diffusion coefficient under its
usual assumptions.

A Green–Kubo friction coefficient can be matched to Stokes friction
only after the force observable, projection, hydrodynamic radius,
boundary condition, and zero-frequency/long-time limit have been
made consistent. In particular, an unprojected force autocorrelation
need not be the correct Mori friction kernel when conserved momentum
or other slow variables are present.

### 16.5 The proposed bridge and its status

The proposed chain is
\[
\boxed{
\begin{gathered}
\text{golden scale cascade }(\varphi)
+\text{ Fourier phase }(2\pi)\\
\Downarrow\quad\text{exact harmonic identities}\\
\nu_g,\ P,\ D,\ C_n,\ K_n\\
\Downarrow\quad\text{observable and projection still to identify}\\
\text{Mori--Zwanzig memory / fluctuation--dissipation}\\
\Downarrow\quad\text{hydrodynamic limit and matching}\\
\eta_{\rm GK}\ \longleftrightarrow\
\zeta\ \longleftrightarrow\ \eta_{\rm Stokes}.
\end{gathered}}
\]

A discrete-scale-invariant memory profile such as
\[
K(t)=A\,t^{-\alpha}
\left[1+\sum_{m\geq1}a_m
\cos\!\left(2\pi m\log_\varphi(t/t_0)+\theta_m\right)\right]
\]
may be investigated as a **phenomenological ansatz** motivated by
golden scaling. It is not derived by the Fourier product above and is
not asserted as a theorem. Its Green–Kubo integrability must be checked:
absolute convergence at large \(t\) follows for a bounded modulation
when \(\alpha>1\); for \(\alpha\leq1\), any conditional cancellation
requires a separate proof.

**Evidence ledger.**
- **Exact:** Fourier action of \(P\) on exponentials; its iterated cosine
  product; the definition of \(C_n(f)\); the finite-block identities
  \(K_n=BD^nC\) and \(\Sigma(z)=B(zI-D)^{-1}C\).
- **Classical external results:** Pisot non-decay for the golden
  Bernoulli Fourier transform; Green–Kubo transport formula;
  Mori–Zwanzig projected-force memory; Stokes drag
  \(\zeta=6\pi\eta a\).
- **Numerical/project-level:** finite harmonic memory matrices and
  their correlations, subject to the sampling and Galerkin limitations
  stated in Sections 7–10.
- **Open:** identify a physical stress or projected-force observable
  represented by \(f\), \(D\), or \(K_n\); establish a justified time
  scale \(\Delta t\); prove convergence of the relevant correlation
  integral/sum; derive the fluctuation–dissipation normalization; and
  demonstrate the hydrodynamic matching to Stokes friction.
- **Not claimed:** \(\eta_{\rm GK}=\eta_{\rm Stokes}\) for the present
  model; a physical viscosity prediction from \(\varphi\) alone; or a
  derivation of the log-periodic ansatz from the golden Bernoulli
  convolution.

### References for this bridge

- P. Erdős, “On a family of symmetric Bernoulli convolutions,”
  *American Journal of Mathematics* **61** (1939), 974–976.
- R. Kubo, “Statistical-Mechanical Theory of Irreversible Processes.
  I. General Theory and Simple Applications to Magnetic and Conduction
  Problems,” *Journal of the Physical Society of Japan* **12** (1957),
  570–586.
- H. Mori, “Transport, Collective Motion, and Brownian Motion,”
  *Progress of Theoretical Physics* **33** (1965), 423–455.
- R. Zwanzig, “Memory Effects in Irreversible Thermodynamics,”
  *Physical Review* **124** (1961), 983–992.
- G. G. Stokes, “On the Effect of the Internal Friction of Fluids on the
  Motion of Pendulums,” *Transactions of the Cambridge Philosophical
  Society* **9** (1851), 8–106.

### 16.6 Monograph and theorem crosswalk

This is a cross-cutting bridge, not a new chapter. Its natural monograph links
are Chapters 1–5 (Fourier/arithmetic and geometric foundations), 13–19
(fractal measures, golden scaling, Markov operators and memory), and 24–27
(transport, continuum limits and physical interpretation). The relevant
theorem-record crosswalk is T100–T107 and T131, read together with the
TSMR-I records in this file. These links are organizational: they do not
upgrade an open physical identification into a proved theorem.

## 17. Identifying the physical stress observable: exact Mori reduction and the Q6 obstruction

This section sharpens the open bridge in Section 16. It gives the exact
operator identity that a discrete model must satisfy, derives the
continuum momentum-to-stress relation used in hydrodynamics, and states
what is currently missing for the golden-Bernoulli/Q6 construction.

### 17.1 Exact discrete Mori–Zwanzig identity

Let \(\mathcal H\) be a Hilbert space, \(T:\mathcal H\to\mathcal H\)
a bounded one-step evolution operator, and \(\mathsf P\) an orthogonal
projection onto resolved variables. Put \(\mathsf Q=I-\mathsf P\) and
write the block operator
\[
T=\begin{pmatrix}
T_{PP}&T_{PQ}\\
T_{QP}&T_{QQ}
\end{pmatrix}
\quad\text{on }\mathsf P\mathcal H\oplus\mathsf Q\mathcal H.
\]
For \(h_n=T^nh\), set \(u_n=\mathsf P h_n\) and \(v_n=\mathsf Qh_n\).
The two block recurrences are
\[
u_{n+1}=T_{PP}u_n+T_{PQ}v_n,\qquad
v_{n+1}=T_{QP}u_n+T_{QQ}v_n.
\]
Solving the second recurrence and substituting into the first gives,
for every \(n\geq0\),
\[
\boxed{
u_{n+1}=T_{PP}u_n+
T_{PQ}T_{QQ}^{\,n}v_0+
\sum_{j=0}^{n-1}
T_{PQ}T_{QQ}^{\,n-1-j}T_{QP}u_j.}
\]
The sum is the exact discrete memory term. Its kernel is
\[
\boxed{K_m=T_{PQ}T_{QQ}^{\,m}T_{QP},\qquad m\geq0.}
\]
The term \(T_{PQ}T_{QQ}^{n}v_0\) is the initial unresolved-state
contribution and must not be silently discarded.

This identity applies to the finite harmonic block decomposition in
Section 8, with \(T_{PP}=A_{11}\), \(T_{PQ}=B\),
\(T_{QP}=C\), \(T_{QQ}=D\). Thus \(K_m=BD^mC\) is an exact
discrete projection-memory kernel for that chosen block matrix.
It is not, by itself, a Green–Kubo stress correlation or a
fluctuation–dissipation theorem. In particular, for a non-self-adjoint
Markov operator, \(T_{PQ}\) and \(T_{QP}\) are not automatically
adjoints, and positivity of the scalar memory sequence does not follow.

### 17.2 The continuum identity that connects momentum to shear stress

Consider an equilibrium fluid with microscopic momentum density
\(g_x(\mathbf q)\), and choose a transverse wavevector
\(\mathbf q=q\,\mathbf e_y\). Local momentum conservation gives
\[
\partial_t g_x(q,t)=-iq\,\Pi_{xy}(q,t),
\]
where \(\Pi_{xy}\) is the corresponding microscopic momentum-flux
(stress) component. This conservation law is the physical bridge:
shear stress is the flux transporting transverse momentum.

In the equilibrium Hilbert space with inner product
\((X,Y)=\langle X^*Y\rangle_{\rm eq}\), let \(\mathsf P\) be the
Mori projection onto \(A=g_x(q)\):
\[
\mathsf P X=(X,A)(A,A)^{-1}A,\qquad \mathsf Q=I-\mathsf P.
\]
For Liouville generator \(\mathcal L\), define the initial random force
\[
F(0)=\mathsf Q\mathcal L A
=-iq\,\mathsf Q\Pi_{xy}(q),
\]
where the last equality uses the momentum conservation law. Under
the standard Mori construction, the orthogonal-dynamics force is
\(F(t)=e^{t\mathsf Q\mathcal L\mathsf Q}F(0)\), and the scalar memory
kernel is
\[
\boxed{
M_A(t)=\frac{(F(t),F(0))}{(A,A)}
=\frac{q^2}{(g_x(q),g_x(q))}
\left(
e^{t\mathsf Q\mathcal L\mathsf Q}\mathsf Q\Pi_{xy}(q),
\mathsf Q\Pi_{xy}(q)
\right).}
\]
This is an exact projected-stress representation under the stated
equilibrium and projection hypotheses. It is the appropriate
Mori object to compare with a coarse-grained memory kernel.

Crucially, the stress in this formula evolves under **orthogonal
dynamics**, not automatically under the full Liouville evolution.
Therefore it is not legitimate to replace this expression by the
ordinary Green–Kubo stress autocorrelation without deriving the
relevant zero-wavevector, zero-frequency and projection limits.
The Green–Kubo shear viscosity remains
\[
\eta_{\rm GK}=\frac{1}{Vk_BT}\int_0^\infty
\langle\delta\Pi_{xy}(t)\delta\Pi_{xy}(0)\rangle_{\rm eq}\,dt,
\]
with the stress evolved under the full equilibrium dynamics. The
matching between this formula and the Mori memory is a hydrodynamic
limit statement, not an algebraic identity at finite \(q\).

### 17.3 A graph-level candidate for Q6/RGS

The reconstructed embedding \(X:V(Q6)\to\mathbb R^3\) permits a
geometric **candidate** for a graph virial stress, provided a mechanical
action is supplied. For an oriented edge \(e=(i,j)\), put
\[
r_e=X_j-X_i,\qquad
f_e=-\frac{\partial U}{\partial r_e},
\]
where \(U\) is an explicitly specified edge-based potential. A
configurational stress candidate is
\[
\boxed{
\Pi^{\rm graph}_{ab}
=\frac1V\sum_{e\in E(Q6)}r_{e,a}f_{e,b},
\qquad
\delta\Pi^{\rm graph}_{ab}
=\Pi^{\rm graph}_{ab}
-\langle\Pi^{\rm graph}_{ab}\rangle_{\rm eq}.}
\]
For shear viscosity the relevant component is the off-diagonal
traceless part, for example \(a=x,b=y\). A complete mechanical model
may also require a kinetic contribution, depending on its degrees of
freedom and Hamiltonian.

This expression is a definition conditional on \(U\), \(V\), and an
equilibrium measure; it is **not yet a computed Q6 stress**. The
available graph geometry and adjacency do not determine the edge
forces, physical volume, temperature, momenta, or time evolution.
Assigning arbitrary edge weights or treating a geometric anisotropy
tensor as a stress would not close this gap.

### 17.4 Necessary identification test for the golden memory

To identify a golden-Bernoulli correlation with a physical shear
stress, one must construct an equilibrium dynamical model and a
centered observable \(\Pi_{xy}\) such that a map \(\mathcal J\) from
the golden-coordinate space into the physical observable space
satisfies, at minimum:

1. **Equilibrium compatibility:** \(\mathcal J\) preserves the relevant
   inner product/covariance and maps constants to constants.
2. **Observable identification:** \(\mathcal J f\) is the centered
   microscopic shear stress, or the projected random force associated
   with transverse momentum; it cannot be declared so by matching
   dimensions or plots.
3. **Dynamical compatibility:** the Markov/compressed evolution
   intertwines with the physical full or orthogonal dynamics in the
   precise sector used. For a discrete model this requires an identity
   or controlled approximation such as
   \(\mathcal J T_{\rm eff}^n f\simeq
   T_{\rm phys,eff}^n\mathcal J f\), with an error estimate.
4. **Time calibration:** one Markov step corresponds to a measured or
   derived \(\Delta t\), not an arbitrary unit.
5. **Fluctuation–dissipation and convergence:** the projected-force
   covariance has the normalization required by the Mori equation,
   and the Green–Kubo integral (or its discrete sum) converges in the
   stated thermodynamic and long-time limits.
6. **Hydrodynamic matching:** the long-wavelength transverse-momentum
   relaxation yields a finite shear viscosity and, for a sphere with
   no-slip boundary conditions at low Reynolds number, the friction
   tends to \(\zeta=6\pi\eta a\).

The current golden Bernoulli operator is a scalar invariant-measure
Markov operator. The present record does not construct a momentum
density, a Liouville generator, a Q6 edge-force action, or a map
\(\mathcal J\) satisfying these conditions. Moreover, its compression
\(D=QPQ\) is not known to be a reversible Markov semigroup. The
physical stress identification is therefore **open**, not proved or
numerically verified.

### 17.5 Decisive next computations

The next work is now sharply specified:

- provide an action \(U\) on the reconstructed Q6/RGS embedding and
  derive forces by differentiation, rather than fitting edge weights;
- construct the invariant Gibbs/equilibrium measure and its
  time-evolution operator (including momenta if the model is
  mechanical);
- calculate the graph virial stress and its equilibrium covariance;
- verify the discrete or continuous momentum-balance identity;
- build the Mori projection onto transverse momentum and compute the
  projected-force memory;
- compare that memory with \(BD^nC\) only after an explicit
  intertwining/covariance map and a time-step calibration are given;
- evaluate the Green–Kubo integral and test the hydrodynamic/Stokes
  limit with finite-size and boundary-condition controls.

**Status update.**
- **Proved here:** the discrete block-memory recurrence and its exact
  kernel; the conditional Mori projected-stress identity from local
  momentum conservation.
- **Defined as candidate:** the Q6 graph virial stress, conditional on
  a specified mechanical action and equilibrium model.
- **Open:** construction of that action and equilibrium dynamics;
  identification of the golden observable with stress or random force;
  FDT normalization; Green–Kubo convergence; and Stokes matching.
- **Explicitly not claimed:** that the existing \(D\), \(C_n\), or
  \(K_n\) already is a physical stress correlation or viscosity kernel.

### References for the projection/stress identification

- H. Mori, “Transport, Collective Motion, and Brownian Motion,”
  *Progress of Theoretical Physics* **33** (1965), 423–455.
- R. Zwanzig, “Memory Effects in Irreversible Thermodynamics,”
  *Physical Review* **124** (1961), 983–992.
- “4.2 Mori–Zwanzig Theory,” *The Green–Kubo Relations*,
  Australian National University online text.
- C. Widder, J. Zimmer, and T. Schilling, “On the generalized
  Langevin equation and the Mori projection operator technique,”
  *Journal of Physics A: Mathematical and Theoretical* **58** (2025),
  405001, DOI: 10.1088/1751-8121/ae02cc.


### 17.6 Action-derived Q6 shear: finite result and obstruction

The implementation-level follow-up is recorded in [RGS–QLG–Q6 PR #217](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/217). It reuses the existing finite Euclidean action and its analytic directional derivative, rather than postulating a new force law.

For a symmetric traceless coframe shear H, e_v(gamma)=(I+gamma H)e_v, define the exact finite-action response
\[
\Pi_H^{action}=-V^{-1}(dS_{Q6}/d\gamma)|_{\gamma=0}.
\]
The code evaluates this derivative analytically and provides a central finite-difference check. The current action has an important limitation: the Wilson plaquette term depends on link holonomies only; hopping, twin and quartic terms depend on the coframe only through determinant-volume factors. Since d log|det e_v|/d gamma = tr(H)=0, those sectors have zero first-order response to this shear. The only possible nonzero contribution is the fixed-frame coframe-difference regularizer. Thus this is an exact derivative of the implemented finite action, not yet the full microscopic shear stress needed for Green–Kubo.

A separate previously derived geometric edge identity is also preserved. For w_e(gamma)=|d_e(gamma)|^{-2}, d_e(gamma)=(I+gamma H)d_e, and H=(E_xy+E_yx)/2,
\[
w'_e(0)=-2\,d_{e,x}d_{e,y}/|d_e|^4.
\]
If a declared edge Hamiltonian has the form H_link(gamma)=sum_e w_e(gamma)E_e with E_e held fixed, then
\[
\Pi_{xy}^{Q6}=-(1/V)\partial_\gamma H_{link}|_0
= (2/V)\sum_e d_{e,x}d_{e,y}|d_e|^{-4}E_e.
\]
This conditional edge-energy response is implemented and finite-difference-auditable in PR #217. It is not identified with the plaquette-only Wilson term in the current unified action: the E_e must be derived from a common metric-dependent action before combining the formulas.

**Updated evidence boundary:** exact finite-action and inverse-square edge-weight derivatives are specified; PR #217 adds implementation and tests (CI pending at last check). Still OPEN: metric-dependent gauge/Hodge and matter kinetic terms, equilibrium measure and time evolution, physical stress covariance, FDT normalization, Green–Kubo convergence, and Stokes matching. No viscosity is claimed.
