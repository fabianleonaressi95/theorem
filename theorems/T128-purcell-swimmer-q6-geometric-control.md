# T128 — Purcell-swimmer geometric control and the Q6 discretization interface

**Status:** [O] open research interface; [N] preliminary independent numerical audit  
**Scope:** finite-dimensional geometric control and a proposed, not-yet-defined, Q6 discretization  
**Source:** Micalizio, Morandotti, Shum & Zoppello, *Purcell swimmer near a wall*, Meccanica 61 (2026), 71, DOI: 10.1007/s11012-026-02136-0.

## 1. Continuous reference model

The swimmer state is
\[
q=(x,y,\theta,\alpha_-,\alpha_+),
\]
with body variables \((x,y,\theta)\) and two shape variables
\((\alpha_-,\alpha_+)\).  In the zero-inertia regime, force and torque
balance give a resistance system
\[
\begin{pmatrix}R_{bb}(q)&R_{bs}(q)\\
R_{sb}(q)&R_{ss}(q)\end{pmatrix}
\begin{pmatrix}\xi_b\\\dot s\end{pmatrix}=0,
\qquad
\xi_b=-R_{bb}^{-1}R_{bs}\dot s.
\]
Thus the local kinematic connection is
\(A(s,y,\theta)=-R_{bb}^{-1}R_{bs}\).  Its curvature and iterated Lie
brackets determine the small-stroke locomotion directions.  This is the
continuous geometric-control object that a discrete model would have to
approximate.

The 2026 paper proves local controllability near configurations parallel
to a no-slip wall for every positive central-to-outer link-length ratio
\(\lambda\).  It also compares Lie-bracket predictions with periodic
control gaits.  Its numerical section explicitly reports MATLAB/\texttt{ode45};
the article lists code availability as not applicable.

## 2. Independent reconstruction audit

A first-pass Python reconstruction was implemented in
\texttt{audits/purcell\_swimmer\_wall/benchmark.py}.  It assembles the
generalized resistance matrix by quadrature of the local resistive-force
law and integrates the four-stage square gait
\((+u_-,+u_+,-u_-,-u_+)\).

For \(L=L_0=L_{-1}=L_1=1\), \(y_0=10^{-2}\), \(r=10^{-4}\), and
amplitude \(\xi=10^{-3}\), the normalized longitudinal displacement
converges under quadrature-order refinement to approximately
\[
\Delta x/\xi^2\simeq 0.0370356.
\]
The paper reports the small-amplitude reference value
\[
\Delta x/\xi^2\longrightarrow 0.0617
\quad (\text{more precisely }5/81).
\]
The mismatch is material (about 40%) and is **not** presented as a
successful reproduction.  It signals that the reconstructed resistance
matrix, sign conventions, or the interpretation of the paper's control
cycle must be checked against the full derivation before this prototype
can be used as a benchmark.  Quadrature convergence alone does not
validate the model.

## 3. Q6 interface: exact requirements, no invented coupling

Q6 has 64 vertices and six coordinate-flip directions per vertex.  The
Purcell shape space is two-dimensional.  There is currently no canonical
map in this repository from Q6 vertices/edges to the two hinge angles and
their controls.  In particular, assigning two arbitrary Q6 directions
to the two hinges would discard the remaining graph structure and would
not be a derivation from the cut-and-project geometry.

A defensible discrete construction must specify all of the following:

1. a map \(\Phi:V(Q6)\to\mathcal S\), where \(\mathcal S\) is a declared
   discretization of the shape space (including periodicity and angle units);
2. an edge-control assignment \(c:E(Q6)\to\{u_-,u_+,\text{idle or justified combinations}\}\);
3. a discrete body-transport rule \(U_e\in SE(2)\), or an equivalent
   discrete connection, derived from the continuous resistance connection;
4. a consistency statement for discrete holonomy/curvature under refinement;
5. a rank/controllability test whose result is invariant under admissible
   relabellings and whose hypotheses are explicit.

Until these data are constructed, Q6 cannot be claimed to reproduce
Purcell locomotion or its controllability theorem.

## 4. What is established and what remains open

- **Established from the source paper:** continuous wall-corrected RFT model,
  local controllability theorem, Lie-bracket gait analysis, MATLAB/\texttt{ode45}
  numerical study.
- **Numerically observed in this audit:** the preliminary quadrature prototype
  is stable with respect to quadrature order but does not reproduce the
  paper's reported leading coefficient.
- **Open:** resolve the coefficient mismatch; independently reproduce the
  published gait figures; derive a Q6-to-shape-space map; construct the
  discrete connection; prove or numerically test a holonomy/controllability
  convergence statement.
- **Not claimed:** DOLFINx, PyTorch, or TensorFlow were used by the authors in
  the Purcell paper; a Q6 swimmer model exists; a physical microswimmer is
  represented by Q6; or the numerical mismatch is an error in the published
  paper.

## References

- Micalizio, E., Morandotti, M., Shum, H. & Zoppello, M. (2026).
  *Purcell swimmer near a wall*. Meccanica 61, 71.
  DOI: [10.1007/s11012-026-02136-0](https://doi.org/10.1007/s11012-026-02136-0).
- Marchello, R., Morandotti, M., Shum, H. & Zoppello, M. (2022).
  *The N-Link Swimmer in Three Dimensions: Controllability and Optimality Results*.
  Acta Applicandae Mathematicae 178, 6.
  DOI: [10.1007/s10440-022-00480-3](https://doi.org/10.1007/s10440-022-00480-3).
