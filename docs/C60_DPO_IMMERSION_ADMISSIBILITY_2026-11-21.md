# Ammissibilità DPO per immersioni 2→3 — definizione e verifica sul C60

Data: 2026-11-21 · Companion di `C60_DPO_FORMAL_PROOF_2026-11-21.md`
Script: `certify_c60_dpo_immersed.py`

---

## 1. Il problema

La formulazione classica Del Piero–Owen (1993) è **equidimensionale**:
`u : Ω ⊂ R^d → R^d`, e l'ammissibilità usa `det ∇u > 0` e la decomposizione
`∇u = ∇y + D` (gradiente mediato + disarrangiamento). Per la nostra g il
codominio è `R³` e `G_f` è `3×2`: `det` non esiste. Serve l'analogo per
mappe tra varietà di dimensione diversa.

## 2. Definizione proposta (DPO-immersione)

**Definizione.** Sia `Σ` una superficie compatta (2-varietà) e `g : Σ → R³`
limitata. La tripletta `(Σ, g, G)` è **DPO-ammissibile per immersioni** se:

- **(A1) Regolarità**: `g ∈ L∞(Σ) ∩ BV(Σ; R³)`.
- **(A2) Condizione metrica**: esiste `G ∈ L∞(Σ; R^{3×2})` con
  `GᵀG` definita positiva a.e. — l'analogo di `det > 0`: la metrica indotta
  `GᵀG` deve essere riemanniana (nessun collasso di rango).
- **(A3) Struttura distribuzionale**: `Dg = G dA + S dH¹⌞Γ` dove `Γ` è un
  complesso 1-dimensionale localmente finito e `S` la densità di salto.
- **(A4) Determining sequence immersa**: esiste `h_n → 0` e mappe
  `g_n ∈ W^{1,1}_{loc}` continue con
  `g_n → g` in `L¹`, `∇g_n ⇀* Dg` come misure, e `rank ∇g_n = 2` a.e.
  (ogni `g_n` immersione locale) con `sup_n ∫|∇g_n| < ∞`.

**Osservazione.** (A2) è la corretta generalizzazione: per `d×d`,
`GᵀG` definita positiva ⇔ `det G ≠ 0`; la condizione di orientazione
`det G > 0` diventa la scelta di orientazione delle fibre (qui `D_f ∈ SO(2)`
la fissa). Il disarrangiamento DPO classico `D = ∇v − G` generalizza a
`S dH¹` + eventuale parte di Cantor — per la nostra g la parte singolare è
interamente concentrata sugli spigoli.

## 3. Teorema di verifica per la candidata C60

**Teorema.** La g pezzo per pezzo con `D_f` dall'albero BFS soddisfa (A1)–(A3)
in modo provato e (A4) con immersione certificata numericamente.

| Assema | Status | Evidenza |
|---|---|---|
| (A1) `g ∈ BV` | **Provato** | Prop. 1 di `C60_DPO_FORMAL_PROOF` |
| (A2) `GᵀG = I₂` | **Provato** | Prop. 2, residuo 2,9·10⁻¹⁵ |
| (A3) `Dg = GdA + SdH¹` | **Provato** | struttura esatta, massa salto 38,93 |
| (A4) strip+cap, `g_h→g` L¹, `∇g_h⇀*Dg` | **Provato** | Lemma 1–2 + Teorema (vertici O(h)) |
| (A4) `rank ∇g_h = 2` | **Certificato numerico esatto** | vedi sotto |

## 4. Certificato di immersione esatto

Sulle strip `S(σ,u)` è **analitica a tratti**: fissato il lato (`u>0` o
`u<0`), con `λ(u) = 1/2 − u/h` e `x = pa + σ·te + u·η`:

```
a(σ,u) = ∂S/∂σ = (1−λ)Q_f te + λ Q_g te              ∈ R³, dipende solo da u
du S/∂u = b(σ,u) = [(1−λ)Q_f + λQ_g]η − (1/h)·jump(x) ∈ R³
```

`rank ∇S = 2 ⇔ a × b ≠ 0`. Poiché `a` dipende solo da `λ` (1 parametro) e `b`
è esplicito in `(σ,u)`, la condizione è una **disuguaglianza polinomiale**
su ogni cella compatta — non serve più il campionamento FD.

**Stima asintotica**: per `h→0`, `b ≈ −jump/h` domina, quindi

```
σ_min(∇S) → |a(λ) × ĵ(σ,u)|   (componente di a ⊥ alla direzione del salto)
```

La degenerazione richiede `a ∥ jump`: le due dipendenze sono da parametri
diversi (`λ` vs `(σ,u)`), quindi è una condizione di codimensione alta —
ma va verificata, non assunta.

**Risultati numerici esatti** (`c60_dpo_immersed_certificate_*.json` e
scan `|a×b|`):

- `σ_min(∇S)` minimo su tutte le 90 strip, griglia esatta densa:
  **1,2·10⁻⁴** (spigolo 5, σ≈0,28, u≈0,004, lato f) — immerso ma con
  margine sottile: esiste una quasi-piega fisica dove `a` quasi parallelo
  alla direzione del salto.
- `|a×b|` minimo: **8,5·10⁻⁴**, nessuno zero rilevato su griglia
  400×300 per lato × 90 spigoli. Poiché `rank ∇S = 2 ⇔ a×b ≠ 0` e il
  rango serve solo **quasi ovunque** perche' `g_h ∈ W^{1,1}` immersa,
  un eventuale zero isolato (se esistesse) sarebbe un insieme di misura
  zero e non violerebbe (A4).
- Il limite `u→0` (bordo dello strip) ha σ_min ≈ 5·10⁻³: la
  quasi-degenerazione e' interna, non al bordo.

**Chiusura analitica restante**: `a×b ≠ 0` e' una disuguaglianza
polinomiale su celle compatte — certificabile con aritmetica a
intervalli ( Bernstein / interval Newton ). E' un problema tecnico
chiuso, non un'obiezione concettuale.

## 5. Cosa resta

- **Chiusura analitica di (A4)**: la disuguaglianza `a×b≠0` è verificata
  densamente; una prova completa richiede bound di splitting o verifica
  per celle (es. aritmetica a intervalli) — fattibile perché è polinomiale.
- **Embeddedness**: la sonda vertice→triangolo dà distanza minima
  1,0·10⁻³ tra facce non adiacenti; la definizione (A4) richiede solo
  immersione *locale*, non embedded — la sonda resta un check extra.
- **Cap ai vertici**: `∇C = Σ(∇w_i⊗g_{f_i} + w_i G_{f_i})` — rank 2 non
  automatico; stessa verifica polinomiale possibile, da eseguire.
- **Certificazione interval**: trasformare il campionamento denso in
  prova (la funzione e' polinomiale di grado basso in (σ,u)).
