# Morandotti two-core C0-IPDG audit: current implementation and evidence

**Updated:** 11 November 2026  
**Repository:** fabianleonaressi95/theorem  
**Scope:** finite-dimensional Frank/Burgers reconstruction, interior-facet traction jumps, and mesh-refinement execution.

## Merged implementation

### PR #161 — Frank–Burgers traction-jump decomposition

[PR #161](https://github.com/fabianleonaressi95/theorem/pull/161) was merged as d43b6906ef88840f0688b8939045fbc8900110e7.

The implementation computes the interior-facet traction jump from the reconstructed stress as
\[
j=\llbracket\sigma n\rrbracket=j_F+j_B.
\]
It records the Frank and Burgers L2 norms and independently assembles the signed mixed term
\[
2\int_{\mathcal F_h^{\rm int}}j_F\cdot j_B\,dS,
\]
together with the squared-norm additivity residual. It also records total, Frank, Burgers, and mixed second-moment tensors in laboratory coordinates and in the longitudinal/transverse core frame, plus the total directional anisotropy.

The [DOLFINx two-core audit run](https://github.com/fabianleonaressi95/theorem/actions/runs/43051485760) completed successfully. Its algebraic tests, numerical audit, and artifact upload all passed.

### PR #162 — five-level traction-jump refinement

[PR #162](https://github.com/fabianleonaressi95/theorem/pull/162) was merged as e88da3e16257a9ab3a867e3b72e97fbd70a2d943.

It adds a dedicated DOLFINx 0.11.0 refinement workflow and executes the two-core audit at
\[
h\in\{0.08,\ 0.06,\ 0.045,\ 0.035,\ 0.027\},
\]
with the existing material and penalty settings. The workflow reruns the 13 algebraic reconstruction tests and uploads the JSON report and per-level FE fields.

Both the [base two-core audit run](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448351) and the [dedicated five-level refinement run](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448456) completed successfully.

## Five-level mixed-source result

The downloaded artifact from the five-level workflow contains the JSON report and per-level FE fields. For the mixed disclination–dislocation case, the reported traction-jump quantities are:

| h | cells | total L2 | Frank L2 | Burgers L2 | signed mixed term | mixed share of total squared jump | eigenvalue anisotropy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.080 | 1,265 | 9.9205e-3 | 7.4448e-3 | 3.9903e-3 | 2.70695e-5 | 27.51% | 0.09767 |
| 0.060 | 2,145 | 4.8440e-3 | 3.1950e-3 | 2.8349e-3 | 5.21961e-6 | 22.24% | 0.17414 |
| 0.045 | 3,642 | 3.6864e-3 | 2.4571e-3 | 2.2855e-3 | 2.32907e-6 | 17.14% | 0.19076 |
| 0.035 | 5,996 | 2.9916e-3 | 1.9843e-3 | 1.8368e-3 | 1.63867e-6 | 18.31% | 0.19337 |
| 0.027 | 9,881 | 2.3754e-3 | 1.5371e-3 | 1.4912e-3 | 1.05594e-6 | 18.71% | 0.21689 |

The mixed cross-term additivity residual is approximately 10^-17 to 10^-18 in absolute value over the five levels. In this particular mixed-source configuration the signed cross term is positive at every level and accounts for approximately 17–28% of the total squared traction jump. This is a result for this source configuration, not a universal sign theorem.

The total jump norm decreases along the tested refinement sequence, but the five levels do not establish a continuum convergence rate. The reported traction-jump eigenvalue anisotropy changes from 0.0977 to 0.2169. The distinct stress-second-moment eigenvalue anisotropy is comparatively stable, approximately 0.184–0.186 for the mixed-source case; these two anisotropy diagnostics must not be conflated.

## Tensor law

The exact discrete statement is recorded as [T091 — Frank–Burgers tensorial interaction and anisotropy composition law](../../theorems/T091-frank-burgers-tensorial-anisotropy-composition-law.md). With j = j_F + j_B, define
\[
T_F=\int j_F\otimes j_F\,dS,\quad
T_B=\int j_B\otimes j_B\,dS,\quad
T_{FB}=\int(j_F\otimes j_B+j_B\otimes j_F)\,dS.
\]
Then
\[
T=\int j\otimes j\,dS=T_F+T_B+T_{FB},
\]
and
\[
\int|j|^2\,dS=\int|j_F|^2\,dS+\int|j_B|^2\,dS
+2\int j_F\cdot j_B\,dS.
\]
The mixed tensor must be retained with its sign and directional structure. The theorem also gives the exact normalized axis-resolved anisotropy formula. The eigenvalue anisotropy of the total tensor is nonlinear and cannot be obtained by adding separate Frank and Burgers anisotropy scores.

## Orientation and separation controls

The orientation audit rotates the mesh in place at 0°, 30° and 60°. With defects co-rotated, the local interaction matrix differs by at most approximately 4.2e-13 and the directional boundary-residual differences by at most approximately 2.7e-11. This supports covariance of the implemented frame transformation for the fixed mesh. With Burgers data fixed in the laboratory frame, core traction components change with relative orientation.

The separate one-mesh separation sweep gives normalized off-diagonal operator coupling C(d) of approximately 0.2583, 0.1138, 0.0624 and 0.0349 at d = 0.48, 0.56, 0.64 and 0.72. The signed operator anisotropy is non-monotone. Since the distance sweep uses one mesh size, it is screening evidence only, not a continuum distance-decay law.

## Evidence boundary and open work

- **Proved:** the finite-dimensional tensor identity and its scalar/directional contractions under linear reconstruction and a common facet-jump convention.
- **Numerically verified:** five-level additivity residuals and a positive mixed contribution for the specified mixed-source case; fixed-mesh orientation covariance; one-resolution separation screening.
- **Open:** convergence of each sector and the mixed tensor as h tends to zero; stability under core-radius and separation refinement; a continuum counterpart with trace/jump regularity; material constitutive interpretation; universal distance law; physical force-balance conclusion.

The successful workflow establishes that the configured computation ran and its outputs were uploaded. It does not, by itself, prove a continuum theorem, a decay law, force equilibrium, or material validation.

## Reproduction

```bash
python3 scripts/rgs_morandotti_two_core_c0_ipdg.py \
  --mesh-sizes 0.08 0.06 0.045 0.035 0.027 \
  --alpha 10 \
  --young-modulus 1.0 \
  --poisson-ratio 0.0 \
  --out artifacts/morandotti_traction_refinement/report.json
```

See [MORANDOTTI_ANISOTROPY.md](../../MORANDOTTI_ANISOTROPY.md) for operational definitions and the orientation/separation protocols.

**FLN**
