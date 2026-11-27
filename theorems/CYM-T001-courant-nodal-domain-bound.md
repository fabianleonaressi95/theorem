# CYM-T001 — Courant nodal-domain bound (classical theorem)

**Status:** proved classical theorem; included as a mathematical constraint, not a new RGS result.

## Statement

Let (L) be a self-adjoint, semibounded elliptic operator on a bounded domain, with boundary conditions for which the spectrum is discrete. List its eigenvalues nondecreasingly, counting multiplicity,
[
\lambda_1\le\lambda_2\le\cdots,
]
and let (u_k) be an eigenfunction associated with (lambda_k). Under the standard hypotheses of Courant's nodal-domain theorem, the number of nodal domains of (u_k) is at most (k).

A nodal domain is a connected component of the complement of the nodal set ({u_k=0}).

## Scope and caveats

- The index convention counts eigenvalues with multiplicity.
- The theorem gives an upper bound, not an exact count or a constructive prediction of nodal geometry.
- Boundary regularity, operator ellipticity, and the admissible boundary conditions matter.
- For vector-valued or complex electromagnetic fields, a scalar observable and corresponding nodal definition must be specified before applying a scalar nodal-domain statement.
- The theorem does not directly apply to arbitrary graph eigenvectors without a discrete analogue and its own hypotheses.

## Relevance to this programme

CYM-T001 supplies a rigorous control for scalar plate/membrane modes. It can be used to reject numerical claims that exceed the permitted nodal-domain count in a setting where the theorem's assumptions hold. It does not establish a universal cymatic law.

## References

- R. Courant and D. Hilbert, *Methods of Mathematical Physics*, Vol. I, Wiley-Interscience (1953), chapter on eigenvalue problems.
- I. Chavel, *Eigenvalues in Riemannian Geometry*, Academic Press (1984), nodal-domain discussion.
