# T128 — Purcell-swimmer geometric control and the Q6 discretization interface

**Status:** [N] numerical reproduction of the stated leading-order benchmark; [O] Q6 discretization interface  
**Scope:** finite-dimensional geometric control and a proposed, not-yet-defined, Q6 discretization  
**Source:** Micalizio, Morandotti, Shum & Zoppello, *Purcell swimmer near a wall*, Meccanica 61 (2026), 71, DOI: 10.1007/s11012-026-02136-0.

## 1. Continuous reference model

The swimmer state is
q = (x,y,theta,alpha_minus,alpha_plus),
with body variables (x,y,theta) and two shape variables
(alpha_minus,alpha_plus). In the zero-inertia regime, force and torque
balance give a resistance system

[R_bb  R_bs] [xi_b ] = 0,
[R_sb  R_ss] [s_dot] 

and hence xi_b = -R_bb^{-1} R_bs s_dot. The local kinematic connection is
A(s,y,theta) = -R_bb^{-1} R_bs. Its curvature and iterated Lie brackets
determine the small-stroke locomotion directions. This is the continuous
geometric-control object that a discrete model would have to approximate.

The 2026 paper proves local controllability near configurations parallel
to a no-slip wall for every positive central-to-outer link-length ratio
lambda. It compares Lie-bracket predictions with periodic control gaits.
Its numerical section explicitly reports MATLAB/ode45; code availability
is listed as not applicable.

## 2. Independent numerical reproduction

A Python reconstruction is implemented in
audits/purcell_swimmer_wall/benchmark.py. It assembles the generalized
resistance matrix by Gauss-Legendre quadrature of the local resistive-force
law and integrates the four-stage square gait
(+u_minus,+u_plus,-u_minus,-u_plus).

For L = L0 = Lminus = Lplus = 1, y0 = 10^-2, r = 10^-4, and amplitude
xi = 10^-3, the normalized longitudinal displacement is approximately
0.06172485. It approaches the published small-amplitude value
5/81 = 0.061728395... . The result is stable for quadrature orders
16, 32, 48, 64 and 96. The two initial control vector fields also match
the analytic values in the paper:
h1 = (0, 1/6, -7/27, 1, 0),
h2 = (0, -1/6, -7/27, 0, 1).

This is a numerical reproduction of the stated benchmark. It is not an
independent proof of the local controllability theorem and does not
reproduce every figure or parameter sweep in the article.

## 3. Q6 interface: exact requirements, no invented coupling

Q6 has 64 vertices and six coordinate-flip directions per vertex. The
Purcell shape space is two-dimensional. There is currently no canonical
map in this repository from Q6 vertices/edges to the two hinge angles and
their controls. Assigning two arbitrary Q6 directions to the two hinges
would discard the remaining graph structure and would not be a derivation
from the cut-and-project geometry.

A defensible discrete construction must specify all of the following:

1. a map Phi: V(Q6) -> S, where S is a declared discretization of the shape
   space (including periodicity and angle units);
2. an edge-control assignment c: E(Q6) -> {u_minus,u_plus,idle or justified
   combinations};
3. a discrete body-transport rule U_e in SE(2), or an equivalent discrete
   connection, derived from the continuous resistance connection;
4. a consistency statement for discrete holonomy/curvature under refinement;
5. a rank/controllability test invariant under admissible relabellings,
   with explicit hypotheses.

Until these data are constructed, Q6 cannot be claimed to reproduce Purcell
locomotion or its controllability theorem.

## 4. Evidence classification

- **Established in the source paper:** continuous wall-corrected RFT model,
  local controllability theorem, Lie-bracket gait analysis, MATLAB/ode45
  numerical study.
- **Numerically reproduced here:** the leading longitudinal square-gait
  coefficient and the two initial control vector fields; quadrature
  stability was checked.
- **Open:** reproduce the remaining published gait figures and parameter
  sweeps; derive a Q6-to-shape-space map; construct the discrete connection;
  prove or numerically test a holonomy/controllability convergence statement.
- **Not claimed:** DOLFINx, PyTorch, or TensorFlow were used by the authors
  in the Purcell paper; a Q6 swimmer model exists; or a physical microswimmer
  is represented by Q6.

## References

- Micalizio, E., Morandotti, M., Shum, H. & Zoppello, M. (2026).
  *Purcell swimmer near a wall*. Meccanica 61, 71.
  DOI: 10.1007/s11012-026-02136-0.
- Marchello, R., Morandotti, M., Shum, H. & Zoppello, M. (2022).
  *The N-Link Swimmer in Three Dimensions: Controllability and Optimality Results*.
  Acta Applicandae Mathematicae 178, 6.
  DOI: 10.1007/s10440-022-00480-3.
