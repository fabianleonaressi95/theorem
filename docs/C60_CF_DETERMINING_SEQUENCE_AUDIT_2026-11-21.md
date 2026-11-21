# C60 — audit della determining sequence Choksi–Fonseca

Data: 2026-11-21  
Classificazione: **correzione matematica necessaria; rilassazione C60 ancora aperta**  
Ambito: successione continua strip+cap descritta in `scripts/c60_dpo_energy.py` e in `docs/C60_DPO_FORMAL_PROOF_2026-11-21.md`.

## 1. Definizione CF da usare

Nel quadro Choksi–Fonseca una structured deformation è una coppia
`(g,G)` con `g ∈ SBV(Ω;R^d)` e `G ∈ L¹(Ω;R^{d×N})`. Una determining sequence
è una successione `u_n ∈ SBV` tale che

```
u_n → g in L¹,
∇u_n 𝓛^N ⇀* G 𝓛^N
```

dove `∇u_n` è la parte assolutamente continua della derivata di `u_n`.
Non è la convergenza delle derivate distribuzionali `Du_n ⇀* Dg`.

La decomposizione SBV del limite è
```
Dg = ∇g 𝓛^N + [g]⊗ν_g 𝓗^{N−1}⌞J_g.
```
Dalla convergenza `u_n → g` in `L¹` segue `Du_n → Dg` in distribuzioni.
Poiché
```
Du_n = ∇u_n 𝓛^N + D^s u_n,
```
e `∇u_n 𝓛^N ⇀* G 𝓛^N`, la parte singolare degli approssimanti deve soddisfare
```
D^s u_n ⇀* (∇g − G) 𝓛^N
             + [g]⊗ν_g 𝓗^{N−1}⌞J_g.
```
Il termine diffuso `(∇g−G)𝓛^N` è prodotto da salti microscopici che si
distribuiscono nel bulk. Il salto macroscopico di `g` resta una componente
distinta. Questo è precisamente il meccanismo che non può essere eliminato
sostituendo gli approssimanti SBV con una successione continua senza cambiare
la nozione di convergenza.

Riferimenti consultati:
- Choksi–Fonseca (1997), *Bulk and Interfacial Energies for Structured Deformations of Continua*, ARMA 138, 37–103, in particolare Def. 2.11, Thm. 2.12 e Remark 2.13.
- *Explicit Formulas for Relaxed Disarrangement Densities Arising from Structured Deformations*, MFO/Mathematics of Materials in Contexts, 2017, che riporta la definizione CF e la decomposizione del limite delle parti singolari.

## 2. Conseguenza per la successione C60 attualmente implementata

Il codice e la prova descrivono `g_h` come **continua** (strip+cap), quindi, se
`g_h ∈ W^{1,1}(Σ;R³)`, vale
```
D_Σ g_h = ∇_Σ g_h 𝓗².
```
Se inoltre `g_h → g` in `L¹` e le misure `∇_Σg_h 𝓗²` sono uniformemente
limitate e convergono debolmente-* come misure, il limite è necessariamente
`D_Σg`. Per il candidato a salti sugli spigoli:
```
D_Σg = G 𝓗² + [g]⊗ν_g 𝓗¹⌞J_g,
```
che non coincide con `G 𝓗²` quando il salto macroscopico è non nullo.

**Conclusione:** la successione continua strip+cap non è, in generale, una
determining sequence CF per la coppia `(g,G)` indicata nel progetto. Essa
può essere una successione di regolarizzazione BV di `g`, ma la convergenza
`∇g_h 𝓗² ⇀* Dg` è la convergenza sbagliata per identificare il campo `G`
di una structured deformation.

Per costruire una vera determining sequence per `(g,G)` occorre una
successione `u_n ∈ SBV` con micro-jump set non vuoto in generale, tale che
`∇u_n 𝓗² ⇀* G 𝓗²`. Le parti singolari `D^s u_n` devono allora generare il
limite diffuso `(∇g−G)𝓗²` oltre al salto macroscopico di `g`. Non basta
ammorbidire tutti gli spigoli rendendo ogni approssimante continuo.

## 3. Riclassificazione del calcolo energetico

I numeri archiviati restano risultati numerici del codice:
- bulk TV nominale: 45.6365164300;
- massa nominale dei salti: 38.9347888585;
- somma: 84.5713052885;
- stime scalate di `∫strip |∇g_h|²`: 129.8960, 229.7719, 444.4263.

Ma la somma 84.5713 **non è stata dimostrata come energia CF di `(g,G)`**.
Per la successione continua essa è interpretabile come candidato al costo TV
della regolarizzazione che converte il salto in gradiente concentrato nello
strip, a condizione che la quadratura e la costruzione siano validate.
Non è il valore dell'infimo CF, né una prova che la successione sia
determining per la coppia strutturata.

Il test quadratico è un'evidenza numerica coerente con crescita `C/h` per
questa discretizzazione e questo schema; non prova da solo un limite
asintotico. Il calcolo degli strip campiona 20 spigoli su 90 e moltiplica per
`90/20`: i valori sono stime campionarie scalate, non integrazione esaustiva.

## 4. Correzioni necessarie ai documenti

1. Rimuovere la frase che afferma `∇g_h ⇀* Dg` come proprietà CF della
   determining sequence.
2. Non classificare come provata la verifica CF (A4) per la successione
   continua.
3. Non chiamare 84.5713052885 `I(g,G)`; denominarlo
   `E_TV^{candidate}(g_h)` o costo TV candidato della regolarizzazione.
4. Mantenere separati `Dg`, `G𝓗²`, `(∇g−G)𝓗²` e
   `[g]⊗ν_g 𝓗¹⌞J_g`.
5. Non inferire dalla divergenza numerica quadratica che la crescita lineare
   sia l'unica energia ammissibile. La scelta di `W,ψ` e le ipotesi di
   rilassamento devono essere dichiarate e verificate separatamente.

## 5. Programma corretto

- **A. Convenzione dei campi:** fissare in modo univoco la mappa macroscopica
  `g`, il campo `G` e quindi `M=∇_Σg−G`.
- **B. Costruzione CF:** costruire `u_n∈SBV(Σ;R³)` con micro-salti e provare
  `u_n→g` in `L¹`, `∇_Σu_n𝓗²⇀*G𝓗²`.
- **C. Identità di bilancio:** provare che
  `D^s_Σu_n⇀*(∇_Σg−G)𝓗²+[g]⊗ν_g𝓗¹⌞J_g`.
- **D. Energia:** valutare `E(u_n)=∫W(∇u_n)dA+∫_{J_{u_n}}ψ([u_n],ν)dH¹`
  sulla vera successione CF.
- **E. Rilassazione:** confrontare il costo della successione costruita con
  il cell formula CF; solo il limite inferiore universale e una recovery
  sequence ottimale possono identificare l'infimo.

## 6. Stato

| Affermazione | Stato aggiornato |
|---|---|
| Decomposizione SBV faccia per faccia di `g` | Provata nel modello poliedrale, con convenzioni di traccia esplicite |
| `G^TG=I₂ ⇒ rank G=2` | Provata algebricamente |
| Valori numerici TV/quadratico dello schema strip | Archiviati; quadratura strip campionaria |
| `g_h` continuo determina la coppia CF `(g,G)` | **Falso in generale** se `[g]≠0` e si richiede il limite CF `G𝓗²` |
| Esistenza di una vera determining sequence CF C60 | Aperta |
| Formula di rilassamento e valore `I(g,G)` | Aperta |

**Classificazione complessiva:** il calcolo energetico è un audit numerico di
una regolarizzazione continua; la costruzione CF per la coppia `(g,G)` e la
sua rilassazione restano problemi aperti.
