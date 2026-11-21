# C60 — identificazione dell'infimo CF per bulk convesso e salto normato

Data: 2026-11-21  
Classificazione: **teorema dimostrato nel modello intrinseco SBV poliedrale dichiarato**  
Prerequisiti: `theorems/C60_CF_DETERMINING_SEQUENCE_M0_2026-11-21.md`.

## 1. Funzionale e classe ammissibile

Sia `Σ` la superficie poliedrale compatta C60, con misura di area `𝓗²`. Si considerino successioni `u_n∈SBV(Σ;ℝ³)` tali che

```
u_n → g                 in L¹(Σ;ℝ³),
∇_Σu_n 𝓗² ⇀* G 𝓗²      in misure di Radon.
```

La convergenza della seconda riga riguarda esclusivamente la parte assolutamente continua della derivata SBV. Per una densità bulk `W` e la densità interfaciale `ψ(a,ν)=|a|`, poniamo

```
I_W(g,G) := inf { liminf_n E_W(u_n) : (u_n) determining },
E_W(u) := ∫_Σ W(∇_Σu) d𝓗² + ∫_{J_u} |[u]| d𝓗¹.
```

Si usano la norma di Frobenius sulle matrici tangenziali e la normale conormale unitaria `ν_u` nello spazio tangente di `Σ`.

## 2. Identificazione del limite singolare

Per ogni successione ammissibile, `u_n→g` in `L¹` implica

```
D_Σu_n → D_Σg   in distribuzioni.
```

Inoltre, per la condizione determinante,

```
∇_Σu_n 𝓗² ⇀* G 𝓗².
```

Se il liminf energetico è finito, si passa a una sottosuccessione con energia uniformemente limitata. Per `W(F)=|F|_F`, il bulk controlla `∫|∇_Σu_n|`; per `W(F)=|F|_F²`, il controllo `L²` implica il controllo `L¹` perché `𝓗²(Σ)<∞`. In entrambi i casi il termine interfaciale controlla

```
|D^s_Σu_n|(Σ) = ∫_{J_{u_n}} |[u_n]⊗ν_{u_n}| d𝓗¹
              = ∫_{J_{u_n}} |[u_n]| d𝓗¹.
```

Le misure `D^s_Σu_n` sono dunque limitate in variazione totale. Dalla convergenza distribuzionale e dalla convergenza debole-* della parte assolutamente continua segue

```
D^s_Σu_n ⇀* D_Σg − G 𝓗².
```

Nel caso C60 corrente, già verificato nel documento prerequisito,

```
∇_Σg = G  𝓗²-q.o.,
D_Σg − G 𝓗² = [g]⊗ν_g 𝓗¹⌞J_g.
```

Per semicontinuità inferiore della variazione totale,

```
liminf_n ∫_{J_{u_n}} |[u_n]| d𝓗¹
  = liminf_n |D^s_Σu_n|(Σ)
  ≥ |D^s_Σg|(Σ)
  = ∫_{J_g} |[g]| d𝓗¹.
```

Questa è la stima interfaciale decisiva. Non discende dalla sola convessità di `ψ`: usa che `ψ(a,ν)=|a|` è la norma associata alla variazione totale del tensore di salto `a⊗ν`.

## 3. Limite inferiore del bulk

### 3.1 Crescita lineare

Per `W_1(F)=|F|_F`, la convergenza debole-* delle misure matriciali dà

```
liminf_n ∫_Σ |∇_Σu_n|_F d𝓗²
  ≥ |G 𝓗²|(Σ)
  = ∫_Σ |G|_F d𝓗².
```

### 3.2 Crescita quadratica

Per `W_2(F)=|F|_F²`, se il liminf è finito, `∇_Σu_n` è limitata in `L²`. Esiste quindi una sottosuccessione debolmente convergente in `L²`, diciamo a `H`. La convergenza debole-* delle misure identifica necessariamente `H=G` quasi ovunque. Per semicontinuità debole della norma `L²`,

```
liminf_n ∫_Σ |∇_Σu_n|_F² d𝓗²
  ≥ ∫_Σ |G|_F² d𝓗².
```

## 4. Teorema di minimalità

**Teorema.** Supponiamo:
1. `g∈SBV(Σ;ℝ³)` nella definizione intrinseca faccia-per-faccia;
2. `∇_Σg=G` quasi ovunque;
3. `Σ` ha area finita e le convergenze determinanti sono quelle del §1.

Allora, per ciascuno dei due integrandi bulk `W_1(F)=|F|_F` e `W_2(F)=|F|_F²`, con densità interfaciale `ψ(a,ν)=|a|`,

```
I_W(g,G) = ∫_Σ W(G) d𝓗² + ∫_{J_g}|[g]| d𝓗¹.
```

**Dimostrazione.** Le sezioni 2 e 3 forniscono, per ogni successione determinante, il limite inferiore separato dei termini bulk e interfaciale. Poiché entrambi sono non negativi, il limite inferiore della somma è almeno la somma dei due limiti inferiori. D'altra parte, la successione costante `u_n=g` è determinante perché `∇_Σg=G`; la sua energia è esattamente il membro destro. Il limite inferiore e il limite superiore coincidono. ∎

Il teorema identifica l'infimo per le due coppie di densità specificate; non è un teorema per ogni integrando convesso o per ogni densità interfaciale.

## 5. Valori C60

Per `G_fᵀG_f=I₂`, si ha `|G_f|_F=√2` e `|G_f|_F²=2`. I valori bulk già calcolati sono:

| Bulk | Integrale bulk |
|---|---:|
| `W₁(F)=|F|_F` | 45.6365164300 |
| `W₂(F)=|F|_F²` | 64.5397804748 |

L'integrale di salto `∫_{J_g}|[g]|d𝓗¹` è stato valutato numericamente su tutti i 90 spigoli, con quadratura trapezoidale a 200 campioni per spigolo: `38.9347888585`.

Ne risultano le identificazioni (con il solo contributo interfaciale numericamente quadraturato):

| Bulk | Valore totale |
|---|---:|
| `W₁(F)=|F|_F` | **84.5713052885** |
| `W₂(F)=|F|_F²` | **103.4745693333** |

La formula integrale è il risultato del teorema; le cifre decimali dell'interfaccia sono approssimazioni numeriche, non valori simbolici esatti.

## 6. Densità interfaciale non coperte

La conclusione usa `ψ(a,ν)=|a|`. Non va sostituita con l'affermazione più ampia «`ψ` convessa nel salto». Per esempio, `ψ(a,ν)=|a|²` non controlla la variazione totale del salto e non è positivamente 1-omogenea. Una suddivisione di un salto `a` in `m` salti paralleli uguali ha costo formale

```
m |a/m|² = |a|²/m → 0.
```

Questo mostra che la stima di variazione totale usata sopra non è disponibile per la densità quadratica; il suo rilassamento richiede un cell problem e una recovery construction globale compatibile con la geometria C60. Non si dichiara qui il valore globale dell'infimo per `ψ=|a|²`.

Più in generale, la convessità da sola non sostituisce subadditività e omogeneità positiva di grado uno, ipotesi usate nei risultati classici sulle densità interfaciali di structured deformations.

## 7. Ambito e limiti

- Il teorema è una dimostrazione diretta nel modello intrinseco SBV sulla superficie poliedrale, mediante misure tangenziali e carte faccia-per-faccia.
- Non dimostra una generalizzazione generale del teorema integrale CF a tutte le varietà o superfici poliedrali.
- Non copre `M=∇_Σg−G≠0`.
- Non copre densità interfaciali quadratiche, anisotrope non normate, o non omogenee.
- La stima quadratica `C/h` degli strip continui resta un risultato separato sulla regolarizzazione continua.

## Riferimenti

- R. Choksi, I. Fonseca, *Bulk and Interfacial Energies for Structured Deformations of Continua*, Arch. Rational Mech. Anal. 138 (1997), 37–103, Def. 2.11, Thm. 2.12, Remark 2.13.
- A. C. Barroso, J. Matias, M. Morandotti, D. R. Owen, *Explicit Formulas for Relaxed Disarrangement Densities Arising from Structured Deformations*, Math. Mech. Complex Systems 5 (2017), 163–189, DOI: 10.2140/memocs.2017.5.163.
