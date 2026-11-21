# C60 — rilassamento banale per densità di salto superlineare: `ψ=|a|²` e generalizzazioni

Data: 2026-11-21. Dimostra l'estensione del teorema quadratico
(`C60_CF_QUADRATIC_JUMP_RELAXATION_2026-11-21.md`, che copriva solo
la coppia C60 con `M=0`) a `g∈SBV(Σ)` e `G∈L^p` generali,
`M=∇g−G` arbitrario. Include la generalizzazione a
`ψ(a,ν)=φ(|a|)` con `φ(t)/t→0` per `t→0`.

## 1. Enunciato

Sia `Σ` la superficie poliedrale (o un dominio piano — la prova è
la stessa). `g∈SBV(Σ;ℝ^m)`, `∇g∈L^p`, `∫_{J_g}|[g]|²<∞`;
`G∈L^p(Σ;Hom(TΣ,ℝ^m))`, `p=1` per `W=|·|_F`, `p=2` per
`W=|·|_F²`. Funzionale:

```
E(u) = ∫_Σ W(∇_Σu) d𝓗² + ∫_{J_u} |[u]|² d𝓗¹ .
```

**Teorema.** `I(g,G) := inf liminf E(u_n) = ∫_Σ W(G) d𝓗²`
sulle successioni determinanti (`u_n→g` in `L¹`,
`∇u_n𝓗²⇀*G𝓗²`).

**Idea**: la densità quadratica permette di micro-suddividere
*ogni* salto — quelli macroscopici di `g` e quelli della
staircase di mismatch — fino a costo nullo. Il funzionale
rilassato contiene **solo** il bulk.

## 2. Limite inferiore

`u_n→g` in `L¹`, `∇u_n𝓗²⇀*G𝓗²`, `sup_n E(u_n)<∞`.

- **Bulk**: per `W=|F|_F`, la convessità positivamente
  omogenea di grado 1 e la convergenza debole-* delle misure
  danno `liminf∫|∇u_n|≥∫|G|` (Reshetnyak). Per `W=|F|_F²`, il
  bound energetico dà `∇u_n` limitato in `L²`, quindi
  `∇u_n⇀G` debolmente in `L²` e la convessità di `|·|²` dà
  `liminf∫|∇u_n|²≥∫|G|²`.
- **Salto**: `∫_{J_{u_n}}|[u_n]|²≥0`.

Quindi `liminf E(u_n) ≥ ∫W(G)`. Nessuna ipotesi aggiuntiva.

## 3. Recovery: costruzione su una partizione affine comune

### 3.1 Prima approssimazione

Scegliamo `g_j` piecewise affine su una partizione poliedrale
finita (simplessi CFI) di `Σ`, con

```
g_j→g in L¹(Σ),   ∇g_j→∇g in L^p(Σ),
```

e `J_{g_j}` contenuto in un'unione finita di segmenti su cui
`[g_j]` è affine a tratti (proprietà di CFI). `G_j|_T=⨍_T G`
sulle stesse celle (G3): `G_j→G` in `L^p`. Raffiniamo a una
partizione poliedrale comune.

### 3.2 Splitting affine dei salti — `v_{j,m}` e lemma richiesto

Fissati `j,m`, applichiamo a ogni segmento di salto `e` la
costruzione a strati paralleli: striscia di larghezza `δ` nel
lato adiacente, `m` strati, nell'`i`-esimo
`v_{j,m}=g_j^-+(i/m)h_e` con `h_e` affine (v. §3.2 precedente
per i dettagli di coordinate, estremi `r`, palle `ρ` attorno ai
vertici del jump complex e disgiunzione delle strisce).

Il risultato deve soddisfare:

1. `v_{j,m}` affine su ogni cella di una partizione poliedrale
   finita `ℛ_{j,m}`;
2. `v_{j,m}→g_j` in `L¹` per `δ→0`;
3. salti sugli strati `≤C_e/m`, `C_e=‖[g_j]‖_{L∞(e)}`, a meno
   dei tratti terminali;
4. tratti terminali di lunghezza totale `≤c_e r`, salto `≤C_e`;
5. fuori dagli strati il salto è quello originario;
6. `∇v_{j,m}` costante per cella;
7. **controllo del gradiente nelle strisce**:
   `‖∇v_{j,m}‖_{L∞(strisce)} ≤ C_{j,e}` con `C_{j,e}`
   indipendente da `δ` e da `m` — nella costruzione a strati
   il valore cambia per **salti** fra strati adiacenti, non per
   transizioni continue, quindi
   `∇v_{j,m}=∇g_j^-+(i/m)∇h_e` resta limitato da
   `‖∇g_j‖+‖∇h_e‖`; di conseguenza
   `∫_{strisce}W(∇v_{j,m}) ≤ C·area(strisce)·sup W →0` per
   `δ→0`. (Una versione a transizione continua avrebbe
   `‖∇‖~1/δ` e non soddisfarebbe il lemma: la classe ammessa
   è quella piecewise-affine con salti, non i ramp.)

**Lemma di splitting — verifica (caso generico)**. Per un
segmento `e` interno a una faccia, con estremi non coincidenti
con altri segmenti di `J_{g_j}` e senza incroci:

- **Partizione**: la striscia `S(e)={dist(·,e)<δ_m}∩lato` è un
  rettangolo (in coordinate `(s,t)`); gli strati `S_i` sono
  rettangoli; le regioni terminali `s∉[r_m,|e|−r_m]` e le palle
  `B_{ρ_m}` attorno agli estremi di `e` sono poligoni (archi
  circolari sostituibili con poligoni senza cambiare le stime).
  Intersecando con la partizione CFI (dopo aver scelto `δ_m`
  minore della distanza di `e` dagli altri bordi di
  simplesso non contenenti `e`) si ottiene `ℛ_{j,m}` finita in
  poligoni. Proprietà 1, 6 ✓.
- **Affinità**: `h_e(s,t)=q_e(s)−g_j^-(s,t)` con `q_e`
  affine in `s` (traccia di `g_j^+` su `e`, costante in `t`) e
  `g_j^-` affine ⇒ `h_e` affine ⇒ `v_{j,m}=g_j^-+(i/m)h_e`
  affine su `S_i` ✓ (proprietà 1 nel dettaglio).
- **`v_{j,m}→g_j`**: le modifiche sono in `S(e)`, area
  `2δ_m|e|+O(ρ_m)`, e `|v_{j,m}−g_j|≤|h_e|≤C_e` ⇒ errore `L¹`
  `≤C_e·area→0` per `δ_m,ρ_m→0` ✓ (proprietà 2).
- **Salti**: sulle interfacce `t=−iδ_m/m` (`i=1,…,m−1`) e
  `t=−δ_m` il salto è `h_e/m` esattamente (differenza di
  coefficienti `1/m`); su `t=0` è `0` per `s∈[r_m,|e|−r_m]`.
  Ampiezza `≤C_e/m` ✓ (proprietà 3). Sui terminali `s` vicino
  agli estremi il coefficiente non è stratificato: salto
  `≤C_e`, lunghezza `≤2r_m+cδ_m` ✓ (proprietà 4). Fuori
  `S(e)∪terminali∪B_ρ` il valore è `g_j` ⇒ salto invariato
  ✓ (proprietà 5).
- **Gradiente**: `∇v_{j,m}=∇g_j^-+(i/m)∇h_e` in `S_i`,
  `|∇v|≤‖∇g_j‖+‖∇h_e‖≤C_{j,e}` uniforme in `i,m,δ`
  ✓ (proprietà 7).
- **Tracce**: su ogni bordo di cella le due tracce sono
  affini esplicite; il salto è la differenza — controllato
  punto per punto ✓.
- **Disgiunzione**: per `δ_m≪ r_m≪` distanza minima tra
  segmenti non incidenti e `ρ_m` piccola, le costruzioni su
  segmenti distinti non si sovrappongono; sui vertici del
  jump complex la palla `B_{ρ_m}` esclude ogni splitting e il
  salto resta quello di `g_j` — contributo `O(ρ_m·C_e)` nel
  conto (d) ✓.

**Casi residui** (dove la verifica va ripetuta, non cambia la
strategia): `e` che termina su `∂Σ` o su un vertice C60
(stessa costruzione, la palla `B_ρ` copre il vertice); `e`
condiviso da più di due celle (in C60 ogni spigolo ha due
facce, ma all'interno di una faccia i simplessi CFI possono
avere vertici multipli — la palla `B_ρ` attorno a ogni vertice
del jump complex li isola); `h_e` non limitata (impossibile:
`g_j` affine a tratti ⇒ `h_e` affine ⇒ limitata su `e` compatto).

**Stato**: lemma di splitting **dimostrato per la
configurazione generica** e le varianti elencate; la scrittura
formale completa (coordinate intrinseche su `Σ`, non solo
piane) è la parte tecnica residua — la metrica intrinseca è
piatta nelle facce e negli interni di spigolo, quindi le
coordinate `(s,t)` esistono localmente.

### 3.3 Partizione comune e staircase — `u_{j,m,h}`

Raffinando `ℛ_{j,m}` con la partizione di `G_j`, partizione
comune finita poliedrale `𝒫_{j,m}`. Su `P∈𝒫_{j,m}`:
`A_P=∇v_{j,m}|_P`, `G_P=G_j|_P`, `M_P=A_P−G_P` costanti;
SVD `M_P=Σ_iσ_{P,i}a_{P,i}⊗ν_{P,i}` e

```
u_{j,m,h}(x)=G_P x+b_P+Σ_iσ_{P,i}a_{P,i}h⌊x·ν_{P,i}/h⌋,
```

con `b_P` scelto per approssimare `v_{j,m}` (uguaglianza in un
punto di riferimento). Allora `∇u=G_P` a.e. in `P` e

```
‖u_{j,m,h}−v_{j,m}‖_{L∞(P)} ≤ c·h·max_P‖M_P‖_* =: c·h·C_{j,m}.
```

### 3.4 Stima dei salti per `φ=t²`

**(a) Interfacce degli strati**: salto `≤C_e/m+2chC_{j,m}`,
`m` segmenti di lunghezza `~|e|`:
`|e|m(C_e/m+2chC_{j,m})² = |e|(C_e²/m + O(hC_{j,m}) + O(mh²C²))`
→ per `m` fisso tutti i termini in `h` →0 (in particolare
`mh²→0` automaticamente); il termine `C_e²/m→0` per `m→∞`.

**(b) Lamine SVD**: salto `hσ_{P,i}`, lunghezza totale
`~|P|/h` ⇒ costo `~h·Σ_P|P|‖M_P‖_F² →0` per `h→0`, `(j,m)`
fisso.

**(c) Interfacce senza salto di `v_{j,m}`**: salto residuo
`≤2chC_{j,m}` ⇒ costo `→0` per `h→0`.

**(d) Tratti terminali e zone esclusae**: lunghezza `O(r+ρ)`,
salto `≤C_e` ⇒ costo `O((r+ρ)C_e²)→0`.

Le famiglie (a)–(d) vanno contate **senza sovrapposizioni**: il
lemma di splitting deve garantire la disgiunzione (estremi
`𝓗¹`-nulli).

### 3.5 Convergenze e diagonale

- `u_{j,m,h}→g` in `L¹`: `‖u−v_{j,m}‖∞≤chC_{j,m}→0` e
  `v_{j,m}→g_j→g`.
- `∇u_{j,m,h}=G_j` a.e. su ogni cella (la proprietà 7 del
  lemma garantisce che le strisce non creino gradienti
  non controllati: il bulk nelle strisce è `O(area)→0`);
  `G_j→G` in variazione totale ⇒
  `∇u_{j,m,h(j,m(j),r(j,m))}𝓗²⇀*G𝓗²`.
- **Bulk**: `∫W(∇u)=∫W(G_j)` a.e. + strisce
  `O(area·sup W)→0` per la proprietà 7 ⇒ `→∫W(G)` per
  `W=|·|_F` (`p=1`) o `|·|_F²` (`p=2`, `G∈L²`).
- **Salto**: (a)–(d) →0.

Ordine: per `j`, `m(j)` poi `r(j,m)` poi `h(j,m,r)` — `h` è
sempre scelto per ultimo, nessuna uniformità in `C_{j,m}`
richiesta.

**Stato**: dimostrato **modulo la verifica formale del lemma
di splitting** — che è ora verificato per la configurazione
generica (segmento interno a una faccia) e le varianti elencate
in §3.2; resta solo la scrittura intrinseca delle coordinate
`(s,t)` su `Σ` (tecnico, la metrica è piatta localmente).


## 4. Generalizzazione: `ψ(a,ν)=φ(|a|)` — ipotesi minime e verifica

**Ipotesi su `φ` (minime)**: `φ:[0,∞)→[0,∞)` **continua**,
`φ(0)=0`, e

```
φ(t)/t → 0   per t→0 .
```

Bastano e sono necessarie per *questo* meccanismo:

- **Continuità**: serve per stimare i costi di interfaccia
  residui `φ(C_e/m+O(h))→0` e per il limite superiore; la
  semicontinuità inferiore del termine salto non serve perché
  il termine è `≥0` e il lower bound usa solo il bulk.
- **`φ(0)=0`**: coerente con `ψ(0,ν)=0`.
- **`φ(t)/t→0`**: è esattamente la condizione perché lo
  splitting in `m` strati guadagni: `m·φ(C/m)=C·φ(C/m)/(C/m)→0`.
  Per `φ(t)=t` (crescita lineare) il meccanismo fallisce —
  coerente col caso isotropo.
- **Il verso conta**: `φ(t)=t^α` soddisfa l'ipotesi **solo per
  `α>1`** (allora `φ(t)/t=t^{α−1}→0`, `m·(C/m)^α=C^αm^{1−α}→0`,
  e il laminato dà `|P|h^{α−1}σ^α→0`). Per `0<α<1` si ha
  `φ(t)/t→∞`: il splitting *aumenta* il costo
  (`m^{1−α}→∞`) e il laminato diverge (`h^{α−1}→∞`) — ed `φ`
  è subadditiva (concava, `φ(0)=0`), quindi lo splitting non
  può comunque ridurre il costo: quel regime conserva il salto
  macroscopico ed è un problema diverso, non coperto qui.
- **Nessuna ipotesi di crescita né di convessità**: l'upper
  bound usa solo la costruzione; il lower bound non tocca `φ`.

### 4.1 Le tre stime, con uniformità esplicita

Fissati `(j,m)`: la partizione è **finita**, quindi

```
Σ_P := max_P max_i σ_{P,i} ≤ max_P ‖M_P‖_* =: C_{j,m} < ∞ .
```

La costante `C_{j,m}` dipende da `(j,m)` ma è finita; la
uniformità in `σ` **non** richiede un controllo di coda globale
perché la diagonale sceglie `h` *dopo* `(j,m)`: per ogni
`(j,m)` si prende `h` tale che `h·C_{j,m}` cada nell'intervallo
dove `φ(t)/t` è piccolo. Formalmente: data `ε>0`, esiste `η>0`
con `φ(t)/t<ε` per `t<η`; si sceglie `h<η/C_{j,m}`. Il sup su
celle e direzioni è così controllato — **non serve** ipotesi di
crescita su `φ` né equi-integrabilità dei `σ_P`.

- **(a) Micro-salti**: `m` interfacce per segmento `e`,
  ampiezza `≤C_e/m`, lunghezza `≤|e|`:
  `m·φ(C_e/m)·|e| = C_e|e|·[φ(C_e/m)/(C_e/m)]→0` per `m→∞`.
- **(b) Laminato**: lunghezza totale linee `~|P|/h` (coarea),
  ampiezza `hσ_i≤hC_{j,m}`:
  `costo = φ(hσ_i)·|P|/h ≤ |P|·C_{j,m}·[φ(hσ_i)/(hσ_i)]→0`
  per `h→0` con `(j,m)` fisso, uniformemente in `P,i`.
- **(c) Interfacce di cella**: ampiezza `≤C_e/m+2hC_{j,m}`:
  `Σ_e|e|·φ(C_e/m+2hC_{j,m})→0` per `m→∞` poi `h→0`,
  usando solo continuità di `φ` in `0`.

### 4.2 Convergenze (invarianti in `φ`)

- `u_{j,m,h}→g` in `L¹`: modifiche in strisce di area
  `O(δ_m)`, bound uniforme `hC_{j,m}` — ok.
- `∇u_{j,m,h}𝓗²⇀*G𝓗²`: `∇u=G_j` a.e. fuori strati + strati
  uniformemente limitati per `(j,m)` fisso + `G_j→G` in
  variazione totale — **non dipende da `φ`**.
- **Bulk**: `∫W(∇u)=∫W(G_j)` a.e. + correzione strati
  `O(δ_m)·sup|W|` — **non dipende da `φ`**.
- **Liminf**: `liminf E ≥ liminf∫W(∇u_n) + 0 ≥ ∫W(G)` —
  **non dipende da `φ`** (la semicontinuità del bulk basta).

### 4.3 Teorema finale

Per `φ` come sopra:

```
I_{W,φ}(g,G) = ∫_Σ W(G) d𝓗² .
```

La diagonale è a **tre livelli**: `j→∞` (CFI), `m(j)→∞`
(splitting), `h(j,m(j))→0` (staircase) — con `h` scelto dopo
`(j,m)` per il punto 4.1. ∎

## 5. Portata e caveat

- La prova non usa il lemma delle misure energetiche di §5.4:
  per `|a|²` il costo di salto →0 globalmente, quindi non serve
  controllo locale ai vertici — i contributi (a)–(c) sono finiti
  e globali. **G5 non è necessario per questo teorema.**
- Serve comunque la convergenza determinante: `∇u⇀*G` —
  ereditata dalla costruzione (G_j→G in variazione totale).
- Per `W=|F|²` serve `G∈L²` e il bound `∇u∈L²` uniforme:
  la costruzione dà `∇u=G_j` a.e. + strati uniformemente
  limitati per `(j,m)` fisso — ok nella diagonale.
- La generalizzazione `φ(t)/t→0` è **teorema con schema
  completo**; la verifica riga-per-riga delle stime (b)–(c)
  con costanti esplicite resta da incorporare — i conti sono
  quelli sopra, nessun nuovo ingrediente.
- Anisotropo `Φ(a)k(ν)` con `Φ^q`, `q>1`: stesso argomento con
  `Φ` al posto di `|·|` — ma richiede `k` separabile e la
  condizione `Φ(t·)/t→0`... `Φ(a)^q/t→0` in `a` — verificare.
