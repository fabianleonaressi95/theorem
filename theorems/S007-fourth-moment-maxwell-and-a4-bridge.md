# S.7 — Fourth-moment Maxwell obstruction and common A4 intertwiner

**Status: PROVED algebraic no-go and finite-group representation statements; Maxwell constitutive response is a candidate.** The record preserves the tensor-index obstruction and the correct subgroup-level route.

## 1. No direct rank-four correction built from two antisymmetric field strengths

Let (R_{ijkl}) be fully symmetric and (F_{ij}=-F_{ji}). Then
[
R_{ijkl}F_{ij}F_{kl}=0.
]
Indeed, interchanging (i) and (j) leaves (R) unchanged but changes the sign of (F_{ij}); hence the contraction equals its negative. This is an exact index-symmetry obstruction. The fourth-moment residual cannot be inserted directly as a nonzero (RFF) Maxwell term, nor identified with a Riemann-type constitutive tensor or teleparallel torsion.

## 2. Correct intermediate: an independent STF order parameter

For (Qinoperatorname{Sym}_0(3)), define
[
A(Q)_{ij}=R_{ijkl}Q_{kl}.
]
The trace-free pair contractions of (R) imply (A(Q)inoperatorname{Sym}_0(3)). A possible electric/magnetic constitutive ansatz is
[
Z_E(Q)=z_EI+g_EA(Q),qquad Z_B(Q)=z_BI+g_BA(Q),
]
with (z_E,z_B>0). Positivity is guaranteed, for example, if
[
|g_E|,|A(Q)|_2<z_E,qquad |g_B|,|A(Q)|_2<z_B.
]
The density
[
mathcal L_{EM}(Q)=rac12E^TZ_E(Q)E-rac12B^TZ_B(Q)B
]
is a well-defined candidate material constitutive law. It is not derived from the Wilson measure and does not predict the fine-structure constant.

If (Q) is integrated with a centered (Qmapsto-Q) symmetric measure, then (langle A(Q)angle=0); the first-order anisotropic correction to the vacuum quadratic Maxwell term vanishes. A Gaussian (Q) coupled linearly to (F^2) produces an (F^4) term at leading nontrivial order. A nonzero background, non-centred measure or Wilson-induced field dependence must be derived before a quadratic anisotropic response can appear.

## 3. Full-group obstruction and common tetrahedral subgroup

The full groups (A_5) and (O_h) cannot be identified by a nontrivial homomorphism (A_5	o O_h): since (A_5) is simple, the kernel is either all of (A_5) or trivial; injectivity is impossible because (60) does not divide (48). Therefore a nonzero full-(A_5)-equivariant map into an (O_h)-representation is not the correct demand.

Both groups contain a tetrahedral subgroup (A_4):
- (A_4subset A_5), as the stabilizer of one letter in the natural five-letter action;
- (A_4subset O_h), as the proper tetrahedral rotation subgroup.

For the five-dimensional irreducible representation of (A_5), the restricted character on the (A_4) classes (identity, double transpositions, and the two 3-cycle classes) is
[
chi_{5downarrow A_4}=(5,1,-1,-1).
]
Using the (A_4) irreducible characters gives
[
oxed{5downarrow A_4=1'oplus1''oplus3.}
]
On the RGS side,
[
operatorname{Sym}_0(3)=E_goplus T_{2g},
]
and restriction to the same tetrahedral subgroup gives (E_gdownarrow A_4=1'oplus1'') (as a real two-plane) and (T_{2g}downarrow A_4=3). Thus the two five-dimensional real representations have the same (A_4) type, and an (A_4)-equivariant real isomorphism exists after restriction.

It is not canonical. One must choose common generators and bases, solve
[
Tho_{Q6}(h)=ho_{STF}(h)T
]
for generators (h) of (A_4), and fix independent normalization/sign freedoms on the 2- and 3-dimensional blocks. Equality of dimensions alone is not an intertwiner.

## 4. Real representation type and bundle compatibility

The real two-dimensional representation obtained from (1'oplus1'') is of complex type, while the three-dimensional block is of real type. The real commutant is
[
operatorname{End}_{A_4}(V_5)simeqmathbb Coplusmathbb R.
]
This leaves a phase/rotation freedom on the real two-plane and a sign on the real three-dimensional block once invariant inner products and bases are fixed. It does not establish a quaternionic structure. Such a structure requires an antiunitary (J) commuting with the action and satisfying (J^2=-I); no such (J) is provided by this representation argument.

For a principal (G)-bundle (P	o M), representation (ho), and associated bundle (E=P	imes_ho V), a principal connection induces (
abla=d+ho_*(omega)). An (A_4)-intertwiner induces a bundle map only when the reductions and transition functions use the same (A_4) action. It is connection-preserving only if
[

abla_{RGS}circPhi=Phicirc
abla_{Q6}.
]
Representation equivalence alone does not imply this equation.

## 5. Evidence and open obligations

- **PROVED:** (R_{ijkl}F_{ij}F_{kl}=0) for fully symmetric (R) and antisymmetric (F); (R:Qinoperatorname{Sym}_0(3)); common (A_4) restriction type (2oplus3); existence (not canonicity) of an (A_4)-intertwiner under the stated representation hypotheses; real commutant type.
- **NUMERICALLY VERIFIED in companion implementation:** positive electric/magnetic response matrices for the declared test inputs and (O_h)-covariance of the simultaneous tensor transformation.
- **CANDIDATE:** Q-dependent Maxwell constitutive response.
- **OPEN:** actual Q6-to-STF intertwiner matrices; derivation of (Q) from PSU/Anti-Twin/coframe geometry; derivation of the (Q)-measure from the complete nonlinear Wilson fibre; connection compatibility; scalar Maxwell normalization and any fine-structure-constant prediction.

The five retained Q6 modes and the RGS (E_goplus T_{2g}) space must be compared through the explicit common (A_4) action. No full (A_5cong O_h) identification is asserted.

## 6. Implementation provenance

The companion bridge paths are src/rgs_fourth_moment_maxwell_bridge.py and tests/test_rgs_fourth_moment_maxwell_bridge.py. The source audit checks the direct antisymmetric contraction, positivity, (O_h)-covariance and trace-free response. The actual Q6 (A_4)-intertwiner remains open.
