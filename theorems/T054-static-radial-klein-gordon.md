# T054 — Radial Klein–Gordon equation for a static spherical ansatz

**Status:** proved for a minimally coupled scalar on the metric ansatz below.  
**Scope:** a field-equation identity, not a wormhole existence or stability theorem.

## 1. Setting

Consider the four-dimensional static, spherically symmetric metric on a radial interval \(I\)
\[
ds^2=-N(u)^2dt^2+du^2+R(u)^2
(d\theta^2+\sin^2\theta\,d\varphi^2),
\]
where \(N,R\in C^1(I)\) and \(N(u)>0\), \(R(u)>0\) on \(I\). Here \(\theta\in(0,\pi)\) and \(\varphi\) is the usual azimuthal coordinate, distinct from the scalar field \(\phi\). Let \(\phi\in C^2(I)\) be a real scalar field and assume \(V\in C^1(\mathbb R)\). It is minimally coupled with action
\[
S_\phi=-\int d^4x\,\sqrt{|g|}
\left[\frac12g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi+V(\phi)\right].
\]
Assume a static radial field \(\phi=\phi(u)\).

## 2. Theorem

The Euler–Lagrange equation \(\Box_g\phi-V'(\phi)=0\) reduces to
\[
\boxed{\ \frac{1}{N R^2}\frac{d}{du}
\left(NR^2\frac{d\phi}{du}\right)-V'(\phi)=0\ }.
\]

## 3. Proof

For the metric above, \(\det g=-N^2R^4\sin^2\theta\), so
\[
\sqrt{|g|}=NR^2|\sin\theta|=NR^2\sin\theta
\quad(0<\theta<\pi),\qquad g^{uu}=1.
\]
For a scalar,
\[
\Box_g\phi=\frac1{\sqrt{|g|}}
\partial_\mu\left(\sqrt{|g|}g^{\mu\nu}\partial_\nu\phi\right).
\]
Since \(\phi\) depends only on \(u\), only the radial derivative remains:
\[
\Box_g\phi
=\frac1{NR^2\sin\theta}\frac{d}{du}
\left(NR^2\sin\theta\,\phi'\right)
=\frac1{NR^2}\frac{d}{du}(NR^2\phi').
\]
Substitution into the Klein–Gordon equation proves the claim. \(\square\)

## 4. Quartic-potential identities

For
\[
V(\phi)=V_0+\frac{\lambda}{4}(\phi^2-\phi_v^2)^2,
\]
direct differentiation gives
\[
V'(\phi)=\lambda\phi(\phi^2-\phi_v^2),\qquad
V''(\phi)=\lambda(3\phi^2-\phi_v^2).
\]
These are algebraic identities and do not establish a solution of the radial boundary-value problem.

## 5. Non-conclusions

The ansatz and equation do not establish a throat, traversability, geodesic completeness, energy-condition violation, a global solution, or linear/dynamical stability. Those require the full coupled field equations and a well-posed boundary-value and perturbation analysis.

**Source:** [consolidated audit of the exploratory scalar–torsion PDF](../manuscripts/FOUR_PDF_CONSOLIDATED_AUDIT.md).
