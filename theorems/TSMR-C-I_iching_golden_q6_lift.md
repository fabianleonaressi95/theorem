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
Y=\sum_{n=1}^{\infty}(\lambda^6)^{n-1}s(H_n).
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
This is a well-defined 64-state transfer model. Its existence alone does not imply singularity or full support. Atomlessness is proved by the exact pair-automaton estimate in Section 11.

For comparison, if each hexagram block is sampled independently and uniformly rather than by Q6 single-line transitions, the six bits in each block are i.i.d. Bernoulli(1/2), and the concatenated digits recover the usual 0/1 Bernoulli convolution coding. That independent-block process is **not** the Q6 random walk.

## 6. Cumulative coordinate and physical interpretation

Since Section 11 proves atomlessness, if the stationary Markov-coded measure \(\nu\) is additionally shown to have interval support, its CDF
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
| Atomlessness of this Markov-coded measure | Proved in Section 11 by a positive almost-everywhere lower local-dimension bound |
| Full support and singularity of this Markov-coded measure | Open |
| Conjugacy with Minkowski question-mark dynamics | Open |
| Physical realization | Open |

## 8. Research questions

1. Determine the topology of the 64 component supports and whether their union has interval support.
2. Determine whether the stationary Markov-coded measure is singular or absolutely continuous.
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
The Q6 transition spectrum is completely known, and the graph-directed Fourier recursion is explicit. The finite translation geometry has substantial exact coincidences and overlapping child hulls. Those facts alone do not establish singularity, absolute continuity, or multifractality of \(\nu\); Section 11 gives a separate exact pair-automaton proof of atomlessness and a positive lower local-dimension bound. The remaining analytical task is to study the matrix cocycle
\[
M(\xi)M(r\xi)\cdots M(r^{n-1}\xi)
\]
and the exact state-labelled overlap graph, retaining all 64 states (or proving a valid smaller automaton).


## 10. State-labelled overlap graph and finite-depth Fourier audit

### 10.1 Labelled hull-overlap graph

The child associated with state \(j\) from parent \(i\) is allowed exactly when \(j\sim i\) in Q6. Its support is contained in the interval
\[
I_{i,j}=s(j)+r[L_j,U_j],\qquad r=\lambda^6,
\]
where \([L_j,U_j]\) is the convex hull of the state-conditioned support. Define a labelled overlap edge
\[
(i; j,k)
\]
when \(j,k\) are distinct Q6-neighbors of the same parent \(i\) and
\[
I_{i,j}\cap I_{i,k}\ne\varnothing.
\]
The edge retains all three hexagram labels. Its two line labels are the unique bottom-to-top line indices changed from parent to child.

Using 64 Bellman iterations in double precision, the diagnostic graph has:
- 48 labelled child-pair overlap edges;
- 40 of the 64 parent states carry at least one such edge;
- 32 parents carry one edge and 8 parents carry two edges;
- each edge joins two distinct one-line changes from its parent.

The smallest observed hull-overlap width is approximately \(2.06114\times10^{-3}\). The Bellman tail after 64 iterations is far smaller than this at the chosen contraction ratio, but the implementation uses floating-point arithmetic and is therefore a numerical diagnostic, not an exact algebraic certification. The graph is **not** the support-intersection graph: hull overlap is necessary for support intersection, but not sufficient.

### 10.2 Finite-depth Fourier observable

The code evaluates
\[
\widehat\nu_N(\xi)=
\frac1{64}\mathbf 1^T
M(\xi)M(r\xi)\cdots M(r^{N-1}\xi)\mathbf 1,
\]
which is the characteristic function of the truncated Markov-coded sum with the stationary initial distribution. At \(\xi=0\), it equals 1 exactly in the mathematical model. Numerical tests compare two truncation depths at a fixed frequency to check convergence of this finite-depth computation.

A sample at depth 80 gives the following magnitudes (rounded):
| \(\xi\) | \(|\widehat\nu_{80}(\xi)|\) |
|---:|---:|
| 1 | 0.79813 |
| 5 | 0.01173 |
| 10 | 0.03952 |
| 20 | 0.00712 |
| 50 | 0.06317 |
| 100 | 0.0000283 |
| 200 | 0.08511 |
| 500 | 0.06803 |
| 1000 | 0.00655 |

The irregular finite-frequency values do not establish decay as \(|\xi|\to\infty\). In particular, a sparse sample with small values cannot prove the Rajchman property or singularity. A rigorous Fourier conclusion requires uniform frequency estimates or a suitable theorem for this specific matrix cocycle.

### 10.3 Correct status of the analysis

The floating-point hull-overlap graph is a state-labelled diagnostic, and the finite-depth Fourier transform is computable and normalized. Section 11 subsequently replaces the bounded-difference part by an exact finite automaton and proves atomlessness. The following remain open:
1. exact certification of the hull-overlap inequalities in \(\mathbb Q(\sqrt5)\);
2. actual support intersections and the topology of the 64 component supports;
3. uniform Fourier decay or a non-decay subsequence;
4. absolute continuity, singularity, and the full local-dimension spectrum.

No multifractal or singular-measure conclusion is inferred from the current finite calculations.


## 11. Exact finite-type overlap automaton and dimension estimate

This section upgrades the floating-point hull-overlap diagnostic to an exact finite-state construction. It concerns the stationary Markov measure \(\nu\) defined in Section 5, with two independent copies of its Q6 coding.

### 11.1 Exact hull diameter

The Bellman operators
\[
(\mathcal L L)_i=\min_{j\sim i}(s(j)+rL_j),\qquad
(\mathcal U U)_i=\max_{j\sim i}(s(j)+rU_j)
\]
are contractions in the sup norm with factor \(r=\lambda^6\). Exact deterministic-policy iteration, followed by exact Bellman verification in \(\mathbb Q(\sqrt5)\), gives
\[
\min_i L_i=\frac7{40}-\frac{11}{40}\lambda,
\qquad
\max_i U_i=\frac{73}{40}+\frac{51}{40}\lambda.
\]
Consequently every component support is contained in a common interval of diameter
\[
D=\max_iU_i-\min_iL_i
=\frac{33}{20}+\frac{31}{20}\lambda.
\]
These are exact algebraic identities, not decimal endpoint fits.

### 11.2 Pair-difference automaton

Take two independent Q6 paths, with current states \(p,q\), and define the normalized prefix difference after \(n\) transitions by
\[
\delta_n=r^{-n}\sum_{t=1}^{n}r^{t-1}
\big(s(H_t)-s(H'_t)\big),\qquad \delta_0=0.
\]
Writing \(\delta_n=a+b\lambda\), its update under the next pair of transitions \(p\to j\), \(q\to k\) is
\[
\boxed{\quad
(p,q,\delta)\longrightarrow
\left(j,k,\frac{\delta+s(j)-s(k)}{r}\right),
\quad j\sim p,\ k\sim q.\quad}
\]
Since \(r^{-1}=13+8\lambda\), every difference remains in \(\mathbb Z[\lambda]\).

If the two coded points satisfy
\[
|Y-Y'|\le D r^n,
\]
then the tail difference is at most \(D\), and therefore
\[
|\delta_n|\le 2D.
\]
Under the conjugate embedding \(\lambda'=-\varphi\), the contraction becomes \(r'=\varphi^6>1\). The maximum conjugate translation difference is
\[
\max_{j,k}|s'(j)-s'(k)|
=\sum_{m=0}^{5}\varphi^m
=\varphi(\varphi^6-1),
\]
so every reachable prefix difference also satisfies
\[
|\delta_n'|\le\varphi.
\]
These two exact embedding bounds define the finite automaton: start from all 4096 states \((p,q,0)\), and retain exactly those transitions for which \(|\delta|\le2D\) and \(|\delta'|\le\varphi\). The bounds are checked by exact sign tests in \(\mathbb Q(\sqrt5)\), not floating-point tolerances.

The reachable automaton has:
- **5566** states \((p,q,a,b)\);
- **34762** directed transitions;
- exactly **13** distinct difference values:
\[
\begin{aligned}
\{&( -3,-2),(-3,-1),(-2,-2),(-2,-1),(-1,-1),(-1,0),\
 &(0,0),(1,0),(1,1),(2,1),(2,2),(3,1),(3,2)\},
\end{aligned}
\]
where each pair denotes \(a+b\lambda\).

This is an exact finite-state pair automaton for all close pairs at the scales used below. It does not assert that every retained state corresponds to an actual support intersection; it is a necessary-state enclosure, which is sufficient for the counting bound.

### 11.3 Exact path-count certificate

Let \(A\) be the integer adjacency matrix of this automaton, counting each ordered pair of allowed one-line transitions. The audit computes the maximum row sum of \(A^{20}\) using integer arithmetic:
\[
\boxed{\quad \|A^{20}\|_\infty
=9412274067081088.\quad}
\]
Thus, by submultiplicativity, the exponential growth rate of the number of admissible paired prefixes is at most
\[
\rho_*=
\left(9412274067081088\right)^{1/20}
\simeq 6.2904936491.
\]

For two independent stationary Q6 paths, each initial state pair has probability \(1/4096\), and each paired transition has probability \(1/36\). Every pair with \(|Y-Y'|\le Dr^n\) is represented by a path of length \(n\) in the automaton. Therefore, for a constant \(C_0<\infty\) independent of \(n\),
\[
(\nu\times\nu)\{|x-y|\le Dr^n\}
\le C_0\left(\frac{\rho_*}{36}\right)^n.
\]
The finite remainder classes modulo 20 are absorbed into \(C_0\).

### 11.4 Consequence for correlation and local dimensions

Define the lower correlation dimension by
\[
\underline D_2(\nu)=
\liminf_{\epsilon\downarrow0}
\frac{\log (\nu\times\nu)\{|x-y|\le\epsilon\}}
{\log\epsilon}.
\]
The path-count estimate yields the rigorous lower bound
\[
\boxed{
\underline D_2(\nu)\ge
\frac{\log\!\left(36/
(9412274067081088)^{1/20}\right)}
{\log(1/\lambda^6)}
\simeq 0.6041966.
}
\]
A geometric-scale Markov inequality and Borel--Cantelli argument then give, for \(\nu\)-almost every \(x\),
\[
\boxed{
\underline d_\nu(x):=
\liminf_{\epsilon\downarrow0}
\frac{\log\nu(B(x,\epsilon))}{\log\epsilon}
\ge 0.6041966.
}
\]
In particular, \(\nu\) is **atomless**: a positive-mass atom would have lower local dimension zero, contradicting the almost-everywhere positive bound.

This is a genuine dimension estimate derived from the exact finite automaton. It does **not** prove that the local dimension exists as a limit, that it is constant almost everywhere, or that the measure is absolutely continuous or singular. It also does not determine the full multifractal spectrum \(f(\alpha)\). Those questions remain open.

### 11.5 Reproducibility and status

Implementation: `audits/tsmr_c_iching_overlap_automaton.py`. Regression tests: `tests/test_tsmr_c_iching_overlap_automaton.py`.

| Claim | Status |
|---|---|
| Bellman hull extrema and global diameter in \(\mathbb Q(\sqrt5)\) | Exact algebraic computation with exact fixed-point verification |
| Pair-difference update and embedding bounds | Exact |
| 5566-state / 34762-transition automaton | Exact finite enumeration |
| \(\|A^{20}\|_\infty\) certificate | Exact integer computation |
| Lower correlation-dimension bound | Rigorous consequence of the automaton count |
| Almost-everywhere lower local-dimension bound | Rigorous consequence via Borel--Cantelli |
| Atomlessness of the stationary Markov measure | Proved by the positive local-dimension bound |
| Existence/constancy of exact local dimension; full multifractal spectrum | Open |
| Absolute continuity versus singularity | Open |
