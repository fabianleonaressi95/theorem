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
