# C60 — recovery generale isotropa: identità per `g∈SBV`, `G∈L^p`

Data: 2026-11-21
Classificazione: **dimostrata sul dominio piano limitato** (e per
il modello poliedrale intrinseco), modulo la citazione del teorema
di densità CFI. Il trasferimento a una superficie curva `Σ` resta
un passo separato (carte, metricha, salti inter-faccia).

## 1. Enunciato

Sia `Ω⊂ℝ²` aperto limitato con bordo Lipschitz, `g∈SBV(Ω;ℝ^m)` con
`∇g∈L¹` e `∫_{J_g}|[g]|d𝓗¹<∞`, e `G∈L^p(Ω;ℝ^{m×2})` con `p` tale
che il bulk sia definito (`p=1` per `W=|F|_F`; `p=2` per
`W=|F|_F²`). Allora, per `ψ(a,ν)=|a|` e `W` come sopra,

```
I_W(g,G) = ∫_Ω W(G)dx + ∫_Ω ‖∇g−G‖_* dx + ∫_{J_g}|[g]|d𝓗¹ .
```

## 2. Componenti

### 2.1 Limite inferiore — provato

Lemma §3.1 di `C60_CF_SBV_ISOTROPIC_THEOREM_2026-11-21.md`:
`liminf_n ∫_{J_{u_n}}|[u_n]| ≥ |μ|_* = ∫‖∇g−G‖_* + ∫_{J_g}|[g]|`,
più semicontinuità del bulk. Vale per qualunque successione
determinante con energia limitata.

### 2.2 Densità di `g` — CFI 2023/2025

Conti–Focardi–Iurlano, *Approximation of SBV functions with
possibly infinite jump set* (JFA 288, 110686, 2025; arXiv
2309.16557), Teorema 1.1 + Corollario 2.1: per `u∈SBV(Ω;ℝ^m)` con
`∇u∈L^p`, `p∈[1,∞)`, e `g_0(|[u]|)∈L¹(Ω;𝓗¹⌞J_u)` per `g_0`
continua, non decrescente, subadditiva, `g_0^{-1}(0)={0}` —
**scegliamo `g_0(t)=t`**, che soddisfa tutte le condizioni — esiste
`g_j` con:

- `g_j` **affine nell'interno di ogni simplesso** di una
decomposizione localmente finita; il suo salto è poliedrale;
- `g_j→g` in `L¹(Ω)`;
- `∇g_j→∇g` in `L^p(Ω)`;
- `∫_{J_{g_j}}|[g_j]|d𝓗¹ → ∫_{J_g}|[g]|d𝓗¹` (Cor. 2.1 con
  `g(a,ν)=|a|`, che verifica (H1)–(H3): simmetria, disuguaglianza
  triangolare con `g_0(t)=t`, `g(0,ν)=0`).

Le correzioni bilipschitz `Φ_j` del teorema sono assorbite dalle
loro stesse stime (Cor. 2.3): la convergenza energetica è enunciata
per `g_j` su `Ω`.

### 2.3 Approssimazione di `G` — costruzione standard

Sia `𝒯_j` la partizione in simplessi di `g_j`, ristretta a `Ω`:
finitamente molte celle (decomposizione localmente finita + `Ω`
limitato). Le celle che toccano `∂Ω` sono troncate — restano
poligoni, e l'affinità di `g_j` si preserva. Definiamo `G_j` come
**media di `G` su ogni cella** (proiezione a tratti costante):

```
G_j|_C := ⨍_C G dx .
```

Allora `G_j→G` fortemente in `L^p` (proprietà standard delle
proiezioni locali). La prova che la coppia `(g_j,G_j)` resta
ammissibile per il teorema poliedrale è nel §3.

### 2.4 Convergenza del funzionale candidato

```
|∫‖∇g_j−G_j‖_* − ∫‖∇g−G‖_*|
   ≤ C(‖∇g_j−∇g‖_{L¹} + ‖G_j−G‖_{L¹}) → 0
```

perché `‖·‖_*` è una norma (Lipschitz). Il bulk:
`∫W(G_j)→∫W(G)` per `W=|F|_F` da `G_j→G` in `L¹` (Lipschitz), e per
`W=|F|_F²` da `G_j→G` in `L²` (convergenza forte + crescità
quadratica). Il salto converge per CFI. Quindi
`ℱ(g_j,G_j)→ℱ(g,G)`.

### 2.5 Teorema poliedrale per `(g_j,G_j)` — provato

`C60_CF_POLYHEDRAL_AFFINE_THEOREM_2026-11-21.md` si applica:
`g_j` è affine su ogni cella del complesso (restrizione di affine
è affine), `G_j` è costante su ogni cella, i salti sono ammessi
(senza continuità). Consegna una recovery `u_{j,k}` con

```
u_{j,k} → g_j in L¹,
∇u_{j,k} 𝓗² ⇀* G_j 𝓗²   (convergenza debole-* delle misure),
limsup_k E_W(u_{j,k}) ≤ ℱ(g_j,G_j) .
```

(Nella costruzione SVD esplicita si ha anzi `∇u_{j,k}=G_j` a.e.,
ma la formulazione corretta e generale è la debole-*.)

### 2.6 Diagonale

Per ogni `j` scegliamo `k(j)` abbastanza grande da controllare
**simultaneamente**: l'errore `L¹` (`<1/j`), l'energia
(`≤ℱ(g_j,G_j)+1/j`) e un numero crescente di funzioni test per la
convergenza debole-* dei gradienti (famiglia densa in `C_c`). Allora

```
u_{j,k(j)} → g in L¹,
∇u_{j,k(j)} 𝓗² ⇀* G 𝓗²
```

perché `∇u_{j,k(j)}𝓗² ⇀* G_j𝓗²` per `k→∞` e `G_j→G` fortemente in
`L^p⊂L¹` ⇒ `G_j𝓗²→G𝓗²` in variazione. La successione diagonale è
quindi determinante per `(g,G)` nella topologia richiesta
(`L¹` + debole-* delle misure dei gradienti). Con `limsup E_W ≤
ℱ(g,G)` e il liminf di §2.1: uguaglianza. ∎

## 3. Verifica tecnica dei tre punti richiesti

**Punto 1 — il teorema poliedrale accetta le coppie `(g_j,G_j)`.**
Il teorema poliedrale (`C60_CF_POLYHEDRAL_AFFINE_THEOREM`) richiede:
`g` **affine su ogni cella** di un complesso poliedrale finito,
`G̃` **costante su ogni cella**, ammissibili `SBV` senza vincoli di
continuità. CFI fornisce `g_j` affine nell'interno di ogni
simplesso di una decomposizione localmente finita; su `Ω` limitato
le celle che intersecano `Ω` sono finite in numero, e le celle
troncate da `∂Ω` sono poligoni (l'affinità si preserva). I salti di
`g_j` sono concentrati sulle facce del complesso — la classe è
esattamente quella del teorema. `G_j` definito come media su ogni
cella è costante per cella. **Verificato.**

**Punto 2 — convergenza forte di `G_j` in `L^p`.** La proiezione
`G↦G_j` (media su cella) converge fortemente in `L^p` per ogni
`G∈L^p` purché il mesh tenda a zero: per funzioni continue vale
per stima uniforme, e per `G∈L^p` per densità + disuguaglianza di
Jensen (`⨍_C|G_j|^p ≤ ⨍_C|G|^p`). Il mesh delle partizioni CFI
tende a zero perché la scala di costruzione è `δ→0`, `ε→0` con
`ε≪δ` (Proposizione 4.1–4.3 del lavoro). La regolarità di forma
dei simplessi (diametro `<cε`, volume `>cεⁿ`) garantisce che le
celle troncate non degenerino. **Verificato** per `p=1,2`.

**Punto 3 — salti sulle giunzioni di faccia (solo per `Σ`).**
Sul dominio piano `Ω` non esistono giunzioni interne: `J_{g_j}` è
già il salto completo e CFI ne dà la convergenza. Su una superficie
poliedrale `Σ`, applicare CFI **singolarmente su ogni faccia**
non basta: i salti di `g` localizzati su `∂f` non sono interni a
nessuna faccia e la loro convergenza non è coperta dal teorema
euclideo applicato a `f`. Serve o una formulazione intrinseca di
CFI su `Σ`, o un argomento separato che includa i bordi di faccia
come dati al contorno con convergenza del costo — **questo resta
l'unico passo non dimostrato** per il caso C60.

## 3bis. Il punto contestato e la sua risoluzione

**Obiezione**: la raffinazione della mesh per `G_j` potrebbe
rompere la compatibilità richiesta dal teorema poliedrale.

**Risposta**: la restrizione di una funzione affine a un sotto-
complesso resta affine; le facce interne del raffinamento non
creano salti nuovi perché i valori delle celle adiacenti concordano
(sono la stessa funzione `g_j`). Il salto di `g_j` resta
identico, concentrato sulle facce del complesso originale. `G_j`
costante per cella raffinata è costante per cella — l'ipotesi del
teorema poliedrale è verbatim soddisfatta. Nessuna ipotesi
aggiuntiva serve.

## 4. Ipotesi finali del teorema

| Ipotesi | Uso |
|---|---|
| `Ω` limitato Lipschitz | CFI + proiezioni di `G` |
| `g∈SBV`, `∇g∈L¹`, `∫_{J_g}|[g]|<∞` | CFI con `g_0(t)=t` |
| `G∈L^p`, `p=1` (`W=|F|`) o `p=2` (`W=|F|²`) | convergenza bulk |
| `ψ=|a|`, `W` convessa con la crescita dichiarata | cell formula + semicontinuità |
| celle troncate a `∂Ω` | poligoni, affine preservata; i salti su `∂Ω` sono termine di bordo separato |

## 5. Cosa resta aperto

- **Superficie curva `Σ`**: CFI è euclideo. Su `Σ` serve
  applicazione faccia-per-faccia (ogni faccia è un poligono
  piano) più controllo dei salti sulle interfacce di faccia —
  la definizione intrinseca `SBV(Σ)` include quei salti e va
  mostrato che la decomposizione non li perde. **Questo è il
  passo residuo per C60.**
- **`ψ` anisotropo**: la densità CFI richiede `g` che verifichi
  (H1)–(H3); per `ψ` anisotropo la cell formula `g_ψ` è provata
  ma la recovery poliedrale eredita il teorema solo se la
  costruzione a strisce realises `ψ` — da verificare.
- **`|a|²`**: collassa sotto splitting, non rientra in `ψ=|a|`.
