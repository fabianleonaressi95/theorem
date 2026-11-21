# C60 — ottimizzazione numerica del campo bulk `G̃` per `ψ(a,ν)=|a|`

Data: 2026-11-21
Classificazione: **calcolo numerico verificato nel modello intrinseco
faccia-per-faccia** (non è un nuovo teorema: usa il cell problem nucleare
`theorems/C60_CF_NUCLEAR_NORM_CELL_PROBLEM_2026-11-21.md` e la
semicontinuità bulk già dimostrate)
Script: `colloquio_morandotti/optimize_c60_gtilde_cf_energy.py`
Audit: `colloquio_morandotti/audits/c60_gtilde_cf_optimization_2026-11-21.json`

## 1. Funzionale da minimizzare

Per una coppia `(g,G̃)` con `G̃` costante su ogni faccia e
`M_f = A_f − G̃_f` (`A_f = ∇_Σg|_f`), il rilassamento CF con
`ψ(a,ν)=|a|` dà

```
I(g,G̃) = Σ_f |f| · [ W(G̃_f) + ‖M_f‖_* ] + ∫_{J_g} |[g]| dH¹,
```

 dove `‖·‖_*` è la norma nucleare (σ₁+σ₂). Il termine di salto
macroscopico `38.93478886` (quadratura sui 90 spigoli) non dipende da
`G̃`. Poiché l'area `|f|` si semplifica, il problema si separa per faccia:

```
min_{X∈R^{3×2}}  W(X) + ‖A_f − X‖_*.
```

Fatto chiave verificato: `A_f = B_fD_f` ha `A_fᵀA_f = I₂`, quindi tutti i
suoi valori singolari valgono 1 (`σ₁=σ₂=1`).

## 2. Soluzioni esatte e verifica numerica

### `W(F)=|F|²_F` — soft-thresholding

Con `Y = A−X`, il problema diventa `min_Y |Y−A|²_F + ‖Y‖_*`, il cui prox è
il soft-thresholding nucleare con soglia `λ/2 = 1/2`:

```
M* = U diag((σ_i − 1/2)_+) Vᵀ = A/2,     G̃* = A − M* = A/2.
```

Verifica indipendente (Nelder–Mead + Powell su `R⁶`, problema convesso):
funzionale analitico `1.5` = numerico `1.5`, `|X_num − X*|_F ≈ 1e-8`.

### `W(F)=|F|_F` — nessun guadagno

Il numerico converge a `X*=A` (f=`√2` per area): con bulk a crescita
lineare il disarrangiamento non conviene. Coerente col fatto che per
`W=|F|` la successione `u_n=g` era già minimale.

## 3. Valori globali sul C60 (`|f|` somme = 32,27)

| `G̃` | bulk `∫|G̃|²` | micro `∫‖M‖_*` | salto | **totale** |
|---|---:|---:|---:|---:|
| `A` (M=0) | 64,5398 | 0 | 38,9348 | **103,4746** |
| `0` | 0 | 64,5398 | 38,9348 | 103,4746 |
| **`A/2` (ottimo W2)** | **16,1349** | **32,2699** | 38,9348 | **87,3396** |

Per `W=|F|`: `G̃=A` resta ottimale → 84,5713.

**Osservazione strutturale**: per `W=|F|²` il minimo su `G̃` non è in
`G̃=∇g`. Il campo bulk ottimale è `G̃* = ½∇_Σg` (uniforme su tutte le
facce, per simmetria `σ_i=1`): metà del gradiente va nel bulk
(`|A/2|² = 0,5`/area) e metà nel difetto nucleare (`‖A/2‖_* = 1`/area),
totale `1,5`/area contro `2`/area del caso `M=0`. Il disarrangiamento
bulk **riduce** l'energia rilassata per bulk quadratico.

## 4. Verifica del cell problem (recupero SVD)

Test numerico indipendente su `[0,1]²` con `M` casuali `3×2` (`h=0,01`):
costo delle linee laminate `= h·σ_j·H¹(linee)` calcolato per corde esatte
→ rapporti `cost/‖M‖_*` ∈ `[0,99996; 1,00001]` — conferma
`𝒞(M)=‖M‖_*` per unità di area.

## 5. Limiti

- Il salto macroscopico `38,93` resta quadratura numerica; le formule
  bulk/micro sono esatte nel modello.
- Trasferimento a `G̃` variabile dentro le facce, densità anisotrope e
  vincoli di immersione: non coperti.
- La classe `G̃` costante faccia per faccia è quella per cui esiste la
  determining sequence a gradini (teorema NONZERO); il minimo trovato è
  il minimo **nella classe CF dichiarata**, non su tutti i campi
  misurabili ammissibili.
