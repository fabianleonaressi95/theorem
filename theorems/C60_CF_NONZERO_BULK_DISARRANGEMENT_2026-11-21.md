# C60 — costruzione CF esplicita per disarrangiamento bulk non nullo

Data: 2026-11-21  
Classificazione: **proposizione costruttiva dimostrata per campi bulk costanti su ciascuna faccia**  
Ambito: superficie poliedrale finita C60, mappe macroscopiche affini faccia-per-faccia.

## 1. Problema

Sia `Σ` il complesso poliedrale C60. Su ogni faccia `f`, si usino coordinate ortonormali `ξ=(ξ₁,ξ₂)` nel piano tangente e si scriva

```
g_f(ξ) = A_f ξ + b_f,       A_f ∈ R^{3×2}.
```

Sia assegnato un campo bulk alternativo `G̃` costante su ciascuna faccia, con matrici `G̃_f∈R^{3×2}`. Si definisca

```
M_f := A_f − G̃_f.
```

Non si assume `M_f=0`. L'obiettivo è costruire `u_h∈SBV(Σ;R³)` tali che

```
u_h → g                    in L¹(Σ;R³),
∇_Σu_h 𝓗² ⇀* G̃ 𝓗²         come misure matriciali.
```

Questa è la condizione determinante CF nella convenzione intrinseca adottata qui: la convergenza riguarda la sola parte assolutamente continua della derivata.

## 2. Quantizzatore a gradini su una faccia

Per `h>0`, si definisca il quantizzatore della griglia cartesiana

```
q_h(ξ) := h floor(ξ₁/h) e₁ + h floor(ξ₂/h) e₂.
```

Quasi ovunque nella faccia, `q_h` è costante; attraversando una linea di griglia ortogonale a `e_i`, il suo salto è `h e_i`. Inoltre

```
|q_h(ξ)−ξ| ≤ √2 h.
```

Definiamo su ogni faccia

```
u_{h,f}(ξ) := G̃_f ξ + b_f + M_f q_h(ξ).
```

Equivalentemente,

```
u_{h,f}(ξ) = g_f(ξ) + M_f(q_h(ξ)−ξ).
```

La seconda formula rende immediata la convergenza uniforme sulla faccia:

```
sup_{ξ∈f}|u_{h,f}(ξ)−g_f(ξ)|
  ≤ √2 h ||M_f||  → 0.
```

Poiché `q_h` è localmente costante, la derivata classica quasi ovunque è esattamente

```
∇_Σu_{h,f}(ξ) = G̃_f.
```

Non si formano strati con gradienti grandi: tutto il disarrangiamento `M_f` è portato dai salti della griglia.

## 3. Misura dei micro-salti

Su una linea di griglia con normale `e_i`, il salto di `u_{h,f}` è

```
[u_{h,f}] = h M_f e_i.
```

La misura di salto è quindi la somma delle misure rettificabili sulle linee della griglia. Poiché `u_{h,f}→g_f` uniformemente, le derivate distribuzionali convergono

```
D u_{h,f} ⇀* Dg_f = A_f 𝓗²⌞f.
```

La parte assolutamente continua è, per ogni `h`, esattamente

```
∇u_{h,f} 𝓗² = G̃_f 𝓗²⌞f.
```

Sottraendo questa identità dalla convergenza delle derivate totali si ottiene

```
D^s u_{h,f} ⇀* (A_f−G̃_f)𝓗²⌞f
             = M_f 𝓗²⌞f.
```

Si può anche verificare la limitatezza uniforme della variazione totale: in un poligono limitato, il numero di segmenti di griglia di ciascuna famiglia è `O(h^{-1})`, ciascun salto ha ampiezza `O(h)` e la lunghezza totale dei segmenti di una famiglia è `O(h^{-1})`; pertanto la massa totale dei salti è `O(1)`. Insieme al bulk costante, `sup_h |Du_{h,f}|(f)<∞`. Ogni `u_{h,f}` è dunque SBV.

## 4. Incollaggio sulle 32 facce

Si definisce `u_h` faccia per faccia con la formula precedente. Non si impone continuità sugli spigoli: la classe è SBV e conserva i salti macroscopici.

Sulla frontiera di ogni faccia,

```
|u_{h,f}−g_f| ≤ √2 h ||M_f||.
```

Quindi, su uno spigolo comune `e=f^-∩f^+`, la traccia del salto soddisfa

```
[u_h]|_e = [g]|_e + O(h)
```

uniformemente lungo lo spigolo. Ne segue che le misure dei salti macroscopici convergono a `[g]⊗ν_g 𝓗¹⌞J_g`. Le micro-linee di griglia interne alle facce non si sovrappongono allo scheletro macroscopico, salvo intersezioni di `𝓗¹`-misura nulla.

Essendoci un numero finito di facce, le stime sono uniformi e si sommano. Si ottiene

```
u_h → g in L¹(Σ;R³),
∇_Σu_h 𝓗² = G̃ 𝓗² per ogni h,
D^s_Σu_h ⇀* M 𝓗² + [g]⊗ν_g 𝓗¹⌞J_g.
```

In particolare `u_h` è una determining sequence per `(g,G̃)` nel modello intrinseco faccia-per-faccia. La costruzione non richiede `M` di rango uno: la quantizzazione nelle due direzioni genera separatamente le due colonne di `M_f`.

## 5. Conseguenze energetiche e limiti

Per ogni bulk continuo `W`, il termine bulk della successione è esattamente

```
∫_Σ W(∇_Σu_h) d𝓗² = ∫_Σ W(G̃) d𝓗².
```

Per una densità interfaciale `ψ(a,ν)=|a|^p`, con `p>0`, il costo dei micro-salti interni ha la scala

```
O(h^{p−1}).
```

Infatti ciascun salto ha ampiezza `O(h)`, mentre la lunghezza totale delle linee di griglia è `O(h^{-1})`. Ne segue:

- `p=1`: costo micro-interfaciale uniformemente limitato; non tende in generale a zero.
- `p>1`: costo micro-interfaciale tende a zero.
- `0<p<1`: la stima scala come `h^{p−1}` e non dà un limite finito.

Per `ψ(a,ν)=|a|`, la griglia cartesiana dà il limite micro-interfaciale

```
∫_f (|M_f e₁| + |M_f e₂|) d𝓗²,
```

a meno dei contributi di bordo che scompaiono nel limite. È un upper bound associato a questa scelta di griglia. Per la densità isotropa lineare `ψ(a,ν)=|a|`, il cell problem è ora risolto: il costo minimo per unità di area è la norma nucleare `||M_f||_*`, raggiunta da una costruzione SVD con rette orientate secondo i vettori singolari. La dimostrazione completa è in [`C60_CF_NUCLEAR_NORM_CELL_PROBLEM_2026-11-21.md`](C60_CF_NUCLEAR_NORM_CELL_PROBLEM_2026-11-21.md).

Il salto macroscopico sugli spigoli resta presente nel limite e contribuisce secondo la densità `ψ([g],ν_g)`, se la densità è continua e la convergenza uniforme delle tracce viene usata nella corrispondente stima.

## 6. Teorema costruttivo

**Teorema.** Sia `g` affine su ciascuna faccia del complesso poliedrale C60 e sia `G̃` un campo matriciale tangenziale costante su ciascuna faccia. Allora esiste una successione `u_h∈SBV(Σ;R³)` tale che

```
u_h → g                         fortemente in L¹,
∇_Σu_h 𝓗² ⇀* G̃ 𝓗²              debolmente-* come misure,
D^s_Σu_h ⇀* (∇_Σg−G̃)𝓗² + [g]⊗ν_g 𝓗¹⌞J_g.
```

Inoltre, la parte assolutamente continua del gradiente coincide con `G̃` esattamente per ogni `h`, e le variazioni totali `|Du_h|(Σ)` sono uniformemente limitate.

**Dimostrazione.** La successione è quella definita in §2. Le stime uniformi e la convergenza sulla singola faccia sono dimostrate in §3; il controllo uniforme delle tracce e l'incollaggio finito sono in §4. La formula per la parte singolare segue sottraendo il limite della parte assolutamente continua dalla convergenza distribuzionale di `Du_h`. ∎

## 7. Portata

- **Provato:** esistenza di una determining sequence intrinseca per ogni campo `G̃` costante faccia per faccia, incluso `M≠0`.
- **Provato:** il gradiente assolutamente continuo è esattamente `G̃` a ogni scala.
- **Provato:** ottimalità del costo micro-interfaciale per `ψ(a,ν)=|a|`, con valore `||M_f||_*` per unità di area (cell problem SVD).\n- **Non provato:** ottimalità per densità 1-omogenee anisotrope o dipendenti dalla normale.
- **Non provato:** formula di rilassamento per campi `G̃` variabili all'interno delle facce.
- **Non provato:** teorema integrale CF generale per tutte le superfici poliedrali.
- **Non provato:** eventuali vincoli aggiuntivi di immersione o embeddedness degli approssimanti; la classe CF SBV non li impone.

La costruzione colma il gap di esistenza per `M≠0` nel caso faccia-per-faccia costante, ma non identifica automaticamente l'infimo energetico generale.
