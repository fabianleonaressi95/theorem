# T030 — Polar factorization and target-gauge ambiguity of the Rumin middle block

**Status:** exact algebraic polar factorization of the generic T025 Gram matrix, including a (U(1))-phase family and arbitrary target-isometry freedom. This is a controlled closure of the inverse problem left by T029; it is **not** a derivation of the geometric Rumin differential coefficients.

## 1. Exact polar representative

Use the T029 notation
[
A^2=\frac{p(q+1)}2,\quad B^2=\frac{q(p+1)}2,\quad
S=A^2+B^2=\frac L2,\quad L=2pq+p+q.
]
Set
[
P_+=\frac1S
\begin{pmatrix}B^2&-AB\\-AB&A^2\end{pmatrix},
\qquad
G=D^*D=\frac{L^2}{4}P_+.
]
Then (P_+^2=P_+=P_+^*), and the positive square root is
[
oxed{D_0:=G^{1/2}=\frac L2P_+
=\frac L{2S}
\begin{pmatrix}B^2&-AB\\-AB&A^2\end{pmatrix}.}
]
It satisfies
[
D_0^*D_0=D_0^2=G,qquad
D_0v_0=0,qquad D_0v_+=\frac L2v_+.
]
This chooses an identified target multiplicity copy and the positive polar gauge. It is a mathematically canonical representative of the Gram data, not a claim about the target basis selected by the contact differential.

## 2. Phase and target-isometry freedom

For any (artheta\in\mathbb R),
[
D_\vartheta=e^{i\vartheta}D_0
\quad\Longrightarrow\quad D_\vartheta^*D_\vartheta=G.
]
More generally, if (U:\mathbb C^2\to\mathbb C^r) is an isometric embedding on the one-dimensional support of (P_+), then
[
D_U=\frac L2\,U P_+,
\qquad D_U^*D_U=G.
]
Thus the Gram matrix determines the right singular line and singular value but does not determine the target singular vector, its phase, or its embedding in the target harmonic space. The ambiguity is genuine, not a numerical defect.

## 3. Equivariance consequence

On a fixed (2I)-isotypic multiplicity sector, the Gram factor is scalar on the irreducible representation factor. Therefore the polar representative (D_0\otimes I_{V_\rho}) is an intertwiner when the source and target copies are identified equivariantly. This proves that an equivariant representative exists for the Gram data. It does **not** prove that the geometric Rumin differential equals this representative in Kitaoka's target basis.

For every irreducible (ho), the multiplicity of the positive line remains (n_\rho(m)) copies, with total dimension (d_\rho n_\rho(m)), as in T027–T029.

## 4. Exact audit

Run:
```bash
python audits/t030_rumin_polar_factorization.py --max-index 20 --json
```
The SymPy audit checks every generic pair in the requested rectangle:
- projector idempotence and self-adjointness;
- (D_0^*D_0=G) and (D_0^2=G);
- phase invariance (D_\vartheta^*D_\vartheta=G);
- target-isometry invariance (D_U^*D_U=G).

The code uses exact radicals and symbolic unit-modulus phases. It does not numerically fit an unknown geometric phase.

## 5. What is needed to identify the actual geometric differential

The remaining geometric calculation is now sharply specified. Choose explicit orthonormal source and target harmonic sections, including phase conventions, and evaluate
[
D=\theta\wedge(\mathcal L_T+d_bL^{-1}d_b)
]
on each source section. The resulting coefficient matrix (D_{\mathrm{geom}}) must then be compared with the polar family by checking
[
D_{\mathrm{geom}}^*D_{\mathrm{geom}}=G,
\qquad
D_{\mathrm{geom}}U_j(g)=U_{j+1}(g)D_{\mathrm{geom}}
\quad(g\in2I).
]
The first identity checks the singular data; the second checks the fixed-basis equivariance. Agreement of singular values alone is insufficient.

Kitaoka's Case V supplies the source and norm data used above. T024 supplies the abstract naturality identity. Neither, without explicit target coefficients in a common basis, fixes the geometric target isometry. This note therefore does not overstate the result.

## 6. Status ledger

| Claim | Status |
|---|---|
| Positive square root (G^{1/2}) | Exact |
| (U(1)) phase invariance | Exact |
| Target-isometry freedom | Exact |
| Existence of an equivariant polar representative after identifying multiplicity copies | Exact representation-theoretic construction |
| Identification with geometric (D_R) in Kitaoka's fixed target basis | Open |
| Explicit source/target harmonic coefficient matrices | Open |

## References

1. A. Kitaoka, *Analytic torsions associated with the Rumin complex on contact spheres*, Int. J. Math. 31 (2020), 2050112, arXiv:1911.03092, §2.3 Case V.
2. T024, *Reynolds projectors and equivariance of the Rumin differential on (S^3/2I)*.
3. T025, *Exact middle-degree Rumin blocks on the standard contact three-sphere*.
4. T029, *Exact Rumin Gram matrices and binary-icosahedral multiplicities*.
