# S010 — Kathara–quaternionic lift and intrinsic RGS triplet response

**Status:** exact planar/quaternionic identities plus archived numerical operator observations; induced RGS representation and physical torsion coupling remain open.  
**Companion source:** [fabianleonaressi95/rgs-qlg-quaternion-bridge](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge)

## 1. Scope and epistemic rule

Kathara/Krystal is the geometric source for the planar stage rule in this record. The source-derived construction is formalized in the companion repository at `docs/KATHARA_KRYSTAL_SPIRAL_SQUARE_GEOMETRY.md`. This document extracts its exact linear algebra and states the tests needed to connect it to the RGS 188D operator and the selected (T_{2u}) triplet.

The use of Kathara geometry as a mathematical input does **not** validate every cosmological, energetic, torsion-field, or antigravity interpretation associated with the wider literature. Exact geometric identities, numerical operator observations, physical hypotheses and historical attributions are kept separate.

## 2. Kathara/Krystal square similarity

The stated stage rule is a clockwise (45^\circ) rotation together with a scale factor (\sqrt2):
\[
T=\sqrt2R_{-\pi/4}
=\begin{pmatrix}1&1\\-1&1\end{pmatrix}.
\]
Direct multiplication gives
\[
T^TT=2I,\qquad\det T=2,
\]
and
\[
T^2=\begin{pmatrix}0&2\\-2&0\end{pmatrix}
=2R_{-\pi/2}.
\]
Consequently, two stages are a clockwise quarter-turn and a doubling of length. In complex coordinates (Tz=(1-i)z), hence (T^2z=-2iz). This is a similarity, not a pure rotation.

For the three centers in the source reconstruction, with (w>0):
\[
p_6=(-w/2,0),\quad p_9=(-w/2,w/2),\quad p_{12}=(0,w),
\]
and
\[
Tp_6=p_9,\qquad Tp_9=p_{12},\qquad T^2p_6=p_{12}.
\]
This three-point orbit is exact under the stated overlay constraints. It does not determine all 12 Kathara centers without the complete incidence/line diagram.

The arithmetic action is also exact:
\[
T(\mathbb Z^2)=\{(u,v)\in\mathbb Z^2:u\equiv v\pmod2\},
\quad T^2(\mathbb Z^2)=2\mathbb Z^2.
\]
The first image is an index-two checkerboard sublattice; the second has index four.

## 3. Quaternionic lift of the Cartesian quarter-turn

The scale-free planar rotation is (R_{-\pi/2}). Embedded as a 3D rotation about the negative (z)-axis, its unit-quaternion lift is
\[
q_{-90}=\cos(-\pi/4)+\mathbf k\sin(-\pi/4)
=\frac{1-\mathbf k}{\sqrt2}.
\]
Then
\[
q_{-90}^2=-\mathbf k,\quad q_{-90}^4=-1,\quad q_{-90}^8=1.
\]
The (SO(3)) rotation has order four, while this (SU(2)\) lift has order eight. This double-cover sign is essential.

For a (120^\circ) rotation about (\mathbf n=(1,1,1)/\sqrt3):
\[
q_{120}=\frac12+\frac{\sqrt3}{2}\mathbf n
=\frac{1+\mathbf i+\mathbf j+\mathbf k}{2},
\quad q_{120}^3=-1,\quad q_{120}^6=1.
\]
Its (SO(3)) image has order three and its spin lift order six.

The quaternion units and the commuting scalar complex unit must remain notationally distinct. The planar rotation is a real (2\times2) representation; the quaternion is its chosen lift after specifying the embedding axis.

## 4. RGS 188D triplet: archived numerical observations

The companion repository archives `reports/rgs_188d/188D_T2U_GEOMETRY_AUDIT.json`. For its selected orthonormal triplet basis (J_0\in\mathbb R^{188\times3}), the report gives:
\[
\|J_0^TJ_0-I_3\|\approx5.60\times10^{-16}.
\]

It distinguishes:
\[
M_{\rm geom}=J_0^TK_{\rm tangent}^{+}J_0
\]
with three eigenvalues approximately (-0.95403126139055) and relative anisotropy (3.96\times10^{-15}), from
\[
M_{\rm field}=J_0^TK_{\rm field}^{+}J_0
\]
with eigenvalues
\[
0.8272550028,\quad0.8272550028,\quad0.9512140709,
\]
and relative anisotropy (0.1427155).

The direct compression (J_0^TK_{\rm field}J_0\) is approximately (4.96933853I_3). This does not imply invariant-subspace behaviour: the archived relative invariance residual is (0.7219434), with leakage outside the triplet (0.3321124).

Interpretation: anisotropic response is already present in the full operator/inverse response and coupling to complementary modes; no independent phenomenological (Q\) should be inserted to manufacture it. The geometry-compressed tangent observable is numerically isotropic. These data do not imply that every RGS triplet is anisotropic, and the selected (T_{2u}) triplet must not be conflated with the separate 94 dynamical two-dimensional planes.

## 5. The missing representation calculation

Let (\rho(q)\) be the actual 188D representation induced by the quaternionic lift. It must be recovered from the archived representation/projector data, not guessed from the abstract quaternion. The decisive tests are
\[
[K_{\rm field},\rho(q)],\qquad
(I-J_0J_0^T)K_{\rm field}J_0,\qquad
J_0^TK_{\rm field}^{+}J_0.
\]
The first tests equivariance, the second quantifies leakage, and the third records the effective triplet response.

The required implementation sequence is:

1. identify the exact coordinate and orientation convention for the Kathara stage map;
2. identify the corresponding element in the relevant finite rotation group and its (SU(2)) lift;
3. recover the 188D representation matrix from the RGS data;
4. verify orthogonality/unitarity, group relations and the action on (J_0);
5. compute commutators, invariant-subspace residuals and mode leakage;
6. only then construct the induced coframe and vary the declared connection action.

No commutator value is claimed in this record until steps 1–5 are executed.

## 6. Torsion: three constructions kept distinct

Cartan torsion for a coframe and connection is
\[
T^a=de^a+\omega^a{}_b\wedge e^b.
\]
A rotating frame alone does not force nonzero torsion: a compensating Levi-Civita/inertial connection can make it vanish.

The companion RGS–QLG repository also contains a minimal Einstein–Cartan–Dirac algebraic relation, in its fixed conventions:
\[
T_{abc}=-\frac{\kappa}{2}\epsilon_{abcd}J_5^d.
\]
This is axial torsion sourced by the Dirac axial current and is algebraic, not propagating. It is not automatically the torsion induced by the Kathara coframe.

Likewise, the local Levi-Civita spin-connection kernel is torsion-free by construction; TEGR uses a separate teleparallel inertial connection. These three routes cannot be merged by notation alone.

The current evidence supports the following status:
- **Exact:** planar Kathara similarity and quaternionic lift identities.
- **Numerically reported:** triplet compression, anisotropic inverse response and leakage.
- **Candidate:** induced quaternionic action on the RGS triplet and coframe.
- **Open:** representation matrix, commutator audit, complete connection variation, and any electromagnetic-to-torsion constitutive law.

## 7. Historical and non-standard physical-source register

The following names occur in the wider source tradition and are recorded for provenance and critical comparison, not as established inputs to the RGS equations:

| Figure / programme | Topic attributed in the cited tradition | Scientific status for this project |
|---|---|---|
| Nikolai Kozyrev | time-asymmetric effects and “torsion” interpretations | Non-standard claims; no accepted field equation or independent validation establishing a physical torsion field |
| Dewey B. Larson | Reciprocal System, reciprocal space/time description | Alternative theoretical system; not a consequence of RGS or standard relativistic electrodynamics |
| Thomas Townsend Brown | Biefeld–Brown effect and electrogravitic interpretation | Electrohydrodynamic thrust/ion-wind effects must be separated from claims of antigravity |
| Gennady Shipov / Anatoly Akimov | “torsion fields” and information/rotation hypotheses | Not an established extension of Einstein–Cartan torsion |
| Harold Aspden | ether, magnetism and permanent-magnet motor hypotheses | Historical/alternative proposals; each claim requires independent reproducible testing |
| John Searl / Bruce DePalma | rotating generator and anomalous-energy claims | Device claims are not accepted evidence of anomalous energy or gravitational coupling |
| Michael Persinger | electromagnetic stimulation and geophysical/neurophysiological hypotheses | Must be evaluated within the specific experimental literature; not evidence for a universal torsion field |
| Nikola Tesla | high-voltage, resonant and wireless power transmission | Historical engineering work is distinct from later “scalar wave” or vacuum-energy interpretations |

The source list supplied for this audit includes David Wilcock's *The Divine Cosmos* page, the *Source Field Investigations* book/listing, and the Italian PDF *Il mistero rivelato*. These are secondary-source provenance, not primary experimental evidence. Kathara/Krystal geometry is the mathematical starting point here; the wider Wilcock-associated claims are not imported as physical axioms.

## 8. Falsification and next audit

A valid RGS/Kathara bridge must fail cleanly if:
- no representation matrix (\rho(q)\) compatible with the stored group action exists;
- the proposed map fails the required group relations;
- the commutator or leakage is incompatible with the claimed invariant sector;
- the coframe/connection equations do not follow from a single declared action;
- the result depends on an arbitrary external anisotropy tensor or unconstrained fitting parameter.

The next implementation deliverable is a reproducible extractor/audit for (\rho(q)\) and the three operator tests in §5. It must record input hashes, source commit, tolerances, software versions and output JSON. Until then the RGS/Kathara quaternionic coupling is a candidate, not a proved physical torsion law.

## References

1. A&A Deane / Emerald Awakening, “Spirals of Creation” (Kathara stage geometry): https://emerald24.org/spirals-of-creation/
2. RGS–QLG quaternion bridge, Kathara/Krystal reconstruction: https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/KATHARA_KRYSTAL_SPIRAL_SQUARE_GEOMETRY.md
3. RGS–QLG quaternion bridge, 188D T2u geometry audit: https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/reports/rgs_188d/188D_T2U_GEOMETRY_AUDIT.json
4. David Wilcock, “The Divine Cosmos” (secondary source): https://www.stazioneceleste.it/articoli/wilcock/wilcock_TDC_01.htm
5. Dewey B. Larson, *The Source Field Investigations* listing/secondary discussion: https://www.amazon.com/Source-Field-Investigations-Civilizations-Prophecies/dp/B09XBYG7K8 and https://www.academia.edu/83269403/The_Source_Field_Investigations
6. “David Wilcock — Il mistero rivelato” (secondary source PDF): https://www.associazioneducati-stark.it/assets/images/articles/david-wilcock-il-mistero-rivelato.pdf
