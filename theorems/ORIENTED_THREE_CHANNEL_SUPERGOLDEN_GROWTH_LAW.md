# Theorem — oriented three-channel supergolden growth law

**Status:** proved for the explicitly defined substitution system.  
**Geometric status:** its realization by Q6/PSU cells is open until the child-incidence rule is derived from an independently specified geometry.

## 1. Definition of the oriented substitution

Let the three channel types be \(A,B,C\). One refinement step replaces each parent by the following ordered multiset of children:
\[
A\mapsto A+B,\qquad B\mapsto C,\qquad C\mapsto A.
\]
Let \(v_n=(a_n,b_n,c_n)^T\in\mathbb N^3\) count the three types after \(n\) steps. With column-vector convention,
\[
v_{n+1}=Mv_n,\qquad
M=\begin{pmatrix}
1&0&1\\
1&0&0\\
0&1&0
\end{pmatrix}.
\]
The matrix is the incidence matrix of the substitution; it is not being inferred from Q6 geometry in this theorem.

## 2. Theorem

For every nonzero initial population \(v_0\in\mathbb N^3\), define the total number of objects
\[
N_n=\mathbf 1^T v_n=a_n+b_n+c_n.
\]
Then:

1. The population vector obeys the exact three-step law
   \[
   \boxed{v_{n+3}=v_{n+2}+v_n.}
   \]
2. The total count obeys the exact scalar recurrence
   \[
   \boxed{N_{n+3}=N_{n+2}+N_n.}
   \]
3. The growth rate is the supergolden number \(s\), the unique positive root of
   \[
   s^3-s^2-1=0:
   \qquad
   \boxed{\lim_{n\to\infty}\frac{N_{n+1}}{N_n}=s.}
   \]
4. The digamma converts this geometric counting growth into a logarithmic increment:
   \[
   \boxed{\lim_{n\to\infty}
   \bigl[\psi(N_{n+1})-\psi(N_n)\bigr]=\log s.}
   \]

The fourth statement is the analytic bridge: the supergolden growth factor is recovered as the exponential of the limiting digamma increment.

## 3. Proof

The characteristic polynomial of \(M\) is
\[
\det(\lambda I-M)=\lambda^3-\lambda^2-1.
\]
By Cayley–Hamilton,
\[
M^3-M^2-I=0,
\]
hence \(M^{n+3}=M^{n+2}+M^n\). Applying this identity to \(v_0\) proves the vector recurrence. Multiplication by \(\mathbf1^T\) proves the scalar recurrence.

The directed type graph is strongly connected and has a self-loop at \(A\); hence \(M\) is primitive. Perron–Frobenius therefore gives a simple positive dominant eigenvalue \(s\), strictly larger in modulus than the other eigenvalues, and positive right and left eigenvectors. For every nonzero nonnegative \(v_0\), the total count has a positive leading Perron coefficient. Thus
\[
N_n=C s^n(1+o(1)),\qquad C>0,
\]
and \(N_{n+1}/N_n\to s\).

Finally, \(N_n\to\infty\), and the digamma asymptotic formula gives
\[
\psi(x)=\log x-\frac{1}{2x}+O(x^{-2}).
\]
Therefore
\[
\begin{aligned}
\psi(N_{n+1})-\psi(N_n)
&=\log\!\left(\frac{N_{n+1}}{N_n}\right)+o(1)\\
&\longrightarrow \log s.
\end{aligned}
\]
This proves all four claims. \(\square\)

## 4. Perron weights and geometric interpretation

The right and left Perron eigenvectors can be normalized as
\[
r=\begin{pmatrix}1\\s^{-1}\\s^{-2}\end{pmatrix},
\qquad
\ell=\begin{pmatrix}1\\s^{-2}\\s^{-1}\end{pmatrix},
\]
so that \(Mr=sr\) and \(M^T\ell=s\ell\).

The right vector gives the asymptotic channel proportions. The left vector gives positive additive weights on parent types: the weighted population \(\ell^Tv_n\) is multiplied exactly by \(s\) at every refinement step. Interpreting these weights as physical lengths, areas, volumes, or energies requires a separately defined geometric measure and an additivity proof; this theorem does not assume such an interpretation.

## 5. Relation to the digamma reflection theorem

The growth law above and the reflection law
\[
\psi(1-x)-\psi(x)=\pi\cot(\pi x)
\]
are two different exact identities of the same special function:

- the reflection law classifies coefficients at fixed rational or algebraic-irrational arguments;
- the substitution theorem uses the digamma at integer population counts and extracts \(\log s\) from asymptotic growth.

They complement one another but are not the same identity. In particular, this theorem does not turn \(\log s\) into \(\pi\cot(\pi s)\).

## 6. Q6/PSU realization criterion

To promote this substitution law to a Q6/PSU geometric law, a construction must independently produce three oriented parent classes and prove the child-incidence table
\[
\begin{array}{c|ccc}
\text{parent}&A&B&C\\ \hline
\text{children}&A+B&C&A
\end{array}
\]
from actual cells, faces, seams, or tangent-channel incidences.

The construction must also:

1. define the three classes before counting children;
2. specify orientation and the Anti-Twin action on each class;
3. define quaternionic frame transport and prove equivariance;
4. verify boundary compatibility and avoid double-counting shared children;
5. enumerate children exactly and reproduce \(M\), up to a documented permutation of channel labels;
6. show the three-channel subspace is closed, or quantify the leakage if it is only approximately closed.

The midpoint subdivision T055 has directional transfer \(2I_3\), so it does not meet this criterion. The required oriented child list is not present in the audited Q6 material yet.

## 7. Epistemic classification

| Claim | Status |
|---|---|
| Exact substitution recurrence | **Proved** |
| Supergolden Perron growth rate | **Proved** |
| Limiting digamma increment \(\log s\) | **Proved** |
| Perron channel proportions and positive additive weights | **Proved** |
| Identification of the three abstract types with Q6 geometric cells | **Open** |
| Derivation of the substitution matrix from Anti-Twin/quaternionic geometry | **Open** |
| Physical interpretation of Perron weights | **Open** |

The theorem is therefore a rigorous growth-and-digamma law for the stated oriented substitution. It becomes a geometric RGS–PSU theorem only after the independent Q6 incidence construction in Section 6 is completed.
