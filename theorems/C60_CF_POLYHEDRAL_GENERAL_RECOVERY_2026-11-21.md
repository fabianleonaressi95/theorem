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
| G4 | Giunzione lungo spigoli | Lemma §4 + G4a (tracce) + G4b (tracce recovery) | **Lemma dimostrato; G4a CHIUSO (CFI Cor. 2.3 + tracce BV); G4b quasi chiuso** — resta solo il caveat piecewise-affine con salti interni |
| G5 | Vertici conici | energia residua nei dischi `B_r(v)` | **Aperto** — serve stima di riempimento, non solo area nulla |

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

**Caveat residuo**: la stima `L^∞` è provata per `g` affine su una
faccia con `M` costante. Per `g_j` piecewise-affine **con salti
interni** (il jump set CFI), la recovery va applicata cella per
cella e i salti interni di `g_j` devono essere ereditati da
`u_{j,k}`: va verificato che la formulazione del teorema
poliedrale ammetta dati piecewise-affine con jump set e che la
costruzione non "levighi" i saldi interni. Se il teorema è
stato enunciato solo per `g` globalmente affine per faccia, serve
l'estensione ovvia per restrizione (l'affine si restringe, i
salti si ereditano) — da scrivere esplicitamente.

## 5. G5 — Vertici conici (APERTO)

Per `v∈V`, `B_r(v)` disco intrinseco di raggio `r`. La condizione
corretta **non** è `sup_n E(u_n;B_r(v))→0` (troppo forte: un
salto di `g` che termina in `v` può dare energia limite
arbitrariamente vicina). La condizione corretta è
**energia residua nulla**:

```
limsup_{r↓0} limsup_n [ E_W(u_n;B_r(v)) −
   ℱ(g,G;B_r(v)) ] = 0 ,
```

i.e. l'energia dei dischi converge al valore del funzionale
limite lì, e quel valore →0 per `r↓0` se le densità sono
integrabili (serve `∫_{B_r(v)}(W(G)+‖∇g−G‖_*)→0`, vera per
misure assolutamente continue). La parte da dimostrare è la
**stima di riempimento**: una costruzione esplicita su
`B_r(v)∖⋃B_{r'}(v)` con costo controllato dalle tracce sul
bordo — un problema di riempimento su dominio conico di angolo
`θ_v`, che si riduce al caso piano per `r` piccolo se si usa la
metrica intrinseca (la punta conica ha area `~θ_v r²`, il bordo
`~θ_v r`).

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
- **C60/`Σ` poliedrale**: G1, G2 (faccia), G3, **G4a** provati;
  **G4b** chiudibile (stima `L^∞` per cella + diagonale; caveat:
  enunciare la recovery per `g_j` piecewise-affine con salti);
  **G5 resta l'unico ostacolo geometrico** — energia residua sui
  60 dischi conici.
- **Anisotropo, `|a|²`, embeddedness**: fuori scope.
