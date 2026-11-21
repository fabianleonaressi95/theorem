# C60 — audit della determining sequence Choksi–Fonseca

Data: 2026-11-21  
Classificazione: **correzione matematica necessaria; rilassazione C60 ancora aperta**  
Classificazione: **successione determinante e due casi energetici identificati; rilassazione generale ancora aperta**  
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
La somma 84.5713 è il costo della successione costante `u_n=g` per
`W(F)=|F|_F` e `ψ(a,ν)=|a|`; poiché `∇_Σg=G`, questa è una determining
sequence CF. La semicontinuità inferiore della variazione totale del salto
e del bulk prova che il costo coincide con l'infimo in questo caso.
Analogamente, per `W(F)=|F|_F²` e la stessa densità interfaciale, il totale
103.47456933 coincide con l'infimo. Le cifre interfaciali restano quadrature
numeriche su tutti i 90 spigoli, non valori simbolici esatti. La prova è in
`theorems/C60_CF_MINIMALITY_CONVEX_BULK_NORM_JUMP_2026-11-21.md`.

Il test quadratico è un'evidenza numerica coerente con crescita `C/h` per
la regolarizzazione continua; non prova da solo un limite asintotico e non
esclude un bulk quadratico per il problema CF. La successione costante
`u_n=g` ha energia finita anche per `W(F)=|F|²`: bulk `64.53978047`
più interfaccia `38.93478886`, totale `103.47456933`. Per crescita
lineare il costo della stessa successione è `84.57130529`.

Precisazione sui campionamenti: il codice integra l'interfaccia `ψ(s)=s`
su tutti i 90 spigoli con 200 campioni per spigolo. È invece l'integrale
quadratico degli strip continui che campiona 20 spigoli e scala per `90/20`.


## 4. Correzioni necessarie ai documenti
## 4. Disarrangiamento bulk non nullo

Per un campo alternativo `G̃` costante su ciascuna faccia, si pone
`M_f=∇_Σg|_f−G̃_f` e si usa il quantizzatore cartesiano
`q_h(ξ)=h floor(ξ₁/h)e₁+h floor(ξ₂/h)e₂`. La mappa
`u_{h,f}=G̃_fξ+b_f+M_fq_h(ξ)` soddisfa `u_h→g` uniformemente,
`∇_Σu_h=G̃` esattamente a.e. per ogni scala e
`D^s_Σu_h⇀*M𝓗²+[g]⊗ν_g𝓗¹`. La variazione totale è uniformemente limitata.
Questo chiude l'esistenza di una determining sequence per `M≠0` nel caso
faccia-per-faccia costante. Il costo micro-interfaciale scala come
`h^{p−1}` per `ψ=|a|^p`; l'ottimalità per `p=1` non è identificata.
faccia-per-faccia costante. Il costo della griglia cartesiana scala come
`h^{p−1}` per `ψ=|a|^p`. Per `p=1`, il cell problem isotropo è ora
identificato esattamente: `C(M_f)=||M_f||_*`, con limite inferiore duale
e recupero SVD. Il caso rango uno è un corollario, poiché
`||M_f||_*=||M_f||_F` per matrici di rango uno.
Prove: `theorems/C60_CF_NONZERO_BULK_DISARRANGEMENT_2026-11-21.md` e
`theorems/C60_CF_NUCLEAR_NORM_CELL_AND_BULK_OPTIMIZATION_2026-11-21.md`.
faccia-per-faccia costante. Il costo micro-interfaciale scala come
`h^{p−1}` per `ψ=|a|^p`. Per `p=1` il cell problem è risolto: la griglia
cartesiana non è ottimale, ma la costruzione SVD lo è e il costo minimo è
la norma nucleare `‖M_f‖_*` per unità di area
(`theorems/C60_CF_NUCLEAR_NORM_CELL_PROBLEM_2026-11-21.md`).
Prova: `theorems/C60_CF_NONZERO_BULK_DISARRANGEMENT_2026-11-21.md`.

## 5. Estensione al costo interfaciale quadratico

Per `ψ₂(a,ν)=|a|²`, la variazione totale non dà un limite inferiore positivo
sul salto macroscopico. È stata costruita una recovery sequence globale per
il complesso C60: su una striscia di larghezza `δ_m` interna a una faccia,
ciascun salto viene ripartito in `m` salti paralleli di ampiezza `O(1/m)`;
le zone terminali hanno lunghezza `r_m→0`. Le stime danno costo
`O(1/m+δ_m+r_m)→0`, con convergenza CF e costo bulk convergente a
`∫_ΣW(G)`. Pertanto, per `W=|F|_F` o `W=|F|_F²`, il rilassamento con
`ψ₂=|a|²` è il solo costo bulk. La costruzione è in
`theorems/C60_CF_QUADRATIC_JUMP_RELAXATION_2026-11-21.md`.

## 6. Correzioni necessarie ai documenti

1. Rimuovere la frase che afferma `∇g_h ⇀* Dg` come proprietà CF della
   determining sequence.
2. Non classificare come provata la verifica CF (A4) per la successione
   continua.
3. Non chiamare 84.5713052885 `I(g,G)`; denominarlo
   `E_TV^{candidate}(g_h)` o costo TV candidato della regolarizzazione.
3. Per `ψ=|a|`, i valori 84.5713052885 e 103.4745693333 identificano
   rispettivamente `I_{W_1}(g,G)` e `I_{W_2}(g,G)`, con interfaccia
   quadraturata numericamente. Non attribuire questa conclusione a densità
   interfaciali diverse.
4. Mantenere separati `Dg`, `G𝓗²`, `(∇g−G)𝓗²` e
   `[g]⊗ν_g 𝓗¹⌞J_g`.
5. Non inferire dalla divergenza numerica quadratica che la crescita lineare
   sia l'unica energia ammissibile. La scelta di `W,ψ` e le ipotesi di
   rilassamento devono essere dichiarate e verificate separatamente.

## 5. Programma corretto
## 7. Programma corretto

- **A. Convenzione dei campi:** fissare in modo univoco la mappa macroscopica
  `g`, il campo `G` e quindi `M=∇_Σg−G`.
- **B. Caso C60 corrente:** `u_n=g` è determining sequence perché `M=0`;
  verificare e mantenere la coerenza delle coordinate tangenziali usate per
  `∇_Σg=G`.
- **C. Generalizzazione:** se si sceglie un campo `G̃` con
  `∇_Σg−G̃≠0`, costruire micro-salti e provare il bilancio
  `D^s_Σu_n⇀*(∇_Σg−G̃)𝓗²+[g]⊗ν_g𝓗¹⌞J_g`.
- **D. Energia:** valutare `E(u_n)=∫W(∇u_n)dA+∫_{J_{u_n}}ψ([u_n],ν)dH¹`
  sulla vera successione CF.
- **E. Ottimalità per `M≠0`:** la successione esiste, ma il costo micro-
  interfaciale per densità 1-omogenee non è ancora ottimizzato; serve un cell
  problem per la matrice `M_f`.
- **E. Rilassazione:** confrontare il costo della successione costruita con
  il cell formula CF; solo il limite inferiore universale e una recovery
  sequence ottimale possono identificare l'infimo.

## 6. Stato
- **E. Ottimalità per `M≠0`:** risolta per `ψ(a,ν)=|a|`; il costo ottimale
  per faccia è `|f| ||M_f||_*`. Restano da studiare densità anisotrope o
- **E. Ottimalità per `M≠0`:** risolta per `ψ(a,ν)=|a|` — la densità di
  cella è la norma nucleare `‖M_f‖_*`; restano le densità anisotrope o
  dipendenti dalla normale.
- **F. Rilassazione generale:** restano da studiare densità interfaciali
  anisotrope/non separabili e bulk non convessi; i casi `M=0`, `ψ=|a|` e
  `ψ=|a|²` con i due bulk indicati sono identificati nei teoremi dedicati.

## 8. Stato

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
| Determining sequence CF per la coppia C60 corrente (`M=0`) | **Provata:** `u_n=g` |
| Costruzione CF per campi bulk alternativi con `M≠0` | **Provata** per campi costanti faccia-per-faccia |
| `I_W(g,G)` per `W=|F|_F` o `|F|_F²`, `ψ=|a|` | **Identificato** dal teorema dedicato |
| `I_{W,2}(g,G)` per `ψ=|a|²` e i due bulk indicati | **Identificato:** costo interfaciale rilassato nullo |
| Determining sequence per `G̃` costante faccia-per-faccia, `M≠0` | **Provata** mediante quantizzazione a gradini |
| Ottimalità del costo interfaciale per `M≠0`, `ψ=|a|` | Aperta: cell problem |
| Cell problem isotropo lineare per `M_f` | **Provato:** costo nucleare, recupero SVD |
| Ottimizzazione `|G|_F² + λ||A−G||_*` | **Formula dimostrata**; script committato, test automatico non ancora eseguito |
| Ottimalità del costo interfaciale per `M≠0`, `ψ=|a|` | **Provata:** `Σ_f |f| ||M_f||_*` |
| Densità interfaciali non normate, ad es. `ψ=|a|²` | Aperta |

**Classificazione complessiva:** la coppia C60 corrente ha una determining
sequence esplicita `u_n=g`. Per `M≠0` e `ψ=|a|`, il costo micro-interfaciale
ottimale è la norma nucleare. Il problema penalizzato con bulk quadratico è
risolto per faccia mediante soft-thresholding. Restano aperti il rilassamento
per densità interfaciali anisotrope o dipendenti dalla normale e la
generalizzazione integrale CF alla classe generale delle superfici poliedrali.
| `I_W(g,G)` per `W=|F|_F` o `|F|_F²`, `ψ=|a|` | **Identificato** dal teorema dedicato |
| `I_{W,2}(g,G)` per `ψ=|a|²` e i due bulk indicati | **Identificato:** costo interfaciale rilassato nullo |
| Determining sequence per `G̃` costante faccia-per-faccia, `M≠0` | **Provata** mediante quantizzazione a gradini |
| Ottimalità del costo interfaciale per `M≠0`, `ψ=|a|` | **Identificata:** norma nucleare `‖M_f‖_*` (cell problem SVD) |
| Densità interfaciali non normate o anisotrope (`ψ=|a|²` per `M=0` è già identificata: rilassamento nullo) | Aperta |

**Classificazione complessiva:** la coppia C60 corrente ha una determining
sequence esplicita `u_n=g`. I funzionali con `W=|F|_F` o `W=|F|_F²` e
`ψ=|a|` sono identificati. Restano aperti l'ottimalità energetica per `M≠0`, il rilassamento per
 densità interfaciali anisotrope più generali e la generalizzazione integrale
CF alla classe generale delle superfici poliedrali.
`ψ=|a|` sono identificati. Per `M≠0` con `G̃` costante faccia per faccia,
l'esistenza della determining sequence è provata e, per `ψ=|a|`, il costo
micro-interfaciale ottimale è la norma nucleare `‖M_f‖_*`. Restano aperti
il rilassamento per densità interfaciali anisotrope o dipendenti dalla
normale, i campi bulk variabili dentro le facce e la generalizzazione
integrale CF alla classe generale delle superfici poliedrali.
