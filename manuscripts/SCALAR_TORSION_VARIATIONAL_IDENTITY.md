# Scalar–torsion variational identity: a restricted derivation

## Status and scope

**Status: conditional variational identity for a displayed action.** This note extracts one calculation from the exploratory document formerly catalogued as *FORMULAZIONE.pdf*. It does not claim a solved RGS–EMS background, a wormhole, a quantum-gravity model, an LQG derivation, or a physical prediction.

The calculation below varies the scalar field while holding the geometric variables fixed. It is not the complete tetrad/spin-connection field system.

## 1. A valid static, spherically symmetric metric ansatz

One geometrical starting point in the source can be retained without attaching a physical interpretation:
\[
ds^2=-N(u)^2dt^2+du^2+R(u)^2
\left(d\theta^2+\sin^2\theta\,d\phi^2\right).
\]
Here \(u\) is proper radial distance, \(N(u)>0\) is the lapse, and \(R(u)>0\) is the areal radius. A local minimum of the areal radius at \(u=0\) requires
\[
R'(0)=0,\qquad R''(0)>0.
\]
These are geometric conditions for a candidate throat in this coordinate ansatz. They do not prove that the metric solves any field equations, that the spacetime is geodesically complete, or that the throat is traversable or stable.

## 2. Action and conventions

Consider
\[
S_\phi=\int_M d^4x\,e\left[
-\frac12F(\phi)T
-T^\mu\partial_\mu F(\phi)
-\frac12g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi
-V(\phi)
\right].
\]
Here \(e=\sqrt{|\det g|}\) is the tetrad determinant, \(T\) is a specified torsion scalar, and \(T^\mu\) is a specified torsion-vector convention. The metric/tetrad, connection and torsion variables are held fixed in this scalar variation. The sign convention for \(\Box=\nabla_\mu\nabla^\mu\) is the one induced by the displayed kinetic term.

A complete teleparallel model must separately specify the tetrad and inertial spin connection, and define \(T\) and \(T^\mu\) from that same pair. The metric alone does not determine these teleparallel quantities.

## 3. Scalar Euler–Lagrange equation

Vary \(\phi\) by a compactly supported variation \(\delta\phi\). The separate contributions are
\[
\delta\left(-\frac12FT\right)
=-\frac12F'(\phi)T\,\delta\phi,
\]
\[
\delta\left(-T^\mu\partial_\mu F\right)
=-T^\mu F''(\phi)\partial_\mu\phi\,\delta\phi
-T^\mu F'(\phi)\partial_\mu\delta\phi.
\]
Integrating the last term by parts gives
\[
-T^\mu F'\partial_\mu\delta\phi
\ longmapsto\
\nabla_\mu(T^\mu F')\,\delta\phi.
\]
Expanding this divergence,
\[
\nabla_\mu(T^\mu F')
=F'\nabla_\mu T^\mu
+F''T^\mu\partial_\mu\phi,
\]
the terms proportional to \(F''T^\mu\partial_\mu\phi\) cancel. Including the kinetic and potential terms yields
\[
\boxed{
\Box\phi-V'(\phi)
-\frac12F'(\phi)T
+F'(\phi)\nabla_\mu T^\mu=0.
}
\]
Thus the last term is \(F'(\phi)\nabla_\mu T^\mu\), not \(\nabla_\mu(F'(\phi)T^\mu)\), for the action written above. A different action or a different definition of the torsion-vector coupling must be varied independently.

For the example \(F(\phi)=1+\xi\phi^2\), the equation contains \(2\xi\phi\nabla_\mu T^\mu\).

## 4. What is still required for a complete theory

The scalar equation alone is insufficient. A complete model must provide:

1. a fixed signature and curvature/torsion sign convention;
2. a tetrad and its inverse;
3. the inertial spin connection, or an explicitly declared pure-tetrad formulation with its frame dependence;
4. definitions of torsion tensor, torsion vector, superpotential and torsion scalar;
5. independent variations with respect to the tetrad and spin connection, including constraints;
6. matter action, units, dimensions and boundary terms;
7. a single well-posed boundary-value problem with asymptotic conditions;
8. convergence and residual checks for any numerical solution.

The teleparallel identity relating the Levi-Civita Ricci scalar and the torsion scalar is convention-dependent in sign and divergence term. It must be checked against the conventions fixed above rather than copied between formulations.

## 5. Excluded interpretations

This calculation does not prove:
- existence or stability of a traversable wormhole;
- a scalar-hair solution or a converged RGS–EMS background;
- a Euclidean instanton or a physical tunnelling probability;
- equivalence to loop quantum gravity or a polymerized Hamiltonian constraint;
- a two-sheet factor-of-two correction to a throat radius;
- a gauge-invariant quaternionic Maxwell sector;
- ER=EPR, gravitational-wave echoes, dark matter, UV finiteness or quantum-information conservation.

These claims require independent actions, equations, mathematical proofs or empirical tests. The historical source and detailed rejection/qualification record remain in [the FORMULAZIONE audit](FORMULAZIONE_CRITICAL_AUDIT.md).
