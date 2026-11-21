# C60 — tentativo di dimostrazione: densità energetica SBV pesata

Data: 2026-11-21
Classificazione: **tentativo di dimostrazione** — la strategia è
valida e la maggior parte dei passi è standard; il gap residuo è
identificato e isolato in §4. Non è un teorema chiuso.

## 1. Enunciato necessario (forma esatta)

Non serve la densità SBV "pesata per `ψ(a,ν)`" in generale: per
`ψ(a,ν)=|a|` e la norma nucleare `|a⊗ν|_*=|a|` (ν unitaria), il
costo di salto è la **massa della parte singolare**:

```
|D^s u|(Ω) = ∫_{J_u} |[u]| d𝓗^{n-1} .
```

Basta dunque il seguente.

**Teorema D (densità stretta per la parte singolare).** Sia
`Ω⊂ℝ²` limitato, `g∈SBV(Ω;ℝ^m)` con `∇g∈L¹` e
`∫_{J_g}|[g]|d𝓗¹<∞`. Esistono `g_j` **localmente affini su un
complesso poliedrale finito** (il salto di `g_j` è contenuto in
`∂` delle celle, dove `g_j` può essere discontinuo) tali che

```
g_j → g in L¹(Ω),
∇g_j → ∇g in L¹(Ω),
|D^s g_j|(Ω) → |D^s g|(Ω) = ∫_{J_g}|[g]|d𝓗¹ .
```

In più, per il campo prescritto: dato `G∈L¹(Ω)`, esiste una
successione di campi `G_j` **costanti a tratti sulle stesse
celle** con `G_j→G` in `L¹` (e in `L²` se `G∈L²`). Allora
`∫‖∇g_j−G_j‖_*→∫‖∇g−G‖_*` perché `‖·‖_*` è Lipschitz.

## 2. Strategia di dimostrazione in quattro passi

### Passo A — regolarizzazione del salto (quasi chiuso per citazione)

Per `g∈SBV`, il teorema di approssimazione di Ambrosio–De
Philippis–Figalli (*On the approximation of SBV functions*,
Ric. Mat. 2013) fornisce `g^{(k)}` con:

- `g^{(k)}→g` in `L¹`, `∇g^{(k)}→∇g` in `L¹`;
- `J_{g^{(k)}}` contenuto in un'unione finita di ipersuperfici
  `C^{1,1}`;
- **convergenza delle energie di superficie**: per `g(x,a,b,ν)`
  continua con crescita controllata,
  `∫_{J_{g^{(k)}}} g(x,g^{(k)+},g^{(k)−},ν)d𝓗¹ →
   ∫_{J_g} g(x,g^+,g^−,ν)d𝓗¹`.

Per la nostra densità `ψ(a,ν)=|a|` serve `g(x,a,b,ν)=|a−b|`:
continua, linear growth — **dovrebbe rientrare nelle ipotesi del
loro teorema** (da verificare la classe di crescenza ammessa;
se è `o(|a|+|b|)` o lineare, ok). Se vale, il Passo A fornisce
direttamente

```
∫_{J_{g^{(k)}}}|[g^{(k)}]|d𝓗¹ → ∫_{J_g}|[g]|d𝓗¹ ,
```

chiudendo il punto senza passare dalla strict convergence di
`|D^s|` (che resta un'alternativa più debole). **Stato: citabile,
con verifica delle ipotesi di crescita su `g` ancora da fare.**

### Passo B — politopalizzazione del salto (gap principale)

Data `g^{(k)}` con `J` unione di ipersuperfici `C¹`, serve
`s_j` poliedrale che:

1. approssimi `J_{g^{(k)}}` con un poliedro `P_j` di facet in
   convergenza di misura (`𝓗¹(P_j△J)→0` o convergenza varifold);
2. estenda i dati di traccia `g^{(k)±}|_J ∈ L¹(J)` a funzioni
   affini sulle celle adiacenti a `P_j`;
3. mantenga `∫_{P_j}|[s_j]| → ∫_J|[g^{(k)}]|`.

Il punto 3 è il più delicato: l'ampiezza del salto su un facet
poliedrale è la differenza dei due interpolanti affini, che
approssima `[g^{(k)}]` solo se le tracce sono interpolanti in
modo coerente. La costruzione naturale: su ogni cella `C` del
complemento di `P_j`, `s_j` = interpolante affine dei valori di
traccia ai vertici/ai punti di `∂C∩J`; il salto attraverso un
facet `F⊂P_j` è `[s_j]|_F ≈ [g^{(k)}]|_F` se `F` è vicino a `J`.

**Stato**: la politopalizzazione di un insieme rettificabile con
convergenza `𝓗¹` è standard; l'estensione affine dei dati di
traccia con controllo del salto pesato **non è un teorema
standard** — è il gap da dimostrare o da citare.

### Passo C — errore bulk (standard)

Con `s_j` affine a tratti e mesh di passo `δ_j→0`,
`∇s_j→∇g` in `L¹` segue dalla convergenza delle derivate dei
polinomi interpolanti più l'approssimazione di `g` nel Passo A.
La convergenza `G_j→G` per proiezione a tratti costanti è
standard (media su celle).

### Passo D — diagonale (standard)

Combinando Passi A–C e il teorema poliedrale (dimostrato), la
diagonale `j→∞` produce la recovery per `(g,G)`.

## 3. Cosa dipende da cosa

| Passo | Ingredienti | Stato |
|---|---|---|
| A: regolarizzazione SBV | DFP 2013: convergenza energia superficiale per `g` continua | **citabile** — verificare ipotesi di crescita su `g(x,a,b,ν)=|a−b|` |
| B: salto poliedrale + tracce | politopalizzazione + estensione affine pesata | **gap** |
| C: bulk | interpolazione affine | standard |
| D: diagonale | — | standard |

## 4. Il gap isolato, precisamente

**Lemma B (dai salti lisci ai salti poliedrali).** Sia
`w∈SBV` con `J_w` unione di curve `C¹` e tracce `w^±∈L¹(J_w)`.
Allora esistono `s_j` affine a tratti su un complesso poliedrale
con `s_j→w` in `L¹`, `∇s_j→∇w` in `L¹`, e
`|D^s s_j|(Ω)→|D^s w|(Ω)`.

Se questo lemma è vero, il Teorema D segue dai Passi A, C, D.
La sua dimostrazione richiede:

1. una successione di politopi `P_j` con `𝓗¹(P_j△J_w)→0` e
   convergenza delle normali `ν_{P_j}→ν_{J_w}` `𝓗¹`-q.o. —
   **standard** (approssimazione politopale di insiemi
   rettificabili);
2. una regola di interpolazione delle tracce `w^±` che produca
   salti `[s_j]` convergenti a `[w]` in `L¹(P_j)` — **da
   dimostrare**: è un problema di estensione di Whitney con
   stima `L¹` del salto;
3. il controllo che i facet di `P_j` non prossimi a `J_w` non
   creino salti spurii — gestibile scegliendo la mesh compatibile
   con `P_j`.

## 5. Conclusione onesta

Il Teorema D **non è dimostrato** da questo tentativo, ma è
ricondotto a due ingredienti:

- **Lemma B** (sopra): il gap tecnico principale;
- la verifica che l'approssimazione SBV citata sia strict nella
  massa — probabile ma da controllare.

Se il Lemma B viene dimostrato o citato in letteratura, l'intera
catena `densità → poliedrale → diagonale` chiude l'identità
generale per `ψ=|a|`, `W=|F|_F`/`|F|_F²`.
