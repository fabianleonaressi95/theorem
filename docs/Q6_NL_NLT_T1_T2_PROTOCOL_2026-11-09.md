# Q6 NL/NLT: protocollo congelato T1–T2

Versione: \`Q6-NL/NLT-T1-T2-v1\`
Data: 2026-11-09

## 1. Campo vettoriale congelato

Il complesso è il 2-scheletro cubicale Q6: 64 vertici, 192 spigoli, 240 facce quadrate. Le matrici di incidenza sono \`B1\` (64×192) e \`B2\` (192×240), con \`B1 @ B2 = 0\`.

Parametri d'ordine:

\[
R_0=\left|\frac1{64}\sum_{i=1}^{64}e^{i\theta_i}\right|,\quad
R_{1d}=\left|\frac1{192}\sum_{e=1}^{192}e^{i(B_1\phi)_e}\right|,\quad
R_{1u}=\left|\frac1{240}\sum_{f=1}^{240}e^{i(B_2^T\phi)_f}\right|.
\]

Entrambi i modelli hanno:

\[
\dot\theta=\omega-\sigma R_{1d}B_1\sin(B_1^T\theta).
\]

NL:

\[
\dot\phi=\widetilde\omega-\sigma R_0B_1^T\sin(B_1\phi)
-\sigma B_2\sin(B_2^T\phi).
\]

NLT:

\[
\dot\phi=\widetilde\omega-\sigma R_0R_{1u}B_1^T\sin(B_1\phi)
-\sigma R_{1d}B_2\sin(B_2^T\phi).
\]

Il seno è componente per componente. Queste equazioni sono implementate in \`models/q6_topological_synchronization.py::rhs\` e non devono essere cambiate durante T1–T4 senza una nuova versione del protocollo.

## 2. Convenzione dei frame

- T1 omogeneo: \`omega=0\` e \`omega_link=0\`.
- T2 eterogeneo: frequenze gaussiane come nel modello sorgente. La media comune dei nodi è rimossa nel frame dei nodi; la media delle frequenze degli spigoli è mantenuta.
- Non si applica una rotazione uniforme aggiuntiva a \`phi\`: in generale essa modifica \`B1 phi\` e \`B2.T phi\` e non è una simmetria automatica del campo.

## 3. T1 — punti fissi omogenei

- Griglia: \`sigma=0,0.05,...,2.00\`.
- Almeno 200 condizioni iniziali indipendenti per ogni sigma e modello.
- Newton in coordinate ridotte, fissando \`theta[0]=0\` per eliminare il modo neutro della fase globale.
- Deduplicazione dei punti fissi modulo la fase globale comune dei nodi.
- Jacobiana numerica centrale del campo ridotto e classificazione mediante la massima parte reale degli autovalori.
- Un punto è classificato linearmente stabile se la massima parte reale è minore di \`-1e-7\`.

La ricerca multistart fornisce un numero di radici trovate, non una prova di completezza. A sigma=0 possono esistere famiglie continue di punti fissi; non vanno etichettate come attrattori isolati.

## 4. T2 — dinamica eterogenea

- 20 seed di fase, due famiglie: inizializzazione quasi allineata e casuale.
- Identica realizzazione di frequenze per le due famiglie e per tutti i seed di fase.
- RK4, \`dt=0.025\` nel run di riferimento.
- Osservabili a \`T,2T,4T\`, con \`T=640\` passi come minimo.
- Output per ogni seed: \`R0,R1_down,R1_up\`, differenza appaiata in R0 e statistiche aggregate.

Soglie preregistrate per T2: separazione media assoluta in R0 > 0.2 e maggiore di 3 deviazioni standard delle differenze appaiate, con almeno 20 seed. La persistenza temporale va valutata confrontando le separazioni a T e 4T; T2 da solo non sostituisce T3.

## 5. Implementazione e riproducibilità

Esecuzione:

\`\`\`bash
python scripts/run_q6_nl_nlt_t1_t2.py \\
  --sigmas 0.00,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.00,1.05,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.65,1.70,1.75,1.80,1.85,1.90,1.95,2.00 \\
  --t1-starts 200 --T-steps 640 --dt 0.025 \\
  --output artifacts/q6_nl_nlt_t1_t2.json
\`\`\`

Il JSON registra la revisione Git, le versioni di Python/NumPy, le frequenze, i seed, il frame e i risultati. Il workflow \`q6-nl-nlt-t1-t2.yml\` esegue il protocollo e conserva il JSON come artifact.

## 6. Limiti espliciti

Questo commit implementa T1 e T2. Non dichiara bistabilità dimostrata. Restano da implementare T3 (sweep avanti/indietro con dwell 640, 2560, 10240), T4 (Q4/Q5/Q6), dimezzamento di dt e confronto con un integratore indipendente. La conclusione resta **non dimostrata** finché non sono soddisfatti tutti i criteri preregistrati.

## 7. T3 — sweep avanti/indietro e persistenza rispetto al dwell

Lo script `scripts/run_qn_nl_nlt_t3_t4.py` implementa il test di isteresi per ciascun modello e dimensione. Per ogni seed e dwell:
- genera una sola realizzazione delle frequenze e la riutilizza nei due rami;
- esegue lo sweep crescente in `sigma`;
- avvia lo sweep decrescente dallo stato terminale del ramo crescente;
- registra `R0`, `R1_down` e `R1_up` a ogni valore di `sigma`.

Per rendere non ambiguo il termine «gap», la statistica preregistrata è la media, sulla griglia di `sigma`, della differenza assoluta tra i due rami per `R0`. Sono inoltre conservati il massimo gap e tutti i valori per `sigma`. Non si confonde questa quantità con l'area integrale del ciclo.

Dwell: 640, 2560 e 10240 passi. Il criterio T3 richiede che il gap medio al dwell più lungo sia almeno metà di quello al dwell più breve e che i tre valori siano non decrescenti. Il report mantiene separati i gap di `R0`, `R1_down` e `R1_up`.

## 8. T4 — confronto cubicale Q4/Q5/Q6

La costruzione è generica: vertici come bitstring, spigoli orientati lungo una coordinata e quadrati orientati come bordi di facce coordinate. Prima della dinamica viene verificato esattamente `B1 @ B2 = 0`. I conteggi attesi sono:
- Q4: 16 vertici, 32 spigoli, 24 quadrati;
- Q5: 32 vertici, 80 spigoli, 80 quadrati;
- Q6: 64 vertici, 192 spigoli, 240 quadrati.

Si usano gli stessi seed, griglia di `sigma`, dwell e convenzione delle frequenze per tutte le dimensioni. Il criterio di persistenza di taglia è `gap_R0(Q6) >= 0.5 * gap_R0(Q4)`, confrontato separatamente per modello e dwell. Q5 è mantenuto come controllo intermedio, non sostituisce il confronto Q4/Q6.

Esecuzione di riferimento:

```bash
python scripts/run_qn_nl_nlt_t3_t4.py \\
  --dimensions 4,5,6 \\
  --sigmas 0.00,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.00,1.05,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.65,1.70,1.75,1.80,1.85,1.90,1.95,2.00 \\
  --seeds 11,23,37,51,67,79,97,109,127,139,151,163,179,191,211,223,239,251,263,277 \\
  --dwells 640,2560,10240 --dt 0.025 \\
  --output artifacts/q6_nl_nlt_t3_t4.json
```

Il costo computazionale è elevato: il protocollo completo va eseguito come job dedicato e non è dichiarato eseguito dal solo fatto che lo script sia stato aggiunto. Il JSON registra dimensioni, audit dei complessi, seed, frequenze, dwell, traiettorie e statistiche. Le verifiche T3/T4 restano non valutate fino alla produzione e al controllo dell'artifact.
