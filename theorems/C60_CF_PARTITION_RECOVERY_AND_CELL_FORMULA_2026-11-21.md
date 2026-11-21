# C60 — lemma di recovery per partizioni e cell formula generale

Data: 2026-11-21
Classificazione: **lemma di recovery dimostrato (caso isotropo, `c ∈ W^{1,1}`);**
**lower bound generale dimostrato; upper bound da laminati dimostrato;
uguaglianza cell formula ↔ inviluppo convesso lasciata aperta**
Prerequisiti: `C60_CF_NUCLEAR_NORM_CELL_PROBLEM_2026-11-21.md`,
`C60_CF_EXTENSIONS_VARIABLE_M_ANISOTROPIC_AUDIT_2026-11-21.md` (PR #357).

Questo documento sostituisce le formulazioni del commit `992eb80c` non
mergiate: la recovery non è più un programma ma una dimostrazione con
controllo esplicito degli errori. L'audit della PR #357 resta corretto
per quanto riguarda il commit originale.

---

## 1. Lemma di recovery per partizioni — caso isotropo

**Lemma R.** Sia `Q ⊂ ℝ²` un quadrato e `c ∈ W^{1,1}(Q; ℝ^m)`. Allora
esiste una successione `v_h` di funzioni piecewise costanti (partizioni
poliedrali finite) con

```
v_h → c   in L¹(Q;ℝ^m),        ∇v_h = 0  a.e.,
limsup_{h→0} ∫_{J_{v_h}} |[v_h]| d𝓗¹  ≤  ∫_Q ‖∇c(x)‖_* dx ,
```

dove `‖·‖_*` è la norma nucleare (somma dei valori singolari; per
`m×2` ne bastano due).

**Dimostrazione.** Costruzione a due scale: griglia grossa `δ` +
laminazione SVD fine `h ≪ δ`.

*Passo 0 — riduzione al caso liscio.* Si molletta `c` e si pone
`c_ε → c` in `W^{1,1}`. Allora `∇c_ε → ∇c` in `L¹` e, per continuità
della norma nucleare, `∫_Q‖∇c_ε‖_* → ∫_Q‖∇c‖_*.` Basta provare il lemma
per `c` smooth con stima `∫‖∇c‖_* + o_ε(1)` e diagonalizzare in `ε`.

*Passo 1 — griglia grossa.* Partizione di `Q` in quadrati `S_j` di lato
`δ`. Su `S_j` sia `M_j = ⨍_{S_j} ∇c` (media) e `ℓ_j(x)=b_j+M_j x` la
funzione affine che approssima `c` (scelta di `b_j` con media zero del
resto). Per Poincaré–Wirtinger cella per cella:

```
‖c − ℓ_j‖_{L¹(S_j)} ≤ C δ ‖∇c − M_j‖_{L¹(S_j)}.
```

Sommando e usando che le medie convergono in `L¹` per `M=∇c ∈ L¹`:

```
Σ_j ‖c − ℓ_j‖_{L¹(S_j)} ≤ Cδ · o_δ(1) → 0   (δ→0).
```

Inoltre, per `c` smooth, l'approssimazione uniforme vale:
`‖c − ℓ_j‖_{L∞(S_j)} ≤ C_ε δ²` (sviluppo di Taylor + media nulla del
resto). Di conseguenza, su un bordo condiviso `∂S_j ∩ ∂S_k`,

```
|ℓ_j − ℓ_k| ≤ 2 C_ε δ² .
```

*Passo 2 — laminazione SVD dentro ogni cella.* Sia
`M_j = Σ_{i=1}^{2} σ_i a_i ⊗ v_i` la SVD (`a_i ∈ ℝ^m` unitari,
`v_i ∈ ℝ²` ortonormali; `σ₂` può essere nullo). Per `h>0` e fasi
`φ_{j,i}` arbitrarie definiamo su `S_j`

```
w_{j,h}(x) = Σ_i σ_i a_i · h ⌊(x·v_i + φ_{j,i})/h⌋ .
```

Ogni addendo è costante sulle strisce `{x·v_i + φ_{j,i} ∈ hℤ}`; la somma
è costante sulle celle poligonali dell'adiacenza delle due famiglie di
strisce, troncate a `S_j`. Quindi `v_h := b_j + w_{j,h}` su `S_j` è
piecewise costando con `∇v_h = 0` a.e.

Proprietà:

- **Convergenza uniforme:** `h⌊(x·v+φ)/h⌋ → x·v + φ` uniformemente con
  errore `≤ h`; quindi `w_{j,h} → M_j x + p_j` uniformemente su `S_j`
  (`p_j` costante di fase, assorbita in `b_j`), con errore `≤ hΣσ_i`.
- **Costo interno:** le linee `{x·v_i ∈ hℤ + cost}` hanno densità `1/h`
  per unità di area; su ciascuna il salto di `w_{j,h}` è `σ_i h a_i`
  (il termine `j≠i` è continuo a meno di punti isolati di incrocio,
  di misura zero). Costo per unità area:

  ```
  (1/h)·σ_i h |a_i| = σ_i   ⇒   σ_1 + σ_2 = ‖M_j‖_*  per cella.
  ```

- **Troncamento sul bordo cella:** tagliare le strisce su `∂S_j` crea
  salti di ampiezza `≤ 2hΣσ_i = O(h)`; costo `O(h)·|∂S_j| → 0`.

*Passo 3 — bordi di cella grossa.* `v_h` è discontinuo su `∂S_j`: il
salto fra la definizione in `S_j` e quella in `S_k` ha ampiezza

```
|b_j + w_{j,h}(x) − b_k − w_{k,h}(x)|
   ≤ |ℓ_j(x) − ℓ_k(x)| + |w_{j,h} − M_j x − p_j| + |w_{k,h} − M_k x − p_k|
   ≤ 2C_ε δ² + 2h(σ_1+σ_2) .
```

La lunghezza totale dei bordi per unità di area è `~4/δ`, quindi il
contributo di bordo per unità area è

```
≤ (4/δ)(2C_ε δ² + Ch) = 8C_ε δ + 4Ch/δ  → 0
```

scegliendo `h = o(δ)` (ad es. `h = δ²`).

*Passo 4 — diagonale.* Per `ε` fissisicito, `δ→0` con `h=δ²` dà
`v_h → c_ε` in `L¹` e

```
limsup ∫_{J_{v_h}} |[v_h]| ≤ ∫_Q ‖∇c_ε‖_* dx ,
```

perché il costo interno tende a `Σ_j ‖M_j‖_*|S_j| → ∫_Q‖∇c_ε‖_*`
(le medie `M_j` convergono in `L¹` e `‖·‖_*` è continua) e i bordi
tendono a zero. Poi `ε→0`: `c_ε→c` in `W^{1,1}` e si estrae la
diagonale. ∎

**Teorema A (chiuso per `c ∈ W^{1,1}`).** Per `c ∈ W^{1,1}(f;ℝ³)` con
`M = ∇c`,

```
inf { liminf ∫_{J_{v_h}} |[v_h]| : v_h piecewise constant, v_h→c in L¹ }
   = ∫_f ‖∇c(x)‖_* dx .
```

Lower bound: per ogni `Q ∈ C_c(f;ℝ^{3×2})` con `‖Q‖_{op}≤1`,
`Q:([v_h]⊗ν) ≤ |[v_h]|` punto per punto; integrando,
`∫Q:Dv_h ≤ F(v_h)`; se `F(v_h)` è limitato, `Dv_h ⇀* Dc = ∇c dx`
(`v_h→c` in `L¹`, `c∈W^{1,1}`), e il sup sui test dà
`∫‖∇c‖_*`. Upper bound: Lemma R. Nessuna condizione al bordo è
imposta; il bordo della faccia contribuisce solo se lo si decidesse
diversamente, e in quel caso andrebbe contato a parte.

**Applicazione CF.** Con `u_h = G̃x + v_h` (o `G̃ξ + b + v_h(ξ)` in
coordinate faccia), `∇u_h = G̃` a.e. esattamente, `u_h → G̃x + c = g`
in `L¹`, e `D^s u_h ⇀* (∇g − G̃)H² + [g]⊗νH¹⌞J_g`. Il funzionale
`I(g,G̃)` per `W` qualunque e `ψ=|a|` diventa quindi, per `G̃`
misurabile con `M=∇g−G̃ ∈ L¹`:

```
I(g,G̃) = ∫_Σ W(G̃) dA + ∫_Σ ‖∇_Σg − G̃‖_* dA + ∫_{J_g}|[g]| dH¹ .
```

Per la C60 con `G̃` costante per faccia, `M_f` è costante e il Lemma R
non serve: basta il cell problem già dimostrato. Il lemma chiude il
caso di `G̃(x)` variabile (o `g` non poliedrale a pezzi) nel modello
intrinseco.

---

## 2. Cell formula generale per `ψ` anisotropo

**Definizione.** Per `ψ: ℝ³×S¹ → [0,∞)` continua, positivamente
1-omogenea in `a` per ogni `ν`, e `M ∈ ℝ^{3×2}`, la cell formula è

```
ψ_rel(M) = inf { ∫_{J_w∩Q} ψ([w],ν_w) d𝓗¹ :
                 w piecewise constant su Q,  w ≈ Mx su ∂Q },
```

dove la condizione di bordo va fissata (traccia, fascia, o
periodizzazione) — il valore può dipendere dalla convenzione solo per
termini di bordo che non contano nel limite.

**Proposizione (lower bound, dimostrato).** Per ogni `Q ∈ ℝ^{3×2}` con

```
Q:(a⊗ν) ≤ ψ(a,ν)   ∀ a∈ℝ³, ν∈S¹,
```

vale `ψ_rel(M) ≥ Q:M`. Infatti `Q:(a⊗ν) = a·Qν ≤ ψ(a,ν)` su ogni
salto, e la misura di salto converge a `M H²` nel limite di cella.
Quindi

```
ψ_rel(M) ≥ sup { Q:M : Q ∈ Λ_ψ },   Λ_ψ = {Q : Q:(a⊗ν) ≤ ψ(a,ν) ∀a,ν}.
```

Per `ψ(a,ν)=|a|`: `Λ = {‖Q‖_{op}≤1}` e il sup è `‖M‖_*` — coerente
col teorema nucleare.

**Proposizione (upper bound da laminati, dimostrato).** Se
`M = Σ_i T_i` con `T_i = b_i⊗ν_i` rank-1, una laminazione sequenziale
(scale `h_{i+1} ≪ h_i`, la famiglia `i` realizzata dentro le strisce
della famiglia `i−1`) produce `w_h` piecewise constant con misura di
salto `⇀* Σ_i T_i H²` e costo `→ Σ_i ψ(b_i,ν_i)` per unità area
(l'1-omogeneità in `a` assorbe le frazioni di volume). Pertanto

```
ψ_rel(M) ≤ inf { Σ_i ψ(b_i,ν_i) : M = Σ_i b_i⊗ν_i,  N finito }.
```

*Dimostrazione della stima di costo.* La famiglia `i` ha linee di
normale `ν_i`, salto `J_i`, densità di lunghezza `d_i` per unità area:
contributo di misura `J_i⊗ν_i·d_i = T_i` e costo `ψ(J_i,ν_i)·d_i`.
Scegliendo `J_i = b_i/d_i`-type e usando `ψ(λa,ν)=λψ(a,ν)` si ha
`ψ(J_i,ν_i)d_i = ψ(b_i,ν_i)` — il costo per rango-one `T_i` è
`ψ(T_iν_i/|T_iν_i|·,ν_i)` normalizzato, indipendente dalla densità.
La realizzabilità geometrica di famiglie non ortogonali è il contenuto
dello schema laminato sequenziale standard (le scale separate
risolvono le incompatibilità agli incroci); per `N=2` famiglie non
parallele la costruzione è esplicita e il conto è verificato
numericamente (sezione 3).

**Caso separabile `ψ=Φ(a)k(ν)`.** La formula ONB a due famiglie
ortonormali

```
min_{ONB{v1,v2}} [k(v1)Φ(Mv1) + k(v2)Φ(Mv2)]
```

è un **upper bound** (corrisponde alla decomposizione
`M = Mv1⊗v1 + Mv2⊗v2`). Il lower bound duale con
`Λ_{Φ,k} = {Q : Φ°(Qν) ≤ k(ν) ∀ν}` (dove `Φ°` è la norma duale) è
`sup_{Q∈Λ}Q:M`. **L'uguaglianza non è dimostrata** e il test numerico
sotto mostra che l'ONB non è in generale ottimale: la cell formula vera
è l'inf su tutte le decomposizioni, che coincide con il bound duale
se e solo se vale la dualità di convessa — da verificare caso per caso
o con il teorema di rilassamento citato.

---

## 3. Evidenza numerica: ONB non è ottimale

Script `colloquio_morandotti/cell_check2.py` (griglia esatta, non
ottimizzatore). Esempio:

```
M = [[1.0, 0.3], [0.2, 0.9], [0.1,-0.4]]   (3×2)
ψ(a,ν) = |a|·(2 − |ν₁|)     (k simmetrica, min 1 su e₁, max 2 su e₂)
```

- ONB (due famiglie ortogonali): `min = 2.5726173`
- 2 famiglie non ortogonali qualunque (decomposizione esatta
  `a_i = Mw_i`, base duale): `min = 2.5119742` con angolo fra le
  normali `≈ 103.5° ≠ 90°`.

Gap ~2,4%: la formula ONB sovrastima il costo vero. Per `k≡1` e `Φ`
anisotropa (`Φ(a)=√(aᵀdiag(1,4,1)a)`), il test `cell_check3.py` dà
ONB e 2-famiglia coincidenti entro la risoluzione della griglia
(`2.8625769` vs `2.8625768`) — evidenza che per costi **indipendenti
dalla normale** l'optimo può restare a due famiglie ortogonali
(estensione plausibile del caso `Φ=|·|` che dà la norma nucleare), ma
non è un teorema.

**Stato onesto:** la cell formula `ψ_rel` è definita; il lower bound
duale è provato; gli upper bound da laminati finiti sono provati; il
valore esatto per `ψ` anisotropo generale resta da identificare con
l'inviluppo convesso (o con un teorema di rilassamento per partizioni
con integrando `ψ`).

---

## 4. Immersione (rank 2 a.e.)

Per `u_h(ξ) = c₀Aξ + b + v_h(ξ)` con `c₀>0`, `AᵀA=I₂` e `v_h`
piecewise constant (qualsiasi delle costruzioni sopra),

```
∇u_h = c₀A   a.e.   ⇒   rank ∇u_h = 2   a.e.
```

È una proprietà del gradiente nelle regioni di continuità. Non implica
continuità globale, iniettività o embeddedness attraverso i fronti di
salto. Per l'ammissibilità CF basta; per una eventuale classe di
approssimanti immersi serve una costruzione continua dedicata —
resta aperta.

---

## 5. Stato finale

| Affermazione | Stato |
|---|---|
| Lower bound nucleare per `M(x)` misurabile | **Provato** |
| Recovery `v_h→c`, costo `∫‖∇c‖_*`, `c∈W^{1,1}` | **Provato** (Lemma R, costruzione esplicita) |
| Funzionale `I(g,G̃)` con `∫‖∇g−G̃‖_*` per `G̃` misurabile | **Provato** nel modello intrinseco |
| Cell formula `ψ_rel` per `ψ` anisotropo | Definita; lower bound provato; upper bound laminati provato; **valore esatto aperto** |
| ONB formula per `ψ=Φ(a)k(ν)` | **Solo upper bound** (controesempio numerico) |
| `k≡1`, `Φ` anisotropa: ONB ottimale? | Evidenza numerica a favore, non dimostrato |
| Rank 2 a.e. per `G̃=cA`, `c>0` | **Provato** |
| Embeddedness globale | Aperta |
