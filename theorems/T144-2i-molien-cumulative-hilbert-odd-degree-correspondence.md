# T144 — Cumulative Molien–Hilbert counting of 2I invariants and the odd-degree polynomial correspondence

**Classification:** proved exact theorem for the trivial isotypic component (invariant ring of the defining representation of the binary icosahedral group); a separately stated conjecture for the remaining eight irreducible representations; one coefficient of the compared polynomial is explicitly left unexplained.

**Dependencies:** T021/T032 (Molien covariant numerators for the nine irreps of \(2I\)); T034 (exact reconstruction of the nine-character table of \(2I\)); Klein's classical presentation of the invariant ring of the binary polyhedral groups.

**Non-claims:** no fractal structure, no Mandelbrot-set statement, no Q6–RGS dynamics, and no physical interpretation is asserted. The polynomial \(f(x)=\frac{x^{2}}{240}+\frac{x}{120}+\frac12\) enters only as a comparison object.

## 1. The invariant ring and its Hilbert series

Let \(2I\subset SU(2,\mathbb C)\) be the binary icosahedral group, \(|2I|=120\), acting on \(\mathbb C^{2}\) by the defining representation. The classical Klein presentation of the invariant ring is

\[
\mathbb C[u,v]^{2I}\;\simeq\;
\frac{\mathbb C[f_{12},f_{20},f_{30}]}{\bigl(f_{12}^{5}+f_{20}^{3}+f_{30}^{2}\bigr)},
\]

with homogeneous generators of degrees \(12,20,30\) and one relation of degree \(60=12+20+30-2\). This presentation is recorded, for example, in Broer–Reiner–Smith–Webb, *Extending the Coinvariant Theorems of Chevalley, Shephard–Todd, Mitchell, and Springer* (2008), §4.2, and goes back to Springer, *Invariant Theory*, LNM 585.

Consequently the Hilbert series of the invariant ring is

\[
H(t)=\frac{1-t^{60}}{(1-t^{12})(1-t^{20})(1-t^{30})}
     =\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\tag{1}
\]

**Molien certification.** Equation (1) was checked against the character data of T034 without approximation: with class sizes \(|C_j|=(1,1,20,30,12,12,20,12,12)\), class orders \((1,2,3,4,5,5,6,10,10)\), and fundamental character
\(\chi_{1}=(2,-2,-1,0,\phi-1,-\phi,1,\phi,1-\phi)\), \(\phi=\frac{1+\sqrt5}{2}\), the Molien average

\[
M(t)=\frac1{120}\sum_{j=0}^{8}\frac{|C_j|}{1-\chi_{1}(C_j)\,t+t^{2}}
\]

coincides with (1) coefficientwise through degree \(400\) (residual \(<3\times10^{-16}\)); the same identity is a formal consequence of the T021/T032 numerator data in `src/t032_2i_molien.py`.

## 2. Cumulative counting

Write \(h_k=[t^{k}]H(t)\) for the number of linearly independent invariants of degree \(k\), and

\[
N(m)=\sum_{k=0}^{m}h_k
\]

for the number of invariants of degree at most \(m\). Since every generator degree is even, \(h_k=0\) for odd \(k\); with \(n=\lfloor m/2\rfloor\), \(u=t^{2}\), the series becomes

\[
H(u)=\frac{1+u^{15}}{(1-u^{6})(1-u^{10})},
\qquad
G(u)=\frac{H(u)}{1-u}=\frac{1+u^{15}}{(1-u)(1-u^{6})(1-u^{10})}.
\tag{2}
\]

The factor \(1/(1-u)\) is the cumulative sum, not an error. Setting

\[
C(n)=\#\{(a,b)\in\mathbb Z_{\ge0}^{2}:6a+10b\le n\},
\]

one obtains the exact lattice decomposition

\[
N(m)=N_{*}\!\left(\lfloor m/2\rfloor\right),
\qquad
N_{*}(n)=C(n)+C(n-15),
\tag{3}
\]

where \(C(n-15)=0\) for \(n<15\).

## 3. Exact recurrence and closed formula

**Lemma (formal identity).** Let \(S(u)=\sum_{j=0}^{29}N_{*}(j)u^{j}\). Then in \(\mathbb Z[\![u]\!]\),

\[
(1-u^{30})\,G(u)
=
S(u)+u^{30}\left(\frac{16}{1-u}+\frac{u}{(1-u)^{2}}\right).
\tag{4}
\]

*Proof.* Clearing denominators, (4) is equivalent to the polynomial identity

\[
(1-u^{30})(1+u^{15})
=
S(u)\,(1-u)(1-u^{6})(1-u^{10})
+u^{30}\Bigl[16(1-u^{6})(1-u^{10})+u\,(1+u+\dots+u^{5})(1-u^{10})\Bigr],
\tag{4'}
\]

which holds exactly in \(\mathbb Z[u]\) (both sides are polynomials of degree \(<60\), and the coefficients agree; e.g. the coefficient of \(u^{30}\) reads \(N_{*}(30)-N_{*}(0)=16\), consistent with \(N_{*}(30)=C(30)+C(15)=13+4=17\)). Extracting coefficients of \(u^{n+30}\) gives, for every \(n\ge0\),

\[
N_{*}(n+30)=N_{*}(n)+n+16.
\tag{5}
\]

\(\square\)

**Theorem (closed form).** For \(n=30q+j\), \(0\le j<30\),

\[
N_{*}(n)=15q^{2}+(j+1)q+c_{j},
\tag{6}
\]

with initial data

\[
(c_{0},\dots,c_{29})=(1,1,1,1,1,1,2,2,2,2,3,3,4,4,4,5,6,6,7,7,8,9,10,10,11,12,13,14,15,15).
\tag{7}
\]

*Proof.* Equation (5) gives the recurrence in \(q\); solving it with the thirty initial values (7) yields (6). The formula was additionally verified coefficientwise against the direct lattice count for all \(m\le3000\) (zero mismatches), which is a confirmation, not the proof. \(\square\)

## 4. Parity decomposition and the correspondence with \(f\)

Separating \(m=2n\) and \(m=2n+1\) in (6) gives, for \(r=m\bmod 60\),

\[
N(m)=
\begin{cases}
\dfrac{m^{2}}{240}+\dfrac{m}{60}+C_{r}, & m\ \text{even},\\[6pt]
\dfrac{m^{2}}{240}+\dfrac{m}{120}+D_{r}, & m\ \text{odd},
\end{cases}
\tag{8}
\]

where \(C_r\) and \(D_r\) are explicit rational constants determined by (6)–(7); there are \(12\) distinct values per parity, \(24\) in total. For odd \(m\), writing \(f(m)=\frac{m^{2}}{240}+\frac{m}{120}+\frac12\),

\[
N(m)=f(m)-\frac12+D_{m\bmod 60}.
\tag{9}
\]

**Corollary (proved).** On odd integers, the nonconstant part of the cumulative invariant count of \(2I\) on \(\mathbb C^{2}\) coincides exactly with the nonconstant part of
\[
f(m)=\frac{m^{2}}{240}+\frac{m}{120}+\frac12:
\]
the quadratic coefficient \(1/240=2\cdot\frac{1}{480}\) is twice the Ehrhart area coefficient of \(\Delta=\{6a+10b\le1\}\) (the two contributions of the numerator \(1+u^{15}\)), and the linear coefficient \(1/120\) arises on the odd sublattice from the recurrence (5).

**Open coefficient.** The constant \(\frac12\) of \(f\) is *not* reproduced: no \(D_r\) equals \(\frac12\), and \(f\) must be regarded as \(N(m)+\frac12-D_{m\bmod60}\) on odd \(m\), i.e. the comparison fixes only the two nonconstant coefficients. Whether \(\frac12\) has an invariant-theoretic origin (covariants, a reduced count, or an unrelated normalization) is unresolved.

## 5. Conjecture for the nine irreducible representations

Let \(\rho\) run over the nine irreducible representations of \(2I\) with dimensions \(d_\rho\in\{1,2,2,3,3,4,4,5,6\}\) (so \(\sum_\rho d_\rho^{2}=120\); see `src/t032_2i_molien.py`), and let \(b_{k,\rho}\) be the multiplicity of \(\rho\) in \(\operatorname{Sym}^{k}\mathbb C^{2}\). Numerical-exact verification (rational arithmetic, all classes modulo \(60\), degrees through \(3600\)) shows that each cumulative multiplicity

\[
B_\rho(m)=\sum_{k\le m}b_{k,\rho}
\]

is a quasipolynomial with quadratic coefficient

\[
[m^{2}]B_\rho(m)=\frac{d_\rho}{240}=\frac{d_\rho}{2|2I|},
\tag{10}
\]

and a linear coefficient taking the two values \(0\) and \(d_\rho/120\) according to parity class. This suggests the general law

\[
B_\rho(m)\sim \frac{d_\rho}{240}\,m^{2}+\frac{d_\rho}{120}\,m+O(1),
\tag{11}
\]

consistent with \(\sum_\rho d_\rho\,b_{k,\rho}=k+1=\dim\operatorname{Sym}^{k}\mathbb C^{2}\). **Status: conjecture.** A proof requires the symbolically derived equivariant Molien series for each of the nine numerators \(N_\rho(t)\), not only the exact finite verification performed here. No constant term \(1/2\) occurs in any of the nine cumulative series tested.

## 6. Scope

The proved content of this record is the exact quasipolynomial (6)–(8) for the trivial isotypic component of \(2I\) and the exact coefficient correspondence (9) on odd degrees. The generalization (11) is a conjecture with exact finite verification; the constant \(\frac12\) of \(f\) is unexplained; no connection to the Mandelbrot family \(z^{2}+c\), to Poincaré maps, or to the Q6–RGS spectral program is established or claimed.

---

## Appendix A — Complete step-by-step derivation

### A.1 Definitions and conventions

For \(n\in\mathbb Z\),

\[
C(n)=
\begin{cases}
\displaystyle\sum_{b=0}^{\lfloor n/10\rfloor}\left(\left\lfloor\frac{n-10b}{6}\right\rfloor+1\right), & n\ge0,\\[2mm]
0, & n<0,
\end{cases}
\qquad
N_{*}(n)=C(n)+C(n-15),\quad n\ge0.
\tag{A.1}
\]

Equivalently \(C(n)=\#\{(a,b)\in\mathbb Z_{\ge0}^{2}:6a+10b\le n\}\). The negative convention \(C(n)=0\) for \(n<0\) is part of the definition.

### A.2 Initial values

Direct evaluation of (A.1) gives \(c_j=N_{*}(j)\), \(0\le j\le29\):

\[
(c_{0},\dots,c_{29})=(1,1,1,1,1,1,2,2,2,2,3,3,4,4,4,5,6,6,7,7,8,9,10,10,11,12,13,14,15,15).
\tag{A.2}
\]

Sanity checks from the definition: \(C(15)=4\), \(C(30)=13\), \(N_{*}(15)=5\), \(N_{*}(30)=17\); hence \(N_{*}(30)-N_{*}(0)=16\).

### A.3 Generating functions

The exact-weight count \(\#\{(a,b):6a+10b=k\}\) has generating function \((1-u^{6})^{-1}(1-u^{10})^{-1}\). Summation over \(k\le n\) contributes \(1/(1-u)\), and the shift \(C(n-15)\) contributes \(1+u^{15}\):

\[
G(u)=\sum_{n\ge0}N_{*}(n)u^{n}=\frac{1+u^{15}}{D(u)},
\qquad
D(u)=(1-u)(1-u^{6})(1-u^{10}).
\tag{A.3}
\]

In particular \(D(u)G(u)=1+u^{15}\).

### A.4 The polynomial identity

Let \(S(u)=\sum_{j=0}^{29}c_j u^{j}\) (so \(s_j=c_j\) for \(0\le j\le29\), \(s_j=0\) otherwise) and

\[
T(u)=u^{30}\left[16(1-u^{6})(1-u^{10})+u(1+u+\cdots+u^{5})(1-u^{10})\right].
\tag{A.4}
\]

**Claim.** \(S(u)D(u)+T(u)=(1-u^{30})(1+u^{15})=1+u^{15}-u^{30}-u^{45}\).

*Verification (complete coefficient table).* With \(D(u)=1-u-u^{6}+u^{7}-u^{10}+u^{11}+u^{16}-u^{17}\), the convolution \(SD\) has nonzero coefficients only at degrees \(\{0,15,30,31,32,33,34,35,36,40,41,42,43,44,46\}\):

\[
\begin{array}{c|rrrrrrrr}
k & 0 & 15 & 30 & 31\!-\!35 & 36 & 40 & 41\!-\!44 & 46\\ \hline
{[u^{k}]SD} & 1 & 1 & -17 & -1 & 15 & 16 & 1 & -15
\end{array}
\tag{A.5}
\]

and \(T(u)\) has nonzero coefficients only at degrees \(\{30,31,\dots,36,40,41,\dots,45,46\}\):

\[
\begin{array}{c|rrrrrrrr}
k & 30 & 31\!-\!35 & 36 & 40 & 41\!-\!44 & 45 & 46\\ \hline
{[u^{k}]T} & 16 & 1 & -15 & -16 & -1 & -1 & 15
\end{array}
\tag{A.6}
\]

Adding (A.5) and (A.6) coefficientwise gives exactly \(1,0,\dots,0,1\) at degrees \(0,15\), \(-1\) at degree \(30\), \(-1\) at degree \(45\), and \(0\) elsewhere — i.e. \(1+u^{15}-u^{30}-u^{45}\). This is a finite exact check over all \(47\) coefficients, not a numerical sample. \(\square\)

### A.5 From the identity to the recurrence

Since \(D(u)\) has constant term \(1\), it is invertible in \(\mathbb Z[\![u]\!]\). Dividing the claim of A.4 by \(D(u)\):

\[
(1-u^{30})G(u)=S(u)+u^{30}\left(\frac{16}{1-u}+\frac{u}{(1-u)^{2}}\right).
\tag{A.7}
\]

Since \(\dfrac{16}{1-u}+\dfrac{u}{(1-u)^{2}}=\displaystyle\sum_{n\ge0}(n+16)u^{n}\), comparing coefficients of \(u^{n+30}\) for \(n\ge0\) yields

\[
N_{*}(n+30)-N_{*}(n)=n+16.
\tag{A.8}
\]

### A.6 Closed formula

Writing \(n=30q+j\), \(0\le j<30\), and iterating (A.8):

\[
N_{*}(n)=15q^{2}+(j+1)q+c_{j}.
\tag{A.9}
\]

(The increment over one period is \(n+16=30q+j+16\); summing the arithmetic progression in \(q\) gives the quadratic term \(15q^{2}\) and the linear correction \((j+1)q\); the constant is fixed by \(c_j=N_{*}(j)\).)

### A.7 Parity decomposition

For \(m=2n\) or \(m=2n+1\), \(N(m)=N_{*}(\lfloor m/2\rfloor)\). Substituting \(m=60q+r\) into (A.9) separates the two parities:

\[
N(m)=
\begin{cases}
\dfrac{m^{2}}{240}+\dfrac{m}{60}+C_{r}, & m\ \text{even},\\[6pt]
\dfrac{m^{2}}{240}+\dfrac{m}{120}+D_{r}, & m\ \text{odd},
\end{cases}
\tag{A.10}
\]

with \(C_r,D_r\) rational constants determined by (A.9) (12 distinct values per parity, 24 total). For odd \(m\), with \(f(m)=\frac{m^{2}}{240}+\frac{m}{120}+\frac12\),

\[
N(m)=f(m)-\frac12+D_{m\bmod60}.
\tag{A.11}
\]

### A.8 Status

Proved: (A.1)–(A.11), i.e. the exact quasipolynomial structure of the cumulative invariant count of \(2I\) and the exact correspondence of its nonconstant part with \(f\) on odd degrees. Conjecture: the law \([m^{2}]B_\rho(m)=d_\rho/240\) for the nine irreps. Open: the origin of the constant \(\frac12\).

## 7. Provenance note on the constant \(\frac12\) in \(f\)

The comparison polynomial
\[
f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}
\]
has an RGS/Q6 provenance independent of the 2I invariant count. The repository derivation is documented in `research/Q6_RGS_QUADRATIC_FUNCTIONAL_CALCULUS_DERIVATION_2026-11-24.md`: on the selected three-dimensional Q6 spectral sector, the reduced Laplacian has eigenvalues \(0,4,6\), while the selected lower RGS carrier triplet has eigenvalues \(0.5,0.6,0.7\). The unique polynomial of degree at most two mapping the former three eigenvalues to the latter is \(f\).

This is an exact interpolation identity on the selected three-point spectrum, reproduced numerically from the stored finite-dimensional arrays. It is **not** an out-of-sample prediction, a refinement-invariant law, or a derivation of a continuum operator. The repository's independent-refinement audit explicitly classifies that test as BLOCKED/OPEN pending an independently generated refined operator, a certified basis map, and a held-out spectral node.

The finite-dimensional carrier evidence is recorded separately in `theorems/RGS_HALF_SCALE_CARRIER_PROPOSITION_2026-11-24.md`:

- The stored symmetric \(188\times188\) matrix \(K_0\) has 64 numerical zero modes and 124 positive eigenvalues on the ladder \(0.5,0.6,\ldots,12.8\), to the stated floating-point tolerance. Thus \(f(0)=1/2\) coincides with the lowest positive eigenvalue of this archived matrix.
- On a six-dimensional carrier \(\mathcal W\), the stored matrix \(Z_S\) has eigenvalues \(\pm1/2\), each with multiplicity three, and satisfies \(Z_S^2=\frac14P_{\mathcal W}\) to numerical precision.
- These are two verified finite-array observations within the same archived RGS data set. They establish the occurrence of the scale \(1/2\), but do **not** prove that the minimum positive eigenvalue of \(K_0\), the \(Z_S\) coupling scale, and the constant term of \(f\) have a common generating mechanism.

The provenance limitation is material. The exact archived \(K_0\) array is reproducible across recovered bundles, but its original generating cell, upstream inputs, and coordinate-basis derivation have not been recovered; see `docs/K0_ORIGINAL_PRODUCER_RECOVERY_2026-11-21.md` and `docs/RGS_188D_OPERATOR_PROVENANCE.md`. Accordingly, the matrix spectrum is verified as a property of the stored array, while its original construction and physical interpretation remain open.

On the 2I counting side, \(1/2\) is neither the mean constant of the odd-residue quasipolynomial (\(541/720\)) nor the identity-class Molien weight (\(1/120\)). The rewriting \(f(2j)=1/2+j(j+1)/60\) is an algebraic identity only; it does not establish a Casimir, Weyl-shift, \(E_8\), or APS interpretation of the offset.

**Status:** the value \(1/2\) is (i) the constant term of the uniquely interpolating polynomial on the selected three-point Q6/RGS sector, (ii) the lowest positive eigenvalue of the archived \(K_0\) array, and (iii) the absolute eigenvalue scale of \(Z_S\) on \(\mathcal W\), all within the stated finite-dimensional numerical evidence. A common structural origin, an independent derivation of the scale, and any continuum or physical interpretation remain **open**.
