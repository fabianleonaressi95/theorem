# Discrete coframe and face torsion candidate on a tetrahedron — 2026-11-26

## Purpose and status

**Carrier-derived specialization:** the finite construction from the hash-checked RGS 64-site coordinates is documented in [RGS_CARRIER_DERIVED_COFRAME_TETRAHEDRON_2026-11-26.md](RGS_CARRIER_DERIVED_COFRAME_TETRAHEDRON_2026-11-26.md), with an executable audit. That specialization supplies concrete edge data for the abstract coframe introduced below; it does not identify the selected tetrahedron with a Q6 incidence cell or with the archived A13 PSU links.


This note adds an independent discrete coframe to the SE(3) edge-transport fixture. It defines a path-based, gauge-covariant face quantity that is a candidate discretization of Cartan torsion.

**Status:** proposed discrete definition plus numerical covariance/flatness checks. It is not a theorem identifying the quantity with continuum Cartan torsion, and it is not a deWit–Nye/Burgers construction.

## Data and conventions

For each oriented edge $i\to j$, let
- $G_{ij}=(R_{ij},t_{ij})\in SE(3)$ be the affine frame transport, with $G_{ji}=G_{ij}^{-1}$;
- $R_{ij}\in SO(3)$ be its rotational part;
- $E_{ij}\in\mathbb R^3_i$ be a separate coframe edge increment expressed in the source fibre.

The coframe is independent data. Its orientation rule is
\[
E_{ji}=-R_{ij}E_{ij}.
\]
This makes the reverse increment the negative of the forward increment transported to the target frame.

Under vertex-frame changes $h_i=(S_i,b_i)\in SE(3)$, use
\[
G'_{ij}=h_jG_{ij}h_i^{-1},\qquad E'_{ij}=S_iE_{ij}.
\]
The translational parts $b_i$ do not act on vectors. The induced rotation is
$R'_{ij}=S_jR_{ij}S_i^{-1}$, so the orientation rule is preserved.

## Candidate face torsion

For an oriented triangle $(i,j,k)$, express all three edge increments in the fibre at $i$ and define
\[
\boxed{
\mathcal T_{ijk}
=E_{ij}+R_{ij}^{-1}E_{jk}
 +(R_{jk}R_{ij})^{-1}E_{ki}.
}
\]
Here $R_{jk}R_{ij}$ is the rotation along the path $i\to j\to k$; its inverse transports a vector at $k$ back to $i$. The base point and path are part of the definition.

The expression transforms covariantly:
\[
\mathcal T'_{ijk}=S_i\mathcal T_{ijk}.
\]
This follows term by term from $R'_{ij}=S_jR_{ij}S_i^{-1}$ and $E'_{ij}=S_iE_{ij}$.

This is a finite path-sum analogue of $D_\omega e=de+\omega\wedge e$. It is not yet a complete simplicial differential: for curved connections, path choices matter and a covariant differential need not square to zero.

## Important separation from the SE(3) translation part

The affine translation $t_{ij}$ is **not** automatically the coframe increment $E_{ij}$. Under a general affine vertex gauge, $t_{ij}$ acquires origin-shift terms involving $b_i,b_j$; it therefore does not transform as a source-fibre vector.

Only after fixing vertex origins (restricting to $b_i=0$) could one define a convention-dependent candidate such as $E_{ij}=R_{ij}^{-1}t_{ij}$. That restriction is not gauge invariant under the full SE(3) frame group and must not be silently imposed. The present fixture keeps $E$ independent.

## Exact checks and numerical fixture

The accompanying script tests:
1. orientation reversal $E_{ji}=-R_{ij}E_{ij}$;
2. covariance of $\mathcal T_{ijk}$ under independent vertex rotations and full SE(3) affine gauges (translations affect $G$, not vector components of $E$);
3. vanishing on a torsion-free pure-gauge fixture, with $R_{ij}=S_jS_i^{-1}$ and $E_{ij}=S_i(x_j-x_i)$;
4. nontriviality for generic independent coframe/connection data.

These are finite-dimensional algebraic and numerical checks of the proposed definition. They do not establish convergence to a continuum theory.

Run:

```bash
python scripts/audit_discrete_coframe_torsion_tetrahedron.py
```

The script writes `audits/DISCRETE_COFRAME_TORSION_TETRAHEDRON_2026-11-26.json`.

## Open items

- Define a geometrically motivated construction of $E$ from the RGS/PSU carrier, rather than selecting arbitrary edge vectors.
- Specify a discrete integration map from a smooth coframe to edge increments and prove a convergence result.
- Define compatible cup/wedge products and a curvature action before formulating a discrete torsion Bianchi identity.
- Relate the construction to deWit/Nye dislocation density only after fixing material/spatial conventions and a continuum limit.
- Test on a nontrivial curved 3-complex and compare alternative face paths/shellings.

No claim is made here that the curvature identity in the parent PR implies a torsion identity.
