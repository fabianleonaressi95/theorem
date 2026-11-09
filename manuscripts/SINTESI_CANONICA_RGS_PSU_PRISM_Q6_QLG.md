# Sintesi canonica RGS–PSU–PRISM–Q6–QLG: stato, struttura e programma di chiusura

**Versione:** 0.1 — 9 novembre 2026  
**Scopo:** consolidare i filoni già presenti nel repository THEOREM in una struttura scientifica unitaria, senza confondere risultati matematici, verifiche numeriche, modelli condizionali e ipotesi fisiche.

## 1. Tesi organizzativa

Il programma non è una singola teoria fisica già dimostrata. È un insieme coordinato di costruzioni geometriche, combinatoriche, spettrali, gauge e fenomenologiche. La sintesi deve individuare i ponti effettivamente costruiti e rendere esplicite le dipendenze che ancora mancano.

La catena architetturale di riferimento è:

\[
X_{O_h}\;\longrightarrow\;Q_6\;\longrightarrow\;
\text{connessioni discrete / holonomie}\;\longrightarrow\;
\text{operatori spettrali}\;\longrightarrow\;
\text{raffinamento}\;\longrightarrow\;\text{limite continuo}.
\]

Il coframe RGS, il settore PSU/Anti-Twin, la geometria spinoriale, QAT e le interpretazioni fisiche sono collegati a questa catena soltanto attraverso mappe e azioni esplicite. La somiglianza geometrica o una coincidenza numerica non costituisce un’identificazione.

## 2. Nucleo combinatorio Q6

Q6 è il cubo booleano a sei bit:

- 64 vertici, 192 archi, grado 6;
- 240 quadrati elementari;
- complesso cellulare cubico con operatori di bordo \(B_1,B_2\) e identità \(B_1B_2=0\);
- ranks riportati per la struttura 1-scheletrica: \(\operatorname{rank}B_1=63\), \(\operatorname{rank}B_2=129\), quindi \(\beta_1=0\) per il complesso completo di facce, da distinguere dal solo grafo (che ha \(\beta_1=129\));
- bipartizione 32/32.

Le tre coppie di bit possono essere organizzate come
\[
(2b_0+b_1,\;2b_2+b_3,\;2b_4+b_5),
\]
con interpretazione trigrammatica da trattare come codifica strutturale, non come identificazione fisica automatica.

Il ponte Q6–gauge usa variabili SU(2) sugli archi e holonomie sulle facce. La struttura di gauge richiede di distinguere:
1. connessione sugli archi;
2. trasformazioni locali ai vertici;
3. holonomie/plaquette;
4. azione Wilson e sua Hessiana;
5. quotient gauge e modi nulli.

Il numero 240 delle facce non implica da solo 240 gradi di libertà indipendenti: le identità di bordo e le ridondanze gauge vanno rispettate.

## 3. RGS / PSU / coframe

Il settore RGS ricostruisce geometrie discrete a partire da configurazioni e spazi tangenti, con coframe/vierbein e matrici Gram.

Dati di audit riportati nel programma:
- spazio tangente di dimensione 188, con 4 direzioni normali;
- \(Q^TQ\) residuo circa \(1.31\times10^{-14}\);
- commutatore con \(O_h\) circa \(5\times10^{-16}\);
- ricostruzione coframe 3D con determinante circa 0.794–1.011 e condizionamento circa 3.006;
- coframe 4D con metrica di firma \((-+++ )\), controllo spettrale riportato positivo per la matrice normalizzata usata nella costruzione;
- il modello Kerr–Schild teleparallel riportato ha \(\det(e)=1\), ma resta un benchmark di costruzione, non una derivazione della dinamica gravitazionale RGS.

Questi numeri sono risultati computazionali da riprodurre con i file originali e versioni degli script. Non costituiscono da soli una soluzione delle equazioni di Einstein o Einstein–Cartan.

## 4. PRISM–Krist-All e struttura spettrale

Il grafo PRISM principale è
\[
C_{64}\square C_6^3\square C_5,
\qquad N=64\cdot6^3\cdot5=69120,
\]
con grado 10. L’indicizzazione canonica registrata è
\[
((((G\cdot6+L)\cdot6+C)\cdot6+T)\cdot5+B).
\]

Audit registrati: 1920 stati attivi; 5760 correzioni; 108 cicli di lunghezza 640; numeri di Betti Hodge riportati \(b_1=5,b_2=10\); gap 0.009630546656; \(\omega=0.098135\); residuo Krist-All \(W_0=5.22\times10^{-16}\). Krist-All: 11725 classi e relazione \(K^3=K^2+I\); radice supergolden \(\psi\approx1.465571231876768\).

Questi sono invarianti e risultati di audit del modello finito. La loro interpretazione come spettro fisico, costante universale o dinamica materiale richiede una derivazione ulteriore e non è assunta.

## 5. Geometria quaternionica, 2I e spazio sferico

Il programma include il gruppo binario icosaedrale \(2I\), le rappresentazioni quaternioniche/Clifford e il quoziente di Poincaré \(S^3/2I\). Il ponte deve essere espresso in termini di:
- rappresentazioni e commutanti;
- spinorialità e scelta della struttura spin;
- operatori Dirac e loro simboli;
- proiezione al quoziente e condizioni di equivarianza;
- confronto tra spettri del modello discreto e benchmark continuo.

Non basta identificare una simmetria icosaedrale per dedurre una struttura spinoriale o un modello cosmologico.

## 6. PSU, Anti-Twin, biverso e QAT

PSU/Anti-Twin e QAT sono un settore geometrico-fisico candidato: due fogli/coni, simmetria Lorentz, ovalizzazione/toroide e riconnessione. La formulazione rigorosa deve specificare:
- varietà o complesso sottostante;
- campi e variabili indipendenti;
- metrica e coframe;
- connessione (Levi-Civita oppure Weitzenböck);
- torsione e curvatura;
- azione e condizioni al contorno;
- osservabili e regime di validità.

L’immagine della sfera inscritta nel cubo, il centro evento e il cono nullo sono una costruzione geometrica utile. Non dimostrano, da soli, che il tempo sia la velocità di riconnessione o che la luce abbia una struttura topologica proposta dal modello. Queste interpretazioni restano ipotesi da formalizzare e confrontare con Maxwell/relatività.

## 7. Gauge, Yang–Mills, QCD e Dirac

Il repository contiene Q6 gauge, Wilson loops, Dirac/Wilson refinement e questioni di anomalia/BRST. Il programma va separato in livelli:

**Livello discreto:** definizioni di link, gauge transformation, plaquette, azione Wilson e operatori.

**Livello analitico:** identità esatte, positività, kernel gauge, stime uniformi e convergenza degli operatori.

**Livello continuo:** limite di forme/operatori, controllo della misura, convergenza resolvente e compatibilità con gauge invariance.

**Livello fisico:** spettro, massa, confinamento o osservabili QCD. Queste affermazioni non discendono automaticamente dai primi tre livelli.

Il teorema Nielsen–Ninomiya resta un vincolo: una costruzione discreta non può dichiarare una soluzione senza identificare precisamente quali ipotesi siano modificate e senza mostrare l’eventuale compensazione dei modi.

## 8. Mosco, FEEC e limite continuo

Il repository registra un benchmark di raffinamento piatto e dossier per il caso curvo. Il caso piatto non prova il caso curvo.

Per il limite PRISM/RGS sono obblighi:
1. definire una famiglia di spazi e mappe di raffinamento;
2. costruire forme quadratiche e domini;
3. dimostrare liminf;
4. costruire recovery sequence;
5. ottenere compattezza discreta;
6. controllare proiezioni commutanti FEEC e convergenza degli aggiunti;
7. trattare stabilità dei modi armonici;
8. derivare l’operatore limite e identificare la geometria.

Il Mosco-2 e il limite Laplace–Beltrami–Yang–Mills rimangono aperti finché non sono dimostrati questi punti.

## 9. Torsione, Einstein–Cartan e teleparallelismo

Distinguere sempre:
- torsione algebrica Einstein–Cartan e spin corrente;
- torsione teleparallel con connessione Weitzenböck;
- connessione Levi-Civita;
- chiusure fenomenologiche (ad esempio FLRW torsion–Lambda dust-like);
- soluzioni delle equazioni variazionali complete.

La nota scalar–torsion dimostra una variazione per l’azione specifica mostrata; non equivale a una soluzione completa tetrad/spin-connection. La chiusura torsione–Lambda è esplicitamente fenomenologica e non va promossa a derivazione Einstein–Cartan.

## 10. Spin glass, isteresi e applicazioni industriali

Il modello Q6 spin glass è indipendente dal settore gauge SU(2) finché non viene dimostrato un ponte. La sincronizzazione topologica NL/NLT, Anti-Twin lift e benchmark di isteresi sono un filone applicativo separato.

Per l’isteresi il confronto industriale deve includere baseline Preisach, Prandtl–Ishlinskii e Bouc–Wen, sweep multi-seed e multi-rate, dwell time, loop area, branch gap, rumore e costo computazionale. Simulazione e benchmark non sono validazione industriale: servono dati di materiali/attuatori e un confronto fuori campione.

## 11. QAT, luce, Maxwell e interpretazioni

Le ipotesi su luce topologica, OAM, cubo-sfera, due fogli, quaternioni e mixing angles vanno confrontate con:
- equazioni di Maxwell e condizioni al contorno;
- modi e polarizzazione;
- quantità conservate;
- propagazione e dispersione;
- benchmark numerici indipendenti.

Le fonti non standard (Legge del Ritmo, etere verticale, ecc.) sono oggetti di ricostruzione critica. Non sono assunte come fisica stabilita.

## 12. Classificazione epistemica obbligatoria

Ogni claim nel progetto deve essere marcato:

- **P — Prova matematica:** derivazione completa con ipotesi esplicite.
- **N — Verifica numerica:** calcolo riproducibile, con residui e tolleranze; non è prova generale.
- **C — Condizionale:** risultato valido sotto ipotesi dichiarate.
- **M — Modello/fenomenologia:** definizione o fit di un modello, non evidenza di verità fisica.
- **H — Ipotesi:** interpretazione o ponte non derivato.
- **O — Aperto:** passaggio mancante identificato.

La sintesi deve conservare i risultati negativi/no-go e i limiti, non solo i risultati favorevoli.

## 13. Dipendenze prioritarie per chiudere il programma

Ordine scientifico (non ordine di quantità di codice):

1. **Congelare le definizioni canoniche:** Q6, complesso cellulare, PSU, PRISM, coframe, gauge variables, Anti-Twin.
2. **Consolidare i teoremi esistenti:** T001–T068 e audit, con tabella claim→file→test→stato.
3. **Rendere il ponte RGS→Q6→coframe→link gauge esplicito:** mappe, equivarianza, dipendenze e residui.
4. **Separare i modelli fisici:** QAT/luce, teleparallel/EC, spin glass/isteresi.
5. **Chiudere prima il limite piatto e poi quello curvo:** FEEC/Mosco e resolvente.
6. **Validare le applicazioni industriali su dati indipendenti.**
7. **Solo dopo** formulare una singola azione unificata e verificarne consistenza, simmetrie, variazioni e limite continuo.

## 14. Criterio di completamento della sintesi

La monografia unitaria non deve essere un collage. Ogni capitolo dovrà contenere: definizioni canoniche, risultati già provati, audit riproducibili, dipendenze, non-conclusioni, problemi aperti e collegamento al capitolo successivo.

Il documento presente è un indice integrativo e una prima sintesi scientifica. Non sostituisce i theorem record né certifica risultati che dipendono da file, dataset o script non riesaminati in questa versione.


## Aggiornamento audit geometria originale 188D — 9 novembre 2026

La matrice originale `X_Oh_reconstructed.npy` è stata recuperata; la rappresentazione testuale `data/rgs_188d/X_Oh_reconstructed.csv` è versionata nel repository. L'audit geometry-only verifica 64×3, valori finiti, rango centrato 3, baricentro nullo, secondo momento (1.25 I_3), pairing antipodale bijettivo e involutivo. Il workflow RGS recovery run 42645820312 è terminato con successo.

Questo non chiude il confronto con il kernel 188D: le matrici originali K0/P_G e il bundle binario non sono ancora committati, e la ricostruzione dell'intertwiner non è stata ripetuta da clean checkout. La mappa geometrica candidata resta distinta dal sottospazio Im(P_G).

## Correzione topologica Q6

Per il solo grafo Q6, \\(\\beta_1=192-64+1=129\\). Nel 2-scheletro cubicale, \\(\\operatorname{rank}B_2=129\\), dunque \\(b_1=0\\) e \\(b_2=240-129=111\\). Il cubo cubicale completo, con tutte le celle fino alla dimensione 6, è contrattile. Non usare la locuzione "complesso completo di facce" per indicare il cubo completo.
