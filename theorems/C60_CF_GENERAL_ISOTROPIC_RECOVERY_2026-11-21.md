# C60 — recovery generale isotropa: identità per `g∈SBV`, `G∈L^p`

Data: 2026-11-21
Classificazione: **dimostrata sul dominio piano limitato** (e per
il modello poliedrale intrinseco), modulo la citazione del teorema
di densità CFI. Il trasferimento a una superficie curva `Σ` resta
un passo separato (carte, metricha, salti inter-faccia).

## 1. Enunciato

Sia `Ω⊂ℝ²` aperto limitato con bordo Lipschitz, `g∈SBV(Ω;ℝ^m)` con
`∇g∈L^p` e `∫_{J_g}|[g]|d𝓗¹<∞`, e `G∈L^p(Ω;ℝ^{m×2})` con `p` tale
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
### 2.3 Approssimazione di G — medie sulle simplici CFI

Sia \(\mathcal T_j\) la decomposizione localmente finita di
\(\mathbb R^2\) in simplessi fornita da CFI. Poiché
\(\overline\Omega\) è compatta e la decomposizione è localmente
finita in tutto \(\mathbb R^2\), solo un numero finito di
simplessi interseca \(\overline\Omega\). Le celle del complesso
su \(\Omega\) sono le intersezioni \(T\cap\Omega\), poligonali;
la restrizione di \(g_j\) resta affine.

Per evitare problemi di celle tagliate molto sottili sul bordo,
non si calcolano le medie sulle intersezioni \(T\cap\Omega\).
Si estende invece \(G\) con zero a \(\widetilde G\) su
\(\mathbb R^2\) e si definisce, per ogni simplesso completo T,

```
G_j|_{T∩Ω} := (1/|T|) ∫_T G̃ dx .
```

Le simplici CFI hanno diametro \(\le c\varepsilon_j\),
volume \(\ge c\varepsilon_j^2\), e sovrapposizione uniformemente
limitata. Le medie sulle celle complete sono quindi stabili in
\(L^p\); per densità delle funzioni continue e diametro tendente
a zero, \(G_j\to G\) fortemente in \(L^p(\Omega)\), per
\(p=1,2\). Le intersezioni con il bordo non alterano la stima,
perché il valore assegnato è la media sulla simplex completa e
la restrizione cambia soltanto il dominio su cui il campo costante
è letto. Ne segue anche
\(\|G_j\mathcal H^2-G\mathcal H^2\|_{\mathcal M}
=\|G_j-G\|_{L^1}\to0\).

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


**G4b — RECOVERY MICROSCOPICA SU CELLE CON SALTI INTERNI (CHIUSO).**
Il teorema poliedrale è stato esteso esplicitamente alla partizione
poliedrale finita fornita dalla densità CFI: su ogni cella T, g_j è
affine e G_j è costante, ma non si impone continuità tra celle.
La stima uniforme fino a T̄ è
||v_{h,T}−g_j|T||_{L∞(T̄)}≤h||A_T−G_T||_*.
Su ogni interfaccia e=T⁻∩T⁺ ciò implica
||[v_h]−[g_j]||_{L¹(e)}
≤h H¹(e)(||A_{T⁻}−G_{T⁻}||_*+||A_{T⁺}−G_{T⁺}||_*).
Per la partizione fissata la somma degli errori è h C_j, con C_j
finita e indipendente da h. Non si assume C_j uniformemente limitata
al variare di j: nella diagonale si sceglie h_j in modo che
h_j C_j≤1/j. Questo controlla anche i salti macroscopici interni,
senza raccordi e senza cancellarli. Si veda §2bis di
C60_CF_POLYHEDRAL_AFFINE_THEOREM_2026-11-21.md.

### 2.6 Diagonale (formulazione esplicita)

Per ogni `j`, sia `(u_{j,k})_{k∈ℕ}` la successione di recovery del
teorema poliedrale per `(g_j,G_j)`. La convergenza garantita è

```
u_{j,k} → g_j in L¹(Ω),
∇u_{j,k} 𝓗² ⇀* G_j 𝓗²   in M(Ω;ℝ^{m×2})  (k→∞),
limsup_k E_W(u_{j,k}) ≤ ℱ(g_j,G_j) .
```

Le misure `∇u_{j,k}𝓗²` vivono in `M(Ω;ℝ^{m×2})`, il duale di
`C_0(Ω;ℝ^{m×2})` — o `C(Ω̄)` se si preferisce topologia debole
contro test continue. Sia `(φ_m)_{m≥1}` una famiglia densa
numerabile di funzioni test in quella topologia (esistono per la
separabilità di `C_0`). Per ogni `j` scegliamo `k(j)` abbastanza
grande da imporre **simultaneamente**:

```
‖u_{j,k(j)} − g_j‖_{L¹} < 1/j,
E_W(u_{j,k(j)}) ≤ ℱ(g_j,G_j) + 1/j,
|∫_Ω φ_m : d(∇u_{j,k(j)}𝓗² − G_j𝓗²)| < 1/j   per m = 1,…,j .
```

Se la nozione di convergenza o il teorema richiedono ulteriori
test o vincoli (ad es. vincoli al bordo), vanno inclusi nella stessa
scelta.

**Convergenza della diagonale.** Poiché `g_j→g` in `L¹`:
`u_{j,k(j)}→g` in `L¹`. Per la debole-*:

- per `k→∞` a `j` fisso, `∇u_{j,k}𝓗² ⇀* G_j𝓗²`;
- per `j→∞`, `G_j→G` fortemente in `L^p ⊂ L¹` ⇒
  `G_j𝓗² → G𝓗²` in variazione ⇒ `G_j𝓗² ⇀* G𝓗²`.

La stima diagonale sugli `m≤j` test, unita alla densità di
`(φ_m)` e alla limitatezza uniforme delle misure, dà
`∇u_{j,k(j)}𝓗² ⇀* G𝓗²`. La successione è quindi determinante per
`(g,G)` nella topologia `L¹` + debole-* delle misure dei
gradienti. Con `limsup E_W(u_{j,k(j)}) ≤ lim_j ℱ(g_j,G_j) =
ℱ(g,G)` e il liminf di §2.1: **uguaglianza**. ∎

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
tende a zero: la costruzione ha due scale `δ` (regolarità di `u`)
e `ε≪δ` (triangolazione fine), e i simplessi hanno diametro
`≤ cε` con `ε↓0` lungo la successione (Prop. 4.1–4.3, §4.3 del
lavoro). La regolarità di forma (diametro `<cε`, volume
`>cεⁿ`) impedisce il degenerare delle celle troncate. **Verificato**
per `p=1,2`. Conseguenza ulteriore: `‖G_j𝓗²−G𝓗²‖_M =
‖G_j−G‖_{L¹}→0` — convergenza in variazione totale, più forte
della debole-* richiesta.

**Punto 3 — salti sulle giunzioni di faccia (per Σ).**
CFI si applica separatamente all'interno di ciascuna faccia. Il
Corollario 2.3 dà convergenza stretta BV; il teorema di continuità
della traccia dà convergenza forte L¹ sulle frontiere delle facce.
Quindi i salti tra facce convergono in L¹ sugli spigoli e il loro
costo converge. Non occorre una versione intrinseca di CFI né
strisce di raccordo. La recovery microscopica sulle celle, inclusi
i salti interni, è trattata da G4b (§2bis del teorema poliedrale).

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
| `g∈SBV`, `∇g∈L^p`, `∫_{J_g}|[g]|<∞` | CFI con `g_0(t)=t` |
| `G∈L^p`, `p=1` (`W=|F|`) o `p=2` (`W=|F|²`) | convergenza bulk |
| `ψ=|a|`, `W` convessa con la crescita dichiarata | cell formula + semicontinuità |
| celle troncate a `∂Ω` | poligoni, affine preservata; i salti su `∂Ω` sono termine di bordo separato |

## 5. Ipotesi CFI — verifica per il caso piano e per C60

### 5.1 Caso piano `Ω` — verificato

| Ipotesi CFI (Thm 1.1) | Verifica |
|---|---|
| `Ω` aperto limitato, bordo Lipschitz | **ok** per poligoni (facce C60: esagoni/pentagoni convessi) |
| `g∈SBV(Ω;ℝ^m)` | ipotesi del teorema |
| `∇g∈L^p`, `p∈[1,∞)` | `p=1` per `W=|F|_F`; `p=2` per `W=|F|_F²` con `G∈L²` |
| `g_0(|[g]|)∈L¹(J_g)`, `g_0(t)=t` | equivalente a `∫_{J_g}|[g]|d𝓗¹<∞` — ipotesi del teorema |
| `g(a,ν)=|a|` verifica (H1)–(H3) | simmetria `|-a|=|a|`; `|s+s'|≤|s|+|s'|` con `g_0(t)=t`; `g(0,ν)=0` |

Tutti i requisiti sono soddisfatti sotto le ipotesi dichiarate
dell'enunciato: **il caso piano è chiuso**.


### G4b e G5 — aggiornamento della recovery globale (2026-11-21)

**G4b è chiuso** per dati piecewise-affine su partizione poliedrale
finita, inclusi i salti interni. Per ogni partizione fissata, la
somma degli errori di traccia sulle interfacce è al più h C_j,
con C_j finita e indipendente dal parametro microscopico h. La
diagonale sceglie h_j C_j≤1/j; non è richiesta uniformità di C_j
rispetto all'indice esterno j. La dimostrazione è in §2bis di
C60_CF_POLYHEDRAL_AFFINE_THEOREM_2026-11-21.md.

**G5 è chiuso per la recovery globale su partizioni poliedrali
finite**, senza riempimento separato dei dischi conici. Per j
fissato, la misura energetica della recovery SVD converge
debolmente-* alla misura candidata Λ_j: il bulk è esatto; i
micro-salti convergono localmente alla densità nucleare per coarea
e somme di Riemann; i salti sulle interfacce convergono per la
stima uniforme delle tracce. La convergenza CFI stretta in BV
sulle facce, insieme alla convergenza delle tracce sugli spigoli,
dà la convergenza debole-* delle misure di salto macroscopiche.
Le densità bulk e mismatch convergono in L¹ (in L² per il bulk
quadratico). La diagonale produce quindi Λ_j,h_j ⇀* Λ.

La misura limite Λ non ha atomi nei vertici: le parti bulk sono
assolutamente continue rispetto a H² e la parte di salto è
assolutamente continua rispetto a H¹. Perciò
Λ(B_r(v))→0. La convergenza delle misure energetiche, prima sui
raggi di continuità e poi per monotonia sui raggi arbitrari,
implica che l'energia della recovery nei dischi tende a zero.
La stima è più forte del solo controllo del residuo richiesto da
G5. Dettagli, lemma locale e ordine dei limiti sono in §5.4 di
C60_CF_POLYHEDRAL_GENERAL_RECOVERY_2026-11-21.md.

**Limite della conclusione:** non è dimostrato un lemma astratto
di riempimento con traccia assegnata sul bordo di un disco conico.
Non serve per la recovery globale qui costruita.

### 5.2 Superficie Σ — giunzione e vertici

La giunzione sugli spigoli è chiusa: CFI Cor. 2.3 dà convergenza
stretta BV su ogni faccia e la continuità della traccia dà
convergenza L¹ sui lati; G4b estende la recovery SVD alle celle
piecewise-affine con salti interni. Non sono necessarie strisce di
raccordo.

Anche il controllo dei vertici è chiuso per la recovery globale:
la misura energetica converge debolmente-* alla misura candidata,
che non ha atomi nei vertici. Ne segue che l'energia nei dischi
intrinseci B_r(v) tende a zero. La dimostrazione completa e la
distinzione rispetto al problema separato di riempimento con
traccia prescritta sono in §5.4 di
C60_CF_POLYHEDRAL_GENERAL_RECOVERY_2026-11-21.md.

**Nota su Kristensen–Rindler** (arXiv:1211.1792): il Teorema 1
controlla tutti i bordi del mesh e preserva esattamente la traccia
sul bordo del dominio; è un riferimento per le interfacce, ma la
costruzione globale in W¹,¹ non sostituisce la separazione
bulk/salto fornita da CFI.

### 5.3 Fuori scope

- `ψ` anisotropo: la cell formula `g_ψ` è provata senza vincolo di
  bordo, ma la recovery poliedrale con `ψ` richiede la
  realizzazione a strisce della densità — non verificata.
- `ψ(a,ν)=|a|²`: collassa sotto splitting; non rientra in (H1)–(H3)
  con `g_0` subadditiva (serve `g_0(t)~t²`, non subadditiva) —
  il teorema CFI **non** si applica.
- Embeddedness/DPO: indipendente, resta aperto.
