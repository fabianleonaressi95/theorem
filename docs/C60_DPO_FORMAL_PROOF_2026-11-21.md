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

## 2. Regolarizzazione continua e determining sequence CF

La costruzione strip+cap descritta nei calcoli definisce una successione
continua `g_h` ottenuta interpolando le tracce affini attraverso gli
spigoli e raccordando i vertici. Le stime di scala per cap e strip possono
studiare il costo TV di questa regolarizzazione. Non dimostrano che
`g_h` determini la coppia strutturata `(g,G)`.

Se `g_h∈W^{1,1}(Σ;R³)`, allora `D_Σg_h=∇_Σg_h 𝓗²`. Se
`g_h→g` in `L¹`, le derivate distribuzionali convergono a `D_Σg`
in distribuzioni. Per la mappa a tratti
```
D_Σg = G 𝓗² + [g]⊗ν_g 𝓗¹⌞J_g.
```
Quando il salto macroscopico è non nullo, questo limite non coincide con
`G 𝓗²`. La convergenza richiesta da Choksi–Fonseca è invece
`∇_Σu_n 𝓗² ⇀* G 𝓗²`, con `u_n∈SBV`; la parte singolare `D^s_Σu_n`
deve generare
```
D^s_Σu_n ⇀* (∇_Σg−G)𝓗² + [g]⊗ν_g 𝓗¹⌞J_g.
```
I micro-salti degli approssimanti sono dunque essenziali in generale.

**Stato corretto.** Le stime geometriche strip/cap e i valori TV restano
calcoli sulla regolarizzazione continua. L'esistenza e la costruzione di
una vera determining sequence CF per la coppia C60 `(g,G)` restano aperte.
Vedere `docs/C60_CF_DETERMINING_SEQUENCE_AUDIT_2026-11-21.md` per la
derivazione, la riclassificazione energetica e il programma corretto.

## 2A. Determining sequence CF esplicita per la coppia corrente

Le definizioni faccia-per-faccia danno `∇_Σg|_f=G_f=B_fD_f` nella carta
ortonormale `B_f). Quindi `M=∇_Σg−G=0` a.e. La successione costante
`u_n=g` appartiene a `SBV(Σ;R³)`, converge a `g` in `L¹` e soddisfa
`∇_Σu_n𝓗²=G𝓗²` per ogni `n`. È pertanto una determining sequence nella
formulazione intrinseca sul complesso poliedrale. La dimostrazione dettagliata
e le conseguenze energetiche sono in
`theorems/C60_CF_DETERMINING_SEQUENCE_M0_2026-11-21.md`.

Questo risultato vale per la coppia corrente con `M=0`; non dimostra una
costruzione per un diverso campo bulk con `M≠0`. L'estensione del quadro
CF dal dominio euclideo alla superficie poliedrale è qui verificata
direttamente mediante la decomposizione SBV sulle facce e le tracce sugli
spigoli.

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
| Convergenza della regolarizzazione continua a `g` | **Da verificare integralmente**; non è una determining sequence CF per `(g,G)` |
| Contributo vertici `O(h)` | Stima candidata; le ipotesi sui pesi/carte vanno rese esplicite |
| Contributo strip TV | Stima numerica/candidata; quadratura non esaustiva |
| Immersione locale degli `g_h` | Numerico (σ_min > 0, margine piccolo) |
| Embeddedness globale | Sonda numerica positiva, non esaustiva |
| Criterio DPO completo per immersioni 2→3 | **Aperto** — serve formulazione dedicata |

Il gap residuo rispetto a una prova DPO completa: la formulazione classica
Del Piero–Owen è equidimensionale (`det` delle matrici quadrate); il caso
`G_f ∈ R^{3×2}` richiede una teoria per mappe tra varietà di dimensione
diversa — candidato naturale: formulare l'ammissibilità tramite la metrica
indotta `GᵀG` e l'energia di salto, non tramite `det`.
