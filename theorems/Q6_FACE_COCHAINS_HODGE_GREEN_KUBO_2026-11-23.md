# Q6: closed face cochains, Hodge dynamics, and a Green–Kubo functional

**Date:** 2026-11-23  
**Status:** exact finite cubical definitions and operator identities; OU/Green–Kubo formula proved for the declared model; physical stress interpretation open.

## 1. Purpose and scope

This note constructs the face-level analogue of the vertex-space Green–Kubo calculation. It uses only the standard cubical 2-skeleton of the six-dimensional cube, its integer incidence matrices, the Euclidean cell inner products, and a specified reversible linear stochastic dynamics.

It does **not** identify the resulting observable with physical shear stress or viscosity. That requires a metric-dependent action, a physical stress tensor, units, and a constitutive interpretation. It also does not identify this face operator with the vertex graph Laplacian.

## 2. The cubical complex and its incidence matrices

Let (I^6=[0,1]^6) with its standard cubical cell structure. A (k)-cell is specified by:
- a set (S={i_1<cdots<i_k}subset{1,ldots,6}) of free coordinate directions;
- a binary assignment (epsilonin{0,1}^{S^c}) of the fixed coordinates.

The number of (k)-cells is
[
N_k=\binom 6k 2^{6-k}.
]
In particular,
[
(N_0,N_1,N_2,N_3)=(64,192,240,160).
]

Orient each cell by its increasing list of free coordinate axes. For a (k)-cell (c=(S,\epsilon)), its boundary is
[
\partial_k c
=\sum_{r=1}^k(-1)^{r-1}
\big(c_{i_r=1}-c_{i_r=0}\big),
]
where the two ((k-1))-faces are obtained by fixing the formerly free coordinate (i_r) to 1 or 0, respectively, and retaining the induced increasing orientation.

Let (B_k) be the matrix of (partial_k:C_k\to C_{k-1}) in these oriented cell bases. Thus
[
B_1\in\mathbb Z^{64\times192},\quad
B_2\in\mathbb Z^{192\times240},\quad
B_3\in\mathbb Z^{240\times160}.
]
The cubical boundary identity gives the exact integer relations
[
B_1B_2=0,\qquad B_2B_3=0.
]
The cell bases are declared orthonormal; this fixes the inner products used below. A different weighted/geometric inner product would change adjoints and projectors and must be specified separately.

## 3. Closed 2-cochains and the projector

A real 2-cochain is a vector (\Omega\in C^2=\mathbb R^{240}), with one component per square face. The coboundary (d^2:C^2\to C^3) is represented by (B_3^T). Hence the closed face-cochain space is
[
Z^2=\ker B_3^T\subset\mathbb R^{240}.
]

The orthogonal projector onto (\operatorname{im}B_3\) is
[
P_{\operatorname{im}B_3}
=B_3(B_3^TB_3)^+B_3^T,
]
where (+\) denotes the Moore–Penrose pseudoinverse. Therefore
[
\boxed{P_{\rm cl}
=I_{240}-B_3(B_3^TB_3)^+B_3^T}
]
is the orthogonal projector onto (Z^2=(\operatorname{im}B_3)^\perp).

The six-cube is contractible, so its cellular homology and cohomology vanish in positive degree. The exact ranks are
[
\operatorname{rank}B_1=63,\qquad
\operatorname{rank}B_2=129,\qquad
\operatorname{rank}B_3=111.
]
Consequently
[
\dim Z^2=240-111=129,
\qquad \operatorname{rank}P_{\rm cl}=129.
]
This 129-dimensional closed-cochain space is not the second cohomology: (H^2=0). In fact, every closed 2-cochain is exact on the cube, (Z^2=\operatorname{im}B_2^T). The projector selects closed cochains, not harmonic representatives.

## 4. The face Hodge Laplacian and its restriction

With the declared Euclidean inner products, the degree-2 combinatorial Hodge Laplacian is
[
\boxed{\Delta_2=B_2^TB_2+B_3B_3^T
\in\mathbb R^{240\times240}.}
]
It is symmetric and positive semidefinite:
[
\langle\Omega,\Delta_2\Omega\rangle
=\|B_2\Omega\|^2+\|B_3^T\Omega\|^2\geq0.
]

The closed subspace (Z^2) is invariant under (\Delta_2). Indeed, for (\Omega\in Z^2),
[
B_3^T\Delta_2\Omega
=B_3^TB_2^TB_2\Omega+B_3^TB_3B_3^T\Omega
=(B_2B_3)^TB_2\Omega=0.
]
Moreover, on (Z^2),
[
\Delta_2\Omega=B_2^TB_2\Omega.
]
Since the cube has (H^2=0), the restricted operator
[
A:=\Delta_2|_{Z^2}:Z^2\to Z^2
]
is positive definite. If (A\Omega=0) and (\Omega\in Z^2), then (B_2\Omega=0) and (B_3^T\Omega=0), so (\Omega) is harmonic; contractibility forces (\Omega=0).

Thus (A) is a finite-dimensional, self-adjoint, strictly positive operator on a 129-dimensional Hilbert space.

### 4.1 Exact spectrum on the closed 2-cochain sector

The cubical cochain complex of (I^6) is the tensor product of six copies of the interval complex. On one factor, the degree-0 Hodge Laplacian has eigenvalues 0 and 2, each simple, while the degree-1 Hodge Laplacian is the scalar 2. The product Hodge Laplacian is the sum of the six factor Laplacians.

For degree p, choose the p coordinates carrying 1-cochains. The remaining 6-p coordinates contribute either the degree-0 eigenvalue 0 or 2. Therefore the full degree-p Hodge spectrum is
\[
m_p(2(p+j))=\binom 6p\binom{6-p}{j},\qquad j=0,\ldots,6-p.
\]
For p=1, this gives multiplicities 6, 30, 60, 60, 30, 6 at eigenvalues 2, 4, 6, 8, 10, 12. For p=0, the multiplicities at 2, 4, 6, 8, 10, 12 are 6, 15, 20, 15, 6, 1.

Because the cube is contractible, there are no harmonic cochains in positive degree. At each positive eigenvalue, the differential identifies the coexact degree-1 eigenspace with the exact degree-2 eigenspace. Hence the multiplicity of the exact degree-2 sector is
\[
m_{2,\mathrm{exact}}(\lambda)=m_1(\lambda)-m_0(\lambda).
\]
Since Z^2=ker B_3^T=im B_2^T, this is precisely the spectrum of A=Delta_2 restricted to Z^2:
\[
\boxed{
\begin{array}{c|rrrrr}
\lambda&4&6&8&10&12\\
\operatorname{mult}_{Z^2}(\lambda)&15&40&45&24&5
\end{array}}
\]
The multiplicities sum to 129, as required. This is an exact tensor-product derivation, not a floating-point diagonalization.

## 5. A declared reversible OU dynamics on closed face cochains

This section makes a model choice. Let (\gamma>0), (\sigma^2>0), and let (W_t) be standard Brownian motion on (Z^2). Define
[
d\Omega_t=-\gamma A\Omega_t\,dt
+\sqrt{2\gamma\sigma^2A}\,dW_t,
\qquad \Omega_t\in Z^2.
]
The square root is the unique positive square root on (Z^2). Since (A) is positive definite, this OU process is non-degenerate on the closed-cochain space and has the unique invariant Gaussian covariance
[
\Sigma=\sigma^2 I_{Z^2}.
]
Its generator is reversible with respect to that Gaussian measure. The constant face-cochain directions are not a separate zero-mode sector here: the state space has already been restricted to (Z^2), and (A) has no kernel on it.

This is a mathematically well-defined test dynamics. It is not yet derived from the full nonlinear curvature model, from microscopic Q6 dynamics, or from a measured mobility.

## 6. Face observables and the Green–Kubo formula

Choose a fixed (b\in Z^2) and define the linear face observable
[
J_b(t)=\langle b,\Omega_t\rangle.
]
At stationarity,
[
C_b(t)=\mathbb E[J_b(t)J_b(0)]
=\sigma^2\langle b,e^{-\gamma At}b\rangle.
]
Let (\Pi_\lambda) be the orthogonal projector onto the eigenspace of (A) with eigenvalue (\lambda>0). The spectral theorem gives
[
C_b(t)=\sigma^2\sum_{\lambda\in\operatorname{spec}(A)}
e^{-\gamma\lambda t}\,\|\Pi_\lambda b\|^2.
]
Integrating term by term (a finite sum),
[
\boxed{
\mathcal G_{\rm face}(b)
=\int_0^\infty C_b(t)\,dt
=\frac{\sigma^2}{\gamma}
\sum_{\lambda\in\operatorname{spec}(A)}
\frac{\|\Pi_\lambda b\|^2}{\lambda}.
}
]
This is the exact Green–Kubo functional for the declared OU process. The factor is (1/(\gamma\lambda)), not (1/(2\gamma\lambda)), because the relaxation eigenvalue here is denoted (\lambda) directly; in the vertex (Q_n) calculation the eigenvalues were (2k), giving (1/(2\gamma k)).

### 6.1 Isotropic unit-vector average

If (b) is uniformly distributed on the unit sphere of the 129-dimensional space (Z^2), and (m_\lambda=\operatorname{rank}\Pi_\lambda), then
[
\mathbb E\|\Pi_\lambda b\|^2=\frac{m_\lambda}{129}.
]
Therefore
[
\boxed{
\mathbb E\mathcal G_{\rm face}(b)
=\frac{\sigma^2}{129\gamma}
\sum_{\lambda\in\operatorname{spec}(A)}
\frac{m_\lambda}{\lambda}.
}
]
Using the exact multiplicities above,
\[
\sum_{\lambda}\frac{m_\lambda}{\lambda}
=\frac{15}{4}+\frac{40}{6}+\frac{45}{8}
+\frac{24}{10}+\frac{5}{12}
=\frac{2263}{120}.
\]
Therefore the exact isotropic Green--Kubo mean is
\[
\boxed{
\mathbb E\mathcal G_{\rm face}
=\frac{\sigma^2}{129\gamma}\,\frac{2263}{120}
=\frac{2263\sigma^2}{15480\gamma}.
\]
This value belongs to the declared OU model and the unit-sphere ensemble on Z^2; it is not yet a physical viscosity.

## 7. Relation to the Q6 cosine-curvature functional

For face phases (\Omega_p\), the dimensionless curvature functional recorded in the Q6 work is
[
\mathcal F(\Omega)=\sum_{p=1}^{240}(1-\cos\Omega_p).
]
Near the flat configuration (\Omega=0),
[
\mathcal F(\Omega)
=\frac12\|\Omega\|^2+O(\|\Omega\|^4).
]
Restricting to (Z^2), the Hessian at zero is the identity on (Z^2). This supports a local harmonic approximation of the face-phase energy.

The OU drift above uses (A) as a chosen positive mobility/relaxation operator, with the quadratic approximation to (\mathcal F) as the local energy. This is one consistent linear reversible model, not a unique consequence of the cosine action. A full nonlinear stochastic model needs a state-space choice for compact phases, a mobility, a measure/gauge prescription, and a normalizable equilibrium measure. The periodic cosine potential on the unbounded linear space (Z^2\subset\mathbb R^{240}) is not by itself confining.

## 8. What would make (J_b) a physical stress observable?

At present (J_b) is a mathematically defined linear face observable. Calling it shear stress requires additional data:

1. a metric or coframe assigning physical areas and orientations to the 240 faces;
2. a specified metric-dependent action or free energy (S(g,\Omega));
3. a one-parameter shear deformation (g(\varepsilon));
4. a stress definition, for example
   [
   J_{\rm shear}(\Omega)
   =\left.\frac{\partial S(g(\varepsilon),\Omega)}
   {\partial\varepsilon}\right|_{\varepsilon=0};
   ]
5. a dynamical law and equilibrium measure for that same face state space;
6. physical units and volume normalization before interpreting the Green–Kubo integral as viscosity.

Only after these choices are fixed can the stress be expanded in face modes, represented by a vector (b_{\rm shear}\), and inserted into the formula in Section 6. No arbitrary identification of (b) with a face-label vector is justified.

## 9. Reversibility test and the supergolden question

The declared generator is (\gamma A), self-adjoint and strictly positive on (Z^2). Every invariant-subspace compression is self-adjoint with real positive spectrum. Therefore this reversible face Green–Kubo generator cannot be the matrix
[
M_s=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix},
\qquad \chi_{M_s}(x)=x^3-x^2-1,
]
whose characteristic polynomial has a non-real conjugate pair.

This excludes only the role of (M_s) as this reversible relaxation generator or a similar matrix. It does not exclude a separate non-reversible transfer map, a directed three-channel refinement, or another operator derived independently from the cubical geometry. Such an operator must be constructed from explicit data; its characteristic polynomial is an output, not an imposed constraint.

## 10. Reproducibility and next finite computation

The exact combinatorial input is fully specified by the cell labels and boundary formula in Section 2. The incidence implementation is `audits/q6_face_cochain_green_kubo.py`, with regression tests in `tests/test_q6_face_cochain_green_kubo.py`. Run `python audits/q6_face_cochain_green_kubo.py` and `python -m unittest tests.test_q6_face_cochain_green_kubo -v`. The script checks boundary identities and exact rational ranks, and records the tensor-product spectrum and Green–Kubo trace. Repository tests/CI have not been run for these commits. A reproducible independent matrix-level comparison should:

1. enumerate cells in a frozen lexicographic order;
2. build (B_1,B_2,B_3) with integer entries;
3. verify (B_1B_2=0) and (B_2B_3=0) exactly;
4. verify ranks (63,129,111) over (\mathbb Q) (or provide modular certificates plus a rational rank proof);
5. build (P_{\rm cl}) and verify (P_{\rm cl}^T=P_{\rm cl}), (P_{\rm cl}^2=P_{\rm cl}), and (B_3^TP_{\rm cl}=0);
6. build (A=\Delta_2|_{Z^2}) in an explicit orthonormal basis of (Z^2);
7. compare the tensor-product eigenvalue/multiplicity table with the explicit incidence-matrix Hodge operator;
8. evaluate the isotropic trace formula in Section 6.1, already reduced exactly above.

No numerical diagonalization or repository test execution is claimed. The spectrum and trace coefficient stated above are obtained analytically from the tensor-product decomposition.

## 11. Evidence ledger

| Statement | Status |
|---|---|
| Cubical cell counts (64,192,240,160) | Exact combinatorial identity |
| (B_1B_2=B_2B_3=0) | Exact cubical boundary identities |
| Ranks (63,129,111) | Exact consequence of contractibility/exactness; also checked by exact rational elimination in the committed audit script |
| (dim Z^2=129), (P_{\rm cl}) formula | Exact finite-dimensional linear algebra |
| (Delta_2) self-adjoint and positive; (Z^2) invariant | Exact |
| (A>0) on (Z^2) | Exact, since (H^2(I^6)=0) |
| OU covariance and Green–Kubo spectral formula | Exact for the declared reversible OU model |
| Face stress/viscosity interpretation | Open; requires metric-dependent stress and physical units |
| Spectrum of (A) and isotropic Green–Kubo coefficient | Exact tensor-product derivation: eigenvalues 4, 6, 8, 10, 12 with multiplicities 15, 40, 45, 24, 5; coefficient 2263/15480 |
| Three-component supergolden transfer map from Q6 faces | Open |

**Conclusion.** This construction provides the requested rigorous face-level starting point: state space, incidence, inner product, closed projector, invariant positive Hodge operator, reversible dynamics, and Green–Kubo formula are all explicitly defined. It stops exactly where the physical stress observable and its metric dependence must be supplied.
