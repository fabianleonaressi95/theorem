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

The Boolean 3D source \`fractal_3d_2.js\` starts with a \(2\times2\times2\) seed. At each step it doubles each dimension and fills each of the eight child octants using a selected mode. Modes 0–7 are the eight coordinate sign-flips
\[
(x,y,z)\mapsto(\epsilon_x x,\epsilon_y y,\epsilon_z z)
\]
in index coordinates (with the appropriate \(N-1-\cdot\) offset); modes 8–15 apply the corresponding reflection and Boolean complement. Each reflected index map is bijective on the parent voxel set. This is a recursive symbolic voxel generator.

It is not yet a conforming geometric subdivision: independently selected octant modes need not match on shared faces. Nor is the Boolean complement a geometric map. Before treating this as a mesh refinement operator, one must audit shared-face traces, orientation, and incidence preservation. The separate rotation-enhanced source \`fractal_3d_with_rotaions.js\` uses additional mode bits for axis rotations and has different scalar-value semantics; it must be audited separately rather than assumed identical to the Boolean implementation.

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
| Recursive 3D octant copies form a conforming 3D mesh | Open; not implied by voxel bijections |
| The recursive transformations induce a chain map on cubical cochains | Open; requires incidence/face-trace audit |
| The symbolic threshold field models physical holography, diffraction, or quantum interference | Not established; visual analogy only |
| Herasymov's constructions derive the RGS \(W(G_2)\) lift or Möbius seam | Not established by inspected sources |
| The combined construction satisfies FEEC Mosco convergence | Open; requires the full geometric, stability, compactness, and recovery-sequence programme |

## 7. Reproducibility audit

Run:
\`\`\`bash
python projects/de_rham_benchmark/audits/audit_herasymov_symbolic.py --self-test
\`\`\`

The script checks the finite in-shuffle permutation/order, Fibonacci ratio convergence, the exact source-code billiard sequence routine, the surface metric determinant identity, and the eight 3D coordinate-reflection bijections. It does not certify inter-octant face conformity or FEEC convergence.
