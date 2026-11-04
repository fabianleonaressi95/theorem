# Vetri di spin — bibliografia scientifica e collegamento Q6

Questa cartella raccoglie fonti esterne sul modello Edwards–Anderson, sul modello Sherrington–Kirkpatrick, sulla soluzione di Parisi, sui risultati matematici rigorosi e sui sistemi a corto raggio. Le voci sono distinte per funzione: modello, review, risultato matematico, dinamica o simulazione.

## A. Modelli fondativi

| Riferimento | Metadati | Ruolo |
|---|---|---|
| S. F. Edwards, P. W. Anderson, “Theory of spin glasses” | *Journal of Physics F: Metal Physics* 5, 965–974 (1975), DOI [10.1088/0305-4608/5/5/017](https://doi.org/10.1088/0305-4608/5/5/017) | Modello EA con interazioni casuali a corto raggio |
| D. Sherrington, S. Kirkpatrick, “Solvable Model of a Spin-Glass” | *Physical Review Letters* 35, 1792–1796 (1975), DOI [10.1103/PhysRevLett.35.1792](https://doi.org/10.1103/PhysRevLett.35.1792) | Modello SK mean-field a interazioni infinite |
| S. Kirkpatrick, D. Sherrington, “Infinite-ranged models of spin-glasses” | *Physical Review B* 17, 4384–4403 (1978), DOI [10.1103/PhysRevB.17.4384](https://doi.org/10.1103/PhysRevB.17.4384) | Estensione dei modelli mean-field, Ising e XY |
| D. J. Thouless, P. W. Anderson, R. G. Palmer, “Solution of ‘Solvable model of a spin glass’” | *Philosophical Magazine* 35, 593–601 (1977), DOI [10.1080/14786437708235992](https://doi.org/10.1080/14786437708235992) | Equazioni TAP e stati metastabili |
| J. R. L. de Almeida, D. J. Thouless, “Stability of the Sherrington-Kirkpatrick solution of a spin glass model” | *Journal of Physics A* 11, 983–990 (1978), DOI [10.1088/0305-4470/11/5/028](https://doi.org/10.1088/0305-4470/11/5/028) | Stabilità AT della soluzione replica-simmetrica |

## B. Rottura di simmetria delle repliche e struttura degli stati

| Riferimento | Metadati | Ruolo |
|---|---|---|
| G. Parisi, “Infinite Number of Order Parameters for Spin-Glasses” | *Physical Review Letters* 43, 1754–1757 (1979), DOI [10.1103/PhysRevLett.43.1754](https://doi.org/10.1103/PhysRevLett.43.1754) | Ansatz RSB con gerarchia di parametri d'ordine |
| G. Parisi, “The order parameter for spin glasses: a function on the interval 0–1” | *Journal of Physics A* 13, 1101–1112 (1980), DOI [10.1088/0305-4470/13/3/042](https://doi.org/10.1088/0305-4470/13/3/042) | Funzione d'ordine continua |
| M. Mézard, G. Parisi, N. Sourlas, G. Toulouse, M. Virasoro, “Replica symmetry breaking and the nature of the spin glass phase” | *Journal de Physique* 45, 843–854 (1984) | Sintesi della struttura RSB |
| F. Guerra, “Broken replica symmetry bounds in the mean field spin glass model” | *Communications in Mathematical Physics* 233, 1–12 (2003), DOI [10.1007/s00220-002-0773-5](https://doi.org/10.1007/s00220-002-0773-5) | Limite rigoroso inferiore per l'energia libera |
| M. Talagrand, “The Parisi formula” | *Annals of Mathematics* 163, 221–263 (2006), DOI [10.4007/annals.2006.163.221](https://doi.org/10.4007/annals.2006.163.221) | Dimostrazione della formula di Parisi per SK |
| D. Panchenko, “The Parisi ultrametricity conjecture” | *Annals of Mathematics* 177, 383–393 (2013), DOI [10.4007/annals.2013.177.1.8](https://doi.org/10.4007/annals.2013.177.1.8) | Teorema di ultrametricità sotto le ipotesi Ghirlanda–Guerra |

## C. Review, sistemi a corto raggio e dinamica

| Riferimento | Metadati | Ruolo |
|---|---|---|
| K. Binder, A. P. Young, “Spin glasses: Experimental facts, theoretical concepts, and open questions” | *Reviews of Modern Physics* 58, 801–976 (1986), DOI [10.1103/RevModPhys.58.801](https://doi.org/10.1103/RevModPhys.58.801) | Review fondamentale: esperimenti, modelli, simulazioni e questioni aperte |
| M. Mézard, “Spin glass theory and its new challenge: structured disorder” | *Indian Journal of Physics* (2024), DOI [10.1007/s12648-023-03029-8](https://doi.org/10.1007/s12648-023-03029-8) | Disordine strutturato e nuove classi di modelli |
| A. Bovier, I. Kurkova, “Rigorous results on some simple spin glass models” | *Markov Processes and Related Fields* 9, 209–242 (2003), DOI [10.20347/WIAS.PREPRINT.749](https://doi.org/10.20347/WIAS.PREPRINT.749) | Risultati rigorosi su modelli GREM e cascata ultrametrica |
| N. Read, “Short-range Ising spin glasses: The metastate interpretation of replica symmetry breaking” | *Physical Review E* 90, 032142 (2014), DOI [10.1103/PhysRevE.90.032142](https://doi.org/10.1103/PhysRevE.90.032142) | Metastati e interpretazione RSB a corto raggio |
| D. Sherrington, S. Kirkpatrick, “50 years of spin glass theory” | *Nature Reviews Physics* 7, 528–529 (2025), DOI [10.1038/s42254-025-00871-z](https://doi.org/10.1038/s42254-025-00871-z) | Commento storico degli autori dei lavori SK/EA |
| P. Charbonneau et al. (eds.), *Spin Glass Theory and Far Beyond* | World Scientific (2023) | Volume collettivo contemporaneo |

## D. Collegamento al progetto RGS–PRISM–Q6

Nel repository `rgs-qlg-quaternion-bridge` è già stato integrato il modello Edwards–Anderson su Q6:

- PR #96, merged: [Add Edwards–Anderson spin glass model on Q6](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/96)
- [Documento tecnico Q6_EDWARDS_ANDERSON_SPIN_GLASS.md](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/Q6_EDWARDS_ANDERSON_SPIN_GLASS.md)
- Grafo: 64 vertici, 192 lati, grado 6; 240 facce esagonali/quadrate secondo la struttura cellulare adottata (specificare la convenzione delle facce nel documento tecnico).
- Variabili Ising ai vertici e accoppiamenti quenched Gaussiani o bimodali sugli archi.
- Osservabili pertinenti: energia, frustrazione, overlap tra repliche, suscettività spin-glass e cumulante di Binder.

### Cosa è matematicamente trasferibile e cosa no

1. **Trasferibile subito:** definizioni di Hamiltoniana EA/SK, disordine quenched, overlap, distribuzione degli overlap, frustrazione, identità di gauge e protocolli di finite-size scaling.
2. **Da verificare sul grafo finito Q6:** distribuzioni di overlap, dipendenza dalla realizzazione del disordine, scaling con famiglie di grafi crescenti e robustezza rispetto alla distribuzione dei couplings.
3. **Non dedotto dal modello finito:** esistenza di una fase spin-glass termodinamica, RSB, ultrametricità nel limite, equivalenza con un sistema tridimensionale, o derivazione della dinamica SU(2)/Yang–Mills.
4. **Separazione di gauge:** il modello EA Ising con couplings casuali non coincide automaticamente con una teoria di gauge Z2; occorre specificare trasformazioni locali, variabili di link e osservabili gauge-invarianti. A maggior ragione non equivale a SU(2).

## E. Sequenza minima di lavoro

- **Passo 1 — definizioni:** congelare Hamiltoniana, distribuzione dei couplings, convenzioni di bordo e insieme delle facce.
- **Passo 2 — controlli esatti:** simmetrie, gauge transformation, limite a disordine nullo e enumerazione esatta su Q6 quando possibile.
- **Passo 3 — numerica:** repliche indipendenti, overlap, Binder cumulant, suscettività e più semi casuali; riportare intervalli e dipendenza dalla taglia.
- **Passo 4 — limite:** costruire una successione di grafi (G_n) con dimensione crescente e dimostrare/controllare il regime di scaling. Q6 singolo non ha limite termodinamico.
- **Passo 5 — ponte RGS:** solo dopo i precedenti, confrontare osservabili e operatori con i settori PRISM, Krist-All e gauge; non identificare le strutture per analogia.

## Stato epistemico

- **Risultati consolidati nella letteratura:** modelli EA e SK, soluzione RSB mean-field, formula di Parisi per SK, ultrametricità sotto ipotesi precise.
- **Risultati numerici interni:** simulazioni su Q6 documentate nel repository collegato; valgono per il grafo e i parametri effettivamente simulati.
- **Candidati:** successioni Q6-like, relazioni tra frustrazione plaquette e osservabili gauge, possibili strutture di overlap.
- **Aperti:** limite termodinamico del modello Q6, RSB/ultrametricità nel limite, connessione dimostrata con SU(2) o con la geometria RGS.

La bibliografia è una base critica per costruire test falsificabili; non costituisce una convalida automatica dell'interpretazione fisica RGS.
