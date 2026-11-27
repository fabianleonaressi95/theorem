# T156 — Vesica–Möbius elastic torsion and the Farey half-threshold

**Date:** 27 November 2026  
**Classification:** exact geometric identities; exact projective conjugacy; finite rational regression; elastic-strip relation from the literature; physical bridge open.  
**Status:** exact algebraic framework plus a finite-width symmetric Möbius BVP implementation; numerical convergence is pending CI execution. Physical FDT identification remains open.

## 1. Why this is T156, not T057

T057 is already used by a separate Moiré–RGS workstream. This record therefore receives the next available theorem number, T156, and does not overwrite that material.

The task is to compare three appearances of one-half while keeping their mathematical meanings separate:

1. Möbius ribbon topology: half-integer linking;
2. Farey dynamics: branch point (x=1/2);
3. Vesica geometry: the candidate normalized separation (chi=1/2).

The number shared by these constructions is not evidence that they have one physical cause.

## 2. Exact Vesica geometry

Let two circles of radius (R>0) have centres ((-a/2,0)) and ((a/2,0)), with (0<a<2R). Put

[
\chi=\frac{a}{2R}\in(0,1),\qquad
b=\sqrt{R^2-\frac{a^2}{4}}=R\sqrt{1-\chi^2}.
]

The intersection points are ((0,\pm b)). The common-lens area is

[
\boxed{\frac{A_v}{R^2}
=2\arccos\chi-2\chi\sqrt{1-\chi^2}.}
]

At the candidate half-separation \(\chi=1/2\),

[
a=R,\qquad b=\frac{\sqrt3}{2}R,\qquad
\boxed{A_v=R^2\left(\frac{2\pi}{3}-\frac{\sqrt3}{2}\right).}
]

The two radii to either intersection point subtend an angle of (2\arccos(\chi)=120^\circ). These are exact Euclidean facts; no continuum limit is involved.

## 3. Observer-relative Minkowski separation

For events (X_1,X_2\) in Minkowski spacetime, let \(\Delta X=X_2-X_1\), and let (u\) be a future-directed observer four-velocity with (u\cdot u=c^2). The observer's spatial projection is

[
d^\mu=
\left(\delta^\mu{}_{\nu}-\frac{u^\mu u_{\nu}}{c^2}\right)
\Delta X^\nu,\qquad
a_u=\sqrt{-d\cdot d}.
]

This projection is covariant when the observer is transformed together with the events. The induced simultaneity slice, and hence its Euclidean Vesica reconstruction, is observer-dependent. Two arbitrary spacetime events do not by themselves determine two equal spatial circles; a chosen rest frame/simultaneity slice and circle radius are additional data.

## 4. Möbius closure: topological half-twist

The ribbon identification is

[
(s,q)\sim(s+L,-q).
]

A single circuit reverses the transverse coordinate; two circuits restore it. This is a non-orientable ribbon. In the standard ribbon-linking convention, its linking number is half-integral, (Lk=\pm1/2).

This topological invariant is not Frenet torsion. In particular, the standard circular centreline is planar and has Frenet torsion zero even though the ribbon has a half-twist. Material-frame twist, writhe, linking number, centreline curvature and Frenet torsion are distinct observables.

## 5. Developable elastic ribbons

For a developable strip in the Starostin–van der Heijden parametrization,

[
\mathbf x(s,t)=\mathbf r(s)+t[\mathbf b(s)+\eta(s)\mathbf t(s)],
]

the centreline curvature and Frenet torsion satisfy

[
\boxed{\tau(s)=\eta(s)\kappa(s).}
]

In the narrow-strip Sadowsky limit, the bending functional is proportional to

[
\boxed{
V_S=Dw\int_0^L
\frac{(\kappa^2+\tau^2)^2}{\kappa^2}\,ds,
}
]

on intervals where \(\kappa\ne0\). This relation supplies a legitimate geometric mechanism for nonzero centreline torsion in a developable ribbon. It does not imply that every Möbius strip has nonzero torsion, and it does not determine an equilibrium without boundary conditions, admissible configurations and an energy minimization.

**Benchmark boundary:** the algebraic audit checks the developability identity and Sadowsky density on supplied profiles. A separate finite-width solver now implements the published symmetric Möbius BVP; until its CI run converges and its invariants are checked, no reproduction of the published minimizer is claimed.

## 6. The second half: FDT threshold to Farey branch

Use the Farey-map convention already fixed in the repository:

[
F(x)=
\begin{cases}
\dfrac{x}{1-x},&0\le x\le\frac12,\\[4pt]
\dfrac{1-x}{x},&\frac12<x\le1.
\end{cases}
]

The endpoint-fixing real projective transformation that sends \(2/3\) to \(1/2\) is

[
\boxed{h(\alpha)=\frac{\alpha}{2-\alpha}},
\qquad
\boxed{h^{-1}(x)=\frac{2x}{1+x}}.
]

It is unique among real Möbius transformations fixing 0 and 1: writing such a map as (a x/(c x+d)), the endpoint conditions give (a=c+d), and the condition (h(2/3)=1/2) gives (c=-d/2), hence the displayed map after projective rescaling.

In particular,

[
\boxed{h(2/3)=1/2.}
]

The conjugated map (G=h^{-1}\circ F\circ h) is

[
\boxed{
G(\alpha)=
\begin{cases}
\dfrac{2\alpha}{2-\alpha},
&0\le\alpha\le\frac23,\\[7pt]
\dfrac{4(1-\alpha)}{2-\alpha},
&\frac23<\alpha\le1.
\end{cases}}
]

Both branches agree at \(\alpha=2/3\), with value 1. This is an exact algebraic conjugacy of maps. It does not derive Farey dynamics from the FDT field equations.

The classical Minkowski question-mark function conjugates this Farey convention to the tent map (T(y)=1-2|y-1/2|):

[
?\circ F=T\circ ?.
]

Consequently, for the constructed map (G),

[
q_{\rm FDT}(\alpha)=?
\left(\frac{\alpha}{2-\alpha}\right)
\quad\Longrightarrow\quad
q_{\rm FDT}(G(\alpha))=T(q_{\rm FDT}(\alpha)).
]

The finite rational regression in this record checks this identity on a bounded test set; the global conjugacy is the classical theorem, not something inferred from the finite test.

## 7. Candidate Vesica coordinate

A natural candidate identification is

[
\boxed{\chi=h(\alpha)=\frac{\alpha}{2-\alpha}.}
]

It sends the FDT value \(\alpha=2/3\) to the Vesica value \(\chi=1/2\). At that point the exact lens geometry is the (120^\circ) configuration in §2.

This is a candidate coordinate identification, not a consequence of the Minkowski projection, the Vesica construction, general relativity or the elastic-strip equations. It must be derived from an independently specified physical model before being interpreted physically.

## 8. The three half-integers: status ledger

| Appearance | Mathematical meaning | Status |
|---|---|---|
| (Lk=\pm1/2) | Möbius ribbon linking in the standard convention | Established topology |
| (x=1/2) | Farey branch boundary | Established definition/dynamics |
| \(\alpha=2/3\leftrightarrow x=1/2\) | Projective coordinate conjugacy | Exact identity |
| \(\chi=1/2\) | Vesica separation and (120^\circ) lens geometry | Exact geometry |
| \(\chi=h(\alpha)\) | Identification of Vesica separation with FDT chart | Candidate |
| \(Lk\) selects the Farey branch | Common physical mechanism | Open |
| Vesica closure selects a specific elastic Möbius equilibrium | Variational/geometric mechanism | Open |

The topological half-linking is not numerically the same observable as the Farey coordinate (1/2). The current result is a rigorously specified comparison, not a unification theorem.

## 9. Reproducibility

Run from the repository root:

```bash
python scripts/audit_t156_vesica_mobius_farey.py
python -m unittest tests.test_t156_vesica_mobius_farey
```

The standard-library audit checks:

- exact rational conjugacy (G=h^{-1}Fh) on a finite rational grid;
- the threshold identity (h(2/3)=1/2);
- the rational Minkowski-question-mark/Farey/tent identity on a finite grid;
- the exact Vesica half-separation benchmark against its closed form;
- the Möbius transverse sign reversal and two-circuit return;
- the developability residual for explicitly supplied \((\eta,\kappa,\tau)\) profiles;
- positivity of the Sadowsky density for \(\kappa\ne0\).

The finite checks are regression evidence only. They do not prove global identities, solve the elastic minimization problem, or establish a physical FDT–Möbius coupling.

## 10. Open proof obligations

1. Derive or reject \(\chi=h(\alpha)\) from a physical construction, rather than choosing it as a coordinate chart.
2. Specify the Vesica-generated ribbon's material frame, boundary conditions and admissible developable configurations.
3. Solve the elastic variational problem and compare its energy, curvature, torsion, writhe and linking against the published Möbius benchmark.
4. Establish whether the elastic equilibrium is selected by the Vesica initial geometry or merely one of many admissible configurations.
5. Derive a genuine FDT return/scattering map from the field/geodesic equations. The monotone radial inflow ODE previously audited is not itself a two-branch Farey map.
6. Only after these steps, test whether the same physical mechanism explains the two appearances of one-half.

## References

- E. L. Starostin and G. H. M. van der Heijden, “The Shape of a Möbius Strip,” *Nature Materials* 6 (2007), 563–567. DOI: [10.1038/nmat1929](https://doi.org/10.1038/nmat1929).
- E. L. Starostin and G. H. M. van der Heijden, “Equilibrium Shapes with Stress Localisation for Inextensible Elastic Möbius and Other Strips,” *Journal of Elasticity* 119 (2015), 67–112.
- Repository companion: [TSMR–FDT comparative note](../research/TSMR-FDT_comparative_note.md), especially §§9–10.5–10.8.
- Repository companion: [Factor 1/2 origins and Liouville dossier](FACTOR_HALF_ORIGINS_LIOUVILLE_LITERATURE_2026-11-24.md).

**Final classification:** exact Euclidean and projective identities; established Möbius/developable-strip mathematics; finite regression checks; candidate Vesica–FDT coordinate; open physical identification and elastic-equilibrium selection.


## 11. Vesica-derived aspect-ratio candidate and finite-width elastic BVP

The Vesica lens has perimeter

\[
P_v=4R\arccos\chi
\]

and half-height

\[
b=R\sqrt{1-\chi^2}.
\]

A specific, reproducible *candidate reduction* is to identify the strip centreline length with the lens perimeter and the strip half-width with the lens half-height:

\[
L:=P_v,\qquad w:=b.
\]

This is a modelling choice, not a geometric identity about a physical ribbon. It gives

\[
\frac{w}{L}=
\frac{\sqrt{1-\chi^2}}{4\arccos\chi}.
\]

At \(\chi=1/2\),

\[
\frac{w}{L}=\frac{3\sqrt3}{8\pi},\qquad
\frac{L}{2w}=\frac{4\pi}{3\sqrt3},\qquad
L=2\pi\Longrightarrow w=\frac{3\sqrt3}{4}\simeq1.299038.
\]

This aspect ratio lies between the \(w=1.0\) and \(w=1.5\) finite-width examples plotted by Starostin–van der Heijden with \(L=2\pi\). It is therefore a useful interpolation benchmark, not evidence that the lens physically selects this strip.

### Finite-width equilibrium system

The numerical companion implements the 15-dimensional symmetric half-strip BVP in Starostin–van der Heijden (2015), Eqs. (23)–(29), with boundary conditions (30)–(38) and the constitutive boundary condition (21). **Source-consistency correction:** the printed Eq. (39) gives a sign for the (2\kappa(1+\eta^2)^2) term that contradicts Eqs. (20)–(21). At \(\eta'(0)=0\), Eq. (21) and \(h=\kappa^2(1+\eta^2)^2V\), (V(0)=1\), require \(M_3(0)=2\kappa(0)(1+\eta(0)^2)^2-\eta(0)M_1(0)\). The solver uses this constitutive-consistent sign and includes a regression test; this discrepancy is explicitly flagged for independent source/author confirmation rather than silently attributed to the paper. The finite-width Wunderlich density is

\[
h(\kappa,\eta,\eta')=
\kappa^2(1+\eta^2)^2
\frac{\operatorname{atanh}(w\eta')}{w\eta'}.
\]

The solver uses the bounded variable \(q=\operatorname{atanh}(w\eta')\) with an explicit edge margin \(\delta=10^{-4}\), so the iterates satisfy \(|w\eta'|\le 1-\delta\). This is a numerical regularization of the edge singularity, not the exact limiting surface. It continues the switching-point regularization through

\[
\kappa(L/2)\in\{0.05,0.02,0.01,0.005\},
\]

rather than imposing the singular endpoint directly. This follows the published numerical strategy, which reports continuation towards values around \(10^{-3}\).

The audit records the collocation residual, maximum \(|w\eta'|\), normalized Wunderlich energy, boundary residual, and drift in the first integrals \(|F|^2\), \(F\cdot M\) and the Hamiltonian. Reproduction files: [solver](../scripts/solve_t156_mobius_elastic_bvp.py), [BVP tests](../tests/test_t156_mobius_elastic_bvp.py), [workflow](../.github/workflows/t156-mobius-elastic-bvp.yml); the exact algebra audit and its tests are [here](../scripts/audit_t156_vesica_mobius_farey.py) and [here](../tests/test_t156_vesica_mobius_farey.py). Repository-root register references: `scripts/audit_t156_vesica_mobius_farey.py`, `scripts/solve_t156_mobius_elastic_bvp.py`, `tests/test_t156_vesica_mobius_farey.py`, `tests/test_t156_mobius_elastic_bvp.py`. The linking value \(Lk=1/2\) is selected by the symmetric Möbius BVP class; it is not independently reconstructed from the computed curve in this implementation.

### Interpretation gate

A successful regularized BVP would establish a numerical finite-width Möbius equilibrium for the *candidate Vesica aspect ratio*. It would not establish that the Vesica generates the Möbius material frame, that \(\chi=h(\alpha)\) follows from FDT, or that the topological \(1/2\) and Farey \(1/2\) have a common physical cause. The exact switching-point limit and an independent linking-number calculation remain separate proof obligations.


### Continuation solver: AUTO-07p

The SciPy solve_bvp collocation attempt is retained as a diagnostic and currently encounters a singular collocation Jacobian. This is not treated as an equilibrium result. The primary numerical route is therefore AUTO-07p, which the source paper itself uses for this BVP because both interval endpoints are singular and the switching point requires continuation.

The AUTO implementation is in `scripts/t156_auto/mobius.f90`, with constants in `scripts/t156_auto/c.mobius` and driver `scripts/t156_auto/mobius.auto`. It continues the regularized endpoint parameter

\[
\kappa(L/2): 0.05\to0.02\to0.01\to0.005
\]

at the Vesica candidate width \(w=3\sqrt3/4\) after \(L=2\pi\) normalization. It uses the constitutive-consistent endpoint sign from Eqs. (20)–(21), not the conflicting sign printed in Eq. (39). The GitHub Actions workflow builds AUTO-07p from its public source and archives the continuation output.

A successful AUTO run would establish a regularized numerical stationary solution for this candidate aspect ratio. It would still not prove global minimality, independently reconstruct the linking number, or derive the Vesica-to-ribbon identification from physical first principles.
