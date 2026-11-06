# Serhii Herasymov: symbolic billiards, curved-surface slicing, and recursive 3D fields

## Source identity and provenance

The author is **Serhii Herasymov**, Medium handle
[\`@sergeygerasimofff\`](https://medium.com/@sergeygerasimofff), GitHub
[\`xcontcom\`](https://github.com/xcontcom), website
[\`xcont.com\`](https://xcont.com).

Primary public sources inspected for this integration:

- [Medium profile](https://medium.com/@sergeygerasimofff)
- [Billiard Fractals: Patterns from Simple Reflections](https://medium.com/@sergeygerasimofff/billiard-fractals-patterns-from-simple-reflections-c1ac1d93ecd4)
- [\`billiard-fractals\` repository](https://github.com/xcontcom/billiard-fractals), especially \`docs/article.md\`, \`js/sequences.js\`, \`js/binarypattern.js\`, \`js/hologram_s.js\`, \`js/hologram_dynamic.js\`
- [Perfect Shuffle: The Strange Fractals Hidden in a Simple Algorithm](https://medium.com/@sergeygerasimofff/perfect-shuffle-the-strange-fractals-hidden-in-a-simple-algorithm-6e65e134a516)
- [\`perfect-shuffle\` repository](https://github.com/xcontcom/perfect-shuffle), especially \`fractal_3d_2.js\` and \`fractal_3d_with_rotaions.js\`
- [\`fractogenesis\` repository](https://github.com/xcontcom/fractogenesis)
- [Evolving Cellular Automata](https://medium.com/@sergeygerasimofff/evolving-cellular-automata-72e9d12e2814) and [\`evolving-cellular-automata\`](https://github.com/xcontcom/evolving-cellular-automata)
- [\`initial-state-evolution\`](https://github.com/xcontcom/initial-state-evolution)

The Medium articles describe the first two projects as translations/adaptations of earlier Habr articles. The repositories are MIT-licensed according to their repository pages; preserve their authorship and licenses if code is reused.

**Attribution boundary.** The inspected Herasymov sources do not establish that he introduced the \(W(G_2)\) construction, the \(R_T\mapsto V_T\) normal lift, or the Möbius seam formula in this repository. Those remain separate RGS/project constructions unless a primary source explicitly links them. Herasymov's verified contribution here is the computational chain below.

---

## 1. Billiard geometry to symbolic dynamics

A ray reflecting in a rectangle can be unfolded into a straight line in a periodically tiled plane. The reflection sequence is therefore encoded by integer crossings and parity changes. Herasymov's implementation constructs a deterministic binary pattern from a rectangular grid and a reflected diagonal path.

The article studies coprime dimensions and Fibonacci pairs:
\[
(F_n,F_{n+1})=(8,13),(13,21),(21,34),(34,55),\ldots,
\qquad
\frac{F_{n+1}}{F_n}\longrightarrow\varphi.
\]
The refinement is a rational approximation to a golden aspect ratio, not by itself a proof of a self-similar continuum limit. The exact parity and boundary behavior depend on the integer pair and must be retained in any convergence argument.

The repository also presents floor/parity codings such as
\[
q_k=\lfloor k\sqrt{\xi}\rfloor\bmod 2
\]
and nonlinear variants such as
\[
q_k=\lfloor k^2\sqrt{\xi}\rfloor\bmod 2.
\]
These are deterministic symbolic codings. The phrase “Sturmian” should be used carefully: the classical mechanical/Sturmian word is normally a difference of consecutive floor values,
\[
s_k=\lfloor(k+1)\theta+\beta\rfloor-\lfloor k\theta+\beta\rfloor,
\]
or an equivalent coding of an irrational circle rotation. Parity of \(\lfloor k\theta\rfloor\) is a different coding and should not be called Sturmian without a separate complexity/rotation proof.

The JavaScript routine \`sequence(m,n)\` is a concrete finite-grid construction. It initializes \(m/2\) bits and flips selected positions according to the parity of \(\lfloor 2kn/m\rfloor\). This is the exact implementation target for the audit; it should not be silently replaced by a different symbolic sequence.

## 2. The actual curved-surface formula and its differential geometry

The source code \`hologram_s.js\` implements, after centering pixel coordinates,
\[
\zeta(x,y)=a\left(c_4^2+x^2+bxy+cy^2\right)^{1/d},
\qquad a=\frac{a_1}{a_2},
\]
and produces binary/continuous fields using
\[
Q_{\mathrm{bin}}(x,y)
=\left\lfloor(\mathrm{phase}+\zeta(x,y))\sqrt2\right\rfloor\bmod2,
\]
\[
Q_{\mathrm{cont}}(x,y)
=\left\lfloor128\left[
1+\sin\bigl(2\pi\,\mathrm{phase}
+\pi\sqrt2\,\zeta(x,y)\bigr)
\right]\right\rfloor.
\]
The article also writes the more general family
\[
z=a(x^2+bxy+cy^2)^d.
\]
The source-code exponent is \(1/d\), whereas the prose formula is displayed with exponent \(d\). This is a source-level convention discrepancy; for reproducibility, the audit records the executable \`hologram_s.js\` convention \(1/d\), and the two parameterizations must not be conflated.

Set
\[
q(x,y)=c_4^2+x^2+bxy+cy^2,\qquad p=1/d,\qquad z=a q^p.
\]
On a domain where \(q>0\),
\[
z_x=apq^{p-1}(2x+by),\qquad
z_y=apq^{p-1}(bx+2cy).
\]
The graph embedding is
\[
X:\Omega\subset\mathbb R^2\to\mathbb R^3,
\qquad X(x,y)=(x,y,z(x,y)).
\]
Its Jacobian and induced metric are
\[
J_X=
\begin{pmatrix}
1&0\\0&1\\z_x&z_y
\end{pmatrix},
\qquad
g=J_X^TJ_X=
\begin{pmatrix}
1+z_x^2&z_xz_y\\z_xz_y&1+z_y^2
\end{pmatrix},
\]
\[
\boxed{\det g=1+|\nabla z|^2>0.}
\]
This is an exact differential-geometric bridge from Herasymov's 2D parameter domain to a 3D embedded surface. It is directly compatible with the pullback metric machinery used in curvilinear FEEC, once the surface is meshed with compatible charts.

Domain conditions matter. For noninteger \(p\), require \(q>0\) (or specify a real branch and its regularity). A sufficient condition for the quadratic part \(x^2+bxy+cy^2\) to be positive definite is \(c>b^2/4\); adding \(c_4^2>0\) can relax this on a bounded domain. If \(q=0\), differentiability depends on \(p\). If \(q<0\), the JavaScript fractional power may become non-real/NaN. Hyperbolic cases such as \(x^2-y^2\) are admissible for integer powers but not automatically for arbitrary real powers.

The binary threshold field is discontinuous. It should be treated as a cell/dual-vertex label or coefficient field, not as a conforming \(H^1\) finite-element 0-form without reconstruction. A sound FEEC bridge is:
1. mesh \(\Omega\) and map cells by \(X\);
2. compute the induced metric \(g\) and area density \(\sqrt{\det g}\);
3. sample \(Q_{\rm bin}\) as a symbolic label on the dual mesh;
4. if a continuous FEEC field is required, define an explicit projection/reconstruction and prove its stability and commuting properties.

## 3. Perfect shuffle: exact finite permutation and recursive 3D voxel construction

For an array of length \(2n\), the in-shuffle in the repository sends the element at position \(i\) to
\[
\boxed{\sigma(i)=2i+1\pmod{2n+1}},\qquad 0\le i<2n.
\]
This is a permutation. Its order is the multiplicative order of \(2\) modulo \(2n+1\), since
\[
\sigma^k(i)+1\equiv2^k(i+1)\pmod{2n+1}.
\]
This explains the modular arithmetic used in the article's return-period routine. The position recurrence printed in the article is the inverse-position update (which source slot supplies a given output slot); it is not the forward map \(\sigma\). The audit keeps these directions distinct.

The 2D version applies the in-shuffle in both array directions and reveals toroidal wraparound in the finite index layout. This is a discrete permutation of pixels, not a continuous deformation of a torus.

The Boolean 3D source `fractal_3d_2.js` starts with a \(2\\times2\\times2\) seed. At each iteration it doubles each array dimension and writes
\[
\mathrm{next}[2x+dx][2y+dy][2z+dz]
= T_{m_{dz,dy,dx}}(\mathrm{current})[x,y,z],
\]
where (m_{dz,dy,dx}) is selected by `drawar[dz][dy][dx]`. **The eight rules are selected by output-index parity classes, not assigned to eight contiguous child octants.** Each rule is applied to the global parent index ((x,y,z)); modes 0–7 are coordinate sign-flips (with (N-1-\cdot) offsets), and modes 8–15 apply the same coordinate map plus Boolean complement. Each individual coordinate map is a bijection of the parent voxel set.

This distinction changes the FEEC question. The code is a parity-sublattice data transform: the eight children of one parent voxel can be mapped to eight different source voxels if the parity rules use different reflections. Therefore the eight outputs need not sample one and the same parent voxel. The new audit `audit_parity_lattice_refinement` checks this directly. For arbitrary source data, a single parent source sample is well-defined only when all eight parity rules induce the same coordinate map; for a single scalar field with the same Boolean value rule, the complement choice must also agree. This is a necessary structural condition, not yet a cubical chain-map proof.

The separate rotation-enhanced source `fractal_3d_with_rotaions.js` uses additional mode bits for axis rotations and has different scalar-value semantics: it does not Boolean-complement values; it optionally increments the sampled value when bit 3 is unset. It must be audited separately rather than assumed identical to the Boolean implementation.

### 3.1 Exact finite bridge: perfect shuffle equals a billiard floor pattern

The repository \`billiard-fractals/js/shuffle_and_billiard_isomorphism.js\` compares two independently generated \(256\times256\) binary arrays. With
\[
p=7,\qquad s=2^p=128,\qquad r=2p+1=15,
\]
each row \(y\) begins from \([0,1]\) and undergoes \(r\) recursive shifted shuffles
\[
\mathcal S_h(a)_{2i}=a_{(i+h)\bmod |a|},\qquad
\mathcal S_h(a)_{2i+1}=a_i,\qquad h=ys.
\]
The first 256 entries are compared against the reversed floor/parity row
\[
B_y(x)=\left\lfloor\frac{(255-x)y}{128}\right\rfloor\bmod2.
\]
A literal independent reproduction gives
\[
\boxed{\#\{(x,y):S_y(x)=B_y(x)\}=256^2=65\,536.}
\]
This is an exact finite computational identity for the stated parameters and indexing convention. It is not yet a theorem for arbitrary \(p\), size, or irrational slope. It is nevertheless the strongest direct bridge found between Herasymov's two principal constructions: a recursive permutation system and the symbolic billiard/floor coding. The audit script now reproduces this exact finite comparison.

---

## 4.1 Wider repository corpus and relevance

The public \`xcontcom\` profile lists 18 repositories. The following is a relevance map, not a claim that every repository contributes to the FEEC theorem.

| Repository | Verified computational theme | Relevance to this programme |
|---|---|---|
| \`billiard-fractals\` | Reflected grid paths, binary sequences, irrational floor codings, curved-surface slicing | **Direct**: symbolic boundary data and embedded-surface metric |
| \`perfect-shuffle\` | Recursive 1D/2D permutations and 3D voxel subdivision | **Direct**: finite permutations and candidate 3D refinement masks |
| \`fractogenesis\` | 2D/3D cellular automata and convolutional voxel growth | **Direct/experimental**: local 3D operators; test face compatibility |
| \`t-fractal\` | Recursive seed accumulation, with 2D and 3D demos | **Direct/experimental**: multiscale occupancy fields |
| \`fractals\` | User-guided recursive geometric fractal evolution; includes \`geom3d/\` | **Geometric comparison**: recursive 2D/3D geometry |
| \`binary-sequence-visualizer\` | Irrational floor/parity sequences combined into 2D patterns | **Direct**: symbolic field generation |
| \`evolving-cellular-automata\` | Genetic search over 512-bit Moore-neighborhood CA rules | **Algorithmic**: rule-space exploration |
| \`initial-state-evolution\` | Co-evolution of two CA fields on a toroidal grid | **Algorithmic**: two-field coupling; not Möbius gluing |
| \`neuroparticles2\` | Per-agent CA applied on shrinking windows \(13\times13\to3\times3\) | **Multiscale**: local coarse-graining operator |
| \`neuroparticles\` | Neural agents, local sensing, toroidal particle field | **Secondary**: emergent dynamics on periodic domains |
| \`particles\` | 2D force-based particles with toroidal boundary conditions | **Secondary**: periodic geometry and interacting fields |
| \`arduino-cellular-automata\` | Life on an \(8\times8\) LED grid | **Implementation only**: finite CA |
| \`cnn-gan\` | Proposal to replace convolution layers with CA and genetic search | **Exploratory**: local operators; README reports no interesting results yet |
| \`perfect-shuffle-music\` | Shuffle-based symbolic crossover of musical sequences | **Algebraic analogy**: deterministic recombination, not spatial geometry |
| \`xor-patterns\` | Scripts for XOR visual patterns and video generation | **Secondary**: binary pattern operators |
| \`perfect-shuffle-cryptography\` | Deterministic shuffle permutation for file encryption | **Secondary**: permutation algebra only |
| \`xcontcom.github.io\` | Project/article index and demos | **Provenance**: documentation |
| \`xcontcom\` | Profile/portfolio repository | **Provenance**: project index |

The strongest additions beyond the two core repositories are \`fractogenesis\` (explicit 3D CA/convolution), \`t-fractal\` (2D/3D recursive seed accumulation), \`binary-sequence-visualizer\` (floor/parity field construction), and \`neuroparticles2\` (repeated local-window reduction). These should be audited in that order after the current core bridge.


### 3.2 Correction from source-level indexing audit: parity classes, not octants

The first visual reading of the UI labels can suggest eight spatial octants. The actual loop nest disproves that interpretation: `dx,dy,dz` are the low bits of each output index, and `drawar[dz][dy][dx]` selects one of eight interleaved parity sublattices. The source coordinate passed to `switchdraw` is the parent-grid coordinate `(x,y,z)`, not a local coordinate within a contiguous octant.

Consequently, an octant-face matching table is not the right conformity test for this implementation. The correct first test is whether the eight parity-selected rules give all children of each parent voxel the same source index. This is only a data-sampling consistency test, not a geometric cell map. The audit evaluates all eight outputs over every parent voxel and records the source-index jumps across neighboring fine-grid voxels. Uniform mode 0 gives one consistent parent source sample per parent voxel and neighboring source-index jumps at most one. A mixed-reflection example fails the single-map condition. This is a direct obstruction to interpreting a generic mixed-rule output as a single-valued parent-cell sampling rule; it does not rule out its intended use as a symbolic/fractal data generator.

The new tests cover the parity indexing, uniform-rule case, and mixed-reflection obstruction. The next mathematical step is to define an actual cubical cell map (including vertices, edges, faces, and 3-cells) and verify its boundary/incidence commutation. A voxel-index sampling rule alone does not supply that map.

### 3.3 Rotation-enhanced generator: exact mode audit

The distinct source `fractal_3d_with_rotaions.js` (spelling as in the repository) uses an 8-bit mode. Its coordinate action is a composition of:

1. a rotation selected by `rotAxis=(mode>>4)&3` and `rotAngle=(mode>>6)&3`;
2. one of eight coordinate reflections selected by `mode&7`.

The source's quarter-turn formulas are ported literally:
[
R_x(x,y,z)=(x,N-1-z,y),quad
R_y(x,y,z)=(z,y,N-1-x),quad
R_z(x,y,z)=(N-1-y,x,z).
]
The selected rotation is repeated zero, one, two, or three times, then the lower-three-bit reflection is applied. Axis code zero means no rotation for every angle code. Exhaustion of all 256 byte modes gives:

- every mode is a bijection of the finite (N^3) voxel index set (checked for (N=3), with the exact affine signed-permutation structure recovered);
- there are 32 distinct coordinate maps, not 48;
- 128 mode values induce orientation-preserving maps and 128 orientation-reversing maps;
- the eight parity rules still select interleaved output sublattices, not contiguous octants.

The scalar action must be kept separate from the coordinate action. The source does **not** complement Boolean values. It executes `if (!(mode & 8)) a++`: exactly 128 byte modes increment the sampled scalar by one and 128 leave it unchanged. The duplicated switch cases 0–7 and 8–15 have the same coordinate lookup; bit 3 controls the increment. Since JavaScript's `++` coerces booleans to numbers, the initial Boolean seed becomes numeric under incrementing modes. With seven iterations and a seed in ({0,1}), values remain bounded by the trivial estimate ([0,8]); this is not a conservation law.

A second parity-sampling audit checks, for every parent voxel, whether all eight parity rules select the same source coordinate and the same scalar action. Uniform rules pass; the included mixed-rotation control fails. This establishes source-index bijectivity of each mode, not a geometric subdivision map, shared-cell trace compatibility, or a de Rham chain map.


### 3.4 Uniform modes induce exact cubical chain automorphisms

To distinguish an actual incidence statement from voxel-index bijectivity, the audit now constructs the oriented cubical complex of the fixed grid
[
K_N=[0,N]^3.
]
A canonical oriented (k)-cell is represented by a lower vertex (vinmathbb Z^3) and an increasing axis set (I=(i_1<cdots<i_k)). Its boundary is
[
partial[v;I]=sum_{r=1}^{k}(-1)^{r-1}
left([v+e_{i_r};Isetminus i_r]-[v;Isetminus i_r]ight).
]

Each of the 32 distinct signed-permutation matrices (A) recovered from the rotation-enhanced source acts on grid vertices by
[
F_A(v)_i=
egin{cases}
v_j,&A_{ij}=+1,\
N-v_j,&A_{ij}=-1,
end{cases}
]
where row (i) has its unique nonzero entry in column (j). The image of an oriented cell is the image cell multiplied by the induced orientation sign: the product of the axis signs and the permutation sign needed to reorder the image axes.

The audit compares the two integer chains cell by cell:
[
oxed{partial P_k(c)=P_{k-1}partial(c),qquad k=1,2,3.}
]
It enumerates all cells in degrees 0 through 3 for each distinct matrix. This is an exact finite combinatorial test, not a floating-point residual.

**Scope:** this proves that every uniform signed-permutation symmetry induces an automorphism of the *same* cubical complex. It does not construct a coarse-to-fine inclusion/prolongation (P_h^k:C^k(K_h)	o C^k(K_{h'})), and it says nothing by itself about the mixed parity-selected generator. A genuine refinement proof still needs a specified subdivision of every cell, with compatible face restrictions and the chain identity across two different mesh levels.

For cochains, the induced pullback is the dual map. Its commutation with the coboundary follows from the chain identity above; it should not be confused with an independently chosen interpolation operator.


## 4. Cellular automata and coupled fields

Herasymov's \`evolving-cellular-automata\` searches a \(2^{512}\) rule space for 2D Moore-neighborhood automata, with toroidal boundary conditions. The later \`initial-state-evolution\` project fixes Conway's Life rule and co-evolves two fields A and B, with A's upper/lower boundary coupled to B and vice versa. These are useful examples of:
- finite-state local evolution;
- toroidal indexing;
- evolutionary search over rules versus initial conditions;
- two-field coupling and measurable cross-field activity.

The toroidal seam in these projects is **not** the Möbius seam of the RGS construction. A torus gluing preserves the orientation of the periodic coordinate; a Möbius gluing reverses the transverse coordinate. The two can be compared only after writing their explicit index maps and checking their action on oriented cells.

## 5. Integration with RGS–PSU–PRISM and curvilinear FEEC

Keep four maps distinct:

1. **Herasymov symbolic billiard map:** reflected grid path \(\to\) binary cell labels / 1D symbolic sequence.
2. **Herasymov graph embedding:** \((x,y)\mapsto(x,y,z(x,y))\), with induced metric \(g=I+\nabla z\otimes\nabla z\).
3. **Herasymov recursive voxel map:** 2D/3D seed field \(\to\) recursively expanded symbolic voxel field via octant transformations.
4. **RGS \(W(G_2)\) geometric lift:** \(R_T\mapsto V_T\), with \(Q_{G_2}\), cofactor vector \(c_T\), normal amplitude \(\alpha(\rho)\), and the separately specified Möbius seam.

The strongest rigorous connection to the existing FEEC work is map 2: it supplies an explicit non-affine surface chart and a metric tensor for the existing covariant-pullback/Gram-matrix pipeline. The strongest computational connection is map 3: it supplies candidate symbolic refinement masks and local signed-permutation actions to test against cubical incidence matrices.

For a cellular map \(f:K_h\to K_{h'}\), the induced cochain pullbacks \(P_h^k\) must satisfy the commuting identity
\[
D_{h'}^kP_h^k=P_h^{k+1}D_h^k
\]
(with degree indexing fixed consistently). This is the correct test before importing a Herasymov voxel transformation into the de Rham complex. A visual self-similarity or bijection of voxel indices does not imply this chain-map property.

For the RGS–PSU–PRISM synthesis:
- Fibonacci rectangles give a controlled \(\varphi\)-approximating aspect-ratio sequence.
- The supergolden \(\psi\)-refinement remains a separate candidate scale law; Herasymov's sources do not establish a \(\psi\)-based recurrence.
- \(W(G_2)\) Gram classes and the \(R_T\mapsto V_T\) normal completion remain independent geometric structures. A bridge would require an explicit intertwining map from the symbolic billiard/shuffle state space to the \(W(G_2)\) triplettes, not an analogy.
- The Möbius seam must not be identified with the toroidal boundary used by his cellular automata.
- The threshold field can be used as a coefficient/label or as data for an independently defined variational functional; it must not be inserted as an arbitrary FEEC mass weight.

## 6. Proof-status ledger

| Statement | Status |
|---|---|
| In-shuffle is the permutation \(\sigma(i)=2i+1\bmod(2n+1)\) on \(2n\) positions | Exact algebraic identity |
| Its period is \(\operatorname{ord}_{2n+1}(2)\) | Exact algebraic identity |
| Graph metric \(g=I+\nabla z\otimes\nabla z\), \(\det g=1+|\nabla z|^2\) | Exact differential geometry where \(z\) is differentiable |
| Fibonacci aspect ratios converge to \(\varphi\) | Standard exact limit |
| Herasymov's finite binary patterns exhibit the article's reported visual structure | Reproducible computational claim; audit/fixtures needed |
| The parity-sublattice data transform defines a conforming 3D cubical mesh | Not established; it is not a geometric cell map, and cubical incidence compatibility remains open |
| Each uniform signed-permutation mode induces a chain automorphism of the fixed cubical grid | Exact finite combinatorial identity; all 32 distinct maps audited |
| A coarse-to-fine refinement operator induced by the mixed parity generator commutes with cubical incidence | Open; requires a cell subdivision and compatible face restrictions |
| The symbolic threshold field models physical holography, diffraction, or quantum interference | Not established; visual analogy only |
| Herasymov's constructions derive the RGS \(W(G_2)\) lift or Möbius seam | Not established by inspected sources |
| The combined construction satisfies FEEC Mosco convergence | Open; requires the full geometric, stability, compactness, and recovery-sequence programme |

## 7. Reproducibility audit

Run:
\`\`\`bash
python projects/de_rham_benchmark/audits/audit_herasymov_symbolic.py --self-test
\`\`\`

The script checks the finite in-shuffle permutation/order, Fibonacci ratio convergence, the exact source-code billiard sequence routine, the surface metric determinant identity, Boolean and rotation-generator parity sampling, all 256 rotation modes, and exact cubical chain identities for the 32 distinct uniform signed-permutation maps on a fixed grid. It does not certify a coarse-to-fine refinement map, FEEC stability, or Mosco convergence.
