# C60 — teorema SBV isotropo: enunciato e stato delle componenti

Data: 2026-11-21
Classificazione: **teorema in costruzione** — l'enunciato è fissato,
ogni componente ha un dato stato di prova. Non è un risultato
completo: la recovery per `g` con salti è aperta
(`C60_CF_LOCALIZATION_LEMMA_2026-11-21.md`).

## 1. Funzionale microscopico effettivo

Dal materiale della PR, il funzionale di partenza sul polyedro `Σ` è

```
E_W(u) := ∫_Σ W(∇_Σu) d𝓗² + ∫_{J_u} |[u]| d𝓗¹ ,
```

con `W(F) = |F|_F` o `|F|_F²` (casi trattati) e densità di salto
`ψ(a,ν) = |a|` (isotropo, 1-omogeneo, convesso in `a`). Il funzionale
rilassato candidato è

```
I(g,G) := inf { liminf_n E_W(u_n) :
                u_n → g in L¹(Σ),  ∇_Σu_n 𝓗² ⇀* G 𝓗² }
```

sulle successioni determinanti CF (Choksi–Fonseca): `g ∈ SBV(Σ)`,
`G ∈ L¹(Σ; ℝ^{3×2})` con la struttura tangente dichiarata nei
documenti precedenti.

## 2. Enunciato candidato (caso isotropo)

Per `M := ∇_Σg − G ∈ L¹`, la formula attesa è

```
I(g,G) = ∫_Σ W(G) dA + ∫_Σ ‖M‖_* dA + ∫_{J_g} |[g]| d𝓗¹ ,
```

con `‖·‖_*` la norma nucleare (somma dei valori singolari) definita
con le metriche tangenti di `Σ`. **Questa formula è una congettura di
lavoro**: non segue automaticamente da CF né dalle recovery locali;
ogni addendo va giustificato separatamente (v. sotto).

## 3. Stato delle componenti

### 3.1 Limite inferiore — parzialmente provato

- **Bulk**: la dualità `‖M‖_* = sup_{‖Q‖_op≤1} Q:M` e la semicontinuità
  delle misure danno `liminf ∫_{J_{u_n}}|[u_n]| ≥ ∫‖∇_Σg−G‖_*` nel
  modello intrinseco — **provato** per `G̃` misurabile
  (documento principale, sezione lower bound).
- **Bulk `W(G)`**: semicontinuità di `∫W(∇u_n)` sotto convergenza
  `L¹`-debole dei gradienti vale per `W` convessa con crescita
  appropriata; per `W=|F|_F²` serve il controllo `L²` (disponibile,
  v. minimality doc). **Provato nei casi esaminati.**
- **Superficie `∫_{J_g}|[g]|`**: la densità `ψ(a,ν)=|a|` è convessa e
  1-omogenea in `a`; lo splitting di un salto in `m` pezzi di
  ampiezza `a/m` costa `m·|a|/m = |a|` — **la densità di salto è
  preservata sotto microstruttura** (a differenza di `|a|²`, che
  collassa). La semicontinuità `∫_{J_{u_n}}|[u_n]| ≥ ∫_{J_g}|[g]|`
  per `u_n→g` in `SBV` è il teorema di lower semicontinuity di
  Ambrosio per funzionali BV-ellittici — **provato**, purché il
  funzionale sia BV-ellittico (da verificare per `|a|` esplicitamente).
- **Accoppiamento**: il lower bound con entrambi i termini
  `W(G)` e `‖M‖_*` simultaneamente richiede che le misure non
  "rubino" massa l'una all'altra — verificato per le successioni
  determinanti perché `∇u_n ⇀* G` fissa la parte AC.

### 3.2 Limite superiore (recovery) — per livelli

| Livello | Stato |
|---|---|
| `M` costante per faccia, `ψ=|a|` | **Provato** (cell problem nucleare) |
| `c ∈ W^{1,1}`, `ψ=|a|` | **Prova candidata** (`C60_CF_VARIABLE_GRADIENT_RECOVERY_PROOF`), audit richiesto |
| `g` con salti su `J` finito poliedrale | **Aperto** — richiede `C60_CF_LOCALIZATION_LEMMA` |
| `g ∈ SBV` generale | **Aperto** — richiede teorema di densità con controllo di salto ed energia |
| `G̃(x)` variabile misurabile | **Aperto** — dipende dal livello `W^{1,1}` |
| Superficie C60 (carte, metriche, giunzioni) | **Aperto** — richiede controllo errori di carta |

### 3.3 Crescita e raccordo agli spigoli — quasi chiuso per `|a|`

Per `W(F)=|F|_F` (crescita lineare, `q=1<2`) la stima
`r²·sup_{|p|≤C/r} f(p) = O(r)` chiude il punto 4 del lemma di
localizzazione **se** il raccordo ha gradiente `O(1/r)` e il costo
superficiale resta `φ=|a|` — la costruzione resta da scrivere.
Per `W(F)=|F|_F²` (`q=2`) la stima è solo `O(1)`: serve una
costruzione con gradiente meglio controllato o una stima più fine —
**gap identificato**, non ancora risolto.

### 3.4 Anisotropo — solo dopo il caso isotropo

La cell formula anisotropa (`g_ψ(M) = sup_{Q∈Λ_ψ} Q:M`) è provata
senza vincolo di bordo; il suo uso nel recovery bulk erediterebbe
gli stessi gap di localizzazione. La formula ONB resta solo upper
bound.

## 4. Ipotesi da verificare prima di dichiarare il teorema

1. `W` convessa, con la crescita dichiarata (`q=1` o `q=2`);
   per `q=2` la ricostruzione agli spigoli va raffinate.
2. `ψ(a,ν)=|a|` BV-ellittica e additiva sotto splitting — verificato
   ma va scritto come ipotesi esplicita.
3. Le metriche tangenti di `Σ` forniscono `‖·‖_*` coerente; il
   passaggio facce→superficie richiede errori di carta uniformi.
4. Il teorema di densità SBV invocato (Lazzaroni–Wozniak–Zhang o
   equivalente) deve preservare **entrambi** i contributi energetici,
   non solo la convergenza `L¹`.
5. L'ordine dei limiti `ε→0, r↓0, ρ↓0` con diagonalizzazione.

## 5. Prossimo passo dimostrabile

Il primo risultato chiudibile senza nuovi ingredienti esterni è il
**caso poliedrale finito con `W=|F|_F`**: recovery bulk (Lemma R
candidato) + lemma di localizzazione (da dimostrare, `q=1` copre il
punto 4) + salti preservati (`|a|` additiva). La parte ancora
mancante è la **costruzione esplicita del raccordo sugli spigoli**
con la sua stima quantitativa — è il contenuto del lemma di
localizzazione, da dimostrare con le stime già disponibili.
