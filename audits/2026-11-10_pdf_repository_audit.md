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
| `18_57.pdf` | `4f5e841771c2` | Per repository-owner identification: Ikeda (1995), spectra of homogeneous spherical spaces. It is not evidence for Weber functions, either eta function, or the (D=-31) class equation. |
| `Mukai.pdf` | `8da87273582b` | Filename alone is insufficient to identify edition/title/content reliably. Pending document-level classification; do not cite from filename. |
| `master05-26-2025.pdf` | `f6a69be2d53e` | Filename alone is insufficient to identify author/title/version. Pending document-level classification; do not cite from filename. |
| `archive/unclassified/zps (1).pdf` | `8bd25231d00c` | Already located under `archive/unclassified/`; retain quarantined until its title, provenance and relevance are established. |

## 2. Direct source audit: Yui–Zagier (1997)

The full paper is available at the author's institutional URL and is also stored in this repository.

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
- `bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md`: corrected DLMF entries 37–38, corrected the citation map, added Khan's Maxwell Optics source and a precise Yui–Zagier scope note.
- `docs/UNITARY_DEDEKIND_DIRICHLET_ETA_BARYCENTRIC_RGS_MORANDOTTI_2026-11-10.md`: corrected DLMF section map and made the Yui–Zagier class-value caveat explicit.

## 6. Remaining PDF work

The three files `Mukai.pdf`, `master05-26-2025.pdf`, and `archive/unclassified/zps (1).pdf` remain unclassified in this audit. No bibliographic details or mathematical relevance have been inferred from their filenames. They need document-level title/author/page inspection before inclusion in a theorem or bibliography.

This is a source and mathematical-claim audit, not a pytest/CI report. No test-suite pass is claimed here.
