# C60 Stone–Wales — induced map on H₂ investigation (2026-11-27)

Autonomous mathematical investigation triggered by
`tests/test_c60_stone_wales.py::test_chain_map_preserves_spherical_fundamental_class`
(branch `fix/c60-sw-homology-evidence`), which reports multiplier ≈ 3.3e-16 —
i.e. `S2 z_fund ≈ 0`. This document distinguishes the three candidate
explanations **without modifying expected test values**.

Reproduce:

```bash
python3 scripts/audit_c60_sw_h2_induced_map.py   # ~4 min, exact integer algebra
# -> audits/c60_sw_h2_induced_map_2026-11-27.json
```

## 1. Setup (exact integer arithmetic)

- Both cellulations are spheres: `dim ker B2 = dim ker B2' = 1`, primitive
  integer generators `z`, `z'` with **all entries = +1** (32 faces each).
- Chain-map identities verified exactly:
  `B1' S1 = B1` ✓ and `B2' S2 = S1 B2` ✓ (integer equality, not tolerance).

## 2. Decisive computation

For the library `S2` (min-norm `lstsq` filling + `x ← rint(x − x[0])` gauge):

- `c = S2 z` is an exact 2-cycle (`B2' c = 0` over ℤ);
- its homology class is `k = (c·z')/(z'·z') = 0/32` → **k = 0**.

So with that gauge choice the induced map `(S2)*: H₂ → H₂` is the zero map.

## 3. Gauge sweep — the decisive test

Each column `x_j` of `S2` is determined only modulo `ker B2' = ℤ·[z']`
(the preimage of a 1-cycle in a sphere is unique up to the fundamental
class). The construction's per-column freedom is therefore exactly
`t_j ∈ ℤ` added to column `j`. Rebuilding `S2` with 200 random gauge
vectors `t ∈ [−3,3]³²`:

- chain-map identity `B2' S2 = S1 B2` still holds **exactly** every trial;
- `S2 z` remains a cycle every trial;
- the induced integer `k` ranges over **≈60 distinct values in [−31, 29]**
  (`gauge_invariant: false`).

Since `z_j = +1` for all `j`, shifting column `j` by `t_j z'` shifts `k` by
`Σ_j t_j` — every integer is reachable. The sweep is consistent with this
closed form.

## 4. Verdict: **H₂ — gauge error** (not H₁, not H₃)

- **H₁ ruled out:** `make_chain_map` *is* a genuine chain map — both
  boundary-intertwining identities hold with exact integers.
- **H₃ ruled out:** the induced map is not a canonical null map; it takes
  every integer value depending on representative choices.
- **H₂ confirmed:** the per-column `lstsq`+pinning gauge chooses
  representatives incoherently. The earlier `multiplier ≈ 0` was **one
  arbitrary gauge outcome**, not a topological obstruction and not a
  refutation of the Stone–Wales geometry.

## 5. Mathematical content of the finding

A chain map `C• → D•` between these sphere cellulations exists and is
correctly built, but **it does not determine a map on H₂**: the ambiguity
per 2-cell column is precisely `H₂(D) ≅ ℤ`, so `(S2)*` is defined only
modulo an arbitrary integer shift. Equivalently, the construction sees the
1-skeleton (S1) faithfully but has no coherent 2-dimensional filling —
consistent with the fact that a *geometric* homotopy between the two
cellulations exists (Stone–Wales is a local bistellar-type move) while the
*algebraic* per-face filling does not encode it.

## 6. What would make `(S2)*` canonical (open, author decision)

1. **Coherent coning:** fix a base vertex/face ordering and define each
   column's filling by an explicit shelling rule, proving
   `S2 z = ±z'` by construction.
2. **Chain homotopy:** exhibit `h: C₂ → D₃`-type data (or a simplicial
   approximation of the geometric flip) so that S2 is determined up to
   homotopy — homotopic chain maps induce identical H₂ maps.
3. **Weaken the claim:** state only that *some* chain map exists (already
   proved by the boundary identities) and report `(S2)* ∈ ℤ` as
   gauge-dependent — i.e. drop the "fundamental class preservation"
   assertion from the test until a canonical S2 exists.

Until one of these is implemented, the honest status is:
**chain map exists ✓; induced H₂ map undetermined (gauge-dependent) —
the ≈0 multiplier is a gauge artifact, preserved here as reproducible
evidence.**
