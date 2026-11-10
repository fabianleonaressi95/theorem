# Repository PDF audit — 10 November 2026

**Repository:** `fabianleonaressi95/theorem`  
**Branch inspected:** `main`  
**Audit scope:** complete PDF inventory (13 files), with focused source audit of the Dedekind/Weber/Dirichlet-eta and Gamma/Beta/Morandotti references. A PDF filename alone is not treated as bibliographic metadata. Files not positively identified are left pending rather than guessed.

## 1. Complete PDF inventory

The following 13 PDF blobs were present in the recursive Git tree at the time of inspection.

| Repository path | Blob SHA (prefix) | Identification / treatment |
|---|---|---|
| `S0025-5718-97-00854-5.pdf` | `961adee998c5` | Yui–Zagier (1997), *On the Singular Values of Weber Modular Functions*. Primary source for Weber definitions, transformation laws and the (D=-31) table entry. Audited against the full text and pp. 1647–1649. |
| `JTNB_2002__14_1_325_0.pdf` | `f55f51a601d6` | Reinhard Schertz (2002), *Weber's Class Invariants Revisited*. Primary source for the singular-value framework, Weber functions and multiplier conventions. |
| `DLMF_ §23.18 Modular Transformations ‣ Modular Functions ‣ Chapter 23 Weierstrass Elliptic and Modular Functions.pdf` | `7958a195078e` | NIST DLMF §23.18, modular transformations. Relevant to Dedekind eta and modular functions. |
| `DLMF_ §25.2 Definition and Expansions ‣ Riemann Zeta Function ‣ Chapter 25 Zeta and Related Functions.pdf` | `aee82919a3b1` | NIST DLMF §25.2, zeta definition and expansions; includes the alternating eta identity at Eq. 25.2.3. |
| `DLMF_ NIST Digital Library of Mathematical Functions.pdf` | `6bce316da42d` | General DLMF reference PDF; cite exact sections, not the whole handbook for a specific identity. |
| `minka-dirichlet.pdf` | `2da3b96f1d5c` | Thomas P. Minka, *Estimating a Dirichlet Distribution* (2000; revisions through 2012). Supports Gamma normalization, expected log coordinates and digamma gradients. |
| `mit18_785f21_lec19.pdf` | `0bc82cf66b37` | A. V. Sutherland, MIT 18.785 Lecture 19, *The Analytic Class Number Formula* (15 Nov 2021). Supports the Dedekind-zeta residue/class-number step. |
| `2203.12769v1.pdf` | `817657f30970` | Amar–Matias–Morandotti–Zappale, *Periodic Homogenization in the Context of Structured Deformations*. Published in ZAMP 73 (2022), article 173, DOI 10.1007/s00033-022-01817-6. Applies under its stated Euclidean periodic hypotheses; it does not prove curved-shell homogenization. |
| `0205083v1.pdf` | `58bda11d547f` | Sameen Ahmed Khan, *Maxwell Optics: I. An Exact Matrix Representation of the Maxwell Equations in a Medium*, Physica Scripta 71 (2005), 440–442; arXiv:physics/0205083. Background on 8×8 Maxwell matrix representations, not a derivation of the RGS fourth-moment constitutive ansatz. |
| `18_57.pdf` | `4f5e841771c2` | **IDENTIFIED / SCOPE-VERIFIED:** Akira Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Mathematical Journal* 18 (1995), 57–67. Source: J-STAGE full paper. It derives Poincaré series and Laplace spectra/multiplicities for homogeneous spherical space forms associated with cyclic, binary dihedral, binary tetrahedral, binary octahedral and binary icosahedral groups. Relevant to the spherical-spectrum/finite-group strand; irrelevant as evidence for Dedekind/Dirichlet eta, Weber invariants, \(\mathbb Q(\sqrt{-31})\), or barycentric Dirichlet covariance. |
| `Mukai.pdf` | `8da87273582b` | Filename alone is insufficient to identify edition/title/content reliably. Pending document-level classification; do not cite from filename. |
| `master05-26-2025.pdf` | `f6a69be2d53e` | Filename alone is insufficient to identify author/title/version. Pending document-level classification; do not cite from filename. |
| `archive/unclassified/zps (1).pdf` | `8bd25231d00c` | Already located under `archive/unclassified/`; retain quarantined until its title, provenance and relevance are established. |

## 2. Source audit: Yui–Zagier (1997) — provenance recorded

The full paper is stored in this repository as `S0025-5718-97-00854-5.pdf`. The page-by-page checks reported here (pp. 1645–1662, including B1–B6 and the numerical principal-value check) were performed by the user after reading the complete paper on a mirror. They are recorded as user-performed verification, not as a separate assistant re-reading in this audit.

- **p. 1647:** defines the classical Weber functions and their transformation under (	aumapsto	au+1) and (	aumapsto-1/	au); defines the class invariant (f(Q)).
- **p. 1648:** gives the alternate formula
  [
  f(A)=epsilon_dzeta^{-1}f_2(	au_Q)
      =epsilon_drac{sqrt2}{f(2	au_Q-1)}
  ]
  for a suitably chosen representative, and explicitly states that the assertion that all (f(A)), rather than only their squares/up-to-sign values, are conjugates is conjectural in their treatment.
- **p. 1649, Table 1:** for (|d|=31), (h(d)=3) and coefficient row (1,0,1,-1), i.e.
  [
  W_{-31}(X)=X^3+X-1.
  ]

For the principal form (Q_0=[1,1,8]), the definition on p. 1647 gives
[
f(Q_0)=zeta_{48}f_2(	au_0),qquad
	au_0=rac{-1+isqrt{31}}2,
]
because (epsilon_{-31}=1) and (b(a-c+a^2c)=1). This is consistent with the S.9 normalization.

**Scope correction:** the table entry is the published Weber class-polynomial/minimal-polynomial result used for the principal invariant. The paper's separate conjectural assertion about all class values being conjugates must not be promoted to a theorem. S.9 now says so explicitly and does not depend on that stronger assertion.

## 3. Eta quotient and numerical cross-check

With (q=e^{2pi i	au}),
[
f(	au)=e^{-pi i/24}
rac{eta_{m Ded}((	au+1)/2)}{eta_{m Ded}(	au)}
=q^{-1/48}prod_{nge1}(1+q^{n-1/2}).
]
The product identity follows by splitting the numerator factors into even and odd indices and cancelling the even factors against (prod_{nge1}(1-q^n)).

At (	au=isqrt{31}), high-precision independent evaluation gives
[
psi=1.465571231876768026656731225219939108ldots,
]
[
sqrt2,psi
=2.072630712743969426305340645406994491ldots,
]
[
f(isqrt{31})
=2.072630712743969426305340645406994491ldots.
]
The difference is below (4	imes10^{-60}) at the working precision. This is consistent with the exact Weber transformation chain in S.9.

The terminology is now explicit:
- plastic constant (p): (p^3-p-1=0), (papprox1.3247179572);
- project supergolden number (psi): (psi^3-psi^2-1=0), (psiapprox1.4655712319).

Thus (sqrt2p
e f(isqrt{31})), while (sqrt2psi=f(isqrt{31})). The earlier numerical objection used the plastic constant in place of the project's supergolden root.

## 4. NIST section correction

Two earlier section assignments were wrong and have been corrected:

- Dedekind eta is in **DLMF Chapter 23**, notably §§23.15 and 23.18. It is not DLMF §27.14.
- The alternating zeta/Dirichlet eta identity is in **DLMF §25.2**, Eq. 25.2.3. DLMF §20.10 is not the source for the Dirichlet eta Mellin integral used in S.10.

The Gamma/Beta/polygamma and Bernoulli references are now mapped to DLMF Chapter 5 and §24.2, respectively. The Mellin identity
[
Gamma(s)eta_D(s)=int_0^inftyrac{x^{s-1}}{e^x+1},dx
]
is derived directly in S.10 by expanding the Fermi kernel and integrating termwise; it is not attributed to §20.10.

## 5. Files updated in this audit

- `theorems/S009-weber-dedekind-eta-supergolden-class-invariant.md`: source caveat, class-field scope, corrected DLMF references.
- `theorems/S010-dirichlet-eta-lambert-series-quadratic-zeta.md`: completely cleaned and corrected reference section; removed the malformed duplicate tail and invalid DLMF §20.10 attribution.
- `theorems/S011-ikeda-binary-tetrahedral-spectrum.md`: verified index convention, subgroup inclusion–exclusion, Ikeda multiplicity formula, independent Molien derivation and initial multiplicities; explicitly excludes any eta/Weber attribution.
- `bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md`: corrected DLMF entries 37–38, corrected the citation map, added Khan's Maxwell Optics source and a precise Yui–Zagier scope note.
- `docs/UNITARY_DEDEKIND_DIRICHLET_ETA_BARYCENTRIC_RGS_MORANDOTTI_2026-11-10.md`: corrected DLMF section map and made the Yui–Zagier class-value caveat explicit.

## 6. Remaining PDF work

The three files `Mukai.pdf`, `master05-26-2025.pdf`, and `archive/unclassified/zps (1).pdf` remain unclassified in this audit. No bibliographic details or mathematical relevance have been inferred from their filenames. They need document-level title/author/page inspection before inclusion in a theorem or bibliography.

This is a source and mathematical-claim audit, not a pytest/CI report. No test-suite pass is claimed here.


## M. Explicit correction and classification — quadratic character sum and Ikeda (1995)

### M.1 The finite character sum is \(-93\)

For \(D=-31\), the primitive quadratic character is \(\chi_{-31}(a)=(a/31)\). Its quadratic residues in \(1,\ldots,30\) are
\[
\{1,2,4,5,7,8,9,10,14,16,18,19,20,25,28\},
\]
whose sum is \(186\). The complementary nonresidues are
\[
\{3,6,11,12,13,15,17,21,22,23,24,26,27,29,30\},
\]
whose sum is \(279\). Since \(1+\cdots+30=465\), the signed sum is
\[
\sum_{a=1}^{30}a\chi_{-31}(a)=186-279=-93.
\]
The previous conversational values \(-63\) and \(-33\) were both arithmetic errors. In particular, the earlier claimed total \(30\cdot31/2=495\) was wrong; it is \(465\). The repository's original value \(-93\) and the resulting formula
\[
L(1,\chi_{-31})=-\frac{\pi}{31^{3/2}}(-93)
=\frac{3\pi}{\sqrt{31}}
\]
are correct. The odd-character finite formula follows from the standard Gauss-sum expression for \(L(1,\chi)\); for this quadratic character, \(\tau(\chi_{-31})=i\sqrt{31}\).

### M.2 What Ikeda (1995) does and does not establish

The PDF 18_57.pdf is positively identified as Akira Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Mathematical Journal* 18 (1995), 57–67. The publisher-hosted J-STAGE PDF is:
https://www.jstage.jst.go.jp/article/kodaimath1978/18/1/18_1_57/_pdf/-char/en

The paper's introduction (p. 57) defines the spherical quotient \(S^{2n-1}/G\), the Laplacian eigenvalues and multiplicities, and the associated Poincaré series. Section 3 (pp. 59–60) discusses Wolf's classification and the cyclic, binary dihedral, binary tetrahedral, binary octahedral and binary icosahedral groups. Section 4 (pp. 60–66) computes the spectra and multiplicities. Therefore classify this PDF as **VERIFIED — relevant to homogeneous spherical spectra and finite-group quotient geometry**. It is **NOT RELEVANT** as a source for Dedekind eta, Dirichlet eta, Weber functions, the field \(\mathbb Q(\sqrt{-31})\), the character \(\chi_{-31}\), Euler Beta/Gamma simplex integrals, or barycentric covariance. No such connection is claimed in S.9/S.10.

### M.3 Status register for the 13 repository PDFs

- **Verified and directly relevant to Weber/eta/CM:** Yui–Zagier (1997), Schertz (2002), DLMF §§23.15/23.18.
- **Verified and directly relevant to Dirichlet eta, zeta, Bernoulli, Gamma/Beta/polygamma:** DLMF §25.2, DLMF §25.15, general DLMF with exact sections, Minka, and MIT 18.785 Lecture 19 for the class-number formula.
- **Verified, relevant to the Morandotti/structured-deformation strand under the paper's own assumptions:** Amar–Matias–Morandotti–Zappale (2022).
- **Verified, relevant only as background for matrix Maxwell formulations:** Khan (2005).
- **Verified, relevant to spherical spectra / finite groups but not the eta/CM calculation:** Ikeda (1995), 18_57.pdf.
- **Pending identification / content audit:** Mukai.pdf and master05-26-2025.pdf; do not cite or use until their title pages, authorship, version and mathematical contents are inspected.
- **Quarantined:** archive/unclassified/zps (1).pdf; retain outside the evidentiary chain until provenance and relevance are established.

This status register distinguishes inventory completeness from semantic review completeness: all 13 PDFs are inventoried, but the three files named above remain unclassified (two pending and one quarantined). It does not claim a complete page-by-page audit of every PDF.


### M.4 Exact verification of Ikeda's binary-tetrahedral formula

The source statements and independent reconstructions are recorded separately in `theorems/S011-ikeda-binary-tetrahedral-spectrum.md`. The repository PDF `18_57.pdf` is the source used for the quoted Ikeda statements.

- **Index:** the general (S^3) harmonic degree is \(\ell\), with eigenvalue \(\ell(\ell+2)\). Ikeda's binary-tetrahedral index is \(\ell=2k\), so \(\lambda_k=4k(k+1)\). This is a reconstruction from the standard sphere eigenvalue and \\(\\ell=2k\\). Ikeda's Theorem 4.4(2) is stated for \\(n>1\\), so it does not itself cover \\(S^3/T^*\\); the \\(n=1\\) agreement is algebraic only.
- **Subgroup average:** Proposition 3.1(2) gives four cyclic subgroups of order 6 and three of order 4, all sharing the central (C_2). Their union has size (4(6-2)+3(4-2)+2=24). Inclusion–exclusion gives exactly
  \[F_{T^*}=\frac{24F_6+12F_4-12F_2}{24}
  =F_6+\frac12F_4-\frac12F_2,\]
  matching the coefficients printed in the p. 63 Poincaré-series formula.
- **Molien:** the defining (SU(2)) representation gives
  \[M(t)=\frac1{24}\left[
  \frac1{(1-t)^2}+\frac1{(1+t)^2}+\frac6{1+t^2}
  +\frac8{1-t+t^2}+\frac8{1+t+t^2}\right]
  =\frac{1+t^{12}}{(1-t^6)(1-t^8)}.\]
  Its even-degree coefficient is
  \[m_{2k}=1+2\lfloor k/3\rfloor+\lfloor k/2\rfloor-k.\]
  Multiplication by the other (SU(2)) factor's dimension (2k+1) recovers Ikeda's
  \[a_k=(2k+1)m_{2k}.\]
- **Numerical spot checks:** (k=3): (m_6=1, a_3=7); (k=6): (m_{12}=2, a_6=26). The initial table is in S011.
- **Scope:** Ikeda supports the spherical-spectrum and finite-group quotient strand only. It does not support a Weber/Dedekind-eta/Dirichlet-eta or \(\mathbb Q(\sqrt{-31})\) connection.



## M.5 Provenance and correction register — Weber/Ikeda

- **Ikeda (1995):** the source statements in `18_57.pdf` are recorded as directly present in the repository PDF: Proposition 3.1(2), p. 63 coefficient combination, and Theorem 4.4(1). Theorem 4.4(2) is explicitly scoped to `n>1`; it is not cited as covering `S^3/T*`. The eigenvalue `4k(k+1)` is an independent reconstruction from `ell=2k` and the unit-sphere eigenvalue. The Molien calculation is also an independent check.
- **Yui–Zagier (1997):** B1–B6 page checks and the 40-digit numerical check are attributed to the user's reported reading of the complete paper, pp. 1645–1662. Do not claim that these checks were independently repeated by the assistant. The `D=-31` polynomial is a tabulated published result; `rho=psi_*^{-1}` is an algebraic reconstruction, and the term `supergolden` is not attributed to Yui–Zagier.
- **Congruence:** the general abbreviated phase/sign condition is `b ≡ -a (mod 48)`, not modulo 24; the user-reported counterexample `[1,23,140]` must be retained in S009.
- **Class values:** the all-classes conjugacy statement remains conjectural in Yui–Zagier. The principal-class conclusion does not rely on that conjecture.
- **Erroneous alternate Molien formula:** do not use `(1+t^6)/((1-t^4)(1-t^6))` for `T*`; the correct binary-tetrahedral Hilbert series in S011 is `(1+t^12)/((1-t^6)(1-t^8))`.
- **CM points:** `(-1+i sqrt(31))/2` has discriminant `-31`; `i sqrt(31)` has order discriminant `-124`. The Weber transformation through the equivalent principal-class representative `(1+i sqrt(31))/2` connects the evaluations. The discriminant distinction does not refute the transformation identity.


## M.6 Final correction register — Ikeda and the binary-tetrahedral invariant space

The corrected independent reconstruction uses invariants in the defining binary-tetrahedral representation, not the commutant:
\[
a_\ell=(\ell+1)\dim\bigl(\operatorname{Sym}^{\ell}(\mathbb C^2)^{T^*}\bigr).
\]
Peter–Weyl gives \(L^2(SU(2)/T^*)\cong\bigoplus_\ell H_\ell\otimes(H_\ell^*)^{T^*}\); the invariant dimension is taken in one factor, while the other factor contributes \(\dim H_\ell=\ell+1\). The previous expression \(\dim(\operatorname{End}(H_\ell)^{T^*})\) counts a commutant and is the wrong quantity for this quotient spectrum. Any table derived from that commutant, in particular one with positive multiplicities at odd \(\ell\), is withdrawn.

The central element \(-I\in T^*\) acts on \(\operatorname{Sym}^{\ell}(\mathbb C^2)\) by \((-1)^\ell\), so odd-degree invariant spaces vanish. The independently derived Molien series is
\[
M(t)=\frac{1+t^{12}}{(1-t^6)(1-t^8)},\qquad
c_\ell=[t^\ell]M(t),
\]
and the spherical multiplicity is \(a_\ell=(\ell+1)c_\ell\). Since only even degrees survive, set \(\ell=2k\); coefficient extraction gives
\[
c_{2k}=1+2\left\lfloor\frac{k}{3}\right\rfloor
+\left\lfloor\frac{k}{2}\right\rfloor-k,
\quad
a_{2k}=(2k+1)c_{2k}.
\]
This agrees with the formula printed in Ikeda Theorem 4.4(1), including zero multiplicities at \(k=1,2,5\). This is an independent Molien/Peter–Weyl verification of the source formula, not a replacement for the source citation.

**Do not confuse the two index conventions:** \(\ell\) is the full spherical-harmonic degree and \(\lambda_\ell=\ell(\ell+2)\) on the unit \(S^3\); Ikeda's binary-tetrahedral index is \(k\), with \(\ell=2k\), hence \(\lambda_k=4k(k+1)\). Theorem 4.4(2) has the explicit restriction \(n>1\); its algebraic \(n=1\) specialization does not extend its theorem or multiplicity statement to \(S^3/T^*\). Theorem 4.4(1) is the relevant \(S^3/T^*\) multiplicity formula.

The Molien series \((1+t^6)/((1-t^4)(1-t^6))\) previously asserted in a draft is **not** the binary-tetrahedral invariant series and must not be reintroduced. The correct series is the one displayed above. S011 is the canonical detailed record and is not to be rewritten merely to reflect a superseded objection.

## M.7 Yui–Zagier: source status and exact scope

The repository contains the complete Yui–Zagier paper as S0025-5718-97-00854-5.pdf. The page-specific checks B1–B6 in this audit are attributed to the user's reported reading of the full article, pp. 1645–1662, and numerical checks; they are not represented as a fresh assistant-side PDF read. In particular:

- The principal form \(Q_0=[1,1,8]\) and \(\tau_0=(-1+i\sqrt{31})/2\) are the \(d=-31\) principal-form data (p. 1647).
- Table 1 (p. 1649) lists \(W_{-31}(X)=X^3+X-1\), with class number 3 and coefficient row \(1,0,1,-1\). It is a tabulated numerical class-invariant result in the paper, not a formal proof of every broader class-value assertion.
- The identity \(f(i\sqrt{31})=\sqrt2\,\psi_*\), with \(\psi_*^3-\psi_*^2-1=0\), is not refuted by the fact that \(i\sqrt{31}\) has order discriminant \(-124\) whereas \(\tau_0\) has discriminant \(-31\). The Weber transformation is applied through the equivalent principal-class representative \(\tau=(1+i\sqrt{31})/2\), for which \(2\tau-1=i\sqrt{31}\). The relation \(\rho=1/\psi_*\), \(\rho^3+\rho-1=0\), is an elementary algebraic reconstruction; “supergolden” is project terminology, not Yui–Zagier terminology.
- Preserve the reported sign/congruence caveat: the abbreviated condition \(b\equiv-a\pmod{24}\) does not determine a 48th-root-of-unity phase. The reported counterexample \([1,23,140]\) shows why the sign-sensitive representative condition must be handled modulo 48 in that transformation. This correction does not invalidate the principal-class calculation using \([1,-1,8]\).
- The paper's stronger assertion that all \(f(A)\), rather than only their squares/up-to-sign values, are conjugates is stated conjecturally by the authors. Do not promote it to a theorem or extend the principal-class conclusion to all three classes without a separate proof.

**Repository policy:** keep the source result, independent algebra, numerical agreement and conjectural extension in separate labels. Do not label the Weber transformation false solely because the two displayed CM points have different order discriminants.

## M.8 T073 referee audit — no global theorem follows from the current hypotheses

T073 remains **OPEN**. The referee analysis supplied for this audit identifies the following obligations, now made explicit in the T073 record:

1. **Intrinsic function spaces:** define \(SBV(S;\mathbb R^m)\), traces, jump sets and \(\nabla_Sg-G\) on the surface, with compatible charts/frames and uniform control for the approximating surfaces.
2. **Coercivity and compactness:** coercivity in \(\nabla_Sg\) alone does not bound \(G\). A joint bound in \(A=\nabla_Sg\) and \(B=G\), or a bound on \(A-B\) together with a bound on \(A\), is a sufficient route to \(L^p\)-control of \(G\). SBV compactness also needs control of jump measure and an \(L^1\) bound or normalization; these do not follow from shape regularity.
3. **Geometry:** require appropriate geometric convergence of \(S_h\to S\), uniformly controlled element maps, metrics/measures and one-sided normals. Shape regularity by itself does not establish these.
4. **L1–L6 remain separate:** compactness; localisation/Radon representation; intrinsic relaxation/cell density; liminf; recovery; and discrete-continuous transfer. L3 is especially nontrivial on a general compact surface because there is no global translation group; an effective density may depend on position, tangent plane and curvature.
5. **Seam modelling:** distinguish the prescribed panel-seam network \(\Gamma_{\rm phys}\) from the variational jump set \(S_g\). Choose a kinematic constraint, a cohesive interface, or a geometric seam with separately specified admissible traces. Prevent double counting between seam and jump energies. Test aligned and non-aligned mesh seams separately.
6. **Convergence hierarchy:** Γ-convergence, Mosco convergence, operator/resolvent convergence and spectral convergence are distinct claims. The latter steps require explicit comparison maps, closed forms/domains, compactness and (for spectral conclusions) compact-resolvent/multiplicity control.

The proposed coercivity \(W(X,A,B)\ge c(|A|^p+|B|^p)-C\), \(p>1\), is a useful sufficient hypothesis, not a necessary characterization. Likewise, a surface version of the Euclidean periodic structured-deformation theorem is not established merely by replacing \(\nabla\) with \(\nabla_S\). The referee's proposed short list H1–H5 is not, by itself, a proof of Γ-convergence: compactness, intrinsic relaxation, liminf and recovery still require complete statements and proofs.

**No change to the status:** T073 is a research programme/checklist. No curved-shell Γ-limit, Mosco limit, operator convergence or spectral convergence is claimed. The update is a clarification of proof obligations, not a theorem promotion.
