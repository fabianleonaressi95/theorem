# T092 — Local two-circle geometry and the Frank–Burgers holonomy bridge

**Date:** 11 November 2026  
**Status:** the local Euclidean construction is proved; the discrete \(SE(2)\) holonomy decomposition is exact by definition; the continuum Cartan interpretation is conditional on a specified coframe/connection and regularity; global mesh realization and convergence to defect-elasticity models remain open.  
**Dependencies:** T091 (finite-dimensional Frank–Burgers traction-jump composition); the Morandotti benchmark and two-core C0-IPDG audit.

## 1. Purpose and logical boundary

This record isolates the geometric bridge from the Two-Circle construction to Frank and Burgers defect data. It does **not** claim that the existence of a small triangle alone solves an arbitrary PDE, nor that every triangulation automatically carries a defect theory. The result has three distinct layers:

1. a proved local equilateral-cell construction on every open Euclidean planar domain;
2. an exact finite discrete description of rotational and translational closure failure by \(SE(2)\) holonomy;
3. a conditional continuum interpretation in terms of curvature (Frank) and torsion (Burgers), followed by a problem-specific elasticity problem of the type studied by Cesana–De Luca–Morandotti.

## 2. Local two-circle construction

Let \(U\subset\mathbb R^2\) be open, \(x\in U\), and \(\epsilon>0\). Since \(U\) is open, there exists \(\rho>0\) such that \(B(x,\rho)\subset U\). Choose a unit vector \(u\), let \(u^\perp\) be its positive quarter-turn, and choose
\[
0<r<\min\{\rho,\epsilon\}.
\]
Set
\[
c_1=x,\qquad c_2=x+ru,
\]
and define
\[
p_\pm=x+\frac r2u\pm\frac{\sqrt3r}{2}u^\perp.
\]
Then
\[
|c_1-c_2|=|c_1-p_\pm|=|c_2-p_\pm|=r.
\]
Thus the two radius-\(r\) circles centred at \(c_1,c_2\) intersect at \(p_+\) and \(p_-\), and each triple \((c_1,c_2,p_\pm)\) is an equilateral triangle of side \(r\). Since all three vertices lie in \(B(x,r)\subset U\), the triangles lie in \(U\); their diameter is \(r<\epsilon\).

**Theorem 92.1 (arbitrarily small local two-circle cells).** For every \(x\) in every open set \(U\subset\mathbb R^2\) and every \(\epsilon>0\), there exist two equal circles with centre separation equal to their radius, contained locally in \(U\), whose intersection produces an equilateral triangle of diameter smaller than \(\epsilon\). In fact the construction gives two triangles, one on each side of the line of centres.

**Proof.** The explicit coordinates above give all three equal side lengths. Openness supplies the ball in which the construction is contained. \(\square\)

The statement is local and scale-covariant in Euclidean geometry. At a boundary point, the same conclusion requires a boundary-adapted one-sided construction or an extension of the domain; it is not asserted here. On a smooth Riemannian surface, normal coordinates give an asymptotically equilateral small cell, but an exactly geodesic equilateral construction requires a separate curvature-dependent argument.

## 3. From local cells to a discrete transport structure

A single cell does not yet define a global mesh. For a family of cells \(\mathcal T_h\), one must additionally prescribe:

- matching vertices/edges on shared interfaces (or a nonconforming interface law);
- orientation and transition maps between local frames;
- boundary conditions and treatment of holes/topology;
- a refinement rule and shape-regularity or an explicitly controlled anisotropic alternative.

On each oriented adjacency \(e:i\to j\), let the relative placement of the local frames be represented by
\[
g_e=(R_e,t_e)\in SE(2),\qquad
R_e\in SO(2),\quad t_e\in\mathbb R^2.
\]
For an oriented closed edge path \(\gamma=(e_1,\ldots,e_m)\), define the ordered product
\[
H_\gamma=g_{e_m}\cdots g_{e_1}=(R_\gamma,t_\gamma).
\]
The product is independent of arbitrary intermediate coordinate descriptions up to conjugation by a change of base frame. Its conjugacy-invariant rotational angle is the discrete Frank angle (modulo \(2\pi\)); the translational component, expressed in the chosen base frame, is the discrete Burgers closure vector. The translation component is frame-dependent under a change of origin, so the base point/frame convention must always be recorded.

**Definition 92.2 (discrete Frank and Burgers closure data).**
\[
\Omega_\gamma=\operatorname{Arg}(R_\gamma)\pmod{2\pi},
\qquad
b_\gamma=t_\gamma.
\]
The pair \((\Omega_\gamma,b_\gamma)\) is the \(SE(2)\) closure defect of the path. It is not assumed that either component is nonzero.

For \(SE(2)\), the multiplication rule is
\[
(R_2,t_2)(R_1,t_1)=(R_2R_1,\;t_2+R_2t_1).
\]
This semidirect-product term matters: in general the translational closure cannot be obtained by simply adding edge translations without transporting them into a common frame. A pure rotation can also affect the translation accumulated around a circuit.

## 4. Continuum Cartan interpretation

Let \(e^a\) be a coframe and \(\omega^a{}_b\) a metric-compatible connection on an oriented two-dimensional region. Define
\[
T^a=de^a+\omega^a{}_b\wedge e^b,\qquad
R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\]
Here \(T^a\) is the torsion 2-form and \(R^a{}_b\) the curvature 2-form.

For a small loop bounding a surface \(S\), the rotational part of the Cartan/connection holonomy is, to leading order,
\[
\Omega_\gamma \simeq \int_S R
\]
in the oriented planar sector (with the appropriate representation and sign convention). The translational closure of the affine/Cartan development is, to leading order,
\[
b_\gamma^a \simeq \int_S T^a,
\]
provided the coframe and connection are used consistently and the integrand is parallel-transported to a common reference frame. For finite loops, path ordering and connection-dependent transport terms must be retained; the displayed surface integrals are not asserted as unrestricted exact identities.

This gives the geometric identification:
\[
\boxed{\text{Frank rotational closure}\ \leftrightarrow\ \text{curvature},\qquad
\text{Burgers translational closure}\ \leftrightarrow\ \text{torsion}.}
\]
The identification is standard Cartan-geometric defect kinematics once the connection/coframe convention is fixed. It does not by itself derive a material constitutive law, a stress field, or a force-balance equation.

## 5. The Morandotti bridge: kinematics to elastic equilibrium

The next step is problem-specific. In planar defect elasticity, Frank data describe wedge-disclination content and Burgers data describe edge-dislocation content. They enter the incompatibility constraints for the elastic strain. One then supplies a constitutive tensor \(\mathbb C\), boundary conditions, core regularisation/source conventions, and solves the equilibrium problem
\[
\operatorname{div}\sigma=0,\qquad \sigma=\mathbb C\varepsilon,
\]
with the strain constrained by the prescribed defect incompatibility.

In two dimensions an Airy potential \(v\), with the convention
\[
\sigma_{11}=\partial_{22}v,\qquad
\sigma_{22}=\partial_{11}v,\qquad
\sigma_{12}=-\partial_{12}v,
\]
automatically satisfies the interior equilibrium equation in the absence of body forces. The remaining equation and boundary data encode the defect sources and elastic response.

The relevant published benchmark is:

P. Cesana, L. De Luca, M. Morandotti, “Semidiscrete Modeling of Systems of Wedge Disclinations and Edge Dislocations via the Airy Stress Function Method,” *SIAM Journal on Mathematical Analysis* 56 (2024), 79–136, DOI: 10.1137/22M1523443.

The Two-Circle construction supplies a possible local geometric cell language for discretising the domain and transporting local frames. The cited work supplies a rigorous elasticity framework for specified disclination/dislocation systems. This record does not claim that the paper uses the Two-Circle construction, nor that its hypotheses follow automatically from local triangulability.

## 6. Relation to T091 and the existing two-core computation

T091 starts after the defect sources have already been specified and a finite-dimensional linear reconstruction has been chosen. It proves, for that reconstruction and common facet-jump convention,
\[
j=j_F+j_B,\qquad
T=T_F+T_B+T_{FB},
\]
where \(j_F,j_B\) are the Frank and Burgers traction-jump contributions and \(T_{FB}\) is the signed mixed tensor.

T092 supplies the preceding geometric/kinematic interpretation of the source labels. The dependency chain is therefore
\[
\text{local two-circle cell}
\to \text{compatible cell complex (additional hypotheses)}
\to SE(2)\text{ transport and closure}
\to (\Omega,b)
\to (R,T)\text{ Cartan interpretation}
\to \text{elastic incompatibility}
\to \text{Morandotti equilibrium}
\to \text{T091 discrete interaction audit}.
\]

The five-level DOLFINx audit and T091 are numerical/finite-dimensional evidence for the last stages only. They do not verify the construction of a global mesh from arbitrary local cells, a continuum Cartan limit, or convergence of the full RGS–PRISM sequence.

## 7. What is proved, conditional, and open

- **Proved:** Theorem 92.1, the explicit local Euclidean two-circle construction at every interior point and arbitrarily small scale.
- **Exact by definition/algebra:** the \(SE(2)\) product and the decomposition of a discrete closure into rotational and translational components, once edge transitions and a base frame are specified.
- **Conditional continuum interpretation:** curvature/Frank and torsion/Burgers correspondence for a chosen Cartan coframe/connection, with parallel transport and path-ordering conventions stated.
- **Open:** a canonical global cell-generation/refinement algorithm from the local construction; conformity or controlled nonconformity; shape-regularity under anisotropic refinement; convergence of discrete \(SE(2)\) holonomy to Cartan holonomy; derivation of the defect source distributions from the cell geometry; and convergence/stability of the resulting elastic solver.
- **Not claimed:** universal solvability of arbitrary PDEs; exact geodesic equilateral cells on arbitrary curved surfaces; a universal Frank–Burgers constitutive law; or physical validation of RGS–PRISM.

## 8. Immediate proof programme

1. Define the admissible cell complex and its orientation/transition data.
2. Prove a mesh-generation or local-to-global assembly lemma under explicit domain assumptions.
3. Define discrete coframes and discrete \(SE(2)\) connection variables on oriented adjacencies.
4. Prove gauge covariance of loop holonomy and identify the base-frame transformation of \(b_\gamma\).
5. Establish a refinement theorem for rotational and translational holonomy, with separate curvature and torsion consistency estimates.
6. Couple the resulting defect measures to the Morandotti variational/KKT and Airy/C0-IPDG formulations; compare the same source data and boundary conditions.
7. Only after those steps, investigate whether the RGS–PRISM cell family gives a useful alternative refinement and whether anisotropy explains measured residual variation.

**Classification:** local geometric theorem proved; discrete closure formalism exact; continuum and global assembly bridges conditional/open.  
**FLN**
