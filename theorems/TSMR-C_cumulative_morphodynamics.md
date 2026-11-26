# TSMR-C — Cumulative morphodynamics and singular dynamical conjugacy

**Record type:** research programme / mathematical framework  
**Status:** core measure-theoretic statements are established; the golden Bernoulli application is conditional on the cited singularity and full-support results; a dynamical conjugacy for the golden overlap system is an open problem. No physical law is claimed.

## 1. Purpose

TSMR-C studies the change from a geometric coordinate to a cumulative-measure coordinate. It is motivated by the Minkowski question-mark function and by the distribution function of the golden Bernoulli convolution. The intended bridge is precise: a probability measure determines an order coordinate, and a dynamical system can be transported through that coordinate when the distribution function is a homeomorphism.

This is not an identification of the Minkowski measure with the golden Bernoulli measure. Their symbolic constructions and dynamical origins are different.

## 2. Cumulative coordinate

Let \(\mu\) be a Borel probability measure on a compact interval \([a,b]\), with no atoms, and define
\[
F_\mu(x)=\mu([a,x]),\qquad a\leq x\leq b.
\]
Then \(F_\mu\) is continuous and nondecreasing. It is strictly increasing exactly when every nonempty open subinterval of \([a,b]\) has positive \(\mu\)-mass, equivalently when \(\operatorname{supp}\mu=[a,b]\). With the endpoint convention \(F_\mu(a^-)=0\), \(F_\mu(b)=1\), it is then an order-preserving homeomorphism from \([a,b]\) onto \([0,1]\).

The probability integral transform gives
\[
(F_\mu)_\#\mu=\mathcal L^1\!\restriction_{[0,1]}.
\]
Thus \(u=F_\mu(x)\) is a uniform coordinate when \(x\) is sampled from \(\mu\). This does not mean that \(F_\mu\) is differentiable or absolutely continuous.

If \(\mu\perp\mathcal L^1\), then
\[
F_\mu'(x)=0\quad\text{for Lebesgue-a.e. }x.
\]
Consequently a continuous, strictly increasing, singular distribution function is possible: its total increase is carried by a singular measure rather than by an ordinary density. The Lebesgue–Stieltjes identity is \(dF_\mu=d\mu\).

## 3. Golden Bernoulli candidate

Let \(\lambda=\varphi^{-1}\), and let
\[
X_\lambda=\sum_{n=0}^{\infty}\varepsilon_n\lambda^n,
\qquad \mathbb P(\varepsilon_n=1)=\mathbb P(\varepsilon_n=-1)=\tfrac12.
\]
Its law \(\nu_\lambda\) satisfies
\[
\nu_\lambda=\tfrac12(S_+)_\#\nu_\lambda+
             \tfrac12(S_-)_\#\nu_\lambda,
\qquad S_\pm(x)=\lambda x\pm1.
\]
The support is \([-1/(1-\lambda),1/(1-\lambda)]\); since \(\lambda>1/2\), this is an interval, and at \(\lambda=\varphi^{-1}\) its endpoints are \(\pm\varphi^2\).

The reciprocal of a Pisot number is a classical singularity parameter for symmetric Bernoulli convolutions (Erdős, 1939). For this parameter, the intended cumulative function is
\[
F_\varphi(x)=\nu_{\varphi^{-1}}(( -\infty,x]).
\]
Subject to the non-atomicity and full-support properties above, \(F_\varphi\) is a strictly increasing continuous singular homeomorphism from \([-\varphi^2,\varphi^2]\) to \([0,1]\), with derivative zero almost everywhere.

**Important distinction:** full support gives strict increase; singularity gives derivative zero almost everywhere. Neither property implies the other. The support interval alone does not prove singularity. The golden measure's singularity is a theorem about its Fourier/arithmetic structure, not a consequence of the support calculation.

The Fourier transform is
\[
\widehat\nu_\lambda(\xi)=
\prod_{n=0}^{\infty}\cos(\lambda^n\xi).
\]
For \(\lambda=1/2\), by contrast, the law is uniform on \([-2,2]\) and its CDF is affine there. This is a useful control case, not the golden case.

## 4. Comparison with Minkowski's question-mark function

The Minkowski function \(?(x)\) is another continuous strictly increasing singular homeomorphism of an interval. Its construction is tied to continued fractions/Farey structure and to a change of symbolic coding; it is not the CDF of the golden Bernoulli convolution.

The valid analogy is structural:
- both maps preserve order and are singular;
- both convert a non-uniform geometric parametrization into a cumulative coordinate;
- both are connected to symbolic/dynamical descriptions.

The stronger statement that \(F_\varphi\) conjugates a particular golden IFS map to a tent, Farey, or finite-state map is **not established here**. It requires an explicit map, a verified invariant measure, and an identity of the form below.

## 5. Transporting dynamics

Let \(T:[a,b]\to[a,b]\) be a map and assume \(F_\mu\) is a homeomorphism. Define
\[
\widetilde T=F_\mu\circ T\circ F_\mu^{-1}:[0,1]\to[0,1].
\]
Then, by construction,
\[
F_\mu\circ T=\widetilde T\circ F_\mu.
\]
This is a topological conjugacy, not an additional dynamical theorem. It preserves orbit structure and topological invariants, but generally does not preserve metric quantities such as derivatives, Lyapunov exponents, or Euclidean distances.

If \(T_\#\mu=\mu\), then \(\widetilde T\) preserves Lebesgue measure:
\[
\widetilde T_\#\mathcal L^1=\mathcal L^1.
\]
This follows from \((F_\mu)_\#\mu=\mathcal L^1\). It is the cleanest rigorous bridge from a singular invariant measure to a uniform coordinate.

For an IFS with overlaps, the random branch process is not automatically a single deterministic map \(T\). A deterministic skew-product or a symbolic extension may be needed. The five-cell Markov partition and the proposed 2x2 transfer matrices remain separate candidates until their transition rules are proved.

## 6. Physical interpretation: what is and is not obtained

For a spectral measure \(\mu\), the integrated density of states or cumulative spectral distribution has the same mathematical form \(N(E)=\mu(( -\infty,E])\). Singular continuous spectral measures can therefore produce continuous but non-absolutely-continuous cumulative functions. This is a legitimate mathematical setting in spectral theory.

Likewise, multifractal measures associated with critical quantum states can be studied through partition sums and generalized dimensions. TSMR-C supplies a coordinate transformation for such measures; it does not explain or predict a quantum spectrum by itself.

The physical bridge requires a model-specific derivation of:
1. the observable whose measure is \(\mu\) (spectral, spatial, transport, or another measure);
2. the physical dynamics \(T\) and its invariance relation \(T_\#\mu=\mu\), if applicable;
3. the measured scaling exponents and their stability under refinement;
4. the relation, if any, between the transformed dynamics and a physical operator.

No claim about quantum gravity, a new force, or a universal physical law follows from singularity alone.

## 7. Propositions and open problems

**Proposition C1 (cumulative-coordinate theorem; established).** If \(\mu\) is atomless with full support on \([a,b]\), then \(F_\mu\) is an increasing homeomorphism onto \([0,1]\) and pushes \(\mu\) to Lebesgue measure.

**Proposition C2 (singular derivative; established).** If additionally \(\mu\perp\mathcal L^1\), then \(F_\mu'=0\) Lebesgue-almost everywhere.

**Proposition C3 (conjugacy transport; established).** If \(F_\mu\) is a homeomorphism, then \(\widetilde T=F_\mu T F_\mu^{-1}\) is topologically conjugate to \(T\). If also \(T_\#\mu=\mu\), then \(\widetilde T\) preserves Lebesgue measure.

**Open problem C4 (golden finite-state model).** Construct and prove a deterministic or symbolic-extension dynamics for the golden Bernoulli convolution whose cumulative-coordinate conjugate has an explicit finite-state description. The proposed 5-cell partition and 2x2 transfer representation are not assumed.

**Open problem C5 (Minkowski comparison).** Determine whether a useful semiconjugacy, conjugacy, or renormalization relation exists between the golden cumulative map and the continued-fraction/Farey coding underlying \(?(x)\). Similarity of singularity properties is not sufficient.

**Open problem C6 (physical realization).** Identify a concrete spectral or transport model whose invariant measure is the golden Bernoulli measure, or a rigorously controlled approximation to it. Without this, the connection remains a mathematical framework and analogy.

## 8. Classification

| Component | Status |
|---|---|
| Cumulative-coordinate and probability-integral-transform statements | Established theorem |
| Derivative-zero conclusion for singular measures | Established theorem |
| Golden Bernoulli support interval | Established support calculation |
| Golden Bernoulli singularity | Established classical result for reciprocal Pisot parameters; cite Erdős |
| Full-support + atomlessness implication for strict CDF increase | Established theorem; verify atomlessness for the chosen measure in any formal proof |
| Minkowski structural analogy | Established qualitative comparison |
| Golden finite-state conjugacy | Open |
| Five-cell Markov partition / 2x2 transfer matrices | Candidate, unverified |
| Physical realization in an RGS/quantum model | Open |

## References

- P. Erdős, “On a family of symmetric Bernoulli convolutions,” *American Journal of Mathematics* **61** (1939), 974–976.
- J. W. S. Cassels, *An Introduction to Diophantine Approximation*, Cambridge University Press, 1957 — background on Pisot numbers and algebraic approximation.
- For the Minkowski question-mark function, use the classical continued-fraction/Farey literature; a dedicated bibliography entry should be added after the exact conjugacy convention and normalization are fixed.
