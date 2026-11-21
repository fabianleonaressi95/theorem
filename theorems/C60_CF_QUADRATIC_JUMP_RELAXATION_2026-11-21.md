# C60 — rilassamento nullo del costo di salto quadratico

Data: 2026-11-21  
Classificazione: **teorema costruttivo nel modello SBV poliedrale faccia-per-faccia**  
Prerequisito: `theorems/C60_CF_DETERMINING_SEQUENCE_M0_2026-11-21.md`.

## 1. Funzionale

Per una densità bulk `W), si consideri il funzionale rilassato sulle successioni determinanti CF della coppia C60 corrente:

```
I_{W,2}(g,G) := inf liminf_m [
    ∫_Σ W(∇_Σu_m) d𝓗²
    + ∫_{J_{u_m}} |[u_m]|² d𝓗¹
],
u_m → g in L¹,
∇_Σu_m 𝓗² ⇀* G 𝓗².
```

Qui `∇_Σg=G` faccia per faccia, quindi `u_m=g` è già una successione determinante, ma non è in generale ottimale per il costo interfaciale quadratico.

## 2. Lemma di suddivisione del salto

Sia `e` uno spigolo interno tra due facce `f^-` e `f^+`. Si sceglie di modificare una striscia soltanto nella faccia `f^-`, lasciando invariata `f^+`.

Usiamo coordinate ortonormali `(s,t)` nella faccia `f^-`, con `s` lungo `e` e `t≤0` diretto verso l'interno di `f^-`. Sia `g^-` la mappa affine su `f^-`. La traccia `g^+(s,0)` sull'altro lato è affine in `s`; la sua estensione costante nella coordinata `t`,

```
q_e(s,t) := g^+(s,0),
h_e(s,t) := q_e(s,t) − g^-(s,t),
```

è affine e limitata in una striscia sufficientemente sottile. In particolare `q_e(s,0)=g^+(s,0)`.

Fissiamo una lunghezza di esclusione `r_m→0` agli estremi dello spigolo e una larghezza `δ_m→0`, con `δ_m/r_m→0`. Sul segmento centrale `s∈[r_m,|e|−r_m]`, dividiamo la striscia `−δ_m<t<0` in `m` strati paralleli di uguale spessore. Nel j-esimo strato, numerato dall'esterno verso lo spigolo, poniamo

```
u_m(s,t) := g^-(s,t) + (j/m) h_e(s,t),   j=1,…,m.
```

Fuori dalla striscia lasciamo `u_m=g^-`; sulla faccia `f^+` lasciamo `u_m=g^+`.

Ogni interfaccia tra due strati consecutivi, inclusa quella sul bordo esterno della striscia, porta un salto di ampiezza `|h_e|/m≤C_e/m`. Sulla linea `t=0`, invece, il valore dell'ultimo strato coincide con la traccia di `g^+`: il salto macroscopico sul segmento centrale è stato sostituito da `m` salti microscopici. Il salto originario resta soltanto sui due segmenti terminali di lunghezza `r_m`.

## 3. Costruzione globale sulla superficie C60

La superficie ha un numero finito di spigoli e angoli diedrali positivi. Per `m` sufficientemente grande, scegliendo `δ_m/r_m` abbastanza piccolo, le strisce centrali associate a spigoli distinti sono disgiunte all'interno di ciascuna faccia. Si applica la costruzione precedente a ogni spigolo, scegliendo una delle due facce incidenti.

Le funzioni risultanti sono affine a tratti su una partizione finita di ogni faccia; pertanto

```
u_m ∈ SBV(Σ;ℝ³).
```

Le costanti geometriche sono uniformabili perché il complesso ha un numero finito di facce e spigoli.

## 4. Stime

Esiste una costante `C` indipendente da `m` tale che:

### Convergenza forte

Le modifiche sono limitate e supportate in strisce di area totale `O(δ_m)`. Quindi

```
||u_m−g||_{L¹(Σ)} ≤ C δ_m → 0.
```

### Convergenza del gradiente assolutamente continuo

In ogni strato,

```
∇_Σu_m = ∇_Σg^- + (j/m)∇_Σh_e,
```

che è uniformemente limitato, poiché `g^-` e `h_e` sono affini e il complesso è finito. Fuori dalle strisce il gradiente resta quello originario `G`. Poiché l'area modificata tende a zero,

```
∇_Σu_m 𝓗² ⇀* G 𝓗².
```

La successione è quindi determinante per la coppia C60.

### Costo interfaciale quadratico

Per ogni spigolo, i `m` salti paralleli hanno ampiezza al più `C_e/m` e lunghezza al più `|e|). Il loro costo totale è limitato da

```
m |e| (C_e/m)² ≤ C_e² |e|/m.
```

Le due sezioni terminali della striscia hanno lunghezza totale `O(δ_m)` e salti uniformemente limitati; il loro costo è `O(δ_m)`. Il salto macroscopico residuo sui segmenti terminali originali ha lunghezza `O(r_m)` e ampiezza uniformemente limitata; il suo costo è `O(r_m)`.

Sommando sui finitissimi spigoli,

```
∫_{J_{u_m}} |[u_m]|² d𝓗¹
  ≤ C(1/m + δ_m + r_m) → 0.
```

### Costo bulk

I gradienti negli strati sono uniformemente limitati e l'area modificata è `O(δ_m)`. Per entrambi gli integrandi continui `W_1(F)=|F|_F` e `W_2(F)=|F|_F²),

```
∫_Σ W_i(∇_Σu_m) d𝓗² → ∫_Σ W_i(G) d𝓗².
```

## 5. Teorema

**Teorema.** Per la coppia C60 corrente con `∇_Σg=G`, per ciascuno dei bulk `W_1(F)=|F|_F` e `W_2(F)=|F|_F²`, e per la densità interfaciale quadratica `ψ_2(a,ν)=|a|²), vale

```
I_{W_i,2}(g,G) = ∫_Σ W_i(G) d𝓗².
```

**Dimostrazione.** Il termine interfaciale è non negativo. La semicontinuità inferiore del bulk dà il limite inferiore `∫W_i(G)`, con lo stesso argomento in norma di misura per `W_1` e in `L²) per `W_2`. La costruzione delle sezioni 2–4 è una recovery sequence determinante con costo interfaciale tendente a zero e costo bulk convergente a `∫W_i(G)`. I due limiti coincidono. ∎

## 6. Valori C60

Poiché `G_fᵀG_f=I₂`,

| Bulk | Infimo con `ψ_2=|a|²` |
|---|---:|
| `W_1(F)=|F|_F` | **45.6365164300** |
| `W_2(F)=|F|_F²` | **64.5397804748** |

Questi valori bulk derivano dalle aree e dalle isometrie faccia-per-faccia già archiviate. Non va aggiunto il costo macroscopico quadratico `∫_{J_g}|[g]|²`: esso è il costo della successione costante, non il valore rilassato.

## 7. Portata

- La costruzione è specifica alla superficie poliedrale finita C60, con mappe affini su ciascuna faccia e un numero finito di spigoli.
- La prova non usa un teorema integrale generale per densità non omogenee: costruisce direttamente la recovery sequence.
- Non copre densità interfaciali anisotrope arbitrarie, né il caso bulk `M≠0`.
- Il risultato spiega perché la sola convessità della densità interfaciale non garantisce conservazione del costo macroscopico: per `|a|²`, la suddivisione in micro-salti abbassa il costo fino a zero.
