# C60 — studio delle estensioni: anisotropo, |a|², embeddedness

Data: 2026-11-21. Continuazione della PR #360. Convenzione:
prodotto dimostrato / candidato / aperto restano separati.

## 1. Densità di salto superlineare: `ψ(a,ν)=|a|²` (e generalizzazioni)

### 1.1 Il punto chiave

La costruzione delle sezioni 2–4 di
`C60_CF_QUADRATIC_JUMP_RELAXATION_2026-11-21.md` suddivide ogni
salto macroscopico in `m` micro-salti di ampiezza `|a|/m`: il
costo `m·(|a|/m)²·len = |a|²len/m → 0`. **Lo stesso argomento si
applica a qualunque salto di ampiezza piccola**, in particolare
ai salti della staircase di mismatch (`M≠0`): le linee di
laminato hanno ampiezza `hσ`, lunghezza `~|P|/h`, costo
quadratico totale `~hσ²|P|→0` senza bisogno di ulteriore
suddivisione.

### 1.2 Teorema (dimostrato, vedi `C60_CF_QUADRATIC_JUMP_GENERAL_2026-11-21.md`)

Sia `ψ(a,ν)=φ(|a|)` con `φ:[0,∞)→[0,∞)` continua,
`φ(0)=0`, `φ(t)/t→0` per `t→0` (es. `φ(t)=t^q`, `q>1`; include
`|a|²`). Allora, per `g∈SBV(Σ)`, `G∈L^p`, `W` convessa con
crescita `p`:

```
I_{W,φ}(g,G) = ∫_Σ W(G) d𝓗² .
```

**Nessun termine `‖∇g−G‖_*`, nessun termine `∫|[g]|`**: la
densità superlineare permette di far sparire *entrambi* i costi
interfaciali, incluso quello indotto dal disallineamento
bulk-disarrangement.

**Schema di prova.**

- *Liminf*: `∫W(∇u_n)⇀` dà `≥∫W(G)` per convessità; il termine
  `∫φ(|[u_n]|)≥0`. Quindi `liminf E ≥ ∫W(G)`.
- *Recovery*: (i) approssimare `g` con `g_j` piecewise-affine
  (CFI o qualsiasi densità, il costo di salto non serve);
  (ii) su ogni cella `P` applicare la staircase SVD per
  `M_P=A_P−G_j|_P` — costo bulk esatto `W(G_j|_P)`, salto
  `hσ→0` con costo `φ(hσ)·|P|/h = o(1)` per `φ(t)/t→0`;
  (iii) micro-suddividere ogni salto macroscopico `[g_j]` su
  `J_{g_j}` in `m(j)` strati — costo `→0` come in §2 del
  documento quadratico;
  (iv) diagonale `j,k(j),m(j)`: `u_n→g` in `L¹`,
  `∇u_n=G_j` a.e. sulle celle ⇒ `⇀*G`, bulk `→∫W(G)`, salto
  `→0`.

**Differenza dal caso `|a|`**: lì la densità era *lineare* in
`|a|` e il micro-splitting non guadagnava (`m·|a|/m=|a|`);
l'identità richiedeva il limite inferiore `‖M‖_*+|[g]|`. Qui la
superlinearità uccide tutto: il rilassamento è **banale**,
`I=∫W(G)`.

**Caveat**: la condizione `φ(t)/t→0` è anche *necessaria* per
questo meccanismo (per `φ(t)=t` il splitting non guadagna). Per
`φ` anisotropo in `a` (es. `Φ(a)^q`, `q>1`) lo stesso argomento
funziona con `Φ` al posto di `|·|`.

## 2. Densità anisotropa `ψ(a,ν)=Φ(a)k(ν)`

### 2.1 Cosa è provato

Dall'audit (§2): per `Φ` norma su `ℝ³`, `k` con `k(ν)=k(−ν)`:

- **Upper bound**: `C_{Φ,k}(M) ≤ min_{ONB{v₁,v₂}} [k(v₁)Φ(Mv₁)+
  k(v₂)Φ(Mv₂)]` (costruzione laminata a due famiglie).
- **Lower bound**: `C_{Φ,k}(M) ≥ sup_{Q∈Λ_{Φ,k}} Q:M` con
  `Λ_{Φ,k}={Q : Φ°(Qν)≤k(ν) ∀ν}` (dualità).
- **Uguaglianza: aperta.** Per `Φ=|·|`, `k≡1` coincide con
  `‖M‖_*` (provato). In generale il minimo laminato a due
  direzioni potrebbe non realizzare il cell formula rilassato:
  servono laminati di ordine superiore o il giusto inviluppo
  convesso/rank-1.

### 2.2 Il problema di cella corretto

Per la densità intermedia serve il **rilassamento** della
funzionale interfaccia sotto il vincolo bulk. Il candidato
naturale non è il minimo a due direzioni ma l'**inviluppo
convesso in `a`** della densità (per `ν` fisso) seguito dal
problema di ottimizzazione su `ν` — la teoria di rilassamento
delle energie interfaccia (cheljadin/Conti–Focardi per le
fratture) dice che il densità rilassata si ottiene con
laminati lungo le direzioni di Rank-1. Per `M∈ℝ^{3×2}`, le
connessioni di Rank-1 sono `M v⊗v` per ogni `v∈S¹`: il
reticolo delle direzioni è un cerchio, non solo due ONB.

**Congettura da verificare**: `C_{Φ,k}(M)` = inf su alberi di
laminati (o misure di Young) di `∫k(ν)Φ(a)dμ` soggetto a
`∫a⊗νdμ=M`. Il lower bound duale `sup Q:M` è il solito
candidato per l'inviluppo; l'uguaglianza upper=lower è il punto
duro.

### 2.3 Impatto sulla catena G1–G5

- **G1 (liminf)**: la norma `N` sulle misure va sostituita dal
  functional di variazione associato a `ψ`; il lower bound
  `≥∫C_{ψ}(dμ)` richiede la giusta dualità.
- **G2 (CFI)**: `g(a,ν)=Φ(a)k(ν)` è subadditiva in `a` se `Φ`
  è una norma e simmetrica se `k(ν)=k(−ν)`; `g_0` va scelta
  `≍Φ(|a|)` — verificabile, ma il teorema CFI usa `g_0` scalare:
  serve `g_0(t)≈sup_{|a|=t}Φ(a)k(ν)` uniforme in `ν`.
- **G4**: la giunzione non dipende dalla forma di `ψ` (il salto
  interfaccia è contato una volta); ok.
- **Teorema poliedrale**: la cell formula `C_{Φ,k}` deve
  *prima* essere identificata (problema §2.2) — è il collo di
  bottiglia.

## 3. Embeddedness / immersione

### 3.1 Formulazione

La superficie `Σ` è intrinsecamente immersa in `ℝ³` tramite `g`
(mappa al embedding/immersion). Si chiede che le recovery
`u_n` preservino una nozione di embeddedness. Tre livelli:

1. **Rank**: `rank ∇u_n = 2` a.e. — necessario perché `u_n`
   sia un'immersione.
2. **Immersione classica**: `u_n` immersione dove liscia.
3. **Embeddedness globale**: `u_n` iniettiva (o embedding
   misurato) su tutta `Σ`.

### 3.2 Cosa è noto

- Per `M` costante con `G̃=cA`, `A^TA=I₂` (isometria faccia):
  `∇u_h=G̃` a.e. ⇒ `rank=2` a.e. — **dimostrato**
  (`C60_CF_EXTENSIONS...` §3).
- Per `M(x)` variabile e `g_j` piecewise-affine con `G_j` medie
  cella: `∇u_{j,k}=G_j` a.e. ⇒ `rank ∇u_{j,k}=rank G_j` a.e.
  **Problema**: `G_j=⨍_T G` può perdere rango — la media di due
  mappe iniettive può essere singolare. Per il C60 originale
  (`G` isometria costante per faccia) le medie restano isometrie;
  per `G` variabile serve un'ipotesi `rank G≥2` *stabile per
  medie* o una costruzione che la preservi (es. medie in
  coordinate rispetto a una base di `G`).

### 3.3 Le difficoltà reali

- **Injectivity**: gli `u_n` hanno salti; l'iniettività va
  definita fuori da `J_{u_n}` o in senso misurato. La
  perturbazione `h‖M‖` è `C⁰`-piccola per `h` piccolo: se `g`
  è un embedding bilipschitz, `u_n` ristretta alle celle è
  vicina a `g_j` che è vicina a `g` — l'iniettività *locale*
  segue per `h` piccolo, ma **globalmente** due punti lontani
  possono avvicinarsi; serve un'ipotesi di separazione di `g`
  (es. `g` embedding con tubular neighborhood) e un controllo
  uniforme del diametro delle celle.
- **Salti**: un salto crea due "fogli" che possono intersecare
  altre parti della superficie — va escluso o controllato.
- **Topologia**: `Σ` chiusa (sfera topologica); un'immersione
  `S²→ℝ³` esiste, ma l'*embedding* richiede di evitare
  auto-intersezioni globali — problema genuinamente globale,
  non locale.

### 3.4 Classificazione

- rank-2 a.e. per `G` costante isometrico: **dimostrato**.
- rank-2 per `G` variabile: **aperto** (medie cella possono
  degenerare).
- immersione/embedding globale: **aperto** — richiede un
  framework (misure di immersione, nozioni di convergence) che
  il modello attuale non ha.

## 4. Sintesi

| Estensione | Stato | Prossimo passo |
|---|---|---|
| `ψ=φ(|a|)`, `φ(t)/t→0` (incl. `\|a\|²`) | **Teorema candidato, schema completo** | Scrivere la prova formale (estende §2 del doc quadratico a `M≠0` e `g` generale) |
| `ψ=Φ(a)k(ν)` separabile | Cell formula **aperta** | Dimostrare `min ONB = sup duale` o trovare il cell formula corretto (laminati/convex envelope) |
| `ψ` anisotropo generale | Aperto | Dopo il separabile: estendere la dualità |
| Embeddedness rank-2 | Parziale (caso isometrico costante) | Ipotesi di stabilità di rango per le medie cella |
| Embeddedness globale | Aperto | Definire la nozione e il framework di convergenza |
