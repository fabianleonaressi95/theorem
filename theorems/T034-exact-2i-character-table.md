# T034 — Exact reconstruction of the nine-character table of the binary icosahedral group

**Status:** exact reconstruction algorithm over \(\mathbb Q(\sqrt5)\), with all source data identified. The table is generated from the nine T021 Molien covariants and the fundamental \(SU(2)\) character. The accompanying exact-arithmetic test is provided but is not claimed to have run in this environment. This theorem reconstructs characters, not explicit unitary matrix models.

## 1. Fixed conjugacy-class convention

Use the nine conjugacy classes in the order already fixed by
\`bibliography/spin-geometry-quaternionic/RUMIN_2I_N1_CHARACTER_AUDIT.py\`:
\[
|C_j|=(1,1,20,30,12,12,20,12,12),
\qquad
\operatorname{ord}(C_j)=(1,2,3,4,5,5,6,10,10).
\]
The fundamental two-dimensional character is
\[
\chi_1=(2,-2,-1,0,\phi-1,-\phi,1,\phi,1-\phi),
\qquad \phi=\frac{1+\sqrt5}{2}.
\]
The symmetric-power characters are computed exactly from
\[
\chi_0(C_j)=1,\quad \chi_1(C_j)\text{ as above},\quad
\chi_m(C_j)=\chi_1(C_j)\chi_{m-1}(C_j)-\chi_{m-2}(C_j).
\]
All entries lie in \(\mathbb Q(\sqrt5)\).

## 2. Molien data as linear equations for the unknown characters

For each irreducible label \(\rho\), T021 gives
\[
M_\rho(t)=\sum_{m\ge0}b_{m,\rho}t^m
=\frac{N_\rho(t)}{(1-t^{12})(1-t^{20})}.
\]
The nine numerator supports and dimensions are transcribed in the existing exact module \`src/t032_2i_molien.py\`. The coefficient \(b_{m,\rho}\) is computed by counting
\[
m=e+12a+20b,\quad e\in\operatorname{supp}N_\rho,\quad a,b\ge0,
\]
with repeated numerator exponents counted with their stated multiplicity (notably the coefficient \(2t^{15}\) in the six-dimensional row).

The character-average identity gives, for every \(m\),
\[
120b_{m,\rho}
=\sum_{j=0}^{8}|C_j|\,\overline{\chi_\rho(C_j)}\,\chi_m(C_j).
\]
The irreducible characters of \(2I\) are real-valued in this class convention, so the conjugation may be omitted after that fact is checked by the resulting exact table.

Let \(A_{m,j}=|C_j|\chi_m(C_j)\). Select nine linearly independent rows of \(A\) over \(\mathbb Q(\sqrt5)\). For each \(\rho\), solve
\[
A_{\mathrm{sel}}\,x_\rho=120(b_{m,\rho})_{m\in\mathrm{sel}}.
\]
This determines all nine values \(\chi_\rho(C_j)\) exactly. The implementation selects independent rows algorithmically rather than assuming that the first nine degrees are independent.

## 3. Exact acceptance identities

The reconstructed table is accepted only if all of the following hold in exact algebraic arithmetic:

1. Every row has the prescribed dimension at the identity class.
2. Weighted row orthogonality:
   \[
   \sum_j|C_j|\overline{\chi_\rho(C_j)}\chi_\sigma(C_j)
   =120\delta_{\rho\sigma}.
   \]
3. The central element \(-1\) acts by a scalar \(\pm I\), hence
   \(\chi_\rho(C_{-1})=\pm d_\rho\).
4. The defining two-dimensional row agrees with the supplied fundamental character.
5. For every \(\rho\) and every \(0\le m\le240\), the reconstructed character average equals the exact Molien coefficient \(b_{m,\rho}\).
6. \(\sum_\rho d_\rho^2=120\).

These checks certify the character table and its class/label convention. They do not certify matrix multiplication relations for a chosen set of representation matrices.

## 4. What this closes and what remains open

**Closed by the exact reconstruction, once the accompanying tests pass:** the machine-readable nine-row character table, exact character orthogonality, the correspondence between the T021 Molien labels and the fixed nine conjugacy classes, and direct character-projector coefficients.

**Still open:** explicit unitary matrices \(\rho(g)\) for every element \(g\in2I\) and every irreducible \(\rho\); exact matrix units on the relevant Rumin harmonic spaces; and the reduced geometric Rumin differential matrices in those bases. Characters determine central isotypic projectors but do not determine matrix units or a concrete basis of each irreducible representation.

No new torsion value, spectral theorem, or Q6/PRISM continuum statement is claimed.

## 5. Reproducibility

From the repository root:
\`\`\`bash
python -m unittest tests.test_t034_exact_2i_character_table -v
python -m src.t034_exact_2i_character_table --output data/2i_character_table_exact.json
\`\`\`
The JSON export stores each algebraic entry as an exact SymPy expression string, together with the class order, class size, irrep dimension, selected interpolation degrees, and verification report. It is not a floating-point export.

## 6. Dependencies and provenance

- T021: nine Molien covariant numerators and the original exact character-average calculation.
- T031: geometric \(2I\)-equivariance and descent.
- T033: matrix-unit formula and the distinction between central projectors and full matrix units.
- \`src/t032_2i_molien.py\`: exact Molien numerator supports and dimensions.
- \`bibliography/spin-geometry-quaternionic/RUMIN_2I_N1_CHARACTER_AUDIT.py\`: fixed class sizes, class orders, and fundamental character.

## Classification

- **Exact input data:** class sizes/orders, fundamental character, nine Molien numerator supports and dimensions.
- **Exact algebraic reconstruction:** character table over \(\mathbb Q(\sqrt5)\), subject to the stated test execution.
- **Not claimed:** explicit representation matrices, exact matrix units on Rumin eigenspaces, or a new analytic result.
