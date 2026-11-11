# Briefing scientifico per il confronto con Marco Morandotti

**Aggiornamento:** 11 novembre 2026  
**Repository:** [fabianleonaressi95/theorem](https://github.com/fabianleonaressi95/theorem)  
**Scopo:** documento breve di ingresso; la nota progettuale e l'appendice tecnica restano i documenti di approfondimento.

## 1. La domanda da discutere

La proposta non è presentare RGS–PRISM come una teoria dei materiali già validata. La domanda, circoscritta e falsificabile, è:

> È possibile costruire una discretizzazione geometrico-topologica delle incompatibilità elastiche che preservi esattamente le identità discrete, rappresenti le sorgenti di dislocazione/disclinazione e converga — in un benchmark controllato — verso il modello variazionale/Airy e la baseline C0-IPDG?

Il riferimento continuo è il lavoro di Cesana, De Luca e Morandotti sull'Airy stress function e sui sistemi di wedge disclinations/edge dislocations (SIAM J. Math. Anal. 56 (2024), DOI [10.1137/22M1523443](https://doi.org/10.1137/22M1523443)). Il riferimento numerico più diretto è Cesana, Fabbrini, León Baldelli e Morandotti, *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation* ([arXiv:2609.29614](https://arxiv.org/abs/2609.29614)).

## 2. Evidenza computazionale già ottenuta

### 2.1 P3 C0-IPDG, singolo core concentrico

È stato implementato ed eseguito in DOLFINx 0.11.0 un port iniziale dei tre problemi di cella P3, con penalità \(\alpha=10\), su un anello con un core concentrico. I campi sono \(\kappa_0,\kappa_1,\kappa_2\).

Al livello più fine riportato, \(h=0.06\), 2.030 triangoli:

| Quantità | Risultato |
|---|---:|
| Errore relativo seminorma \(H^2\), \(\kappa_0\) | 3,46% |
| Errore relativo seminorma \(H^2\), \(\kappa_1\) | 4,47% |
| Errore relativo seminorma \(H^2\), \(\kappa_2\) | 4,60% |
| Residuo identità flusso completo | \(2,55\times10^{-10}\) |

È stata verificata la decomposizione discreta
\[
M_\Delta-M_H=B_{\partial\Omega_\varepsilon}+B_{\mathcal F_h^i},
\]
includendo sia il flusso sul bordo fisico sia i contributi a due lati sulle facce interne. Il contributo interno è essenziale per i campi C0-IPDG: il solo bordo fisico non chiude l'identità.

**Limite:** è una riproduzione numerica parziale dei tre problemi di cella per un singolo core; non è la ricostruzione multi-core completa del preprint, né una prova del limite singolare.

Report e specifica: [MORANDOTTI_C0_IPDG_REPRODUCTION_PLAN.md](rgs_defect_benchmark/MORANDOTTI_C0_IPDG_REPRODUCTION_PLAN.md). Driver: [rgs_morandotti_c0_ipdg.py](../scripts/rgs_morandotti_c0_ipdg.py).

### 2.2 P3 C0-IPDG, interazione a due core

Il secondo gate è stato eseguito: due core distinti, sei problemi di cella P3 e matrici d'interazione \(6\times6\) Hessiana e Laplaciana, con flussi di bordo e interni.

Sulla geometria fissata (centri \((-0.28,0)\), \((0.28,0)\), raggio core 0.12, raggio esterno 1), i livelli più fini riportati sono:

| \(h\) | Triangoli | Massimo dei 6 residui normali | Media dei 6 residui normali | Residuo identità flusso |
|---:|---:|---:|---:|---:|
| 0,055 | 2.485 | 0,080354 | 0,03979 | \(2,59\times10^{-9}\) |
| 0,040 | 4.582 | 0,041203 | 0,02149 | \(3,98\times10^{-10}\) |
| 0,030 | 8.212 | 0,019257 | 0,010421 | \(6,10\times10^{-11}\) |

A \(h=0.03\), entrambe le matrici d'interazione sono simmetriche entro la precisione di assemblaggio e positive definite; \(\operatorname{cond}(M_H)\simeq53.32\). Tutti e sei i residui delle derivate normali diminuiscono sui due raffinamenti più fini; i residui delle tracce di valore restano circa \(10^{-16}\).

**Limite:** è una verifica numerica a due core e geometria fissata. Non dimostra ancora un ordine asintotico, la ricostruzione per \(N\) arbitrario, il limite singolare o la dinamica. Manca un campo analitico off-centre indipendente per un confronto d'errore \(H^2\).

### 2.3 Confronti Q1/P1–Airy: due regimi distinti

I risultati non vanno fusi in un unico benchmark perché i domini e le condizioni al contorno sono differenti.

- **Regime periodico liscio, \(n=32\):** differenza energetica Q1–Airy 0,0254% per inclusione shear e 0,0947% per dipolo shear; P1–Airy 0,1070% e 0,4195%. In questo test Q1 è più vicino al riferimento Airy di P1. Per il complesso triangolato P1, \(D_1D_0=0\) esattamente.
- **Regime traction-free con difetti regolarizzati:** al livello \(n=129\), per il dipolo di disclinazione il divario energetico cochain–Airy resta 18,52%. Il divario Q1–cochain è 12,12%. Questo è un limite concreto del benchmark, non un dato da nascondere.

**Conclusione ammessa:** esistono confronti quantitativi riproducibili e identità discrete esatte nei casi implementati. Non è dimostrato un vantaggio generale di RGS–PRISM rispetto a FEM/Airy.

Report: [PERIODIC_Q6_Q1_P1_AIRY_2026-11-09.md](rgs_defect_benchmark/PERIODIC_Q6_Q1_P1_AIRY_2026-11-09.md) e [dossier dei teoremi](MORANDOTTI_TEOREMI_DOSSIER_2026-11-09.md).

## 3. I risultati matematici che danno struttura alla proposta

| Record | Contenuto effettivo | Stato da comunicare |
|---|---|---|
| [T055](../theorems/T055-q6-dyadic-subdivision-chain-map.md) | Mappe di catena intere per la suddivisione dyadica del 2-scheletro cubico Q6 | Identità combinatorie dimostrate sul complesso finito |
| [T068–T070](../theorems/T068-barycentric-covariance-quadrature-law.md) | Covarianza baricentrica, momenti Dirichlet e quadratura con controllo del resto | Identità finite e stime sotto le ipotesi dichiarate |
| [T079](../theorems/T079-morandotti-surface-gradient-barycentre-bridge.md) | Split \(\nabla_S y=G+\mathsf D\), incompatibilità superficiale e circolazione | Identità di Stokes esatta per campi regolari; trasferimento al guscio cucito ancora aperto |
| [T080](../theorems/T080-exact-discrete-stokes-qball-structured-gradient.md) | Complesso discreto di Stokes per il Q-ball | Risultati esatti nella discretizzazione dichiarata |
| [T081](../theorems/T081-morandotti-gamma-euler-barycentric-energy.md) | Media baricentrica della densità del secondo ordine \(W_2\), normalizzazione Dirichlet e sensibilità digamma/polygamma | Identità esatte sotto integrabilità e ipotesi di differenziazione |
| [T082](../theorems/T082-morandotti-second-order-first-variation-dirichlet-anisotropy.md) | Prima variazione della densità rilassata e risposta baricentrica anisotropa | Formula variazionale condizionale; trasferimento al guscio aperto |

Il collegamento più diretto con la teoria di Morandotti è T079–T082. La variabile \(\mathsf D=\nabla g-G\) è la disarrangiamento del gradiente strutturato; non viene identificata con un campo gauge, con il gradiente di Bernoulli o con una cucitura. T081 distingue esplicitamente il campo tensoriale del secondo ordine \(\Gamma_{\mathrm{Mor}}\) dalla funzione Gamma di Euler \(\Gamma_E\). T082 non assume che la densità rilassata sia differenziabile: la prima variazione e la relazione con il moltiplicatore valgono solo quando sono soddisfatte le ipotesi di esistenza, regolarità ed envelope theorem.

## 4. Dove si colloca il guscio calcistico

Il guscio poliedrico con pannelli, cuciture e frame tangenti è una **seconda applicazione**, non il benchmark iniziale per la teoria di Airy piana. Il modello shell consente di studiare:
- gradienti tangenziali e mismatch strutturato;
- anisotropia dei pannelli;
- salti e leggi costitutive indipendenti sulle cuciture;
- trasporto fra frame locali e fibrati tangenti;
- effetti di secondo ordine e bending.

Non si identifica automaticamente una cucitura con una dislocazione o un difetto cristallino. Una legge di interfaccia per le cuciture deve essere specificata e calibrata separatamente. Il trasferimento della teoria Euclidea di structured deformations al guscio curvo, con 90 cuciture fisiche, e la convergenza \(\Gamma\)/Mosco restano problemi aperti.

Riferimenti interni: [T073](../theorems/T073-unified-football-shell-rgs-prism-limit-program.md), [T076](../theorems/T076-constitutive-mechanics-fatigue-hysteresis-football-seams.md), [documento di raccordo calcistico](../manuscripts/DOCUMENTO_RACCORDO_CALCISTICO_MORANDOTTI_RGS_PRISM.md).

## 5. Cosa chiedere a Morandotti

Non chiedere una valutazione globale di RGS–PRISM. Chiedere un confronto su tre questioni tecniche:

1. **Benchmark di riferimento:** quale configurazione a due core/dipolo e quale osservabile (matrice d'interazione, energia, stress, momento di Burgers/Frank) è il test più significativo rispetto ai suoi risultati?
2. **Mappa discreta:** quale spazio/cochain e quale diagramma di commutazione dovrebbero collegare incompatibilità/Airy e variabili RGS–PRISM senza introdurre sorgenti spurie?
3. **Teoria del limite:** quali ipotesi minime di coercività, compattezza e consistenza renderebbero plausibile una convergenza variazionale per la discretizzazione scelta?

La proposta è falsificabile: se la discretizzazione non supera la baseline su accuratezza, robustezza, costo o rappresentazione dei difetti, il benchmark deve documentarlo.

## 6. Stato complessivo: non confondere i livelli

**Già dimostrato o verificato nei casi dichiarati**
- identità di catena intere del complesso Q6 e delle mappe di suddivisione considerate;
- identità analitica Hessiano–Laplaciano sotto le condizioni al bordo specificate;
- chiusura numerica del flusso completo P3 single-core e two-core;
- positività/simmetria delle matrici d'interazione nei test P3 riportati;
- identità di Stokes e formule baricentriche nelle rispettive ipotesi.

**Numericamente sostenuto, ma non teorema**
- riduzione dei residui delle condizioni normali nel test P3 a due core sui livelli fini;
- convergenza dei benchmark Q1/P1 verso Airy nei casi periodici lisci;
- trend di raffinamento dei campi nei benchmark traction-free regolarizzati.

**Ancora aperto**
- riproduzione della ricostruzione C0-IPDG per numero arbitrario di core e dati generali;
- confronto analitico off-centre indipendente per il test a due core;
- limite singolare dei core e dinamica;
- mappa dimostrata Airy–cochain RGS–PRISM;
- convergenza Mosco/\(\Gamma\) della sequenza curva RGS–PRISM;
- trasferimento della teoria di structured deformations al guscio cucito;
- calibrazione e validazione sperimentale su materiali reali.

## 7. Documenti da inviare e ordine di lettura

1. **Prima lettura:** [Nota progettuale Morandotti–RGS–PRISM](../manuscripts/NOTA_PROGETTUALE_MORANDOTTI_RGS_PRISM.md).
2. **Questo briefing:** risultati aggiornati e domanda di confronto.
3. **Solo se richiesto:** [Appendice tecnica completa](../manuscripts/APPENDICE_TECNICA_MORANDOTTI_RGS_PRISM.md), [piano di riproduzione C0-IPDG](rgs_defect_benchmark/MORANDOTTI_C0_IPDG_REPRODUCTION_PLAN.md), [matrice bibliografica](../manuscripts/MATRICE_BIBLIOGRAFICA_MORANDOTTI_RGS_PRISM.md).

**Richiesta proposta:** un primo colloquio tecnico breve per scegliere un benchmark condiviso e individuare le condizioni matematiche necessarie per una comparazione corretta.

---
**FLN**
