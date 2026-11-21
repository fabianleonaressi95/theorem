# C60 — lemma di raccordo e recovery per gradiente variabile

Data: 2026-11-21
Classificazione: **dimostrazione completa del recovery isotropo per
`c ∈ W^{1,1}`** — il lemma di raccordo richiesto in
`C60_CF_PARTITION_RECOVERY_AND_CELL_FORMULA_2026-11-21.md` §3.
Documento autonomo: non usa il documento principale oltre alle
notazioni.

## Lemma R (forma finale)

Sia `Q ⊂ ℝ²` un quadrato e `c ∈ W^{1,1}(Q;ℝ^m)`. Esistono funzioni
`v_h` piecewise costanti su partizioni poliedrali finite di `Q` tali
che

```
v_h → c in L¹(Q;ℝ^m),   ∇v_h = 0 a.e.,
limsup_{h→0} ∫_{J_{v_h}} |[v_h]| d𝓗¹ ≤ ∫_Q ‖∇c(x)‖_* dx ,
```

con `‖·‖_*` la norma nucleare (`σ₁+σ₂` per matrici `m×2`).

## Dimostrazione

### Passo 0 — riduzione al caso liscio

Estendere `c` e mollecare: `c_ε = c*ρ_ε → c` in `W^{1,1}(Q)`.
Allora `∇c_ε→∇c` in `L¹` e, poiché `‖·‖_*` è una norma,
`|‖M‖_*−‖N‖_*|≤‖M−N‖_*≤C‖M−N‖_F`, si ha
`∫_Q‖∇c_ε‖_*→∫_Q‖∇c‖_*`. Basta provare il lemma per
`c∈C^∞(Q̄)` con costanti dipendenti solo da `‖c‖_{C²}`, e poi
diagonalizzare in `ε`. Indicheremo `C_c` costanti dipendenti da `c`.

### Passo 1 — griglia grossa e affine di cella

Partizione di `Q` in `N^2` sotto-quadrati di lato `δ=L/N` (essendo
`Q` un quadrato, **tutte** le celle sono quadrati completi — non esiste
alcuna cella troncata da `∂Q`, quindi la stima di slicing
`|hL_h(S_j,ν)−|S_j||≤Ch·Per(S_j)=Chδ` e il conteggio globale
`O(h/δ)` valgono senza eccezioni; forma e costante di Poincaré
uniformi). Su `S_j`:

```
M_j := ⨍_{S_j} ∇c dx,    x_j := centro di S_j,
ℓ_j(x) := β_j + M_j x,   β_j := ⨍_{S_j} c dx − M_j x_j .
```

Allora `⨍_{S_j}(c−ℓ_j)=0` e `∇(c−ℓ_j)=∇c−M_j` ha media zero.
Poincaré–Wirtinger:

```
‖c−ℓ_j‖_{L¹(S_j)} ≤ C_P δ ‖∇c−M_j‖_{L¹(S_j)} .
```

Sommando e usando `M_δ→∇c` in `L¹` (per `c` smooth, anzi
uniformemente):

```
Σ_j ‖c−ℓ_j‖_{L¹(S_j)} ≤ C_P δ·o(1) → 0 .
```

Inoltre, su ogni cella **chiusa** `S̄_j` vale la stima uniforme

```
‖c−ℓ_j‖_{L∞(S̄_j)} ≤ C_c δ² .      (1)
```

*Verifica di (1).* Sviluppando `c` attorno a `x_j`:
`c(x)−c(x_j)−∇c(x_j)(x−x_j)=O(δ²‖D²c‖)`;
`|M_j−∇c(x_j)|≤⨍_{S_j}|∇c−∇c(x_j)|≤Cδ‖D²c‖`;
`|c(x_j)−β_j−M_jx_j|=|c(x_j)−⨍c|≤Cδ²‖D²c‖`. Tre contributi `O(δ²)`.

### Passo 2 — laminazione SVD dentro ogni cella

SVD di `M_j` (`m×2`, rango ≤2): `M_j = σ_1 a_1⊗v_1 + σ_2 a_2⊗v_2`,
`a_i∈ℝ^m` unitari, `v_i∈ℝ²` ortonormali, `σ_2` può essere nullo.
Fasi `φ_{j,i}` arbitrarie; per `h>0`:

```
w_{j,h}(x) := Σ_{i=1}^{2} σ_i a_i · h⌊(x·v_i + φ_{j,i})/h⌋ .
```

**Identità esatta con la costante di fase.** Poiché
`h⌊t/h⌋ = t − hρ(t)` con `ρ(t)∈[0,1)` la parte frazionaria,

```
w_{j,h}(x) = M_j x + p_j + r_{j,h}(x),
   p_j := Σ_i σ_i a_i φ_{j,i},
   |r_{j,h}(x)| ≤ h(σ_1+σ_2) = h‖M_j‖_*   ∀x∈ℝ² .
```

La costante che rende `v_h ≈ ℓ_j` è allora **univoca**:

```
v_h|_{S_j}(x) := β_j + w_{j,h}(x) − p_j
             = ℓ_j(x) + r_{j,h}(x) ,          (2)
```

cioè `v_h|_{S_j} = ℓ_j + r_{j,h}` identicamente, con
`|r_{j,h}|≤h‖M_j‖_*` su tutto `S̄_j` (la stima è globale, non solo
interno).

**Struttura.** Le strisce `{x·v_i+φ_{j,i}∈hℤ}` delle due famiglie
(`v_1⊥v_2`) determinano celle poligonali convesse; `v_h` è costante
su ciascuna, troncata a `S_j`. `∇v_h=0` a.e.

**Costo interno — conto esplicito.** Sulle linee
`{x·v_i+φ_{j,i}∈hℤ}∩S_j`, a meno dei punti isolati di incrocio con
l'altra famiglia (`𝓗¹`-nulli), solo il termine `i` salta:
`[v_h]=±σ_i h a_i`, `|[v_h]|=σ_i h`. Per la famiglia `i`, sia `L_i`
la lunghezza totale delle sue linee in `S_j`. Sia
`A(t) := 𝓗¹(S_j ∩ {x·v_i = t})`. Poiché `|∇(x·v_i)|=1`, la formula di
coarea dà `∫_ℝ A(t)dt = |S_j|`, e `L_i = Σ_k A(kh−φ_{j,i})` (le linee
sono i livelli `t ∈ hℤ−φ_{j,i}`). La stima di quadratura per funzioni
a variazione limitata su una griglia traslata è

```
|h Σ_k A(kh−φ) − ∫_ℝ A(t)dt| ≤ C h · TV(A) ,
```

con `C` universale e **indipendente dalla traslazione `φ`** (la
stima per regola di rettangoli di una funzione BV controlla
l'errore per ogni scelta di nodi). Per `S_j` quadrato, `A` è continua,
piecewise lineare e **unimodale** (cresce linearmente da 0 al valore
massimo e decresce): `TV(A) = 2 max_t A(t) ≤ 2 diam(S_j) ≤ C Per(S_j)`
uniformemente in `ν` (la maggiorazione usa solo diametro e perimetro,
non la direzione). Quindi

```
|hL_i − |S_j|| ≤ C h · Per(S_j) = C h δ ,
costo famiglia i in S_j = σ_i h·L_i = σ_i |S_j| + O(σ_i h δ) .
```

Il costo interno totale per cella è `|S_j|‖M_j‖_* + O(hδ‖M_j‖_*)`.
Sommato sulle `O(δ^{-2})` celle l'errore è `O(h/δ)`: con la scelta
`h=δ³` diventa `O(δ²)→0`. (Con `h=δ²` darebbe `O(δ)→0` anch'esso, ma
`h=δ³` rende il margine esplicito.)

### Passo 3 — raccordo sui bordi di cella (il lemma mancante)

Sia `E = ∂S_j∩∂S_k` un'interfaccia interna di `Q` e `x∈E`. Poiché
`E ⊂ S̄_j∩S̄_k`, la formula (2) vale su **entrambi** i lati e la
stima (1) vale su entrambe le celle chiuse:

```
|v_h^j(x) − v_h^k(x)|
 ≤ |v_h^j−ℓ_j|(x) + |ℓ_j(x)−c(x)| + |c(x)−ℓ_k(x)| + |ℓ_k−v_h^k|(x)
 ≤ h‖M_j‖_* + C_cδ² + C_cδ² + h‖M_k‖_*
 ≤ C_c(δ² + h) .                                    (3)
```

**Punto chiave:** non serve che `ℓ_j` e `ℓ_k` coincidano sul bordo —
serve solo che entrambe approssimino la *stessa* funzione `c` nello
stesso punto `x`, e la stima (1) è su celle chiuse. La costante di
fase `p_j` non è libera: è fissata da (2) e non appare nella stima
finale perché `v_h^j−ℓ_j=r_{j,h}` è già `O(h)`.

Lunghezza totale delle interfacce interne per unità di area:
`≈ 4/δ` (perimetro `4δ` per cella, area `δ²`, ogni spigolo contato
una volta). Con `h=δ³` (allora `h/δ=δ²→0`), il contributo di bordo
per unità area:

```
≤ (4/δ)·C_c(δ² + δ³) = 4C_cδ + O(δ²) → 0 .          (4)
```

Nessun'altra interfaccia artificiale esiste: dentro `S_j` il costo è
quello laminato; su `∂S_j` quello di (4); il bordo esterno `∂Q` non
contribuisce (nessun vincolo di traccia imposto).

### Passo 4 — convergenza e diagonalizzazione esplicita

Per `δ→0` con `h=δ³`:

```
‖v_h−c‖_{L¹(Q)} ≤ Σ_j (|S_j|·h‖M_j‖_* + ‖ℓ_j−c‖_{L¹(S_j)})
              ≤ Ch + C_P δ·o(1) → 0 ,
```

quindi `v_h→c` in `L¹` (per `c` smooth; la maggiorazione
`|v_h−ℓ_j|≤h‖M_j‖_*` usa (2), e `Σ‖ℓ_j−c‖_{L¹}→0` dal Passo 1).
Il costo interno per cella è `|S_j|‖M_j‖_* + O(hδ‖M_j‖_*)`; sommato
dà `∫_Q‖M_δ(x)‖_*dx + O(h/δ) → ∫_Q‖∇c‖_*dx` per `c` smooth
(`M_δ→∇c` uniformemente). Pertanto, per `c` smooth e `h=δ³`:

```
limsup_{δ→0} ∫_{J_{v_h}} |[v_h]| ≤ ∫_Q ‖∇c‖_* dx .
```

**Diagonalizzazione esplicita.** Sia `c_ε = c*ρ_ε → c` in `W^{1,1}`
(Passo 0), `ε_n ↓ 0` con `‖c_{ε_n}−c‖_{W^{1,1}}<1/n`. Per ogni `n`,
`c_{ε_n}` è smooth: esiste `δ_n > 0` tale che, posto `h_n = δ_n³`, la
costruzione sopra dia `v_n` con **energia totale** (costo interno +
raccordi) che soddisfa simultaneamente

```
‖v_n − c_{ε_n}‖_{L¹} < 1/n,
F(v_n) := ∫_{J_{v_n}}|[v_n]|d𝓗¹ < ∫_Q‖∇c_{ε_n}‖_*dx + 1/n ,
```

dove la seconda disuguaglianza include già i raccordi perché `F` è il
costo di salto completo della funzione, non la sola parte interna.

Allora `‖v_n−c‖_{L¹} ≤ ‖v_n−c_{ε_n}‖ + ‖c_{ε_n}−c‖ → 0` e

```
limsup_n ∫_{J_{v_n}}|[v_n]| ≤ lim_n ∫_Q‖∇c_{ε_n}‖_* = ∫_Q‖∇c‖_* .
```

∎

## Lower bound (ricapitolazione)

Per `Q(x)` continua a supporto compatto in `Q` con
`‖Q(x)‖_{op}≤1`: `Q:([v_h]⊗ν)=[v_h]·Qν≤|[v_h]|` punto per punto.
I costi limitati danno `|Dv_h|(Q)≤F(v_h)` limitato; `v_h→c` in `L¹`
⇒ `Dv_h⇀*Dc=∇c dx`; il sup sui campi test (duale `L¹–L∞` della
norma nucleare) dà `liminf F(v_h)≥∫_Q‖∇c‖_*`. Con l'upper bound del
Lemma R:

```
inf_{v_h→c in L¹} liminf F(v_h) = ∫_Q ‖∇c(x)‖_* dx .   ∎
```

## Applicazione CF

Con `u_h(ξ)=G̃ξ+b+v_h(ξ)` su una faccia (`v_h→c=g−G̃ξ−b` dal Lemma R):

- `∇_Σu_h = G̃` a.e. esattamente (`∇v_h=0`);
- `u_h→g` in `L¹`;
- `D^su_h ⇀* (∇_Σg−G̃)𝓗² + [g]⊗ν_g 𝓗¹⌞J_g`.

Per `W` qualunque e `ψ(a,ν)=|a|`, nel modello intrinseco:

```
I(g,G̃) = ∫_Σ W(G̃)dA + ∫_Σ‖∇_Σg−G̃‖_*dA + ∫_{J_g}|[g]|dH¹ ,
```

dimostrato per `G̃` misurabile con `∇_Σg−G̃∈L¹`.

**Ipotesi e caveat dell'applicazione.** Il passaggio da faccia a
superficie usa il modello intrinseco dichiarato: la costruzione è
fatta su ogni faccia piana separatamente e il termine
`∫_{J_g}|[g]|dH¹` conta i salti macroscopici di bordo, che la
laminazione interna non tocca (le linee di salto della costruzione
restano dentro la faccia; il bordo esterno `∂f` non ha vincoli di
traccia). La convergenza `D^su_h ⇀* (∇_Σg−G̃)H² + [g]⊗νH¹⌞J_g`
richiede inoltre che la parte di bordo della successione non crei
concentrazione spurie: le stime del Lemma R controllano il costo
interno e i raccordi di cella, mentre i bordi di faccia ereditano il
trattamento del cell problem costante per faccia. Per `G̃` costante
per faccia non serve nulla di tutto ciò: vale il teorema nucleare
diretto.
