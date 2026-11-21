# C60 — determining sequence Choksi–Fonseca nel caso di disarrangiamento bulk nullo

Data: 2026-11-21  
Classificazione: **proposizione dimostrata nel modello faccia-per-faccia dichiarato**  
Riferimento: `docs/C60_DPO_FORMAL_PROOF_2026-11-21.md`, Proposizioni 1–2.

## 1. Dati del problema e controllo di coerenza

Sia `Σ` la superficie poliedrale compatta del icosaedro troncato, decomposizione finita in facce piane `f`. Sul relativo piano tangente si usa la carta ortonormale `ξ=B_f^T(x-x_f)in P_f⊂R²`.

Il documento formale definisce la mappa sulla faccia mediante una rotazione `Q_fin SO(3)` la cui restrizione al piano tangente è rappresentata, nella carta `B_f`, da
Sia `Σ` la superficie poliedrale compatta del icosaedro troncato, decomposizione finita in facce piane `f`. Sul relativo piano tangente si usa la carta ortonormale `ξ=B_f^T(x-x_f) ∈ P_f ⊂ R²`.

Il documento formale definisce la mappa sulla faccia mediante una rotazione `Q_f ∈ SO(3)` la cui restrizione al piano tangente è rappresentata, nella carta `B_f`, da
```
g_f(ξ) = B_f D_f ξ + b_f,
G_f     = B_f D_f,
D_f ∈ SO(2),  B_fᵀB_f=I₂.
```
Pertanto, nella stessa carta tangenziale e con la stessa convenzione di coordinate,
```
∇_Σ g|_f = B_f D_f = G_f.
```
È essenziale che le due matrici siano espresse nella medesima carta: non si devono confrontare la matrice ambientale `Q_f|_{T_f}` e la matrice coordinata `B_fD_f` senza inserire la base.

La parte singolare globale di `D_Σg) è concentrata sullo scheletro degli spigoli:
La parte singolare globale di `D_Σg è concentrata sullo scheletro degli spigoli:
```
D_Σg = G 𝓗²⌞Σ + [g]⊗ν_g 𝓗¹⌞J_g.
```
Non vi è parte di Cantor nel modello faccia-per-faccia finito.

Ne segue che il disarrangiamento bulk della coppia è
```
M := ∇_Σg − G = 0   𝓗²-a.e. su Σ.
```

## 2. Proposizione — successione determinante esplicita

**Proposizione.** Assumendo le identità faccia-per-faccia sopra riportate e la definizione di `SBV(Σ;R³)` mediante carte/strati sulle facce poliedrali con tracce compatibili lungo gli spigoli, la successione
```
u_n := g   per ogni n
```
è una determining sequence Choksi–Fonseca per la coppia `(g,G)`, nella versione intrinseca sulla superficie.

**Dimostrazione.**

1. Per la decomposizione faccia-per-faccia già dimostrata, `g∈SBV(Σ;R³)`.
2. `u_n=g` implica immediatamente `u_n→g` fortemente in `L¹(Σ;R³)` (anzi, identicamente).
3. La parte assolutamente continua della derivata intrinseca di `u_n` è `∇_Σu_n=∇_Σg=G` quasi ovunque su ciascuna faccia. Quindi
   ```
   ∇_Σu_n 𝓗² = G 𝓗²
   ```
   per ogni `n`, e la convergenza debole-* delle misure è esatta, non soltanto asintotica.
4. La parte singolare è, per ogni `n`, il salto macroscopico già presente in `g`:
   ```
   D^s_Σu_n = [g]⊗ν_g 𝓗¹⌞J_g.
   ```
   La relazione generale di identificazione si riduce a
   ```
   D^s_Σu_n ⇀* (∇_Σg−G)𝓗² + [g]⊗ν_g 𝓗¹⌞J_g
               = [g]⊗ν_g 𝓗¹⌞J_g,
   ```
   perché `M=0`.
5. Infine `G_f^TG_f=I₂` implica rango tangenziale 2 su ogni faccia. Questo è un fatto a.e. per la mappa a tratti; non afferma continuità attraverso gli spigoli né embeddedness globale.

Tutte le condizioni della determining sequence sono quindi soddisfatte esattamente nel modello intrinseco dichiarato. ∎

## 3. Conseguenze energetiche — correzione importante

La successione determinante `u_n=g` non contiene strip continui e non concentra il salto in un gradiente dell'ordine `1/h`. Il costo lungo questa successione, per un integrando bulk `W` e densità interfaciale `ψ`, è
```
E(u_n) = ∫_Σ W(G) dA + ∫_{J_g} ψ([g],ν_g) dH¹,
```
indipendentemente da `n`. È quindi un concorrente ammissibile e fornisce un **limite superiore** per l'infimo rilassato.
indipendentemente da `n`. È un concorrente ammissibile. Per `ψ(a,ν)=|a|` e i due bulk specificati nella Sezione 3, il teorema di minimalità archiviato in `theorems/C60_CF_MINIMALITY_CONVEX_BULK_NORM_JUMP_2026-11-21.md` mostra che questo costo coincide con l'infimo rilassato.

Per `ψ(a,ν)=|a|`, l'integrale sui salti macroscopici è stato calcolato numericamente su tutti i 90 spigoli con quadratura trapezoidale (200 campioni per spigolo). Ne seguono i valori:
- `W(F)=|F|_F`: bulk `45.6365164300`; interfaccia `38.9347888585`; totale `84.5713052885`.
- `W(F)=|F|_F²`: bulk `64.5397804748`; stessa interfaccia `38.9347888585`; totale `103.4745693333`.

Il test `∫strip |∇g_h|² dA ~ C/h` riguarda invece la regolarizzazione continua strip+cap, che non è la successione CF qui costruita. Esso **non esclude** un'energia bulk quadratica nel problema CF. Per questa coppia e questa successione costante, entrambi i costi sono finiti. I valori sono energie di una successione ammissibile (con quadratura numerica per l'interfaccia), non l'infimo rilassato.

## 4. Cosa è dimostrato e cosa resta aperto

| Affermazione | Stato |
|---|---|
| `g∈SBV(Σ;R³)` nel modello poliedrale faccia-per-faccia | Provata nel documento formale |
| `∇_Σg=G` a.e. sulle facce, con la stessa carta tangenziale | Segue dalle definizioni `g_f` e `G_f`; mantenere esplicita la convenzione di base |
| `u_n=g` è determining sequence per `(g,G)` | Provata, nella formulazione intrinseca SBV su `Σ` |
| Immersione locale a.e. della successione | Segue da `G_f^TG_f=I₂` |
| Embeddedness/iniettività globale | Non dimostrata e non richiesta dalla nozione CF SBV |
| Formula di rilassamento `I(g,G)` e suo valore minimo | Aperta |
| Estensione rigorosa del teorema CF da domini euclidei a superfici poliedrali | Da enunciare come adattamento intrinseco; la prova della successione costante usa direttamente la decomposizione SBV sulle facce |

## 5. Generalizzazione se il campo bulk viene cambiato

Se in una futura versione si sceglie un campo `G̃` con `M=∇_Σg−G̃≠0`, la successione costante non è più determinante. In tal caso occorre costruire micro-salti che diffondano nel bulk la misura `M𝓗²`. Il problema è diverso e non va confuso con la coppia C60 attualmente definita, per la quale `M=0`.
| `I_W(g,G)` per `W(F)=|F|_F` o `|F|_F²`, `ψ(a,ν)=|a|` | Identificato dal teorema di minimalità dedicato |
| Rilassamento per densità interfaciali diverse da `|a|` | Aperto |
| Estensione rigorosa del teorema CF da domini euclidei a superfici poliedrali | Da enunciare come adattamento intrinseco; la prova della successione costante usa direttamente la decomposizione SBV sulle facce |

## 5. Generalizzazione per un campo bulk alternativo

Per un campo `G̃` costante su ciascuna faccia, anche con `M=∇_Σg−G̃≠0`, la successione costante non è determinante, ma una costruzione esplicita esiste: quantizzazione a gradini `q_h` e definizione `u_{h,f}=G̃_fξ+b_f+M_fq_h(ξ)`. Il gradiente assolutamente continuo è esattamente `G̃_f`; i salti interni della griglia generano nel limite `M_f𝓗²`. La costruzione globale e le stime sono dimostrate in `theorems/C60_CF_NONZERO_BULK_DISARRANGEMENT_2026-11-21.md`. L'ottimalità energetica, soprattutto per densità 1-omogenee, resta un problema separato.

## Riferimento teorico

Barroso, Matias, Morandotti & Owen, *Explicit Formulas for Relaxed Disarrangement Densities Arising from Structured Deformations*, Math. Mech. Complex Systems 5 (2017), 163–189, DOI: 10.2140/memocs.2017.5.163. La formulazione CF usa `u_n→g` in `L¹` e la convergenza delle parti assolutamente continue `∇u_n` a `G` nel senso delle misure; la parte singolare limite soddisfa
`(∇g−G)𝓛^N+[g]⊗ν_g𝓗^{N−1}`.
La presente proposizione è la verifica diretta del caso `∇_Σg−G=0` sul complesso poliedrale C60.
La presente proposizione è la verifica diretta del caso `∇_Σg−G=0` sul complesso poliedrale C60. Per l'identificazione dell'infimo con salto normato si veda `theorems/C60_CF_MINIMALITY_CONVEX_BULK_NORM_JUMP_2026-11-21.md`.
