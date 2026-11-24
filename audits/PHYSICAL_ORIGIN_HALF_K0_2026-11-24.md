# Physical origin of the half-unit in the RGS–PSU spectral ladder

Date: 2026-11-24  
Status: **research audit / open question** (not a theorem)

## 1. Question and fixed numerical input

The question is not whether a formula containing (1/2) can be found. It is whether the offset in the stored operator has an independently identifiable physical origin.

The current numerical record for the 188-dimensional operator is:

\[
K_0=\frac{N+5I}{10},\qquad
\operatorname{spec}(N)=\{0,1,\ldots,123\},
\]
so that the 124 positive eigenvalues of (K_0) are
\[
\lambda_k(K_0)=\frac{k+5}{10},\qquad k=0,\ldots,123.
\]
In particular, \(\lambda_{\min}=1/2\), the spacing is \(1/10\), and the 124-dimensional ladder can be *labelled* by \(m=-123/2,\ldots,123/2\).

This establishes an affine spectral identity on the stored arrays. It does **not** by itself establish a Hamiltonian, canonical variables, an SU(2) action, or physical spin \(j=123/2\). Any 124-dimensional Hilbert space admits an abstract spin-\(61.5\) representation after one chooses ladder matrices; that construction is not evidence that the physical system carries that representation.

The common-basis certificate and the cubic-symmetry audit are treated as settled input: the transported \(O_h\) action leaves \(K_0\) invariant only for identity and inversion. The present note does not revive a cubic-triplet/SU(2) coupling.

## 2. Four genuinely different mechanisms

### 2.1 Canonical zero-point term

For a canonical pair \([q,p]=i\hbar\), define
\[
a=\frac{1}{\sqrt{2\hbar}}\left(\sqrt{M\omega}\,q+
\frac{i}{\sqrt{M\omega}}p\right),\qquad [a,a^\dagger]=1.
\]
Then
\[
H=\frac{p^2}{2M}+\frac12M\omega^2q^2
=\hbar\omega\left(a^\dagger a+\frac12\right).
\]
The half is forced by the canonical commutator and the symmetric quadratic Hamiltonian. It is not a spin effect.

**RGS test required:** identify, from the model's original variables and energy functional, a canonical pair (or a symplectic form and compatible complex structure), derive the commutator/Poisson bracket, and derive the quadratic Hamiltonian with its normalization independently of the observed spectrum. Merely defining \(a\) from the already diagonalized \(K_0\) would be circular.

### 2.2 Maslov / Bohr–Sommerfeld correction

For a one-dimensional regular orbit with two simple turning points, the semiclassical quantization rule is
\[
\oint p\,dq=2\pi\hbar\left(n+\frac{\mu}{4}\right),
\qquad \mu=2,
\]
hence \(n+1/2\). Equivalently, each simple turning point contributes a phase correction \(\pi/4\). More generally the shift is controlled by the Maslov class/index, not universally by one half.

**RGS test required:** identify a symplectic phase space, a closed classical orbit or Lagrangian cycle, and its caustics/turning points; compute the Maslov index from that geometry. The finite matrix spectrum alone contains no orbit, action integral, or caustic data. Until those structures are independently specified, the Maslov explanation is a candidate mechanism, not an explanation of this \(K_0\).

### 2.3 Spinorial holonomy

The covering homomorphism \(SU(2)\to SO(3)\) has kernel \(\{I,-I\}\). In a half-integral spin representation,
\[
U(2\pi)=(-1)^{2j}I=-I.
\]
This explains the sign under a full spatial turn for genuine half-integral spin. It does not explain a uniform affine shift of an arbitrary finite spectrum.

**RGS test required:** exhibit a continuous rotation action on the physical state space, its generators, and the group law; then demonstrate the nontrivial lift/holonomy. The established \(\mathbb Z_2\) symmetry of \(K_0\) is spatial inversion, not a continuous rotation group and not the central element of a demonstrated SU(2) representation. Do not identify these two \(\mathbb Z_2\)'s.

### 2.4 APS / eta boundary correction

For a Dirac-type operator on a compact manifold with boundary, the APS index formula contains
\[
\operatorname{ind}_{APS}(D)=\int_M \mathcal A(D)
-\frac{\eta(D_{\partial M})+h}{2},
\]
with \(h=\dim\ker D_{\partial M}\). Here the half multiplies a boundary spectral-asymmetry correction. It is not automatically a lowest eigenvalue or a zero-point energy.

**RGS test required:** identify a Dirac-type operator, a manifold with boundary (or a justified boundary model), its induced tangential operator, and compute the eta invariant and kernel term with fixed conventions. No such APS boundary problem is presently identified for \(K_0\).

## 3. Internal RGS discriminant: the \(Z_S\) half-sector

The stored spectral report records:
- \(Z_S\) eigenvalues \(-1/2\) (multiplicity 3), \(0\) (182), \(+1/2\) (3);
- \(Z_S^2\) has eigenvalue \(1/4\) on a rank-6 subspace and zero elsewhere;
- \(Z_A\) is antisymmetric and \(Z_A Z_S+Z_S Z_A\) has residual about \(3.3\times10^{-16}\);
- the smallest positive eigenvalue of \(K_0\) is also \(1/2\).

The existing report explicitly classifies the equality as a **spectral coincidence**, not a derivation. The next discriminating calculation is to compare the support of \(Z_S\) (and the singular support of \(Z_A\)) with the lowest eigenspace of \(K_0\), and to evaluate:
\[
[P_S,K_0],\quad (K_0-\tfrac12 I)P_S,\quad
P_S=4Z_S^2,
\]
together with the corresponding singular-value support projector for \(Z_A\). If \(P_S\) is a rank-six projector, it cannot equal the one-dimensional lowest eigenspace projector of a simple ladder; it may nevertheless be an invariant subspace or encode a separate Clifford-like sector. The calculation must report ranks, principal angles, commutators and restricted spectra, not just compare the number \(1/2\).

This is the most immediate internal test because all required matrices are already stored. It does not require guessing a physical interpretation.

## 4. What the current data do and do not say

| Statement | Status | Reason |
|---|---|---|
| \(K_0=(N+5I)/10\) on the archived arrays | Numerical identity / reported certification | Existing integer-operator audit |
| Lowest positive eigenvalue of \(K_0\) is \(1/2\) | Numerically established | Spectral ladder report |
| \(Z_S\) has a rank-six \(1/4\)-eigenspace for \(Z_S^2\) | Numerically established | Spectral report |
| The two appearances of \(1/2\) have the same eigenspace or mechanism | Open | Requires support comparison |
| \(K_0\) is a quantized Hamiltonian with zero-point energy | Not established | No independently derived canonical pair/Hamiltonian |
| The shift is a Maslov correction | Not established | No phase space, orbit or Maslov class identified |
| \(j=61.5\) is physical spin | Not established | Abstract ladder algebra is not a physical rotation action |
| The shift is an APS boundary term | Not established | No boundary Dirac problem identified |

## 5. Falsifiable work order

1. Run `scripts/audit_half_sector_vs_k0.py` on the archived `K0.npy`, `Z_S.npy`, and `Z_A.npy`; preserve the JSON output and input hashes.
2. If the six-dimensional \(Z_S\) support is invariant under \(K_0\), inspect the restricted spectrum and determine whether the value \(1/2\) is an eigenvalue on that entire sector or only one eigenvalue among several.
3. Trace the coefficients 10 and 5 in \(N=10K_0-5I\) back to the original definition of the quadratic form/operator. If 5 was selected only to make the spectrum integral, the shift is a normalization/affine recentering, not a physical prediction.
4. Only after that algebraic provenance check, test the canonical/Maslov route against the original configuration-space and tangent-space data.
5. Keep spinorial and APS routes conditional on identifying the missing continuous action or boundary Dirac operator.

## 6. Bibliography / reliable starting points

- M. S. Child, *Semiclassical Mechanics with Molecular Applications*, Oxford University Press (1991), Chapter 3, “Quantization”, DOI: [10.1093/oso/9780198556541.003.0003](https://doi.org/10.1093/oso/9780198556541.003.0003). Discusses the Maslov phase at turning points and the Bohr–Sommerfeld shift.
- *Quantum Mechanics*, Chapter 56, “Solving the Harmonic Oscillator Algebraically”, [online text](https://mochizuki-tus.github.io/QM_Textbook_EN/ch56_creation_annihilation.html). Explicitly derives \(H=\hbar\omega(a^\dagger a+1/2)\) from \([a,a^\dagger]=1\).
- MIT 8.321, *Quantum Theory I*, Lecture 21, [lecture notes](https://ocw.mit.edu/courses/8-321-quantum-theory-i-fall-2017/d38bbdf1fa238bbb91cbb93fe7078760_MIT8_321F17_lec21.pdf). Distinguishes SU(2) half-integral representations from SO(3) representations.
- *An Equivariant Atiyah–Patodi–Singer Index Theorem for Proper Actions I: The Index Formula*, International Mathematics Research Notices (2023), [article](https://academic.oup.com/imrn/article/2023/4/3138/6454154). States the \((\eta+h)/2\) boundary correction and its spectral-asymmetry meaning.

## 7. Verdict

**No physical origin of the \(1/2\) in \(K_0\) has yet been derived.** The four mechanisms above are established mechanisms in their own settings, but none can be transferred to \(K_0\) without the structures listed in the corresponding tests. The immediate next step is the matrix-level \(Z_S/Z_A\)-support audit and the provenance of the affine coefficients 10 and 5. This keeps the investigation falsifiable and avoids relabelling a numerical half-integer as physical spin.
