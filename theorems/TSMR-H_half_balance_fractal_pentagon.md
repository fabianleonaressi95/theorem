# TSMR-H — The half-balance principle: Bernoulli overlap, entropy, and the pentagonal projector

**Record type:** exact structural theorem plus explicitly conditional cross-model identification  
**Status:** the binary overlap threshold, entropy maximizer, and pentagonal projection identities are proved below. Their common scalar balance parameter is exact once identified. A canonical operator intertwining or a physical De Aquino coupling is **not** established.

## 1. Two-branch Bernoulli geometry

Fix \(0<\lambda<1\) and the two affine contractions
\[
S_-(x)=\lambda x-1,\qquad S_+(x)=\lambda x+1.
\]
Their compact invariant set is the interval
\[
K_\lambda=[-R_\lambda,R_\lambda],\qquad R_\lambda=\frac1{1-\lambda}.
\]
Indeed, \(S_-(K_\lambda)\cup S_+(K_\lambda)=K_\lambda\). The two first-level images are
\[
S_-(K_\lambda)=[-1-\lambda R_\lambda,-1+\lambda R_\lambda],\quad
S_+(K_\lambda)=[1-\lambda R_\lambda,1+\lambda R_\lambda].
\]
The signed gap between them is therefore
\[
g(\lambda)=2-2\lambda R_\lambda
=\frac{2(1-2\lambda)}{1-\lambda}.
\]

**Theorem H1 (binary separation threshold).**
- If \(0<\lambda<1/2\), the first-level pieces are disjoint and separated by \(g(\lambda)>0\).
- If \(\lambda=1/2\), they touch at one endpoint: \(g(\lambda)=0\).
- If \(1/2<\lambda<1\), they overlap, with overlap length \(-g(\lambda)>0\).

Thus \(\lambda=1/2\) is the exact geometric transition from separated to overlapping first-level branches. This is a statement about the IFS geometry; it does **not** by itself determine absolute continuity or singularity of the invariant measure.

For the symmetric Bernoulli convolution
\[
\nu_{p,\lambda}=\operatorname{Law}\!\left(\sum_{n=0}^{\infty}\varepsilon_n\lambda^n\right),
\quad
\mathbb P(\varepsilon_n=+1)=p,\quad
\mathbb P(\varepsilon_n=-1)=1-p,
\]
the parameter \(p\) specifies branch probabilities, whereas \(\lambda\) specifies geometric contraction. They are independent parameters. In particular, at \(p=\lambda=1/2\), the measure is uniform on \([-2,2]\). The critical geometric value \(1/2\) is therefore not, by itself, a singular-fractal measure.

## 2. The probability half: maximum binary entropy

The binary Shannon entropy is
\[
h(p)=-p\log p-(1-p)\log(1-p),\qquad 0<p<1.
\]
It satisfies
\[
h'(p)=\log\frac{1-p}{p},\qquad
h''(p)=-\frac1p-\frac1{1-p}<0.
\]
Hence \(h\) has a unique global maximum at
\[
p=\frac12,\qquad h(1/2)=\log 2.
\]
This is the equal-weight Bernoulli point. It is a probability/entropy statement, not the geometric separation theorem H1.

## 3. The pentagonal half: an orthogonal projection

Let \(E\in\mathbb R^{2\times5}\) have columns
\[
e_j=(\cos(2\pi j/5),\sin(2\pi j/5))^T,\qquad j=0,\ldots,4.
\]
Then
\[
EE^T=\frac52 I_2,\qquad G_5=E^TE,\qquad
P=\frac25E^TE.
\]
Consequently \(P=P^T=P^2\) and \(\operatorname{rank}P=2\): it is the orthogonal projector onto the pentagonal frame plane in \(\mathbb R^5\).

For a unit vector \(q\in\mathbb R^5\), put
\[
x=\|Pq\|^2,\qquad \|(I-P)q\|^2=1-x.
\]
The symmetric mixing functional
\[
B(x)=x(1-x)
\]
has the unique maximum \(B(1/2)=1/4\), since
\[
B(x)=\frac14-(x-\tfrac12)^2.
\]
Therefore the balanced pentagonal state is characterized by
\[
\boxed{\|Pq\|^2=\|(I-P)q\|^2=\frac12.}
\]
Moreover,
\[
q^TG_5q=\frac52\|Pq\|^2,
\]
so at balance
\[
\boxed{q^TG_5q=\frac54.}
\]

This is a variational selection **for the stated symmetric mixing functional**. The regular pentagon alone does not force an arbitrary unit vector \(q\) to be balanced.

## 4. Exact common scalar principle — and its limit

The entropy \(h(t)\) and the quadratic mixing functional \(B(t)=t(1-t)\) are different functions, but both are strictly concave, invariant under \(t\leftrightarrow1-t\), and uniquely maximized at \(t=1/2\). If the pentagonal active norm is used as a channel probability,
\[
p_q:=\|Pq\|^2,
\]
then the induced binary entropy \(h(p_q)\) and the pentagonal mixing \(B(p_q)\) are simultaneously maximized precisely when
\[
p_q=\frac12.
\]

This gives an exact common **balance coordinate** linking equal Bernoulli weights and equal pentagonal norm shares. It does not identify the full Bernoulli measure with the pentagonal projector, and it does not identify the contraction ratio \(\lambda\) with \(p_q\). Setting \(p=\lambda=p_q=1/2\) defines a special diagonal submodel; it is not a theorem about all Bernoulli convolutions.

## 5. Golden Bernoulli regime: why the fractal survives beyond the threshold

For
\[
\lambda_g=\varphi^{-1}=\frac{\sqrt5-1}{2},
\qquad \lambda_g^2+\lambda_g=1,
\]
one has \(\lambda_g>1/2\). Thus the two IFS pieces overlap and the attractor is an interval. Nevertheless, the equal-weight golden Bernoulli convolution is singular: the inverse golden ratio is a Pisot number, and the arithmetic overlaps produce a singular measure. Its support geometry is interval-like while its measure remains fractal/singular.

This distinction is essential:
- \(\lambda=1/2\), \(p=1/2\): uniform measure on an interval;
- \(\lambda=\varphi^{-1}>1/2\), \(p=1/2\): overlapping branches and a singular golden Bernoulli measure.

The fractal object here is the measure and its scaling/entropy structure, not necessarily a disconnected support.

The golden algebra also gives
\[
\varphi=\frac12+\frac{\sqrt5}{2}.
\]
In the De Aquino model recorded in the companion audit, the zero of \(m_g/m_i=3-2\sqrt{1+\xi^2}\) occurs at \(\xi_*^2=5/4\), hence \(|\xi_*|=\sqrt5/2\). This is an exact algebraic identity within that model. Together with the pentagonal identity \(q^TG_5q=5/4\), it gives a common numerical threshold. A physical identification of \(\xi_*\) with \(q^TG_5q\), or a derivation of its scale from an action, remains conditional/open.

## 6. Relation to singular cumulative coordinates and Minkowski's question-mark function

For an atomless probability measure \(\mu\) with full interval support, its cumulative distribution function \(F_\mu\) is continuous and strictly increasing. If \(\mu\) is singular with respect to Lebesgue measure, then \(F_\mu'=0\) almost everywhere. The golden Bernoulli measure supplies a singular-measure example; Minkowski's question-mark function is another strictly increasing singular distribution function arising from a different arithmetic construction.

The shared regularity class motivates a comparison of cumulative-coordinate dynamics. It does **not** imply equality of the two functions, equality of their measures, or a conjugacy between their underlying dynamics. The precise cumulative-coordinate results and their hypotheses are recorded in [TSMR-C](TSMR-C_cumulative_morphodynamics.md).

## 7. Classification and open bridge

**Proved here:** the first-level overlap threshold \(g(\lambda)\); the unique entropy maximizer \(p=1/2\); the pentagonal projector identity; the unique maximizer of \(x(1-x)\); and the equivalence \(q^TG_5q=5/4\iff\|Pq\|^2=1/2\) for unit \(q\).

**Established background result:** singularity of the equal-weight golden Bernoulli convolution at \(\lambda=\varphi^{-1}\), despite interval support.

**Conditional identification:** treating \(\|Pq\|^2\) as a Bernoulli channel probability, or identifying the pentagonal quadratic form with De Aquino's dimensionless \(\xi^2\).

**Open:** construct a measure/operator map from the Bernoulli symbolic system to the pentagonal frame; derive the coupling and physical normalization from one action; determine whether a finite-state or graph-directed model tied to Q6 preserves the singular measure and its multifractal spectrum. No such intertwiner or physical derivation is claimed here.

## References

- P. Erdős, “On a family of symmetric Bernoulli convolutions,” *Amer. J. Math.* 61 (1939), 974–976.
- J. C. Alexander and D. Zagier, “The Entropy of a Certain Infinitely Convolved Bernoulli Measure,” *J. London Math. Soc.* 44 (1991), 121–134. DOI: [10.1112/jlms/s2-44.1.121](https://doi.org/10.1112/jlms/s2-44.1.121).
- Y. Peres, W. Schlag, and B. Solomyak, “Sixty Years of Bernoulli Convolutions,” survey.
- F. De Aquino, “Correlation Between Gravitational and Inertial Mass: Theory and Experimental Test” (2002), arXiv:physics/0205089; cited as a model proposal, not accepted physical law.
