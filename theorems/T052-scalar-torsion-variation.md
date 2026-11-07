# T052 — Scalar Euler–Lagrange equation for the displayed scalar–torsion action

**Status:** proved conditionally for the action and fixed geometric variables below.  
**Scope:** scalar variation only; not the tetrad or spin-connection field equations.

## 1. Setting and action

Let \((M,g)\) be a smooth four-dimensional spacetime, let \(e=\sqrt{|\det g|}\), and let \(T\) and \(T^\mu\) be fixed torsion scalar and torsion-vector fields defined by a chosen teleparallel convention. Let \(F,V\in C^2(\mathbb R)\). Consider
\[
S_\phi=\int_M d^4x\,e\left[
-\frac12F(\phi)T
-T^\mu\partial_\mu F(\phi)
-\frac12g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi
-V(\phi)\right].
\]
Throughout, \\(\\nabla\\) is the Levi-Civita derivative of \\(g\\), not the teleparallel connection; thus \\(\\nabla_\\mu T^\\mu=e^{-1}\\partial_\\mu(eT^\\mu)\\). The scalar d'Alembertian convention is \\(\\Box=g^{\\mu\\nu}\\nabla_\\mu\\nabla_\\nu=\\nabla_\\mu\\nabla^\\mu\\). Assume variations \(\delta\phi\) are compactly supported. The geometric variables and torsion fields are held fixed.

## 2. Theorem

The Euler–Lagrange equation obtained by varying \(\phi\) is
\[
\boxed{\ \Box\phi-V'(\phi)-\frac12F'(\phi)T
+F'(\phi)\nabla_\mu T^\mu=0\ },
\qquad
\Box=\nabla_\mu\nabla^\mu.
\]
In particular, the last term is \(F'(\phi)\nabla_\mu T^\mu\), not the unexpanded divergence \(\nabla_\mu(F'(\phi)T^\mu)\).

## 3. Proof

The variation of the first term is
\[
\delta(-\tfrac12FT)=-\tfrac12F'T\,\delta\phi.
\]
The torsion-vector term varies as
\[
\delta(-T^\mu\partial_\mu F)
=-T^\mu F''\partial_\mu\phi\,\delta\phi
-T^\mu F'\partial_\mu\delta\phi.
\]
After integration by parts, the last term contributes
\[
\nabla_\mu(T^\mu F')\,\delta\phi
=\left(F'\nabla_\mu T^\mu+
F''T^\mu\partial_\mu\phi\right)\delta\phi.
\]
The terms proportional to \(F''T^\mu\partial_\mu\phi\) cancel. The kinetic term contributes \(\Box\phi\,\delta\phi\), and the potential contributes \(-V'\delta\phi\). Since \(\delta\phi\) is arbitrary, the stated equation follows. \(\square\)

## 4. Special case

For \(F(\phi)=1+\xi\phi^2\), the equation becomes
\[
\Box\phi-V'(\phi)-\xi\phi T
+2\xi\phi\nabla_\mu T^\mu=0.
\]

## 5. Limitations

The result does not specify a complete teleparallel theory. Such a theory must define the tetrad, inertial spin connection, torsion conventions, boundary terms, matter action and independent variations with respect to geometric variables. No wormhole solution, stability result or physical prediction follows from this scalar equation alone.

**Source:** [scalar–torsion variational identity note](../manuscripts/SCALAR_TORSION_VARIATIONAL_IDENTITY.md).
