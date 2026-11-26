# T109 — The dimension dependence of the Q_n influence bound

**Status:** proved exact identities; sharpness example proved; Aaronson–Ambainis dimension-free strengthening remains a separate theorem (not reproved here).

## 1. Conventions

Let \(Q_n\) be the graph on \(\{-1,1\}^n\), with an edge between \(x\) and \(x^{(i)}\), where \(x^{(i)}\) is obtained by flipping coordinate \(i\). Equip the cube with uniform probability measure. Write the Walsh expansion
\[
f(x)=\sum_{S\subseteq[n]}\widehat f(S)\chi_S(x),
\qquad \chi_S(x)=\prod_{i\in S}x_i.
\]
Define the squared-difference influence
\[
\mathcal I_i(f):=\mathbb E_x\bigl[(f(x)-f(x^{(i)}))^2\bigr].
\]
This convention is four times the frequently used Boolean influence
\(I_i(f)=\frac14\mathcal I_i(f)\) on the \(\{-1,1\}^n\) cube.

## 2. Exact theorem for every dimension

For every real-valued \(f\) on \(Q_n\),
\[
\boxed{\mathcal I_i(f)=4\sum_{S\ni i}\widehat f(S)^2.}
\]
Consequently,
\[
\boxed{\sum_{i=1}^n\mathcal I_i(f)
=4\sum_{S\ne\varnothing}|S|\widehat f(S)^2.}
\]
Since \(\operatorname{Var}(f)=\sum_{S\ne\varnothing}\widehat f(S)^2\), this gives
\[
4\operatorname{Var}(f)
\le \sum_i\mathcal I_i(f)
\le 4d\,\operatorname{Var}(f)
\quad\text{if }\deg(f)\le d,
\]
and, without a degree assumption,
\[
\boxed{\max_{1\le i\le n}\mathcal I_i(f)
\ge \frac4n\operatorname{Var}(f).}
\]

**Proof.** Flipping coordinate \(i\) changes \(\chi_S\) to \(-\chi_S\) exactly when \(i\in S\). Thus
\(f(x)-f(x^{(i)})=2\sum_{S\ni i}\widehat f(S)\chi_S(x)\).
Walsh orthonormality gives the first identity. Sum over \(i\), count each \(S\) exactly \(|S|\) times, and use \(1\le |S|\le d\) on the nonconstant Fourier support. The maximum bound follows by averaging. \(\square\)

## 3. Laplacian form

Let \(L_n=nI-A(Q_n)\) be the combinatorial graph Laplacian. The Walsh characters are eigenvectors:
\[
L_n\chi_S=2|S|\chi_S.
\]
Therefore
\[
\langle f,L_nf\rangle
=\frac12\sum_i\mathcal I_i(f)
=2\sum_{S\ne\varnothing}|S|\widehat f(S)^2.
\]
The spectral gap is \(2\), independently of \(n\). The degree-\(d\) upper bound above is the spectral-support estimate
\(\langle f,L_nf\rangle\le 2d\,\operatorname{Var}(f)\).

## 4. Sharp obstruction to a linear, dimension-free bound

Set
\[
f_n(x)=\frac1n\sum_{j=1}^n x_j.
\]
Then \(|f_n|\le1\), \(\deg(f_n)=1\),
\[
\operatorname{Var}(f_n)=\frac1n,\qquad
\mathcal I_i(f_n)=\frac4{n^2},\qquad
\frac{\max_i\mathcal I_i(f_n)}{\operatorname{Var}(f_n)}=\frac4n.
\]
Hence no positive constant \(c\), independent of \(n\), can make
\(\max_i\mathcal I_i(f)\ge c\,\operatorname{Var}(f)\)
hold for all bounded degree-one functions. This example does **not** contradict Aaronson–Ambainis: its influence is of order \(\operatorname{Var}(f_n)^2\), which is larger than a constant multiple of \(\operatorname{Var}(f_n)^{5/2}\).

## 5. What this does and does not establish

- **Proved:** Walsh influence identity, total-influence identity, degree-\(d\) upper bound on total influence, dimension-dependent lower bound, and the Laplacian spectral identities for every \(Q_n\).
- **Proved:** the linear-in-variance lower bound cannot be made dimension-free, even at degree one.
- **Not proved:** a dimension-free lower bound of the Aaronson–Ambainis form, such as
  \(\max_i I_i(f)\ge c\,\operatorname{Var}(f)^{5/2}/d^6\).
- **Research gap:** the exact identities control the *sum* of coordinate influences. A dimension-free theorem must add a genuinely degree-sensitive mechanism that prevents this total influence from being spread too evenly over arbitrarily many coordinates. The spectral gap alone cannot do that.

The recent preprint by D. Turturean, *A proof of the Aaronson–Ambainis conjecture*, arXiv:2611.09773 (6 November 2026), reports the dimension-free bound and a Lean formalization. This record does not claim an independent verification of that 60-page proof; it isolates the elementary \(Q_n\) identities and the precise point at which they stop.

## 6. Relation to T108 and Q6

For \(n=6\), the general estimate gives
\(\max_i\mathcal I_i(f)\ge(2/3)\operatorname{Var}(f)\), exactly the T108 bound. T109 is its dimension-general parent. The Q6 cubical cohomology statements in T108 are separate from this Fourier argument: graph cycle-space dimensions must not be identified with cubical cohomology.

## References

- D. Turturean, “A proof of the Aaronson–Ambainis conjecture,” arXiv:2611.09773, submitted 6 November 2026.
- S. Aaronson and A. Ambainis, “The Need for Structure in Quantum Speedups,” *Theory of Computing* 10 (2014), arXiv:0911.0996.
