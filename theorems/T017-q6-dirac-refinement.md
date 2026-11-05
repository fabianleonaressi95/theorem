# T017 — Cubical refinement of Q6 and the Dirac doubling audit

**Status:** exact finite-lattice identities proved below; numerical checks are reproducibility tests; continuum convergence is proved only for fixed physical momentum on the stated flat-torus refinement. This construction does **not** evade Nielsen–Ninomiya.

## 1. Definition of the refinement

Let
\[
Q_6=(C_2)^{\square 6}\cong \operatorname{Cay}(\mathbb Z_2^6,\{e_1,\ldots,e_6\}).
\]
For every integer \(n\geq 1\), define
\[
Q_{6,n}=(C_{2n})^{\square 6},\qquad
V_{6,n}=(\mathbb Z/(2n)\mathbb Z)^6,\qquad h_n=n^{-1}.
\]
Thus \(Q_{6,1}=Q_6\). The sequence is a sequence of six-dimensional periodic cubical lattices, not a claim that the original six-bit graph itself has a continuous momentum space. With physical side length \(2\), the vertices are \(x=h_n j\), and the allowed momenta are \(p_j=2\pi m_j/(2n)=\pi m_j/n\).

For \(n=1\), each coordinate translation satisfies \(T_j=T_j^{-1}\), so the centered difference vanishes exactly. For \(n\geq2\), it is generally nonzero.

## 2. Clifford representation and naive Dirac symbol

Choose Hermitian \(8\times8\) matrices \(\Gamma_1,\ldots,\Gamma_6\) satisfying
\[
\Gamma_j\Gamma_k+\Gamma_k\Gamma_j=2\delta_{jk}I_8.
\]
Such a representation exists because the complex irreducible Clifford representation in six Euclidean dimensions has dimension \(2^3=8\).

On lattice spinors define
\[
D_{n}^{\rm naive}
=\sum_{j=1}^6\Gamma_j\,\frac{T_j-T_j^{-1}}{2h_n}.
\]
It is anti-Hermitian. On a Fourier character of momentum \(p\), its symbol is
\[
D_n^{\rm naive}(p)
=\frac{i}{h_n}\sum_{j=1}^6\Gamma_j\sin p_j.
\]
The square is
\[
\big(D_n^{\rm naive}(p)\big)^2
=-\frac{1}{h_n^2}\sum_{j=1}^6\sin^2(p_j)\,I_8.
\]
Hence a zero occurs exactly when every \(p_j\in\{0,\pi\}\) modulo \(2\pi\). On every grid \(Q_{6,n}\), these are \(2^6=64\) distinct momentum corners. The Jacobian orientation at corner \(p^{(\epsilon)}_j=\pi\epsilon_j\) is
\[
\operatorname{sgn}\det\left[\frac{\partial(\sin p_j)}{\partial p_k}\right]_{p=p^{(\epsilon)}}
=\prod_{j=1}^6\cos(p_j)=(-1)^{\sum_j\epsilon_j}.
\]
There are \(\binom 6q\) corners with sign \((-1)^q\), and therefore
\[
\sum_{\epsilon\in\{0,1\}^6}(-1)^{|\epsilon|}
=\sum_{q=0}^6(-1)^q\binom6q=(1-1)^6=0.
\]
This is the exact lattice-corner cancellation for this six-dimensional symbol. It is a chirality-orientation proxy in even spatial dimension; it must not be relabelled as a four-dimensional physical Weyl-species count.

At \(n=1\), the only allowed momenta are \(p_j\in\{0,\pi\}\), so all 64 Fourier sectors are zeros of the centered operator. This is consistent with \(T_j=T_j^{-1}\). It is distinct from the forward-difference operator \(D_+=\sum_j\Gamma_j(T_j-I)\) audited in T016, whose only zero character is the trivial one.

## 3. Fixed-momentum continuum limit

Fix a physical momentum \(k\in\pi\mathbb Z^6\), the momentum lattice of the fixed side-length-2 torus, and choose \(p_n=h_n k\). This is an allowed lattice momentum for every sufficiently large \(n\). Then
\[
\frac{\sin(h_n k_j)}{h_n}\longrightarrow k_j,
\]
and, in operator norm on the finite-dimensional spin space,
\[
D_n^{\rm naive}(h_n k)\longrightarrow i\sum_{j=1}^6\Gamma_j k_j.
\]
More quantitatively, for fixed \(k\),
\[
\left\|D_n^{\rm naive}(h_n k)-i\Gamma\cdot k\right\|
\leq \sum_{j=1}^6\left|\frac{\sin(h_n k_j)}{h_n}-k_j\right|
\leq \frac{h_n^2}{6}\sum_{j=1}^6|k_j|^3,
\]
using \(|\sin t-t|\leq |t|^3/6\) and \(\|\Gamma_j\|=1\). This is a local symbol limit near the zero corner. It does not remove the other 63 corners, whose physical momenta escape to the ultraviolet as \(h_n\to0\).

## 4. Wilson modification

Let \(r>0\) and define the dimensionless Wilson scalar
\[
W_n(p)=\frac r{h_n}\sum_{j=1}^6(1-\cos p_j).
\]
The Wilson–Dirac symbol is
\[
D_n^{W}(p)=
\frac i{h_n}\sum_{j=1}^6\Gamma_j\sin p_j+W_n(p)I_8.
\]
At a corner \(p^{(\epsilon)}\), the naive kinetic term vanishes and
\[
W_n(p^{(\epsilon)})=\frac{2r}{h_n}|\epsilon|.
\]
Thus the origin corner is massless and the other 63 corners acquire positive Wilson masses. In this free symbol, \(D_n^W(p)\) can vanish only if both its scalar part and every sine component vanish; since \(W_n\geq0\), this happens only at \(p=0\).

Let \(\Gamma_* = i^3\Gamma_1\Gamma_2\cdots\Gamma_6\), with the phase chosen so that \(\Gamma_*^2=I\), \(\Gamma_*^\dagger=\Gamma_*\), and \(\{\Gamma_*,\Gamma_j\}=0\). Then
\[
\{\Gamma_*,D_n^W(p)\}=2W_n(p)\Gamma_*.
\]
The Wilson term therefore breaks the naive anticommutation with chirality at nonzero lattice spacing, except at the physical corner. This is the mechanism by which the unwanted corners are lifted; it is not an exact chiral, local, single-species regulator satisfying all the naive hypotheses simultaneously.

## 5. Results and proof status

### PROVED (within the definitions above)
1. \(Q_{6,1}=Q_6\), and the centered difference is zero at \(n=1\).
2. The naive symbol has exactly 64 zero corners on the continuous Brillouin torus and on every allowed finite momentum grid.
3. The corner orientation signs sum to zero.
4. The fixed-physical-momentum symbol converges to the continuum Euclidean Dirac symbol with an \(O(h_n^2|k|^3)\) bound.
5. The free Wilson symbol has exactly one zero corner for \(r>0\), and its Wilson term breaks the naive chiral anticommutation away from the origin.

### VERIFIED_NUMERICALLY
The companion script checks Clifford anticommutators, finite-grid corner counts, orientation balance, the \(n=1\) degeneracy, and the Wilson corner masses for several \(n\). The JSON report is generated by running the script; no numerical output is promoted to a proof.

### OPEN
- A physically relevant \(3+1\)-dimensional construction derived from the six-bit Q6 data. The present refinement is six-dimensional and is deliberately explicit about that mismatch.
- A proof of convergence of full resolvents/spectra and eigenvectors, not merely the fixed-momentum symbol.
- Gauge-covariant coupling, reflection positivity, and interacting continuum control.
- Any claim that a Q6-derived construction evades Nielsen–Ninomiya. No such claim follows here.

## 6. Interpretation

T017 establishes a controlled and falsifiable refinement model, but its result is conventional: the naive centered Dirac operator doubles, and the Wilson term lifts the extra corners by sacrificing the naive chiral anticommutation. The original finite Q6 graph is not itself a chiral continuum regulator. The distinction between this centered operator and T016's forward operator must be preserved in all subsequent comparisons.

## 7. References to verify against primary texts

- H. B. Nielsen and M. Ninomiya, *Absence of neutrinos on a lattice (I). Proof by homotopy theory*, Nucl. Phys. B 185 (1981), 20–40, DOI: 10.1016/0550-3213(81)90361-8.
- K. G. Wilson, *Quarks and strings on a lattice*, in *New Phenomena in Subnuclear Physics* (1977), 69–142. Full bibliographic metadata and exact equation/page mapping remain to be checked against the source edition.
- The present derivations are self-contained; these citations identify the historical context and are not claimed as page-verified transcriptions.
