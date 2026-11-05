# T029 — Exact Rumin Gram matrices and binary-icosahedral multiplicities

**Status:** exact (2\times2) matrices for (D^*D) in the normalized two-copy multiplicity basis of the generic Kitaoka Case V blocks; exact McKay multiplicities for all nine irreducible (2I)-sectors over the audited range. **This is not yet a construction of the geometric coefficient matrix of (D).**

**Base:** merged T028, commit `9d7899da49a403f7d3940e5d501133b0f201fe60`.  
**Group:** (2I\subset SU(2)), order (120).  
**Generic range:** (p,q\geq1), (m=p+q).

## 1. What can be determined without choosing a target basis

T025 supplies the two normalized middle-degree multiplicity vectors and the exact data
[
A^2=\frac{p(q+1)}2,\qquad B^2=\frac{q(p+1)}2,qquad
L=2pq+p+q,qquad A^2+B^2=\frac L2.
]
The exact line is spanned by (v_0=(A,B)^T), since (D d_R^0=0). Its orthogonal complement is spanned by (v_+=(B,-A)^T). The positive singular value is (L/2), so
[
D^*D=\frac{L^2}{4}\,P_{v_+}.
]
In the normalized (((1,0),(0,1))) multiplicity basis this gives the explicit exact matrix
[
\boxed{
G_{p,q}:=(D^*D)_{p,q}
=\frac{L}{2}
\begin{pmatrix}
B^2&-AB\\
-AB&A^2
\end{pmatrix}
=\frac{L}{2}
\begin{pmatrix}
\frac{q(p+1)}2&
-\frac12\sqrt{pq(p+1)(q+1)}\\
-\frac12\sqrt{pq(p+1)(q+1)}&
\frac{p(q+1)}2
\end{pmatrix}.}
\tag{1}
]
Here (A,B) are chosen positive as in Kitaoka's normalized highest-weight vectors; changing a phase convention conjugates the displayed matrix by the corresponding diagonal unitary.

The identities are exact:
[
G_{p,q}v_0=0,\quad
G_{p,q}v_+=\frac{L^2}{4}v_+,\quad
G_{p,q}^2=\frac{L^2}{4}G_{p,q},\quad
\operatorname{tr}G_{p,q}=\frac{L^2}{4},\quad
\det G_{p,q}=0.
]
This is more explicit than the diagonal singular-value normal form in T025: it expresses the Gram operator in the original two-copy multiplicity basis, rather than rotating to its eigenbasis.

## 2. Restriction to all nine (2I) irreducibles

Let
[
V_m=\operatorname{Sym}^m(\mathbb C^2)|_{2I}
\cong\bigoplus_{\rho\in\widehat{2I}}n_\rho(m)V_\rho,
\qquad d_\rho=\dim V_\rho.
]
T027's affine-(E_8) McKay recurrence gives the exact integers (n_\rho(m)), and
[
\sum_\rho d_\rho n_\rho(m)=m+1.
]
Since (1) acts as the identity on the (V_m) factor, the kernel and positive eigenspace dimensions in the (ho)-isotypic sector are both
[
\boxed{d_\rho n_\rho(m).}
]
The positive eigenvalue remains (L^2/4). No extra factor (d_\rho) is to be applied to the copy count (n_\rho(m)) itself.

The audit imports the existing T027 recurrence rather than reimplementing or silently changing its label map. It checks the weighted-dimension identity for every (m=p+q) in the rectangular range and accumulates kernel/positive dimensions separately for all nine labels.

## 3. Exact audit

Run from the repository root:
```bash
python audits/t029_rumin_gram_matrices_2i.py --max-index 20 --json
```
The script uses SymPy exact algebraic arithmetic and checks, for every generic pair in the requested rectangle:

1. the exact (2\times2) Gram matrix (1);
2. its kernel and positive eigenvectors;
3. the polynomial identity (G^2-(L^2/4)G=0), trace and determinant;
4. the McKay weighted-dimension identity at (m=p+q);
5. equality of the kernel and positive multiplicities in each of the nine (2I)-sectors.

## 4. Crucial limitation: why this is not yet the geometric (D)-matrix

Knowing (D^*D=G_{p,q}) determines the singular values and right singular vectors, but not the target singular vector or its phase. If (D) is represented as a map from a two-dimensional source multiplicity space to a target multiplicity space, then (D=U\,G_{p,q}^{1/2}) on its support for an isometric target embedding (U). Different (U)'s give the same (D^*D). Therefore the geometric coefficient matrix of (D) cannot be inferred from T025's singular-value data alone.

To determine it, the next input must be a fixed orthonormal target harmonic basis and the actual action of
[
D=\theta\wedge(\mathcal L_T+d_bL^{-1}d_b)
]
on the chosen source basis, with the contact metric and adjoints fixed. Only after that calculation can the target phase/unitary be fixed and the differential intertwining residuals of T024 be tested as matrix identities.

## 5. Boundary cases and status

The two Kitaoka boundary families (q=-1) and (p=-1), with eigenvalues ((p+1)^2/4) and ((q+1)^2/4), are not obtained by substituting negative indices into (1). They remain separate, as in T025.

| Claim | Status |
|---|---|
| Matrix (G_{p,q}) in (1) | Exact consequence of T025 data in its normalized two-copy basis |
| Kernel/positive eigenvectors and trace/determinant identities | Exact algebra |
| Nine (2I)-sector multiplicities | Exact McKay recurrence; finite range checked by script |
| Geometric matrix (D) in a fixed source/target basis | Open |
| Full source/target representation matrices and matrix intertwining residuals | Open |
| Boundary-family matrices | Open; eigenvalues retained separately |

## References

1. A. Kitaoka, *Analytic torsions associated with the Rumin complex on contact spheres*, Int. J. Math. 31 (2020), 2050112, [arXiv:1911.03092](https://arxiv.org/abs/1911.03092), especially §2.3, Case V–VII.
2. T024, *Reynolds projectors and equivariance of the Rumin differential on (S^3/2I)*.
3. T025, *Exact middle-degree Rumin blocks on the standard contact three-sphere*.
4. T027, *Exact McKay–Molien bridge for the nine Rumin twists*.
