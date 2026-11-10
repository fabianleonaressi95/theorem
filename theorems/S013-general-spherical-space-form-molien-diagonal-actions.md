# S013 — General scalar spectrum of spherical space forms, Molien theory, and diagonal SU(2) actions

**Record type:** theorem framework plus exact finite-group identities, source audit, and explicitly provisional examples.  
**Status:** the general invariant-theoretic formulas below are proved under the stated hypotheses. The two finite diagonal examples are proved free for the displayed generators and have the stated group orders. Their previously reported spectral coefficient lists remain *numerical, not symbolically certified*. The parameter-family notation \(J^2_{m,n}\), \(J^3_m\) has not been tied to a primary classification source; no uniform theorem for those families is claimed.

**Related records:** [S011](S011-ikeda-binary-tetrahedral-spectrum.md), [S012](S012-ikeda-cyclic-binary-polyhedral-spectra.md).  
**Primary historical source:** A. Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Math. J.* 18 (1995), 57–67, DOI [10.2996/kmj/1138043353](https://doi.org/10.2996/kmj/1138043353).

---

## 1. Scope and conventions

Let \(S^3\subset\mathbb R^4\) be the unit round sphere and let
\[
\Gamma\subset SO(4)
\]
be finite and act freely. The quotient \(S^3/\Gamma\) is a spherical space form. The scalar Laplace spectrum of the unit sphere is
\[
\lambda_n=n(n+2),\qquad n=0,1,2,\ldots,
\]
and the degree-\(n\) spherical-harmonic space \(\mathcal H_n(S^3)\) has dimension \((n+1)^2\).

The quotient eigenspace is naturally
\[
\mathcal H_n(S^3/\Gamma)\simeq\mathcal H_n(S^3)^\Gamma,
\]
so its multiplicity is
\[
d_n(\Gamma)=\dim\mathcal H_n(S^3)^\Gamma.
\]
The zero eigenvalue has multiplicity one when the quotient is connected.

All formulas below use the unit-radius metric. For radius \(R\), eigenvalues are divided by \(R^2\); multiplicities are unchanged.

## 2. Reynolds projector: general multiplicity formula

For a finite group acting linearly on a finite-dimensional complex vector space \(W\), the averaging operator
\[
P_\Gamma=\frac1{|\Gamma|}\sum_{g\in\Gamma}\rho_W(g)
\]
is the projection onto \(W^\Gamma\). Taking its trace gives
\[
\dim W^\Gamma=\frac1{|\Gamma|}\sum_{g\in\Gamma}\chi_W(g).
\]

Applying this to \(W=\mathcal H_n(S^3)\) proves
\[
\boxed{\displaystyle
d_n(\Gamma)=\frac1{|\Gamma|}\sum_{g\in\Gamma}
\chi_{\mathcal H_n}(g).}
\]
This is exact for every finite subgroup of \(SO(4)\); no homogeneity assumption is needed.

### 2.1 Harmonic Molien series in the real four-dimensional representation

Let \(P_n(\mathbb R^4)\) denote homogeneous polynomials of degree \(n\), and let \(\mathcal H_n(\mathbb R^4)\) be the harmonic homogeneous polynomials. The equivariant decomposition
\[
P_n(\mathbb R^4)=\mathcal H_n(\mathbb R^4)\oplus
r^2P_{n-2}(\mathbb R^4)
\]
implies, at the level of invariant Hilbert series,
\[
D_\Gamma(t)=(1-t^2)M_\Gamma(t),
\]
where
\[
M_\Gamma(t)=\frac1{|\Gamma|}
\sum_{g\in\Gamma}\frac1{\det(I-tg)}
\]
is the ordinary Molien series of the real four-dimensional representation. Therefore
\[
\boxed{\displaystyle
D_\Gamma(t)=\sum_{n\ge0}d_n(\Gamma)t^n
=\frac{1-t^2}{|\Gamma|}
\sum_{g\in\Gamma}\frac1{\det(I-tg)}.}
\]
The identity is an equality of formal power series and rational functions. It is the general exact generating function for scalar spherical multiplicities of a specified finite \(SO(4)\)-action.

**Do not confuse the two Molien series:** the four-dimensional real-representation Molien series \(M_\Gamma\) must be multiplied by \(1-t^2\) to obtain harmonic multiplicities. The two-dimensional binary-\(SU(2)\) Molien series used later is a different object.

## 3. The \(SU(2)\times SU(2)\) lift and Peter–Weyl formula

Identify \(S^3\) with \(SU(2)\). The standard double cover is
\[
SU(2)_L\times SU(2)_R\longrightarrow SO(4),
\qquad (a,b):x\longmapsto axb^{-1},
\]
with kernel
\[
\{(1,1),(-1,-1)\}.
\]
Let \(\widetilde\Gamma\) be the full preimage of \(\Gamma\), so
\(|\widetilde\Gamma|=2|\Gamma|\).

The degree-\(n\) spherical-harmonic representation is
\[
\mathcal H_n(S^3)\simeq V_n\otimes V_n^*,
\qquad V_n=\operatorname{Sym}^n(\mathbb C^2),
\]
and the pair \((a,b)\) acts on the two factors. Thus
\[
\boxed{\displaystyle
d_n(\Gamma)=\frac1{|\widetilde\Gamma|}
\sum_{(a,b)\in\widetilde\Gamma}
\chi_n(a)\,\overline{\chi_n(b)},}
\]
where \(\chi_n\) is the character of \(\operatorname{Sym}^n(\mathbb C^2)\). For \(a\in SU(2)\) with eigenvalues \(e^{i\theta},e^{-i\theta}\),
\[
\chi_n(a)=\frac{\sin((n+1)\theta)}{\sin\theta},
\]
with values at \(\sin\theta=0\) defined by continuity. This is the Peter–Weyl/Reynolds formula for a general free double action.

For unit quaternions \(a,b\), the character is real and depends only on their scalar parts. If
\[
\operatorname{Re}(a)=\cos\alpha,\qquad
\operatorname{Re}(b)=\cos\beta,
\]
the real four-dimensional transformation \(x\mapsto axb^{-1}\) has eigen-angle pair \(\alpha+\beta,\alpha-\beta\), and
\[
\boxed{\displaystyle
\det(I-t\rho(a,b))=
[1-2t\cos(\alpha+\beta)+t^2]
[1-2t\cos(\alpha-\beta)+t^2].}
\]
This gives an exact finite Molien sum whenever the finite subgroup of pairs is explicitly known.

### 3.1 Free-action criterion in the lift

The transformation \(x\mapsto axb^{-1}\) fixes a point \(x\in SU(2)\) precisely when
\[
a=xbx^{-1}.
\]
Thus it has a fixed point iff \(a\) and \(b\) are conjugate in \(SU(2)\). Two \(SU(2)\) elements are conjugate iff they have the same trace, equivalently the same real quaternionic part. Hence
\[
\boxed{\Gamma\text{ acts freely on }S^3
\iff
\operatorname{Re}(a)\ne\operatorname{Re}(b)
\text{ for every }(a,b)\in\widetilde\Gamma
\setminus\{(1,1),(-1,-1)\}.}
\]
The two excluded pairs are the kernel of the covering map and represent the identity in \(SO(4)\). This criterion is exact and is particularly useful for finite quaternionic generators.

## 4. Binary groups acting on one side: the two-dimensional Molien relation

Let \(\Delta\subset SU(2)\) act by left multiplication only. Define its two-dimensional invariant Hilbert series
\[
A_\Delta(t)=\sum_{n\ge0}
\dim(V_n^\Delta)t^n
=\frac1{|\Delta|}\sum_{g\in\Delta}
\frac1{\det(I-tg_{\mathbb C^2})}.
\]
Since
\[
\mathcal H_n(S^3)\simeq V_n\otimes V_n^*
\]
and the right factor is untouched, the spherical multiplicity is
\[
d_n=(n+1)\dim(V_n^\Delta).
\]
Therefore
\[
\boxed{\displaystyle
D_\Delta(t)=A_\Delta(t)+tA_\Delta'(t).}
\]
This is not the same as the four-dimensional harmonic Molien formula in §2.1.

For the binary polyhedral groups, the invariant Hilbert series are
\[
A_{2T}(t)=\frac{1+t^{12}}{(1-t^6)(1-t^8)},
\]
\[
A_{2O}(t)=\frac{1+t^{18}}{(1-t^8)(1-t^{12})},
\]
\[
A_{2I}(t)=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]
They are recorded in S011/S012 and provide independent checks of the corresponding three-dimensional formulas in Ikeda's Theorems 4.4(1), 4.5(1), and 4.6(1).

## 5. Binary dihedral multiplicities and the endpoint correction

Use \(Dic_m=D^*_{4m}\subset SU(2)\), of order \(4m\), generated by
\[
a=\operatorname{diag}(e^{i\pi/m},e^{-i\pi/m}),\qquad
b=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
with
\[
a^{2m}=1,\quad b^2=a^m=-I,\quad bab^{-1}=a^{-1}.
\]
The central element \(-I\) acts on \(V_n\) as \((-1)^n\), so there are no invariants for odd \(n\). For \(n=2k\), the weight count gives
\[
\dim V_{2k}^{Dic_m}
=\left\lfloor\frac{k}{m}\right\rfloor
+\frac{1+(-1)^k}{2}.
\]
Consequently the scalar multiplicity for the left quotient is
\[
\boxed{\displaystyle
a_k=(2k+1)\left(
\left\lfloor\frac{k}{m}\right\rfloor+
\frac{1+(-1)^k}{2}\right),\quad
\lambda_k=4k(k+1).}
\]
Equivalently,
\[
a_k=
\begin{cases}
(2k+1)(\lfloor k/m\rfloor+1),&k\text{ even},\\
(2k+1)\lfloor k/m\rfloor,&k\text{ odd}.
\end{cases}
\]
The odd branch is positive starting at \(k=m\), not strictly after \(m\). In particular, if \(m\) is odd, the endpoint \(k=m\) has multiplicity \(2m+1\). This is the coefficient-level correction to the strict inequality as printed/transcribed in Ikeda Theorem 4.3(1). See the corrected statement in [S012](S012-ikeda-cyclic-binary-polyhedral-spectra.md).

### 5.1 First prism eigenvalue and the separate Theorem 5.1 inconsistency

At \(k=2\),
\[
a_2=5\left(\left\lfloor\frac2m\right\rfloor+1\right)
=
\begin{cases}
10,&m=2,\\
5,&m\ge3.
\end{cases}
\]
The eigenvalue is \(\lambda_2=24\). Ikeda's Theorem 5.1 table reports multiplicity \(3\) for \(S^3/D^*_{4m}\), \(m\ge2\). That printed value is incompatible with Theorem 4.3(1) and the direct invariant-weight count. It is a second, logically separate inconsistency:
- Theorem 4.3(1): endpoint/strict-inequality issue in the odd branch;
- Theorem 5.1: first prism eigenvalue multiplicity \(3\), instead of \(10\) for \(m=2\) and \(5\) for \(m\ge3\).

The eigenvalue \(24\) itself is correct. The correction and the distinction are now explicitly recorded in S012.

## 6. Literature propagation and independent checks

This section distinguishes explicit eigenmode construction, later reuse of a multiplicity formula, and a formal correction. A paper's citation of Ikeda does not by itself show that it copied a particular erroneous line.

### 6.1 Lehoucq–Uzan–Weeks (2003)

R. Lehoucq, J.-P. Uzan, J. Weeks, “Eigenmodes of Lens and Prism Spaces,” *Kodai Math. J.* 26 (2003), 119–136, DOI [10.2996/kmj/1050496653](https://doi.org/10.2996/kmj/1050496653), arXiv:[math/0202072](https://arxiv.org/abs/math/0202072).

The article constructs explicit orthonormal eigenmode bases for lens and prism spaces. It is an independent pre-2005 eigenmode treatment and an important cross-check for prism-space spectral calculations. It is not an erratum to Ikeda and should not be described as a formal correction of Theorem 4.3 or 5.1.

### 6.2 Aurich–Lustig–Steiner (2005)

R. Aurich, S. Lustig, F. Steiner, “CMB Anisotropy of Spherical Spaces,” *Class. Quantum Grav.* 22 (2005), 3443, DOI [10.1088/0264-9381/22/17/006](https://doi.org/10.1088/0264-9381/22/17/006), arXiv:[astro-ph/0504656](https://arxiv.org/abs/astro-ph/0504656).

The prism-mode audit identifies omitted low modes at the odd-index boundary for the cases \(m=3\) and \(m=5\):
- \(m=3\): \(k=3\), \(\beta=2k+1=7\), \(\lambda=48\), multiplicity \(7\);
- \(m=5\): \(k=5\), \(\beta=11\), \(\lambda=120\), multiplicity \(11\).

These are precisely the \(k=m\) endpoint modes that the strict \(k>m\) reading would omit. The paper's cosmological calculation is not thereby declared wholly invalid: no complete independent CMB pipeline rerun is contained in this record. The later 2012 paper explicitly lists the 2005 work among the sources whose prism multiplicity error is corrected.

### 6.3 Aurich–Lustig (2012)

R. Aurich, S. Lustig, “How well-proportioned are lens and prism spaces?”, *Class. Quantum Grav.* 29 (2012), 175003, DOI [10.1088/0264-9381/29/17/175003](https://doi.org/10.1088/0264-9381/29/17/175003), arXiv:[1201.6490](https://arxiv.org/abs/1201.6490).

Table 1 explicitly says that an error in Ikeda (1995), Aurich–Lustig–Steiner (2005), and Lustig's 2007 dissertation is corrected. It gives a prism multiplicity expression in terms of \(\beta\) and the deck-group parameter. This is a published mathematical correction in a later paper, not a formal journal erratum attached to Ikeda's 1995 article.

For the prism space, the table uses the wave-number convention
\[
\beta=2k+1,\qquad E_\beta=\beta^2-1=4k(k+1).
\]
Its multiplicity formula is to be translated carefully into the \(k\)-convention before comparison; \(\beta\) is not the harmonic degree \(n\) itself.

### 6.4 2026 representation-theoretic preprint

V. Martin, A. Merino, R. Poddar, S. Roby, “Representation theory and massive spectral zeta functions on spherical space forms,” arXiv:[2611.05490v1](https://arxiv.org/abs/2611.05490), submitted 3 November 2026.

The preprint uses Peter–Weyl and Molien methods for lens spaces and the ADE binary subgroups, including prism spaces and the binary tetrahedral, octahedral, and icosahedral quotients. It states that the work is in preparation for submission to the *Journal of Mathematical Physics*; at this record date it is a preprint, not a peer-reviewed publication.

Its binary-dihedral formula (Corollary 5.11) is
\[
m_{D_m}(n)=
\begin{cases}
0,&n\text{ odd},\\
(n+1)(\lfloor n/(2m)\rfloor+1),&n\equiv0\pmod4,\\
(n+1)\lfloor n/(2m)\rfloor,&n\equiv2\pmod4.
\end{cases}
\]
Putting \(n=2k\) gives exactly
\[
(2k+1)\left(\lfloor k/m\rfloor+\mathbf1_{2\mid k}\right),
\]
which is the formula in §5. This is an independent modern representation-theoretic confirmation of the corrected dihedral multiplicity formula. It does not repair Ikeda's original publication formally, and its stated ADE scope does not cover every free finite subgroup of \(SO(4)\).

The preprint's Molien series for the three binary polyhedral groups agree with the series in §4:
\[
2T:\frac{1+t^{12}}{(1-t^6)(1-t^8)},\quad
2O:\frac{1+t^{18}}{(1-t^8)(1-t^{12})},\quad
2I:\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]
The massive spectral-zeta continuation and determinant formulas are a separate part of that preprint; this record does not certify every analytic continuation step. The existing analytic audit notes for Proposition 5.4, Theorem 5.6 and Proposition 5.7 are preliminary and the icosahedral Bessel/polylog comparison remains to be completed.

## 7. Diagonal finite subgroups: two explicitly generated examples

The following constructions use the action \(x\mapsto axb^{-1}\) and quaternionic notation. In every case, the quotient of the lift by the diagonal kernel \(\{(1,1),(-1,-1)\}\) is the actual subgroup of \(SO(4)\).

### 7.1 Candidate \(J^2_{2,3}\): binary-dihedral diagonal product

Let
\[
u=e^{\pi i/4},\qquad a=e^{\pi i/3},
\]
and consider the lifted generators
\[
g_1=(i,1),\qquad
g_2=(1,a),\qquad
g_3=(u,j).
\]
The first projection is \(C_8=\langle u\rangle\); the second is
\[
Dic_3=\langle a,j\rangle,\qquad |Dic_3|=12.
\]
The quotient maps
\[
\phi_1:C_8\to C_2,\quad \phi_1(u^r)=r\bmod2,
\]
\[
\phi_2:Dic_3\to C_2,\quad
\phi_2(a^s)=0,\quad\phi_2(ja^s)=1
\]
are surjective. The subgroup generated by the displayed pairs is the corresponding fibre product
\[
\widetilde J^2_{2,3}
=\{(x,y)\in C_8\times Dic_3:\phi_1(x)=\phi_2(y)\}.
\]
Its order is
\[
|\widetilde J^2_{2,3}|=\frac{8\cdot12}{2}=48,
\qquad |J^2_{2,3}|=24.
\]

**Freeness proof.** If \(x=u^r\) has even \(r\), the fibre-product condition forces \(y\in\langle a\rangle\). The real parts of such \(y\) lie in \(\{1,-1,\frac12,-\frac12\}\), whereas the real parts of \(u^r\) for even \(r\) lie in \(\{1,0,-1\}\). Equality is possible only at the common central values \(1\) and \(-1\). If \(r\) is odd, then \(y\in j\langle a\rangle\) has real part zero, while \(\operatorname{Re}(u^r)\ne0\). Thus the only pairs with equal real parts are \((1,1)\) and \((-1,-1)\), the covering kernel. The induced \(SO(4)\)-action is free.

**Status:** the order and freeness are proved for these displayed generators. The identification of the notation \(J^2_{2,3}\) with a named family in a primary classification source is not established.

### 7.2 Candidate \(J^3_3\): tetrahedral diagonal product

Let
\[
u=e^{\pi i/9},\qquad
q=\frac{-1-i-j+k}{2},
\]
and take
\[
\begin{aligned}
g_1&=(e^{\pi i/3},1),\\
g_2&=(1,i),\\
g_3&=(1,j),\\
g_4&=(u,q).
\end{aligned}
\]
The first projection is \(C_{18}=\langle u\rangle\); the second is the binary tetrahedral group \(2T=\langle i,j,q\rangle\), of order 24. The quotient \(2T/Q_8\) is \(C_3\). Let
\[
\phi_1:C_{18}\to C_3,\quad \phi_1(u^r)=r\bmod3,
\]
and let \(\phi_2:2T\to2T/Q_8\simeq C_3\) be the quotient map, with the coset of \(q\) chosen as generator. The generated subgroup is the fibre product
\[
\widetilde J^3_3
=\{(x,y)\in C_{18}\times2T:\phi_1(x)=\phi_2(y)\}.
\]
Hence
\[
|\widetilde J^3_3|=\frac{18\cdot24}{3}=144,
\qquad |J^3_3|=72.
\]

**Freeness proof.** If \(r\equiv0\pmod3\), the fibre-product condition forces the second component into \(Q_8\), whose real parts lie in \(\{-1,0,1\}\). For \(u^r\) with \(3\mid r\), equality of real parts occurs only at \(r=0,9,18\), and the corresponding second components are \(1\) or \(-1\); these are precisely the two elements of the covering kernel. If \(r\not\equiv0\pmod3\), the second component lies in \(2T\setminus Q_8\), whose real parts are \(\pm1/2\). But
\[
\cos(\pi r/9)=\pm1/2
\]
forces \(3\mid r\), a contradiction. Thus the induced \(SO(4)\)-action is free.

**Status:** the order and freeness are proved for these displayed generators. The identification of the notation \(J^3_3\) with a named family in a primary classification source is not established.

### 7.3 General parameter families remain unproved

Previously proposed general generators were
\[
J^2_{m,n}:\quad
g_1=[e^{\pi i/m},1],\quad
g_2=[1,e^{\pi i/n}],\quad
g_3=[e^{\pi i/(2m)},j],
\]
with \(m\) even and \(\gcd(m,n)=1\), and
\[
J^3_m:\quad
g_1=[e^{\pi i/m},1],\quad
g_2=[1,i],\quad g_3=[1,j],\quad
g_4=\left[e^{\pi i/(3m)},\frac{-1-i-j+k}{2}\right],
\]
with \(\gcd(m,6)=3\). Here brackets denote pairs modulo the diagonal central kernel.

These are retained as *candidate presentations only*. The claimed general orders, the full range of freeness conditions, and a closed parameter-dependent Molien factorization have not been proved. In particular, the two verified instances above do not establish the whole parameter families.

### 7.4 Previously computed coefficient lists: provisional only

Earlier floating-point quaternionic closure and character averaging produced the following lists through \(n=20\):
\[
\begin{aligned}
J^2_{2,3}:&\quad
(d_0,\ldots,d_{20})=\\
&(1,0,0,0,1,0,5,0,8,0,7,0,17,0,18,0,23,0,31,0,38);
\end{aligned}
\]
\[
\begin{aligned}
J^3_3:&\quad
(d_0,\ldots,d_{20})=\\
&(1,0,0,0,0,0,1,0,3,0,2,0,6,0,5,0,9,0,10,0,14).
\end{aligned}
\]
Thus the provisional truncated series are
\[
D_{J^2_{2,3}}(t)=
1+t^4+5t^6+8t^8+7t^{10}+17t^{12}
+18t^{14}+23t^{16}+\cdots,
\]
\[
D_{J^3_3}(t)=
1+t^6+3t^8+2t^{10}+6t^{12}+5t^{14}
+9t^{16}+10t^{18}+14t^{20}+\cdots.
\]

**These are not certified exact coefficients.** The enumeration used floating-point quaternion arithmetic and tolerance-based equality. They must not be cited as exact, promoted to theorem statements, or used as a proof of the general parameter formulas. Exact cyclotomic/algebraic-number enumeration, independent group-order verification, and exact character averaging are still required.

For any explicitly enumerated finite pair group \(J\), the exact finite Molien expression is
\[
\boxed{\displaystyle
D_J(t)=\frac{1-t^2}{|J|}
\sum_{(a,b)\in J}
\frac1{
[1-2t\cos(\alpha_a+\beta_b)+t^2]
[1-2t\cos(\alpha_a-\beta_b)+t^2]
},}
\]
where \(\operatorname{Re}(a)=\cos\alpha_a\) and
\(\operatorname{Re}(b)=\cos\beta_b\). This is a rational function once the finite group and its elements are specified. A factorized formula in the family parameters has not been derived.

## 8. Classification and source-provenance corrections

Daniel Allcock, “Spherical Space Forms Revisited,” *Trans. Amer. Math. Soc.* 370 (2018), 5561–5582, DOI [10.1090/tran/7167](https://doi.org/10.1090/tran/7167), arXiv:[1509.00906](https://arxiv.org/abs/1509.00906), gives a simplified treatment of Wolf's classification of finite groups that can act freely and isometrically on a round sphere of some dimension, and removes redundancies from the group list. Its six-structure statement is a classification across sphere dimensions. It is **not**, by itself, a classification of every free four-dimensional real representation \(G\to SO(4)\), and must not be cited as if it supplied a ready-made list of all \(S^3\) actions.

The exact strings \(J^2_{m,n}\) and \(J^3_m\) have not been matched to a reliable primary source in the audit recorded here. An earlier attribution to Mingyang Li's 2025 Berkeley thesis was incorrect: that thesis is on gravitational instantons with conformally Kähler geometry, not the asserted classification of these diagonal spherical groups. An earlier attempted attribution to an Evan Patrick Wright 2013 Stony Brook thesis is also invalid: the located dissertation is *Ricci-Flat Anti-Self-Dual Asymptotically Locally Euclidean 4-Manifolds*, not the asserted four-family classification. These attributions must not be repeated.

The correct classification task is representation-theoretic: specify the finite subgroup of \(SU(2)\times SU(2)\), quotient by the diagonal kernel, and verify that no nonidentity element has a fixed point. Abstract group isomorphism alone does not classify the free \(SO(4)\)-representations.

## 9. Open verification register

| ID | Task | Status |
|---|---|---|
| S013-O1 | Exact cyclotomic enumeration of the two displayed lifted groups | Open |
| S013-O2 | Exact character averages and exact coefficients through \(n=20\) | Open |
| S013-O3 | Derive and factor the rational Molien series for each verified example | Open |
| S013-O4 | Prove or refute the general \(J^2_{m,n}\) presentation, order and freeness conditions | Open |
| S013-O5 | Prove or refute the general \(J^3_m\) presentation, order and freeness conditions | Open |
| S013-O6 | Identify the primary source, if any, for the notation \(J^2_{m,n}\), \(J^3_m\) | Open |
| S013-O7 | Match the examples and parameter families rigorously to the full \(S^3\) free-action classification | Open |
| S013-O8 | Complete the literature audit of the 2007 dissertation and the 2012–2015 follow-up literature | Open |
| S013-O9 | Independently reproduce the full CMB numerical pipeline after restoring omitted prism modes | Open |
| S013-O10 | Complete the icosahedral heavy-mass Bessel/polylog analytic cross-check in arXiv:2611.05490 | Open |

No full CMB recalculation is claimed. No physical or cosmological conclusion is inferred solely from a multiplicity correction.

## 10. Bibliography

1. A. Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Math. J.* 18 (1995), 57–67. DOI: [10.2996/kmj/1138043353](https://doi.org/10.2996/kmj/1138043353).
2. R. Lehoucq, J.-P. Uzan, J. Weeks, “Eigenmodes of Lens and Prism Spaces,” *Kodai Math. J.* 26 (2003), 119–136. DOI: [10.2996/kmj/1050496653](https://doi.org/10.2996/kmj/1050496653); arXiv: [math/0202072](https://arxiv.org/abs/math/0202072).
3. R. Aurich, S. Lustig, F. Steiner, “CMB Anisotropy of Spherical Spaces,” *Class. Quantum Grav.* 22 (2005), 3443. DOI: [10.1088/0264-9381/22/17/006](https://doi.org/10.1088/0264-9381/22/17/006); arXiv: [astro-ph/0504656](https://arxiv.org/abs/astro-ph/0504656).
4. R. Aurich, S. Lustig, “How well-proportioned are lens and prism spaces?”, *Class. Quantum Grav.* 29 (2012), 175003. DOI: [10.1088/0264-9381/29/17/175003](https://doi.org/10.1088/0264-9381/29/17/175003); arXiv: [1201.6490](https://arxiv.org/abs/1201.6490).
5. D. Allcock, “Spherical Space Forms Revisited,” *Trans. Amer. Math. Soc.* 370 (2018), 5561–5582. DOI: [10.1090/tran/7167](https://doi.org/10.1090/tran/7167); arXiv: [1509.00906](https://arxiv.org/abs/1509.00906).
6. V. Martin, A. Merino, R. Poddar, S. Roby, “Representation theory and massive spectral zeta functions on spherical space forms,” arXiv: [2611.05490v1](https://arxiv.org/abs/2611.05490), 3 November 2026. Preprint; not peer reviewed at the date of this record.

## 11. Final epistemic status

- **Proved:** Reynolds averaging; harmonic Molien formula; \(SU(2)\times SU(2)\) character formula; determinant identity; free-action criterion; binary-dihedral invariant dimension formula; order and freeness of the two explicitly displayed diagonal examples.
- **Source-checked / independently reconstructed:** Ikeda's three-dimensional binary-group formulas in S011/S012, with the two distinct prism errors explicitly separated.
- **Independent published confirmation:** Lehoucq–Uzan–Weeks explicit prism eigenmodes; Aurich–Lustig 2012 published correction; Martin–Merino–Poddar–Roby 2026 preprint formula.
- **Numerically observed only:** the two truncated coefficient lists in §7.4.
- **Candidate only:** the general \(J^2_{m,n}\) and \(J^3_m\) presentations.
- **Open:** exact enumeration, general parameter formulas, primary provenance of the \(J\)-notation, complete \(S^3\) representation classification comparison, full CMB rerun, and remaining analytic checks of the 2026 preprint.

The record is deliberately not a claim that all spherical space-form spectral theory is solved. It establishes a general exact framework, documents the Ikeda correction chain, and separates the proved finite examples from the still-open parameter-family and computational work.
