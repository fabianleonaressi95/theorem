# Q6–Purcell calibrated shape interface

This audit uses the already recovered golden 6D-to-3D internal projection from
the RGS–PSU cut-and-project convention. It does not assign two arbitrary Q6
coordinate flips to the two swimmer hinges.

## Mathematical construction

For the centered Q6 state \(v\in\{0,1\}^6\), the internal coordinate is

\[
Y_v=P_\perp(v-\tfrac12\mathbf 1),\qquad
P_\perp=\frac{A(\phi^*)}{\sqrt{2(2+\phi^*)}}.
\]

A calibrated orthonormal 2-frame \(B\in\mathbb R^{2\times3}\) and scale
\(\kappa>0\) define the candidate shape coordinate

\[
\Phi_{B,\kappa}(v)=\kappa B Y_v\pmod{2\pi}.
\]

Every one of the six cut-and-project edge directions contributes to both
shape channels through \(B P_\perp e_j\). There are 192 oriented canonical
edges, 32 per coordinate-flip direction.

The pair \((B,\kappa)\) is an explicit calibration input. It is not selected
by the cut-and-project data alone. T129 proves the corresponding linear
\(A_5\)-equivariance obstruction under its stated representation hypotheses.

## Local SE(2) transport

For each edge, the code evaluates the continuous T128 connection
\(A=-R_{bb}^{-1}R_{bs}\) at the midpoint of the lifted shape segment and
returns its one-step exponential in \(SE(2)\). This is a local finite-graph
approximation, not a path-refinement theorem.

## Run

~~~bash
python -m pytest tests/test_purcell_q6_shape_interface.py -q
~~~

Dependencies are those of the T128 benchmark: NumPy and SciPy.

## Scope

The audit checks finite graph combinatorics, the calibrated shape potential,
edge increments, and \(SE(2)\) matrix structure. It does not derive the
calibration from a physical wall/swimmer experiment, propagate the swimmer
body globally along arbitrary paths, or prove convergence of discrete
holonomy to continuous holonomy.
