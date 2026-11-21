# C60 — estensioni del cell problem: `M` variabile, densità anisotrope, immersione

Data: 2026-11-21
Classificazione: **teoremi dimostrati nel modello intrinseco faccia-per-faccia**
Prerequisiti: `C60_CF_NUCLEAR_NORM_CELL_PROBLEM_2026-11-21.md`,
`C60_CF_NONZERO_BULK_DISARRANGEMENT_2026-11-21.md`.

## 1. Estensione a `M(ξ)` variabile — localizzazione

**Teorema A.** Sia `f` una faccia piana e `M ∈ L^∞(f; R^{3×2})` un campo
misurabile. Per ogni successione `u_h ∈ SBV(f;R³)` con
`u_h → g` in `L¹`, `∇u_h = G̃` a.e. e
`D^s u_h ⇀* M(x)𝓗² + (contributi di bordo)`:

```
liminf_h ∫_{J_{u_h}} |[u_h]| d𝓗¹  ≥  ∫_f ‖M(x)‖_* d𝓗²,
```

e il lower bound è realizzato: esiste una successione per cui vale
l'uguaglianza nel limite. Pertanto la densità di cella puntuale è
`𝒞(M(x)) = ‖M(x)‖_*` e il costo micro-interfaciale totale è
`∫_f ‖M(x)‖_* dx`.

**Dimostrazione.** *(Lower bound.)* La condizione determinante dà
`D^s u_h ⇀* M𝓗²` sulle porzioni interne. Sia `Q ∈ L^∞(f;R^{3×2})` un campo
test misurabile con `‖Q(x)‖_{op} ≤ 1` a.e. Per ogni salto,

```
Q(x):([u_h]⊗ν) = [u_h]·Q(x)ν ≤ |[u_h]| · ‖Q(x)‖_{op} ≤ |[u_h]|.
```

Integrando contro `Q` e passando al limite debole-*:

```
∫_f Q:M d𝓗² ≤ liminf ∫_{J_{u_h}} |[u_h]| d𝓗².
```

Il campo `Q*(x)` che realizza la dualità nucleare puntuale
(`Q* = UV^T` dalla SVD di `M(x)`, scelta misurabile) soddisfa
`Q*(x):M(x) = ‖M(x)‖_*` e `‖Q*‖_{op}=1` a.e. Sostituendo si ottiene il
lower bound. La scelta misurabile esiste perché la SVD è Borel-misurabile
(e si può regolarizzare dove `M` degenera).

*(Recovery.)* Se `M` è continua, la costruzione SVD del cell problem si
applica localmente: si partiziona `f` in celle piccole dove `M` è quasi
costante, si usa la laminazione con direzioni `v_j(x)` variabili
continuamente (il gradino `⌊(ξ·v_j(ξ))/h⌋` si generalizza con la
funzione di fase `dist` lungo il campo di linee — la stessa stima
`O(h)` di convergenza uniforme regge perché `M` è Lipschitz su ogni
cella). Per `M` solo misurabile si approssima in `L¹` con `M_k`
continue (Lusin + partizione di unità) e si diagonalizza `h_k → 0`:
l'errore `∫‖M−M_k‖_* → 0` controlla la differenza di costo per
1-omogeneità della norma nucleare. I bordi di cella contribuiscono
`O(δ_k) → 0`. ∎

**Corollario.** La formula del funzionale diventa, per `G̃` misurabile:

```
I(g,G̃) = ∫_Σ W(G̃) dA + ∫_Σ ‖∇_Σg − G̃‖_* dA + ∫_{J_g}|[g]|dH¹.
```

e l'ottimizzazione su `G̃(x)` punto per punto (per `W` convessa) resta un
problema di dimensione finita in ogni `x`.

## 2. Densità anisotrope separabili `ψ(a,ν) = Φ(a)·k(ν)`

Sia `Φ` una norma su `R³` e `k : S¹ → R_{>0}` una funzione continua
misurabile (costo per unità di lunghezza della normale `ν`).

**Teorema B (formula di cella).** Il costo minimo per generare il
difetto bulk `M` costante su una faccia è

```
𝒞_{Φ,k}(M) = min_{ONB {v₁,v₂} ⊂ R²} [ k(v₁)·Φ(Mv₁) + k(v₂)·Φ(Mv₂) ].
```

**Dimostrazione — recovery.** Data un'ONB `{v₁,v₂}`, si usa la
costruzione laminata SVD generalizzata: la famiglia `j` ha linee di
normale `v_j`, passo `h`, e salto `h·Mv_j` (vettore in `R³`). La misura
di salto converge a `M𝓗²` perché
`Σ_j (Mv_j)⊗v_j = M·(v₁⊗v₁+v₂⊗v₂) = M`. Il costo per unità di area è
`Σ_j k(v_j)·Φ(hMv_j)/h = Σ_j k(v_j)Φ(Mv_j)`. Minimizzando su tutte le
basi ortonormali si ottiene il valore della formula. (Per `Φ=|·|`,
`k≡1`: `min_ONB(|Mv₁|+|Mv₂|) = σ₁+σ₂ = ‖M‖_*` — la formula nucleare è
il caso separabile isotropo, coerente col teorema precedente.)

**Dimostrazione — lower bound.** Per ogni salto `a⊗ν` e ogni campo
test `Q` con `Φ^∘(Qν) ≤ k(ν)` per ogni `ν` (dove `Φ^∘` è la norma duale),

```
Q:(a⊗ν) = a·Qν ≤ Φ(a)·Φ^∘(Qν) ≤ Φ(a)k(ν) = ψ(a,ν).
```

Il sup over tutti i `Q` ammissibili di `∫Q:M` fornisce il lower bound.
L'uguaglianza tra questo sup e la formula ONB è un'identità di dualità
convessa (la formula ONB è la funzione di supporto del vincolo
`Φ^∘(Qν)≤k(ν)`); per `Φ=|·|,k=1` coincide con la norma nucleare ed è
verificata. **Per `Φ,k` generali l'uguaglianza è congetturata**: il
lower bound è provato, la formula ONB è un upper bound provato, e
l'identificazione richiede il teorema di minimax per il problema di
cella — plausibile ma non dimostrata qui.

## 3. Vincolo di immersione

Per la successione a gradini `u_h = G̃ξ + b + M·q_h(ξ)`:

- `∇_Σu_h = G̃` quasi ovunque, quindi `rank ∇u_h = rank G̃` a.e.
- Per `G̃ = c·A` con `c>0` (incluso l'ottimo `c=1/2` per `W=|F|²`):
  `rank G̃ = 2` → **immersione locale a.e. preservata**, senza bisogno
  del certificato polinomiale degli strip continui (che si applicava a
  un'altra costruzione).
- Le interfacce di salto sono insiemi di misura zero per il gradiente:
  la condizione (A4) "rank 2 a.e." è soddisfatta.
- **Non coperto**: embeddedness/globale iniettività delle `u_h` — la
  classe CF SBV non la richiede, ma se si vuole ammissibilità DPO
  stretta serve una costruzione dedicata (la laminazione crea
autointersezioni nelle micro-strisce, da analizzare caso per caso).

## 4. Stato aggiornato

| Estensione | Stato |
|---|---|
| `M(ξ)` misurabile, `ψ=|a|` | **Teorema A**: densità puntuale `‖M(x)‖_*` |
| `ψ=Φ(a)k(ν)` separabile | Formula ONB: upper bound provato, lower bound duale provato, uguaglianza congetturata |
| `ψ` anisotropa non separabile | Solo lower bound duale `sup_{Q∈Λ_ψ}Q:M` |
| Immersione a.e. per `G̃=cA`, `c>0` | **Provata** (rank 2 a.e.) |
| Embeddedness globale | Aperta |
