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


## 11. Exact contraction, non-normal memory, and the finite-sample defect

There is an exact operator inequality that constrains the interpretation of every Galerkin table. Since the cumulative-coordinate Markov operator preserves Lebesgue measure,
[
int_0^1 mathscr M_g h(t),dt=int_0^1h(t),dt
]
for every integrable (h). Jensen's inequality gives
[
|mathscr M_g f(t)|^2leq mathscr M_g(|f|^2)(t),
]
and therefore
[
oxed{|mathscr M_g f|_{L^2}leq|f|_{L^2}.}
]
Let (Q_H) be the orthogonal projection onto the resolved complement
(operatorname{span}{psi_{k,c},psi_{k,s}:2leq kleq H}). Its exact
compression (D_H=Q_Hmathscr M_gQ_H|_{operatorname{ran}Q_H}) must satisfy
[
oxed{|D_H|_{2	o2}leq1,qquad ho(D_H)leq1.}
]
Thus a genuine loss of contractivity is mathematically impossible for the
exact operator compression. Strict contraction, a uniform gap below one,
and convergence as H tends to infinity do not follow from this inequality.

### Refined empirical audit

The vectorized NumPy audit was rerun with 300,000 samples, 48 Bernoulli
terms, seed 20261124, and cutoffs through H=16. The result record is
results/tsmr_i_harmonic_convergence.json.

| H | dim(Q_H) | rho(D_H) | ||D_H||_2 (empirical) | ||K_0||_F | ||K_1||_F | ||K_2||_F | ||K_3||_F |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 2 | 0.21457 | 0.21457 | 0.11524 | 0.02378 | 0.00500 | 0.00106 |
| 3 | 4 | 0.14899 | 0.47642 | 0.12943 | 0.00387 | 0.00142 | 0.00011 |
| 4 | 6 | 0.36107 | 0.86673 | 0.12323 | 0.04485 | 0.02413 | 0.00158 |
| 6 | 10 | 0.31920 | 0.97645 | 0.12497 | 0.05689 | 0.01329 | 0.00201 |
| 8 | 14 | 0.38050 | 0.99582 | 0.12435 | 0.05528 | 0.01031 | 0.01198 |
| 10 | 18 | 0.43350 | 1.00115 | 0.12437 | 0.05507 | 0.01825 | 0.00830 |
| 12 | 22 | 0.41251 | 1.00286 | 0.12449 | 0.05544 | 0.02025 | 0.01012 |
| 16 | 30 | 0.41403 | 1.00550 | 0.12442 | 0.05520 | 0.01971 | 0.00099 |

The empirical singular norm exceeds one by at most about 0.55% in this
table (H=16). This is not a physical or operator-theoretic instability:
it is a finite-sample/empirical-CDF defect, amplified as higher frequencies
are resolved. The exact contraction theorem above is the benchmark that
the numerical scheme must respect in the limit. This defect should be used
as an error diagnostic, not clipped or interpreted as a true norm.

Three further observations are supported by the finite data:

1. The initial coupling stabilizes: ||K_0||_F stays close to 0.1244 from
   H=4 through H=16.
2. Higher harmonics change the transient memory profile. In particular,
   ||K_2||_F and ||K_3||_F are not monotone in H, and the H=8, 12, and 16
   sequences have visible rebounds at intermediate n. The 2+2 model
   therefore captures the existence of memory but under-resolves its
   temporal profile.
3. For the tested finite sections, rho(D_H) remains below 0.44 and the
   recorded kernels are very small by n=20. This is evidence for decay in
   these truncations, not a proof of a uniform spectral gap or of
   convergence of the infinite-dimensional Mori-Zwanzig kernel.

The current mathematical picture is consequently **contractive but
potentially non-normal**, with a nontrivial transient memory response.
The open problem is to control the empirical-CDF error uniformly in H and
then establish whether the exact complement has a spectral gap, merely
strong stability, or approximate unit-modulus modes. The audit now records
both eigenvalue radius and largest singular value; the latter is essential
because eigenvalues alone miss non-normal transient amplification.
