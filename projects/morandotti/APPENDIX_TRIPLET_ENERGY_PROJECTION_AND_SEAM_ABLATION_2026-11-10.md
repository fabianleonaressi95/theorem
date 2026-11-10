# Lettura meccanica dei tripletti: proiezione delle energie di pannelli e cuciture

Questa nota accompagna lo script `scripts/audit_morandotti_triplet_energy_projection.py`.

## Obiettivo

Non basta osservare che il sottospazio rotazionale RGS trasferito ha dimensione tre e forma angoli piccoli con i tre modi più bassi della shell. Per renderlo utile a Morandotti dobbiamo chiedere: **quali termini della rigidezza del pallone agiscono su quel sottospazio?**

Sia (B\in\mathbb R^{276\times3}) una base ortonormale ambientale del tripletto trasferito, dopo proiezione sui piani tangenti locali. La matrice di rigidezza ridotta del tripletto è
\[
K_{eff}=B^TKB\in\mathbb R^{3\times3}.
\]
La matrice è simmetrica. I suoi tre autovalori sono invarianti rispetto a una rotazione ortogonale della base (B); perciò sono più significativi delle tre colonne prese singolarmente.

## Separazione dei contributi

La shell implementata ha:
- energia membranale CST ortotropa;
- energia flessionale di cerniera sui bordi interni dei pannelli;
- contributo di cerniera aggiuntivo sui bordi di cucitura;
- eventuale rinforzo lineare delle cuciture.

La decomposizione è
\[
K=K_{mem}+K_{hinge,panel}+K_{hinge,seam}+K_{line,seam}.
\]
Per ciascun contributo:
\[
K_{eff}^{(a)}=B^TK_aB.
\]
Si riportano matrice (3\times3), autovalori, traccia e norma di Frobenius. La quota di traccia
\[
f_a=\frac{\operatorname{tr}K_{eff}^{(a)}}
{\sum_b\operatorname{tr}K_{eff}^{(b)}}
\]
fornisce una misura sintetica del contributo energetico medio sul sottospazio. Non sostituisce l'analisi dei singoli autovalori e non è una frazione universale indipendente dalla base materiale o dalla configurazione.

## Ablation numerica

Il solver esistente restituisce la matrice globale (K), ma non espone separatamente i blocchi. Lo script ricostruisce i contributi per differenza tra assemblaggi con gli stessi parametri:
1. un assemblaggio con fattore di cerniera interno piccolo (epsilon=10^{-3});
2. un assemblaggio con fattore interno unitario e fattore cucitura nullo;
3. un assemblaggio con fattore interno unitario e fattore cucitura impostato al valore richiesto;
4. se (E_st_s\ne0), un ulteriore assemblaggio con rinforzo lineare.

Il fattore (epsilon>0) evita di risolvere il sistema membranale puro, che presenta meccanismi flessionali fuori piano. Si ricava
\[
K_{hinge,panel}=\frac{K(1,0)-K(\epsilon,0)}{1-\epsilon},
\qquad
K_{mem}=K(\epsilon,0)-\epsilon K_{hinge,panel}.
\]
Il contributo addizionale delle cerniere di cucitura è
\[
K_{hinge,seam}=K(1,s)-K(1,0),
\]
dove (s) è il moltiplicatore di rigidezza delle cuciture. Il rinforzo lineare è la differenza tra assemblaggio con e senza (E_st_s).

La somma dei blocchi viene confrontata con la matrice globale originale; il residuo relativo è riportato. Se il residuo non è piccolo, la decomposizione non va interpretata.

## Confronto spettrale

Lo script ricostruisce la tripletta rotazionale RGS da (e_a\times X_i), la trasferisce 64→92, la proietta sul tangente locale (T\in\mathbb R^{276\times184}) e la confronta con i tre autovettori più bassi di (K_{tan}). Riporta:
- angoli principali tra i sottospazi;
- gap tra terzo e quarto autovalore;
- matrici (B^TK_aB);
- autovalori e tracce per contributo;
- residuo di ricostruzione additiva della rigidezza.

L'angolo misura l'allineamento geometrico; il gap misura quanto il sottospazio basso sia separato dal resto dello spettro; le matrici proiettate misurano come i meccanismi implementati contribuiscano alla rigidezza del tripletto.

## Esecuzione

\`\`\`bash
python scripts/audit_morandotti_triplet_energy_projection.py \\
  --neighbors 16 --E1 1000 --E2 700 --nu12 0.25 --G12 300 \\
  --thickness 0.02 --seam-bending-factor 4 --seam-Et 0 \\
  --out reports/morandotti_triplet_energy_projection.json
\`\`\`

Lo script produce JSON e NPZ. Il risultato va archiviato con i parametri effettivi e la versione della mesh.

## Limiti e interpretazione

- I parametri di default sono dimostrativi, non misure del pallone reale.
- La shell è lineare: CST membranale più cerniere diedrali. Non comprende contatto, pieghe, danno, slip adesivo o omogeneizzazione della trama.
- Il tripletto è quello rotazionale definito cinematicamente nella sorgente RGS; non è stato identificato come (T_{2u}).
- La mesh del pallone ha geometria icosaedrica/troncato-icosaedrica; non si impone automaticamente la simmetria cubica (O_h).
- La proiezione delle energie è un audit numerico del modello costitutivo, non una validazione sperimentale.
- Le singole colonne di (B) possono ruotare tra esecuzioni; interpretare autovalori, tracce e invarianti del sottospazio, non il “modo 1/2/3” senza una convenzione aggiuntiva.

## Domanda sperimentale

Dopo la calibrazione dei moduli ortotropi e delle cuciture su provini, la stessa analisi deve essere ripetuta su scansioni del pallone sotto pressione e carico. La domanda verificabile è se il contributo delle cuciture cambia in modo misurabile la rigidezza e lo splitting del sottospazio rotazionale trasferito, e se la previsione coincide con gli spostamenti osservati. Solo successivamente si potrà collegare la forma deformata e l'orientazione delle cuciture al modello aerodinamico del Magnus.
