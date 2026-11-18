# Vesica Piscis, \u221a3, Needham, and the pentagon–hexagon construction

**Record type:** source-and-geometry dossier  
**Date:** 18 November 2026  
**Status:** exact Euclidean identities proved; source comparison established; historical/interpretive links kept separate from theorem claims.

## 1. Scope and correction of the Needham reference

The relevant Needham is **Tristan Needham, _Visual Complex Analysis_** (Oxford: Clarendon Press/Oxford University Press, 1997), in the discussion of fractional powers and the geometry of roots of unity (Chapter 2, §VI, pp. 91–95 in the edition previously identified in this research thread). The relevant mathematical object is the equilateral-triangle geometry of the cube roots of a complex number / unity, where the factor \(\sqrt3\) is the height-to-side geometry of a 120-degree configuration.

Do **not** cite Needham's later Möbius/cross-ratio exercises about mapping families of circles to concentric circles as the source of the Vesica Piscis result. That was a mistaken identification in an earlier discussion.

The present dossier makes a precise comparison: Needham's cube-root geometry and the Vesica Piscis share the same equilateral-triangle / third-root-of-unity geometry. It does **not** claim that Needham proves a theorem specifically named “Vesica Piscis”, nor that the construction in Bonilla is taken from Needham.

## 2. Vesica Piscis and the exact \(\sqrt3\) ratio

Let two circles have common radius \(r\), with their centres separated by \(r\). Put the centres at
\[
A=(0,0),\qquad B=(r,0).
\]
Their intersection points are
\[
C=\left(\frac r2,\frac{\sqrt3 r}{2}\right),\qquad
D=\left(\frac r2,-\frac{\sqrt3 r}{2}\right).
\]
Thus the common chord has length
\[
CD=\sqrt3\,r,
\]
and the centre-axis segment has length \(AB=r\). Therefore
\[
\boxed{CD/AB=\sqrt3.}
\]

The two axes of the lens have lengths \(2r\) (centre-axis direction) and \(\sqrt3r\) (common chord direction). Consequently the long-axis/short-axis ratio is \(2/\sqrt3\), not \(\sqrt3\). These are two distinct ratios and must not be conflated.

A stronger converse is studied by Mauro Maria Baldi: for two intersecting circles, the condition that the cross-shaped pair of segments described in his paper has ratio \(\sqrt3\) characterizes the Vesica Piscis configuration. Baldi gives both a Euclidean and an analytic-geometry proof. The accessible record is a 2020 working-paper/preprint, not to be silently upgraded to a peer-reviewed publication.

## 3. The common equilateral-triangle structure and Needham

Set \(r=1\) and identify the plane with \(\mathbb C\). The Vesica intersection points are
\[
C=\frac12+i\frac{\sqrt3}{2}=e^{i\pi/3}=-\omega^2,
\qquad
D=\frac12-i\frac{\sqrt3}{2}=e^{-i\pi/3}=-\omega,
\]
where
\[
\omega=e^{2\pi i/3},\qquad 1+\omega+\omega^2=0.
\]
The three points
\[
-1,\quad -\omega,\quad -\omega^2
\]
are the vertices of an equilateral triangle on the unit circle. The side length is \(\sqrt3\), since
\[
|\omega-\omega^2|=\sqrt3.
\]

This is the exact bridge to Needham's treatment of cube roots: the three cube roots of a nonzero complex number differ by multiplication by \(1,\omega,\omega^2\), hence are equally spaced in argument by \(2\pi/3\). For unit modulus they form an equilateral triangle; its chord length is \(\sqrt3\). The Vesica construction realizes the same triangle in the complex plane, up to an overall sign/rotation.

**Interpretation boundary.** This is a shared geometric realization of the third roots of unity, not evidence that the Vesica itself is a monodromy computation. For the analytic continuation of \(w^3=z\) around the origin, the three branches cycle by multiplication by \(\omega\); that is the monodromy statement. The static Vesica picture alone does not establish analytic continuation or monodromy.

The natural arithmetic setting is the Eisenstein lattice \(\mathbb Z[\omega]\) and the quadratic field \(\mathbb Q(\sqrt{-3})\). This is the triangular/hexagonal side of the dossier.

## 4. Eisenstein integers: the arithmetic form of the triangular geometry

The Eisenstein integers give an exact arithmetic model for the equilateral-triangle/hexagonal lattice underlying the \(\sqrt3\) geometry.

Let
\[
\omega=e^{2\pi i/3}=\frac{-1+i\sqrt3}{2},\qquad
\mathbb Z[\omega]=\{a+b\omega:a,b\in\mathbb Z\}.
\]
This is the triangular lattice. Its six units
\[
\{\pm1,\pm\omega,\pm\omega^2\}
\]
encode the six directions separated by multiples of \(60^\circ\), the algebraic counterpart of hexagonal symmetry.

For the normalized Vesica in §3,
\[
C=-\omega^2,\qquad D=-\omega,
\]
and its common chord is
\[
C-D=\omega-\omega^2=1+2\omega=i\sqrt3.
\]
The chord is therefore an Eisenstein integer, with norm
\[
N(1+2\omega)=(1+2\omega)(1+2\omega^2)=3,
\qquad |C-D|=\sqrt3.
\]
The Eisenstein prime \(1-\omega\) also has norm 3, and the rational prime 3 ramifies in \(\mathbb Q(\sqrt{-3})\):
\[
(1-\omega)^2=-3\omega,
\qquad 3=-\omega^2(1-\omega)^2.
\]

**Meaning.** Needham's cube roots of unity give the complex-analytic picture; Eisenstein integers give its integral lattice and norm structure; the Vesica realizes a chord of Eisenstein norm 3. These are compatible descriptions of the same triangular geometry.

**Boundary.** This does not create an arithmetic identification between \(\mathbb Q(\sqrt{-3})\) and \(\mathbb Q(\sqrt5)\). The pentagonal/golden-ratio side belongs to a different quadratic field. Any deeper arithmetic bridge requires a separately defined object and proof; it cannot be inferred from the geometric construction alone.

**Connection with cubic reciprocity.** The ring \(\mathbb Z[\omega]\) is not merely a convenient lattice: it is the arithmetic setting for cubic residue symbols and the law of cubic reciprocity. The factor \(1-\omega\) is a prime factor above 3 and occurs in Eisenstein's supplementary law. In the formulation discussed by Kenneth S. Williams, if \(\pi=a+b\omega\) is a primary Eisenstein prime with \(a=3m-1\), \(b=3n\), and norm a rational prime \(p\equiv1\pmod3\), then
\[
\left(\frac{1-\omega}{\pi}\right)_3=\omega^{2m}.
\]
Thus the factor \(1-\omega\) is arithmetically significant, not merely a factor in the decomposition of 3.

Historically, Jacobi published results on cubic residues in 1827 and developed proofs in his Königsberg lectures (dated 1837 in Lemmermeyer's modern historical account); Eisenstein published the first complete proofs of the cubic and quartic reciprocity laws in 1844, together with supplementary laws. The priority should therefore be stated carefully: Jacobi anticipated and developed the theory; Eisenstein supplied the first complete published proofs.

**Interpretation boundary.** This is a correspondence through the same arithmetic ring, not a claim that the Vesica itself is the context of cubic reciprocity, nor that the geometric figure implies the reciprocity theorem. The Vesica realizes one Eisenstein integer of norm 3; cubic reciprocity is a theorem about residue symbols in the ring as a whole.

## 5. Bonilla: Vesica, pentagon, hexagon, and \(\Phi\)

Ibo Bonilla Oconitrillo's web essay, _Relación áurea entre pentágono y hexágono_ (2023 version as indexed on the author's site), explicitly asks whether the regular pentagon and hexagon can be constructed from one another, whether their relation to the golden ratio can be demonstrated, and whether the Vesica Piscis is involved. The essay proposes constructions from the Vesica and extends the discussion to the truncated icosahedron (12 pentagons and 20 hexagons).

The source is useful as a **construction proposal and research lead**, but its broad claims must be checked construction by construction. In particular:
- the regular pentagon identity \(d/s=\Phi\) is standard and exact;
- the truncated icosahedron's golden-ratio coordinates are standard once a coordinate model and scale are fixed;
- the existence of pentagons and hexagons on the same polyhedral surface does not by itself prove a unique planar pentagon–hexagon construction;
- the claimed “perfect Fibonacci sequence” and universal statements in the essay are not established by the elementary construction alone.

A rigorous, independently documented intermediate construction is given by Sparavigna and Baldi, _A Study of the Regular Pentagon with a Classic Geometric Approach_ (2016), §6, which constructs a regular pentagon from the Vesica Piscis using straightedge and compass. The sixfold circle arrangement / Flower of Life supplies adjacent equal circles whose centres are one radius apart; that adjacent pair is precisely the Vesica starting configuration. This yields the composition:
\[
\text{sixfold circle arrangement}
\longrightarrow \text{adjacent-circle Vesica}
\longrightarrow \text{regular pentagon}.
\]
This is a composition of Euclidean constructions; it does not mean that the cyclic groups \(C_6\) and \(C_5\) are nested or that the pentagon inherits sixfold symmetry.

## 6. The cyclotomic bridge between the triangular and pentagonal fields

The two quadratic fields are distinct, but both have precise cyclotomic descriptions.

### 6.1 Triangular side

Let \(\zeta_3=e^{2\pi i/3}=\omega\). Then
\[
\mathbb Q(\sqrt{-3})=\mathbb Q(\zeta_3),
\]
and its ring of integers is \(\mathbb Z[\omega]\). This is the field underlying the Eisenstein lattice and cubic reciprocity.

### 6.2 Pentagon and golden-ratio side

Let \(\zeta_5=e^{2\pi i/5}\). The maximal real subfield of the fifth cyclotomic field is
\[
\mathbb Q(\zeta_5)^+=\mathbb Q(\zeta_5+\zeta_5^{-1})=\mathbb Q(\sqrt5).
\]
Moreover,
\[
\zeta_5+\zeta_5^{-1}=2\cos(2\pi/5)
=\frac{\sqrt5-1}{2}=\Phi-1,
\]
so
\[
\boxed{\Phi=1+\zeta_5+\zeta_5^{-1}=2\cos(\pi/5).}
\]
The golden ratio is therefore generated by the real part of a primitive fifth root of unity. This is the exact cyclotomic origin of the pentagonal quadratic field.

### 6.3 Their compositum

The fields \(\mathbb Q(\zeta_3)\) and \(\mathbb Q(\zeta_5)^+\) are distinct quadratic Galois extensions of \(\mathbb Q\). Their intersection is \(\mathbb Q\), so their compositum has degree 4:
\[
K=\mathbb Q(\sqrt{-3},\sqrt5)
=\mathbb Q(\sqrt{-3},\Phi).
\]
It is a biquadratic extension with Galois group \(C_2\times C_2\), and
\[
K\subset\mathbb Q(\zeta_{15}),
\qquad [\mathbb Q(\zeta_{15}):\mathbb Q]=\varphi(15)=8.
\]
The full fifteenth cyclotomic field is \(\mathbb Q(\zeta_3,\zeta_5)\); \(K\) is the degree-four subfield obtained by adjoining \(\zeta_3\) and the real subfield of \(\mathbb Q(\zeta_5)\). Do not identify \(K\) with the whole \(\mathbb Q(\zeta_{15})\).

**Conclusion.** There is a rigorous arithmetic bridge: the triangular/Eisenstein field and the pentagonal/golden-ratio field are linearly disjoint quadratic subfields whose compositum lies in the fifteenth cyclotomic field. This does not identify the two fields and does not by itself produce a new reciprocity law or a geometric-spectral law. It provides a common Galois/cyclotomic framework in which a future interaction can be formulated precisely.

## 7. Status register

| Item | Statement | Status |
|---|---|---|
| V1 | For equal circles with centre separation \(r\), the common chord is \(\sqrt3r\). | Proved |
| V2 | The Vesica intersection points and the third roots of unity form the same equilateral-triangle configuration up to rotation/sign. | Proved |
| N1 | Needham's cube-root discussion supplies the roots-of-unity geometry used in the comparison. | Source identified; page-level citation should be checked against the user's edition before quoting |
| E1 | The normalized Vesica chord is the Eisenstein integer \(1+2\omega\) with norm 3; 3 ramifies in \(\mathbb Q(\sqrt{-3})\). | Proved exactly |
| E2 | Cubic reciprocity is formulated in \(\mathbb Z[\omega]\); the factor \(1-\omega\) occurs in Eisenstein's supplementary law. | Classical theorem; source documented |
| C1 | \(\mathbb Q(\sqrt5)=\mathbb Q(\zeta_5)^+\), with \(\Phi=1+\zeta_5+\zeta_5^{-1}\). | Proved exactly |
| C2 | \(\mathbb Q(\sqrt{-3},\sqrt5)\) is a degree-four biquadratic subfield of \(\mathbb Q(\zeta_{15})\). | Proved exactly |
| B1 | The Vesica can be used in a straightedge-and-compass construction of a regular pentagon. | Published construction; independently checkable |
| B2 | A sixfold circle arrangement contains adjacent-circle pairs defining a Vesica. | Proved from the arrangement's defining geometry |
| B3 | The chain sixfold arrangement → Vesica → pentagon is a composition of constructions. | Proved as a composition |
| B4 | Every broader claim in Bonilla's essay (including the “perfect Fibonacci sequence” and universal natural-law conclusions) follows from these constructions. | Not established |
| H1 | A deeper unified arithmetic/dynamical structure between \(\mathbb Q(\sqrt{-3})\) and \(\mathbb Q(\sqrt5)\) is present. | Open question; no field equivalence asserted |

## 8. Bibliography and primary links

1. Tristan Needham, _Visual Complex Analysis_, Oxford: Clarendon Press, 1997, Chapter 2, §VI, discussion of fractional powers / cube roots and roots of unity (pp. 91–95 in the edition previously identified). Verify pagination against the edition used before a verbatim quotation.
2. Mauro Maria Baldi, “On a property of the Vesica Piscis” (working paper, 2020), DOI: [10.5281/zenodo.4273133](https://doi.org/10.5281/zenodo.4273133); institutional record: [University of Milano-Bicocca repository](https://u-pad.unimc.it/handle/11393/324790).
3. Ibo Bonilla Oconitrillo, “Relación áurea entre pentágono y hexágono”, [author's page](https://iboenweb.com/ibo/docs/relacion_aurea_pentagono_hexagono_phi.html).
4. A. C. Sparavigna and M. M. Baldi, “A Study of the Regular Pentagon with a Classic Geometric Approach” (2016), §6, straightedge-and-compass construction from the Vesica Piscis.
5. A. C. Sparavigna and M. M. Baldi, “Flower of Life, Six-Fold Symmetry and Honeycomb Packing of Circles in the Mycenaean Geometry” (2016), for the sixfold circle arrangement and its relation to adjacent-circle geometry.
6. F. Lemmermeyer, _Reciprocity Laws: From Euler to Eisenstein_ (Springer, 2000), chapters on cubic and Eisenstein reciprocity; historical discussion of Jacobi and Eisenstein.
7. K. S. Williams, “Note on the Supplement to the Law of Cubic Reciprocity,” _Proceedings of the American Mathematical Society_ 47 (1975), 333 ff. [Author's PDF](https://people.math.carleton.ca/~williams/papers/pdf/067.pdf).
8. “The Eisenstein integers and cubic reciprocity,” Uppsala University thesis. [Full text PDF](https://uu.diva-portal.org/smash/get/diva2:1728553/FULLTEXT01.pdf).
9. Trinity College Dublin, number theory lecture notes, §15.1, for \(\mathbb Q(\sqrt5)\) and the golden ratio. [PDF](https://www.maths.tcd.ie/pub/Maths/Courseware/NumberTheory/NumberTheory.pdf).

## 9. Editorial rule for future use

When citing this chain, cite Needham for the complex roots-of-unity / cube-root geometry; cite Baldi for the converse characterization of the Vesica via the \(\sqrt3\) cross-ratio; cite Williams and Lemmermeyer for cubic reciprocity and its supplementary law; cite Bonilla for the proposed pentagon–hexagon synthesis; and cite Sparavigna–Baldi for the independently documented geometric constructions. Cite the cyclotomic identity for \(\Phi\) separately from the geometric construction. Do not attribute Baldi's theorem to Needham, do not state that Needham directly proves the Vesica Piscis theorem, and do not present the compositum field as a new reciprocity theorem.


## 10. Integral Galois action and its trace metric

This section makes the biquadratic field in §6.3 explicit as a rank-four integral Galois module. It also records the invariance of the natural trace form. In this particular extension the trace form is already invariant under the full Galois group; averaging over the group is unnecessary.

Let
\[
K=\mathbb Q(\alpha,\beta),\qquad \alpha=\sqrt{-3},\quad \beta=\sqrt5,
\]
and put
\[
e_1=1,\quad e_2=\frac{1+\beta}{2},\quad
e_3=\frac{1+\alpha}{2},\quad e_4=e_2e_3.
\]
Since the fundamental discriminants \(-3\) and \(5\) are coprime, these elements form an integral basis:
\[
\mathcal O_K=\mathbb Z[e_2,e_3]
=\mathbb Z e_1\oplus\mathbb Z e_2\oplus\mathbb Z e_3\oplus\mathbb Z e_4.
\]
The absolute field discriminant is
\[
|\operatorname{disc}(K)|=(-3)\cdot5\cdot(-15)=225.
\]

Write \(G=\operatorname{Gal}(K/\mathbb Q)=\langle\sigma_\alpha,\sigma_\beta\rangle\cong C_2\times C_2\), where \(\sigma_\alpha\) changes the sign of \(\alpha\) and fixes \(\beta\), while \(\sigma_\beta\) changes the sign of \(\beta\) and fixes \(\alpha\). Their actions on the integral basis are
\[
\begin{aligned}
&\sigma_\alpha(e_1)=e_1,\quad \sigma_\alpha(e_2)=e_2,\quad
\sigma_\alpha(e_3)=e_1-e_3,\quad
\sigma_\alpha(e_4)=e_2-e_4,\\
&\sigma_\beta(e_1)=e_1,\quad \sigma_\beta(e_2)=e_1-e_2,\quad
\sigma_\beta(e_3)=e_3,\quad
\sigma_\beta(e_4)=e_3-e_4.
\end{aligned}
\]
With column-coordinate vectors in the ordered basis \((e_1,e_2,e_3,e_4)\), the corresponding integral matrices are
\[
S_\alpha=
\begin{pmatrix}
1&0&1&0\\0&1&0&1\\0&0&-1&0\\0&0&0&-1
\end{pmatrix},\qquad
S_\beta=
\begin{pmatrix}
1&1&0&0\\0&-1&0&0\\0&0&1&1\\0&0&0&-1
\end{pmatrix}.
\]
They satisfy
\[
S_\alpha^2=S_\beta^2=I,\qquad
S_\alpha S_\beta=S_\beta S_\alpha.
\]

### 10.1 The trace form is invariant under all of \(G\)

Complex conjugation on this field is precisely \(c=\sigma_\alpha\). Since \(G\) is abelian, every \(\sigma\in G\) commutes with \(c\). Define
\[
\langle x,y\rangle_K
=\operatorname{Tr}_{K/\mathbb Q}(x\overline y).
\]
Then, for every \(\sigma\in G\),
\[
\begin{aligned}
\langle\sigma x,\sigma y\rangle_K
&=\operatorname{Tr}_{K/\mathbb Q}
  (\sigma(x)\overline{\sigma(y)})\\
&=\operatorname{Tr}_{K/\mathbb Q}
  (\sigma(x)\sigma(\overline y))\\
&=\operatorname{Tr}_{K/\mathbb Q}(\sigma(x\overline y))\\
&=\operatorname{Tr}_{K/\mathbb Q}(x\overline y)
=\langle x,y\rangle_K.
\end{aligned}
\]
The last equality is invariance of the field trace under Galois automorphisms. Thus the original trace form—not merely a group-averaged replacement—is positive definite and \(G\)-invariant in this biquadratic, abelian case.

In the chosen integral basis its Gram matrix is
\[
H=(\operatorname{Tr}(e_i\overline{e_j}))_{i,j}
=
\begin{pmatrix}
4&2&2&1\\
2&6&1&3\\
2&1&4&2\\
1&3&2&6
\end{pmatrix},
\qquad \det H=225.
\]
In particular,
\[
S_\alpha^{\mathsf T}HS_\alpha=H,
\qquad
S_\beta^{\mathsf T}HS_\beta=H.
\]
The matrices need not be symmetric in the chosen coordinate basis: they are orthogonal, and hence self-adjoint as involutions, with respect to the inner product represented by \(H\).

**Scope warning.** The argument uses the fact that complex conjugation is central in \(G\), here because \(G\) is abelian. For a general non-abelian Galois extension, the same trace form need not be invariant under the whole Galois group. Group averaging can produce an invariant positive-definite form in a finite-group representation, but it is not needed here and is not the original trace form.

### 10.2 The Galois operator and its spectrum

Define the sum operator and the associated Cayley-graph Laplacian on the four-dimensional rational representation:
\[
A_G=S_\alpha+S_\beta
=
\begin{pmatrix}
2&1&1&0\\
0&0&0&1\\
0&0&0&1\\
0&0&0&-2
\end{pmatrix},
\qquad
L_G=2I-S_\alpha-S_\beta.
\]
The eigenvalues are
\[
\operatorname{Spec}(A_G)=\{-2,0,0,2\},\qquad
\operatorname{Spec}(L_G)=\{0,2,2,4\},
\]
with multiplicities \(1,2,1\) for the Laplacian. This follows directly from the four characters of \(C_2\times C_2\): on a character with values \((\varepsilon,\delta)\in\{\pm1\}^2\), the operators act by \(\varepsilon+\delta\) and \(2-\varepsilon-\delta\), respectively.

The character projectors are
\[
P_{\varepsilon,\delta}
=\frac14(I+\varepsilon S_\alpha)(I+\delta S_\beta),
\qquad \varepsilon,\delta\in\{\pm1\}.
\]
Each has rank one over \(\mathbb Q\).

**Interpretation boundary.** The spectrum \(\{0,2,2,4\}\) is exact, but is forced by the Cayley graph / regular representation of \(C_2\times C_2\). It is not, by itself, a new spectral law or a derived physical spectrum. The operator acts on the rank-four lattice module (equivalently, the regular representation), not on the set of all points of the infinite lattice \(\mathcal O_K\).

### 10.3 Status

| Item | Statement | Status |
|---|---|---|
| G1 | The displayed four elements form an integral basis of \(\mathcal O_K\); \(|\operatorname{disc}(K)|=225\). | Exact algebraic-number-theory result |
| G2 | The two displayed matrices give the integral action of \(C_2\times C_2\) on \(\mathcal O_K\). | Exact; directly checkable |
| G3 | The form \(\operatorname{Tr}(x\overline y)\) is positive definite and invariant under all of \(G\). | Proved; uses centrality of complex conjugation |
| G4 | The Gram matrix is \(H\) as displayed, with determinant 225. | Exact computation |
| G5 | The Cayley Laplacian has spectrum \(0,2,2,4\). | Exact; representation-theoretic |
| G6 | A nontrivial new spectral relation linking this Galois module to Vesica/pentagon geometry or to a physical operator exists. | Open; not established by G1–G5 |

## 11. Golden-ratio cotangent expansion and Bernoulli representation

This section records the exact analytic identity obtained by evaluating Euler's partial-fraction expansion of the cotangent at the golden-ratio parameter. It is an analytic consequence of periodicity and the zeta expansion; it is **not** a geometric consequence of the truncated icosahedron, and it does not validate any physical threshold formula used to motivate the parameter.

### 11.1 Exact parameter reduction

Let
\[
\varphi=\frac{1+\sqrt5}{2},\qquad
\varphi^3=2+\sqrt5,
\]
and define
\[
\varepsilon=\frac{\sqrt5-2}{2}.
\]
Rationalization gives
\[
\varepsilon=\frac{1}{4+2\sqrt5}
=\frac{1}{2\varphi^3},\qquad 0<\varepsilon<1.
\]
Since \(\sqrt5/2=1+\varepsilon\) and cotangent has period \(\pi\),
\[
\boxed{
\pi\cot\left(\frac{\pi\sqrt5}{2}\right)
=\pi\cot(\pi\varepsilon)
=\pi\cot\left(\frac{\pi}{2\varphi^3}\right).
}
\]

### 11.2 Euler–zeta expansion

For \(|x|<1\), Euler's partial-fraction expansion yields
\[
\pi\cot(\pi x)
=\frac1x-2\sum_{n=1}^{\infty}\zeta(2n)x^{2n-1}.
\]
Substituting \(x=\varepsilon=1/(2\varphi^3)\) gives the absolutely convergent identity
\[
\boxed{
\pi\cot\left(\frac{\pi}{2\varphi^3}\right)
=2\varphi^3-
2\sum_{n=1}^{\infty}
\zeta(2n)\left(\frac{1}{2\varphi^3}\right)^{2n-1}.
}
\]
All terms in the subtracted series are positive. Thus the partial sums
\[
S_N=\frac1\varepsilon-
2\sum_{n=1}^{N}\zeta(2n)\varepsilon^{2n-1}
\]
decrease to the limit from above.

### 11.3 Bernoulli-number form

With the convention
\[
\frac{x}{e^x-1}=\sum_{m=0}^{\infty}B_m\frac{x^m}{m!},
\]
the even zeta values satisfy
\[
\zeta(2n)=(-1)^{n+1}
\frac{B_{2n}(2\pi)^{2n}}{2(2n)!}.
\]
Therefore the same identity can be written
\[
\boxed{
\pi\cot(\pi\varepsilon)
=\frac1\varepsilon-
\sum_{n=1}^{\infty}
(-1)^{n+1}\frac{B_{2n}(2\pi)^{2n}}{(2n)!}
\varepsilon^{2n-1}.
}
\]
This is a change of representation of the same cotangent series, not a new independent identity. It connects the present evaluation to the Bernoulli-number material through the standard even-zeta formula.

### 11.4 Certified truncation bound

After retaining terms through \(\zeta(2N)\), the omitted tail has negative sign relative to the partial sum:
\[
S_N-\pi\cot(\pi\varepsilon)
=2\sum_{n=N+1}^{\infty}\zeta(2n)\varepsilon^{2n-1}>0.
\]
Since \(\zeta(2n)\leq\zeta(2N+2)\) for \(n\geq N+1\),
\[
0<S_N-\pi\cot(\pi\varepsilon)
\leq
\frac{2\zeta(2N+2)\varepsilon^{2N+1}}{1-\varepsilon^2}.
\]
This supplies an explicit error bound for numerical evaluation.

### 11.5 Numerical check

Using \(\varepsilon=0.1180339887498948482045868343656\ldots\), direct evaluation of the cotangent and the zeta partial sums gives:

| Truncation | Partial sum |
|---|---:|
| \(1/\varepsilon\) (no zeta terms) | 8.472135954999579 |
| through \(\zeta(2)\) | 8.083819696718215 |
| through \(\zeta(4)\) | 8.080260039100665 |
| through \(\zeta(6)\) | 8.080213423332925 |
| through \(\zeta(8)\) | 8.080212782349567 |
| through \(\zeta(10)\) | 8.080212773446790 |
| limit | **8.080212773321099** |

The independently evaluated limit is
\[
\boxed{
\pi\cot(\pi\varepsilon)
=8.0802127733210986785886243049\ldots
}
\]
The value \(8.080620081\) that appeared in an earlier exchange is erroneous and must not be reused. The table above is consistent with the defining cotangent and with the convergent series.

### 11.6 Interpretation and status

The exact results are:
- the algebraic identity \(\varepsilon=1/(2\varphi^3)\);
- the periodic reduction of the cotangent argument;
- the Euler–zeta expansion and its equivalent Bernoulli representation;
- the explicit tail bound and the numerical value above.

If this parameter is motivated by a proposed threshold equation (for example, a zero of a model-dependent quantity \(m_g\)), that motivation is conditional on the validity and assumptions of that external equation. The cotangent calculation does not prove the physical model or the threshold.

No derivation has been established from the face geometry, edge lengths, dihedral angles, seams, or aerodynamics of the truncated icosahedron to this cotangent value. The relationship to the soccer-ball geometry therefore remains **open / not established**; no geometric or physical law is claimed here.

| Item | Statement | Status |
|---|---|---|
| Z1 | \(\varepsilon=(\sqrt5-2)/2=1/(2\varphi^3)\). | Exact algebraic identity |
| Z2 | \(\pi\cot(\pi\sqrt5/2)=\pi\cot(\pi/(2\varphi^3))\). | Exact, by periodicity |
| Z3 | The value has the stated absolutely convergent expansion in \(\zeta(2n)\). | Proved, for \(|\varepsilon|<1\) |
| Z4 | The Bernoulli-number expression is equivalent via the even-zeta formula. | Classical identity |
| Z5 | The truncation error obeys the displayed explicit bound. | Proved |
| Z6 | The cotangent value is derived from truncated-icosahedron geometry or soccer-ball aerodynamics. | Not established; open |
| Z7 | The parameter is a physically justified threshold. | Not established by this analytic calculation; requires independent validation of the model |
