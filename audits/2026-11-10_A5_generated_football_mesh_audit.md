# A5 action audit of the generated football shell

**Scope:** audit of the *generated reference mesh* in `models/football_shell.py`, not a measured football scan.  
**Status:** exact topology and induced group action specified; numerical character decomposition and operator commutators are pending execution against the repository runtime.

## 1. Source inspected

The mesh is generated from the regular icosahedron by directed-edge truncation. The generator creates:
- 60 truncated vertices, indexed by directed edges of the icosahedron;
- 12 pentagonal panels, one around each icosahedron vertex;
- 20 hexagonal panels, one for each icosahedron face;
- 32 polygonal panels in total;
- 90 physical seams, i.e. polygon-boundary edges;
- 92 mechanical nodes after adding one centre node per panel;
- 180 fan triangles and 270 triangular-mesh hinges.

These counts are encoded in `models/football_shell.py` and independently summarized in `docs/FOOTBALL_ORTHOTROPIC_DISCRETE_SHELL.md`. The 90 seams are not the 270 hinges: the latter include internal fan edges.

## 2. Exact combinatorial action

Every rotational symmetry of the regular icosahedron permutes its 12 vertices, 30 edges and 20 triangular faces. It therefore acts on a directed icosahedron edge `(i,j)), hence on each of the 60 truncated vertices. It also acts on the 12 pentagonal and 20 hexagonal panels.

The proper rotational subgroup has order 60 and is isomorphic to (A_5). The induced permutations preserve the incidence relation between truncated vertices and panels, and consequently preserve the 90 polygon-boundary seams. This gives genuine permutation representations on:
[
C_0^{m shell}congmathbb C^{60},qquad
C_1^{m seam}congmathbb C^{90},qquad
C_2^{m panel}congmathbb C^{32}.
]
For unoriented cell spaces, the Reynolds operators are
[
P_j=\frac1{60}\sum_{g\in A_5}\rho_j(g),\qquad P_j^2=P_j=P_j^*.
]
For oriented chains, edge and face permutations must additionally carry orientation signs. The polygonal panel complex is a cell decomposition of the closed sphere; its cellular boundary matrices satisfy (partial_1partial_2=0) and commute with the induced signed group action.

## 3. Critical distinction: combinatorial symmetry versus mechanical symmetry

The *reference combinatorics* has (A_5) symmetry. The actual numerical stiffness need not.

The shell solver assigns a material frame to each panel using its first listed edge and a common material angle. A common scalar angle in these locally chosen frames does not automatically define an (A_5)-equivariant orthotropic tensor field. In particular:
- the isotropic material case is compatible with the full geometric symmetry, provided all seam and hinge coefficients are constant on group orbits;
- an orthotropic panel law is (A_5)-equivariant only if the material axes are transported equivariantly under every rotation;
- nonuniform seam reinforcement, panel defects, or imposed data can further break the symmetry;
- nonzero cube/sphere and (H_4) radial shape modes generally break (A_5), since they impose cubic rather than icosahedral symmetry.

Thus the valid test is not merely a group action on vertices. It is
[
\|K\rho(g)-\rho(g)K\|,\qquad
\|M\rho(g)-\rho(g)M\|
]
for every group element, with both absolute and relative residuals. If the material model is anisotropic, its local constitutive tensors must first be transformed and checked under the group action.

## 4. What is and is not established from the current repository

Established from the generator and topology:
- the generated shell has 60/90/32 vertex/seam/panel counts;
- its incidence is induced from the icosahedral truncation;
- its *reference combinatorics* inherits the proper icosahedral action;
- the 92-node mechanical mesh is a fan refinement of the 32 polygonal panels.

Not established by the currently committed report:
- the five (A_5)-irreducible multiplicities of the 60-, 90-, and 32-dimensional representations;
- signed cellular boundary equivariance in a committed executable certificate;
- commutation of the actual assembled (K) and (M) with all 60 rotations;
- (A_5)-equivariance of the default orthotropic material frames;
- any identification of this finite shell spectrum with the spectrum of (S^3/2I).

No experimental point cloud is present: `data/scans/football_scan_template.csv` is only an empty template. The current model is therefore a generated mathematical reference geometry, not a fitted physical football.

## 5. Required next numerical certificate

The executable audit must:
1. recover all 120 automorphisms of the icosahedral graph and retain the 60 orientation-preserving ones;
2. induce permutations on directed-edge vertices, polygon panels, and polygon-boundary seams;
3. verify group closure and the (A_5) conjugacy-class sizes (1,15,20,12,12);
4. build signed cellular boundary matrices and check (partial_1partial_2=0) and equivariance;
5. compute the character inner products for all five irreducible (A_5) characters;
6. assemble isotropic and orthotropic (K,M), report all commutator residuals, and identify exactly which material-frame conventions preserve the symmetry.

The character multiplicities are deliberately not guessed from the dimensions 60, 90 and 32. They must be generated from the actual induced permutations and checked by character orthogonality.

## 6. Consequence for T074

The group/Hopf/Seifert bridge in T074 is an exact continuous group-theoretic result. This audit supplies the finite-shell side at the level of its generated combinatorics. The missing bridge is now sharply localized: calculate the actual cell characters and determine the symmetry subgroup of each assembled mechanical operator. Only after that can shell modes be compared with (A_5)-invariant spherical harmonics and, via the Hopf/Seifert representation decomposition, with (2I)-invariant modes on (S^3/2I).

**No spectral equivalence is claimed.**
