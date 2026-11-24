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
