# Vesica three-circle model and golden homothety: exact audit

**Date:** 2026-11-23  
**Status:** exact result for the explicitly defined model; candidate model only for comparison with the Rapporto Vesica. It is not claimed to reconstruct the report's missing diagram.

## 1. Explicit three-circle configuration

Fix a scale \(R>0\). Take three equal circles of radius \(R\), with centres at the vertices of an equilateral triangle of side \(R\):
\[
c_1=(0,0),\qquad c_2=(R,0),\qquad
c_3=(R/2,\sqrt3R/2).
\]
Each pair of circles intersects in two points. The six distinct pairwise intersection points are
\[
\begin{aligned}
p_1&=(R/2,\sqrt3R/2),&
p_2&=(R/2,-\sqrt3R/2),\\
p_3&=(0,0),&
p_4&=(3R/2,\sqrt3R/2),\\
p_5&=(R,0),&
p_6&=(-R/2,\sqrt3R/2).
\end{aligned}
\]
Here \(p_1,p_3,p_5\) are also the centres of the third circle in the corresponding pairwise intersections. This is a fully specified three-circle arrangement, not an assumption about the undocumented coordinates in the source illustration.

Let \(o=(c_1+c_2+c_3)/3=(R/2,\sqrt3R/6)\) be the centroid. The six vectors \(p_j-o\) have polar angles, in cyclic order,
\[
30^\circ,\ 90^\circ,\ 150^\circ,\ 210^\circ,\ 270^\circ,\ 330^\circ.
\]
Thus the six intersection points determine exactly **six distinct outward ray directions**, equally spaced by \(60^\circ\). Their distances from \(o\) alternate between \(R/\sqrt3\) and \(2R/\sqrt3\). If opposite rays are identified as one unoriented line, there are three lines.

This calculation gives a useful negative test: this canonical equilateral three-circle arrangement does **not** produce an 8-ray or 10-ray family. It is not evidence that every possible Vesica arrangement fails to do so; a different placement or a different ray-selection rule would be a different model.

## 2. The associated angular graph operator

Order the six ray directions cyclically and connect consecutive directions. The resulting angular adjacency graph is the cycle \(C_6\). Its unweighted combinatorial Laplacian is
\[
L_6=2I_6-A(C_6).
\]
Its exact spectrum is
\[
\operatorname{spec}(L_6)=\{0,1,1,3,3,4\}.
\]
This is an exact operator attached to the specified six-ray arrangement. It is a combinatorial angular operator; it is not yet a physical Hamiltonian, a Laplace--Beltrami operator on a surface, or Pellis's Golden Resonance Operator.

If instead one chooses a metric graph Laplacian with edge weights equal to inverse squared Euclidean edge lengths, the operator must be specified with its vertex measure and normalization. That metric choice is not silently identified with \(L_6\).

## 3. Golden hierarchy as homothety

Now scale the entire configuration by
\[
R_n=R_0\phi^{-n},\qquad
\phi=\frac{1+\sqrt5}{2}.
\]
Every point becomes \(p_{j,n}=o+\phi^{-n}(p_j-o)\). A positive homothety preserves angles, coincidences, incidence, and the cyclic order of the six rays. Therefore, at every level \(n\), the ray count remains six.

The combinatorial operator \(L_6\) is unchanged under this scaling. For a metric graph operator whose edge weights are proportional to \(\ell^{-2}\), all edge lengths scale by \(\phi^{-n}\), so the operator scales by \(\phi^{2n}\), subject to the same vertex-measure convention. In neither case does the number of rays change.

Consequently, a sequence of radii in ratio \(\phi\) cannot, by homothety alone, produce the source-reported count sequence
\[
(8,10),\quad(10,12),\quad(14,18).
\]
To obtain changing counts one must add non-homothetic data: for example, a level-dependent rotation, a different circle-incidence pattern, a new set of centres, or a specified rule for selecting and identifying rays. The report excerpt does not state such a rule.

## 4. What would be needed to reproduce the reported grids

A reproducible construction of the 8×10, 10×12, and 14×18 pairs must provide:
1. the centres and radii at each level;
2. the precise pairs of circles defining each Vesica;
3. which intersection points, common chords, or lens boundaries are retained;
4. the origin and angular domain used to define a ray;
5. whether opposite rays count separately;
6. how duplicate or symmetry-equivalent directions are handled;
7. the level-to-level transformation, including any rotation or change in incidence.

Only after these data are fixed can one form the incidence matrix, count distinct directions, construct a graph or cell complex, and define its Laplacian or other operator. An operator chosen before the geometry is fixed would encode the modeller's choice, not a derivation from the report.

## 5. Classification

| Claim | Status |
|---|---|
| The specified equilateral three-circle configuration has six distinct pairwise intersection points | Exact |
| Those points define six equally spaced outward ray directions from the centroid | Exact |
| The angular graph is \(C_6\) and its combinatorial Laplacian has spectrum \(0,1,1,3,3,4\) | Exact for this model |
| Golden homothety \(R_n=R_0\phi^{-n}\) changes the ray count | False for this model; homothety preserves directions and incidence |
| This canonical model derives the report's 8×10 / 10×12 / 14×18 grids | False |
| Some other explicitly defined Vesica arrangement may yield those grids | Open |
| The resulting operator is Pellis's physical resonance operator | Not established |

**Conclusion.** The three-circle model supplies a first exact geometric/operator benchmark and rules out one tempting shortcut: golden scaling of a fixed Vesica arrangement does not generate new ray counts. The source's grid claim remains underdetermined until its actual circle arrangement and ray-counting rule are supplied. No identification with \(S^3/2I\), the Pellis resonance operator, or a physical degree of freedom is asserted.
