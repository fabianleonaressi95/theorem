# T164 — Quaternionic resolution of the Q6 three-branch incidence

**Status:** exact local quaternionic and spin-lift identities; local PL junction model defined. Global assembly over all Q6 branch faces remains OPEN.

## 1. The incidence defect in T163

T163 gives 60 coordinate 4-cells and 160 coordinate 3-faces. Each 3-face is incident to three 4-cells. This is not the local incidence of a regular 4-manifold across a codimension-one face, where there are two sides.

A quaternion-valued frame change alone cannot alter this incidence number. The topological resolution must replace the singular neighbourhood, not merely relabel its fibres.

## 2. A local PL replacement: three sectors around a codimension-two core


For the Lorentzian realization, take the core tangent plane to have signature ((+,-)), spanned by time and the spatial axis (n=(1,1,1)/\sqrt3). Its orthogonal normal 2-plane is spacelike. The three (2\pi/3) wedges therefore lie in a Euclidean transverse disk, and the quaternion (q_*) rotates precisely this normal plane while leaving the timelike core plane fixed. The local model is
[
\mathbb R^{1,1}_{\rm core}\times D^2_{\rm spacelike}.
]

Replace the neighbourhood of a triple 3-face by
[
mathcal N simeq mathbb R^2_{m core}	imes D^2_{perp}.
]
Partition the transverse disk into three closed wedges of angle (2pi/3). The three 4D sectors are
[
mathcal S_a=mathbb R^2_{m core}	imes W_a,qquad a=0,1,2.
]
Their pairwise interfaces are
[
mathcal I_{01},quadmathcal I_{12},quadmathcal I_{20},
]
each a 3D hypersurface shared by exactly two sectors. All three interfaces meet along the common 2D core (mathbb R^2_{m core}).

The transverse link of the core is the circle with three vertices and three edges:
[
L_{m core}=C_3simeq S^1.
]
Every link vertex has degree two; every interface has exactly two adjacent sectors. Since the three wedges fill the disk once, this local replacement is topologically a 4-ball neighbourhood (with a possible conical metric/connection defect if the geometric sector angles do not sum to (2pi)).

This is a genuine local incidence resolution, unlike a change of gauge labels. It does not yet prove that the 160 replacements can be glued globally without overlaps or incompatible boundary subdivisions.

## 3. The binary-icosahedral quaternion

Use the scalar-first Hamilton convention and set
[
q_*=rac{1+i+j+k}{2}.
]
This is one of the 120 unit quaternions of the already implemented binary icosahedral group (2I). It obeys
[
q_* i q_*^{-1}=j,quad
q_* j q_*^{-1}=k,quad
q_* k q_*^{-1}=i,
]
[
q_*^3=-1,qquad q_*^6=1.
]
Its projection to (SO(3)) is a rotation through (2pi/3) about the ((1,1,1)/sqrt3) axis and has order three. Its lift in (SU(2)) has order six.

Thus the same element implements the cyclic permutation of the three branch labels and records the nontrivial central sign seen by spinors after one full three-sector circuit.

## 4. Vector closure versus spin closure

Take the three cyclic spin transitions all equal to (U(q_*)), where (U:SU(2)	o SO(3)) is the double-cover representation. Then
[
U(q_*)^3=-I_2,
]
while their vector rotations satisfy
[
pi(U(q_*))^3=I_3.
]
This is not a contradiction: the vector frame closes, while its chosen spin lift returns with the central sign.

There are two distinct possibilities:

1. **Uncompensated spin junction:** the spinor acquires holonomy (-I_2). This is a genuine (mathbb Z_2) spinorial defect/monodromy around the core.
2. **Closed spin lift:** choose lift signs ((-q_*,q_*,q_*)) on the three interfaces. Since (q_*) and (-q_*) induce the same (SO(3)) rotation, the vector geometry is unchanged, while the spin product becomes (+I_2).

The sign assignment is a lift-cocycle choice. It must be globally consistent on the network of junctions; it cannot be selected independently at every face without checking cocycle constraints and the resulting spin structure.

## 5. PSU–Anti-Twin is a separate factor

Let
[
J_{AT}=	au_x=egin{pmatrix}0&1\1&0end{pmatrix},
qquad J_{AT}^2=I.
]
The quaternionic spin transport acts on the spinor factor; (J_{AT}) acts on the two-sheet factor. On the tensor product they commute:
[
[U(q_*)otimes I_2, I_2otimes J_{AT}]=0.
]
The central spin sign (-I_2) is **not** the PSU–Anti-Twin sheet exchange. They are different representations and different (mathbb Z_2) data. A future model may couple them through a derived action, but no identification is assumed here.

## 6. What this resolves, and what it does not

**Resolved locally:** the three-way codimension-one incidence can be replaced by a codimension-two three-sector junction whose transverse link is (C_3); the binary-icosahedral quaternion supplies a canonical cyclic (SU(2)) transport; vector and spin holonomies are computed separately; the independent Anti-Twin factor is retained.

**Still open globally:**
- construct a common subdivision of the boundaries of all 60 four-cells;
- assign each of the 160 triple faces a compatible 2D core and three pairwise interfaces;
- check all edge/vertex links after replacement (in particular every 4D vertex link must be (S^3) for a PL 4-manifold);
- audit projected-cell overlaps and orientation consistency;
- solve the global (mathbb Z_2) lift-cocycle constraints;
- extend the compact quaternionic (SU(2)) transport to the Lorentzian spin group (Spin^+(1,3)simeq SL(2,mathbb C)), using complexified quaternions/biquaternions for boosts;
- couple the resulting connection to the independent Cartan coframe and compute torsion/curvature and throat matching.

The quaternionic element handles the compact rotational part. It does not by itself encode Lorentz boosts or prove a global Lorentzian manifold.

## 7. Reproducible implementation

Companion repository:
- `src/quaternionic_branch_junction.py`
- `tests/test_quaternionic_branch_junction.py`

The audit checks (2I)-membership, quaternion norm and powers, cyclic conjugation of (i,j,k), the (C_3) transverse link, the two possible spin-lift products, and the independence of sheet exchange.

## 8. Evidence classification

- **PROVED EXACTLY:** (q_*in2I), (q_*^3=-1), cyclic conjugation, order-six spin lift and order-three vector rotation.
- **PROVED LOCALLY BY THE MODEL:** three wedges fill a transverse disk; each interface has two incident sectors; the transverse link is (C_3simeq S^1).
- **NUMERICAL TESTS:** implementation diagnostics and tensor-factor commutator; CI must be checked separately.
- **OPEN:** global PL gluing, global spin structure, Lorentzian (SL(2,mathbb C)) lift, Cartan equations and continuum/Sakharov limit.


## 9. Global incidence-level audit over the 60 Q6 four-cells

The combinatorial part of the junction network can be solved globally, before solving the geometric embedding.

Enumerate the 60 coordinate 4-faces as vertices of an adjacency graph. Each of the 160 coordinate 3-faces determines an ordered triple of incident 4-cells. Replace that triple by its three pairwise interface edges. The exact counts are:
[
|V|=60,qquad |J|=160,qquad |E_{m pair}|=3|J|=480.
]
No pairwise interface edge is repeated: every pair of 4-cells occurs in exactly one triple junction. Consequently every 4-cell has degree 16 in this graph, and the graph is connected.

This edge-disjointness gives an explicit global solution of the **incidence-level** spin-lift sign constraints. On each ordered junction cycle ((a,b),(b,c),(c,a)), assign lift signs ((-1,+1,+1)). Their product is (-1), which cancels (q_*^3=-1); hence every junction spin product is (+1). Since each pairwise interface belongs to only one junction, no edge receives conflicting sign assignments.

This proves consistency of the Z2 signs on the pairwise-interface graph. It does **not** yet prove compatibility of the geometric 3D interface subdivisions where different junctions meet along lower-dimensional Q6 cells. The global PL 4-manifold condition, including every vertex link being (S^3), remains open.

The executable companion audit is `audit_global_q6_spin_lift_cocycle()` in `src/quaternionic_branch_junction.py`; tests are in `tests/test_quaternionic_branch_junction.py`.


## 10. Lorentzian completion of the quaternionic rotation factor — T165

The compact (SU(2)) junction transport now has an explicit Lorentzian extension through (Spin^+(1,3)\simeq SL(2,\mathbb C)). Minkowski vectors are Hermitian (2\times2) matrices (X=x^0I+x^i\sigma_i), and (X\mapsto AXA^\dagger) preserves (det X=x^T\eta x). Unit quaternions give the spatial rotation subgroup; Hermitian exponentials (\exp(\chi n\cdot\sigma/2)) give boosts. See T165 for the exact representation and numerical audit.

This removes the algebraic gap between compact quaternionic rotations and Lorentzian spin transformations. It does not yet provide the actual edge field (A_{vw}\in SL(2,\mathbb C)) on the globally resolved Q6 complex or solve its Cartan equations.
