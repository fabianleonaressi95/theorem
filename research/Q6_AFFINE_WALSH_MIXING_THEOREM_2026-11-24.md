# Exact commutator law for affine Q6 actions on the Walsh filtration

**Date:** 2026-11-24  
**Status:** proved finite-dimensional theorem; exhaustive finite enumeration of the natural Q6 automorphism group. No physical Anti-Twin mixing mechanism is established.

## 1. Setup

Let H = l2(F_2^6). For j=0,...,6, let V_j=span_F2(e_1,...,e_j), and let E_j be the orthogonal projection onto Walsh characters chi_s(x)=(-1)^(s.x) with s in V_j. Thus rank(E_j)=2^j.

For T(x)=Px+b, P in GL(6,2), let U_T f=f composed with T^{-1}. On Walsh characters U_T sends index s to P^{-T}s, up to a unit-modulus phase determined by b. Define r_j(P)=dim_F2(V_j intersect P^{-T}V_j).

## 2. Theorem

For every P in GL(6,2), b in F_2^6 and j,
  
  ||[U_T,E_j]||_F^2 = 2^(j+1)-2^(r_j(P)+1)

and

  ||[U_T,E_j]||_2 = 0 if r_j(P)=j, and 1 otherwise.

Both norms are independent of b.

### Proof

In the Walsh basis E_j is the coordinate projection onto V_j, containing 2^j characters. The affine unitary maps this coordinate set to P^{-T}V_j; b changes phases but not supports. Their intersection contains exactly 2^(r_j(P)) Walsh coordinates.

For two coordinate projections E,Q of equal rank m and intersection rank d, direct evaluation in the common coordinate basis gives ||[U,E]||_F^2=2(m-d), where Q=UEU*. Here m=2^j and d=2^(r_j(P)), yielding the Frobenius identity. The commutator is a direct sum of zero blocks and nonzero 2-by-2 exchange blocks with singular value 1. Hence its operator norm is 1 exactly when the projections differ. QED.

## 3. Natural Q6 automorphisms

The unweighted six-cube graph has Aut(Q6) isomorphic to (F_2)^6 semidirect S_6, of order 2^6*6!=46,080. An automorphism is determined by the image of one vertex and the induced permutation of its six neighbours. The translation part is any bit flip b and preserves every prefix conditional expectation.

A coordinate permutation preserves E_j exactly when it preserves the first-j coordinate set. For a fixed j, its stabilizer has size j!*(6-j)!. It preserves all seven levels iff it is the identity. Thus exactly 64 of the 46,080 cube automorphisms preserve the entire ordered filtration.

The filtration is ordered and is not invariant under the full cube symmetry group. A coordinate swap is a genuine graph automorphism and can mix the ordered Walsh levels, although it is not one of the stored Anti-Twin maps.

## 4. Exhaustive classification

The audit enumerates all 720 elements of S_6 and groups them by r_0,...,r_6. It finds 51 distinct profiles. Exact multiplicities and Frobenius-square / spectral profiles are stored in results/quantum_fractal_q6/affine_walsh_mixing.json.

For the swap of 0-based coordinates 2 and 4 (1-based 3 and 5),
  
  r=(0,1,2,2,3,5,6),
  ||[U,E_j]||_F^2=(0,0,0,8,16,0,0),
  ||[U,E_j]||_2=(0,0,0,1,1,0,0).

Thus j=3 gives 2*sqrt(2), and j=4 gives 4, exactly matching the synthetic control in PR #435. All earlier levels j=0,1,2 and later levels j=5,6 commute.

## 5. Anti-Twin and physical boundary

The stored Pi_AT is translation b=(0,0,0,1,1,1); Q6_antipodal is b=(1,1,1,1,1,1). Both lie in the translation subgroup and commute with every E_j. Stored Anti-Twin therefore does not break this filtration.

A coordinate swap belongs to the natural graph automorphism group of Q6, but current stored data do not select a particular swap as the physical Anti-Twin or PRISM coupling. Therefore:
- proved: affine commutator formula and translation independence;
- exhaustively enumerated: 51 profiles across 720 coordinate permutations;
- exact graph symmetry: coordinate swaps are genuine Q6 automorphisms;
- open: a physically selected RGS/PRISM operator with nonzero profile, and any dynamical memory-decay or multifractal law.

General GL(6,2) maps are algebraic tests, not automatically Q6 graph automorphisms. Preserving Hamming adjacency forces the linear part to permute the six unit vectors, hence to be a coordinate permutation.

## 6. Reproduction

Run:
  python experiments/quantum_fractal_q6/affine_walsh_mixing.py
  python -m pytest tests/test_q6_affine_walsh_mixing.py -q

The script uses exact combinatorial intersection dimensions and writes the JSON profile census. Regression tests compare the theorem with direct position-basis commutator calculations for the swap and affine translations.
