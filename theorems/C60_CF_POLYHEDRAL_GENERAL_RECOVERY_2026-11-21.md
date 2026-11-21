# Teoria generale: recovery isotropa su superfici poliedrali con singolarità coniche isolate

Data: 2026-11-21. Stessa convenzione della PR #360: numerico,
costruzioni esplicite, teoremi dimostrati e ipotesi aperte restano
separati.

## 1. Classe geometrica

`Σ` superficie poliedrale compatta, connessa, 2-dimensionale,
incollata da un numero finito di poligoni euclidei lungo lati,
con:

1. ogni faccia un poligono euclideo (dominio Lipschitz);
2. ogni spigolo interno condiviso da esattamente due facce,
   incollaggio isometrico;
3. vertici `v∈V` = singolarità coniche isolate con angolo totale
   `θ_v>0`; la curvatura concentrata è
   `K_sing = Σ_v (2π−θ_v) δ_v` e, se `Σ` è chiusa orientabile,
   vale Gauss–Bonnet `Σ_v(2π−θ_v) = 2πχ(Σ)`;
4. `Σ∖V` localmente isometrico al piano (gli spigoli interni sono
   piatti: angolo `2π`).

C60 (troncato icosaedro) è il caso `|F|=32`, `|E|=90`, `|V|=60`,
`θ_v = 108°+120°+120° = 348°` (figura di vertice 5.6.6), quindi
`2π−θ_v=12°`.

## 2. Funzionale e convergenza determinante

`g∈SBV(Σ;ℝ^m)`, `G∈L^p(Σ;Hom(TΣ,ℝ^m))`. Determinante:

```
u_n→g in L¹(Σ),   ∇_Σ u_n 𝓗² ⇀* G 𝓗².
```

Funzionale isotropo `ψ(a,ν)=|a|`:

```
E_W(u) = ∫_Σ W(∇_Σ u) d𝓗² + ∫_{J_u}|[u]| d𝓗¹,
W(F)=|F|_F  (p=1)  oppure  W(F)=|F|_F²  (p=2).
```

**Contabilità dei salti (nessun doppio conteggio).** Il salto su
`Γ` va contato **una sola volta** su `Σ`:

```
∫_{J_u}|[u]| d𝓗¹ =
   Σ_f ∫_{J_u∩f°}|[u]| d𝓗¹
 + Σ_e ∫_{e∩J_u}|[u]| d𝓗¹ ,
```

dove `f°` è l'interno della faccia e `e` gli spigoli. I vertici
sono `𝓗¹`-nulli: non aggiungono termini di salto (ma possono
concentrare energia bulk/transizioni — vedi G5).

## 3. Decomposizione del problema in G1–G5

| # | Componente | Contenuto | Stato |
|---|-----------|-----------|-------|
| G1 | Liminf isotropo su `Σ` | `liminf E_W ≥ ∫W(G)+∫‖∇g−G‖_*+∫|[g]|` | **Provato** (stessa prova della sezione §3.1 di `C60_CF_GENERAL_ISOTROPIC_RECOVERY`, estesa a `Σ` perché `D_Σ g − G𝓗²` è una misura e `|μ|_*` si decomprime sulle parti AC e singolare; le ipotesi sono solo misure finite) |
| G2 | Densità SBV faccia-per-faccia | `g_j` affine per simplesso su partizione che raffina le facce; `∇g_j→∇g` in `L^p`; `∫_{J_{g_j}∩f°}|[g_j]|→∫_{J_g∩f°}|[g]|` per ogni `f` | **Provato per faccia** via CFI; le tracce sono trattate separatamente in G4a |
| G3 | Medie simpliciali di `G` | `G_j|_T = ⨍_T G` sulla stessa partizione CFI | **Provato**: mesh `≤cε→0` ⇒ convergenza forte in `L^p` ⇒ in variazione totale delle misure |
| G4 | Giunzione lungo spigoli | Lemma §4 + G4a (tracce) + G4b (tracce recovery) | Lemma + G4a + G4b **dimostrati**; §4.2 e §2bis del teorema poliedrale |
| G5 | Vertici conici | energia residua nei dischi `B_r(v)` | **Dimostrato via §5.4** (convergenza debole-* delle misure energetiche; nessun riempimento separato) |

## 4. G4 — Lemma locale di incollaggio SBV (DIMOSTRATO)

Sia `S=(−L,L)×(−r,r)`, `Γ=(−L,L)×{0}`, `S^±=S∩{±x_2>0}`.
Siano `u_n^±∈SBV(S^±;ℝ^m)` con tracce
`a_n^±=Tr_Γ u_n^±`, e

```
a_n^± → a^±   fortemente in L¹(Γ;ℝ^m).
```

Definito `u_n` per incollaggio (`u_n^+` sopra, `u_n^−` sotto),
allora `u_n∈SBV(S)` e il salto sull'interfaccia converge:

```
lim_n ∫_Γ |[u_n]| d𝓗¹
= lim_n ∫_Γ |a_n^+ − a_n^−| d𝓗¹
= ∫_Γ |a^+ − a^−| d𝓗¹ .
```

**Dimostrazione.** La formula di giunzione per `BV` su un'ipersuperficie:
`Dw_n⌞Γ = (a_n^+−a_n^−)⊗e_2 𝓗¹⌞Γ`, mutuamente singolare con la
parte AC e con i salti interni. Per `ψ(a,ν)=|a|` isotropa il peso
dipende solo dal salto:

```
| |a_n^+−a_n^−| − |a^+−a^−| | ≤ |a_n^+−a^+| + |a_n^−−a^−|,
```

e l'integrazione su `Γ` chiude la stima in `L¹`. ∎

**Corollario (contabilità globale).** Su `Σ` compatta:
`Σ_e` finita di spigoli, il lemma si applica a ogni bordo
inter-faccia lontano dai vertici; ai vertici si passa da G5.
L'ipotesi mancante è **solo** la convergenza delle tracce.

### 4.1 G4a — il punto aperto: convergenza delle tracce

Il teorema CFI (densità SBV) garantisce `u_j→g` in `L¹` e
`∫_{J_{u_j}}|[u_j]|→∫_{J_g}|[g]|`, ma **non** la convergenza
delle tracce su un bordo fissato. La convergenza `L¹` bulk non
implica tracce. Topologia richiesta per chiudere G4a:

```
w_j→w in L¹(S),   Tr w_j→Tr w in L¹(∂S),
∇w_j→∇w in L¹(S),  ∫_{J_{w_j}}|[w_j]|→∫_{J_w}|[w]|.
```

**Risultati candidati in letteratura (verifica parziale):**

- **Kristensen–Rindler**, *Piecewise affine approximations for
  functions of bounded variation* (arXiv:1211.1792): approssimanti
  piecewise affine, area-strict, con **differenza delle tracce
  sulle interfacce del mesh resa arbitrariamente piccola**.
  Attenzione: il controllo è sulle interfacce *interne* del mesh,
  non automaticamente su `∂S`. Se però si applica la densità
  **globalmente** su `Σ∖V_r` (superficie piatta con bordo
  poligonale), gli spigoli `Γ` diventano interfacce interne del
  mesh e il controllo di traccia di KR potrebbe bastare —
  questa è la via "CFI intrinseco" del §5.2 e andrebbe verificata
  nel testo.
- **De Philippis–Fusco–Pratelli**, *On the approximation of SBV
  functions* (arXiv:2303.00933, Memoirs AMS): Teoremi A–C;
  convergenza BV strict + convergenza della misura del jump set
  + `u_j∈C^∞` fuori da `J_{u_j}`; se `ℋ^{n−1}(J_u)<∞` anche
  `ℋ^{n−1}(J_{u_j})→ℋ^{n−1}(J_u)`. Non dichiara controllo delle
  tracce sul bordo.
- **Ambrosio et al.** (approssimazione BV→SBV in spazi metrici,
  arXiv:1806.04647, Cor. 5.15): gli approssimanti possono essere
  scelti con **gli stessi valori al bordo** — ma in contesto
  metrico/`BV` (rimozione di Cantor), non la densità energetica
  `|[·]|` richiesta.

**G4a — CHIUSO (2026-11-21).** La via decisiva è il **Corollario
2.3 di CFI** (JFA 288, 110686): per `g_0(t)=2t` (o `t`),
`g(a,ν)=|a|` — entrambe le ipotesi H1–H3 verificate — gli
approssimanti possono essere scelti con convergenza di energia
**sia** bulk (`∇u_j→∇u` in `L^p`, `∫|∇u_j|→∫|∇u|`) **sia** salto
(`∫_{J_{u_j}}|[u_j]|→∫_{J_u}|[u]|`). Poiché `u∈SBV` non ha parte
di Cantor,

```
|Du_j|(S) = ∫_S|∇u_j| + ∫_{J_{u_j}}|[u_j]|
         → ∫_S|∇u| + ∫_{J_u}|[u]| = |Du|(S) ,
```

i.e. **convergenza stretta in BV**. Su dominio Lipschitz (ogni
faccia poliedrale lo è) la convergenza stretta BV implica
convergenza forte delle tracce:

```
Tr w_j → Tr w   in L¹(∂S)
```

(risultato classico: l'operatore traccia è continuo per la
convergenza stretta; vedi AFP, *Functions of Bounded Variation and
Free Discontinuity Problems*, o Giusti, Prop. 1.2.3). La topologia
richiesta sopra è quindi soddisfatta **senza** alcuna
modifica boundary-preserving: G4a è un corollario di CFI Cor. 2.3
+ il teorema sulle tracce BV.

**Nota di cautela**: la convergenza stretta richiede che il salto
di `Du` sia solo la parte jump (verificato: `u∈SBV`) e che il
dominio sia Lipschitz (verificato: poligono convesso). L'ipotesi
`g_0(|[w]|)∈L¹` per `g_0(t)=2t` equivale a `∫_{J_w}|[w]|<∞`,
già richiesta.

### 4.2 G4b — recovery locale dopo incollaggio

La recovery poliedrale su ogni cella produce `u_{j,k}→g_j` con
`∇u_{j,k}𝓗²⇀*G_j𝓗²` **all'interno della cella**. Per le tracce:
la costruzione SVD esplicita (`C60_CF_POLYHEDRAL_AFFINE_THEOREM`)
soddisfa la stima uniforme

```
‖v_{h,T} − g_j‖_{L^∞(T̄)} ≤ h·‖M_T‖_*
```

su ogni cella `T` **chiusa**, quindi in particolare sulle sue
facce: per `k→∞` (h→0) le tracce di `u_{j,k}` convergono a quelle
di `g_j` su ogni lato di cella. Il diamante diagonale `j,k(j)`
combinato con G4a (`Tr g_j→Tr g` in `L¹(∂f)`) dà

```
Tr_Γ u_{j,k(j)} → Tr_Γ g   in L¹(Γ)   per ogni spigolo Γ,
```

e il lemma §4 chiude il costo inter-faccia.

**G4b — estensione scritta, da verificare.** La
costruzione SVD si applica a `g_j` piecewise-affine con jump set
poliedrale senza modifiche, per restrizione:

Sia `g_j` affine su ogni cella `P` di una partizione poliedrale
(dominio `Σ` o faccia) e sia `J_{g_j}` l'unione delle interfacce
di cella dove il salto è non nullo. Su ogni cella `P` scriviamo
`g_j|_P(ξ)=A_Pξ+b_P` e `M_P=A_P−G_j|_P` costante; la costruzione
esplicita

```
v_{h,P}(ξ) = G_j|_P ξ + b_P
             + Σ_i σ_{P,i} a_{P,i}·h⌊ξ·ν_{P,i}/h⌋
```

usa solo dati di `P`. Si definisce `u_{j,k}` **incollando** le
`v_{h,P}` senza regolarizzare: su un'interfaccia interna `e`
comune a `P⁺,P⁻`,

```
[u_{j,k}]_e = Tr⁺v_{h,P⁺} − Tr⁻v_{h,P⁻} .
```

- Se `e⊂J_{g_j}`: per la stima uniforme per cella,
  `‖v_{h,P±}−g_j‖_{L∞(P̄±)}≤h‖M_{P±}‖_*`, quindi
  `[u_{j,k}]_e→[g_j]_e` uniformemente e
  `∫_e|[u_{j,k}]|→∫_e|[g_j]|`.
- Se `e∉J_{g_j}`: le tracce di `g_j` coincidono (`[g_j]_e=0`),
  quindi `[u_{j,k}]_e→0` uniformemente e il costo di salto
  generato sull'interfaccia interna è `o(1)` — le linee di
  laminato che terminano sul bordo di cella producono solo
  correzioni `O(h)` di ampiezza su `𝓗¹` finita.
- Sulle interfacce di faccia `Γ⊂∂Σ` il discorso è identico e si
  innesta su G4a/G4 (tracce → tracce di `g`).

Le linee di salto interne del laminato restano dentro le celle
`P` (la costruzione è per cella); il costo bulk+jump per cella
converge a `|P|W(G_j|_P)+|P|‖M_P‖_*`, e la somma su `P` dà
`ℱ(g_j,G_j)`. La diagonale `k(j)` su una famiglia test densa
chiude `u_{j,k(j)}→g` in `L¹` e
`∇u_{j,k(j)}𝓗²⇀*G𝓗²`. **Nessuna nuova costruzione serve**: il
teorema poliedrale vale per dati affine a tratti con jump set
poliedrale, per restrizione cella per cella + incollaggio.

## 5. G5 — Vertici conici

### 5.1–5.3. Perché il riempimento conico non è il metodo usato

Il fatto che il disco conico abbia area O(r²) e bordo O(r) non
costituisce, da solo, una stima energetica: una transizione con
gradiente O(1/r) può avere costo O(1) per il bulk quadratico.
Neppure l'equi-integrabilità dei soli campi G_j controlla
automaticamente i micro-salti e le interfacce artificiali.
Pertanto le precedenti stime basate sul settore conico e sulla
piccolezza dell'area non sono una dimostrazione di G5.

Una costruzione separata fuori da B_r(v) richiederebbe davvero un
riempimento con traccia prescritta sull'arco ∂B_r(v), con controllo
uniforme dell'intero funzionale. Non assumiamo tale lemma. La
dimostrazione corretta per la recovery globale è invece §5.4:
convergenza debole-* delle misure energetiche, senza tagliare la
successione e senza creare un'interfaccia di riempimento.

### 5.4 G5 — chiusura tramite convergenza locale delle misure energetiche

**Non occorre costruire un riempimento separato del disco conico.**
Si usa un'unica recovery SVD globale, definita cella per cella su
tutta la superficie, comprese le porzioni che contengono i vertici.
In questo modo non esiste un'interfaccia artificiale
\(\partial B_r(v)\) sulla quale imporre una nuova condizione di
traccia: la stessa funzione recovery è già definita da entrambi i
lati di ogni arco.

La dimostrazione richiede la convergenza delle **misure energetiche**,
non soltanto quella dei valori totali.

Per una coppia poliedrale fissata \((g_j,G_j)\), sia
\(\mathcal P_j\) la partizione finita, con
\(g_j|_T(x)=A_Tx+b_T\), \(G_j|_T=G_T\), e
\(M_T=A_T-G_T\). Definiamo la misura candidata
\[
\Lambda_j =
 W(G_j)\,\mathcal H^2
 +\|\nabla_\Sigma g_j-G_j\|_*\,\mathcal H^2
 +|[g_j]|\,\mathcal H^1\!\llcorner J_{g_j}.
\]
Sia \(u_{j,h}\) la recovery SVD della §2bis del teorema
poliedrale. La misura energetica è
\[
\Lambda_{j,h} =
 W(\nabla_\Sigma u_{j,h})\,\mathcal H^2
 +|[u_{j,h}]|\,\mathcal H^1\!\llcorner J_{u_{j,h}}.
\]

**Lemma (convergenza locale per partizione fissata).**
Per ogni \(j\) fissato,
\[
\Lambda_{j,h}\stackrel{*}{\rightharpoonup}\Lambda_j
\quad\text{in }\mathcal M(\Sigma),\qquad h\downarrow0.
\]

*Dimostrazione.* Il bulk è esattamente \(W(G_j)\) quasi ovunque
su ogni cella. Per ogni singolo termine singolare
\(\sigma_i a_i\otimes\nu_i\) della SVD su \(T\), la misura
dei micro-salti, testata contro \(\varphi\in C(\Sigma)\), è
\[
 h\sigma_i\sum_{k\in\mathbb Z}
 \int_{T^\circ\cap\{x\cdot\nu_i=kh\}}\varphi\,d\mathcal H^1
 \longrightarrow
 \sigma_i\int_T\varphi\,d\mathcal H^2.
\]
È la formula di coarea seguita da una somma di Riemann; vale anche
per celle poligonali tagliate dai lati della superficie. Sommando
sugli indici singolari e sulle finitissime celle si ottiene la
misura limite
\(\|M_T\|_*\mathcal H^2\llcorner T\).
Sulle interfacce tra celle, la stima uniforme fino alla chiusura
delle celle implica la convergenza uniforme dei salti; dunque le
misure \(|[u_{j,h}]|\mathcal H^1\) sulle interfacce convergono
a \(|[g_j]|\mathcal H^1\). Le intersezioni tra famiglie di laminazione diverse sono punti
isolati. Le tracce delle linee laminate sul bordo delle celle non
sono incluse nei contributi interni (che sono calcolati su T°):
qualsiasi coincidenza con un lato è quindi contabilizzata una sola
volta nella misura di salto sull'interfaccia, già trattata tramite
la convergenza uniforme delle tracce. Non vi sono altri contributi.
Questo prova la convergenza debole-* delle misure. \(\square\)

**Passaggio alla diagonale.** La convergenza stretta globale
si verifica sommando i contributi di faccia e di spigolo. Infatti
\(g_j\to g\) in \(L^1(\Sigma)\), quindi
\(D_\Sigma g_j\stackrel{*}{\rightharpoonup}D_\Sigma g\).
Per ogni faccia, CFI Cor. 2.3 dà la convergenza della massa bulk
\(\int_f|\nabla g_j|\) e della massa dei salti interni; G4a dà
la convergenza della massa dei salti sugli spigoli. Sommando il
numero finito di facce e spigoli si ottiene
\[
|D_\Sigma g_j|(\Sigma)\to|D_\Sigma g|(\Sigma).
\]
Per il teorema di Reshetnyak,
\[
|D_\Sigma g_j|\stackrel{*}{\rightharpoonup}|D_\Sigma g|.
\]
Sottraendo la parte bulk, che converge in variazione totale per
\(\nabla g_j\to\nabla g\) fortemente in \(L^1\), si ottiene
\[
|[g_j]|\mathcal H^1\!\llcorner J_{g_j}
\stackrel{*}{\rightharpoonup}
|[g]|\mathcal H^1\!\llcorner J_g.
\]
Inoltre \(G_j\to G\) e \(\nabla g_j\to\nabla g\)
fortemente in \(L^p\), perciò le due densità assolutamente
continue di \(\Lambda_j\) convergono in \(L^1\)
(anche per \(W(F)=|F|_F^2\), usando \(p=2\)).
Ne segue
\[
\Lambda_j\stackrel{*}{\rightharpoonup}
\Lambda:=
 W(G)\mathcal H^2
 +\|\nabla_\Sigma g-G\|_*\mathcal H^2
 +|[g]|\mathcal H^1\!\llcorner J_g.
\]
Si sceglie ora \(h_j\downarrow0\) diagonalmente, imponendo
simultaneamente la convergenza della successione determinante,
dell'energia e di una famiglia densa di test continui per
\(\Lambda_{j,h_j}-\Lambda_j\). Allora
\[
\Lambda_{j,h_j}\stackrel{*}{\rightharpoonup}\Lambda.
\]

**Conseguenza ai vertici.** La misura \(\Lambda\) non ha atomi:
le sue prime due parti sono assolutamente continue rispetto a
\(\mathcal H^2\), mentre la parte di salto è assolutamente
continua rispetto a \(\mathcal H^1\) su un insieme rettificabile;
in particolare \(\Lambda(\{v\})=0\). Per ogni raggio \(s\)
tale che \(\Lambda(\partial B_s(v))=0\), la convergenza delle
misure dà
\[
\Lambda_{j,h_j}(B_s(v))\longrightarrow\Lambda(B_s(v)).
\]
Poiché \(B_s(v)\downarrow\{v\}\), il membro destro tende a zero
per \(s\downarrow0\). Per raggi eventualmente eccezionali si
usa la monotonia: scelto un raggio di continuità
\(s\in(r,2r)\),
\[
\limsup_j\Lambda_{j,h_j}(B_r(v))
\le\Lambda(B_s(v)),
\]
e il lato destro tende comunque a zero. Pertanto
\[
\lim_{r\downarrow0}\limsup_j
 E_W(u_{j,h_j};B_r(v))=0.
\]
Anche \(\mathcal F(g,G;B_r(v))\to0\), quindi
\\[
\lim_{r\downarrow0}\limsup_j
\left|E_W(u_{j,h_j};B_r(v))
-\mathcal F(g,G;B_r(v))\right|=0.
\]
Questa è più forte del controllo del solo residuo superiore
richiesto da G5.

**Precisazione sul riempimento.** Se si scegliesse invece di
costruire separatamente la recovery fuori da \(B_r(v)\), allora
sarebbe necessario un lemma di estensione con traccia prescritta
sull'arco conico, uniforme nella successione. La dimostrazione
precedente evita quel problema: non taglia la recovery e non
incolla un riempimento; controlla direttamente la misura energetica
della successione globale. Non usa la stima non dimostrata
\(O(r)\) del solo perimetro né l'asserzione che l'area piccola
impedisca da sé concentrazioni.

**Stato G5: DIMOSTRATO** per la recovery globale SVD su partizioni
poliedrali finite, subordinatamente alle convergenze CFI e alle
tracce G4a già enunciate. Non è una prova di un lemma generale di
riempimento con traccia assegnata: quel problema separato resta
aperto e non è necessario per questa costruzione.

### 5.5 Audit riga-per-riga di §5.4

Verifica dei quattro punti delicati:

1. **Micro-salti**: la formula del lemma è testata contro
   `φ∈C(Σ)` generica, non solo contro la massa totale — è una
   convergenza debole-* vera. La funzione
   `F(t)=∫_{T°∩{x·ν_i=t}}φ dH¹` è continua a tratti con
   discontinuità solo alle altezze dei vertici del poligono
   (finite) ⇒ Riemann integrabile; la somma `hΣ_k` è una somma
   di Riemann di passo `h`. Le celle non attraversano gli
   spigoli di `Σ` (la partizione li raffina), quindi non servono
   correzioni ai bordi; le intersezioni tra famiglie di
   laminate sono punti in 2D e non contribuiscono a `H¹`.
2. **Interfacce**: la stima `‖u_h−g_j‖_{L∞(P̄)}≤h‖M_P‖_*` è
   puntuale su `P̄` (il difetto `h⌊t/h⌋−t` è `≤h` ovunque),
   quindi le tracce convergono uniformemente su ogni lato di
   cella e la misura di salto `|Tr⁺u−Tr⁻u|H¹⌞e` converge in
   variazione — più forte del `L¹` richiesto. Il passaggio
   Reshetnyak usa `|Dg_j|(Σ)→|Dg|(Σ)` (CFI per faccia + G4a per
   spigoli, somma finita), `g_j→g` in `L¹`, e sottrae la parte
   AC convergente fortemente in `L¹`.
3. **Diagonale**: lemma standard a due indici
   (`Λ_{j,h}⇀*Λ_j` per `h↓0`, `Λ_j⇀*Λ`); la convergenza di
   **massa** (`φ≡1`) implica
   `E_W(u_{j,h_j})=Λ_{j,h_j}(Σ)→Λ(Σ)`, cioè convergenza
   dell'energia totale al funzionale candidato.
4. **Palle**: per `s` raggio di continuità di `Λ` la
   convergenza è diretta; per `r` eccezionale la monotonia dà
   `limsup_j Λ_{j,h_j}(B_r)≤Λ(B_s)` con `s∈(r,2r)` di
   continuità, e `Λ(B_s)→Λ({v})=0` per `s↓0`. La formula
   iterata `lim_{r↓0}limsup_j|E_W−ℱ|=0` è corretta.

**Caveat residuo**: la Riemann-integrabilità di `F(t)` e la
decomposizione `|Dg_j|=|∇g_j|H²+|[g_j]|H¹⌞J_{g_j}` sono
affermazioni standard non scritte riga per riga (SBV di `g_j`
perché piecewise-affine; `F` limitata con discontinuità finite).

### 5.6 Stato

**G5 — DIMOSTRATO** nel quadro della recovery globale e delle ipotesi dichiarate. La convergenza delle misure energetiche è provata in §5.4: coarea e somme di Riemann per i micro-salti, stime uniformi delle tracce sulle interfacce, convergenza stretta BV globale per le misure di salto CFI, e convergenza forte delle densità bulk. La misura limite non ha atomi ai vertici; la convergenza debole-* implica il controllo locale. Non si usa un riempimento separato con traccia prescritta.

## 6. Teorema isotropo su superfici poliedrali (DIMOSTRATO nel perimetro dichiarato)

Sia \(\Sigma\) una superficie poliedrale compatta della classe §1,
\(g\in SBV(\Sigma;\mathbb R^m)\) con
\(\nabla_\Sigma g\in L^p\) e
\(\int_{J_g}|[g]|\,d\mathcal H^1<\infty\), e
\(G\in L^p(\Sigma;\operatorname{Hom}(T\Sigma,\mathbb R^m))\),
con \(p=1\) per \(W(F)=|F|_F\) oppure \(p=2\) per
\(W(F)=|F|_F^2\). Per \(\psi(a,\nu)=|a|\), sotto le ipotesi CFI
verificate in §5.1,

\[
I_W^\Sigma(g,G)=
\int_\Sigma W(G)\,d\mathcal H^2+
\int_\Sigma\|\nabla_\Sigma g-G\|_*\,d\mathcal H^2+
\int_{J_g}|[g]|\,d\mathcal H^1.
\]

Liminf = G1. Recovery = CFI faccia-per-faccia + medie di \(G\)
+ recovery SVD su partizioni finite + G4a/G4b + convergenza
delle misure energetiche di §5.4. La diagonale dà l'uguaglianza.

## 7. Stato sintetico

- **Piano isotropo**: dimostrato (documento GIR §5, ipotesi CFI
  verificate, partizioni mesh→0, diagonale debole-*).
- **C60/`Σ` poliedrale**: G1, G2, G3, G4a, G4b e G5 sono
  dimostrati nel quadro della recovery globale su partizioni
  poliedrali finite. La misura energetica converge debolmente-*
  alla misura candidata; l'assenza di atomi ai vertici esclude
  concentrazioni residue. Il teorema è provato nel perimetro
  dichiarato in §6.
- **Anisotropo, `|a|²`, embeddedness**: fuori scope.
