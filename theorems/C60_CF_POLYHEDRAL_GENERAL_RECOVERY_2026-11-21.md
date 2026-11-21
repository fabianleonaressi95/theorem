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
`θ_v = 23·(360°/60) = 138°`? — non serve la forma esatta: ciò che
conta è `θ_v<2π` e finitezza di `V`.

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
| G2 | Densità SBV faccia-per-faccia | `g_j` affine per simplesso su partizione che raffina le facce; `∇g_j→∇g` in `L^p`; `∫_{J_{g_j}∩f°}|[g_j]|→∫_{J_g∩f°}|[g]|` per ogni `f` | **Provato per faccia** via CFI (ipotesi §5.1 del documento C60 verificabili: facce = poligoni convessi Lipschitz, `g_0(t)=t`, `g(a,ν)=|a|`). **Non** garantisce tracce — vedi G4a |
| G3 | Medie simpliciali di `G` | `G_j|_T = ⨍_T G` sulla stessa partizione CFI | **Provato**: mesh `≤cε→0` ⇒ convergenza forte in `L^p` ⇒ in variazione totale delle misure |
| G4 | Giunzione lungo spigoli | Lemma §4 + G4a (tracce) + G4b (tracce recovery) | Lemma + G4a **dimostrati**; G4b: estensione cella-per-cella **scritta** (§4.2), da verificare nei dettagli di convergenza dei costi sulle interfacce di salto |
| G5 | Vertici conici | energia residua nei dischi `B_r(v)` | **Ridotto, non dimostrato**: `B_r(v)` è un settore conico piatto, ma servono stima uniforme della recovery locale, controllo dei raccordi sugli archi `∂B_r∩Γ` e ordine dei limiti esplicito (§5.3). `θ_v≥2π` resta aperto |

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

### 5.1 Il disco conico è piatto

Un intorno intrinseco `B_r(v)` di un vertice conico è isometrico
a un **settore piano di angolo `θ_v`** (con i bordi laterali
identificati): la metrica è `dρ²+ρ²dφ²`, `0≤φ<θ_v`, ed `𝓗²` è la
misura piana pesata. L'unico punto non piatto è `v` stesso, di
misura nulla. Per `θ_v<2π` il settore è un dominio Lipschitz
(stellato, convesso se `θ_v≤π`); per `θ_v≥2π` si usa la
rappresentazione conica o una partizione in settori `<2π` —
l'argomento CFI è locale e si applica su ciascuno.

**Conseguenza**: non serve alcuna "costruzione di riempimento"
separata. Il disco conico è una cella di tipo faccia: vi si
applica la stessa catena G2+G3+teorema poliedrale, e le sue
interfacce circolari `∂B_r(v)` (archi di lunghezza `θ_v r`
internamente piatti) sono trattate dalle stesse tracce del §4.

### 5.2 Energia residua: la stima

La condizione corretta è energia *residua* nulla:

```
limsup_{r↓0} limsup_{j,k} [ E_W(u_{j,k};B_r(v)) −
   ℱ(g,G;B_r(v)) ] = 0 .
```

Per la costruzione esplicita, su ogni cella `P` che incontra
`B_r(v)`:

- **bulk**: `∫_{P∩B_r} W(G_j) d𝓗²` con `W=|·|_F` o `|·|_F²`.
  Poiché `G_j→G` in `L^p` e `{G_j}` è equi-integrabile,
  `sup_j ∫_{B_r}|G_j|^p → 0` per `r↓0` (assoluta continuità +
  convergenza forte); il termine limite `∫_{B_r}W(G)→0` per la
  stessa ragione.
- **mismatch**: `|P∩B_r|·‖M_P‖_*`, sommato su `P` dà
  `∫_{B_r}‖∇g_j−G_j‖_*` → `∫_{B_r}‖∇g−G‖_*→0`.
- **salti**: `∫_{J_{g_j}∩B_r}|[g_j]|→∫_{J_g∩B_r}|[g]|→0` per
  `r↓0`, essendo `|[g]|𝓗¹⌞J_g` una misura finita e `B_r↓{v}`
  con `𝓗¹({v})=0`. Le linee di laminato che attraversano `∂B_r`
  contribuiscono `O(h)·𝓗¹(∂B_r∩celle)=O(h·θ_v r)→0`.
- **concentrazione**: la costruzione ha limiti uniformi
  (`‖v_h−g_j‖∞≤h‖M‖` per cella, gradienti `G_j` equi-integrabili,
  numero di celle che incontrano `B_r(v)` localmente limitato
  per la regolarità della partizione): **nessuna concentrazione
  di energia è possibile** — tutti i contributi sono maggiorati
  da integrali di funzioni equi-integrabili su insiemi di misura
  →0.


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
[
 h\sigma_i\sum_{k\in\mathbb Z}
 \int_{T\cap\{x\cdot\nu_i=kh\}}\varphi\,d\mathcal H^1
 \longrightarrow
 \sigma_i\int_T\varphi\,d\mathcal H^2.
]
È la formula di coarea seguita da una somma di Riemann; vale anche
per celle poligonali tagliate dai lati della superficie. Sommando
sugli indici singolari e sulle finitissime celle si ottiene la
misura limite
\(\|M_T\|_*\mathcal H^2\llcorner T\).
Sulle interfacce tra celle, la stima uniforme fino alla chiusura
delle celle implica la convergenza uniforme dei salti; dunque le
misure \(|[u_{j,h}]|\mathcal H^1\) sulle interfacce convergono
a \(|[g_j]|\mathcal H^1\). Le intersezioni tra famiglie di
laminazione e interfacce sono insiemi finiti di punti e non
portano massa \(\mathcal H^1\). Non vi sono altri contributi.
Questo prova la convergenza debole-* delle misure. \(\square\)

**Passaggio alla diagonale.** La convergenza CFI stretta in BV
sulle facce, insieme alla convergenza forte delle tracce sugli
spigoli già dimostrata in G4a, dà la convergenza debole-* delle
misure di variazione totale su tutta \(\Sigma\). Sottraendo la
parte bulk, che converge fortemente in \(L^1\), si ottiene
[
 |[g_j]|\mathcal H^1\!\llcorner J_{g_j}
 \stackrel{*}{\rightharpoonup}
 |[g]|\mathcal H^1\!\llcorner J_g.
]
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
]
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
]
e il lato destro tende comunque a zero. Pertanto
\[
\lim_{r\downarrow0}\limsup_j
 E_W(u_{j,h_j};B_r(v))=0.
\]
Anche \(\mathcal F(g,G;B_r(v))\to0\), quindi
[
\lim_{r\downarrow0}\limsup_j
\left|E_W(u_{j,h_j};B_r(v))
-\mathcal F(g,G;B_r(v))\right|=0.
]
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

### 5.3 Stato

**G5 — RIDOTTO, non ancora dimostrato.** Per `θ_v<2π` (copre C60:
`θ_v=138°`) la strategia è: settore conico piatto + stessa catena
piana + stima §5.2. Ma la stima §5.2 da sola **non basta**:
equi-integrabilità di `G_j` e finitezza della misura di salto
controllano i termini del funzionale limite, non l'energia delle
recovery `u_{j,k}` nei settori. Servono:

1. una **stima uniforme della recovery locale** nei settori —
   le stesse maggiorazioni per cella (bulk `|P∩B_r|W(G_j)`,
   mismatch `|P∩B_r|‖M_P‖_*`, salti `∫_{J_{g_j}∩B_r}|[g_j]|`)
   vanno sommanti e mostrate uniformi in `(j,k)`;
2. il **controllo dei costi di interfaccia** introdotti dal
   raccordo lungo gli archi `∂B_r(v)∩Γ` (non solo la convergenza
   delle tracce di `g_j`, ma delle recovery `u_{j,k}`);
3. un **ordine dei limiti esplicito**: prima `k→∞` (recovery
   interna), poi `j→∞`, poi `r↓0` — oppure una diagonale che
   renda il residuo nullo.

La piattezza del settore garantisce che la *catena* si applichi
in linea di principio, ma non sostituisce la stima energetica.
Per `θ_v≥2π` serve inoltre una variante geometrica — **aperto**,
non necessario per C60.

**Conseguenza per la classificazione**: il risultato finale su
C60 isotropo **non è dichiarato completo** finché G4b (dettagli
delle interfacce di salto) e G5 (stima uniforme + ordine dei
limiti) non sono dimostrati e incorporati nella diagonale.

## 6. Teorema obiettivo (condizionale, NON dimostrato)

Sotto G1–G5 (o sotto le ipotesi verificabili che li sostituiscono):

```
I_W^Σ(g,G) = ∫_Σ W(G) + ∫_Σ ‖∇_Σ g−G‖_* + ∫_{J_g}|[g]|.
```

Liminf = G1. Recovery = G2+G3+teorema poliedrale + G4 (lemma 4 +
G4a + G4b) + G5, con diagonale debole-* già formalizzata.

## 7. Stato sintetico

- **Piano isotropo**: dimostrato (documento GIR §5, ipotesi CFI
  verificate, partizioni mesh→0, diagonale debole-*).
- **C60/`Σ` poliedrale**: G1, G2 (faccia), G3, G4a provati.
  **G4b**: estensione cella-per-cella scritta, da verificare.
  **G5**: ridotto alla stima uniforme sui settori conici +
  compatibilità delle tracce sugli archi + ordine dei limiti —
  **non ancora dimostrato**. Il risultato finale resta
  subordinato alla chiusura di questi due punti.
- **Anisotropo, `|a|²`, embeddedness**: fuori scope.
