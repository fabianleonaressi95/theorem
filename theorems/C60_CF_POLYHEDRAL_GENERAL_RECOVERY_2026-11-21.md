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
| G4 | Giunzione lungo spigoli | Lemma locale sotto; serve convergenza tracce | **Lemma elementare dimostrato**; **G4a (tracce) aperta** |
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
implica tracce. Due vie:

- **(a)** citare un teorema di densità SBV *con controllo del
  bordo* (es. tracce che convergono in `L¹(∂Ω)`) — da verificare
  in letteratura;
- **(b)** modifica CFI in una striscia `dist(x,∂f)<δ` che forza
  la convergenza delle tracce, con costo controllato da
  `𝓗¹(J_g∩striscia)→0` — il lemma di localizzazione isola
  esattamente questa stima.

### 4.2 G4b — recovery locale dopo incollaggio

La recovery poliedrale su ogni faccia produce `u_{j,k}→g_j` con
`∇u_{j,k}𝓗²⇀*G_j𝓗²` **all'interno della faccia**. Dopo
incollaggio piecewise, le tracce sui bordi delle facce sono
quelle dei `u_{j,k}|_f`; l'identità del lemma 4 vale se le tracce
di `u_{j,k}|_f` convergono a quelle di `g_j|_f` — ma la recovery
poliedrale produce microstruttura che può oscillare vicino al
bordo. Va verificato che la costruzione staircase/laminate sia
uniforme fino al bordo, o che una striscia di raccordo assorba
l'errore. **Aperto.**

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
- **C60/`Σ` poliedrale**: G1, G2 (faccia), G3 provati; **G4a,
  G4b, G5 aperti** — sono i soli ostacoli residui.
- **Anisotropo, `|a|²`, embeddedness**: fuori scope.
