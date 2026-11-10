# T074 — Icosahedral shell, binary lift, and Hopf–Seifert spectral bridge

**Status: PARTIALLY PROVED — group-theoretic and fibration statements are standard and proved below; the induced action on the chosen football cell complex and every shell-to-continuum spectral limit remain OPEN.**  
**Purpose:** provide the missing mathematically precise interface between the truncated-icosahedral shell in T073 and the binary-icosahedral spherical quotient in T010/S012. This record does not identify the shell with a spherical space form.

## 1. The two geometries and the exact group map

Let \(I\subset SO(3)\) be the rotational icosahedral group. It is isomorphic to \(A_5\) and has order 60. Let
\[
p:SU(2)\longrightarrow SO(3)
\]
be the standard double covering, and define
\[
2I=p^{-1}(I)\subset SU(2).
\]
Then \(|2I|=120\), and there is an exact sequence
\[
1\longrightarrow\{\pm1\}\longrightarrow 2I
\xrightarrow{\ p\ } A_5\longrightarrow1.
\]
The central element \(-1\) acts trivially under the adjoint/conjugation action on the imaginary quaternions and is the kernel of the covering map.

The truncated icosahedron is a polyhedral surface with rotational symmetry group \(I\cong A_5\). Its boundary is topologically \(S^2\), but its induced metric is piecewise flat and has edges/vertices; it is not the round sphere. The Poincaré homology sphere
\[
P^3=S^3/(2I)
\]
is a different, three-dimensional Riemannian manifold. The common group is a symmetry bridge, not an identification of spaces.

## 2. Hopf map equivariance and the quotient Seifert fibration

Identify \(S^3\) with the unit quaternions, equivalently \(SU(2)\). The Hopf map can be written
\[
h:S^3\longrightarrow S^2,\qquad h(q)=q\,i\,q^{-1},
\]
where \(S^2\) is the unit sphere in the imaginary quaternions. The circle acts on the right by \(q\mapsto qe^{i\theta}\), and this is exactly the Hopf fibre action.

For every \(g\in2I\),
\[
h(gq)=gq i q^{-1}g^{-1}=p(g)\cdot h(q),
\]
where \(p(g)\) acts on the imaginary quaternions by rotation. Thus the Hopf map is \(2I\)-equivariant for the left action on \(S^3\) and the projected \(A_5\)-action on \(S^2\). It descends to
\[
\bar h:S^3/(2I)\longrightarrow S^2/A_5.
\]

The right Hopf circle action commutes with left multiplication by \(2I\), so it descends to a circle action on \(S^3/(2I)\). Consequently \(S^3/(2I)\) is a Seifert-fibred 3-manifold over the orbifold \(S^2/A_5\). The quotient orbifold has underlying topological space \(S^2\) and cone-point orders \((2,3,5)\). This is not an ordinary smooth circle bundle over a smooth quotient surface: exceptional fibres encode the nontrivial stabilizers of the \(A_5\)-action.

**Conclusion 2.1.** The map \(S^3/(2I)\to S^2/A_5\) is an actual quotient of the Hopf fibration, not a visual analogy between a football and a spherical space form.

## 3. The angular invariant sector on the round two-sphere

Let \(\mathcal H_\ell(S^2)\) be the degree-\(\ell\) spherical harmonics, with
\[
-\Delta_{S^2}u=\ell(\ell+1)u,
\qquad \dim\mathcal H_\ell=2\ell+1.
\]
The invariant multiplicity on the orbifold quotient is
\[
d_\ell^{A_5}
=\dim\mathcal H_\ell(S^2)^{A_5}
=\frac1{60}\sum_{g\in A_5}
\operatorname{Tr}\!\left(g\mid\mathcal H_\ell(S^2)\right).
\]
Equivalently, for a rotation of angle \(\theta\), its character on \(\mathcal H_\ell\) is
\[
\chi_\ell(\theta)
=\frac{\sin((\ell+\tfrac12)\theta)}{\sin(\theta/2)},
\]
with the continuous value \(2\ell+1\) at \(\theta=0\). The conjugacy-class sizes in \(A_5\) are 1, 15, 20, 12, 12, with rotation angles \(0,\pi,2\pi/3,2\pi/5,4\pi/5\), respectively. Hence
\[
d_\ell^{A_5}
=\frac1{60}\left[
(2\ell+1)+15\chi_\ell(\pi)
+20\chi_\ell(2\pi/3)
+12\chi_\ell(2\pi/5)
+12\chi_\ell(4\pi/5)
\right].
\]
The first nonconstant invariant harmonic occurs at \(\ell=6\), giving round-sphere eigenvalue \(6\cdot7=42\). This is an exact angular benchmark for the round orbifold sector. It is not an eigenvalue of the piecewise-flat truncated-icosahedral shell, nor of a general elastic shell operator.

## 4. The three-dimensional scalar benchmark is different

For the unit round \(S^3\), scalar harmonics of degree \(n\) have eigenvalue
\[
\lambda_n=n(n+2).
\]
The \(2I\)-invariant subspace gives the scalar spectrum on the round quotient \(S^3/(2I)\). T010 records the character calculation
\[
\lambda_1^{\rm scalar}(S^3/2I)=168,
\qquad m(168)=13.
\]
This corresponds to the first allowed full harmonic degree \(n=12\). It is not obtained by multiplying the two-dimensional value 42 by four; the two operators act on different spaces and their spectra are not identified by the Hopf map.

The Hopf/Seifert structure relates the spaces and their symmetry representations. Any spectral relation between a base operator and a total-space operator requires an explicit decomposition into fibre modes, including the relevant line bundles/orbifold representations and vertical contributions.

## 5. What the shell symmetry actually supplies

Let \(K=(V,E,F)\) be the oriented polyhedral cell complex of the truncated-icosahedral boundary, with
\[
|V|=60,\qquad |E|=90,\qquad |F|=32
\]
(12 pentagonal and 20 hexagonal faces). The rotational group \(A_5\) acts combinatorially on cells and therefore defines permutation representations
\[
\rho_j:A_5\to U(C_j(K;\mathbb C)),\qquad j=0,1,2.
\]
For each chain degree define the exact Reynolds projector
\[
P_j=\frac1{60}\sum_{g\in A_5}\rho_j(g).
\]
It satisfies \(P_j^2=P_j=P_j^*\). Since the boundary maps are equivariant,
\[
\partial_j\rho_j(g)=\rho_{j-1}(g)\partial_j,
\qquad
\partial_jP_j=P_{j-1}\partial_j.
\]
Thus the invariant chain spaces form a subcomplex. These identities are exact once the actual combinatorial action and orientation conventions have been constructed.

For a discrete operator \(A_j\) on \(C_j(K)\), symmetry reduction is valid only if
\[
A_j\rho_j(g)=\rho_j(g)A_j\quad\text{for all }g\in A_5.
\]
This commutation is guaranteed for an operator assembled from fully \(A_5\)-equivariant geometry and constitutive data. It is not guaranteed by the combinatorial symmetry alone. In particular, panel-dependent orthotropy, seam weights, defects, or boundary conditions may break the symmetry. The symmetry-breaking residuals must then be measured rather than projected away.

The exact character of each cell representation is computable from the fixed-cell counts (including orientation signs where oriented chains are used):
\[
\chi_{C_j}(g)=\operatorname{Tr}\rho_j(g).
\]
The irreducible multiplicities follow from
\[
m_\alpha(C_j)=\frac1{60}\sum_{[g]}
|[g]|\,\overline{\chi_\alpha(g)}\,\chi_{C_j}(g).
\]
No decomposition of \(C_0,C_1,C_2\) is asserted in this record until the actual shell incidence data and all 60 group permutations have been checked. Cell counts alone do not determine the representations.

## 6. The missing analytic bridge to T073 and Morandotti

The following are separate implications, not one automatic theorem:
1. **Combinatorial equivariance:** construct the \(A_5\)-action on the shell cell complex and prove the chain identities in §5.
2. **Discrete operator equivariance:** prove commutation for the chosen mass, stiffness, seam and defect operators. If the material data break symmetry, decompose the operator into symmetric and symmetry-breaking parts.
3. **Geometric approximation:** define comparison maps from refined shell meshes to a specified limit surface and prove metric, measure, normal and bundle convergence.
4. **Variational limit:** specify the bulk and interface densities and prove equicoercivity plus the liminf and recovery-sequence inequalities for the intrinsic structured-deformation functional. The Euclidean periodic structured-deformation homogenisation theorem of Amar–Matias–Morandotti–Zappale does not by itself establish this curved-shell result.
5. **Mosco/operator limit:** for closed quadratic forms on varying Hilbert spaces, define the identification maps and prove both Mosco inequalities and compactness/resolvent hypotheses.
6. **Spectral limit:** only after the operator/form convergence and compactness conditions are established may one infer convergence of eigenvalues and spectral subspaces, with multiplicities handled by spectral projections.

The spherical quotient benchmarks in §§3–4 are reference spectra for symmetry sectors. They do not supply the missing compactness, coercivity, consistency, or recovery sequences for the football-shell refinement.

## 7. Explicit proof-status ledger

| Statement | Status |
|---|---|
| \(2I\to A_5\) is the binary double cover with kernel \(\{\pm1\}\) | Proved standard group theory |
| Hopf map is equivariant for left \(2I\) and projected \(A_5\) actions | Proved by the identity in §2 |
| \(S^3/2I\to S^2/A_5\) is the induced Seifert fibration | Proved |
| Orbifold cone orders are \((2,3,5)\) | Proved from stabilizers of the icosahedral rotation action |
| Round \(S^2/A_5\) first nonconstant invariant harmonic is degree 6 | Exact character calculation; formula given in §3 |
| Round \(S^3/2I\) scalar first eigenvalue is 168 with multiplicity 13 | Recorded in T010 |
| Actual cell permutation characters for the repository football mesh | Open: construct and verify all permutations |
| Commutation of the actual shell stiffness/mass with \(A_5\) | Conditional on symmetric geometry/material data; otherwise quantify defect |
| Spectral convergence from shell refinements to a spherical quotient | Open; no identification or theorem claimed |
| Morandotti structured-deformation Γ-limit on the curved shell | Open |

## 8. Required reproducible computation

The next computational artifact must be generated from the repository's actual vertex coordinates and face incidence, not from hard-coded character decompositions. It must:

- construct the 60 proper rotational symmetries as permutations of the 60 vertices;
- verify closure, identity, inverses, and the \(A_5\) conjugacy-class sizes;
- induce edge and face permutations from incidence;
- construct oriented boundary matrices and verify \(\partial_1\partial_2=0\);
- verify equivariance of both boundary maps;
- calculate the five irreducible character multiplicities for each chain representation;
- test \([K_h,\rho(g)]\) and \([M_h,\rho(g)]\) for the actual shell matrices, reporting absolute and relative residuals.

Until this artifact exists, the group/Hopf bridge is proved, but the shell representation-theory bridge is not yet computationally closed.

## References

- T010, *Rumin spectral reduction on the Poincaré homology sphere*.
- S012, *Ikeda (1995): cyclic and binary-polyhedral scalar spectra*.
- T073, *Unified football-shell / RGS–PRISM–Q6 limit programme*.
- Standard Hopf fibration \(S^1\to S^3\to S^2\), the double cover \(SU(2)\to SO(3)\), and the rotational icosahedral group \(A_5\).
