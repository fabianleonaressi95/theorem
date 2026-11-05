# T025 — Exact middle-degree Rumin blocks on the standard contact three-sphere

**Status:** exact finite-dimensional reduction of the middle-degree operator (D^dagger D) on the generic (S^3) harmonic sectors, derived from Kitaoka's normalized highest-weight vectors. The calculation is independently checked by an exact-arithmetic audit script. This is not yet a realization of all (2I) representation matrices or a full twisted spectrum computation.

**Base:** T024, branch `t024-rumin-reynolds-intertwiners`.  
**Geometry:** standard CR/contact (S^3subsetmathbb C^2), with Kitaoka's contact form and metric conventions.  
**Group:** (2Isubset SU(2)), order (120).

## 1. Why the middle operator must be treated separately

In contact dimension three, the Rumin complex has
[
E^0\xrightarrow{d_R^0}E^1\xrightarrow{D_R}E^2\xrightarrow{d_R^2}E^3,
]
where (d_R^0,d_R^2) are first order and the middle operator (D_R) is second order. Kitaoka defines the rescaled differential (d_E^k=a_kd_R^k), with (a_k=|1-k|^{-1/2}) for (k\ne1), and (a_1=1). In particular, the middle operator is unchanged: (D_E=D_R=D).

The geometric formula used in the source is
[
D=\theta\wedge\bigl(\mathcal L_T+d_bL^{-1}d_b\bigr),
\qquad L=d\theta\wedge,
\]
where (T) is the Reeb field and (d_b\alpha=d\alpha-\theta\wedge\iota_Td\alpha). On Sasakian manifolds the equivalent CR expression is
[
D=\theta\wedge\left(\mathcal L_T
-i(\partial_b+\bar\partial_b)
(\partial_b^\dagger-\bar\partial_b^\dagger)\right).
]
These are geometric differential formulas, not arbitrary equivariant maps.

The Rumin Laplacian in middle degree is
[
\Delta_E^1=(d_E^0(d_E^0)^\dagger)^2+D^\dagger D.
\]
Consequently, its eigenvalue on all of (E^1) must not be confused with the spectrum of (D^\dagger D) alone. The latter is isolated below on the orthogonal complement of \(\operatorname{im}d_E^0\).

## 2. Generic (S^3) block: exact reduction

For (p,q\ge1), set
[
m=p+q,\qquad L_{p,q}=2pq+p+q.
]
The relevant (U(2)) highest weight is ((q,-p)). On restriction to (SU(2)), it is
[
V_{p,q}|_{SU(2)}\simeq\operatorname{Sym}^{m}(\mathbb C^2),
\qquad \dim V_{p,q}=m+1.
]
In the middle-degree space (E^1), the corresponding (U(2))-type occurs in two bidegree copies, represented by the normalized highest-weight vectors in the \((1,0)\) and \((0,1)\) summands.

Kitaoka's Case V calculation gives the squared norms of the two components of (d_E\psi^{(0,0)}_{(q,0,0,p)}):
[
A^2=\frac{p(q+1)}2,\qquad
B^2=\frac{q(p+1)}2.
\]
Thus
[
A^2+B^2=\frac{2pq+p+q}{2}=\frac{L_{p,q}}2.
\]
For the orthogonal middle-degree combination, the formula for (D) uses
[
C=\frac{p-q}{2},\qquad
A'=C-2A^2=-\frac{L_{p,q}}2,\qquad
B'=C+2B^2=\frac{L_{p,q}}2.
\]
Kitaoka obtains
[
D^\dagger D\big|_{(\operatorname{im}d_E^0)^\perp}
=
\frac{(A'B)^2+(B'A)^2}{A^2+B^2}
=
\frac{L_{p,q}^2}{4}.
\]
The equality follows exactly because (A'=-L_{p,q}/2), (B'=L_{p,q}/2), and (A^2+B^2=L_{p,q}/2).

On the complementary exact line, (D=0), since (D\,d_E^0=0). Therefore, in orthonormal source/target bases adapted to these two multiplicity lines, the middle differential has singular-value normal form
[
D_{p,q}\sim
\begin{pmatrix}
0&0\\
0&L_{p,q}/2
\end{pmatrix},
\qquad
(D^\dagger D)_{p,q}\sim
\begin{pmatrix}
0&0\\
0&L_{p,q}^2/4
\end{pmatrix}.
\tag{1}
]
Each entry in (1) is tensored with the identity on the (m+1) dimensional (SU(2))-module. The unitary changes of basis absorb the phase and identify the source and target multiplicity lines; (1) is a singular-value normal form, not a claim that the unnormalized geometric basis has this diagonal matrix.

This gives the exact positive eigenvalue
[
\boxed{\lambda_{p,q}(D^\dagger D)=\frac{(2pq+p+q)^2}{4}}
\]
with representation dimension (p+q+1) before restriction to (2I). The zero line has the same representation dimension.

## 3. Boundary sectors

The two exceptional cases in Kitaoka's decomposition must be kept separate from the generic (p,q\ge1) block:

- (q=-1, p\ge1): the relevant space is the ((1,0)) boundary type and (D=\theta\wedge\mathcal L_T); the eigenvalue of (D^\dagger D), and of the middle Rumin Laplacian on this sector, is ((p+1)^2/4).
- (p=-1, q\ge1): the conjugate ((0,1)) boundary type has eigenvalue ((q+1)^2/4).

These boundary eigenvalues are not obtained by substituting negative indices into the generic formula.

## 4. Restriction to the binary icosahedral group

Because (2I\subset SU(2)), the (m)-th harmonic module restricts to
[
V_m=\operatorname{Sym}^m(\mathbb C^2)|_{2I}.
]
For an irreducible (2I)-representation \(\rho\), the central projector is
[
P_{\rho,m}=\frac{d_\rho}{120}
\sum_{g\in2I}\overline{\chi_\rho(g)}\,U_m(g).
]
The scalar block (1) commutes with this action. Hence the exact positive eigenvalue on the \(\rho\)-isotypic part is still (L_{p,q}^2/4), with multiplicity
[
d_\rho\,\dim\operatorname{Hom}_{2I}(V_\rho,V_m)
]
for the positive multiplicity line; the zero line has the same representation-theoretic multiplicity. For the untwisted quotient sector take \(\rho=\mathbf1\), so the positive multiplicity is
[
a_m=\dim(V_m^{2I})
=\frac1{120}\sum_{g\in2I}\chi_m(g).
]
This is the correct place to insert the Molien/character calculation from T021–T024. No numerical value of \(a_m\) is hard-coded in this theorem note.

## 5. Exact audit

The companion script `audits/t025_rumin_middle_degree_blocks.py` uses rational arithmetic only. It checks, over a rectangular range of positive integer \((p,q)\):

1. (A^2+B^2=L_{p,q}/2);
2. (A'=-L_{p,q}/2) and (B'=L_{p,q}/2);
3. the source expression (((A'B)^2+(B'A)^2)/(A^2+B^2)) equals (L_{p,q}^2/4);
4. the boundary expressions remain separate;
5. the block trace and determinant of \(\operatorname{diag}(0,L_{p,q}^2/4)\) agree with its two exact eigenvalues.

The audit is an exact algebraic consistency check of the published reduction. It is not a discretization of the differential operator and does not claim to numerically approximate its full spectrum.

## 6. Status ledger

| Claim | Status |
|---|---|
| Geometric second-order formula for (D_R) | Published formula, under the stated contact/CR conventions |
| Generic (p,q\ge1) singular values of the middle block | Exact consequence of Kitaoka's Case V calculation |
| (D^\dagger D) block (1) | Exact in orthonormal multiplicity bases |
| (SU(2)) dimension (p+q+1) | Exact representation-theoretic fact |
| Restriction/projector decomposition for (2I) | Exact finite-group representation theory; projector construction in T024 |
| Exact rational audit | Companion script |
| Explicit unnormalized coefficient matrices in a fixed global harmonic basis | Still open |
| All nine twisted multiplicity tables and full zeta/torsion comparison | Still open; continue from T021–T024 |
| Full matrix realization of all (d_R^k) in one fixed basis | Still open |

## References

1. A. Kitaoka, *Analytic torsions associated with the Rumin complex on contact spheres*, Int. J. Math. 31 (2020), 2050112, [arXiv:1911.03092](https://arxiv.org/abs/1911.03092). In particular: §1.1 equations (1.1)–(1.3), Proposition 1.1, Lemma 2.1, and §2.3 Case V–VII.
2. M. Rumin and N. Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier 62 (2012), 727–782, [DOI:10.5802/aif.2693](https://doi.org/10.5802/aif.2693).

## Classification

- **Proved from the cited formulae:** generic middle-degree singular values and the (D^\dagger D) two-line block.
- **Exact-arithmetic verified:** all rational identities in the companion audit range.
- **Open:** fixed-basis coefficient matrices, explicit group matrices for all (2I) irreps, and the full nine-twist zeta/torsion computation.
- **Not claimed:** a new eigenvalue theorem for the sphere, or a completed full matrix diagonalization of the differential complex.
