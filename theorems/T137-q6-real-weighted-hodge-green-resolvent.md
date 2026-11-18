# T137 — Real weighted Hodge decomposition and Green resolvent on Q6

**Classification:** proved finite-dimensional theorem under the stated cubical-complex and positive-definiteness hypotheses. The concrete matrix implementation and numerical baseline remain to be audited. No Maxwell continuum limit or Kubo response is claimed.

**Dependencies:** T104 (Q6 cycle–cocycle–holonomy law); T105 (hexagram-resolved charge and circuit response). T104 is stated over \(\mathbb F_2\); this record separately constructs the real cochain complex and does not transfer ranks merely by changing coefficients.

## 1. Real cubical cochain complex

Let \(X=I^6\) be the full six-dimensional cubical complex and \(Q_6=X^{(1)}\) its 1-skeleton. Use the real cellular cochain complex
\[
C^0(X;\mathbb R)\xrightarrow{D_0}C^1(X;\mathbb R)
\xrightarrow{D_1}C^2(X;\mathbb R),
\]
with
\[
\dim C^0=64,\qquad \dim C^1=192,\qquad \dim C^2=240.
\]
Fix orientations of vertices, edges, and square faces, and use the corresponding signed incidence matrices
\[
D_0\in\mathbb R^{192\times64},\qquad
D_1\in\mathbb R^{240\times192}.
\]
The chain-complex identity is
\[
D_1D_0=0.
\]

Since \(X\) is contractible, its real cohomology vanishes in positive degrees. In particular,
\[
H^1(X;\mathbb R)=0,
\qquad
\ker D_1=\operatorname{im}D_0.
\]
The graph \(Q_6\) is connected, so \(\operatorname{rank}_{\mathbb R}D_0=64-1=63\). Exactness at \(C^1\) then gives
\[
\operatorname{rank}_{\mathbb R}D_1
=192-\dim\ker D_1
=192-63=129.
\]
These real-rank statements follow from the real cellular complex of the contractible cube, not from the \(\mathbb F_2\) rank computation in T104.

## 2. Positive weighted inner products and adjoints

Choose symmetric positive-definite matrices
\[
M_0\in\mathbb R^{64\times64},\quad
M_1\in\mathbb R^{192\times192},\quad
M_2\in\mathbb R^{240\times240}.
\]
They define inner products
\[
\langle x,y\rangle_{M_k}=x^TM_ky.
\]
The weighted adjoints are
\[
D_0^\dagger=M_0^{-1}D_0^TM_1,\qquad
D_1^\dagger=M_1^{-1}D_1^TM_2.
\]
Define the degree-one Hodge Laplacian as the map \(C^1\to C^1\)
\[
\boxed{\Delta_1=D_0D_0^\dagger+D_1^\dagger D_1.}
\]
Equivalently,
\[
\Delta_1=
M_1^{-1}D_0M_0^{-1}D_0^TM_1+
M_1^{-1}D_1^TM_2D_1.
\]

## 3. Theorem: weighted Hodge decomposition and absence of harmonic 1-cochains

Under the hypotheses above:

1. \(\Delta_1\) is self-adjoint in the \(M_1\) inner product:
   \[
   \langle u,\Delta_1v\rangle_{M_1}
   =\langle\Delta_1u,v\rangle_{M_1}.
   \]
2. \(M_1\Delta_1\) is symmetric positive semidefinite, and
   \[
   u^TM_1\Delta_1u
   =\|D_0^\dagger u\|_{M_0}^2+
     \|D_1u\|_{M_2}^2\ge0.
   \]
3. The harmonic 1-cochain space is zero:
   \[
   \ker\Delta_1=\ker D_0^\dagger\cap\ker D_1=\{0\}.
   \]
4. There is an \(M_1\)-orthogonal decomposition
   \[
   \boxed{
   C^1=
   \underbrace{\operatorname{im}D_0}_{63}
   \oplus_{M_1}
   \underbrace{\operatorname{im}D_1^\dagger}_{129}.
   }
   \]
5. The quotient \(C^1/\operatorname{im}D_0\) has dimension 129 and is identified with \(\operatorname{im}D_1^\dagger\) by taking the unique \(M_1\)-orthogonal representative of each class. This representative depends on the chosen inner product; the quotient dimension does not.

### Proof

For every \(u\in C^1\), the quadratic-form identity follows directly from the definitions of the weighted adjoints. If \(\Delta_1u=0\), positive definiteness of \(M_0,M_2\) implies \(D_0^\dagger u=0\) and \(D_1u=0\). Exactness gives \(u=D_0x\). Hence
\[
\|u\|_{M_1}^2
=\langle D_0x,u\rangle_{M_1}
=\langle x,D_0^\dagger u\rangle_{M_0}=0,
\]
so \(u=0\).

Moreover,
\[
\operatorname{im}D_1^\dagger
=(\ker D_1)^{\perp_{M_1}}
=(\operatorname{im}D_0)^{\perp_{M_1}}.
\]
The two subspaces therefore form an orthogonal direct sum. Their dimensions are
\[
\dim\operatorname{im}D_0=63,\qquad
\dim\operatorname{im}D_1^\dagger
=\operatorname{rank}D_1=129,
\]
which sum to 192. Orthogonal projection onto the second summand gives the unique representative of each quotient class. \(\square\)

## 4. Symmetric Euclidean representation and Green resolvent

The operator is self-adjoint in the weighted inner product, but its matrix need not be symmetric in the standard Euclidean inner product. Define
\[
\widetilde{\Delta}_1
=M_1^{1/2}\Delta_1M_1^{-1/2}.
\]
Then \(\widetilde{\Delta}_1\) is real symmetric positive definite and is similar to \(\Delta_1\). In particular, its eigenvalues are real and strictly positive.

For \(z\notin\sigma(\Delta_1)\), define the resolvent
\[
G_1(z)=(\Delta_1-zI)^{-1}.
\]
The equivalent symmetric representation is
\[
\boxed{
G_1(z)=M_1^{-1/2}
(\widetilde{\Delta}_1-zI)^{-1}M_1^{1/2}.
}
\]
Indeed,
\[
\Delta_1-zI
=M_1^{-1/2}(\widetilde{\Delta}_1-zI)M_1^{1/2}.
\]
The resolvent identity to be checked numerically is
\[
(\Delta_1-zI)G_1(z)-I=0.
\]

## 5. Reproducibility and acceptance tests

A concrete implementation must publish the orientation convention and the three mass matrices. The baseline \(M_0=M_1=M_2=I\) is a combinatorial reference case only; it is not, by itself, a physical metric or a Maxwell discretization.

Required checks:

| Check | Exact/theoretical target |
|---|---:|
| \(D_1D_0\) | zero matrix |
| \(\operatorname{rank}_{\mathbb R}D_0\) | 63 |
| \(\operatorname{rank}_{\mathbb R}D_1\) | 129 |
| \(M_k=M_k^T>0\) | all three degrees |
| \(M_1\Delta_1\) | symmetric positive definite |
| \(\widetilde\Delta_1\) | symmetric positive definite |
| Hodge summand dimensions | \(63+129=192\) |
| Weighted orthogonality | \(D_0^TM_1D_1^\dagger=0\) |
| Resolvent residual | \(\|(\Delta_1-zI)G_1(z)-I\|\) near roundoff |

The exact incidence identities and ranks should be certified with integer/rational linear algebra where possible. Floating-point eigensolvers are used for the weighted spectral and resolvent checks, not as substitutes for the exact rank proof. For nontrivial weights, report their construction, condition numbers, and sensitivity of the smallest eigenvalue.

## 6. Scope: what this theorem does not establish

- The 129-dimensional quotient is a gauge quotient of the real cochain space; it is not a 129-dimensional harmonic space.
- The weighted Hodge Laplacian is not automatically the Maxwell curl–curl operator.
- No continuum convergence follows from this finite-dimensional theorem.
- No physical coupling operator \(W\), resonator splitting, or linewidth is determined here.
- No Kubo susceptibility follows without a specified dynamics, state, perturbation, and observables.

The Maxwell bridge is a separate result: it must specify a geometric realization, compatible FEEC/Whitney spaces, material Hodge stars, boundary conditions, and convergence of discrete eigenspaces or resolvents. Kubo response is a further result after the physical dynamics and measurement protocol have been fixed.

## 7. Relation to T104 and T105

T104 establishes the finite topological cycle–cocycle structure over \(\mathbb F_2\). T137 separately proves the corresponding real weighted Hodge decomposition from the real cellular complex and positive-definite inner products. T105 supplies a distinct circuit/response framework. The three records must not be collapsed into a single physical claim.
