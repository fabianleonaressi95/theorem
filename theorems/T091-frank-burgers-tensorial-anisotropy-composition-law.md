# T091 — Frank–Burgers tensorial interaction and anisotropy composition law

**Date:** 11 November 2026  
**Status:** exact discrete tensor identity proved under linear reconstruction; five-level numerical verification completed for the stated two-core benchmark; continuum limit, constitutive interpretation and universal distance law remain open.  
**Dependencies:** PR #161, PR #162; the operational anisotropy definitions in MORANDOTTI_ANISOTROPY.md.

## 1. Scope and hypotheses

Let \(\mathcal T_h\) be a fixed finite-element mesh of a two-core domain and let \(\mathcal F_h^{\mathrm{int}}\) denote its interior facets. Let the discrete Airy reconstruction be linear in its source data. Split the source into a Frank/disclination part and a Burgers/dislocation part,
\[
\Phi=\Phi_F+\Phi_B.
\]
Linearity gives
\[
\sigma_h(\Phi)=\sigma_{F,h}+\sigma_{B,h}.
\]
Use the same facet-normal and jump convention for all three fields and define
\[
j_F=\llbracket\sigma_{F,h}n\rrbracket,\qquad
j_B=\llbracket\sigma_{B,h}n\rrbracket,\qquad
j=j_F+j_B.
\]
All integrals below are over \(\mathcal F_h^{\mathrm{int}}\), with the same facet measure and quadrature convention as the assembled audit.

This statement concerns the discrete reconstructed stress and its interior-facet traction jump. It is not a constitutive material law and does not identify the Airy stress with a velocity or circulation field.

## 2. Tensorial interaction law

Define the Frank and Burgers second-moment tensors by
\[
T_F=\int j_F\otimes j_F\,dS,\qquad
T_B=\int j_B\otimes j_B\,dS,
\]
and define the symmetric mixed interaction tensor
\[
T_{FB}=\int
\left(j_F\otimes j_B+j_B\otimes j_F\right)\,dS.
\]
The total traction-jump second moment is
\[
T=\int j\otimes j\,dS.
\]

**Theorem (discrete Frank–Burgers tensor composition).** Under the hypotheses in Section 1,
\[
\boxed{T=T_F+T_B+T_{FB}.}
\tag{91.1}
\]
Consequently,
\[
\boxed{
\int |j|^2\,dS
=\int|j_F|^2\,dS+\int|j_B|^2\,dS
+2\int j_F\cdot j_B\,dS.
}
\tag{91.2}
\]
For every unit direction \(u\in\mathbb R^2\),
\[
\boxed{
u^TTu
=\int (u\cdot j_F)^2\,dS
+\int (u\cdot j_B)^2\,dS
+2\int (u\cdot j_F)(u\cdot j_B)\,dS.
}
\tag{91.3}
\]
The mixed term is signed. It may be positive, negative or zero; it must not be dropped or replaced by the sum of two independent sector scores.

### Proof

Since \(j=j_F+j_B\), expand
\[
j\otimes j
=j_F\otimes j_F+j_B\otimes j_B
+j_F\otimes j_B+j_B\otimes j_F.
\]
Integrating gives (91.1). Taking the trace and using
\(\operatorname{tr}(a\otimes b)=a\cdot b\) gives (91.2). Contracting (91.1) with \(u\) on both sides gives (91.3). No asymptotic or constitutive assumption is used. \(\square\)

## 3. Anisotropy composition law

Let \(e_\parallel\) be the unit vector joining the two core centres and let \(e_\perp\) be its in-plane orthogonal unit vector. For any symmetric tensor \(X\), define
\[
s(X)=\operatorname{tr}X,\qquad
\delta(X)=e_\parallel^TXe_\parallel-e_\perp^TXe_\perp.
\]
For \(s(T)>0\), define the signed axis-resolved anisotropy
\[
\mathcal A_\parallel(T)=\frac{\delta(T)}{s(T)}.
\]
By (91.1), both numerator and denominator split exactly:
\[
\delta(T)=\delta(T_F)+\delta(T_B)+\delta(T_{FB}),
\]
\[
s(T)=s(T_F)+s(T_B)+s(T_{FB}).
\]
Therefore the **Frank–Burgers anisotropy composition law** is
\[
\boxed{
\mathcal A_\parallel(T)=
\frac{\delta(T_F)+\delta(T_B)+\delta(T_{FB})}
{s(T_F)+s(T_B)+s(T_{FB})}.
}
\tag{91.4}
\]
The denominator is the total squared jump and is nonnegative; it is positive unless the jump vanishes almost everywhere. The mixed contribution to the directional contrast is not determined by the scalar mixed norm alone: the full tensor \(T_{FB}\), including its off-diagonal entry, is required.

The benchmark also reports the rotation-invariant eigenvalue anisotropy
\[
\mathcal A_{\mathrm{eig}}(T)=
\frac{\lambda_{\max}(T)-\lambda_{\min}(T)}
{\lambda_{\max}(T)+\lambda_{\min}(T)}
=
\frac{\sqrt{(T_{11}-T_{22})^2+4T_{12}^2}}
{\operatorname{tr}T},
\tag{91.5}
\]
when \(\operatorname{tr}T>0\). This is a nonlinear scalar function of the total tensor; in general it is **not** the sum or weighted average of the separate sector eigenvalue anisotropies. Equation (91.1), not an additive scalar anisotropy score, is the exact composition statement.

## 4. Five-level numerical verification

The merged five-level DOLFINx 0.11.0 workflow used equal circular cores of radius \(0.12\), centre separation \(0.56\), \(E=1\), \(\nu=0\), and target mesh sizes
\[
h=0.08,\ 0.06,\ 0.045,\ 0.035,\ 0.027.
\]
For the mixed disclination–dislocation source case, the report gives:

| \(h\) | cells | \(\|j\|_{L^2}\) | \(\|j_F\|_{L^2}\) | \(\|j_B\|_{L^2}\) | \(2\langle j_F,j_B\rangle\) | mixed share of \(\|j\|^2\) | \(\mathcal A_{\rm eig}(T)\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.080 | 1,265 | 9.9205e-3 | 7.4448e-3 | 3.9903e-3 | 2.70695e-5 | 27.51% | 0.09767 |
| 0.060 | 2,145 | 4.8440e-3 | 3.1950e-3 | 2.8349e-3 | 5.21961e-6 | 22.24% | 0.17414 |
| 0.045 | 3,642 | 3.6864e-3 | 2.4571e-3 | 2.2855e-3 | 2.32907e-6 | 17.14% | 0.19076 |
| 0.035 | 5,996 | 2.9916e-3 | 1.9843e-3 | 1.8368e-3 | 1.63867e-6 | 18.31% | 0.19337 |
| 0.027 | 9,881 | 2.3754e-3 | 1.5371e-3 | 1.4912e-3 | 1.05594e-6 | 18.71% | 0.21689 |

The mixed cross-term additivity residual is between approximately \(10^{-17}\) and \(10^{-18}\) in absolute value across these five levels. In this particular mixed-source run the signed cross term is positive at every level and contributes about 17–28% of the total squared traction jump. This sign is an observed property of this source configuration, not a universal sign theorem.

The total jump norm decreases along the tested refinement sequence, while the reported eigenvalue anisotropy changes from 0.0977 to 0.2169. The five-level sequence is not sufficient to infer a continuum rate: the report itself records substantial level-to-level changes in the traction-jump norms. The separate stress-second-moment eigenvalue anisotropy is comparatively stable, approximately 0.184–0.186 for the mixed source case; it must not be conflated with the interior-facet traction-jump anisotropy.

The single-sector controls have zero mixed term by construction. The mixed case is therefore the relevant test of the cross interaction, rather than a comparison of independently computed Frank-only and Burgers-only anisotropy scores.

## 5. Geometry, orientation and separation controls

The orientation audit rotates the mesh geometry in place and compares 0°, 30° and 60°. With defects co-rotated, the local interaction matrix changes by at most approximately \(4.2\times10^{-13}\), and directional boundary-residual differences are at most approximately \(2.7\times10^{-11}\). This supports covariance of the implemented discrete geometry/source-frame transformation for that fixed mesh. When Burgers data are held fixed in the laboratory frame, the core traction components change with relative orientation, as expected; this is a controlled orientation response, not a proof of a universal constitutive anisotropy.

The separate one-mesh separation sweep reports normalized off-diagonal operator coupling
\[
C(d)=\frac{\|M_{01}(d)\|_F}{\|M_{00}(d)\|_F}
\]
of approximately 0.2583, 0.1138, 0.0624 and 0.0349 at
\(d=0.48,0.56,0.64,0.72\), respectively. This is a monotone decrease over the four sampled separations. The signed operator anisotropy is non-monotone (approximately 0.6185, 0.5493, 0.5715, 0.4800). Because this sweep uses one mesh size, these values are screening data only; they do not establish a continuum distance-decay law.

## 6. Classification and open work

- **Proved:** the finite-dimensional tensor identity (91.1), scalar identity (91.2), directional identity (91.3), and normalized axis-resolved composition formula (91.4), under the stated linear reconstruction and common jump convention.
- **Numerically verified:** the five-level additivity residual and a nonzero positive mixed contribution for the reported mixed-source configuration; fixed-mesh orientation covariance; the one-resolution separation-screening trend.
- **Candidate/open:** convergence of each sector and of the mixed tensor as \(h\to0\); stability under core-radius and separation refinement; a continuum counterpart with trace/jump regularity; a material constitutive interpretation; any universal distance law or physical force-balance conclusion.

The exact identity is not a new universal law of defect mechanics independent of the reconstruction: its mathematical content is the tensor expansion of a linearly reconstructed jump. The research content is the explicit Frank/Burgers sector bookkeeping, its directional tensor, and the numerical determination of the signed interaction term in this two-core problem.

## 7. Reproducibility record

- [PR #161 — Frank–Burgers traction-jump decomposition](https://github.com/fabianleonaressi95/theorem/pull/161)
- [PR #162 — five-level refinement workflow](https://github.com/fabianleonaressi95/theorem/pull/162)
- [Five-level workflow run and JSON/FE-field artifact](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448456)
- [Base two-core audit run](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448351)
- [Operational definitions and reproduction command](../MORANDOTTI_ANISOTROPY.md)

**Classification:** exact discrete identity proved; numerical evidence recorded; continuum/material law open.  
**FLN**
