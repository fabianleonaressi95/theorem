# C60 — teorema CF isotropo per dati affini su poliedro finito

Data: 2026-11-21
Classificazione: **dimostrato** nel modello intrinseco dichiarato,
per `ψ(a,ν)=|a|` e `W ∈ {|F|_F, |F|_F²}`. Non richiede il lemma di
localizzazione: la classe SBV conserva i salti macroscopici e la
convergenza uniforme controlla le tracce sugli spigoli.

## 1. Enunciato

Sia `Σ` una superficie poliedrale compatta con un numero finito di
facce piane `f`. Siano

- `g` affine su ogni faccia: `g|_f(ξ) = A_f ξ + b_f`;
- `G̃` costante su ogni faccia: `G̃|_f = G̃_f`;
- `M_f := ∇_Σg|_f − G̃_f = A_f − G̃_f` (matrice `3×2` tangente);
- `ψ(a,ν) = |a|` la densità di salto isotropa.

Allora, per `W(F)=|F|_F` o `W(F)=|F|_F²`,

```
I_W(g,G̃) = ∫_Σ W(G̃) d𝓗² + Σ_f |f|·‖M_f‖_* + ∫_{J_g} |[g]| d𝓗¹ ,
```

dove `‖·‖_*` è la norma nucleare (somma dei valori singolari) e
`J_g` è l'insieme dei salti di `g` (inclusi i bordi di faccia dove
`g` è discontinuo).

## 2. Dimostrazione

### Lower bound

Per ogni successione determinante `u_n→g` in `L¹` con
`∇_Σu_n𝓗² ⇀* G̃𝓗²`, il lemma di liminf del costo di salto
(`C60_CF_SBV_ISOTROPIC_THEOREM_2026-11-21.md` §3.1) dà

```
liminf_n ∫_{J_{u_n}}|[u_n]| ≥ |μ|_*(Σ)
   = Σ_f |f|·‖M_f‖_* + ∫_{J_g}|[g]|d𝓗¹ ,
```

perché `μ = D_Σg − G̃𝓗² = (⊕_f M_f)𝓗² + [g]⊗ν_g𝓗¹⌞J_g` e le due
parti sono mutuamente singolari. La semicontinuità convessa del bulk
lungo la stessa sottosuccessione dà `liminf ∫W(∇u_n) ≥ ∫W(G̃)`.
Sommando: `liminf E_W(u_n) ≥` formula candidata. ∎

### Upper bound (recovery)

Su ogni faccia `f`, sia `M_f = Σ_{i=1}^{r_f} σ_{f,i} a_{f,i}⊗ν_{f,i}`
la decomposizione SVD (`r_f ≤ 2`) e `p_f := Σ_i σ_{f,i}a_{f,i}φ_{f,i}`
la costante di fase. Definiamo la laminazione **con compensazione di
fase esplicita**:

```
u_{h,f}(ξ) = G̃_f ξ + b_f + Σ_i σ_{f,i} a_{f,i}
             · h⌊(ξ·ν_{f,i}+φ_{f,i})/h⌋ − p_f .
```

Poiché `h⌊t/h⌋ = t − h·frac(t)`, vale l'identità esatta

```
u_{h,f}(ξ) − g_f(ξ) = r_{h,f}(ξ),   |r_{h,f}(ξ)| ≤ h‖M_f‖_*
   per ogni ξ ∈ ℝ² ,
```

quindi `u_{h,f} → g_f` **uniformemente su `f̄`** (non solo in `L¹`).
Tre proprietà (cell problem nucleare, già dimostrato):

1. convergenza uniforme su `f̄` come sopra;
2. `∇_Σu_{h,f} = G̃_f` a.e. (la parte laminata è costante a tratti);
3. `∫_{J_{u_{h,f}}∩f}|[u_{h,f}]|d𝓗¹ → |f|·‖M_f‖_*` quando `h→0`
   (le linee troncate al bordo danno errore `O(h·Per(f))`, e le
   intersezioni delle due famiglie di linee sono `𝓗¹`-nulle).

**Tracce sugli spigoli.** La convergenza uniforme su `f̄` implica la
convergenza uniforme delle tracce su ogni lato `e ⊂ ∂f`:
`u_{h,f}|_e → g_f|_e` uniformemente. Per un lato comune
`e = f⁻∩f⁺`, il salto effettivo della funzione globale è
`[u_h]|_e = u_{h,f⁻}|_e − u_{h,f⁺}|_e` e quindi

```
[u_h]|_e → [g]|_e   uniformemente su e  ⟹
∫_e |[u_h]|d𝓗¹ → ∫_e |[g]|d𝓗¹ .
```

Le `u_{h,f}` si incollano in una funzione globale `u_h` su `Σ`:
su ogni spigolo `e` la funzione ha il salto `[u_h]|_e`, che è
**parte del funzionale** e non un artefatto da raccordare. Le linee
di laminazione che terminano sul bordo contribuiscono solo tramite
la traccia sopra (punti isolati di incrocio, `𝓗¹`-nulli); nessun
altro costo di bordo esiste perché la cell formula è senza vincolo
di traccia. I vertici sono fini e non generano termine energetico.
La somma sugli spigoli (numero finito) dà

```
∫_{J_{u_h}}|[u_h]|d𝓗¹ → Σ_f |f|·‖M_f‖_* + ∫_{J_g}|[g]|d𝓗¹ ,
```

e `∫_Σ W(∇_Σu_h) = ∫_Σ W(G̃)` esattamente. Quindi
`limsup_h E_W(u_h) ≤` formula candidata. Con `h→0` lungo una
sottosuccessione: uguaglianza. ∎

## 3. Ipotesi usate e loro verifica

| Ipotesi | Dove è verificata |
|---|---|
| Cell formula `f_rel(M)=‖M‖_*` senza vincolo di bordo | `C60_CF_NUCLEAR_NORM_CELL_PROBLEM` — provato per `ψ=|a|` |
| Liminf del costo di salto = `|μ|_*` | Lemma §3.1 del documento SBV — provato |
| Semicontinuità di `W` | `W` convessa; `W=|F|_F` immediata, `|F|_F²` con `G̃∈L²` automatico (costante per faccia) |
| Convergenza uniforme ⇒ tracce sugli spigoli | Elementare: errore `≤h‖M‖_*` uniforme su `f̄` |
| Intersezioni di linee e vertici `𝓗¹`-nulli | Le due famiglie SVD hanno normali ortogonali; i vertici sono fini |
| Nessun vincolo di traccia sul bordo di `Q`/faccia | La cell formula è senza dato al bordo — coerente |

**Non usato**: il lemma di localizzazione, la recovery `W^{1,1}`,
la regolarizzazione continua. La struttura SBV basta perché i salti
di bordo sono parte del funzionale, non un difetto da raccordare.

## 4. Cosa questo NON copre

- **`M(x)` variabile** su una faccia: servirebbe la recovery
  `W^{1,1}` (prova candidata) più il controllo delle tracce al bordo
  — la laminazione globale non ha più `M` costante.
- **`g` non affine**: serve approssimazione SBV energetica.
- **Superfici curve**: il modello è poliedrale; il trasferimento
  richiede il controllo delle carte.
- **`ψ` anisotropo o `|a|²`**: la cell formula e la preservazione
  del salto cambiano (`|a|²` collassa sotto splitting).
- **C60 specifico**: il teorema è per il modello poliedrale con
  dati affini; per la coppia C60 originale `M=0` e vale il caso
  già dimostrato (`u_n=g`). Il valore sta nell'estensione a
  `M_f≠0` costante per faccia.
