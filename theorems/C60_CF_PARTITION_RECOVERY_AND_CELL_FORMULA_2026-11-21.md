# C60 — lemma di recovery per partizioni e cell formula generale

Data: 2026-11-21
Classificazione: **Lemma R dimostrato per intero (caso isotropo,
`c ∈ W^{1,1}`); Teorema cell formula dimostrato per `ψ` 1-omogenea
con simmetria `(a,ν)→(−a,−ν)` — caso anisotropo chiuso**
Prerequisiti: `C60_CF_NUCLEAR_NORM_CELL_PROBLEM_2026-11-21.md`,
`C60_CF_EXTENSIONS_VARIABLE_M_ANISOTROPIC_AUDIT_2026-11-21.md` (PR #357).

Questo documento sostituisce le formulazioni del commit `992eb80c` non
mergiate. Due risultati sono dimostrati per intero senza citare
tteoremi di rilassamento esterni: il lemma di recovery per partizioni
(caso isotropo) e la cell formula generale (qualunque `ψ` con le
ipotesi sotto). Un controesempio numerico mostra che la formula ONB a
due famiglie ortogonali non è in generale ottimale.

---

## 1. Lemma di recovery per partizioni — caso isotropo

**Ipotesi su `ψ`.** In tutta la sezione 2 si assume
`ψ: ℝ³×S¹ → [0,∞)` continua, con

```
c|a| ≤ ψ(a,ν) ≤ C|a|        (crescita e coercività)
ψ(λa,ν) = λψ(a,ν)  per λ>0 (1-omogeneità in a)
ψ(−a,−ν) = ψ(a,ν)          (simmetria non orientata)
```

**Lemma R.** Sia `Q ⊂ ℝ²` un quadrato e `c ∈ W^{1,1}(Q;ℝ^m)`. Esiste
una successione `v_h` di funzioni piecewise costanti (partizioni
poliedrali finite) con

```
v_h → c in L¹(Q;ℝ^m),   ∇v_h = 0 a.e.,
limsup_{h→0} ∫_{J_{v_h}} |[v_h]| d𝓗¹ ≤ ∫_Q ‖∇c(x)‖_* dx ,
```

`‖·‖_*` = norma nucleare (`σ₁+σ₂` per matrici `m×2`).

**Dimostrazione.** Costruzione a due scale: griglia grossa `δ` +
laminazione SVD fine `h ≪ δ`.

### Passo 0 — riduzione al caso liscio

Si estende `c` e si molletta: `c_ε = c*ρ_ε → c` in `W^{1,1}(Q)`, quindi
`∇c_ε → ∇c` in `L¹` e, poiché `|‖M‖_*−‖N‖_*| ≤ ‖M−N‖_* ≤ C‖M−N‖_F`,

```
∫_Q ‖∇c_ε‖_* → ∫_Q ‖∇c‖_* .
```

Basta provare il lemma per `c ∈ C^∞` con stima
`limsup F(v_h) ≤ ∫‖∇c‖_* + o_ε(1)` e poi diagonalizzare in `ε`.
Sia `C_ε := ‖D²c_ε‖_∞`.

### Passo 1 — griglia grossa e approssimazione affine

Partizione di `Q` in quadrati `S_j` di lato `δ` (quelli di bordo
troncati). Su `S_j` sia `M_j := ⨍_{S_j}∇c` e `x_j` il centro; sia
`ℓ_j(x) = b_j + M_j(x−x_j)` con `b_j` scelto in modo che
`⨍_{S_j}(c−ℓ_j) = 0` (possibile poiché `M_j` è la media del gradiente:
la parte affine con gradiente medio ha media corretta a meno di una
costante, fissata da `b_j`).

`c−ℓ_j ∈ W^{1,1}(S_j)` ha media zero e `∇(c−ℓ_j) = ∇c − M_j` ha media
zero. Per Poincaré–Wirtinger (medie nulle, costante dipendente solo
dalla forma del quadrato):

```
‖c − ℓ_j‖_{L¹(S_j)} ≤ C_P δ ‖∇c − M_j‖_{L¹(S_j)} .
```

Sommando in `j`:

```
Σ_j ‖c − ℓ_j‖_{L¹(S_j)} ≤ C_P δ · ‖∇c − M_δ‖_{L¹(Q)} → 0
```

perché `M_δ → ∇c` in `L¹` al raffinarsi della griglia (convergenza
delle medie locali per `∇c ∈ L¹`). Per `c` smooth vale anche la stima
uniforme di ordine due: svuluppando `c` attorno a `x_j` e usando
`|M_j − ∇c(x_j)| ≤ C_ε δ`,

```
‖c − ℓ_j‖_{L∞(S_j)} ≤ C'_ε δ² .
```

### Passo 2 — laminazione SVD dentro ogni cella

SVD di `M_j` (`m×2`, rango ≤2): `M_j = σ_1 a_1⊗v_1 + σ_2 a_2⊗v_2`,
`a_i ∈ ℝ^m` unitari, `v_1,v_2 ∈ ℝ²` ortonormali, `σ_1 ≥ σ_2 ≥ 0`
(`σ_2=0` se rango 1). Per `h>0` e fasi `φ_{j,i}` definite

```
w_{j,h}(x) := Σ_{i=1}^{2} σ_i a_i · h⌊(x·v_i + φ_{j,i})/h⌋ ,
```

e si pone `v_h|_{S_j} := b_j' + w_{j,h}`, dove `b_j'` assorbe la fase
`p_j = Σ_i σ_i a_i φ_{j,i}` (costante per cella).

**Piecewise constant.** Ogni addendo è costante sulle strisce
`{x·v_i + φ_{j,i} ∈ hℤ}`; la somma di due famiglie di strisce
direzionate diversamente è costante sulle celle poligonali della loro
disposizione, troncate a `S_j`. Quindi `v_h` è piecewise constant con
partizione poliedrale finita e `∇v_h = 0` a.e.

**Convergenza uniforme.** Da `|h⌊t/h⌋ − t| ≤ h`:

```
w_{j,h}(x) = Σ_i σ_i a_i (x·v_i + φ_{j,i}) + O(h Σσ_i)
           = M_j(x−x_j) + p_j + O(h)
```

uniformemente su `S_j`, con errore `≤ h(σ_1+σ_2) ≤ h‖M_j‖_*`. Quindi

```
v_h = ℓ_j + O(h)   uniformemente su S_j .
```

**Costo interno.** Le linee di salto della famiglia `i` sono
`{x·v_i + φ_{j,i} ∈ hℤ}` (dentro `S_j`, troncate). Su una linea di
famiglia 1, il termine `i=2` è continuo tranne nei punti isolati in
cui `x·v_2 + φ_{j,2} ∈ hℤ` — un insieme `𝓗¹`-trascurabile sulla linea.
Dunque `[v_h] = ±σ_1 h a_1` a.e. sulla linea, `|[v_h]| = σ_1 h`.
Le linee hanno densità `1/h` per unità di area (distanza `h` in
direzione `v_i`), quindi

```
costo per unità area → σ_1 + σ_2 = ‖M_j‖_*   per ogni cella S_j.
```

Le intersezioni fra le due famiglie sono punti: nessun contributo.

**Troncamento sul bordo cella.** Le strisce tagliate da `∂S_j` creano
salti di ampiezza `≤ 2h(σ_1+σ_2) = O(h)`; costo `O(h)·|∂S_j| → 0`
per `h→0` a `δ` fisso.

### Passo 3 — bordi di cella grossa

`v_h` salta su ogni `∂S_j` (condiviso da `S_j,S_k`) con ampiezza

```
|v_h^j(x) − v_h^k(x)| ≤ |ℓ_j(x) − c(x)| + |c(x) − ℓ_k(x)| + O(h)
                    ≤ 2C'_ε δ² + Ch·sup_j‖M_j‖_* .
```

(`x ∈ ∂S_j∩∂S_k ⊂ closure` di entrambe le celle, e `c` è univaluato
lì.) La lunghezza totale dei bordi per unità di area è `≈ 4/δ`.
Contributo per unità area:

```
≤ (4/δ)(2C'_ε δ² + Ch·C_M) = 8C'_ε δ + 4C_M h/δ → 0
```

scegliendo `h = δ²` (allora `h/δ = δ → 0`).

### Passo 4 — convergenza in L¹ e diagonale

Per `ε,δ` fissati e `h=δ²`, su `S_j`:
`‖v_h − c_ε‖_{L¹(S_j)} ≤ |S_j|(C'_ε δ² + Ch‖M_j‖_*)`;
sommando, `‖v_h − c_ε‖_{L¹(Q)} → 0` per `δ→0`. Quindi per `ε` fisso
esiste successione (in `δ`) con `v_h→c_ε` in `L¹` e

```
limsup_{δ→0} F(v_h) ≤ Σ_j ‖M_j‖_* |S_j| + 0
                   = ∫_Q ‖M_δ(x)‖_* dx → ∫_Q ‖∇c_ε‖_* dx ,
```

perché `M_δ → ∇c_ε` in `L¹` (anima `c_ε` smooth: anzi uniforme) e
`‖·‖_*` è una norma. Infine `ε→0`: `c_ε→c` in `L¹`, si estrae la
diagonale, e `∫‖∇c_ε‖_*→∫‖∇c‖_*`. ∎

**Teorema A (caso isotropo, `c∈W^{1,1}`).** Con `F(v)=∫_{J_v}|[v]|d𝓗¹`,

```
inf { liminf F(v_h) : v_h piecewise constant, v_h→c in L¹(Q) }
   = ∫_Q ‖∇c(x)‖_* dx .
```

**Lower bound.** Sia `Q(x)` continua a supporto compatto in `Q` con
`‖Q(x)‖_{op} ≤ 1`. Per ogni salto,
`Q:([v_h]⊗ν) = [v_h]·Qν ≤ |[v_h]|·‖Q‖_{op} ≤ |[v_h]|`.
Poiché `v_h` è piecewise constant, `Dv_h = [v_h]⊗ν 𝓗¹⌞J_{v_h}` è
puramente singolare; se `F(v_h)` è limitato allora `|Dv_h|(Q)` è
limitato e, a meno di sottosuccessione, `Dv_h ⇀* μ`. Da `v_h→c` in
`L¹`, `μ = Dc = ∇c dx` (`c∈W^{1,1}`). Allora

```
∫_Q Q:∇c dx = lim_h ∫ Q:Dv_h ≤ liminf_h F(v_h) .
```

Il sup su `Q` continue con `‖Q‖_{op}≤1` vale `∫_Q‖∇c‖_*` per dualità
`L¹–L∞` (la palla operatore è il duale unitario della norma nucleare:
`sup_{‖Q‖op≤1}Q:M = ‖M‖_*` punto per punto, e i campi misurabili
ammessi si approssimano con continui). ∎

**Applicazione CF.** Con `u_h(ξ) = G̃ξ + b + v_h(ξ)` su una faccia
(`v_h→c` dal Lemma R, `c = g − G̃ξ − b`):

- `∇_Σ u_h = G̃` a.e. esattamente (`∇v_h=0`);
- `u_h → g` in `L¹`;
- `D^s u_h ⇀* (∇_Σg − G̃)𝓗² + [g]⊗ν_g 𝓗¹⌞J_g`.

Per `W` qualunque e `ψ(a,ν)=|a|`, nel modello intrinseco:

```
I(g,G̃) = ∫_Σ W(G̃) dA + ∫_Σ ‖∇_Σg − G̃‖_* dA + ∫_{J_g}|[g]| dH¹ ,
```

dimostrato per `G̃` misurabile con `∇_Σg−G̃ ∈ L¹` (in particolare per
`G̃` costante per faccia, dove riconduce al cell problem già noto, e
per `G̃(x)` variabile qualunque). Per la C60 con `G̃_f` costante per
faccia il Lemma R non serve: `M_f` è costante e vale il teorema
nucleare diretto.

---

## 2. Cell formula generale per `ψ` — teorema completo

**Definizione.** Per `M ∈ ℝ^{3×2}` e `ψ` con le ipotesi di testa sezione:

```
ψ_rel(M) := inf { Σ_i ψ(b_i,ν_i) : N∈ℕ, b_i∈ℝ³, ν_i∈S¹ distinti
                   modulo segno, M = Σ_i b_i⊗ν_i } .
```

**Proposizione 1 (lower bound, dimostrato).** Per ogni successione
`w_h` piecewise constant con `w_h → Mx + b` in `L¹(Q)` e costi
`C_h = ∫_{J_{w_h}}ψ([w_h],ν_{w_h})d𝓗¹` limitati, e per ogni `Q ∈ Λ_ψ`:

```
Q:(a⊗ν) = a·Qν ≤ ψ(a,ν)  ∀a,ν   ⇔   Q ∈ Λ_ψ ,
```

quindi `∫_Q Q:Dw_h = ∫_{J_{w_h}}Q:([w_h]⊗ν)d𝓗¹ ≤ C_h`.
La coercività `ψ≥c|a|` dà `|Dw_h|(Q) ≤ C_h/c` limitato; da
`w_h→Mx+b` in `L¹`, `Dw_h ⇀* M dx` (il gradiente debole di `Mx+b`),
quindi `Q:M·|Q| = lim ∫Q:Dw_h ≤ liminf C_h`. Il sup su `Q∈Λ_ψ`
(costante nella cella) dà

```
liminf C_h ≥ |Q_cell| · sup_{Q∈Λ_ψ} Q:M .
```

**Proposizione 2 (upper bound, dimostrato — costruzione esplicita).**
Sia `M = Σ_{i=1}^{N} b_i⊗ν_i` con `ν_i` a due a due non paralleli
(eventuali paralleli si fondono in un unico termine). Sia `Q` un
quadrato e

```
v_h(x) = b + Σ_i b_i · h⌊(x·ν_i + φ_i)/h⌋ ,   x∈Q .
```

Allora:

- `v_h` è piecewise constant: la disposizione di `N` famiglie di
  strisce `{x·ν_i ∈ hℤ−φ_i}` produce celle poligonali finite;
  `∇v_h = 0` a.e.
- `h⌊(x·ν_i+φ_i)/h⌋ → x·ν_i+φ_i` uniformemente (`≤h`), quindi
  `v_h → b + Σ_i b_i(x·ν_i+φ_i) = b' + Mx` in `L∞`, dove
  `Σb_i⊗ν_i = M` e `b'` assorbe le fasi.
- La misura di salto converge a `M dx`: su una linea di famiglia `i`
  (a meno degli `N−1` punti isolati di incrocio con le altre famiglie,
  `𝓗¹`-trascurabili) solo `s_i` salta, `[v_h] = hb_i`, normale `ν_i`,
  densità `1/h` ⇒ contributo `b_i⊗ν_i` per unità area; somma `= M`.
- Costo: per unità area, famiglia `i` contribuisce
  `(1/h)·ψ(hb_i,ν_i) = ψ(b_i,ν_i)` per 1-omogeneità. Totale
  `→ Σ_i ψ(b_i,ν_i)`.

Dunque `ψ_rel(M) ≤ inf-decomposizioni` come in definizione, e il
candidato esatto è il min di questa classe (il vincolo "direzioni
distinte" non toglie generalità: paralleli si fondono).

**Teorema (cell formula).** Sotto le ipotesi di testa sezione,

```
boxed{  ψ_rel(M) = sup_{Q∈Λ_ψ} Q:M
       = inf { Σ_i ψ(b_i,ν_i) : M = Σ_i b_i⊗ν_i }  }
```

cioè la densità di cella è la **funzione di supporto** dell'insieme
`Λ_ψ` e coincide con l'**inviluppo convesso** dell'estensione
`Θ(T) := ψ(a,ν)` per `T = a⊗ν` rank-1 (`+∞` altrove): l'inf sulle
decomposizioni è la formula di Carathéodory per l'inviluppo convesso
di una funzione positivamente 1-omogenea (i pesi `t_i` si assorbono
ridefinendo `b_i ← t_i b_i`, usando `ψ(t_i b_i,ν_i) = t_iψ(b_i,ν_i)`),
e la sua duale è esattamente `sup_{Q∈Λ_ψ}`.

**Dimostrazione dell'uguaglianza.** Dal Prop. 1 (applicato a
sukcessioni ammissibili) `ψ_rel ≥ sup_Λ`; dal Prop. 2
`ψ_rel ≤ inf-decomp = sup_Λ` per dualità convessa. ∎

**Casi particolari.**

- `ψ(a,ν)=|a|`: `Λ_ψ={‖Q‖_{op}≤1}` ⇒ `ψ_rel=‖M‖_*` (teorema nucleare,
  recuperato come caso `Φ=|·|,k≡1`).
- `ψ(a,ν)=|a|²`: non 1-omogenea — fuori dalle ipotesi; il rilassamento
  a costo nullo dimostrato nel documento quadratico resta il risultato
  corretto per quel caso (la formula non si applica).
- `ψ=Φ(a)k(ν)` separabile: `Λ_{Φ,k}={Q: Φ°(Qν)≤k(ν) ∀ν}`; la cell
  formula è `sup` su questo insieme, **non** la formula ONB.

**Controesempio numerico (ONB non ottimale).** Script
`colloquio_morandotti/cell_check2.py` (griglia esatta sulle due
normali, decomposizione `a_i = Mw_i` con base duale — nessun
ottimizzatore). Con `M=[[1,0.3],[0.2,0.9],[0.1,−0.4]]` e
`ψ(a,ν)=|a|(2−|ν₁|)`:

```
ONB (ν₂=ν₁+90°):        min = 2.5726173
2 famiglie generiche:   min = 2.5119742   (angolo ≈103.5°)
```

La formula ONB sovrastima il costo vero di ~2,4%: è un upper bound
valido (corrisponde a una decomposizione particolare), non la cell
formula. Per `k≡1` e `Φ(a)=√(aᵀdiag(1,4,1)a)` il test `cell_check3.py`
dà ONB e 2-famiglia coincidenti entro la risoluzione della griglia:
evidenza che per costi indipendenti da `ν` l'ottimo possa restare a
due famiglie ortogonali, **non dimostrato** in generale.

---

## 3. Immersione (rank 2 a.e.)

Per `u_h(ξ) = c₀Aξ + b + v_h(ξ)` con `c₀>0`, `AᵀA=I₂` e `v_h`
piecewise constant (qualsiasi costruzione sopra, costante o variabile
per cella),

```
∇u_h = c₀A   a.e.   ⇒   rank ∇u_h = 2   a.e.
```

Proprietà del gradiente nelle regioni di continuità; non implica
continuità globale, iniettività o embeddedness attraverso i fronti di
salto. Per l'ammissibilità CF basta; per una classe di approssimanti
immersi serve una costruzione continua dedicata — resta aperta.

---

## 4. Stato finale

| Affermazione | Stato |
|---|---|
| Lower bound nucleare per `M(x)` misurabile, `ψ=|a|` | **Provato** |
| Recovery `v_h→c`, costo `∫‖∇c‖_*`, `c∈W^{1,1}` | **Provato** (Lemma R, dimostrazione completa) |
| `I(g,G̃)` con `∫‖∇_Σg−G̃‖_*` per `G̃` misurabile | **Provato** nel modello intrinseco |
| Cell formula `ψ_rel = sup_{Λ_ψ} = inf-decomposizioni` | **Provato** per `ψ` 1-omogenea in `a`, coerciva, con simmetria `(−a,−ν)` |
| `ψ=|a|` → `‖M‖_*` | **Provato** (caso particolare) |
| `ψ=Φ(a)k(ν)`: ONB formula | **Solo upper bound** (controesempio numerico ~2,4%) |
| `k≡1`, `Φ` anisotropa: ONB ottimale? | Evidenza numerica, non dimostrato |
| `ψ=|a|²` | Fuori ipotesi; risultato separato (costo rilassato nullo per `M=0`) |
| Rank 2 a.e. per `G̃=cA`, `c>0` | **Provato** |
| Embeddedness globale | Aperta |
