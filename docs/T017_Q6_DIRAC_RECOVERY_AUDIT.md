# T017 — Q6 Dirac recovery and multiplicity audit

**Status: PARTIAL RECOVERY / OPEN.** This file records a reproducible exact audit of the Q6 graph spectrum and specifies what is still required to recover T017's actual Dirac operator. It does not claim that the graph Laplacian is the Dirac square.

## 1. Source and provenance boundary

The connected repository currently accessible is `fabianleonaressi95/theorem`. The user-designated historical repository name `fabianleonaressi95/theroem` was not accessible through the connected GitHub installation in this run. Searches of the accessible default branch for `T017`, `Q6 Dirac`, `rgs_q6_dirac`, and `Clifford Q6` returned no matching source file. The historical T017 statement, operator convention, and source matrices therefore remain unrecovered. Do not silently substitute another operator.

Existing repository context:
- `docs/Q6_D5_INTEGER_FIBER_QUOTIENT.md`: Q6 edge-cycle map and exact five-mode quotient.
- `docs/Q6_D5_SATURATED_KERNEL_AND_TAIL_BOUND.md`: Smith-normal-form kernel and tail bound.
- `docs/Q6_D5_WILSON_FIVE_TORUS_MARGINAL.md`: 68-dimensional annihilator torus.
- Issue #84: exact Q6-D5 integer-fibre reproduction.

These are adjacent Q6 constructions, not evidence for the missing T017 Dirac definition.

## 2. Exact graph result

Let the vertices be binary strings (x\in\mathbb F_2^6), with an edge between strings differing in one coordinate. The graph Laplacian is
[
(Lf)(x)=6f(x)-\sum_{i=1}^6 f(x+e_i).
]
For every subset (S\subseteq\{1,\ldots,6\}), define the Walsh character
[
\chi_S(x)=(-1)^{\sum_{i\in S}x_i}.
]
Then
[
\sum_{i=1}^6\chi_S(x+e_i)=(6-2|S|)\chi_S(x),
\qquad L\chi_S=2|S|\chi_S.
]
The 64 Walsh characters form an orthogonal basis. Thus the graph-Laplacian eigenvalues and multiplicities are exactly
[
\lambda_j=2j,\qquad m_j=\binom 6j,
\quad j=0,\ldots,6,
]
namely multiplicities ((1,6,15,20,15,6,1)). Their sum is 64.

This is an analytic proof for the graph Laplacian; the accompanying Python test independently checks the finite matrix action and the complete Walsh basis using integer arithmetic.

## 3. Do not conflate three operators

1. **Vertex graph Laplacian** (L_0): acts on 64 vertex functions; spectrum above.
2. **Cubical Hodge Laplacian** Δ_k: acts on oriented (k)-cells of the full 6-cube. The number of (k)-cells is
   [
   N_k=\binom 6k 2^{6-k},\qquad \sum_{k=0}^6N_k=3^6=729.
   ]
3. **Cubical Dirac** (D=d+d^*): acts on the direct sum of all cubical cochains, once incidence conventions and inner products are fixed. It satisfies (D^2=dd^*+d^*d), degree by degree, with the appropriate boundary conventions.

With standard unit inner products and ordinary cubical boundary maps, the degree-zero Hodge Laplacian is \\Delta_0=d_0^*d_0 and equals the vertex graph Laplacian of the cube's 1-skeleton. Higher-dimensional cells do not add a higher-incidence term in degree zero. The full Dirac nevertheless acts on all cochain degrees; knowing only its degree-zero block does not determine the complete Dirac spectrum or multiplicities.

## 4. Multiplicity and Clifford tests still required for T017

Before claiming the T017 Dirac spectrum, recover and record:
- the precise chain/cochain complex and boundary conditions (full cube, periodic quotient, or another Q6 construction);
- the oriented incidence matrices (d_k), inner products/Hodge stars, and grading;
- the exact definition of (D), including factors of (i), lattice spacing, mass term, and any Wilson/twist term;
- the Clifford generators and their anticommutators;
- the symmetry group acting on the complex and the representation on each eigenspace;
- the precise meaning of the previously reported relation (D_+(k)^2=4mI), including the domain of (k,m) and whether it is a block identity or a spectral statement.

Acceptance tests:
1. (d_{k+1}d_k=0) exactly.
2. Clifford relations hold exactly or with a documented numerical residual.
3. (D) is self-adjoint under the stated inner product.
4. (D^2) agrees with the declared Hodge/Dirac Laplacian.
5. Character/Reynolds multiplicities agree with direct eigenspace dimensions.
6. Zero modes, boundary modes, and possible doubling are counted separately.
7. Any claimed continuum limit is tested independently; finite Q6 multiplicities alone do not establish it.

## 5. Status ledger

| Claim | Status |
|---|---|
| Q6 graph has 64 vertices and 192 edges | Exact combinatorial fact |
| Graph Laplacian spectrum (2j), multiplicity ({6\choose j}) | Proved; independently tested in integer arithmetic |
| Full 6-cube has 729 cells across all dimensions | Exact combinatorial fact |
| T017 Dirac definition recovered | Open: source file not found in accessible repository |
| T017 full Dirac spectrum and multiplicities | Open |
| Clifford representation and symmetry multiplicities | Open |
| Absence of fermion doubling | Open |
| Identification with Rumin/CR Dirac on (S^3/2I) | Open; distinct complexes and geometries |

## 6. Reproduction

Run:
```bash
python scripts/test_t017_q6_dirac_recovery.py
```

The test is intentionally limited to the graph Laplacian and Walsh basis. It is not a test of the missing T017 operator.

## References

- A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, Universitext, Springer, 2012, DOI: [10.1007/978-1-4614-1939-6](https://doi.org/10.1007/978-1-4614-1939-6). Background on graph spectra and hypercube eigenvalues.
- N. Biggs, *Algebraic Graph Theory*, 2nd ed., Cambridge University Press, 1993. Graph Laplacians and character methods.
- The cube's cellular chain complex and the identity (d^2=0) are standard algebraic topology; a specific T017 realization still requires its own incidence data and conventions.

**No full Dirac spectrum, Rumin equivalence, or physical unification claim is made in this audit.**
