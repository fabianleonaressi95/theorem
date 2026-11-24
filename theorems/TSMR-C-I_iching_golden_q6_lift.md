# TSMR-C-I — I Ching trigram/hexagram coding and the golden Q6 lift

**Record type:** exact finite combinatorial model plus graph-directed extension  
**Status:** trigram collision and Q6 counts are exact; failure of scalar lumpability is exactly testable; the resulting infinite Markov measure is a defined model, not identified with the classical i.i.d. Erdős measure or a physical system.

## 1. Correct symbolic objects

The symbols 100 and 011 are **I Ching trigrams**, not arbitrary binary words. We encode each trigram by its three line values read from bottom to top, with yang = 1 and yin = 0:

| Code | Trigram | Image |
|---|---|---|
| 000 | Kun ☷ | Earth |
| 001 | Gen ☶ | Mountain |
| 010 | Kan ☵ | Water |
| 011 | Xun ☴ | Wind/Wood |
| 100 | Zhen ☳ | Thunder |
| 101 | Li ☲ | Fire |
| 110 | Dui ☱ | Lake |
| 111 | Qian ☰ | Heaven |

Thus 100 is Zhen (Thunder) and 011 is Xun (Wind/Wood). They are complementary line patterns, not two interchangeable notations for one trigram.

## 2. Golden evaluation of a trigram

Set \(\lambda=\varphi^{-1}\), so \(\lambda^2=1-\lambda\). For a trigram \(g=(d_0,d_1,d_2)\), with \(d_0\) the bottom line, define the research observable
\[
\pi_3(g)=d_0+d_1\lambda+d_2\lambda^2.
\]
Then
\[
\pi_3(100)=1=\lambda+\lambda^2=\pi_3(011).
\]
This is the exact golden collision Zhen/Xun. It is a collision of a chosen scalar evaluation, **not** an identity of I Ching states or line configurations.

The other six trigrams have distinct values, so the eight trigrams map to seven scalar values. The scalar projection loses one bit of state information.

## 3. Six lines: the 64 hexagrams and Q6

A hexagram is an ordered pair of lower and upper trigrams. Encode its six lines bottom-to-top by \(h=(d_0,\ldots,d_5)\in\{0,1\}^6\), with \((d_0,d_1,d_2)\) the lower trigram and \((d_3,d_4,d_5)\) the upper trigram.

Use the six-level golden observable
\[
\pi_6(h)=\sum_{k=0}^{5}d_k\lambda^k.
\]
All arithmetic can be done exactly in \(\mathbb Z[\lambda]\), using
\[
\lambda^0=(1,0),\;\lambda=(0,1),\;\lambda^2=(1,-1),\;
\lambda^3=(-1,2),\;\lambda^4=(2,-3),\;\lambda^5=(-3,5),
\]
where \((a,b)\) represents \(a+b\lambda\).

**Exact finite result:** the 64 hexagrams map to 33 distinct values under \(\pi_6\). This is a many-to-one observable, not a quotient of the hexagram state space that automatically respects dynamics.

The natural single-line-change graph is the 6-dimensional hypercube \(Q_6\): two hexagrams are adjacent exactly when one of their six lines is flipped. It has 64 vertices, degree 6, and 192 undirected edges. The simple random walk has transition matrix
\[
P(h,h')=\begin{cases}1/6,&d_H(h,h')=1,\\0,&\text{otherwise.}\end{cases}
\]
It is symmetric and doubly stochastic, hence its stationary distribution is uniform on the 64 hexagrams.

## 4. Crucial obstruction: the golden scalar classes are not Markov-lumpable

Let \(h\sim h'\) iff \(\pi_6(h)=\pi_6(h')\). A partition is strongly lumpable for the Q6 random walk only if any two states in the same class have the same total transition probability into every class.

The exact audit checks this condition using integer pairs in \(\mathbb Z[\lambda]\). It finds that the 33 scalar classes are **not** an equitable partition of Q6: 21 of the 33 classes contain states with different class-transition profiles.

Therefore:
- the 33 scalar values alone do not define a Markov chain inherited from the Q6 line-flip walk;
- one must retain the 64-state hexagram lift (or add sufficient memory/labels);
- a 33-state transfer matrix obtained by simply collapsing equal golden values would be mathematically invalid.

This is the correct I Ching formulation of the collision issue. A generic binary left shift is not substituted for the I Ching line-change dynamics.

## 5. A legitimate 64-state graph-directed golden measure

The Q6 random walk defines a stationary Markov chain \((H_n)_{n\ge0}\) on the 64 hexagrams with transition matrix \(P\) above. Let
\[
s(h)=\pi_6(h),\qquad
Y=\sum_{n=0}^{\infty}(\lambda^6)^n s(H_n).
\]
Since \(0<\lambda^6<1\) and \(s(h)\) is bounded, the series converges absolutely. This defines a Markov-coded self-similar probability measure, distinct in general from the i.i.d. Bernoulli convolution.

For each initial state \(i\), let \(\nu_i\) be the law of \(Y\) conditional on \(H_0=i\). The Markov property gives the exact vector graph-directed equation
\[
\nu_i=\sum_{j\in Q_6}P_{ij}\,(S_j)_\#\nu_j,
\qquad
S_j(x)=\lambda^6x+s(j).
\]
The stationary mixture is
\[
\nu=\frac1{64}\sum_{i\in Q_6}\nu_i.
\]
This is a well-defined 64-state transfer model. Its existence does not imply that \(\nu\) is singular, atomless, or full-support; those are separate analytical questions to be tested/proved.

For comparison, if each hexagram block is sampled independently and uniformly rather than by Q6 single-line transitions, the six bits in each block are i.i.d. Bernoulli(1/2), and the concatenated digits recover the usual 0/1 Bernoulli convolution coding. That independent-block process is **not** the Q6 random walk.

## 6. Cumulative coordinate and physical interpretation

If the stationary Markov-coded measure \(\nu\) is shown to be atomless and to have interval support, its CDF
\[
F_\nu(x)=\nu(( -\infty,x])
\]
is a strictly increasing continuous cumulative coordinate. If \(\nu\) is also singular with respect to Lebesgue measure, then \(F_\nu'=0\) almost everywhere. These conclusions are conditional: they are not inferred from the finite 64-state graph or the scalar collision count.

If a physical observable is later shown to have this measure as its spectral or spatial distribution, the cumulative coordinate can be interpreted accordingly. Until such a model-specific derivation exists, this is a mathematical construction, not a physical law.

## 7. Status

| Statement | Status |
|---|---|
| 100 = Zhen and 011 = Xun in bottom-to-top line convention | Definition/convention |
| \(\pi_3(100)=\pi_3(011)\) from \(1=\lambda+\lambda^2\) | Exact identity |
| Eight trigrams give seven scalar values | Exact finite calculation |
| 64 hexagrams, Q6 degree 6 and 192 edges | Exact combinatorics |
| Six-line golden evaluation has 33 distinct values | Exact finite calculation |
| Scalar partition is not strongly lumpable for Q6 (21 failing classes) | Exact finite calculation |
| 64-state Markov-coded measure and vector transfer equation | Defined model; analytic properties open |
| Atomlessness, full support, singularity of this Markov-coded measure | Open |
| Conjugacy with Minkowski question-mark dynamics | Open |
| Physical realization | Open |

## 8. Research questions

1. Determine the support and overlap structure of the 64-state graph-directed IFS.
2. Prove or disprove atomlessness and singularity of the stationary Markov-coded measure.
3. Determine whether the 64-state transfer operator admits a smaller exact representation retaining the required memory, rather than an invalid scalar quotient.
4. Compare the Markov-coded measure with the i.i.d. golden Bernoulli convolution using Fourier decay, local dimensions, and generalized dimensions.
5. Only after these steps, investigate whether its CDF conjugates a natural dynamical action to a simpler interval map.

## 9. Transfer spectrum and overlap audit

### 9.1 Exact spectrum of the Q6 transition matrix

For the simple line-flip walk, \(P=A(Q_6)/6\). The hypercube spectrum gives
\[
\operatorname{Spec}(P)=\left\{1-\frac{k}{3}: k=0,\ldots,6\right\},
\qquad
m_k=\binom{6}{k}.
\]
Thus the eigenvalues and multiplicities are
\[
1^{(1)},\;(2/3)^{(6)},\;(1/3)^{(15)},\;0^{(20)},
\;(-1/3)^{(15)},\;(-2/3)^{(6)},\;(-1)^{(1)}.
\]
The eigenvalue \(-1\) is the bipartite period-two mode: the walk alternates between even- and odd-parity hexagrams. The chain is irreducible with uniform stationary distribution, but it is not aperiodic. The usual one-sided gap from 1 to the next eigenvalue is \(1/3\); the absolute spectral gap is zero because of \(-1\). A lazy walk would remove this periodicity, but it is a different model and is not silently substituted here.

### 9.2 Fourier transfer matrix

With \(r=\lambda^6\), define
\[
f_i(\xi)=\mathbb E[e^{i\xi Y}\mid H_0=i].
\]
The conditional recursion is
\[
f_i(\xi)=\sum_jP_{ij}e^{i\xi s(j)}f_j(r\xi),
\qquad
f(\xi)=M(\xi)f(r\xi),
\]
where
\[
M(\xi)=P\,D(\xi),\qquad
D(\xi)=\operatorname{diag}(e^{i\xi s(j)}).
\]
Since \(D(\xi)\) is unitary, all singular values of \(M(\xi)\) equal those of \(P\). This is an exact norm statement, but it does **not** imply Fourier decay: the spectral radius and the iterated phase products still matter. At \(\xi=0\), \(M(0)=P\).

### 9.3 Exact translation overlaps and convex-hull diagnostics

The 64 translation states \(s(j)\) take 33 distinct exact values in \(\mathbb Z[\lambda]\), with multiplicities:
- 12 values occurring once;
- 12 values occurring twice;
- 8 values occurring three times;
- 1 value occurring four times.

The smallest gap between distinct translation values is exactly
\[
\min_{u\ne v}|s(u)-s(v)|=\lambda^6=r.
\]
This is a finite exact arithmetic statement. Equal translations are distinct hexagram states with different transition neighborhoods in general, which is why their future measures cannot be merged by scalar value alone.

For each state \(i\), the convex hull endpoints of its graph-directed support satisfy the Bellman equations
\[
L_i=\min_{j\sim i}(s(j)+rL_j),\qquad
U_i=\max_{j\sim i}(s(j)+rU_j).
\]
Iterating these contractions from zero gives monotone numerical endpoint approximations; the remaining error is bounded by a geometric tail of order \(r^{12}\) times the global range. At 12 iterations, the global endpoint estimates are approximately
\[
\min_iL_i\simeq0.0050406531,\qquad
\max_iU_i\simeq2.6129933357.
\]
At the first graph-directed level, 48 parent/child-pair convex-hull overlaps are detected across the 64 parent states. These are **convex-hull overlaps only**: they do not prove that the underlying compact support sets intersect, nor that the measure has interval support. The code reports them as diagnostics, not as a separation or intersection theorem.

### 9.4 Current mathematical conclusion

The Q6 transition spectrum is completely known, and the graph-directed Fourier recursion is explicit. The finite translation geometry has substantial exact coincidences and overlapping child hulls. None of these facts alone establishes atomlessness, singularity, absolute continuity, or multifractality of \(\nu\). The next analytical task is to study the matrix cocycle
\[
M(\xi)M(r\xi)\cdots M(r^{n-1}\xi)
\]
and the exact state-labelled overlap graph, retaining all 64 states (or proving a valid smaller automaton).
