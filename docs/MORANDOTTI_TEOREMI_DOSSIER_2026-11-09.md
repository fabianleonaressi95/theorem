# Dossier scientifico RGS–PRISM per il confronto con Marco Morandotti

**Versione di lavoro:** 9 novembre 2026  
**Repository:** `fabianleonaressi95/theorem`  
**Riferimento applicativo:** elasticità incompatibile, difetti, funzione di Airy, metodi FEM e problemi di cella.

## Sintesi esecutiva

Il materiale attualmente documentato consente di presentare quattro risultati di natura distinta:

1. **T055 — teorema combinatorio dimostrato:** la suddivisione dyadica del 2-scheletro cubico standard di Q6 induce mappe di catena esatte.
2. **Identità continua Hessiano–Laplaciano — identità analitica dimostrata sotto ipotesi esplicite:** per le funzioni di cella Airy con tracce affini e derivate normali corrispondenti su ogni componente del bordo, le forme integrali Hessiana e Laplaciana coincidono.
3. **Confronti FEM/Airy — verifiche numeriche riproducibili:** confronti Q1, P1/cochain e Airy su sorgenti lisce e difetti regolarizzati, con raffinamenti e residui.
4. **P3 C0-IPDG — riproduzione parziale numerica:** tre problemi di cella su un anello con un singolo core concentrico, con verifica discreta del flusso completo bordo + facce interne.

Questi risultati sono un punto di partenza matematico per un confronto sui gradienti e sui difetti. Non dimostrano ancora una teoria RGS dei materiali, una convergenza Mosco/Γ, il limite singolare dei core, né una validazione sperimentale su provini prodotti mediante manifattura additiva.

## 1. Riferimenti scientifici di confronto

Il riferimento più diretto è:

P. Cesana, L. De Luca, M. Morandotti, *Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method*, SIAM Journal on Mathematical Analysis 56 (2024), 79–136. DOI: [10.1137/22M1523443](https://doi.org/10.1137/22M1523443).

Per la formulazione agli elementi finiti:

P. Cesana, E. Fabbrini, A. A. León Baldelli, M. Morandotti, *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation*, [arXiv:2609.29614](https://arxiv.org/abs/2609.29614).

Il lavoro del 2024 tratta sistemi di dislocazioni di bordo e disclinazioni a cuneo nel quadro dell'elasticità incompatibile e della funzione di Airy, con un risultato di equivalenza energetica asintotica nel limite singolare regolarizzato. Il preprint 2026 descrive una formulazione FEM basata su problemi di cella biharmonici e ricostruzione mediante una matrice finito-dimensionale.

Il dossier non attribuisce a RGS–PRISM risultati già dimostrati in questi lavori: li usa come riferimenti esterni rispetto ai quali misurare la riproducibilità e l'eventuale contributo originale.

## 2. Teorema esterno di riferimento — Cesana, Fabbrini, León Baldelli, Morandotti (2026)

**Classificazione: E — teorema pubblicato nel preprint del gruppo Morandotti; non è un risultato RGS.**

Il Theorem 2.2 di *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation* è il riferimento analitico diretto per il dossier. Il dominio è limitato, semplicemente connesso e piecewise-$C^2$ Lipschitz; si rimuovono $N=J+K$ core disgiunti di raggio $\varepsilon$, associati a dislocazioni di bordo e disclinazioni a cuneo. Il materiale è isotropo in plane strain, con $E>0$ e $\nu\in(-1,1/2)$.

Il teorema stabilisce tre livelli.

1. **Caratterizzazione variazionale Airy.** Il minimizzatore unico del funzionale elastico in termini del potenziale di Airy equivale alla soluzione debole dell'equazione di Euler–Lagrange nella classe ammissibile $\mathscr C(\Omega_\varepsilon)$.
2. **Equivalenza stress–strain.** Sotto l'ipotesi di regolarità $\hat v\in H^4(\Omega_\varepsilon)$, la deformazione ricavata da $\hat\epsilon=\mathbb C^{-1}\operatorname{cof}(D^2\hat v)$ è la soluzione unica del problema meccanico con equilibrio, trazione nulla, incompatibilità nulla fuori dai core e circuitazioni che codificano gli angoli di Frank e i vettori di Burgers.
3. **Ricostruzione mediante problemi di cella.** Per una geometria fissata si risolvono $3N$ problemi biharmonici: $\kappa_0^i,\kappa_1^i,\kappa_2^i$ per ciascun core. Il potenziale generale si ricostruisce mediante una matrice d'interazione $\mathcal M\in\mathbb R^{3N\times3N}$ e un vettore $\Phi$ costruito dai dati di Frank e Burgers:
   
   $
   \hat v(x)=-\frac{E}{1-\nu^2}\langle\mathcal M^{-1}\kappa(x),\Phi\rangle.
   $

Il punto algoritmico essenziale è la separazione tra geometria e dati dei difetti: a geometria, posizioni dei core e raggio fissati, i (3N) campi di cella si riutilizzano per differenti valori di Burgers e Frank, ricostruendo il campo tramite algebra finito-dimensionale.

**Rilevanza per il nostro lavoro:** questa è la specifica matematica da riprodurre. Il driver RGS attuale esegue i tre problemi P3 per $N=1$, ma non ha ancora la matrice multi-core completa $\mathcal M$, né la ricostruzione generale per $N>1$. È quindi una riproduzione parziale di una componente del metodo, non del Theorem 2.2 nel suo complesso.

Fonte primaria: [arXiv:2609.29614, Theorem 2.2 e Remark 2.3](https://arxiv.org/abs/2609.29614).

## 3. Teorema esterno di evoluzione dissipativa con direzioni cristalline

**Classificazione: E — teorema di esistenza pubblicato; modello e ipotesi specifiche.**

Un secondo risultato direttamente pertinente è Cesana, Grillo, Morandotti e Pastore, *Dissipative evolution of Volterra disclinations*, SIAM Journal on Applied Mathematics 85 (2025), 1361–1386, DOI [10.1137/24M1688096](https://doi.org/10.1137/24M1688096), preprint [arXiv:2408.15457](https://arxiv.org/abs/2408.15457).

Nel caso isotropo, le posizioni $\boldsymbol\Xi=(\Xi_1,\ldots,\Xi_N)$ evolvono secondo un sistema dissipativo guidato dalle forze ricavate dal potenziale elastico di Airy. Nel caso cristallino, si introduce un insieme finito $\mathcal G$ di direzioni unitarie, simmetrico rispetto al segno e tale che $\operatorname{Span}\mathcal G=\mathbb R^2$. Ogni difetto può muoversi lungo la direzione che massimizza l'allineamento con la forza. Nei punti in cui due direzioni sono entrambe massimizzanti, la dinamica diventa una inclusione differenziale.

**Theorem 5.1:** per una configurazione iniziale interna al prodotto dei dischi e fuori dall'insieme di collisione $\Pi$, esiste un tempo $T^*>0$ e almeno una soluzione locale assolutamente continua della dinamica vincolata alle direzioni cristalline, nel senso della convessificazione dell'insieme delle velocità ammissibili.

Il risultato è locale: non afferma esistenza globale, assenza di collisioni per ogni tempo, né unicità in tutti i casi. Il testo discute condizioni di unicità destra e fenomeni di cross-slip/fine cross-slip nei punti di cambio della direzione massimizzante.

**Rilevanza per Morandotti e per RGS–PRISM:** questo è il ponte più diretto tra difetti e anisotropia discreta. L'insieme $\mathcal G$ può essere confrontato con direzioni preferenziali derivate da una microstruttura o da un reticolo. Per un confronto RGS–PRISM, tuttavia, non basta scegliere le direzioni del grafo: occorre dimostrare come la geometria del reticolo determina $\mathcal G$ e come le forze discrete convergono alle forze del modello continuo.

**Nuovo problema concreto:** costruire una versione RGS discreta della legge di selezione direzionale, provarne la consistenza con il campo di forza Airy e confrontare traiettorie, energia e cambi di direzione con la differential inclusion pubblicata.

Fonte primaria: [arXiv:2408.15457, §5 e Theorem 5.1](https://arxiv.org/abs/2408.15457); record editoriale [CVGMT](https://cvgmt.sns.it/paper/6744/).

## 4. T055 — teorema esatto di suddivisione dyadica Q6

**Classificazione: D — teorema combinatorio dimostrato.**

Sia (K) il 2-scheletro cubico di ([0,1]^6), con celle orientate secondo le convenzioni del costruttore Q6. I conteggi sono

\[
(|K_0|,|K_1|,|K_2|)=(64,192,240).
\]

Sia (K') la suddivisione a metà di ogni coordinata attiva. I conteggi del complesso raffinato sono

\[
(|K'_0|,|K'_1|,|K'_2|)=(496,1344,960).
\]

Indichiamo con (B_1,B_2) gli operatori di bordo del complesso grossolano e con (B'_1,B'_2) quelli del raffinato. Le mappe di suddivisione intere (S_0,S_1,S_2) mandano rispettivamente un vertice nel vertice corrispondente, un arco nella somma dei suoi due semiarchi orientati e una faccia nella somma delle quattro sottofacce orientate.

Il risultato è

\[
\boxed{B'_1S_1=S_0B_1,\qquad B'_2S_2=S_1B_2.}
\]

Inoltre,

\[
B'_1B'_2=0.
\]

### Dimostrazione

Per un arco orientato, la somma dei due semiarchi ha bordo uguale al vertice terminale meno il vertice iniziale: il vertice intermedio si cancella. Questo dà (B'_1S_1=S_0B_1) su ogni arco della base.

Per una faccia orientata, le quattro sottofacce hanno l'orientazione indotta dalla faccia madre. Ogni lato interno compare due volte con orientazioni opposte e si cancella; restano soltanto i lati esterni, che sono precisamente le suddivisioni dei quattro lati della faccia originaria. Questo dà (B'_2S_2=S_1B_2). Infine ogni faccia raffinata ha bordo chiuso, quindi (B'_1B'_2=0). Le identità sono intere, non uguaglianze approssimate in floating point. (square)

La matrice aggregata di trasferimento delle sei direzioni coordinate è (D=2I_6): ogni arco viene sostituito da due semiarchi paralleli alla stessa direzione.

**Rilevanza per Morandotti:** il teorema fornisce una costruzione di raffinamento cellulare che conserva esattamente gli operatori di bordo. È una base matematica per discretizzazioni struttura-preservanti e per costruire complessi raffinati.

**Limite:** riguarda la suddivisione cubica standard. Non identifica la suddivisione con Kathara/Krist-All, non prova una legge supergolden e non fornisce ancora una mappa verso la mesh perforata usata nei problemi di elasticità.

Fonte: [T055 — Exact dyadic subdivision chain map](https://github.com/fabianleonaressi95/theorem/blob/work/rgs-defect-benchmark-torino/theorems/T055-q6-dyadic-subdivision-chain-map.md).

## 5. Identità analitica Hessiano–Laplaciano per le funzioni di cella Airy

**Classificazione: D/E — identità analitica dimostrata sotto le ipotesi di regolarità e bordo qui dichiarate.**

In due dimensioni, per (u,v) sufficientemente regolari,

\[
\operatorname{div}\left((\operatorname{cof}D^2u)\nabla v\right)
=(\operatorname{cof}D^2u):D^2v
=\Delta u\,\Delta v-D^2u:D^2v.
\]

La prima uguaglianza usa l'identità (operatorname{div}(operatorname{cof}D^2u)=0), valida per Hessiane di funzioni sufficientemente regolari; la seconda è un'identità algebrica per matrici simmetriche (2\times2).

Integrando sul dominio perforato (Omega_\varepsilon),

\[
\int_{\Omega_\varepsilon}
(\Delta u\,\Delta v-D^2u:D^2v)\,dx
=
\int_{\partial\Omega_\varepsilon}
(\operatorname{cof}D^2u\,n)\cdot\nabla v\,ds.
\]

Per i problemi di cella Airy considerati, su ciascuna componente del bordo la traccia di Dirichlet è affine e la derivata normale coincide con quella della stessa funzione affine. Ne segue che la derivata tangenziale della traccia e la derivata normale prescritta determinano il gradiente affine al bordo. La seconda derivata tangenziale di (u) è quindi nulla sul bordo, ossia (D^2u\,t=0). Nella base ortonormale ((n,t)), l'Hessiana ha la forma (operatorname{diag}(a,0)), per cui ((operatorname{cof}D^2u)n=0). Il flusso si annulla e si ottiene

\[
\boxed{
\int_{\Omega_\varepsilon}D^2u:D^2v\,dx
=
\int_{\Omega_\varepsilon}\Delta u\,\Delta v\,dx.}
\]

Questo chiarisce perché il solver delle funzioni di cella possa assemblare il prodotto Hessiano mentre il postprocessing costruisce la matrice d'interazione con il prodotto dei Laplaciani: sotto le condizioni di bordo indicate le due forme continue coincidono.

**Distinzione:** l'identità è analitica; la sua realizzazione discreta richiede di contabilizzare i flussi sulle componenti fisiche del bordo e sulle facce interne della mesh, specialmente per campi C0 con gradienti non globalmente continui.

## 6. Verifica P3 C0-IPDG dell'identità

**Classificazione: N — verifica numerica riproducibile su un singolo core concentrico.**

Il driver DOLFINx 0.11.0 usa elementi Lagrange P3 su una corona circolare, un core concentrico, penalità (alpha=10), e risolve i tre problemi di cella (kappa_0,kappa_1,kappa_2).

Al livello (h=0.06), con 2.030 celle, gli errori relativi nel seminorma (H^2) sono:

| Campo | Errore relativo (H^2) |
|---|---:|
| (kappa_0) | 3,46% |
| (kappa_1) | 4,47% |
| (kappa_2) | 4,60% |

Il controllo discreto assembla il flusso al bordo fisico e il flusso a due lati sulle facce interne:

\[
M_\Delta-M_H=B_{\partial\Omega_\varepsilon}+B_{\mathcal F_h^i}.
\]

Residui relativi:

| (h) | Residuo identità |
|---:|---:|
| 0,22 | (4,69\times10^{-7}) |
| 0,14 | (6,00\times10^{-8}) |
| 0,09 | (2,91\times10^{-9}) |
| 0,06 | (2,55\times10^{-10}) |

Il residuo di simmetria della matrice di flusso totale scende da (2,26\times10^{-5}) a (2,04\times10^{-8}). Il flusso sulle sole componenti fisiche esterne non basta: il contributo delle facce interne è necessario per il campo C0-IPDG.

**Conclusione ammessa:** il controllo di assemblaggio dell'identità discreta è superato per i tre campi P3 del problema a singolo core concentrico.

**Conclusioni non ammesse:** non è una riproduzione completa dell'algoritmo multi-core del preprint; non prova il limite singolare del core né un ordine generale di convergenza.

CI: [run 42662098640](https://github.com/fabianleonaressi95/theorem/actions/runs/42662098640). Artifact: [13693953816](https://github.com/fabianleonaressi95/theorem/actions/runs/42662098640/artifacts/13693953816).

## 7. Confronto periodico Q6–Q1–P1–Airy

**Classificazione: N — benchmark numerico per sorgenti lisce.**

Dominio toroidale ([0,4]^2), parametri isotropi (lambda=mu=1), condizioni periodiche allineate e due sorgenti shear lisce: inclusione gaussiana e dipolo gaussiano.

Sono confrontati:
- quoziente cinematico Q6 sulla cella (4\times4);
- Q1 quadrilatero con quadratura Gauss (2\times2);
- P1 triangolare/cochain con entrambe le diagonali;
- riferimento Airy spettrale in Fourier.

A (n=32):

| Sorgente | Q1–Airy energia | P1–Airy energia | Q1–P1 energia |
|---|---:|---:|---:|
| Inclusione shear | 0,0254% | 0,1070% | 0,0815% |
| Dipolo shear | 0,0947% | 0,4195% | 0,3251% |

Gli errori P1 su stress/deformazione sono rispettivamente 0,5570%/0,3025% per l'inclusione e 0,8959%/0,6936% per il dipolo. I residui dei sistemi sono dell'ordine (10^{-14}); la compatibilità Airy spettrale è dell'ordine (10^{-16}).

Per il complesso triangolato P1 vale esattamente (D_1D_0=0) a tutti i livelli e per entrambe le diagonali. Al livello (n=4), che è la cella Q6 effettiva, il lift conserva pullback ed energia entro precisione macchina.

**Lettura scientifica:** entrambi i metodi FEM convergono numericamente verso Airy nel test liscio; Q1 è più vicino al riferimento di P1 nei dati riportati. Questo benchmark non dimostra un vantaggio di RGS–PRISM. I livelli (n>4) sono raffinamenti FEM, non grafi Q6 più grandi.

Fonte: [report periodico Q6–Q1–P1–Airy](https://github.com/fabianleonaressi95/theorem/blob/work/rgs-defect-benchmark-torino/docs/rgs_defect_benchmark/PERIODIC_Q6_Q1_P1_AIRY_2026-11-09.md). CI: [run 42659067311](https://github.com/fabianleonaressi95/theorem/actions/runs/42659067311), artifact [13693946123](https://github.com/fabianleonaressi95/theorem/actions/runs/42659067311/artifacts/13693946123).

## 8. Difetti regolarizzati: Q1, P1/cochain e Airy

**Classificazione: N — confronto numerico; non teorema di limite singolare.**

Il benchmark traction-free confronta elasticità Q1, P1/cochain e riferimento Airy finite-difference per inclusione shear, dipolo shear, dislocazione di bordo di Volterra regolarizzata, disclinazione a cuneo e dipolo di disclinazione.

La differenza energetica relativa Q1/cochain a (n=65) è:

| Caso | Differenza Q1/cochain |
|---|---:|
| Inclusione shear | 0,309% |
| Dipolo shear | 0,395% |
| Dislocazione Volterra regolarizzata | 2,41% |
| Disclinazione a cuneo | 5,35% |
| Dipolo di disclinazione | 31,23% |

Per il dipolo di disclinazione il divario scende a 12,12% a (n=129), ma rimane significativo. A (n=129), gli errori dei campi rispetto ad Airy sono circa 5,7–6,0%, mentre il divario energetico cochain–Airy è ancora 18,52%.

Un audit separato avvicina un dipolo di disclinazioni di Frank opposte a una dislocazione di bordo, fissando (b=0,002), core gaussiano (sigma=0,025), (n=129), e variando la separazione. Per (d=2h) si ottiene un residuo quasi nullo, ma esso deriva da un'identità dello stencil centrato grid-aligned. Non è una dimostrazione del limite continuo né dell'espansione energetica rinormalizzata del teorema 2024.

**Conclusione ammessa:** le discretizzazioni sono confrontate quantitativamente e gli errori dei campi diminuiscono con il raffinamento nei casi riportati.

**Conclusione non ammessa:** equivalenza energetica asintotica dei difetti singolari, convergenza Mosco/Γ o riproduzione del teorema di Cesana–De Luca–Morandotti.

Fonte: [confronto Q1–cochain P1–Airy](https://github.com/fabianleonaressi95/theorem/blob/work/rgs-defect-benchmark-torino/docs/rgs_defect_benchmark/THREE_WAY_COMPARISON_2026-11-09.md).

## 9. Quoziente cinematico Q6 verso cella materiale periodica

**Classificazione: D/N — identità combinatorie esatte e verifica numerica dell'energia periodica.**

L'embedding Gray identifica il grafo Q6 con (C_4\square C_4\square C_4). Collassando il terzo fattore come fibra interna a quattro stati si ottiene una cella (C_4\square C_4) con 16 vertici, 32 spigoli e 16 facce. Le mappe intere di catena e il pullback cinematico hanno residui esattamente nulli.

Il conteggio dei 240 quadrati del cubo a sei dimensioni va distinto: 192 appartengono al sottocomplesso prodotto, 48 sono facce generate dai due bit all'interno di ciascuna coppia e non vengono identificate con facce della cella materiale.

**Limite:** il quoziente è una costruzione combinatoria/cinematica finita. Non è ancora una realizzazione fisica del grafo PRISM completo, né una mappa al mesh perforato traction-free. Non è dimostrata una convergenza Mosco/Γ.

Fonte: [Q6 PRISM kinematic map](https://github.com/fabianleonaressi95/theorem/blob/work/rgs-defect-benchmark-torino/docs/rgs_defect_benchmark/Q6_PRISM_KINEMATIC_MAP.md).

## 10. Tabella di stato epistemico

| ID | Risultato | Stato | Portata effettiva |
|---|---|---|---|
| T055 | Suddivisione dyadica Q6 e mappe di catena | D | Teorema finito esatto |
| A1 | Identità Hessiano–Laplaciano per funzioni di cella con tracce affini | D/E | Identità analitica sotto ipotesi |
| P3-1 | P3 C0-IPDG, tre campi su singolo core concentrico | N | Riproduzione parziale |
| P3-2 | Flusso bordo + facce interne e residuo matriciale | N | Audit discreto superato |
| FEM-PER | Q6/Q1/P1/Airy periodico | N | Sorgenti lisce |
| FEM-DEF | Q1/cochain/Airy traction-free con difetti regolarizzati | N | Benchmark quantitativo |
| Q6-MAP | Quoziente Q6→cella periodica | D/N | Mappe finite esatte, energia verificata |
| MOSCO | Limite variazionale del modello discreto | O | Non dimostrato |
| CORE | Limite singolare e rinormalizzazione | O | Non completato |
| PRISM-FEM | Mappa dal PRISM completo alla mesh fisica | O | Non costruita |
| AM-EXP | Calibrazione su provini di manifattura additiva | O | Nessun dato sperimentale nel benchmark |

## 11. Pertinenza per gradienti e materiali

### Gradienti

I risultati più trasferibili sono la conservazione esatta delle relazioni di bordo sotto raffinamento, il confronto fra discretizzazioni e l'analisi degli errori dei campi stress/deformazione. Il passo successivo è formulare un problema con coefficienti spazialmente variabili, ad esempio (lambda(x),mu(x)), e confrontare gradienti di proprietà e campi di deformazione su mesh allineate.

### Difetti

Il confronto Q1/P1/Airy e l'audit C0-IPDG sono il nucleo più vicino ai problemi studiati dal gruppo Morandotti. La priorità è completare la ricostruzione multi-core e fuori centro, mantenendo fissi geometria, raggi dei core, condizioni al contorno, momenti di Burgers/Frank e parametri elastici.

### Manifattura additiva

Un test credibile richiede almeno:
- geometria e orientazione di stampa del provino;
- mappa micro-CT o metallografica di porosità e difetti;
- proprietà elastiche locali o loro stima;
- condizioni di carico e protocollo sperimentale;
- confronto quantitativo fra campo previsto e misurato.

La struttura Q6/PRISM può essere proposta come discretizzazione candidata soltanto dopo aver definito una mappa verificabile tra celle astratte e microstruttura misurata. Non si afferma che ciò sia già stato fatto.

## 12. Problemi aperti prioritari

1. Completare la riproduzione dell'algoritmo multi-core del preprint 2026: (3N) problemi di cella, matrice di interazione M e ricostruzione per dati generali di Burgers e Frank.
2. Aggiungere core fuori centro e geometrie con più core non sovrapposti.
3. Separare sistematicamente il limite (h\to0) dal limite (ε\to0), con rinormalizzazione.
4. Dimostrare, se le ipotesi lo consentono, una convergenza variazionale Mosco o Γ.
5. Costruire e verificare la mappa di catena Q6/PRISM verso la mesh fisica perforata.
6. Estendere i coefficienti elastici a campi spazialmente variabili e anisotropi.
7. Solo successivamente introdurre variabili interne, dissipazione e isteresi.
8. Confrontare con dati di provini reali, compresi materiali prodotti mediante manifattura additiva.

## 13. Conclusione destinata al confronto scientifico

Il progetto dispone già di un teorema combinatorio esatto di raffinamento Q6, di un'identità analitica che chiarisce la relazione tra le forme Hessiana e Laplaciana dei problemi di cella Airy, di benchmark FEM/Airy con dati quantitativi e di una prima verifica P3 C0-IPDG con flussi interni esplicitamente contabilizzati.

Il contributo più immediatamente discutibile con Morandotti non è una pretesa teoria alternativa dei materiali, ma una base riproducibile per studiare:
- conservazione delle strutture discrete;
- discretizzazione dei gradienti;
- rappresentazione e interazione dei difetti;
- confronto fra formulazioni energetiche;
- estensione a coefficienti eterogenei e microstrutture.

Il limite scientifico attuale è altrettanto chiaro: la ricostruzione multi-core, il limite singolare, la convergenza variazionale, la mappa PRISM–mesh fisica e la validazione sperimentale sono ancora aperti. Sono questi i passaggi che trasformerebbero i benchmark presenti in un programma matematico e applicativo sui materiali.

---

## Appendice — file e verifiche riproducibili

- `theorems/T055-q6-dyadic-subdivision-chain-map.md`
- `docs/rgs_defect_benchmark/PERIODIC_Q6_Q1_P1_AIRY_2026-11-09.md`
- `docs/rgs_defect_benchmark/THREE_WAY_COMPARISON_2026-11-09.md`
- `docs/rgs_defect_benchmark/Q6_PRISM_KINEMATIC_MAP.md`
- `docs/rgs_defect_benchmark/MORANDOTTI_C0_IPDG_REPRODUCTION_PLAN.md`
- `scripts/rgs_morandotti_c0_ipdg.py`
- `scripts/rgs_airy_cell_matrix_identity.py`
- `scripts/rgs_airy_cell_matrix_p2.py`

CI:
- [Regressione unificata: run 42662098852](https://github.com/fabianleonaressi95/theorem/actions/runs/42662098852) — 47 test superati.
- [P3 C0-IPDG: run 42662098640](https://github.com/fabianleonaressi95/theorem/actions/runs/42662098640) — esecuzione e identità discreta superate.

La PR #119 è ancora draft: il suo stato draft è coerente con i problemi aperti sopra e non va presentata come lavoro integralmente concluso.
