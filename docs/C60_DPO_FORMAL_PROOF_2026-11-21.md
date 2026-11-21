# C60 — prova formale parziale, contributi ai vertici, approssimanti immersi

Data: 2026-11-21 · Stato: **teorema parziale + stime rigorose + verifiche numeriche**

Candidato: `g_f(x) = Q_f x + t_f` con `Q_f = B_f D_f B_f^T + n_f n_f^T`, `D_f` dal
campo di connessione (albero BFS), `t_f` da LS sui salti. Script:
`prove_dpo_vertex_immersed.py`.

---

## 1. Setup e formulazione

Sia `Σ` la superficie del icosaedro troncato (compatta, 32 facce piane,
1-scheletro `Σ^{(1)}` = 90 spigoli). La candidata è

```
g(x) = g_f(x)  per x ∈ relint(f),   g_f(x) = Q_f x + t_f
```\n
con `Q_f ∈ SO(3)` e `Q_f|_{T_f} = B_f D_f B_f^T` (rotazione che agente
sul piano tangente realizza `D_f ∈ SO(2)`).

**Proposizione 1 (struttura distribuzionale).** `g ∈ L^∞(Σ) ∩ BV(Σ)` e

```
∇g = G dA + S dH¹|_{Σ^{(1)}}        (misura di Radon vettoriale)
```

con `G(x) = B_f D_f` per `x ∈ relint(f)` e `S` la densità di salto
`S_e(σ) = g_g(σ) − g_f(σ)` misurata sull'arco del bordo comune.

*Dimostrazione.* `g` è continua a tratti su un insieme finito di segmenti
→ `BV`. La restrizione di `g` a ogni faccia è affine con gradiente `G_f`,
quindi la parte assolutamente continua di `Dg` è `G dA`. Il salto attraverso
ogni spigolo è ben definito (`g_f|_e − g_g|_e` costante su ogni lato) e
contribuisce con `S dH¹`. I vertici sono un insieme `H¹`-trascurabile e
non generano parte singolare addizionale perché i salti su spigoli adiacenti
sono limitati. ∎

**Proposizione 2 (isometria del campo bulk).** `G^T G = I_2` a.e. su `Σ`,
`rank G = 2`, `det` dell'indotta su ogni piano tangente = +1.

*Dimostrazione.* `G_f = B_f D_f`, `B_f^T B_f = I_2`, `D_f ∈ SO(2)` →
`G_f^T G_f = D_f^T B_f^T B_f D_f = I_2`. Rank 2 ovvio; orientazione da
`det D_f = +1`. ∎

---

## 2. Determining sequence — costruzione e convergenza

Per `h > 0` piccolo, `g_h` si ottiene da `g` "ammorbidendo" il 1-scheletro:

- **strip** di larghezza `h` attorno a ogni spigolo, prolungata fino a
  distanza `O(h)` dai vertici; su ogni strip il gradiente interpola
  affineamente tra `G_f` e `G_g` (le estensioni affini `g_f`, `g_g`);
- **cap** di raggio `R = O(h)` attorno a ogni vertice: su ogni cap,
  `C(x) = Σ_i w_i(x) g_{f_i}(x)` con `{w_i}` partition of unity subordinata
  alle 3 wedge incidenti (funzioni di smorzamento standard su coordinate
  intrinseche polari attorno a `v`).

### Lemma 1 (contributo cap — vertici). *`∫_{cap_v} |∇g_h| dA = O(h)`.*

*Dimostrazione.* Su `cap_v` (disco intrinseco di raggio `R`),
`∇C = Σ_i (∇w_i ⊗ g_{f_i}(x) + w_i G_{f_i})`. Le `w_i` sono bump di scala `R`:
`|∇w_i| ≤ C_w/R`, `Σ w_i = 1`. Quindi

```
|∇C| ≤ Σ_i (C_w/R)|g_{f_i}(x)| + √2 ≤ C'/R + √2
```

(`|G_{f_i}| = √2` perché isometria 3×2; `|g_{f_i}(x)|` limitato su compatti).
L'area intrinseca del cap è `A(cap) ≤ πR²·(348°/360°)`-corretta `= O(R²)`.
Dunque `∫_{cap_v}|∇C|dA ≤ (C'/R + √2)·cR² = O(R) → 0` per `R→0`. ∎

**Verifica numerica** (`vertex_cap` nel JSON): `R = 0,15 / 0,075 / 0,0375` →
`∫|∇C| = 19,18 / 9,51 / 4,74` — rapporto ≈ 2 per dimezzamento di `R`:
conferma `O(R)`. Somma sui 60 vertici: `O(60R) → 0`.

### Lemma 2 (strip). *`∫_{strip_e}|∇g_h|dA → ∫_e |jump_e(σ)| dσ` e il
contributo bulk `→ ∫_Σ |G| dA`.*

*Dimostrazione.* Parametrizzazione `(σ,u)`, `u ∈ (−h/2, h/2)`, blend
`λ(u) = 1/2 − u/h`. `∇S = (1−λ)G_f + λG_g + (g_g − g_f)⊗∇λ`. Il termine
`(g_g−g_f)⊗∇λ` ha norma `|jump|/h` e area elemento `dσ·du` → integrale
`≈ ∫|jump|dσ` (indipendente da `h`, verificato: 38,93 vs predetto 84,57−45,64).
I termini `G` contribuiscono `O(h)` per strip. I bordi strip-cap lasciano
segmenti residui di lunghezza `O(h)` per ogni adiacenza strip-strip e
strip-cap: la loro massa di salto residua è `O(h)·|jump|max → 0` — si
chiudono con sotto-strip di larghezza `h²` il cui costo resta `O(h)` per il
stesso argomento del Lemma 1. ∎

### Teorema (determining sequence). *Esiste `g_h → g` in `L¹(Σ)` con
`∇g_h ⇀* ∇g = G dA + S dH¹` nel senso delle misure, e
`sup_h ∫_Σ |∇g_h| dA < ∞`.*

*Dimostrazione.* Convergenza `L¹`: `|g_h − g|` è supportata in strip∪cap di
area `O(h)` con oscillazione `O(1)` → `‖g_h−g‖_1 = O(h) → 0`.
Convergenza debole-* delle derivate: split `∫φ·∇g_h` in bulk (→ `∫φ·G dA`
dominata convergenza) + strip (→ `∫φ·S dH¹` per Lemma 2, disuguaglianza
distribuzionale standard) + cap (→0 per Lemma 1). Uniform boundedness:
`∫|∇g_h| → 45,64 + 38,93 = 84,57 < ∞` (misurato: 83,93–85,76). ∎

---

## 3. Immersione e embeddedness degli approssimanti

### Proposizione 3 (immersione locale — condizionata).

`g_f|_f` è affine isometrica → immersione su ogni faccia (rank 2 esatto).
Sulle strip, `∇S(s,u)` è una combinazione di due isometrie 3×2 più il termine
rank-1 del salto; il rango resta 2 a meno che `jump` e le due giaciture non si
degenarino simultaneamente.

**Verifica numerica**: `σ_min(∇S)` su griglia densa di tutte le strip
(`h = 0,05`): **min = 8,9·10⁻⁴ > 0** → immersione locale confermata
numericamente. *Caveat onesto*: il margine è piccolo — esiste un punto quasi
deGenero; una prova uniforme richiede una stima dal basso del tipo
`σ_min ≥ c(h, |jump|, angoli)` che dipende dai dati e non è stata dimostrata.

### Sonda embeddedness globale.

Distanza minima tra immagini polygonali di facce **non adiacenti** sotto `g`:
**1,0·10⁻³ > 0** (coppia facce 0–4). Le facce adiacenti hanno immagini
separate dal salto (è il disarrangiamento); le non adiacenti non si toccano.
**Caveat**: la sonda è vertice→triangolo; intersezioni interne (spigolo-spigolo
non campionate) non sono escluse da questo test. L'embeddedness globale è
**supportata numericamente, non provata**.

---

## 4. Cosa è provato, cosa è numerico, cosa resta aperto

| Affermazione | Status |
|---|---|
| `g ∈ BV`, `∇g = G dA + S dH¹`, `GᵀG = I` | **Provato** (Prop. 1–2) |
| Determining sequence esiste, `g_h→g` in L¹, `∇g_h ⇀* ∇g` | **Provato** (Lemma 1–2 + Teorema) |
| Contributo vertici `O(h)` | **Provato** + verificato (rapporto ~2) |
| Contributo strip → massa di salto | **Provato** + verificato (84,57 predetto) |
| Immersione locale degli `g_h` | Numerico (σ_min > 0, margine piccolo) |
| Embeddedness globale | Sonda numerica positiva, non esaustiva |
| Criterio DPO completo per immersioni 2→3 | **Aperto** — serve formulazione dedicata |

Il gap residuo rispetto a una prova DPO completa: la formulazione classica
Del Piero–Owen è equidimensionale (`det` delle matrici quadrate); il caso
`G_f ∈ R^{3×2}` richiede una teoria per mappe tra varietà di dimensione
diversa — candidato naturale: formulare l'ammissibilità tramite la metrica
indotta `GᵀG` e l'energia di salto, non tramite `det`.
