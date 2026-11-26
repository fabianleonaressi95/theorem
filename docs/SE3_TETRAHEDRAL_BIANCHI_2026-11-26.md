# Transported non-Abelian Bianchi identity on a tetrahedron — 2026-11-26

## Result and scope

This note derives and tests the curvature Bianchi identity for arbitrary edge transports on one oriented tetrahedron. It is an exact finite-dimensional group identity. It is **not** the discrete torsion Bianchi identity and does not identify affine closure with Cartan torsion or deWit/Nye dislocation density.

## Conventions

An oriented edge transport $G_{ij}\in SE(3)$ maps coordinates at vertex $i$ to coordinates at vertex $j$. Reversing orientation gives $G_{ji}=G_{ij}^{-1}$. Products are composed as maps: $AB$ means $A$ after $B$.

For an oriented triangular face based at its first vertex, define
\[
H_{ijk}=G_{ki}G_{jk}G_{ij}.
\]
The oriented boundary of the tetrahedron $[0123]$ is
\[
\partial[0123]=[123]-[023]+[013]-[012].
\]

The holonomies $H_{012},H_{013},H_{023}$ are based at vertex 0, while $H_{123}$ is based at vertex 1. Bring the latter to the fibre at 0 along edge $0\to1$:
\[
K_{123}=G_{01}^{-1}H_{123}G_{01}.
\]

## Exact ordered identity

With these conventions the non-Abelian boundary identity is
\[
\boxed{H_{013}\,K_{123}\,H_{012}^{-1}\,H_{023}^{-1}=I.}
\]

This is an exact identity for every assignment of six invertible edge transports, hence in particular for arbitrary $SE(3)$ transports. To see the cancellation, write
\[
\begin{aligned}
H_{012}&=G_{20}G_{12}G_{01},\\
H_{013}&=G_{30}G_{13}G_{01},\\
H_{023}&=G_{30}G_{23}G_{02},\\
K_{123}&=G_{01}^{-1}G_{13}^{-1}G_{23}G_{12}G_{01}.
\end{aligned}
\]
Then
\[
\begin{aligned}
&H_{013}K_{123}H_{012}^{-1}H_{023}^{-1}\\
={}&(G_{30}G_{13}G_{01})
(G_{01}^{-1}G_{13}^{-1}G_{23}G_{12}G_{01})
(G_{01}^{-1}G_{12}^{-1}G_{20})
(G_{02}^{-1}G_{23}^{-1}G_{30}^{-1})=I,
\end{aligned}
\]
using $G_{ji}=G_{ij}^{-1}$ and cancelling adjacent inverse pairs. The order is essential; this is not a commutative product of face curvatures.

## Gauge covariance

Under independent vertex-frame changes $h_i\in SE(3)$,
\[
G_{ij}'=h_jG_{ij}h_i^{-1},\qquad
H_{ijk}'=h_iH_{ijk}h_i^{-1}.
\]
In particular, $K_{123}'=h_0K_{123}h_0^{-1}$. Therefore the full ordered product transforms by conjugation at vertex 0:
\[
P'=h_0Ph_0^{-1}.
\]
Since $P=I$, the identity is gauge covariant.

## Numerical audit

Run:

```bash
python scripts/audit_se3_tetrahedral_bianchi.py
```

The deterministic NumPy script tests 1,000 seeded random assignments of six $SE(3)$ edge transports and four independent vertex gauges. It checks:
- both-sided group inverse residuals;
- the ordered transported Bianchi product;
- face-holonomy conjugation at each face base point;
- conjugation covariance of the full Bianchi product at vertex 0.

It writes `audits/SE3_TETRAHEDRAL_BIANCHI_2026-11-26.json`.

## Mathematical status and limitations

- **Proved algebraically:** the displayed tetrahedral identity, under the stated edge orientation, base point, and product convention.
- **Numerical verification:** the implementation checks the identity and gauge covariance on seeded random data; numerical residuals are implementation checks, not the proof.
- **Not established:** a general shelling-independent formula for arbitrary 3-complexes; a discrete torsion identity $D_A\mathcal T=\mathcal R\smile_A E$; a continuum limit; a Cartan torsion or Nye/deWit identification; a Burgers-vector interpretation; cohomological flux statements for curved connections.

The identity is an algebraic boundary-of-boundary cancellation. It is not by itself a dynamical or constitutive law, and it does not constrain the individual face holonomies to be trivial. Extending it to a general 3-complex requires specifying a shelling and comparison paths and proving the corresponding ordered cancellation cell by cell.
